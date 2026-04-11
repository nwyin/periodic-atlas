"""Build atlas-{snapshot_year}.{parquet,duckdb} from validated element YAMLs.

The builder flattens the nested Element models into long-format fact
tables, preserving source_id on every claim-bearing row. Every fact in
the atlas is traceable via a join to the `sources` table.

Tables emitted (all carry `snapshot_year`):

- elements          one row per element (scalars, flag counts)
- production        flow quantities (mine / refined) one row per (symbol, stage)
- reserves          stock quantities (economic_reserves, resources)
- shares            unified long table: mining, refining, reserves,
                    isotope_producers — keyed by share_type
- end_uses          (symbol, application, share_pct, source_id)
- prices            (symbol, year, form, basis, region, value, unit, source_id)
- events            (symbol, date, event, impact, source_id)
- sources           (source_id, symbol, title, publisher, url, retrieved, ...)
- isotope_markets   (symbol, isotope, mode, precursor, delivery_form, ...)
- feedstocks        (symbol, substrate, concentration_pct, source_id)
- byproducts        (symbol, parent_symbol)
- substitutes       (symbol, availability, notes, source_id)
- criticality       (symbol, flag_name, value) — long form for cross-element queries

Also emits:
- atlas-{snapshot_year}.duckdb with native tables (self-contained file)
- coverage.json (per-element and aggregate coverage report)

Runnable snippet:
    cd inquiries/material-world/atlas
    uv run python scripts/build.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import duckdb
import pandas as pd
from rich.console import Console
from rich.table import Table

from atlas.models import Element, Quantity, load_all_elements

ROOT = Path(__file__).resolve().parents[1]
ELEMENTS_DIR = ROOT / "elements"
BUILD_DIR = ROOT / "build"


# =============================================================================
# flatteners — one function per table
# =============================================================================

def _quantity_fields(q: Quantity | None, prefix: str = "") -> dict[str, Any]:
    """Expand a Quantity into flat columns for a parquet row."""
    if q is None:
        return {
            f"{prefix}value": None,
            f"{prefix}unit": None,
            f"{prefix}form": None,
            f"{prefix}approximate": None,
            f"{prefix}confidence": None,
            f"{prefix}source_id": None,
            f"{prefix}notes": None,
        }
    return {
        f"{prefix}value": q.value,
        f"{prefix}unit": q.unit.value,
        f"{prefix}form": q.form,
        f"{prefix}approximate": q.approximate,
        f"{prefix}confidence": q.confidence,
        f"{prefix}source_id": q.source_id,
        f"{prefix}notes": q.notes,
    }


def flatten_elements(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        reporting_year = max((pb.reporting_year for pb in el.production), default=None)
        rows.append({
            "symbol": el.symbol,
            "atomic_number": el.atomic_number,
            "name": el.name,
            "category": el.category.value,
            "industrial_tier": el.industrial_tier.value,
            "commercial_production": el.commercial_production,
            "snapshot_year": el.snapshot_year,
            "reporting_year": reporting_year,
            "form_notes": el.form_notes,
            "narrative": el.narrative,
            "has_production": bool(el.production),
            "num_production_blocks": len(el.production),
            "has_reserves": el.reserves is not None,
            "has_research_only": el.research_only is not None,
            "has_ownership_concentration": el.ownership_concentration is not None,
            "num_isotope_markets": len(el.isotope_markets),
            "num_end_uses": len(el.end_uses.uses),
            "end_uses_completeness": el.end_uses.completeness,
            "num_feedstocks": len(el.feedstock_origins),
            "num_byproducts": len(el.byproduct_of),
            "num_substitutes": len(el.substitutes),
            "num_prices": len(el.prices),
            "num_events": len(el.geopolitical_events),
            "num_sources": len(el.sources),
            "us_critical_list_as_of_2025": el.criticality.us_critical_list_as_of_2025,
            "eu_crm_list_as_of_2024": el.criticality.eu_crm_list_as_of_2024,
            "eu_strategic_list_as_of_2024": el.criticality.eu_strategic_list_as_of_2024,
            "doe_short_term_criticality_rank": el.criticality.doe_short_term_criticality_rank,
            "criticality_source_id": el.criticality.source_id,
        })
    return pd.DataFrame(rows)


def flatten_production(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for pi, p in enumerate(el.production):
            for stage, q in (("mine", p.mine), ("refined", p.refined)):
                if q is None:
                    continue
                row = {
                    "symbol": el.symbol,
                    "snapshot_year": el.snapshot_year,
                    "reporting_year": p.reporting_year,
                    "stream": p.stream,
                    "block_index": pi,
                    "stage": stage,
                    "grouped_reporting": p.grouped_reporting,
                    "commodity_group": p.commodity_group,
                }
                row.update(_quantity_fields(q))
                rows.append(row)
    return pd.DataFrame(rows)


def flatten_reserves(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        if el.reserves is None:
            continue
        for kind, q in (("economic_reserves", el.reserves.economic_reserves), ("resources", el.reserves.resources)):
            if q is None:
                continue
            row = {
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "kind": kind,
            }
            row.update(_quantity_fields(q))
            rows.append(row)
    return pd.DataFrame(rows)


def flatten_shares(elements: list[Element]) -> pd.DataFrame:
    """Unified long table for mining/refining/reserves/isotope_producers shares."""
    rows = []
    for el in elements:
        def emit_share_list(
            share_type: str,
            sl: Any,
            isotope: str | None = None,
            stream: str | None = None,
        ) -> None:
            for s in sl.shares:
                q = s.quantity
                rows.append({
                    "symbol": el.symbol,
                    "snapshot_year": el.snapshot_year,
                    "share_type": share_type,
                    "stream": stream,
                    "isotope": isotope,
                    "country": s.country,
                    "share_pct": s.share_pct,
                    "confidence": s.confidence,
                    "quantity_value": q.value if q else None,
                    "quantity_unit": q.unit.value if q else None,
                    "quantity_form": q.form if q else None,
                    "quantity_source_id": q.source_id if q else None,
                    "completeness": sl.completeness,
                    "source_id": s.source_id,
                    "notes": s.notes,
                })

        for pb in el.production:
            emit_share_list("mining", pb.mining_by_country, stream=pb.stream)
            emit_share_list("refining", pb.refining_by_country, stream=pb.stream)
        if el.reserves:
            emit_share_list("reserves", el.reserves.reserves_by_country)
        for im in el.isotope_markets:
            emit_share_list("isotope_producers", im.producers, isotope=im.isotope)

    return pd.DataFrame(rows)


def flatten_end_uses(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for u in el.end_uses.uses:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "application": u.application,
                "share_pct": u.share_pct,
                "completeness": el.end_uses.completeness,
                "source_id": u.source_id,
                "notes": u.notes,
            })
    return pd.DataFrame(rows)


def flatten_prices(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for p in el.prices:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "year": p.year,
                "value": p.value,
                "unit": p.unit.value,
                "form": p.form,
                "basis": p.basis,
                "region": p.region,
                "source_id": p.source_id,
                "notes": p.notes,
            })
    return pd.DataFrame(rows)


def flatten_events(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for ev in el.geopolitical_events:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "date": ev.date,
                "event": ev.event,
                "impact": ev.impact,
                "source_id": ev.source_id,
            })
    return pd.DataFrame(rows)


def flatten_sources(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for s in el.sources:
            rows.append({
                "source_id": s.id,
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "title": s.title,
                "publisher": s.publisher,
                "url": s.url,
                "retrieved": s.retrieved,
                "publication_year": s.publication_year,
                "superseded_by": s.superseded_by,
            })
    return pd.DataFrame(rows)


def flatten_isotope_markets(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for im in el.isotope_markets:
            row = {
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "isotope": im.isotope,
                "half_life_seconds": im.half_life_seconds,
                "production_mode": im.production_mode,
                "reporting_year": im.reporting_year,
                "precursor": im.precursor,
                "delivery_form": im.delivery_form,
                "producers_completeness": im.producers.completeness,
                "num_producers": len(im.producers.shares),
                "notes": im.notes,
            }
            row.update(_quantity_fields(im.production_quantity, prefix="production_"))
            rows.append(row)
    return pd.DataFrame(rows)


def flatten_feedstocks(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for f in el.feedstock_origins:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "substrate": f.substrate,
                "typical_concentration_pct": f.typical_concentration_pct,
                "source_id": f.source_id,
                "notes": f.notes,
            })
    return pd.DataFrame(rows)


def flatten_byproducts(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for parent in el.byproduct_of:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "parent_symbol": parent,
            })
    return pd.DataFrame(rows)


def flatten_substitutes(elements: list[Element]) -> pd.DataFrame:
    rows = []
    for el in elements:
        for sub in el.substitutes:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "availability": sub.availability,
                "notes": sub.notes,
                "source_id": sub.source_id,
            })
    return pd.DataFrame(rows)


def flatten_criticality(elements: list[Element]) -> pd.DataFrame:
    """Long-form criticality table for cross-element queries.

    Each flag becomes one row so queries like 'show me every element on
    the US 2025 list' are a single SELECT without column introspection.
    """
    rows = []
    for el in elements:
        c = el.criticality
        flag_pairs = [
            ("us_critical_list_as_of_2025", c.us_critical_list_as_of_2025),
            ("eu_crm_list_as_of_2024", c.eu_crm_list_as_of_2024),
            ("eu_strategic_list_as_of_2024", c.eu_strategic_list_as_of_2024),
        ]
        for flag_name, value in flag_pairs:
            rows.append({
                "symbol": el.symbol,
                "snapshot_year": el.snapshot_year,
                "flag_name": flag_name,
                "value": bool(value),
                "source_id": c.source_id,
            })
    return pd.DataFrame(rows)


# =============================================================================
# coverage report
# =============================================================================

def coverage_report(elements: list[Element]) -> dict[str, Any]:
    total = len(elements)
    if total == 0:
        return {"total": 0}

    def count(pred) -> int:
        return sum(1 for e in elements if pred(e))

    return {
        "total_elements": total,
        "commercial_production": count(lambda e: e.commercial_production),
        "research_only": count(lambda e: e.research_only is not None),
        "has_production": count(lambda e: bool(e.production)),
        "has_reserves": count(lambda e: e.reserves is not None),
        "has_isotope_markets": count(lambda e: bool(e.isotope_markets)),
        "has_mining_shares": count(lambda e: any(pb.mining_by_country.shares for pb in e.production)),
        "has_refining_shares": count(lambda e: any(pb.refining_by_country.shares for pb in e.production)),
        "has_end_uses": count(lambda e: bool(e.end_uses.uses)),
        "has_prices": count(lambda e: bool(e.prices)),
        "has_events": count(lambda e: bool(e.geopolitical_events)),
        "has_feedstocks": count(lambda e: bool(e.feedstock_origins)),
        "has_byproducts": count(lambda e: bool(e.byproduct_of)),
        "has_substitutes": count(lambda e: bool(e.substitutes)),
        "us_critical_list_as_of_2025": count(lambda e: e.criticality.us_critical_list_as_of_2025),
        "eu_crm_list_as_of_2024": count(lambda e: e.criticality.eu_crm_list_as_of_2024),
        "by_tier": {
            str(tier): count(lambda e, t=tier: e.industrial_tier.value == t)
            for tier in (0, 1, 2, 3, 4)
        },
    }


# =============================================================================
# orchestration
# =============================================================================

TABLE_BUILDERS: dict[str, Any] = {
    "elements": flatten_elements,
    "production": flatten_production,
    "reserves": flatten_reserves,
    "shares": flatten_shares,
    "end_uses": flatten_end_uses,
    "prices": flatten_prices,
    "events": flatten_events,
    "sources": flatten_sources,
    "isotope_markets": flatten_isotope_markets,
    "feedstocks": flatten_feedstocks,
    "byproducts": flatten_byproducts,
    "substitutes": flatten_substitutes,
    "criticality": flatten_criticality,
}


def build_all(elements: list[Element]) -> dict[str, pd.DataFrame]:
    return {name: builder(elements) for name, builder in TABLE_BUILDERS.items()}


def write_parquet(tables: dict[str, pd.DataFrame], out_dir: Path) -> list[Path]:
    out_dir.mkdir(exist_ok=True)
    written = []
    for name, df in tables.items():
        path = out_dir / f"atlas_{name}.parquet"
        df.to_parquet(path, index=False)
        written.append(path)
    return written


def write_duckdb(tables: dict[str, pd.DataFrame], out_path: Path) -> None:
    """Write a self-contained DuckDB file with native tables."""
    if out_path.exists():
        out_path.unlink()
    con = duckdb.connect(str(out_path))
    try:
        for name, df in tables.items():
            con.register(f"_{name}_df", df)
            con.execute(f"CREATE TABLE atlas_{name} AS SELECT * FROM _{name}_df")
            con.unregister(f"_{name}_df")
    finally:
        con.close()


def main() -> None:
    console = Console()
    elements = load_all_elements(ELEMENTS_DIR)

    if not elements:
        console.print("[red]No element files found in elements/.[/red]")
        return

    snapshot_year = elements[0].snapshot_year
    if any(e.snapshot_year != snapshot_year for e in elements):
        console.print("[yellow]Warning: elements have inconsistent snapshot_year values[/yellow]")

    BUILD_DIR.mkdir(exist_ok=True)
    tables = build_all(elements)

    paths = write_parquet(tables, BUILD_DIR)
    for p in paths:
        console.print(f"[green]wrote[/green] {p.relative_to(ROOT)}  ({len(tables[p.stem.removeprefix('atlas_')])} rows)")

    duckdb_path = BUILD_DIR / f"atlas-{snapshot_year}.duckdb"
    write_duckdb(tables, duckdb_path)
    console.print(f"[green]wrote[/green] {duckdb_path.relative_to(ROOT)}")

    cov = coverage_report(elements)
    (BUILD_DIR / "coverage.json").write_text(json.dumps(cov, indent=2))
    console.print(f"[green]wrote[/green] build/coverage.json")

    console.print()
    table = Table(title=f"Atlas {snapshot_year} coverage")
    table.add_column("Metric")
    table.add_column("Count", justify="right")
    table.add_column("Share", justify="right")
    total = cov["total_elements"]
    for k, v in cov.items():
        if isinstance(v, dict):
            continue
        share = f"{v / total * 100:.0f}%" if total else "-"
        table.add_row(k, str(v), share)
    console.print(table)

    console.print()
    console.print("[bold]Query with:[/bold]")
    console.print(f"  duckdb {duckdb_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

"""Build atlas-2025.parquet and a coverage report from all element YAMLs.

Flattens the nested element model into three long tables:
    - elements:        one row per element (scalars only)
    - mining_shares:   (element, country, share_pct, tonnes)
    - refining_shares: (element, country, share_pct, tonnes)
    - end_uses:        (element, application, share_pct)

Plus a JSON coverage report showing which fields are populated per element.

Runnable snippet:
    cd inquiries/material-world/atlas
    uv run python scripts/build.py
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from rich.console import Console
from rich.table import Table

from atlas.models import Element, load_all_elements

ROOT = Path(__file__).resolve().parents[1]
ELEMENTS_DIR = ROOT / "elements"
BUILD_DIR = ROOT / "build"


def flatten_elements(elements: list[Element]) -> dict[str, pd.DataFrame]:
    element_rows = []
    mining_rows = []
    refining_rows = []
    end_use_rows = []

    for el in elements:
        prod = el.production
        mine_q = prod.mine if prod else None
        refined_q = prod.refined if prod else None

        element_rows.append(
            {
                "symbol": el.symbol,
                "atomic_number": el.atomic_number,
                "name": el.name,
                "category": el.category.value,
                "industrial_tier": el.industrial_tier.value,
                "commercial_production": el.commercial_production,
                "mine_value": mine_q.value if mine_q else None,
                "mine_unit": mine_q.unit.value if mine_q else None,
                "refined_value": refined_q.value if refined_q else None,
                "refined_unit": refined_q.unit.value if refined_q else None,
                "production_year": prod.year if prod else None,
                "us_critical_2025": el.criticality.us_critical_2025,
                "eu_crm_2024": el.criticality.eu_crm_2024,
                "eu_strategic_2024": el.criticality.eu_strategic_2024,
                "byproduct_of": ",".join(el.byproduct_of) if el.byproduct_of else None,
                "substitutes_available": el.substitutes_available,
                "num_end_uses": len(el.end_uses),
                "num_geopolitical_events": len(el.geopolitical_events),
                "num_sources": len(el.sources),
            }
        )

        if prod:
            for s in prod.mining_by_country:
                mining_rows.append({"symbol": el.symbol, "country": s.country, "share_pct": s.share_pct, "tonnes": s.tonnes})
            for s in prod.refining_by_country:
                refining_rows.append({"symbol": el.symbol, "country": s.country, "share_pct": s.share_pct, "tonnes": s.tonnes})

        for eu in el.end_uses:
            end_use_rows.append({"symbol": el.symbol, "application": eu.application, "share_pct": eu.share_pct})

    return {
        "elements": pd.DataFrame(element_rows),
        "mining_shares": pd.DataFrame(mining_rows),
        "refining_shares": pd.DataFrame(refining_rows),
        "end_uses": pd.DataFrame(end_use_rows),
    }


def coverage_report(elements: list[Element]) -> dict:
    total = len(elements)
    if total == 0:
        return {"total": 0}
    return {
        "total": total,
        "commercial_production": sum(1 for e in elements if e.commercial_production),
        "has_production_block": sum(1 for e in elements if e.production is not None),
        "has_reserves": sum(1 for e in elements if e.reserves is not None),
        "has_mining_shares": sum(1 for e in elements if e.production and e.production.mining_by_country),
        "has_refining_shares": sum(1 for e in elements if e.production and e.production.refining_by_country),
        "has_end_uses": sum(1 for e in elements if e.end_uses),
        "has_prices": sum(1 for e in elements if e.prices),
        "has_geopolitical_events": sum(1 for e in elements if e.geopolitical_events),
        "research_only": sum(1 for e in elements if e.research_only is not None),
        "by_tier": {
            tier: sum(1 for e in elements if e.industrial_tier.value == tier)
            for tier in (0, 1, 2, 3, 4)
        },
    }


def main() -> None:
    console = Console()
    elements = load_all_elements(ELEMENTS_DIR)

    tables = flatten_elements(elements)
    BUILD_DIR.mkdir(exist_ok=True)

    for name, df in tables.items():
        out = BUILD_DIR / f"atlas_{name}.parquet"
        df.to_parquet(out, index=False)
        console.print(f"[green]wrote[/green] {out.relative_to(ROOT)}  ({len(df)} rows)")

    cov = coverage_report(elements)
    (BUILD_DIR / "coverage.json").write_text(json.dumps(cov, indent=2))
    console.print(f"[green]wrote[/green] build/coverage.json")

    console.print()
    table = Table(title="Coverage report")
    table.add_column("Metric")
    table.add_column("Count", justify="right")
    table.add_column("Share", justify="right")
    for k, v in cov.items():
        if isinstance(v, dict):
            continue
        share = f"{v / cov['total'] * 100:.0f}%" if cov["total"] else "-"
        table.add_row(k, str(v), share)
    console.print(table)


if __name__ == "__main__":
    main()

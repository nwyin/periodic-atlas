"""Build static HTML viewer from build/atlas-{snapshot_year}.duckdb.

Generates:
  viewer/index.html          — stats row + element grid
  viewer/{symbol}.html       — per-element stub with chart placeholders
  viewer/assets/atlas.css    — minimal typography + grid

Runnable:
    uv run python scripts/build_viewer.py

For deterministic output in tests, pass `--timestamp "2025-01-01T00:00:00"` or
use the `generate_viewer()` function directly with `timestamp=` keyword arg.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
VIEWER_DIR = ROOT / "viewer"
CHARTS_PRICES_JS = ROOT / "viewer" / "assets" / "charts_prices.js"
CHARTS_PRODUCTION_JS = ROOT / "viewer" / "assets" / "charts_production.js"
CHARTS_ISOTOPES_JS = ROOT / "viewer" / "assets" / "charts_isotopes.js"
CHARTS_MAP_JS = ROOT / "viewer" / "assets" / "charts_map.js"
CHARTS_COUNTRY_JS = ROOT / "viewer" / "assets" / "charts_country.js"
CHARTS_BYPRODUCT_GRAPH_JS = ROOT / "viewer" / "assets" / "charts_byproduct_graph.js"
WORLD_COUNTRIES_GEOJSON = ROOT / "viewer" / "assets" / "world_countries_50m.geojson"
TABLE_SORT_JS = ROOT / "viewer" / "assets" / "table_sort.js"
TABLE_FILTER_JS = ROOT / "viewer" / "assets" / "table_filter.js"

# ─────────────────────────────────────────────────────────────────────────────
# Feature flags — flip to True when destination pages ship
# ─────────────────────────────────────────────────────────────────────────────

# Set True when country pages (viewer/countries/{ISO}.html) are deployed.
COUNTRY_PAGES_ENABLED: bool = True
# Set True when byproduct graph (viewer/byproducts.html) is deployed.
BYPRODUCT_GRAPH_ENABLED: bool = True

# ── Site navigation ────────────────────────────────────────────────────────────
# CC-6: shared nav links embedded in every page shell.
_NAV_LINKS: list[tuple[str, str]] = [
    ("Elements", "index.html"),
    ("Byproduct graph", "byproducts.html"),
]

# ── Country name overrides ─────────────────────────────────────────────────────
# Parallel to WIKIPEDIA_NAME_OVERRIDES.  Allows brevity tweaks without touching
# the GeoJSON.  Unresolved open question from spec §8 Q3: for now no overrides.
COUNTRY_NAME_OVERRIDES: dict[str, str] = {}

# 1 lb = 0.4536 kg; usd_per_lb → usd_per_kg by dividing by this factor.
# Preferred normalisation unit for price charts: usd_per_kg.
# See also: viewer/assets/charts_prices.js — same rationale documented there.
_LB_TO_KG = 0.4536

CHART_PLACEHOLDERS = [
    ("production-chart", "Production charts — see B1"),
    ("reserves-chart", "Reserves + end uses — see B2"),
    ("prices-chart", "Geopolitical events — see B3"),
    ("sources-panel", "Sources — see B4"),
    ("isotope-panel", "Isotope markets — see B5"),
]

# External price-chart provider. We link out rather than mirror the data.
PRICE_URL_TEMPLATE = "https://tradingeconomics.com/commodity/{slug}"
ELEMENT_PRICE_SLUGS: dict[str, str] = {
    "Au": "gold",
    "Ag": "silver",
    "Cu": "copper",
    "Al": "aluminum",
    "Ni": "nickel",
    "Zn": "zinc",
    "Sn": "tin",
    "Pb": "lead",
    "Pt": "platinum",
    "Pd": "palladium",
    "Rh": "rhodium",
    "Ru": "ruthenium",
    "Ir": "iridium",
    "Os": "osmium",
    "Li": "lithium",
    "Co": "cobalt",
    "V": "vanadium",
    "U": "uranium",
    "Mo": "molybdenum",
    "W": "tungsten",
    "Re": "rhenium",
    "Nb": "niobium",
    "Ta": "tantalum",
    "Zr": "zirconium",
    "Hf": "hafnium",
    "Be": "beryllium",
    "Ti": "titanium",
    "Fe": "iron-ore",
    "Mn": "manganese",
    "Cr": "chromium",
    "Mg": "magnesium",
    "Nd": "neodymium",
    "Dy": "dysprosium",
    "Sb": "antimony",
    "Bi": "bismuth",
    "Ga": "gallium",
    "In": "indium",
    "Ge": "germanium",
    "Te": "tellurium",
    "Se": "selenium",
    "Cd": "cadmium",
}

# Wikipedia URL is derived from the element name; overrides catch disambiguation pages.
WIKIPEDIA_NAME_OVERRIDES: dict[str, str] = {
    "Mercury": "Mercury_(element)",
}

# ─────────────────────────────────────────────────────────────────────────────
# End-use canonicalization (CC-2)
# ─────────────────────────────────────────────────────────────────────────────

#: Maps raw atlas_end_uses.application slugs → one of 14 canonical buckets.
#: Unmapped slugs fall through to the "other" bucket.  Add entries here as new
#: element YAMLs introduce novel slugs; a build-time warning fires automatically
#: when any element's unmapped share exceeds 20 %.
END_USE_BUCKET_MAP: dict[str, str] = {
    # batteries
    "batteries": "batteries",
    "battery_alloys_nimh": "batteries",
    "li_ion_batteries": "batteries",
    "lithium_ion_batteries": "batteries",
    "battery_cathodes": "batteries",
    "energy_storage": "batteries",
    # magnets
    "ndfeb_permanent_magnets": "magnets",
    "permanent_magnets": "magnets",
    "ceramic_ferrite_magnets": "magnets",
    "magnets": "magnets",
    # superalloys
    "superalloys_aircraft_turbines": "superalloys",
    "superalloys": "superalloys",
    "superalloys_and_high_performance_alloys": "superalloys",
    "aerospace_and_defense": "superalloys",
    "aerospace_pressuring_purging": "superalloys",
    # semiconductors
    "semiconductors": "semiconductors",
    "semiconductor_and_electronics": "semiconductors",
    "electronics": "semiconductors",
    "photovoltaics": "semiconductors",
    "cdte_solar_and_semiconductors": "semiconductors",
    "solar_panels": "semiconductors",
    "fiber_optics": "semiconductors",
    "optical_fiber": "semiconductors",
    # catalysts
    "catalysts": "catalysts",
    "autocatalysts": "catalysts",
    "autocatalysts_gasoline_twc": "catalysts",
    "chemical_catalysts": "catalysts",
    "catalysts_fcc_and_auto": "catalysts",
    "catalysts_and_polishing": "catalysts",
    "chemical_and_industrial_catalysts": "catalysts",
    "catalysts_and_other": "catalysts",
    "petroleum_refining_catalysts": "catalysts",
    # fertilizers
    "ammonia_and_fertilizers": "fertilizers",
    "agriculture_and_fertilizers": "fertilizers",
    "fertilizers": "fertilizers",
    "agricultural": "fertilizers",
    "animal_feed": "fertilizers",
    # steel_and_alloys
    "alloy_steels": "steel_and_alloys",
    "alloy_steels_and_cast_irons": "steel_and_alloys",
    "stainless_steel": "steel_and_alloys",
    "steel": "steel_and_alloys",
    "alloys": "steel_and_alloys",
    "alloys_other": "steel_and_alloys",
    "aluminum_alloys": "steel_and_alloys",
    "aluminum_scandium_alloys": "steel_and_alloys",
    "aluminum_smelting_flux": "steel_and_alloys",
    "brass_and_bronze": "steel_and_alloys",
    "babbitt_brass_bronze_tinning": "steel_and_alloys",
    "brazing_and_soldering": "steel_and_alloys",
    "bar_tin": "steel_and_alloys",
    "battery_alloys": "steel_and_alloys",
    # cutting_tools (carbides)
    "cemented_carbides": "cutting_tools",
    "cemented_carbides_cutting_tools": "cutting_tools",
    "cutting_tools": "cutting_tools",
    # glass_and_ceramics
    "glass": "glass_and_ceramics",
    "ceramics_and_glass": "glass_and_ceramics",
    "ceramics_glass_optical": "glass_and_ceramics",
    "ceramics_and_glazes": "glass_and_ceramics",
    "ceramics_and_opacifiers": "glass_and_ceramics",
    "ceramics_glass_other": "glass_and_ceramics",
    "ceramics_ysz_refractories": "glass_and_ceramics",
    "ceramic_and_refractory": "glass_and_ceramics",
    "building_construction": "glass_and_ceramics",
    # pigments_and_coatings
    "pigments_and_coatings": "pigments_and_coatings",
    "coatings_and_plating": "pigments_and_coatings",
    "plating": "pigments_and_coatings",
    # nuclear
    "nuclear_fuel": "nuclear",
    "nuclear_reactors": "nuclear",
    "nuclear_and_isotope_applications": "nuclear",
    "nuclear_shielding": "nuclear",
    # medical
    "medical_devices": "medical",
    "medical_imaging": "medical",
    "radiation_therapy": "medical",
    "medical_isotopes": "medical",
    "actinide_research_and_target_materials": "medical",
    "beta_emitter_power_and_gauge_sources": "medical",
    # lighting
    "fluorescent_lamps": "lighting",
    "lighting_and_displays": "lighting",
    "leds": "lighting",
    "lamps": "lighting",
}

#: Canonical bucket slugs — JS must mirror this list in END_USE_BUCKETS constant.
END_USE_BUCKETS: list[str] = [
    "batteries",
    "magnets",
    "superalloys",
    "semiconductors",
    "catalysts",
    "fertilizers",
    "steel_and_alloys",
    "cutting_tools",
    "glass_and_ceramics",
    "pigments_and_coatings",
    "nuclear",
    "medical",
    "lighting",
    "other",
]


# ─────────────────────────────────────────────────────────────────────────────
# Unit normalisation
# ─────────────────────────────────────────────────────────────────────────────


def _normalize_price_units(prices: list[dict]) -> list[dict]:
    """Convert usd_per_lb → usd_per_kg so all price series share a common y-axis.

    price_per_kg = price_per_lb / _LB_TO_KG  (i.e. × 2.2046…)
    The same normalisation is documented in viewer/assets/charts_prices.js.
    Other unit pairs (usd_per_m3, usd_per_tonne, …) are left unchanged.
    """
    result = []
    for p in prices:
        if p.get("unit") == "usd_per_lb":
            p = {**p, "value": round(p["value"] / _LB_TO_KG, 4), "unit": "usd_per_kg"}
        result.append(p)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Half-life formatting
# ─────────────────────────────────────────────────────────────────────────────

_YEAR_S = 365.25 * 86400  # seconds per Julian year
_DAY_S = 86400
_HOUR_S = 3600
_MINUTE_S = 60


def _format_half_life(seconds: float) -> str:
    """Convert a half-life in seconds to a human-readable string.

    Examples:
        1.365e10  → "432.4 years"
        21624     → "6.0 hours"
        7200      → "2.0 hours"
        90        → "1.5 minutes"
        45        → "45.0 seconds"
    """
    if seconds >= _YEAR_S:
        years = seconds / _YEAR_S
        if years >= 1_000:
            return f"{years:,.0f} years"
        if years >= 10:
            return f"{years:.1f} years"
        return f"{years:.2f} years"
    if seconds >= _DAY_S:
        days = seconds / _DAY_S
        return f"{days:.1f} days"
    if seconds >= _HOUR_S:
        hours = seconds / _HOUR_S
        return f"{hours:.1f} hours"
    if seconds >= _MINUTE_S:
        minutes = seconds / _MINUTE_S
        return f"{minutes:.1f} minutes"
    return f"{seconds:.1f} seconds"


# ─────────────────────────────────────────────────────────────────────────────
# Isotope markets data builder
# ─────────────────────────────────────────────────────────────────────────────


def _build_isotope_data(con: "duckdb.DuckDBPyConnection", symbol: str) -> list[dict]:  # type: ignore[name-defined]
    """Return isotope market records for *symbol*, each with embedded producer shares.

    Each record shape:
        isotope, half_life_seconds, half_life_display, production_mode,
        precursor, delivery_form, reporting_year,
        production_quantity: {value, unit},
        producers: [{country, share_pct, confidence, notes}, ...],
        producers_completeness, notes
    """
    markets_df = con.execute(
        """
        SELECT isotope, half_life_seconds, production_mode, reporting_year,
               precursor, delivery_form, producers_completeness, notes,
               production_value, production_unit
        FROM atlas_isotope_markets
        WHERE symbol = ?
        ORDER BY isotope
        """,
        [symbol],
    ).df()

    if markets_df.empty:
        return []

    # Producer shares per isotope
    shares_df = con.execute(
        """
        SELECT isotope, country, share_pct, confidence, notes
        FROM atlas_shares
        WHERE symbol = ? AND share_type = 'isotope_producers'
        ORDER BY isotope, share_pct DESC
        """,
        [symbol],
    ).df()

    shares_by_isotope: dict[str, list[dict]] = {}
    for row in shares_df.to_dict(orient="records"):
        iso = str(row["isotope"])
        shares_by_isotope.setdefault(iso, []).append(
            {
                "country": str(row["country"]) if row["country"] else "",
                "share_pct": float(row["share_pct"]) if row["share_pct"] is not None else None,
                "confidence": str(row["confidence"]) if row["confidence"] else "unknown",
                "notes": str(row["notes"]) if row["notes"] and str(row["notes"]) not in ("nan", "None") else None,
            }
        )

    def _safe_float(v) -> float | None:
        if v is None:
            return None
        try:
            f = float(v)
            return None if (f != f) else f
        except (TypeError, ValueError):
            return None

    result: list[dict] = []
    for row in markets_df.to_dict(orient="records"):
        iso = str(row["isotope"])
        hl_sec = _safe_float(row.get("half_life_seconds"))
        hl_display = _format_half_life(hl_sec) if hl_sec is not None else "unknown"

        precursor = row.get("precursor")
        if precursor and str(precursor) not in ("nan", "None"):
            precursor = str(precursor).strip()
        else:
            precursor = None

        delivery_form = row.get("delivery_form")
        if delivery_form and str(delivery_form) not in ("nan", "None"):
            delivery_form = str(delivery_form).strip()
        else:
            delivery_form = None

        notes = row.get("notes")
        if notes and str(notes) not in ("nan", "None"):
            notes = str(notes).strip()
        else:
            notes = None

        completeness = row.get("producers_completeness")
        if completeness and str(completeness) not in ("nan", "None"):
            completeness = str(completeness)
        else:
            completeness = "unknown"

        result.append(
            {
                "isotope": iso,
                "half_life_seconds": hl_sec,
                "half_life_display": hl_display,
                "production_mode": str(row.get("production_mode") or ""),
                "precursor": precursor,
                "delivery_form": delivery_form,
                "reporting_year": int(row["reporting_year"]) if row.get("reporting_year") is not None else None,
                "production_quantity": {
                    "value": _safe_float(row.get("production_value")),
                    "unit": str(row["production_unit"])
                    if row.get("production_unit") and str(row.get("production_unit")) not in ("nan", "None")
                    else None,
                },
                "producers": shares_by_isotope.get(iso, []),
                "producers_completeness": completeness,
                "notes": notes,
            }
        )
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Byproduct graph data builder
# ─────────────────────────────────────────────────────────────────────────────


def _normalize_mine_value(value: float | None, unit: str | None, stream: str | None) -> float | None:
    """Normalize a production value to tonnes/yr.

    Units handled:
      - tonnes_per_year          → identity
      - million_tonnes_per_year  → × 1e6
      - kg_per_year              → ÷ 1000
      - million_m3_per_year      → None (non-mass; not useful for node sizing)
      - contained_in_zircon_feed (Hf upstream stream) → None (not refined metal)

    Returns None when the unit is not mass-equivalent or value is absent.
    """
    if value is None or unit is None:
        return None
    # Reject the Hf upstream zircon-feed stream (not refined metal output)
    if stream and "zircon_feed" in stream:
        return None
    if unit == "tonnes_per_year":
        return float(value)
    if unit == "million_tonnes_per_year":
        return float(value) * 1_000_000
    if unit == "kg_per_year":
        return float(value) / 1000.0
    # Other units (m3, etc.) are not mass-equivalent → None
    return None


def _byproduct_graph_json(con: "duckdb.DuckDBPyConnection") -> str:  # type: ignore[name-defined]
    """Build the byproduct DAG JSON payload.

    Pulls edges from atlas_byproducts, node metadata from atlas_elements and
    atlas_production.  Normalises mine output to tonnes/yr.  Runs Kahn's
    algorithm topological sort; raises ValueError on cycle.

    Returns a JSON string suitable for embedding as:
      <script id="byproduct-graph-data" type="application/json">…</script>
    """
    # ── 1. Edges ──────────────────────────────────────────────────────────────
    edge_rows = con.execute("SELECT parent_symbol, symbol FROM atlas_byproducts ORDER BY symbol, parent_symbol").fetchall()
    edges = [{"source": str(parent), "target": str(child)} for parent, child in edge_rows]

    # ── 2. Node set: union of all symbols and parent_symbols ─────────────────
    all_symbols: set[str] = set()
    for parent, child in edge_rows:
        all_symbols.add(str(parent))
        all_symbols.add(str(child))

    byproduct_of: dict[str, list[str]] = {}
    for parent, child in edge_rows:
        byproduct_of.setdefault(str(child), []).append(str(parent))

    # ── 3. Element metadata ───────────────────────────────────────────────────
    el_rows = con.execute(
        """
        SELECT symbol, name, industrial_tier,
               us_critical_list_as_of_2025,
               eu_crm_list_as_of_2024,
               eu_strategic_list_as_of_2024
        FROM atlas_elements
        WHERE symbol = ANY(?)
        """,
        [list(all_symbols)],
    ).fetchall()
    meta: dict[str, dict] = {}
    for sym, name, tier, us_crit, eu_crm, eu_strat in el_rows:
        meta[str(sym)] = {
            "name": str(name),
            "tier": int(tier) if tier is not None else 0,
            "us_critical": bool(us_crit),
            "eu_crm": bool(eu_crm),
            "eu_strategic": bool(eu_strat),
        }

    # ── 4. Production data — pick best mine value per symbol ─────────────────
    prod_rows = con.execute(
        """
        SELECT symbol, value, unit, stream
        FROM atlas_production
        WHERE stage = 'mine'
          AND symbol = ANY(?)
        ORDER BY symbol
        """,
        [list(all_symbols)],
    ).fetchall()

    # Collect all candidate values per symbol; pick the best one:
    # prefer non-None normalised values; among those pick the highest
    # (handles multi-stream elements like Ti, Al)
    prod_candidates: dict[str, list[float]] = {}
    for sym, value, unit, stream in prod_rows:
        sym = str(sym)
        normed = _normalize_mine_value(
            float(value) if value is not None else None,
            str(unit) if unit else None,
            str(stream) if stream else None,
        )
        if normed is not None:
            prod_candidates.setdefault(sym, []).append(normed)

    mine_value: dict[str, float | None] = {sym: None for sym in all_symbols}
    for sym, vals in prod_candidates.items():
        mine_value[sym] = max(vals)

    # ── 5. Assemble nodes ─────────────────────────────────────────────────────
    nodes = []
    for sym in sorted(all_symbols):
        m = meta.get(sym, {})
        nodes.append(
            {
                "symbol": sym,
                "name": m.get("name", sym),
                "tier": m.get("tier", 0),
                "us_critical": m.get("us_critical", False),
                "eu_crm": m.get("eu_crm", False),
                "eu_strategic": m.get("eu_strategic", False),
                "mine_value": mine_value.get(sym),
                "mine_unit": "tonnes_per_year",
                "byproduct_of": sorted(byproduct_of.get(sym, [])),
            }
        )

    # ── 6. DAG validation — Kahn's algorithm ─────────────────────────────────
    in_degree: dict[str, int] = {sym: 0 for sym in all_symbols}
    children: dict[str, list[str]] = {sym: [] for sym in all_symbols}
    for e in edges:
        children[e["source"]].append(e["target"])
        in_degree[e["target"]] += 1

    queue = [sym for sym in all_symbols if in_degree[sym] == 0]
    visited: list[str] = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for child in children[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    if len(visited) != len(all_symbols):
        cycle_nodes = [sym for sym in all_symbols if sym not in set(visited)]
        raise ValueError(f"Cycle detected in byproduct graph involving nodes: {sorted(cycle_nodes)}")

    payload = {
        "nodes": nodes,
        "edges": edges,
        "dag_validated": True,
        "snapshot_year": 2025,
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


# ─────────────────────────────────────────────────────────────────────────────
# HTML helpers
# ─────────────────────────────────────────────────────────────────────────────


def _html_escape(text: str | None) -> str:
    if text is None:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")


def _badge(text: str, css_class: str) -> str:
    return f'<span class="badge badge-{css_class}">{_html_escape(text)}</span>'


def _criticality_badges(row: dict) -> str:
    parts = []
    if row.get("us_critical_list_as_of_2025"):
        parts.append(_badge("US Critical", "us-critical"))
    if row.get("eu_crm_list_as_of_2024"):
        parts.append(_badge("EU CRM", "eu-crm"))
    if row.get("eu_strategic_list_as_of_2024"):
        parts.append(_badge("EU Strategic", "eu-strategic"))
    doe_rank = row.get("doe_short_term_criticality_rank")
    if doe_rank is not None and str(doe_rank) not in ("nan", "None", ""):
        try:
            rank_int = int(float(doe_rank))
            parts.append(_badge(f"DOE #{rank_int}", "doe"))
        except (ValueError, TypeError):
            pass
    return "".join(parts)


def _commercial_badge(commercial: bool) -> str:
    if commercial:
        return _badge("Commercial", "commercial")
    return _badge("No commercial production", "no-commercial")


# ─────────────────────────────────────────────────────────────────────────────
# HHI computation (CC-1 / CC-2)
# ─────────────────────────────────────────────────────────────────────────────


def _compute_hhi(shares: list[dict]) -> tuple[int | None, str | None, float | None]:
    """Return (hhi, top_country, top_share_pct) from a list of share dicts.

    Excludes the ZZ rest-of-world bucket from both HHI and top-country selection.
    Returns (None, None, None) if no named-country shares exist or the list is empty.

    Args:
        shares: List of dicts with at minimum {"country": str, "share_pct": float|None}.
    """
    named = [s for s in shares if s.get("country") not in (None, "", "ZZ", "XX")]
    if not named:
        return None, None, None
    hhi = round(sum((float(s["share_pct"]) ** 2) for s in named if s.get("share_pct") is not None))
    top = max(named, key=lambda s: float(s["share_pct"]) if s.get("share_pct") is not None else -1.0)
    top_country = str(top["country"])
    top_share = float(top["share_pct"]) if top.get("share_pct") is not None else None
    return hhi, top_country, top_share


# ─────────────────────────────────────────────────────────────────────────────
# Element metadata index builder (CC-1)
# ─────────────────────────────────────────────────────────────────────────────


def _build_element_index(
    elements_list: list[dict],
    mining_shares_by_symbol: dict[str, list[dict]],
    refining_shares_by_symbol: dict[str, list[dict]],
    end_uses_by_symbol: dict[str, list[dict]],
    byproduct_by_symbol: dict[str, list[str]],
    reserves_shares_by_symbol: dict[str, list[dict]] | None = None,
) -> str:
    """Return compact JSON string for the atlas-element-index <script> block.

    Schema per CC-1 (specs/README.md):
        symbol, name, atomic_number, category, tier, commercial_production,
        criticality {us_critical, eu_crm, eu_strategic, doe_rank},
        byproduct_of, top_mining_country, top_mining_share, hhi_mining,
        hhi_refining, end_use_buckets,
        producer_countries_mining, top_country_mining, top_country_share_pct,
        has_mining, has_refining, has_reserves, critical (heatmap extras).
    """
    reserves_shares_by_symbol = reserves_shares_by_symbol or {}
    index: list[dict] = []

    for el in elements_list:
        symbol = str(el["symbol"])
        doe_raw = el.get("doe_short_term_criticality_rank")
        try:
            doe_rank: int | None = int(float(doe_raw)) if doe_raw is not None and str(doe_raw) not in ("nan", "None", "") else None
        except (ValueError, TypeError):
            doe_rank = None

        # Mining HHI + top country
        mining_shares = mining_shares_by_symbol.get(symbol, [])
        hhi_mining, top_mining_country, top_mining_share = _compute_hhi(mining_shares)

        # Refining HHI (no top-country exposed; used by heatmap)
        refining_shares = refining_shares_by_symbol.get(symbol, [])
        hhi_refining, _top_ref, _share_ref = _compute_hhi(refining_shares)

        # Producer countries (mining, excludes ZZ/XX)
        producer_countries: list[str] = sorted({str(s["country"]) for s in mining_shares if s.get("country") not in (None, "", "ZZ", "XX")})

        # End-use buckets
        uses = end_uses_by_symbol.get(symbol, [])
        bucket_set: set[str] = set()
        unmapped_share: float = 0.0
        total_share: float = sum(float(u["share_pct"]) for u in uses if u.get("share_pct") is not None)

        for use in uses:
            app = str(use.get("application") or "")
            share = float(use["share_pct"]) if use.get("share_pct") is not None else 0.0
            bucket = END_USE_BUCKET_MAP.get(app)
            if bucket:
                bucket_set.add(bucket)
            else:
                unmapped_share += share
                if app:
                    print(f"[warn] end_use slug not in bucket map: {app!r} (symbol={symbol})", file=sys.stderr)

        if unmapped_share > 0 and uses:
            bucket_set.add("other")
            if total_share > 0 and (unmapped_share / total_share) > 0.20:
                print(
                    f"[warn] {symbol}: {unmapped_share:.0f}% of end-use share is unmapped to a bucket "
                    f"(>{int(unmapped_share / total_share * 100)}% threshold exceeded)",
                    file=sys.stderr,
                )

        # Byproduct parents
        byproduct_of = byproduct_by_symbol.get(symbol, [])

        # Heatmap extras (CC-1 additions): per-stage presence + simple criticality bool
        us_crit = bool(el.get("us_critical_list_as_of_2025"))
        eu_crm = bool(el.get("eu_crm_list_as_of_2024"))
        eu_strat = bool(el.get("eu_strategic_list_as_of_2024"))
        critical_bool = us_crit or eu_crm or eu_strat or (doe_rank is not None)
        reserves_shares = reserves_shares_by_symbol.get(symbol, [])

        entry: dict = {
            "symbol": symbol,
            "name": str(el.get("name") or ""),
            "atomic_number": int(el["atomic_number"]),
            "category": str(el.get("category") or ""),
            "tier": int(el["industrial_tier"]) if el.get("industrial_tier") is not None else 0,
            "commercial_production": bool(el.get("commercial_production")),
            "criticality": {
                "us_critical": us_crit,
                "eu_crm": eu_crm,
                "eu_strategic": eu_strat,
                "doe_rank": doe_rank,
            },
            "critical": critical_bool,
            "byproduct_of": byproduct_of,
            "top_mining_country": top_mining_country,
            "top_mining_share": top_mining_share,
            "hhi_mining": hhi_mining,
            "hhi_refining": hhi_refining,
            "has_mining": len(mining_shares) > 0,
            "has_refining": len(refining_shares) > 0,
            "has_reserves": len(reserves_shares) > 0,
            "end_use_buckets": sorted(bucket_set),
            # Aliases used by table_filter.js (match spec §4.1 field names)
            "producer_countries_mining": producer_countries,
            "top_country_mining": top_mining_country,
            "top_country_share_pct": top_mining_share,
        }
        index.append(entry)

    return json.dumps(index, ensure_ascii=False, separators=(",", ":"))


def _render_ext_links(symbol: str, name: str) -> str:
    title_name = (name or symbol).title()
    wiki_slug = WIKIPEDIA_NAME_OVERRIDES.get(title_name, title_name)
    wiki_url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(wiki_slug)
    parts = [f'<a href="{_html_escape(wiki_url)}" target="_blank" rel="noopener">Wikipedia<span class="arrow">↗</span></a>']
    price_slug = ELEMENT_PRICE_SLUGS.get(symbol)
    if price_slug:
        price_url = PRICE_URL_TEMPLATE.format(slug=price_slug)
        parts.append(
            f'<a href="{_html_escape(price_url)}" target="_blank" rel="noopener">'
            f'Live prices (Trading Economics)<span class="arrow">↗</span></a>'
        )
    return '<div class="ext-links">' + "".join(parts) + "</div>"


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────

CSS = """\
/* Atlas — minimal system-font stylesheet */
:root {
  --bg:       #ffffff;
  --surface:  #f6f7f8;
  --border:   #d4d8de;
  --text:     #1a1c1e;
  --muted:    #6b7280;
  --accent:   #2563eb;

  --badge-commercial:    #16a34a;
  --badge-no-commercial: #6b7280;
  --badge-us-critical:   #dc2626;
  --badge-eu-crm:        #7c3aed;
  --badge-eu-strategic:  #9333ea;
  --badge-doe:           #d97706;

  --tier-primary:        #0369a1;
  --tier-secondary:      #6b7280;
  --tier-tertiary:       #92400e;
  --map-land:            #dbe4ee;
  --map-land-stroke:     #94a3b8;
  --map-land-hover:      #bfdbfe;
  --map-land-hover-stroke: #2563eb;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg:      #0f1117;
    --surface: #1a1d26;
    --border:  #2d3140;
    --text:    #e8eaf0;
    --muted:   #9ca3af;
    --accent:  #60a5fa;
    --map-land:            #374151;
    --map-land-stroke:     #4b5563;
    --map-land-hover:      #1d4ed8;
    --map-land-hover-stroke: #93c5fd;
  }
}

*, *::before, *::after { box-sizing: border-box; }

body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  background: var(--bg);
  color: var(--text);
  margin: 0;
  padding: 0 1rem;
  /* Allow the map-panel-shell to break out to 100vw without a scrollbar */
  overflow-x: clip;
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.container { max-width: 1100px; margin: 0 auto; padding: 1.5rem 0; }

/* ── header ── */
header { border-bottom: 1px solid var(--border); padding-bottom: 1rem; margin-bottom: 1.5rem; }
header h1 { margin: 0 0 0.25rem; font-size: 1.5rem; }
header p.subtitle { margin: 0; color: var(--muted); font-size: 0.9rem; }

/* ── element grid / table ── */
.element-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
.element-table th {
  text-align: left;
  padding: 0.5rem 0.6rem;
  border-bottom: 2px solid var(--border);
  color: var(--muted);
  font-weight: 600;
  white-space: nowrap;
}
.element-table td {
  padding: 0.45rem 0.6rem;
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}
.element-table tr:hover td { background: var(--surface); }
.symbol-cell { font-weight: 700; font-size: 1rem; }
.atomic-num  { color: var(--muted); font-size: 0.8rem; }

/* ── badges ── */
.badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  color: #fff;
  margin-right: 0.2em;
  white-space: nowrap;
}
.badge-commercial    { background: var(--badge-commercial); }
.badge-no-commercial { background: var(--badge-no-commercial); }
.badge-us-critical   { background: var(--badge-us-critical); }
.badge-eu-crm        { background: var(--badge-eu-crm); }
.badge-eu-strategic  { background: var(--badge-eu-strategic); }
.badge-doe           { background: var(--badge-doe); color: #fff; }

/* ── binary criticality cells (index table) ── */
.crit-cell { text-align: center; }
.crit-yes  { color: var(--badge-us-critical); font-weight: 700; }
.crit-no   { color: var(--muted); }

/* ── header tooltip (hover a <th> to see its source document) ── */
.th-tip { position: relative; cursor: help; border-bottom: 1px dotted var(--muted); }
.th-tip:hover::after,
.th-tip:focus::after {
  content: attr(data-tip);
  position: absolute;
  top: calc(100% + 4px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--text);
  color: var(--bg);
  padding: 0.45rem 0.6rem;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 400;
  line-height: 1.4;
  letter-spacing: 0;
  text-transform: none;
  white-space: normal;
  width: 240px;
  z-index: 20;
  box-shadow: 0 4px 10px rgba(0,0,0,0.18);
  pointer-events: none;
}

/* ── source tier badges — distinct colors required by INV-2 ── */
.badge-tier-primary   { background: var(--tier-primary); }
.badge-tier-secondary { background: var(--tier-secondary); }
.badge-tier-tertiary  { background: var(--tier-tertiary); }

/* ── element page ── */
.el-header {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}
.el-symbol { font-size: 3rem; font-weight: 800; line-height: 1; }
.el-name   { font-size: 1.6rem; font-weight: 300; }
.el-meta   { color: var(--muted); font-size: 0.9rem; margin-bottom: 0.75rem; }

.ext-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  font-size: 0.85rem;
  margin: 0.25rem 0 1rem;
}
.ext-links a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid transparent;
}
.ext-links a:hover { border-bottom-color: var(--accent); }
.ext-links .arrow { opacity: 0.6; margin-left: 0.15em; }

.narrative-block {
  background: var(--surface);
  border-left: 4px solid var(--accent);
  border-radius: 0 6px 6px 0;
  padding: 0.75rem 1rem;
  margin: 1.25rem 0;
  white-space: pre-wrap;
  font-size: 0.9rem;
  line-height: 1.65;
}

/* ── chart placeholders ── */
.chart-placeholder {
  border: 2px dashed var(--border);
  border-radius: 6px;
  padding: 2rem;
  text-align: center;
  color: var(--muted);
  font-size: 0.88rem;
  margin: 1.25rem 0;
}

/* ── sources panel ── */
.sources-panel { margin: 1.5rem 0; }
.sources-panel h2 { font-size: 1rem; margin: 0 0 0.75rem; }

.source-cards { display: grid; gap: 0.75rem; }

.source-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.75rem 1rem;
}
.source-card-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.3rem;
}
.source-card-header a { font-weight: 600; font-size: 0.9rem; }
.source-card-meta { font-size: 0.8rem; color: var(--muted); margin-bottom: 0.45rem; }
.source-card-superseded {
  font-size: 0.8rem;
  color: var(--badge-us-critical);
  margin-bottom: 0.4rem;
  font-weight: 600;
}
.source-card-refs { font-size: 0.8rem; display: flex; flex-wrap: wrap; gap: 0.3rem; align-items: center; }
.source-card-refs .refs-label { color: var(--muted); margin-right: 0.1rem; }

.ref-chip {
  display: inline-block;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 0.1em 0.45em;
  font-size: 0.75rem;
  color: var(--text);
  white-space: nowrap;
}

/* ── isotope panel ── */
.isotope-panel { margin: 1.5rem 0; }
.isotope-panel > h2 { font-size: 1rem; margin: 0 0 0.75rem; }

.isotope-cards { display: grid; gap: 1rem; }

.isotope-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.75rem 1rem;
}
.isotope-card-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}
.isotope-card-header h3 { margin: 0; font-size: 1rem; font-weight: 700; }
.isotope-meta { font-size: 0.85rem; color: var(--muted); margin-bottom: 0.75rem; }
.isotope-meta-row { margin-bottom: 0.2rem; }
.isotope-meta-label { font-weight: 600; color: var(--text); }

/* production mode badge colors */
.badge-mode-stockpile_separated   { background: #7c3aed; }
.badge-mode-reactor_generated     { background: #0369a1; }
.badge-mode-accelerator_generated { background: #b45309; }
.badge-mode-decay_product         { background: #059669; }
.badge-mode-naturally_occurring   { background: #6b7280; }

/* producers section */
.producers-section { margin-top: 0.75rem; }
.producers-section h4 {
  font-size: 0.85rem; margin: 0 0 0.5rem;
  color: var(--muted); font-weight: 600;
}

/* low-confidence producers are visually distinct */
.producer-low-confidence {
  opacity: 0.7;
  font-style: italic;
}

/* ── index map ── */
.map-panel {
  margin: 0 0 1.75rem;
}

.map-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.map-panel-header h2 {
  margin: 0;
  font-size: 1rem;
}

.map-panel-copy {
  margin: 0;
  color: var(--muted);
  font-size: 0.88rem;
}

.country-map-shell {
  position: relative;
  background: linear-gradient(180deg, var(--surface), var(--bg));
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  overflow: hidden;
  /* Break out of the 1100px container to use the full viewport width */
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
  width: 100vw;
}

.country-map-root {
  min-height: 420px;
  padding: 0.5rem;
  max-height: 80vh;
}

.country-map-root svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 78vh;
}

.country-map-fallback {
  padding: 2rem 1.25rem;
  color: var(--muted);
  font-size: 0.9rem;
}

.country-shape {
  fill: var(--map-land);
  stroke: var(--map-land-stroke);
  stroke-width: 0.7;
  transition: fill 120ms ease, stroke 120ms ease, stroke-width 120ms ease;
}

.country-shape:hover,
.country-shape.is-hovered,
.country-shape.is-pinned {
  fill: var(--map-land-hover);
  stroke: var(--map-land-hover-stroke);
  stroke-width: 1.2;
}

.country-map-tooltip {
  position: fixed;
  z-index: 20;
  width: min(360px, calc(100vw - 2rem));
  padding: 0.85rem 0.95rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: 0 12px 35px rgba(15, 23, 42, 0.16);
  pointer-events: none;
}

.country-map-tooltip[hidden] {
  display: none;
}

.country-map-tooltip-title {
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 0.15rem;
}

.country-map-tooltip-subtitle {
  color: var(--muted);
  font-size: 0.74rem;
  margin-bottom: 0.5rem;
}

.country-map-tooltip-table-wrap {
  max-height: 320px;
  overflow-y: auto;
}

.country-map-tooltip-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
}

.country-map-tooltip-table th {
  text-align: left;
  color: var(--muted);
  font-weight: 600;
  border-bottom: 1px solid var(--border);
  padding: 0 0 0.3rem;
  white-space: nowrap;
}

.country-map-tooltip-table td {
  border-bottom: 1px solid var(--border);
  padding: 0.28rem 0;
  vertical-align: top;
}

.country-map-tooltip-table tbody tr:last-child td {
  border-bottom: none;
}

.country-map-tooltip-col-el {
  font-weight: 700;
  padding-right: 0.55rem;
  white-space: nowrap;
}

.country-map-tooltip-col-stage {
  color: var(--muted);
  padding-right: 0.55rem;
  white-space: nowrap;
}

.country-map-tooltip-col-global {
  text-align: right;
  color: var(--accent);
  font-weight: 600;
  white-space: nowrap;
}

.country-map-drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.28);
  opacity: 0;
  pointer-events: none;
  transition: opacity 140ms ease;
  z-index: 25;
}

.country-map-drawer-backdrop.is-open {
  opacity: 1;
  pointer-events: auto;
}

.country-map-drawer {
  position: fixed;
  top: 0;
  right: 0;
  width: min(460px, calc(100vw - 1rem));
  height: 100vh;
  background: var(--bg);
  border-left: 1px solid var(--border);
  box-shadow: -16px 0 40px rgba(15, 23, 42, 0.16);
  transform: translateX(100%);
  transition: transform 180ms ease;
  z-index: 30;
  display: grid;
  grid-template-rows: auto 1fr;
}

.country-map-drawer.is-open {
  transform: translateX(0);
}

.country-map-drawer-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: flex-start;
  padding: 1rem 1rem 0.75rem;
  border-bottom: 1px solid var(--border);
}

.country-map-drawer-title {
  margin: 0;
  font-size: 1.05rem;
}

.country-map-drawer-subtitle {
  margin: 0.2rem 0 0;
  color: var(--muted);
  font-size: 0.8rem;
}

.country-map-drawer-close {
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text);
  border-radius: 999px;
  width: 2rem;
  height: 2rem;
  font-size: 1rem;
  line-height: 1;
  cursor: pointer;
}

.country-map-drawer-body {
  padding: 0.9rem 1rem 1rem;
  overflow-y: auto;
}

.country-map-drawer-summary {
  color: var(--muted);
  font-size: 0.82rem;
  margin: 0 0 0.75rem;
}

.country-map-drawer-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}

.country-map-drawer-table th {
  position: sticky;
  top: 0;
  background: var(--bg);
  text-align: left;
  color: var(--muted);
  font-weight: 600;
  border-bottom: 1px solid var(--border);
  padding: 0 0 0.45rem;
}

.country-map-drawer-table td {
  border-bottom: 1px solid var(--border);
  padding: 0.45rem 0;
  vertical-align: top;
}

.country-map-drawer-table td a {
  font-weight: 700;
}

.country-map-drawer-stream {
  display: block;
  color: var(--muted);
  font-size: 0.75rem;
  margin-top: 0.1rem;
}

.country-map-drawer-global {
  color: var(--accent);
  font-weight: 600;
  white-space: nowrap;
}

.country-map-drawer-empty {
  color: var(--muted);
  font-size: 0.84rem;
}

.country-map-empty {
  color: var(--muted);
  font-size: 0.82rem;
}

@media (max-width: 860px) {
  .country-map-drawer {
    width: 100vw;
    max-width: 100vw;
  }
}

/* ── footer ── */
footer {
  border-top: 1px solid var(--border);
  margin-top: 2rem;
  padding-top: 0.75rem;
  font-size: 0.8rem;
  color: var(--muted);
}
footer a { color: var(--muted); }

/* ── site nav ── */
.site-nav {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  font-size: 0.875rem;
}
.site-nav a { color: var(--muted); }
.site-nav a:hover { color: var(--accent); text-decoration: none; }

/* ── country pages ── */
.country-page-header { display: flex; align-items: baseline; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.5rem; }
.country-flag { font-size: 2rem; line-height: 1; }
.country-iso-badge { font-size: 0.85rem; color: var(--muted); font-family: monospace; }
.country-territory-note { font-size: 0.85rem; color: var(--muted); margin-left: 0.25rem; }
.country-stat-pills { display: flex; gap: 0.75rem; flex-wrap: wrap; margin: 1rem 0; }
.country-stat-pill { background: var(--surface); border: 1px solid var(--border); border-radius: 0.375rem; padding: 0.35rem 0.75rem; font-size: 0.85rem; }
.country-stat-pill strong { display: block; font-size: 1.25rem; }
.country-map-thumbnail { width: 240px; height: 135px; background: var(--surface); border: 1px solid var(--border); border-radius: 0.375rem; display: inline-block; vertical-align: top; margin-left: 1rem; }
.country-header-row { display: flex; align-items: flex-start; flex-wrap: wrap; }
.country-jump-nav { display: flex; gap: 1rem; margin: 1rem 0; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; font-size: 0.9rem; }
.country-page-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.country-page-table th { text-align: left; padding: 0.5rem 0.4rem; border-bottom: 2px solid var(--border); color: var(--muted); font-weight: 600; cursor: pointer; user-select: none; white-space: nowrap; }
.country-page-table th[aria-sort="ascending"]::after { content: " \2191"; }
.country-page-table th[aria-sort="descending"]::after { content: " \2193"; }
.country-page-table td { padding: 0.4rem 0.4rem; border-bottom: 1px solid var(--border); vertical-align: top; }
.country-page-table tr:hover td { background: var(--surface); }
.country-page-empty { color: var(--muted); font-style: italic; padding: 0.5rem 0; }
.country-bar-chart { margin: 1.5rem 0; }
.country-related { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--border); }
.country-related-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; }
.country-related-tag { font-size: 0.8rem; background: var(--surface); border: 1px solid var(--border); border-radius: 0.25rem; padding: 0.2rem 0.4rem; }
.country-map-drawer-link { margin-top: 0.75rem; font-size: 0.9rem; }

/* ── table controls (filter chips + search) ── */
.table-controls {
  margin: 0 0 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.table-search-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.table-search {
  flex: 1 1 220px;
  max-width: 340px;
  padding: 0.35rem 0.65rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text);
  font-size: 0.88rem;
}

.table-search:focus {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.clear-all-btn {
  padding: 0.3rem 0.65rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--surface);
  color: var(--text);
  font-size: 0.82rem;
  cursor: pointer;
  white-space: nowrap;
}

.clear-all-btn:hover { background: var(--border); }

.filter-row {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  flex-wrap: wrap;
}

.filter-group-label {
  font-size: 0.78rem;
  color: var(--muted);
  font-weight: 600;
  white-space: nowrap;
  min-width: 5.5rem;
}

.filter-chip {
  padding: 0.2rem 0.6rem;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--surface);
  color: var(--text);
  font-size: 0.78rem;
  cursor: pointer;
  white-space: nowrap;
  transition: background 80ms ease, border-color 80ms ease;
}

.filter-chip:hover { border-color: var(--accent); }

.filter-chip:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.filter-chip.active {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.filter-select {
  padding: 0.25rem 0.55rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text);
  font-size: 0.82rem;
  cursor: pointer;
}

.country-page-link {
  font-size: 0.8rem;
  color: var(--accent);
  white-space: nowrap;
}

/* ── empty state row ── */
.table-empty-state td {
  text-align: center;
  color: var(--muted);
  padding: 1.5rem 0.6rem;
  font-size: 0.88rem;
}

.table-empty-state .clear-inline-btn {
  background: none;
  border: none;
  color: var(--accent);
  cursor: pointer;
  font-size: 0.88rem;
  padding: 0 0.2rem;
  text-decoration: underline;
}

/* ── sortable column headers ── */
.th-sortable {
  cursor: pointer;
  user-select: none;
  position: relative;
}

.th-sortable:hover { background: var(--surface); }

.th-sortable:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.th-sortable::after {
  content: "";
  display: inline-block;
  width: 0.7em;
  margin-left: 0.3em;
  opacity: 0.35;
}

.th-sortable[aria-sort="ascending"]::after  { content: "▲"; opacity: 1; }
.th-sortable[aria-sort="descending"]::after { content: "▼"; opacity: 1; }

/* ── byproduct graph CTA ── */
.byproduct-graph-cta {
  margin: 0.75rem 0 0;
  font-size: 0.85rem;
}

/* ── sr-only utility ── */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

/* ── heatmap controls ── */
:root {
  --map-no-data: #e8e8e8;
}
@media (prefers-color-scheme: dark) {
  :root { --map-no-data: #374151; }
}

.heatmap-controls {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.heatmap-selector-wrap {
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.heatmap-element-select {
  width: 220px;
  font-size: 0.85rem;
  padding: 0.3rem 0.5rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text);
}

.heatmap-clear {
  background: none;
  border: 1px solid var(--border);
  border-radius: 999px;
  width: 1.6rem;
  height: 1.6rem;
  font-size: 1rem;
  line-height: 1;
  cursor: pointer;
  color: var(--muted);
  padding: 0;
}
.heatmap-clear:hover { color: var(--text); border-color: var(--text); }

.heatmap-stage-toggle {
  display: flex;
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
}

.heatmap-stage-btn {
  background: var(--bg);
  border: none;
  border-right: 1px solid var(--border);
  padding: 0.3rem 0.7rem;
  font-size: 0.82rem;
  cursor: pointer;
  color: var(--muted);
  transition: background 120ms, color 120ms;
}
.heatmap-stage-btn:last-child { border-right: none; }
.heatmap-stage-btn:hover { background: var(--surface); color: var(--text); }
.heatmap-stage-btn.is-active {
  color: var(--accent);
  font-weight: 600;
  border-bottom: 2px solid var(--accent);
}
.heatmap-stage-toggle[aria-disabled="true"] .heatmap-stage-btn {
  opacity: 0.4;
  pointer-events: none;
}

.heatmap-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-bottom: 0.5rem;
}

.heatmap-chip {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.2em 0.55em;
  border: 1px solid var(--accent);
  border-radius: 999px;
  color: var(--accent);
  background: transparent;
  cursor: pointer;
  transition: background 120ms, color 120ms;
  white-space: nowrap;
}
.heatmap-chip:hover { background: var(--accent); color: #fff; }
.heatmap-chip.is-active { background: var(--accent); color: #fff; }

/* ── heatmap legend ── */
.heatmap-legend {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-top: 0.5rem;
  padding: 0.4rem 0;
  flex-wrap: wrap;
}

.heatmap-legend-label {
  font-size: 0.78rem;
  color: var(--muted);
  white-space: nowrap;
}

.heatmap-legend-bar-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.heatmap-legend-bar {
  display: block;
  border-radius: 3px;
}

.heatmap-legend-ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.7rem;
  color: var(--muted);
  width: 200px;
}

.heatmap-legend-footnote {
  font-size: 0.72rem;
  color: var(--muted);
  font-style: italic;
}

/* ── heatmap tooltip / drawer extras ── */
.country-map-heatmap-share {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text);
  margin-top: 0.3rem;
}
.country-map-heatmap-no-data {
  font-weight: 400;
  color: var(--muted);
  font-style: italic;
}

.heatmap-drawer-primary {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
}
.heatmap-drawer-element { font-size: 0.9rem; margin-bottom: 0.2rem; }
.heatmap-drawer-element a { font-weight: 700; }
.heatmap-drawer-stage-label { font-size: 0.78rem; color: var(--muted); margin-bottom: 0.4rem; }
.heatmap-drawer-share-pct { font-size: 1.4rem; font-weight: 700; color: var(--accent); }
.heatmap-drawer-quantity { font-size: 0.8rem; color: var(--muted); }
.heatmap-drawer-no-data { font-size: 0.85rem; color: var(--muted); font-style: italic; }
.heatmap-drawer-divider {
  font-size: 0.75rem;
  color: var(--muted);
  text-align: center;
  margin: 0.75rem 0 0.5rem;
  border-top: 1px solid var(--border);
  padding-top: 0.5rem;
}

/* ── byproduct graph page ── */
.byproduct-graph-panel {
  position: relative;
  margin: 0 0 2rem;
}

#byproduct-graph-root {
  overflow: visible;
  min-height: 300px;
}

#byproduct-graph-root svg {
  display: block;
  width: 100%;
  height: auto;
  overflow: visible;
}

.byproduct-tooltip {
  position: fixed;
  z-index: 50;
  max-width: 300px;
  padding: 0.75rem 0.85rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.14);
  pointer-events: none;
  font-size: 0.82rem;
  line-height: 1.5;
}

.byproduct-tooltip[hidden] { display: none; }

.byproduct-tooltip-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.byproduct-tooltip-row {
  color: var(--muted);
  margin-bottom: 0.1rem;
}

.byproduct-tooltip-row strong {
  color: var(--text);
  font-weight: 600;
}

/* byproduct graph legend */
.byproduct-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.5rem;
  margin: 0.5rem 0 1rem;
  font-size: 0.8rem;
  color: var(--muted);
}

.byproduct-legend-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.byproduct-legend-swatch {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  flex-shrink: 0;
}

.byproduct-legend-swatch-sq {
  width: 14px;
  height: 14px;
  border-radius: 3px;
  flex-shrink: 0;
}
"""


# ─────────────────────────────────────────────────────────────────────────────
# ISO name / sovereignt map (built from bundled GeoJSON at call time)
# ─────────────────────────────────────────────────────────────────────────────


def _build_iso_name_map() -> tuple[dict[str, str], dict[str, str]]:
    """Return (iso_to_name, iso_to_sovereignt) built from the bundled GeoJSON.

    Uses ISO_A2 (not ISO_A2_EH) as the key so that dependency territories
    that share an ISO_A2_EH with their sovereign are not conflated.  When a
    code appears in multiple features the first non-'-99' feature wins.
    NAME_EN is preferred over ADMIN.  COUNTRY_NAME_OVERRIDES may further
    substitute a display name.

    Returns two dicts:
        iso_to_name:      {ISO_A2: display_name}
        iso_to_sovereignt:{ISO_A2: sovereignt_name}
    """
    iso_to_name: dict[str, str] = {}
    iso_to_sovereignt: dict[str, str] = {}
    if not WORLD_COUNTRIES_GEOJSON.exists():
        return iso_to_name, iso_to_sovereignt

    import json as _json

    geojson = _json.loads(WORLD_COUNTRIES_GEOJSON.read_text(encoding="utf-8"))
    for feature in geojson.get("features", []):
        props = feature.get("properties") or {}
        iso = props.get("ISO_A2") or ""
        if not iso or iso == "-99":
            continue
        if iso in iso_to_name:
            continue  # first non-'-99' feature wins
        name_en = props.get("NAME_EN") or props.get("ADMIN") or iso
        # Apply optional project-level override
        display_name = COUNTRY_NAME_OVERRIDES.get(iso, name_en)
        sovereignt = props.get("SOVEREIGNT") or display_name
        iso_to_name[iso] = display_name
        iso_to_sovereignt[iso] = sovereignt

    return iso_to_name, iso_to_sovereignt


# ─────────────────────────────────────────────────────────────────────────────
# Country page data inversion
# ─────────────────────────────────────────────────────────────────────────────


def _build_country_page_data(con: "duckdb.DuckDBPyConnection") -> dict[str, list[dict]]:  # type: ignore[name-defined]
    """Invert atlas_shares into a per-country dict with ranks and criticality.

    Returns {ISO_A2: [row_dict, ...]} where each row_dict matches the shape
    defined in spec §4.1.  ZZ and XX are excluded.  Share types covered:
    mining, refining, reserves.
    """
    rows = con.execute(
        """
        SELECT
            s.country,
            s.symbol,
            e.name AS element_name,
            s.share_type AS stage,
            s.stream,
            s.share_pct,
            s.quantity_value,
            s.quantity_unit,
            s.confidence,
            s.notes,
            e.us_critical_list_as_of_2025,
            e.eu_crm_list_as_of_2024,
            RANK() OVER (
                PARTITION BY s.symbol, s.share_type
                ORDER BY s.share_pct DESC NULLS LAST
            ) AS global_rank
        FROM atlas_shares s
        JOIN atlas_elements e ON e.symbol = s.symbol
        WHERE s.country NOT IN ('ZZ', 'XX')
          AND s.country IS NOT NULL
          AND s.share_type IN ('mining', 'refining', 'reserves')
        ORDER BY s.country, s.share_type, s.share_pct DESC NULLS LAST
        """
    ).fetchall()

    # Build byproduct_of lookup: symbol -> [parent_symbol, ...]
    byproduct_of: dict[str, list[str]] = {}
    tables = {r[0] for r in con.execute("SHOW TABLES").fetchall()}
    if "atlas_byproducts" in tables:
        bp_rows = con.execute("SELECT symbol, parent_symbol FROM atlas_byproducts ORDER BY symbol, parent_symbol").fetchall()
        for sym, parent in bp_rows:
            byproduct_of.setdefault(str(sym), []).append(str(parent))

    def _safe_float(v) -> float | None:
        if v is None:
            return None
        try:
            f = float(v)
            return None if (f != f) else f
        except (TypeError, ValueError):
            return None

    def _safe_str(v) -> str | None:
        if v is None:
            return None
        s = str(v)
        return None if s in ("nan", "None", "") else s

    country_data: dict[str, list[dict]] = {}
    for row in rows:
        (
            country,
            symbol,
            element_name,
            stage,
            stream,
            share_pct,
            quantity_value,
            quantity_unit,
            confidence,
            notes,
            us_critical,
            eu_crm,
            global_rank,
        ) = row

        country_code = str(country)
        entry = {
            "symbol": str(symbol),
            "element_name": str(element_name) if element_name else str(symbol),
            "stage": str(stage),
            "stream": _safe_str(stream),
            "share_pct": _safe_float(share_pct),
            "quantity_value": _safe_float(quantity_value),
            "quantity_unit": _safe_str(quantity_unit),
            "confidence": _safe_str(confidence) or "high",
            "notes": _safe_str(notes),
            "global_rank": int(global_rank) if global_rank is not None else None,
            "us_critical": bool(us_critical) if us_critical is not None else False,
            "eu_crm": bool(eu_crm) if eu_crm is not None else False,
            "byproduct_of": byproduct_of.get(str(symbol), []),
        }
        country_data.setdefault(country_code, []).append(entry)

    n_countries = len(country_data)
    n_rows = sum(len(v) for v in country_data.values())
    print(f"country pages: {n_countries} countries, {n_rows} total rows")
    return country_data


# ─────────────────────────────────────────────────────────────────────────────
# Country summary stats
# ─────────────────────────────────────────────────────────────────────────────


def _compute_country_summary(rows: list[dict]) -> dict:
    """Compute the four summary stat pills for a country page.

    Args:
        rows: All row dicts for this country (from _build_country_page_data).

    Returns:
        {"n_mined": int, "n_refined": int, "n_top3_reserves": int, "n_critical": int}
    """
    mined: set[str] = set()
    refined: set[str] = set()
    top3_reserves: set[str] = set()
    critical: set[str] = set()

    for row in rows:
        sym = row["symbol"]
        stage = row["stage"]
        if stage == "mining":
            mined.add(sym)
        elif stage == "refining":
            refined.add(sym)
        elif stage == "reserves":
            rank = row.get("global_rank")
            if rank is not None and rank <= 3:
                top3_reserves.add(sym)
        if row.get("us_critical") or row.get("eu_crm"):
            critical.add(sym)

    return {
        "n_mined": len(mined),
        "n_refined": len(refined),
        "n_top3_reserves": len(top3_reserves),
        "n_critical": len(critical),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Flag emoji helper
# ─────────────────────────────────────────────────────────────────────────────


def _flag_emoji(iso2: str) -> str:
    """Return the Unicode flag emoji for a two-letter ISO-2 code.

    Rendering caveat: Windows browsers display letter pairs rather than flags.
    This is acceptable for v1 (see spec §8 Q1).
    """
    if len(iso2) != 2 or not iso2.isalpha():
        return ""
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in iso2.upper())


# ─────────────────────────────────────────────────────────────────────────────
# Ordinal formatting
# ─────────────────────────────────────────────────────────────────────────────


def _ordinal(n: int) -> str:
    """Return 1st, 2nd, 3rd, 4th, … for integer n."""
    if 11 <= (n % 100) <= 13:
        return f"{n}th"
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


# ─────────────────────────────────────────────────────────────────────────────
# Sources data builder
# ─────────────────────────────────────────────────────────────────────────────

#: Tables and their source_id column names for referenced_by counting.
_REF_TABLES: list[tuple[str, str, str]] = [
    ("production", "atlas_production", "source_id"),
    ("shares", "atlas_shares", "source_id"),
    ("reserves", "atlas_reserves", "source_id"),
    ("end_uses", "atlas_end_uses", "source_id"),
    ("prices", "atlas_prices", "source_id"),
    ("events", "atlas_events", "source_id"),
    ("isotope_markets", "atlas_isotope_markets", "production_source_id"),
    ("feedstocks", "atlas_feedstocks", "source_id"),
    ("substitutes", "atlas_substitutes", "source_id"),
    ("criticality", "atlas_criticality", "source_id"),
]


def _build_sources_data(con: "duckdb.DuckDBPyConnection", symbol: str) -> list[dict]:  # type: ignore[name-defined]
    """Return enriched source records for *symbol* with referenced_by counts.

    Each record:
        source_id, title, publisher, url, retrieved, publication_year,
        source_tier, superseded_by, referenced_by (dict category->count)
    """
    sources_df = con.execute(
        """
        SELECT source_id, title, publisher, url, retrieved, publication_year,
               source_tier, superseded_by
        FROM atlas_sources
        WHERE symbol = ?
        ORDER BY source_id
        """,
        [symbol],
    ).df()

    if sources_df.empty:
        return []

    # Build referenced_by counts via UNION ALL — one pass over all fact tables.
    union_clauses = "\n    UNION ALL\n    ".join(
        f"SELECT {sid_col} AS source_id, '{cat}' AS cat FROM {table} WHERE symbol = ?" for cat, table, sid_col in _REF_TABLES
    )
    refs_query = f"""
    WITH all_refs AS (
        {union_clauses}
    )
    SELECT source_id, cat, COUNT(*) AS cnt
    FROM all_refs
    WHERE source_id IS NOT NULL
    GROUP BY source_id, cat
    """
    refs_df = con.execute(refs_query, [symbol] * len(_REF_TABLES)).df()

    # Build dict: source_id -> {category: count}
    refs_by_source: dict[str, dict[str, int]] = {}
    for row in refs_df.itertuples(index=False):
        refs_by_source.setdefault(row.source_id, {})[row.cat] = int(row.cnt)

    result: list[dict] = []
    for row in sources_df.to_dict(orient="records"):
        sid = str(row["source_id"])
        superseded = row.get("superseded_by")
        # Normalise pandas NaN / None to None
        if superseded is not None and str(superseded) in ("nan", "None", ""):
            superseded = None
        result.append(
            {
                "source_id": sid,
                "title": row.get("title"),
                "publisher": row.get("publisher"),
                "url": row.get("url"),
                "retrieved": row.get("retrieved"),
                "publication_year": row.get("publication_year"),
                "source_tier": row.get("source_tier") or "secondary",
                "superseded_by": superseded,
                "referenced_by": refs_by_source.get(sid, {}),
            }
        )
    return result


def _build_country_map_data(con: "duckdb.DuckDBPyConnection") -> dict[str, object]:  # type: ignore[name-defined]
    """Return country-level mining/refining rows for the index hover map."""
    rows = con.execute(
        """
        SELECT
            s.country,
            s.symbol,
            s.share_type,
            s.stream,
            s.quantity_value,
            s.quantity_unit,
            CASE
                WHEN s.share_pct IS NOT NULL THEN s.share_pct
                WHEN s.quantity_value IS NOT NULL AND p.value IS NOT NULL AND p.value <> 0
                    THEN 100.0 * s.quantity_value / p.value
                ELSE NULL
            END AS global_pct
        FROM atlas_shares s
        JOIN atlas_production p
          ON p.symbol = s.symbol
         AND p.snapshot_year = s.snapshot_year
         AND p.stream IS NOT DISTINCT FROM s.stream
         AND (
            (s.share_type = 'mining' AND p.stage = 'mine')
            OR
            (s.share_type = 'refining' AND p.stage = 'refined')
         )
        WHERE s.share_type IN ('mining', 'refining')
          AND s.country IS NOT NULL
          AND s.country NOT IN ('ZZ', 'XX')
          AND s.quantity_value IS NOT NULL
          AND p.value IS NOT NULL
        """
    ).fetchall()

    countries: dict[str, list[dict[str, object]]] = {}
    for country, symbol, share_type, stream, quantity_value, quantity_unit, global_pct in rows:
        if country is None or symbol is None or quantity_value is None or quantity_unit is None or global_pct is None:
            continue
        country_code = str(country)
        entry = {
            "symbol": str(symbol),
            "stage": "mining" if share_type == "mining" else "refining",
            "stream": str(stream) if stream else None,
            "quantity_value": float(quantity_value),
            "quantity_unit": str(quantity_unit),
            "global_pct": round(float(global_pct), 3),
        }
        countries.setdefault(country_code, []).append(entry)

    for entries in countries.values():
        entries.sort(
            key=lambda row: (
                -float(row["global_pct"]),
                str(row["symbol"]),
                str(row["stage"]),
                str(row["stream"] or ""),
            )
        )

    # ── Reserves augmentation ──────────────────────────────────────────────
    # Add `reserves` sub-key: country ISO-2 → list of {symbol, share_pct, quantity_value, quantity_unit}
    # Excludes ZZ (rest-of-world aggregate) and rows with null share_pct.
    reserves_rows = con.execute(
        """
        SELECT country, symbol, share_pct, quantity_value, quantity_unit
        FROM atlas_shares
        WHERE share_type = 'reserves'
          AND country IS NOT NULL
          AND country NOT IN ('ZZ', 'XX')
          AND share_pct IS NOT NULL
        ORDER BY country, share_pct DESC
        """
    ).fetchall()

    reserves: dict[str, list[dict[str, object]]] = {}
    for country, symbol, share_pct, quantity_value, quantity_unit in reserves_rows:
        if country is None or symbol is None:
            continue
        country_code = str(country)
        entry = {
            "symbol": str(symbol),
            "share_pct": round(float(share_pct), 3),
            "quantity_value": float(quantity_value) if quantity_value is not None else None,
            "quantity_unit": str(quantity_unit) if quantity_unit else None,
        }
        reserves.setdefault(country_code, []).append(entry)

    return {
        "countries": countries,
        "country_count": len(countries),
        "row_count": sum(len(entries) for entries in countries.values()),
        "reserves": reserves,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Nav helper
# ─────────────────────────────────────────────────────────────────────────────


def _nav_html(prefix: str = "") -> str:
    """Return the <nav class="site-nav"> block.

    Args:
        prefix: Path prefix for hrefs.  "" for index-level pages,
                "../" for pages one level deep (elements/, countries/).
    """
    links = " &bull; ".join(f'<a href="{prefix}{href}">{_html_escape(label)}</a>' for label, href in _NAV_LINKS)
    return f'<nav class="site-nav">{links}</nav>'


# ─────────────────────────────────────────────────────────────────────────────
# Page builders
# ─────────────────────────────────────────────────────────────────────────────


def _page_shell(title: str, body: str, footer: str, include_table_filter: bool = False) -> str:
    nav = _nav_html(prefix="")
    table_filter_tag = (
        ('\n  <script src="assets/table_sort.js" defer></script>\n  <script src="assets/table_filter.js" defer></script>')
        if include_table_filter
        else ""
    )
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_html_escape(title)}</title>
  <link rel="stylesheet" href="assets/atlas.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="assets/charts_map.js" defer></script>{table_filter_tag}
</head>
<body>
<div class="container">
{nav}
{body}
<footer>
{footer}
</footer>
</div>
</body>
</html>"""


def _element_page_shell(title: str, body: str, footer: str) -> str:
    """Same as _page_shell but with ../ prefix for the CSS href.
    Also loads d3 v7 + charts_prices.js (B3 charts).
    """
    nav = _nav_html(prefix="../")
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_html_escape(title)}</title>
  <link rel="stylesheet" href="../assets/atlas.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="../assets/charts_prices.js" defer></script>
  <script src="../assets/charts_isotopes.js" defer></script>
</head>
<body>
<div class="container">
{nav}
{body}
<footer>
{footer}
</footer>
</div>
<script src="../assets/charts_production.js"></script>
<script src="../assets/charts_reserves.js"></script>
</body>
</html>"""


def _country_page_shell(title: str, body: str, footer: str) -> str:
    """Page shell for viewer/countries/{ISO}.html pages (one level deep)."""
    nav = _nav_html(prefix="../")
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_html_escape(title)}</title>
  <link rel="stylesheet" href="../assets/atlas.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
<div class="container">
{nav}
{body}
<footer>
{footer}
</footer>
</div>
<script src="../assets/charts_country.js"></script>
</body>
</html>"""


def _byproducts_page(graph_json: str, element_index_json: str, snapshot_year: int, footer: str) -> str:
    """Render the full byproducts.html page."""
    nav = _nav_html(prefix="")
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Byproduct dependency graph | Atlas {snapshot_year}</title>
  <link rel="stylesheet" href="assets/atlas.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
<div class="container">
{nav}
<header>
  <h1>Byproduct dependency graph</h1>
  <p class="subtitle">Elements whose supply is governed by another commodity&rsquo;s economics.</p>
</header>
<section class="byproduct-graph-panel">
  <div id="byproduct-graph-root"></div>
  <div id="byproduct-tooltip" class="byproduct-tooltip" hidden></div>
  <script id="byproduct-graph-data" type="application/json">{graph_json}</script>
  <script id="atlas-element-index" type="application/json">{element_index_json}</script>
</section>
<footer>
{footer}
</footer>
</div>
<script src="assets/charts_byproduct_graph.js"></script>
</body>
</html>"""


def _index_body(
    elements: list[dict],
    snapshot_year: int,
    country_map_data: dict[str, object],
    element_index: list[dict] | None = None,
) -> str:
    country_map_json = json.dumps(country_map_data, ensure_ascii=False, separators=(",", ":"))
    element_index_json = json.dumps(element_index or [], ensure_ascii=False, separators=(",", ":"))

    # Build a lookup from symbol -> element_index entry for data-* attribute rendering
    index_by_symbol: dict[str, dict] = {}
    if element_index:
        for entry in element_index:
            index_by_symbol[entry["symbol"]] = entry

    # Category chips — derive from actual element data for completeness
    _CATEGORY_LABELS: dict[str, str] = {
        "actinide": "Actinide",
        "alkali_metal": "Alkali metal",
        "alkaline_earth_metal": "Alkaline earth metal",
        "lanthanide": "Lanthanide",
        "metalloid": "Metalloid",
        "noble_gas": "Noble gas",
        "nonmetal": "Nonmetal",
        "post_transition_metal": "Post-transition metal",
        "synthetic_superheavy": "Synthetic superheavy",
        "transition_metal": "Transition metal",
    }
    categories_seen: list[str] = []
    for el in elements:
        cat = str(el.get("category") or "")
        if cat and cat not in categories_seen:
            categories_seen.append(cat)
    category_chips_html = ""
    for cat in sorted(categories_seen):
        label = _CATEGORY_LABELS.get(cat, cat.replace("_", " ").title())
        category_chips_html += f'    <button class="filter-chip" data-filter-key="cat" data-filter-val="{_html_escape(cat)}" aria-label="Category: {_html_escape(label)}">{_html_escape(label)}</button>\n'

    rows_html = ""
    for el in elements:
        symbol = el["symbol"]
        atomic = el["atomic_number"]
        name = el["name"]
        category = el["category"] or ""
        tier = el["industrial_tier"]
        commercial_flag = bool(el["commercial_production"])
        comm_html = _commercial_badge(commercial_flag)

        def _crit_td(flag: object) -> str:
            if flag:
                return '<td class="crit-cell crit-yes" aria-label="yes">&#10003;</td>'
            return '<td class="crit-cell crit-no" aria-label="no">&mdash;</td>'

        us_td = _crit_td(el.get("us_critical_list_as_of_2025"))
        crm_td = _crit_td(el.get("eu_crm_list_as_of_2024"))
        strat_td = _crit_td(el.get("eu_strategic_list_as_of_2024"))

        # Derive data-* attributes from the element index entry (if available)
        idx = index_by_symbol.get(symbol, {})
        crit = idx.get("criticality", {})
        us_critical_attr = "true" if crit.get("us_critical") else "false"
        eu_crm_attr = "true" if crit.get("eu_crm") else "false"
        eu_strat_attr = "true" if crit.get("eu_strategic") else "false"
        doe_rank_raw = crit.get("doe_rank")
        doe_rank_attr = str(int(doe_rank_raw)) if doe_rank_raw is not None else "0"
        byproduct_of_list = idx.get("byproduct_of", [])
        byproduct_attr = "true" if byproduct_of_list else "false"
        enduse_buckets = idx.get("end_use_buckets", [])
        enduse_attr = " ".join(enduse_buckets)
        producer_countries = idx.get("producer_countries_mining", [])
        prod_countries_attr = " ".join(producer_countries)
        top_country_attr = str(idx.get("top_country_mining") or "")
        top_share_val = idx.get("top_country_share_pct")
        top_share_attr = f"{float(top_share_val):.1f}" if top_share_val is not None else ""
        hhi_mining_val = idx.get("hhi_mining")
        hhi_mining_attr = str(int(hhi_mining_val)) if hhi_mining_val is not None else ""

        rows_html += f"""\
  <tr
    data-symbol="{_html_escape(symbol)}"
    data-atomic-number="{atomic}"
    data-name="{_html_escape(name)}"
    data-category="{_html_escape(category)}"
    data-tier="{tier}"
    data-commercial="{str(commercial_flag).lower()}"
    data-byproduct="{byproduct_attr}"
    data-us-critical="{us_critical_attr}"
    data-eu-crm="{eu_crm_attr}"
    data-eu-strategic="{eu_strat_attr}"
    data-doe-rank="{doe_rank_attr}"
    data-enduse-buckets="{_html_escape(enduse_attr)}"
    data-producer-countries="{_html_escape(prod_countries_attr)}"
    data-top-country="{_html_escape(top_country_attr)}"
    data-top-share="{_html_escape(top_share_attr)}"
    data-hhi-mining="{_html_escape(hhi_mining_attr)}"
  >
    <td class="symbol-cell"><a href="elements/{_html_escape(symbol)}.html">{_html_escape(symbol)}</a></td>
    <td class="atomic-num">{atomic}</td>
    <td>{_html_escape(name)}</td>
    <td>{_html_escape(category)}</td>
    <td>{tier}</td>
    <td>{comm_html}</td>
    {us_td}
    {crm_td}
    {strat_td}
  </tr>
"""

    # Serialize element_index for the inline <script> block
    element_index_json = json.dumps(element_index or [], ensure_ascii=False, separators=(",", ":"))
    country_flag_attr = "true" if COUNTRY_PAGES_ENABLED else "false"
    byproduct_flag_attr = "true" if BYPRODUCT_GRAPH_ENABLED else "false"

    return f"""\
<header>
  <h1>Periodic Element Supply Chain Atlas &mdash; {snapshot_year}</h1>
  <p class="subtitle">A structured, source-cited snapshot of critical element supply chains.</p>
</header>
<section class="map-panel">
  <div class="map-panel-header">
    <p id="map-panel-copy" class="map-panel-copy">Hover for a compact scan of attributed 2025 mining/refining rows. Click a country for a fuller breakdown with native quantities and share of global annual output.</p>
  </div>
  <div class="heatmap-controls" id="heatmap-controls">
    <div class="heatmap-selector-wrap">
      <label for="heatmap-element-select" class="sr-only">Element</label>
      <select id="heatmap-element-select" class="heatmap-element-select">
        <option value="">&mdash; select element &mdash;</option>
      </select>
      <button id="heatmap-clear" class="heatmap-clear" hidden aria-label="Clear element selection">&times;</button>
    </div>
    <div class="heatmap-stage-toggle" id="heatmap-stage-toggle" aria-disabled="true">
      <button class="heatmap-stage-btn is-active" data-stage="mining">Mining</button>
      <button class="heatmap-stage-btn" data-stage="refining">Refining</button>
      <button class="heatmap-stage-btn" data-stage="reserves">Reserves</button>
    </div>
  </div>
  <div class="heatmap-chips" id="heatmap-chips"></div>
  <div class="country-map-shell">
    <div id="country-map-root" class="country-map-root" data-geojson-src="assets/world_countries_50m.geojson">
      <div class="country-map-fallback">Loading country map&hellip;</div>
    </div>
  </div>
  <div id="country-map-tooltip" class="country-map-tooltip" hidden></div>
  <div id="country-map-drawer-backdrop" class="country-map-drawer-backdrop" hidden></div>
  <aside id="country-map-drawer" class="country-map-drawer" hidden aria-hidden="true">
    <div class="country-map-drawer-header">
      <div>
        <h3 id="country-map-drawer-title" class="country-map-drawer-title">Country detail</h3>
        <p id="country-map-drawer-subtitle" class="country-map-drawer-subtitle">Click a country to pin a detailed view.</p>
      </div>
      <button id="country-map-drawer-close" class="country-map-drawer-close" type="button" aria-label="Close country detail">&times;</button>
    </div>
    <div id="country-map-drawer-body" class="country-map-drawer-body"></div>
  </aside>
  <script id="atlas-element-index" type="application/json">{element_index_json}</script>
  <script id="atlas-country-map-data" type="application/json">{country_map_json}</script>
  <script id="atlas-element-index" type="application/json">{element_index_json}</script>
</section>
<script id="atlas-element-index" type="application/json">{element_index_json}</script>
<div class="table-controls" id="table-controls"
     data-country-pages-enabled="{country_flag_attr}"
     data-byproduct-graph-enabled="{byproduct_flag_attr}">
  <div class="table-search-row">
    <input type="search" class="table-search" id="table-search"
           placeholder="Symbol, name, or number\u2026" aria-label="Search elements">
    <button class="clear-all-btn" id="clear-all-btn" hidden>Clear all filters \u00d7</button>
  </div>
  <div class="filter-row" data-filter-group="criticality" aria-label="Criticality filters">
    <span class="filter-group-label">Criticality</span>
    <button class="filter-chip" data-filter-key="us_critical">US Critical</button>
    <button class="filter-chip" data-filter-key="eu_crm">EU CRM</button>
    <button class="filter-chip" data-filter-key="eu_strategic">EU Strategic</button>
    <button class="filter-chip" data-filter-key="doe_rank">DOE rank</button>
  </div>
  <div class="filter-row" data-filter-group="tier" aria-label="Industrial tier filters">
    <span class="filter-group-label">Tier</span>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="0">0</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="1">1</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="2">2</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="3">3</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="4">4</button>
  </div>
  <div class="filter-row" data-filter-group="category" aria-label="Category filters">
    <span class="filter-group-label">Category</span>
{category_chips_html}  </div>
  <div class="filter-row" data-filter-group="misc" aria-label="Other filters">
    <span class="filter-group-label">Other</span>
    <button class="filter-chip" data-filter-key="commercial_only">Commercial only</button>
    <button class="filter-chip" data-filter-key="no_commercial">No commercial production</button>
    <button class="filter-chip" data-filter-key="byproduct_only">Byproduct-only</button>
  </div>
  <div class="filter-row" data-filter-group="selects">
    <span class="filter-group-label">End-use</span>
    <select class="filter-select" id="enduse-select" aria-label="Filter by end-use bucket">
      <option value="">All end-uses</option>
    </select>
    <span class="filter-group-label">Country</span>
    <select class="filter-select" id="country-select" aria-label="Filter by producer country (mining)">
      <option value="">All countries</option>
    </select>
    <a class="country-page-link" id="country-page-link" href="#" hidden>View country page \u2192</a>
  </div>
</div>
<div class="byproduct-graph-cta" id="byproduct-graph-cta" hidden>
  <a href="byproducts.html">Open byproduct dependency graph \u2192</a>
</div>
<table class="element-table" id="element-table">
  <thead>
    <tr>
      <th class="th-sortable" data-sort-key="symbol" role="columnheader" aria-sort="none" tabindex="0">Symbol</th>
      <th class="th-sortable" data-sort-key="atomic_number" role="columnheader" aria-sort="none" tabindex="0">#</th>
      <th class="th-sortable" data-sort-key="name" role="columnheader" aria-sort="none" tabindex="0">Name</th>
      <th class="th-sortable" data-sort-key="category" role="columnheader" aria-sort="none" tabindex="0">Category</th>
      <th class="th-sortable" data-sort-key="tier" role="columnheader" aria-sort="none" tabindex="0">Tier</th>
      <th class="th-sortable" data-sort-key="commercial" role="columnheader" aria-sort="none" tabindex="0">Production</th>
      <th class="crit-cell th-sortable" data-sort-key="us_critical" role="columnheader" aria-sort="none" tabindex="0"><span class="th-tip" tabindex="-1" data-tip="USGS Final List of Critical Minerals (2022 Federal Register notice; governs US policy through 2025). 50 commodities deemed essential to the US economy / national security with significant supply-risk exposure.">US Critical</span></th>
      <th class="crit-cell th-sortable" data-sort-key="eu_crm" role="columnheader" aria-sort="none" tabindex="0"><span class="th-tip" tabindex="-1" data-tip="EU Critical Raw Materials Act (March 2024), Annex II. 34 critical raw materials with high economic importance and elevated supply-risk.">EU CRM</span></th>
      <th class="crit-cell th-sortable" data-sort-key="eu_strategic" role="columnheader" aria-sort="none" tabindex="0"><span class="th-tip" tabindex="-1" data-tip="EU Critical Raw Materials Act (March 2024), Annex I. 17 strategic raw materials prioritised for the green and digital transitions (subset of CRM).">EU Strategic</span></th>
      <th class="th-sortable" data-sort-key="top_country_share" role="columnheader" aria-sort="none" tabindex="0">Top country</th>
      <th class="th-sortable" data-sort-key="hhi_mining" role="columnheader" aria-sort="none" tabindex="0">HHI <sup title="Herfindahl-Hirschman Index (mining). Higher = more concentrated. Max 10,000 = single-country monopoly.">?</sup></th>
    </tr>
  </thead>
  <tbody>
{rows_html}    <tr class="table-empty-state" hidden>
      <td colspan="11">No elements match the active filters.
        <button class="clear-inline-btn" type="button">Clear filters</button>
      </td>
    </tr>
  </tbody>
</table>"""


def _render_sources_panel(sources: list[dict]) -> str:
    """Render the #sources-panel div from enriched source records."""
    if not sources:
        return '<div id="sources-panel" class="sources-panel"><h2>Sources</h2><p><em>No sources recorded.</em></p></div>'

    REF_ORDER = [
        "production",
        "shares",
        "reserves",
        "end_uses",
        "prices",
        "events",
        "isotope_markets",
        "feedstocks",
        "substitutes",
        "criticality",
    ]

    cards_html = ""
    for s in sources:
        sid = str(s.get("source_id", ""))
        title_raw = str(s.get("title") or sid)
        publisher = str(s.get("publisher") or "")
        url_raw = str(s.get("url") or "")
        retrieved = str(s.get("retrieved") or "")
        pub_year = s.get("publication_year")
        tier = str(s.get("source_tier") or "secondary")
        superseded_by = s.get("superseded_by")
        referenced_by: dict = s.get("referenced_by") or {}

        # Title — linked if URL present
        if url_raw and url_raw not in ("nan", "None"):
            title_html = f'<a href="{_html_escape(url_raw)}" target="_blank" rel="noopener">{_html_escape(title_raw)}</a>'
        else:
            title_html = _html_escape(title_raw)

        # Tier badge
        tier_safe = tier if tier in ("primary", "secondary", "tertiary") else "secondary"
        tier_badge = f'<span class="badge badge-tier-{tier_safe}">{_html_escape(tier_safe)}</span>'

        # Meta line: publisher · year · retrieved
        meta_parts = []
        if publisher and publisher not in ("nan", "None"):
            meta_parts.append(_html_escape(publisher))
        if pub_year is not None and str(pub_year) not in ("nan", "None", ""):
            meta_parts.append(str(int(float(str(pub_year)))))
        if retrieved and retrieved not in ("nan", "None"):
            meta_parts.append(f"retrieved {_html_escape(retrieved)}")
        meta_html = " &bull; ".join(meta_parts) if meta_parts else ""

        # Superseded-by warning
        superseded_html = ""
        if superseded_by is not None and str(superseded_by) not in ("nan", "None", ""):
            superseded_html = f'<div class="source-card-superseded">&#9888; superseded by <code>{_html_escape(str(superseded_by))}</code></div>'

        # Referenced-by chips
        chips = ""
        total_refs = sum(referenced_by.values())
        if total_refs > 0:
            for cat in REF_ORDER:
                cnt = referenced_by.get(cat, 0)
                if cnt:
                    chips += f'<span class="ref-chip">{_html_escape(cat)} {cnt}</span>'
        refs_html = ""
        if chips:
            refs_html = f'<div class="source-card-refs"><span class="refs-label">referenced by:</span>{chips}</div>'

        cards_html += f"""\
  <div class="source-card" data-source-id="{_html_escape(sid)}">
    <div class="source-card-header">
      {tier_badge}
      {title_html}
    </div>
    {"<div class='source-card-meta'>" + meta_html + "</div>" if meta_html else ""}
    {superseded_html}
    {refs_html}
  </div>
"""

    return f"""\
<div id="sources-panel" class="sources-panel">
  <h2>Sources ({len(sources)})</h2>
  <div class="source-cards">
{cards_html}  </div>
</div>"""


def _render_isotope_panel(isotopes: list[dict]) -> str:
    """Render the #isotope-panel div.

    If *isotopes* is empty, returns a placeholder div (same style as other placeholders).
    Otherwise returns a full panel with one card per isotope plus an inline JSON data block
    for the charts_isotopes.js bar chart renderer.
    """
    if not isotopes:
        return '<div id="isotope-panel" class="chart-placeholder">Isotope markets — see B5</div>'

    # Inline JSON for the JS renderer (bar chart + low-confidence styling)
    isotope_json = json.dumps(isotopes, ensure_ascii=False, separators=(",", ":"))
    inline_script = f'<script id="isotope-data" type="application/json">{isotope_json}</script>'

    cards_html = ""
    for iso in isotopes:
        isotope_name = str(iso.get("isotope", ""))
        hl_display = str(iso.get("half_life_display", ""))
        prod_mode = str(iso.get("production_mode", ""))
        precursor = iso.get("precursor")
        delivery_form = iso.get("delivery_form")
        reporting_year = iso.get("reporting_year")
        completeness = str(iso.get("producers_completeness", ""))
        producers = iso.get("producers") or []

        # Production mode badge — use a known CSS class or fallback
        safe_mode = (
            prod_mode
            if prod_mode
            in (
                "stockpile_separated",
                "reactor_generated",
                "accelerator_generated",
                "decay_product",
                "naturally_occurring",
            )
            else "unknown"
        )
        mode_badge = f'<span class="badge badge-mode-{_html_escape(safe_mode)}">{_html_escape(prod_mode or "unknown")}</span>'

        # Meta rows: half-life, precursor, delivery form
        meta_rows = f'<div class="isotope-meta-row"><span class="isotope-meta-label">Half-life:</span> {_html_escape(hl_display)}</div>\n'
        if precursor:
            meta_rows += f'<div class="isotope-meta-row"><span class="isotope-meta-label">Precursor:</span> {_html_escape(precursor)}</div>\n'
        if delivery_form:
            meta_rows += (
                f'<div class="isotope-meta-row"><span class="isotope-meta-label">Delivery form:</span> {_html_escape(delivery_form)}</div>\n'
            )
        if reporting_year:
            meta_rows += f'<div class="isotope-meta-row"><span class="isotope-meta-label">Reporting year:</span> {reporting_year}</div>\n'

        # Producers: build an HTML table; JS will optionally replace with bar chart
        if producers:
            completeness_label = completeness.replace("_", " ").title() if completeness else ""
            completeness_badge = (
                f'<span class="badge badge-no-commercial" style="font-size:0.7rem">{_html_escape(completeness_label)}</span>'
                if completeness_label
                else ""
            )
            producer_rows_html = ""
            for p in producers:
                country = str(p.get("country") or "")
                share = p.get("share_pct")
                conf = str(p.get("confidence") or "")
                low_class = " producer-low-confidence" if conf == "low" else ""
                share_str = f"{share:.0f}%" if share is not None else "?"
                # Link country to country page when enabled and not an excluded pseudo-code
                if COUNTRY_PAGES_ENABLED and country and country not in ("ZZ", "XX", ""):
                    country_cell = f'<a href="../countries/{_html_escape(country)}.html">{_html_escape(country)}</a>'
                else:
                    country_cell = _html_escape(country)
                producer_rows_html += f"""\
    <tr class="producer-row{low_class}">
      <td style="padding:0.2rem 0.5rem;font-weight:600">{country_cell}</td>
      <td style="padding:0.2rem 0.5rem">{share_str}</td>
      <td style="padding:0.2rem 0.5rem;font-size:0.75rem;color:var(--muted)">{_html_escape(conf)}</td>
    </tr>
"""
            producers_html = f"""\
<div class="producers-section">
  <h4>Producers {completeness_badge}</h4>
  <div class="producers-chart" data-isotope="{_html_escape(isotope_name)}">
    <table style="border-collapse:collapse;font-size:0.85rem;width:100%">
      <thead>
        <tr style="font-size:0.75rem;color:var(--muted)">
          <th style="padding:0.2rem 0.5rem;text-align:left">Country</th>
          <th style="padding:0.2rem 0.5rem;text-align:left">Share</th>
          <th style="padding:0.2rem 0.5rem;text-align:left">Confidence</th>
        </tr>
      </thead>
      <tbody>
{producer_rows_html}      </tbody>
    </table>
  </div>
</div>"""
        else:
            producers_html = ""

        cards_html += f"""\
  <div class="isotope-card" data-isotope="{_html_escape(isotope_name)}">
    <div class="isotope-card-header">
      <h3>{_html_escape(isotope_name)}</h3>
      {mode_badge}
    </div>
    <div class="isotope-meta">
{meta_rows}    </div>
    {producers_html}
  </div>
"""

    return f"""\
<div id="isotope-panel" class="isotope-panel">
  <h2>Isotope Markets ({len(isotopes)})</h2>
  {inline_script}
  <div class="isotope-cards">
{cards_html}  </div>
</div>"""


def _reserves_json(reserves_rows: list[dict], shares_rows: list[dict], end_uses_rows: list[dict]) -> str:
    """Build the inline JSON blob for reserves + end-uses charts.

    Returns a JSON string that is embedded as:
      <script id="reserves-data" type="application/json">...</script>

    Structure:
      {
        "reserves": {"economic_reserves": float|null, "resources": float|null, "unit": str|null},
        "reserves_by_country": [{"country": str, "share_pct": float, "quantity": float|null,
                                  "quantity_unit": str|null, "confidence": str}, ...],
        "end_uses": {"completeness": str, "uses": [{"application": str, "share_pct": float,
                                                     "confidence": str}, ...]}
      }
    """

    def _safe_float(v) -> float | None:
        if v is None:
            return None
        try:
            f = float(v)
            return None if (f != f) else f  # NaN check
        except (TypeError, ValueError):
            return None

    # Build reserves summary (economic_reserves + resources)
    econ_res: float | None = None
    resources: float | None = None
    unit: str | None = None
    for r in reserves_rows:
        kind = str(r.get("kind", ""))
        val = _safe_float(r.get("value"))
        u = str(r.get("unit", "")) if r.get("unit") else None
        if kind == "economic_reserves":
            econ_res = val
            unit = u or unit
        elif kind == "resources":
            resources = val
            unit = unit or u

    reserves_summary = {"economic_reserves": econ_res, "resources": resources, "unit": unit}

    # Build reserves_by_country list
    rbc = []
    for s in shares_rows:
        rbc.append(
            {
                "country": str(s.get("country", "")),
                "share_pct": _safe_float(s.get("share_pct")),
                "quantity": _safe_float(s.get("quantity_value")),
                "quantity_unit": str(s.get("quantity_unit", "")) if s.get("quantity_unit") else None,
                "confidence": str(s.get("confidence", "high")),
            }
        )

    # Build end_uses list
    completeness = "partial"
    uses = []
    for u in end_uses_rows:
        completeness = str(u.get("completeness", "partial"))
        uses.append(
            {
                "application": str(u.get("application", "")),
                "share_pct": _safe_float(u.get("share_pct")),
                "confidence": str(u.get("confidence", "high")),
            }
        )

    payload = {
        "reserves": reserves_summary,
        "reserves_by_country": rbc,
        "end_uses": {"completeness": completeness, "uses": uses},
    }
    return json.dumps(payload, separators=(",", ":"))


def _production_json(production_rows: list[dict], shares_rows: list[dict]) -> str:
    """Build the inline JSON blob for production + mining/refining share charts.

    Returns a JSON string embedded as:
      <script id="production-data" type="application/json">...</script>

    Structure:
      {
        "streams": [
          {
            "stream_id": int|null,
            "mining": [{"country": str, "share_pct": float, "quantity": float|null,
                         "unit": str|null, "form": str|null, "confidence": str}, ...],
            "refining": [...same shape...],
            "completeness": {"mining": str, "refining": str},
            "world_mine": {"value": float|null, "unit": str|null, "form": str|null},
            "world_refined": {"value": float|null, "unit": str|null, "form": str|null}
          }, ...
        ]
      }

    Each unique stream_id gets its own entry.  stream_id=None means the element
    has no multi-stream split (the common case).
    """

    def _safe_float(v) -> float | None:
        if v is None:
            return None
        try:
            f = float(v)
            return None if (f != f) else f  # NaN check
        except (TypeError, ValueError):
            return None

    def _safe_str(v) -> str | None:
        if v is None:
            return None
        s = str(v)
        return None if s in ("nan", "None", "") else s

    # Collect all stream ids present in shares (may be None/null)
    stream_ids: list = []
    seen: set = set()
    for row in shares_rows:
        sid = row.get("stream")
        # pandas NA / None → None
        if sid is not None:
            try:
                sid = int(sid)
            except (TypeError, ValueError):
                sid = None
        key = sid
        if key not in seen:
            seen.add(key)
            stream_ids.append(key)

    # Also include streams present only in production (no shares)
    for row in production_rows:
        sid = row.get("stream")
        if sid is not None:
            try:
                sid = int(sid)
            except (TypeError, ValueError):
                sid = None
        key = sid
        if key not in seen:
            seen.add(key)
            stream_ids.append(key)

    if not stream_ids:
        return json.dumps({"streams": []}, separators=(",", ":"))

    result_streams = []
    for stream_id in stream_ids:
        # Filter shares for this stream
        def _match_stream(row, sid=stream_id):
            rv = row.get("stream")
            if rv is not None:
                try:
                    rv = int(rv)
                except (TypeError, ValueError):
                    rv = None
            return rv == sid

        stream_shares = [r for r in shares_rows if _match_stream(r)]

        mining_shares: list[dict] = []
        refining_shares: list[dict] = []
        mining_completeness = "partial"
        refining_completeness = "partial"

        for s in stream_shares:
            share_type = str(s.get("share_type", ""))
            entry = {
                "country": _safe_str(s.get("country")) or "",
                "share_pct": _safe_float(s.get("share_pct")),
                "quantity": _safe_float(s.get("quantity_value")),
                "unit": _safe_str(s.get("quantity_unit")),
                "form": _safe_str(s.get("quantity_form")),
                "confidence": _safe_str(s.get("confidence")) or "high",
            }
            if share_type == "mining":
                mining_shares.append(entry)
                mining_completeness = _safe_str(s.get("completeness")) or "partial"
            elif share_type == "refining":
                refining_shares.append(entry)
                refining_completeness = _safe_str(s.get("completeness")) or "partial"

        # World totals from production rows for this stream
        world_mine: dict = {"value": None, "unit": None, "form": None}
        world_refined: dict = {"value": None, "unit": None, "form": None}
        for p in production_rows:
            p_stream = p.get("stream")
            if p_stream is not None:
                try:
                    p_stream = int(p_stream)
                except (TypeError, ValueError):
                    p_stream = None
            if p_stream != stream_id:
                continue
            stage = _safe_str(p.get("stage")) or ""
            val = _safe_float(p.get("value"))
            unit = _safe_str(p.get("unit"))
            form = _safe_str(p.get("form"))
            if stage == "mine" and world_mine["value"] is None:
                world_mine = {"value": val, "unit": unit, "form": form}
            elif stage == "refined" and world_refined["value"] is None:
                world_refined = {"value": val, "unit": unit, "form": form}

        result_streams.append(
            {
                "stream_id": stream_id,
                "mining": mining_shares,
                "refining": refining_shares,
                "completeness": {
                    "mining": mining_completeness,
                    "refining": refining_completeness,
                },
                "world_mine": world_mine,
                "world_refined": world_refined,
            }
        )

    return json.dumps({"streams": result_streams}, separators=(",", ":"))


def _render_producer_country_links(shares_rows: list[dict]) -> str:
    """Return a compact static list of producer countries (with country-page links) for element pages.

    Only renders mining and refining rows; used so the static HTML contains
    href="../countries/{ISO}.html" links that test CP-4 can assert on.  The
    full interactive chart is still rendered by charts_production.js.
    """
    if not COUNTRY_PAGES_ENABLED or not shares_rows:
        return ""

    # Deduplicate: keep the highest share_pct row per (country, share_type)
    seen: dict[tuple[str, str], float] = {}
    for r in shares_rows:
        country = str(r.get("country") or "")
        share_type = str(r.get("share_type") or "")
        if not country or country in ("ZZ", "XX") or share_type not in ("mining", "refining"):
            continue
        share = float(r.get("share_pct") or 0)
        key = (country, share_type)
        if key not in seen or share > seen[key]:
            seen[key] = share

    if not seen:
        return ""

    # Sort by descending share
    sorted_items = sorted(seen.items(), key=lambda kv: -kv[1])

    # Build compact inline list: "CD (76%), ID (10%), …"
    parts = []
    for (country, _stage), share in sorted_items[:10]:  # cap at 10 for readability
        href = f"../countries/{_html_escape(country)}.html"
        parts.append(f'<a href="{href}">{_html_escape(country)}</a>')

    return '<p class="el-producer-links" style="font-size:0.85rem;color:var(--muted)">Top producers: ' + ", ".join(parts) + "</p>"


def _element_body(
    el: dict,
    sources: list[dict],
    reserves_data: str = "{}",
    chart_data: dict | None = None,
    production_data: str = '{"streams":[]}',
    isotope_panel_html: str = "",
    mining_refining_shares: list[dict] | None = None,
) -> str:
    symbol = el["symbol"]
    atomic = el["atomic_number"]
    name = el["name"]
    category = el["category"] or ""
    tier = el["industrial_tier"]
    commercial = bool(el["commercial_production"])

    crit_html = _criticality_badges(el)
    comm_html = _commercial_badge(commercial)
    ext_links_html = _render_ext_links(symbol, name)

    narrative_html = ""
    if el.get("narrative") and str(el["narrative"]) not in ("nan", "None", ""):
        narrative_html = f'<div class="narrative-block">{_html_escape(str(el["narrative"]))}</div>'

    # Build placeholders — skip panels rendered separately below
    placeholders_html = ""
    for div_id, label in CHART_PLACEHOLDERS:
        if div_id in ("sources-panel", "production-chart", "isotope-panel"):
            continue  # rendered separately below
        placeholders_html += f'<div id="{div_id}" class="chart-placeholder">{_html_escape(label)}</div>\n'

    sources_panel_html = _render_sources_panel(sources)
    # isotope_panel_html is passed in from generate_viewer; default is a placeholder div
    if not isotope_panel_html:
        isotope_panel_html = '<div id="isotope-panel" class="chart-placeholder">Isotope markets — see B5</div>'

    no_commercial_note = ""
    if not commercial:
        no_commercial_note = '<p class="no-commercial-note"><em>No commercial production.</em></p>'

    # Inline JSON data for B3 charts (charts_prices.js reads this on DOMContentLoaded)
    chart_data_json = json.dumps(chart_data or {}, ensure_ascii=False, separators=(",", ":"))
    inline_data_script = f'<script type="application/json" id="atlas-chart-data">{chart_data_json}</script>'

    # Static producer country links (Step 10: wraps country ISOs in <a href="../countries/{ISO}.html">)
    producer_links_html = _render_producer_country_links(mining_refining_shares or [])

    return f"""\
{inline_data_script}
<p><a href="../index.html">&larr; Back to index</a></p>
<div class="el-header">
  <span class="el-symbol">{_html_escape(symbol)}</span>
  <span class="el-name">{_html_escape(name)}</span>
</div>
<div class="el-meta">
  Atomic number {atomic} &bull; {_html_escape(category)} &bull; Tier {tier}
</div>
<div class="badges-row">
  {comm_html}{crit_html}
</div>
{ext_links_html}
{no_commercial_note}
{narrative_html}
{producer_links_html}
<script id="production-data" type="application/json">{production_data}</script>
<div id="production-chart" class="chart-placeholder">Production charts — see B1</div>
<script id="reserves-data" type="application/json">{reserves_data}</script>
{placeholders_html}
{isotope_panel_html}
{sources_panel_html}"""


# ─────────────────────────────────────────────────────────────────────────────
# Country page renderer
# ─────────────────────────────────────────────────────────────────────────────


def _render_stage_table(stage_rows: list[dict], has_notes_col: bool) -> str:
    """Render the table for one stage section on a country page."""
    rows_html = ""
    for row in stage_rows:
        sym = row["symbol"]
        element_name = row["element_name"]
        share_pct = row.get("share_pct")
        qty_val = row.get("quantity_value")
        qty_unit = row.get("quantity_unit")
        rank = row.get("global_rank")
        conf = row.get("confidence") or ""
        notes = row.get("notes") or ""
        byproduct_of = row.get("byproduct_of") or []

        share_str = f"{share_pct:.1f}%" if share_pct is not None else "—"
        if qty_val is not None and qty_unit:
            unit_label = qty_unit.replace("_", " ")
            qty_str = f"{qty_val:,.0f} {unit_label}" if qty_val >= 100 else f"{qty_val:.1f} {unit_label}"
        else:
            qty_str = "—"
        rank_str = _ordinal(rank) if rank is not None else "—"
        low_class = " producer-low-confidence" if conf == "low" else ""

        # Notes: truncate + byproduct note
        notes_parts = []
        if notes:
            truncated = notes[:120] + "…" if len(notes) > 120 else notes
            notes_parts.append(f'<span title="{_html_escape(notes)}">{_html_escape(truncated)}</span>')
        if byproduct_of:
            parents = ", ".join(_html_escape(p) for p in byproduct_of)
            notes_parts.append(f'<span class="byproduct-note">byproduct of {parents}</span>')
        notes_td = " ".join(notes_parts)

        notes_cell = f"<td>{notes_td}</td>" if has_notes_col else ""

        rows_html += f"""\
  <tr class="{low_class.strip()}">
    <td><a href="../elements/{_html_escape(sym)}.html">{_html_escape(sym)}</a><br><small>{_html_escape(element_name)}</small></td>
    <td style="text-align:right">{share_str}</td>
    <td>{_html_escape(qty_str)}</td>
    <td style="text-align:center">{rank_str}</td>
    <td class="{low_class.strip()}">{_html_escape(conf)}</td>
    {notes_cell}
  </tr>
"""

    notes_th = "<th>Notes</th>" if has_notes_col else ""
    header = f"""\
<thead>
  <tr>
    <th>Element</th>
    <th style="text-align:right">Share %</th>
    <th>Quantity</th>
    <th style="text-align:center">Global rank</th>
    <th>Confidence</th>
    {notes_th}
  </tr>
</thead>"""

    return f'<table class="country-page-table sortable-table">\n{header}\n<tbody>\n{rows_html}</tbody>\n</table>'


def _render_country_page(
    iso: str,
    country_name: str,
    sovereignt: str,
    rows: list[dict],
    summary: dict,
    iso_to_name: dict[str, str],
) -> str:
    """Build the full body HTML for a country page.

    Args:
        iso:          ISO-2 country code.
        country_name: Display name from GeoJSON / overrides.
        sovereignt:   Sovereign state name (for territory notes).
        rows:         All row dicts for this country (from _build_country_page_data).
        summary:      Output of _compute_country_summary(rows).
        iso_to_name:  Full ISO→name map (for co-producer links).
    """
    flag = _flag_emoji(iso)
    title_html = f'<h1 class="country-page-header"><span class="country-flag">{flag}</span> {_html_escape(country_name)} <span class="country-iso-badge">({_html_escape(iso)})</span>'

    # Territory note: if sovereign differs from display name, note the relationship
    if sovereignt and sovereignt != country_name:
        title_html += f' <span class="country-territory-note">(administered by {_html_escape(sovereignt)})</span>'
    title_html += "</h1>"

    subtitle = '<p class="subtitle">Supply chain footprint &mdash; snapshot year 2025</p>'

    # Summary stat pills
    pills_html = f"""\
<div class="country-stat-pills">
  <div class="country-stat-pill"><strong>{summary["n_mined"]}</strong>Elements mined</div>
  <div class="country-stat-pill"><strong>{summary["n_refined"]}</strong>Elements refined</div>
  <div class="country-stat-pill"><strong>{summary["n_top3_reserves"]}</strong>Top-3 reserves</div>
  <div class="country-stat-pill"><strong>{summary["n_critical"]}</strong>Critical elements</div>
</div>"""

    # World-map thumbnail (client-side initialised by charts_country.js)
    map_thumb = f'<div class="country-map-thumbnail" id="country-map-thumb" data-country-code="{_html_escape(iso)}"></div>'

    # Jump nav
    jump_nav = """\
<nav class="country-jump-nav">
  <a href="#mining">Mining</a>
  <a href="#refining">Refining</a>
  <a href="#reserves">Reserves</a>
</nav>"""

    # Stage sections
    stage_rows_map: dict[str, list[dict]] = {"mining": [], "refining": [], "reserves": []}
    for r in rows:
        stage_rows_map.setdefault(r["stage"], []).append(r)

    # Default sort: descending share_pct
    for stage_list in stage_rows_map.values():
        stage_list.sort(key=lambda r: -(r.get("share_pct") or 0))

    sections_html = ""
    for stage_key, stage_label in [("mining", "Mining"), ("refining", "Refining"), ("reserves", "Reserves")]:
        stage_list = stage_rows_map.get(stage_key, [])
        n = len(stage_list)
        has_notes = any(r.get("notes") or r.get("byproduct_of") for r in stage_list)
        section_body = (
            _render_stage_table(stage_list, has_notes_col=has_notes)
            if stage_list
            else '<p class="country-page-empty">No attributed data for this stage.</p>'
        )
        sections_html += f"""\
<section id="{stage_key}">
  <h2>{stage_label} ({n} element{"s" if n != 1 else ""})</h2>
  {section_body}
</section>
"""

    # Chart data: top-15 elements by share_pct across all stages
    all_chart_rows = sorted(rows, key=lambda r: -(r.get("share_pct") or 0))[:15]
    chart_data = [
        {
            "symbol": r["symbol"],
            "element_name": r["element_name"],
            "stage": r["stage"],
            "share_pct": r.get("share_pct"),
        }
        for r in all_chart_rows
    ]
    chart_json = json.dumps(chart_data, ensure_ascii=False, separators=(",", ":"))
    chart_section = ""
    if len(rows) >= 3:
        chart_section = f"""\
<script id="country-chart-data" type="application/json">{chart_json}</script>
<div id="country-bar-chart" class="country-bar-chart"></div>"""

    # Related: co-producers — countries sharing top-3 rank for same element+stage
    top3_by_el_stage: dict[tuple[str, str], set[str]] = {}
    for r in rows:
        rank = r.get("global_rank")
        if rank is not None and rank <= 3:
            key = (r["symbol"], r["stage"])
            top3_by_el_stage.setdefault(key, set())

    # We need to find other top-3 countries for the same element+stage
    # Build from rows we have: rows only covers THIS country.
    # The co-producer data needs all countries. We embed the needed info at render time.
    # For now: collect symbols+stages where this country is top-3; the JS / build can
    # expand later. We'll store for the HTML section.
    # NOTE: Since _build_country_page_data returns only rows per-country,
    # we need to pass the full dataset or re-query. Per spec §3.5 we find all
    # other countries ranking top-3 in same element+stage. We store the
    # co-producers in the page data at generate_viewer time.
    # The actual co-producer rendering happens in generate_viewer where we have
    # all country data. For now we embed a placeholder div that generate_viewer
    # will fill via _render_country_page's `co_producers` parameter.
    # → signature extended below, related section rendered via parameter.

    # Related section placeholder (will be overridden in generate_viewer)
    related_html = ""  # filled by caller

    return (
        f"{title_html}\n{subtitle}\n"
        f'<div class="country-header-row">'
        f"<div>{pills_html}</div>"
        f"{map_thumb}"
        f"</div>\n"
        f"{jump_nav}\n"
        f"{sections_html}\n"
        f"{chart_section}\n"
        f"{related_html}"
    )


def _render_country_page_full(
    iso: str,
    country_name: str,
    sovereignt: str,
    rows: list[dict],
    summary: dict,
    iso_to_name: dict[str, str],
    all_country_data: dict[str, list[dict]],
) -> str:
    """Build the full body HTML for a country page including co-producers section.

    Args:
        all_country_data: Full {iso: rows} dict so we can find co-producers.
    """
    flag = _flag_emoji(iso)
    title_html = (
        f'<h1 class="country-page-header">'
        f'<span class="country-flag">{flag}</span> '
        f"{_html_escape(country_name)} "
        f'<span class="country-iso-badge">({_html_escape(iso)})</span>'
    )
    if sovereignt and sovereignt != country_name:
        title_html += f' <span class="country-territory-note">(administered by {_html_escape(sovereignt)})</span>'
    title_html += "</h1>"

    subtitle = '<p class="subtitle">Supply chain footprint &mdash; snapshot year 2025</p>'

    pills_html = f"""\
<div class="country-stat-pills">
  <div class="country-stat-pill"><strong>{summary["n_mined"]}</strong>Elements mined</div>
  <div class="country-stat-pill"><strong>{summary["n_refined"]}</strong>Elements refined</div>
  <div class="country-stat-pill"><strong>{summary["n_top3_reserves"]}</strong>Top-3 reserves</div>
  <div class="country-stat-pill"><strong>{summary["n_critical"]}</strong>Critical elements</div>
</div>"""

    map_thumb = f'<div class="country-map-thumbnail" id="country-map-thumb" data-country-code="{_html_escape(iso)}"></div>'

    jump_nav = """\
<nav class="country-jump-nav">
  <a href="#mining">Mining</a>
  <a href="#refining">Refining</a>
  <a href="#reserves">Reserves</a>
</nav>"""

    stage_rows_map: dict[str, list[dict]] = {"mining": [], "refining": [], "reserves": []}
    for r in rows:
        stage_rows_map.setdefault(r["stage"], []).append(r)
    for stage_list in stage_rows_map.values():
        stage_list.sort(key=lambda r: -(r.get("share_pct") or 0))

    sections_html = ""
    for stage_key, stage_label in [("mining", "Mining"), ("refining", "Refining"), ("reserves", "Reserves")]:
        stage_list = stage_rows_map.get(stage_key, [])
        n = len(stage_list)
        has_notes = any(r.get("notes") or r.get("byproduct_of") for r in stage_list)
        section_body = (
            _render_stage_table(stage_list, has_notes_col=has_notes)
            if stage_list
            else '<p class="country-page-empty">No attributed data for this stage.</p>'
        )
        sections_html += f"""\
<section id="{stage_key}">
  <h2>{stage_label} ({n} element{"s" if n != 1 else ""})</h2>
  {section_body}
</section>
"""

    # Chart data
    all_chart_rows = sorted(rows, key=lambda r: -(r.get("share_pct") or 0))[:15]
    chart_data = [
        {
            "symbol": r["symbol"],
            "element_name": r["element_name"],
            "stage": r["stage"],
            "share_pct": r.get("share_pct"),
        }
        for r in all_chart_rows
    ]
    chart_json = json.dumps(chart_data, ensure_ascii=False, separators=(",", ":"))
    chart_section = ""
    if len(rows) >= 3:
        chart_section = f"""\
<script id="country-chart-data" type="application/json">{chart_json}</script>
<div id="country-bar-chart" class="country-bar-chart"></div>"""

    # Co-producers section
    # For each element+stage where this country is top-3, find all other top-3 countries.
    this_country_el_stage: set[tuple[str, str]] = set()
    for r in rows:
        rank = r.get("global_rank")
        if rank is not None and rank <= 3:
            this_country_el_stage.add((r["symbol"], r["stage"]))

    co_producers: set[str] = set()
    for other_iso, other_rows in all_country_data.items():
        if other_iso == iso:
            continue
        for r in other_rows:
            key = (r["symbol"], r["stage"])
            if key in this_country_el_stage:
                rank = r.get("global_rank")
                if rank is not None and rank <= 3:
                    co_producers.add(other_iso)

    related_html = ""
    if co_producers:
        sorted_coproducers = sorted(co_producers)
        # Cap at 20
        extra = 0
        if len(sorted_coproducers) > 20:
            extra = len(sorted_coproducers) - 20
            sorted_coproducers = sorted_coproducers[:20]
        tags_html = ""
        for cp_iso in sorted_coproducers:
            cp_name = iso_to_name.get(cp_iso, cp_iso)
            tags_html += (
                f'<a href="{_html_escape(cp_iso)}.html" class="country-related-tag">{_html_escape(cp_name)} ({_html_escape(cp_iso)})</a>\n'
            )
        if extra:
            tags_html += f'<span class="country-related-tag">and {extra} more</span>\n'
        related_html = f"""\
<section class="country-related">
  <h2>Countries with overlapping top-3 positions</h2>
  <div class="country-related-tags">
{tags_html}  </div>
</section>"""
    else:
        related_html = """\
<section class="country-related">
  <!-- Critical minerals overview: placeholder for future link -->
</section>"""

    return (
        f"{title_html}\n{subtitle}\n"
        f'<p><a href="../index.html">&larr; Atlas index</a></p>\n'
        f'<div class="country-header-row">'
        f"<div>{pills_html}</div>"
        f"{map_thumb}"
        f"</div>\n"
        f"{jump_nav}\n"
        f"{sections_html}\n"
        f"{chart_section}\n"
        f"{related_html}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# Main generator
# ─────────────────────────────────────────────────────────────────────────────


def generate_viewer(
    db_path: Path,
    viewer_dir: Path,
    timestamp: str | None = None,
) -> None:
    """Generate the full static viewer into viewer_dir.

    Args:
        db_path:    Path to the atlas duckdb file.
        viewer_dir: Output directory (created if absent).
        timestamp:  ISO-format string used in the footer.  Defaults to utcnow().
                    Pass a fixed string in tests to get deterministic output.
    """
    if not db_path.exists():
        print(f"error: {db_path} not found — run scripts/build.py first", file=sys.stderr)
        sys.exit(1)

    ts = timestamp or datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    con = duckdb.connect(str(db_path), read_only=True)
    try:
        # Verify tables exist and have rows where expected
        tables = {row[0] for row in con.execute("SHOW TABLES").fetchall()}
        for required in ("atlas_elements", "atlas_criticality", "atlas_sources"):
            if required not in tables:
                print(f"error: table {required!r} not found in {db_path}", file=sys.stderr)
                sys.exit(1)

        elements_df = con.execute(
            """
            SELECT
                e.symbol, e.atomic_number, e.name, e.category, e.industrial_tier,
                e.commercial_production, e.narrative,
                e.us_critical_list_as_of_2025,
                e.eu_crm_list_as_of_2024,
                e.eu_strategic_list_as_of_2024,
                e.doe_short_term_criticality_rank,
                e.snapshot_year
            FROM atlas_elements e
            ORDER BY e.atomic_number
            """
        ).df()

        if elements_df.empty:
            print("error: atlas_elements table is empty", file=sys.stderr)
            sys.exit(1)

        snapshot_year: int = int(elements_df["snapshot_year"].iloc[0])

        elements_list = elements_df.to_dict(orient="records")

        # Build enriched sources data per symbol (includes referenced_by counts)
        sources_by_symbol: dict[str, list[dict]] = {}
        for sym in [el["symbol"] for el in elements_list]:
            sources_by_symbol[sym] = _build_sources_data(con, sym)

        country_map_data = _build_country_map_data(con)

        # Prepare reserves dict: symbol -> list of reserve rows
        reserves_df = con.execute("SELECT symbol, kind, value, unit FROM atlas_reserves ORDER BY symbol, kind").df()
        reserves_by_symbol: dict[str, list[dict]] = {}
        for row in reserves_df.to_dict(orient="records"):
            sym = row["symbol"]
            reserves_by_symbol.setdefault(sym, []).append(row)

        # Prepare reserves country shares: symbol -> list of share rows
        shares_df = con.execute(
            """
            SELECT symbol, country, share_pct, quantity_value, quantity_unit, confidence, completeness
            FROM atlas_shares
            WHERE share_type = 'reserves'
            ORDER BY symbol, share_pct DESC
            """
        ).df()
        shares_by_symbol: dict[str, list[dict]] = {}
        for row in shares_df.to_dict(orient="records"):
            sym = row["symbol"]
            shares_by_symbol.setdefault(sym, []).append(row)

        # Prepare end_uses: symbol -> list of use rows
        end_uses_df = con.execute(
            "SELECT symbol, application, share_pct, confidence, completeness FROM atlas_end_uses ORDER BY symbol, share_pct DESC"
        ).df()
        end_uses_by_symbol: dict[str, list[dict]] = {}
        for row in end_uses_df.to_dict(orient="records"):
            sym = row["symbol"]
            end_uses_by_symbol.setdefault(sym, []).append(row)

        # Prices per symbol (B3) — normalise usd_per_lb → usd_per_kg
        prices_by_symbol: dict[str, list[dict]] = {}
        if "atlas_prices" in tables:
            prices_df = con.execute("SELECT symbol, year, value, unit, form, basis, region FROM atlas_prices ORDER BY symbol, year").df()
            for row in prices_df.to_dict(orient="records"):
                sym = row["symbol"]
                prices_by_symbol.setdefault(sym, []).append(
                    {
                        "year": int(row["year"]),
                        "value": float(row["value"]),
                        "unit": str(row["unit"]),
                        "form": str(row["form"]) if row["form"] else "",
                        "basis": str(row["basis"]) if row["basis"] else "",
                        "region": str(row["region"]) if row["region"] else "",
                    }
                )
            for sym in prices_by_symbol:
                prices_by_symbol[sym] = _normalize_price_units(prices_by_symbol[sym])

        # Events per symbol (B3)
        events_by_symbol: dict[str, list[dict]] = {}
        if "atlas_events" in tables:
            events_df = con.execute("SELECT symbol, date, event, impact FROM atlas_events ORDER BY symbol, date").df()
            for row in events_df.to_dict(orient="records"):
                sym = row["symbol"]
                events_by_symbol.setdefault(sym, []).append(
                    {
                        "date": str(row["date"]),
                        "event": str(row["event"]) if row["event"] else "",
                        "impact": str(row["impact"]) if row["impact"] else "",
                    }
                )

        # Production world totals per symbol (B1)
        production_by_symbol: dict[str, list[dict]] = {}
        if "atlas_production" in tables:
            prod_df = con.execute(
                "SELECT symbol, stream, block_index, stage, value, unit, form FROM atlas_production ORDER BY symbol, stream, block_index, stage"
            ).df()
            for row in prod_df.to_dict(orient="records"):
                sym = row["symbol"]
                production_by_symbol.setdefault(sym, []).append(row)

        # Mining + refining country shares per symbol (B1)
        mining_refining_shares_by_symbol: dict[str, list[dict]] = {}
        if "atlas_shares" in tables:
            mr_df = con.execute(
                """
                SELECT symbol, share_type, stream, country, share_pct,
                       quantity_value, quantity_unit, quantity_form, confidence, completeness
                FROM atlas_shares
                WHERE share_type IN ('mining', 'refining')
                ORDER BY symbol, share_type, share_pct DESC
                """
            ).df()
            for row in mr_df.to_dict(orient="records"):
                sym = row["symbol"]
                mining_refining_shares_by_symbol.setdefault(sym, []).append(row)

        # Isotope markets per symbol (B5)
        isotope_data_by_symbol: dict[str, list[dict]] = {el["symbol"]: [] for el in elements_list}
        if "atlas_isotope_markets" in tables and "atlas_shares" in tables:
            for sym in [el["symbol"] for el in elements_list]:
                isotope_data_by_symbol[sym] = _build_isotope_data(con, sym)

        # Country page data (one query, all countries)
        country_page_data: dict[str, list[dict]] = {}
        if COUNTRY_PAGES_ENABLED and "atlas_shares" in tables:
            country_page_data = _build_country_page_data(con)

        # Byproduct parents per symbol — from atlas_byproducts table
        byproduct_by_symbol: dict[str, list[str]] = {el["symbol"]: [] for el in elements_list}
        if "atlas_byproducts" in tables:
            bp_df = con.execute("SELECT symbol, parent_symbol FROM atlas_byproducts ORDER BY symbol, parent_symbol").df()
            for row in bp_df.to_dict(orient="records"):
                sym = str(row["symbol"])
                parent = str(row["parent_symbol"])
                byproduct_by_symbol.setdefault(sym, []).append(parent)

        # Split mining vs refining shares for element index
        mining_shares_by_symbol: dict[str, list[dict]] = {}
        refining_shares_by_symbol: dict[str, list[dict]] = {}
        for sym, shares in mining_refining_shares_by_symbol.items():
            for s in shares:
                if str(s.get("share_type", "")) == "mining":
                    mining_shares_by_symbol.setdefault(sym, []).append(s)
                elif str(s.get("share_type", "")) == "refining":
                    refining_shares_by_symbol.setdefault(sym, []).append(s)

        # Build element metadata index (CC-1)
        element_index = _build_element_index(
            elements_list,
            mining_shares_by_symbol,
            refining_shares_by_symbol,
            end_uses_by_symbol,
            byproduct_by_symbol,
            reserves_shares_by_symbol=shares_by_symbol,
        )
        element_index_list = json.loads(element_index)

        # Byproduct graph data (BPG) — requires atlas_byproducts table
        graph_json: str = ""
        if "atlas_byproducts" in tables and BYPRODUCT_GRAPH_ENABLED:
            graph_json = _byproduct_graph_json(con)

    finally:
        con.close()

    # ── Write output files ──
    viewer_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = viewer_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    elements_dir = viewer_dir / "elements"
    elements_dir.mkdir(exist_ok=True)

    # CSS
    (assets_dir / "atlas.css").write_text(CSS, encoding="utf-8")

    # charts_prices.js — copy from project source so tests in tmpdirs get the file too
    if CHARTS_PRICES_JS.exists():
        (assets_dir / "charts_prices.js").write_text(CHARTS_PRICES_JS.read_text(encoding="utf-8"), encoding="utf-8")

    # charts_production.js — copy from project source
    if CHARTS_PRODUCTION_JS.exists():
        (assets_dir / "charts_production.js").write_text(CHARTS_PRODUCTION_JS.read_text(encoding="utf-8"), encoding="utf-8")

    # charts_isotopes.js — copy from project source
    if CHARTS_ISOTOPES_JS.exists():
        (assets_dir / "charts_isotopes.js").write_text(CHARTS_ISOTOPES_JS.read_text(encoding="utf-8"), encoding="utf-8")

    if CHARTS_MAP_JS.exists():
        (assets_dir / "charts_map.js").write_text(CHARTS_MAP_JS.read_text(encoding="utf-8"), encoding="utf-8")

    if CHARTS_COUNTRY_JS.exists():
        (assets_dir / "charts_country.js").write_text(CHARTS_COUNTRY_JS.read_text(encoding="utf-8"), encoding="utf-8")

    if WORLD_COUNTRIES_GEOJSON.exists():
        (assets_dir / "world_countries_50m.geojson").write_text(WORLD_COUNTRIES_GEOJSON.read_text(encoding="utf-8"), encoding="utf-8")

    # table_sort.js + table_filter.js — copy from project source
    if TABLE_SORT_JS.exists():
        (assets_dir / "table_sort.js").write_text(TABLE_SORT_JS.read_text(encoding="utf-8"), encoding="utf-8")
    if TABLE_FILTER_JS.exists():
        (assets_dir / "table_filter.js").write_text(TABLE_FILTER_JS.read_text(encoding="utf-8"), encoding="utf-8")

    if CHARTS_BYPRODUCT_GRAPH_JS.exists():
        (assets_dir / "charts_byproduct_graph.js").write_text(CHARTS_BYPRODUCT_GRAPH_JS.read_text(encoding="utf-8"), encoding="utf-8")

    # Footer shared across pages
    repo_url = "https://github.com/anomalyco/opencode"
    footer_index = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'
    footer_element = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'
    footer_country = footer_element

    # element_index is already the compact JSON string (from _build_element_index)
    element_index_json = element_index

    # index.html
    index_body = _index_body(elements_list, snapshot_year, country_map_data, element_index_list)
    index_html = _page_shell(
        f"Periodic Element Supply Chain Atlas — {snapshot_year}",
        index_body,
        footer_index,
        include_table_filter=True,
    )
    (viewer_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Per-element pages
    for el in elements_list:
        sym = el["symbol"]
        el_sources = sources_by_symbol.get(sym, [])
        res_json = _reserves_json(
            reserves_by_symbol.get(sym, []),
            shares_by_symbol.get(sym, []),
            end_uses_by_symbol.get(sym, []),
        )
        prod_json = _production_json(
            production_by_symbol.get(sym, []),
            mining_refining_shares_by_symbol.get(sym, []),
        )
        chart_data = {
            "prices": prices_by_symbol.get(sym, []),
            "events": events_by_symbol.get(sym, []),
        }
        isotope_data = isotope_data_by_symbol.get(sym, [])
        iso_panel_html = _render_isotope_panel(isotope_data)
        body = _element_body(
            el,
            el_sources,
            reserves_data=res_json,
            chart_data=chart_data,
            production_data=prod_json,
            isotope_panel_html=iso_panel_html,
            mining_refining_shares=mining_refining_shares_by_symbol.get(sym, []),
        )
        title = f"{sym} — {el['name']} | Atlas {snapshot_year}"
        html = _element_page_shell(title, body, footer_element)
        (elements_dir / f"{sym}.html").write_text(html, encoding="utf-8")

    # Per-country pages
    if COUNTRY_PAGES_ENABLED and country_page_data:
        iso_to_name, iso_to_sovereignt = _build_iso_name_map()
        countries_dir = viewer_dir / "countries"
        countries_dir.mkdir(exist_ok=True)
        for iso, iso_rows in sorted(country_page_data.items()):
            country_name = iso_to_name.get(iso, iso)
            if not iso_to_name.get(iso):
                print(f"warning: ISO {iso!r} not found in GeoJSON name map; using code as name", file=sys.stderr)
            sovereignt = iso_to_sovereignt.get(iso, country_name)
            summary = _compute_country_summary(iso_rows)
            body = _render_country_page_full(iso, country_name, sovereignt, iso_rows, summary, iso_to_name, country_page_data)
            title = f"{country_name} ({iso}) | Atlas {snapshot_year}"
            html = _country_page_shell(title, body, footer_country)
            (countries_dir / f"{iso}.html").write_text(html, encoding="utf-8")
            print(f"viewer/countries/{iso}.html written")

    # byproducts.html + byproducts-data.json
    if graph_json and BYPRODUCT_GRAPH_ENABLED:
        byproducts_html = _byproducts_page(graph_json, element_index_json, snapshot_year, footer_index)
        (viewer_dir / "byproducts.html").write_text(byproducts_html, encoding="utf-8")
        (viewer_dir / "byproducts-data.json").write_text(graph_json, encoding="utf-8")
        print("viewer/byproducts.html written")
        print("viewer/byproducts-data.json written")

    print(f"viewer/index.html written ({len(elements_list)} elements)")
    for el in elements_list:
        print(f"viewer/elements/{el['symbol']}.html written")
    print("viewer/assets/atlas.css written")
    if CHARTS_PRICES_JS.exists():
        print("viewer/assets/charts_prices.js written")
    if CHARTS_PRODUCTION_JS.exists():
        print("viewer/assets/charts_production.js written")
    if CHARTS_ISOTOPES_JS.exists():
        print("viewer/assets/charts_isotopes.js written")
    if CHARTS_MAP_JS.exists():
        print("viewer/assets/charts_map.js written")
    if CHARTS_COUNTRY_JS.exists():
        print("viewer/assets/charts_country.js written")
    if WORLD_COUNTRIES_GEOJSON.exists():
        print("viewer/assets/world_countries_50m.geojson written")
    if TABLE_SORT_JS.exists():
        print("viewer/assets/table_sort.js written")
    if TABLE_FILTER_JS.exists():
        print("viewer/assets/table_filter.js written")
    if CHARTS_BYPRODUCT_GRAPH_JS.exists():
        print("viewer/assets/charts_byproduct_graph.js written")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build atlas static HTML viewer")
    parser.add_argument("--db", type=Path, default=BUILD_DIR / "atlas-2025.duckdb", help="DuckDB source file")
    parser.add_argument("--out", type=Path, default=VIEWER_DIR, help="Output directory")
    parser.add_argument("--timestamp", default=None, help="Override build timestamp (ISO format)")
    args = parser.parse_args()

    generate_viewer(args.db, args.out, timestamp=args.timestamp)


if __name__ == "__main__":
    main()

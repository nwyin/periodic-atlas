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
WORLD_COUNTRIES_GEOJSON = ROOT / "viewer" / "assets" / "world_countries_50m.geojson"

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
    "Au": "gold", "Ag": "silver", "Cu": "copper", "Al": "aluminum",
    "Ni": "nickel", "Zn": "zinc", "Sn": "tin", "Pb": "lead",
    "Pt": "platinum", "Pd": "palladium", "Rh": "rhodium",
    "Ru": "ruthenium", "Ir": "iridium", "Os": "osmium",
    "Li": "lithium", "Co": "cobalt", "V": "vanadium", "U": "uranium",
    "Mo": "molybdenum", "W": "tungsten", "Re": "rhenium",
    "Nb": "niobium", "Ta": "tantalum", "Zr": "zirconium",
    "Hf": "hafnium", "Be": "beryllium", "Ti": "titanium",
    "Fe": "iron-ore", "Mn": "manganese", "Cr": "chromium", "Mg": "magnesium",
    "Nd": "neodymium", "Dy": "dysprosium",
    "Sb": "antimony", "Bi": "bismuth", "Ga": "gallium",
    "In": "indium", "Ge": "germanium", "Te": "tellurium",
    "Se": "selenium", "Cd": "cadmium",
}

# Wikipedia URL is derived from the element name; overrides catch disambiguation pages.
WIKIPEDIA_NAME_OVERRIDES: dict[str, str] = {
    "Mercury": "Mercury_(element)",
}


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
                    "unit": str(row["production_unit"]) if row.get("production_unit") and str(row.get("production_unit")) not in ("nan", "None") else None,
                },
                "producers": shares_by_isotope.get(iso, []),
                "producers_completeness": completeness,
                "notes": notes,
            }
        )
    return result


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


def _render_ext_links(symbol: str, name: str) -> str:
    title_name = (name or symbol).title()
    wiki_slug = WIKIPEDIA_NAME_OVERRIDES.get(title_name, title_name)
    wiki_url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(wiki_slug)
    parts = [
        f'<a href="{_html_escape(wiki_url)}" target="_blank" rel="noopener">'
        f'Wikipedia<span class="arrow">↗</span></a>'
    ]
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
"""


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

    return {
        "countries": countries,
        "country_count": len(countries),
        "row_count": sum(len(entries) for entries in countries.values()),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Page builders
# ─────────────────────────────────────────────────────────────────────────────


def _page_shell(title: str, body: str, footer: str) -> str:
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_html_escape(title)}</title>
  <link rel="stylesheet" href="assets/atlas.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="assets/charts_map.js" defer></script>
</head>
<body>
<div class="container">
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
{body}
<footer>
{footer}
</footer>
</div>
<script src="../assets/charts_production.js"></script>
<script src="../assets/charts_reserves.js"></script>
</body>
</html>"""


def _index_body(elements: list[dict], snapshot_year: int, country_map_data: dict[str, object]) -> str:
    country_map_json = json.dumps(country_map_data, ensure_ascii=False, separators=(",", ":"))

    rows_html = ""
    for el in elements:
        symbol = el["symbol"]
        atomic = el["atomic_number"]
        name = el["name"]
        category = el["category"] or ""
        tier = el["industrial_tier"]
        commercial_flag = bool(el["commercial_production"])
        crit_html = _criticality_badges(el)
        comm_html = _commercial_badge(commercial_flag)

        rows_html += f"""\
  <tr>
    <td class="symbol-cell"><a href="elements/{_html_escape(symbol)}.html">{_html_escape(symbol)}</a></td>
    <td class="atomic-num">{atomic}</td>
    <td>{_html_escape(name)}</td>
    <td>{_html_escape(category)}</td>
    <td>{tier}</td>
    <td>{comm_html}</td>
    <td>{crit_html}</td>
  </tr>
"""

    return f"""\
<header>
  <h1>Periodic Element Supply Chain Atlas &mdash; {snapshot_year}</h1>
  <p class="subtitle">A structured, source-cited snapshot of critical element supply chains.</p>
</header>
<section class="map-panel">
  <div class="map-panel-header">
    <p class="map-panel-copy">Hover for a compact scan of attributed 2025 mining/refining rows. Click a country for a fuller breakdown with native quantities and share of global annual output.</p>
  </div>
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
  <script id="atlas-country-map-data" type="application/json">{country_map_json}</script>
</section>
<table class="element-table">
  <thead>
    <tr>
      <th>Symbol</th>
      <th>#</th>
      <th>Name</th>
      <th>Category</th>
      <th>Tier</th>
      <th>Production</th>
      <th>Criticality</th>
    </tr>
  </thead>
  <tbody>
{rows_html}  </tbody>
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
        safe_mode = prod_mode if prod_mode in (
            "stockpile_separated", "reactor_generated", "accelerator_generated",
            "decay_product", "naturally_occurring",
        ) else "unknown"
        mode_badge = f'<span class="badge badge-mode-{_html_escape(safe_mode)}">{_html_escape(prod_mode or "unknown")}</span>'

        # Meta rows: half-life, precursor, delivery form
        meta_rows = f'<div class="isotope-meta-row"><span class="isotope-meta-label">Half-life:</span> {_html_escape(hl_display)}</div>\n'
        if precursor:
            meta_rows += f'<div class="isotope-meta-row"><span class="isotope-meta-label">Precursor:</span> {_html_escape(precursor)}</div>\n'
        if delivery_form:
            meta_rows += f'<div class="isotope-meta-row"><span class="isotope-meta-label">Delivery form:</span> {_html_escape(delivery_form)}</div>\n'
        if reporting_year:
            meta_rows += f'<div class="isotope-meta-row"><span class="isotope-meta-label">Reporting year:</span> {reporting_year}</div>\n'

        # Producers: build an HTML table; JS will optionally replace with bar chart
        if producers:
            completeness_label = completeness.replace("_", " ").title() if completeness else ""
            completeness_badge = f'<span class="badge badge-no-commercial" style="font-size:0.7rem">{_html_escape(completeness_label)}</span>' if completeness_label else ""
            producer_rows_html = ""
            for p in producers:
                country = str(p.get("country") or "")
                share = p.get("share_pct")
                conf = str(p.get("confidence") or "")
                low_class = " producer-low-confidence" if conf == "low" else ""
                share_str = f"{share:.0f}%" if share is not None else "?"
                producer_rows_html += f"""\
    <tr class="producer-row{low_class}">
      <td style="padding:0.2rem 0.5rem;font-weight:600">{_html_escape(country)}</td>
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


def _element_body(
    el: dict,
    sources: list[dict],
    reserves_data: str = "{}",
    chart_data: dict | None = None,
    production_data: str = '{"streams":[]}',
    isotope_panel_html: str = "",
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
<script id="production-data" type="application/json">{production_data}</script>
<div id="production-chart" class="chart-placeholder">Production charts — see B1</div>
<script id="reserves-data" type="application/json">{reserves_data}</script>
{placeholders_html}
{isotope_panel_html}
{sources_panel_html}"""


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

    if WORLD_COUNTRIES_GEOJSON.exists():
        (assets_dir / "world_countries_50m.geojson").write_text(WORLD_COUNTRIES_GEOJSON.read_text(encoding="utf-8"), encoding="utf-8")

    # Footer shared across pages
    repo_url = "https://github.com/anomalyco/opencode"
    footer_index = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'
    footer_element = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'

    # index.html
    index_body = _index_body(elements_list, snapshot_year, country_map_data)
    index_html = _page_shell(f"Periodic Element Supply Chain Atlas — {snapshot_year}", index_body, footer_index)
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
        body = _element_body(el, el_sources, reserves_data=res_json, chart_data=chart_data, production_data=prod_json, isotope_panel_html=iso_panel_html)
        title = f"{sym} — {el['name']} | Atlas {snapshot_year}"
        html = _element_page_shell(title, body, footer_element)
        (elements_dir / f"{sym}.html").write_text(html, encoding="utf-8")

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
    if WORLD_COUNTRIES_GEOJSON.exists():
        print("viewer/assets/world_countries_50m.geojson written")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build atlas static HTML viewer")
    parser.add_argument("--db", type=Path, default=BUILD_DIR / "atlas-2025.duckdb", help="DuckDB source file")
    parser.add_argument("--out", type=Path, default=VIEWER_DIR, help="Output directory")
    parser.add_argument("--timestamp", default=None, help="Override build timestamp (ISO format)")
    args = parser.parse_args()

    generate_viewer(args.db, args.out, timestamp=args.timestamp)


if __name__ == "__main__":
    main()

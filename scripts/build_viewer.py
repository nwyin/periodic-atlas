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
from datetime import datetime, timezone
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
VIEWER_DIR = ROOT / "viewer"

CHART_PLACEHOLDERS = [
    ("production-chart", "Production charts — see B1"),
    ("reserves-chart", "Reserves + end uses — see B2"),
    ("prices-chart", "Prices + events — see B3"),
    ("sources-panel", "Sources — see B4"),
    ("isotope-panel", "Isotope markets — see B5"),
]


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
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg:      #0f1117;
    --surface: #1a1d26;
    --border:  #2d3140;
    --text:    #e8eaf0;
    --muted:   #9ca3af;
    --accent:  #60a5fa;
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
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.container { max-width: 1100px; margin: 0 auto; padding: 1.5rem 0; }

/* ── header ── */
header { border-bottom: 1px solid var(--border); padding-bottom: 1rem; margin-bottom: 1.5rem; }
header h1 { margin: 0 0 0.25rem; font-size: 1.5rem; }
header p.subtitle { margin: 0; color: var(--muted); font-size: 0.9rem; }

/* ── stats row ── */
.stats-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1.75rem;
}
.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.75rem 1rem;
}
.stat-card .stat-value { font-size: 2rem; font-weight: 700; line-height: 1; }
.stat-card .stat-label { font-size: 0.8rem; color: var(--muted); margin-top: 0.2rem; }

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
    """Same as _page_shell but with ../ prefix for the CSS href."""
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
{body}
<footer>
{footer}
</footer>
</div>
<script src="../assets/charts_reserves.js"></script>
</body>
</html>"""


def _index_body(elements: list[dict], stats: dict, snapshot_year: int) -> str:
    total = stats["total_elements"]
    commercial = stats["commercial_production"]
    us_crit = stats["us_critical_list_as_of_2025"]
    eu_crm = stats["eu_crm_list_as_of_2024"]

    stat_cards = f"""\
  <div class="stat-card"><div class="stat-value">{total}</div><div class="stat-label">elements</div></div>
  <div class="stat-card"><div class="stat-value">{commercial}</div><div class="stat-label">commercial production</div></div>
  <div class="stat-card"><div class="stat-value">{us_crit}</div><div class="stat-label">US Critical List 2025</div></div>
  <div class="stat-card"><div class="stat-value">{eu_crm}</div><div class="stat-label">EU CRM List 2024</div></div>"""

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
<div class="stats-row">
{stat_cards}
</div>
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


def _element_body(el: dict, sources: list[dict], reserves_data: str = "{}") -> str:
    symbol = el["symbol"]
    atomic = el["atomic_number"]
    name = el["name"]
    category = el["category"] or ""
    tier = el["industrial_tier"]
    commercial = bool(el["commercial_production"])

    crit_html = _criticality_badges(el)
    comm_html = _commercial_badge(commercial)

    narrative_html = ""
    if el.get("narrative") and str(el["narrative"]) not in ("nan", "None", ""):
        narrative_html = f'<div class="narrative-block">{_html_escape(str(el["narrative"]))}</div>'

    # Build placeholders — skip sources-panel since we render it separately below
    placeholders_html = ""
    for div_id, label in CHART_PLACEHOLDERS:
        if div_id == "sources-panel":
            continue  # replaced by the real sources panel below
        placeholders_html += f'<div id="{div_id}" class="chart-placeholder">{_html_escape(label)}</div>\n'

    sources_panel_html = _render_sources_panel(sources)

    no_commercial_note = ""
    if not commercial:
        no_commercial_note = '<p class="no-commercial-note"><em>No commercial production.</em></p>'

    return f"""\
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
{no_commercial_note}
{narrative_html}
<script id="reserves-data" type="application/json">{reserves_data}</script>
{placeholders_html}
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

        # Stats for index
        stats = {
            "total_elements": len(elements_df),
            "commercial_production": int(elements_df["commercial_production"].sum()),
            "us_critical_list_as_of_2025": int(elements_df["us_critical_list_as_of_2025"].fillna(False).sum()),
            "eu_crm_list_as_of_2024": int(elements_df["eu_crm_list_as_of_2024"].fillna(False).sum()),
        }

        elements_list = elements_df.to_dict(orient="records")

        # Build enriched sources data per symbol (includes referenced_by counts)
        sources_by_symbol: dict[str, list[dict]] = {}
        for sym in [el["symbol"] for el in elements_list]:
            sources_by_symbol[sym] = _build_sources_data(con, sym)

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

    # Footer shared across pages
    repo_url = "https://github.com/anomalyco/opencode"
    footer_index = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'
    footer_element = f'Built {ts} &bull; Snapshot year {snapshot_year} &bull; <a href="{repo_url}" target="_blank" rel="noopener">repo</a>'

    # index.html
    index_body = _index_body(elements_list, stats, snapshot_year)
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
        body = _element_body(el, el_sources, reserves_data=res_json)
        title = f"{sym} — {el['name']} | Atlas {snapshot_year}"
        html = _element_page_shell(title, body, footer_element)
        (elements_dir / f"{sym}.html").write_text(html, encoding="utf-8")

    print(f"viewer/index.html written ({len(elements_list)} elements)")
    for el in elements_list:
        print(f"viewer/elements/{el['symbol']}.html written")
    print("viewer/assets/atlas.css written")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build atlas static HTML viewer")
    parser.add_argument("--db", type=Path, default=BUILD_DIR / "atlas-2025.duckdb", help="DuckDB source file")
    parser.add_argument("--out", type=Path, default=VIEWER_DIR, help="Output directory")
    parser.add_argument("--timestamp", default=None, help="Override build timestamp (ISO format)")
    args = parser.parse_args()

    generate_viewer(args.db, args.out, timestamp=args.timestamp)


if __name__ == "__main__":
    main()

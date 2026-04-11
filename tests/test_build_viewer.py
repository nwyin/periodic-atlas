"""Tests for scripts/build_viewer.py.

Invariants verified (B0):
  INV-1: generator runs end-to-end against real build/atlas-2025.duckdb without error
  INV-2: viewer/index.html contains a link to every element's page
  INV-3: every {symbol}.html contains the element's symbol and name
  INV-4: two back-to-back runs produce identical output (uses injected timestamp)
  INV-5: Og (no commercial_production) renders "No commercial production" text

Invariants verified (B4 — sources panel):
  B4-INV-1: Every source in atlas_sources for an element appears in that element's sources panel.
  B4-INV-2: CSS contains distinct styles for badge-tier-primary / badge-tier-secondary / badge-tier-tertiary.
  B4-INV-3: referenced_by counts reconcile with actual row counts in each fact table.
  B4-INV-4: A source with superseded_by set renders a visible 'superseded by' warning.

B2 invariants:
  B2-INV-1: every element with reserves gets a non-empty reserves_by_country list in its JSON
  B2-INV-2: every element with end_uses gets a non-empty uses list in its JSON
  B2-INV-3: elements without reserves/end_uses get null economic_reserves and empty uses (no crash)
  B2-INV-4: low-confidence entries are serialized with their confidence field

Invariants verified (B3 — price + events charts):
  B3-INV-1: Co JSON has 6 price points across 2 (basis, region) groups
  B3-INV-2: Co event dates appear in chronological order in the injected JSON
  B3-INV-3: Co prices are normalised to usd_per_kg (originally usd_per_lb in YAML)
  B3-INV-4: Og (no prices, no events) → empty arrays in JSON; charts_prices.js
             carries "No price history" and "No geopolitical events recorded" strings

Critical paths:
  - fresh run into tmpdir produces index.html + 9 per-element pages
  - every chart-placeholder div id is present in each per-element stub
  - Co renders reserves (11M econ, 25M resources) + 12 country bars + 4-slice donut
  - Am (no reserves, has end_uses) has null reserves + 3 low-confidence uses
  - charts_reserves.js is referenced in every element page
  - charts_prices.js is copied into assets dir during generation

Failure modes:
  - missing duckdb → clear error message, sys.exit non-zero
  - empty atlas_elements table → friendly error
"""

from __future__ import annotations

import json
import re

_json = json
_re = re
import subprocess
import sys
from pathlib import Path

import duckdb
import pytest

# Make scripts/ importable for the builders without packaging them.
_SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(_SCRIPTS_DIR))

import build_viewer  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REAL_DB = ROOT / "build" / "atlas-2025.duckdb"
FIXED_TS = "2025-01-01T00:00:00Z"

EXPECTED_SYMBOLS = ["He", "F", "Ne", "Co", "Ga", "Tc", "Nd", "Am", "Og"]
CHART_IDS = ["production-chart", "reserves-chart", "prices-chart", "sources-panel", "isotope-panel"]


# ─────────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def viewer_dir(tmp_path_factory):
    """Run the generator once into a tmpdir and return the output path."""
    out = tmp_path_factory.mktemp("viewer")
    build_viewer.generate_viewer(REAL_DB, out, timestamp=FIXED_TS)
    return out


# ─────────────────────────────────────────────────────────────────────────────
# INV-1: generator runs end-to-end without error
# ─────────────────────────────────────────────────────────────────────────────


def test_inv1_runs_without_error(viewer_dir):
    """The generator completed; if it raised, the fixture would have failed."""
    assert (viewer_dir / "index.html").exists()


# ─────────────────────────────────────────────────────────────────────────────
# INV-2: index.html links to every element page
# ─────────────────────────────────────────────────────────────────────────────


def test_inv2_index_links_all_elements(viewer_dir):
    index_text = (viewer_dir / "index.html").read_text()
    for sym in EXPECTED_SYMBOLS:
        assert f"elements/{sym}.html" in index_text, f"index.html missing link for {sym}"


# ─────────────────────────────────────────────────────────────────────────────
# INV-3: every {symbol}.html contains symbol and name
# ─────────────────────────────────────────────────────────────────────────────


def test_inv3_element_pages_contain_symbol_and_name(viewer_dir):
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT symbol, name FROM atlas_elements").fetchall()
    finally:
        con.close()

    for sym, name in rows:
        page = viewer_dir / "elements" / f"{sym}.html"
        assert page.exists(), f"missing page for {sym}"
        text = page.read_text()
        assert sym in text, f"{sym}.html missing symbol"
        assert name in text, f"{sym}.html missing name '{name}'"


# ─────────────────────────────────────────────────────────────────────────────
# INV-4: deterministic output with fixed timestamp
# ─────────────────────────────────────────────────────────────────────────────


def test_inv4_deterministic(tmp_path):
    out1 = tmp_path / "run1"
    out2 = tmp_path / "run2"
    build_viewer.generate_viewer(REAL_DB, out1, timestamp=FIXED_TS)
    build_viewer.generate_viewer(REAL_DB, out2, timestamp=FIXED_TS)

    for fname in ["index.html"] + [f"elements/{sym}.html" for sym in EXPECTED_SYMBOLS]:
        f1 = (out1 / fname).read_text()
        f2 = (out2 / fname).read_text()
        assert f1 == f2, f"{fname} differs between runs"


# ─────────────────────────────────────────────────────────────────────────────
# INV-5: Og (no commercial production) renders without errors
# ─────────────────────────────────────────────────────────────────────────────


def test_inv5_og_no_commercial_production(viewer_dir):
    og_text = (viewer_dir / "elements" / "Og.html").read_text()
    assert "No commercial production" in og_text
    # Should not be empty / crash; all placeholder divs must be present
    for div_id in CHART_IDS:
        assert f'id="{div_id}"' in og_text, f"Og.html missing #{div_id}"


# ─────────────────────────────────────────────────────────────────────────────
# Critical path: fresh run produces correct file set
# ─────────────────────────────────────────────────────────────────────────────


def test_fresh_run_file_set(viewer_dir):
    assert (viewer_dir / "index.html").exists()
    assert (viewer_dir / "assets" / "atlas.css").exists()
    for sym in EXPECTED_SYMBOLS:
        assert (viewer_dir / "elements" / f"{sym}.html").exists()


# ─────────────────────────────────────────────────────────────────────────────
# Critical path: every chart placeholder div id present in each element page
# ─────────────────────────────────────────────────────────────────────────────


def test_chart_placeholder_ids_present(viewer_dir):
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        for div_id in CHART_IDS:
            assert f'id="{div_id}"' in text, f"{sym}.html missing #{div_id}"


# ─────────────────────────────────────────────────────────────────────────────
# Failure mode: missing duckdb exits non-zero with a clear message
# ─────────────────────────────────────────────────────────────────────────────


def test_missing_db_exits_nonzero(tmp_path):
    result = subprocess.run(
        [sys.executable, str(_SCRIPTS_DIR / "build_viewer.py"), "--db", str(tmp_path / "nope.duckdb"), "--out", str(tmp_path / "out")],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "nope.duckdb" in result.stderr or "not found" in result.stderr


# ─────────────────────────────────────────────────────────────────────────────
# Failure mode: empty atlas_elements table exits non-zero with friendly message
# ─────────────────────────────────────────────────────────────────────────────


def test_empty_elements_table_exits_nonzero(tmp_path):
    empty_db = tmp_path / "empty.duckdb"
    con = duckdb.connect(str(empty_db))
    try:
        # Create the required tables but leave atlas_elements empty
        con.execute(
            "CREATE TABLE atlas_elements (symbol VARCHAR, atomic_number INTEGER, name VARCHAR, category VARCHAR, industrial_tier INTEGER, commercial_production BOOLEAN, narrative VARCHAR, us_critical_list_as_of_2025 BOOLEAN, eu_crm_list_as_of_2024 BOOLEAN, eu_strategic_list_as_of_2024 BOOLEAN, doe_short_term_criticality_rank DOUBLE, snapshot_year INTEGER)"
        )
        con.execute("CREATE TABLE atlas_criticality (symbol VARCHAR, flag_name VARCHAR, value BOOLEAN)")
        con.execute("CREATE TABLE atlas_sources (source_id VARCHAR, symbol VARCHAR, title VARCHAR, publisher VARCHAR, url VARCHAR)")
    finally:
        con.close()

    result = subprocess.run(
        [sys.executable, str(_SCRIPTS_DIR / "build_viewer.py"), "--db", str(empty_db), "--out", str(tmp_path / "out")],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "empty" in result.stderr.lower() or "error" in result.stderr.lower()


# ─────────────────────────────────────────────────────────────────────────────
# Verify d3 CDN script tag present
# ─────────────────────────────────────────────────────────────────────────────


def test_d3_cdn_in_pages(viewer_dir):
    index = (viewer_dir / "index.html").read_text()
    assert "d3js.org/d3.v7.min.js" in index

    for sym in EXPECTED_SYMBOLS:
        page = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "d3js.org/d3.v7.min.js" in page, f"{sym}.html missing d3 script"


# ─────────────────────────────────────────────────────────────────────────────
# B4-INV-1: Every source_id in atlas_sources appears in the element's sources panel
# ─────────────────────────────────────────────────────────────────────────────


def test_b4_inv1_all_sources_appear_in_panel(viewer_dir):
    """Every source_id stored in atlas_sources for an element must be present
    in that element's rendered sources panel."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT symbol, source_id FROM atlas_sources").fetchall()
    finally:
        con.close()

    for sym, source_id in rows:
        page = viewer_dir / "elements" / f"{sym}.html"
        assert page.exists(), f"missing page for {sym}"
        html = page.read_text()
        assert source_id in html, f"{sym}.html missing source_id={source_id!r} in sources panel"


# ─────────────────────────────────────────────────────────────────────────────
# B4-INV-2: CSS has distinct styles for all three tier badge classes
# ─────────────────────────────────────────────────────────────────────────────


def test_b4_inv2_distinct_tier_badge_styles(viewer_dir):
    """The generated CSS must contain distinct rules for primary, secondary, and
    tertiary tier badges. Without this, tiers would be visually indistinguishable."""
    css = (viewer_dir / "assets" / "atlas.css").read_text()
    assert "badge-tier-primary" in css, "CSS missing .badge-tier-primary"
    assert "badge-tier-secondary" in css, "CSS missing .badge-tier-secondary"
    assert "badge-tier-tertiary" in css, "CSS missing .badge-tier-tertiary"

    # Extract background colors — each tier must use a distinct CSS variable or color
    import re

    tier_rules: dict[str, str] = {}
    for tier in ("primary", "secondary", "tertiary"):
        pattern = rf"\.badge-tier-{tier}\s*\{{([^}}]+)\}}"
        m = re.search(pattern, css)
        assert m, f"CSS missing rule block for .badge-tier-{tier}"
        tier_rules[tier] = m.group(1)

    # The three blocks must not all have the same background declaration
    bg_values = set()
    for tier, rule_body in tier_rules.items():
        m = re.search(r"background\s*:\s*([^;]+)", rule_body)
        assert m, f".badge-tier-{tier} rule has no background declaration"
        bg_values.add(m.group(1).strip())

    assert len(bg_values) == 3, f"Tier badge backgrounds are not all distinct: {bg_values}"


# ─────────────────────────────────────────────────────────────────────────────
# B4-INV-3: referenced_by counts reconcile with actual fact-table row counts
# ─────────────────────────────────────────────────────────────────────────────


def test_b4_inv3_referenced_by_counts_reconcile():
    """Build sources data for Co and verify each referenced_by count matches
    what a direct DuckDB query would return for that (symbol, source_id) pair."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        sources = build_viewer._build_sources_data(con, "Co")

        # Tables: (category key, table name, source_id column)
        ref_tables = build_viewer._REF_TABLES

        for src in sources:
            sid = src["source_id"]
            claimed = src["referenced_by"]
            for cat, table, col in ref_tables:
                actual = con.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} = ? AND symbol = 'Co'", [sid]).fetchone()[0]
                claimed_count = claimed.get(cat, 0)
                assert claimed_count == actual, f"Co/{sid}: referenced_by[{cat!r}]={claimed_count} but actual row count in {table} is {actual}"
    finally:
        con.close()


# ─────────────────────────────────────────────────────────────────────────────
# B4-INV-4: superseded_by warning renders when set
# ─────────────────────────────────────────────────────────────────────────────


def _make_superseded_db(tmp_path: Path) -> Path:
    """Create a minimal DuckDB with two sources where one supersedes the other."""
    db_path = tmp_path / "superseded.duckdb"
    con = duckdb.connect(str(db_path))
    try:
        # Copy schema tables from real DB so the generator can run
        real = duckdb.connect(str(REAL_DB), read_only=True)
        tables = [row[0] for row in real.execute("SHOW TABLES").fetchall()]
        for t in tables:
            df = real.execute(f"SELECT * FROM {t} WHERE symbol = 'Co'").df()
            # Ensure superseded_by stays as VARCHAR (pandas/duckdb would infer INTEGER for all-NULL object cols)
            if "superseded_by" in df.columns:
                df["superseded_by"] = df["superseded_by"].astype("string")
            con.register("_tmp_df", df)
            con.execute(f"CREATE TABLE {t} AS SELECT * FROM _tmp_df")
            con.unregister("_tmp_df")
        real.close()

        # Inject a superseded source row (superseded_by points to existing usgs source)
        con.execute(
            """
            INSERT INTO atlas_sources
              (source_id, symbol, snapshot_year, title, publisher, url, retrieved, publication_year, superseded_by, source_tier)
            VALUES
              ('old_source_co', 'Co', 2025, 'Old Co Report', 'USGS', NULL, '2024-01-01', 2024, 'usgs_mcs_2025_cobalt', 'secondary')
            """
        )
    finally:
        con.close()
    return db_path


def test_b4_inv4_superseded_by_warning_renders(tmp_path):
    """A source with superseded_by != NULL must render a visible warning in the HTML."""
    db_path = _make_superseded_db(tmp_path)
    out_dir = tmp_path / "viewer_superseded"
    build_viewer.generate_viewer(db_path, out_dir, timestamp=FIXED_TS)

    co_html = (out_dir / "elements" / "Co.html").read_text()
    # The superseded source id must appear in the warning
    assert "old_source_co" in co_html, "superseded source_id missing from page"
    # The warning must reference what supersedes it
    assert "usgs_mcs_2025_cobalt" in co_html, "superseded_by target id missing from warning"
    # The explicit warning text must be rendered (from source-card-superseded class)
    assert "superseded by" in co_html, "No 'superseded by' warning text rendered"


# ─────────────────────────────────────────────────────────────────────────────
# Helpers for B2 tests
# ─────────────────────────────────────────────────────────────────────────────


def _extract_reserves_json(html: str) -> dict:
    """Extract and parse the inline reserves-data JSON from an element page."""
    m = re.search(r'<script id="reserves-data" type="application/json">(.*?)</script>', html)
    assert m, "reserves-data script tag not found in page"
    return json.loads(m.group(1))


# ─────────────────────────────────────────────────────────────────────────────
# B2-INV-1: elements with reserves get a non-empty reserves_by_country list
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_inv1_elements_with_reserves_have_country_bars(viewer_dir):
    """Symbols with atlas_reserves rows must have non-empty reserves_by_country in their JSON."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT DISTINCT symbol FROM atlas_shares WHERE share_type='reserves'").fetchall()
        symbols_with_reserve_shares = {r[0] for r in rows}
    finally:
        con.close()

    for sym in symbols_with_reserve_shares:
        page = (viewer_dir / "elements" / f"{sym}.html").read_text()
        d = _extract_reserves_json(page)
        assert len(d["reserves_by_country"]) > 0, f"{sym}: has reserve shares but reserves_by_country is empty"


# ─────────────────────────────────────────────────────────────────────────────
# B2-INV-2: elements with end_uses get a non-empty uses list
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_inv2_elements_with_end_uses_have_donut_data(viewer_dir):
    """Symbols with atlas_end_uses rows must have non-empty uses list in their JSON."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT DISTINCT symbol FROM atlas_end_uses").fetchall()
        symbols_with_uses = {r[0] for r in rows}
    finally:
        con.close()

    for sym in symbols_with_uses:
        page = (viewer_dir / "elements" / f"{sym}.html").read_text()
        d = _extract_reserves_json(page)
        assert len(d["end_uses"]["uses"]) > 0, f"{sym}: has end_uses rows but uses list is empty"


# ─────────────────────────────────────────────────────────────────────────────
# B2-INV-3: elements without data get null/empty, not a crash
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_inv3_missing_data_renders_empty_state(viewer_dir):
    """Og and Tc have no reserves and Og has no end_uses — pages must not crash."""
    # Og: no reserves, no end_uses
    og = (viewer_dir / "elements" / "Og.html").read_text()
    d_og = _extract_reserves_json(og)
    assert d_og["reserves"]["economic_reserves"] is None, "Og should have null economic_reserves"
    assert d_og["reserves_by_country"] == [], "Og should have empty reserves_by_country"
    assert d_og["end_uses"]["uses"] == [], "Og should have empty end_uses"
    # Page must still have the reserves-chart div
    assert 'id="reserves-chart"' in og, "Og.html missing #reserves-chart div"


# ─────────────────────────────────────────────────────────────────────────────
# B2-INV-4: low-confidence entries carry the confidence field
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_inv4_low_confidence_entries_serialized(viewer_dir):
    """Am has low-confidence end_uses — confidence must be in the JSON payload."""
    am = (viewer_dir / "elements" / "Am.html").read_text()
    d = _extract_reserves_json(am)
    assert len(d["end_uses"]["uses"]) > 0, "Am should have end_uses"
    for use in d["end_uses"]["uses"]:
        assert "confidence" in use, f"Am end_use missing confidence field: {use}"
        assert use["confidence"] == "low", f"Am end_use expected low confidence, got: {use['confidence']}"


# ─────────────────────────────────────────────────────────────────────────────
# B2 critical path: Co renders correct reserves + end-uses data
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_co_reserves_and_end_uses(viewer_dir):
    """Co critical path: 11M economic, 25M resources, country bars, 4-slice donut."""
    co = (viewer_dir / "elements" / "Co.html").read_text()
    d = _extract_reserves_json(co)

    # Reserves summary
    assert d["reserves"]["economic_reserves"] == 11_000_000.0, "Co economic_reserves should be 11M"
    assert d["reserves"]["resources"] == 25_000_000.0, "Co resources should be 25M"
    assert d["reserves"]["unit"] == "tonnes", f"Co unit: {d['reserves']['unit']}"

    # Country bars: CD is the dominant producer
    assert len(d["reserves_by_country"]) >= 4, "Co should have at least 4 country entries"
    cd = next((c for c in d["reserves_by_country"] if c["country"] == "CD"), None)
    assert cd is not None, "Co missing CD (DRC) in reserves_by_country"
    assert cd["share_pct"] == 55.0, f"Co CD share should be 55%, got {cd['share_pct']}"

    # End uses: 4 slices
    assert len(d["end_uses"]["uses"]) == 4, f"Co should have 4 end_uses, got {len(d['end_uses']['uses'])}"
    assert d["end_uses"]["completeness"] == "complete", "Co end_uses should be complete"
    # All Co uses are high confidence
    for use in d["end_uses"]["uses"]:
        assert use["confidence"] == "high", f"Co use {use['application']} should be high confidence"


# ─────────────────────────────────────────────────────────────────────────────
# B2 critical path: Am has no reserves but populated donut
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_am_no_reserves_with_end_uses(viewer_dir):
    """Am critical path: null reserves, empty country bars, 3-entry low-confidence donut."""
    am = (viewer_dir / "elements" / "Am.html").read_text()
    d = _extract_reserves_json(am)

    # No reserves
    assert d["reserves"]["economic_reserves"] is None, "Am should have no economic_reserves"
    assert d["reserves"]["resources"] is None, "Am should have no resources"
    assert d["reserves_by_country"] == [], "Am should have no country reserve shares"

    # End uses populated
    assert len(d["end_uses"]["uses"]) == 3, f"Am should have 3 end_uses, got {len(d['end_uses']['uses'])}"
    # All are low confidence
    for use in d["end_uses"]["uses"]:
        assert use["confidence"] == "low", f"Am use {use['application']} should be low confidence"


# ─────────────────────────────────────────────────────────────────────────────
# B2: charts_reserves.js referenced in every element page
# ─────────────────────────────────────────────────────────────────────────────


def test_b2_charts_reserves_js_in_pages(viewer_dir):
    """Every element page must reference charts_reserves.js for the chart code."""
    for sym in EXPECTED_SYMBOLS:
        page = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "charts_reserves.js" in page, f"{sym}.html missing charts_reserves.js reference"


# =============================================================================
# B3 — Price chart + events timeline tests
# =============================================================================


def _extract_chart_data(html_text: str) -> dict:
    """Parse the inline atlas-chart-data JSON from an element page."""
    m = _re.search(r'id="atlas-chart-data">(.*?)</script>', html_text, _re.DOTALL)
    assert m, "atlas-chart-data script block not found in page"
    return _json.loads(m.group(1))


# ─────────────────────────────────────────────────────────────────────────────
# B3-INV-1: Co has 6 price points across 2 (basis, region) groups
# ─────────────────────────────────────────────────────────────────────────────


def test_b3_inv1_co_price_points_and_groups(viewer_dir):
    """Co has exactly 6 price records across 2 distinct (basis, region) series."""
    text = (viewer_dir / "elements" / "Co.html").read_text()
    data = _extract_chart_data(text)

    prices = data["prices"]
    assert len(prices) == 6, f"Expected 6 Co price points, got {len(prices)}"

    groups = {(p["basis"], p["region"]) for p in prices}
    # Current data has us_domestic/US (2020-2024) and lme/global (2024)
    assert len(groups) == 2, f"Expected 2 (basis, region) groups for Co, got {sorted(groups)}"
    assert ("us_domestic", "US") in groups
    assert ("lme", "global") in groups


# ─────────────────────────────────────────────────────────────────────────────
# B3-INV-2: Events appear in chronological order
# ─────────────────────────────────────────────────────────────────────────────


def test_b3_inv2_events_chronological_order(viewer_dir):
    """Co events must be sorted from earliest to latest date in the injected JSON."""
    text = (viewer_dir / "elements" / "Co.html").read_text()
    data = _extract_chart_data(text)

    events = data["events"]
    assert len(events) >= 2, "Co must have at least 2 events to test ordering"
    dates = [e["date"] for e in events]
    assert dates == sorted(dates), f"Co events not in chronological order: {dates}"

    # Verify the specific known ordering for Co
    assert dates[0] == "2024-01"
    assert dates[-1] == "2025-02"


# ─────────────────────────────────────────────────────────────────────────────
# B3-INV-3: Co prices normalised to usd_per_kg (no usd_per_lb in injected data)
# ─────────────────────────────────────────────────────────────────────────────


def test_b3_inv3_co_prices_normalised_to_kg(viewer_dir):
    """Co is priced in usd_per_lb in the YAML; the generator must convert to usd_per_kg."""
    text = (viewer_dir / "elements" / "Co.html").read_text()
    data = _extract_chart_data(text)

    prices = data["prices"]
    assert prices, "Co price list must not be empty"
    for p in prices:
        assert p["unit"] == "usd_per_kg", f"Expected usd_per_kg but got {p['unit']!r} for {p}"


def test_b3_inv3_normalise_unit_helper():
    """_normalize_price_units converts usd_per_lb values and leaves other units intact."""
    raw = [
        {"year": 2024, "value": 17.0, "unit": "usd_per_lb", "form": "metal", "basis": "x", "region": "US"},
        {"year": 2024, "value": 500.0, "unit": "usd_per_kg", "form": "metal", "basis": "y", "region": "US"},
        {"year": 2023, "value": 14.0, "unit": "usd_per_m3", "form": "gas", "basis": "z", "region": "US"},
    ]
    normalised = build_viewer._normalize_price_units(raw)

    assert normalised[0]["unit"] == "usd_per_kg"
    # 17 / 0.4536 ≈ 37.478
    assert abs(normalised[0]["value"] - 17.0 / 0.4536) < 0.01
    assert normalised[1]["unit"] == "usd_per_kg"  # already correct, untouched
    assert normalised[1]["value"] == 500.0
    assert normalised[2]["unit"] == "usd_per_m3"  # non-lb unit untouched
    assert normalised[2]["value"] == 14.0


# ─────────────────────────────────────────────────────────────────────────────
# B3-INV-4: empty states — Og has no prices/events; JS strings verified in asset
# ─────────────────────────────────────────────────────────────────────────────


def test_b3_inv4_og_empty_prices_and_events(viewer_dir):
    """Og has no YAML prices or events; injected JSON must have empty arrays."""
    text = (viewer_dir / "elements" / "Og.html").read_text()
    data = _extract_chart_data(text)
    assert data["prices"] == [], f"Og prices should be empty, got {data['prices']}"
    assert data["events"] == [], f"Og events should be empty, got {data['events']}"


def test_b3_inv4_empty_state_strings_in_js(viewer_dir):
    """charts_prices.js must contain the empty-state messages used when data is absent."""
    js_text = (viewer_dir / "assets" / "charts_prices.js").read_text()
    assert "No price history" in js_text
    assert "No geopolitical events recorded" in js_text


# ─────────────────────────────────────────────────────────────────────────────
# B3: charts_prices.js present in assets and referenced by element pages
# ─────────────────────────────────────────────────────────────────────────────


def test_b3_charts_prices_js_deployed(viewer_dir):
    """charts_prices.js must be written into assets/ during generation."""
    assert (viewer_dir / "assets" / "charts_prices.js").exists()


def test_b3_charts_prices_js_referenced_in_element_pages(viewer_dir):
    """Every element page must reference charts_prices.js."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "charts_prices.js" in text, f"{sym}.html missing charts_prices.js reference"


def test_b3_atlas_chart_data_present_in_all_element_pages(viewer_dir):
    """Every element page must have an atlas-chart-data script block."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert 'id="atlas-chart-data"' in text, f"{sym}.html missing atlas-chart-data block"

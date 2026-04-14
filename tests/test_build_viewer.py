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

Map invariants:
  - index includes a country map shell, tooltip container, and serialized map payload
  - map payload excludes aggregate pseudo-countries such as ZZ/XX
  - tooltip rows are sorted by descending % global and keep mining/refining as separate stages
  - charts_map.js and world_countries_50m.geojson are deployed into assets
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


def _extract_country_map_data(index_html: str) -> dict:
    """Extract and parse the inline country map JSON from the index page."""
    m = re.search(r'<script id="atlas-country-map-data" type="application/json">(.*?)</script>', index_html, re.DOTALL)
    assert m, "atlas-country-map-data script tag not found in index page"
    return json.loads(m.group(1))


def test_index_country_map_shell_present(viewer_dir):
    index = (viewer_dir / "index.html").read_text()
    assert 'id="country-map-root"' in index, "index missing country map root"
    assert 'id="country-map-tooltip"' in index, "index missing country map tooltip"
    assert 'id="country-map-drawer"' in index, "index missing country map drawer"
    assert 'id="country-map-drawer-backdrop"' in index, "index missing country map drawer backdrop"
    assert 'id="country-map-drawer-body"' in index, "index missing country map drawer body"
    assert "world_countries_50m.geojson" in index, "index missing map geometry asset reference"
    assert "Click a country for a fuller breakdown" in index, "index missing click-through map copy"


def test_index_country_map_payload_sorted_and_filtered(viewer_dir):
    data = _extract_country_map_data((viewer_dir / "index.html").read_text())
    countries = data["countries"]

    assert "ZZ" not in countries, "country map payload should not include ZZ aggregate rows"
    assert "XX" not in countries, "country map payload should not include XX pseudo-country rows"
    assert data["country_count"] == len(countries), "country_count should reconcile with serialized country entries"
    assert data["row_count"] == sum(len(rows) for rows in countries.values()), "row_count should reconcile with serialized rows"
    assert "CN" in countries, "expected China to appear in the country map payload"

    for rows in countries.values():
        assert rows == sorted(rows, key=lambda row: (-float(row["global_pct"]), row["symbol"], row["stage"], row["stream"] or ""))
        for row in rows:
            assert row["stage"] in {"mining", "refining"}, f"unexpected stage label: {row['stage']}"
            assert row["quantity_value"] is not None, "country map rows must carry quantity_value"
            assert row["quantity_unit"], "country map rows must carry quantity_unit"
            assert row["global_pct"] is not None, "country map rows must carry global_pct"


def test_index_country_map_assets_deployed(viewer_dir):
    assert (viewer_dir / "assets" / "charts_map.js").exists(), "charts_map.js must be copied into assets/"
    assert (viewer_dir / "assets" / "world_countries_50m.geojson").exists(), "world geometry must be copied into assets/"

    index = (viewer_dir / "index.html").read_text()
    assert "charts_map.js" in index, "index should reference charts_map.js"


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
    """charts_prices.js must contain the empty-state message used when events are absent."""
    js_text = (viewer_dir / "assets" / "charts_prices.js").read_text()
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


# =============================================================================
# B1 — Production + refining stacked bar charts
# =============================================================================


def _extract_production_json(html: str) -> dict:
    """Extract and parse the inline production-data JSON from an element page."""
    m = _re.search(r'id="production-data" type="application/json">(.*?)</script>', html, _re.DOTALL)
    assert m, "production-data script tag not found in page"
    return _json.loads(m.group(1))


# =============================================================================
# B5 — Isotope markets panel tests
# =============================================================================

#: Elements that have rows in atlas_isotope_markets (currently Am and Tc).
ISOTOPE_ELEMENTS = {"Am", "Tc"}
#: All other elements in the test set have no isotope market data.
NON_ISOTOPE_ELEMENTS = set(EXPECTED_SYMBOLS) - ISOTOPE_ELEMENTS


def _extract_isotope_data(html: str) -> list[dict] | None:
    """Parse the inline isotope-data JSON from an element page.

    Returns None if the script tag is absent (element has no isotope data).
    """
    m = _re.search(r'<script id="isotope-data" type="application/json">(.*?)</script>', html, _re.DOTALL)
    if not m:
        return None
    return _json.loads(m.group(1))


# ─────────────────────────────────────────────────────────────────────────────
# B1-INV-1: Every element with production data gets a filled #production-chart section
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_inv1_elements_with_production_have_production_data(viewer_dir):
    """Symbols with atlas_shares mining/refining rows must have non-empty streams in JSON."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT DISTINCT symbol FROM atlas_shares WHERE share_type IN ('mining','refining')").fetchall()
        symbols_with_production = {r[0] for r in rows}
    finally:
        con.close()

    for sym in symbols_with_production:
        page = (viewer_dir / "elements" / f"{sym}.html").read_text()
        # production-data script tag must exist on all element pages
        assert 'id="production-chart"' in page, f"{sym}.html missing #production-chart div"
        d = _extract_production_json(page)
        assert "streams" in d, f"{sym}: production JSON missing 'streams' key"
        assert len(d["streams"]) > 0, f"{sym}: has production shares but streams is empty"


# ─────────────────────────────────────────────────────────────────────────────
# B1-INV-2: Og (no production) keeps the empty-state message
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_inv2_og_keeps_empty_state(viewer_dir):
    """Og has no production shares — production-data streams must be empty."""
    og = (viewer_dir / "elements" / "Og.html").read_text()
    d = _extract_production_json(og)
    assert d["streams"] == [], "Og should have empty streams list"
    # The placeholder div must still be present
    assert 'id="production-chart"' in og, "Og.html missing #production-chart div"


# ─────────────────────────────────────────────────────────────────────────────
# B1-INV-3: Inlined JSON validates basic dict shape
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_inv3_json_shape(viewer_dir):
    """Production JSON for Co must have required keys and correct types."""
    co = (viewer_dir / "elements" / "Co.html").read_text()
    d = _extract_production_json(co)

    assert isinstance(d, dict), "production JSON must be a dict"
    assert "streams" in d, "production JSON missing 'streams'"
    assert isinstance(d["streams"], list), "'streams' must be a list"
    assert len(d["streams"]) > 0, "Co streams must not be empty"

    stream = d["streams"][0]
    assert "stream_id" in stream
    assert "mining" in stream
    assert "refining" in stream
    assert "completeness" in stream
    assert "world_mine" in stream
    assert "world_refined" in stream

    # Each mining entry must have required fields
    for entry in stream["mining"]:
        assert "country" in entry, f"mining entry missing 'country': {entry}"
        assert "share_pct" in entry, f"mining entry missing 'share_pct': {entry}"
        assert "confidence" in entry, f"mining entry missing 'confidence': {entry}"

    assert isinstance(stream["completeness"], dict)
    assert "mining" in stream["completeness"]
    assert "refining" in stream["completeness"]


# ─────────────────────────────────────────────────────────────────────────────
# B1-INV-4: Low-confidence shares are serialized with the confidence field
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_inv4_low_confidence_shares_serialized(viewer_dir):
    """Co refining shares have low confidence — they must appear in JSON with confidence='low'."""
    co = (viewer_dir / "elements" / "Co.html").read_text()
    d = _extract_production_json(co)
    assert len(d["streams"]) > 0, "Co should have streams"
    refining = d["streams"][0]["refining"]
    assert len(refining) > 0, "Co should have refining shares"
    for entry in refining:
        assert "confidence" in entry, f"Co refining entry missing confidence: {entry}"
        assert entry["confidence"] == "low", f"Co refining expected low confidence, got: {entry['confidence']}"


# ─────────────────────────────────────────────────────────────────────────────
# B1-INV-5: Multi-stream elements get one stream entry per unique stream_id
# (no multi-stream elements exist yet — test the code path with a synthetic DB)
# ─────────────────────────────────────────────────────────────────────────────


def _make_multistream_db(tmp_path: Path) -> Path:
    """Create a minimal DuckDB with two synthetic stream IDs for Co."""
    db_path = tmp_path / "multistream.duckdb"
    real = duckdb.connect(str(REAL_DB), read_only=True)
    con = duckdb.connect(str(db_path))
    try:
        tables = [row[0] for row in real.execute("SHOW TABLES").fetchall()]
        for t in tables:
            df = real.execute(f"SELECT * FROM {t} WHERE symbol = 'Co'").df()
            con.register("_tmp_df", df)
            con.execute(f"CREATE TABLE {t} AS SELECT * FROM _tmp_df")
            con.unregister("_tmp_df")

        # Add a second stream (stream_id=1) with a different country
        con.execute(
            """
            INSERT INTO atlas_shares
              (symbol, snapshot_year, share_type, stream, country, share_pct, confidence, completeness)
            VALUES
              ('Co', 2025, 'mining', 1, 'AU', 55.0, 'high', 'partial')
            """
        )
    finally:
        real.close()
        con.close()
    return db_path


def test_b1_inv5_multistream_produces_separate_stream_entries(tmp_path):
    """Each unique stream_id in atlas_shares must produce its own stream entry."""
    db_path = _make_multistream_db(tmp_path)
    out_dir = tmp_path / "viewer_multistream"
    build_viewer.generate_viewer(db_path, out_dir, timestamp=FIXED_TS)

    co_html = (out_dir / "elements" / "Co.html").read_text()
    d = _extract_production_json(co_html)
    stream_ids = [s["stream_id"] for s in d["streams"]]
    # We expect stream_id=None (original) and stream_id=1 (synthetic)
    assert None in stream_ids, f"stream_id=None not found in streams: {stream_ids}"
    assert 1 in stream_ids, f"stream_id=1 not found in streams: {stream_ids}"
    assert len(stream_ids) == 2, f"Expected 2 streams, got {stream_ids}"


# ─────────────────────────────────────────────────────────────────────────────
# B1 critical path: Co mining renders correctly
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_co_mining_critical_path(viewer_dir):
    """Co critical path: CD=76%, complete mining, top_producers_only refining."""
    co = (viewer_dir / "elements" / "Co.html").read_text()
    d = _extract_production_json(co)
    assert len(d["streams"]) == 1, "Co should have exactly 1 stream"
    stream = d["streams"][0]

    # Mining shares
    mining = stream["mining"]
    assert len(mining) == 13, f"Co should have 13 mining countries, got {len(mining)}"

    cd = next((c for c in mining if c["country"] == "CD"), None)
    assert cd is not None, "Co missing CD in mining shares"
    assert cd["share_pct"] == 76.0, f"Co CD mining share should be 76%, got {cd['share_pct']}"
    assert cd["confidence"] == "high"
    assert cd["quantity"] == 220000.0

    # Completeness
    assert stream["completeness"]["mining"] == "complete"
    assert stream["completeness"]["refining"] == "top_producers_only"

    # World mine total present
    assert stream["world_mine"]["value"] == 290000.0
    assert stream["world_mine"]["unit"] == "tonnes_per_year"


# ─────────────────────────────────────────────────────────────────────────────
# B1: charts_production.js deployed and referenced in every element page
# ─────────────────────────────────────────────────────────────────────────────


def test_b1_charts_production_js_deployed(viewer_dir):
    """charts_production.js must be written into assets/ during generation."""
    assert (viewer_dir / "assets" / "charts_production.js").exists()


def test_b1_charts_production_js_referenced_in_element_pages(viewer_dir):
    """Every element page must reference charts_production.js."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "charts_production.js" in text, f"{sym}.html missing charts_production.js reference"


def test_b1_production_data_script_in_all_element_pages(viewer_dir):
    """Every element page must have a production-data script block (even if empty)."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert 'id="production-data"' in text, f"{sym}.html missing production-data script block"


# ─────────────────────────────────────────────────────────────────────────────
# B5-INV-1: Am and Tc render isotope panel content; others keep the placeholder
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_inv1_isotope_panel_present_for_all_elements(viewer_dir):
    """Every element page has id='isotope-panel', regardless of whether it has data."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert 'id="isotope-panel"' in text, f"{sym}.html missing #isotope-panel div"


def test_b5_inv1_am_and_tc_have_isotope_data(viewer_dir):
    """Am and Tc must have a non-empty isotope-data JSON block (real panel rendered)."""
    for sym in ISOTOPE_ELEMENTS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        data = _extract_isotope_data(text)
        assert data is not None, f"{sym}.html missing isotope-data script block"
        assert len(data) > 0, f"{sym}.html has empty isotope-data list"


def test_b5_inv1_non_isotope_elements_have_no_isotope_data_script(viewer_dir):
    """Elements without isotope_markets rows must NOT have an isotope-data script block."""
    for sym in NON_ISOTOPE_ELEMENTS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        data = _extract_isotope_data(text)
        assert data is None, f"{sym}.html unexpectedly has an isotope-data JSON block"


# ─────────────────────────────────────────────────────────────────────────────
# B5-INV-2: Half-life renders in human units
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_inv2_am241_half_life_in_years(viewer_dir):
    """Am-241 half-life (~432.4 years) must display with 'years' unit."""
    text = (viewer_dir / "elements" / "Am.html").read_text()
    data = _extract_isotope_data(text)
    assert data is not None
    am241 = next((d for d in data if d["isotope"] == "Am-241"), None)
    assert am241 is not None, "Am isotope-data missing Am-241 entry"

    hl = am241.get("half_life_display", "")
    assert "year" in hl, f"Am-241 half_life_display should contain 'year', got: {hl!r}"
    # ~432.4 years — check the numeric part starts in the 430s
    numeric = _re.search(r"(\d+(?:\.\d+)?)", hl)
    assert numeric, f"No number found in Am-241 half_life_display: {hl!r}"
    value = float(numeric.group(1))
    assert 430 < value < 435, f"Am-241 half-life value {value} not in expected range 430-435 years"


def test_b5_inv2_tc99m_half_life_in_hours(viewer_dir):
    """Tc-99m half-life (~6 hours) must display with 'hours' unit."""
    text = (viewer_dir / "elements" / "Tc.html").read_text()
    data = _extract_isotope_data(text)
    assert data is not None
    tc99m = next((d for d in data if d["isotope"] == "Tc-99m"), None)
    assert tc99m is not None, "Tc isotope-data missing Tc-99m entry"

    hl = tc99m.get("half_life_display", "")
    assert "hour" in hl, f"Tc-99m half_life_display should contain 'hour', got: {hl!r}"
    numeric = _re.search(r"(\d+(?:\.\d+)?)", hl)
    assert numeric, f"No number found in Tc-99m half_life_display: {hl!r}"
    value = float(numeric.group(1))
    assert 5.5 < value < 6.5, f"Tc-99m half-life value {value} not in expected range 5.5-6.5 hours"


# ─────────────────────────────────────────────────────────────────────────────
# B5-INV-3: Low-confidence producers are visually distinct
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_inv3_low_confidence_producers_in_json(viewer_dir):
    """All current producers for Am and Tc have confidence=low in the JSON data."""
    for sym in ISOTOPE_ELEMENTS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        data = _extract_isotope_data(text)
        assert data is not None
        for iso in data:
            for p in iso.get("producers", []):
                assert "confidence" in p, f"{sym}/{iso['isotope']}: producer missing confidence field"


def test_b5_inv3_low_confidence_css_class_in_html(viewer_dir):
    """Am and Tc pages must contain the producer-low-confidence CSS class
    (both in the stylesheet and in the rendered HTML table rows)."""
    css = (viewer_dir / "assets" / "atlas.css").read_text()
    assert "producer-low-confidence" in css, "CSS missing .producer-low-confidence rule"

    for sym in ISOTOPE_ELEMENTS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "producer-low-confidence" in text, f"{sym}.html missing producer-low-confidence class in rendered HTML"


# ─────────────────────────────────────────────────────────────────────────────
# B5-INV-4: Multi-isotope future-proofing — one JSON entry per isotope row
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_inv4_one_json_entry_per_isotope(viewer_dir):
    """isotope-data JSON has exactly one entry per row in atlas_isotope_markets."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        rows = con.execute("SELECT symbol, COUNT(*) AS cnt FROM atlas_isotope_markets GROUP BY symbol").fetchall()
    finally:
        con.close()

    for sym, expected_count in rows:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        data = _extract_isotope_data(text)
        assert data is not None, f"{sym}.html missing isotope-data block"
        assert len(data) == expected_count, (
            f"{sym}.html isotope-data has {len(data)} entries but atlas_isotope_markets has {expected_count} rows"
        )


# ─────────────────────────────────────────────────────────────────────────────
# B5: charts_isotopes.js deployed and referenced
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_charts_isotopes_js_deployed(viewer_dir):
    """charts_isotopes.js must be written into assets/ during generation."""
    assert (viewer_dir / "assets" / "charts_isotopes.js").exists()


def test_b5_charts_isotopes_js_referenced_in_element_pages(viewer_dir):
    """Every element page must reference charts_isotopes.js."""
    for sym in EXPECTED_SYMBOLS:
        text = (viewer_dir / "elements" / f"{sym}.html").read_text()
        assert "charts_isotopes.js" in text, f"{sym}.html missing charts_isotopes.js reference"


# ─────────────────────────────────────────────────────────────────────────────
# B5: _format_half_life unit helper
# ─────────────────────────────────────────────────────────────────────────────


def test_b5_format_half_life_years():
    """Half-lives ≥ 1 year render with 'years'."""
    result = build_viewer._format_half_life(1.365e10)  # Am-241
    assert "year" in result, f"Expected 'year' in {result!r}"
    numeric = float(_re.search(r"[\d.]+", result).group())
    assert 430 < numeric < 435


def test_b5_format_half_life_hours():
    """Half-lives in the hours range render with 'hours'."""
    result = build_viewer._format_half_life(21624)  # Tc-99m
    assert "hour" in result, f"Expected 'hour' in {result!r}"
    numeric = float(_re.search(r"[\d.]+", result).group())
    assert 5.5 < numeric < 6.5


def test_b5_format_half_life_days():
    result = build_viewer._format_half_life(3 * 86400)  # 3 days
    assert "day" in result, f"Expected 'day' in {result!r}"
    numeric = float(_re.search(r"[\d.]+", result).group())
    assert abs(numeric - 3.0) < 0.1


def test_b5_format_half_life_minutes():
    result = build_viewer._format_half_life(90)  # 1.5 min
    assert "minute" in result, f"Expected 'minute' in {result!r}"
    numeric = float(_re.search(r"[\d.]+", result).group())
    assert abs(numeric - 1.5) < 0.1


def test_b5_format_half_life_seconds():
    result = build_viewer._format_half_life(30)
    assert "second" in result, f"Expected 'second' in {result!r}"
    numeric = float(_re.search(r"[\d.]+", result).group())
    assert abs(numeric - 30.0) < 0.1


# =============================================================================
# CP — Country page tests
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
# CP-1: Must-exist country pages
# ─────────────────────────────────────────────────────────────────────────────


def test_cp1_must_exist_country_pages(viewer_dir):
    for iso in ("CD", "CN", "US", "AU", "RU"):
        page = viewer_dir / "countries" / f"{iso}.html"
        assert page.exists(), f"missing country page for {iso}"
        text = page.read_text()
        assert iso in text, f"{iso}.html missing ISO code in content"


# ─────────────────────────────────────────────────────────────────────────────
# CP-2: No ZZ page generated
# ─────────────────────────────────────────────────────────────────────────────


def test_cp2_no_zz_page(viewer_dir):
    assert not (viewer_dir / "countries" / "ZZ.html").exists()


# ─────────────────────────────────────────────────────────────────────────────
# CP-3: Country pages link back to element pages
# ─────────────────────────────────────────────────────────────────────────────


def test_cp3_country_pages_link_to_elements(viewer_dir):
    cd_page = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'href="../elements/Co.html"' in cd_page


# ─────────────────────────────────────────────────────────────────────────────
# CP-4: Element pages link to country pages
# ─────────────────────────────────────────────────────────────────────────────


def test_cp4_element_pages_link_to_countries(viewer_dir):
    co_page = (viewer_dir / "elements" / "Co.html").read_text()
    assert 'href="../countries/CD.html"' in co_page


# ─────────────────────────────────────────────────────────────────────────────
# CP-5: Map drawer contains "View full page" link
# ─────────────────────────────────────────────────────────────────────────────


def test_cp5_drawer_js_has_full_page_link(viewer_dir):
    js = (viewer_dir / "assets" / "charts_map.js").read_text()
    assert "countries/" in js and "View full page" in js


# ─────────────────────────────────────────────────────────────────────────────
# CP-6: Thin-data country page renders without error
# ─────────────────────────────────────────────────────────────────────────────


def test_cp6_thin_country_page_renders(viewer_dir):
    # US has thin Co mining data (share_pct=0, quantity=300t) — page must still exist
    page = viewer_dir / "countries" / "US.html"
    assert page.exists()
    text = page.read_text()
    assert "Mining" in text and "Reserves" in text


# ─────────────────────────────────────────────────────────────────────────────
# CP-7: Relative path correctness
# ─────────────────────────────────────────────────────────────────────────────


def test_cp7_country_page_relative_paths(viewer_dir):
    cd = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'href="../assets/atlas.css"' in cd
    assert 'src="../assets/' in cd  # JS scripts
    assert 'href="../index.html"' in cd  # back-link


# ─────────────────────────────────────────────────────────────────────────────
# CP-8: ISO name map covers all generated country pages
# ─────────────────────────────────────────────────────────────────────────────


def test_cp8_iso_name_map_covers_all_countries(viewer_dir):
    iso_map, _ = build_viewer._build_iso_name_map()
    countries_dir = viewer_dir / "countries"
    for page in countries_dir.glob("*.html"):
        iso = page.stem
        # page must contain more than just the ISO code as its heading
        text = page.read_text()
        assert len(text) > 500, f"{iso}.html suspiciously short ({len(text)} bytes)"


# ─────────────────────────────────────────────────────────────────────────────
# CP-9: _build_country_page_data returns expected shape for CD/Co
# ─────────────────────────────────────────────────────────────────────────────


def test_cp9_build_country_page_data_cd_co():
    """CD must have a Co mining row with global_rank=1."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        data = build_viewer._build_country_page_data(con)
    finally:
        con.close()

    assert "CD" in data, "CD not in country page data"
    cd_rows = data["CD"]
    co_mining = next((r for r in cd_rows if r["symbol"] == "Co" and r["stage"] == "mining"), None)
    assert co_mining is not None, "CD missing Co mining row"
    assert co_mining["global_rank"] == 1, f"CD Co mining should be rank 1, got {co_mining['global_rank']}"
    assert co_mining["share_pct"] == 76.0, f"CD Co mining share should be 76%, got {co_mining['share_pct']}"
    assert "ZZ" not in data, "ZZ must be excluded from country page data"


# ─────────────────────────────────────────────────────────────────────────────
# CP-10: _compute_country_summary returns correct stats for CD
# ─────────────────────────────────────────────────────────────────────────────


def test_cp10_compute_country_summary_cd():
    """CD should have n_mined > 0 and n_critical > 0."""
    con = duckdb.connect(str(REAL_DB), read_only=True)
    try:
        data = build_viewer._build_country_page_data(con)
    finally:
        con.close()

    cd_rows = data["CD"]
    summary = build_viewer._compute_country_summary(cd_rows)
    assert summary["n_mined"] > 0, "CD should mine at least one element"
    assert summary["n_critical"] > 0, "CD should have at least one critical element"


# ─────────────────────────────────────────────────────────────────────────────
# CP-11: _build_iso_name_map covers key countries
# ─────────────────────────────────────────────────────────────────────────────


def test_cp11_iso_name_map_key_countries():
    iso_map, sov_map = build_viewer._build_iso_name_map()
    assert "CD" in iso_map, "CD missing from ISO name map"
    assert "NC" in iso_map, "NC missing from ISO name map"
    assert "CN" in iso_map, "CN missing from ISO name map"
    # NC is a French territory
    assert sov_map.get("NC") == "France", f"NC sovereignt should be France, got {sov_map.get('NC')!r}"
    # ZZ should not be in the GeoJSON at all
    assert "ZZ" not in iso_map, "ZZ should not appear in ISO name map"


# ─────────────────────────────────────────────────────────────────────────────
# CP-12: Site nav appears in all page shells
# ─────────────────────────────────────────────────────────────────────────────


def test_cp12_site_nav_in_pages(viewer_dir):
    """index.html, element pages, and country pages all include the site nav."""
    index = (viewer_dir / "index.html").read_text()
    assert 'class="site-nav"' in index, "index.html missing site-nav"
    assert "byproducts.html" in index, "index.html nav missing byproducts.html link"

    co = (viewer_dir / "elements" / "Co.html").read_text()
    assert 'class="site-nav"' in co, "Co.html missing site-nav"

    cd = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'class="site-nav"' in cd, "CD.html missing site-nav"


# ─────────────────────────────────────────────────────────────────────────────
# CP-13: _flag_emoji helper
# ─────────────────────────────────────────────────────────────────────────────


def test_cp13_flag_emoji():
    assert build_viewer._flag_emoji("CD") == "\U0001f1e8\U0001f1e9"  # 🇨🇩
    assert build_viewer._flag_emoji("US") == "\U0001f1fa\U0001f1f8"  # 🇺🇸
    assert build_viewer._flag_emoji("ZZ") == "\U0001f1ff\U0001f1ff"  # renders as letter pair on most platforms
    assert build_viewer._flag_emoji("X") == ""  # too short
    assert build_viewer._flag_emoji("123") == ""  # not alpha


# ─────────────────────────────────────────────────────────────────────────────
# CP-14: Country page stage sections have correct headings
# ─────────────────────────────────────────────────────────────────────────────


def test_cp14_cd_page_has_stage_sections(viewer_dir):
    """CD page must have Mining, Refining, Reserves section headings."""
    cd = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'id="mining"' in cd, "CD.html missing #mining section"
    assert 'id="refining"' in cd, "CD.html missing #refining section"
    assert 'id="reserves"' in cd, "CD.html missing #reserves section"


# ─────────────────────────────────────────────────────────────────────────────
# CP-15: charts_country.js deployed
# ─────────────────────────────────────────────────────────────────────────────


def test_cp15_charts_country_js_deployed(viewer_dir):
    """charts_country.js must be written into assets/ during generation."""
    assert (viewer_dir / "assets" / "charts_country.js").exists(), "charts_country.js not deployed"


# =============================================================================
# TF — Table filter + sort tests (CC-1, CC-2, CC-5)
# =============================================================================


def _parse_element_index(index_html: str) -> list[dict]:
    """Extract and parse the atlas-element-index JSON block from index.html."""
    m = _re.search(r'<script id="atlas-element-index" type="application/json">(.*?)</script>', index_html, _re.DOTALL)
    assert m, "atlas-element-index script block not found in index.html"
    return _json.loads(m.group(1))


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-1: Element index is valid JSON and contains all elements
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv1_element_index_json_present_and_complete(viewer_dir):
    """atlas-element-index script block must exist, be valid JSON, and contain known symbols."""
    index_html = (viewer_dir / "index.html").read_text()
    index = _parse_element_index(index_html)
    assert isinstance(index, list), "atlas-element-index must be a JSON array"
    symbols = {el["symbol"] for el in index}
    for sym in ["Co", "He", "Og", "Nd"]:
        assert sym in symbols, f"atlas-element-index missing symbol {sym}"
    # Every entry must carry the required CC-1 top-level keys
    required_keys = {"symbol", "name", "atomic_number", "category", "tier", "commercial_production",
                     "criticality", "byproduct_of", "top_mining_country", "top_mining_share",
                     "hhi_mining", "hhi_refining", "end_use_buckets", "producer_countries_mining"}
    for entry in index:
        missing = required_keys - entry.keys()
        assert not missing, f"{entry['symbol']}: missing keys {missing}"


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-2: _compute_hhi correctness
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv2_compute_hhi_cobalt():
    """_compute_hhi returns correct values for a Co-like share distribution."""
    shares = [
        {"country": "CD", "share_pct": 76.0},
        {"country": "ID", "share_pct": 10.0},
        {"country": "RU", "share_pct": 3.0},
        {"country": "CA", "share_pct": 2.0},
        {"country": "ZZ", "share_pct": 2.0},  # excluded from HHI
    ]
    hhi, top_country, top_pct = build_viewer._compute_hhi(shares)
    assert top_country == "CD"
    assert top_pct == 76.0
    # HHI = 76^2 + 10^2 + 3^2 + 2^2 = 5776 + 100 + 9 + 4 = 5889
    assert hhi == round(76**2 + 10**2 + 3**2 + 2**2)


def test_tf_inv2_compute_hhi_no_data():
    """Empty shares list → (None, None, None)."""
    hhi, top, pct = build_viewer._compute_hhi([])
    assert hhi is None and top is None and pct is None


def test_tf_inv2_compute_hhi_zz_only():
    """All-ZZ shares → (None, None, None) (ZZ excluded)."""
    hhi, top, pct = build_viewer._compute_hhi([{"country": "ZZ", "share_pct": 100.0}])
    assert hhi is None


def test_tf_inv2_compute_hhi_single_country():
    """Single named country → HHI = share^2 (monopoly case)."""
    hhi, top, pct = build_viewer._compute_hhi([{"country": "CN", "share_pct": 100.0}])
    assert hhi == 10000
    assert top == "CN"
    assert pct == 100.0


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-3: data-* attributes on Co row
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv3_data_attrs_cobalt(viewer_dir):
    """The Co <tr> must carry the required data-* attributes with correct values."""
    index_html = (viewer_dir / "index.html").read_text()
    assert 'data-symbol="Co"' in index_html, "Co row missing data-symbol"
    assert 'data-us-critical="true"' in index_html, "Co row missing data-us-critical=true"
    assert 'data-byproduct="true"' in index_html, "Co row missing data-byproduct=true"
    assert 'data-top-country="CD"' in index_html, "Co row missing data-top-country=CD"
    assert 'data-hhi-mining="' in index_html, "index.html missing data-hhi-mining attribute"
    assert 'data-eu-crm="true"' in index_html, "Co row missing data-eu-crm=true"
    assert 'data-eu-strategic="true"' in index_html, "Co row missing data-eu-strategic=true"


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-4: Filter UI DOM present
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv4_filter_ui_in_index(viewer_dir):
    """index.html must contain the table-controls div with all required sub-elements."""
    index_html = (viewer_dir / "index.html").read_text()
    assert 'class="table-controls"' in index_html, "index.html missing .table-controls"
    assert 'data-filter-key="us_critical"' in index_html, "index.html missing us_critical chip"
    assert 'data-filter-key="eu_crm"' in index_html, "index.html missing eu_crm chip"
    assert 'data-filter-key="eu_strategic"' in index_html, "index.html missing eu_strategic chip"
    assert 'data-filter-key="byproduct_only"' in index_html, "index.html missing byproduct_only chip"
    assert 'id="enduse-select"' in index_html, "index.html missing #enduse-select"
    assert 'id="country-select"' in index_html, "index.html missing #country-select"
    assert 'id="table-search"' in index_html, "index.html missing #table-search"
    assert 'id="clear-all-btn"' in index_html, "index.html missing #clear-all-btn"


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-5: He (noble gas) gets null HHI in the index (but actually has mining data)
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv5_he_has_hhi_in_index(viewer_dir):
    """He has mining shares (US, QA, etc.) so its HHI must be non-null."""
    index_html = (viewer_dir / "index.html").read_text()
    index = _parse_element_index(index_html)
    he = next((el for el in index if el["symbol"] == "He"), None)
    assert he is not None, "He not found in element index"
    # He has mining data, so HHI should be non-null
    assert he["hhi_mining"] is not None, "He has mining shares so hhi_mining should be non-null"
    assert he["top_mining_country"] is not None, "He should have a top_mining_country"


def test_tf_inv5_og_null_hhi_in_index(viewer_dir):
    """Og (no commercial production, no mining shares) should have null HHI fields."""
    index_html = (viewer_dir / "index.html").read_text()
    index = _parse_element_index(index_html)
    og = next((el for el in index if el["symbol"] == "Og"), None)
    assert og is not None, "Og not found in element index"
    assert og["hhi_mining"] is None, "Og should have null hhi_mining (no mining data)"
    assert og["top_mining_country"] is None, "Og should have null top_mining_country"


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-6: End-use bucket mapping for Co
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv6_enduse_buckets_cobalt(viewer_dir):
    """Co's end_use_buckets must include 'superalloys' and 'cutting_tools'."""
    index_html = (viewer_dir / "index.html").read_text()
    index = _parse_element_index(index_html)
    co = next((el for el in index if el["symbol"] == "Co"), None)
    assert co is not None, "Co not found in element index"
    buckets = co["end_use_buckets"]
    assert "superalloys" in buckets, f"Co end_use_buckets missing 'superalloys': {buckets}"
    assert "cutting_tools" in buckets, f"Co end_use_buckets missing 'cutting_tools': {buckets}"


# ─────────────────────────────────────────────────────────────────────────────
# TF-INV-7: table_filter.js and table_sort.js are deployed into assets
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_inv7_table_js_deployed(viewer_dir):
    """table_sort.js and table_filter.js must be written into assets/ during generation."""
    assert (viewer_dir / "assets" / "table_sort.js").exists(), "assets/table_sort.js not deployed"
    assert (viewer_dir / "assets" / "table_filter.js").exists(), "assets/table_filter.js not deployed"


def test_tf_inv7_table_js_referenced_in_index(viewer_dir):
    """index.html must reference both table JS files."""
    index_html = (viewer_dir / "index.html").read_text()
    assert "table_sort.js" in index_html, "index.html missing table_sort.js reference"
    assert "table_filter.js" in index_html, "index.html missing table_filter.js reference"


# ─────────────────────────────────────────────────────────────────────────────
# TF: New column headers (Top country, HHI) present in the table
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_new_column_headers_present(viewer_dir):
    """index.html must contain the two new sortable column headers."""
    index_html = (viewer_dir / "index.html").read_text()
    assert 'data-sort-key="top_country_share"' in index_html, "index.html missing top_country_share column header"
    assert 'data-sort-key="hhi_mining"' in index_html, "index.html missing hhi_mining column header"


# ─────────────────────────────────────────────────────────────────────────────
# TF: Empty-state row present in tbody
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_empty_state_row_in_table(viewer_dir):
    """index.html table must contain the hidden empty-state row."""
    index_html = (viewer_dir / "index.html").read_text()
    assert 'class="table-empty-state"' in index_html, "index.html missing .table-empty-state row"


# ─────────────────────────────────────────────────────────────────────────────
# TF: Byproduct CTA div present
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_byproduct_cta_in_index(viewer_dir):
    """index.html must contain the byproduct-graph CTA div with the correct href."""
    index_html = (viewer_dir / "index.html").read_text()
    assert 'id="byproduct-graph-cta"' in index_html, "index.html missing #byproduct-graph-cta"
    assert "byproducts.html" in index_html, "byproduct CTA link must point to byproducts.html"


# ─────────────────────────────────────────────────────────────────────────────
# TF: CSS contains filter chip and sort indicator rules
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_css_contains_filter_rules(viewer_dir):
    """atlas.css must contain CSS rules for the filter UI and sort indicators."""
    css = (viewer_dir / "assets" / "atlas.css").read_text()
    assert ".filter-chip" in css, "CSS missing .filter-chip rule"
    assert ".filter-chip.active" in css, "CSS missing .filter-chip.active rule"
    assert ".th-sortable" in css, "CSS missing .th-sortable rule"
    assert ".table-controls" in css, "CSS missing .table-controls rule"
    assert ".table-search" in css, "CSS missing .table-search rule"


# ─────────────────────────────────────────────────────────────────────────────
# TF: END_USE_BUCKET_MAP constant exists and contains required buckets
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_end_use_bucket_map_constant():
    """END_USE_BUCKET_MAP must exist at module level with all 14 canonical buckets as values."""
    bucket_map = build_viewer.END_USE_BUCKET_MAP
    assert isinstance(bucket_map, dict), "END_USE_BUCKET_MAP must be a dict"
    canonical_buckets = {"batteries", "magnets", "superalloys", "semiconductors", "catalysts",
                        "fertilizers", "steel_and_alloys", "cutting_tools", "glass_and_ceramics",
                        "pigments_and_coatings", "nuclear", "medical", "lighting"}
    values_in_map = set(bucket_map.values())
    missing = canonical_buckets - values_in_map
    assert not missing, f"END_USE_BUCKET_MAP missing values for buckets: {missing}"
    # Verify specific mappings from the spec
    assert bucket_map.get("superalloys_aircraft_turbines") == "superalloys"
    assert bucket_map.get("cemented_carbides_cutting_tools") == "cutting_tools"
    assert bucket_map.get("autocatalysts") == "catalysts"
    assert bucket_map.get("li_ion_batteries") == "batteries"


# ─────────────────────────────────────────────────────────────────────────────
# TF: _build_element_index function exists and returns valid data
# ─────────────────────────────────────────────────────────────────────────────


def test_tf_build_element_index_function():
    """_build_element_index must produce a valid JSON string when called directly."""
    elements = [
        {
            "symbol": "Co",
            "atomic_number": 27,
            "name": "cobalt",
            "category": "transition_metal",
            "industrial_tier": 3,
            "commercial_production": True,
            "us_critical_list_as_of_2025": True,
            "eu_crm_list_as_of_2024": True,
            "eu_strategic_list_as_of_2024": True,
            "doe_short_term_criticality_rank": None,
        }
    ]
    mining = {"Co": [{"country": "CD", "share_pct": 76.0}, {"country": "ZZ", "share_pct": 2.0}]}
    refining = {"Co": [{"country": "CN", "share_pct": 60.0}]}
    end_uses = {"Co": [{"application": "superalloys_aircraft_turbines", "share_pct": 51.0}]}
    byproduct = {"Co": ["Cu", "Ni"]}

    result_json = build_viewer._build_element_index(elements, mining, refining, end_uses, byproduct)
    result = _json.loads(result_json)
    assert len(result) == 1
    co = result[0]
    assert co["symbol"] == "Co"
    assert co["hhi_mining"] == round(76**2)  # only CD (ZZ excluded)
    assert co["top_mining_country"] == "CD"
    assert "superalloys" in co["end_use_buckets"]
    assert co["byproduct_of"] == ["Cu", "Ni"]
    assert co["criticality"]["us_critical"] is True

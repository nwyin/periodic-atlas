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

Critical paths:
  - fresh run into tmpdir produces index.html + 9 per-element pages
  - every chart-placeholder div id is present in each per-element stub

Failure modes:
  - missing duckdb → clear error message, sys.exit non-zero
  - empty atlas_elements table → friendly error
"""

from __future__ import annotations

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

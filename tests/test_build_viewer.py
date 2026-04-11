"""Tests for scripts/build_viewer.py.

Invariants verified:
  INV-1: generator runs end-to-end against real build/atlas-2025.duckdb without error
  INV-2: viewer/index.html contains a link to every element's page
  INV-3: every {symbol}.html contains the element's symbol and name
  INV-4: two back-to-back runs produce identical output (uses injected timestamp)
  INV-5: Og (no commercial_production) renders "No commercial production" text

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

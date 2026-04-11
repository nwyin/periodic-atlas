"""Tests for scripts/build.py flatteners.

These tests lock in the column names of every emitted parquet table so
that schema drift breaks the test suite immediately rather than silently
producing parquet files with different column sets from one build to the
next. They also verify provenance joins: every claim-bearing row's
source_id must resolve to an entry in atlas_sources.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make scripts/ importable for the builders without packaging them.
_SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(_SCRIPTS_DIR))

import build  # noqa: E402

from atlas.models import (  # noqa: E402
    CountryShare,
    CountryShareList,
    EndUse,
    EndUseList,
    FeedstockOrigin,
    FlowUnit,
    GeopoliticalEvent,
    IsotopeMarket,
    Price,
    ProductionBlock,
    Quantity,
    Reserves,
    Source,
    StockUnit,
    SubstituteClaim,
)

from tests.conftest import make_element, make_quantity, make_share_list, make_source


def _rich_element():
    """An element with every field populated, for full-column coverage tests."""
    return make_element(
        symbol="Te",
        atomic_number=52,
        name="tellurium",
        snapshot_year=2025,
        reporting_year=2024,
        byproduct_of=["Cu"],
        feedstock_origins=[
            FeedstockOrigin(substrate="copper_anode_slimes", typical_concentration_pct=0.1, source_id="test_source"),
        ],
        substitutes=[
            SubstituteClaim(availability="partial", notes="CIGS competes with CdTe in thin-film solar", source_id="test_source"),
        ],
        reserves=Reserves(
            economic_reserves=Quantity(
                value=31000, unit=StockUnit.TONNES, form="metal", source_id="test_source",
            ),
        ),
        prices=[
            Price(year=2024, value=75, unit="usd_per_kg", form="metal", basis="spot", source_id="test_source"),  # type: ignore[arg-type]
        ],
        geopolitical_events=[
            GeopoliticalEvent(date="2025-02-15", event="Test event", impact="Test impact", source_id="test_source"),
        ],
    )


class TestFlatteners:
    def test_elements_table_has_expected_columns(self):
        el = make_element()
        df = build.flatten_elements([el])
        assert len(df) == 1
        expected = {
            "symbol", "atomic_number", "name", "category", "industrial_tier",
            "commercial_production", "snapshot_year", "num_end_uses",
            "num_sources", "us_critical_list_as_of_2025",
        }
        assert expected.issubset(set(df.columns))

    def test_production_table_emits_row_per_stage(self):
        el = make_element()
        df = build.flatten_production([el])
        assert len(df) == 1  # mine only, no refined
        assert df.iloc[0]["stage"] == "mine"
        assert df.iloc[0]["unit"] == "tonnes_per_year"
        assert df.iloc[0]["source_id"] == "test_source"

    def test_reserves_table_only_when_present(self):
        el = make_element()  # no reserves
        df = build.flatten_reserves([el])
        assert len(df) == 0

        el_r = _rich_element()
        df_r = build.flatten_reserves([el_r])
        assert len(df_r) == 1
        assert df_r.iloc[0]["kind"] == "economic_reserves"
        assert df_r.iloc[0]["unit"] == "tonnes"

    def test_shares_table_unifies_mining_and_refining(self):
        el = make_element(
            production=ProductionBlock(
                reporting_year=2024,
                mine=make_quantity(),
                mining_by_country=make_share_list(countries=[("CN", 80.0), ("US", 20.0)], completeness="complete"),
                refining_by_country=make_share_list(countries=[("CN", 90.0), ("ZZ", 10.0)], completeness="top_producers_only"),
            ),
        )
        df = build.flatten_shares([el])
        assert set(df["share_type"].unique()) == {"mining", "refining"}
        assert len(df) == 4
        assert set(df.columns).issuperset({"symbol", "share_type", "country", "share_pct", "completeness", "source_id"})

    def test_shares_table_includes_isotope_producers(self):
        el = make_element(
            symbol="Am",
            atomic_number=95,
            name="americium",
            category="actinide",  # type: ignore[arg-type]
            industrial_tier=2,  # type: ignore[arg-type]
            with_production=False,
            isotope_markets=[
                IsotopeMarket(
                    isotope="Am-241",
                    half_life_seconds=1.36e10,
                    production_mode="stockpile_separated",
                    reporting_year=2024,
                    producers=CountryShareList(
                        shares=[
                            CountryShare(country="US", share_pct=60, source_id="test_source"),
                            CountryShare(country="ZZ", share_pct=40, source_id="test_source"),
                        ],
                        completeness="top_producers_only",
                    ),
                ),
            ],
        )
        df = build.flatten_shares([el])
        isotope_rows = df[df["share_type"] == "isotope_producers"]
        assert len(isotope_rows) == 2
        assert set(isotope_rows["isotope"].unique()) == {"Am-241"}

    def test_end_uses_preserves_completeness(self):
        el = make_element()
        df = build.flatten_end_uses([el])
        assert len(df) == 2
        assert (df["completeness"] == "complete").all()

    def test_prices_column_set(self):
        el = _rich_element()
        df = build.flatten_prices([el])
        assert len(df) == 1
        assert df.iloc[0]["unit"] == "usd_per_kg"
        assert df.iloc[0]["basis"] == "spot"
        assert df.iloc[0]["form"] == "metal"

    def test_events_column_set(self):
        el = _rich_element()
        df = build.flatten_events([el])
        assert len(df) == 1
        assert df.iloc[0]["date"] == "2025-02-15"
        assert df.iloc[0]["source_id"] == "test_source"

    def test_sources_table_has_source_rows(self):
        el = make_element()
        df = build.flatten_sources([el])
        assert len(df) == 1
        assert df.iloc[0]["source_id"] == "test_source"
        assert df.iloc[0]["symbol"] == "Te"

    def test_isotope_markets_expands_quantity_fields(self):
        el = make_element(
            symbol="Tc",
            atomic_number=43,
            name="technetium",
            with_production=False,
            isotope_markets=[
                IsotopeMarket(
                    isotope="Tc-99m",
                    half_life_seconds=21624.0,
                    production_mode="reactor_generated",
                    reporting_year=2024,
                    producers=CountryShareList(
                        shares=[CountryShare(country="NL", share_pct=50, source_id="test_source")],
                        completeness="partial",
                    ),
                ),
            ],
        )
        df = build.flatten_isotope_markets([el])
        assert len(df) == 1
        assert df.iloc[0]["production_mode"] == "reactor_generated"
        assert df.iloc[0]["num_producers"] == 1
        # production_quantity is None; columns should exist with None values
        assert "production_value" in df.columns
        assert df.iloc[0]["production_value"] is None

    def test_feedstocks_and_byproducts_tables(self):
        el = _rich_element()
        fs = build.flatten_feedstocks([el])
        bp = build.flatten_byproducts([el])
        assert len(fs) == 1
        assert fs.iloc[0]["substrate"] == "copper_anode_slimes"
        assert len(bp) == 1
        assert bp.iloc[0]["parent_symbol"] == "Cu"

    def test_criticality_is_long_form(self):
        el = _rich_element()
        df = build.flatten_criticality([el])
        # 3 flag columns become 3 rows
        assert len(df) == 3
        assert set(df["flag_name"]) == {
            "us_critical_list_as_of_2025",
            "eu_crm_list_as_of_2024",
            "eu_strategic_list_as_of_2024",
        }


class TestProvenanceJoin:
    def test_every_source_id_in_output_resolves_to_sources_table(self):
        """Build every table from a rich element and join each source_id column
        against the sources table. Any orphaned source_id is a schema bug."""
        el = _rich_element()
        tables = build.build_all([el])
        sources = tables["sources"]
        known_source_ids = set(zip(sources["symbol"], sources["source_id"]))

        for table_name, df in tables.items():
            if table_name == "sources" or "source_id" not in df.columns:
                continue
            for _, row in df.iterrows():
                sid = row.get("source_id")
                if sid is None or (isinstance(sid, float) and str(sid) == "nan"):
                    continue
                assert (row["symbol"], sid) in known_source_ids, (
                    f"orphaned source_id {sid!r} in atlas_{table_name}"
                )


class TestBuildOrchestration:
    def test_build_all_returns_expected_tables(self):
        el = make_element()
        tables = build.build_all([el])
        assert set(tables.keys()) == set(build.TABLE_BUILDERS.keys())

    def test_coverage_report_fields(self):
        el = make_element()
        cov = build.coverage_report([el])
        assert cov["total_elements"] == 1
        assert "by_tier" in cov

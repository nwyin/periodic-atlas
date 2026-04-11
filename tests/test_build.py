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

import pytest

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
            SubstituteClaim(application="solar_cdte", availability="partial", notes="CIGS competes with CdTe in thin-film solar", source_id="test_source"),
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
            "commercial_production", "snapshot_year", "reporting_year",
            "num_end_uses", "num_sources", "us_critical_list_as_of_2025",
            "num_production_blocks",
        }
        assert expected.issubset(set(df.columns))

    def test_elements_table_reporting_year_is_max_across_blocks(self):
        """reporting_year on the wide elements table is the max of
        production-block reporting years (or None for elements without
        production)."""
        from atlas.models import ProductionBlock

        multi = make_element(
            production=[
                ProductionBlock(
                    reporting_year=2023,
                    stream="ore",
                    mine=make_quantity(),
                    mining_by_country=make_share_list(),
                ),
                ProductionBlock(
                    reporting_year=2024,
                    stream="crude_steel",
                    refined=make_quantity(),
                ),
            ],
        )
        df = build.flatten_elements([multi])
        assert df.iloc[0]["reporting_year"] == 2024
        assert df.iloc[0]["num_production_blocks"] == 2

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
        assert set(df.columns).issuperset({
            "symbol", "share_type", "country", "share_pct",
            "completeness", "source_id", "quantity_source_id", "confidence", "stream",
        })

    def test_shares_table_quantity_source_id_can_differ_from_row_source_id(self):
        """H2: when CountryShare.source_id differs from the nested
        CountryShare.quantity.source_id, both should survive in the parquet
        shares table as separate columns."""
        el = make_element(
            extra_sources=[make_source("other_source")],
            production=ProductionBlock(
                reporting_year=2024,
                mine=make_quantity(),
                mining_by_country=CountryShareList(
                    shares=[
                        CountryShare(
                            country="CN",
                            share_pct=80,
                            quantity=Quantity(
                                value=500,
                                unit=FlowUnit.TONNES_PER_YEAR,
                                form="metal",
                                source_id="other_source",
                            ),
                            source_id="test_source",
                        ),
                        CountryShare(country="US", share_pct=20, source_id="test_source"),
                    ],
                    completeness="complete",
                ),
            ),
        )
        df = build.flatten_shares([el])
        mining_rows = df[df["share_type"] == "mining"]
        # First row has a nested quantity with its own source_id
        cn_row = mining_rows[mining_rows["country"] == "CN"].iloc[0]
        assert cn_row["source_id"] == "test_source"
        assert cn_row["quantity_source_id"] == "other_source"
        us_row = mining_rows[mining_rows["country"] == "US"].iloc[0]
        assert us_row["source_id"] == "test_source"
        # No nested quantity on US row -> quantity_source_id is null
        assert us_row["quantity_source_id"] is None or (
            isinstance(us_row["quantity_source_id"], float)
            and str(us_row["quantity_source_id"]) == "nan"
        )

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
        # 3 boolean flags + 1 doe rank row per element
        assert len(df) == 4
        assert set(df["flag_name"]) == {
            "us_critical_list_as_of_2025",
            "eu_crm_list_as_of_2024",
            "eu_strategic_list_as_of_2024",
            "doe_short_term_criticality_rank",
        }
        # rank_value column exists and is populated only on the rank row
        assert "rank_value" in df.columns
        rank_rows = df[df["flag_name"] == "doe_short_term_criticality_rank"]
        assert len(rank_rows) == 1


def _row_is_claim_bearing(table_name: str, row) -> bool:
    """Return True when a flattened row represents an active factual claim.

    A claim-bearing row must carry a source_id. The provenance test fails
    on any row that is claim-bearing but has source_id=None. The criticality
    table is a special case: rows where every flag is False and the rank is
    None are *negative* membership ("not on the list"), not active claims,
    so they are not required to cite a source.
    """
    if table_name == "criticality":
        value = row.get("value")
        rank_value = row.get("rank_value")
        has_value = value is True
        has_rank = rank_value is not None and not (
            isinstance(rank_value, float) and str(rank_value) == "nan"
        )
        return bool(has_value or has_rank)
    return True


def _is_null(x) -> bool:
    return x is None or (isinstance(x, float) and str(x) == "nan")


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
                if _is_null(sid):
                    assert not _row_is_claim_bearing(table_name, row), (
                        f"claim-bearing row in atlas_{table_name} has null source_id: "
                        f"{dict(row)}"
                    )
                    continue
                assert (row["symbol"], sid) in known_source_ids, (
                    f"orphaned source_id {sid!r} in atlas_{table_name}"
                )

    def test_null_source_id_on_active_criticality_flag_fails(self):
        """Regression: in v0.2, build.flatten_criticality emitted a row with
        source_id=None even when the flag was True because CriticalityFlags
        allowed source_id=None. C1 forbids that combination at the model level;
        this test locks in the shape of the resulting parquet rows.
        """
        from atlas.models import CriticalityFlags

        # Explicit attempt to construct the forbidden combination should
        # fail at the Pydantic layer before build.py ever sees it.
        from pydantic import ValidationError

        with pytest.raises(ValidationError, match="source_id is required"):
            CriticalityFlags(us_critical_list_as_of_2025=True)

    def test_provenance_test_catches_fabricated_null_source_id(self):
        """If we manually fabricate a claim-bearing row with source_id=None
        the provenance test must reject it. This ensures H3 has teeth."""
        el = _rich_element()
        tables = build.build_all([el])
        # Force a null source_id on a prices row (claim-bearing, non-criticality).
        tables["prices"].loc[0, "source_id"] = None

        sources = tables["sources"]
        known_source_ids = set(zip(sources["symbol"], sources["source_id"]))

        caught = False
        for table_name, df in tables.items():
            if table_name == "sources" or "source_id" not in df.columns:
                continue
            for _, row in df.iterrows():
                sid = row.get("source_id")
                if _is_null(sid):
                    if _row_is_claim_bearing(table_name, row):
                        caught = True
                        break
            if caught:
                break
        assert caught, "provenance test must fail when a claim-bearing row has null source_id"


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

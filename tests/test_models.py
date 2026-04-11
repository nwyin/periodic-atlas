"""Tests for atlas v0.2 Pydantic models.

Coverage targets:
- Stock-vs-flow unit discipline (ProductionBlock rejects stock units in flow fields; Reserves rejects flow in stock fields)
- Year disambiguation (snapshot_year, reporting_year, event date horizon)
- Source-id resolution across every provenance-bearing model
- Share-list completeness semantics
- Grouped-commodity reporting flag consistency
- IsotopeMarket production_mode discriminator
- Commercial-vs-research mutual exclusivity
- byproduct_of element-symbol validation
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from atlas.models import (
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
    ResearchOnly,
    Reserves,
    Source,
    StockUnit,
    SubstituteClaim,
)

from tests.conftest import make_element, make_quantity, make_share_list, make_source


class TestQuantity:
    def test_flow_unit_is_flow(self) -> None:
        q = make_quantity(unit=FlowUnit.TONNES_PER_YEAR)
        assert q.is_flow
        assert not q.is_stock

    def test_stock_unit_is_stock(self) -> None:
        q = make_quantity(unit=StockUnit.TONNES)
        assert q.is_stock
        assert not q.is_flow

    def test_range_requires_both_bounds(self) -> None:
        with pytest.raises(ValidationError, match="range requires both low and high"):
            Quantity(value=1000, unit=FlowUnit.TONNES_PER_YEAR, form="metal", low=900, source_id="s")

    def test_range_must_be_ordered(self) -> None:
        with pytest.raises(ValidationError, match="low.*> high"):
            Quantity(value=1000, unit=FlowUnit.TONNES_PER_YEAR, form="metal", low=1100, high=900, source_id="s")


class TestStockFlowDiscipline:
    def test_production_mine_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match="must be a flow quantity"):
            ProductionBlock(
                reporting_year=2024,
                mine=make_quantity(unit=StockUnit.TONNES),
            )

    def test_production_refined_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match="must be a flow quantity"):
            ProductionBlock(
                reporting_year=2024,
                refined=make_quantity(unit=StockUnit.TONNES),
            )

    def test_reserves_rejects_flow_unit(self) -> None:
        with pytest.raises(ValidationError, match="must be a stock quantity"):
            Reserves(
                economic_reserves=make_quantity(unit=FlowUnit.TONNES_PER_YEAR),
            )

    def test_reserves_accepts_stock_unit(self) -> None:
        r = Reserves(economic_reserves=make_quantity(unit=StockUnit.TONNES))
        assert r.economic_reserves is not None
        assert r.economic_reserves.is_stock


class TestYearDisambiguation:
    def test_reporting_year_must_not_exceed_snapshot(self) -> None:
        with pytest.raises(ValidationError, match=r"production\[0\]\.reporting_year=2026 exceeds snapshot_year=2025"):
            make_element(snapshot_year=2025, reporting_year=2026)

    def test_reporting_year_can_lag_snapshot(self) -> None:
        e = make_element(snapshot_year=2025, reporting_year=2023)
        assert len(e.production) == 1
        assert e.production[0].reporting_year == 2023

    def test_event_beyond_snapshot_rejected(self) -> None:
        with pytest.raises(ValidationError, match="is beyond snapshot horizon"):
            make_element(
                geopolitical_events=[
                    GeopoliticalEvent(date="2026-03-15", event="future event", source_id="test_source")
                ],
            )

    def test_event_within_snapshot_accepted(self) -> None:
        e = make_element(
            geopolitical_events=[
                GeopoliticalEvent(date="2025-06-01", event="past event", source_id="test_source")
            ],
        )
        assert len(e.geopolitical_events) == 1

    def test_price_year_beyond_snapshot_rejected(self) -> None:
        with pytest.raises(ValidationError, match="prices.*year=2099 exceeds snapshot_year=2025"):
            make_element(
                prices=[Price(year=2099, value=10, unit="usd_per_kg", source_id="test_source")],  # type: ignore[arg-type]
            )


class TestSourceIdResolution:
    def test_unknown_source_id_in_production_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'missing'"):
            make_element(
                production=ProductionBlock(
                    reporting_year=2024,
                    mine=make_quantity(source_id="missing"),
                ),
            )

    def test_unknown_source_id_in_country_share_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'nope'"):
            make_element(
                production=ProductionBlock(
                    reporting_year=2024,
                    mine=make_quantity(),
                    mining_by_country=CountryShareList(
                        shares=[CountryShare(country="US", share_pct=60, source_id="nope")],
                    ),
                ),
            )

    def test_unknown_source_id_in_end_use_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'bad'"):
            make_element(
                end_uses=EndUseList(
                    uses=[EndUse(application="x", share_pct=50, source_id="bad")],
                ),
            )

    def test_unknown_source_id_in_feedstock_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'ghost'"):
            make_element(
                feedstock_origins=[
                    FeedstockOrigin(substrate="monazite", typical_concentration_pct=4, source_id="ghost")
                ],
            )

    def test_element_with_claims_needs_sources(self) -> None:
        with pytest.raises(ValidationError, match="has claims but no sources list"):
            make_element(extra_sources=[], sources=[])  # type: ignore[arg-type]


class TestShareListCompleteness:
    def test_complete_rejects_low_sum(self) -> None:
        with pytest.raises(ValidationError, match="declared 'complete' but sum to only"):
            CountryShareList(
                shares=[CountryShare(country="US", share_pct=30, source_id="s")],
                completeness="complete",
            )

    def test_complete_accepts_round_sum(self) -> None:
        csl = CountryShareList(
            shares=[
                CountryShare(country="US", share_pct=60, source_id="s"),
                CountryShare(country="CN", share_pct=40, source_id="s"),
            ],
            completeness="complete",
        )
        assert len(csl.shares) == 2

    def test_over_105_always_rejected(self) -> None:
        with pytest.raises(ValidationError, match="exceeds 105%"):
            CountryShareList(
                shares=[
                    CountryShare(country="US", share_pct=60, source_id="s"),
                    CountryShare(country="CN", share_pct=60, source_id="s"),
                ],
            )

    def test_top_producers_only_needs_zz_bucket(self) -> None:
        with pytest.raises(ValidationError, match="no 'ZZ'"):
            CountryShareList(
                shares=[
                    CountryShare(country="US", share_pct=30, source_id="s"),
                    CountryShare(country="CN", share_pct=20, source_id="s"),
                ],
                completeness="top_producers_only",
            )

    def test_top_producers_only_accepts_zz_bucket(self) -> None:
        csl = CountryShareList(
            shares=[
                CountryShare(country="CN", share_pct=70, source_id="s"),
                CountryShare(country="US", share_pct=10, source_id="s"),
                CountryShare(country="ZZ", share_pct=20, source_id="s"),
            ],
            completeness="top_producers_only",
        )
        assert len(csl.shares) == 3

    def test_partial_passes_low_sum(self) -> None:
        csl = CountryShareList(
            shares=[CountryShare(country="US", share_pct=20, source_id="s")],
            completeness="partial",
        )
        assert len(csl.shares) == 1


class TestGroupedReporting:
    def test_grouped_requires_commodity_group(self) -> None:
        with pytest.raises(ValidationError, match="grouped_reporting=true requires commodity_group"):
            ProductionBlock(reporting_year=2024, grouped_reporting=True)

    def test_commodity_group_requires_grouped_flag(self) -> None:
        with pytest.raises(ValidationError, match="commodity_group set but grouped_reporting is false"):
            ProductionBlock(reporting_year=2024, commodity_group="rare_earths")

    def test_grouped_consistent(self) -> None:
        pb = ProductionBlock(reporting_year=2024, grouped_reporting=True, commodity_group="rare_earths")
        assert pb.grouped_reporting
        assert pb.commodity_group == "rare_earths"


class TestIsotopeMarket:
    def test_basic_isotope_market_validates(self) -> None:
        im = IsotopeMarket(
            isotope="Am-241",
            half_life_seconds=1.36e10,
            production_mode="stockpile_separated",
            production_quantity=make_quantity(unit=FlowUnit.GRAMS_PER_YEAR, form="oxide"),
            reporting_year=2024,
        )
        assert im.isotope == "Am-241"
        assert im.production_mode == "stockpile_separated"

    def test_invalid_production_mode_rejected(self) -> None:
        with pytest.raises(ValidationError):
            IsotopeMarket(
                isotope="Am-241",
                half_life_seconds=1.36e10,
                production_mode="imaginary_mode",  # type: ignore[arg-type]
                production_quantity=make_quantity(unit=FlowUnit.GRAMS_PER_YEAR),
                reporting_year=2024,
            )


class TestCommercialResearchExclusivity:
    def test_commercial_needs_production_or_isotopes(self) -> None:
        with pytest.raises(ValidationError, match="commercial_production=true requires"):
            make_element(commercial_production=True, with_production=False)

    def test_non_commercial_rejects_production(self) -> None:
        with pytest.raises(ValidationError, match="commercial_production=false but production"):
            make_element(commercial_production=False)

    def test_research_only_element_validates(self) -> None:
        e = make_element(
            symbol="Og",
            atomic_number=118,
            name="oganesson",
            category="synthetic_superheavy",  # type: ignore[arg-type]
            industrial_tier=1,  # type: ignore[arg-type]
            commercial_production=False,
            with_production=False,
            with_end_uses=False,
            research_only=ResearchOnly(
                longest_lived_isotope="Og-294",
                half_life_seconds=0.00069,
                iupac_recognized_year=2015,
                total_ever_produced=Quantity(
                    value=5, unit=StockUnit.ATOMS_TOTAL, form="unspecified",
                    approximate=True, source_id="test_source",
                ),
            ),
        )
        assert e.commercial_production is False
        assert e.research_only is not None


class TestByproductValidation:
    def test_byproduct_accepts_element_symbol(self) -> None:
        e = make_element(byproduct_of=["Cu", "Ni"])
        assert e.byproduct_of == ["Cu", "Ni"]

    def test_byproduct_rejects_feedstock_name(self) -> None:
        with pytest.raises(ValidationError, match="element symbols"):
            make_element(byproduct_of=["natural_gas"])

    def test_feedstock_origin_accepts_raw_material(self) -> None:
        e = make_element(
            feedstock_origins=[
                FeedstockOrigin(
                    substrate="natural_gas",
                    typical_concentration_pct=0.3,
                    source_id="test_source",
                )
            ],
        )
        assert e.feedstock_origins[0].substrate == "natural_gas"

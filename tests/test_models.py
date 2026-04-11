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
    CriticalityFlags,
    EndUse,
    EndUseList,
    FeedstockOrigin,
    FlowUnit,
    GeopoliticalEvent,
    IsotopeMarket,
    OwnershipConcentration,
    OwnershipStake,
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


class TestNestedStockFlowDiscipline:
    def test_mining_country_share_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match="mining_by_country.*must be a flow"):
            ProductionBlock(
                reporting_year=2024,
                mine=make_quantity(),
                mining_by_country=CountryShareList(
                    shares=[
                        CountryShare(
                            country="CN",
                            share_pct=80,
                            quantity=make_quantity(unit=StockUnit.TONNES),
                            source_id="s",
                        ),
                    ],
                ),
            )

    def test_refining_country_share_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match="refining_by_country.*must be a flow"):
            ProductionBlock(
                reporting_year=2024,
                refining_by_country=CountryShareList(
                    shares=[
                        CountryShare(
                            country="CN",
                            share_pct=80,
                            quantity=make_quantity(unit=StockUnit.TONNES),
                            source_id="s",
                        ),
                    ],
                ),
            )

    def test_reserves_country_share_rejects_flow_unit(self) -> None:
        with pytest.raises(ValidationError, match="reserves_by_country.*must be a stock"):
            Reserves(
                economic_reserves=make_quantity(unit=StockUnit.TONNES),
                reserves_by_country=CountryShareList(
                    shares=[
                        CountryShare(
                            country="CD",
                            share_pct=55,
                            quantity=make_quantity(unit=FlowUnit.TONNES_PER_YEAR),
                            source_id="s",
                        ),
                    ],
                ),
            )

    def test_isotope_market_production_quantity_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match="production_quantity must be a flow"):
            IsotopeMarket(
                isotope="Am-241",
                half_life_seconds=1.36e10,
                production_mode="stockpile_separated",
                production_quantity=make_quantity(unit=StockUnit.KG),
                reporting_year=2024,
            )

    def test_isotope_market_producer_share_rejects_stock_unit(self) -> None:
        with pytest.raises(ValidationError, match=r"producers\[0\].quantity must be a flow"):
            IsotopeMarket(
                isotope="Am-241",
                half_life_seconds=1.36e10,
                production_mode="stockpile_separated",
                reporting_year=2024,
                producers=CountryShareList(
                    shares=[
                        CountryShare(
                            country="US",
                            share_pct=50,
                            quantity=make_quantity(unit=StockUnit.KG),
                            source_id="s",
                        ),
                    ],
                    completeness="partial",
                ),
            )

    def test_research_only_total_ever_produced_rejects_flow_unit(self) -> None:
        with pytest.raises(ValidationError, match="total_ever_produced must be a stock"):
            ResearchOnly(
                longest_lived_isotope="Og-294",
                total_ever_produced=make_quantity(unit=FlowUnit.GRAMS_PER_YEAR),
            )


class TestCriticalityFlagsSourceRequirement:
    # INV-1: us_critical=True without us_critical_source_id must fail
    def test_us_critical_flag_requires_us_critical_source_id(self) -> None:
        with pytest.raises(ValidationError, match="us_critical_source_id"):
            CriticalityFlags(us_critical_list_as_of_2025=True)

    # INV-2a: eu_crm=True without eu_crm_source_id must fail
    def test_eu_crm_flag_requires_eu_crm_source_id(self) -> None:
        with pytest.raises(ValidationError, match="eu_crm_source_id"):
            CriticalityFlags(eu_crm_list_as_of_2024=True)

    # INV-2b: eu_strategic=True without eu_strategic_source_id must fail
    def test_eu_strategic_flag_requires_eu_strategic_source_id(self) -> None:
        with pytest.raises(ValidationError, match="eu_strategic_source_id"):
            CriticalityFlags(eu_strategic_list_as_of_2024=True)

    # INV-2c: doe_rank set without doe_rank_source_id must fail
    def test_doe_rank_requires_doe_rank_source_id(self) -> None:
        with pytest.raises(ValidationError, match="doe_rank_source_id"):
            CriticalityFlags(doe_short_term_criticality_rank=3)

    def test_all_inactive_accepts_no_sources(self) -> None:
        c = CriticalityFlags()
        assert c.us_critical_list_as_of_2025 is False
        assert c.us_critical_source_id is None
        assert c.eu_crm_source_id is None
        assert c.eu_strategic_source_id is None
        assert c.doe_rank_source_id is None

    # INV-3: mixed case — us_critical + eu_crm each with their own source validates OK
    def test_mixed_per_flag_sources_validate(self) -> None:
        c = CriticalityFlags(
            us_critical_list_as_of_2025=True,
            us_critical_source_id="usgs_source",
            eu_crm_list_as_of_2024=True,
            eu_crm_source_id="eu_source",
        )
        assert c.us_critical_list_as_of_2025 is True
        assert c.us_critical_source_id == "usgs_source"
        assert c.eu_crm_list_as_of_2024 is True
        assert c.eu_crm_source_id == "eu_source"

    def test_old_single_source_id_field_rejected(self) -> None:
        """Old shape with top-level source_id must fail — no backward-compat shim."""
        with pytest.raises(ValidationError):
            CriticalityFlags(us_critical_list_as_of_2025=True, source_id="x")  # type: ignore[call-arg]

    # INV-4: per-flag source_ids must resolve to entries in the element sources list
    def test_unknown_us_critical_source_id_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'missing_source'"):
            make_element(
                criticality=CriticalityFlags(
                    us_critical_list_as_of_2025=True,
                    us_critical_source_id="missing_source",
                ),
            )

    def test_known_eu_crm_source_id_resolves(self) -> None:
        e = make_element(
            criticality=CriticalityFlags(
                eu_crm_list_as_of_2024=True,
                eu_crm_source_id="test_source",
            ),
        )
        assert e.criticality.eu_crm_source_id == "test_source"


class TestSourceIdIntegrity:
    def test_duplicate_source_id_rejected(self) -> None:
        with pytest.raises(ValidationError, match="duplicate source id"):
            make_element(
                sources=[make_source("usgs"), make_source("usgs")],
            )

    def test_dangling_superseded_by_rejected(self) -> None:
        with pytest.raises(ValidationError, match="superseded_by.*does not resolve"):
            make_element(
                sources=[
                    Source(id="old", title="Old source", superseded_by="never_declared"),
                    make_source("test_source"),
                ],
            )

    def test_source_cannot_supersede_itself(self) -> None:
        with pytest.raises(ValidationError, match="cannot supersede itself"):
            make_element(
                sources=[
                    Source(id="test_source", title="T", superseded_by="test_source"),
                ],
            )

    def test_valid_superseded_by_chain_accepted(self) -> None:
        e = make_element(
            sources=[
                Source(id="old", title="Old", superseded_by="test_source"),
                make_source("test_source"),
            ],
        )
        assert len(e.sources) == 2

    def test_nested_isotope_producer_quantity_dangling_source_rejected(self) -> None:
        with pytest.raises(ValidationError, match="unknown source_id 'phantom'"):
            make_element(
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
                                CountryShare(
                                    country="US",
                                    share_pct=50,
                                    quantity=Quantity(
                                        value=10,
                                        unit=FlowUnit.GRAMS_PER_YEAR,
                                        form="oxide",
                                        source_id="phantom",
                                    ),
                                    source_id="test_source",
                                ),
                                CountryShare(country="ZZ", share_pct=50, source_id="test_source"),
                            ],
                            completeness="top_producers_only",
                        ),
                    ),
                ],
            )


class TestCountryShareConfidence:
    def test_defaults_to_high(self) -> None:
        s = CountryShare(country="CN", share_pct=80, source_id="s")
        assert s.confidence == "high"

    def test_accepts_low(self) -> None:
        s = CountryShare(country="CN", share_pct=80, source_id="s", confidence="low")
        assert s.confidence == "low"

    def test_rejects_bogus_level(self) -> None:
        with pytest.raises(ValidationError):
            CountryShare(country="CN", share_pct=80, source_id="s", confidence="maybe")  # type: ignore[arg-type]


class TestEndUseConfidence:
    def test_defaults_to_high(self) -> None:
        u = EndUse(application="batteries", share_pct=60, source_id="s")
        assert u.confidence == "high"

    def test_accepts_low(self) -> None:
        u = EndUse(application="batteries", share_pct=60, source_id="s", confidence="low")
        assert u.confidence == "low"


class TestSubstituteClaimApplication:
    def test_application_is_required(self) -> None:
        with pytest.raises(ValidationError):
            SubstituteClaim(availability="partial", notes="x", source_id="s")  # type: ignore[call-arg]

    def test_valid_claim_with_application(self) -> None:
        c = SubstituteClaim(
            application="rf_power_amplifiers",
            availability="partial",
            notes="SiGe CMOS in midtier 3G handsets",
            source_id="s",
        )
        assert c.application == "rf_power_amplifiers"


class TestOwnershipConcentration:
    def test_empty_stakes_requires_container_source_id(self) -> None:
        with pytest.raises(ValidationError, match="must set `source_id` on the container"):
            OwnershipConcentration(notes="prose claim")

    def test_empty_stakes_with_source_accepted(self) -> None:
        oc = OwnershipConcentration(notes="prose claim", source_id="s")
        assert oc.notes == "prose claim"
        assert oc.source_id == "s"
        assert oc.stakes == []

    def test_multiple_stakes_accepted(self) -> None:
        oc = OwnershipConcentration(
            stakes=[
                OwnershipStake(entity="Glencore", share_pct=30, source_id="s"),
                OwnershipStake(entity="CMOC", share_pct=25, source_id="s"),
                OwnershipStake(entity="ERG", share_pct=15, source_id="s"),
            ],
            completeness="top_producers_only",
        )
        assert len(oc.stakes) == 3

    def test_stakes_sum_over_100_rejected(self) -> None:
        with pytest.raises(ValidationError, match="stakes sum to"):
            OwnershipConcentration(
                stakes=[
                    OwnershipStake(entity="A", share_pct=60, source_id="s"),
                    OwnershipStake(entity="B", share_pct=60, source_id="s"),
                ],
            )

    def test_stakes_sum_equal_to_100_accepted(self) -> None:
        oc = OwnershipConcentration(
            stakes=[
                OwnershipStake(entity="A", share_pct=60, source_id="s"),
                OwnershipStake(entity="B", share_pct=40, source_id="s"),
            ],
            completeness="complete",
        )
        assert len(oc.stakes) == 2


class TestProductionAsList:
    def test_production_accepts_list_of_blocks(self) -> None:
        e = make_element(
            production=[
                ProductionBlock(
                    reporting_year=2024,
                    stream="mineral_concentrate",
                    mine=make_quantity(value=7000, unit=FlowUnit.KG_PER_YEAR, form="concentrate"),
                    mining_by_country=make_share_list(),
                ),
                ProductionBlock(
                    reporting_year=2024,
                    stream="sponge_metal",
                    refined=make_quantity(value=200, unit=FlowUnit.TONNES_PER_YEAR, form="metal"),
                ),
            ],
        )
        assert len(e.production) == 2
        streams = {pb.stream for pb in e.production}
        assert streams == {"mineral_concentrate", "sponge_metal"}

    def test_empty_production_list_accepted_when_isotope_markets_present(self) -> None:
        e = make_element(
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
                            CountryShare(country="US", share_pct=50, source_id="test_source"),
                            CountryShare(country="ZZ", share_pct=50, source_id="test_source"),
                        ],
                        completeness="top_producers_only",
                    ),
                ),
            ],
        )
        assert e.production == []

    def test_commercial_production_requires_production_or_isotopes(self) -> None:
        with pytest.raises(ValidationError, match="requires a non-empty production list"):
            make_element(commercial_production=True, with_production=False)

    def test_stream_discriminator_optional_single_block(self) -> None:
        e = make_element(
            production=ProductionBlock(
                reporting_year=2024,
                mine=make_quantity(),
                mining_by_country=make_share_list(),
            ),
        )
        assert len(e.production) == 1
        assert e.production[0].stream is None


class TestSourceTier:
    def test_default_is_secondary(self) -> None:
        s = Source(id="s", title="T")
        assert s.source_tier == "secondary"

    def test_accepts_primary(self) -> None:
        s = Source(id="s", title="T", source_tier="primary")
        assert s.source_tier == "primary"


class TestMillionTonnesUnit:
    def test_million_tonnes_per_year_is_flow(self) -> None:
        q = make_quantity(unit=FlowUnit.MILLION_TONNES_PER_YEAR, form="ore")
        assert q.is_flow
        assert q.unit.value == "million_tonnes_per_year"


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

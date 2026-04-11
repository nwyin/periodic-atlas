"""Shared fixtures for atlas schema tests.

`make_element()` builds a minimal valid Element with sensible defaults that
individual tests can override via kwargs. Matches the pattern used elsewhere
in the egotheism repo (`capital/tests/test_screener.py`) — seed helpers with
overridable defaults rather than per-test fixture proliferation.
"""

from __future__ import annotations

from typing import Any

import pytest

from atlas.models import (
    CountryShare,
    CountryShareList,
    CriticalityFlags,
    Element,
    ElementCategory,
    EndUse,
    EndUseList,
    FlowUnit,
    IndustrialTier,
    ProductionBlock,
    Quantity,
    Source,
    StockUnit,
)


def make_source(source_id: str = "test_source") -> Source:
    return Source(
        id=source_id,
        title="Test source",
        publisher="Atlas test suite",
        url=None,
        retrieved="2026-04-11",
        publication_year=2026,
    )


def make_quantity(
    value: float = 1000.0,
    unit: FlowUnit | StockUnit = FlowUnit.TONNES_PER_YEAR,
    form: str = "metal",
    source_id: str = "test_source",
    **overrides: Any,
) -> Quantity:
    return Quantity(value=value, unit=unit, form=form, source_id=source_id, **overrides)  # type: ignore[arg-type]


def make_share_list(
    countries: list[tuple[str, float]] | None = None,
    completeness: str = "partial",
    source_id: str = "test_source",
) -> CountryShareList:
    countries = countries or [("US", 60.0), ("CN", 40.0)]
    return CountryShareList(
        shares=[CountryShare(country=c, share_pct=p, source_id=source_id) for c, p in countries],
        completeness=completeness,  # type: ignore[arg-type]
    )


def make_element(
    symbol: str = "Te",
    atomic_number: int = 52,
    name: str = "tellurium",
    category: ElementCategory = ElementCategory.METALLOID,
    industrial_tier: IndustrialTier = IndustrialTier.CRITICAL_SCARCE,
    commercial_production: bool = True,
    snapshot_year: int = 2025,
    reporting_year: int = 2024,
    with_production: bool = True,
    with_end_uses: bool = True,
    extra_sources: list[Source] | None = None,
    **element_overrides: Any,
) -> Element:
    """Build a minimal valid Element with sane defaults.

    Override any field via kwargs. Use `with_production=False` to test
    research-only elements.
    """
    sources = element_overrides.pop("sources", None)
    if sources is None:
        sources = [make_source()]
        if extra_sources:
            sources.extend(extra_sources)

    if "production" in element_overrides:
        production = element_overrides.pop("production")
    elif with_production:
        production = ProductionBlock(
            reporting_year=reporting_year,
            mine=make_quantity(value=580.0, unit=FlowUnit.TONNES_PER_YEAR, form="metal"),
            mining_by_country=make_share_list(),
        )
    else:
        production = None

    if "end_uses" in element_overrides:
        end_uses = element_overrides.pop("end_uses")
    elif with_end_uses:
        end_uses = EndUseList(
            uses=[
                EndUse(application="solar_cdte", share_pct=40, source_id="test_source"),
                EndUse(application="other", share_pct=60, source_id="test_source"),
            ],
            completeness="complete",
        )
    else:
        end_uses = EndUseList()

    criticality = element_overrides.pop("criticality", CriticalityFlags())

    return Element(
        symbol=symbol,
        atomic_number=atomic_number,
        name=name,
        category=category,
        industrial_tier=industrial_tier,
        commercial_production=commercial_production,
        snapshot_year=snapshot_year,
        production=production,
        end_uses=end_uses,
        criticality=criticality,
        sources=sources,
        **element_overrides,
    )


@pytest.fixture
def element() -> Element:
    """A minimal valid Element ready for tests to mutate via model_copy."""
    return make_element()


@pytest.fixture
def element_factory():
    """Factory fixture that returns the make_element helper."""
    return make_element

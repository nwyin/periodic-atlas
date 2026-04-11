"""Pydantic schema for the periodic element supply chain atlas.

One YAML file per element under atlas/elements/{symbol}.yaml.
The builder loads all files, validates through these models, and emits a
unified Parquet + DuckDB snapshot for querying.

Design notes:
- Quantities use a (value, unit) pair because elements span 13 orders of
  magnitude (iron ore at 2.5 Gt/year, einsteinium at ~2 mg total ever).
- Country codes use ISO 3166-1 alpha-2 ("CN", "CD", "US") — simple to join
  against GeoJSON polygons without a translation layer.
- `source_id` is a string key referring to a Source block at the bottom
  of each file. Claims without citations fail validation.
- ResearchOnly is a separate block for elements with no commercial
  production (superheavies, research isotopes). Keeps the main
  production schema clean.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


# -------- enums --------

class IndustrialTier(int, Enum):
    """Maps to the 5-category ranking from the inquiry doc."""

    NO_SUPPLY_CHAIN = 1          # synthetic superheavies, Fr, At, Rn, Pa
    NICHE_OR_NOVELTY = 2         # Am, Pu, Cf, Tc, Os, Tl, Rb, Cs, Hg, Po, Ra, Ac, Pm, Np, Cm, Bk
    CRITICAL_SCARCE = 3          # Li, Co, Ga, Ge, REEs, PGMs, W, Nb, Ta, Re, Be, Hf, Sb, Te, Bi, He, Ne
    HIGH_VOLUME_WORKHORSE = 4    # Fe, Al, Cu, Si, Ni, H, N, O, C, P, S, K, Cl, Na, Ca, Cr, Mn, Ti, Zn, Sn, Pb, Ag, Mo, Zr, Au, Ar, Br, Ba, Sr, I, Cd, U, La, Ce, B
    UNCLASSIFIED = 0             # placeholder for elements awaiting classification


class Unit(str, Enum):
    # flow units (per year)
    TONNES_PER_YEAR = "tonnes_per_year"
    KG_PER_YEAR = "kg_per_year"
    GRAMS_PER_YEAR = "grams_per_year"
    MG_PER_YEAR = "mg_per_year"
    MILLION_CUBIC_METERS_PER_YEAR = "million_m3_per_year"
    MILLION_LITERS_PER_YEAR = "million_L_per_year"
    # stock units (cumulative / reserves / totals)
    TONNES = "tonnes"
    KG = "kg"
    GRAMS = "grams"
    MG = "mg"
    ATOMS_TOTAL = "atoms_ever_synthesized"


class PriceUnit(str, Enum):
    PER_TONNE = "usd_per_tonne"
    PER_KG = "usd_per_kg"
    PER_GRAM = "usd_per_gram"
    PER_TROY_OUNCE = "usd_per_troy_oz"


class ElementCategory(str, Enum):
    ALKALI_METAL = "alkali_metal"
    ALKALINE_EARTH = "alkaline_earth"
    TRANSITION_METAL = "transition_metal"
    POST_TRANSITION_METAL = "post_transition_metal"
    METALLOID = "metalloid"
    REACTIVE_NONMETAL = "reactive_nonmetal"
    NOBLE_GAS = "noble_gas"
    LANTHANIDE = "lanthanide"
    ACTINIDE = "actinide"
    SYNTHETIC_SUPERHEAVY = "synthetic_superheavy"


# -------- primitives --------

class Quantity(BaseModel):
    """A scalar measurement with units. Supports approximate and range values."""

    model_config = ConfigDict(extra="forbid")

    value: float = Field(description="Point estimate; use the midpoint for ranges.")
    unit: Unit
    low: float | None = Field(default=None, description="Range low bound, if reported as a range.")
    high: float | None = Field(default=None, description="Range high bound, if reported as a range.")
    approximate: bool = Field(default=False, description="True when the source reports '~' or 'about'.")
    notes: str | None = None
    source_id: str

    @model_validator(mode="after")
    def check_range(self) -> "Quantity":
        if (self.low is None) != (self.high is None):
            raise ValueError("Quantity range requires both low and high, or neither.")
        if self.low is not None and self.high is not None and self.low > self.high:
            raise ValueError(f"Quantity low ({self.low}) > high ({self.high})")
        return self


class CountryShare(BaseModel):
    """A country's share of mining, refining, reserves, etc."""

    model_config = ConfigDict(extra="forbid")

    country: str = Field(pattern=r"^[A-Z]{2}$", description="ISO 3166-1 alpha-2 country code.")
    share_pct: float = Field(ge=0, le=100)
    tonnes: float | None = Field(default=None, ge=0, description="Absolute quantity, same unit as parent production.")
    notes: str | None = None


class EndUse(BaseModel):
    """A single end-use application consuming some share of supply."""

    model_config = ConfigDict(extra="forbid")

    application: str = Field(description="Snake_case slug; canonicalize across elements for cross-element queries.")
    share_pct: float = Field(ge=0, le=100)
    notes: str | None = None


class GeopoliticalEvent(BaseModel):
    """A discrete supply-chain disruption, policy change, or market shock."""

    model_config = ConfigDict(extra="forbid")

    date: str = Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$", description="ISO date; year, year-month, or full date.")
    event: str
    impact: str | None = None
    source_id: str

    @field_validator("date", mode="before")
    @classmethod
    def stringify_date(cls, v: object) -> str:
        if isinstance(v, date):
            return v.isoformat()
        return str(v)


class CriticalityFlags(BaseModel):
    """Membership in various government critical-materials lists."""

    model_config = ConfigDict(extra="forbid")

    us_critical_2025: bool = False
    eu_crm_2024: bool = False
    eu_strategic_2024: bool = False
    doe_criticality_rank: int | None = Field(default=None, ge=1, description="DOE short-term criticality matrix rank (1 = most critical).")
    notes: str | None = None


class Price(BaseModel):
    model_config = ConfigDict(extra="forbid")

    year: int
    value: float
    unit: PriceUnit
    source_id: str
    notes: str | None = None


class Source(BaseModel):
    """A citation referenced by source_id throughout the element file."""

    model_config = ConfigDict(extra="forbid")

    id: str
    title: str | None = None
    publisher: str | None = None
    url: str | None = None
    retrieved: str | None = Field(default=None, pattern=r"^\d{4}-\d{2}-\d{2}$")

    @field_validator("retrieved", mode="before")
    @classmethod
    def stringify_retrieved(cls, v: object) -> str | None:
        if v is None:
            return None
        if isinstance(v, date):
            return v.isoformat()
        return str(v)


class ResearchOnly(BaseModel):
    """For elements with no commercial supply chain (superheavies, research isotopes).

    Replaces the full production/refining block for Tier 1 elements.
    """

    model_config = ConfigDict(extra="forbid")

    longest_lived_isotope: str | None = None
    half_life_seconds: float | None = None
    discovered_year: int | None = None
    discovered_at: str | None = Field(default=None, description="Lab or facility name.")
    total_ever_produced: Quantity | None = None
    active_production_labs: list[str] = Field(default_factory=list)
    notes: str | None = None


class ProductionBlock(BaseModel):
    """Production metrics for a single snapshot year."""

    model_config = ConfigDict(extra="forbid")

    year: int
    mine: Quantity | None = Field(default=None, description="Raw mine/extraction output.")
    refined: Quantity | None = Field(default=None, description="Refined / purified output, if distinct from mine.")
    production_form: str | None = Field(default=None, description="e.g. 'metal equivalent', 'oxide', 'concentrate'.")
    mining_by_country: list[CountryShare] = Field(default_factory=list)
    refining_by_country: list[CountryShare] = Field(default_factory=list)

    @model_validator(mode="after")
    def shares_sum_sane(self) -> "ProductionBlock":
        for label, shares in (("mining", self.mining_by_country), ("refining", self.refining_by_country)):
            if shares:
                total = sum(s.share_pct for s in shares)
                if total > 105:
                    raise ValueError(f"{label} shares sum to {total:.1f}%, exceeds 105% tolerance")
        return self


class Reserves(BaseModel):
    model_config = ConfigDict(extra="forbid")

    economic_reserves: Quantity | None = None
    resources: Quantity | None = Field(default=None, description="Broader resource base including sub-economic.")
    reserves_by_country: list[CountryShare] = Field(default_factory=list)


class OwnershipConcentration(BaseModel):
    """Single-company or single-facility concentration (e.g. CBMM for niobium)."""

    model_config = ConfigDict(extra="forbid")

    top_entity: str | None = None
    top_entity_share_pct: float | None = Field(default=None, ge=0, le=100)
    notes: str | None = None


# -------- top level --------

class Element(BaseModel):
    """One periodic element. Root object in each YAML file."""

    model_config = ConfigDict(extra="forbid")

    symbol: str = Field(pattern=r"^[A-Z][a-z]?$", max_length=3)
    atomic_number: int = Field(ge=1, le=118)
    name: str
    category: ElementCategory
    industrial_tier: IndustrialTier
    commercial_production: bool = Field(description="False for superheavies and pure-research elements.")
    form_notes: str | None = Field(default=None, description="What form the element is traded in — metal, oxide, fluorspar, etc.")

    production: ProductionBlock | None = None
    reserves: Reserves | None = None
    ownership_concentration: OwnershipConcentration | None = None
    research_only: ResearchOnly | None = None

    byproduct_of: list[str] = Field(default_factory=list, description="Parent elements this one is extracted from as a byproduct.")
    substitutes_available: Literal["none", "partial", "full"] = "none"
    substitutes_notes: str | None = None

    end_uses: list[EndUse] = Field(default_factory=list)
    criticality: CriticalityFlags = Field(default_factory=CriticalityFlags)
    prices: list[Price] = Field(default_factory=list)
    geopolitical_events: list[GeopoliticalEvent] = Field(default_factory=list)
    narrative: str | None = Field(default=None, description="Free-form summary paragraph carried over from the inquiry doc.")

    sources: list[Source] = Field(default_factory=list)

    @model_validator(mode="after")
    def commercial_vs_research_consistent(self) -> "Element":
        if self.commercial_production and self.research_only and self.production is None:
            raise ValueError(f"{self.symbol}: commercial_production=true but no production block (research_only alone is insufficient)")
        if not self.commercial_production and self.production is not None:
            raise ValueError(f"{self.symbol}: commercial_production=false but production block is set")
        return self

    @model_validator(mode="after")
    def end_use_shares_sum_sane(self) -> "Element":
        if self.end_uses:
            total = sum(e.share_pct for e in self.end_uses)
            if total > 105:
                raise ValueError(f"{self.symbol}: end_use shares sum to {total:.1f}%, exceeds 105% tolerance")
        return self

    @model_validator(mode="after")
    def source_ids_resolve(self) -> "Element":
        known = {s.id for s in self.sources}

        def check(sid: str | None, where: str) -> None:
            if sid is not None and sid not in known:
                raise ValueError(f"{self.symbol}: unknown source_id '{sid}' in {where}")

        def check_quantity(q: Quantity | None, where: str) -> None:
            if q is not None:
                check(q.source_id, where)

        if self.production:
            check_quantity(self.production.mine, "production.mine")
            check_quantity(self.production.refined, "production.refined")
        if self.reserves:
            check_quantity(self.reserves.economic_reserves, "reserves.economic_reserves")
            check_quantity(self.reserves.resources, "reserves.resources")
        if self.research_only:
            check_quantity(self.research_only.total_ever_produced, "research_only.total_ever_produced")
        for p in self.prices:
            check(p.source_id, f"prices[{p.year}]")
        for ev in self.geopolitical_events:
            check(ev.source_id, f"geopolitical_events[{ev.date}]")
        return self


# -------- loader --------

def load_element(path: Path) -> Element:
    """Load a single YAML file into a validated Element."""
    with path.open() as f:
        raw = yaml.safe_load(f)
    return Element.model_validate(raw)


def load_all_elements(elements_dir: Path) -> list[Element]:
    """Load every *.yaml file in the elements directory, sorted by atomic number."""
    elements = [load_element(p) for p in sorted(elements_dir.glob("*.yaml"))]
    return sorted(elements, key=lambda e: e.atomic_number)

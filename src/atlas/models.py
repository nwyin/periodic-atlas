"""Pydantic schema v0.2 for the periodic element supply chain atlas.

One YAML file per element under atlas/elements/{symbol}.yaml.
The builder loads all files, validates through these models, and emits a
unified Parquet + DuckDB snapshot for querying.

v0.2 design principles (derived from Codex review + Plan agent design review):

1. Every factual claim carries a source_id. The `Cited` mixin enforces this
   on Quantity, CountryShare, EndUse, OwnershipConcentration, SubstituteClaim,
   FeedstockOrigin, Price, GeopoliticalEvent. If validation passes, every
   load-bearing claim is sourced.

2. Stock and flow units are typed separately. A `StockUnit` cannot appear in
   a production flow field, and a `FlowUnit` cannot appear in a reserves
   stock field. This is enforced at validation time via model-level validators
   that introspect which field the Quantity is attached to.

3. Years are explicit and triple-layered:
     - `Element.snapshot_year` — the atlas version (e.g. 2025).
     - `ProductionBlock.reporting_year` — the year the source reported for
       (USGS MCS 2025 reports 2024 data).
     - `Source.publication_year` — when the source itself was published.
   A validator rejects `reporting_year > snapshot_year` and any
   `GeopoliticalEvent.date` beyond `snapshot_year-12-31`.

4. IsotopeMarket is a first-class sub-model for elements where the economic
   reality is an isotope market (Am-241, Tc-99m, Pu-238, Pm-147, Cf-252,
   At-211). The `production_mode` discriminator distinguishes
   stockpile-separated (Am, Pu) from reactor-generated-on-demand (Tc-99m)
   from accelerator-generated (At-211) from decay-product (Ra, Ac).

5. Grouped commodities (REEs reported as one USGS chapter) are handled
   with a `grouped_reporting` flag on ProductionBlock plus a
   `commodity_group` slug. Dedicated CommodityGroup sibling models are
   deferred to v0.3.

6. Share lists declare their completeness: `complete` (must sum to 95-105%),
   `top_producers_only` (must include an `others` bucket or pass the floor),
   or `partial` (no floor enforced).

7. Byproducts and feedstocks are modeled distinctly. `byproduct_of` is a
   list of element symbols (co-produced metals like Ga-from-Al). Feedstocks
   like natural gas for He are modeled as `FeedstockOrigin` records with
   substrate + typical concentration + source.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


# =============================================================================
# enums
# =============================================================================

class IndustrialTier(int, Enum):
    """Maps to the 5-category ranking from the inquiry doc."""

    UNCLASSIFIED = 0
    NO_SUPPLY_CHAIN = 1          # synthetic superheavies, Fr, At, Rn, Pa
    NICHE_OR_NOVELTY = 2         # Am, Pu, Cf, Tc, Os, Tl, Rb, Cs, Hg, Po, Ra, Ac, Pm, Np, Cm, Bk
    CRITICAL_SCARCE = 3          # Li, Co, Ga, Ge, REEs, PGMs, W, Nb, Ta, Re, Be, Hf, Sb, Te, Bi, He, Ne
    HIGH_VOLUME_WORKHORSE = 4    # Fe, Al, Cu, Si, Ni, H, N, O, C, P, S, K, Cl, Na, Ca, Cr, Mn, Ti, Zn, Sn, Pb, Ag, Mo, Zr, Au, Ar, Br, Ba, Sr, I, Cd, U, La, Ce, B


class FlowUnit(str, Enum):
    """Units measuring a flow (quantity per year)."""

    MILLION_TONNES_PER_YEAR = "million_tonnes_per_year"
    TONNES_PER_YEAR = "tonnes_per_year"
    KG_PER_YEAR = "kg_per_year"
    GRAMS_PER_YEAR = "grams_per_year"
    MG_PER_YEAR = "mg_per_year"
    MILLION_M3_PER_YEAR = "million_m3_per_year"
    MILLION_L_PER_YEAR = "million_L_per_year"


class StockUnit(str, Enum):
    """Units measuring a stock (cumulative total, reserves, inventory)."""

    TONNES = "tonnes"
    KG = "kg"
    GRAMS = "grams"
    MG = "mg"
    MILLION_M3 = "million_m3"
    MILLION_L = "million_L"
    ATOMS_TOTAL = "atoms_ever_synthesized"


class PriceUnit(str, Enum):
    PER_TONNE = "usd_per_tonne"
    PER_KG = "usd_per_kg"
    PER_POUND = "usd_per_lb"
    PER_GRAM = "usd_per_gram"
    PER_TROY_OUNCE = "usd_per_troy_oz"
    PER_CUBIC_METER = "usd_per_m3"
    PER_LITER = "usd_per_L"


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


Form = Literal[
    "metal",
    "alloy",
    "oxide",
    "dioxide",
    "concentrate",
    "ore",
    "halide",
    "fluoride",
    "chloride",
    "carbonate",
    "sulfate",
    "hydroxide",
    "sulfide",
    "nitride",
    "compound_other",
    "gas_crude",
    "gas_grade_a",
    "liquid_cryogenic",
    "contained_element",
    "sealed_source",
    "isotope_generator",
    "unspecified",
]


PriceBasis = Literal[
    "spot",
    "contract",
    "retail",
    "lme",
    "shfe",
    "cme",
    "china_domestic",
    "europe_domestic",
    "us_domestic",
    "price_list",
    "other",
]


IsotopeProductionMode = Literal[
    "stockpile_separated",     # Am-241, Pu-238 — legacy reprocessed stock
    "reactor_generated",        # Tc-99m, Mo-99, Pu-238 — produced in a reactor per-cycle
    "accelerator_generated",    # At-211, Ac-225 cyclotron routes
    "decay_product",            # Ra from uranium decay chain
    "naturally_occurring",      # U-235, K-40
]


ShareListCompleteness = Literal[
    "complete",
    "top_producers_only",
    "partial",
]


# =============================================================================
# primitives
# =============================================================================

class Cited(BaseModel):
    """Mixin: every factual claim must cite a source_id present in Element.sources."""

    model_config = ConfigDict(extra="forbid")

    source_id: str


class Quantity(Cited):
    """A scalar quantity with explicit unit dimension and trade form.

    `unit` is either a FlowUnit or a StockUnit. Which dimension is required
    depends on the field the Quantity is attached to — enforced at the
    parent model level (e.g. ProductionBlock rejects StockUnit in `mine`).
    """

    value: float
    unit: FlowUnit | StockUnit
    form: Form = "unspecified"
    low: float | None = None
    high: float | None = None
    approximate: bool = False
    confidence: Literal["high", "medium", "low"] = "high"
    notes: str | None = None

    @model_validator(mode="after")
    def check_range(self) -> "Quantity":
        if (self.low is None) != (self.high is None):
            raise ValueError("Quantity range requires both low and high, or neither.")
        if self.low is not None and self.high is not None and self.low > self.high:
            raise ValueError(f"Quantity low ({self.low}) > high ({self.high})")
        return self

    @property
    def is_flow(self) -> bool:
        return isinstance(self.unit, FlowUnit)

    @property
    def is_stock(self) -> bool:
        return isinstance(self.unit, StockUnit)


class CountryShare(Cited):
    """A single country's share of mining, refining, reserves, or similar."""

    country: str = Field(pattern=r"^[A-Z]{2}$", description="ISO 3166-1 alpha-2 code.")
    share_pct: float = Field(ge=0, le=100)
    quantity: Quantity | None = Field(default=None, description="Absolute output matching the parent share type's dimension.")
    confidence: Literal["high", "medium", "low"] = Field(
        default="high",
        description="Confidence in the share_pct and country attribution. Use 'low' for placeholder or derived-from-prose shares.",
    )
    notes: str | None = None


class CountryShareList(BaseModel):
    """A list of country shares with explicit completeness semantics."""

    model_config = ConfigDict(extra="forbid")

    shares: list[CountryShare] = Field(default_factory=list)
    completeness: ShareListCompleteness = "partial"

    @model_validator(mode="after")
    def check_completeness(self) -> "CountryShareList":
        if not self.shares:
            return self
        total = sum(s.share_pct for s in self.shares)
        if total > 105:
            raise ValueError(f"Shares sum to {total:.1f}%, exceeds 105% tolerance")
        if self.completeness == "complete" and total < 95:
            raise ValueError(
                f"Shares declared 'complete' but sum to only {total:.1f}%. "
                f"Either include the remaining producers or change completeness to 'top_producers_only' / 'partial'."
            )
        if self.completeness == "top_producers_only":
            has_others = any(s.country == "ZZ" for s in self.shares)
            if not has_others and total < 95:
                raise ValueError(
                    f"Shares declared 'top_producers_only' but sum to only {total:.1f}% "
                    f"and no 'ZZ' (rest-of-world) bucket present. Add an 'others' share or mark 'partial'."
                )
        return self


class EndUse(Cited):
    """A single end-use application consuming some share of supply."""

    application: str = Field(description="Snake_case slug; canonicalize across elements for cross-element queries.")
    share_pct: float = Field(ge=0, le=100)
    confidence: Literal["high", "medium", "low"] = Field(
        default="high",
        description="Confidence in the share_pct attribution. Use 'low' for placeholder or inquiry-doc-derived shares.",
    )
    notes: str | None = None


class EndUseList(BaseModel):
    model_config = ConfigDict(extra="forbid")

    uses: list[EndUse] = Field(default_factory=list)
    completeness: ShareListCompleteness = "partial"

    @model_validator(mode="after")
    def check_completeness(self) -> "EndUseList":
        if not self.uses:
            return self
        total = sum(u.share_pct for u in self.uses)
        if total > 105:
            raise ValueError(f"End-use shares sum to {total:.1f}%, exceeds 105% tolerance")
        if self.completeness == "complete" and total < 95:
            raise ValueError(f"End-uses declared 'complete' but sum to only {total:.1f}%")
        return self


class GeopoliticalEvent(Cited):
    """A discrete supply-chain disruption, policy change, or market shock."""

    date: str = Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    event: str
    impact: str | None = None

    @field_validator("date", mode="before")
    @classmethod
    def stringify_date(cls, v: object) -> str:
        if isinstance(v, date):
            return v.isoformat()
        return str(v)


class CriticalityFlags(BaseModel):
    """Membership in various government critical-materials lists.

    Field names encode "membership as-of YYYY", not a hypothetical "YYYY list revision".
    """

    model_config = ConfigDict(extra="forbid")

    us_critical_list_as_of_2025: bool = False
    eu_crm_list_as_of_2024: bool = False
    eu_strategic_list_as_of_2024: bool = False
    doe_short_term_criticality_rank: int | None = Field(default=None, ge=1)
    notes: str | None = None
    source_id: str | None = None


class Price(Cited):
    """A price point with enough context to be unambiguous."""

    year: int
    value: float
    unit: PriceUnit
    form: Form = "unspecified"
    basis: PriceBasis = "other"
    region: str | None = None
    notes: str | None = None


class Source(BaseModel):
    """A citation referenced by source_id throughout the element file."""

    model_config = ConfigDict(extra="forbid")

    id: str
    title: str | None = None
    publisher: str | None = None
    url: str | None = None
    retrieved: str | None = Field(default=None, pattern=r"^\d{4}-\d{2}-\d{2}$")
    publication_year: int | None = Field(default=None, ge=1800, le=2100)
    superseded_by: str | None = Field(default=None, description="source_id of a newer source that replaces this one.")
    source_tier: Literal["primary", "secondary", "tertiary"] = Field(
        default="secondary",
        description=(
            "Provenance tier. 'primary' = authoritative dataset read directly (USGS MCS, "
            "DOE NIDC product info). 'secondary' = trade press / market report / IEA summary. "
            "'tertiary' = Wikipedia / blog / derived. Round 1 defaults everything to secondary; "
            "round 2 assigns real tiers."
        ),
    )

    @field_validator("retrieved", mode="before")
    @classmethod
    def stringify_retrieved(cls, v: object) -> str | None:
        if v is None:
            return None
        if isinstance(v, date):
            return v.isoformat()
        return str(v)


class SubstituteClaim(Cited):
    """A claim that a substitute exists for this element in some application."""

    model_config = ConfigDict(extra="forbid")

    availability: Literal["none", "partial", "full"]
    notes: str


class FeedstockOrigin(Cited):
    """A feedstock that this element is extracted from.

    Distinct from `byproduct_of` which is restricted to element symbols.
    Feedstocks can be raw materials (natural_gas, bauxite, monazite_sand).
    """

    model_config = ConfigDict(extra="forbid")

    substrate: str = Field(description="Raw material or process stream name. Snake_case.")
    typical_concentration_pct: float | None = Field(default=None, ge=0, le=100)
    notes: str | None = None


class ResearchOnly(BaseModel):
    """For elements with no commercial supply chain (superheavies, research-only isotopes)."""

    model_config = ConfigDict(extra="forbid")

    longest_lived_isotope: str | None = None
    half_life_seconds: float | None = None
    discovered_year: int | None = None
    iupac_recognized_year: int | None = None
    discovered_at: str | None = Field(default=None, description="Lab or collaboration name.")
    production_mode: IsotopeProductionMode | None = None
    total_ever_produced: Quantity | None = None
    active_production_labs: list[str] = Field(default_factory=list)
    notes: str | None = None


class IsotopeMarket(BaseModel):
    """Economic activity centered on a single isotope rather than the element as a whole.

    Used for Am-241 (smoke detectors), Tc-99m (medical imaging), Pu-238 (RTGs),
    Pm-147 (nuclear batteries), Cf-252 (neutron sources), At-211 (targeted alpha therapy).
    """

    model_config = ConfigDict(extra="forbid")

    isotope: str = Field(description="e.g. 'Am-241', 'Tc-99m'. Format: {symbol}-{mass_number}[m] with optional metastable suffix.")
    half_life_seconds: float
    production_mode: IsotopeProductionMode
    production_quantity: Quantity | None = Field(
        default=None,
        description="Annual production rate. Optional because many isotope markets (Am-241, Pu-238) have classified or unpublished volumes.",
    )
    producers: CountryShareList = Field(default_factory=CountryShareList)
    precursor: str | None = Field(default=None, description="e.g. 'Mo-99 for Tc-99m', 'plutonium_stockpile for Am-241'.")
    delivery_form: str | None = Field(default=None, description="e.g. 'sealed sources', 'generator column'.")
    reporting_year: int
    notes: str | None = None


class ProductionBlock(BaseModel):
    """Production metrics for a single reporting year.

    `reporting_year` is the year the source reported data for — distinct from
    `Element.snapshot_year`. USGS MCS 2025 reports 2024 data, so a 2025 snapshot
    using the MCS 2025 document has `snapshot_year=2025, reporting_year=2024`.
    """

    model_config = ConfigDict(extra="forbid")

    reporting_year: int
    mine: Quantity | None = Field(default=None, description="Raw mine/extraction output (a flow).")
    refined: Quantity | None = Field(default=None, description="Refined / purified output (a flow).")
    mining_by_country: CountryShareList = Field(default_factory=CountryShareList)
    refining_by_country: CountryShareList = Field(default_factory=CountryShareList)
    grouped_reporting: bool = Field(default=False, description="True when the source reports this element as part of a larger group (e.g. REEs).")
    commodity_group: str | None = Field(default=None, description="Slug of the group (e.g. 'rare_earths', 'platinum_group_metals').")
    notes: str | None = None

    @model_validator(mode="after")
    def mine_refined_are_flows(self) -> "ProductionBlock":
        for name, q in (("mine", self.mine), ("refined", self.refined)):
            if q is not None and q.is_stock:
                raise ValueError(f"ProductionBlock.{name} must be a flow quantity, got stock unit {q.unit.value!r}")
        return self

    @model_validator(mode="after")
    def grouped_reporting_consistent(self) -> "ProductionBlock":
        if self.grouped_reporting and not self.commodity_group:
            raise ValueError("grouped_reporting=true requires commodity_group to be set")
        if self.commodity_group and not self.grouped_reporting:
            raise ValueError("commodity_group set but grouped_reporting is false")
        return self


class Reserves(BaseModel):
    model_config = ConfigDict(extra="forbid")

    economic_reserves: Quantity | None = None
    resources: Quantity | None = None
    reserves_by_country: CountryShareList = Field(default_factory=CountryShareList)
    notes: str | None = None

    @model_validator(mode="after")
    def reserves_are_stocks(self) -> "Reserves":
        for name, q in (("economic_reserves", self.economic_reserves), ("resources", self.resources)):
            if q is not None and q.is_flow:
                raise ValueError(f"Reserves.{name} must be a stock quantity, got flow unit {q.unit.value!r}")
        return self


class OwnershipConcentration(Cited):
    """Single-company or single-facility concentration."""

    model_config = ConfigDict(extra="forbid")

    top_entity: str | None = None
    top_entity_share_pct: float | None = Field(default=None, ge=0, le=100)
    notes: str | None = None


# =============================================================================
# top level
# =============================================================================

class Element(BaseModel):
    """One periodic element. Root object in each YAML file."""

    model_config = ConfigDict(extra="forbid")

    symbol: str = Field(pattern=r"^[A-Z][a-z]?$", max_length=3)
    atomic_number: int = Field(ge=1, le=118)
    name: str
    category: ElementCategory
    industrial_tier: IndustrialTier
    commercial_production: bool
    snapshot_year: int = Field(ge=1900, le=2100, description="The atlas version year. All reporting_year fields must be <= this.")
    form_notes: str | None = None

    production: ProductionBlock | None = None
    reserves: Reserves | None = None
    ownership_concentration: OwnershipConcentration | None = None
    isotope_markets: list[IsotopeMarket] = Field(default_factory=list)
    research_only: ResearchOnly | None = None

    byproduct_of: list[str] = Field(
        default_factory=list,
        description="Parent element symbols this element is co-produced with. Element symbols only.",
    )
    feedstock_origins: list[FeedstockOrigin] = Field(
        default_factory=list,
        description="Non-element feedstocks like natural_gas, bauxite, monazite_sand.",
    )
    substitutes: list[SubstituteClaim] = Field(default_factory=list)

    end_uses: EndUseList = Field(default_factory=EndUseList)
    criticality: CriticalityFlags = Field(default_factory=CriticalityFlags)
    prices: list[Price] = Field(default_factory=list)
    geopolitical_events: list[GeopoliticalEvent] = Field(default_factory=list)
    narrative: str | None = None

    sources: list[Source] = Field(default_factory=list)

    @field_validator("byproduct_of")
    @classmethod
    def byproduct_are_symbols(cls, v: list[str]) -> list[str]:
        for sym in v:
            if not (1 <= len(sym) <= 3 and sym[0].isupper() and sym[1:].islower()):
                raise ValueError(f"byproduct_of entries must be element symbols (e.g. 'Al'), got {sym!r}")
        return v

    @model_validator(mode="after")
    def commercial_vs_research_consistent(self) -> "Element":
        has_production = self.production is not None
        has_isotopes = bool(self.isotope_markets)
        has_research = self.research_only is not None
        if self.commercial_production and not (has_production or has_isotopes):
            raise ValueError(
                f"{self.symbol}: commercial_production=true requires either a production block or at least one isotope_market"
            )
        if not self.commercial_production and (has_production or has_isotopes):
            raise ValueError(
                f"{self.symbol}: commercial_production=false but production or isotope_markets is set"
            )
        if not has_research and not has_production and not has_isotopes:
            raise ValueError(
                f"{self.symbol}: element has no production, no isotope_markets, and no research_only — nothing to describe"
            )
        return self

    @model_validator(mode="after")
    def reporting_year_in_range(self) -> "Element":
        if self.production and self.production.reporting_year > self.snapshot_year:
            raise ValueError(
                f"{self.symbol}: production.reporting_year={self.production.reporting_year} exceeds snapshot_year={self.snapshot_year}"
            )
        for i, im in enumerate(self.isotope_markets):
            if im.reporting_year > self.snapshot_year:
                raise ValueError(
                    f"{self.symbol}: isotope_markets[{i}].reporting_year={im.reporting_year} exceeds snapshot_year={self.snapshot_year}"
                )
        for i, p in enumerate(self.prices):
            if p.year > self.snapshot_year:
                raise ValueError(f"{self.symbol}: prices[{i}].year={p.year} exceeds snapshot_year={self.snapshot_year}")
        return self

    @model_validator(mode="after")
    def events_within_snapshot(self) -> "Element":
        horizon = f"{self.snapshot_year}-12-31"
        for i, ev in enumerate(self.geopolitical_events):
            if ev.date > horizon:
                raise ValueError(
                    f"{self.symbol}: geopolitical_events[{i}].date={ev.date} is beyond snapshot horizon {horizon}. "
                    f"Events beyond the snapshot year belong in a later snapshot, not this one."
                )
        return self

    @model_validator(mode="after")
    def source_ids_resolve(self) -> "Element":
        known = {s.id for s in self.sources}
        if not known and self._has_any_claim():
            raise ValueError(f"{self.symbol}: element has claims but no sources list")

        def check(sid: str | None, where: str) -> None:
            if sid is None:
                return
            if sid not in known:
                raise ValueError(f"{self.symbol}: unknown source_id {sid!r} referenced from {where}")

        check(self.criticality.source_id, "criticality.source_id")

        if self.production:
            if self.production.mine:
                check(self.production.mine.source_id, "production.mine")
            if self.production.refined:
                check(self.production.refined.source_id, "production.refined")
            for i, s in enumerate(self.production.mining_by_country.shares):
                check(s.source_id, f"production.mining_by_country[{i}]")
                if s.quantity:
                    check(s.quantity.source_id, f"production.mining_by_country[{i}].quantity")
            for i, s in enumerate(self.production.refining_by_country.shares):
                check(s.source_id, f"production.refining_by_country[{i}]")
                if s.quantity:
                    check(s.quantity.source_id, f"production.refining_by_country[{i}].quantity")

        if self.reserves:
            if self.reserves.economic_reserves:
                check(self.reserves.economic_reserves.source_id, "reserves.economic_reserves")
            if self.reserves.resources:
                check(self.reserves.resources.source_id, "reserves.resources")
            for i, s in enumerate(self.reserves.reserves_by_country.shares):
                check(s.source_id, f"reserves.reserves_by_country[{i}]")

        if self.ownership_concentration:
            check(self.ownership_concentration.source_id, "ownership_concentration")

        for i, im in enumerate(self.isotope_markets):
            if im.production_quantity:
                check(im.production_quantity.source_id, f"isotope_markets[{i}].production_quantity")
            for j, s in enumerate(im.producers.shares):
                check(s.source_id, f"isotope_markets[{i}].producers[{j}]")

        for i, u in enumerate(self.end_uses.uses):
            check(u.source_id, f"end_uses[{i}]")

        for i, f in enumerate(self.feedstock_origins):
            check(f.source_id, f"feedstock_origins[{i}]")

        for i, sub in enumerate(self.substitutes):
            check(sub.source_id, f"substitutes[{i}]")

        for i, p in enumerate(self.prices):
            check(p.source_id, f"prices[{i}]")

        for i, ev in enumerate(self.geopolitical_events):
            check(ev.source_id, f"geopolitical_events[{i}]")

        if self.research_only and self.research_only.total_ever_produced:
            check(self.research_only.total_ever_produced.source_id, "research_only.total_ever_produced")

        return self

    def _has_any_claim(self) -> bool:
        return bool(
            self.production
            or self.reserves
            or self.isotope_markets
            or self.ownership_concentration
            or self.end_uses.uses
            or self.prices
            or self.geopolitical_events
            or self.feedstock_origins
            or self.substitutes
            or (self.research_only and self.research_only.total_ever_produced)
        )


# =============================================================================
# loader
# =============================================================================

def load_element(path: Path) -> Element:
    """Load a single YAML file into a validated Element."""
    with path.open() as f:
        raw = yaml.safe_load(f)
    return Element.model_validate(raw)


def load_all_elements(elements_dir: Path) -> list[Element]:
    """Load every *.yaml file in the elements directory, sorted by atomic number."""
    elements = [load_element(p) for p in sorted(elements_dir.glob("*.yaml"))]
    return sorted(elements, key=lambda e: e.atomic_number)

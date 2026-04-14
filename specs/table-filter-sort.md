---
title: "Feature spec: element table filter and sort"
tags: [atlas, viewer, spec, table]
status: draft
created: 2026-04-14
---

# Feature spec: element table filter and sort

## 1. Goal

Add client-side filter, sort, and free-text search to the `<table class="element-table">` on `viewer/index.html`. No server round-trips; all state lives in the URL query string. The feature makes the ~118-row table navigable by criticality, tier, category, producer country, end-use bucket, and byproduct provenance, and adds two derived columns (top mining country share, HHI) that expose supply-concentration at a glance.

---

## 2. Scope / locked decisions

### In scope

- Filter by: US critical list, EU CRM, EU strategic, DOE rank presence; industrial tier (0–4); element category; commercial production (boolean); end-use bucket (curated set, see §4.3); producer country (mining); byproduct-only elements (non-empty `byproduct_of`).
- Sort any existing column plus two new derived columns: top-country share (mining) and HHI (mining).
- Free-text search across symbol, name, and atomic number.
- URL state: `?filters=us_critical,tier_3&sort=hhi_mining_desc&q=cobalt` for deep-linkable views.
- Empty-state messaging when zero rows match.
- Accessible keyboard navigation of filter chips and column headers.
- Two new derived columns rendered by `build_viewer.py` as `data-*` attributes (not visible table cells initially; toggled visible by JS when column header is clicked).

### Out of scope (v1)

- Server-side search or indexing.
- Persist filter state to `localStorage` (URL is sufficient for sharing; cross-tab persistence deferred).
- Refining HHI as a visible column (available in the metadata payload for heatmap; surfaced on demand in a tooltip only).
- Reserves HHI column.
- End-use filter with more than one active bucket simultaneously (multi-select deferred; single-select covers the core use cases).
- Animated row transitions on filter change.
- Filter count badges on inactive filter chips.
- Mobile breakpoint redesign of the filter bar (defer; the table is already horizontally scrollable).

---

## 3. UX design

### 3.1 Layout

The filter controls live in a `<div class="table-controls">` block inserted immediately before `<table class="element-table">` in `_index_body`. Structure:

```
┌─ .table-controls ──────────────────────────────────────────────────────────┐
│  [🔍 input.table-search]          [Clear all filters ×]                   │
│                                                                            │
│  Criticality: [US Critical] [EU CRM] [EU Strategic] [DOE rank]            │
│  Tier:        [0] [1] [2] [3] [4]                                          │
│  Category:    [transition_metal] [lanthanide] … (10 categories)            │
│  Production:  [Commercial only] [No commercial]                            │
│  End-use:     <select.enduse-select> ▾                                     │
│  Country:     <select.country-select> ▾   [→ country page]                │
│  Byproduct:   [Byproduct-only]                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

Filter chips are `<button class="filter-chip" data-filter-key="..." data-filter-val="...">`. Active chips gain `class="filter-chip active"`. The "Clear all filters" button is hidden when no filter is active.

End-use and country filters are `<select>` elements (not chips) because the option sets are large. The country select is populated at page load from the metadata payload; its first option is `<option value="">All countries</option>`.

### 3.2 Column sort affordances

Every `<th>` in `<thead>` gains `role="columnheader"` and `aria-sort="none|ascending|descending"`. Clicking a header cycles none → ascending → descending → none. A small `▲`/`▼` icon (CSS `::after` pseudo-element, no extra DOM) indicates active sort direction. Two new columns are appended to the header row: `Top country (mining)` and `HHI (mining)`.

Numeric sort (`atomic_number`, `tier`, `top_country_share_pct`, `hhi_mining`) uses numeric comparison; all other columns sort lexicographically on the text content of the cell.

### 3.3 Search box

`<input type="search" class="table-search" placeholder="Symbol, name, or number…" aria-label="Search elements">`. Positioned top-left of `.table-controls`. Debounced 150 ms. Matched text is not highlighted in v1 (deferred).

### 3.4 URL state

The JS module reads and writes `window.location.search` using `URLSearchParams` without triggering navigation (`history.replaceState`). Parameters:

| Param | Example values | Semantics |
|---|---|---|
| `q` | `cobalt` | Free-text search string |
| `filters` | `us_critical,tier_3,eu_crm` | Comma-separated active chip filter keys |
| `enduse` | `batteries` | Active end-use bucket slug |
| `country` | `CD` | Active producer country ISO-2 |
| `sort` | `hhi_mining_desc` | Column key + `_asc` or `_desc` |

On page load, `table_filter.js` reads these params and reapplies state before the first paint. This makes deep links work correctly including browser back/forward.

Filter key encoding: `us_critical`, `eu_crm`, `eu_strategic`, `doe_rank`, `tier_0`…`tier_4`, `cat_transition_metal`…`cat_synthetic_superheavy`, `commercial_only`, `no_commercial`, `byproduct_only`.

Sort column keys: `symbol`, `atomic_number`, `name`, `category`, `tier`, `commercial`, `criticality` (sorts by number of active flags, descending), `top_country_share`, `hhi_mining`.

### 3.5 Empty state

When zero `<tr>` elements are visible after filtering, a `<tr class="table-empty-state">` row (hidden by default via CSS) is made visible. Its single `<td colspan="9">` reads: `No elements match the active filters. Clear filters to reset.` with an inline "Clear filters" button.

### 3.6 Keyboard access

- Filter chips are `<button>` elements; tab-navigable, activated by Space/Enter.
- Column headers are `<th tabindex="0">`; activated by Enter.
- The country and end-use selects are native `<select>` — fully keyboard accessible without extra work.
- Pressing Escape while the search box is focused clears the search field.

---

## 4. Data model

### 4.1 Element metadata index (shared with heatmap and country-page specs)

`build_viewer.py` emits a single JSON payload embedded as:

```html
<script id="atlas-element-index" type="application/json">...</script>
```

immediately before `<table class="element-table">` in `_index_body`. This is the **shared element metadata index** that the heatmap choropleth (see `specs/heatmap.md`) also consumes for its fill-scale. Whoever lands first creates this payload; the other spec reads it via `document.getElementById('atlas-element-index')`.

Schema (one object per element, array ordered by atomic number):

```jsonc
[
  {
    "symbol": "Co",
    "atomic_number": 27,
    "name": "cobalt",
    "category": "transition_metal",        // ElementCategory value
    "tier": 3,                             // IndustrialTier int 0–4
    "commercial": true,
    "byproduct_of": ["Cu", "Ni"],          // empty array if none
    "criticality": {
      "us_critical": true,
      "eu_crm": true,
      "eu_strategic": true,
      "doe_rank": null                     // int or null
    },
    "end_use_buckets": ["superalloys", "chemicals", "cutting_tools"],
    "producer_countries_mining": ["CD", "ID", "RU", "CA"],  // excludes ZZ
    "top_country_mining": "CD",            // ISO-2 of highest share_pct; null if no mining data
    "top_country_share_pct": 76.0,         // float; null if no mining data
    "hhi_mining": 5912,                    // int 0–10000; null if no mining data
    "hhi_refining": 3640                   // int 0–10000; null if no refining data
  },
  ...
]
```

`end_use_buckets` contains zero or more bucket slugs from the curated bucket list (§4.3). A single element may appear in multiple buckets if its raw slugs map to multiple buckets (common for cross-cutting elements like Ni or Pt).

Elements with no `mining_by_country` data (noble gases, synthetics, elements with only isotope markets) have `top_country_mining: null`, `top_country_share_pct: null`, `hhi_mining: null`. These elements sort to the bottom (nulls last) when sorting by those columns.

### 4.2 HHI and top-country-share computation

Both are computed in `build_viewer.py` in a new helper function `_compute_hhi(shares: list[dict]) -> tuple[int | None, str | None, float | None]` that returns `(hhi, top_country_iso2, top_share_pct)`.

Formula: `HHI = round(sum(s.share_pct ** 2 for s in shares if s.country != "ZZ"))`. The `ZZ` rest-of-world bucket is excluded from HHI because including it would inflate concentration for elements where other countries absorb the remainder. The `ZZ` bucket is also excluded from `top_country_mining` selection; if the largest named country has the highest share, that is the top country.

Handling edge cases:

| Situation | Behaviour |
|---|---|
| `mining_by_country.shares` is empty | Return `(None, None, None)` |
| All shares are `ZZ` | Return `(None, None, None)` |
| Only one named country | HHI = `round(share_pct ** 2)` (possibly 10000 for monopoly) |
| `completeness = "partial"` | Compute HHI from available shares; JS renders value with `~` prefix and `title` tooltip "Based on partial data" |

The `_compute_hhi` helper is called in `_build_element_index` (new function, see §5) for mining shares and again for refining shares.

### 4.3 End-use canonicalization

There are approximately 397 unique raw `application` slugs across all element YAMLs. These are too granular to filter on directly. A curated mapping reduces them to 14 buckets. The mapping is defined as a constant `END_USE_BUCKET_MAP: dict[str, str]` at the top of `build_viewer.py`:

```python
END_USE_BUCKET_MAP: dict[str, str] = {
    # batteries
    "batteries": "batteries",
    "battery_alloys_nimh": "batteries",
    "li_ion_batteries": "batteries",
    "lithium_ion_batteries": "batteries",
    "battery_cathodes": "batteries",
    # magnets
    "ndfeb_permanent_magnets": "magnets",
    "permanent_magnets": "magnets",
    "ceramic_ferrite_magnets": "magnets",
    "magnets": "magnets",
    # superalloys
    "superalloys_aircraft_turbines": "superalloys",
    "superalloys": "superalloys",
    "superalloys_and_high_performance_alloys": "superalloys",
    "aerospace_and_defense": "superalloys",
    # semiconductors
    "semiconductors": "semiconductors",
    "semiconductor_and_electronics": "semiconductors",
    "electronics": "semiconductors",
    "photovoltaics": "semiconductors",
    "cdte_solar_and_semiconductors": "semiconductors",
    # catalysts
    "catalysts": "catalysts",
    "autocatalysts": "catalysts",
    "autocatalysts_gasoline_twc": "catalysts",
    "chemical_catalysts": "catalysts",
    "catalysts_fcc_and_auto": "catalysts",
    "catalysts_and_polishing": "catalysts",
    # fertilizers
    "ammonia_and_fertilizers": "fertilizers",
    "agriculture_and_fertilizers": "fertilizers",
    "fertilizers": "fertilizers",
    # steel_and_alloys
    "alloy_steels": "steel_and_alloys",
    "alloy_steels_and_cast_irons": "steel_and_alloys",
    "stainless_steel": "steel_and_alloys",
    "steel": "steel_and_alloys",
    "cemented_carbides": "cutting_tools",
    "cemented_carbides_cutting_tools": "cutting_tools",
    # cutting_tools (carbides)
    "cutting_tools": "cutting_tools",
    # glass_and_ceramics
    "glass": "glass_and_ceramics",
    "ceramics_and_glass": "glass_and_ceramics",
    "ceramics_glass_optical": "glass_and_ceramics",
    "optical_fiber": "glass_and_ceramics",
    # pigments_and_coatings
    "pigments_and_coatings": "pigments_and_coatings",
    "coatings_and_plating": "pigments_and_coatings",
    "plating": "pigments_and_coatings",
    # nuclear
    "nuclear_fuel": "nuclear",
    "nuclear_reactors": "nuclear",
    "nuclear_and_isotope_applications": "nuclear",
    # medical
    "medical_devices": "medical",
    "medical_imaging": "medical",
    "radiation_therapy": "medical",
    "medical_isotopes": "medical",
    # lighting
    "fluorescent_lamps": "lighting",
    "lighting_and_displays": "lighting",
    "leds": "lighting",
}
```

The 14 bucket labels: `batteries`, `magnets`, `superalloys`, `semiconductors`, `catalysts`, `fertilizers`, `steel_and_alloys`, `cutting_tools`, `glass_and_ceramics`, `pigments_and_coatings`, `nuclear`, `medical`, `lighting`, `other`.

Raw slugs not in `END_USE_BUCKET_MAP` map to `"other"`. The `"other"` bucket is only added to an element's `end_use_buckets` list if it has at least one unmapped slug with `share_pct > 0`. Elements with no end-uses get an empty list.

This mapping must be expanded as new elements are added. An assertion in `_build_element_index` logs a warning (does not raise) when an unmapped slug is encountered, so the mapping can be extended incrementally.

### 4.4 `data-*` attributes on table rows

Each `<tr>` in `<tbody>` gets the following attributes for JS-driven show/hide without re-parsing the payload on every filter change:

```html
<tr
  data-symbol="Co"
  data-atomic-number="27"
  data-name="cobalt"
  data-category="transition_metal"
  data-tier="3"
  data-commercial="true"
  data-byproduct="true"
  data-us-critical="true"
  data-eu-crm="true"
  data-eu-strategic="true"
  data-doe-rank="0"          <!-- 0 = absent; positive int = rank present -->
  data-enduse-buckets="superalloys chemicals cutting_tools"   <!-- space-separated -->
  data-producer-countries="CD ID RU CA"                       <!-- space-separated ISO-2, no ZZ -->
  data-top-country="CD"
  data-top-share="76.0"      <!-- "" if null -->
  data-hhi-mining="5912"     <!-- "" if null -->
>
```

The two new `<td>` cells for top country and HHI are appended by JS at load time (reading from the metadata payload), not emitted by `build_viewer.py`. This keeps the HTML output minimal and avoids rebuilding the table structure. The cells are inserted into every row's DOM via a one-time `initDerivedColumns()` call in `table_filter.js`.

---

## 5. Implementation plan

Steps are ordered; each depends on the previous.

### Step 1 — `_compute_hhi` helper (~25 lines)

**File:** `scripts/build_viewer.py`  
**Location:** after `_criticality_badges` (~line 275)

```python
def _compute_hhi(shares: list[dict]) -> tuple[int | None, str | None, float | None]:
    """Return (hhi, top_country, top_share_pct) from a list of CountryShare dicts.

    Excludes the ZZ rest-of-world bucket from both HHI and top-country selection.
    Returns (None, None, None) if no named-country shares exist.
    """
```

Accepts the same `list[dict]` shape as rows from `atlas_shares` (`{"country": ..., "share_pct": ...}`). Filters out `country == "ZZ"`, computes HHI from the remainder, selects the top country.

### Step 2 — `END_USE_BUCKET_MAP` constant (~70 lines)

**File:** `scripts/build_viewer.py`  
**Location:** near other top-level constants, after `WIKIPEDIA_NAME_OVERRIDES` (~line 70)

Add the full `END_USE_BUCKET_MAP: dict[str, str]` constant as specified in §4.3.

### Step 3 — `_build_element_index` function (~80 lines)

**File:** `scripts/build_viewer.py`  
**Location:** after `_compute_hhi`

```python
def _build_element_index(
    elements_list: list[dict],
    mining_shares_by_symbol: dict[str, list[dict]],
    refining_shares_by_symbol: dict[str, list[dict]],
    end_uses_by_symbol: dict[str, list[dict]],
    byproduct_by_symbol: dict[str, list[str]],
) -> str:
    """Return JSON string for the atlas-element-index <script> block."""
```

Iterates `elements_list`, calls `_compute_hhi` for mining and refining shares, maps end-use slugs through `END_USE_BUCKET_MAP`, and serializes the result to compact JSON. Logs (does not raise) for unmapped slugs.

### Step 4 — Extend `generate_viewer` to fetch byproduct data and call `_build_element_index` (~40 lines)

**File:** `scripts/build_viewer.py`  
**Location:** inside `generate_viewer`, in the DuckDB query block (~line 1628)

Add a query for `atlas_byproducts` (or equivalent column on `atlas_elements`):

```python
byproduct_df = con.execute(
    "SELECT symbol, byproduct_of FROM atlas_elements ORDER BY atomic_number"
).df()
byproduct_by_symbol: dict[str, list[str]] = {}
for row in byproduct_df.to_dict(orient="records"):
    raw = row.get("byproduct_of") or []
    byproduct_by_symbol[row["symbol"]] = list(raw) if isinstance(raw, list) else []
```

Then after the existing queries, build the index:

```python
element_index_json = _build_element_index(
    elements_list,
    mining_refining_shares_by_symbol,   # already fetched; split by share_type
    end_uses_by_symbol,
    byproduct_by_symbol,
)
```

Pass `element_index_json` into `_index_body`.

### Step 5 — Extend `_index_body` to emit the payload and filter UI (~60 lines added)

**File:** `scripts/build_viewer.py`  
**Function:** `_index_body` (~line 1048)

Add `element_index_json: str` parameter. Before the table, emit:

```html
<script id="atlas-element-index" type="application/json">{element_index_json}</script>
<div class="table-controls" id="table-controls">
  <div class="table-search-row">
    <input type="search" class="table-search" id="table-search"
           placeholder="Symbol, name, or number…" aria-label="Search elements">
    <button class="clear-all-btn" id="clear-all-btn" hidden>Clear all filters ×</button>
  </div>
  <div class="filter-row" data-filter-group="criticality" aria-label="Criticality filters">
    <span class="filter-group-label">Criticality</span>
    <button class="filter-chip" data-filter-key="us_critical">US Critical</button>
    <button class="filter-chip" data-filter-key="eu_crm">EU CRM</button>
    <button class="filter-chip" data-filter-key="eu_strategic">EU Strategic</button>
    <button class="filter-chip" data-filter-key="doe_rank">DOE rank</button>
  </div>
  <div class="filter-row" data-filter-group="tier" aria-label="Industrial tier filters">
    <span class="filter-group-label">Tier</span>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="0">0</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="1">1</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="2">2</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="3">3</button>
    <button class="filter-chip" data-filter-key="tier" data-filter-val="4">4</button>
  </div>
  <div class="filter-row" data-filter-group="category" aria-label="Category filters">
    <span class="filter-group-label">Category</span>
    <!-- 10 chips, one per ElementCategory value, label humanized -->
  </div>
  <div class="filter-row" data-filter-group="misc" aria-label="Miscellaneous filters">
    <span class="filter-group-label">Other</span>
    <button class="filter-chip" data-filter-key="commercial_only">Commercial only</button>
    <button class="filter-chip" data-filter-key="no_commercial">No commercial production</button>
    <button class="filter-chip" data-filter-key="byproduct_only">Byproduct-only</button>
  </div>
  <div class="filter-row" data-filter-group="selects">
    <span class="filter-group-label">End-use</span>
    <select class="filter-select" id="enduse-select" aria-label="Filter by end-use bucket">
      <option value="">All end-uses</option>
      <!-- 14 options injected by JS from END_USE_BUCKETS constant -->
    </select>
    <span class="filter-group-label">Producer country</span>
    <select class="filter-select" id="country-select" aria-label="Filter by producer country (mining)">
      <option value="">All countries</option>
      <!-- options injected by JS from element index -->
    </select>
    <a class="country-page-link" id="country-page-link" href="#" hidden>View country page →</a>
  </div>
</div>
```

Add `data-*` attributes to every `<tr>` as specified in §4.4. Add two new `<th>` cells (`Top country` and `HHI`) to the header row.

### Step 6 — `viewer/assets/table_filter.js` (~350 lines)

New file. Loaded via `<script src="assets/table_filter.js" defer></script>` added to `_page_shell` (or injected inline in `_index_body`). Structure:

```
table_filter.js
├── Constants
│   ├── END_USE_BUCKETS: string[]       (14 bucket slugs, human labels)
│   └── SORT_COLUMNS: Record<string, SortFn>
├── State
│   ├── activeFilters: Set<string>
│   ├── activeEnduse: string | null
│   ├── activeCountry: string | null
│   ├── sortKey: string | null
│   ├── sortDir: 'asc' | 'desc' | null
│   └── searchQuery: string
├── init()
│   ├── parseUrlState()
│   ├── buildSelectOptions()          — populates country + enduse selects from index
│   ├── initDerivedColumns()          — inserts Top country + HHI <td> into every row
│   ├── attachEventListeners()
│   └── applyState()
├── applyState()
│   ├── filterRows()                  — sets row.hidden based on all active filters
│   ├── sortRows()                    — reorders <tbody> children
│   ├── updateHeaderArrows()
│   ├── updateChipActiveClass()
│   ├── updateEmptyState()
│   ├── updateCountryPageLink()       — shows/hides the "View country page →" link
│   └── pushUrlState()
└── Helpers
    ├── matchesFilters(rowEl, index): boolean
    ├── compareRows(a, b, key, dir): number
    ├── debounce(fn, ms): fn
    └── humanizeCategory(slug): string
```

`filterRows` reads `data-*` attributes directly from each `<tr>` (string attribute access, no dataset parsing overhead for booleans — compare string `"true"`). For end-use bucket filter: `row.dataset.endusesBuckets.split(' ').includes(activeEnduse)`. For country filter: `row.dataset.producerCountries.split(' ').includes(activeCountry)`.

`sortRows` collects all non-hidden rows into an array, sorts, and re-appends to `<tbody>`. When a sort key is `null`, rows are restored to their original DOM order (tracked by `data-atomic-number` as the original sort key).

`initDerivedColumns` reads the `atlas-element-index` payload once, builds a `Map<symbol, entry>`, then for each `<tr>` creates two `<td>` elements and appends them. Top-country cell shows the ISO-2 code; HHI cell shows the integer with a `~` prefix if `completeness` was `partial`. The HHI `<td>` has a `title` attribute: `"Herfindahl-Hirschman Index (mining). Higher = more concentrated. Max 10,000 = single-country monopoly."`.

`updateCountryPageLink`: when `activeCountry` is set, sets the `<a>` href to `countries/{activeCountry}.html` and removes `hidden`. This anticipates the `specs/country-page.md` feature. The link is rendered in the DOM now but the target pages do not exist until that feature lands; in the interim, the link is suppressed by checking `COUNTRY_PAGES_ENABLED` (a constant set to `false` in v1, flipped to `true` when country pages ship).

### Step 7 — CSS additions to `atlas.css` (~80 lines added to `CSS` constant)

**File:** `scripts/build_viewer.py`, `CSS` constant

Add rules for: `.table-controls`, `.table-search-row`, `.table-search`, `.filter-row`, `.filter-group-label`, `.filter-chip`, `.filter-chip.active`, `.filter-chip:hover`, `.filter-chip:focus-visible`, `.filter-select`, `.clear-all-btn`, `.country-page-link`, `.table-empty-state td`, `.sort-indicator` (the `::after` arrow on sorted `<th>`), `.th-sortable` (cursor pointer + hover bg).

Color tokens reuse existing CSS variables: `--accent` for active chips, `--surface` for chip base, `--border` for chip outline.

Dark-mode overrides: none needed — all new rules use existing CSS variables.

### Step 8 — Wire `table_filter.js` into page shell

**File:** `scripts/build_viewer.py`, `_page_shell` function or inline in `_index_body`

Add `<script src="assets/table_filter.js" defer></script>` to `_page_shell`'s `<head>` block (or conditionally only on the index page). The simpler approach is to add it to `_page_shell` behind a parameter `include_table_filter: bool = False` and pass `True` when building `index.html`.

Also copy `table_filter.js` from `viewer/assets/table_filter.js` into the output `assets_dir` during `generate_viewer` (same pattern as `charts_*.js`).

---

## 6. Testing

New test cases in `tests/test_build_viewer.py`. Add a `FILTER_SYMBOLS` fixture set: `["Co", "Li", "Og", "He", "Nd"]` — covers commercial+critical, commercial+critical, no-commercial, noble-gas-no-mining, lanthanide-REE.

### TF-INV-1: Element index payload is valid JSON and contains all elements

```python
def test_element_index_json_present_and_complete(index_html):
    match = re.search(r'id="atlas-element-index"[^>]*>(\[.*?\])<\/script>', index_html, re.DOTALL)
    assert match, "atlas-element-index script block not found"
    index = json.loads(match.group(1))
    symbols = {el["symbol"] for el in index}
    assert "Co" in symbols and "He" in symbols and "Og" in symbols
    assert len(index) == len(EXPECTED_SYMBOLS)   # extend to full count once stabilized
```

### TF-INV-2: HHI computation correctness

```python
def test_compute_hhi_cobalt():
    from build_viewer import _compute_hhi
    # Co mining: CD=76, ID=10, RU=3, CA=2, PH=1, AU=1, CU=1, PG=1, TR=1, MG=1, US=0, ZZ=2
    shares = [
        {"country": "CD", "share_pct": 76},
        {"country": "ID", "share_pct": 10},
        {"country": "RU", "share_pct": 3},
        {"country": "ZZ", "share_pct": 2},   # excluded from HHI
        # ... etc
    ]
    hhi, top_country, top_pct = _compute_hhi(shares)
    assert top_country == "CD"
    assert top_pct == 76.0
    assert hhi == round(76**2 + 10**2 + 3**2 + ... )  # compute expected

def test_compute_hhi_no_data():
    from build_viewer import _compute_hhi
    hhi, top, pct = _compute_hhi([])
    assert hhi is None and top is None and pct is None

def test_compute_hhi_zz_only():
    from build_viewer import _compute_hhi
    hhi, top, pct = _compute_hhi([{"country": "ZZ", "share_pct": 100}])
    assert hhi is None
```

### TF-INV-3: `data-*` attributes present on Co row

```python
def test_data_attrs_cobalt(index_html):
    assert 'data-symbol="Co"' in index_html
    assert 'data-us-critical="true"' in index_html
    assert 'data-byproduct="true"' in index_html
    assert 'data-top-country="CD"' in index_html
    assert 'data-hhi-mining="' in index_html   # value checked separately
```

### TF-INV-4: Filter UI DOM present

```python
def test_filter_ui_in_index(index_html):
    assert 'class="table-controls"' in index_html
    assert 'data-filter-key="us_critical"' in index_html
    assert 'id="enduse-select"' in index_html
    assert 'id="country-select"' in index_html
    assert 'id="table-search"' in index_html
```

### TF-INV-5: He (noble gas, no mining) gets null HHI fields

```python
def test_he_null_hhi_in_index(index_html):
    match = re.search(r'id="atlas-element-index"[^>]*>(\[.*?\])<\/script>', index_html, re.DOTALL)
    index = json.loads(match.group(1))
    he = next(el for el in index if el["symbol"] == "He")
    assert he["hhi_mining"] is None
    assert he["top_country_mining"] is None
```

### TF-INV-6: End-use bucket mapping — Co maps to "superalloys" and "chemicals" and "cutting_tools"

```python
def test_enduse_buckets_cobalt(index_html):
    index = _parse_element_index(index_html)
    co = next(el for el in index if el["symbol"] == "Co")
    assert "superalloys" in co["end_use_buckets"]
    assert "cutting_tools" in co["end_use_buckets"]
```

### TF-INV-7: `table_filter.js` is copied into assets

```python
def test_table_filter_js_deployed(tmp_viewer_dir):
    assert (tmp_viewer_dir / "assets" / "table_filter.js").exists()
```

---

## 7. Cross-feature dependencies

### 7.1 Shared element metadata payload (heatmap)

`specs/heatmap.md` needs the same `atlas-element-index` JSON block for its fill scale (HHI, tier, criticality). **Coordination rule:** whichever feature lands first adds the `<script id="atlas-element-index">` block and the `_build_element_index` / `_compute_hhi` functions. The second feature reads the payload without modifying it. If the heatmap feature needs additional fields (e.g. `reserves_hhi`), those fields should be added as a coordinated extension rather than a separate payload, to avoid two competing `<script>` blocks.

The shared payload schema (§4.1) is the proposed contract. Flag any field additions in the PR description.

### 7.2 Country page links (country-page spec)

The "View country page →" link in the producer-country filter (§3.1, step 6) points to `countries/{ISO}.html`. The country-page spec should confirm:

- The URL scheme `viewer/countries/{ISO}.html` (ISO uppercase, no subdirectory nesting).
- Whether a landing index at `viewer/countries/index.html` exists (useful for the case where the user navigates to the link before country pages are built).

Until `specs/country-page.md` ships, the link is hidden by the `COUNTRY_PAGES_ENABLED = false` guard in `table_filter.js`. The country-page spec landing PR sets that constant to `true`.

### 7.3 Byproduct graph (byproduct-graph spec)

The `byproduct_only` filter chip surfaces elements where `byproduct_of` is non-empty — exactly the node set of the byproduct DAG in `specs/byproduct-graph.md`. When `byproduct_only` is the sole active filter, `table_filter.js` should render a secondary action button below the table:

```html
<div class="byproduct-graph-cta" id="byproduct-graph-cta" hidden>
  <a href="byproduct-graph.html">Open byproduct dependency graph →</a>
</div>
```

The `byproduct-graph.md` spec should confirm the URL `viewer/byproduct-graph.html`. This button is hidden by `BYPRODUCT_GRAPH_ENABLED = false` in v1 (same pattern as the country-page link).

---

## 8. Open questions

1. **End-use bucket completeness.** The 397 raw slugs mapping to 14 buckets leaves an `"other"` catch-all. What threshold of unmapped share_pct (e.g. >10% of an element's total end-use share landing in "other") should trigger a review task? Proposal: log a warning during `generate_viewer` if any element has >20% of its end-use share unmapped; add a CI check.

2. **Multi-bucket end-use filter.** Should a user be able to select multiple end-use buckets simultaneously (OR semantics: show elements in batteries OR magnets)? The `<select>` element supports only single-select without extra JS. Multi-select could be a `<details>/<summary>` dropdown with checkboxes. Decision deferred to v1.1; for v1 single-select is sufficient.

3. **Partial HHI data display.** The `~` prefix convention (§4.2) for partial-completeness HHI is a simple heuristic. Should the column header have a footnote explaining the completeness distinction? Proposal: yes — a `<sup>*</sup>` on the column header linking to an inline footnote below the table.

4. **Filter state persistence.** URL state covers the sharing use case. If user navigates to an element page and returns, the filter state is preserved by browser back/forward naturally (URL is unchanged). No `localStorage` needed in v1.

5. **Commercial=false elements in the table.** Currently ~38 elements have `commercial_production=false`. With no filter active, all 118 rows are visible, including synthetics with no supply chain. The "Commercial only" chip is the escape hatch. Consider whether the default page load should pre-apply `commercial_only` (reducing the initial view to ~80 rows). Recommendation: do not pre-filter by default — the URL can encode `?filters=commercial_only` in any shared links that want the restricted view. The default state should be the full table.

6. **Category chip label humanization.** The raw values are snake_case enum strings (e.g. `transition_metal`). The `humanizeCategory` JS function should map these to display labels (e.g. `Transition metal`). This mapping should live in `table_filter.js` as a constant, not be emitted by `build_viewer.py`, to keep the Python side free of presentation concerns.

7. **DOE rank sort ordering.** Elements with `doe_rank: null` should sort last (not first) when sorting by DOE rank. Within ranked elements, lower rank number = more critical = sort first in descending mode.

---

## 9. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| End-use slug set grows faster than the bucket map is maintained | Medium | CI warning for unmapped slugs (§8.1); map is a single constant easy to extend |
| Two sibling specs both try to add `atlas-element-index` first, causing a merge conflict | Low–medium | Coordinate via PR draft status; first PR merged wins, second PR adapts |
| `data-*` attribute inflation bloats `index.html` significantly for 118 rows | Low | Each row gains ~200 bytes of attributes; adds ~24 KB to index.html, acceptable |
| Country select populated from mining shares only — elements that appear only in refining or reserves data are invisible to the country filter | Low | In scope for v1; refining-country filter is an open question for v1.1 |
| `table_filter.js` sort rewrites the DOM order; if another script also modifies `<tbody>` order, conflicts arise | Low | No other JS currently reorders the index table; document this assumption |

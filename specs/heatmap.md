---
title: "Feature spec: heatmap choropleth map"
tags: [atlas, viewer, spec, map]
status: draft
created: 2026-04-14
---

# Feature spec: heatmap choropleth map

## 1. Goal

When a user selects an element and a supply-chain stage (mining / refining / reserves), the world map shades every country proportionally to that country's share of global output for that stage. The default neutral map (hover-scan of all elements) persists until an element is chosen; selecting one switches the map into heatmap mode, replacing the neutral fill with a sequential color ramp and narrowing the hover tooltip and drawer to that element's data. Switching the stage toggle updates the fill live. The state is deep-linkable via URL params so a specific view (e.g., cobalt mining) can be shared or referenced from another page. Clearing the selection returns the map to neutral mode.

---

## 2. Scope / locked decisions

| Item | Decision | Rationale |
|---|---|---|
| Color scale | Logarithmic (base-10, domain `[0.1, 100]` mapped to `[0, 1]` in log space, then interpolated) | Co ≈ 76% DRC, Nb ≈ 90% BR, Pt ≈ 70% ZA — a linear scale renders the rest of the world invisible. Log scale preserves signal in the 1–10% band where the geopolitical story lives. Quantile would also work but changes meaning when elements are added; log is stable and meaningful. |
| Element selector UX | Searchable `<select>` with `<datalist>`-style or native `<select>` with optgroup by tier, plus a pinned chip row for tier-3 critical elements | ~80 elements fit in a grouped dropdown; search filters on symbol + name. Chip row surfaces the 15–20 most-cited criticals (US/EU/DOE listed) without requiring the dropdown. Mobile-friendly. No custom autocomplete widget needed. |
| Stage toggle | 3-way segmented control: Mining / Refining / Reserves | The DRC-vs-China cobalt divergence is the motivating example: DRC ≈ 76% mining, China ≈ 65–80% refining. Stages must be first-class; they cannot be collapsed. |
| ZZ (rest of world) | Never colored; explained in legend footnote | ZZ is not a real ISO code. Coloring it would be misleading. |
| Heatmap vs neutral map | Overlay mode: heatmap replaces neutral fill; hover/click behavior is narrowed to selected element | Replacing fill in-place avoids redrawing SVG geometry (expensive). The same `<path>` elements receive updated `fill` attributes via d3 transition. |
| URL deep link | `?heatmap=Co&stage=mining` | Shareable state. Parsed on page load before GeoJSON fetch completes; applied after render. |
| Legend | Color ramp bar, 5 labeled thresholds, footnote for uncolored countries | Must be positioned below the map SVG within `.country-map-shell`. |
| Country-page link | Drawer footer adds "View full country page →" linking to `countries/{ISO}.html` | Coordinates with `specs/country-page.md`; conditional on that route existing (link hidden if page absent). |
| Reserves stage | Uses `atlas_shares` where `share_type = 'reserves'` | Existing data model already tracks this; `_build_country_map_data` currently excludes it. A new payload key is needed. |
| Out of scope | Animation between stages, element comparison (two elements simultaneously), mobile swipe gesture on map, per-element HHI display on map | Deferred. HHI is in the element-metadata index (see §7) but not rendered on the map itself. |
| Out of scope | Building the country pages (`viewer/countries/`) | That's `specs/country-page.md`. This spec only adds a conditional link in the drawer. |

---

## 3. UX design

### 3.1 Initial state (no element selected)

The map renders exactly as it does today: neutral gray fill, hover tooltip shows the multi-element scan, click opens the existing multi-row drawer. The heatmap controls appear above the map: element selector (empty/placeholder), stage toggle (grayed out, Mining pre-selected but inactive), no legend visible.

```
[ Element: ________________ ▼ ]   [ Mining | Refining | Reserves ]  ← grayed until element chosen
[ chip: Li ] [ chip: Co ] [ chip: Nd ] [ chip: Pt ] …               ← critical chips, always visible
```

### 3.2 Selecting an element

User types in the selector or clicks a chip. On selection:

1. Stage toggle becomes active (Mining is default; if the element has no mining data, auto-advance to Refining, then Reserves).
2. Map paths receive updated fill via a 300 ms d3 `transition().attr('fill', ...)` call.
3. Countries with no data for that element+stage receive fill `var(--map-no-data)` (a light neutral, distinct from the colored ramp).
4. Legend appears below the map SVG.
5. Map panel header copy changes to: "Cobalt — mining share by country. Click a country for detail."
6. URL is updated via `history.replaceState` to `?heatmap=Co&stage=mining`.

### 3.3 Stage toggle

Clicking Mining / Refining / Reserves re-applies the color scale for that stage using already-loaded data (no network request). Transition is 200 ms. URL param `stage` updates. If the selected stage has no data for the current element, countries all render in the no-data fill and the legend shows "No data for this stage."

### 3.4 Hover tooltip (heatmap mode)

Tooltip content narrows to the selected element only:

```
Democratic Republic of Congo
Cobalt — mining
76.4%  of global output   (97,000 t/yr)
```

If no data for that country+element+stage: "No attributed data for this stage."

The existing multi-element table is hidden in heatmap mode.

### 3.5 Click / drawer (heatmap mode)

The drawer title shows the country name. Body leads with the selected element's row (share_pct, quantity, stage), then the existing full-element scan table below a "— All attributed elements —" divider. The drawer footer adds:

```
View full country page →   (links to countries/{ISO}.html, hidden if page absent)
```

### 3.6 Clearing selection

"Clear" button appears next to the element selector when an element is active. Clicking it returns to neutral mode: fills reset to neutral, legend hidden, tooltip reverts to multi-element scan, URL params removed via `history.replaceState`.

### 3.7 URL state on page load

On `DOMContentLoaded`, parse `location.search` for `heatmap` and `stage`. If `heatmap` matches a known symbol in the element-metadata index, pre-select that element and stage after the GeoJSON fetch resolves. Invalid params are silently ignored (no error state).

### 3.8 Empty / error states

- Element selected, no data at all for any stage: All countries render in no-data fill. Legend reads "No production data found."
- GeoJSON load failure: existing fallback behavior; heatmap controls are still rendered (harmless).
- Element param in URL but not in dataset: selector stays empty, URL params cleared.

---

## 4. Data model

### 4.1 Reuse of existing payload

`#atlas-country-map-data` already carries mining and refining rows keyed by ISO-2 code. The heatmap JS reads this same payload — no new network request is needed for mining and refining stages. However:

- The existing payload groups rows by **country**, not by element+stage. The heatmap needs the inverse index: look up a country's share for a specific element+stage.
- Reserves data is absent from the current payload.

### 4.2 Payload augmentation: reserves in existing payload

Add a `reserves` sub-key to the existing `atlas-country-map-data` JSON (built by `_build_country_map_data` in `scripts/build_viewer.py`):

```json
{
  "countries": { "CD": [...], ... },
  "country_count": 42,
  "row_count": 218,
  "reserves": {
    "CD": [
      { "symbol": "Co", "share_pct": 51.2, "quantity_value": 3600000, "quantity_unit": "tonnes" }
    ],
    ...
  }
}
```

Shape of each reserves entry: `{ symbol, share_pct, quantity_value, quantity_unit }`. `share_pct` is taken directly from `atlas_shares.share_pct` where `share_type = 'reserves'`. Country `ZZ` is excluded. Rows sorted by descending `share_pct` within each country.

### 4.3 New payload: element-metadata index

A second `<script>` block embedded in `index.html`:

```html
<script id="atlas-element-index" type="application/json">...</script>
```

Shape:

```json
[
  {
    "symbol": "Co",
    "name": "Cobalt",
    "category": "transition_metal",
    "tier": 3,
    "critical": true,
    "has_mining": true,
    "has_refining": true,
    "has_reserves": true
  },
  ...
]
```

Fields:

| Field | Source | Notes |
|---|---|---|
| `symbol` | `atlas_elements.symbol` | |
| `name` | `atlas_elements.name` | |
| `category` | `atlas_elements.category` | |
| `tier` | `atlas_elements.industrial_tier` | integer 0–4 |
| `critical` | `true` if any of `us_critical_list_as_of_2025`, `eu_crm_list_as_of_2024`, `eu_strategic_list_as_of_2024` is true, or `doe_short_term_criticality_rank` is not null | Used to populate chips row |
| `has_mining` | `true` if any `atlas_shares` row exists for this symbol with `share_type='mining'` | Used to disable stage toggle tabs |
| `has_refining` | same for `share_type='refining'` | |
| `has_reserves` | same for `share_type='reserves'` | |

`hhi_mining` and `hhi_refining` are deferred to the element-metadata index owner (see §7). This spec reads but does not compute them.

**Note for `table-filter-sort` spec**: this index serves the same filtering need. Whoever lands first should own the schema; add `hhi_mining`, `hhi_refining`, and `top_country_share` fields as proposed in the shared-schema note in §7.

### 4.4 Build function changes

In `scripts/build_viewer.py`:

**New function** `_build_element_index(con, elements_list) -> list[dict]` (~30 lines):

```python
def _build_element_index(con, elements_list: list[dict]) -> list[dict]:
    # Query atlas_shares once for all symbols with share_type IN ('mining','refining','reserves')
    # Build set of (symbol, share_type) pairs, then annotate each element dict.
    ...
```

**Modified function** `_build_country_map_data(con)` (~15 additional lines): add a second query for `share_type = 'reserves'` and attach result as `reserves` key.

**Modified function** `_index_body(elements, snapshot_year, country_map_data)`: accept an additional `element_index: list[dict]` param; embed `#atlas-element-index` JSON block before `#atlas-country-map-data`.

**Modified call site** in `generate_viewer()`: compute `element_index = _build_element_index(con, elements_list)` and pass it through.

---

## 5. Implementation plan

Steps are ordered by dependency. Estimated line counts are for the diff, not the file total.

### Step 1 — Build: `_build_element_index` + reserves augmentation (~65 lines)

**File**: `scripts/build_viewer.py`

- Add `_build_element_index(con, elements_list) -> list[dict]` after `_build_country_map_data`.
- Modify `_build_country_map_data` to run a second DuckDB query for reserves shares and attach as `data["reserves"]`.
- Add `element_index` param to `_index_body`; embed `<script id="atlas-element-index" type="application/json">` block.
- Wire in `generate_viewer()`: call `_build_element_index`, pass result to `_index_body`.

### Step 2 — HTML: heatmap controls markup (~20 lines)

**File**: `scripts/build_viewer.py`, inside `_index_body`

Add inside `.map-panel` before `.country-map-shell`:

```html
<div class="heatmap-controls" id="heatmap-controls">
  <div class="heatmap-selector-wrap">
    <label for="heatmap-element-select" class="sr-only">Element</label>
    <select id="heatmap-element-select" class="heatmap-element-select">
      <option value="">— select element —</option>
      <!-- optgroups by tier, populated by JS from atlas-element-index -->
    </select>
    <button id="heatmap-clear" class="heatmap-clear" hidden aria-label="Clear element selection">&times;</button>
  </div>
  <div class="heatmap-stage-toggle" id="heatmap-stage-toggle" aria-disabled="true">
    <button class="heatmap-stage-btn is-active" data-stage="mining">Mining</button>
    <button class="heatmap-stage-btn" data-stage="refining">Refining</button>
    <button class="heatmap-stage-btn" data-stage="reserves">Reserves</button>
  </div>
</div>
<div class="heatmap-chips" id="heatmap-chips">
  <!-- critical element chips — populated by JS -->
</div>
```

Also add legend HTML after the `<svg>` is injected (JS-created, not build-time HTML; see Step 4).

### Step 3 — JS: `charts_map.js` heatmap mode (~200 lines added to existing 288-line file)

**File**: `viewer/assets/charts_map.js`

Additions within the existing IIFE, after the GeoJSON `.then(...)` block:

**3a. Parse element-metadata index** (~10 lines):

```js
const elementIndexScript = document.getElementById("atlas-element-index");
const elementIndex = elementIndexScript ? JSON.parse(elementIndexScript.textContent || "[]") : [];
```

**3b. Populate `<select>` optgroups** (~20 lines):

Group elements by `tier` descending (3 first: "Critical & Scarce", 4: "High-Volume", 2: "Niche", 0/1: "Other"). Filter to only elements with `has_mining || has_refining || has_reserves`. Populate chips row from `critical === true` elements.

**3c. Build inverse index** (~15 lines):

From the existing `countries` payload (mining+refining) and new `reserves` sub-key, build:

```js
// Map: symbol -> stage -> { [isoCode]: { share_pct, quantity_value, quantity_unit } }
const heatmapIndex = buildHeatmapIndex(countries, payload.reserves || {});
```

**3d. Log color scale** (~15 lines):

```js
// d3.scaleSequentialLog — domain [0.1, 100], range via d3.interpolateYlOrRd
// Clamp: values < 0.1 → floor fill; values > 100 → ceiling (shouldn't occur)
const colorScale = d3.scaleSequential()
  .domain([Math.log10(0.1), Math.log10(100)])
  .range([0, 1])
  .clamp(true);
const colorInterp = d3.interpolateYlOrRd;
const heatFill = (sharePct) => sharePct > 0 ? colorInterp(colorScale(Math.log10(Math.max(sharePct, 0.1)))) : noDataFill;
```

CSS variable `--map-no-data: #e8e8e8` for countries with no data.

**3e. Apply/clear heatmap** (~50 lines):

```js
// applyHeatmap(symbol, stage) — sets path fills via d3 transition
// clearHeatmap() — resets fills to var(--map-neutral), reverts tooltip behavior
```

**3f. Legend render** (~40 lines):

Insert a `<div class="heatmap-legend">` below the SVG. Render a horizontal gradient bar using an inline `<canvas>` (60 × 12 px, drawn via `colorInterp`), 5 labeled tick marks at 0.1%, 1%, 5%, 20%, 100%, and a footnote: "Uncolored: no data or rest-of-world aggregate."

**3g. Tooltip / drawer overrides** (~30 lines):

In heatmap mode, `showTooltip` and `renderDrawerRows` check `activeSymbol !== null` and branch to heatmap-specific renderers. Existing neutral renderers remain unchanged.

**3h. URL state** (~20 lines):

On module init, check `new URLSearchParams(location.search)` for `heatmap` + `stage`. After GeoJSON renders, call `applyHeatmap` with parsed values. On state change, call `history.replaceState(null, '', '?' + params.toString())`. On clear, call `history.replaceState(null, '', location.pathname)`.

### Step 4 — CSS (~80 lines)

**File**: `scripts/build_viewer.py` (inside `CSS` string constant)

Add sections:

```css
/* ── heatmap controls ── */
.heatmap-controls { ... }            /* flex row, gap, align-center */
.heatmap-element-select { ... }      /* width: 220px, font-size: 0.85rem */
.heatmap-clear { ... }               /* small ×, positioned inline */
.heatmap-stage-toggle { ... }        /* segmented control container */
.heatmap-stage-btn { ... }           /* individual stage button */
.heatmap-stage-btn.is-active { ... } /* accent border-bottom + color */
.heatmap-stage-toggle[aria-disabled="true"] .heatmap-stage-btn { opacity: 0.4; pointer-events: none; }
.heatmap-chips { ... }               /* flex wrap, gap: 0.4rem, margin-top: 0.5rem */
.heatmap-chip { ... }                /* small pill, accent border */
.heatmap-chip.is-active { ... }      /* filled accent bg */

/* ── heatmap legend ── */
.heatmap-legend { ... }              /* flex row, align-center, gap, margin-top: 0.5rem */
.heatmap-legend-bar { ... }          /* canvas element */
.heatmap-legend-ticks { ... }        /* flex row of labeled ticks */
.heatmap-legend-footnote { ... }     /* small muted text */
```

### Step 5 — Tests (~50 lines)

**File**: `tests/test_build_viewer.py`

See §6 for full list.

---

## 6. Testing

All tests go in `tests/test_build_viewer.py`. New invariant block: **Heatmap (HM)**.

### HM-INV-1: `atlas-element-index` block is present and valid JSON

```python
def test_hm_inv1_element_index_present(viewer_dir):
    index_html = (viewer_dir / "index.html").read_text()
    assert 'id="atlas-element-index"' in index_html
    # Extract JSON between script tags
    m = re.search(r'id="atlas-element-index"[^>]*>(.*?)</script>', index_html, re.DOTALL)
    assert m, "atlas-element-index script block not found"
    data = json.loads(m.group(1))
    assert isinstance(data, list)
    assert len(data) > 0
    # Co must be present with expected shape
    co = next((e for e in data if e["symbol"] == "Co"), None)
    assert co is not None
    assert co["has_mining"] is True
    assert isinstance(co["tier"], int)
    assert isinstance(co["critical"], bool)
```

### HM-INV-2: element-index critical flag matches criticality columns

```python
def test_hm_inv2_critical_flag_matches_db(viewer_dir):
    # Connect to real DB; assert that every element flagged critical=True
    # has at least one of the four criticality columns set.
    ...
```

### HM-INV-3: reserves sub-key in country-map-data, excludes ZZ

```python
def test_hm_inv3_reserves_in_map_payload(viewer_dir):
    index_html = (viewer_dir / "index.html").read_text()
    m = re.search(r'id="atlas-country-map-data"[^>]*>(.*?)</script>', index_html, re.DOTALL)
    data = json.loads(m.group(1))
    assert "reserves" in data
    # ZZ must not appear
    assert "ZZ" not in data["reserves"]
    # If any element has reserves data, at least one country entry should appear
    ...
```

### HM-INV-4: `has_mining` / `has_refining` / `has_reserves` consistent with shares table

```python
def test_hm_inv4_has_stage_flags_consistent(viewer_dir):
    # Connect to DB; for a sample of elements (Co, He, Og),
    # assert has_mining/has_refining/has_reserves match actual share rows.
    ...
```

### HM-INV-5: `_build_element_index` deterministic — repeated calls produce same output

Test via `_build_element_index` unit call (open DB directly in test).

### UI smoke notes (not automated)

- With `?heatmap=Co&stage=mining` in URL, DRC should be darkest red, with tooltip showing ≈76%.
- Stage toggle: switch to Refining → China darkens, DRC lightens.
- Selecting He (no mining data) → Mining tab auto-advances to Refining or Reserves; all-countries no-data fill if no data for that stage.
- Clearing selection restores neutral tooltip behavior.
- Chip for Co is visible and clicking it pre-selects Co.

---

## 7. Cross-feature dependencies

### What this spec needs from siblings

| Dependency | Sibling spec | Status |
|---|---|---|
| `viewer/countries/{ISO}.html` route must exist for drawer link | `specs/country-page.md` | Conditional: link is hidden if page is absent. No hard dependency — implement the link check via `fetch(url, {method:'HEAD'})` or a build-time flag. |
| Shared element-metadata index schema | `specs/table-filter-sort.md` | See note below. |

### Shared element-metadata index

Both this spec and `specs/table-filter-sort.md` need an element metadata lookup by symbol. This spec proposes the schema above (§4.3) with fields `symbol, name, category, tier, critical, has_mining, has_refining, has_reserves`. The `table-filter-sort` spec likely needs additional fields: `top_country_share` (max share_pct across all stages), `hhi_mining`, `hhi_refining`.

**Coordination rule**: whoever lands first owns the `_build_element_index` function and the `#atlas-element-index` script block. The second spec extends the schema by adding columns to the same DuckDB query and the same JSON block, not by creating a second block. The two specs should not both define this function independently.

Proposed extended schema (flag for table-filter-sort to adopt or reject):

```json
{
  "symbol": "Co",
  "name": "Cobalt",
  "category": "transition_metal",
  "tier": 3,
  "critical": true,
  "has_mining": true,
  "has_refining": true,
  "has_reserves": true,
  "top_mining_country": "CD",
  "top_mining_share": 76.4,
  "hhi_mining": 6200,
  "hhi_refining": 4800
}
```

HHI computation belongs in `_build_element_index` since it requires the full shares list anyway (sum of squared share_pcts × 100). This spec defers adding HHI to whoever resolves the merge conflict.

### What siblings can consume from this spec

- The `#atlas-element-index` JSON block is useful to `specs/byproduct-graph.md` for labeling graph nodes with tier and criticality without a separate payload.
- The drawer's "View full country page →" link pattern is a coordination point with `specs/country-page.md`: the route must be `countries/{ISO}.html` relative to `index.html` (i.e., `viewer/countries/CD.html`).

---

## 8. Open questions

| Question | Owner | Blocking? |
|---|---|---|
| Should `<select>` use native `<optgroup>` or a custom listbox for search-as-you-type on ~80 elements? Native select doesn't filter on input in most browsers without JS. A `<datalist>` on a text `<input>` filters but loses the grouping. | Frontend | No — default to native select; upgrade to filtered input if UX review flags it. |
| Color scheme: `YlOrRd` (yellow-orange-red) vs a single-hue blue-purple ramp. YlOrRd is colorblind-problematic at the yellow end. | Design | No — use YlOrRd for now; note the issue for a future accessibility pass. |
| Should the legend show absolute quantities (tonnes/yr) as a second axis, or share_pct only? Quantity scale varies enormously across elements. | Product | No — share_pct only for now; quantity in tooltip/drawer. |
| Deep-link format: `?heatmap=Co&stage=mining` vs a hash fragment `#Co/mining`. Hash fragments don't get sent to the server (irrelevant for a static site but affects future SSR). | Architecture | No — use query params for shareability and consistency. |
| Chip row: should clicking a chip that is already active deselect it (toggle) or be a no-op? | UX | No — toggle (deselect) is more intuitive; treat as clear. |
| `HEAD` fetch to detect country page existence is a network round-trip per drawer open. Alternative: build-time flag in `element_index` or a manifest of generated country pages. | Build | No — defer; use `HEAD` fetch for now, cache result in a `Set`. |

---

## 9. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Log scale domain edge: elements with all countries < 0.1% (e.g., niche isotopes) — every country renders at min-color, indistinguishable from no-data fill | Medium | Medium | Clamp domain floor to the actual minimum non-zero share for the selected element+stage, computed at render time |
| `_build_country_map_data` reserves query adds noticeable build time if `atlas_shares` is large | Low | Low | Query is a single pass with `WHERE share_type = 'reserves'`; should be fast. Profile if test suite regresses. |
| Two sibling specs define `_build_element_index` independently, causing merge conflict | High | Medium | Coordinate: this spec proposes the schema; `table-filter-sort` spec should reference it by name and only extend it |
| `history.replaceState` called too frequently (on every mousemove stage if wired incorrectly) | Low | Low | Debounce or call only on selection/toggle change events, not on hover |
| `<select>` optgroup UX is poor on mobile (OS-rendered picker doesn't filter) | Medium | Low | Acceptable for v1; note for UX review. Chips provide a mobile-friendly fast path for the ~20 most-used elements |
| Country-page drawer link breaks if `specs/country-page.md` is never implemented | High | Low | Link is guarded by a `HEAD` check or build-time flag; silently hidden if page absent |

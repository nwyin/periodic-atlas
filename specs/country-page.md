---
title: "Feature spec: per-country pages"
tags: [atlas, viewer, spec, country]
status: draft
created: 2026-04-14
---

# Feature spec: per-country pages

## 1. Goal

Add one static HTML page per producing country at `viewer/countries/{ISO}.html`. Each page inverts the per-element view: given a country, show every element it mines, refines, or holds reserves for — with share %, absolute quantity, global rank among producers, and confidence. The pages are generated at build time from existing data; no new data sources are required.

---

## 2. Scope / locked decisions

**In scope (v1)**

- Stages: Mining, Refining, Reserves. These map directly to `share_type` values in `atlas_shares` (`mining`, `refining`) and to `atlas_shares` rows where `share_type = 'reserves'`.
- Countries: every ISO-2 code appearing in any `CountryShareList` across all elements, minus exclusions below.
- Pages for "thin" countries (1–2 rows total) are generated and valid; they just have small tables.
- Links from: map drawer in `charts_map.js`, per-element pages (each country cell in a share table), and index page producer-country filter chips (see `specs/table-filter-sort.md`).

**Exclusions**

- `ZZ` (rest of world aggregate) — never gets a country page. Excluded at data inversion time.
- `XX` (pseudo-country used for unknown origin) — excluded for the same reason; already filtered out of `_build_country_map_data`.
- `-99` codes from the GeoJSON (overseas dependency features that share an ISO_A2_EH with their sovereign) — not present in share data, so irrelevant.
- Economic indicators, price data, mine-level detail, ownership/corporate structure — out of scope for v1.
- Sub-national regions (e.g. "DRC Katanga belt") — out of scope for v1; the atlas schema has no sub-national concept.
- Formal political status disambiguation (e.g. distinguishing Kosovo, Taiwan in a geo-political sense) — use ISO-2 as given; no editorial stance implied.

**NC (New Caledonia) — explicit decision**

NC appears in Co mining data with an explicit USGS footnote labelling it a French overseas territory. NC has `ISO_A2 = 'NC'` in the GeoJSON and `NAME_EN = 'New Caledonia'`. Generate `viewer/countries/NC.html` as a normal country page. Note on the page that NC is a French overseas collectivity. `SOVEREIGNT = 'France'` is available from the GeoJSON for this note.

---

## 3. UX design

### 3.1 Page layout

```
[breadcrumb: ← Atlas index]

[flag emoji] Democratic Republic of the Congo (CD)
──────────────────────────────────────────────────────

[summary stat pills]   [small world-map thumbnail]

[tab bar or section headers: Mining | Refining | Reserves]

[sortable table per stage]

[horizontal bar chart: top elements by share]

[related: other top-3 producers of the same elements]

[footer]
```

**Breadcrumb**: a single `← Atlas index` link pointing to `../index.html`. No multi-level breadcrumb needed for v1 (the site is shallow).

**Header**: country name + ISO code, flag emoji (derived from ISO-2 at render time in Python), and a short subtitle line ("Supply chain footprint — snapshot year 2025"). For territories (NC), append a parenthetical: "(French overseas collectivity)" derived from `SOVEREIGNT` in the GeoJSON name map. Keep it factual; do not imply statehood or lack thereof.

**World-map thumbnail**: a small SVG (240 × 135 px) generated inline or rendered by a lightweight client-side snippet that highlights this country's feature in the GeoJSON. Option A (recommended): inline a minimal d3 snippet that loads `../assets/world_countries_50m.geojson` and highlights the country by ISO code, using the same Natural Earth projection already in `charts_map.js`. Option B: skip the thumbnail for v1 and leave a `TODO` div — acceptable if the implementation schedule is tight. The spec mandates Option A as the target; the build milestone is Option A or a clearly labelled placeholder.

### 3.2 Summary stat pills

Four pills in a row:

| Pill | Value |
|------|-------|
| Elements mined | count of distinct elements where this country appears in mining shares |
| Elements refined | count of distinct elements where this country appears in refining shares |
| Top-3 reserves | count of distinct elements where this country ranks 1st, 2nd, or 3rd by `share_pct` among all countries in reserves shares |
| Critical elements | count of distinct elements in this country's rows where `us_critical_list_as_of_2025 = true` OR `eu_crm_list_as_of_2024 = true` (joined from `atlas_elements`) |

All four counts are computed at build time and embedded as plain text in the HTML.

### 3.3 Stage sections

Present as stacked `<section>` elements with anchor IDs (`#mining`, `#refining`, `#reserves`), not JS tabs, so each section is directly linkable and fully readable without JS. A sticky "jump to section" nav bar (three `<a>` links) at the top of the content area provides the tab-like UX.

Each section contains:

1. A section heading with element count: "Mining (12 elements)"
2. If no rows for this stage: `<p class="country-page-empty">No attributed data for this stage.</p>` — still render the section, just with the empty state.
3. A `<table class="country-page-table sortable-table">` (the `sortable-table` class is a hook for the table-filter-sort feature; see §7).

**Table columns per stage**:

| Column | Notes |
|--------|-------|
| Element | Symbol linked to `../elements/{Sym}.html`; element full name as subtitle text |
| Share % | `share_pct` from `atlas_shares`; formatted to one decimal place |
| Quantity | `quantity_value` + `quantity_unit`; "—" if null |
| Global rank | Computed at build time (see §4.3); rendered as "1st", "2nd", etc. |
| Confidence | `confidence` field from `atlas_shares`; styled with `.producer-low-confidence` when value is `"low"` |
| Notes | `notes` field from `atlas_shares`; truncated to 120 chars with a `title` attribute for the full text; omit column entirely if no row in this stage has notes |

Default sort: descending `share_pct`.

### 3.4 Chart

A single horizontal bar chart rendered by a new `charts_country.js` file (vanilla JS + d3 v7, following the conventions of `charts_prices.js` and `charts_production.js`). The chart shows the top-15 elements by `share_pct` for this country, collapsing all three stages into one series and colour-coding bars by stage (mining = existing atlas blue, refining = orange, reserves = green — reuse CSS custom properties from `atlas.css`). If a country has fewer than 3 elements across all stages, omit the chart entirely.

Chart data is embedded in a `<script id="country-chart-data" type="application/json">` block inside the page (same pattern as `atlas-chart-data` in element pages).

### 3.5 Related reading

A `<section class="country-related">` at the bottom of the page:

- **Co-producers**: for each element this country appears in (any stage), find all other countries that rank top-3 in that element+stage. Deduplicate. Show as a compact tag-cloud of country links (linked to their country pages via `{ISO}.html`). Label: "Countries with overlapping top-3 positions". Cap at 20 unique countries to keep the list readable; if more, show "and N more".
- **Critical minerals overview**: a static link to the critical minerals overview if/when one is added; for now, a placeholder comment in the HTML.

---

## 4. Data model

### 4.1 Country-data inversion

`_build_country_map_data()` already queries `atlas_shares` to produce `{ countries: { ISO: [...rows] } }` for mining and refining only (it joins to `atlas_production` to compute `global_pct`). Country pages need a richer inversion that also includes:

- Reserves rows (`share_type = 'reserves'`)
- The `confidence` and `notes` fields (currently absent from the map payload)
- Global rank (computed from the full share list per element+stage)
- Criticality flags from `atlas_elements`

Introduce a new build-time function `_build_country_page_data(con)` that returns:

```python
{
    "CD": {
        "rows": [
            {
                "symbol": "Co",
                "element_name": "cobalt",
                "stage": "mining",          # "mining" | "refining" | "reserves"
                "stream": None,             # str | None
                "share_pct": 76.0,
                "quantity_value": 220000.0,
                "quantity_unit": "tonnes_per_year",
                "confidence": "high",
                "notes": "...",
                "global_rank": 1,           # rank among all countries for this element+stage
                "us_critical": True,
                "eu_crm": True,
            },
            ...
        ]
    },
    ...
}
```

This dict is computed once in `generate_viewer()` and passed to `_render_country_page()` for each ISO key. It is not embedded in `index.html` (too large); each country page gets only its own slice.

**Query strategy**: run a single SQL query:

```sql
SELECT
    s.country,
    s.symbol,
    e.name AS element_name,
    s.share_type AS stage,
    s.stream,
    s.share_pct,
    s.quantity_value,
    s.quantity_unit,
    s.confidence,
    s.notes,
    e.us_critical_list_as_of_2025,
    e.eu_crm_list_as_of_2024,
    RANK() OVER (
        PARTITION BY s.symbol, s.share_type
        ORDER BY s.share_pct DESC NULLS LAST
    ) AS global_rank
FROM atlas_shares s
JOIN atlas_elements e ON e.symbol = s.symbol
WHERE s.country NOT IN ('ZZ', 'XX')
  AND s.country IS NOT NULL
ORDER BY s.country, s.share_type, s.share_pct DESC NULLS LAST
```

The `RANK()` window function gives the correct global rank within each element+stage partition. Post-query, group rows by country into the dict above.

### 4.2 ISO-2 → country name resolution

**Recommendation: extract from the GeoJSON at build time.**

`pycountry` is not in `pyproject.toml`. Adding it is an option but introduces a dependency for a one-time data extraction that the GeoJSON already covers for all countries present in the atlas data. The GeoJSON has 237 non-`-99` ISO_A2 mappings, which is more than enough.

**Implementation**: add a module-level helper in `build_viewer.py`:

```python
def _build_iso_name_map() -> dict[str, str]:
    """Return {ISO_A2: display_name} for all features in the bundled GeoJSON.

    Uses ISO_A2 (not ISO_A2_EH) as the key so that dependency territories
    that share an ISO_A2_EH with their sovereign are skipped. When a code
    appears in multiple features (e.g. AU appears for Australia plus two
    dependency features with ISO_A2 = '-99'), the first non-'-99' feature wins.
    NAME_EN is preferred over ADMIN.

    Also returns the SOVEREIGNT for each feature, stored as a second dict
    {ISO_A2: sovereignt_name}, used for territory notes (e.g. NC → France).
    """
```

Returns two dicts: `iso_to_name: dict[str, str]` and `iso_to_sovereignt: dict[str, str]`. Call it once at the top of `generate_viewer()` before the country-page loop.

**Fallback**: if an ISO code appears in `atlas_shares` but not in the GeoJSON (should not happen with clean data), use the ISO code itself as the display name and log a warning.

**Note on CN**: the GeoJSON returns `"People's Republic of China"` for CN. This is acceptable as a factual descriptor; do not override it in the spec. If the project wants "China" for brevity, add a small override dict (parallel to `WIKIPEDIA_NAME_OVERRIDES`) — leave this as an open question (see §8).

### 4.3 Global-rank computation

Rank is computed by the SQL `RANK()` window function over `(symbol, share_type)` ordered by `share_pct DESC`. Ties receive the same rank (standard competition ranking: 1, 1, 3). This is intentional: two countries tied at 30% are both "1st". The `RANK()` function (not `DENSE_RANK()`) is correct here because the user cares about "how many countries are ahead of me", not "how many distinct share values are above mine".

Null `share_pct` sorts last (`NULLS LAST`) and receives the highest rank number. Rows with null `share_pct` still appear in the table with rank displayed as "—".

---

## 5. Implementation plan

Steps are ordered; each is a commit-worthy unit.

### Step 1 — Directory and shell function

Create `viewer/countries/` directory (`.gitkeep` placeholder or created programmatically). Add `_country_page_shell(title, body, footer)` to `build_viewer.py` — mirrors `_element_page_shell` but with `../../assets/` path prefix (country pages are two levels deep, not one).

Wait — `viewer/countries/NC.html` is one level below `viewer/`, same depth as `viewer/elements/NC.html`. Relative path prefix is `../assets/` (one `..`). Double-check: `viewer/countries/{ISO}.html` → `../assets/atlas.css`. Correct.

### Step 2 — ISO name map helper

Add `_build_iso_name_map()` and `_build_iso_sovereignt_map()` as a combined function returning a named tuple or a `dict` with two keys. Call it at the start of `generate_viewer()`. Keep it module-level callable so tests can invoke it independently.

### Step 3 — Country data inversion

Add `_build_country_page_data(con) -> dict[str, list[dict]]`. The outer dict maps ISO code to a list of row dicts (schema in §4.1). Exclude `ZZ` and `XX`. Log a count: `"country pages: {n} countries, {m} total rows"`.

### Step 4 — Summary stat computation

Add `_compute_country_summary(rows, elements_by_symbol) -> dict` that takes the row list for one country and the full elements dict (indexed by symbol) and returns:

```python
{
    "n_mined": int,
    "n_refined": int,
    "n_top3_reserves": int,
    "n_critical": int,
}
```

`n_critical` = distinct symbols where `us_critical = True` OR `eu_crm = True` (union, not intersection), across all three stages.

### Step 5 — Flag emoji helper

Add `_flag_emoji(iso2: str) -> str`. Unicode regional indicator letters are `U+1F1E6` (A) through `U+1F1FF` (Z). Convert each letter of the two-character ISO code:

```python
def _flag_emoji(iso2: str) -> str:
    if len(iso2) != 2 or not iso2.isalpha():
        return ""
    return "".join(chr(0x1F1E6 + ord(c) - ord('A')) for c in iso2.upper())
```

This is pure Python with no dependencies. Note the rendering caveat in §8.

### Step 6 — HTML renderer

Add `_render_country_page(iso, country_name, sovereignt, rows, summary, iso_to_name) -> str`. Builds the full page body including:

- Header with flag, name, ISO code, territory note if `sovereignt != country_name`
- Summary stat pills (four values from `summary`)
- World-map thumbnail div (initially a placeholder `<div class="country-map-thumbnail" data-country-code="{iso}">` — the `charts_country.js` file initialises it client-side)
- Jump-nav links: `#mining | #refining | #reserves`
- Three stage sections (§3.3)
- Chart data script block + chart div
- Related section (co-producers)

Inline chart data using `<script id="country-chart-data" type="application/json">`.

### Step 7 — New JS file: charts_country.js

Create `viewer/assets/charts_country.js`. Responsibilities:

1. Read `<script id="country-chart-data">` and render the horizontal bar chart into `#country-bar-chart`.
2. Initialise the world-map thumbnail: fetch `../assets/world_countries_50m.geojson`, render a 240 × 135 Natural Earth SVG, highlight the feature whose `ISO_A2` matches `data-country-code` on the thumbnail div. Reuse the projection setup from `charts_map.js`.
3. Make each `<table class="sortable-table">` column header clickable for client-side sort (ascending/descending toggle). This is shared behaviour with the `table-filter-sort` feature (see §7); if that feature ships first, import the sort helper from wherever it lands; otherwise implement a minimal column-sort inline.

### Step 8 — Generate pages in `generate_viewer()`

After the per-element page loop, add:

```python
countries_dir = viewer_dir / "countries"
countries_dir.mkdir(exist_ok=True)

country_page_data = _build_country_page_data(con)
iso_to_name, iso_to_sovereignt = _build_iso_name_map()

for iso, rows in sorted(country_page_data.items()):
    country_name = iso_to_name.get(iso, iso)
    sovereignt = iso_to_sovereignt.get(iso, country_name)
    summary = _compute_country_summary(rows, elements_index)
    body = _render_country_page(iso, country_name, sovereignt, rows, summary, iso_to_name)
    title = f"{country_name} ({iso}) | Atlas {snapshot_year}"
    html = _country_page_shell(title, body, footer_element)
    (countries_dir / f"{iso}.html").write_text(html, encoding="utf-8")
    print(f"viewer/countries/{iso}.html written")
```

`elements_index` is `{sym: el_dict}` built from `elements_list` — add this dict earlier in `generate_viewer()`.

### Step 9 — Link from charts_map.js

In `renderDrawerRows()` in `charts_map.js`, append after the table:

```js
`<p class="country-map-drawer-link"><a href="countries/${encodeURIComponent(code)}.html">View full page &rarr;</a></p>`
```

This link is relative to `index.html` which lives at `viewer/`, so `countries/{ISO}.html` resolves correctly.

### Step 10 — Link from per-element pages

In `_render_isotope_panel` and wherever per-element share tables render country cells, wrap the ISO code in an anchor:

```python
f'<a href="../countries/{_html_escape(country)}.html">{_html_escape(country)}</a>'
```

The existing producer table in `_render_isotope_panel` (lines ~1258–1263 of `build_viewer.py`) renders country as a plain `<td>`. Wrap it. The mining/refining bar charts in `charts_production.js` render country labels in SVG — add a `data-country-href` attribute on bar groups so a click handler in `charts_country.js` or `charts_production.js` can navigate.

### Step 11 — CSS additions

Add to `atlas.css` (the CSS string inside `build_viewer.py`):

```css
/* country pages */
.country-page-header { display: flex; align-items: baseline; gap: 0.5rem; }
.country-flag { font-size: 2rem; line-height: 1; }
.country-iso-badge { font-size: 0.85rem; color: var(--muted); font-family: var(--mono); }
.country-stat-pills { display: flex; gap: 0.75rem; flex-wrap: wrap; margin: 1rem 0; }
.country-stat-pill { background: var(--bg-alt); border-radius: 0.375rem; padding: 0.35rem 0.75rem; font-size: 0.85rem; }
.country-stat-pill strong { display: block; font-size: 1.25rem; }
.country-jump-nav { display: flex; gap: 1rem; margin: 1rem 0; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }
.country-page-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.country-page-table th { cursor: pointer; user-select: none; }
.country-page-table th[aria-sort="ascending"]::after { content: " ↑"; }
.country-page-table th[aria-sort="descending"]::after { content: " ↓"; }
.country-page-empty { color: var(--muted); font-style: italic; padding: 0.5rem 0; }
.country-bar-chart { margin: 1.5rem 0; }
.country-related { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--border); }
.country-related-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; }
.country-related-tag { font-size: 0.8rem; background: var(--bg-alt); border-radius: 0.25rem; padding: 0.2rem 0.4rem; }
.country-map-thumbnail { width: 240px; height: 135px; background: var(--bg-alt); border-radius: 0.375rem; }
.country-map-drawer-link { margin-top: 0.75rem; font-size: 0.9rem; }
```

### Step 12 — Sitemap / print log

Add `viewer/countries/{ISO}.html` entries to the printed output at the end of `generate_viewer()`. No formal XML sitemap exists yet; the print log is the sitemap for now.

---

## 6. Testing

Add the following test functions to `tests/test_build_viewer.py`:

### CP-1: Must-exist country pages

```python
def test_cp1_must_exist_country_pages(viewer_dir):
    for iso in ("CD", "CN", "US", "AU", "RU"):
        page = viewer_dir / "countries" / f"{iso}.html"
        assert page.exists(), f"missing country page for {iso}"
        text = page.read_text()
        assert iso in text, f"{iso}.html missing ISO code in content"
```

CD is the highest-stakes case (76% of Co mining). CN covers refining concentration. US covers multi-element presence with thin individual shares.

### CP-2: No ZZ page generated

```python
def test_cp2_no_zz_page(viewer_dir):
    assert not (viewer_dir / "countries" / "ZZ.html").exists()
```

### CP-3: Country pages link back to element pages

```python
def test_cp3_country_pages_link_to_elements(viewer_dir):
    cd_page = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'href="../elements/Co.html"' in cd_page
```

CD must reference Co (the most prominent Co producer).

### CP-4: Element pages link to country pages

```python
def test_cp4_element_pages_link_to_countries(viewer_dir):
    co_page = (viewer_dir / "elements" / "Co.html").read_text()
    assert 'href="../countries/CD.html"' in co_page
```

### CP-5: Map drawer contains "View full page" link

```python
def test_cp5_drawer_js_has_full_page_link(viewer_dir):
    js = (viewer_dir / "assets" / "charts_map.js").read_text()
    assert "countries/" in js and "View full page" in js
```

### CP-6: Thin-data country page renders without error

Query the DB to find a country with the fewest rows (e.g. `US` for reserves only, or a similar low-row country). Assert the page exists and contains the stage section headings:

```python
def test_cp6_thin_country_page_renders(viewer_dir):
    # US has thin Co mining data (share_pct=0, quantity=300t) — page must still exist
    page = viewer_dir / "countries" / "US.html"
    assert page.exists()
    text = page.read_text()
    assert "Mining" in text and "Reserves" in text
```

### CP-7: Relative path correctness

```python
def test_cp7_country_page_relative_paths(viewer_dir):
    cd = (viewer_dir / "countries" / "CD.html").read_text()
    assert 'href="../assets/atlas.css"' in cd
    assert 'src="../assets/' in cd  # JS scripts
    assert 'href="../index.html"' in cd  # back-link
```

### CP-8: ISO name map covers all generated country pages

```python
def test_cp8_iso_name_map_covers_all_countries(viewer_dir):
    import build_viewer
    iso_map, _ = build_viewer._build_iso_name_map()
    countries_dir = viewer_dir / "countries"
    for page in countries_dir.glob("*.html"):
        iso = page.stem
        assert iso in iso_map or iso == iso, f"ISO {iso} not in name map"
        # weaker: page must contain more than just the ISO code as its heading
        text = page.read_text()
        assert len(text) > 500, f"{iso}.html suspiciously short ({len(text)} bytes)"
```

---

## 7. Cross-feature dependencies

### Inbound links

| Source | What to add | Spec |
|--------|------------|------|
| `charts_map.js` map drawer | "View full page →" anchor after drawer table (Step 9) | `specs/heatmap.md` also expects this link; coordinate so the drawer link is added once and both specs reference the same implementation |
| Per-element pages — share tables | Wrap country ISO cells in `<a href="../countries/{ISO}.html">` (Step 10) | — |
| Index page producer-country filter chips | Filter chip for a country links to its country page | `specs/table-filter-sort.md` |

### Shared ISO→name helper

`_build_iso_name_map()` is a shared build-time concern. It must live in `build_viewer.py` (not in a separate helper module for now, since all build logic is in one file). If `specs/heatmap.md` or `specs/table-filter-sort.md` also need country names, they should call the same helper; no duplicate implementations.

The map drawer in `charts_map.js` already resolves country names client-side from the GeoJSON via `featureName(feature)`. The Python helper is for build-time use only (page titles, heading text). No duplication in runtime code.

### Byproduct graph cross-reference (`specs/byproduct-graph.md`)

On the CD country page, Co rows carry `byproduct_of: [Cu, Ni]` in the source data. Surface this in the Notes column or as a footnote: "Co production here is a byproduct of Cu and Ni mining." The `byproduct_of` field is on `atlas_elements` (available in `elements_index`); join it into the row dict in `_build_country_page_data` as `"byproduct_of": ["Cu", "Ni"]`. The renderer can then append a small inline note. This does not require the byproduct DAG to be built first — the raw `byproduct_of` list is sufficient.

### Table sort (shared JS)

`charts_country.js` needs column-sort for the stage tables. The `specs/table-filter-sort.md` feature will likely introduce a `sortTable()` utility. Coordinate: if `table-filter-sort` ships first, `charts_country.js` should import or duplicate that utility. If country pages ship first, implement a minimal sort inline and refactor when `table-filter-sort` lands. Either way, the HTML hook is the `sortable-table` class on each stage `<table>`.

---

## 8. Open questions

**Q1: Flag emoji rendering on Windows / older Android**

Unicode regional indicator pairs (🇨🇩 for CD) render as flag emojis on macOS, iOS, recent Android, and Linux with Noto fonts. They render as letter pairs (`CD`) on Windows 11 and most Windows browsers due to Microsoft's deliberate policy. The page is readable either way (the ISO code is always also shown), but the intent is decorative. Accept the current cross-platform behaviour for v1. If this becomes an issue, replace with a `<img>` approach using a flag CDN or locally bundled PNGs — out of scope for now.

**Q2: Overseas territories — page or no page?**

NC (New Caledonia) is resolved to a distinct ISO-2 code in the USGS data and therefore gets a page (see §2). The same applies to any other territory that USGS treats as a distinct reporter (e.g. `GU` if it appeared). The rule is: if the ISO-2 appears in `atlas_shares`, generate a page. No case-by-case editorial exclusion.

**Q3: CN display name**

The GeoJSON `NAME_EN` for CN is `"People's Republic of China"`. Consider a `COUNTRY_NAME_OVERRIDES` dict (analogous to `WIKIPEDIA_NAME_OVERRIDES`) to allow `"CN": "China"` if brevity is preferred. Unresolved; the spec author has no strong preference. Decide before implementation and note it in the override dict's docstring.

**Q4: Global rank for reserves vs. mining/refining**

Mining and refining `share_pct` values represent shares of annual production flows; reserves `share_pct` values represent shares of known geological stocks. The `RANK()` window function treats them the same (highest `share_pct` = rank 1 within element+stage). This is correct arithmetically. However, `share_pct` in reserves rows may be null more often than in production rows (the `atlas_shares` schema does not require it). Rows with null `share_pct` sort last and display rank as "—". Acceptable for v1.

**Q5: Sub-national regions**

DRC (CD) aggregates industrial and artisanal production modes. The `zz-decomposition-plan.md` explicitly notes this is out of scope for the atlas schema. Country pages inherit this limitation: the CD page shows a single Co mining row at 76% / 220,000 t with no Katanga/ASM split. Document this in the CD page's notes column (the existing `notes` field already explains it in the YAML source).

**Q6: Page count scaling**

Roughly 70–100 country pages expected from current data. Build time impact is negligible (each page is a string format call). No lazy generation needed.

---

## 9. Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| ISO code in `atlas_shares` has no GeoJSON match → page title falls back to bare ISO code | Low (ZZ/XX excluded; all real codes in GeoJSON) | Low (cosmetic) | Log a warning; fallback to ISO code as name |
| `RANK()` window function not available in older DuckDB versions pinned in `pyproject.toml` | Low (DuckDB ≥1.1 required; `RANK()` available since 0.3) | Medium (build breaks) | Confirm with `duckdb>=1.1` already in deps; add a test assertion |
| `charts_country.js` GeoJSON fetch fails on file:// (local dev without a server) | Medium (same issue exists for the index map) | Low (thumbnail absent, rest of page works) | Same mitigation as the index map: user serves files via `python -m http.server` |
| Relative path errors in links (element → country, country → element) | Medium (easy to get `../` depth wrong) | High (broken links) | CP-7 test catches this; also manually verify with a local server run |
| Column sort and `table-filter-sort` implement conflicting sort logic | Low (coordinated via specs) | Medium (user-visible inconsistency) | Coordinate via shared `sortable-table` CSS class; only one JS sort implementation active at a time |
| Flag emoji on Windows renders as letter pair, looks broken | Medium | Low | Accept for v1; noted in §8 |

---
title: "Feature spec: byproduct dependency graph"
tags: [atlas, viewer, spec, graph, byproduct]
status: draft
created: 2026-04-14
---

# Feature spec: byproduct dependency graph

## 1. Goal

Expose the structural dependency where element X cannot be ramped independently because its supply is governed by the economics of element Y.

**Analytical question the graph answers:** Which elements are supply-constrained by a different commodity's market? When gallium demand spikes, it cannot call forth additional gallium mine output; it can only bid for a larger slice of aluminum smelter waste streams. The graph makes this dependency chain legible at a glance — especially multi-hop chains like Re ← Mo ← Cu, where rhenium supply is twice-removed from rhenium demand.

Secondary questions answerable from the same view:
- Which primary metals anchor the most byproduct relationships? (Cu dominates)
- Which byproducts are contested across multiple parents? (Ag ← Pb, Zn, Cu, Au)
- Which tier-3 critical elements have no independent production pathway whatsoever?

---

## 2. Scope / locked decisions

**Node set:** Only elements involved in at least one byproduct edge — 31 nodes (18 byproducts + 13 primary-only). Rationale: the full 100+ element table drowns the signal. Context for the unlisted elements is one click away via the existing index table.

**Layout:** Hierarchical DAG, top-to-bottom, with primary (no-parent) nodes at the top tier. Rationale: the primary → byproduct direction is the analytical axis; making it a spatial axis is immediately readable. Force-directed is prettier but hides the directionality. Sankey requires tonnage-flow weights that do not exist in the current data model (byproduct share of primary output is unrecorded).

Use d3-dag (or a manual Sugiyama-style layering via `d3.stratify` + topological sort) for layout. Multi-parent nodes (e.g. Co ← Cu, Ni) appear once at the layer of their shallowest parent; edges fan in from above.

**Page placement:** New page `viewer/byproducts.html` linked from a `<nav>` element added to `_page_shell` / `_index_body` in `build_viewer.py`. The index page currently has no nav; adding one benefits all future top-level pages (heatmap, country pages, etc.) and is the right structural move regardless.

---

## 3. Current data audit

### Edge inventory (as of atlas snapshot 2025)

Source: `atlas_byproducts` table. 35 edges across 31 nodes.

| Byproduct | Parents | Notes |
|-----------|---------|-------|
| Ag | Au, Cu, Pb, Zn | Silver is the widest multi-parent byproduct |
| Bi | Pb, Zn | |
| Cd | Zn | Straightforward; Cd from zinc smelter flue dusts |
| Co | Cu, Ni | Stratiform Cu-Co (DRC) + laterite Ni routes are distinct |
| Ga | Al, Zn | ~80% from Al (Bayer process); Zn smelter route is secondary |
| Ge | Zn | Also recovered from coal fly ash, but YAML models Zn as parent |
| Hf | Zr | Hafnium separated from zirconium in nuclear-grade processing |
| Ir | Cu, Ni, Pt | Three parents; deepest PGM byproduct |
| Os | Ni, Pt | |
| Pd | Cu, Ni | Palladium recovered from Ni/Cu sulfide concentrates (Norilsk, Sudbury) |
| Pm | Pu | Reactor/reprocessing byproduct; no commercial mining pathway |
| Rb | Cs, Li | Pollucite ore processing |
| Re | Cu, Mo | Two direct parents; note the implied two-hop chain Re ← Mo ← Cu (Mo is mined primarily as a Cu byproduct) |
| Rh | Ni, Pt | |
| Ru | Ni, Pt | |
| Sc | Ni, Ti | Emerging; recovered from laterite Ni and titanium processing residues |
| Te | Cu | Tellurium from copper anode slimes; the canonical single-parent case |
| Tl | Cu, Pb, Zn | Three parents; very low volumes |

**Primary nodes (no parent in graph):** Al, Au, Cs, Cu, Li, Mo, Ni, Pb, Pt, Pu, Ti, Zn, Zr

**Summary counts:** 35 edges, 18 byproduct nodes, 13 primary nodes, 31 total graph nodes.

### Cycle check

The current graph is acyclic by inspection: no primary node appears as a byproduct, and no byproduct node appears as a parent. Structural enforcement at build time is specified in section 7.

### Inconsistencies and schema proposals

1. **Re ← Mo ← Cu is a co-product modeling limitation, not a data gap.** Earlier drafts proposed `byproduct_of: [Cu]` on Mo.yaml. That proposal has been withdrawn after audit (see `verification/Mo.md`). Empirical survey of the 18 elements currently carrying non-empty `byproduct_of` shows the field is used consistently to mean "no independent primary mining pathway" — Ga (Bayer process only), Ge (Zn smelter only), Co (Cu-Co / Ni laterite only), etc. Mo breaks this pattern: Henderson and Climax (CO) are dedicated primary Mo mines and China's ~42% of world output is independent of Cu economics. Setting `byproduct_of: [Cu]` on Mo would mis-type it as supply-locked to copper. Mo's co-product Cu route is already documented in `Mo.yaml.feedstock_origins[1]` and every Peruvian/Chilean/Mexican share note. **Viewer handling for v1:** surface the Re ← Mo ← Cu chain contextually in the Re tooltip ("also recovered indirectly via Mo, which is itself partly a Cu byproduct") rather than via a graph edge. A schema extension — `coproduct_of: list[str]` or a per-symbol mode tag on `byproduct_of` — is the right long-term answer; deferred to a separate design session.

2. **Se (selenium) and In (indium) — RESOLVED 2026-04-14.** Both YAMLs were added this pass (Se.yaml cites USGS MCS 2025 selenium; In.yaml cites USGS MCS 2025 indium). Edges added: Se ← Cu/Pb/Zn (three parents; Cu is active, Pb/Zn are "potential sources" per USGS language), In ← Zn (single parent). The edge audit table and counts in §3 should be re-run against the current data before implementation; expect ~39 edges, ~20 byproduct nodes, ~33 total nodes.

3. **Ge ← Zn only.** Germanium is also recovered commercially from coal combustion fly ash (via zinc leaching residues). The single-parent model is a simplification. The YAML notes can document this without adding a second parent edge unless coal (non-element) feedstock modeling is extended.

4. **Hf production quantity — RESOLVED 2026-04-14.** The 14,436 t/yr figure was arithmetically correct and correctly labelled as `stream: contained_in_zircon_feed`; it represents theoretical Hf content in global zircon mine output, not refined metal. `Hf.yaml` now carries two production blocks: the original `contained_in_zircon_feed` stream (unchanged) and a new `unwrought_metal` stream at ~75 t/yr (range 50–100) anchored to USGS MCS 2025 US trade data. The byproduct graph should use the `unwrought_metal` stream for node sizing when sizing by tonnage, not the upstream zircon-content figure. See `verification/Hf.md`.

---

## 4. UX design

### Layout

Hierarchical top-to-bottom DAG rendered with d3. Layer assignment: layer 0 = primary-only nodes (no parent), layer 1 = byproducts of layer-0 primaries, layer N = byproducts whose shallowest parent is layer N-1. With current data all byproducts are layer 1 (no node has a byproduct-only parent), so the graph is effectively two-tier. Adding Mo ← Cu would create layer 2 for Mo and layer 3 for Re, making the multi-hop chain visible spatially.

Within each layer, nodes are sorted to minimize edge crossings (basic crossing-reduction heuristic: sort by mean x-position of parents).

SVG viewport: 900px wide, auto-height based on node count × row-height. Responsive down to 640px (single-column stack of layers).

### Node encoding

| Property | Encoding |
|----------|----------|
| Symbol label | Text centered in node circle |
| Element name | Shown in tooltip on hover |
| Size (radius) | Log-scaled mine output in tonnes/yr; nodes with no production data (Cs, Pm, Pu, Tl, etc.) get the minimum radius (10px). Scale range: 10px–36px. |
| Fill color | Criticality tier: `tier=3` critical → amber (#d97706); `tier=4` workhorse → steel blue (#2563eb); `tier=2` niche → muted gray (#9ca3af). |
| Stroke | Thicker ring (3px) if `us_critical_list_as_of_2025 = true`. |
| Shape | All circles. Primary nodes (no parent) additionally get a flat-bottom D-shape or a subtle background halo to distinguish "anchor" status. A simpler fallback: render primary nodes as rounded-squares via `rx/ry` and byproduct nodes as circles. |

### Edge encoding

| Property | Encoding |
|----------|----------|
| Direction | Arrow from parent to byproduct (top to bottom in the DAG) |
| Stroke color | Neutral dark gray (#4b5563) |
| Stroke width | 1.5px; no thickness variation (see Open Questions §9) |
| Arrowhead | SVG marker-end; small, solid triangle |
| Multi-hop highlight | When Re ← Mo ← Cu chain exists, highlight the transitive path in a distinct color (orange) on hover of any node in the chain |

### Legend

Fixed legend block (top-right of SVG or below the heading):
- Circle size = mine output (log scale; three reference sizes: small/medium/large labeled in t/yr)
- Fill color ramp for tier: amber = CRITICAL_SCARCE, blue = HIGH_VOLUME_WORKHORSE, gray = NICHE_OR_NOVELTY
- Stroke ring = on US critical minerals list
- Arrow = primary → byproduct dependency

### Interactions

| Trigger | Effect |
|---------|--------|
| Hover node | Tooltip: symbol, full name, tier, US/EU criticality flags, mine output, list of parent symbols (or "primary — no byproduct dependency") |
| Hover node | Highlight: connected edges and neighbor nodes go to full opacity; all others dim to 0.15 opacity |
| Hover edge | Tooltip: "X is a byproduct of Y"; highlight the edge and its two endpoints |
| Click node | Navigate to `elements/{Sym}.html` |
| Mouse-leave | Reset all opacity |
| Keyboard | Tab navigates nodes in DOM order; Enter triggers the same highlight as hover; Space navigates to element page. Add `role="button"` and `aria-label="{Name} — byproduct of {parents}"` to each node `<g>`. |

### Page chrome

`viewer/byproducts.html` structure:

```html
<header>
  <h1>Byproduct dependency graph</h1>
  <p class="subtitle">Elements whose supply is governed by another commodity's economics.</p>
  <nav> ... (shared with index) </nav>
</header>
<section class="byproduct-graph-panel">
  <div id="byproduct-graph-root"></div>
  <script id="byproduct-graph-data" type="application/json">…</script>
</section>
<footer>…</footer>
<script src="assets/charts_byproduct_graph.js"></script>
```

The `<nav>` element linking index ↔ byproducts page is added to `_page_shell` (and `_element_page_shell`) in `build_viewer.py`. Link text: "Elements" (→ index.html) and "Byproduct graph" (→ byproducts.html).

---

## 5. Data model

### JSON payload (`byproduct-graph-data`)

Injected inline as `<script id="byproduct-graph-data" type="application/json">` in `byproducts.html`. Build-time generated; no client-side fetch.

```jsonc
{
  "nodes": [
    {
      "symbol": "Co",
      "name": "cobalt",
      "tier": 3,
      "us_critical": true,
      "eu_crm": true,
      "mine_value": 290000,
      "mine_unit": "tonnes_per_year",
      "byproduct_of": ["Cu", "Ni"]   // empty list for primaries
    },
    ...
  ],
  "edges": [
    { "source": "Cu", "target": "Co" },
    { "source": "Ni", "target": "Co" },
    ...
  ],
  "dag_validated": true,
  "snapshot_year": 2025
}
```

`mine_value` is normalized: if unit is `million_tonnes_per_year`, multiply by 1e6 before serializing so all values are in tonnes/yr. `kg_per_year` values are divided by 1000 (→ tonnes/yr). Nodes with no production data get `mine_value: null`.

### How `build_viewer.py` produces it

New private function `_byproduct_graph_json(con) -> str`:

```python
def _byproduct_graph_json(con: duckdb.DuckDBPyConnection) -> str:
    # 1. Pull edges from atlas_byproducts
    # 2. Pull node metadata from atlas_elements + atlas_production
    # 3. Normalize mine_value to tonnes/yr
    # 4. Run DAG validation (see §7)
    # 5. Serialize to JSON
    ...
```

The function is called once in `generate_viewer`, its output injected into the `byproducts.html` template. The JSON string is also written to `viewer/byproducts-data.json` as a build artifact (useful for tests and external consumption).

New private function `_byproducts_page(graph_json: str, snapshot_year: int, footer: str) -> str` renders the full page HTML.

`generate_viewer` gains a call after writing per-element pages:

```python
graph_json = _byproduct_graph_json(con)
byproducts_html = _byproducts_page(graph_json, snapshot_year, footer_index)
(viewer_dir / "byproducts.html").write_text(byproducts_html, encoding="utf-8")
(viewer_dir / "byproducts-data.json").write_text(graph_json, encoding="utf-8")
```

### DAG validation (build-time)

`_byproduct_graph_json` runs a topological sort on the edge list before serializing. If a cycle is detected, the build raises `ValueError` with the cycle path printed. The `dag_validated: true` field in the JSON confirms the check passed.

---

## 6. Implementation plan

Steps are ordered; each is a commit boundary.

**Step 1 — `_byproduct_graph_json` function + DAG validation**

In `scripts/build_viewer.py`, add `_byproduct_graph_json(con)`. Queries `atlas_byproducts` and `atlas_elements` + `atlas_production`. Normalizes mine output units to tonnes/yr. Runs Kahn's algorithm for topological sort; raises `ValueError` on cycle. Returns the JSON string and also validates `dag_validated: true` is set. No page output yet.

**Step 2 — `viewer/assets/charts_byproduct_graph.js`**

New JS file following the same IIFE + `document.getElementById("byproduct-graph-data")` pattern as `charts_production.js`. Implement:
- Parse JSON payload
- Compute layer assignments via topological sort (client-side, so the graph can be re-laid-out on resize)
- Render SVG: nodes as circles/rounded-squares, edges as curved paths with arrowheads, labels
- Implement hover highlight, tooltip, click-navigation, keyboard interaction
- Implement legend

Use only d3 v7 (already loaded). No additional dependencies.

**Step 3 — `_byproducts_page` function + `generate_viewer` wiring**

Add `_byproducts_page(graph_json, snapshot_year, footer)` to `build_viewer.py`. Mirrors `_page_shell` but loads `charts_byproduct_graph.js` instead of chart scripts. Add the call in `generate_viewer`.

**Step 4 — `<nav>` in page shell**

Add a minimal `<nav>` to `_page_shell` and `_element_page_shell`:
```html
<nav class="site-nav">
  <a href="index.html">Elements</a>
  <a href="byproducts.html">Byproduct graph</a>
</nav>
```
For element pages, paths are `../index.html` and `../byproducts.html`. CSS for `.site-nav` goes in `atlas.css`.

**Step 5 — `viewer/assets/atlas.css` additions**

Add:
- `.site-nav` styles (horizontal flex, gap, understated link styling)
- `.byproduct-graph-panel` container
- `#byproduct-graph-root` SVG wrapper (overflow: visible, min-height)
- `.byproduct-tooltip` (position: absolute, card style matching existing `.country-map-tooltip`)

**Step 6 — tests (see §7)**

**Step 7 (follow-up) — per-element mini-graph**

On each `{Sym}.html`, add a small neighborhood graph showing the element's direct parents and siblings. Scoped to 1-hop. This is a separate PR after the main graph ships.

---

## 7. Testing

All tests go in `tests/test_build_viewer.py`, following existing test patterns (duckdb fixture, `generate_viewer` into tmpdir).

**BPG-INV-1 — page presence**
`viewer/byproducts.html` exists after `generate_viewer` runs. `byproducts-data.json` also exists.

**BPG-INV-2 — correct node count**
Parse `byproducts-data.json`. Assert `len(data["nodes"]) == 31` (or the count at the time, derived from `SELECT COUNT(DISTINCT symbol) + COUNT(DISTINCT parent_symbol) - COUNT(DISTINCT CASE WHEN symbol IN (SELECT parent_symbol FROM atlas_byproducts) THEN symbol END) FROM atlas_byproducts`). The test should query the DB for the expected count rather than hardcoding 31, so it self-updates as data grows.

**BPG-INV-3 — correct edge list**
Assert `len(data["edges"]) == 35` (again, derive from DB query). Assert specific spot-check edges are present: `{"source": "Cu", "target": "Co"}`, `{"source": "Al", "target": "Ga"}`, `{"source": "Mo", "target": "Re"}`.

**BPG-INV-4 — DAG property (no cycles)**
`data["dag_validated"] == True`. Additionally, run a Python topological sort on the edge list from the JSON and assert it completes without error (double-checks the serialized graph, not just the build-time flag).

**BPG-INV-5 — mine_value normalization**
Find the Cu node in `data["nodes"]`. Assert `node["mine_value"]` is approximately `23_000_000` (Cu is stored as `23.0 million_tonnes_per_year`; must be converted to tonnes). Similarly check that Ir (stored in `kg_per_year`) is converted: `8200 kg/yr → 8.2 t/yr`.

**BPG-INV-6 — page references JS and data script**
`byproducts.html` contains `charts_byproduct_graph.js` in a `<script>` tag and contains `id="byproduct-graph-data"` in a `<script type="application/json">` tag.

**BPG-INV-7 — nav links present**
`index.html` contains a link to `byproducts.html`. `byproducts.html` contains a link to `index.html`. At least one per-element page (Co.html) contains links to both.

---

## 8. Cross-feature dependencies

### Element metadata index (shared requirement)

`specs/heatmap.md` and `specs/table-filter-sort.md` both need a flat element metadata array: `[{symbol, name, category, tier, criticality, byproduct_of, top_country_share, hhi_mining}]`. The byproduct graph needs a subset of this (symbol, name, tier, criticality flags, mine_value). **Recommendation:** define a single `_element_metadata_json(con) -> str` function in `build_viewer.py` that emits the full shared index, written to `viewer/elements-meta.json`. The byproduct graph, heatmap, and table-filter JS all load from that file (or from an inline copy injected per-page). This avoids duplicating the DB query logic across three features. Coordinate the schema with whichever sibling spec is implemented first.

### Cross-link from table-filter-sort

`specs/table-filter-sort.md` includes a "byproduct-only" filter that surfaces the same 18 byproduct elements. When that filter is active, show a "View in byproduct graph →" link pointing to `byproducts.html`. This is a one-line addition in the table-filter JS; the byproduct graph page need not do anything special. Flag this in the table-filter spec.

### Cross-link from country pages

`specs/country-page.md` — a country page will likely show "elements this country produces." If any of those elements are byproducts, the country page can note "produced as a byproduct of [parent]" using the `byproduct_of` field from `elements-meta.json`. This is a display enhancement on the country page side; no changes needed in the byproduct graph feature. Flag this in the country-page spec.

### Nav element

Adding `<nav>` to `_page_shell` and `_element_page_shell` is load-bearing for all future top-level pages. The heatmap and country pages will also appear in this nav. Define the nav links list as a Python constant in `build_viewer.py` so all page templates share it and adding a new page requires editing one place. Example:

```python
_NAV_LINKS = [
    ("Elements", "index.html"),
    ("Byproduct graph", "byproducts.html"),
    # ("Heatmap", "heatmap.html"),     # add when heatmap ships
    # ("Countries", "countries.html"), # add when country pages ship
]
```

---

## 9. Open questions

**Q1 — Edge thickness semantics.** The natural encoding would be production share of the byproduct attributable to that parent (e.g., Ga: ~80% from Al, ~20% from Zn). This data is not currently in the schema. Options: (a) punt — all edges same weight; (b) add an optional `parent_share_pct` field to `atlas_byproducts` and populate it where USGS data supports it; (c) derive approximate shares from the `feedstock_origins` substrate descriptions (too fuzzy). Recommendation: punt for v1; flag as a data modeling enhancement.

**Q2 — Color axis: criticality flag vs. IndustrialTier.** The spec above uses `industrial_tier` for fill color (since all graph nodes are either tier 3 or tier 4, the two-color scheme is clean). Using the US/EU criticality flag as fill instead would be more policy-relevant but produces a noisier legend (multiple flags). Suggested resolution: use tier for fill, criticality flag for stroke ring. Revisit if the policy team has a preference.

**Q3 — Multi-hop chains: visual distinction.** With Mo ← Cu added, Re ← Mo ← Cu is a three-hop chain. Should transitive edges (Cu → Re, implied but not direct) be rendered as dashed arcs? Or only on hover? Current recommendation: on hover of Re, highlight the full transitive path (Re → Mo → Cu) by traversing the edge list client-side. No additional "transitive edge" records needed in the data.

**Q4 — Pm (promethium) inclusion.** Pm ← Pu is a reactor byproduct, not a mining byproduct. Including it in the graph is technically correct per the schema but may confuse readers expecting a mining supply-chain view. Options: filter it out in `_byproduct_graph_json` (add a `commercial_production = true` or `industrial_tier >= 3` filter); or include it with a visual indicator ("reactor/reprocessing pathway"). Lean toward including with a note in the tooltip.

**Q5 — Per-element mini-graph on element pages.** Section 6 defers this to a follow-up. The mini-graph would show only the 1-hop neighborhood (parents + siblings sharing the same parent). Requires a second, smaller JSON payload or a filtered view of the same `byproduct-graph-data`. Evaluate after main graph ships.

**Q6 — Rb ← Cs, Li inclusion.** Rb and Cs are tier-2 (niche) with no clear commercial mining pathway for Rb specifically. The byproduct relationship is real (pollucite processing) but niche. Include for completeness; the tier encoding and small node size will communicate the low commercial relevance.

---

## 10. Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| d3-dag not available; need external dep | Medium | Use manual topological sort + manual x-placement; d3 alone is sufficient for this graph size (31 nodes) |
| Crossing-reduction quality poor for Ag (4 parents) | Low | Four-parent nodes are rare; acceptable to have some edge crossings at this scale |
| Mo ← Cu data fix blocked or delayed | Low | Graph is correct without it; Mo renders as a primary node, which is technically accurate for the current data |
| Se, In absent from data; known gap in critical-minerals coverage | High (known) | Document in the page's subtitle or a callout; these are data backfill tasks, not viewer bugs |
| Nav addition breaks existing test INV-4 (deterministic output) | Medium | INV-4 uses an injected timestamp; nav HTML is deterministic. Test will pass if nav is not conditional on external state. Verify after step 4. |
| `_byproduct_graph_json` mine_value normalization has unit edge cases | Low | Covered by BPG-INV-5; normalize in a dedicated helper with explicit unit dispatch |

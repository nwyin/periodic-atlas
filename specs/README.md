---
title: "Viewer feature specs — index & coordination"
tags: [atlas, viewer, spec, index]
status: active
created: 2026-04-14
---

# Viewer feature specs

Four specs were drafted together on 2026-04-14. They share infrastructure (element metadata payload, map drawer, nav, sort utility) and must be landed with that coordination in mind. This index records the cross-cutting decisions and the recommended build order.

## Specs

| # | File | Owner feature | Status |
|---|---|---|---|
| 1 | `heatmap.md` | Choropleth map mode: pick element + stage, color countries by `share_pct` (log scale). | draft |
| 2 | `table-filter-sort.md` | Index table filter chips (criticality, tier, category, end-use bucket, producer country, byproduct-only) + sort (incl. new HHI / top-country-share columns) + free-text search. | draft |
| 3 | `country-page.md` | New `viewer/countries/{ISO}.html` pages — inverse of per-element pages; mining / refining / reserves tabs, global rank per row. | draft |
| 4 | `byproduct-graph.md` | New page visualising `byproduct_of` DAG (35 edges, 31 nodes). Flags elements whose supply is governed by a different commodity's economics. | draft |

## Cross-cutting decisions — locked here, referenced in specs

These overrule any conflicting detail inside an individual spec.

### CC-1 — Shared element metadata payload

**Canonical: inline `<script id="atlas-element-index" type="application/json">` block in `index.html`, per-element-page shells, and the byproduct-graph page.**

Schema (superset of all consumer needs):

```ts
[{
  symbol: str,
  name: str,
  atomic_number: int,
  category: ElementCategory,          // transition_metal, lanthanide, ...
  tier: 0 | 1 | 2 | 3 | 4,             // industrial_tier
  commercial_production: bool,
  criticality: {
    us_critical: bool,
    eu_crm: bool,
    eu_strategic: bool,
    doe_rank: int | null
  },
  byproduct_of: string[],              // symbols
  top_mining_country: str | null,      // ISO-2
  top_mining_share: float | null,      // 0–100
  hhi_mining: float | null,            // 0–10000
  hhi_refining: float | null,
  end_use_buckets: string[]            // canonicalised buckets, see CC-2
}]
```

Owning function: `_build_element_index(con, elements_list) -> list[dict]` in `scripts/build_viewer.py`. Whoever ships first creates it; later specs **extend the same function and the same inline block** — no second artifact, no separate `elements-meta.json` file.

`byproduct-graph.md` originally proposed an external `elements-meta.json` artifact. **Override:** use the inline `#atlas-element-index` pattern for consistency with the existing `#atlas-country-map-data` block and to keep the viewer a zero-fetch static site.

### CC-2 — End-use canonicalisation

`EndUse.application` slugs are per-element free text (~400 unique). `table-filter-sort.md` introduces `END_USE_BUCKET_MAP` — a curated dict of ~14 canonical buckets (batteries, superalloys, semiconductors, magnets, catalysts, structural, …) with a `"other"` fallback and a build-time warning when unmapped share exceeds 20%.

The bucket list lives in `build_viewer.py` as a module-level constant, is surfaced on the element index as `end_use_buckets: string[]`, and is the only canonical source of "what industries consume element X." Heatmap, byproduct graph, and country pages read the same buckets where relevant.

### CC-3 — Byproduct graph page URL

**Canonical: `viewer/byproducts.html`** (plural, no hyphen), matching the `byproduct-graph.md` spec.

`table-filter-sort.md` currently refers to `byproduct-graph.html` at line 594 / 598 — **this is the URL to use at build time: `byproducts.html`**. Fix on implementation.

### CC-4 — Map drawer "View full country page →" link

Both `heatmap.md` and `country-page.md` add a "View full page →" link to the drawer in `viewer/assets/charts_map.js`. **Country-page spec owns this implementation** (the page is what's being linked to). Heatmap consumes the same link when in heatmap mode — it's stage-independent.

Placement: drawer header, right-aligned, below the country name. Links to `countries/{ISO}.html`. Hidden when pinned country is `ZZ` or when the country has no generated page.

### CC-5 — Shared sort utility

Both `table-filter-sort.md` (index table) and `country-page.md` (stage tables on country pages) need column sort. Factor into `viewer/assets/table_sort.js` — a tiny generic utility that takes a `<table>` element and wires clickable `<th>` headers. Both specs call this module rather than reimplementing.

If `country-page.md` lands first, it ships a minimal inline sort; the subsequent table-filter PR extracts and migrates both call sites to `table_sort.js`. Acceptable temporary duplication.

### CC-6 — Site navigation

The viewer has no global nav today. Byproduct-graph introduces one as `<nav class="site-nav">` inside `_page_shell` / `_element_page_shell`, driven by a `_NAV_LINKS` constant in `build_viewer.py`.

Initial link set:
```python
_NAV_LINKS = [
    ("Elements", "index.html"),
    ("Byproduct graph", "byproducts.html"),
]
```

Country pages, heatmap mode (no separate page), and the index all use the same nav. The nav lands with whichever of byproduct-graph or country-page ships first.

### CC-7 — Feature-flag pattern for cross-links

`table-filter-sort.md` ships links to country pages and the byproduct graph behind `COUNTRY_PAGES_ENABLED` and `BYPRODUCT_GRAPH_ENABLED` boolean constants in `build_viewer.py`. These exist **solely so the table filter can land first without producing broken links**; flip them in the PR that ships the destination pages. Remove the flags once both destinations have landed and the pattern is no longer load-bearing.

## Recommended implementation order

1. **`country-page.md`** — smallest surface area, builds the `_build_iso_name_map` helper and the map-drawer link (CC-4), ships the `<nav>` scaffolding (CC-6).
2. **`table-filter-sort.md`** — lands `_build_element_index` (CC-1), `END_USE_BUCKET_MAP` (CC-2), `table_sort.js` (CC-5). Flips `COUNTRY_PAGES_ENABLED = true`.
3. **`heatmap.md`** — extends `_build_element_index` only if the CC-1 schema is missing fields; otherwise consumes as-is. Augments the existing country-map payload with reserves rows.
4. **`byproduct-graph.md`** — ships `viewer/byproducts.html`. Flips `BYPRODUCT_GRAPH_ENABLED = true`. Removes both feature flags.

This order minimises merge pain: each later spec either consumes scaffolding from the earlier one verbatim, or extends it additively.

## Data integrity follow-ups

Surfaced by the byproduct-graph edge audit. Most were resolved on 2026-04-14.

| # | Finding | Status |
|---|---|---|
| D-1 | `elements/Se.yaml` and `elements/In.yaml` were missing. | **Resolved 2026-04-14.** Both YAMLs created with full USGS MCS 2025 citations and verification docs. Se: world 3,700 t (CN 49%, JP 19%), `byproduct_of: [Cu, Pb, Zn]`. In: world 1,080 t (CN 70%), `byproduct_of: [Zn]`. 107 elements now validate cleanly. |
| D-2 | `elements/Mo.yaml` has `byproduct_of: []`; was proposed to set to `[Cu]`. | **Reclassified as modeling limitation, not data bug.** Audit (see `verification/Mo.md`) shows Mo has meaningful primary production (Henderson/Climax in CO; ~42% of world output from China's primary mines). The existing `byproduct_of: []` is semantically correct under the prevailing "pure-byproduct only" interpretation of the field. `specs/byproduct-graph.md` §3 updated: Re ← Mo ← Cu chain handled contextually in tooltip rather than via a graph edge. Schema extension (`coproduct_of` or mode tags on `byproduct_of`) deferred to a separate design. |
| D-3 | `elements/Hf.yaml` shows production ~14,436 t/yr vs. expected ~70 t/yr. | **Resolved via reframing 2026-04-14.** The 14,436 figure is arithmetically correct and was already labelled `stream: contained_in_zircon_feed` — it represents theoretical Hf content in global zircon mine output, not refined metal. USGS MCS 2025 explicitly states world Hf production data are not available. Hf.yaml now carries two production blocks: the original upstream zircon-content stream plus a new `unwrought_metal` stream at ~75 t/yr (range 50–100, low confidence) anchored to USGS US trade data. Byproduct-graph viewer should size by `unwrought_metal`. See `verification/Hf.md`. |
| D-4 | `Pm ← Pu` is a reactor byproduct, not a mining byproduct. | **Unchanged.** Byproduct-graph spec §3 correctly excludes it via `commercial_production=true` + mining-mode filter. Revisit only if a nuclear-byproduct view is ever wanted. |

## Still-open data gaps (not in this pass's scope)

The enhanced `scripts/validate.py` now reports missing elements against the canonical 118-element list, with an `OUT_OF_SCOPE_SYMBOLS` opt-out for elements genuinely lacking a supply chain (currently: Es, Fm, Md, No, Lr). After D-1 was resolved, 6 commercially significant elements remain without YAMLs:

| Symbol | Z | Why it matters |
|---|---|---|
| Mg | 12 | Magnesium metal & magnesia — structural alloys, desulfurization; CN dominates |
| V | 23 | Vanadium — HSLA steels, redox-flow batteries; CN, RU, ZA |
| As | 33 | Arsenic — legacy pesticides, compound semiconductors; byproduct of Cu/Pb |
| Kr | 36 | Krypton — lighting, insulation gas; air separation byproduct |
| Xe | 54 | Xenon — lithography plasma, satellite thrusters; air separation byproduct |
| Th | 90 | Thorium — potential nuclear fuel cycle, mantles, alloying |

These are batched for a separate data-entry PR; the validator surfaces them on every run until they're either added or opted out.

## Validator coverage check (added 2026-04-14)

`scripts/validate.py` now reports three new classes of coverage issue:
- **Missing elements** — any canonical symbol (1–118) without a YAML, excluding `OUT_OF_SCOPE_SYMBOLS`.
- **Unexpected elements** — YAMLs whose symbol isn't in the canonical list (catches typos).
- **Dangling `byproduct_of` references** — an element cites a byproduct parent that has no YAML in the atlas.

All three are warnings, not errors — they don't fail validation. Rationale: scope decisions belong to the project author, not the validator.

## Open coordination questions (non-blocking)

1. **Element selector component** — heatmap, byproduct graph, and (conceivably) table filter all render an element dropdown. Factor into `viewer/assets/element_selector.js`? Defer until the second consumer exists (YAGNI).
2. **Hovercard** — multiple features show "element at a glance" hovercards. Single implementation or per-feature? Defer.
3. **URL state** — heatmap uses `?heatmap=Co&stage=mining`; table filter uses `?filter=...&sort=...`. No conflict today; revisit if they ever need to coexist on the same page.
4. **Accessibility** — keyboard navigation for map, graph, and filter chips is specced inconsistently. Do a pass after all four ship.

## See also

- `atlas/zz-decomposition-plan.md` — prior multi-element methodology pass.
- `atlas/src/atlas/models.py` — schema.
- `atlas/scripts/build_viewer.py` — the single file where all four features converge.

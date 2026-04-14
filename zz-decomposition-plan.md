---
title: "ZZ-Bucket Decomposition Plan"
tags:
  - atlas
  - plan
  - methodology
  - long-tail-producers
created: 2026-04-14
status: active
---

# ZZ-Bucket Decomposition Plan

## Problem

The atlas currently inherits USGS Mineral Commodity Summaries's reporting threshold: USGS names top producers by country and rolls everything else into an "Other countries" residual, represented in our YAML as `country: ZZ`. For some commodities this residual hides geopolitically material producers.

Motivating example: `Au.yaml` places 23.6% / 780 t of 2024 world gold production into `ZZ`. That bucket contains Sudan (~80 t/yr, largely artisanal, conflict-linked), Venezuela, DRC, Papua New Guinea, Philippines, Kyrgyzstan, Côte d'Ivoire, Guyana, and others — none of which individually meet USGS's naming threshold but several of which are analytically important (ASM economies, sanctions risk, conflict financing).

This plan decomposes the ZZ bucket for a targeted set of elements using authoritative secondary sources.

## Locked decisions

| Decision | Value |
|---|---|
| Element scope | 7 commodities: Au, Sn, Ta, W, Co (deferred), Li, REEs-as-group |
| Naming threshold | ≥ 1% of world total **OR** appears in ≥ 2 authoritative secondary sources at material tonnage |
| Pilot | Au |
| Cobalt | Deferred — its interesting split is within-country (DRC ASM vs industrial), a different problem |
| REEs | Decomposed at the `rare_earths` group level only; individual lanthanides not split |
| Scope of decomposition | `mining_by_country` only (not `refining_by_country`, not `reserves_by_country`) this pass |
| Schema changes | None — existing `CountryShare.source_id` / `confidence` / `Quantity.approximate` / `Source.source_tier` fields suffice |

## Methodology

1. **USGS world total is the anchor.** Decomposition happens *within* the ZZ bucket. The world total never inflates. Adding 120 t of Sudan gold means moving 120 t from ZZ to SD; it does not change the 3,300 t total.
2. **Per-row provenance.** Every new `CountryShare` carries its own `source_id`, `confidence` (typically `medium` or `low`), and `notes` citing the secondary source and its reporting year.
3. **Tier discipline.** New `Source` entries use `source_tier: secondary`. Primary (USGS) and secondary rows coexist in the same share list — the per-row `source_id` is the provenance trail.
4. **Quantities are approximate.** All secondary-sourced `Quantity` values set `approximate: true`.
5. **List-level completeness.** After decomposition the share list retains `completeness: complete` if it still sums to 95–105%; otherwise downgrade to `top_producers_only`.
6. **Narrative update.** Each decomposed element gets a sentence in `narrative` noting the long-tail augmentation and its source tier.
7. **Verification note.** Each decomposed element's `verification/{Sym}.md` is updated with a short subsection documenting the added rows and their provenance.

## Per-element workflow

For each target element:

1. Read current YAML; capture named producers, ZZ residual tonnage, USGS world total, reporting year.
2. Research secondary sources; build a candidate long-tail list (country, tonnage, source).
3. Apply the naming threshold; select candidates that qualify.
4. Draft new `CountryShare` rows (per-row `source_id` / `confidence: medium|low` / `Quantity.approximate: true`).
5. Decrement ZZ tonnage by the sum of new named tonnages.
6. Append new `Source` entries with `source_tier: secondary` and `retrieved: 2026-04-14` (or actual retrieval date).
7. Update `narrative` with one sentence on decomposition methodology.
8. Update `verification/{Sym}.md`.
9. Run `uv run atlas/scripts/validate.py` and `atlas/scripts/build.py`; confirm validation passes.
10. Commit.

## Element tracker

| # | Element | File(s) | Status | Primary secondary sources | Outcome |
|---|---|---|---|---|---|
| 1 | Au | `elements/Au.yaml` | **done** (2026-04-14) | WGC, SWISSAID, ICG, USGS MYB, corporate disclosures | 13 countries named (SD, CI, GN, AR, VE, PG, CL, BO, ZW, PH, CD, DO, TR); ZZ 780 t → 227 t; 14 new sources |
| 2 | Sn | `elements/Sn.yaml` | **done** (2026-04-14) | ITA, Andrada Mining, Ecofin Agency | 2 countries named (NA, UG); ZZ 1,800 t → 200 t; 4 new sources. USGS already dense — minimal headroom |
| 3 | Ta | `elements/Ta.yaml` | **reviewed, no change** (2026-04-14) | T.I.C., ITSCI, UN GoE S/2024/969, BGS | ZZ only 14 t / 0.67% — USGS names down to 0.1%. No YAML edit; verification note documents analytical findings (Rubaya/M23, DRC↔RW attribution, ITSCI unit confusion) for a follow-up pass |
| 4 | W | `elements/W.yaml` | **done** (2026-04-14) | BGS WMP 2019-2023, USGS MYB country chapters | 3 countries named (CD, MN, BR); ZZ 1,500 t → 520 t; 3 new sources. BGS-USGS Vietnam reporting-basis discrepancy flagged |
| 5 | Li | `elements/Li.yaml` | **done** (2026-04-14) | Nevada Div. of Minerals, Albemarle 10-K (SEC) | 1 country named (US, reconstructing USGS's withheld figure); ~3,500 t; explicit ZZ added at ~1,000 t; 2 new sources; completeness top_producers_only → complete |
| 6 | REEs (group) | `elements/Ce.yaml` (canonical carrier) | **done** (2026-04-14) | USGS MCS 2025, corporate disclosures | No new country qualified; primary output was a **data correction** — the TZ 13,000 t row was actually Thailand; phantom TH 300 t row removed. Brazil flagged for next cycle due to Serra Verde ramp |
| 7 | Co | `elements/Co.yaml` | **out of scope** (2026-04-14) | — | ZZ bucket only 2%; the interesting split is within-DRC (ASM vs industrial), which is an architectural problem (schema has no native concept). User decision 2026-04-14: within-country splits and edge-case ZZ accuracy are out of scope for this atlas. No further work. |

## Summary (2026-04-14)

Pass completed across 6 elements in a single session. Au was the outlier (23.6% ZZ, 13 named additions). All other elements had sub-2% ZZ residuals: Sn/W/Li received 1–3 named additions each via the 2-secondary-sources rule; Ta and REEs required no YAML decomposition but the REE review surfaced a significant data correction (TZ/TH mis-labelling in Ce.yaml). Aggregate: **19 new country rows added; 23 new sources introduced; 1 data-integrity fix applied; 5 verification docs updated**. All files pass validation and build cleanly.

Key methodological takeaway: the 1%-or-two-sources threshold does real work — without the 2-source arm, only Au and (borderline) W would have seen meaningful decomposition. With it, Sn and Li also yielded defensible additions. USGS already names aggressively for most commodities, so the analytical payoff of this pass is concentrated in Au.

## Deferred / out of scope (this pass)

- **Cobalt** (see above).
- **Refining-side decomposition** (`refining_by_country`). Many ZZ residuals on the refining side are larger and more geopolitically material than on the mining side (e.g., Chinese refining concentration). Separate pass.
- **Reserves-side decomposition** (`reserves_by_country`). Low analytical value given reserves are noisier than production.
- **Sub-national splits** (ASM vs industrial within one country). Schema does not natively support this; needs a separate design.
- **Individual lanthanide splits** below the REE group level.
- **Coverage threshold metadata field** on `CountryShareList` (e.g., `coverage_threshold_pct`). Deferrable; consider for schema v0.3.
- **Viewer changes** — no UI tier-color-coding in this pass.

## Validation expectations

After each element is decomposed:

- `CountryShareList` `shares` still sums to 95–105% (enforced by `check_completeness`).
- All per-row `source_id` values resolve to entries in `Element.sources` (enforced by `source_ids_resolve`).
- New `Source` entries have `source_tier: secondary`, non-null `retrieved`, non-null `publication_year`.
- Build step (`atlas/scripts/build.py`) succeeds.

## Risks

| Risk | Mitigation |
|---|---|
| Secondary totals conflict with USGS world total | Anchor on USGS world total; shrink ZZ to fit; never inflate |
| Staleness: secondary sources lag USGS by 1–2 years | Reporting year stated per row; accept up to 2-year lag with a note |
| Tier creep (mixing primary + secondary invisibly) | Per-row `source_id` and `confidence` — the row itself carries its tier |
| Over-inclusion of marginal producers | Enforce the 1%-or-two-sources threshold strictly |

## Open questions (non-blocking)

1. Should we add a `coverage_threshold_pct` field to `CountryShareList` to self-document the naming rule? Defer to v0.3 schema bump.
2. Should the viewer color-code shares by `source_tier`? Useful but not required for this pass.
3. Should cobalt within-country ASM get its own schema concept (e.g., `production_mode_split`)? Decide after the ZZ-decomposition work lands and we can assess patterns.

---

See also: `sources-and-methodology.md` in the parent inquiry folder, `atlas/src/atlas/models.py` (schema).

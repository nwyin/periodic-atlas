# Verification: Tl

- Element: thallium (Tl)
- Snapshot year: 2025
- Verifier: worker-2416ef443821
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 7 |
| discrepancy | 0 |
| inferred | 1 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 10000 kg_per_year | usgs_mcs_2025_thallium | verified | "In 2023 ... global production of thallium was estimated to be about 10,000 kilograms." p.2 |
| end_uses.uses[0].share_pct | 100 % | usgs_mcs_2025_thallium | inferred | USGS lists multiple specialty uses for thallium but provides no percentage split: "The primary end uses included the following..." followed by the use list on p.1, and "The primary global uses for thallium include gamma radiation detection equipment, high-temperature superconductors, infrared optical materials, low-melting glass, photoelectric cells, and radioisotopes." p.2. The YAML's single 100% bucket is an aggregation inferred from the absence of a published breakdown. |
| prices[0].value | 9500 usd_per_kg | usgs_mcs_2025_thallium | verified | "Price, metal, dollars per kilogram ... 2024e ... 9,500" p.1 |
| prices[1].value | 8800 usd_per_kg | usgs_mcs_2025_thallium | verified | "Price, metal, dollars per kilogram ... 2023 ... 8,800" p.1 |
| prices[2].value | 9400 usd_per_kg | usgs_mcs_2025_thallium | verified | "Price, metal, dollars per kilogram ... 2022 ... 9,400" p.1 |
| prices[3].value | 8400 usd_per_kg | usgs_mcs_2025_thallium | verified | "Price, metal, dollars per kilogram ... 2021 ... 8,400" p.1 |
| prices[4].value | 8200 usd_per_kg | usgs_mcs_2025_thallium | verified | "Price, metal, dollars per kilogram ... 2020 ... 8,200" p.1 |
| geopolitical_events[0].impact | 1620 kilograms imported to Puerto Rico | usgs_mcs_2025_thallium | verified | "a significant quantity of thallium waste and scrap (1,620 kilograms) was imported to Puerto Rico from the Dominican Republic in July 2024" p.1 |

## Notes
`elements/Tl.yaml` is absent from this worktree, so verification used the authored file from git commit `15392c0f435fe77bdb0a30e94b94e3a5677c6418` via `git show`. No sourced numeric reserve totals, reserve shares, production shares, feedstock quantities, substitute quantities, or criticality-list citations are present in the YAML, so no additional numeric rows were required for this pass.

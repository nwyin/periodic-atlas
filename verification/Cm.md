# Verification: Cm

- Element: curium (Cm)
- Snapshot year: 2025
- Verifier: agent worker-95c6be70f283
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 3 |
| discrepancy | 0 |
| inferred | 4 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| feedstock_origins[0].notes (production route precursor) | plutonium-242 | nidc_cm244_product_2024 | verified | NIDC Cm-244 product sheet: "Production Route: Successive neutron captures and beta decays of plutonium-242." |
| feedstock_origins[1].notes (production route precursor) | californium-252 | nidc_cm248_product_2024 | verified | NIDC Cm-248 product sheet: "Production Route: Decay of californium-252." |
| end_uses.uses[0].share_pct | 100 | ornl_mirig_2025 | inferred | ORNL MIRIG says curium-248 is used in "a variety of research applications such as super-heavy element discovery," but the page does not publish a quantified 100% end-use split. |
| geopolitical_events[0].date | 2025-09-30 | ornl_isotope_supply_chain_2025 | verified | ORNL article header: "Published: September 30, 2025." |
| criticality.us_critical_list_as_of_2025 | false | usgs_critical_minerals_2025 | inferred | USGS 2025 draft list page enumerates 54 minerals from "Samarium" through "Scandium"; curium is not listed, so the false flag is inferred from omission rather than stated directly. |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | inferred | EUR-Lex Annex II snippet lists critical raw materials such as "antimony ... tungsten ... vanadium"; curium does not appear, so the false flag is inferred from omission. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | inferred | EUR-Lex Annex I snippet lists strategic raw materials such as "bauxite/alumina/aluminium ... platinum group metals ... tungsten"; curium does not appear, so the false flag is inferred from omission. |

## Notes

`elements/Cm.yaml` is absent from this worktree, so verification used the exact historical file from `git show d09fe75:elements/Cm.yaml` without modifying any element data.

Cm has no sourced production tonnage, reserves, prices, or substitute-share figures in the recovered YAML. The only source-backed structured claims with numeric content are the two isotope-number feedstock routes, the 100% end-use share, and the dated geopolitical event. The three criticality flags are included because they are in scope, but they are necessarily `inferred` claims: the cited USGS and EU sources publish positive lists, not explicit "curium is not listed" statements.

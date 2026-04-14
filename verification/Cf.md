# Verification: Cf

- Element: californium (Cf)
- Snapshot year: 2025
- Verifier: worker-f7544b856112 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 5 |
| discrepancy | 0 |
| inferred | 5 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].producers.shares[US].share_pct | 70 | ornl_cf252_contract_2013 | verified | "Cf-252 produced at ORNL supplies approximately 70 percent of global demand for the material." — ORNL contract announcement, published February 28, 2013 |
| isotope_markets[0].producers.shares[RU].share_pct | 30 | ornl_cf252_contract_2013 | inferred | "The only other facility capable of producing Cf-252 is in Dimitrovgrad, Russia. Cf-252 produced at ORNL supplies approximately 70 percent of global demand for the material." — residual share for Russia is implied as 30%, not stated directly |
| feedstock_origins[0].substrate | curium_composite_targets | ornl_cf252_sheet | verified | "Using the hot cells in the Radiochemical Engineering Development Center (REDC), curium composite pellets are made and placed in specially designed targets." — ORNL Cf-252 sheet, p.1 |
| substitutes[0].availability | none | ornl_cf252_contract_2013 | inferred | "\"Californium-252 serves as a unique, portable neutron source\" ... used for \"applications that focus mostly on analysis, detection and nuclear energy.\"" — uniqueness and breadth of use support no full drop-in substitute, but the source does not literally say "none" |
| end_uses.uses[0].share_pct | 100 | ornl_cf252_sheet | inferred | "Cf-252 is an intense neutron source with a wide range of industrial applications." The sheet lists reactor startup plus port security, energy exploration, and cement analysis; 100% is an analyst roll-up for the isotope's neutron-source market, not a stated percentage |
| criticality.us_critical_list_as_of_2025 | false | us_federal_register_critical_minerals_2025 | inferred | "The final 2025 List of Critical Minerals ... includes the following 60 minerals: aluminum, antimony, arsenic, barite, beryllium, bismuth, boron, cerium, cesium, chromium, cobalt, copper, dysprosium, erbium, europium, fluorspar ... zirconium." — Californium does not appear in the cited list |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | inferred | "The following raw materials shall be considered critical: (a) antimony ... (o) hafnium ... (aa) platinum group metals ... (ah) vanadium." — Annex II of Regulation (EU) 2024/1252; californium does not appear in the critical raw materials list |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | inferred | "The following raw materials shall be considered strategic: (a) bauxite/alumina/aluminium ... (m) platinum group metals ... (q) tungsten." — Annex I of Regulation (EU) 2024/1252; californium does not appear in the strategic raw materials list |
| geopolitical_events[0].date | 2025-09 | ornl_isotope_investment_2025 | verified | "Published: September 30, 2025" — ORNL facility-investment article |
| geopolitical_events[0].event / impact | nearly $1 billion | ornl_isotope_investment_2025 | verified | "Together, they account for nearly $1 billion in proposed Department of Energy funding." — ORNL facility-investment article |

## Notes

`elements/Cf.yaml` has no sourced `production` tonnage, `reserves`, or `prices` section to verify. The sourced claim set is limited to Cf-252 producer shares, feedstock origin, substitute availability, end-use share, criticality flags, and one geopolitical event.

The ORNL sources support the Cf-252 production structure cleanly: ORNL says it is one of only two world production sites in the 2013 contract announcement and the only Western Hemisphere producer in the 2021 isotope sheet. The Russia `30%` share and the `100%` end-use share are correctly treated as inferred because the cited sources describe market structure and applications but do not publish those exact percentages.

Both criticality flags are negative-list inferences. The cited US Federal Register and EU CRMA annexes provide enumerated lists that do not include californium; neither source states the exclusion explicitly, so the `false` flags are `inferred` rather than `verified`.

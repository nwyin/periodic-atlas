# Verification: Hg

- Element: mercury (Hg)
- Snapshot year: 2025
- Verifier: worker-b993d3b96efb (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 5 |
| discrepancy | 2 |
| inferred | 0 |
| source_unreachable | 8 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 2500 tonnes_per_year | usgs_mcs_2025_mercury | discrepancy | USGS Mineral Commodity Summaries 2025, Mercury chapter, table on p. 108: `World total (rounded) 4 1,130 1,200` with 2024 country values `China 1,000`, `Kyrgyzstan 6`, `Morocco 2`, `Norway 20`, `Peru (exports) 30`, `Tajikistan 100`. The cited source supports about 1,200 t for 2024, not 2,500 t. |
| production[0].mining_by_country[CN].share_pct | 80 pct | usgs_mcs_2025_mercury | discrepancy | From the same USGS p. 108 table, China is `1,000` out of `1,200` world total, which is 83.3%, not 80%. |
| production[0].mining_by_country[KG].share_pct | 8 pct | unep_global_mercury_assessment_2018 | source_unreachable | The cited UNEP handle page is reachable, but the underlying `GMA2018.pdf` content was not retrievable in the web tool during this run, so I could not extract document text to test the 8% figure directly. |
| production[0].mining_by_country[TJ].share_pct | 4 pct | unep_global_mercury_assessment_2018 | source_unreachable | Same issue as above: the cited UNEP source metadata is reachable, but the actual PDF content was not retrievable in this environment, so the 4% claim could not be checked against the document text. |
| production[0].mining_by_country[MX].share_pct | 4 pct | unep_global_mercury_assessment_2018 | source_unreachable | Same issue as above: the cited UNEP source metadata is reachable, but the actual PDF content was not retrievable in this environment, so the 4% claim could not be checked against the document text. |
| production[0].mining_by_country[ZZ].share_pct | 4 pct | unep_global_mercury_assessment_2018 | source_unreachable | Same issue as above: the cited UNEP source metadata is reachable, but the actual PDF content was not retrievable in this environment, so the 4% residual share could not be checked against the document text. |
| end_uses.uses[artisanal_and_small_scale_gold_mining].share_pct | 38 pct | unep_global_mercury_assessment_2018 | source_unreachable | The cited UNEP document download was unavailable via the web tool, so I could not inspect the figure or table that would be needed to validate the 38% demand share directly. |
| end_uses.uses[vinyl_chloride_monomer_production].share_pct | 25 pct | unep_global_mercury_assessment_2018 | source_unreachable | The cited UNEP document download was unavailable via the web tool, so I could not inspect the figure or table that would be needed to validate the 25% demand share directly. |
| end_uses.uses[chlor_alkali].share_pct | 16 pct | unep_global_mercury_assessment_2018 | source_unreachable | The cited UNEP document download was unavailable via the web tool, so I could not inspect the figure or table that would be needed to validate the 16% demand share directly. |
| end_uses.uses[products_and_other_industrial_uses].share_pct | 21 pct | unep_global_mercury_assessment_2018 | source_unreachable | The cited UNEP document download was unavailable via the web tool, so I could not inspect the figure or table that would be needed to validate the 21% demand share directly. |
| criticality.us_critical_list_as_of_2025 | false | us_federal_register_critical_minerals_2025 | verified | The final 2025 U.S. list says it `includes the following 60 minerals` and then enumerates them through `zinc, and zirconium`; mercury is not listed (Federal Register `Final 2025 List of Critical Minerals`). |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | verified | CRMA Annex II states `The following raw materials shall be considered critical:` and lists materials from `antimony` through `vanadium`; `mercury` is not present in the annex list. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | CRMA Annex I states `The following raw materials shall be considered strategic:` and lists materials from `bauxite/alumina/aluminium` through `tungsten`; `mercury` is not present in the annex list. |
| geopolitical_events[0].date | 2017-08-16 | minamata_convention_text | verified | The Minamata Convention booklet states that the convention `entered into force on 16 August 2017`. |
| geopolitical_events[1].date | 2023-11 | minamata_cop5_decisions | verified | The official report of the fifth meeting states that COP-5 `was held ... from 30 October to 3 November 2023` and that the Conference of the Parties `adopted decision MC-5/4 on amendments to annexes A and B`. That supports YAML's month-level `2023-11` event date. |

## Notes

`elements/Hg.yaml` is not present in `HEAD` or `main` in this worktree. This report was therefore prepared against the last committed mercury snapshot, commit `1faecff23d7d6ce262c8fca3dea570387c8514e4` (`Add mercury element profile`), retrieved with `git show`.

The only sourced numeric claims in that historical YAML are one world mine-production value, five country-share percentages, and four end-use percentages. Those ten numeric claims all appear in the Claims table above.

The USGS source was reachable and machine-readable. It contradicts the YAML's `production[0].mine.value` and also yields a higher China share (83.3%) than the YAML's rounded 80%.

The cited UNEP `Global Mercury Assessment 2018` landing page is reachable, but the actual PDF content was not fetchable in the web tool from the cited handle/download path during this run. Because I could not inspect the source document itself, the UNEP-backed country-share and end-use share claims are marked `source_unreachable` rather than `verified` or `discrepancy`.

`Hg.yaml` has no `reserves` or `prices` section in the historical snapshot I verified, despite the broader issue template mentioning those categories.

`feedstock_origins` and `substitutes` each carry `source_id` fields, but those entries are qualitative only and contain no numeric claims to include under the issue invariant requiring every distinct numeric claim to appear in the table.

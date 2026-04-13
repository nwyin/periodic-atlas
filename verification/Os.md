# Verification: Os

- Element: osmium (Os)
- Snapshot year: 2025
- Verifier: worker-e5cac659c0e7 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 15 |
| discrepancy | 6 |
| inferred | 21 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 100 kg_per_year | usgs_mcs_2025_pgm | discrepancy | USGS PGM chapter reports palladium and platinum mine output, but no standalone osmium mine tonnage. |
| production[0].mine.notes (osmium basket share) | roughly 0.026% | usgs_mcs_2025_pgm | discrepancy | Not stated directly, and the exact osmium basket share cannot be reproduced from the cited USGS table alone. |
| production[0].mine.notes (2024 palladium mine output) | 190,000 kg | usgs_mcs_2025_pgm | verified | `"World total (rounded) 208,000 190,000"` for palladium mine production, USGS MCS 2025 p.140. |
| production[0].mine.notes (2024 platinum mine output) | 170,000 kg | usgs_mcs_2025_pgm | verified | `"World total (rounded) 179,000 170,000"` for platinum mine production, USGS MCS 2025 p.140. |
| production[0].mining_by_country.shares[ZA].share_pct | 70.6 | usgs_mcs_2025_pgm | inferred | Not stated directly; `120,000 / 170,000 = 70.6%` from USGS 2024 platinum mine production values for South Africa and world total, p.140. |
| production[0].mining_by_country.shares[ZA].quantity.value | 71 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the inferred 70.6% platinum-share proxy to its 100 kg world osmium estimate. |
| production[0].mining_by_country.shares[ZA].notes (Pt numerator and denominator) | 120,000 kg Pt out of 170,000 kg world Pt | usgs_mcs_2025_pgm | verified | `"South Africa 74,900 72,000 125,000 120,000 63,000,000"` and `"World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000"`, USGS p.140. |
| production[0].mining_by_country.shares[ZW].share_pct | 11.2 | usgs_mcs_2025_pgm | inferred | Not stated directly; `19,000 / 170,000 = 11.2%` from USGS 2024 platinum mine production values, p.140. |
| production[0].mining_by_country.shares[ZW].quantity.value | 11 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the inferred 11.2% platinum-share proxy to its 100 kg world osmium estimate. |
| production[0].mining_by_country.shares[ZW].notes (Pt numerator and denominator) | 19,000 kg Pt out of 170,000 kg world Pt | usgs_mcs_2025_pgm | verified | `"Zimbabwe 15,900 15,000 19,200 19,000 1,200,000"` and `"World total (rounded) ... 170,000"`, USGS p.140. |
| production[0].mining_by_country.shares[RU].share_pct | 10.6 | usgs_mcs_2025_pgm | inferred | Not stated directly; `18,000 / 170,000 = 10.6%` from USGS 2024 platinum mine production values, p.140. |
| production[0].mining_by_country.shares[RU].quantity.value | 11 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the inferred 10.6% platinum-share proxy to its 100 kg world osmium estimate. |
| production[0].mining_by_country.shares[RU].notes (Pt numerator and denominator) | 18,000 kg Pt out of 170,000 kg world Pt | usgs_mcs_2025_pgm | verified | `"Russiae 87,000 75,000 21,000 18,000 10 16,000,000"` and `"World total (rounded) ... 170,000"`, USGS p.140. |
| production[0].mining_by_country.shares[CA].share_pct | 3.1 | usgs_mcs_2025_pgm | inferred | Not stated directly; `5,200 / 170,000 = 3.1%` from USGS 2024 platinum mine production values, p.140. |
| production[0].mining_by_country.shares[CA].quantity.value | 3 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the inferred 3.1% platinum-share proxy to its 100 kg world osmium estimate. |
| production[0].mining_by_country.shares[CA].notes (Pt numerator and denominator) | 5,200 kg Pt out of 170,000 kg world Pt | usgs_mcs_2025_pgm | verified | `"Canada 16,100 15,000 5,170 5,200 310,000"` and `"World total (rounded) ... 170,000"`, USGS p.140. |
| production[0].mining_by_country.shares[US].share_pct | 1.2 | usgs_mcs_2025_pgm | inferred | Not stated directly; `2,000 / 170,000 = 1.2%` from USGS 2024 platinum mine production values, p.140. |
| production[0].mining_by_country.shares[US].quantity.value | 1 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the inferred 1.2% platinum-share proxy to its 100 kg world osmium estimate. |
| production[0].mining_by_country.shares[US].notes (Pt numerator and denominator) | 2,000 kg Pt out of 170,000 kg world Pt | usgs_mcs_2025_pgm | verified | `"United States 10,300 8,000 3,040 2,000 820,000"` and `"World total (rounded) ... 170,000"`, USGS p.140. |
| production[0].mining_by_country.shares[ZZ].share_pct | 3.3 | usgs_mcs_2025_pgm | inferred | Not stated directly; the listed country platinum shares sum to 96.7%, leaving a 3.3% residual in YAML. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 3 kg_per_year | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies the residual 3.3% share to its 100 kg world osmium estimate. |
| reserves.economic_reserves.value | 21,000 kg | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies an assumed ~0.026% osmium basket share to USGS world PGM reserves `>81,000,000 kg`. |
| reserves.economic_reserves.notes (world PGM reserves) | more than 81,000,000 kg | usgs_mcs_2025_pgm | verified | `"World total (rounded) ... >81,000,000"` in the PGM reserves column, USGS p.140. |
| reserves.economic_reserves.notes (osmium basket share) | approximately 0.026% | usgs_mcs_2025_pgm | discrepancy | The cited USGS source does not provide an osmium reserve share, and the exact 0.026% assumption is not stated there. |
| reserves.economic_reserves.notes (recoverable osmium volume) | about one cubic meter | usgs_mcs_2025_pgm | discrepancy | The note cites a volume claim from RSC, but the attached source id points to USGS, which does not mention one cubic meter of recoverable osmium. |
| reserves.reserves_by_country.shares[ZA].share_pct | 77.5 | usgs_mcs_2025_pgm | inferred | Not stated directly; `63,000,000 / 81,330,000 = 77.5%` using the sum of listed country PGM reserves in the USGS table, p.140. |
| reserves.reserves_by_country.shares[ZA].notes (PGM reserves) | 63,000,000 kg | usgs_mcs_2025_pgm | verified | `"South Africa ... 63,000,000"` in the PGM reserves column, USGS p.140. |
| reserves.reserves_by_country.shares[ZA].notes (implied osmium) | roughly 16,000 kg | usgs_mcs_2025_pgm | inferred | Not stated directly; `21,000 × 77.5% ≈ 16,300`, which YAML rounds to roughly 16,000 kg. |
| reserves.reserves_by_country.shares[RU].share_pct | 19.7 | usgs_mcs_2025_pgm | inferred | Not stated directly; `16,000,000 / 81,330,000 = 19.7%` using the sum of listed country PGM reserves in the USGS table, p.140. |
| reserves.reserves_by_country.shares[RU].notes (PGM reserves) | 16,000,000 kg | usgs_mcs_2025_pgm | verified | `"Russiae ... 10 16,000,000"` in the PGM reserves column, USGS p.140 footnote 10. |
| reserves.reserves_by_country.shares[RU].notes (implied osmium) | roughly 4,100 kg | usgs_mcs_2025_pgm | inferred | Not stated directly; `21,000 × 19.7% ≈ 4,100`. |
| reserves.reserves_by_country.shares[ZW].share_pct | 1.5 | usgs_mcs_2025_pgm | inferred | Not stated directly; `1,200,000 / 81,330,000 = 1.5%` using the sum of listed country PGM reserves in the USGS table, p.140. |
| reserves.reserves_by_country.shares[ZW].notes (PGM reserves) | 1,200,000 kg | usgs_mcs_2025_pgm | verified | `"Zimbabwe ... 1,200,000"` in the PGM reserves column, USGS p.140. |
| reserves.reserves_by_country.shares[US].share_pct | 1.0 | usgs_mcs_2025_pgm | inferred | Not stated directly; `820,000 / 81,330,000 = 1.0%` using the sum of listed country PGM reserves in the USGS table, p.140. |
| reserves.reserves_by_country.shares[US].notes (PGM reserves) | 820,000 kg | usgs_mcs_2025_pgm | verified | `"United States ... 820,000"` in the PGM reserves column, USGS p.140. |
| reserves.reserves_by_country.shares[CA].share_pct | 0.4 | usgs_mcs_2025_pgm | inferred | Not stated directly; `310,000 / 81,330,000 = 0.4%` using the sum of listed country PGM reserves in the USGS table, p.140. |
| reserves.reserves_by_country.shares[CA].notes (PGM reserves) | 310,000 kg | usgs_mcs_2025_pgm | verified | `"Canada ... 310,000"` in the PGM reserves column, USGS p.140. |
| end_uses.uses[0].share_pct | 100 | rsc_osmium | inferred | RSC says `"Osmium has only a few uses"` and lists hard alloys plus catalyst use; YAML collapses the cited uses into one 100% specialty bucket. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex Annex II lists `"platinum group metals"` among critical raw materials. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex Annex I lists `"platinum group metals"` among strategic raw materials. |
| geopolitical_events[0].date | 2024-01 | usgs_mcs_2025_pgm | discrepancy | USGS p.140 supports a 2024 South African PGM output decline, but does not give a January 2024 event date. |
| geopolitical_events[1].date | 2024-01 | usgs_mcs_2025_pgm | discrepancy | USGS p.140 supports a 2024 Russian PGM output decline, but does not give a January 2024 event date. |

## Notes

Most directly quoted numbers in `elements/Os.yaml` come from the USGS platinum-group-metals chapter: 2024 platinum mine output by country and combined PGM reserves by country. The platinum-share proxy percentages reconcile numerically against that table and are best treated as `inferred`, not directly reported osmium shares.

The file's standalone osmium production and reserve tonnages depend on an assumed osmium basket share of about `0.026%`. That assumption is not stated in the cited USGS source, so the resulting osmium totals are not directly verifiable from the attached source IDs. The same issue affects the `one cubic meter` reserve note, which points to USGS even though the prose attributes it to RSC.

The RSC page supports the qualitative end-use and nickel-refining claims, but not a numerical end-use split. The EU criticality flags are supported by the Critical Raw Materials Act annexes because osmium is included within the listed `platinum group metals` category.

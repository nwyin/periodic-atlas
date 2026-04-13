# Verification: Re

- Element: rhenium (Re)
- Snapshot year: 2025
- Verifier: worker-a15fd29f29b2 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 30 |
| discrepancy | 0 |
| inferred | 15 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 62000 kg_per_year | usgs_mcs_2025_rhenium | verified | "Estimated world rhenium production in 2024 was 62,000 kilograms" and table "World total (rounded) 62,600 62,000" — USGS MCS 2025 p.147 |
| production[0].mining_by_country[US].quantity.value | 9500 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "United States 9,410 9,500 400,000" — 2024 mine production |
| production[0].mining_by_country[US].share_pct | 15.32% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 9,500 / 62,000 = 15.3226%, matching YAML |
| production[0].mining_by_country[AM].quantity.value | 200 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Armenia 210 200 95,000" — 2024 mine production |
| production[0].mining_by_country[AM].share_pct | 0.32% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 200 / 62,000 = 0.3226%, matching YAML |
| production[0].mining_by_country[CL].quantity.value | 29000 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Chile 30,000 29,000 1,300,000" — 2024 mine production |
| production[0].mining_by_country[CL].share_pct | 46.77% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 29,000 / 62,000 = 46.7742%, matching YAML |
| production[0].mining_by_country[CN].quantity.value | 5300 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "China 5,300 5,300 19,000" — 2024 mine production |
| production[0].mining_by_country[CN].share_pct | 8.55% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 5,300 / 62,000 = 8.5484%, matching YAML |
| production[0].mining_by_country[KZ].quantity.value | 500 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Kazakhstan 500 500 190,000" — 2024 mine production |
| production[0].mining_by_country[KZ].share_pct | 0.81% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 500 / 62,000 = 0.8065%, matching YAML |
| production[0].mining_by_country[KR].quantity.value | 3000 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Korea, Republic of 2,800 3,000 NA" — 2024 mine production |
| production[0].mining_by_country[KR].share_pct | 4.84% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 3,000 / 62,000 = 4.8387%, matching YAML |
| production[0].mining_by_country[PL].quantity.value | 9400 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Poland 9,380 9,400 NA" — 2024 mine production |
| production[0].mining_by_country[PL].share_pct | 15.16% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 9,400 / 62,000 = 15.1613%, matching YAML |
| production[0].mining_by_country[UZ].quantity.value | 5000 kg_per_year | usgs_mcs_2025_rhenium | verified | Table p.147: "Uzbekistan 5,000 5,000 NA" — 2024 mine production |
| production[0].mining_by_country[UZ].share_pct | 8.06% | usgs_mcs_2025_rhenium | inferred | Not stated directly; 5,000 / 62,000 = 8.0645%, matching YAML |
| production[1].refined.value | 25000 kg_per_year | usgs_mcs_2025_rhenium | verified | "approximately 25,000 kilograms of secondary rhenium was produced worldwide in 2024" — USGS MCS 2025 p.147 |
| reserves.reserves_by_country[US].quantity.value | 400000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "United States ... 400,000" — reserves column |
| reserves.reserves_by_country[US].share_pct | 17.29% | usgs_mcs_2025_rhenium | inferred | Reserves world total is "Large," so YAML uses quantified subset denominator 2,314,000 kg; 400,000 / 2,314,000 = 17.2861% |
| reserves.reserves_by_country[AM].quantity.value | 95000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "Armenia ... 95,000" — reserves column |
| reserves.reserves_by_country[AM].share_pct | 4.11% | usgs_mcs_2025_rhenium | inferred | Quantified subset denominator 2,314,000 kg; 95,000 / 2,314,000 = 4.1054%, matching YAML |
| reserves.reserves_by_country[CL].quantity.value | 1300000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "Chile ... 1,300,000" — reserves column |
| reserves.reserves_by_country[CL].share_pct | 56.18% | usgs_mcs_2025_rhenium | inferred | Quantified subset denominator 2,314,000 kg; 1,300,000 / 2,314,000 = 56.1798%, matching YAML |
| reserves.reserves_by_country[CN].quantity.value | 19000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "China ... 19,000" — reserves column |
| reserves.reserves_by_country[CN].share_pct | 0.82% | usgs_mcs_2025_rhenium | inferred | Quantified subset denominator 2,314,000 kg; 19,000 / 2,314,000 = 0.8211%, matching YAML |
| reserves.reserves_by_country[KZ].quantity.value | 190000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "Kazakhstan ... 190,000" — reserves column |
| reserves.reserves_by_country[KZ].share_pct | 8.21% | usgs_mcs_2025_rhenium | inferred | Quantified subset denominator 2,314,000 kg; 190,000 / 2,314,000 = 8.2110%, matching YAML |
| reserves.reserves_by_country[RU].quantity.value | 310000 kg | usgs_mcs_2025_rhenium | verified | Table p.147: "Russia NA NA 310,000" — reserves column |
| reserves.reserves_by_country[RU].share_pct | 13.40% | usgs_mcs_2025_rhenium | inferred | Quantified subset denominator 2,314,000 kg; 310,000 / 2,314,000 = 13.3967%, matching YAML |
| reserves.notes (identified U.S. resources) | 7000000 kg | usgs_mcs_2025_rhenium | verified | World Resources p.147: "Identified U.S. resources are estimated to be about 7 million kilograms." |
| end_uses.uses[superalloys].share_pct | 80% | usgs_mcs_2025_rhenium | verified | "representing an estimated 80% and 15%, respectively, of end uses" — superalloys first, USGS MCS 2025 p.146 |
| end_uses.uses[petroleum_reforming_catalysts].share_pct | 15% | usgs_mcs_2025_rhenium | verified | "representing an estimated 80% and 15%, respectively, of end uses" — petroleum-reforming catalysts second, p.146 |
| end_uses.uses[other_specialty_uses].share_pct | 5% | usgs_mcs_2025_rhenium | inferred | Not stated directly; residual share is 100% - 80% - 15% = 5%, matching YAML |
| prices[2020,metal].value | 1030 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Metal pellets, 99.99% pure 1,030 977 1,120 1,070 1,370" — 2020 value |
| prices[2021,metal].value | 977 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Metal pellets, 99.99% pure 1,030 977 1,120 1,070 1,370" — 2021 value |
| prices[2022,metal].value | 1120 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Metal pellets, 99.99% pure 1,030 977 1,120 1,070 1,370" — 2022 value |
| prices[2023,metal].value | 1070 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Metal pellets, 99.99% pure 1,030 977 1,120 1,070 1,370" — 2023 value |
| prices[2024,metal].value | 1370 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Metal pellets, 99.99% pure 1,030 977 1,120 1,070 1,370" — 2024e value |
| prices[2020,ammonium_perrhenate].value | 1090 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Ammonium perrhenate 1,090 866 911 920 1,270" — 2020 value |
| prices[2021,ammonium_perrhenate].value | 866 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Ammonium perrhenate 1,090 866 911 920 1,270" — 2021 value |
| prices[2022,ammonium_perrhenate].value | 911 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Ammonium perrhenate 1,090 866 911 920 1,270" — 2022 value |
| prices[2023,ammonium_perrhenate].value | 920 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Ammonium perrhenate 1,090 866 911 920 1,270" — 2023 value |
| prices[2024,ammonium_perrhenate].value | 1270 usd_per_kg | usgs_mcs_2025_rhenium | verified | Salient Statistics p.146: "Ammonium perrhenate 1,090 866 911 920 1,270" — 2024e value |
| prices[*].notes (APR rhenium content) | 69.42% | usgs_mcs_2025_rhenium | verified | Footnote 3 p.147: "The rhenium content of ammonium perrhenate is 69.42%." |

## Notes

**Source accessed:** USGS Mineral Commodity Summaries 2025, Rhenium chapter (`https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rhenium.pdf`), pages 146 to 147. The PDF was reachable and machine-readable.

**Production shares:** All `production[0].mining_by_country[*].share_pct` values are calculated from the published 2024 world total of 62,000 kg and the per-country 2024 mine-production figures in the USGS table. The source does not print these percentages explicitly, so they are marked `inferred`.

**Reserve shares:** The USGS reserves table gives numeric reserve figures for six countries but reports the world total reserve position only as `Large`. YAML therefore computes country shares against the quantified subset of 2,314,000 kg (400,000 + 95,000 + 1,300,000 + 19,000 + 190,000 + 310,000). Those percentages are valid calculations but not explicit source statements, so they are marked `inferred`.

**Resources scope:** The only source-backed numeric resource figure in `Re.yaml` is the note that identified U.S. resources are about 7 million kg. There is no published numeric world-total reserve value to verify against because the source uses the qualitative label `Large`.

**Residual end use:** The 5% `other_specialty_uses` share is arithmetic remainder from the source's explicit 80% superalloys plus 15% petroleum-reforming catalysts. It matches YAML but is not written as a separate percentage in the source text.

**No sourced numeric claims in some sections:** `criticality` has no `source_id` fields, `geopolitical_events` is empty, and `feedstock_origins` and `substitutes` contain sourced qualitative statements but no numeric values to verify.

# Verification: Ba

- Element: barium (Ba)
- Snapshot year: 2025
- Verifier: worker-a6d09f97acdc (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 58 |
| discrepancy | 1 |
| inferred | 23 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 8,200,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "World total (rounded) … 8,200" — USGS MCS 2025 p.41 World Mine Production table, 2024e column (footnote 10: Excludes U.S. production); data in thousand metric tons |
| production[0].mine.notes: 2023 world ex-US total | 8,080,000 tonnes | usgs_mcs_2025_barite | verified | "World total (rounded) … 8,080" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mine.notes: US 2.3 million tons sold 2024e | 2,300,000 tonnes | usgs_mcs_2025_barite | verified | "An estimated 2.3 million tons of barite (from domestic production and imports) was sold by crushers and grinders operating in nine States" — USGS MCS 2025 p.40 Domestic Production and Use; Salient Statistics Ground and crushed 2024e = 2,300 (thousand metric tons) |
| production[0].mining_by_country[IN].quantity.value | 2,600,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "India … 2,600" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[IN].notes: 2023 = 2,600,000 | 2,600,000 tonnes | usgs_mcs_2025_barite | verified | "India … 2,600" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[IN].notes: India 40% US imports | 40% | usgs_mcs_2025_barite | verified | "Import Sources (2020–23): India, 40%" — USGS MCS 2025 p.40 |
| production[0].mining_by_country[IN].share_pct | 31.71 | usgs_mcs_2025_barite | inferred | Not stated; 2,600,000 / 8,200,000 = 31.707% ≈ 31.71% (computed against published ex-US world total) |
| production[0].mining_by_country[CN].quantity.value | 2,100,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "China … 2,100" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].notes: 2023 = 2,000,000 | 2,000,000 tonnes | usgs_mcs_2025_barite | verified | "China … 2,000" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[CN].notes: China 25% US imports | 25% | usgs_mcs_2025_barite | verified | "China, 25%" with footnote 6 "Includes Hong Kong" — USGS MCS 2025 p.40 Import Sources (2020–23) |
| production[0].mining_by_country[CN].share_pct | 25.61 | usgs_mcs_2025_barite | inferred | Not stated; 2,100,000 / 8,200,000 = 25.610% ≈ 25.61% |
| production[0].mining_by_country[MA].quantity.value | 1,000,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Morocco … 1,000" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[MA].notes: 2023 = 1,000,000 | 1,000,000 tonnes | usgs_mcs_2025_barite | verified | "Morocco … 1,000" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[MA].notes: Morocco 17% US imports | 17% | usgs_mcs_2025_barite | verified | "Morocco, 17%" — USGS MCS 2025 p.40 Import Sources (2020–23) |
| production[0].mining_by_country[MA].share_pct | 12.20 | usgs_mcs_2025_barite | inferred | Not stated; 1,000,000 / 8,200,000 = 12.195% ≈ 12.20% |
| production[0].mining_by_country[KZ].quantity.value | 650,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Kazakhstan … 650" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[KZ].notes: 2023 = 650,000 (unchanged) | 650,000 tonnes | usgs_mcs_2025_barite | verified | "Kazakhstan … 650" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[KZ].share_pct | 7.93 | usgs_mcs_2025_barite | inferred | Not stated; 650,000 / 8,200,000 = 7.927% ≈ 7.93% |
| production[0].mining_by_country[MX].quantity.value | 330,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Mexico … 330" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[MX].notes: 2023 = 320,000 | 320,000 tonnes | usgs_mcs_2025_barite | verified | "Mexico … 320" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[MX].notes: Mexico 14% US imports | 14% | usgs_mcs_2025_barite | verified | "Mexico, 14%" — USGS MCS 2025 p.40 Import Sources (2020–23) |
| production[0].mining_by_country[MX].share_pct | 4.02 | usgs_mcs_2025_barite | inferred | Not stated; 330,000 / 8,200,000 = 4.024% ≈ 4.02% |
| production[0].mining_by_country[IR].quantity.value | 310,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Iran … 310" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[IR].notes: 2023 = 300,000 | 300,000 tonnes | usgs_mcs_2025_barite | verified | "Iran … 300" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[IR].share_pct | 3.78 | usgs_mcs_2025_barite | inferred | Not stated; 310,000 / 8,200,000 = 3.780% ≈ 3.78% |
| production[0].mining_by_country[LA].quantity.value | 300,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Laos … 300" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[LA].notes: 2023 = 300,000 (unchanged) | 300,000 tonnes | usgs_mcs_2025_barite | verified | "Laos … 300" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[LA].share_pct | 3.66 | usgs_mcs_2025_barite | inferred | Not stated; 300,000 / 8,200,000 = 3.659% ≈ 3.66% |
| production[0].mining_by_country[RU].quantity.value | 250,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Russia … 250" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[RU].notes: 2023 = 250,000 (unchanged) | 250,000 tonnes | usgs_mcs_2025_barite | verified | "Russia … 250" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[RU].share_pct | 3.05 | usgs_mcs_2025_barite | inferred | Not stated; 250,000 / 8,200,000 = 3.049% ≈ 3.05% |
| production[0].mining_by_country[TR].quantity.value | 220,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Turkey … 220" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[TR].notes: 2023 = 216,000 (reported) | 216,000 tonnes | usgs_mcs_2025_barite | verified | "Turkey … 216" with footnote 9 "Reported" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[TR].share_pct | 2.68 | usgs_mcs_2025_barite | inferred | Not stated; 220,000 / 8,200,000 = 2.683% ≈ 2.68% |
| production[0].mining_by_country[PK].quantity.value | 130,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Pakistan … 130" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[PK].notes: 2023 = 130,000 (unchanged) | 130,000 tonnes | usgs_mcs_2025_barite | verified | "Pakistan … 130" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| production[0].mining_by_country[PK].share_pct | 1.59 | usgs_mcs_2025_barite | inferred | Not stated; 130,000 / 8,200,000 = 1.585% ≈ 1.59% |
| production[0].mining_by_country[ZZ].quantity.value | 320,000 tonnes_per_year | usgs_mcs_2025_barite | verified | "Other countries … 320" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 3.90 | usgs_mcs_2025_barite | inferred | Not stated; 320,000 / 8,200,000 = 3.902% ≈ 3.90% |
| production[0].notes: net import reliance >75% all years 2020–2024e | >75% | usgs_mcs_2025_barite | verified | "Net import reliance as a percentage of apparent consumption >75 >75 >75 >75 >75" — USGS MCS 2025 p.40 Salient Statistics, 2020–2024e columns |
| reserves.resources.value | 2,000,000,000 tonnes (~2 billion) | usgs_mcs_2025_barite | verified | "The world's barite resources in all categories were about 2 billion tons" — USGS MCS 2025 p.41 World Resources |
| reserves.resources.notes: ~740 million tons identified | 740,000,000 tonnes | usgs_mcs_2025_barite | verified | "only about 740 million tons were identified resources" — USGS MCS 2025 p.41 World Resources |
| reserves.resources.notes: US 150 million identified | 150,000,000 tonnes | usgs_mcs_2025_barite | verified | "identified resources of barite were estimated to be 150 million tons" — USGS MCS 2025 p.41 World Resources |
| reserves.resources.notes: US 150 million undiscovered | 150,000,000 tonnes | usgs_mcs_2025_barite | verified | "undiscovered resources contributed an additional 150 million tons" — USGS MCS 2025 p.41 World Resources |
| reserves.reserves_by_country[CN].quantity.value | 110,000,000 tonnes | usgs_mcs_2025_barite | verified | "China … 110,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column (thousand metric tons) |
| reserves.reserves_by_country[CN].share_pct | 28.06 | usgs_mcs_2025_barite | inferred | Not stated; 110,000,000 / 392,000,000 = 28.061% ≈ 28.06% (denominator = sum of six countries with quantified reserves) |
| reserves.reserves_by_country[IR].quantity.value | 100,000,000 tonnes | usgs_mcs_2025_barite | verified | "Iran … 100,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[IR].share_pct | 25.51 | usgs_mcs_2025_barite | inferred | Not stated; 100,000,000 / 392,000,000 = 25.510% ≈ 25.51% |
| reserves.reserves_by_country[KZ].quantity.value | 85,000,000 tonnes | usgs_mcs_2025_barite | verified | "Kazakhstan … 85,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[KZ].share_pct | 21.68 | usgs_mcs_2025_barite | inferred | Not stated; 85,000,000 / 392,000,000 = 21.684% ≈ 21.68% |
| reserves.reserves_by_country[IN].quantity.value | 51,000,000 tonnes | usgs_mcs_2025_barite | verified | "India … 51,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[IN].share_pct | 13.01 | usgs_mcs_2025_barite | inferred | Not stated; 51,000,000 / 392,000,000 = 13.010% ≈ 13.01% |
| reserves.reserves_by_country[TR].quantity.value | 34,000,000 tonnes | usgs_mcs_2025_barite | verified | "Turkey … 34,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[TR].share_pct | 8.67 | usgs_mcs_2025_barite | inferred | Not stated; 34,000,000 / 392,000,000 = 8.673% ≈ 8.67% |
| reserves.reserves_by_country[RU].quantity.value | 12,000,000 tonnes | usgs_mcs_2025_barite | verified | "Russia … 12,000" — USGS MCS 2025 p.41 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[RU].share_pct | 3.06 | usgs_mcs_2025_barite | inferred | Not stated; 12,000,000 / 392,000,000 = 3.061% ≈ 3.06% |
| reserves.notes: 392,000,000 t partial sum denominator | 392,000,000 tonnes | usgs_mcs_2025_barite | inferred | Not stated; arithmetic sum CN(110,000) + IR(100,000) + KZ(85,000) + IN(51,000) + TR(34,000) + RU(12,000) = 392,000 thousand metric tons. US, MA, MX, LA, PK reserves = NA per source. |
| feedstock_origins[barite_ore].notes: 14% depletion allowance | 14% | usgs_mcs_2025_barite | verified | "Depletion Allowance: 14% (domestic and foreign)." — USGS MCS 2025 p.40 |
| substitutes[oil_gas_drilling_fluids].notes: no large-scale alternatives | none | usgs_mcs_2025_barite | verified | "Owing to technical and economic factors, there are no large-scale alternatives to barite in oil- and gas-drilling fluids." — USGS MCS 2025 p.41 Substitutes |
| substitutes[specific_drilling_circumstances].notes: most common alternatives | CaCO3, hematite, ilmenite, MnO4 | usgs_mcs_2025_barite | verified | "Calcium carbonate, hematite, ilmenite, and manganese tetroxide are the most common alternatives used in specific circumstances." — USGS MCS 2025 p.41 Substitutes |
| substitutes[specific_drilling_circumstances].notes: celestite/iron carbonate/strontium carbonate | mentioned in literature | usgs_mcs_2025_barite | verified | "Some technical literature and patents also mention use of celestite, iron carbonate, and strontium carbonate, but these are not estimated to be widely used." — USGS MCS 2025 p.41 Substitutes |
| end_uses[oil_gas_drilling_fluid_weighting].share_pct | 91 | usgs_mcs_2025_barite | inferred | Source states ">90%"; not a specific percentage. "Typically, more than 90% of the barite sold in the United States is used as a weighting agent in fluids used in the drilling of oil and natural gas wells." — USGS MCS 2025 p.40 Domestic Production and Use. 91% is an analyst interpolation of ">90%". |
| end_uses[industrial_fillers_and_additives].share_pct | 9 | usgs_mcs_2025_barite | inferred | Not stated; residual from oil/gas share (100% − 91% = 9%). Source confirms remaining uses as "filler, extender, or weighting agent" without quantifying. |
| prices[2020].value | 183.0 USD/tonne | usgs_mcs_2025_barite | verified | "Price, average unit value, ground, ex-works, dollars per metric ton … 183" — USGS MCS 2025 p.40 Salient Statistics, 2020 column |
| prices[2021].value | 167.0 USD/tonne | usgs_mcs_2025_barite | verified | "Price, average unit value, ground, ex-works, dollars per metric ton … 167" — USGS MCS 2025 p.40 Salient Statistics, 2021 column |
| prices[2022].value | 145.0 USD/tonne | usgs_mcs_2025_barite | verified | "Price, average unit value, ground, ex-works, dollars per metric ton … 145" — USGS MCS 2025 p.40 Salient Statistics, 2022 column |
| prices[2023].value | 223.0 USD/tonne | usgs_mcs_2025_barite | verified | "Price, average unit value, ground, ex-works, dollars per metric ton … 223" — USGS MCS 2025 p.40 Salient Statistics, 2023 column |
| prices[2024].value | 220.0 USD/tonne | usgs_mcs_2025_barite | verified | "Price, average unit value, ground, ex-works, dollars per metric ton … 220" — USGS MCS 2025 p.40 Salient Statistics, 2024e column |
| geopolitical_events[US rig count 2024]: US rigs start 2024 | 622 | usgs_mcs_2025_barite | verified | "At the beginning of 2024, the number of drill rigs operating in the United States was 622" — USGS MCS 2025 p.41 Events |
| geopolitical_events[US rig count 2024]: US rigs Oct 2024 | 585 | usgs_mcs_2025_barite | verified | "by the end of October 2024, the number of rigs operating had declined to 585" — USGS MCS 2025 p.41 Events |
| geopolitical_events[US rig count 2024]: 39% below 2019 | 39% | usgs_mcs_2025_barite | verified | "Rig counts remained 39% lower than that in the same period in 2019" — USGS MCS 2025 p.41 Events |
| geopolitical_events[US rig count 2024]: 2.3 million tons sold 2024 | 2,300,000 tonnes | usgs_mcs_2025_barite | verified | "An estimated 2.3 million tons of barite (from domestic production and imports) was sold by crushers and grinders operating in nine States" — USGS MCS 2025 p.40 (also p.41 Events context) |
| geopolitical_events[world rig count 2024]: world rig count 2024 | 1,169 | usgs_mcs_2025_barite | verified | "the world annual average rig count excluding the United States was 1,169" — USGS MCS 2025 p.41 Events |
| geopolitical_events[world rig count 2024]: world rig count 2023 | 1,154 | usgs_mcs_2025_barite | verified | "compared with 1,154 in 2023" — USGS MCS 2025 p.41 Events |
| geopolitical_events[world rig count 2024]: world production 2023 | 8,080,000 tonnes | usgs_mcs_2025_barite | verified | "World total (rounded) … 8,080" — USGS MCS 2025 p.41 World Mine Production table, 2023 column |
| geopolitical_events[world rig count 2024]: world production 2024e | 8,200,000 tonnes | usgs_mcs_2025_barite | verified | "World total (rounded) … 8,200" — USGS MCS 2025 p.41 World Mine Production table, 2024e column |
| geopolitical_events[China/Iran/Turkey reserves revised]: text confirmed | reserves revised | usgs_mcs_2025_barite | verified | "Reserves for China, Iran, and Turkey were revised based on company and Government reports." — USGS MCS 2025 p.41 World Mine Production and Reserves |
| geopolitical_events[China/Iran/Turkey reserves revised].impact: "163,000 thousand metric tons" | 163,000 kt | usgs_mcs_2025_barite | discrepancy | YAML states CN+IR+TR reserves total "163,000 thousand metric tons" but actual sum from the same source is CN(110,000) + IR(100,000) + TR(34,000) = 244,000 thousand metric tons. The 163,000 kt figure is arithmetically incorrect. The total of all six reporting countries is 392,000 kt (the denominator used correctly in reserves_by_country notes). |
| geopolitical_events[API 4.1 SG spec 2010]: API issued 4.1 SG spec in 2010 | 2010 | usgs_mcs_2025_barite | verified | "the American Petroleum Institute issued an alternate specification for 4.1-specific-gravity weighting agents in 2010" — USGS MCS 2025 p.41 World Mine Production and Reserves |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_barite | inferred | Not stated in USGS barite chapter; barium/barite absent from US 2022 Critical Minerals List (Federal Register) — external policy knowledge |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_barite | inferred | Not stated in source; barium/barite absent from EU CRM Annex I/II (Regulation 2024/1252) — external policy knowledge |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_barite | inferred | Not stated in source; barium/barite absent from EU CRMA 2024 Annex I strategic list — external policy knowledge |

## Notes

All numeric claims derive from a single source: USGS MCS 2025 Barite chapter (pp. 40–41). The PDF was fetched from https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-barite.pdf and extracted via pdftotext -layout.

Key structural facts confirmed:
- All world production totals (2023: 8,080,000 t; 2024e: 8,200,000 t) explicitly EXCLUDE U.S. production per footnote 10: "Excludes U.S. production." U.S. mine production is "W" (withheld) in all five years.
- Data in the World Mine Production and Reserves table are in thousand metric tons. All YAML quantity.value fields correctly convert to tonnes (multiply by 1,000).
- Named-country 2024e entries sum to 8,210,000 t vs. stated world total 8,200,000 t; the 10,000 t gap is within rounding (stated as rounded). This is noted in the YAML production notes and is not a discrepancy.
- World total reserves = NA per source. Country reserves are only reported where data were developed after the 2010 API 4.1 SG standard adoption. Morocco, Mexico, Laos, Pakistan, and USA have reserves = NA.
- Reserve share percentages are computed against the partial sum of 392,000,000 t (six countries with quantified reserves), not a world total. This denominator is correctly noted in the YAML.
- Turkey's 2023 mine production value (216) carries source footnote 9 "Reported," distinguishing it from the "e" (estimated) designation in the table header.
- End-use share 91% (oil/gas) is inferred from ">90%" text; no explicit percentage is stated in the source.
- Criticality flags are inferred from external policy knowledge; the USGS barite chapter does not address criticality classifications.
- Import source percentages (India 40%, China 25% incl. HK, Morocco 17%, Mexico 14%, Other 4%) are directly confirmed from "Import Sources (2020–23)" table in the source.

**One discrepancy found:** The geopolitical event for China/Iran/Turkey reserves revision incorrectly states the combined reserves of these three countries as "163,000 thousand metric tons." The correct arithmetic sum from the source data is CN(110,000) + IR(100,000) + TR(34,000) = 244,000 thousand metric tons. The 163,000 figure does not correspond to any identifiable subset of the reserves table. This is a calculation error in the YAML notes text.

Price series behavior confirmed: prices declined from $183 (2020) → $167 (2021) → $145 (2022) before surging to $223 (2023) and easing to $220 (2024e). The narrative description of "50% above the 2022 low" is approximately correct: ($220 − $145)/$145 = 51.7%.

# Verification: Sr

- Element: strontium (Sr)
- Snapshot year: 2025
- Verifier: worker-aa8fe438f2de (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 45 |
| discrepancy | 0 |
| inferred | 10 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 510,000 tonnes_per_year | usgs_mcs_2025_strontium | verified | "World total (rounded) … 510,000" — USGS MCS 2025 p.171 World Mine Production table, 2024e column (gross weight celestite) |
| production[0].mine.notes (2023 world total 509,000 t) | 509,000 | usgs_mcs_2025_strontium | verified | "World total (rounded) … 509,000" — USGS MCS 2025 p.171 World Mine Production table, 2023 column |
| production[0].mining_by_country[IR].quantity.value | 200,000 tonnes_per_year | usgs_mcs_2025_strontium | verified | "Iran … 200,000" — USGS MCS 2025 p.171 World Mine Production table, 2024e column |
| production[0].mining_by_country[IR].quantity (2023 = 200,000, unchanged) | 200,000 | usgs_mcs_2025_strontium | verified | "Iran … 200,000" — USGS MCS 2025 p.171 World Mine Production table, 2023 column |
| production[0].mining_by_country[IR].share_pct | 39.22 | usgs_mcs_2025_strontium | inferred | Not stated; 200,000 / 510,000 = 39.22% (computed against USGS-reported world total) |
| production[0].mining_by_country[IR].notes (reserves 7,100,000 t) | 7,100,000 | usgs_mcs_2025_strontium | verified | "Iran … 7,100,000" — USGS MCS 2025 p.171 World Mine Production and Reserves table, Reserves column |
| production[0].mining_by_country[ES].quantity.value | 200,000 tonnes_per_year | usgs_mcs_2025_strontium | verified | "Spain … 200,000" — USGS MCS 2025 p.171 World Mine Production table, 2024e column |
| production[0].mining_by_country[ES].quantity (2023 = 200,000, unchanged) | 200,000 | usgs_mcs_2025_strontium | verified | "Spain … 200,000" — USGS MCS 2025 p.171 World Mine Production table, 2023 column |
| production[0].mining_by_country[ES].share_pct | 39.22 | usgs_mcs_2025_strontium | inferred | Not stated; 200,000 / 510,000 = 39.22% (computed against USGS-reported world total) |
| production[0].mining_by_country[CN].quantity.value | 80,000 tonnes_per_year | usgs_mcs_2025_strontium | verified | "China … 80,000" — USGS MCS 2025 p.171 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].quantity (2023 = 80,000, unchanged) | 80,000 | usgs_mcs_2025_strontium | verified | "China … 80,000" — USGS MCS 2025 p.171 World Mine Production table, 2023 column |
| production[0].mining_by_country[CN].share_pct | 15.69 | usgs_mcs_2025_strontium | inferred | Not stated; 80,000 / 510,000 = 15.69% (computed against USGS-reported world total) |
| production[0].mining_by_country[CN].notes (reserves 12,000,000 t) | 12,000,000 | usgs_mcs_2025_strontium | verified | "China … 12,000,000" — USGS MCS 2025 p.171 World Mine Production and Reserves table, Reserves column |
| production[0].mining_by_country[MX].quantity.value | 25,000 tonnes_per_year | usgs_mcs_2025_strontium | verified | "Mexico … 25,000" — USGS MCS 2025 p.171 World Mine Production table, 2024e column |
| production[0].mining_by_country[MX].notes (2023 = 28,000, reported) | 28,000 | usgs_mcs_2025_strontium | verified | "Mexico … 28,000" — USGS MCS 2025 p.171 World Mine Production table, 2023 column (footnote 8: Reported) |
| production[0].mining_by_country[MX].share_pct | 4.90 | usgs_mcs_2025_strontium | inferred | Not stated; 25,000 / 510,000 = 4.90% (computed against USGS-reported world total) |
| production[0].mining_by_country[AR].quantity.value | 700 tonnes_per_year | usgs_mcs_2025_strontium | verified | "Argentina … 700" — USGS MCS 2025 p.171 World Mine Production table, 2024e column |
| production[0].mining_by_country[AR].quantity (2023 = 700, unchanged) | 700 | usgs_mcs_2025_strontium | verified | "Argentina … 700" — USGS MCS 2025 p.171 World Mine Production table, 2023 column |
| production[0].mining_by_country[AR].share_pct | 0.14 | usgs_mcs_2025_strontium | inferred | Not stated; 700 / 510,000 = 0.137% ≈ 0.14% (computed against USGS-reported world total) |
| reserves.resources.value | 1,000,000,000 tonnes | usgs_mcs_2025_strontium | verified | "World resources of strontium may exceed 1 billion tons." — USGS MCS 2025 p.171 World Resources |
| reserves.reserves_by_country[CN].quantity.value | 12,000,000 tonnes | usgs_mcs_2025_strontium | verified | "China … 12,000,000" — USGS MCS 2025 p.171 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[CN].share_pct | 62.83 | usgs_mcs_2025_strontium | inferred | Not stated; 12,000,000 / 19,100,000 = 62.83% (partial sum of quantified country reserves only) |
| reserves.reserves_by_country[IR].quantity.value | 7,100,000 tonnes | usgs_mcs_2025_strontium | verified | "Iran … 7,100,000" — USGS MCS 2025 p.171 World Mine Production and Reserves table, Reserves column |
| reserves.reserves_by_country[IR].share_pct | 37.17 | usgs_mcs_2025_strontium | inferred | Not stated; 7,100,000 / 19,100,000 = 37.17% (partial sum of quantified country reserves only) |
| reserves.notes (world reserves = "Large") | Large | usgs_mcs_2025_strontium | verified | "World total … Large" — USGS MCS 2025 p.171 World Mine Production and Reserves table, Reserves column |
| reserves.notes (Argentina, Mexico, Spain, US reserves = NA) | NA | usgs_mcs_2025_strontium | verified | "Argentina … NA; Mexico … NA; Spain … NA; United States … NA" — USGS MCS 2025 p.171 Reserves column |
| feedstock_origins[celestite_ore].typical_concentration_pct | 43.88 | usgs_mcs_2025_strontium | verified | "The strontium content of celestite ore is 43.88%" — USGS MCS 2025 p.171 footnote 1 |
| form_notes (SrCO3 strontium content 59.35%) | 59.35 | usgs_mcs_2025_strontium | verified | "carbonate (59.35%)" — USGS MCS 2025 p.171 footnote 2 (strontium compound conversion factors) |
| form_notes (strontium nitrate strontium content 41.40%) | 41.40 | usgs_mcs_2025_strontium | verified | "nitrate (41.40%)" — USGS MCS 2025 p.171 footnote 2 |
| substitutes[ceramic_ferrite_magnets].availability | partial | usgs_mcs_2025_strontium | verified | "Barium can be substituted for strontium in ceramic ferrite magnets; however, the resulting barium composite will have a reduced maximum operating temperature" — USGS MCS 2025 p.171 Substitutes |
| substitutes[pyrotechnics_and_signals].availability | none | usgs_mcs_2025_strontium | verified | "Substituting for strontium in pyrotechnics is hindered by difficulty in obtaining the desired brilliance and visibility imparted by strontium and its compounds." — USGS MCS 2025 p.171 Substitutes |
| substitutes[drilling_fluids].availability | full | usgs_mcs_2025_strontium | verified | "In drilling mud, barite is the preferred material, but celestite may substitute for some barite, especially when barite prices are high." — USGS MCS 2025 p.171 Substitutes |
| end_uses[ceramic_ferrite_magnets].share_pct | 40 | usgs_mcs_2025_strontium | verified | "ceramic ferrite magnets, 40%" — USGS MCS 2025 p.170 Domestic Production and Use (end-use distribution) |
| end_uses[pyrotechnics_and_signals].share_pct | 40 | usgs_mcs_2025_strontium | verified | "pyrotechnics and signals, 40%" — USGS MCS 2025 p.170 Domestic Production and Use |
| end_uses[drilling_fluids].share_pct | 2 | usgs_mcs_2025_strontium | verified | "drilling fluids, 2%" — USGS MCS 2025 p.170 Domestic Production and Use |
| end_uses[other_industrial].share_pct | 18 | usgs_mcs_2025_strontium | verified | "other uses, including electrolytic production of zinc, glass, master alloys, and pigments and fillers, 18%" — USGS MCS 2025 p.170 |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_strontium | inferred | Strontium not mentioned as a critical mineral in USGS MCS 2025; net import reliance noted at 100% but no critical-list designation cited |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_strontium | inferred | Not mentioned in USGS MCS 2025 strontium chapter as appearing on EU CRM list |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_strontium | inferred | Not mentioned in USGS MCS 2025 strontium chapter as appearing on EU Strategic Raw Materials list |
| prices[2024].value | 390.0 USD/tonne | usgs_mcs_2025_strontium | verified | "390" — USGS MCS 2025 p.170 Salient Statistics, Price row, 2024e column (average unit value of celestite imports at port of exportation, dollars per ton) |
| prices[2023].value | 82.0 USD/tonne | usgs_mcs_2025_strontium | verified | "82" — USGS MCS 2025 p.170 Salient Statistics, Price row, 2023 column |
| prices[2022].value | 143.0 USD/tonne | usgs_mcs_2025_strontium | verified | "143" — USGS MCS 2025 p.170 Salient Statistics, Price row, 2022 column |
| prices[2021].value | 210.0 USD/tonne | usgs_mcs_2025_strontium | verified | "210" — USGS MCS 2025 p.170 Salient Statistics, Price row, 2021 column |
| prices[2020].value | 90.0 USD/tonne | usgs_mcs_2025_strontium | verified | "90" — USGS MCS 2025 p.170 Salient Statistics, Price row, 2020 column |
| geopolitical_events[celestite_import_drop].impact (95% decrease 2024) | 95% | usgs_mcs_2025_strontium | verified | "Imports of celestite in 2024 decreased by 95% compared with those in 2023" — USGS MCS 2025 p.170 Events, Trends, and Issues |
| geopolitical_events[celestite_import_drop].impact (rig count 15% decrease) | 15% | usgs_mcs_2025_strontium | verified | "weekly average active rig count decreased by 15% in the first 9 months in 2024 compared with that in the same period in 2023" — USGS MCS 2025 p.170 Events |
| geopolitical_events[celestite_import_drop].impact (rig count 39% below 2019) | 39% | usgs_mcs_2025_strontium | verified | "remained 39% lower than that in the same period in 2019 before the global coronavirus disease 2019 (COVID-19) pandemic" — USGS MCS 2025 p.170 Events |
| geopolitical_events[compound_imports_increase].impact (20% increase 2024) | 20% | usgs_mcs_2025_strontium | verified | "Imports of strontium compounds were estimated to have increased by 20% in 2024." — USGS MCS 2025 p.171 Events |
| geopolitical_events[compound_imports_increase].impact (~4,000 mt strontium content) | 4,000 | usgs_mcs_2025_strontium | verified | "Strontium compounds … 4,000" — USGS MCS 2025 p.170 Salient Statistics, Imports for consumption, 2024e column |
| geopolitical_events[compound_imports_increase].impact (Germany 49%, Mexico 43%) | Germany 49%, Mexico 43% | usgs_mcs_2025_strontium | verified | "Strontium compounds: Germany, 49%; Mexico, 43%" — USGS MCS 2025 p.170 Import Sources (2020–23) |
| geopolitical_events[compound_imports_increase].impact (Mexico 100% celestite 2020–23) | Mexico 100% | usgs_mcs_2025_strontium | verified | "Celestite: Mexico, 100%." — USGS MCS 2025 p.170 Import Sources (2020–23) |
| geopolitical_events[dod_dpa_investment].impact (February 2024) | 2024-02 | usgs_mcs_2025_strontium | verified | "In February 2024, the U.S. Department of Defense announced results of a funding opportunity under the Defense Production Act Investments program" — USGS MCS 2025 p.171 Events |
| geopolitical_events[dod_dpa_investment].impact (Louisiana and Ohio companies) | Louisiana, Ohio | usgs_mcs_2025_strontium | verified | "A company in Louisiana and a company in Ohio were selected for the domestic production of strontium nitrate, strontium oxalate, and strontium peroxide" — USGS MCS 2025 p.171 Events |
| geopolitical_events[dod_dpa_investment].impact (strontium nitrate, oxalate, peroxide) | nitrate, oxalate, peroxide | usgs_mcs_2025_strontium | verified | "strontium nitrate, strontium oxalate, and strontium peroxide, among other chemicals" — USGS MCS 2025 p.171 Events |
| geopolitical_events[strontium_atomic_clock].impact (most accurate timepiece 2024) | most accurate timepiece | usgs_mcs_2025_strontium | verified | "In 2024, a strontium atomic clock was recognized as the most accurate timepiece to date." — USGS MCS 2025 p.171 Events |
| geopolitical_events[strontium_atomic_clock].impact (oldest stars strontium and barium spectra) | strontium and barium | usgs_mcs_2025_strontium | verified | "three of the oldest stars in the universe were identified through low amounts of strontium and barium in their spectra" — USGS MCS 2025 p.171 Events |

## Notes

All numeric claims in Sr.yaml are sourced from USGS MCS 2025 Strontium chapter (pp. 170–171). No discrepancies found.

Key observations:
- World mine production figures are in **gross weight of celestite** (not strontium content), per footnote 6: "Gross weight of celestite in tons." The YAML correctly notes this distinction.
- The salient statistics table (imports, prices) is in **metric tons strontium content**, per the page header "(Data in metric tons, strontium content, unless otherwise specified)." The price row is in USD per ton of celestite (gross weight) at port of exportation (FOB origin).
- Share percentages for production countries and reserve countries are computed values (not stated in source); all correctly flagged as inferred.
- The 2024e celestite price spike to $390/ton (from $82 in 2023) is confirmed as a volume artifact: "A small quantity of high-value celestite imports were reported; these were most likely mineral specimens." The YAML notes this correctly.
- The strontium compound apparent consumption increase (22%) mentioned in the source's narrative differs slightly from the import increase (20%). The YAML reports 20% (imports), which is correct. The 22% figure applies to apparent consumption (imports minus exports).
- Salient Statistics 2024e: strontium compound imports = 4,000 mt (strontium content); celestite imports = 100 mt (strontium content), converted from gross weight celestite at 43.88%.
- Mexico 2023 celestite production = 28,000 tons is flagged as "Reported" (footnote 8) in the source, consistent with the YAML note.
- World reserves listed as "Large" (unquantified). Only China and Iran have quantified figures; all other countries show NA. Reserve share percentages in YAML are computed against the partial sum of 19,100,000 tons (China + Iran only), correctly documented.
- Criticality flags (false for US, EU CRM, EU strategic lists) are inferred — the USGS MCS 2025 chapter does not explicitly state these; absence of designation is inferred from the chapter's text and the DoD DPA investment context.

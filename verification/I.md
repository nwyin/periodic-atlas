# Verification: I

- Element: iodine (I)
- Snapshot year: 2025
- Verifier: worker-36f54045267a (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 80 |
| discrepancy | 0 |
| inferred | 26 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 33,000 tonnes_per_year | usgs_mcs_2025_iodine | verified | "World total (rounded) … 433,000" p.93 — pdftotext artifact prepends footnote-superscript '4' to 2024 figure; correct value 33,000 confirmed by summing country rows (210+22,000+30+700+9,300+3+770=33,013≈33,000) and footnote 4 "Excludes U.S. production." |
| production[0].mine.notes (2023 world total 32,600) | 32,600 | usgs_mcs_2025_iodine | verified | "World total (rounded) … 432,600" p.93 2023 column — same pdftotext artifact; correct 32,600 confirmed by country sum (200+21,000+30+700+9,900+3+770=32,603≈32,600) |
| production[0].mine.notes (US withheld, three companies Oklahoma) | W / three companies Oklahoma | usgs_mcs_2025_iodine | verified | "Iodine was produced from brines in 2024 by three companies operating in Oklahoma. U.S. iodine production in 2024 was withheld" — p.92 Domestic Production and Use |
| production[0].mining_by_country[CL].quantity.value | 22,000 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Chile … 22,000" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[CL].share_pct | 66.64 | usgs_mcs_2025_iodine | inferred | Not stated; 22,000 / 33,013 = 66.64% (denominator = named-country sum, not rounded total) |
| production[0].mining_by_country[CL].notes (2023 Chile = 21,000) | 21,000 | usgs_mcs_2025_iodine | verified | "Chile … 21,000" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[JP].quantity.value | 9,300 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Japan … 9,300" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[JP].share_pct | 28.17 | usgs_mcs_2025_iodine | inferred | Not stated; 9,300 / 33,013 = 28.17% |
| production[0].mining_by_country[JP].notes (2023 Japan = 9,900) | 9,900 | usgs_mcs_2025_iodine | verified | "Japan … 9,900" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[TM].quantity.value | 770 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Turkmenistan … 770" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[TM].share_pct | 2.33 | usgs_mcs_2025_iodine | inferred | Not stated; 770 / 33,013 = 2.33% |
| production[0].mining_by_country[TM].notes (2023 Turkmenistan = 770) | 770 | usgs_mcs_2025_iodine | verified | "Turkmenistan … 770" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[TM].notes (reserves 70,000) | 70,000 | usgs_mcs_2025_iodine | verified | "Turkmenistan … 70,000" — p.93 Reserves column |
| production[0].mining_by_country[IR].quantity.value | 700 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Iran … 700" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[IR].share_pct | 2.12 | usgs_mcs_2025_iodine | inferred | Not stated; 700 / 33,013 = 2.12% |
| production[0].mining_by_country[IR].notes (2023 Iran = 700) | 700 | usgs_mcs_2025_iodine | verified | "Iran … 700" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[IR].notes (reserves 40,000) | 40,000 | usgs_mcs_2025_iodine | verified | "Iran … 40,000" — p.93 Reserves column |
| production[0].mining_by_country[AZ].quantity.value | 210 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Azerbaijan … 210" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[AZ].share_pct | 0.64 | usgs_mcs_2025_iodine | inferred | Not stated; 210 / 33,013 = 0.64% |
| production[0].mining_by_country[AZ].notes (2023 Azerbaijan = 200) | 200 | usgs_mcs_2025_iodine | verified | "Azerbaijan … 200" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[AZ].notes (reserves 170,000) | 170,000 | usgs_mcs_2025_iodine | verified | "Azerbaijan … 170,000" — p.93 Reserves column |
| production[0].mining_by_country[ID].quantity.value | 30 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Indonesia … 30" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[ID].share_pct | 0.09 | usgs_mcs_2025_iodine | inferred | Not stated; 30 / 33,013 = 0.09% |
| production[0].mining_by_country[ID].notes (2023 Indonesia = 30) | 30 | usgs_mcs_2025_iodine | verified | "Indonesia … 30" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[ID].notes (reserves NA) | NA | usgs_mcs_2025_iodine | verified | "Indonesia … NA" — p.93 Reserves column |
| production[0].mining_by_country[RU].quantity.value | 3 tonnes_per_year | usgs_mcs_2025_iodine | verified | "Russia … 3" — p.93 Mine production table, 2024 column |
| production[0].mining_by_country[RU].share_pct | 0.01 | usgs_mcs_2025_iodine | inferred | Not stated; 3 / 33,013 = 0.009% ≈ 0.01% |
| production[0].mining_by_country[RU].notes (2023 Russia = 3) | 3 | usgs_mcs_2025_iodine | verified | "Russia … 3" — p.93 Mine production table, 2023 column |
| production[0].mining_by_country[RU].notes (reserves 120,000) | 120,000 | usgs_mcs_2025_iodine | verified | "Russia … 120,000" — p.93 Reserves column |
| production[0].notes (Chile 90%, Japan 9%, other 1% import sources 2020-23) | Chile 90%, Japan 9%, other 1% | usgs_mcs_2025_iodine | verified | "Import Sources (2020–23): Chile, 90%; Japan, 9%; and other, 1%." — p.92 |
| reserves.economic_reserves.value | 6,200,000 tonnes | usgs_mcs_2025_iodine | verified | "World total (rounded) … 6,200,000" — p.93 Reserves column |
| reserves.reserves_by_country[JP].quantity.value | 4,900,000 tonnes | usgs_mcs_2025_iodine | verified | "Japan … 4,900,000" — p.93 Reserves column |
| reserves.reserves_by_country[JP].share_pct | 79.03 | usgs_mcs_2025_iodine | inferred | Not stated; 4,900,000 / 6,200,000 = 79.03% |
| reserves.reserves_by_country[CL].quantity.value | 610,000 tonnes | usgs_mcs_2025_iodine | verified | "Chile … 610,000" — p.93 Reserves column |
| reserves.reserves_by_country[CL].share_pct | 9.84 | usgs_mcs_2025_iodine | inferred | Not stated; 610,000 / 6,200,000 = 9.84% |
| reserves.reserves_by_country[US].quantity.value | 250,000 tonnes | usgs_mcs_2025_iodine | verified | "United States … 250,000" — p.93 Reserves column |
| reserves.reserves_by_country[US].share_pct | 4.03 | usgs_mcs_2025_iodine | inferred | Not stated; 250,000 / 6,200,000 = 4.03% |
| reserves.reserves_by_country[AZ].quantity.value | 170,000 tonnes | usgs_mcs_2025_iodine | verified | "Azerbaijan … 170,000" — p.93 Reserves column |
| reserves.reserves_by_country[AZ].share_pct | 2.74 | usgs_mcs_2025_iodine | inferred | Not stated; 170,000 / 6,200,000 = 2.74% |
| reserves.reserves_by_country[RU].quantity.value | 120,000 tonnes | usgs_mcs_2025_iodine | verified | "Russia … 120,000" — p.93 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 1.94 | usgs_mcs_2025_iodine | inferred | Not stated; 120,000 / 6,200,000 = 1.94% |
| reserves.reserves_by_country[TM].quantity.value | 70,000 tonnes | usgs_mcs_2025_iodine | verified | "Turkmenistan … 70,000" — p.93 Reserves column |
| reserves.reserves_by_country[TM].share_pct | 1.13 | usgs_mcs_2025_iodine | inferred | Not stated; 70,000 / 6,200,000 = 1.13% |
| reserves.reserves_by_country[IR].quantity.value | 40,000 tonnes | usgs_mcs_2025_iodine | verified | "Iran … 40,000" — p.93 Reserves column |
| reserves.reserves_by_country[IR].share_pct | 0.65 | usgs_mcs_2025_iodine | inferred | Not stated; 40,000 / 6,200,000 = 0.65% |
| reserves.notes (named-country sum excluding Indonesia NA = 6,160,000) | 6,160,000 | usgs_mcs_2025_iodine | inferred | Arithmetic sum: 4,900,000+610,000+250,000+170,000+120,000+70,000+40,000=6,160,000; Indonesia listed as NA — not directly stated in source |
| reserves.notes (seawater 0.06 ppm iodine) | 0.06 ppm | usgs_mcs_2025_iodine | verified | "Seawater contains 0.06 part per million iodine" — p.93 World Resources |
| reserves.notes (oceans ~90 billion tons iodine) | 90 billion tons | usgs_mcs_2025_iodine | verified | "the oceans are estimated to contain approximately 90 billion tons of iodine" — p.93 World Resources |
| reserves.notes (Laminaria accumulate up to 0.45% iodine dry basis) | 0.45% | usgs_mcs_2025_iodine | verified | "Seaweeds of the Laminaria family are able to extract and accumulate up to 0.45% iodine on a dry basis" — p.93 World Resources |
| reserves.notes (seaweed major source prior to 1959) | prior to 1959 | usgs_mcs_2025_iodine | verified | "the seaweed industry represented a major source of iodine prior to 1959" — p.93 World Resources |
| prices[2024][CIF].value | 59.00 USD/kg | usgs_mcs_2025_iodine | verified | "Price, crude iodine, average unit value of imports … 59.00" — p.92 Salient Statistics, 2024e column |
| prices[2024][CIF].notes (4% less than 2023) | 4% | usgs_mcs_2025_iodine | verified | "about 4% less than that in 2023" — p.92 Domestic Production and Use |
| prices[2024][spot].value | 69.00 USD/kg | usgs_mcs_2025_iodine | verified | "spot prices for iodine crystal averaged about $69 per kilogram during the first 9 months of 2024" — p.93 Events |
| prices[2024][spot].notes (3% less than 2023 annual average) | 3% | usgs_mcs_2025_iodine | verified | "about 3% less than the 2023 annual average of $71.48 per kilogram" — p.93 Events |
| prices[2023][CIF].value | 61.55 USD/kg | usgs_mcs_2025_iodine | verified | "Price … 61.55" — p.92 Salient Statistics, 2023 column |
| prices[2023][spot].value | 71.48 USD/kg | usgs_mcs_2025_iodine | verified | "the 2023 annual average of $71.48 per kilogram" — p.93 Events |
| prices[2022][CIF].value | 45.81 USD/kg | usgs_mcs_2025_iodine | verified | "Price … 45.81" — p.92 Salient Statistics, 2022 column |
| prices[2021][CIF].value | 32.72 USD/kg | usgs_mcs_2025_iodine | verified | "Price … 32.72" — p.92 Salient Statistics, 2021 column |
| prices[2020][CIF].value | 31.57 USD/kg | usgs_mcs_2025_iodine | verified | "Price … 31.57" — p.92 Salient Statistics, 2020 column |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_iodine | inferred | Not stated in source; iodine absent from 2022 US Critical Minerals List per Federal Register |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_iodine | inferred | Not stated in source; iodine absent from EU CRM Annex I/II (Regulation 2024/1252) |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_iodine | inferred | Not stated in source; iodine absent from EU CRMA 2024 Annex I strategic list |
| criticality.notes (net import reliance >50% in 2020) | >50% | usgs_mcs_2025_iodine | verified | "Net import reliance … >50" — p.92 Salient Statistics, 2020 column |
| criticality.notes (net import reliance >50% in 2021) | >50% | usgs_mcs_2025_iodine | verified | "Net import reliance … >50" — p.92 Salient Statistics, 2021 column |
| criticality.notes (net import reliance >50% in 2022) | >50% | usgs_mcs_2025_iodine | verified | "Net import reliance … >50" — p.92 Salient Statistics, 2022 column |
| criticality.notes (net import reliance <50% in 2023) | <50% | usgs_mcs_2025_iodine | verified | "Net import reliance … <50" — p.92 Salient Statistics, 2023 column |
| criticality.notes (net import reliance >50% in 2024e) | >50% | usgs_mcs_2025_iodine | verified | "Net import reliance … >50" — p.92 Salient Statistics, 2024e column |
| end_uses.uses[x_ray_contrast_media] (leading use, first in descending order) | x_ray_contrast_media (rank 1) | usgs_mcs_2025_iodine | verified | "the leading uses of iodine and its compounds were X-ray contrast media (XRCM), pharmaceuticals, liquid crystal displays (LCDs), iodophors, animal feed, and fluorochemicals, in descending order of quantity consumed" — p.92 |
| end_uses.uses[pharmaceuticals] (second in descending order) | pharmaceuticals (rank 2) | usgs_mcs_2025_iodine | verified | Listed second in "X-ray contrast media (XRCM), pharmaceuticals, …" — p.92 Domestic Production and Use |
| end_uses.uses[liquid_crystal_displays] (third in descending order) | liquid_crystal_displays (rank 3) | usgs_mcs_2025_iodine | verified | Listed third in the descending-order sequence — p.92 |
| end_uses.uses[iodophors] (fourth in descending order) | iodophors (rank 4) | usgs_mcs_2025_iodine | verified | Listed fourth in the descending-order sequence — p.92 |
| end_uses.uses[animal_feed] (fifth in descending order) | animal_feed (rank 5) | usgs_mcs_2025_iodine | verified | Listed fifth in the descending-order sequence — p.92 |
| end_uses.uses[fluorochemicals] (sixth in descending order) | fluorochemicals (rank 6) | usgs_mcs_2025_iodine | verified | Listed sixth in the descending-order sequence — p.92 |
| end_uses.uses[other_uses] (biocides, food supplements, nylon) | biocides / food supplements / nylon | usgs_mcs_2025_iodine | verified | "Other applications of iodine included biocides, food supplements, and nylon." — p.92 |
| end_uses.uses[other_uses].notes (domestic crude/inorganic ~80%) | ~80% | usgs_mcs_2025_iodine | verified | "Crude iodine and inorganic iodine compounds were estimated to account for almost 80% of domestic iodine consumption in 2024" — p.92 |
| end_uses.uses[other_uses].notes (domestic organic ~20%) | ~20% | usgs_mcs_2025_iodine | verified | "organic iodine compounds were estimated to account for about 20%" — p.92 |
| end_uses.uses[x_ray_contrast_media].share_pct | 35 | usgs_mcs_2025_iodine | inferred | No explicit % in source; estimate based on rank-1 position and industry data patterns; USGS MCS 2025 states only descending order |
| end_uses.uses[pharmaceuticals].share_pct | 20 | usgs_mcs_2025_iodine | inferred | No explicit % in source; rank-2 estimate |
| end_uses.uses[liquid_crystal_displays].share_pct | 15 | usgs_mcs_2025_iodine | inferred | No explicit % in source; rank-3 estimate |
| end_uses.uses[iodophors].share_pct | 10 | usgs_mcs_2025_iodine | inferred | No explicit % in source; rank-4 estimate |
| end_uses.uses[animal_feed].share_pct | 10 | usgs_mcs_2025_iodine | inferred | No explicit % in source; rank-5 estimate |
| end_uses.uses[fluorochemicals].share_pct | 6 | usgs_mcs_2025_iodine | inferred | No explicit % in source; rank-6 estimate |
| end_uses.uses[other_uses].share_pct | 4 | usgs_mcs_2025_iodine | inferred | No explicit % in source; residual after ranking estimates sum to 96% |
| geopolitical_events[2024-07].date (seventh production plant, second half 2024) | 2024-07 | usgs_mcs_2025_iodine | inferred | Source says "in the second half of 2024" (July–December); YAML uses 2024-07 as earliest H2 month — specific month not confirmed in source |
| geopolitical_events[2024-07].event (100–150 t/yr capacity addition) | 100–150 t/yr | usgs_mcs_2025_iodine | verified | "expected to add an additional 100 to 150 metric tons per year of crystalline iodine" — p.93 Events |
| geopolitical_events[2024-07].impact (eighth plant agreement, operational 2025) | eighth plant / 2025 | usgs_mcs_2025_iodine | verified | "The company also signed an agreement for an eighth plant that was expected to become operational in 2025." — p.93 Events |
| geopolitical_events[2024-01 price].impact (spot ~$69/kg first 9 months 2024) | ~$69/kg | usgs_mcs_2025_iodine | verified | "spot prices for iodine crystal averaged about $69 per kilogram during the first 9 months of 2024" — p.93 Events |
| geopolitical_events[2024-01 price].impact (3% less than 2023 annual average $71.48) | 3% / $71.48 | usgs_mcs_2025_iodine | verified | "about 3% less than the 2023 annual average of $71.48 per kilogram" — p.93 Events |
| geopolitical_events[2024-01 price].impact (iodine sales increased in 2024) | sales increased | usgs_mcs_2025_iodine | verified | "iodine sales increased, reflecting strong global demand in 2024" — p.93 Events |
| geopolitical_events[2024-01 price].impact (CIF $59.00 from $61.55 in 2023) | $59.00 / $61.55 | usgs_mcs_2025_iodine | verified | Salient Statistics 2024e = 59.00; 2023 = 61.55 — p.92 |
| geopolitical_events[2024-01 price].impact (US imports 3,300 from 2,860 in 2023) | 3,300 / 2,860 | usgs_mcs_2025_iodine | verified | "Imports for consumption … 2,860 … 3,300" — p.92 Salient Statistics, 2023 and 2024e columns |
| geopolitical_events[2024-01 chile].impact (Chile 22,000 t 2024e, Japan 9,300 t) | 22,000 / 9,300 | usgs_mcs_2025_iodine | verified | "Chile … 22,000" and "Japan … 9,300" — p.93 Mine production table, 2024 column |
| geopolitical_events[2024-01 chile].impact (Chile ~two-thirds of world ex-US) | ~two-thirds | usgs_mcs_2025_iodine | verified | "Excluding production in the United States, Chile accounted for about two-thirds of world production in 2024." — p.93 Events |
| geopolitical_events[2024-01 chile].impact (Chile 90%, Japan 9% import sources 2020-23) | Chile 90% / Japan 9% | usgs_mcs_2025_iodine | verified | "Import Sources (2020–23): Chile, 90%; Japan, 9%; and other, 1%." — p.92 |
| feedstock_origins[caliche_ore].notes (Chilean desert nitrate mines) | Chilean desert nitrate mines | usgs_mcs_2025_iodine | verified | "the Chilean desert nitrate mines" — p.93 Events |
| feedstock_origins[caliche_ore].notes (Chile 22,000 t ~67% ex-US) | 22,000 / ~67% | usgs_mcs_2025_iodine | verified | Chile 22,000 t from p.93 table; ~67% ex-US from "about two-thirds of world production" — p.93 Events |
| feedstock_origins[gas_and_oil_brine].notes (gasfields and oilfields in Japan) | gasfields and oilfields Japan | usgs_mcs_2025_iodine | verified | "the gasfields and oilfields in Japan" — p.93 Events |
| feedstock_origins[gas_and_oil_brine].notes (Japan 9,300 t/yr 2024e) | 9,300 t/yr | usgs_mcs_2025_iodine | verified | "Japan … 9,300" — p.93 Mine production table, 2024 column |
| feedstock_origins[gas_and_oil_brine].notes (three companies NW Oklahoma) | three companies NW Oklahoma | usgs_mcs_2025_iodine | verified | "three companies operating in Oklahoma" — p.92 Domestic Production and Use; "iodine-rich brine wells in northwestern Oklahoma" — p.93 Events |
| substitutes[animal_feed_catalytic_nutritional_pharmaceutical_photographic].notes | no comparable substitutes | usgs_mcs_2025_iodine | verified | "No comparable substitutes exist for iodine in many of its principal applications, such as in animal feed, catalytic, nutritional, pharmaceutical, and photographic uses." — p.93 Substitutes |
| substitutes[biocide_colorant_ink].notes (bromine and chlorine) | bromine and chlorine | usgs_mcs_2025_iodine | verified | "Bromine and chlorine could be substituted for iodine in biocide, colorant, and ink" — p.93 Substitutes |
| substitutes[biocide_colorant_ink].notes (usually less desirable) | usually less desirable | usgs_mcs_2025_iodine | verified | "although they are usually considered less desirable than iodine" — p.93 Substitutes |
| substitutes[iodine_biocides].notes (antibiotics) | antibiotics | usgs_mcs_2025_iodine | verified | "Antibiotics can be used as a substitute for iodine biocides." — p.93 Substitutes |

## Notes

All 106 numeric claims derive from a single source: USGS MCS 2025 Iodine chapter (pp. 92–93). The PDF was fetched from https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-iodine.pdf and extracted via pdftotext -layout.

**Critical pdftotext artifact (confirmed):** The USGS table footnote superscript "4" (footnote text: "Excludes U.S. production.") is placed adjacent to the "World total (rounded)" row label. pdftotext merges the "4" into the leading digit of both the 2023 and 2024 mine production values, rendering "32,600" as "432,600" and "33,000" as "433,000". The correct world totals — 32,600 (2023) and 33,000 (2024e) — are confirmed by independent summation of all named-country rows. This artifact does NOT affect the Reserves column; the world reserve total of 6,200,000 is correct as stated.

**Key structural facts confirmed:**
- World production totals (2023: 32,600 t; 2024e: 33,000 t) explicitly EXCLUDE U.S. production per footnote 4.
- U.S. production is "W" (withheld) for all five years 2020–2024e in the Salient Statistics table.
- World reserves = 6,200,000 metric tons. Japan holds 4,900,000 (79%), Chile 610,000 (10%), United States 250,000 (4%). Indonesia listed as NA; China and Uzbekistan have no reported reserves.
- Named-country reserve sum (excluding Indonesia NA) = 6,160,000 metric tons; stated world total 6,200,000 metric tons likely includes rounding or unlisted countries.
- Net import reliance: >50% in 2020, 2021, 2022, and 2024e; <50% in 2023 only.
- Import sources (2020–23 average): Chile 90%, Japan 9%, other 1%.
- End-use ranking confirmed in descending order: XRCM, pharmaceuticals, LCD, iodophors, animal feed, fluorochemicals. No explicit percentage breakdown given by USGS; all share_pct values are analyst estimates marked `inferred`.
- Share percentages for mine production and reserves are computed (country value ÷ appropriate denominator) and marked `inferred`; none are stated in the source.
- Criticality flags (false for all three lists) reflect external policy knowledge not stated in the USGS chapter; all marked `inferred`.
- The geopolitical event date "2024-07" for the seventh production plant opening is an approximation; the source states only "second half of 2024" without specifying a month.
- No discrepancies found between YAML values and the source document.

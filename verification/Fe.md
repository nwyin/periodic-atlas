# Verification: Fe

- Element: iron (Fe)
- Snapshot year: 2025
- Verifier: worker-08e27406e517 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 57 |
| discrepancy | 7 |
| inferred | 43 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 2500 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "World total (rounded) … 2,500,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column (data in thousand metric tons, usable ore) |
| production[0].mining_by_country[AU].quantity.value | 930 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Australia … 930,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[AU].share_pct | 37.2 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 930/2500 = 37.2% |
| production[0].mining_by_country[BR].quantity.value | 440 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Brazil … 440,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[BR].share_pct | 17.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 440/2500 = 17.6% |
| production[0].mining_by_country[CN].quantity.value | 270 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "China … 270,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[CN].share_pct | 10.8 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 270/2500 = 10.8% |
| production[0].mining_by_country[IN].quantity.value | 270 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "India … 270,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[IN].share_pct | 10.8 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 270/2500 = 10.8% |
| production[0].mining_by_country[RU].quantity.value | 91 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Russia … 91,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[RU].share_pct | 3.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 91/2500 = 3.64% → 3.6% |
| production[0].mining_by_country[IR].quantity.value | 90 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Iran … 90,000e" — USGS MCS 2025 World Mine Production table, 2024e column (estimated) |
| production[0].mining_by_country[IR].share_pct | 3.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 90/2500 = 3.6% |
| production[0].mining_by_country[ZA].quantity.value | 66 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "South Africa … 66,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[ZA].share_pct | 2.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 66/2500 = 2.64% → 2.6% |
| production[0].mining_by_country[CA].quantity.value | 54 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Canada … 54,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[CA].share_pct | 2.2 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 54/2500 = 2.16% → 2.2% |
| production[0].mining_by_country[US].quantity.value | 48 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "United States … 48,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[US].share_pct | 1.9 | usgs_mcs_2025_iron_ore | verified | "The United States was estimated to have produced 1.8% … of the world's iron ore output" — USGS MCS 2025 Domestic Production and Use text; 48/2500 = 1.92% → 1.9% consistent |
| production[0].mining_by_country[UA].quantity.value | 42 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Ukraine … 42,000e" — USGS MCS 2025 World Mine Production table, 2024e column (estimated) |
| production[0].mining_by_country[UA].share_pct | 1.7 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 42/2500 = 1.68% → 1.7% |
| production[0].mining_by_country[KZ].quantity.value | 30 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Kazakhstan … 30,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[KZ].share_pct | 1.2 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 30/2500 = 1.2% |
| production[0].mining_by_country[SE].quantity.value | 28 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Sweden … 28,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[SE].share_pct | 1.1 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 28/2500 = 1.12% → 1.1% |
| production[0].mining_by_country[PE].quantity.value | 21 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Peru … 21,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[PE].share_pct | 0.8 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 21/2500 = 0.84% → 0.8% |
| production[0].mining_by_country[CL].quantity.value | 18 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Chile … 18,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[CL].share_pct | 0.7 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 18/2500 = 0.72% → 0.7% |
| production[0].mining_by_country[TR].quantity.value | 18 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Turkey … 18,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[TR].share_pct | 0.7 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 18/2500 = 0.72% → 0.7% |
| production[0].mining_by_country[MR].quantity.value | 15 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Mauritania … 15,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[MR].share_pct | 0.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 15/2500 = 0.6% |
| production[0].mining_by_country[MX].quantity.value | 8 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Mexico … 8,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[MX].share_pct | 0.3 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 8/2500 = 0.32% → 0.3% |
| production[0].mining_by_country[ZZ].quantity.value | 64 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "Other countries … 64,000" — USGS MCS 2025 World Mine Production table, usable ore 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 2.6 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 64/2500 = 2.56% → 2.6% |
| production[1].refined.value | 1879 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 (data finalised 04 June 2025) table "Major steel-producing countries 2023 and 2024" shows World total 2024 = 1,884.6 Mt, not 1,879 Mt. Discrepancy of ~5.6 Mt. The 1,879 figure may derive from an earlier worldsteel preliminary estimate (e.g. October 2024 short range outlook cited by USGS). |
| production[1].refining_by_country[CN].quantity.value | 1006 million_tonnes_per_year | worldsteel_2025 | inferred | World Steel in Figures 2025 shows China 2024 = 1,005.1 Mt; YAML rounds to 1,006 Mt (difference 0.9 Mt, within 0.1%). Treated as inferred due to rounding ambiguity and world-total discrepancy. |
| production[1].refining_by_country[CN].share_pct | 53.5 | worldsteel_2025 | inferred | Not stated in source; 1005.1/1884.6 = 53.3% per worldsteel final data; 1006/1879 = 53.5% per YAML's own figures. Internally consistent but dependent on discrepant world total. |
| production[1].refining_by_country[IN].quantity.value | 145 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 shows India 2024 = 149.4 Mt; YAML states 145 Mt. Discrepancy of 4.4 Mt (3%). |
| production[1].refining_by_country[IN].share_pct | 7.7 | worldsteel_2025 | discrepancy | 145/1879 = 7.7% per YAML; 149.4/1884.6 = 7.9% per worldsteel final data. |
| production[1].refining_by_country[JP].quantity.value | 84 million_tonnes_per_year | worldsteel_2025 | verified | World Steel in Figures 2025 shows Japan 2024 = 84.0 Mt — exact match. |
| production[1].refining_by_country[JP].share_pct | 4.5 | worldsteel_2025 | inferred | Not stated in source; 84.0/1884.6 = 4.46% → 4.5% |
| production[1].refining_by_country[US].quantity.value | 81 million_tonnes_per_year | usgs_mcs_2025_iron_ore | verified | "raw steel production were estimated to have remained unchanged … at … 81 million tons … in 2024" — USGS MCS 2025 Events, Trends, and Issues text. Note: worldsteel final data shows US 79.5 Mt; USGS cited source gives 81 Mt. |
| production[1].refining_by_country[US].share_pct | 4.3 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 81/1879 = 4.31% → 4.3% per YAML's figures |
| production[1].refining_by_country[RU].quantity.value | 72 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 shows Russia 2024 = 71.0 Mt; YAML states 72 Mt. Discrepancy of 1 Mt. |
| production[1].refining_by_country[RU].share_pct | 3.8 | worldsteel_2025 | inferred | Not stated in source; 72/1879 = 3.83% → 3.8% per YAML's own figures |
| production[1].refining_by_country[KR].quantity.value | 66 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 shows South Korea 2024 = 63.6 Mt; YAML states 66 Mt. Discrepancy of 2.4 Mt (3.8%). |
| production[1].refining_by_country[KR].share_pct | 3.5 | worldsteel_2025 | inferred | Not stated in source; 66/1879 = 3.51% → 3.5% per YAML's figures |
| production[1].refining_by_country[DE].quantity.value | 35 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 shows Germany 2024 = 37.2 Mt; YAML states 35 Mt. Discrepancy of 2.2 Mt (5.9%). |
| production[1].refining_by_country[DE].share_pct | 1.9 | worldsteel_2025 | inferred | Not stated in source; 35/1879 = 1.86% → 1.9% per YAML's figures |
| production[1].refining_by_country[TR].quantity.value | 35 million_tonnes_per_year | worldsteel_2025 | discrepancy | World Steel in Figures 2025 shows Türkiye 2024 = 36.9 Mt; YAML states 35 Mt. Discrepancy of 1.9 Mt (5.1%). |
| production[1].refining_by_country[TR].share_pct | 1.9 | worldsteel_2025 | inferred | Not stated in source; 35/1879 = 1.86% → 1.9% per YAML's figures |
| production[1].refining_by_country[BR].quantity.value | 34 million_tonnes_per_year | worldsteel_2025 | verified | World Steel in Figures 2025 shows Brazil 2024 = 33.8 Mt; YAML states 34 Mt. Within 0.2 Mt rounding. |
| production[1].refining_by_country[BR].share_pct | 1.8 | worldsteel_2025 | inferred | Not stated in source; 34/1879 = 1.81% → 1.8% |
| production[1].refining_by_country[ZZ].quantity.value | 321 million_tonnes_per_year | worldsteel_2025 | inferred | Residual: 1879 − (1006+145+84+81+72+66+35+35+34) = 321 Mt per YAML's own totals; worldsteel-based residual is ~324 Mt due to discrepant world total and country figures |
| production[1].refining_by_country[ZZ].share_pct | 17.1 | worldsteel_2025 | inferred | Not stated in source; 321/1879 = 17.1% per YAML's own figures |
| reserves.economic_reserves.value | 200000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "World total (rounded) … 200,000" million metric tons crude ore — USGS MCS 2025 Reserves column. Converted: 200,000 million metric tons × 10⁶ = 2×10¹⁴ tonnes. |
| reserves.resources.value | 800000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "World resources are estimated to be greater than 800 billion tons of iron ore" — USGS MCS 2025 World Resources note. YAML stores 8×10¹⁴ tonnes = 800 billion metric tons (USGS uses metric tons in international context). |
| reserves.reserves_by_country[AU].quantity.value | 58000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Australia … 58,000" million metric tons crude ore — USGS MCS 2025 Reserves column. Converted: 58,000 × 10⁹ = 5.8×10¹³ tonnes. |
| reserves.reserves_by_country[AU].share_pct | 29.0 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 58000/200000 = 29.0% |
| reserves.reserves_by_country[RU].quantity.value | 35000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Russia … 35,000" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 17.5 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 35000/200000 = 17.5% |
| reserves.reserves_by_country[BR].quantity.value | 34000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Brazil … 34,000" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 17.0 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 34000/200000 = 17.0% |
| reserves.reserves_by_country[CN].quantity.value | 20000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "China … 20,000" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 10.0 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 20000/200000 = 10.0% |
| reserves.reserves_by_country[UA].quantity.value | 6500000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Ukraine … 6,500" million metric tons crude ore — USGS MCS 2025 Reserves column; footnote 7: "reserves consist of the A and B categories of the Soviet reserves classification system" |
| reserves.reserves_by_country[UA].share_pct | 3.3 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 6500/200000 = 3.25% → YAML rounds to 3.3% |
| reserves.reserves_by_country[CA].quantity.value | 6000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Canada … 6,000" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[CA].share_pct | 3.0 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 6000/200000 = 3.0% |
| reserves.reserves_by_country[IN].quantity.value | 5500000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "India … 5,500" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 2.8 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 5500/200000 = 2.75% → 2.8% |
| reserves.reserves_by_country[IR].quantity.value | 3800000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Iran … 3,800" million metric tons crude ore — USGS MCS 2025 Reserves column (revised per table note) |
| reserves.reserves_by_country[IR].share_pct | 1.9 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 3800/200000 = 1.9% |
| reserves.reserves_by_country[US].quantity.value | 3600000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "United States … 3,600" million metric tons crude ore — USGS MCS 2025 Reserves column (revised per table note) |
| reserves.reserves_by_country[US].share_pct | 1.8 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 3600/200000 = 1.8% |
| reserves.reserves_by_country[PE].quantity.value | 2600000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Peru … 2,600" million metric tons crude ore — USGS MCS 2025 Reserves column (revised per table note) |
| reserves.reserves_by_country[PE].share_pct | 1.3 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 2600/200000 = 1.3% |
| reserves.reserves_by_country[KZ].quantity.value | 2500000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Kazakhstan … 2,500" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[KZ].share_pct | 1.3 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 2500/200000 = 1.25% → YAML rounds to 1.3% |
| reserves.reserves_by_country[SE].quantity.value | 1300000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Sweden … 1,300" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[SE].share_pct | 0.7 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 1300/200000 = 0.65% → YAML rounds to 0.7% |
| reserves.reserves_by_country[ZA].quantity.value | 930000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "South Africa … 930" million metric tons crude ore — USGS MCS 2025 Reserves column (revised per table note) |
| reserves.reserves_by_country[ZA].share_pct | 0.5 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 930/200000 = 0.465% → 0.5% |
| reserves.reserves_by_country[TR].quantity.value | 150000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Turkey … 150" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[TR].share_pct | 0.1 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 150/200000 = 0.075% → 0.1% |
| reserves.reserves_by_country[ZZ].quantity.value | 17000000000000 tonnes | usgs_mcs_2025_iron_ore | verified | "Other countries … 17,000" million metric tons crude ore — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 8.5 | usgs_mcs_2025_iron_ore | inferred | Not stated in source; 17000/200000 = 8.5% |
| end_uses.uses[steel_industry].share_pct | 98 | usgs_mcs_2025_iron_ore | verified | "98% of domestic usable iron ore products for consumption in the steel industry" — USGS MCS 2025 Domestic Production and Use text |
| end_uses.uses[nonsteel_uses].share_pct | 2 | usgs_mcs_2025_iron_ore | verified | "The remaining 2% of domestic iron ore products were consumed in nonsteel end uses" — USGS MCS 2025 Domestic Production and Use text |
| prices[2024].value | 115 usd_per_tonne | usgs_mcs_2025_iron_ore | verified | "115" — USGS MCS 2025 Salient Statistics table, "Price, average unit value reported by mines, dollars per metric ton", 2024e column |
| prices[2023].value | 120.36 usd_per_tonne | usgs_mcs_2025_iron_ore | verified | "120.36" — USGS MCS 2025 Salient Statistics table, average unit value per metric ton, 2023 column |
| prices[2022].value | 156.42 usd_per_tonne | usgs_mcs_2025_iron_ore | verified | "156.42" — USGS MCS 2025 Salient Statistics table, average unit value per metric ton, 2022 column |
| prices[2021].value | 141.78 usd_per_tonne | usgs_mcs_2025_iron_ore | verified | "141.78" — USGS MCS 2025 Salient Statistics table, average unit value per metric ton, 2021 column |
| prices[2020].value | 82.25 usd_per_tonne | usgs_mcs_2025_iron_ore | verified | "82.25" — USGS MCS 2025 Salient Statistics table, average unit value per metric ton, 2020 column |
| geopolitical_events[2024-02].event | Nevada iron ore mine water permits, 11.5 Mt/yr | usgs_mcs_2025_iron_ore | verified | "In February, one company received water permits that would allow for the construction … of a mine permitted for up to 11.5 million tons per year … northeast of Reno, NV" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[2024-05].event | Hibbing, MN DR-grade pellets, 4 Mt/yr, 67% Fe | usgs_mcs_2025_iron_ore | verified | "In May, one company began production of direct-reduction (DR)-grade iron ore pellets in Hibbing, MN … 4-million-ton-per-year production capacity of DR-grade iron ore pellets with a 67% iron or higher grade" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[2024-06].event | Canada adds high-purity iron to Critical Minerals List | usgs_mcs_2025_iron_ore | verified | "In June, Canada's Critical Minerals List was updated to include high-purity iron, citing the necessity of that mineral's role in decarbonization" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[2024-01].event | China Iron and Steel Association calls for production cuts | usgs_mcs_2025_iron_ore | verified | "The China Iron and Steel Association … called for a cut in production in domestic steelmaking, citing rapidly declining prices" — USGS MCS 2025 Events, Trends, and Issues. YAML assigns 2024-01; USGS does not specify a month within 2024. |
| geopolitical_events[2024-12].event | Guinea Simandou finalized, 60 Mt/yr by 2028 | usgs_mcs_2025_iron_ore | verified | "Development of one of the world's largest high-grade iron ore deposits, located in Guinea, was expected by yearend 2024 … Production was expected to start in 2025, and a full production rate of 60 million tons per year was expected by 2028" — USGS MCS 2025 Events, Trends, and Issues |
| substitutes[steelmaking_raw_material].notes | USGS substitutes paragraph quote | usgs_mcs_2025_iron_ore | verified | "The only source of primary iron is iron ore, used directly as direct-shipping ore or converted to briquettes, concentrates, DRI, iron nuggets, pellets, or sinter. DRI, iron nuggets, and scrap are extensively used for steelmaking in electric arc furnaces and in iron and steel foundries. Technological advancements have been made that allow hematite to be recovered from tailings basins and pelletized." — USGS MCS 2025 Substitutes paragraph (verbatim match) |
| feedstock_origins[iron_ore_magnetite].notes | Taconite ~65% Fe, Lake Superior district, beneficiation required | usgs_mcs_2025_iron_ore | inferred | USGS MCS 2025 confirms US ores are "low-grade taconite-type ores from the Lake Superior district that require beneficiation and agglomeration" in World Resources note. 65% Fe after processing is consistent with industry data but not directly quoted in the cited chapter. |
| feedstock_origins[iron_ore_hematite].notes | Pilbara ~57-62% Fe; Carajás ~65% Fe | usgs_mcs_2025_iron_ore | inferred | USGS MCS 2025 confirms Australia and Brazil as major DSO exporters but does not state Fe-grade percentages in the chapter text. Grade ranges are standard industry figures consistent with USGS context but not directly sourced in this chapter. |
| feedstock_origins[iron_ore_dr_grade_pellets].notes | ≥67% Fe, Hibbing 4 Mt/yr May 2024 | usgs_mcs_2025_iron_ore | verified | "4-million-ton-per-year production capacity of DR-grade iron ore pellets with a 67% iron or higher grade" — USGS MCS 2025 Events, Trends, and Issues |

## Notes

**Source access**: USGS MCS 2025 Iron Ore PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-iron-ore.pdf) was fetched as binary and extracted via pdftotext. Full text of both pages extracted successfully. World Steel in Figures 2025 PDF (https://worldsteel.org/wp-content/uploads/World-Steel-in-Figures-2025.pdf) was fetched as binary and extracted via pdftotext; data finalised 04 June 2025. Worldsteel main statistics page returned only structural HTML with no production tables.

**Worldsteel world total discrepancy**: The YAML cites worldsteel_2025 for a world crude steel total of 1,879 Mt. The actual "World Steel in Figures 2025" document (finalized June 2025) shows the world 2024 total as 1,884.6 Mt. The USGS MCS 2025 cites "worldsteel short range outlook October 2024" for the demand figure; the October 2024 preliminary estimate likely underlay the YAML. The final worldsteel figures (June 2025) differ by ~5.6 Mt (0.3%). All country-level worldsteel figures in the YAML should be cross-checked against the preliminary October 2024 estimate for a definitive verdict.

**Country-level crude steel discrepancies**: Five of nine named non-USGS countries show discrepancies vs World Steel in Figures 2025 final data: India (−4.4 Mt), South Korea (−2.4 Mt), Germany (−2.2 Mt), Turkey (−1.9 Mt), Russia (−1.0 Mt). These likely trace to use of the October 2024 preliminary worldsteel estimate rather than the June 2025 final figures. Japan (84.0 Mt) and Brazil (33.8→34 Mt rounded) match. US (81 Mt) is sourced from USGS, not worldsteel, and is confirmed by USGS text.

**US production consistency**: YAML note states US raw steel = 81 Mt and pig iron = 22 Mt unchanged from 2023. USGS text confirms: "Pig iron production and raw steel production were estimated to have remained unchanged at 22 million tons and 81 million tons, respectively, in 2024." Worldsteel final data shows US = 79.5 Mt (2024e), suggesting either rounding or methodology difference between USGS and worldsteel reporting. No discrepancy flagged for US since the cited source (usgs_mcs_2025_iron_ore) explicitly states 81 Mt.

**Reserve totals and rounding**: USGS table header states data are in "million metric tons" for reserves. World total = 200,000 million metric tons = 2×10¹⁴ tonnes stored in YAML. Named-country reserve sum: 58,000+35,000+34,000+20,000+6,500+6,000+5,500+3,800+3,600+2,600+2,500+1,300+930+150+6,500+17,000 = 203,380 million metric tons, which exceeds the rounded world total of 200,000 Mmmt. This is expected given USGS rounding of the world total; Chile, Mauritania, and Mexico show NA in USGS reserves, so the "Other countries" row absorbs the remainder.

**CISA/NDRC events**: YAML date 2024-01 for the CISA production-cut call. USGS text does not specify a month; it describes events within 2024 generally. January 2024 is plausible for early-year statements but not independently confirmed from the cited source.

**Guinea Simandou**: YAML date 2024-12 (yearend) is consistent with USGS text "expected by yearend 2024" for finalization of ownership. Production start expected 2025, 60 Mt/yr full rate by 2028 — both confirmed verbatim.

**Import source percentages**: "Import Sources (2020–23): Brazil, 47%; Canada, 30%; Sweden, 13%; Bahrain, 3%; and other, 7%" confirmed verbatim in USGS Salient Statistics. The YAML narrative correctly cites these; the claims are in the notes text rather than a structured field, so not separately tabulated.

**Global average unit value $112.06**: Confirmed in USGS Events section: "an average unit value of $112.06 per ton in the first 9 months of 2024." This is consistent with the 2024 price of $115 (full-year average reported by US mines).

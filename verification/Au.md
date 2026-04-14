# Verification: Au

- Element: gold (Au)
- Snapshot year: 2025
- Verifier: worker-80c038b51456 (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 87 |
| discrepancy | 2 |
| inferred | 39 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[2024].mine.value | 160 tonnes_per_year | usgs_mcs_2025_gold | verified | "domestic gold mine production was estimated to be 160 tons" — USGS MCS 2025 p.82 Domestic Production and Use; Salient Statistics Mine row 2024e = 160 |
| production[2024].mine.notes (value $12 billion) | ~$12 billion | usgs_mcs_2025_gold | verified | "the value was estimated to be $12 billion" — USGS MCS 2025 p.82 Domestic Production and Use |
| production[2024].mine.notes (9% increase in value from 2023) | 9% | usgs_mcs_2025_gold | verified | "a 9% increase from the value in 2023" — USGS MCS 2025 p.82 Domestic Production and Use |
| production[2024].mine.notes (40+ lode mines in 12 states) | 40+ mines; 12 states | usgs_mcs_2025_gold | verified | "Gold was produced at more than 40 lode mines in 12 States" — USGS MCS 2025 p.82 |
| production[2024].mine.notes (Nevada ~70%) | ~70% | usgs_mcs_2025_gold | verified | "accounting for about 70% of total domestic production" — USGS MCS 2025 p.82 |
| production[2024].mine.notes (Alaska ~16%) | ~16% | usgs_mcs_2025_gold | verified | "produced about 16% of domestic gold" — USGS MCS 2025 p.82 |
| production[2024].mine.notes (~7% byproduct copper) | ~7% | usgs_mcs_2025_gold | verified | "About 7% of domestic gold was recovered as a byproduct of processing domestic base-metal ores, chiefly copper ores" — USGS MCS 2025 p.82 |
| production[2024].mine.notes (top 26 operations ~97%) | ~97% | usgs_mcs_2025_gold | verified | "The top 26 operations yielded about 97% of the mined gold produced in the United States" — USGS MCS 2025 p.82 |
| production[2024].refined.value | 260 tonnes_per_year | usgs_mcs_2025_gold | inferred | Not stated as a single figure; derived as primary 170 t + secondary 90 t = 260 t; both components directly stated in Salient Statistics 2024e |
| production[2024].refined.notes (primary 170 t, 2024e) | 170 t | usgs_mcs_2025_gold | verified | "Primary … 170" — USGS MCS 2025 p.82 Salient Statistics, Refinery Primary row, 2024e column |
| production[2024].refined.notes (secondary 90 t, 2024e) | 90 t | usgs_mcs_2025_gold | verified | "Secondary (new and old scrap) … 90" — USGS MCS 2025 p.82 Salient Statistics, 2024e column |
| production[2024].refined.notes (~15 refineries) | ~15 | usgs_mcs_2025_gold | verified | "Commercial-grade gold was produced at approximately 15 refineries" — USGS MCS 2025 p.82 |
| production[2024].refined.notes (primary 179 t, 2023) | 179 t | usgs_mcs_2025_gold | verified | "Primary … 179" — USGS MCS 2025 p.82 Salient Statistics, Refinery Primary row, 2023 column |
| production[2024].refined.notes (secondary 96 t, 2023) | 96 t | usgs_mcs_2025_gold | verified | "Secondary (new and old scrap) … 96" — USGS MCS 2025 p.82 Salient Statistics, 2023 column |
| production[2024].refined.notes (scrap ~45% US consumption) | ~45% | usgs_mcs_2025_gold | verified | "equivalent to about 45% of reported consumption" — USGS MCS 2025 p.82 Recycling |
| production[2024].notes (world mine production 2023 = 3,250 t) | 3,250 t | usgs_mcs_2025_gold | verified | "World total (rounded) … 3,250" — USGS MCS 2025 p.83 World Mine Production table, 2023 column |
| production[2024].notes (world mine production 2024e = 3,300 t) | 3,300 t | usgs_mcs_2025_gold | verified | "World total (rounded) … 3,300" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].notes (top 5 countries = 41% of world) | 41% | usgs_mcs_2025_gold | verified | "together accounted for 41% of estimated global production in 2024" — USGS MCS 2025 p.82 Events |
| production[2024].notes (Burkina Faso reserves = NA) | NA | usgs_mcs_2025_gold | verified | "Burkina Faso … NA" — USGS MCS 2025 p.83 World Mine Production table, Reserves column |
| production[2024].mining_by_country[CN].quantity.value | 380 tonnes_per_year | usgs_mcs_2025_gold | verified | "China … 380" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[CN].share_pct | 11.52 | usgs_mcs_2025_gold | inferred | Not stated; 380/3,300 = 11.515% ≈ 11.52% |
| production[2024].mining_by_country[RU].quantity.value | 310 tonnes_per_year | usgs_mcs_2025_gold | verified | "Russia … 310" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[RU].share_pct | 9.39 | usgs_mcs_2025_gold | inferred | Not stated; 310/3,300 = 9.394% ≈ 9.39% |
| production[2024].mining_by_country[AU].quantity.value | 290 tonnes_per_year | usgs_mcs_2025_gold | verified | "Australia … 290" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[AU].share_pct | 8.79 | usgs_mcs_2025_gold | inferred | Not stated; 290/3,300 = 8.788% ≈ 8.79% |
| production[2024].mining_by_country[AU].notes (JORC reserves 4,600 t) | 4,600 t | usgs_mcs_2025_gold | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 4,600 tons" — USGS MCS 2025 p.83 footnote 11 |
| production[2024].mining_by_country[CA].quantity.value | 200 tonnes_per_year | usgs_mcs_2025_gold | verified | "Canada … 200" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[CA].share_pct | 6.06 | usgs_mcs_2025_gold | inferred | Not stated; 200/3,300 = 6.061% ≈ 6.06% |
| production[2024].mining_by_country[US].quantity.value | 160 tonnes_per_year | usgs_mcs_2025_gold | verified | "United States … 160" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[US].share_pct | 4.85 | usgs_mcs_2025_gold | inferred | Not stated; 160/3,300 = 4.848% ≈ 4.85% |
| production[2024].mining_by_country[KZ].quantity.value | 130 tonnes_per_year | usgs_mcs_2025_gold | verified | "Kazakhstan … 130" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[KZ].share_pct | 3.94 | usgs_mcs_2025_gold | inferred | Not stated; 130/3,300 = 3.939% ≈ 3.94% |
| production[2024].mining_by_country[MX].quantity.value | 130 tonnes_per_year | usgs_mcs_2025_gold | verified | "Mexico … 130" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[MX].share_pct | 3.94 | usgs_mcs_2025_gold | inferred | Not stated; 130/3,300 = 3.939% ≈ 3.94% |
| production[2024].mining_by_country[GH].quantity.value | 130 tonnes_per_year | usgs_mcs_2025_gold | verified | "Ghana … 130" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[GH].share_pct | 3.94 | usgs_mcs_2025_gold | inferred | Not stated; 130/3,300 = 3.939% ≈ 3.94% |
| production[2024].mining_by_country[UZ].quantity.value | 120 tonnes_per_year | usgs_mcs_2025_gold | verified | "Uzbekistan … 120" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[UZ].share_pct | 3.64 | usgs_mcs_2025_gold | inferred | Not stated; 120/3,300 = 3.636% ≈ 3.64% |
| production[2024].mining_by_country[ID].quantity.value | 100 tonnes_per_year | usgs_mcs_2025_gold | verified | "Indonesia … e100 … 100" — USGS MCS 2025 p.83 World Mine Production table, 2024e column (e = estimated) |
| production[2024].mining_by_country[ID].share_pct | 3.03 | usgs_mcs_2025_gold | inferred | Not stated; 100/3,300 = 3.030% ≈ 3.03% |
| production[2024].mining_by_country[PE].quantity.value | 100 tonnes_per_year | usgs_mcs_2025_gold | verified | "Peru … 100" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[PE].share_pct | 3.03 | usgs_mcs_2025_gold | inferred | Not stated; 100/3,300 = 3.030% ≈ 3.03% |
| production[2024].mining_by_country[ZA].quantity.value | 100 tonnes_per_year | usgs_mcs_2025_gold | verified | "South Africa … 100" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[ZA].share_pct | 3.03 | usgs_mcs_2025_gold | inferred | Not stated; 100/3,300 = 3.030% ≈ 3.03% |
| production[2024].mining_by_country[BR].quantity.value | 70 tonnes_per_year | usgs_mcs_2025_gold | verified | "Brazil … 70" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[BR].share_pct | 2.12 | usgs_mcs_2025_gold | inferred | Not stated; 70/3,300 = 2.121% ≈ 2.12% |
| production[2024].mining_by_country[ML].quantity.value | 70 tonnes_per_year | usgs_mcs_2025_gold | verified | "Mali … e67 … 70" — USGS MCS 2025 p.83 World Mine Production table, 2024e column (e = estimated for 2023) |
| production[2024].mining_by_country[ML].share_pct | 2.12 | usgs_mcs_2025_gold | inferred | Not stated; 70/3,300 = 2.121% ≈ 2.12% |
| production[2024].mining_by_country[BF].quantity.value | 60 tonnes_per_year | usgs_mcs_2025_gold | verified | "Burkina Faso … 60" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[BF].share_pct | 1.82 | usgs_mcs_2025_gold | inferred | Not stated; 60/3,300 = 1.818% ≈ 1.82% |
| production[2024].mining_by_country[CO].quantity.value | 60 tonnes_per_year | usgs_mcs_2025_gold | verified | "Colombia … 60" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[CO].share_pct | 1.82 | usgs_mcs_2025_gold | inferred | Not stated; 60/3,300 = 1.818% ≈ 1.82% |
| production[2024].mining_by_country[TZ].quantity.value | 60 tonnes_per_year | usgs_mcs_2025_gold | verified | "Tanzania … 60" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[TZ].share_pct | 1.82 | usgs_mcs_2025_gold | inferred | Not stated; 60/3,300 = 1.818% ≈ 1.82% |
| production[2024].mining_by_country[ZZ].quantity.value | 780 tonnes_per_year | usgs_mcs_2025_gold | verified | "Other countries … 780" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| production[2024].mining_by_country[ZZ].share_pct | 23.64 | usgs_mcs_2025_gold | inferred | Not stated; 780/3,300 = 23.636% ≈ 23.64% |
| reserves.economic_reserves.value | 64,000 tonnes | usgs_mcs_2025_gold | verified | "World total (rounded) … 64,000" — USGS MCS 2025 p.83 World Mine Production table, Reserves column |
| reserves.resources.value | 33,000 tonnes | usgs_mcs_2025_gold | verified | "An assessment of U.S. gold resources indicated 33,000 tons of gold" — USGS MCS 2025 p.83 World Resources |
| reserves.resources.notes (15,000 t identified) | 15,000 tonnes | usgs_mcs_2025_gold | verified | "15,000 tons in identified … resources" — USGS MCS 2025 p.83 World Resources |
| reserves.resources.notes (18,000 t undiscovered) | 18,000 tonnes | usgs_mcs_2025_gold | verified | "18,000 tons in undiscovered resources" — USGS MCS 2025 p.83 World Resources |
| reserves.resources.notes (nearly one-quarter in porphyry copper) | ~25% | usgs_mcs_2025_gold | verified | "Nearly one-quarter of the gold in undiscovered resources was estimated to be contained in porphyry copper deposits" — USGS MCS 2025 p.83 World Resources |
| reserves.notes (named country reserves sum) | 64,200 t | usgs_mcs_2025_gold | discrepancy | Stated in YAML notes as 64,200 t; arithmetic sum of 16 named countries + Other from the USGS table = 64,400 t (AU12,000+RU12,000+ZA5,000+ID3,600+CA3,200+CN3,100+US3,000+PE2,500+BR2,400+KZ2,300+UZ1,800+MX1,400+GH1,000+ML800+CO700+TZ400+ZZ9,200 = 64,400); world total stated as 64,000 t (rounded) — USGS MCS 2025 p.83 |
| reserves.reserves_by_country[AU].quantity.value | 12,000 tonnes | usgs_mcs_2025_gold | verified | "Australia … 12,000" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[AU].share_pct | 18.75 | usgs_mcs_2025_gold | inferred | Not stated; 12,000/64,000 = 18.75% |
| reserves.reserves_by_country[AU].notes (JORC 4,600 t) | 4,600 tonnes | usgs_mcs_2025_gold | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 4,600 tons" — USGS MCS 2025 p.83 footnote 11 |
| reserves.reserves_by_country[RU].quantity.value | 12,000 tonnes | usgs_mcs_2025_gold | verified | "Russia … 12,000" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 18.75 | usgs_mcs_2025_gold | inferred | Not stated; 12,000/64,000 = 18.75% |
| reserves.reserves_by_country[ZA].quantity.value | 5,000 tonnes | usgs_mcs_2025_gold | verified | "South Africa … 5,000" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[ZA].share_pct | 7.81 | usgs_mcs_2025_gold | inferred | Not stated; 5,000/64,000 = 7.813% ≈ 7.81% |
| reserves.reserves_by_country[ID].quantity.value | 3,600 tonnes | usgs_mcs_2025_gold | verified | "Indonesia … 3,600" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[ID].share_pct | 5.63 | usgs_mcs_2025_gold | inferred | Not stated; 3,600/64,000 = 5.625% ≈ 5.63% |
| reserves.reserves_by_country[CA].quantity.value | 3,200 tonnes | usgs_mcs_2025_gold | verified | "Canada … 3,200" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[CA].share_pct | 5.00 | usgs_mcs_2025_gold | inferred | Not stated; 3,200/64,000 = 5.00% |
| reserves.reserves_by_country[CN].quantity.value | 3,100 tonnes | usgs_mcs_2025_gold | verified | "China … 3,100" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 4.84 | usgs_mcs_2025_gold | inferred | Not stated; 3,100/64,000 = 4.844% ≈ 4.84% |
| reserves.reserves_by_country[US].quantity.value | 3,000 tonnes | usgs_mcs_2025_gold | verified | "United States … 3,000" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[US].share_pct | 4.69 | usgs_mcs_2025_gold | inferred | Not stated; 3,000/64,000 = 4.688% ≈ 4.69% |
| reserves.reserves_by_country[PE].quantity.value | 2,500 tonnes | usgs_mcs_2025_gold | verified | "Peru … 2,500" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[PE].share_pct | 3.91 | usgs_mcs_2025_gold | inferred | Not stated; 2,500/64,000 = 3.906% ≈ 3.91% |
| reserves.reserves_by_country[BR].quantity.value | 2,400 tonnes | usgs_mcs_2025_gold | verified | "Brazil … 2,400" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 3.75 | usgs_mcs_2025_gold | inferred | Not stated; 2,400/64,000 = 3.75% |
| reserves.reserves_by_country[KZ].quantity.value | 2,300 tonnes | usgs_mcs_2025_gold | verified | "Kazakhstan … 2,300" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[KZ].share_pct | 3.59 | usgs_mcs_2025_gold | inferred | Not stated; 2,300/64,000 = 3.594% ≈ 3.59% |
| reserves.reserves_by_country[UZ].quantity.value | 1,800 tonnes | usgs_mcs_2025_gold | verified | "Uzbekistan … 1,800" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[UZ].share_pct | 2.81 | usgs_mcs_2025_gold | inferred | Not stated; 1,800/64,000 = 2.813% ≈ 2.81% |
| reserves.reserves_by_country[MX].quantity.value | 1,400 tonnes | usgs_mcs_2025_gold | verified | "Mexico … 1,400" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[MX].share_pct | 2.19 | usgs_mcs_2025_gold | inferred | Not stated; 1,400/64,000 = 2.188% ≈ 2.19% |
| reserves.reserves_by_country[GH].quantity.value | 1,000 tonnes | usgs_mcs_2025_gold | verified | "Ghana … 1,000" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[GH].share_pct | 1.56 | usgs_mcs_2025_gold | inferred | Not stated; 1,000/64,000 = 1.563% ≈ 1.56% |
| reserves.reserves_by_country[ML].quantity.value | 800 tonnes | usgs_mcs_2025_gold | verified | "Mali … 800" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[ML].share_pct | 1.25 | usgs_mcs_2025_gold | inferred | Not stated; 800/64,000 = 1.25% |
| reserves.reserves_by_country[CO].quantity.value | 700 tonnes | usgs_mcs_2025_gold | verified | "Colombia … 700" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[CO].share_pct | 1.09 | usgs_mcs_2025_gold | inferred | Not stated; 700/64,000 = 1.094% ≈ 1.09% |
| reserves.reserves_by_country[TZ].quantity.value | 400 tonnes | usgs_mcs_2025_gold | verified | "Tanzania … 400" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[TZ].share_pct | 0.63 | usgs_mcs_2025_gold | inferred | Not stated; 400/64,000 = 0.625% ≈ 0.63% |
| reserves.reserves_by_country[ZZ].quantity.value | 9,200 tonnes | usgs_mcs_2025_gold | verified | "Other countries … 9,200" — USGS MCS 2025 p.83 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 14.38 | usgs_mcs_2025_gold | inferred | Not stated; 9,200/64,000 = 14.375% ≈ 14.38% |
| end_uses.uses[jewelry].share_pct | 45 | usgs_mcs_2025_gold | verified | "in jewelry, 45%" — USGS MCS 2025 p.83 Events (World Gold Council data, footnote 3 and 9) |
| end_uses.uses[central_bank_and_institutional].share_pct | 21 | usgs_mcs_2025_gold | verified | "central banks and other institutions, 21%" — USGS MCS 2025 p.83 Events |
| end_uses.uses[physical_investment_bars].share_pct | 19 | usgs_mcs_2025_gold | verified | "physical bars, 19%" — USGS MCS 2025 p.83 Events |
| end_uses.uses[coins_and_medals].share_pct | 7 | usgs_mcs_2025_gold | verified | "official coins and medals and imitation coins, 7%" — USGS MCS 2025 p.83 Events |
| end_uses.uses[electrical_and_electronics].share_pct | 6 | usgs_mcs_2025_gold | verified | "electrical and electronics, 6%" — USGS MCS 2025 p.83 Events |
| end_uses.uses[other_industrial].share_pct | 2 | usgs_mcs_2025_gold | discrepancy | Source states "other, 1%" — USGS MCS 2025 p.83 Events; YAML field value is 2, but the notes within the same entry correctly state "other: 1%"; source total sums to 99% (rounding); YAML field should be 1, not 2 |
| end_uses.uses[jewelry].notes (jewelry -7%, first 9 months 2024) | -7% | usgs_mcs_2025_gold | verified | "jewelry decreased by 7% compared with those in the first 9 months of 2023" — USGS MCS 2025 p.83 |
| end_uses.uses[electrical_and_electronics].notes (electronics +12%) | +12% | usgs_mcs_2025_gold | verified | "electronics increased by 12%" — USGS MCS 2025 p.83 |
| end_uses.uses[other_industrial].notes (other unchanged) | unchanged | usgs_mcs_2025_gold | verified | "other industrial applications were unchanged" — USGS MCS 2025 p.83 |
| end_uses.uses[other_industrial].notes (dentistry -5%) | -5% | usgs_mcs_2025_gold | verified | "dentistry decreased by 5%" — USGS MCS 2025 p.83 |
| end_uses.uses[physical_investment_bars].notes (bars +12%) | +12% | usgs_mcs_2025_gold | verified | "global consumption of gold in physical bars increased by 12%" — USGS MCS 2025 p.83 |
| end_uses.uses[coins_and_medals].notes (coins -25%) | -25% | usgs_mcs_2025_gold | verified | "coins and medals decreased by 25%" — USGS MCS 2025 p.83 |
| end_uses.uses[central_bank_and_institutional].notes (CB -17%) | -17% | usgs_mcs_2025_gold | verified | "gold holdings in central banks decreased by 17%" — USGS MCS 2025 p.83 |
| end_uses.uses[central_bank_and_institutional].notes (ETF -87%) | -87% | usgs_mcs_2025_gold | verified | "global investments in gold-based exchange-traded funds and similar investments decreased by 87%" — USGS MCS 2025 p.83 footnote 9 |
| end_uses.uses[other_industrial].notes (total global -3%) | -3% | usgs_mcs_2025_gold | verified | "Total global consumption in the first 9 months of 2024 decreased by 3% compared with that in the first 9 months of 2023" — USGS MCS 2025 p.83 footnote 9 |
| prices[2024].value | 2,400 USD/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 2,400" — USGS MCS 2025 p.82 Salient Statistics, 2024e column |
| prices[2023].value | 1,945 USD/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 1,945" — USGS MCS 2025 p.82 Salient Statistics, 2023 column |
| prices[2022].value | 1,802 USD/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 1,802" — USGS MCS 2025 p.82 Salient Statistics, 2022 column |
| prices[2021].value | 1,801 USD/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 1,801" — USGS MCS 2025 p.82 Salient Statistics, 2021 column |
| prices[2020].value | 1,774 USD/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 1,774" — USGS MCS 2025 p.82 Salient Statistics, 2020 column |
| prices[2024].notes (23% increase from 2023) | 23% | usgs_mcs_2025_gold | verified | "The estimated gold price in 2024 increased by 23%" — USGS MCS 2025 p.82 Events |
| prices[2024].notes (new record-high annual average) | new record | usgs_mcs_2025_gold | verified | "reached a new record-high annual price compared with the previous record-high annual price in 2023" — USGS MCS 2025 p.82 Events |
| prices[2024].notes (Q1 increasing, Q2 decreasing, Q3/Q4 increasing) | Q trend | usgs_mcs_2025_gold | verified | "fluctuated with an increasing trend in the first quarter, a decreasing trend into the second quarter, and an increasing trend into the beginning of the fourth quarter" — USGS MCS 2025 p.82 Events |
| feedstock_origins[copper_ore_byproduct].notes (~7% byproduct) | ~7% | usgs_mcs_2025_gold | verified | "About 7% of domestic gold was recovered as a byproduct of processing domestic base-metal ores, chiefly copper ores" — USGS MCS 2025 p.82 |
| feedstock_origins[gold_silver_dore].notes (Mexico 38%) | 38% | usgs_mcs_2025_gold | verified | "Dore: Mexico, 38%" — USGS MCS 2025 p.82 Import Sources (2020–23) |
| feedstock_origins[gold_silver_dore].notes (Colombia 20%) | 20% | usgs_mcs_2025_gold | verified | "Colombia, 20%" — USGS MCS 2025 p.82 Import Sources (2020–23) |
| feedstock_origins[gold_silver_dore].notes (Argentina 12%) | 12% | usgs_mcs_2025_gold | verified | "Argentina, 12%" — USGS MCS 2025 p.82 Import Sources (2020–23) |
| feedstock_origins[gold_silver_dore].notes (Nicaragua 8%) | 8% | usgs_mcs_2025_gold | verified | "Nicaragua, 8%" — USGS MCS 2025 p.82 Import Sources (2020–23) |
| feedstock_origins[gold_silver_dore].notes (other 22%) | 22% | usgs_mcs_2025_gold | verified | "and other, 22%" — USGS MCS 2025 p.82 Import Sources (2020–23) |
| feedstock_origins[gold_scrap].notes (~90 t scrap 2024) | ~90 t | usgs_mcs_2025_gold | verified | "an estimated 90 tons of new and old scrap was recycled" — USGS MCS 2025 p.82 Recycling |
| feedstock_origins[gold_scrap].notes (~45% US consumption from scrap) | ~45% | usgs_mcs_2025_gold | verified | "equivalent to about 45% of reported consumption" — USGS MCS 2025 p.82 Recycling |
| substitutes[electrical_and_electronic_contacts].notes (base metals clad with gold in electrical/electronic) | qualitative | usgs_mcs_2025_gold | verified | "Base metals clad with gold alloys are widely used to economize on gold in electrical and electronic products" — USGS MCS 2025 p.83 Substitutes |
| substitutes[jewelry].notes (base metals clad with gold in jewelry) | qualitative | usgs_mcs_2025_gold | verified | "Base metals clad with gold alloys are widely used to economize on gold in jewelry" — USGS MCS 2025 p.83 Substitutes |
| substitutes[general_industrial].notes (palladium, platinum, silver substitutes) | qualitative | usgs_mcs_2025_gold | verified | "Generally, palladium, platinum, and silver may substitute for gold" — USGS MCS 2025 p.83 Substitutes |
| geopolitical_events[0].event (record-high $2,400) | $2,400/troy oz | usgs_mcs_2025_gold | verified | "Price, dollars per troy ounce … 2,400" — USGS MCS 2025 p.82 Salient Statistics, 2024e |
| geopolitical_events[0].impact (23% above prior record $1,945) | 23%; $1,945 | usgs_mcs_2025_gold | verified | "increased by 23%"; "Price … 1,945" (2023) — USGS MCS 2025 p.82 |
| geopolitical_events[0].impact (Q trend: Q1 rising, Q2 falling, Q4 rising) | Q trend | usgs_mcs_2025_gold | verified | "increasing trend in the first quarter, a decreasing trend into the second quarter, and an increasing trend into the beginning of the fourth quarter" — USGS MCS 2025 p.82 Events |
| geopolitical_events[1].impact (ETF -87%) | -87% | usgs_mcs_2025_gold | verified | "global investments in gold-based exchange-traded funds and similar investments decreased by 87%" — USGS MCS 2025 p.83 footnote 9 |
| geopolitical_events[1].impact (CB holdings -17%) | -17% | usgs_mcs_2025_gold | verified | "gold holdings in central banks decreased by 17%" — USGS MCS 2025 p.83 |
| geopolitical_events[1].impact (bars +12%) | +12% | usgs_mcs_2025_gold | verified | "global consumption of gold in physical bars increased by 12%" — USGS MCS 2025 p.83 |
| geopolitical_events[1].impact (electronics +12%) | +12% | usgs_mcs_2025_gold | verified | "electronics increased by 12%" — USGS MCS 2025 p.83 |
| geopolitical_events[2].event (world mine production 3,300 t) | 3,300 t | usgs_mcs_2025_gold | verified | "World total (rounded) … 3,300" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (world production 3,250 t in 2023) | 3,250 t | usgs_mcs_2025_gold | verified | "World total (rounded) … 3,250" — USGS MCS 2025 p.83 World Mine Production table, 2023 column |
| geopolitical_events[2].impact (China 380 t) | 380 t | usgs_mcs_2025_gold | verified | "China … 380" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (Russia 310 t) | 310 t | usgs_mcs_2025_gold | verified | "Russia … 310" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (Australia 290 t) | 290 t | usgs_mcs_2025_gold | verified | "Australia … 290" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (Canada 200 t) | 200 t | usgs_mcs_2025_gold | verified | "Canada … 200" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (US 160 t) | 160 t | usgs_mcs_2025_gold | verified | "United States … 160" — USGS MCS 2025 p.83 World Mine Production table, 2024e column |
| geopolitical_events[2].impact (top 5 = 41%) | 41% | usgs_mcs_2025_gold | verified | "together accounted for 41% of estimated global production in 2024" — USGS MCS 2025 p.82 Events |
| geopolitical_events[3].impact (US mine 170 t in 2023) | 170 t | usgs_mcs_2025_gold | verified | "United States … 170" — USGS MCS 2025 p.83 World Mine Production table, 2023 column |
| geopolitical_events[3].impact (US mine 160 t in 2024e) | 160 t | usgs_mcs_2025_gold | verified | "Mine … 160" — USGS MCS 2025 p.82 Salient Statistics, 2024e column |
| geopolitical_events[3].impact (193 t in 2020) | 193 t | usgs_mcs_2025_gold | verified | "Mine … 193" — USGS MCS 2025 p.82 Salient Statistics, 2020 column |
| geopolitical_events[3].impact (value $12 billion, +9%) | $12 billion; +9% | usgs_mcs_2025_gold | verified | "the value was estimated to be $12 billion, a 9% increase from the value in 2023" — USGS MCS 2025 p.82 |
| geopolitical_events[3].impact (employment ~12,000, 2024e) | ~12,000 | usgs_mcs_2025_gold | verified | "Employment, mine and mill, number … 12,000" — USGS MCS 2025 p.82 Salient Statistics, 2024e column |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_gold | inferred | Not stated in USGS MCS 2025 gold chapter; gold does not appear in the 2022 USGS Critical Minerals List (50 minerals); absence from chapter's context confirms non-critical status |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_gold | inferred | Not stated in USGS MCS 2025 gold chapter; gold is not included in the EU CRM 2023 list per general regulatory reference; source does not address EU criticality |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_gold | inferred | Not stated in USGS MCS 2025 gold chapter; gold is not listed in EU CRMA 2024 strategic raw materials; source does not address EU strategic status |

## Notes

- **Source coverage**: All numeric claims in Au.yaml trace to USGS MCS 2025 gold chapter (pp.82–83). The source PDF was downloaded and extracted cleanly via pdftotext -layout. No claims require the secondary World Gold Council source beyond what is already quoted through USGS footnotes 3 and 9.
- **Discrepancy 1 — other_industrial share_pct**: The YAML field `end_uses.uses[other_industrial].share_pct` is set to 2, but the source explicitly states "other, 1%". The notes within the same YAML entry correctly quote "other: 1%", indicating the field value was likely manually adjusted to make the six categories sum to 100% (45+21+19+7+6+2=100), whereas the source data sum is 99% (45+21+19+7+6+1=99), a rounding artifact common in the WGC demand data. The field should be corrected to 1 in a follow-up pass.
- **Discrepancy 2 — reserves sum arithmetic**: The YAML notes claim "Named country reserves sum to 64,200 t" but the arithmetic sum of the 16 named countries + Other countries from the USGS table is 64,400 t (not 64,200 t). The world total of 64,000 t is explicitly labelled "(rounded)" in USGS, so the ~400 t overage is within expected rounding; the stated 64,200 figure is simply an arithmetic error in the notes text.
- **End-use percentages**: Per project notes and USGS footnotes 3 and 9, the end-use percentages are **global** figures sourced from World Gold Council, not US domestic. This is consistent with the YAML notes and project context.
- **Net import reliance**: The Salient Statistics table shows "E" (Net exporter) for 2021–2024e and "(8)" for 2020. Footnote 8 explains the 2020 value is suppressed due to large unreported investor stock purchases. This is consistent with YAML criticality notes describing the US as a net exporter.
- **Australia JORC vs USGS reserves**: The USGS reports Australia reserves as 12,000 t in USGS format; footnote 11 notes JORC-compliant reserves were 4,600 t. Both figures are cited in the YAML and verified.
- **Criticality flags**: No source_id is assigned to criticality fields in the YAML. Flags are marked inferred based on absence of gold from the USGS MCS 2025 critical minerals context and general regulatory knowledge. A dedicated critical-minerals list fetch would be needed for full verification.
- **Bullion import sources** (narrative): Switzerland 35%, Canada 27%, South Africa 8%, Australia 7% — verified from Import Sources section p.82: "Bullion: Switzerland, 35%; Canada, 27%; South Africa, 8%; Australia, 7%; and other, 23%."

## ZZ-bucket decomposition (2026-04-14)

Per `atlas/zz-decomposition-plan.md`, the USGS "Other countries" residual (780 t / 23.64% of 2024 world production) was decomposed using secondary sources. Thirteen producers were named at a naming threshold of **≥1% of world production OR ≥2 authoritative secondary sources at material tonnage**. New named shares reallocate ~553 t out of the 780 t ZZ bucket, leaving ~227 t / 6.87% in the residual row.

| Country | ISO2 | 2024 t | share_pct | Confidence | Primary source | Corroborating source |
|---|---|---|---|---|---|---|
| Sudan | SD | 64 | 1.94 | medium | `sudan_tribune_smrc_2024_gold` (SMRC official) | SWISSAID African Gold 2024 (70–90 t inc. informal) |
| Côte d'Ivoire | CI | 58 | 1.76 | high | `mining_com_cote_divoire_2024_gold` | Endeavour Mining corporate disclosures (Lafigué first pour 2024) |
| Guinea | GN | 55 | 1.67 | medium | `usgs_myb_guinea_2023_gold` | AngloGold Siguiri disclosures; West Africa aggregate coverage |
| Argentina | AR | 53 | 1.61 | high | `panorama_minero_argentina_2024_gold` | BN Americas / Barrick Veladero 2024 results |
| Venezuela | VE | 50 | 1.52 | low | `icg_venezuela_gold_2025` (central estimate) | US State Dept Congressional Report 2024 (~75 t, 2021); OECD (25–37.5 t). Wide range; sanctions opacity. |
| Papua New Guinea | PG | 45 | 1.36 | medium | `newmont_fy2024_results` (Lihir 19.1 t) | Statista PNG historical series; Barrick/Zijin Porgera restart; K92 Kainantu |
| Chile | CL | 42 | 1.27 | medium | `ey_chile_mining_2025` | GBR Chile Mining 2024; Gold Fields Salares Norte first-pour 2024 |
| Bolivia | BO | 40 | 1.21 | medium | `ceic_bolivia_gold_2024` | InsightCrime analytical coverage (ASM, informal flows to UAE/India) |
| Zimbabwe | ZW | 37 | 1.12 | high | `pindula_fidelity_zimbabwe_2024` (Fidelity Gold Refineries, sole buyer) | EquityAxis corroborating coverage |
| Philippines | PH | 32 | 0.97 | medium | `mgb_philippines_metallic_2024` | CEIC Philippines gold series (31.0 t 2023 baseline). Below 1% floor; admitted on 2-source rule. |
| DR Congo | CD | 28 | 0.85 | medium | `ecofin_kibali_drc_2024` (Kibali 21.3 t formal) | SWISSAID Africa gold 2024 (formal captures <20% of real output). Below 1% floor; admitted on 2-source rule. |
| Dominican Republic | DO | 26 | 0.79 | high | `barrick_pueblo_viejo_2024` | Mining Weekly / Barrick Q4 2024 results; Phase 1 expansion commercial Q3 2024. Below 1% floor; admitted on 2-source rule. |
| Turkey | TR | 23 | 0.70 | medium | `nordic_monitor_turkey_gold_2024` | WGC Q3 2024 supply. Çöpler offline all of 2024 (~6–7 t removed). Below 1% floor; admitted on 2-source rule. |

**Sum of new named shares:** 553 t / 16.77% of world. **New ZZ residual:** 227 t / 6.87%.

**Non-qualifying countries (researched but kept in ZZ):** Kyrgyzstan (~22 t), Suriname (~32 t; right at threshold but formal/ASM split is ambiguous), Ecuador (~18 t, Lundin Fruta del Norte 15.6 t), Mongolia (~13 t), Egypt (~15 t, Sukari-dominated), Saudi Arabia (~14 t, Ma'aden), Tajikistan (~14 t, Zarafshon), Nicaragua (~14 t, Calibre + Equinox), Guyana (~13.5 t), Ethiopia (~15–25 t calendar 2024 vs 37 t FY 2024/25 — the step-change happened H2 2024 post-FX reform), Senegal (~10 t, Endeavour Sabodala-Massawa), Eritrea (~4 t), Niger (~2.4 t), North Korea (~1–2 t).

**Caveats:**
- **Sudan, Venezuela, DR Congo** figures are formal/official. SWISSAID, ICG, and US State Department analyses indicate real totals including smuggled/ASM flows are materially higher — in DRC's case, by 3–5× (SWISSAID: formal captures <20% of real). These rows carry `confidence: medium` (SD, CD) or `low` (VE) and their notes describe the informal picture.
- **Côte d'Ivoire (58 t) is the single biggest omission from the USGS MCS 2025 named list** — it now exceeds Tanzania, Burkina Faso, and Colombia (all USGS-named at 60 t).
- **Argentina, Papua New Guinea, and Chile** are borderline on the 33-t threshold and would historically have been USGS-named; their exclusion from the USGS MCS 2025 named list is notable.
- **Ethiopia** sits awkwardly between calendar and fiscal-year reporting: FY2024/25 (July 2024 – June 2025) is ~37 t, but calendar-2024 is closer to ~15–25 t. Kept in ZZ rather than split the difference.

**Methodology:** `atlas/zz-decomposition-plan.md` (pilot element, 2026-04-14).


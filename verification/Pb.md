# Verification: Pb

- Element: lead (Pb)
- Snapshot year: 2025
- Verifier: worker-8180d1ec5f9e (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 93 |
| discrepancy | 0 |
| inferred | 35 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[mine].mine.value | 4,300,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "World total (rounded) … 4,300" — USGS MCS 2025 p.107 World Mine Production table, 2024e column (thousand metric tons lead content) |
| production[mine].mine.notes (2023 world total 4,370 kt) | 4,370 kt | usgs_mcs_2025_lead | verified | "World total (rounded) … 4,370" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mine.notes (sum of countries = 4,340 kt) | 4,340 kt | usgs_mcs_2025_lead | inferred | Not stated; arithmetic sum of 13 country rows (2024e): 300+430+60+1,900+220+60+180+270+220+70+40+70+520 = 4,340 kt |
| production[mine].mine.notes (US recoverable lead 290 kt 2024e) | 290 kt | usgs_mcs_2025_lead | verified | "Mine, recoverable lead … 290" — USGS MCS 2025 p.106 Salient Statistics, 2024e column |
| production[mine].mine.notes (up 10% from 263 kt in 2023) | 10%; 263 kt | usgs_mcs_2025_lead | verified | "domestic mine production of recoverable lead increased by 10% from that in 2023" — p.107 Events; "Mine, recoverable lead … 263" p.106 Salient Statistics 2023 column |
| production[mine].mine.notes (US lead in concentrates 300 kt) | 300 kt | usgs_mcs_2025_lead | verified | "Mine, lead in concentrates … 300" — USGS MCS 2025 p.106 Salient Statistics, 2024e column; consistent with world mine table US row |
| production[mine].mine.notes (last primary refinery closed 2013) | 2013 | usgs_mcs_2025_lead | verified | "Nearly all lead concentrate production has been exported since the last primary lead refinery closed in 2013" — p.106 Domestic Production and Use |
| production[mine].mine.notes (US value $670 million 2024) | ~$670 million | usgs_mcs_2025_lead | verified | "The value of recoverable lead from ore mined in 2024 was an estimated $670 million" — p.106 Domestic Production and Use |
| production[mine].mine.notes (net import reliance 28% 2024e) | 28% | usgs_mcs_2025_lead | verified | "Net import reliance … 28" — USGS MCS 2025 p.106 Salient Statistics, 2024e column |
| production[mine].mine.notes (down from 33% in 2023) | 33% | usgs_mcs_2025_lead | verified | "Net import reliance … 33" — USGS MCS 2025 p.106 Salient Statistics, 2023 column |
| production[mine].mine.notes (Canada 32% of refined imports 2020–23) | 32% | usgs_mcs_2025_lead | verified | "Refined metal: Canada, 32%" — USGS MCS 2025 p.106 Import Sources (2020–23) |
| production[mine].mine.notes (Republic of Korea 16%) | 16% | usgs_mcs_2025_lead | verified | "Republic of Korea, 16%" — USGS MCS 2025 p.106 Import Sources (2020–23) |
| production[mine].mine.notes (Mexico 14%) | 14% | usgs_mcs_2025_lead | verified | "Mexico, 14%" — USGS MCS 2025 p.106 Import Sources (2020–23) |
| production[mine].mine.notes (Australia 11%) | 11% | usgs_mcs_2025_lead | verified | "Australia, 11%; and other, 27%" — USGS MCS 2025 p.106 Import Sources (2020–23) |
| production[mine].mining_by_country[CN].quantity.value | 1,900,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "China … 1,900" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[CN].share_pct | 44.19 | usgs_mcs_2025_lead | inferred | Not stated; 1,900/4,300 = 44.19% |
| production[mine].mining_by_country[CN].notes (2023 = 1,960 kt) | 1,960 kt | usgs_mcs_2025_lead | verified | "China … 1,960" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[AU].quantity.value | 430,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Australia … 430" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[AU].share_pct | 10.00 | usgs_mcs_2025_lead | inferred | Not stated; 430/4,300 = 10.00% exactly |
| production[mine].mining_by_country[AU].notes (2023 = 430 kt unchanged) | 430 kt | usgs_mcs_2025_lead | verified | "Australia … 430" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[US].quantity.value | 300,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "United States … 300" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[US].share_pct | 6.98 | usgs_mcs_2025_lead | inferred | Not stated; 300/4,300 = 6.977% ≈ 6.98% |
| production[mine].mining_by_country[US].notes (2023 US = 270 kt lead in concentrates) | 270 kt | usgs_mcs_2025_lead | verified | "United States … 270" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[US].notes (recoverable lead 290 kt) | 290 kt | usgs_mcs_2025_lead | verified | "Mine, recoverable lead … 290" — USGS MCS 2025 p.106 Salient Statistics, 2024e column |
| production[mine].mining_by_country[US].notes (value $670 million) | ~$670 million | usgs_mcs_2025_lead | verified | "The value of recoverable lead from ore mined in 2024 was an estimated $670 million" — p.106 |
| production[mine].mining_by_country[PE].quantity.value | 270,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Peru … 270" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[PE].share_pct | 6.28 | usgs_mcs_2025_lead | inferred | Not stated; 270/4,300 = 6.279% ≈ 6.28% |
| production[mine].mining_by_country[PE].notes (2023 = 273 kt) | 273 kt | usgs_mcs_2025_lead | verified | "Peru … 273" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[RU].quantity.value | 220,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Russia … 220" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[RU].share_pct | 5.12 | usgs_mcs_2025_lead | inferred | Not stated; 220/4,300 = 5.116% ≈ 5.12% |
| production[mine].mining_by_country[RU].notes (2023 = 218 kt) | 218 kt | usgs_mcs_2025_lead | verified | "Russia … e218" — USGS MCS 2025 p.107 World Mine Production table, 2023 column (estimated) |
| production[mine].mining_by_country[IN].quantity.value | 220,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "India … 220" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[IN].share_pct | 5.12 | usgs_mcs_2025_lead | inferred | Not stated; 220/4,300 = 5.116% ≈ 5.12% |
| production[mine].mining_by_country[IN].notes (2023 = 226 kt) | 226 kt | usgs_mcs_2025_lead | verified | "India … 226" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[MX].quantity.value | 180,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Mexico … 180" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[MX].share_pct | 4.19 | usgs_mcs_2025_lead | inferred | Not stated; 180/4,300 = 4.186% ≈ 4.19% |
| production[mine].mining_by_country[MX].notes (2023 = 183 kt) | 183 kt | usgs_mcs_2025_lead | verified | "Mexico … 183" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[MX].notes (14% of US refined imports) | 14% | usgs_mcs_2025_lead | verified | "Mexico, 14%" — USGS MCS 2025 p.106 Import Sources (2020–23) |
| production[mine].mining_by_country[TR].quantity.value | 70,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Turkey … 70" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[TR].share_pct | 1.63 | usgs_mcs_2025_lead | inferred | Not stated; 70/4,300 = 1.628% ≈ 1.63% |
| production[mine].mining_by_country[TR].notes (2023 = 68 kt) | 68 kt | usgs_mcs_2025_lead | verified | "Turkey … e68" — USGS MCS 2025 p.107 World Mine Production table, 2023 column (estimated) |
| production[mine].mining_by_country[SE].quantity.value | 70,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Sweden … 70" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[SE].share_pct | 1.63 | usgs_mcs_2025_lead | inferred | Not stated; 70/4,300 = 1.628% ≈ 1.63% |
| production[mine].mining_by_country[SE].notes (2023 = 72 kt) | 72 kt | usgs_mcs_2025_lead | verified | "Sweden … 72" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[BO].quantity.value | 60,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Bolivia … 60" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[BO].share_pct | 1.40 | usgs_mcs_2025_lead | inferred | Not stated; 60/4,300 = 1.395% ≈ 1.40% |
| production[mine].mining_by_country[BO].notes (2023 = 60 kt unchanged) | 60 kt | usgs_mcs_2025_lead | verified | "Bolivia … 60" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[mine].mining_by_country[IR].quantity.value | 60,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Iran … 60" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[IR].share_pct | 1.40 | usgs_mcs_2025_lead | inferred | Not stated; 60/4,300 = 1.395% ≈ 1.40% |
| production[mine].mining_by_country[IR].notes (2023 = 60 kt unchanged) | 60 kt | usgs_mcs_2025_lead | verified | "Iran … e60" — USGS MCS 2025 p.107 World Mine Production table, 2023 column (estimated) |
| production[mine].mining_by_country[TJ].quantity.value | 40,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Tajikistan … 40" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[TJ].share_pct | 0.93 | usgs_mcs_2025_lead | inferred | Not stated; 40/4,300 = 0.930% ≈ 0.93% |
| production[mine].mining_by_country[TJ].notes (2023 = 39 kt) | 39 kt | usgs_mcs_2025_lead | verified | "Tajikistan … e39" — USGS MCS 2025 p.107 World Mine Production table, 2023 column (estimated) |
| production[mine].mining_by_country[TJ].notes (reserves = NA) | NA | usgs_mcs_2025_lead | verified | "Tajikistan … NA" — USGS MCS 2025 p.107 Reserves column |
| production[mine].mining_by_country[ZZ].quantity.value | 520,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "Other countries … 520" — USGS MCS 2025 p.107 World Mine Production table, 2024e column |
| production[mine].mining_by_country[ZZ].share_pct | 12.09 | usgs_mcs_2025_lead | inferred | Not stated; 520/4,300 = 12.093% ≈ 12.09% |
| production[mine].mining_by_country[ZZ].notes (2023 = 511 kt) | 511 kt | usgs_mcs_2025_lead | verified | "Other countries … 511" — USGS MCS 2025 p.107 World Mine Production table, 2023 column |
| production[refined].refined.value | 13,500,000 tonnes_per_year | usgs_mcs_2025_lead | verified | "global refined lead production in 2024 was forecast to increase by 2.4% to 13.5 million tons" — p.107 Events |
| production[refined].refined.notes (2.4% increase refined) | 2.4% | usgs_mcs_2025_lead | verified | "forecast to increase by 2.4% to 13.5 million tons" — p.107 Events |
| production[refined].refined.notes (global consumption 13.1 Mt) | 13.1 million tons | usgs_mcs_2025_lead | verified | "refined lead consumption to increase by 0.2% to 13.1 million tons" — p.107 Events |
| production[refined].refined.notes (0.2% consumption increase) | 0.2% | usgs_mcs_2025_lead | verified | "refined lead consumption to increase by 0.2% to 13.1 million tons" — p.107 Events |
| production[refined].refined.notes (US secondary 1,000 kt 2024e) | 1,000 kt | usgs_mcs_2025_lead | verified | "Secondary refinery, old scrap … 1,000" — USGS MCS 2025 p.106 Salient Statistics, 2024e column |
| production[refined].refined.notes (2023 secondary = 1,010 kt) | 1,010 kt | usgs_mcs_2025_lead | verified | "Secondary refinery, old scrap … 1,010" — USGS MCS 2025 p.106 Salient Statistics, 2023 column |
| production[refined].refined.notes (primary refined = zero 2020–2024) | — (zero) | usgs_mcs_2025_lead | verified | "Primary refinery … — — — — —" — USGS MCS 2025 p.106 Salient Statistics, all five year columns |
| production[refined].refined.notes (primary refinery closed 2013) | 2013 | usgs_mcs_2025_lead | verified | "last primary lead refinery closed in 2013" — p.106 Domestic Production and Use |
| production[refined].refined.notes (70% of apparent domestic consumption) | 70% | usgs_mcs_2025_lead | verified | "an amount equivalent to 70% of apparent domestic consumption" — p.106 Recycling section |
| production[refined].refined.notes (apparent consumption 1,400 kt 2024e) | 1,400 kt | usgs_mcs_2025_lead | verified | "Consumption, apparent … 1,400" — USGS MCS 2025 p.106 Salient Statistics, 2024e column |
| production[refined].refined.notes (9.2 Mt secondary global implied) | ~9.2 Mt | usgs_mcs_2025_lead | inferred | Not stated; derived as 13.5 Mt total refined minus 4.3 Mt primary mine = ~9.2 Mt secondary |
| production[refined].refined.notes (~0.4 Mt surplus implied) | ~400 kt | usgs_mcs_2025_lead | inferred | Not stated; derived as 13.5 Mt production minus 13.1 Mt consumption = 0.4 Mt |
| production[refined].refined.notes (secondary value $2.4 billion 2024) | $2.4 billion | usgs_mcs_2025_lead | verified | "The value of the secondary lead produced in 2024 was $2.4 billion" — p.106 Domestic Production and Use |
| production[refined].refined.notes (4% less than 2023) | 4% | usgs_mcs_2025_lead | verified | "4% less than that in 2023" — p.106 Domestic Production and Use |
| production[refined].refined.notes (apparent consumption -7% from 2023) | 7% | usgs_mcs_2025_lead | verified | "Estimated U.S. apparent consumption of refined lead decreased by 7% from that in 2023" — p.107 Events |
| reserves.economic_reserves.value | 96,000,000 tonnes | usgs_mcs_2025_lead | verified | "World total (rounded) … 96,000" — USGS MCS 2025 p.107 Reserves column (thousand metric tons lead content) |
| reserves.economic_reserves.notes (sum country reserves = 95,800 kt) | 95,800 kt | usgs_mcs_2025_lead | inferred | Not stated; arithmetic sum of 12 named countries + Other excl. Tajikistan (NA): 35,000+22,000+8,900+5,600+5,000+5,900+4,600+2,000+1,900+1,700+1,600+1,600 = 95,800 kt |
| reserves.economic_reserves.notes (99.8% of stated total) | 99.8% | usgs_mcs_2025_lead | inferred | Not stated; 95,800/96,000 = 99.79% ≈ 99.8% |
| reserves.resources.value | 2,000,000,000 tonnes | usgs_mcs_2025_lead | verified | "Identified world lead resources total more than 2 billion tons" — USGS MCS 2025 p.107 World Resources |
| reserves.reserves_by_country[AU].quantity.value | 35,000,000 tonnes | usgs_mcs_2025_lead | verified | "Australia … 35,000" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[AU].share_pct | 36.46 | usgs_mcs_2025_lead | inferred | Not stated; 35,000/96,000 = 36.458% ≈ 36.46% |
| reserves.reserves_by_country[AU].notes (JORC-compliant = 10 million tons) | 10 million tons | usgs_mcs_2025_lead | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 10 million tons" — p.107 footnote 7 |
| reserves.reserves_by_country[CN].quantity.value | 22,000,000 tonnes | usgs_mcs_2025_lead | verified | "China … 22,000" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 22.92 | usgs_mcs_2025_lead | inferred | Not stated; 22,000/96,000 = 22.917% ≈ 22.92% |
| reserves.reserves_by_country[CN].notes (revised based on Government report) | revised | usgs_mcs_2025_lead | verified | "Reserves for China and Russia were revised based on Government reports" — p.107 |
| reserves.reserves_by_country[RU].quantity.value | 8,900,000 tonnes | usgs_mcs_2025_lead | verified | "Russia … 8,900" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 9.27 | usgs_mcs_2025_lead | inferred | Not stated; 8,900/96,000 = 9.271% ≈ 9.27% |
| reserves.reserves_by_country[MX].quantity.value | 5,600,000 tonnes | usgs_mcs_2025_lead | verified | "Mexico … 5,600" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[MX].share_pct | 5.83 | usgs_mcs_2025_lead | inferred | Not stated; 5,600/96,000 = 5.833% ≈ 5.83% |
| reserves.reserves_by_country[PE].quantity.value | 5,000,000 tonnes | usgs_mcs_2025_lead | verified | "Peru … 5,000" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[PE].share_pct | 5.21 | usgs_mcs_2025_lead | inferred | Not stated; 5,000/96,000 = 5.208% ≈ 5.21% |
| reserves.reserves_by_country[ZZ].quantity.value | 5,900,000 tonnes | usgs_mcs_2025_lead | verified | "Other countries … 5,900" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 6.15 | usgs_mcs_2025_lead | inferred | Not stated; 5,900/96,000 = 6.146% ≈ 6.15% |
| reserves.reserves_by_country[US].quantity.value | 4,600,000 tonnes | usgs_mcs_2025_lead | verified | "United States … 4,600" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[US].share_pct | 4.79 | usgs_mcs_2025_lead | inferred | Not stated; 4,600/96,000 = 4.792% ≈ 4.79% |
| reserves.reserves_by_country[IR].quantity.value | 2,000,000 tonnes | usgs_mcs_2025_lead | verified | "Iran … 2,000" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[IR].share_pct | 2.08 | usgs_mcs_2025_lead | inferred | Not stated; 2,000/96,000 = 2.083% ≈ 2.08% |
| reserves.reserves_by_country[IN].quantity.value | 1,900,000 tonnes | usgs_mcs_2025_lead | verified | "India … 1,900" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 1.98 | usgs_mcs_2025_lead | inferred | Not stated; 1,900/96,000 = 1.979% ≈ 1.98% |
| reserves.reserves_by_country[SE].quantity.value | 1,700,000 tonnes | usgs_mcs_2025_lead | verified | "Sweden … 1,700" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[SE].share_pct | 1.77 | usgs_mcs_2025_lead | inferred | Not stated; 1,700/96,000 = 1.771% ≈ 1.77% |
| reserves.reserves_by_country[BO].quantity.value | 1,600,000 tonnes | usgs_mcs_2025_lead | verified | "Bolivia … 1,600" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[BO].share_pct | 1.67 | usgs_mcs_2025_lead | inferred | Not stated; 1,600/96,000 = 1.667% ≈ 1.67% |
| reserves.reserves_by_country[TR].quantity.value | 1,600,000 tonnes | usgs_mcs_2025_lead | verified | "Turkey … 1,600" — USGS MCS 2025 p.107 Reserves column |
| reserves.reserves_by_country[TR].share_pct | 1.67 | usgs_mcs_2025_lead | inferred | Not stated; 1,600/96,000 = 1.667% ≈ 1.67% |
| reserves.reserves_by_country[TJ].notes (reserves = NA) | NA | usgs_mcs_2025_lead | verified | "Tajikistan … NA" — USGS MCS 2025 p.107 Reserves column |
| end_uses.uses[lead_acid_batteries].share_pct | 86 | usgs_mcs_2025_lead | verified | "Lead-acid battery industry accounted for an estimated 86% of reported U.S. lead consumption during 2024" — p.106 Domestic Production and Use |
| end_uses.uses[ammunition_shot_and_weights].share_pct | 6 | usgs_mcs_2025_lead | inferred | Not stated in MCS 2025 lead chapter; YAML confidence = low. MCS 2025 gives only the 86% battery figure explicitly; remaining 14% split is estimated from historical USGS data. |
| end_uses.uses[other_industrial_uses].share_pct | 8 | usgs_mcs_2025_lead | inferred | Not stated in MCS 2025 lead chapter; YAML confidence = low. Residual category from historical USGS data; 86+6+8 = 100%. |
| prices[2024].value | 1.10 USD/lb (110 c/lb) | usgs_mcs_2025_lead | verified | "Price, average, North American, cents per pound … 110" — USGS MCS 2025 p.106 Salient Statistics, 2024e column; source footnote 3: S&P Global Platts Metals Week |
| prices[2023].value | 1.141 USD/lb (114.1 c/lb) | usgs_mcs_2025_lead | verified | "Price, average, North American, cents per pound … 114.1" — USGS MCS 2025 p.106 Salient Statistics, 2023 column |
| prices[2022].value | 1.165 USD/lb (116.5 c/lb) | usgs_mcs_2025_lead | verified | "Price, average, North American, cents per pound … 116.5" — USGS MCS 2025 p.106 Salient Statistics, 2022 column |
| prices[2021].value | 1.130 USD/lb (113.0 c/lb) | usgs_mcs_2025_lead | verified | "Price, average, North American, cents per pound … 113.0" — USGS MCS 2025 p.106 Salient Statistics, 2021 column |
| prices[2020].value | 0.913 USD/lb (91.3 c/lb) | usgs_mcs_2025_lead | verified | "Price, average, North American, cents per pound … 91.3" — USGS MCS 2025 p.106 Salient Statistics, 2020 column |
| prices[2024].notes (first 9-month average = 110 c/lb) | 110 c/lb | usgs_mcs_2025_lead | verified | "During the first 9 months of 2024, the average North American price for lead was 110 cents per pound" — p.107 Events |
| prices[2024].notes (4% below 2023 annual average) | 4% | usgs_mcs_2025_lead | verified | "4% less than the annual average price of 114.1 cents per pound in 2023" — p.107 Events |
| geopolitical_events[mine_recovery_2024].notes (US recoverable lead +10% to 290 kt) | 10%; 290 kt | usgs_mcs_2025_lead | verified | "domestic mine production of recoverable lead increased by 10% from that in 2023" — p.107 Events |
| geopolitical_events[mine_recovery_2024].notes (net import reliance 28% from 33%) | 28%; 33% | usgs_mcs_2025_lead | verified | "the net import reliance decreased to 28% from 33%" — p.107 Events |
| geopolitical_events[lme_stocks_2024].event (LME stocks 199,000 tons) | 199,000 tons | usgs_mcs_2025_lead | verified | "Global stocks of lead in LME-approved warehouses were 199,000 tons at the end of September" — p.107 Events |
| geopolitical_events[lme_stocks_2024].event (49% more than yearend 2023) | 49% | usgs_mcs_2025_lead | verified | "49% more than those at yearend 2023" — p.107 Events |
| geopolitical_events[ilzsg_2024].event (refined +2.4% to 13.5 Mt) | +2.4%; 13.5 Mt | usgs_mcs_2025_lead | verified | "global refined lead production in 2024 was forecast to increase by 2.4% to 13.5 million tons" — p.107 Events |
| geopolitical_events[ilzsg_2024].event (consumption +0.2% to 13.1 Mt) | +0.2%; 13.1 Mt | usgs_mcs_2025_lead | verified | "refined lead consumption to increase by 0.2% to 13.1 million tons" — p.107 Events |
| geopolitical_events[battery_exports_2024].event (20 million batteries in 9 months) | 20 million | usgs_mcs_2025_lead | verified | "20 million spent SLI lead-acid batteries were exported" — p.107 Events |
| geopolitical_events[battery_exports_2024].event (+11% from same period 2023) | 11% | usgs_mcs_2025_lead | verified | "an 11% increase from 18.5 million batteries exported in the same period in 2023" — p.107 Events |
| geopolitical_events[reserves_revision_2025].event (China and Russia reserves revised) | revised | usgs_mcs_2025_lead | verified | "Reserves for China and Russia were revised based on Government reports" — p.107 World Mine Production and Reserves |
| geopolitical_events[reserves_revision_2025].impact (China 22,000 kt) | 22,000 kt | usgs_mcs_2025_lead | verified | "China … 22,000" — USGS MCS 2025 p.107 Reserves column |
| geopolitical_events[reserves_revision_2025].impact (Russia 8,900 kt) | 8,900 kt | usgs_mcs_2025_lead | verified | "Russia … 8,900" — USGS MCS 2025 p.107 Reserves column |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_lead | inferred | USGS MCS 2025 lead chapter does not state lead is on the US Critical Minerals List; lead is absent from the 2022 Federal Register Critical Minerals List (87 FR 10381). No explicit statement in the cited source. |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_lead | inferred | Not stated in the cited USGS lead chapter. Lead is absent from EU CRM Act 2023 Annex II; would require an EU-sourced citation for direct verification. |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_lead | inferred | Not stated in the cited USGS lead chapter. Lead is absent from EU SRMA 2024 Annex I; would require an EU-sourced citation for direct verification. |
| substitutes[cable_covering].availability | full | usgs_mcs_2025_lead | verified | "Substitution by plastics has reduced the use of lead in cable covering" — USGS MCS 2025 p.107 Substitutes paragraph |
| substitutes[food_cans].availability | full | usgs_mcs_2025_lead | verified | "Substitution by plastics has reduced the use of lead in … cans" — USGS MCS 2025 p.107 Substitutes paragraph |
| substitutes[potable_water_solder].availability | full | usgs_mcs_2025_lead | verified | "Tin has replaced lead in solder for potable water systems" — USGS MCS 2025 p.107 Substitutes paragraph |
| substitutes[electronics_soldering].availability | full | usgs_mcs_2025_lead | verified | "The electronics industry has moved toward lead-free solders" — USGS MCS 2025 p.107 Substitutes paragraph |
| substitutes[crt_shielding].availability | full | usgs_mcs_2025_lead | verified | "flat-panel displays that do not require lead shielding" — USGS MCS 2025 p.107 Substitutes paragraph |
| substitutes[wheel_weights].availability | full | usgs_mcs_2025_lead | verified | "Steel and zinc are common substitutes for lead in wheel weights" — USGS MCS 2025 p.107 Substitutes paragraph |

## Notes

**Source access**: USGS MCS 2025 Lead PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-lead.pdf) fetched and extracted via pdftotext -layout. Both pages (pp. 106–107) fully readable. All claims trace to a single primary source.

**Zero discrepancies**: All 93 verified claims match the USGS source exactly. Every quantity in the World Mine Production table, every reserves value, and all five years of price data are confirmed. No YAML data field contains a value that contradicts the source document.

**Country sum vs. stated world total (mine production)**: The 13 country rows for 2024e sum to 4,340 kt; the stated world total is 4,300 kt (rounded). The YAML correctly attributes this to rounding and computes share_pcts against the stated 4,300 kt denominator, yielding a sum of 100.93%. This is within the ±5% completeness tolerance.

**Country sum vs. stated world total (reserves)**: The 12 quantified country rows plus Other countries, excluding Tajikistan (NA), sum to 95,800 kt vs. stated world total 96,000 kt — 99.8% coverage. The YAML notes this accurately.

**All share_pcts are inferred**: The USGS lead chapter does not publish country percentage shares for either mine production or reserves. Every share_pct value is derived by dividing the country quantity by the stated world total. All calculations are arithmetically correct.

**End-use percentages**: The USGS MCS 2025 lead chapter provides only the 86% battery figure explicitly. The 6% (ammunition) and 8% (other industrial) figures are marked confidence: low and are historical estimates from prior USGS end-use surveys. Both are correctly tagged as inferred.

**Secondary production global figure**: The 9.2 Mt global secondary production figure is not stated in the MCS 2025 source; it is derived as 13.5 − 4.3 = 9.2 Mt and correctly marked as an inference in the YAML notes (confidence: medium on the refined block).

**Prices — basis and source**: All five North American average prices (2020–2024e) are from the Salient Statistics table, sourced from S&P Global Platts Metals Week (footnote 3). The YAML correctly identifies these as North American average cents per pound converted to USD/lb (÷100). The 2024e price of 110 c/lb represents the first-9-month average per the Events text, confirmed as the annual estimate in the Salient Statistics table.

**Tajikistan**: The source table lists Tajikistan mine production as estimated (e) for both 2023 (39 kt) and 2024e (40 kt), and its reserves as NA. The YAML correctly reflects all three values and notes the NA reserves status.

**Criticality flags**: Lead is absent from the 2022 US Critical Minerals List, EU CRM Act 2023 Annex II, and EU SRMA 2024 Annex I. The USGS lead chapter does not explicitly state these exclusions; all three false flags are therefore inferred. A direct Federal Register or EU Official Journal citation would be needed for full verification.

**ILZSG citation**: The ILZSG figures (13.5 Mt production, 13.1 Mt consumption, 2.4% and 0.2% growth rates) are cited in the USGS text as "According to the International Lead and Zinc Study Group" with footnote 5 identifying the source as the ILZSG September 30, 2024 Lisbon press release. These are verified within the USGS chapter; the underlying ILZSG press release was not independently fetched.

**US mine production detail**: The World Mine Production table shows the US 2024e value as 300 kt (lead in concentrates). The Salient Statistics table separately shows "Mine, recoverable lead = 290 kt" for 2024e. The YAML's country quantity (300 kt) correctly uses the world mine table figure; the 290 kt recoverable-lead figure is correctly presented in notes only.

**Australia JORC footnote**: The USGS source footnote 7 states "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 10 million tons." This JORC figure (10 Mt) is substantially less than the USGS total (35,000 kt = 35 Mt) reflecting different resource-category definitions. The YAML notes this accurately.

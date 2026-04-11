# Verification: Mo

- Element: molybdenum (Mo)
- Snapshot year: 2025
- Verifier: worker-3e23480c8fd1 (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 92 |
| discrepancy | 7 |
| inferred | 42 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[mine].mine.value | 260,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "World total (rounded) 248,000 260,000 15,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mine.notes (2023 world total 248,000 t) | 248,000 t | usgs_mcs_2025_molybdenum | verified | "World total (rounded) 248,000 260,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mine.notes (US 2024e = 33,000 t) | 33,000 t | usgs_mcs_2025_molybdenum | verified | "United States 34,000 33,000" — USGS MCS 2025 p.123; also "decreased by 3% to 33,000 tons of molybdenum content in 2024" p.122 |
| production[mine].mine.notes (US 2023 = 34,000 t) | 34,000 t | usgs_mcs_2025_molybdenum | verified | "compared with 34,000 tons in 2023" — USGS MCS 2025 p.122 Domestic Production and Use |
| production[mine].mine.notes (two primary Colorado operations) | 2 operations in Colorado | usgs_mcs_2025_molybdenum | verified | "Molybdenum concentrate production at primary molybdenum mines continued at two operations in Colorado" — p.122 |
| production[mine].mine.notes (byproduct seven operations: 4 AZ, 1 MT, 1 NV, 1 UT) | 7 operations | usgs_mcs_2025_molybdenum | verified | "molybdenum concentrate production from mines where molybdenum was a byproduct continued at seven operations (four in Arizona and one each in Montana, Nevada, and Utah)" — p.122 |
| production[mine].mine.notes (three US roasting plants) | 3 roasting plants | usgs_mcs_2025_molybdenum | verified | "Three roasting plants converted molybdenum concentrate to molybdic oxide" — p.122 |
| production[mine].mine.notes (net import reliance = E) | E (net exporter) | usgs_mcs_2025_molybdenum | verified | "Net import reliance … E" — USGS MCS 2025 p.122 Salient Statistics, all years 2020–2024e |
| production[mine].mine.notes (recycling up to 30% of apparent supply) | up to 30% | usgs_mcs_2025_molybdenum | verified | "The amount of molybdenum recycled as part of new and old steel and other scrap may be as much as 30% of the apparent supply of molybdenum" — p.122 Recycling |
| production[mine].mining_by_country[CN].quantity.value | 110,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "China e96,000 110,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[CN].share_pct | 42.31% | usgs_mcs_2025_molybdenum | inferred | Not stated; 110,000 / 260,000 = 42.308% ≈ 42.31% |
| production[mine].mining_by_country[CN].notes (2023 = 96,000e) | 96,000 t (estimated) | usgs_mcs_2025_molybdenum | verified | "China e96,000 110,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[CN].notes (both primary and byproduct) | primary + byproduct | usgs_mcs_2025_molybdenum | verified | "only China and the United States produced molybdenum from both primary molybdenum mines and byproduct copper mines" — p.123 Events |
| production[mine].mining_by_country[PE].quantity.value | 41,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Peru 33,500 41,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[PE].share_pct | 15.77% | usgs_mcs_2025_molybdenum | inferred | Not stated; 41,000 / 260,000 = 15.769% ≈ 15.77% |
| production[mine].mining_by_country[PE].notes (2023 = 33,500) | 33,500 t | usgs_mcs_2025_molybdenum | verified | "Peru 33,500 41,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[PE].notes (+22% increase 2024) | +22% | usgs_mcs_2025_molybdenum | inferred | Not stated; (41,000 - 33,500) / 33,500 = 22.4% ≈ 22% |
| production[mine].mining_by_country[PE].notes (64% of US ore/concentrate imports) | 64% | usgs_mcs_2025_molybdenum | verified | "Molybdenum ore and concentrates: Peru, 64%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[PE].notes (35% of total US Mo imports) | 35% | usgs_mcs_2025_molybdenum | verified | "Total: Peru, 35%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[CL].quantity.value | 38,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Chile 44,100 38,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[CL].share_pct | 14.62% | usgs_mcs_2025_molybdenum | inferred | Not stated; 38,000 / 260,000 = 14.615% ≈ 14.62% |
| production[mine].mining_by_country[CL].notes (2023 = 44,100) | 44,100 t | usgs_mcs_2025_molybdenum | verified | "Chile 44,100 38,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[CL].notes (34% of total US Mo imports) | 34% | usgs_mcs_2025_molybdenum | verified | "Total: … Chile, 34%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[CL].notes (77% of US FeMo imports) | 77% | usgs_mcs_2025_molybdenum | verified | "Ferromolybdenum: Chile, 77%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[US].quantity.value | 33,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "United States 34,000 33,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[US].share_pct | 12.69% | usgs_mcs_2025_molybdenum | inferred | Not stated; 33,000 / 260,000 = 12.692% ≈ 12.69% |
| production[mine].mining_by_country[US].notes (2023 = 34,000) | 34,000 t | usgs_mcs_2025_molybdenum | verified | "United States 34,000 33,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[US].notes (apparent consumption 2024e ~12,000 mt) | ~12,000 t | usgs_mcs_2025_molybdenum | verified | "Apparent … 12,000" — USGS MCS 2025 p.122 Salient Statistics, 2024e column |
| production[mine].mining_by_country[US].notes (exports ore/concentrate 2024e ~45,000 mt) | ~45,000 t | usgs_mcs_2025_molybdenum | verified | "Exports: Ore and concentrates … 45,000" — USGS MCS 2025 p.122 Salient Statistics, 2024e column |
| production[mine].mining_by_country[MX].quantity.value | 17,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Mexico 17,500 17,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[MX].share_pct | 6.54% | usgs_mcs_2025_molybdenum | inferred | Not stated; 17,000 / 260,000 = 6.538% ≈ 6.54% |
| production[mine].mining_by_country[MX].notes (2023 = 17,500) | 17,500 t | usgs_mcs_2025_molybdenum | verified | "Mexico 17,500 17,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[MX].notes (18% of US ore/concentrate imports) | 18% | usgs_mcs_2025_molybdenum | verified | "Molybdenum ore and concentrates: … Mexico, 18%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[MX].notes (10% of total US Mo imports) | 10% | usgs_mcs_2025_molybdenum | verified | "Total: … Mexico, 10%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[AM].quantity.value | 8,000 tonnes_per_year (estimated) | usgs_mcs_2025_molybdenum | verified | "Armenia e7,600 e8,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[AM].share_pct | 3.08% | usgs_mcs_2025_molybdenum | inferred | Not stated; 8,000 / 260,000 = 3.077% ≈ 3.08% |
| production[mine].mining_by_country[AM].notes (2023 = 7,600e) | 7,600 t (estimated) | usgs_mcs_2025_molybdenum | verified | "Armenia e7,600 e8,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[AM].notes (reserves 150 kt) | 150 kt | usgs_mcs_2025_molybdenum | verified | "Armenia … 150" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[KZ].quantity.value | 3,900 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Kazakhstan 3,730 3,900" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[KZ].share_pct | 1.50% | usgs_mcs_2025_molybdenum | inferred | Not stated; 3,900 / 260,000 = 1.500% |
| production[mine].mining_by_country[KZ].notes (2023 = 3,730) | 3,730 t | usgs_mcs_2025_molybdenum | verified | "Kazakhstan 3,730 3,900" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[KZ].notes (reserves 7 kt) | 7 kt | usgs_mcs_2025_molybdenum | verified | "Kazakhstan … 7" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[MN].quantity.value | 3,100 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Mongolia 3,160 3,100" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[MN].share_pct | 1.19% | usgs_mcs_2025_molybdenum | inferred | Not stated; 3,100 / 260,000 = 1.192% ≈ 1.19% |
| production[mine].mining_by_country[MN].notes (2023 = 3,160) | 3,160 t | usgs_mcs_2025_molybdenum | verified | "Mongolia 3,160 3,100" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[MN].notes (reserves 10 kt) | 10 kt | usgs_mcs_2025_molybdenum | verified | "Mongolia … 10" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[IR].quantity.value | 3,000 tonnes_per_year (estimated) | usgs_mcs_2025_molybdenum | verified | "Iran e2,500 e3,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[IR].share_pct | 1.15% | usgs_mcs_2025_molybdenum | inferred | Not stated; 3,000 / 260,000 = 1.154% ≈ 1.15% |
| production[mine].mining_by_country[IR].notes (2023 = 2,500e) | 2,500 t (estimated) | usgs_mcs_2025_molybdenum | verified | "Iran e2,500 e3,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[IR].notes (reserves 43 kt) | 43 kt | usgs_mcs_2025_molybdenum | verified | "Iran … 43" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[RU].quantity.value | 1,700 tonnes_per_year (estimated) | usgs_mcs_2025_molybdenum | verified | "Russia e1,700 e1,700" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[RU].share_pct | 0.65% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,700 / 260,000 = 0.654% ≈ 0.65% |
| production[mine].mining_by_country[RU].notes (2023 = 1,700e unchanged) | 1,700 t (estimated) | usgs_mcs_2025_molybdenum | verified | "Russia e1,700 e1,700" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[RU].notes (reserves 1,100 kt) | 1,100 kt | usgs_mcs_2025_molybdenum | verified | "Russia … 1,100" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[UZ].quantity.value | 1,700 tonnes_per_year (estimated) | usgs_mcs_2025_molybdenum | verified | "Uzbekistan e1,700 e1,700" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[UZ].share_pct | 0.65% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,700 / 260,000 = 0.654% ≈ 0.65% |
| production[mine].mining_by_country[UZ].notes (2023 = 1,700e unchanged) | 1,700 t (estimated) | usgs_mcs_2025_molybdenum | verified | "Uzbekistan e1,700 e1,700" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[UZ].notes (reserves 21 kt) | 21 kt | usgs_mcs_2025_molybdenum | verified | "Uzbekistan … 21" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[CA].quantity.value | 1,200 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Canada 1,150 1,200" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[CA].share_pct | 0.46% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,200 / 260,000 = 0.462% ≈ 0.46% |
| production[mine].mining_by_country[CA].notes (2023 = 1,150) | 1,150 t | usgs_mcs_2025_molybdenum | verified | "Canada 1,150 1,200" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[CA].notes (Idaho mine restart 2H 2027; Pennsylvania facility) | Idaho restart 2027; Pennsylvania rampup | usgs_mcs_2025_molybdenum | verified | "a Canadian company announced plans to restart its idled Idaho molybdenum mine in the second half of 2027 as well as a progressive rampup to full capacity production at its molybdenum-processing facility in Pennsylvania" — p.123 Events |
| production[mine].mining_by_country[CA].notes (reserves 64 kt) | 64 kt | usgs_mcs_2025_molybdenum | verified | "Canada … 64" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[AU].quantity.value | 1,000 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Australia 660 1,000" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[AU].share_pct | 0.38% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,000 / 260,000 = 0.385% ≈ 0.38% |
| production[mine].mining_by_country[AU].notes (2023 = 660) | 660 t | usgs_mcs_2025_molybdenum | verified | "Australia 660 1,000" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[AU].notes (total reserves 690 kt; JORC 250,000 tons) | 690 kt; JORC 250,000 tons | usgs_mcs_2025_molybdenum | verified | "Australia … 690" — p.123 Reserves; footnote 6: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 250,000 tons" |
| production[mine].mining_by_country[KP].quantity.value | 700 tonnes_per_year (estimated) | usgs_mcs_2025_molybdenum | verified | "Korea, North e400 e700" — USGS MCS 2025 p.123 World Mine Production table, 2024e column (estimated) |
| production[mine].mining_by_country[KP].share_pct | 0.27% | usgs_mcs_2025_molybdenum | inferred | Not stated; 700 / 260,000 = 0.269% ≈ 0.27% |
| production[mine].mining_by_country[KP].notes (2023 = 400e) | 400 t (estimated) | usgs_mcs_2025_molybdenum | verified | "Korea, North e400 e700" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[KP].notes (reserves NA) | NA | usgs_mcs_2025_molybdenum | verified | "Korea, North … NA" — USGS MCS 2025 p.123 Reserves column |
| production[mine].mining_by_country[KR].quantity.value | 300 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Korea, Republic of 339 300" — USGS MCS 2025 p.123 World Mine Production table, 2024e column |
| production[mine].mining_by_country[KR].share_pct | 0.12% | usgs_mcs_2025_molybdenum | inferred | Not stated; 300 / 260,000 = 0.115% ≈ 0.12% |
| production[mine].mining_by_country[KR].notes (2023 = 339) | 339 t | usgs_mcs_2025_molybdenum | verified | "Korea, Republic of 339 300" — USGS MCS 2025 p.123 World Mine Production table, 2023 column |
| production[mine].mining_by_country[KR].notes (19% of US FeMo imports) | 19% | usgs_mcs_2025_molybdenum | verified | "Ferromolybdenum: … Republic of Korea, 19%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[KR].notes (reserves 8 kt) | 8 kt | usgs_mcs_2025_molybdenum | verified | "Korea, Republic of … 8" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[AR].quantity.value | 0 tonnes_per_year | usgs_mcs_2025_molybdenum | verified | "Argentina — —" — USGS MCS 2025 p.123 World Mine Production table, both 2023 and 2024e (zero) |
| production[mine].mining_by_country[AR].share_pct | 0.0% | usgs_mcs_2025_molybdenum | inferred | Not stated; 0 / 260,000 = 0% |
| production[mine].mining_by_country[AR].notes (reserves 100 kt) | 100 kt | usgs_mcs_2025_molybdenum | verified | "Argentina … 100" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| production[mine].mining_by_country[CL].notes (Chile 12% of US ore/concentrate imports) | 12% | usgs_mcs_2025_molybdenum | verified | "Molybdenum ore and concentrates: … Chile, 12%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[CA].notes (Canada 5% of US ore/concentrate imports) | 5% | usgs_mcs_2025_molybdenum | verified | "Molybdenum ore and concentrates: … Canada, 5%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].mining_by_country[KR].notes (UK 3% of US FeMo imports) | 3% | usgs_mcs_2025_molybdenum | verified | "Ferromolybdenum: … United Kingdom, 3%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| production[mine].notes (Korea 6% of total US Mo imports) | 6% | usgs_mcs_2025_molybdenum | verified | "Total: … Republic of Korea, 6%" — USGS MCS 2025 p.122 Import Sources (2020–23) |
| reserves.economic_reserves.value | 15,000,000 tonnes | usgs_mcs_2025_molybdenum | verified | "World total (rounded) … 15,000" — USGS MCS 2025 p.123 Reserves column (thousand metric tons; ×1,000 = 15,000,000 t) |
| reserves.resources.value | 25,400,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Identified resources … in the United States are about 5.4 million tons and, in the rest of the world, about 20 million tons" — p.123; 5,400,000 + 20,000,000 = 25,400,000 |
| reserves.resources.notes (US resources 5.4 million tons) | 5,400,000 t | usgs_mcs_2025_molybdenum | verified | "Identified resources of molybdenum in the United States are about 5.4 million tons" — USGS MCS 2025 p.123 World Resources |
| reserves.resources.notes (rest of world ~20 million tons) | 20,000,000 t | usgs_mcs_2025_molybdenum | verified | "in the rest of the world, about 20 million tons" — USGS MCS 2025 p.123 World Resources |
| reserves.reserves_by_country[CN].quantity.value | 5,900,000 tonnes | usgs_mcs_2025_molybdenum | verified | "China … 5,900" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[CN].share_pct | 39.33% | usgs_mcs_2025_molybdenum | inferred | Not stated; 5,900,000 / 15,000,000 = 39.333% ≈ 39.33% |
| reserves.reserves_by_country[US].quantity.value | 3,500,000 tonnes | usgs_mcs_2025_molybdenum | verified | "United States … 3,500" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[US].share_pct | 23.33% | usgs_mcs_2025_molybdenum | inferred | Not stated; 3,500,000 / 15,000,000 = 23.333% ≈ 23.33% |
| reserves.reserves_by_country[PE].quantity.value | 1,900,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Peru … 1,900" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[PE].share_pct | 12.67% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,900,000 / 15,000,000 = 12.667% ≈ 12.67% |
| reserves.reserves_by_country[CL].quantity.value | 1,400,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Chile … 1,400" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[CL].share_pct | 9.33% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,400,000 / 15,000,000 = 9.333% ≈ 9.33% |
| reserves.reserves_by_country[RU].quantity.value | 1,100,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Russia … 1,100" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[RU].share_pct | 7.33% | usgs_mcs_2025_molybdenum | inferred | Not stated; 1,100,000 / 15,000,000 = 7.333% ≈ 7.33% |
| reserves.reserves_by_country[AU].quantity.value | 690,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Australia … 690" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[AU].share_pct | 4.60% | usgs_mcs_2025_molybdenum | inferred | Not stated; 690,000 / 15,000,000 = 4.600% |
| reserves.reserves_by_country[AU].notes (JORC-compliant subset 250,000 tons) | 250,000 tons | usgs_mcs_2025_molybdenum | verified | Footnote 6: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 250,000 tons" — USGS MCS 2025 p.123 |
| reserves.reserves_by_country[AM].quantity.value | 150,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Armenia … 150" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[AM].share_pct | 1.00% | usgs_mcs_2025_molybdenum | inferred | Not stated; 150,000 / 15,000,000 = 1.000% |
| reserves.reserves_by_country[MX].quantity.value | 130,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Mexico … 130" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[MX].share_pct | 0.87% | usgs_mcs_2025_molybdenum | inferred | Not stated; 130,000 / 15,000,000 = 0.867% ≈ 0.87% |
| reserves.reserves_by_country[AR].quantity.value | 100,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Argentina … 100" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[AR].share_pct | 0.67% | usgs_mcs_2025_molybdenum | inferred | Not stated; 100,000 / 15,000,000 = 0.667% ≈ 0.67% |
| reserves.reserves_by_country[CA].quantity.value | 64,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Canada … 64" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[CA].share_pct | 0.43% | usgs_mcs_2025_molybdenum | inferred | Not stated; 64,000 / 15,000,000 = 0.427% ≈ 0.43% |
| reserves.reserves_by_country[IR].quantity.value | 43,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Iran … 43" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[IR].share_pct | 0.29% | usgs_mcs_2025_molybdenum | inferred | Not stated; 43,000 / 15,000,000 = 0.287% ≈ 0.29% |
| reserves.reserves_by_country[UZ].quantity.value | 21,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Uzbekistan … 21" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[UZ].share_pct | 0.14% | usgs_mcs_2025_molybdenum | inferred | Not stated; 21,000 / 15,000,000 = 0.140% |
| reserves.reserves_by_country[MN].quantity.value | 10,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Mongolia … 10" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[MN].share_pct | 0.07% | usgs_mcs_2025_molybdenum | inferred | Not stated; 10,000 / 15,000,000 = 0.067% ≈ 0.07% |
| reserves.reserves_by_country[KR].quantity.value | 8,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Korea, Republic of … 8" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[KR].share_pct | 0.05% | usgs_mcs_2025_molybdenum | inferred | Not stated; 8,000 / 15,000,000 = 0.053% ≈ 0.05% |
| reserves.reserves_by_country[KZ].quantity.value | 7,000 tonnes | usgs_mcs_2025_molybdenum | verified | "Kazakhstan … 7" — USGS MCS 2025 p.123 Reserves column (thousand metric tons) |
| reserves.reserves_by_country[KZ].share_pct | 0.05% | usgs_mcs_2025_molybdenum | inferred | Not stated; 7,000 / 15,000,000 = 0.047% ≈ 0.05% |
| feedstock_origins[molybdenite_concentrate].notes (3 US roasting plants producing MoO₃) | 3 roasting plants | usgs_mcs_2025_molybdenum | verified | "Three roasting plants converted molybdenum concentrate to molybdic oxide" — p.122 |
| feedstock_origins[molybdenite_concentrate].notes (MoO₃ 57% Mo content) | 57% Mo | usgs_mcs_2025_molybdenum | verified | Footnote 3: "U.S. molybdic oxide (MoO3) price, 57% molybdenum content" — p.123 |
| feedstock_origins[porphyry_copper_ore].notes (Peru, Chile, Mexico exclusively byproduct) | exclusively byproduct | usgs_mcs_2025_molybdenum | verified | "the other countries produced molybdenum as a byproduct from copper mines" (Peru, Chile, Mexico in top-5 context) — p.123 Events |
| feedstock_origins[porphyry_copper_ore].notes (China and US both primary and byproduct) | both types | usgs_mcs_2025_molybdenum | verified | "only China and the United States produced molybdenum from both primary molybdenum mines and byproduct copper mines" — p.123 Events |
| feedstock_origins[porphyry_copper_ore].notes (declining ore grades; end-of-life mid-2030s) | mid-2030s | usgs_mcs_2025_molybdenum | verified | "Declining ore grades at porphyry copper mines continued to affect molybdenum production. Several large porphyry copper mines are expected to reach end-of-life in the mid-2030s" — p.123 Events |
| substitutes[alloy_steels].notes ("little substitution in steels and cast irons") | little substitution | usgs_mcs_2025_molybdenum | verified | "There is little substitution for molybdenum in its major application in steels and cast irons" — p.123 Substitutes |
| substitutes[alloy_steels].notes (boron, chromium, niobium, vanadium in alloy steels) | B, Cr, Nb, V | usgs_mcs_2025_molybdenum | verified | "Potential substitutes include boron, chromium, niobium (columbium), and vanadium in alloy steels" — p.123 Substitutes |
| substitutes[tool_steels].notes (tungsten in tool steels) | tungsten | usgs_mcs_2025_molybdenum | verified | "tungsten in tool steels" — p.123 Substitutes |
| substitutes[refractory_materials].notes (graphite, tantalum, tungsten for refractory) | graphite, Ta, W | usgs_mcs_2025_molybdenum | verified | "graphite, tantalum, and tungsten for refractory materials in high-temperature electric furnaces" — p.123 Substitutes |
| substitutes[pigments].notes (cadmium-red, chrome-orange, organic-orange for Mo orange) | Cd-red, Cr-orange, organic-orange | usgs_mcs_2025_molybdenum | verified | "cadmium-red, chrome-orange, and organic-orange pigments for molybdenum orange" — p.123 Substitutes |
| end_uses[alloy_steels_and_cast_irons].share_pct | 50% | usgs_mcs_2025_molybdenum | inferred | Not explicitly stated in MCS 2025; consistent with historical USGS Mo end-use data. Source only states Mo is "used principally as an alloying agent in cast iron, steel, and superalloys" |
| end_uses[stainless_and_high_alloy_steels].share_pct | 20% | usgs_mcs_2025_molybdenum | inferred | Not explicitly stated in MCS 2025; based on historical USGS Mo end-use data |
| end_uses[superalloys].share_pct | 10% | usgs_mcs_2025_molybdenum | inferred | Not explicitly stated in MCS 2025; source mentions superalloys as a principal use |
| end_uses[catalysts].share_pct | 10% | usgs_mcs_2025_molybdenum | inferred | Not explicitly stated in MCS 2025; source mentions catalysts among "numerous chemical applications" |
| end_uses[lubricants_pigments_and_other_chemicals].share_pct | 10% | usgs_mcs_2025_molybdenum | inferred | Not explicitly stated in MCS 2025; source mentions "catalysts, lubricants, and pigments" without percentages |
| prices[2024].value | 41.72 USD/kg | usgs_mcs_2025_molybdenum | discrepancy | YAML assigns $41.72/kg to year 2024, but source table shows: 2020=$19.19, 2021=$35.62, 2022=$41.72, 2023=$54.32, 2024e=$47. USGS MCS 2025 p.122 Salient Statistics: "Price, average, dollars per kilogram 19.19 35.62 41.72 54.32 47" (columns: 2020, 2021, 2022, 2023, 2024e). Correct 2024e price = $47/kg. |
| prices[2024].notes (2024e = $41.72/kg) | $41.72/kg for 2024e | usgs_mcs_2025_molybdenum | discrepancy | Source shows 2024e = $47/kg; $41.72 is the 2022 price. The 13% decrease applies: $54.32 × (1−0.13) ≈ $47. p.122 |
| prices[2024].notes (2023 avg = $47/kg) | 2023 = $47/kg | usgs_mcs_2025_molybdenum | discrepancy | Source shows 2023 = $54.32/kg (not $47). The $47 figure is the 2024e price. USGS MCS 2025 p.122 Salient Statistics |
| prices[2023].value | 47.0 USD/kg | usgs_mcs_2025_molybdenum | discrepancy | YAML assigns $47/kg to year 2023, but source shows 2023 = $54.32/kg and 2024e = $47/kg. USGS MCS 2025 p.122 Salient Statistics |
| prices[2022].value | 54.32 USD/kg | usgs_mcs_2025_molybdenum | discrepancy | YAML assigns $54.32/kg to year 2022, but source shows 2022 = $41.72/kg and 2023 = $54.32/kg. USGS MCS 2025 p.122 Salient Statistics |
| prices[2022].notes (highest price 2020–2024) | highest in range | usgs_mcs_2025_molybdenum | discrepancy | YAML claims 2022 = $54.32/kg is highest; actually $54.32 belongs to 2023, and 2022 = $41.72/kg. 2023 is the peak. USGS MCS 2025 p.122 |
| prices[2021].value | 35.62 USD/kg | usgs_mcs_2025_molybdenum | verified | "Price, average, dollars per kilogram … 35.62" — USGS MCS 2025 p.122 Salient Statistics, 2021 column |
| prices[2020].value | 19.19 USD/kg | usgs_mcs_2025_molybdenum | verified | "Price, average, dollars per kilogram … 19.19" — USGS MCS 2025 p.122 Salient Statistics, 2020 column |
| prices[*].source (Argus Media Group, Argus Non-Ferrous Markets) | Argus Media Group | usgs_mcs_2025_molybdenum | verified | Footnote 3: "U.S. molybdic oxide (MoO3) price, 57% molybdenum content. Source: Argus Media Group, Argus Non-Ferrous Markets" — p.123 |
| geopolitical_events[0].event (Canadian company Idaho mine restart 2H 2027) | restart 2H 2027 | usgs_mcs_2025_molybdenum | verified | "a Canadian company announced plans to restart its idled Idaho molybdenum mine in the second half of 2027" — p.123 Events |
| geopolitical_events[0].event (Pennsylvania Mo-processing facility rampup) | Pennsylvania rampup | usgs_mcs_2025_molybdenum | verified | "a progressive rampup to full capacity production at its molybdenum-processing facility in Pennsylvania" — p.123 Events |
| geopolitical_events[1].event (6% global production increase to 260,000 t) | +6% to 260,000 t | usgs_mcs_2025_molybdenum | verified | "Estimated global molybdenum production in 2024 increased by 6% compared with that in 2023" — p.123 Events; table: 248,000 → 260,000 |
| geopolitical_events[1].event (price fell 13%) | −13% | usgs_mcs_2025_molybdenum | verified | "the estimated average U.S. molybdic oxide price decreased by 13% compared with that in 2023" — p.123 Events |
| geopolitical_events[1].event ("to $41.72/kg") | $41.72/kg | usgs_mcs_2025_molybdenum | discrepancy | Event description states price fell "to $41.72/kg" but source shows 2024e price = $47/kg. $41.72 is the 2022 price. USGS MCS 2025 p.122 Salient Statistics |
| geopolitical_events[1].impact (China +14,000 t to 110,000 t) | +14,000 t; 110,000 t | usgs_mcs_2025_molybdenum | verified | Table: China 2023 = e96,000 t, 2024e = 110,000 t; difference = 14,000 t — USGS MCS 2025 p.123 |
| geopolitical_events[1].impact (Peru +7,500 t to 41,000 t) | +7,500 t; 41,000 t | usgs_mcs_2025_molybdenum | verified | Table: Peru 2023 = 33,500 t, 2024e = 41,000 t; difference = 7,500 t — USGS MCS 2025 p.123 |
| geopolitical_events[1].impact (Peru +22%) | +22% | usgs_mcs_2025_molybdenum | inferred | Not stated; (41,000 − 33,500) / 33,500 = 22.4% ≈ 22% |
| geopolitical_events[1].impact (Chile 44,100 → 38,000, −14%) | −14%; 44,100 → 38,000 | usgs_mcs_2025_molybdenum | verified | Table: Chile 2023 = 44,100 t, 2024e = 38,000 t — USGS MCS 2025 p.123 |
| geopolitical_events[1].impact (Chile −14% computed) | −14% | usgs_mcs_2025_molybdenum | inferred | Not stated; (44,100 − 38,000) / 44,100 = 13.8% ≈ 14% |
| geopolitical_events[2].event (declining ore grades at porphyry copper mines) | declining ore grades | usgs_mcs_2025_molybdenum | verified | "Declining ore grades at porphyry copper mines continued to affect molybdenum production" — p.123 Events |
| geopolitical_events[2].event (several large porphyry copper mines end-of-life mid-2030s) | mid-2030s | usgs_mcs_2025_molybdenum | verified | "Several large porphyry copper mines are expected to reach end-of-life in the mid-2030s" — p.123 Events |

## Notes

**Price year-assignment error (major discrepancy):** The YAML prices block has a systematic 2-year shift for 2022–2024. The USGS MCS 2025 p.122 Salient Statistics table (columns: 2020, 2021, 2022, 2023, 2024e) clearly shows:

| Year | Correct price (USD/kg) | YAML value |
|---|---|---|
| 2020 | 19.19 | 19.19 (correct) |
| 2021 | 35.62 | 35.62 (correct) |
| 2022 | 41.72 | 54.32 (wrong — this is 2023's price) |
| 2023 | 54.32 | 47.00 (wrong — this is 2024e's price) |
| 2024e | 47.00 | 41.72 (wrong — this is 2022's price) |

The geopolitical_events[1] event description also incorrectly states the 2024 price as "$41.72/kg" (should be "$47/kg"). The YAML notes within the 2024 and 2022 price entries contain correlated errors (e.g., claiming 2022 is "the highest price in 2020–2024" when 2023 is actually the peak).

**Apparent consumption note:** The Events text on p.123 contains a drafting error reading "Estimated apparent consumption in 2023 increased by 11% compared with that in 2023" — both years should differ (likely "in 2024 compared with that in 2023"). The salient statistics table confirms 2023 apparent consumption = 10,900 t and 2024e = 12,000 t (+10.1% ≈ 11%). No YAML claim is affected by this source error.

**Country sum vs. world total:** The sum of the 16 listed country production values (2024e) = 263,600 t (not 264,600 t as stated in the YAML production notes). The world total 260,000 t is rounded; the ~3,600 t discrepancy is a rounding artifact. The YAML notes field states 264,600 t, which contains a further 1,000 t arithmetic error, but this is a notes-level annotation rather than a structured YAML claim.

**Source coverage:** All structured claims with source_id = usgs_mcs_2025_molybdenum trace to the two-page USGS MCS 2025 Molybdenum chapter (pp.122–123). The source is fully accessible (PDF download confirmed). End-use percentage splits (50/20/10/10/10) are not stated anywhere in MCS 2025 and are inferred from historical USGS data patterns; they carry confidence: low in the YAML.

**Criticality flags:** The criticality block (us_critical_list_as_of_2025, eu_crm_list_as_of_2024, eu_strategic_list_as_of_2024) carries no source_id in Mo.yaml and was not independently verified here. Molybdenum absence from the US 2022 Critical Minerals List and EU CRM list is consistent with USGS commentary on US net-exporter status.

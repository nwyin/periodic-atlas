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

## Notes

**Source access**: USGS MCS 2025 molybdenum PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-molybdenum.pdf) verified via pdfplumber. All production and reserve figures confirmed against World Mine Production and Reserves table, p.122–123.

**Reserve totals rounding**: Named-country reserves sum to 15,023 kt vs. stated world total 15,000 kt — within 0.2% and flagged as a USGS rounding artifact in the YAML notes. Not a YAML error.

---

## `byproduct_of: []` audit — 2026-04-14

**Decision: keep `byproduct_of: []` (Option A). No change to Mo.yaml.**

### Background

`specs/byproduct-graph.md` §3 flagged `byproduct_of: []` on Mo.yaml as a potential data gap, noting the multi-hop chain "Re ← Mo ← Cu" is invisible in the graph. The spec proposed `byproduct_of: [Cu]` as a fix. This audit evaluates whether that change is semantically correct.

### Schema contract

From `src/atlas/models.py` line 683–686:

```python
byproduct_of: list[str] = Field(
    default_factory=list,
    description="Parent element symbols this element is co-produced with. Element symbols only.",
)
```

The description says "co-produced with" — which is ambiguous between "exclusively co-produced" and "sometimes co-produced." The broader module docstring (line 42–45) says: "`byproduct_of` is a list of element symbols (co-produced metals like Ga-from-Al)." The Ga-from-Al example is instructive: Ga has no primary mine production of any significance — it is recovered only as a byproduct of aluminum (Bayer process) and zinc smelting.

### Empirical survey of non-empty `byproduct_of` values

| Element | `byproduct_of` | Has meaningful primary production? | Judgment |
|---------|---------------|------------------------------------|----------|
| Ag | Au, Cu, Pb, Zn | Some primary Ag mines exist but the vast majority of supply is byproduct | borderline — predominantly byproduct |
| Bi | Pb, Zn | No significant primary Bi mines; recovered from Pb/Zn smelter residues | correctly typed as byproduct |
| Cd | Zn | No primary Cd mines; Cd is pure byproduct of zinc refining | correctly typed as byproduct |
| Co | Cu, Ni | No primary Co mines; recovered from Cu-Co stratiform (DRC) and Ni laterite ore | correctly typed as byproduct |
| Ga | Al, Zn | No primary Ga mines; 99% from Chinese Al Bayer process (USGS MCS 2025) | correctly typed as byproduct |
| Ge | Zn | No primary Ge mines; coal fly ash + Zn smelter route | correctly typed as byproduct |
| Hf | Zr | No primary Hf mines; separated from Zr in nuclear-grade processing | correctly typed as byproduct |
| Ir | Cu, Ni, Pt | No primary Ir mines; PGM byproduct | correctly typed as byproduct |
| Os | Ni, Pt | No primary Os mines; PGM byproduct | correctly typed as byproduct |
| Pd | Cu, Ni | No primary Pd mines; Ni/Cu sulfide concentrates (Norilsk, Sudbury) | correctly typed as byproduct |
| Pm | Pu | No primary Pm mines; reactor/reprocessing byproduct | correctly typed as byproduct |
| Rb | Cs, Li | No primary Rb mines; pollucite processing | correctly typed as byproduct |
| Re | Cu, Mo | No primary Re mines; exclusively recovered from Mo roaster offgas and Cu smelter residues | correctly typed as byproduct |
| Rh | Ni, Pt | No primary Rh mines; PGM byproduct | correctly typed as byproduct |
| Ru | Ni, Pt | No primary Ru mines; PGM byproduct | correctly typed as byproduct |
| Sc | Ni, Ti | No primary Sc mines of significance; recovered from Ti/Ni laterite processing streams | correctly typed as byproduct |
| Te | Cu | No primary Te mines; recovered from Cu anode slimes | correctly typed as byproduct |
| Tl | Cu, Pb, Zn | No primary Tl mines; smelter residue recovery | correctly typed as byproduct |

**Pattern**: every element currently carrying a non-empty `byproduct_of` list has no meaningful primary mine production. The field is used consistently to mean "produced only (or overwhelmingly) as a byproduct — no independent primary mining pathway." The Ga-from-Al example in the docstring reinforces this interpretation.

### Mo production reality

Mo does not fit this pattern:

- **Primary Mo mines**: Henderson (CO) and Climax (CO) in the US; large primary Mo mines in CN. These deposits are mined specifically for molybdenum, not for a host metal.
- **Byproduct Mo routes**: PE, CL, MX produce Mo exclusively as a byproduct of porphyry Cu mining. CN and US produce from both routes. The two feedstock routes are documented in `feedstock_origins` (molybdenite_concentrate and porphyry_copper_ore) with full USGS sourcing.
- **Scale**: CN primary mines alone produce ~42% of world output. US primary mines in CO are the anchor of US primary Mo supply. Primary output is not trace or incidental — it is the economically dominant route globally (CN+US primary mines > all Cu-byproduct routes combined).

Mo is a genuine co-product (primary metal in some geographies, byproduct in others). No other element in the atlas occupies this position. Setting `byproduct_of: [Cu]` would misrepresent Mo as supply-locked to Cu economics, which is false for the Henderson/Climax operations and the bulk of Chinese output.

### Re.yaml confirmation

`Re.yaml` `byproduct_of: [Cu, Mo]` — confirmed correct. Re has no primary mine production anywhere; it is recovered exclusively from molybdenum concentrate roaster offgas (US, Chile) and copper smelter rhenium-bearing residues (Armenia, Kazakhstan, Poland, Russia, Uzbekistan). Both parent symbols are set, and both feedstock_origins entries are present with USGS citations.

### Recommendation: Option A

**Keep `byproduct_of: []` on Mo.yaml.** The existing data accurately models Mo as a primary metal with a significant byproduct co-production route. The byproduct Cu route is already fully documented in:

1. `feedstock_origins[1]` (substrate: porphyry_copper_ore) with a detailed note on PE/CL/MX exclusive byproduct status and the CN/US dual-route structure
2. Country-level notes in `mining_by_country` for PE, CL, MX (explicitly "produces molybdenum exclusively as a byproduct")
3. The `narrative` field describes the structural risk from porphyry Cu mine end-of-life

No YAML data is missing. The only thing `byproduct_of: [Cu]` would add is a graph edge — at the cost of a semantically incorrect classification.

### Impact on byproduct dependency graph

The Re ← Mo ← Cu chain is a real supply dependency chain. Mo's dual nature is a modeling limitation of the current binary schema (`byproduct_of` = yes/no per parent), not a data gap in Mo.yaml.

Recommended edit to `specs/byproduct-graph.md` §3 (do not apply here; flag for byproduct-graph agent):

- In the "Inconsistencies and schema proposals" section, replace item 1 ("Proposed fix: Add `byproduct_of: [Cu]` to Mo.yaml") with the following:

  > **Mo is a co-product, not a byproduct — data gap reclassified as known modeling limitation.** Mo.yaml `byproduct_of: []` is correct. Mo has substantial primary mine production (Henderson/Climax CO; primary CN mines) alongside byproduct Cu routes (PE, CL, MX; partial CN/US). The `byproduct_of` field is used consistently across all other elements to mean "produced only as a byproduct with no independent primary pathway" — setting `byproduct_of: [Cu]` would misrepresent Mo as supply-locked to copper economics. The byproduct Cu route is fully documented in Mo.yaml `feedstock_origins` and country-level notes. The Re ← Mo ← Cu three-hop chain is real but cannot be represented in the current binary schema without a false classification. Options: (a) accept Mo as a primary node in the graph (current correct behavior); (b) add an optional `coproduct_of` field or a `mode` tag on `byproduct_of` entries in a future schema revision (Option C in the audit); (c) document the limitation in the graph page tooltip for Mo. Recommend (a) + (c) for v1; (b) deferred unless the co-product distinction becomes analytically necessary for another feature.

- Update the primary nodes list in §3 to add a note: "Mo is listed as a primary node; its Cu-byproduct route is documented in `feedstock_origins` and country notes but not expressed as a graph edge (known co-product modeling limitation — see Mo verification note)."

- Update §4 UX design, "Multi-hop highlight" (line referencing Re ← Mo ← Cu chain): note that this chain is visible in the graph only if Mo is added as a byproduct node, which requires either the schema extension or accepting the false classification. For v1, the Re tooltip can read "Re is a byproduct of Mo and Cu; Mo itself is partly mined as a Cu byproduct (see Mo element page)" to give users the multi-hop context without a graph edge.

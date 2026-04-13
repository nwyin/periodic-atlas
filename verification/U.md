# Verification: U

- Element: uranium (U)
- Snapshot year: 2025
- Verifier: worker-666114604f8b (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 90 |
| discrepancy | 0 |
| inferred | 30 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 54,345 tonnes_per_year | nea_iaea_redbook_2024 | verified | "increasing a further 9.8% to 54 345 tU in 2023" — Table 1.18 and Chapter 1 narrative |
| production[0].mine.notes (9.8% increase from 2022) | 9.8% | nea_iaea_redbook_2024 | verified | "increasing a further 9.8% to 54 345 tU in 2023" — Red Book Chapter 1 narrative |
| production[0].mine.notes (49,490 tU in 2022) | 49,490 | nea_iaea_redbook_2024 | verified | "before then increasing 4.5% to 49 490 tU in 2022" — Table 1.18 total row 2022 column = 49,490 |
| production[0].mine.notes (47,361 tU in 2021) | 47,361 | nea_iaea_redbook_2024 | verified | "world uranium production reached its low point in 2020 and 2021 at 47 588 tU and 47 361 tU" — Red Book Chapter 1; Table 1.18 total 2021 = 47,361 |
| production[0].mine.notes (2016 peak ~63,000 tU) | ~63,000 | nea_iaea_redbook_2024 | verified | "just 86% of 2016 peak production of almost 63 000 tU" — Red Book Chapter 1 narrative |
| production[0].mine.notes (17 countries produced uranium in 2022) | 17 | nea_iaea_redbook_2024 | verified | "Of the 17 countries that produced uranium in 2022" — Red Book Chapter 1 |
| production[0].mine.notes (86% of 2016 peak) | 86% | nea_iaea_redbook_2024 | verified | "just 86% of 2016 peak production" — Red Book Chapter 1 explicit statement |
| production[0].mine.notes (14.3% recovery from 47,361 tU) | 14.3% | nea_iaea_redbook_2024 | inferred | Not stated in source; computed 54,345/47,361 − 1 = 14.74%; YAML states 14.3% which more closely matches 54,345/47,588 − 1 = 14.2% (the 2020 low); minor arithmetic inconsistency in notes, not in primary YAML value |
| production[0].mining_by_country[KZ].quantity.value | 21,112 | nea_iaea_redbook_2024 | verified | "Kazakhstan … 21 112" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[KZ].share_pct | 38.85 | nea_iaea_redbook_2024 | inferred | Not stated; 21,112 / 54,345 = 38.845%, rounds to 38.85% (half-up) |
| production[0].mining_by_country[CA].quantity.value | 10,986 | nea_iaea_redbook_2024 | verified | "Canada … 10 986" — Table 1.18, 2023 column |
| production[0].mining_by_country[CA].share_pct | 20.21 | nea_iaea_redbook_2024 | inferred | Not stated; 10,986 / 54,345 = 20.21% |
| production[0].mining_by_country[CA].notes (Cameco 2024 target 6,925 tU each mine) | 6,925 tU each | nea_iaea_redbook_2024 | verified | "Cameco provided guidance that its plan is to produce 6 925 tU at each of McArthur River/Key Lake and Cigar Lake in 2024" — Red Book Chapter 1 |
| production[0].mining_by_country[NA].quantity.value | 6,985 | nea_iaea_redbook_2024 | verified | "Namibia … 6 985" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[NA].share_pct | 12.85 | nea_iaea_redbook_2024 | inferred | Not stated; 6,985 / 54,345 = 12.85% |
| production[0].mining_by_country[AU].quantity.value | 4,658 | nea_iaea_redbook_2024 | verified | "Australia … 4 658" — Table 1.18, 2023 column |
| production[0].mining_by_country[AU].share_pct | 8.57 | nea_iaea_redbook_2024 | inferred | Not stated; 4,658 / 54,345 = 8.57% |
| production[0].mining_by_country[UZ].quantity.value | 4,000 | nea_iaea_redbook_2024 | verified | "Uzbekistan … 4 000" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[UZ].share_pct | 7.36 | nea_iaea_redbook_2024 | inferred | Not stated; 4,000 / 54,345 = 7.36% |
| production[0].mining_by_country[RU].quantity.value | 2,600 | nea_iaea_redbook_2024 | verified | "Russia … 2 600" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[RU].share_pct | 4.78 | nea_iaea_redbook_2024 | inferred | Not stated; 2,600 / 54,345 = 4.78% |
| production[0].mining_by_country[CN].quantity.value | 1,600 | nea_iaea_redbook_2024 | verified | "China … 1 600" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[CN].share_pct | 2.94 | nea_iaea_redbook_2024 | inferred | Not stated; 1,600 / 54,345 = 2.94% |
| production[0].mining_by_country[NE].quantity.value | 1,130 | nea_iaea_redbook_2024 | verified | "Niger … 1 130" — Table 1.18, 2023 column |
| production[0].mining_by_country[NE].share_pct | 2.08 | nea_iaea_redbook_2024 | inferred | Not stated; 1,130 / 54,345 = 2.08% |
| production[0].mining_by_country[NE].notes (Niger 2022 = 2,020 tU) | 2,020 | nea_iaea_redbook_2024 | verified | "Niger … 2 020" — Table 1.18, 2022 column; also confirmed in Chapter 1 narrative |
| production[0].mining_by_country[IN].quantity.value | 485 | nea_iaea_redbook_2024 | verified | "India … 485" — Table 1.18, 2023 column |
| production[0].mining_by_country[IN].share_pct | 0.89 | nea_iaea_redbook_2024 | inferred | Not stated; 485 / 54,345 = 0.892% rounds to 0.89% |
| production[0].mining_by_country[ZA].quantity.value | 200 | nea_iaea_redbook_2024 | verified | "South Africa … 200" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[ZA].share_pct | 0.37 | nea_iaea_redbook_2024 | inferred | Not stated; 200 / 54,345 = 0.368% rounds to 0.37% |
| production[0].mining_by_country[UA].quantity.value | 300 | nea_iaea_redbook_2024 | verified | "Ukraine … 300" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[UA].share_pct | 0.55 | nea_iaea_redbook_2024 | inferred | Not stated; 300 / 54,345 = 0.552% rounds to 0.55% |
| production[0].mining_by_country[US].quantity.value | 19 | nea_iaea_redbook_2024 | verified | "United States … 19" — Table 1.18, 2023 column (secretariat estimate *, footnote i: US data withheld, estimate based on industry information) |
| production[0].mining_by_country[US].share_pct | 0.03 | nea_iaea_redbook_2024 | inferred | Not stated; 19 / 54,345 = 0.035% rounds to 0.03% |
| production[0].mining_by_country[US].notes (EIA: 50,000 lb U3O8 = ~19 tU, 2023) | 50,000 lb ≈ 19 tU | eia_domestic_prod_2024 | verified | "U.S. uranium mines produced 677,000 pounds of U3O8 … in 2024, a significant increase from the 50,000 pounds produced in 2023" — EIA Domestic Uranium Production Report 2024 |
| production[0].mining_by_country[US].notes (677,000 lb U3O8 in 2024) | 677,000 lb | eia_domestic_prod_2024 | verified | "U.S. uranium mines produced 677,000 pounds of triuranium octoxide (U3O8)" — EIA Domestic Uranium Production Report 2024 |
| production[0].mining_by_country[US].notes (six ISR facilities, 14.1M lb/yr capacity) | 6 facilities / 14.1M lb/yr | eia_domestic_prod_2024 | verified | "Six in-situ recovery facilities were operating with a combined capacity of 14.1 million pounds U3O8 per year" — EIA Domestic Uranium Production Report 2024 |
| production[0].mining_by_country[US].notes (55.9M lb purchased from foreign sources 2024) | 55.9M lb | eia_umar_2024 | verified | "purchased a total of 55.9 million pounds U3O8e … during 2024" — EIA UMAR 2024 introduction |
| production[0].mining_by_country[ZZ].quantity.value | 270 | nea_iaea_redbook_2024 | inferred | Not stated as a total; sum of remaining producers: Brazil 171 + Pakistan 50 + Czechia 25 + Iran 21 + Hungary 3 = 270 (rounded from Table 1.18 2023 data) |
| production[0].mining_by_country[ZZ].share_pct | 0.50 | nea_iaea_redbook_2024 | inferred | Not stated; 270 / 54,345 = 0.497% rounds to 0.50% |
| production[0].mining_by_country[ZZ].notes (Brazil 171 tU) | 171 | nea_iaea_redbook_2024 | verified | "Brazil … 171" — Table 1.18, 2023 column |
| production[0].mining_by_country[ZZ].notes (Pakistan 50 tU) | 50 | nea_iaea_redbook_2024 | verified | "Pakistan … 50" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[ZZ].notes (Czech Republic 25 tU) | 25 | nea_iaea_redbook_2024 | verified | "Czechia … 25" — Table 1.18, 2023 column (estimate e: production from mine rehabilitation only) |
| production[0].mining_by_country[ZZ].notes (Iran 21 tU) | 21 | nea_iaea_redbook_2024 | verified | "Iran, Islamic Rep of … 21" — Table 1.18, 2023 column (secretariat estimate *) |
| production[0].mining_by_country[ZZ].notes (Hungary 3 tU) | 3 | nea_iaea_redbook_2024 | verified | "Hungary … 3" — Table 1.18, 2023 column (estimate e: from mine rehabilitation) |
| reserves.economic_reserves.value | 1,881,100 | nea_iaea_redbook_2024 | verified | "<USD 80/kgU … 1 881 100" — Table 1.1, 2023 row, Total Identified resources section |
| reserves.economic_reserves.notes (5.5% decrease from 1,990,800 tU in 2021) | 5.5% / 1,990,800 | nea_iaea_redbook_2024 | verified | "<USD 80/kgU … 1 990 800 … 1 881 100 … -109 700 … -5.5" — Table 1.1 rows for 2021/2023 and % change column |
| reserves.resources.value | 5,925,700 | nea_iaea_redbook_2024 | verified | "<USD 130/kgU … 5 925 700" — Table 1.1, 2023 row |
| reserves.resources.notes (2.5% decrease from 6,078,500 tU in 2021) | 2.5% / 6,078,500 | nea_iaea_redbook_2024 | verified | "<USD 130/kgU … 6 078 500 … 5 925 700 … -152 800 … -2.5" — Table 1.1 |
| reserves.resources.notes (<USD 260/kgU total = 7,934,500 tU) | 7,934,500 | nea_iaea_redbook_2024 | verified | "<USD 260/kgU … 7 934 500" — Table 1.1, 2023 row |
| reserves.reserves_by_country[AU].quantity.value | 1,671,200 | nea_iaea_redbook_2024 | verified | "Australia … 1 671 200" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[AU].notes (1,935,200 tU at <USD 260/kgU) | 1,935,200 | nea_iaea_redbook_2024 | verified | "Australia … 1 935 200" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[AU].notes (28% of global total) | 28% | nea_iaea_redbook_2024 | verified | "Globally, Australia continues to dominate the world's uranium resources with 28% of the [world resources]" — Red Book Chapter 1; computed 1,671,200/5,925,700 = 28.21% |
| reserves.reserves_by_country[AU].share_pct | 28.21 | nea_iaea_redbook_2024 | inferred | Not stated; 1,671,200 / 5,925,700 = 28.21% |
| reserves.reserves_by_country[KZ].quantity.value | 813,900 | nea_iaea_redbook_2024 | verified | "Kazakhstan … 813 900" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[KZ].notes (498,700 tU at <USD 40/kgU) | 498,700 | nea_iaea_redbook_2024 | verified | "Kazakhstan … 498 700" — Table 1.2a, <USD 40/kgU column (body text rounds to 498,800; table value 498,700 used) |
| reserves.reserves_by_country[KZ].notes (873,400 tU at <USD 260/kgU) | 873,400 | nea_iaea_redbook_2024 | verified | "Kazakhstan … 873 400" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[KZ].share_pct | 13.73 | nea_iaea_redbook_2024 | inferred | Not stated; 813,900 / 5,925,700 = 13.73% |
| reserves.reserves_by_country[CA].quantity.value | 582,000 | nea_iaea_redbook_2024 | verified | "Canada … 582 000" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[CA].notes (287,900 tU at <USD 80/kgU) | 287,900 | nea_iaea_redbook_2024 | verified | "Canada … 287 900" — Table 1.2a, <USD 80/kgU column |
| reserves.reserves_by_country[CA].notes (852,200 tU at <USD 260/kgU) | 852,200 | nea_iaea_redbook_2024 | verified | "Canada … 852 200" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[CA].share_pct | 9.82 | nea_iaea_redbook_2024 | inferred | Not stated; 582,000 / 5,925,700 = 9.82% |
| reserves.reserves_by_country[NA].quantity.value | 497,900 | nea_iaea_redbook_2024 | verified | "Namibia … 497 900" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[NA].notes (33,200 tU at <USD 80/kgU) | 33,200 | nea_iaea_redbook_2024 | verified | "Namibia … 33 200" — Table 1.2a, <USD 80/kgU column |
| reserves.reserves_by_country[NA].notes (550,800 tU at <USD 260/kgU) | 550,800 | nea_iaea_redbook_2024 | verified | "Namibia … 550 800" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[NA].share_pct | 8.40 | nea_iaea_redbook_2024 | inferred | Not stated; 497,900 / 5,925,700 = 8.40% |
| reserves.reserves_by_country[RU].quantity.value | 476,600 | nea_iaea_redbook_2024 | verified | "Russia … 476 600" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[RU].notes (32,400 tU at <USD 80/kgU) | 32,400 | nea_iaea_redbook_2024 | verified | "Russia … 32 400" — Table 1.2a, <USD 80/kgU column |
| reserves.reserves_by_country[RU].notes (652,500 tU at <USD 260/kgU) | 652,500 | nea_iaea_redbook_2024 | verified | "Russia … 652 500" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[RU].share_pct | 8.04 | nea_iaea_redbook_2024 | inferred | Not stated; 476,600 / 5,925,700 = 8.04% |
| reserves.reserves_by_country[NE].quantity.value | 336,000 | nea_iaea_redbook_2024 | verified | "Niger … 336 000" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[NE].notes (Imouraren deposit 105,000 tU at <USD 130/kgU) | 105,000 | nea_iaea_redbook_2024 | inferred | Not directly stated in Table 1.2a or the Niger national report passages reviewed; national report gives total RAR <USD 130/kgU = 273,136 tU + IR 62,818 tU ≈ 336,000 tU for all Niger deposits; the 105,000 tU for Imouraren specifically is not confirmed in available text |
| reserves.reserves_by_country[NE].notes (454,000 tU at <USD 260/kgU) | 454,000 | nea_iaea_redbook_2024 | verified | "Niger … 454 000" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[NE].share_pct | 5.67 | nea_iaea_redbook_2024 | inferred | Not stated; 336,000 / 5,925,700 = 5.67% |
| reserves.reserves_by_country[ZA].quantity.value | 320,900 | nea_iaea_redbook_2024 | verified | "South Africa … 320 900" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZA].notes (228,000 tU at <USD 80/kgU) | 228,000 | nea_iaea_redbook_2024 | verified | "South Africa … 228 000" — Table 1.2a, <USD 80/kgU column |
| reserves.reserves_by_country[ZA].notes (436,400 tU at <USD 260/kgU) | 436,400 | nea_iaea_redbook_2024 | verified | "South Africa … 436 400" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[ZA].share_pct | 5.42 | nea_iaea_redbook_2024 | inferred | Not stated; 320,900 / 5,925,700 = 5.42% |
| reserves.reserves_by_country[CN].quantity.value | 270,500 | nea_iaea_redbook_2024 | verified | "China … 270 500" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[CN].notes (73,200 tU at <USD 40/kgU) | 73,200 | nea_iaea_redbook_2024 | verified | "China … 73 200" — Table 1.2a, <USD 40/kgU column |
| reserves.reserves_by_country[CN].notes (291,300 tU at <USD 260/kgU) | 291,300 | nea_iaea_redbook_2024 | verified | "China … 291 300" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[CN].share_pct | 4.57 | nea_iaea_redbook_2024 | inferred | Not stated; 270,500 / 5,925,700 = 4.57% |
| reserves.reserves_by_country[BR].quantity.value | 167,800 | nea_iaea_redbook_2024 | verified | "Brazil … 167 800" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[BR].notes (177,800 tU at <USD 260/kgU) | 177,800 | nea_iaea_redbook_2024 | verified | "Brazil … 177 800" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[BR].notes (>100,000 tU removed in reassessment) | >100,000 | nea_iaea_redbook_2024 | verified | "the comprehensive reviews and reassessments of Brazil's and Uzbekistan's uranium resources resulted in the removal of approximately 100 000 tU and 70 000 tU, respectively" — Red Book Chapter 1 |
| reserves.reserves_by_country[BR].share_pct | 2.83 | nea_iaea_redbook_2024 | inferred | Not stated; 167,800 / 5,925,700 = 2.83% |
| reserves.reserves_by_country[MN].quantity.value | 144,600 | nea_iaea_redbook_2024 | verified | "Mongolia … 144 600" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[MN].share_pct | 2.44 | nea_iaea_redbook_2024 | inferred | Not stated; 144,600 / 5,925,700 = 2.44% |
| reserves.reserves_by_country[UA].quantity.value | 106,700 | nea_iaea_redbook_2024 | verified | "Ukraine … 106 700" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[UA].notes (184,800 tU at <USD 260/kgU) | 184,800 | nea_iaea_redbook_2024 | verified | "Ukraine … 184 800" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[UA].share_pct | 1.80 | nea_iaea_redbook_2024 | inferred | Not stated; 106,700 / 5,925,700 = 1.80% |
| reserves.reserves_by_country[US].quantity.value | 67,800 | nea_iaea_redbook_2024 | verified | "United States … 67 800" — Table 1.2a, <USD 130/kgU column (footnote h: Secretariat estimate; other cost data withheld for company confidentiality) |
| reserves.reserves_by_country[US].notes (121,400 tU at <USD 260/kgU) | 121,400 | nea_iaea_redbook_2024 | verified | "United States … 121 400" — Table 1.2a, <USD 260/kgU column |
| reserves.reserves_by_country[US].share_pct | 1.14 | nea_iaea_redbook_2024 | inferred | Not stated; 67,800 / 5,925,700 = 1.14% |
| reserves.reserves_by_country[ZZ].quantity.value | 469,800 | nea_iaea_redbook_2024 | inferred | Not stated; residual = 5,925,700 − sum(12 named countries) = 469,800 |
| reserves.reserves_by_country[ZZ].share_pct | 7.93 | nea_iaea_redbook_2024 | inferred | Not stated; 469,800 / 5,925,700 = 7.93% |
| reserves.reserves_by_country[ZZ].notes (Uzbekistan 45,000 tU) | 45,000 | nea_iaea_redbook_2024 | verified | "Uzbekistan … 45 000" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZZ].notes (Botswana 87,200 tU) | 87,200 | nea_iaea_redbook_2024 | verified | "Botswana … 87 200" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZZ].notes (Peru 33,400 tU) | 33,400 | nea_iaea_redbook_2024 | verified | "Peru … 33 400" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZZ].notes (Argentina 34,300 tU) | 34,300 | nea_iaea_redbook_2024 | verified | "Argentina … 34 300" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZZ].notes (Tanzania 57,700 tU) | 57,700 | nea_iaea_redbook_2024 | verified | "Tanzania … 57 700" — Table 1.2a, <USD 130/kgU column |
| reserves.reserves_by_country[ZZ].notes (Malawi 15,900 tU) | 15,900 | nea_iaea_redbook_2024 | verified | "Malawi … 15 900" — Table 1.2a, <USD 130/kgU column |
| feedstock_origins[sandstone_uranium_ore].notes (ISR ~52% world production 2024) | ~52% | wna_uranium_production_2024 | verified | WNA "World Uranium Mining Production" page lists 2024 production method breakdown: ISL/ISR = 52% |
| end_uses.uses[nuclear_power_fuel].notes (438 reactors operational) | 438 | nea_iaea_redbook_2024 | verified | "On 1 January 2023, a total of 438 commercial nuclear reactors were operational globally" — Red Book Chapter 2 |
| end_uses.uses[nuclear_power_fuel].notes (394 GWe net capacity) | 394 GWe | nea_iaea_redbook_2024 | verified | "total installed nuclear generating capacity (394 GWe)" — Figure 2.1 title and Table 2.1 summary |
| end_uses.uses[nuclear_power_fuel].notes (~59,018 tU annual requirements) | ~59,018 | nea_iaea_redbook_2024 | verified | "World uranium requirements (59 018 tU)" — Figure 2.1 title; also "World annual uranium requirements amounted to around 59 000 tU as of 1 January 2023" |
| end_uses.uses[nuclear_power_fuel].share_pct | 99 | nea_iaea_redbook_2024 | inferred | Not stated as 99%; derived from the Red Book noting virtually all mine production goes to commercial reactors; the 1% residual for defense/research is unquantified |
| end_uses.uses[nuclear_power_fuel].notes (~2,600 TWh in 2023) | ~2,600 TWh | nea_iaea_redbook_2024 | inferred | Red Book reports 2,683 TWh (2021) and 2,595 TWh (2022); 2023 figure not stated in Red Book (data as of 1 January 2023); YAML estimate consistent with 2022 trend |
| end_uses.uses[nuclear_power_fuel].notes (~10% of world electricity supply) | ~10% | nea_iaea_redbook_2024 | inferred | Not explicitly stated for 2023 in Red Book; nuclear share has been approximately 10% of world electricity in recent years; the YAML note reflects general knowledge consistent with IEA/IAEA data |
| end_uses.uses[research_reactors_defense_other].share_pct | 1 | nea_iaea_redbook_2024 | inferred | Not stated; residual after 99% to commercial power; Red Book acknowledges naval/defense HEU use but gives no percentage |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_overview | verified | "the removal of helium, potash, rhenium, strontium, and uranium" — USGS MCS 2025 p.18, "The United States List of Critical Minerals" section; references 87 FR 10381 |
| criticality.notes (87 FR 10381, 24 February 2022) | 87 FR 10381 | usgs_mcs_2025_overview | verified | "the U.S. Geological Survey (USGS) published the '2022 Final List of Critical Minerals' in the Federal Register (87 FR 10381)" — USGS MCS 2025 p.18 |
| criticality.notes (83 FR 23295, 2018 list) | 83 FR 23295 | usgs_mcs_2025_overview | verified | "The 2022 list of critical minerals, which revised the U.S. list of critical minerals published in 2018 (83 FR 23295)" — USGS MCS 2025 p.18 |
| criticality.eu_crm_list_as_of_2024 | false | nea_iaea_redbook_2024 | inferred | Not stated in source; uranium absent from EU CRM Regulation (EU) 2024/1252 annexes; nuclear materials fall under Euratom Supply Agency framework — confirmed by absence from EU CRM lists |
| criticality.eu_strategic_list_as_of_2024 | false | nea_iaea_redbook_2024 | inferred | Not stated in source; uranium absent from EU CRMA 2024 Annex I (Strategic Raw Materials) — consistent with Euratom's separate regulatory jurisdiction |
| prices[2020].value | 33.27 USD/lb | eia_umar_2024 | verified | "2020 … 33.27" — Table S1b, Total purchased (weighted-average price) row |
| prices[2021].value | 33.91 USD/lb | eia_umar_2024 | verified | "2021 … 33.91" — Table S1b, Total purchased (weighted-average price) row |
| prices[2022].value (contract) | 39.08 USD/lb | eia_umar_2024 | verified | "2022 … 39.08" — Table S1b, Total purchased (weighted-average price) row |
| prices[2022].value (spot year-end) | 47.75 USD/lb | nea_iaea_redbook_2024 | verified | "USD 47.75/lb U3O8 (USD 124/kg U) for 2022" — Red Book Chapter 1 narrative; TradeTech Exchange Value year-end 2022 |
| prices[2022].notes (year-end spot $47.75 = USD 124/kgU) | USD 124/kgU | nea_iaea_redbook_2024 | verified | "USD 47.75/lb U3O8 (USD 124/kg U) for 2022" — Red Book Chapter 1 |
| prices[2023].value (contract) | 43.80 USD/lb | eia_umar_2024 | verified | "2023 … 43.80" — Table S1b, Total purchased (weighted-average price) row; also introduction text "the 2023 weighted-average price of $43.80 per pound U3O8e" |
| prices[2023].notes (12% increase from 2022) | 12% | eia_umar_2024 | verified | 43.80 / 39.08 − 1 = 12.1%; the UMAR states "20% higher than the 2023 weighted-average price" for 2024 vs 2023, consistent with 2022→2023 being 12% |
| prices[2023].notes (91% long-term contracts) | 91% | eia_umar_2024 | inferred | 91% is explicitly stated for 2024 deliveries in UMAR 2024; the same figure is cited for 2023 in the YAML notes but is not explicitly stated for 2023 in the 2024 UMAR report |
| prices[2023].value (spot year-end) | 91.00 USD/lb | nea_iaea_redbook_2024 | verified | "USD 91.00/lb U3O8 (USD 236/kg U) for 2023" — Red Book Chapter 1 narrative; TradeTech Exchange Value year-end 2023 |
| prices[2023].notes (year-end spot $91.00 = USD 236/kgU) | USD 236/kgU | nea_iaea_redbook_2024 | verified | "USD 91.00/lb U3O8 (USD 236/kg U) for 2023" — Red Book Chapter 1 |
| prices[2024].value (contract) | 52.71 USD/lb | eia_umar_2024 | verified | "weighted-average price of $52.71 per pound U3O8e" — EIA UMAR 2024 introduction; also Table S1b 2024 row |
| prices[2024].notes (20% higher than 2023) | 20% | eia_umar_2024 | verified | "The 2024 weighted-average price of $52.71 per pound U3O8e was 20% higher than the 2023 weighted-average price" — EIA UMAR 2024 introduction |
| prices[2024].notes (highest since 2012) | highest since 2012 | eia_umar_2024 | verified | "the highest price since 2012" — EIA UMAR 2024 introduction |
| prices[2024].notes (55.9M lb total purchased) | 55.9M lb | eia_umar_2024 | verified | "purchased a total of 55.9 million pounds U3O8e" — EIA UMAR 2024 introduction; Table S1a 2024 = 55.9 |
| prices[2024].notes (51.6M lb in 2023) | 51.6M lb | eia_umar_2024 | verified | "The 2024 total of 55.9 million pounds U3O8e was 8% higher than the 2023 total of 51.6 million pounds" — EIA UMAR 2024 |
| prices[2024].notes (8% higher than 2023) | 8% | eia_umar_2024 | verified | "was 8% higher than the 2023 total" — EIA UMAR 2024 introduction |
| prices[2024].notes (9% spot contracts at $54.09/lb) | 9% / $54.09 | eia_umar_2024 | verified | "9% of the uranium delivered was purchased under spot contracts at a weighted-average price of $54.09 per pound" — EIA UMAR 2024 introduction |
| prices[2024].notes (91% long-term at $50.97/lb) | 91% / $50.97 | eia_umar_2024 | verified | "The remaining 91% was purchased under long-term contracts at a weighted-average price of $50.97 per pound" — EIA UMAR 2024 introduction |
| prices[2024].notes (21 new contracts at $86.20/lb) | 21 / $86.20 | eia_umar_2024 | verified | "COOs signed 21 new purchase contracts … at a weighted-average price of $86.20 per pound" — EIA UMAR 2024 introduction; Table 8: 3,007 thousand lb at $86.20, 21 contracts |
| geopolitical_events[2022-02].notes (Russia-Ukraine war February 2022) | 2022-02 | nea_iaea_redbook_2024 | verified | "The next surge in the uranium spot price was triggered by the start of the Russian-Ukraine war in 2022" — Red Book Chapter 2 |
| geopolitical_events[2022-02].impact (spot ~$43→~$64/lb Feb-April 2022) | ~$43 → ~$64/lb | nea_iaea_redbook_2024 | inferred | Red Book confirms 2022 spot surge on Russia-Ukraine war; year-end 2022 = $47.75/lb; specific $43→$64 trajectory between February and April 2022 not explicitly stated in Red Book text reviewed |
| geopolitical_events[2022-02].impact (utilities rebuilding inventories) | inventories rebuilt | nea_iaea_redbook_2024 | verified | "many utilities relying on Russian-sourced enriched uranium started to look for alternative supplies" — Red Book Chapter 2 |
| geopolitical_events[2023-07].notes (coup on 26 July 2023) | 26 July 2023 | nea_iaea_redbook_2024 | verified | "On 26 July 2023, a coup d'état occurred in Niger, the country's democratically elected president was detained, and a military junta established" — Red Book Niger national report |
| geopolitical_events[2023-07].impact (Niger production 2,020 → 1,130 tU) | 2,020 / 1,130 | nea_iaea_redbook_2024 | verified | "Niger … 2 020" (2022) and "Niger … 1 130" (2023) — Table 1.18 |
| geopolitical_events[2023-07].impact (SOMAIR halted yellowcake Sept 2023) | September 2023 halt | nea_iaea_redbook_2024 | verified | "In September 2023 Somaïr halted yellowcake production at the Arlit mine and brought forward plant maintenance" — Red Book Niger report and Chapter 1 |
| geopolitical_events[2023-07].impact (Imouraren permit revoked June 2024) | June 2024 | nea_iaea_redbook_2024 | verified | "In June 2024 Orano announced that Nigerien authorities had withdrawn the operating permit for the Imouraren uranium mine" — Red Book Chapter 1 and Niger national report |
| geopolitical_events[2023-07].impact (SOMAIR operating license revoked September 2024) | September 2024 | nea_iaea_redbook_2024 | inferred | The Red Book confirms Imouraren permit revocation (June 2024) but does not explicitly state SOMAIR operating license was revoked in September 2024; this post-dates the Red Book's 2024 narrative window for Niger |
| geopolitical_events[2023-07].impact (~20% of EU uranium imports) | ~20% EU imports | nea_iaea_redbook_2024 | inferred | Red Book describes Niger as "France's and the EU's primary source of uranium supply for decades" but does not state a specific EU import share percentage in the passages reviewed |
| geopolitical_events[2023-12].notes (COP28 December 2023) | December 2023 | nea_iaea_redbook_2024 | verified | "In December 2023, more than 20 countries made a joint declaration during the 28th Conference of the Parties … (COP28) in Dubai to triple installed nuclear capacity by 2050" — Red Book Chapter 2 |
| geopolitical_events[2023-12].impact (22+ countries initially, 30+ subsequently) | 22+ / 30+ | nea_iaea_redbook_2024 | verified | "call by over 20 countries" and "This declaration, now signed by over 30 countries" — Red Book Chapter 2; YAML's ">22 countries" consistent with "over 20" |
| geopolitical_events[2023-12].impact (spot $91/lb year-end 2023) | $91/lb | nea_iaea_redbook_2024 | verified | "USD 91.00/lb U3O8 (USD 236/kg U) for 2023" — Red Book Chapter 1 |
| geopolitical_events[2023-12].impact (spot $106/lb January 2024) | $106/lb | nea_iaea_redbook_2024 | verified | "uranium spot price rose to USD 106/lb U3O8" and "prices rising from USD 30/lb U3O8 at the start of 2021 to a high of USD 106/lb U3O8 in January 2024" — Red Book Chapter 1 |
| geopolitical_events[2023-12].impact (demand 130,000-140,000 tU/yr by 2050) | 130,000-140,000 tU/yr | nea_iaea_redbook_2024 | inferred | Red Book has high-case demand projections pointing to significant increases but the specific 130,000–140,000 tU range for 2050 is an analytic inference in the YAML; not confirmed as a direct quote from the Red Book tables reviewed |
| geopolitical_events[2024-05].notes (US Prohibiting Russian Uranium Imports Act, May 2024) | May 2024 | nea_iaea_redbook_2024 | verified | "In May 2024, the United States passed the Prohibiting Russian Uranium Imports Act, which bans the import of Russian-produced LEU until the end of 2040" — Red Book Chapter 2 |
| geopolitical_events[2024-05].impact (waiver through 2027 / until 1 January 2028) | through 2027 | nea_iaea_redbook_2024 | verified | "the law provides waivers for US nuclear plants/utilities … valid until 1 January 2028" — Red Book Chapter 2 |
| geopolitical_events[2024-05].impact (annual import limit 476 metric tons in 2024) | 476 metric tons | nea_iaea_redbook_2024 | verified | "starting at 476 metric tons in 2024 and decreasing each year" — Red Book Chapter 2 |
| geopolitical_events[2024-05].impact (effective 11 August 2024) | 11 August 2024 | nea_iaea_redbook_2024 | inferred | Red Book states "In May 2024, the United States passed the Prohibiting Russian Uranium Imports Act" but does not explicitly state the 11 August 2024 effective date; the date is 90 days after enactment consistent with the legislation |
| geopolitical_events[2024-01].impact (spot $106/lb USD 275/kgU, January 2024) | $106/lb / USD 275/kgU | nea_iaea_redbook_2024 | verified | "uranium spot price rose to USD 106/lb U3O8, and since March through August of 2024 has averaged between USD 80 to 90/lb U3O8" — Red Book Chapter 1; "USD 106/lb U3O8 (USD 275/kg U) in January 2024" — Red Book |
| geopolitical_events[2024-01].impact (March-August 2024 average $80-90/lb) | $80-90/lb | nea_iaea_redbook_2024 | verified | "since March through August of 2024 has averaged between USD 80 to 90/lb U3O8" — Red Book Chapter 1 |
| geopolitical_events[2024-01].impact (highest price in 17 years) | 17 years | nea_iaea_redbook_2024 | verified | "prices rising from USD 30/lb U3O8 at the start of 2021 to a high of USD 106/lb U3O8 in January 2024" — context; Red Book notes this level not seen since ~2007 (17 years prior to 2024) |
| geopolitical_events[2024-01].impact (Kazatomprom sulphuric acid shortages) | sulphuric acid shortages | nea_iaea_redbook_2024 | verified | "due to sulphuric acid shortages the company subsequently reduced guidance for 2024" — Red Book Chapter 1 on Kazatomprom |

## Notes

**Source coverage:** Five sources were cited in U.yaml. Primary sources — NEA/IAEA Red Book 2024 (NEA No. 7683) and EIA UMAR 2024 — were fetched and verified via pdftotext extraction. The EIA Domestic Uranium Production Report 2024 was verified via the EIA annual production page. The WNA page for world uranium mining production was fetched directly. The USGS MCS 2025 overview was extracted via pdftotext from the downloaded PDF.

**No discrepancies found.** All primary numeric claims match the cited sources.

**Table 1.18 country production (2023):** All 12 named-country quantities in U.yaml match Table 1.18 exactly. Secretariat estimates (marked *) are appropriately flagged `approximate: true` in the YAML. The ZZ remainder (270 tU = Brazil 171 + Pakistan 50 + Czechia 25 + Iran 21 + Hungary 3) is confirmed by summing the Table 1.18 entries. Grand total = 54,345 tU ✓

**Table 1.2a country resources (<USD 130/kgU):** All 12 named-country resource values match exactly. All 12 additional cost-category values in notes (at <USD 40/kgU, <USD 80/kgU, or <USD 260/kgU) match the table. One minor within-document inconsistency: Kazakhstan's <USD 40/kgU resources are listed as 498,700 tU in Table 1.2a but the body text of Chapter 1 rounds to 498,800 tU; the YAML uses the table value (498,700) which is authoritative.

**Table 1.1 global resources:** All three primary resource totals match exactly — <USD 80/kgU = 1,881,100 tU; <USD 130/kgU = 5,925,700 tU; <USD 260/kgU = 7,934,500 tU. The 2021 baseline values (1,990,800; 6,078,500; 7,917,500) and percentage changes (−5.5%, −2.5%, +0.2%) are all confirmed.

**EIA UMAR prices:** All five weighted-average purchase price values (2020–2024) and all purchase volume figures match Table S1b and the introductory text of the 2024 UMAR exactly.

**Red Book spot prices:** Year-end 2022 ($47.75/lb = USD 124/kgU) and year-end 2023 ($91.00/lb = USD 236/kgU) are both explicitly stated verbatim in the Red Book Chapter 1 narrative. The January 2024 peak ($106/lb = USD 275/kgU) is also explicitly stated.

**KZ body-text rounding:** The Red Book body text says Kazakhstan produces "more than the combined production from Canada, Namibia, Australia, and Uzbekistan." Checking 2023 data: KZ = 21,112 vs CA+NA+AU+UZ = 10,986+6,985+4,658+4,000 = 26,629. This claim is FALSE for 2023. However, looking at the Red Book's exact wording: this statement explicitly refers to 2022 production ("Kazakhstan remained by far the world's largest producer, at 43% of global production, even as production continued at scaled back levels. Kazakhstan's production alone in 2022 amounted to more than the combined production from Canada, Namibia, Australia, and Uzbekistan"). In 2022: KZ = 21,279 vs CA+NA+AU+UZ = 7,380+5,612+4,555+3,561 = 21,108. The 2022 comparison is accurate. The YAML's notes for KZ apply this statement to 2023, which is not accurate for 2023 (KZ 21,112 < combined 26,629). This is a minor inaccuracy in the KZ notes section (comparing 2023 data to a 2022 comparative statement), but it does not affect the primary numeric claims (quantities/shares) so no claim row is flagged as discrepancy.

**COP28 country count:** The Red Book states "over 20 countries" (earlier in the text) and then "now signed by over 30 countries." The YAML says "more than 22 countries (subsequently expanding to 30+)" — both figures are consistent with the Red Book's statements.

**Niger SOMAIR expulsion claim:** The YAML asserts "(3) expelled Orano from Niger entirely" in the Niger coup event. The Red Book (the cited source) does not confirm this specific claim. The Red Book only confirms the Imouraren permit revocation (June 2024) and the SOMAIR production halt (September 2023). The claim about SOMAIR license revocation in September 2024 and complete Orano expulsion from Niger appears to reflect post-Red Book events not covered in the cited source. Both are marked `inferred`.

**Imouraren deposit 105,000 tU:** The YAML cites 105,000 tU at <USD 130/kgU for the Imouraren deposit specifically. The Red Book's Niger national report gives Imouraren mineral reserves (proven + probable) and resources but does not provide a cost-categorized breakout of 105,000 tU for Imouraren alone; the country total of 336,000 tU at <USD 130/kgU is confirmed. Marked `inferred`.

**2023 TWh nuclear generation:** The YAML claims "approximately 2,600 TWh" for 2023. The Red Book only reports through 2022 (2,595 TWh). The 2023 estimate is consistent with the 2022 figure and reasonable, but not explicitly sourced from the Red Book. Marked `inferred`.

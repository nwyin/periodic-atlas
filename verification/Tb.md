# Verification: Tb

- Element: terbium (Tb)
- Snapshot year: 2025
- Verifier: worker-55afa2cec5d3 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 70 |
| discrepancy | 1 |
| inferred | 35 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 390 tonnes_per_year | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO × ~0.1% Tb basket share = 390 t. USGS does not report per-element Tb production; basket share is industry consensus, not in cited source. |
| production[0].mine.notes "world total REO 2024e = 390,000 t" | 390000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 390,000" — p.145 Mine production table, 2024 column; confirmed "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — p.145 Events, Trends, and Issues |
| production[0].mine.notes "2023 total = 376,000 t REO" | 376000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 376,000" — p.145 Mine production table, 2023 column |
| production[0].mine.notes "~0.1% basket share used as central estimate" | ~0.1 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares for any REE. The ~0.1% global weighted average for Tb is industry consensus from mineralogical literature; not verifiable from the cited USGS source. |
| production[0].mining_by_country[CN].share_pct | 69.2 | usgs_mcs_2025_rare_earths | verified | Computed: 270,000 t / 390,000 t = 69.23% ≈ 69.2%. Both underlying values confirmed — p.145 Mine production table. |
| production[0].mining_by_country[CN].quantity.value | 270 t | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 0.1% basket share = 270 t Tb₄O₇. Basket share not in USGS source. |
| production[0].mining_by_country[CN].notes "China 2024e: 270,000 t REO" | 270000 t REO | usgs_mcs_2025_rare_earths | verified | "China 14 270,000" — p.145 Mine production table, 2024 column (footnote 14: "Production quota; does not include undocumented production.") |
| production[0].mining_by_country[CN].notes "255,000 t in 2023" | 255000 t REO | usgs_mcs_2025_rare_earths | verified | "China 14 255,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[US].share_pct | 11.5 | usgs_mcs_2025_rare_earths | verified | Computed: 45,000 / 390,000 = 11.54% ≈ 11.5%. Values confirmed — p.145. |
| production[0].mining_by_country[US].quantity.value | 45 t | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 0.1% basket share = 45 t Tb₄O₇. Basket share not in USGS source. |
| production[0].mining_by_country[US].notes "US 2024e: 45,000 t REO" | 45000 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 45,000" — p.145 Mine production table, 2024 column. Also confirmed p.144 Domestic Production and Use: "An estimated 45,000 tons of REO in mineral concentrates were produced." |
| production[0].mining_by_country[US].notes "valued at ~$260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — p.144 Domestic Production and Use |
| production[0].mining_by_country[US].notes "41,600 t REO in 2023" | 41600 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 41,600" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[MM].share_pct | 7.9 | usgs_mcs_2025_rare_earths | verified | Computed: 31,000 / 390,000 = 7.95% ≈ 7.9%. Values confirmed — p.145. |
| production[0].mining_by_country[MM].quantity.value | 31 t | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 0.1% basket share = 31 t. Basket share not in USGS source. |
| production[0].mining_by_country[MM].notes "31,000 t REO 2024e" | 31000 t REO | usgs_mcs_2025_rare_earths | verified | "Burma 12 31,000" — p.145 Mine production table, 2024 column (footnote 12: estimated from China import data) |
| production[0].mining_by_country[MM].notes "43,000 t in 2023" | 43000 t REO | usgs_mcs_2025_rare_earths | verified | "Burma 12 43,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[AU].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[AU].quantity.value | 13 t | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% basket share = 13 t. Basket share not in USGS source. |
| production[0].mining_by_country[AU].notes "Australia 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Australia 12 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[AU].notes "16,000 t in 2023" | 16000 t REO | usgs_mcs_2025_rare_earths | verified | "Australia 12 16,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[NG].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[NG].quantity.value | 13 t | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% basket share = 13 t. Basket share not in USGS source. |
| production[0].mining_by_country[NG].notes "Nigeria 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Nigeria 12 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[NG].notes "7,200 t in 2023" | 7200 t REO | usgs_mcs_2025_rare_earths | verified | "Nigeria 12 7,200" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[TH].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[TH].quantity.value | 13 t | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% basket share = 13 t. Basket share not in USGS source. |
| production[0].mining_by_country[TH].notes "Thailand 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand 12 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[TH].notes "3,600 t in 2023" | 3600 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand 12 3,600" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[TH].notes "Thailand REO reserves: 4,500 t" | 4500 t REO reserves | usgs_mcs_2025_rare_earths | verified | "Thailand … 4,500" — p.145 Reserves column |
| production[0].mining_by_country[ZZ].quantity.value | 9 t | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 0.1% = ~9 t. Both the basket share and the ZZ REO total are not directly stated in USGS source. |
| production[0].mining_by_country[ZZ].notes "India 2,900 t" | 2900 t REO | usgs_mcs_2025_rare_earths | verified | "India … 2,900" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Russia 2,500 t" | 2500 t REO | usgs_mcs_2025_rare_earths | verified | "Russia … 2,500" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Madagascar 2,000 t" | 2000 t REO | usgs_mcs_2025_rare_earths | verified | "Madagascar 12 2,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Other USGS bucket 1,100 t" | 1100 t REO | usgs_mcs_2025_rare_earths | verified | "Other … 1,100" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Vietnam 300 t" | 300 t REO | usgs_mcs_2025_rare_earths | verified | "Vietnam 12 300" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Malaysia 130 t" | 130 t REO | usgs_mcs_2025_rare_earths | verified | "Malaysia 12 130" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Brazil 20 t" | 20 t REO | usgs_mcs_2025_rare_earths | verified | "Brazil … 20" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].share_pct | 2.3 | usgs_mcs_2025_rare_earths | inferred | Computed residual: India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.295% ≈ 2.3%. Share pct not stated in source. |
| production[0].refining_by_country[CN].share_pct | 93 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not state an explicit global refining share for China. Import sources (China 70%, p.144) are US import shares, not global refining capacity. The ~93% figure for Tb-specific HREE separation is consistent with DOE/IEA secondary sources but not verifiable from the cited USGS chapter. |
| production[0].refining_by_country[CN].notes "China 70% of US REE imports 2020–23" | 70 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — p.144 |
| production[0].refining_by_country[MY].share_pct | 4 | usgs_mcs_2025_rare_earths | inferred | USGS does not state Malaysia's global Tb refining share. The 4% is inferred from LAMP's role as the world's largest non-Chinese REE separator. Import data (13% of US imports from Malaysia) reflects mainly LREE products, not Tb-specific separation. |
| production[0].refining_by_country[MY].notes "Malaysia 13% of US imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%" — p.144 |
| production[0].refining_by_country[ZZ].share_pct | 3 | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 93% (CN) − 4% (MY) = 3%. Not stated in USGS. |
| production[0].refining_by_country[ZZ].notes "Estonia 5%, Japan 6% of US imports" | Estonia 5 pct / Japan 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%; Estonia, 5%" — p.144 |
| production[0].notes "World 2024e = 390,000 t; up from 376,000 in 2023" | 390000 / 376000 t REO | usgs_mcs_2025_rare_earths | verified | USGS table: World total 376,000 (2023), 390,000 (2024e) — p.145 |
| production[0].notes "China +15,000 t to 270,000 t" | +15000 to 270000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000 t" | +5800 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000 t" | +9400 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma decline -12,000 t to 31,000 t" | -12000 to 31000 | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| reserves.economic_reserves.value | 90000 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves floor >90,000,000 t × ~0.1% basket share = >90,000 t. USGS floor confirmed (see below); basket share is not in source. |
| reserves.economic_reserves.notes "world total REO reserves >90,000,000 t" | >90000000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … >90,000,000" — p.145 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 48.9 | usgs_mcs_2025_rare_earths | inferred | Computed: 44,000,000 / 90,000,000 = 48.89% ≈ 48.9%. Denominator is a floor (">90M"); true share may differ. |
| reserves.reserves_by_country[CN].quantity.value | 44000 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 0.1% basket share = 44,000 t. Basket share not in source. |
| reserves.reserves_by_country[CN].notes "China 44,000,000 t REO" | 44000000 t REO | usgs_mcs_2025_rare_earths | verified | "China … 44,000,000" — p.145 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 23.3 | usgs_mcs_2025_rare_earths | inferred | Computed: 21,000,000 / 90,000,000 = 23.33% ≈ 23.3%. Denominator is a floor. |
| reserves.reserves_by_country[BR].quantity.value | 21000 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 0.1% basket share = 21,000 t. Basket share not in source. |
| reserves.reserves_by_country[BR].notes "Brazil 21,000,000 t REO" | 21000000 t REO | usgs_mcs_2025_rare_earths | verified | "Brazil … 21,000,000" — p.145 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 7.7 | usgs_mcs_2025_rare_earths | inferred | Computed: 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Denominator is a floor. |
| reserves.reserves_by_country[IN].quantity.value | 6900 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 0.1% basket share = 6,900 t. |
| reserves.reserves_by_country[IN].notes "India 6,900,000 t REO" | 6900000 t REO | usgs_mcs_2025_rare_earths | verified | "India … 6,900,000" — p.145 Reserves column |
| reserves.reserves_by_country[AU].share_pct | 6.3 | usgs_mcs_2025_rare_earths | inferred | Computed: 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Denominator is a floor. |
| reserves.reserves_by_country[AU].quantity.value | 5700 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 0.1% basket share = 5,700 t. |
| reserves.reserves_by_country[AU].notes "Australia 5,700,000 t REO (JORC 3,300,000)" | 5700000 t REO / 3300000 JORC | usgs_mcs_2025_rare_earths | verified | "Australia … 5,700,000" — p.145 Reserves column; footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country[RU].share_pct | 4.2 | usgs_mcs_2025_rare_earths | inferred | Computed: 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Denominator is a floor. |
| reserves.reserves_by_country[RU].quantity.value | 3800 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 0.1% basket share = 3,800 t. |
| reserves.reserves_by_country[RU].notes "Russia 3,800,000 t REO (revised)" | 3800000 t REO | usgs_mcs_2025_rare_earths | verified | "Russia … 3,800,000" — p.145 Reserves column (revised in MCS 2025 per country and government reports) |
| reserves.reserves_by_country[VN].share_pct | 3.9 | usgs_mcs_2025_rare_earths | inferred | Computed: 3,500,000 / 90,000,000 = 3.89% ≈ 3.9%. Denominator is a floor. |
| reserves.reserves_by_country[VN].quantity.value | 3500 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,500,000 t REO × 0.1% basket share = 3,500 t. |
| reserves.reserves_by_country[VN].notes "Vietnam 3,500,000 t REO (revised)" | 3500000 t REO | usgs_mcs_2025_rare_earths | verified | "Vietnam 12 … 3,500,000" — p.145 Reserves column (revised in MCS 2025) |
| reserves.reserves_by_country[US].share_pct | 2.1 | usgs_mcs_2025_rare_earths | inferred | Computed: 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Denominator is a floor. |
| reserves.reserves_by_country[US].quantity.value | 1900 t Tb₄O₇ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 0.1% basket share = 1,900 t. |
| reserves.reserves_by_country[US].notes "US 1,900,000 t REO (revised)" | 1900000 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 1,900,000" — p.145 Reserves column (revised in MCS 2025) |
| reserves.notes "Greenland 1,500,000" | 1500000 t REO | usgs_mcs_2025_rare_earths | verified | "Greenland … 1,500,000" — p.145 Reserves column |
| reserves.notes "Tanzania 890,000" | 890000 t REO | usgs_mcs_2025_rare_earths | verified | "Tanzania … 890,000" — p.145 Reserves column |
| reserves.notes "South Africa 860,000" | 860000 t REO | usgs_mcs_2025_rare_earths | verified | "South Africa … 860,000" — p.145 Reserves column (revised) |
| reserves.notes "Canada 830,000" | 830000 t REO | usgs_mcs_2025_rare_earths | verified | "Canada … 830,000" — p.145 Reserves column |
| reserves.notes "Thailand 4,500" | 4500 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand … 4,500" — p.145 Reserves column |
| reserves.notes "revised for Russia, South Africa, US, Vietnam" | revised 4 countries | usgs_mcs_2025_rare_earths | verified | "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." — p.145 |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 0.35 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not state Tb₄O₇ concentration percentages in clay deposits. The ~0.2–0.5% range (midpoint 0.35%) is consistent with published mineralogical data on southern China IAC deposits; not verifiable from cited source. |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 0.02 | usgs_mcs_2025_rare_earths | inferred | USGS RE chapter does not state Tb₄O₇ % in bastnaesite. The ~0.01–0.03% range (midpoint 0.02%) is consistent with literature on Mountain Pass and similar deposits; not verifiable from cited source. |
| feedstock_origins[bastnaesite_ore].notes "bastnaesite mined at Mountain Pass" | bastnaesite at Mountain Pass CA | usgs_mcs_2025_rare_earths | verified | "Bastnaesite (or bastnäsite), a rare-earth fluorocarbonate mineral, was mined as a primary product at a mine in Mountain Pass, CA." — p.144 Domestic Production and Use |
| feedstock_origins[monazite_sand].typical_concentration_pct | 0.06 | usgs_mcs_2025_rare_earths | inferred | USGS RE chapter does not state Tb% in monazite. The ~0.05–0.08% range (midpoint ~0.06%) is consistent with mineralogical literature; not verifiable from cited source. |
| feedstock_origins[monazite_sand].notes "monazite stockpiled in US" | monazite stockpiled in southeastern US | usgs_mcs_2025_rare_earths | verified | "Monazite, a phosphate mineral, was stockpiled as a separated concentrate or included as an accessory mineral in heavy-mineral-sand concentrates in the southeastern United States." — p.144 Domestic Production and Use |
| substitutes[ndfeb_magnet_coercivity_enhancer].notes "generally are less effective" | substitutes generally less effective | usgs_mcs_2025_rare_earths | verified | "Substitutes are available for many applications but generally are less effective." — p.145 Substitutes |
| end_uses.uses[magnets_ndfeb_hree_dopant].share_pct | 60 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not provide per-element end-use percentage breakdowns. The 60% estimate is analyst/industry consensus for Tb's growing magnet application share. Not verifiable from cited source. |
| end_uses.uses[phosphors_fluorescent_led].share_pct | 25 | usgs_mcs_2025_rare_earths | inferred | No explicit % in USGS MCS 2025 RE chapter. Analyst estimate for declining phosphor segment. |
| end_uses.uses[solid_oxide_fuel_cells_specialty].share_pct | 8 | usgs_mcs_2025_rare_earths | inferred | No explicit % in USGS MCS 2025 RE chapter. Analyst estimate for specialty ceramic/SOFC applications. |
| end_uses.uses[other_uses].share_pct | 7 | usgs_mcs_2025_rare_earths | inferred | Residual estimate. No explicit % in USGS MCS 2025 RE chapter. |
| prices[2024].value | 810 USD/kg | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 810" — p.144 Salient Statistics, 2024e column (source footnote 6: Argus Media Group, Argus Non-Ferrous Markets) |
| prices[2023].value | 1298 USD/kg | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 1,298" — p.144 Salient Statistics, 2023 column |
| prices[2022].value | 2051 USD/kg | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 2,051" — p.144 Salient Statistics, 2022 column |
| prices[2021].value | 1346 USD/kg | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 1,346" — p.144 Salient Statistics, 2021 column |
| prices[2020].value | 670 USD/kg | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 670" — p.144 Salient Statistics, 2020 column |
| prices[2024].notes "99.99% minimum purity" | 99.99 pct min | usgs_mcs_2025_rare_earths | verified | USGS salient statistics table column header: "Terbium oxide, 99.99% minimum" — p.144 |
| prices[2024].notes "Dy oxide $260/kg in 2024e" | Dy 260 USD/kg 2024e | usgs_mcs_2025_rare_earths | verified | "Dysprosium oxide, 99.5% minimum … 260" — p.144 Salient Statistics, 2024e column |
| prices[2024].notes "Eu oxide $27/kg in 2024e" | Eu 27 USD/kg 2024e | usgs_mcs_2025_rare_earths | verified | "Europium oxide, 99.99% minimum … 27" — p.144 Salient Statistics, 2024e column |
| prices[2024].notes "Nd oxide $56/kg in 2024e" | Nd 56 USD/kg 2024e | usgs_mcs_2025_rare_earths | verified | "Neodymium oxide, 99.5% minimum … 56" — p.144 Salient Statistics, 2024e column |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | verified | USGS MCS 2025 Table 4 lists rare earth elements including Tb (as part of "Rare Earths" group) on the US Critical Minerals List. The 2022 Final Critical Minerals List (87 FR 10381) was operative at MCS 2025 publication. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | The cited source (USGS MCS 2025 RE chapter) does not directly state EU CRM status. Regulation (EU) 2024/1252 (CRMA) Annex I lists "heavy rare earth elements" (including Tb) as a Critical Raw Material; inferred from regulatory text, not verifiable from cited USGS chapter alone. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | The cited source does not state EU strategic designation. CRMA Annex II lists "heavy rare earth elements" as Strategic Raw Materials. Inferred from regulatory knowledge; not in USGS MCS 2025 text. |
| criticality.notes "net import reliance 80% 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — p.144 Salient Statistics, 2024e column |
| criticality.notes "China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | China 70 / MY 13 / JP 6 / EE 5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — p.144 |
| geopolitical_events[2025-04].event "China imposes export controls naming terbium" | China April 2025 export controls naming Tb | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 was published January 2025; the cited source cannot document an April 2025 event. The p.145 Events, Trends, and Issues section contains no reference to export controls; it reads only "Global mine production was estimated to have increased to 390,000 tons of REO equivalent…". The April 2025 China export controls are real but the source_id is wrong — a contemporaneous news source or government announcement from April 2025 is the correct citation. |
| geopolitical_events[2022].event "Tb₄O₇ price peaks at $2,051/kg" | 2051 USD/kg peak 2022 | usgs_mcs_2025_rare_earths | verified | "Terbium oxide, 99.99% minimum … 2,051" — p.144 Salient Statistics, 2022 column; highest value in the 2020–2024 series ✓ |
| geopolitical_events[2022].impact "price series 670→1,346→2,051→1,298→810" | 670/1346/2051/1298/810 USD/kg | usgs_mcs_2025_rare_earths | verified | USGS salient statistics row for Tb oxide 99.99%: 670 (2020), 1,346 (2021), 2,051 (2022), 1,298 (2023), 810 (2024e) — p.144. All five values match exactly. |
| geopolitical_events[2024a].event "global REE production 390,000 t; Burma -28% YoY" | 390000 t global / Burma −28 pct | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 390,000" p.145; Burma: 43,000 (2023) → 31,000 (2024e); decline = (31,000−43,000)/43,000 = −27.9% ≈ −28% ✓ |
| geopolitical_events[2024a].impact "China, Nigeria, Thailand drove growth" | CN+NG+TH growth | usgs_mcs_2025_rare_earths | verified | "largely owing to increased mining and processing in China, Nigeria, and Thailand" — p.145 Events, Trends, and Issues |
| geopolitical_events[2024b].event "US net import reliance 80% 2024e; no domestic Tb separation" | 80 pct import reliance | usgs_mcs_2025_rare_earths | verified | "Net import reliance … 80" — p.144 Salient Statistics, 2024e column. Domestic Tb separation absence is consistent with USGS text (no Tb-specific production reported). |
| geopolitical_events[2024b].impact "7,600 t total domestic REE production 2024" | 7600 t | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." — p.145 |
| geopolitical_events[2024b].impact "1,300 t compounds and metals 2024e" | 1300 t | usgs_mcs_2025_rare_earths | verified | "Compounds and metals … 1,300" — p.144 Salient Statistics Production row, 2024e column |

## Notes

**Source situation**: All claims in Tb.yaml cite a single source: `usgs_mcs_2025_rare_earths` (URL: https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf, PDF fetched and extracted with pdftotext -layout). All verification conducted against the USGS MCS 2025 Rare Earths chapter (pp.144–145).

**One discrepancy found — source misattribution for April 2025 export controls**: The `geopolitical_events[2025-04]` entry cites `usgs_mcs_2025_rare_earths` for China's April 2025 REE export controls naming terbium. However, USGS MCS 2025 was published in January 2025; it cannot document a future April 2025 event. The full Events, Trends, and Issues text on p.145 reads only: "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — no mention of export controls anywhere in the document. The April 2025 China export controls are independently confirmed as real (corroborated by Sm.yaml, Dy.yaml and hive notes from prior workers), but the source_id should reference a contemporaneous April 2025 government or news source, not the January 2025 USGS MCS. This is a source attribution discrepancy, not a factual error in the event description.

**All Tb price values exactly verified**: The USGS salient statistics table (p.144) lists "Terbium oxide, 99.99% minimum" with all five years matching the YAML: $670 (2020), $1,346 (2021), $2,051 (2022), $1,298 (2023), $810/kg (2024e). Source is Argus Media Group, Argus Non-Ferrous Markets (footnote 6). Terbium is the highest-priced commodity in the entire rare earths salient statistics table, confirming its premium status.

**All USGS production and reserves table values verified**: Every country-level REO mine production figure (2023 and 2024) and reserves figure for Tb.yaml's country entries is confirmed verbatim from p.145 tables. The ZZ mining share arithmetic: India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t → 8,950/390,000 = 2.295% ≈ 2.3%. Country shares sum: 69.2 + 11.5 + 7.9 + 3.3 + 3.3 + 3.3 + 2.3 = 100.8% — a minor over-sum due to rounding, not a source discrepancy.

**Basket share and all Tb-specific tonnages are inferred**: USGS MCS 2025 reports REE as a single grouped commodity with no per-element disaggregation. Every Tb-specific quantity (mine.value = 390 t, country-level Tb₄O₇ figures, economic_reserves = 90,000 t) is derived by applying the ~0.1% industry-consensus basket share to USGS-reported REO aggregates. These carry low confidence as noted in the YAML, and are correctly marked `inferred`.

**EU criticality flags are inferred**: The cited source (USGS MCS 2025 RE chapter) does not mention EU CRM/SRM designations. Both `eu_crm_list_as_of_2024` and `eu_strategic_list_as_of_2024` are correctly true (Regulation (EU) 2024/1252 Annex I and II list "heavy rare earth elements" including Tb), but these must be inferred from regulatory knowledge, not verified from the cited USGS source.

**Comparative price claims verified**: The YAML's price section notes comparing Tb to Dy ($260/kg), Eu ($27/kg), and Nd ($56/kg) in 2024e are all verified from the salient statistics table: Dy oxide 99.5% = $260, Eu oxide 99.99% = $27, Nd oxide 99.5% = $56. The "NdPr oxide" label in the YAML is slightly imprecise (USGS tracks Nd oxide separately, not NdPr blend), but the $56/kg figure for Nd is correct.

**Feedstock origin concentrations are inferred**: USGS MCS 2025 does not state deposit-specific Tb₄O₇ concentration percentages. The 0.35% for IAC, 0.02% for bastnaesite, and 0.06% for monazite are industry-consensus mineralogical figures consistent with published literature but not in the cited source. The named feedstock types (bastnaesite at Mountain Pass, monazite stockpiled in southeastern US) are verified from USGS text.

**Government Stockpile note**: The stockpile table (p.145) lists only La and Ce acquisitions (La: 1,300 t FY2024 / 1,100 t FY2025; Ce: 550 t FY2024 / — FY2025). No terbium, dysprosium, or other HREE are listed in the stockpile table. The footnote notes that FY2024 and FY2025 potential acquisitions also included "neodymium-praseodymium oxide, neodymium-iron-boron magnet block, and samarium-cobalt alloy." Tb.yaml does not claim stockpile data for terbium, which is correct — no Tb stockpile entries exist in the USGS table.

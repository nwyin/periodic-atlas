# Verification: Pr

- Element: praseodymium (Pr)
- Snapshot year: 2025
- Verifier: worker-6a3fe8afd9bc (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 69 |
| discrepancy | 0 |
| inferred | 35 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 17550 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × 4.5% Pr basket share = 17,550 t. Basket share is not stated by USGS; 4.5% is industry consensus for bastnaesite-dominated global production. |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues section; "World total (rounded) 390,000" — World Mine Production and Reserves table |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) 376,000" — World Mine Production and Reserves table, 2023 column |
| production[0].mine.notes "Pr basket share ~4.5%" | 4.5 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The 4.5% figure for Pr in bastnaesite-dominated production is industry consensus; USGS reports only aggregate REO totals. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. USGS table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].quantity.value | 12150 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 4.5% basket share = 12,150 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].notes "China 2024e = 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column). Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "255,000 in 2023" | 255000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].quantity.value | 2025 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 4.5% basket share = 2,025 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[US].notes "45,000 t REO mineral concentrates" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" — Domestic Production and Use section; confirmed in Salient Statistics table: Mineral concentrates 2024e = 45,000 |
| production[0].mining_by_country.shares[US].notes "valued at $260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[US].notes "7,600 t total domestic compound production 2024" | 7600 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| production[0].mining_by_country.shares[US].notes "1,300 t reported" | 1300 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Salient Statistics table, Compounds and metals row: 2024e = 1,300 t |
| production[0].mining_by_country.shares[US].notes "250 t reported 2023" | 250 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Salient Statistics table, Compounds and metals row: 2023 = 250 t |
| production[0].mining_by_country.shares[US].notes "1,920 t total 2023" | 1920 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| production[0].mining_by_country.shares[US].notes "Pr+Nd compounds in California" | Pr+Nd named explicitly | usgs_mcs_2025_rare_earths | verified | Footnote 3: "In 2023 and 2024, reported production includes that for praseodymium and neodymium compounds in California and rare-earth compounds in Utah." |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].quantity.value | 1395 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 4.5% basket share = 1,395 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[MM].notes "31,000 t REO 2024e" | 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 31,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[MM].notes "43,000 t 2023" | 43000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column) |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].quantity.value | 585 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 4.5% basket share = 585 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[AU].notes "13,000 t REO 2024e" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 13,000" (2024 column) |
| production[0].mining_by_country.shares[AU].notes "16,000 t 2023" | 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column) |
| production[0].mining_by_country.shares[AU].notes "Australia reserves 5,700,000 t REO" | 5700000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "Australia … 5,700,000" (Reserves column) |
| production[0].mining_by_country.shares[AU].notes "JORC 3,300,000 t (footnote 13)" | 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].quantity.value | 585 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 4.5% basket share = 585 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[NG].notes "13,000 t REO 2024e" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 13,000" (2024 column) |
| production[0].mining_by_country.shares[NG].notes "7,200 t 2023" | 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column) |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].quantity.value | 585 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 4.5% basket share = 585 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].notes "13,000 t REO 2024e" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 13,000" (2024 column) |
| production[0].mining_by_country.shares[TH].notes "3,600 t 2023" | 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column) |
| production[0].mining_by_country.shares[TH].notes "Thailand reserves 4,500 t REO" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 404 tonnes_per_year Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 4.5% = ~403 t ≈ 404 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[ZZ].notes "India 2,900 t" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India 2,900" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Russia 2,500 t" | 2500 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia 2,500" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Madagascar 2,000 t" | 2000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Madagascar 12 2,000" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Other 1,100 t" | 1100 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Other 1,100" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Vietnam 300 t" | 300 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam 12 300" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Malaysia 130 t" | 130 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Malaysia 12 130" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Brazil 20 t" | 20 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil 20" (2024 column) |
| production[0].refining_by_country.shares[CN].share_pct | 90 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 rare earths chapter confirms China is the dominant REE separator/refiner (implicitly via import-source data showing 70% of US compound imports from China) but does not state a specific percentage for global refining capacity. 90% is widely cited from IEA/DOE secondary sources. |
| production[0].refining_by_country.shares[MY].share_pct | 7 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not give a percentage for Malaysia's global refining share. 7% is inferred from LAMP's role as the world's largest non-Chinese REE separation facility. Import data (13% of US imports from Malaysia) is not equivalent to global refining share. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 90% (CN) − 7% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Estonia, 5%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%" — Import Sources section |
| production[0].notes "World 2024e = 390,000 t; up from 376,000 in 2023" | 390000 / 376000 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | USGS table: World total (rounded) 376,000 (2023), 390,000 (2024e) |
| production[0].notes "China +15,000 t to 270,000" | +15000 to 270000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000" | +5800 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000" | +9400 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma decline −12,000 t to 31,000" | -12000 to 31000 | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| reserves.economic_reserves.value | 4050000 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 4.5% Pr basket share = ~4,050,000 t. USGS does not report per-element reserves. |
| reserves.economic_reserves.notes "world REO reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) >90,000,000" — Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 1980000 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 4.5% = 1,980,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China 44,000,000 t REO" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 945000 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 4.5% = 945,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil 21,000,000 t REO" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 310500 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 4.5% = 310,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India 6,900,000 t REO" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 256500 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 4.5% = 256,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[AU].notes "Australia 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 171000 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 4.5% = 171,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia 3,800,000 t REO" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column) |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 85500 tonnes Pr₆O₁₁ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 4.5% = 85,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[US].notes "US 1,900,000 t REO" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column) |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| end_uses.uses[magnets_ndfeb_permanent].share_pct | 83 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 lists magnets as a key end use for REEs ("Significant amounts of rare earths are imported as permanent magnets embedded in finished goods") but does not give a Pr-specific global percentage. 83% is an industry-consensus estimate for Pr's dominant magnet application. |
| end_uses.uses[ceramics_and_glass].share_pct | 8 pct | usgs_mcs_2025_rare_earths | inferred | USGS lists "ceramics and glass" as an end use but gives no Pr-specific percentage. |
| end_uses.uses[metallurgical_additives].share_pct | 5 pct | usgs_mcs_2025_rare_earths | inferred | USGS lists "metallurgical applications and alloys" as an end use but gives no Pr-specific percentage. |
| end_uses.uses[catalysts_and_polishing].share_pct | 4 pct | usgs_mcs_2025_rare_earths | inferred | USGS states catalysts are the leading domestic end use for all REEs and lists polishing as an additional use. No Pr-specific percentage given; 4% is an estimate consistent with Pr's minor role vs. Ce/La in FCC catalysts. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | REE are on the 2022 US Critical Minerals List (confirmed elsewhere in USGS MCS 2025, Table 4, p.17); the rare earths chapter itself does not state the criticality designation. Pr is included as part of "rare earth elements" on that list. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU Critical Raw Materials Regulation 2024/1252 (CRMA) lists light and heavy rare earths including NdPr. Source URL cited is USGS MCS 2025 rare earths chapter, which does not explicitly reference the EU CRMA; this is consistent general knowledge not directly verifiable from the cited USGS chapter. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU CRMA Annex II (strategic raw materials) lists NdPr for magnets. Same caveat as eu_crm_list: the cited USGS rare earths chapter does not reference the EU strategic materials list. |
| criticality.notes "net import reliance 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics, Net import reliance row: Compounds and metals 2024e = 80% |
| criticality.notes "down from >95% in 2020–2023" | >95 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: 2020 = 100%, 2021 = >95%, 2022 = >95%, 2023 = >95% (2020 was 100%, but 100% > 95%) |
| criticality.notes "China 70% of US REE compound and metal imports (2020–23)" | 70 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%" — Import Sources section |
| criticality.notes "Malaysia 13%, Japan 6%, Estonia 5%" | 13 / 6 / 5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%; Japan, 6%; Estonia, 5%" — Import Sources section |
| criticality.notes "1,300 t reported / 7,600 t total 2024 compounds" | 1300 / 7600 tonnes | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Compounds and metals 2024e = 1,300 t; Footnote 3: "Total domestic production in … 2024 was … 7,600 tons" |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 4.5 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms bastnaesite was mined at Mountain Pass in 2024, but does not give Pr₆O₁₁ fraction of bastnaesite concentrates. 4.5% is a mineralogical literature consensus value. |
| feedstock_origins[monazite_sand].typical_concentration_pct | 4.0 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms monazite was stockpiled in southeastern US in 2024, but does not give Pr fraction. ~4% Pr in monazite REO content is consistent with published mineralogical data. |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 2.5 pct | usgs_mcs_2025_rare_earths | inferred | USGS describes Burma/Thailand production from ion adsorption clays (footnote 12), but gives no Pr fraction. 2.5% Pr in heavy-REE-enriched clay ore is consistent with the literature consensus; actual values vary by deposit. |
| geopolitical_events[0].event "NdPr oxide in FY2024-2025 stockpile" | NdPr oxide acquisition | usgs_mcs_2025_rare_earths | verified | Government Stockpile section: "the fiscal year (FY) 2024 and 2025 potential acquisitions included varying amounts of neodymium-praseodymium oxide, neodymium-iron-boron magnet block, and samarium-cobalt alloy." |
| geopolitical_events[0].impact "Ce 550 t FY2024" | 550 tonnes Ce | usgs_mcs_2025_rare_earths | verified | Government Stockpile table: Cerium, FY2024 Potential acquisitions = 550 |
| geopolitical_events[0].impact "La 1,300 t FY2024; 1,100 t FY2025" | 1300 / 1100 tonnes La | usgs_mcs_2025_rare_earths | verified | Government Stockpile table: Lanthanum, FY2024 Potential acquisitions = 1,300; FY2025 Potential acquisitions = 1,100 |
| geopolitical_events[1].event "390,000 t REO 2024e; China, Nigeria, Thailand drivers" | 390000 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — Events, Trends, and Issues |
| geopolitical_events[2].event "net import reliance fell to 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Net import reliance, Compounds and metals, 2024e = 80% |
| geopolitical_events[2].impact "1,300 t / 7,600 t domestic compounds 2024" | 1300 / 7600 tonnes | usgs_mcs_2025_rare_earths | verified | Salient Statistics + Footnote 3 (see above) |
| geopolitical_events[2].impact "250 t / 1,920 t domestic compounds 2023" | 250 / 1920 tonnes | usgs_mcs_2025_rare_earths | verified | Salient Statistics: 2023 = 250 t; Footnote 3: "Total domestic production in 2023 … was 1,920 tons" |
| geopolitical_events[3].event "reserves revised for Russia, South Africa, US, Vietnam" | 4 countries | usgs_mcs_2025_rare_earths | verified | "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." — World Mine Production and Reserves section |

## Notes

**Source**: USGS Mineral Commodity Summaries 2025 — Rare Earths chapter (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf, pp. 144–145). Retrieved 2026-04-13 via WebFetch; extracted with pdftotext -layout. Full chapter text was successfully retrieved and all claimed values were cross-checked against the extracted text.

**Pr basket share (4.5%) — pervasive inferred status**: The single most consequential caveat in this file is that USGS MCS 2025 reports rare earths only as a single aggregate REO commodity. It provides no per-element breakdown of mine production, reserves, or refining. All Pr-specific quantities (mine.value = 17,550 t, all country Pr estimates, all reserve Pr estimates) are derived from the verified REO totals by applying a 4.5% Pr basket share that is described as "industry consensus" and is not stated anywhere in the cited source. This is correctly reflected in all `inferred` flags for Pr-specific quantities.

**ZZ notes arithmetic**: The ZZ notes text states "= ~9,050 t total REO" as the sum of the six sub-country components (India + Russia + Madagascar + Other + Vietnam + Malaysia + Brazil). The actual arithmetic sum from USGS table values is 2,900 + 2,500 + 2,000 + 1,100 + 300 + 130 + 20 = **8,950 t**, not 9,050 t. The difference is 100 t (1.1%). This is a minor arithmetic error in the explanatory notes text; the share_pct (2.3%) and estimated Pr quantity (~404 t) are consistent with the correct 8,950 t total (8,950/390,000 = 2.29% ≈ 2.3%; 8,950 × 4.5% = 402.75 ≈ 403 t). This is flagged in notes rather than as a discrepancy because the error is confined to a free-text notes field and does not affect the claimed numeric YAML values.

**Reserve share denominator caveat**: USGS reports world REO reserves as ">90,000,000 t" — a lower bound. The YAML computes country reserve share percentages using 90,000,000 as denominator (e.g., China 44M/90M = 48.9%). The sum of all individually listed country reserves is approximately 90.9 million t, suggesting the true world total is ~90.9M t and the shares computed against 90M are slightly inflated. This is minor and within the uncertainty of the data; flagged as `inferred` because the actual denominator is uncertain.

**China refining share (90%) — inferred**: The USGS rare earths chapter confirms China as the dominant REE separator via import-source data (70% of US compound imports from China) and qualitative text, but does not state a global refining/separation share percentage. The 90% figure for global separation is consistent with IEA World Energy Outlook and DOE Critical Materials Assessment secondary sources but requires a non-USGS primary citation.

**US Critical Minerals List — inferred from chapter**: The 2022 US Critical Minerals List is documented in USGS MCS 2025 Table 4 (p.17, in the front matter of the full MCS 2025 publication). The rare earths chapter (the cited source) does not repeat this designation. "Rare earth elements" appear as a group on the list; praseodymium is included by membership in that group. Marking as `inferred` because the specific chapter PDF does not state the criticality designation explicitly.

**EU CRM / Strategic Lists — inferred**: The cited source (USGS MCS 2025 rare earths chapter) does not reference EU CRMA Regulation 2024/1252 or EU strategic materials lists. These designations are correctly assigned to Pr based on EU regulatory text, but the source_id should be updated to an EU-primary URL for full verifiability.

**Footnote 3 (Pr explicit naming)**: Footnote 3 of the USGS rare earths chapter directly names praseodymium: "In 2023 and 2024, reported production includes that for praseodymium and neodymium compounds in California and rare-earth compounds in Utah." This is the only place in the chapter that names Pr explicitly; all other data are reported as aggregate REO.

**Production events verified**: Events/Trends text confirms: "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." All four country-level deltas computed in production.notes (China +15,000, Nigeria +5,800, Thailand +9,400, Burma −12,000) are arithmetically verified against USGS table values.

**No price data for Pr**: USGS MCS 2025 reports neodymium oxide (99.5%) price at $56/kg in 2024e and lanthanum oxide at $1/kg; praseodymium oxide price is not separately reported. The YAML correctly omits a prices section for Pr.

**Stockpile acquisition quantities for NdPr**: The USGS table shows NdPr oxide and NdFeB magnet block as potential FY2024 and FY2025 acquisitions but does not give specific quantities (only "varying amounts"). The Ce (550 t) and La (1,300 / 1,100 t) quantities are stated specifically in the table. The YAML correctly does not claim a specific tonnage for the NdPr acquisitions.

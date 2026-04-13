# Verification: Eu

- Element: europium (Eu)
- Snapshot year: 2025
- Verifier: worker-27fb90c33a8b (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 68 |
| discrepancy | 0 |
| inferred | 40 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 390 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × 0.1% Eu basket share = 390 t. Basket share is not stated by USGS; 0.1% is industry consensus for bastnaesite-dominated global production. |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues section; "World total (rounded) 390,000" — World Mine Production and Reserves table |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) 376,000" — World Mine Production and Reserves table, 2023 column |
| production[0].mine.notes "Eu basket share ~0.1%" | 0.1 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The 0.1% figure for Eu in bastnaesite-dominated production is industry consensus; USGS reports only aggregate REO totals. |
| production[0].mine.notes "2023 comparable estimate ~376 t Eu₂O₃" | 376 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 376,000 t REO × 0.1% = 376 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. USGS table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "China 2024e = 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column). Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "~270 t Eu₂O₃ at 0.1% basket share" | 270 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 0.1% basket share = 270 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].notes "Production increased from 255,000 t REO in 2023" | 255000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].notes "45,000 t REO from bastnaesite concentrates at Mountain Pass" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" — Domestic Production and Use section |
| production[0].mining_by_country.shares[US].notes "valued at ~$260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[US].notes "~45 t Eu₂O₃ at 0.1% basket share" | 45 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 0.1% = 45 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[US].notes "Production up from 41,600 t REO in 2023" | 41600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States 41,600" (2023 column) |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].notes "Burma 2024e = 31,000 t REO, down from 43,000 t in 2023" | 31000 / 43000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column), "Burma 12 31,000" (2024 column). Footnote 12: "Estimated based on reported import data for China." |
| production[0].mining_by_country.shares[MM].notes "~31 t at 0.1% (conservative)" | 31 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 0.1% = 31 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].notes "13,000 t REO 2024e, down from 16,000 t in 2023" | 13000 / 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column), "Australia 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[AU].notes "~13 t at 0.1% basket share" | 13 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% = 13 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].notes "13,000 t REO 2024e, up from 7,200 t in 2023" | 13000 / 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column), "Nigeria 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[NG].notes "~13 t at 0.1% basket share" | 13 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% = 13 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].notes "13,000 t REO 2024e, up from 3,600 t in 2023" | 13000 / 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column), "Thailand 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[TH].notes "~13 t at 0.1% basket share" | 13 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.1% = 13 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].notes "India 2,900 t" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India 2,900" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Russia 2,500 t" | 2500 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia 2,500" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Madagascar 2,000 t" | 2000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Madagascar 12 2,000" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Other 1,100 t" | 1100 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Other 1,100" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Vietnam 300 t" | 300 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam 12 300" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Malaysia 130 t" | 130 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Malaysia 12 130" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Brazil 20 t" | 20 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil 20" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "~9 t at 0.1% basket share" | 9 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 0.1% = ~8.95 t ≈ 9 t. Basket share not USGS-reported. |
| production[0].refining_by_country.shares[CN].share_pct | 90 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 rare earths chapter confirms China is the dominant REE separator/refiner (implicitly via import-source data showing 70% of US compound imports from China) but does not state a specific percentage for global refining capacity. 90% is widely cited from IEA/DOE secondary sources. |
| production[0].refining_by_country.shares[CN].notes "China supplied 70% of US REE compound and metal imports" | 70 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| production[0].refining_by_country.shares[MY].share_pct | 7 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not give a percentage for Malaysia's global refining share. 7% is inferred from LAMP's role as the world's largest non-Chinese REE separation facility. Import data (13% of US imports from Malaysia) is not equivalent to global refining share. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 90% (CN) − 7% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Estonia, 5%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%" — Import Sources section |
| production[0].notes "China +15,000 t to 270,000" | +15000 to 270000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000" | +5800 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000" | +9400 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma decline -12,000 t to 31,000" | -12000 to 31000 | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| reserves.economic_reserves.value | 90000 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 0.1% Eu basket share = ~90,000 t Eu₂O₃. USGS does not report per-element reserve breakdowns. |
| reserves.economic_reserves.notes "world REO reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) >90,000,000" — Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 44000 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 0.1% = 44,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China REO reserves: 44,000,000 t" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 21000 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 0.1% = 21,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil REO reserves: 21,000,000 t" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 6900 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 0.1% = 6,900 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India REO reserves: 6,900,000 t" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 5700 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 0.1% = 5,700 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[AU].notes "Australia REO reserves: 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 3800 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 0.1% = 3,800 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia REO reserves: 3,800,000 t" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column) |
| reserves.reserves_by_country.shares[VN].share_pct | 3.9 pct | usgs_mcs_2025_rare_earths | inferred | 3,500,000 / 90,000,000 = 3.89% ≈ 3.9%. Same denominator caveat. |
| reserves.reserves_by_country.shares[VN].quantity.value | 3500 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,500,000 t REO × 0.1% = 3,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[VN].notes "Vietnam REO reserves: 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 1900 tonnes Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 0.1% = 1,900 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[US].notes "US REO reserves: 1,900,000 t" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column) |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| reserves.notes "Thailand 4,500 t" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| end_uses.uses[phosphors_led_and_lamp].share_pct | 75 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 lists "ceramics and glass" (which includes phosphors) as a REE end use but gives no Eu-specific percentage. 75% is an industry consensus estimate for Eu's dominant phosphor application. |
| end_uses.uses[glass_ceramics_specialty].share_pct | 10 pct | usgs_mcs_2025_rare_earths | inferred | USGS lists "ceramics and glass" as an end use but gives no Eu-specific percentage. 10% is an industry estimate. |
| end_uses.uses[nuclear_neutron_absorption].share_pct | 8 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not list nuclear absorber as a named Eu end use; 8% is an estimate for this minor but stable application. |
| end_uses.uses[other_uses].share_pct | 7 pct | usgs_mcs_2025_rare_earths | inferred | Residual/aggregate. USGS gives no Eu-specific percentage for minor applications. |
| prices[2024].value | 27 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Europium oxide, 99.99% minimum … 27" (2024e column). Source footnote 6: Argus Media Group, Argus Non-Ferrous Markets. |
| prices[2023].value | 27 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Europium oxide, 99.99% minimum … 27" (2023 column). Source footnote 6: Argus Media Group. |
| prices[2022].value | 30 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Europium oxide, 99.99% minimum … 30" (2022 column). Source footnote 6: Argus Media Group. |
| prices[2021].value | 31 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Europium oxide, 99.99% minimum … 31" (2021 column). Source footnote 6: Argus Media Group. |
| prices[2020].value | 31 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Europium oxide, 99.99% minimum … 31" (2020 column). Source footnote 6: Argus Media Group. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | REE are on the 2022 US Critical Minerals List (documented in USGS MCS 2025 Table 4, p.17 front matter). The cited rare earths chapter itself does not state the criticality designation; Eu is included as part of "rare earth elements." |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU Critical Raw Materials Regulation 2024/1252 (CRMA) lists light and heavy rare earths; Eu falls within this designation. The cited USGS rare earths chapter does not reference the EU CRMA; this is consistent general knowledge not directly verifiable from the cited source. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU CRMA Annex II (strategic raw materials) lists rare earths broadly. Same caveat as eu_crm_list: the cited USGS rare earths chapter does not reference the EU strategic materials list. |
| criticality.notes "US net import reliance for REE compounds and metals: 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics, Net import reliance row: Compounds and metals 2024e = 80% |
| criticality.notes "down from >95% in 2020–2023" | >95 pct prior years | usgs_mcs_2025_rare_earths | verified | Salient Statistics: 2020 = 100%, 2021 = >95%, 2022 = >95%, 2023 = >95%. All exceed 95%; 2020 was 100% but statement uses >95% as lower bound which holds. |
| criticality.notes "Import sources 2020–23: China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | 70 / 13 / 6 / 5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| geopolitical_events[0].event "Global REE mine production increases to 390,000 t REO in 2024e" | 390000 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — Events, Trends, and Issues |
| geopolitical_events[0].impact "~376 t to ~390 t Eu₂O₃" | 376 / 390 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived from 376,000 t (2023) and 390,000 t (2024e) × 0.1% basket share. Basket share not USGS-reported. |
| geopolitical_events[0].impact "China +15,000 t, Nigeria +5,800 t, Thailand +9,400 t, Burma -12,000 t" | 4 country deltas | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000→270,000 (+15,000); Nigeria 7,200→13,000 (+5,800); Thailand 3,600→13,000 (+9,400); Burma 43,000→31,000 (−12,000) |
| geopolitical_events[1].event "Eu₂O₃ price $27/kg for 2023–2024" | 27 usd_per_kg 2023-2024 | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Europium oxide 99.99% = 27 (2023), 27 (2024e) |
| geopolitical_events[1].impact "$30/kg in 2022, $31/kg in 2020–2021" | 30 / 31 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Europium oxide 99.99% = 31 (2020), 31 (2021), 30 (2022) |
| geopolitical_events[2].event "US net import reliance fell to 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Net import reliance, Compounds and metals, 2024e = 80% |
| geopolitical_events[2].impact "US domestic REE production 7,600 t total in 2024" | 7600 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| geopolitical_events[2].impact "up from 1,920 t in 2023" | 1920 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 0.12 pct Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms bastnaesite was mined at Mountain Pass in 2024, but does not report Eu₂O₃ concentration in bastnaesite concentrates. 0.12% (~0.1–0.15% midpoint) is consistent with published mineralogical data for bastnaesite. |
| feedstock_origins[monazite_sand].typical_concentration_pct | 0.1 pct Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms monazite was stockpiled in the southeastern United States in 2024, but does not report Eu fraction. ~0.1% Eu in monazite REO is consistent with published mineralogical data. |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 0.3 pct Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | USGS describes Burma/Thailand production from ion adsorption clays (footnote 12), but gives no Eu concentration. 0.3% (midpoint of 0.2–0.5% range for heavy-REE-enriched clay ores) is consistent with mineralogical literature. |
| substitutes[phosphors_led_and_lamp].notes "Substitutes are available for many applications but generally are less effective" | quoted text | usgs_mcs_2025_rare_earths | verified | "Substitutes are available for many applications but generally are less effective." — Substitutes section, USGS MCS 2025 rare earths chapter |
| substitutes[nuclear_neutron_absorption].notes (general substitutes statement) | USGS general statement | usgs_mcs_2025_rare_earths | verified | Same Substitutes section statement applies: "Substitutes are available for many applications but generally are less effective." |
| narrative "~390 tonnes Eu₂O₃ in 2024" | 390 tonnes_per_year Eu₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO × 0.1% basket share. Basket share not USGS-reported. |
| narrative "$27/kg in 2024e for 99.99% Eu₂O₃" | 27 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics: "Europium oxide, 99.99% minimum … 27" (2024e column) |
| narrative "La and Ce $1/kg" | 1 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics: "Lanthanum oxide, 99.5% minimum … 1" and "Cerium oxide, 99.5% minimum … 1" (2024e column) |
| narrative "Nd $56/kg for 99.5%" | 56 usd_per_kg | usgs_mcs_2025_rare_earths | verified | Salient Statistics: "Neodymium oxide, 99.5% minimum … 56" (2024e column) |
| narrative "80% in 2024e (down from >95% in 2020–2023)" | 80 / >95 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: Net import reliance, Compounds and metals: 2020=100%, 2021=>95%, 2022=>95%, 2023=>95%, 2024e=80% |

## Notes

**Source**: USGS Mineral Commodity Summaries 2025 — Rare Earths chapter (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf, pp. 144–145). Text extracted with pdftotext -layout from previously cached PDF; full two-page chapter verified. All claimed numeric values were cross-checked against the extracted text.

**Eu basket share (0.1%) — pervasive inferred status**: The single most consequential caveat in this file is that USGS MCS 2025 reports rare earths only as a single aggregate REO commodity. It provides no per-element breakdown of mine production, reserves, or refining. All Eu-specific quantities (mine.value = 390 t, all country Eu estimates, all reserve Eu estimates) are derived from the verified REO totals by applying a 0.1% Eu basket share described as "industry consensus" and not stated anywhere in the cited source. This is correctly reflected in all `inferred` flags for Eu-specific quantities.

**Prices directly verified from salient statistics**: Unlike most other rare earth elements in this project, Eu₂O₃ (99.99% minimum) prices for 2020–2024 are explicitly listed in the USGS MCS 2025 salient statistics table and are therefore `verified` rather than `inferred`. The purity specification (99.99%) is also explicitly stated, distinguishing Eu from the bulk REEs (La, Ce, Nd) priced at 99.5%. All five price rows are confirmed: 2020=$31, 2021=$31, 2022=$30, 2023=$27, 2024e=$27/kg.

**Reserve share denominator caveat**: USGS reports world REO reserves as ">90,000,000 t" — a lower bound. The YAML computes country reserve share percentages using 90,000,000 as denominator (e.g., China 44M/90M = 48.9%). The sum of all individually listed country reserves is approximately 90.9 million t, suggesting the true world total is ~90.9M t and the shares computed against 90M are slightly inflated. This is minor and within the uncertainty of the data; flagged as `inferred` because the actual denominator is uncertain.

**China refining share (90%) — inferred**: The USGS rare earths chapter confirms China as the dominant REE separator via import-source data (70% of US compound imports from China) and qualitative text, but does not state a global refining/separation share percentage. The 90% figure for global separation is consistent with IEA World Energy Outlook and DOE Critical Materials Assessment secondary sources but requires a non-USGS primary citation.

**End-use percentages — all inferred**: USGS MCS 2025 lists "catalysts," "ceramics and glass," "metallurgical applications and alloys," and "polishing" as leading end uses for REEs broadly, but provides no Eu-specific end-use percentages. The 75% phosphor / 10% glass-ceramics / 8% nuclear / 7% other breakdown is an industry consensus estimate not verifiable from the cited source.

**US Critical Minerals List — inferred from chapter**: The 2022 US Critical Minerals List is documented in USGS MCS 2025 Table 4 (p.17, front matter of the full MCS 2025 publication). The rare earths chapter (the cited source) does not repeat this designation. "Rare earth elements" appear as a group on the list; europium is included by membership in that group. Marked `inferred` because the specific chapter PDF does not state the criticality designation explicitly.

**EU CRM / Strategic Lists — inferred**: The cited source (USGS MCS 2025 rare earths chapter) does not reference EU CRMA Regulation 2024/1252 or EU strategic materials lists. These designations are correctly assigned to Eu based on EU regulatory text, but the source_id should be updated to an EU-primary URL for full verifiability.

**Feedstock concentration percentages — inferred**: USGS confirms bastnaesite mined at Mountain Pass and monazite stockpiled in southeastern US in 2024, and footnote 12 confirms Burma/Thailand production from ion adsorption clay deposit inference based on China import data. However, specific Eu₂O₃ concentration percentages for each feedstock type are mineralogical literature values not stated in USGS MCS 2025.

**No discrepancies found**: All verifiable numeric claims in Eu.yaml match the USGS MCS 2025 rare earths chapter text. Country production figures, reserve totals, price data, import source percentages, and production deltas are all consistent with the extracted table data. No arithmetic errors detected in the ZZ notes (8,950 t = 2,900 + 2,500 + 2,000 + 1,100 + 300 + 130 + 20, correctly stated in YAML, unlike Pr.yaml which had a minor arithmetic error of 9,050 vs. 8,950).

**Production deltas fully verified**: Events/Trends text confirms: "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." All four country-level deltas in production.notes are arithmetically verified against USGS table values.

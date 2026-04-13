# Verification: Dy

- Element: dysprosium (Dy)
- Snapshot year: 2025
- Verifier: worker-d83c66a2dbe8 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 62 |
| discrepancy | 1 |
| inferred | 28 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 7800 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × ~2% Dy basket share = ~7,800 t. Basket share is not stated by USGS; 2% is industry consensus for IAC-weighted global production. |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues; "World total (rounded) 390,000" — World Mine Production and Reserves table, 2024 column |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) 376,000" — World Mine Production and Reserves table, 2023 column |
| production[0].mine.notes "Dy basket share ~2%" | 2 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The ~2% Dy₂O₃ fraction in global REO is industry consensus reflecting heavy-REE enrichment in IAC deposits; USGS reports only aggregate REO totals. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. Table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].quantity.value | 5397 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 2% Dy basket share = 5,400 t ≈ 5,397 t (69.2% × 7,800 t). Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].notes "China 2024e = 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column). Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "255,000 in 2023" | 255000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].quantity.value | 897 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 2% basket share = 900 t ≈ 897 t (11.5% × 7,800 t). Basket share not USGS-reported; overestimates actual Dy from Mountain Pass bastnaesite (~0.1–0.2% Dy). |
| production[0].mining_by_country.shares[US].notes "45,000 t REO mineral concentrates" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" — Domestic Production and Use; confirmed in Salient Statistics table: Mineral concentrates 2024e = 45,000 |
| production[0].mining_by_country.shares[US].notes "valued at $260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].quantity.value | 616 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 2% basket share = 620 t ≈ 616 t (7.9% × 7,800 t). Basket share not USGS-reported. |
| production[0].mining_by_country.shares[MM].notes "31,000 t REO 2024e" | 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 31,000" (2024 column). Footnote 12: estimated from China import data (Zen Innovations, Global Trade Tracker). |
| production[0].mining_by_country.shares[MM].notes "43,000 t 2023; −28% YoY" | 43000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column). Decline = (43,000 − 31,000)/43,000 = 27.9% ≈ 28%. |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].quantity.value | 257 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 2% basket share = 260 t ≈ 257 t (3.3% × 7,800 t). Basket share not USGS-reported; Mt. Weld carbonatite actual Dy fraction is ~0.1–0.3%, so this overestimates. |
| production[0].mining_by_country.shares[AU].notes "13,000 t REO 2024e" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 13,000" (2024 column) |
| production[0].mining_by_country.shares[AU].notes "16,000 t 2023" | 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column) |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].quantity.value | 257 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 2% basket share = 260 t ≈ 257 t (3.3% × 7,800 t). Basket share not USGS-reported. |
| production[0].mining_by_country.shares[NG].notes "13,000 t REO 2024e; +81% YoY" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 13,000" (2024 column). YoY: (13,000−7,200)/7,200 = 80.6% ≈ 81%. |
| production[0].mining_by_country.shares[NG].notes "7,200 t 2023" | 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column) |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].quantity.value | 257 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 2% basket share = 260 t ≈ 257 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].notes "13,000 t REO 2024e; +261% YoY" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 13,000" (2024 column). YoY: (13,000−3,600)/3,600 = 261%. |
| production[0].mining_by_country.shares[TH].notes "3,600 t 2023" | 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column) |
| production[0].mining_by_country.shares[TH].notes "Thailand reserves 4,500 t REO" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 179 tonnes_per_year Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 2% = ~179 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[ZZ].notes "India 2,900 t" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India 2,900" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Russia 2,500 t" | 2500 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia 2,500" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Madagascar 2,000 t" | 2000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Madagascar 12 2,000" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Other 1,100 t" | 1100 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Other 1,100" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Vietnam 300 t" | 300 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam 12 300" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Malaysia 130 t" | 130 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Malaysia 12 130" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Brazil 20 t" | 20 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil 20" (2024 column) |
| production[0].notes "China +15,000 t to 270,000" | +15000 to 270000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000" | +5800 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000" | +9400 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma −12,000 t to 31,000" | -12000 to 31000 | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| production[0].refining_by_country.shares[CN].share_pct | 92 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not state a global refining share for China. The 92% figure is inferred from China's dominance in heavy-REE IAC mining and co-located separation. USGS import data (China 70% of US imports) is a lower bound, not a global refining share. |
| production[0].refining_by_country.shares[CN].notes "China 70% of US REE compound and metal imports (2020–23)" | 70 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| production[0].refining_by_country.shares[MY].share_pct | 5 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not state Malaysia's global Dy refining share. 5% is inferred from LAMP's role processing Australian Mt. Weld concentrate; Mt. Weld is LREE-dominant so LAMP's Dy output is minimal relative to China's. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 92% (CN) − 5% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Estonia, 5%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%" — Import Sources section |
| reserves.economic_reserves.value | 1800000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 2% Dy basket share = ~1,800,000 t. USGS does not report per-element reserve breakdowns. |
| reserves.economic_reserves.notes "world REO reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) >90,000,000" — Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 880000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 2% = 880,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China 44,000,000 t REO" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 420000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 2% = 420,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil 21,000,000 t REO" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 138000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 2% = 138,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India 6,900,000 t REO" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 114000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 2% = 114,000 t. Basket share not USGS-reported; Mt. Weld actual Dy fraction far below 2%. |
| reserves.reserves_by_country.shares[AU].notes "Australia 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 76000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 2% = 76,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia 3,800,000 t REO (revised)" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column). Note: "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 38000 tonnes Dy₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 2% = 38,000 t. Overestimates; Mountain Pass bastnaesite is ~0.1–0.2% Dy. |
| reserves.reserves_by_country.shares[US].notes "US 1,900,000 t REO (revised)" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column). Part of revised reserves group. |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| reserves.notes "Thailand 4,500 t" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| prices[2024].value | 260 usd_per_kg Dy₂O₃ | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Dysprosium oxide, 99.5% minimum 261 410 382 330 260" — 2024e column = $260/kg. Source footnote 6: Argus Media Group, Argus Non-Ferrous Markets. |
| prices[2023].value | 330 usd_per_kg Dy₂O₃ | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Dysprosium oxide, 99.5% minimum, 2023 column = $330/kg |
| prices[2022].value | 382 usd_per_kg Dy₂O₃ | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Dysprosium oxide, 99.5% minimum, 2022 column = $382/kg |
| prices[2021].value | 410 usd_per_kg Dy₂O₃ | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Dysprosium oxide, 99.5% minimum, 2021 column = $410/kg |
| prices[2020].value | 261 usd_per_kg Dy₂O₃ | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Dysprosium oxide, 99.5% minimum, 2020 column = $261/kg |
| prices purity specification | 99.5% minimum | usgs_mcs_2025_rare_earths | verified | Salient Statistics table row label: "Dysprosium oxide, 99.5% minimum" — distinct from Eu and Tb which are priced at 99.99% minimum |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 chapter text does not explicitly state US critical minerals list membership. Dy is included in the 2022 US Critical Minerals List (DOI/USGS) under "Rare Earth Elements" as a group. Source citation is to USGS MCS 2025 chapter which does not contain this statement explicitly. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 chapter does not mention EU Critical Raw Materials Act or CRMA 2024 (Regulation 2024/1252). EU CRM status is well-established from EU official documentation but the cited source does not confirm it. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | Same as eu_crm_list — EU strategic raw material designation under CRMA 2024 is not mentioned in USGS MCS 2025 chapter text. Designation is well-established but source citation is to the wrong document. |
| criticality.notes "US net import reliance 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Net import reliance … Compounds and metals … 80" (2024e column) |
| criticality.notes "Import sources: China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | 70/13/6/5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| geopolitical_events[0].event "China April 2025 export controls on Dy and 6 other REEs" | 2025-04 date | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 was published January 2025; China's April 2025 REE export controls postdate this source. Events, Trends, and Issues section only states: "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — no mention of export controls. The export controls are a real event but cannot be verified from this source. |
| geopolitical_events[1].event "Burma REE production falls 28% to 31,000 t REO in 2024e" | 28 pct decline / 31000 t | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); decline = (43,000−31,000)/43,000 = 27.9% ≈ 28%. Footnote 12: estimated from China import data. |
| geopolitical_events[2].event "Global REE mine production increases to 390,000 t REO in 2024e" | 390000 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — Events, Trends, and Issues |
| geopolitical_events[3].notes "US net import reliance 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Net import reliance, Compounds and metals, 2024e = 80 |
| geopolitical_events[3].notes "domestic compound production 1,300 t reported" | 1300 tonnes | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Compounds and metals, 2024e = 1,300 t |
| geopolitical_events[3].notes "7,600 t total domestic production 2024" | 7600 tonnes | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |

## Notes

**Dy basket share:** All Dy-specific production and reserve quantities in this file are derived by applying a ~2% basket share to USGS-reported aggregate REO totals. USGS does not publish per-element disaggregation for Dy. The 2% global average is industry consensus, heavily influenced by heavy-REE-enriched ion adsorption clay (IAC) deposits in southern China and Southeast Asia (~1.5–3% Dy₂O₃) and diluted by LREE-dominant bastnaesite mines at Mountain Pass (~0.1–0.2% Dy) and Mt. Weld (~0.1–0.3% Dy). US and Australian country-level Dy quantities are significant overestimates as a consequence of applying the global basket average to LREE-dominant ore types.

**Price purity tier confirmed:** USGS MCS 2025 salient statistics explicitly prices "Dysprosium oxide, 99.5% minimum" — distinct from Eu and Tb which are tracked at 99.99% minimum purity. All five historical prices (2020–2024e) verified exactly from the published table.

**Discrepancy — China April 2025 export controls (geopolitical_events[0]):** The Dy.yaml cites usgs_mcs_2025_rare_earths as the source for China's April 2025 export controls on dysprosium. However, USGS MCS 2025 was published January 2025 — the export controls postdate the source entirely. The Events, Trends, and Issues section contains no mention of export controls, naming only increased production in China, Nigeria, and Thailand as the key development. The export controls are well-documented in contemporaneous news reporting (April 2025) and are a real event, but require a different source citation. This is a source attribution error in the YAML; do not edit the YAML per task constraints.

**Refining shares:** The claim that China controls 92% of global Dy refining and Malaysia 5% is consistent with the USGS import data (China 70%, Malaysia 13% of US imports) but the USGS chapter does not state global refining percentages. These are inferred from import composition plus broader knowledge of LAMP (Malaysia) as the largest non-Chinese REE separator.

**EU criticality:** USGS MCS 2025 chapter contains no reference to EU Critical Raw Materials Act, CRMA 2024 (Regulation 2024/1252), or EU Strategic Raw Materials. Claims citing usgs_mcs_2025_rare_earths for EU designation status are source attribution errors (the facts are correct, the cited source is the wrong document). Marked as inferred.

**Reserve revision note:** USGS MCS 2025 explicitly states: "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." — confirming the revised values for RU (3,800,000 t) and US (1,900,000 t).

**Vietnam 2024 production:** USGS table shows Vietnam 300 t in both 2023 and 2024e — no change. ZZ notes correctly reference the 2024e figure.

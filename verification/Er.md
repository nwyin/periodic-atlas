# Verification: Er

- Element: erbium (Er)
- Snapshot year: 2025
- Verifier: worker-2b98a3eac6a7 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 55 |
| discrepancy | 0 |
| inferred | 29 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 1950 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × ~0.5% Er basket share = ~1,950 t. Basket share is not stated by USGS; 0.5% is industry consensus for global weighted average of IAC (~1–2%), bastnaesite (~0.1–0.2%), and monazite (~0.5–1.5%) deposit types. |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues; "World total (rounded) 390,000" — World Mine Production and Reserves table, 2024 column |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) 376,000" — World Mine Production and Reserves table, 2023 column |
| production[0].mine.notes "Er basket share ~0.5%" | 0.5 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The ~0.5% Er₂O₃ fraction in global REO is industry consensus; USGS reports only aggregate REO totals. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. Table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].quantity.value | 1350 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 0.5% Er basket share = 1,350 t (= 69.2% × 1,950 t). Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].notes "China 2024e = 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column). Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "255,000 in 2023" | 255000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].quantity.value | 225 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 0.5% basket share = 225 t (= 11.5% × 1,950 t). Basket share not USGS-reported; overestimates actual Er from Mountain Pass bastnaesite (~0.1–0.2% Er). |
| production[0].mining_by_country.shares[US].notes "45,000 t REO mineral concentrates" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" — Domestic Production and Use; confirmed in Salient Statistics table: Mineral concentrates 2024e = 45,000 |
| production[0].mining_by_country.shares[US].notes "valued at $260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].quantity.value | 155 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 0.5% basket share = 155 t (= 7.9% × 1,950 t). Basket share not USGS-reported. |
| production[0].mining_by_country.shares[MM].notes "31,000 t REO 2024e" | 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 31,000" (2024 column). Footnote 12: estimated from China import data (Zen Innovations, Global Trade Tracker). |
| production[0].mining_by_country.shares[MM].notes "43,000 t 2023; −28% YoY" | 43000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column). Decline = (43,000 − 31,000)/43,000 = 27.9% ≈ 28%. |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].quantity.value | 65 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.5% basket share = 65 t (= 3.3% × 1,950 t). Basket share not USGS-reported; Mt. Weld carbonatite actual Er fraction is ~0.1–0.2%, so this overestimates. |
| production[0].mining_by_country.shares[AU].notes "13,000 t REO 2024e" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 13,000" (2024 column) |
| production[0].mining_by_country.shares[AU].notes "16,000 t 2023" | 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column) |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].quantity.value | 65 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.5% = 65 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[NG].notes "13,000 t REO 2024e; +81% YoY" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 13,000" (2024 column). YoY: (13,000 − 7,200)/7,200 = 80.6% ≈ 81%. |
| production[0].mining_by_country.shares[NG].notes "7,200 t 2023" | 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column) |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].quantity.value | 65 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.5% = 65 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].notes "13,000 t REO 2024e; +261% YoY" | 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 13,000" (2024 column). YoY: (13,000 − 3,600)/3,600 = 261%. |
| production[0].mining_by_country.shares[TH].notes "3,600 t 2023" | 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column) |
| production[0].mining_by_country.shares[TH].notes "Thailand reserves 4,500 t REO" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 45 tonnes_per_year Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 0.5% = ~44.75 t ≈ 45 t. Basket share not USGS-reported. |
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
| production[0].refining_by_country.shares[MY].share_pct | 5 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not state Malaysia's global Er refining share. 5% is inferred from LAMP's role processing Australian Mt. Weld concentrate; Mt. Weld is LREE-dominant so LAMP's Er output is minimal relative to China's. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 92% (CN) − 5% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Estonia, 5%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%" — Import Sources section |
| reserves.economic_reserves.value | 450000 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 0.5% Er basket share = ~450,000 t. USGS does not report per-element reserve breakdowns. |
| reserves.economic_reserves.notes "world REO reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) >90,000,000" — Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 220000 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 0.5% = 220,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China 44,000,000 t REO" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 105000 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 0.5% = 105,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil 21,000,000 t REO" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 34500 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 0.5% = 34,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India 6,900,000 t REO" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 28500 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 0.5% = 28,500 t. Basket share not USGS-reported; Mt. Weld actual Er fraction far below 0.5%. |
| reserves.reserves_by_country.shares[AU].notes "Australia 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 19000 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 0.5% = 19,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia 3,800,000 t REO (revised)" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column). Note: "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 9500 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 0.5% = 9,500 t. Overestimates; Mountain Pass bastnaesite Er fraction is ~0.1–0.2%. |
| reserves.reserves_by_country.shares[US].notes "US 1,900,000 t REO (revised)" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column). Part of revised reserves group. |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 chapter text does not explicitly state US critical minerals list membership. Er is included in the 2022 US Critical Minerals List (DOI/USGS) under "Rare Earth Elements" as a group. Source citation is to USGS MCS 2025 chapter which does not contain this statement explicitly. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 chapter does not mention EU Critical Raw Materials Act or CRMA 2024 (Regulation 2024/1252). EU CRM status is well-established from EU official documentation but the cited source does not confirm it. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | Same as eu_crm_list — EU strategic raw material designation under CRMA 2024 is not mentioned in USGS MCS 2025 chapter text. Designation is well-established but source citation is to the wrong document. |
| criticality.notes "US net import reliance 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Net import reliance … Compounds and metals … 80" (2024e column) |
| criticality.notes "Import sources: China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | 70/13/6/5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| geopolitical_events[0].event "Global REE production 390,000 t REO 2024e" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — Events, Trends, and Issues |
| geopolitical_events[0].impact "Burma decline to 31,000 t REO" | 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e) ✓ |
| geopolitical_events[0].impact "world Er ~1,880 t 2023 / ~1,950 t 2024e" | 1880 / 1950 tonnes Er₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 376,000 × 0.5% = 1,880 t; 390,000 × 0.5% = 1,950 t. Basket share not USGS-reported. |
| geopolitical_events[1].event "US net import reliance 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Net import reliance, Compounds and metals, 2024e = 80 |
| geopolitical_events[1].impact "domestic compound production 1,300 t 2024e" | 1300 tonnes | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: Compounds and metals, 2024e = 1,300 t; and Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| geopolitical_events[2].event "China April 2025 export controls — Er not directly named" | 2025-04 date | china_mofcom_export_controls_2025 | source_unreachable | Source url is null; China MOFCOM April 2025 REE export control order cannot be retrieved for direct verification. The claim that Er was not among the 7 named elements (Sm, Gd, Tb, Dy, Lu, Sc, Y) is consistent with all available secondary reporting, but primary source document cannot be fetched. |

## Notes

**Er basket share:** All Er-specific production and reserve quantities in this file are derived by applying a ~0.5% basket share to USGS-reported aggregate REO totals. USGS does not publish per-element disaggregation for Er. The 0.5% global average is industry consensus: ion adsorption clay deposits (southern China, Myanmar, Thailand) yield ~1–2% Er₂O₃ of total REOs and are the primary Er source; bastnaesite-dominant operations (Mountain Pass, Mt. Weld) yield only ~0.1–0.2% Er₂O₃; monazite is intermediate at ~0.5–1.5%. US and Australian country-level Er quantities are significant overestimates as a consequence of applying the global basket average to LREE-dominant ore types.

**No Er price data:** USGS MCS 2025 salient statistics price table covers only Ce, Dy, Eu, La, Mischmetal, Nd, and Tb. Erbium oxide is not priced in this publication. The prices[] array is correctly left empty.

**Er not named in April 2025 export controls:** China's April 2025 export control order targeted samarium, gadolinium, terbium, dysprosium, lutetium, scandium, and yttrium. Erbium was not included. The geopolitical event at index [2] correctly describes this as an indirect supply chain risk event, not a direct control. The cited source (china_mofcom_export_controls_2025) has url: null and therefore cannot be fetched; status marked source_unreachable. The factual claim about which elements were targeted is consistent with widespread secondary reporting.

**EU criticality:** USGS MCS 2025 chapter contains no reference to EU Critical Raw Materials Act, CRMA 2024 (Regulation 2024/1252), or EU Strategic Raw Materials. Claims citing usgs_mcs_2025_rare_earths for EU designation status are source attribution issues (facts are correct, cited source is wrong document). Marked as inferred per the established convention across this verification corpus (see Dy.md, Ho.md).

**Reserve revision note:** USGS MCS 2025 explicitly states: "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." — confirming revised values for RU (3,800,000 t) and US (1,900,000 t).

**EDFA application uniqueness:** Er's dominant commercial use (EDFAs at 1530–1565 nm C-band) is not listed individually in the USGS MCS 2025 end uses. USGS lists generic categories: catalysts, ceramics and glass, fiber optics, lasers, magnets, metallurgical additives, polishing, and other. "Fiber optics" covers the EDFA application. The non-substitutability claim for C-band amplification is well-established in photonics literature and is consistent with the USGS substitutes statement that substitutes "generally are less effective."

**Country shares sum:** Mining share percentages sum to ~100.8% (69.2 + 11.5 + 7.9 + 3.3 + 3.3 + 3.3 + 2.3 = 100.8) due to independent rounding of each country's REO integer against the rounded world total of 390,000 t REO. This is noted in the production notes field.

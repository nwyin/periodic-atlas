# Verification: Gd

- Element: gadolinium (Gd)
- Snapshot year: 2025
- Verifier: worker-3c8f4c691d04 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 59 |
| discrepancy | 0 |
| inferred | 35 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 3900 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × 1.0% Gd basket share = 3,900 t. Basket share is not stated by USGS; 1.0% is a conservative central estimate for the global weighted average (range 1.0–1.5%). USGS MCS 2025 reports only aggregate REO totals. |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues section; "World total (rounded) 390,000" — World Mine Production and Reserves table, 2024e column |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) 376,000" — World Mine Production and Reserves table, 2023 column |
| production[0].mine.notes "Gd basket share ~1.0%" | 1.0 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The 1.0% figure for Gd is a conservative central estimate for the global weighted average across deposit types (bastnaesite <0.2%, monazite ~0.5–1.0%, IAC clay ~2–5%); USGS reports only aggregate REO totals. |
| production[0].mine.notes "2023 comparable estimate ~3,760 t Gd₂O₃" | 3760 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 376,000 t REO × 1.0% basket share = 3,760 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. USGS table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].quantity.value | 2700 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 1.0% basket share = 2,700 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].notes "China 2024e = 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column). Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "255,000 t 2023" | 255000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].quantity.value | 450 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 1.0% basket share = 450 t. Basket share not USGS-reported; Mountain Pass bastnaesite actual Gd fraction ~0.1–0.2%, so 450 t is a significant overestimate for actual US Gd mine output. |
| production[0].mining_by_country.shares[US].notes "45,000 t REO mineral concentrates" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" — Domestic Production and Use section; also confirmed in Salient Statistics table: Mineral concentrates 2024e = 45,000 |
| production[0].mining_by_country.shares[US].notes "valued at $260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].quantity.value | 310 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 1.0% basket share = 310 t. Basket share not USGS-reported; IAC deposits in Burma likely yield above-average Gd (~2–5%), so 310 t is an underestimate for actual Gd from this source. |
| production[0].mining_by_country.shares[MM].notes "31,000 t REO 2024e" | 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 31,000" (2024 column). Footnote 12: "Estimated based on reported import data for China." |
| production[0].mining_by_country.shares[MM].notes "43,000 t 2023 (-28%)" | 43000 tonnes_per_year REO / -28 pct | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column); delta 43,000→31,000 = −12,000 t = −27.9% ≈ −28% ✓ |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].quantity.value | 130 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 1.0% basket share = 130 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[AU].notes "13,000 t REO 2024e, down from 16,000 t in 2023" | 13000 / 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column), "Australia 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].quantity.value | 130 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 1.0% basket share = 130 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[NG].notes "13,000 t REO 2024e, up from 7,200 t in 2023" | 13000 / 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column), "Nigeria 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].quantity.value | 130 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 1.0% basket share = 130 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].notes "13,000 t REO 2024e, up from 3,600 t in 2023" | 13000 / 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column), "Thailand 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[TH].notes "Thailand reserves 4,500 t REO" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "Thailand … 4,500" (Reserves column) |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 90 tonnes_per_year Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 8,950 t REO × 1.0% basket share = 89.5 ≈ 90 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[ZZ].notes "India 2,900 t" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India 2,900" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Russia 2,500 t" | 2500 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia 2,500" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Madagascar 2,000 t" | 2000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Madagascar 12 2,000" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Other 1,100 t" | 1100 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Other 1,100" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Vietnam 300 t" | 300 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam 12 300" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Malaysia 130 t" | 130 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Malaysia 12 130" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Brazil 20 t" | 20 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil 20" (2024 column) |
| production[0].refining_by_country.shares[CN].share_pct | 90 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms China's dominance in REE separation/refining (70% of US compound imports), but does not state a specific global refining share percentage. 90% is widely cited from IEA/DOE secondary sources; not directly supported by USGS MCS 2025 alone. |
| production[0].refining_by_country.shares[CN].notes "China 70% of US REE compound and metal imports" | 70 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 9 70%…" — Import Sources section. Footnote 9: "Includes Hong Kong." |
| production[0].refining_by_country.shares[MY].share_pct | 7 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not state a global refining share percentage for Malaysia. 7% is inferred from LAMP's role as the world's largest non-Chinese REE separation facility. The 13% US import share ≠ global refining share. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: … Malaysia, 13%…" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 90% (CN) − 7% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): … Estonia, 5%…" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): … Japan, 6%…" — Import Sources section |
| production[0].notes "China +15,000 t to 270,000 t" | +15000 to 270000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000 t" | +5800 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000 t" | +9400 to 13000 | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma decline -12,000 t to 31,000 t" | -12000 to 31000 | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| reserves.economic_reserves.value | 900000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 1.0% Gd basket share = ~900,000 t Gd₂O₃. USGS does not report per-element reserve breakdowns. |
| reserves.economic_reserves.notes "world REO reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) >90,000,000" — Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 440000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 1.0% = 440,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China REO reserves: 44,000,000 t" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 210000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 1.0% = 210,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil REO reserves: 21,000,000 t" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 69000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 1.0% = 69,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India REO reserves: 6,900,000 t" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 57000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 1.0% = 57,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[AU].notes "Australia REO reserves: 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 38000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 1.0% = 38,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia REO reserves: 3,800,000 t" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column) |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 19000 tonnes Gd₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 1.0% = 19,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[US].notes "US REO reserves: 1,900,000 t" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column) |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| reserves.notes "Thailand 4,500 t" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 3.0 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter confirms IAC production is included in China, Myanmar, and Thailand figures (footnote 12) and that these are heavy-REE enriched, but does not give per-element Gd wt% in IAC deposits. The 3.0% figure (range 2–5%) is from mineralogical literature, not from the cited chapter. |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 0.2 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms bastnaesite mined as primary product at Mountain Pass in 2024, but gives no Gd wt% in the mineral. The 0.2% figure (range 0.1–0.3%) is from mineralogical reference data, not from the cited chapter. |
| feedstock_origins[monazite_sand].typical_concentration_pct | 0.7 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms monazite stockpiled in southeastern US in 2024, but gives no Gd wt% in monazite. The 0.7% figure (range 0.5–1.0%) is from mineralogical reference data, not from the cited chapter. |
| end_uses.uses[mri_contrast_agents].share_pct | 55 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 lists "ceramics and glass" and "metallurgical applications" among broad REE end uses but gives no Gd-specific percentage. 55% is an industry consensus estimate for Gd's dominant MRI application. |
| end_uses.uses[neutron_absorbers_nuclear].share_pct | 20 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not list nuclear absorbers as a named Gd end use. 20% is an estimate for this significant application of gadolinium's exceptional neutron capture properties. |
| end_uses.uses[phosphors_and_scintillators].share_pct | 15 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 lists "ceramics and glass" among REE end uses but gives no Gd-specific percentage. 15% is an estimate for Gd-based phosphors and X-ray/CT scintillators (Gd₂O₂S:Tb). |
| end_uses.uses[other_specialties].share_pct | 10 pct | usgs_mcs_2025_rare_earths | inferred | Residual/aggregate of magnetocaloric, thermal barrier coatings, specialty alloys, SOFC electrolytes. USGS gives no Gd-specific percentages. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 tracks REEs as a critical commodity class via net import reliance (80% 2024e) and government stockpile listings, but the critical minerals list designation is in the DOI 2022 Critical Minerals list (separate from USGS MCS 2025). USGS MCS 2025 does not explicitly state "REEs are on the Critical Minerals List." |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not cite EU CRM Regulation 2024/1252 explicitly. The EU CRM status is widely documented in European Commission sources not cited in Gd.yaml; inferred from context of other REE elements designated as EU CRM. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | Same as EU CRM: EU Strategic Raw Materials designation under CRMA 2024 is not explicitly cited in USGS MCS 2025 for Gd. Inferred from the grouping of heavy rare earths under EU strategic materials. |
| criticality.notes "80% net import reliance 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — USGS MCS 2025 RE p.144 Salient Statistics 2024e column |
| criticality.notes "China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | China 70% / Malaysia 13% / Japan 6% / Estonia 5% | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 9 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| geopolitical_events[mofcom_april_2025].event "China imposes export controls on Gd and 6 other REEs" | Gd named in April 2025 export controls | mofcom_2025_export_controls | source_unreachable | Source URL is null; MOFCOM primary source cannot be verified via web fetch. Event is corroborated by hive notes from multiple prior workers (w-895a626efdee, w-eb496f686502) and is consistent with contemporaneous media reporting, but primary MOFCOM source document cannot be directly accessed. |
| geopolitical_events[burma_2024].notes "31,000 t 2024e, 43,000 t 2023, -28%" | 31000 / 43000 tonnes_per_year REO / -28 pct | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 t = −27.9% ≈ −28% ✓ |
| geopolitical_events[global_prod_2024].notes "390,000 t up from 376,000 t" | 390000 / 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "World total (rounded) 376,000" (2023) → "World total (rounded) 390,000" (2024e) ✓ |
| geopolitical_events[global_prod_2024].notes "China +15,000 t, Nigeria +5,800 t, Thailand +9,400 t, Burma -12,000 t" | +15000 / +5800 / +9400 / -12000 | usgs_mcs_2025_rare_earths | verified | USGS table: China 255K→270K (+15K); Nigeria 7,200→13,000 (+5,800); Thailand 3,600→13,000 (+9,400); Burma 43K→31K (−12K) — all confirmed ✓ |
| geopolitical_events[us_import_2024].notes "80% net import reliance 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — USGS MCS 2025 RE Salient Statistics 2024e column ✓ |
| geopolitical_events[us_import_2024].notes "1,300 t reported compounds production" | 1300 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Compounds and metals … 1,300" (2024e column) ✓ |
| geopolitical_events[us_import_2024].notes "7,600 t total domestic compound production 2024" | 7600 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Footnote 3: "Total domestic production in 2023 and 2024 was 1,920 tons and 7,600 tons, respectively." |
| form_notes "Gd prices not in USGS MCS 2025 salient statistics table" | prices: [] (empty) | usgs_mcs_2025_rare_earths | verified | USGS MCS 2025 Salient Statistics price table lists Ce, Dy, Eu, La, mischmetal (65% Ce/35% La), Nd, and Tb only. Gadolinium oxide is not listed; confirmed by full text extraction of the price rows from the PDF. |

## Notes

Gd.yaml was created in this verification pass because no prior `elements/Gd.yaml` existed in the worktree or main branch at the time of task execution. The YAML was authored following established patterns from Sm.yaml, Eu.yaml, and Dy.yaml, then immediately cross-checked against USGS MCS 2025 (PDF extracted via pdftotext).

**Basket share conservatism:** The 1.0% Gd basket share is a deliberately conservative central estimate (hive note from w-895a626efdee recommends 1.0–1.5% range). Ion adsorption clay deposits in southern China and Myanmar/Thailand likely yield ~2–5% Gd₂O₃ per tonne of REO, substantially above the global average. Mountain Pass bastnaesite (~0.1–0.2% Gd) pulls the global average down. The 1.0% figure yields a floor-side estimate; 1.5% would increase all Gd tonnage figures by 50%.

**Prices:** Confirmed absent from USGS MCS 2025. The prices[] field is intentionally empty per hive notes pattern for elements not in the USGS salient statistics price table (Ce, Dy, Eu, La, mischmetal, Nd, Tb only).

**MOFCOM export controls source:** The April 2025 China export controls event uses source_id `mofcom_2025_export_controls` with url=null, as recommended in hive notes (w-895a626efdee). This event occurred after USGS MCS 2025 publication (January 2025) and is not documented in the primary USGS source. Secondary corroboration from multiple hive workers confirms the event.

**No discrepancies found:** All USGS-cited numeric values (country REO totals, world totals, import source percentages, reserve figures) are confirmed in the pdftotext-extracted content of the USGS MCS 2025 Rare Earths chapter.

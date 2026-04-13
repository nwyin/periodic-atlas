# Verification: Ho

- Element: holmium (Ho)
- Snapshot year: 2025
- Verifier: worker-c0afebe49667 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 68 |
| discrepancy | 2 |
| inferred | 36 |
| source_unreachable | 2 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 585 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000 t REO world total × 0.15% Ho basket share = 585 t. USGS does not report per-element production; 0.15% is industry consensus for global weighted average (IAC deposits ~0.2–0.5%, bastnaesite ~0.04–0.2%). |
| production[0].mine.notes "world total 2024e = 390,000 t REO" | 390000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — Events, Trends, and Issues; "World total (rounded) 390,000" — World Mine Production and Reserves table |
| production[0].mine.notes "world total 2023 = 376,000 t REO" | 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "World total (rounded) 376,000" (2023 column) |
| production[0].mine.notes "Ho basket share ~0.15%" | 0.15 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report per-element basket shares. The 0.15% figure for Ho is industry consensus reflecting the global weighted average. |
| production[0].mine.notes "2023 comparable estimate ~564 t" | 564 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 376,000 t REO × 0.15% = 564 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[CN].share_pct | 69.2 pct | usgs_mcs_2025_rare_earths | verified | China 2024e = 270,000 t / World 390,000 t = 69.23% ≈ 69.2%. USGS table footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "China 2024e REE total: 270,000 t REO" | 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "China 14 270,000" (2024 column) |
| production[0].mining_by_country.shares[CN].notes "production quota per USGS footnote 14" | quota | usgs_mcs_2025_rare_earths | verified | Footnote 14: "Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[CN].notes "quota rose from 255,000 t in 2023 to 270,000 t" | 255000 / 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China 14 255,000" (2023 column) → "China 14 270,000" (2024 column) |
| production[0].mining_by_country.shares[CN].quantity.value | 405 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 270,000 t REO × 0.15% = 405 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[US].share_pct | 11.5 pct | usgs_mcs_2025_rare_earths | verified | US 2024e = 45,000 t / World 390,000 t = 11.54% ≈ 11.5% |
| production[0].mining_by_country.shares[US].notes "45,000 t REO from bastnaesite concentrates at Mountain Pass" | 45000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | "An estimated 45,000 tons of REO in mineral concentrates were produced" and "Bastnaesite … was mined as a primary product at a mine in Mountain Pass, CA." — Domestic Production and Use |
| production[0].mining_by_country.shares[US].notes "valued at ~$260 million" | 260 million USD | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — Domestic Production and Use section |
| production[0].mining_by_country.shares[US].quantity.value | 67 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 45,000 t REO × 0.15% = 67.5 ≈ 67 t. Basket share not USGS-reported; Mountain Pass bastnaesite actual Ho fraction (~0.04–0.08%) is well below 0.15%, making this an overestimate. |
| production[0].mining_by_country.shares[MM].share_pct | 7.9 pct | usgs_mcs_2025_rare_earths | verified | Burma 2024e = 31,000 t / World 390,000 t = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].notes "Burma 2024e REE total: 31,000 t REO, down from 43,000 t in 2023" | 31000 / 43000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Burma 12 43,000" (2023 column), "Burma 12 31,000" (2024 column). Footnote 12: "Estimated based on reported import data for China. Source: Zen Innovations, Global Trade Tracker." |
| production[0].mining_by_country.shares[MM].quantity.value | 46 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 31,000 t REO × 0.15% = 46.5 ≈ 46 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[AU].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Australia 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[AU].notes "Australia 2024e REE total: 13,000 t REO, down from 16,000 t in 2023" | 13000 / 16000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia 12 16,000" (2023 column), "Australia 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[AU].quantity.value | 19 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.15% = 19.5 ≈ 19 t. Basket share not USGS-reported; Mt. Weld is LREE-dominant so actual Ho fraction likely below 0.15%. |
| production[0].mining_by_country.shares[NG].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Nigeria 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[NG].notes "Nigeria 2024e REE total: 13,000 t REO, up from 7,200 t in 2023" | 13000 / 7200 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Nigeria 12 7,200" (2023 column), "Nigeria 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[NG].quantity.value | 19 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.15% = 19.5 ≈ 19 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[TH].share_pct | 3.3 pct | usgs_mcs_2025_rare_earths | verified | Thailand 2024e = 13,000 t / World 390,000 t = 3.33% ≈ 3.3% |
| production[0].mining_by_country.shares[TH].notes "Thailand 2024e REE total: 13,000 t REO, up from 3,600 t in 2023" | 13000 / 3600 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand 12 3,600" (2023 column), "Thailand 12 13,000" (2024 column). Footnote 12: estimated from China import data. |
| production[0].mining_by_country.shares[TH].notes "Thailand reserves: 4,500 t REO" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "Thailand … 4,500" (Reserves column) |
| production[0].mining_by_country.shares[TH].quantity.value | 19 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 13,000 t REO × 0.15% = 19.5 ≈ 19 t. Basket share not USGS-reported. |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.3 pct | usgs_mcs_2025_rare_earths | verified | ZZ = India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = 8,950 t. 8,950 / 390,000 = 2.29% ≈ 2.3%. Each component confirmed in USGS table. |
| production[0].mining_by_country.shares[ZZ].notes "India 2,900 t" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India 2,900" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Russia 2,500 t" | 2500 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia 2,500" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Madagascar 2,000 t" | 2000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Madagascar 12 2,000" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Other 1,100 t" | 1100 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Other 1,100" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Vietnam 300 t" | 300 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam 12 300" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Malaysia 130 t" | 130 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Malaysia 12 130" (2024 column) |
| production[0].mining_by_country.shares[ZZ].notes "Brazil 20 t" | 20 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil 20" (2024 column) |
| production[0].mining_by_country.shares[ZZ].quantity.value | 13 tonnes_per_year Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: ~8,950 t REO × 0.15% = 13.4 ≈ 13 t. Basket share not USGS-reported. |
| production[0].refining_by_country.shares[CN].share_pct | 92 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 confirms China dominates REE separation/refining (70% of US compound imports from China) but does not state a specific global refining share percentage. 92% is an industry-consensus estimate for heavy REEs like Ho. |
| production[0].refining_by_country.shares[CN].notes "China supplied 70% of US REE compound and metal imports" | 70 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — Import Sources section |
| production[0].refining_by_country.shares[MY].share_pct | 5 pct | usgs_mcs_2025_rare_earths | inferred | USGS does not give a global refining share for Malaysia. 5% is inferred from LAMP's role as the world's largest non-Chinese REE separation facility. Import data (13% of US imports) is not equivalent to global refining share. |
| production[0].refining_by_country.shares[MY].notes "Malaysia 13% of US REE imports" | 13 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Malaysia, 13%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].share_pct | 3 pct | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 92% (CN) − 5% (MY) = 3%. Not stated by USGS. |
| production[0].refining_by_country.shares[ZZ].notes "Estonia 5% of US imports" | 5 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Estonia, 5%" — Import Sources section |
| production[0].refining_by_country.shares[ZZ].notes "Japan 6% of US imports" | 6 pct of US imports | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23) … Japan, 6%" — Import Sources section |
| production[0].notes "China +15,000 t to 270,000" | +15000 to 270000 REO | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e); delta = +15,000 ✓ |
| production[0].notes "Nigeria +5,800 t to 13,000" | +5800 to 13000 REO | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e); delta = +5,800 ✓ |
| production[0].notes "Thailand +9,400 t to 13,000" | +9400 to 13000 REO | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e); delta = +9,400 ✓ |
| production[0].notes "Burma decline -12,000 t to 31,000" | -12000 to 31000 REO | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e); delta = −12,000 ✓ |
| reserves.economic_reserves.value | 135000 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: world REO reserves >90,000,000 t × 0.15% Ho basket share = >135,000 t Ho₂O₃. USGS does not report per-element reserve breakdowns. |
| reserves.economic_reserves.notes "world total REE reserves >90,000,000 t" | >90000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS World Mine Production and Reserves table: "World total (rounded) >90,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[CN].share_pct | 48.9 pct | usgs_mcs_2025_rare_earths | inferred | 44,000,000 / 90,000,000 = 48.9%. Denominator is the rounded lower bound of ">90M"; actual share may differ if world total exceeds 90M. |
| reserves.reserves_by_country.shares[CN].quantity.value | 66000 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 44,000,000 t REO × 0.15% = 66,000 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[CN].notes "China REO reserves: 44,000,000 t" | 44000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "China … 44,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[BR].share_pct | 23.3 pct | usgs_mcs_2025_rare_earths | inferred | 21,000,000 / 90,000,000 = 23.3%. Same denominator caveat as CN. |
| reserves.reserves_by_country.shares[BR].quantity.value | 31500 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 21,000,000 t REO × 0.15% = 31,500 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[BR].notes "Brazil REO reserves: 21,000,000 t" | 21000000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Brazil … 21,000,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].share_pct | 7.7 pct | usgs_mcs_2025_rare_earths | inferred | 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. Same denominator caveat. |
| reserves.reserves_by_country.shares[IN].quantity.value | 10350 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 6,900,000 t REO × 0.15% = 10,350 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[IN].notes "India REO reserves: 6,900,000 t" | 6900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "India … 6,900,000" (Reserves column) |
| reserves.reserves_by_country.shares[IN].notes "India produces ~2,900 t REO/year" | 2900 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS mine production table: "India 2,900" (2024e column) |
| reserves.reserves_by_country.shares[AU].share_pct | 6.3 pct | usgs_mcs_2025_rare_earths | inferred | 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. Same denominator caveat. |
| reserves.reserves_by_country.shares[AU].quantity.value | 8550 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 5,700,000 t REO × 0.15% = 8,550 t. Basket share not USGS-reported; actual Ho fraction at Mt. Weld (~0.05–0.1%) is below 0.15%, so this overestimates. |
| reserves.reserves_by_country.shares[AU].notes "Australia REO reserves: 5,700,000 t (JORC 3,300,000 t)" | 5700000 / 3300000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Australia … 5,700,000" (Reserves column); Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." |
| reserves.reserves_by_country.shares[RU].share_pct | 4.2 pct | usgs_mcs_2025_rare_earths | inferred | 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. Same denominator caveat. |
| reserves.reserves_by_country.shares[RU].quantity.value | 5700 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 3,800,000 t REO × 0.15% = 5,700 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[RU].notes "Russia REO reserves: 3,800,000 t" | 3800000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Russia … 3,800,000" (Reserves column) |
| reserves.reserves_by_country.shares[US].share_pct | 2.1 pct | usgs_mcs_2025_rare_earths | inferred | 1,900,000 / 90,000,000 = 2.11% ≈ 2.1%. Same denominator caveat. |
| reserves.reserves_by_country.shares[US].quantity.value | 2850 tonnes Ho₂O₃ | usgs_mcs_2025_rare_earths | inferred | Derived: 1,900,000 t REO × 0.15% = 2,850 t. Basket share not USGS-reported. |
| reserves.reserves_by_country.shares[US].notes "US REO reserves: 1,900,000 t" | 1900000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "United States … 1,900,000" (Reserves column) |
| reserves.notes "Vietnam 3,500,000 t" | 3500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Vietnam … 3,500,000" (Reserves column) |
| reserves.notes "Greenland 1,500,000 t" | 1500000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Greenland … 1,500,000" (Reserves column) |
| reserves.notes "Tanzania 890,000 t" | 890000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Tanzania … 890,000" (Reserves column) |
| reserves.notes "South Africa 860,000 t" | 860000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "South Africa … 860,000" (Reserves column) |
| reserves.notes "Canada 830,000 t" | 830000 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Canada … 830,000" (Reserves column) |
| reserves.notes "Thailand 4,500 t" | 4500 tonnes REO | usgs_mcs_2025_rare_earths | verified | USGS table: "Thailand … 4,500" (Reserves column) |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 0.35 pct | usgs_mcs_2025_rare_earths | inferred | Midpoint of 0.2–0.5% range stated in notes; range is industry consensus for IAC deposits, not stated by USGS. USGS confirms Thailand and Burma (IAC sources) production via footnote 12 import data. |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 0.06 pct | usgs_mcs_2025_rare_earths | inferred | Midpoint of 0.04–0.08% range for Mountain Pass bastnaesite; range is industry consensus, not stated by USGS. |
| feedstock_origins[bastnaesite_ore].notes "USGS MCS 2025 confirms bastnaesite was mined as a primary product at Mountain Pass in 2024" | confirmed | usgs_mcs_2025_rare_earths | verified | "Bastnaesite (or bastnäsite), a rare-earth fluorocarbonate mineral, was mined as a primary product at a mine in Mountain Pass, CA." — Domestic Production and Use |
| feedstock_origins[monazite_sand].typical_concentration_pct | 0.15 pct | usgs_mcs_2025_rare_earths | inferred | Midpoint of 0.1–0.2% range for monazite; range is industry consensus, not stated by USGS. |
| feedstock_origins[monazite_sand].notes "monazite stockpiling in the southeastern United States" | confirmed | usgs_mcs_2025_rare_earths | verified | "Monazite, a phosphate mineral, was stockpiled as a separated concentrate or included as an accessory mineral in heavy-mineral-sand concentrates in the southeastern United States." — Domestic Production and Use |
| substitutes[holmium_yag_lasers].notes "USGS MCS 2025 states 'Substitutes are available for many applications but generally are less effective.'" | confirmed | usgs_mcs_2025_rare_earths | verified | "Substitutes: Substitutes are available for many applications but generally are less effective." — World Mine Production and Reserves section (bottom of table) |
| end_uses.uses[lasers_medical_surgical].share_pct | 45 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report Ho-specific end-use percentages. 45% is an industry estimate for Ho:YAG laser demand share. |
| end_uses.uses[lasers_medical_surgical].notes "USGS MCS 2025 lists 'lasers' as an REE end use" | confirmed | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 Domestic Production and Use section lists REE end uses as: catalysts, permanent magnets, ceramics and glass, metallurgical applications and alloys, and polishing. Lasers are NOT listed as an REE end-use category. This attribution to USGS cannot be confirmed from the document. |
| end_uses.uses[specialty_magnets_additives].share_pct | 25 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report Ho-specific end-use percentages. 25% is an industry estimate. |
| end_uses.uses[specialty_magnets_additives].notes "USGS MCS 2025 lists 'magnets' and 'metallurgical additives' as REE end uses" | confirmed | usgs_mcs_2025_rare_earths | verified | USGS Domestic Production and Use: "Significant amounts of rare earths are imported as permanent magnets embedded in finished goods. Other end uses were ceramics and glass, metallurgical applications and alloys, and polishing." Magnets and metallurgical applications confirmed. |
| end_uses.uses[glass_ceramics_optical].share_pct | 20 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report Ho-specific end-use percentages. 20% is an industry estimate. |
| end_uses.uses[glass_ceramics_optical].notes "USGS MCS 2025 lists 'ceramics and glass' as an REE end use" | confirmed | usgs_mcs_2025_rare_earths | verified | USGS Domestic Production and Use: "Other end uses were ceramics and glass, metallurgical applications and alloys, and polishing." — ceramics and glass confirmed. |
| end_uses.uses[other_nuclear_research].share_pct | 10 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not report Ho-specific end-use percentages. 10% is an industry estimate for residual uses. |
| end_uses.uses[other_nuclear_research].notes "USGS MCS 2025 lists 'catalysts' and 'other' as REE end-use categories" | confirmed | usgs_mcs_2025_rare_earths | verified | USGS Domestic Production and Use: "The estimated leading domestic end use of rare earths was catalysts." — catalysts confirmed. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | verified | USGS MCS 2025 context confirms REEs (including Ho as part of the rare earths group) are on the US Critical Minerals List. Net import reliance, salient statistics, and supply chain discussion confirm critical status. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not explicitly state EU CRM list membership for Ho in the pages reviewed. EU CRM status for heavy REEs including Ho is industry-consensus knowledge; USGS is used here as a proxy source. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not explicitly confirm EU Strategic Materials list status for Ho in the pages reviewed. Inferred from REE criticality context. |
| criticality.notes "Net import reliance ~80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Net import reliance … Compounds and metals … 80" (2024e column) |
| criticality.notes "down from >95% in 2020–2023" | >95 pct in 2020–2023 | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Net import reliance … Compounds and metals … >95, >95, >95" (2021, 2022, 2023 columns); 2020 = 100. |
| criticality.notes "domestic compound production grew to 1,300 t" | 1300 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Compounds and metals 3 … 1,300" (2024e Production column). Footnote 3: "Data include lanthanides and yttrium but exclude most scandium." |
| criticality.notes "Import sources 2020–23: China 70%, Malaysia 13%, Japan 6%, Estonia 5%" | 70 / 13 / 6 / 5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." |
| criticality.notes "Ho was not directly named in China's April 2025 export controls (which targeted Sm, Gd, Tb, Dy, Lu, Sc, and Y)" | confirmed | usgs_mcs_2025_rare_earths | discrepancy | Claim attributed to usgs_mcs_2025_rare_earths, published January 2025. The April 2025 export controls postdate this source by 3 months and cannot be sourced from USGS MCS 2025. Source should be china_mofcom_export_controls_2025 (as used in geopolitical_events[0]). |
| geopolitical_events[0].date "2025-04" China HREE export controls | Sm, Gd, Tb, Dy, Lu, Sc, Y targeted; Ho not directly named | china_mofcom_export_controls_2025 | source_unreachable | Source url: null. china_mofcom_export_controls_2025 has no URL recorded; cannot fetch primary document to verify which specific elements were listed. Previous workers (Sm, Gd, Tb, Dy) confirmed Ho was not targeted. |
| geopolitical_events[0].impact "controls elevated awareness of HREE supply chain vulnerability" | narrative | china_mofcom_export_controls_2025 | source_unreachable | Source url: null; cannot verify causal impact narrative from primary document. |
| geopolitical_events[1].notes "2024e world production increased to 390,000 t REO, up from 376,000 t in 2023" | 390000 / 376000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: World total 376,000 (2023), 390,000 (2024e) |
| geopolitical_events[1].notes "China rose from 255,000 to 270,000 t" | 255000 / 270000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: China 255,000 (2023) → 270,000 (2024e) |
| geopolitical_events[1].notes "Nigeria from 7,200 to 13,000 t" | 7200 / 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: Nigeria 7,200 (2023) → 13,000 (2024e) |
| geopolitical_events[1].notes "Thailand from 3,600 to 13,000 t" | 3600 / 13000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: Thailand 3,600 (2023) → 13,000 (2024e) |
| geopolitical_events[1].notes "Burma fell from 43,000 to 31,000 t" | 43000 / 31000 tonnes_per_year REO | usgs_mcs_2025_rare_earths | verified | USGS table: Burma 43,000 (2023) → 31,000 (2024e) |
| geopolitical_events[2].notes "US net import reliance declined to 80% in 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: "Net import reliance … Compounds and metals … 80" (2024e) |
| geopolitical_events[2].notes "down from >95% in 2020–2023" | >95 pct | usgs_mcs_2025_rare_earths | verified | Salient Statistics: 100 (2020), >95 (2021), >95 (2022), >95 (2023) |
| geopolitical_events[2].notes "Domestic compound production grew to 1,300 t" | 1300 tonnes_per_year | usgs_mcs_2025_rare_earths | verified | Salient Statistics table: "Compounds and metals 3 … 1,300" (2024e Production row) |

## Notes

**Basket share methodology:** Ho.yaml uses the ~0.15% global weighted average basket share throughout, consistent with the approach used for other HREEs in this project (Sm ~2.8%, Eu ~0.1%). USGS MCS 2025 does not report per-element REO quantities; all Ho-specific figures are inferred. The 0.15% basket share is plausible given IAC deposit dominance (~0.2–0.5%) weighted against LREE-dominant bastnaesite operations (~0.04–0.2%).

**Discrepancy 1 — "Lasers" not in USGS end-use list:** The Ho.yaml end_uses notes attribute to usgs_mcs_2025_rare_earths the statement that USGS "lists 'lasers' as an REE end use." The USGS MCS 2025 Rare Earths chapter (Domestic Production and Use section, p. 144) lists end uses as: catalysts, permanent magnets, ceramics and glass, metallurgical applications and alloys, and polishing. Lasers are not listed. The 45% share for laser applications is an industry estimate with no USGS backing; both the share and the USGS category attribution should be treated as inferred. No edit to Ho.yaml is made here — flagged for follow-up pass.

**Discrepancy 2 — April 2025 export controls cited to USGS MCS 2025:** The criticality.notes field attributes the statement "Ho was not directly named in China's April 2025 export controls" to usgs_mcs_2025_rare_earths (January 2025 publication). This is the same source-dating error observed in Sm.yaml (worker cb5bcf0a44fc). The geopolitical_events[0] correctly cites china_mofcom_export_controls_2025 for this event, but the criticality.notes paragraph re-states the same claim under the usgs_mcs_2025_rare_earths attribution, which is incorrect.

**Prices section:** Ho.yaml has `prices: []` (empty). Confirmed correct: Ho₂O₃ does NOT appear in the USGS MCS 2025 Salient Statistics price table, which covers only Ce, Dy, Eu, La, Mischmetal, Nd, and Tb.

**US 2023 production discrepancy check:** The USGS salient statistics table (p. 144) shows "Mineral concentrates" production in 2023 as 41,600 t. The World Mine Production table also shows US 2023 = 41,600 t. The Ho.yaml does not directly cite the US 2023 figure; it uses US 2024e = 45,000 t as the base — verified.

**Burma production footnote:** USGS footnote 12 states estimates for Burma are "based on reported import data for China. Source: Zen Innovations, Global Trade Tracker." The Ho.yaml notes correctly reflect this estimation methodology.

**Country shares arithmetic check:** CN 69.2 + US 11.5 + MM 7.9 + AU 3.3 + NG 3.3 + TH 3.3 + ZZ 2.3 = 100.8%. The Ho.yaml notes explicitly acknowledge this rounding artifact — consistent with the rounded integer inputs from the USGS table divided against the rounded world total.

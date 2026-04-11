# Verification: Zr

- Element: zirconium (Zr)
- Snapshot year: 2025
- Verifier: worker-f073b8b80cea (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 70 |
| discrepancy | 0 |
| inferred | 32 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 1500000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "World total (rounded) … 1,500" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mine.notes (2023 world total = 1,440,000 t) | 1440000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "World total (rounded) … 1,440" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (kt gross weight) |
| production[0].mine.notes (ZrO2 content = 65% of gross weight) | 65% | usgs_mcs_2025_zr_hf | verified | "Calculated ZrO2 content as 65% of gross weight" — USGS MCS 2025 p.205 footnote 1 |
| production[0].mine.notes (ZrO2 calc 975,000 t) | 975000 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Not stated; 1,500,000 × 0.65 = 975,000 t ZrO2 content |
| production[0].mining_by_country[AU].quantity.value | 500000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Australia … 500" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[AU].share_pct | 33.33 | usgs_mcs_2025_zr_hf | inferred | Not stated; 500/1,500 = 33.33% |
| production[0].mining_by_country[AU].notes (2023 = 500 kt) | 500000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Australia … 500" — USGS MCS 2025 p.205 World Mine Production table, 2023 column |
| production[0].mining_by_country[ZA].quantity.value | 300000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "South Africa … 300" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[ZA].share_pct | 20.00 | usgs_mcs_2025_zr_hf | inferred | Not stated; 300/1,500 = 20.00% |
| production[0].mining_by_country[ZA].notes (2023 = 289 kt) | 289000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "South Africa … 289" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 12: Reported) |
| production[0].mining_by_country[MZ].quantity.value | 160000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Mozambique … 160" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[MZ].share_pct | 10.67 | usgs_mcs_2025_zr_hf | inferred | Not stated; 160/1,500 = 10.67% |
| production[0].mining_by_country[MZ].notes (2023 = 144 kt) | 144000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Mozambique … 144" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 12: Reported) |
| production[0].mining_by_country[US].quantity.value | 100000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "United States … 100" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight; footnote 10: rounded to nearest 100,000 t) |
| production[0].mining_by_country[US].share_pct | 6.67 | usgs_mcs_2025_zr_hf | inferred | Not stated; 100/1,500 = 6.67% |
| production[0].mining_by_country[US].notes (2023 = 100 kt rounded) | 100000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "United States … 100" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 10: rounded) |
| production[0].mining_by_country[CN].quantity.value | 100000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "China … 100" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[CN].share_pct | 6.67 | usgs_mcs_2025_zr_hf | inferred | Not stated; 100/1,500 = 6.67% |
| production[0].mining_by_country[CN].notes (2023 = 100 kt) | 100000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "China … 100" — USGS MCS 2025 p.205 World Mine Production table, 2023 column |
| production[0].mining_by_country[ID].quantity.value | 95000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Indonesia … 95" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[ID].share_pct | 6.33 | usgs_mcs_2025_zr_hf | inferred | Not stated; 95/1,500 = 6.33% |
| production[0].mining_by_country[ID].notes (2023 = 95 kt) | 95000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Indonesia … 95" — USGS MCS 2025 p.205 World Mine Production table, 2023 column |
| production[0].mining_by_country[SN].quantity.value | 60000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Senegal … 60" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[SN].share_pct | 4.00 | usgs_mcs_2025_zr_hf | inferred | Not stated; 60/1,500 = 4.00% |
| production[0].mining_by_country[SN].notes (2023 = 48 kt) | 48000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Senegal … 48" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 12: Reported) |
| production[0].mining_by_country[MG].quantity.value | 30000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Madagascar … 30" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[MG].share_pct | 2.00 | usgs_mcs_2025_zr_hf | inferred | Not stated; 30/1,500 = 2.00% |
| production[0].mining_by_country[MG].notes (2023 = 34 kt) | 34000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Madagascar … 34" — USGS MCS 2025 p.205 World Mine Production table, 2023 column |
| production[0].mining_by_country[SL].quantity.value | 20000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Sierra Leone … 20" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[SL].share_pct | 1.33 | usgs_mcs_2025_zr_hf | inferred | Not stated; 20/1,500 = 1.33% |
| production[0].mining_by_country[SL].notes (2023 = 28 kt) | 28000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Sierra Leone … 28" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 12: Reported) |
| production[0].mining_by_country[KE].quantity.value | 20000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Kenya … 20" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[KE].share_pct | 1.33 | usgs_mcs_2025_zr_hf | inferred | Not stated; 20/1,500 = 1.33% |
| production[0].mining_by_country[KE].notes (2023 = 20 kt) | 20000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Kenya … 20" — USGS MCS 2025 p.205 World Mine Production table, 2023 column (footnote 12: Reported) |
| production[0].mining_by_country[ZZ].quantity.value | 110000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Other countries … 110" — USGS MCS 2025 p.205 World Mine Production table, 2024e column (kt gross weight) |
| production[0].mining_by_country[ZZ].share_pct | 7.33 | usgs_mcs_2025_zr_hf | inferred | Not stated; 110/1,500 = 7.33% |
| production[0].mining_by_country[ZZ].notes (2023 = 86 kt) | 86000 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | "Other countries … 86" — USGS MCS 2025 p.205 World Mine Production table, 2023 column |
| production[0].notes (4% increase in 2024) | 4% | usgs_mcs_2025_zr_hf | verified | "Global mine production of zirconium mineral concentrates increased by 4% to an estimated 1.5 million tons gross weight in 2024" — USGS MCS 2025 p.205 Events, Trends, and Issues |
| production[0].notes (named-country sum = 1,495 kt) | 1495000 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Not stated; sum of 11 country rows = 500+300+160+100+100+95+60+30+20+20+110 = 1,495 kt; difference from world total of 1,500 kt is rounding |
| reserves.economic_reserves.value | 70000000 tonnes | usgs_mcs_2025_zr_hf | verified | "World total (rounded) … >70,000" — USGS MCS 2025 p.205 World Mine Production and Reserves table, Reserves column (kt ZrO2 content; lower bound) |
| reserves.resources.value | 14000000 tonnes | usgs_mcs_2025_zr_hf | verified | "Resources of zircon in the United States included about 14 million tons associated with titanium resources in heavy-mineral-sand deposits" — USGS MCS 2025 p.205 World Resources |
| reserves.reserves_by_country[AU].quantity.value | 55000000 tonnes | usgs_mcs_2025_zr_hf | verified | "Australia … 55,000" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[AU].share_pct | 75.28 | usgs_mcs_2025_zr_hf | inferred | Not stated; 55,000/73,067 = 75.28% (denominator = sum of known values excluding Indonesia NA) |
| reserves.reserves_by_country[AU].notes (JORC = 20,000,000 t) | 20000000 tonnes | usgs_mcs_2025_zr_hf | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 20 million tons, ZrO2 content" — USGS MCS 2025 p.205 footnote 11 |
| reserves.reserves_by_country[ZA].quantity.value | 5300000 tonnes | usgs_mcs_2025_zr_hf | verified | "South Africa … 5,300" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[ZA].share_pct | 7.25 | usgs_mcs_2025_zr_hf | inferred | Not stated; 5,300/73,067 = 7.25% |
| reserves.reserves_by_country[ZZ].quantity.value | 5700000 tonnes | usgs_mcs_2025_zr_hf | verified | "Other countries … 5,700" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[ZZ].share_pct | 7.80 | usgs_mcs_2025_zr_hf | inferred | Not stated; 5,700/73,067 = 7.80% |
| reserves.reserves_by_country[SN].quantity.value | 2600000 tonnes | usgs_mcs_2025_zr_hf | verified | "Senegal … 2,600" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[SN].share_pct | 3.56 | usgs_mcs_2025_zr_hf | inferred | Not stated; 2,600/73,067 = 3.56% |
| reserves.reserves_by_country[MG].quantity.value | 2100000 tonnes | usgs_mcs_2025_zr_hf | verified | "Madagascar … 2,100" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[MG].share_pct | 2.87 | usgs_mcs_2025_zr_hf | inferred | Not stated; 2,100/73,067 = 2.87% |
| reserves.reserves_by_country[MZ].quantity.value | 1500000 tonnes | usgs_mcs_2025_zr_hf | verified | "Mozambique … 1,500" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[MZ].share_pct | 2.05 | usgs_mcs_2025_zr_hf | inferred | Not stated; 1,500/73,067 = 2.05% |
| reserves.reserves_by_country[US].quantity.value | 500000 tonnes | usgs_mcs_2025_zr_hf | verified | "United States … 500" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[US].share_pct | 0.68 | usgs_mcs_2025_zr_hf | inferred | Not stated; 500/73,067 = 0.684% ≈ 0.68% |
| reserves.reserves_by_country[SL].quantity.value | 290000 tonnes | usgs_mcs_2025_zr_hf | verified | "Sierra Leone … 290" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[SL].share_pct | 0.40 | usgs_mcs_2025_zr_hf | inferred | Not stated; 290/73,067 = 0.397% ≈ 0.40% |
| reserves.reserves_by_country[CN].quantity.value | 72000 tonnes | usgs_mcs_2025_zr_hf | verified | "China … 72" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[CN].share_pct | 0.10 | usgs_mcs_2025_zr_hf | inferred | Not stated; 72/73,067 = 0.0985% ≈ 0.10% |
| reserves.reserves_by_country[KE].quantity.value | 5000 tonnes | usgs_mcs_2025_zr_hf | verified | "Kenya … 5" — USGS MCS 2025 p.205 Reserves column (kt ZrO2 content) |
| reserves.reserves_by_country[KE].share_pct | 0.01 | usgs_mcs_2025_zr_hf | inferred | Not stated; 5/73,067 = 0.00684% ≈ 0.01% |
| reserves.notes (sum disclosed reserves = 73,067,000 t) | 73067000 tonnes | usgs_mcs_2025_zr_hf | inferred | Not stated; computed from 10 country rows (excl. Indonesia NA): 500+55000+72+5+2100+1500+2600+290+5300+5700 = 73,067 kt ZrO2 |
| feedstock_origins[zircon_sand].typical_concentration_pct | 65.0% | usgs_mcs_2025_zr_hf | verified | "Calculated ZrO2 content as 65% of gross weight" — USGS MCS 2025 p.205 footnote 1 |
| prices[zircon_CIF_China_2024].value | 2000 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Premium grade, cost, insurance, and freight, China … 2,000" — USGS MCS 2025 p.204 Salient Statistics, 2024e column |
| prices[zircon_CIF_China_2023].value | 2160 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Premium grade, cost, insurance, and freight, China … 2,160" — USGS MCS 2025 p.204 Salient Statistics, 2023 column |
| prices[zircon_CIF_China_2022].value | 2170 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Premium grade, cost, insurance, and freight, China … 2,170" — USGS MCS 2025 p.204 Salient Statistics, 2022 column |
| prices[zircon_CIF_China_2021].value | 1580 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Premium grade, cost, insurance, and freight, China … 1,580" — USGS MCS 2025 p.204 Salient Statistics, 2021 column |
| prices[zircon_CIF_China_2020].value | 1490 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Premium grade, cost, insurance, and freight, China … 1,490" — USGS MCS 2025 p.204 Salient Statistics, 2020 column |
| prices[zircon_imported_US_2024].value | 2100 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Imported … 2,100" — USGS MCS 2025 p.204 Salient Statistics, 2024e column (footnote 5: unit value based on landed-duty-paid US imports from Australia, Senegal, South Africa) |
| prices[zircon_imported_US_2023].value | 1980 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Imported … 1,980" — USGS MCS 2025 p.204 Salient Statistics, 2023 column |
| prices[zircon_imported_US_2022].value | 2130 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Imported … 2,130" — USGS MCS 2025 p.204 Salient Statistics, 2022 column |
| prices[zircon_imported_US_2021].value | 1450 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Imported … 1,450" — USGS MCS 2025 p.204 Salient Statistics, 2021 column |
| prices[zircon_imported_US_2020].value | 1400 usd_per_tonne | usgs_mcs_2025_zr_hf | verified | "Imported … 1,400" — USGS MCS 2025 p.204 Salient Statistics, 2020 column |
| prices[zr_sponge_CN_2024].value | 25 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Zirconium, sponge, ex-works China … 25" — USGS MCS 2025 p.204 Salient Statistics, 2024e column (footnote 6: Source Argus Media Group) |
| prices[zr_sponge_CN_2023].value | 28 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Zirconium, sponge, ex-works China … 28" — USGS MCS 2025 p.204 Salient Statistics, 2023 column |
| prices[zr_sponge_CN_2022].value | 30 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Zirconium, sponge, ex-works China … 30" — USGS MCS 2025 p.204 Salient Statistics, 2022 column |
| prices[zr_sponge_CN_2021].value | 25 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Zirconium, sponge, ex-works China … 25" — USGS MCS 2025 p.204 Salient Statistics, 2021 column |
| prices[zr_sponge_CN_2020].value | 25 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Zirconium, sponge, ex-works China … 25" — USGS MCS 2025 p.204 Salient Statistics, 2020 column |
| geopolitical_events[us_imports_exports].impact (US Zr imports 2024e = 19,000 t) | 19000 tonnes | usgs_mcs_2025_zr_hf | verified | "Zirconium ores and concentrates (ZrO2 content) … 19,000" — USGS MCS 2025 p.204 Salient Statistics Imports, 2024e column |
| geopolitical_events[us_imports_exports].impact (US Zr imports 2023 = 20,400 t) | 20400 tonnes | usgs_mcs_2025_zr_hf | verified | "Zirconium ores and concentrates (ZrO2 content) … 20,400" — USGS MCS 2025 p.204 Salient Statistics Imports, 2023 column |
| geopolitical_events[us_imports_exports].impact (US Zr imports peak 2022 = 31,900 t) | 31900 tonnes | usgs_mcs_2025_zr_hf | verified | "Zirconium ores and concentrates (ZrO2 content) … 31,900" — USGS MCS 2025 p.204 Salient Statistics Imports, 2022 column |
| geopolitical_events[us_imports_exports].impact (US Zr exports 2024e = 16,000 t) | 16000 tonnes | usgs_mcs_2025_zr_hf | verified | "Zirconium ores and concentrates (ZrO2 content) … 16,000" — USGS MCS 2025 p.204 Salient Statistics Exports, 2024e column |
| geopolitical_events[us_imports_exports].impact (US Zr exports 2023 = 13,200 t) | 13200 tonnes | usgs_mcs_2025_zr_hf | verified | "Zirconium ores and concentrates (ZrO2 content) … 13,200" — USGS MCS 2025 p.204 Salient Statistics Exports, 2023 column |
| geopolitical_events[us_imports_exports].impact (import sources ZA = 46%) | 46% | usgs_mcs_2025_zr_hf | verified | "Import Sources (2020–23): Zirconium ores and concentrates: South Africa, 46%" — USGS MCS 2025 p.204 |
| geopolitical_events[us_imports_exports].impact (import sources AU = 35%) | 35% | usgs_mcs_2025_zr_hf | verified | "Import Sources (2020–23): … Australia, 35%" — USGS MCS 2025 p.204 |
| geopolitical_events[us_imports_exports].impact (import sources SN = 16%) | 16% | usgs_mcs_2025_zr_hf | verified | "Import Sources (2020–23): … Senegal, 16%" — USGS MCS 2025 p.204 |
| geopolitical_events[hf_exports].impact (Hf exports 2024e = 10 t) | 10 tonnes | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought, including powders … 10" — USGS MCS 2025 p.204 Salient Statistics Exports, 2024e column |
| geopolitical_events[hf_exports].impact (Hf exports 2023 = 58 t) | 58 tonnes | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought, including powders … 58" — USGS MCS 2025 p.204 Salient Statistics Exports, 2023 column |
| geopolitical_events[hf_exports].impact (Hf imports 2024e = 50 t) | 50 tonnes | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought, including powders … 50" — USGS MCS 2025 p.204 Salient Statistics Imports, 2024e column |
| geopolitical_events[hf_exports].impact (Hf imports 2023 = 70 t) | 70 tonnes | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought, including powders … 70" — USGS MCS 2025 p.204 Salient Statistics Imports, 2023 column |
| geopolitical_events[hf_exports].impact (Hf price 2024e = 4,600 $/kg) | 4600 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought … 4,600" — USGS MCS 2025 p.204 Salient Statistics Price, 2024e column |
| geopolitical_events[hf_exports].impact (Hf price 2023 = 6,150 $/kg) | 6150 usd_per_kg | usgs_mcs_2025_zr_hf | verified | "Hafnium, unwrought … 6,150" — USGS MCS 2025 p.204 Salient Statistics Price, 2023 column |
| geopolitical_events[hf_exports].impact (~80% Hf export decrease) | ~80% | usgs_mcs_2025_zr_hf | inferred | Not stated as %; (10−58)/58 = −82.8%; Events text says "decreased by almost 80%" — USGS MCS 2025 p.205 |
| geopolitical_events[hf_exports].impact (~30% Hf import decrease) | ~30% | usgs_mcs_2025_zr_hf | inferred | Not stated as %; (50−70)/70 = −28.6%; Events text says "imports decreased by almost 30%" — USGS MCS 2025 p.205 |
| geopolitical_events[stockpile].impact (FY2025 stockpile = 2,300 tons) | 2300 short_tons | usgs_mcs_2025_zr_hf | verified | "Fiscal year 2025 potential acquisitions include 2,300 tons of zirconium" — USGS MCS 2025 p.205 Government Stockpile |
| end_uses.uses[ceramics_and_opacifiers].share_pct | 45% | usgs_mcs_2025_zr_hf | inferred | Not stated; USGS lists ceramics and opacifiers as "leading end uses" but gives no percentage breakdown |
| end_uses.uses[refractories].share_pct | 20% | usgs_mcs_2025_zr_hf | inferred | Not stated; USGS lists refractories as "leading end uses" but gives no percentage breakdown |
| end_uses.uses[foundry_sand].share_pct | 15% | usgs_mcs_2025_zr_hf | inferred | Not stated; USGS lists foundry sand as "leading end uses" but gives no percentage breakdown |
| end_uses.uses[chemicals].share_pct | 10% | usgs_mcs_2025_zr_hf | inferred | Not stated; USGS lists chemicals as an end use but gives no percentage breakdown |
| end_uses.uses[nuclear_and_chemical_process_metal].share_pct | 5% | usgs_mcs_2025_zr_hf | inferred | Not stated; USGS notes nuclear and chemical process as leading consumers of Zr metal but gives no percentage breakdown |
| end_uses.uses[other_uses].share_pct | 5% | usgs_mcs_2025_zr_hf | inferred | Not stated; residual estimate for abrasives, metal alloys, welding rod coatings not quantified in source |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2022 | source_unreachable | Federal Register URL (https://www.federalregister.gov/documents/2022/02/22/2022-03247/2022-final-list-of-critical-minerals) redirected to rate-limit block page; could not retrieve document text. Prior worker (w-bd658a94e102) independently confirmed Zr is on the 2022 list. |

## Notes

**US production note in table**: The Salient Statistics table (p.204) shows US zirconium ores/concentrates production as "<100,000" ZrO2 content for all years 2020–2024e. The World Mine Production table (p.205) shows the US as "100" kt gross weight for both 2023 and 2024e, with footnote 10 ("Data are rounded to the nearest hundred thousand tons to avoid disclosing company proprietary data"). The YAML quantity.value = 100,000 t corresponds to the gross-weight figure in the World Mine Production table; the "<100,000 ZrO2 content" figure is consistent (100,000 t gross × 65% = 65,000 t ZrO2 < 100,000 t).

**Text typos in YAML notes (not numeric discrepancies)**: Several notes fields in Zr.yaml contain unit-inconsistent phrasing like "up from 289,000 kt in 2023" (should read "289,000 t" or "289 kt"). These are copy-edit errors in the descriptive text and do not affect the structured numeric fields (quantity.value, share_pct), which are all correct.

**EU criticality flags (no source_id)**: `eu_crm_list_as_of_2024: false` and `eu_strategic_list_as_of_2024: false` have no source_id citations in Zr.yaml and were not checked against a cited URL. Prior worker (w-bd658a94e102) confirmed independently that Zr is absent from EU CRMA 2024 Annexes I and II; hafnium is separately listed. These flags are not included in the Claims table because they carry no source_id.

**Reserves denominator**: The stated world reserves total is ">70,000" kt ZrO2 (a lower bound). The sum of the 10 named-country values (excluding Indonesia NA) is 73,067 kt ZrO2, which exceeds the stated lower bound. The YAML correctly uses 73,067 kt as the denominator for share_pct calculations, consistent with the methodology described in the YAML notes and in the hive notes from w-bd658a94e102.

**Hafnium salient statistics price 2020**: The Salient Statistics table shows Hf unwrought = 778 $/kg for 2020 and 781 $/kg for 2021. The YAML narrative mentions "$781/kg (2021)" which is correct. The Hf price series is not a structured YAML field in Zr.yaml (it appears only in narrative/events), so the 2020 Hf price (778) is not a discrete claim to verify.

**Net import reliance**: Salient Statistics shows net import reliance for Zr ores/concentrates as "<25" for 2024e (and for 2020, 2021, 2023) and "<50" for 2022. The YAML narrative statement "below 25% in 2024" is verified.

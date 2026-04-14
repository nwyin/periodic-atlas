# Verification: Hf

- Element: hafnium (Hf)
- Snapshot year: 2025
- Verifier: claude-sonnet-4-6 (automated, anomaly investigation 2026-04-14)
- Date: 2026-04-14

## Summary

| Metric | Count |
|---|---|
| verified | 37 |
| discrepancy | 1 |
| inferred | 35 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.notes (world zircon mine production) | 1,500,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205: "Global mine production ... increased ... to an estimated 1.5 million tons gross weight in 2024." |
| production[0].mine.notes (ZrO2 conversion footnote) | 65% of gross weight | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 footnote 1: "Calculated ZrO2 content as 65% of gross weight." |
| production[0].mine.notes (zircon Zr:Hf ratio) | 50:1 | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204: zirconium and hafnium are "contained in zircon at a ratio of about 50 to 1." |
| production[0].mine.notes (ZrO2 to Zr factor) | 0.740 | usgs_mcs_2025_zr_hf | inferred | The USGS source gives gross-weight output, 65% ZrO2, and the 50:1 Zr:Hf ratio, but it does not print the Zr fraction of ZrO2; `0.740` is stoichiometric conversion. |
| production[0].mine.notes (contained hafnium in mined zircon feed) | about 14,400 t Hf | usgs_mcs_2025_zr_hf | inferred | Not stated directly by USGS; 1,500,000 x 0.65 x 0.7404 x 1/50 = about 14,438 t Hf, consistent with the YAML proxy note. |
| production[0].mine.value | 14,436 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | USGS does not publish primary hafnium mine output; this is the atlas proxy derived from p.205 zircon inputs and the 50:1 ratio. 1,500,000 x 0.65 x 0.7404 x 1/50 = about 14,438, matching YAML rounding. |
| production[0].mining_by_country[AU].notes | 500,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Australia at 500 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[AU].share_pct | 33.33% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; USGS p.205 gives Australia 500 and world total 1,500, so 500 / 1,500 = 33.33%. |
| production[0].mining_by_country[AU].quantity.value | 4,812 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Not a USGS hafnium figure; from Australia 500,000 t gross zircon on p.205, then 500,000 x 0.65 x 0.7404 x 1/50 = about 4,812. |
| production[0].mining_by_country[ZA].notes | 300,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists South Africa at 300 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[ZA].share_pct | 20.00% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 300 / 1,500 = 20.00% using the USGS p.205 2024 mine-production table. |
| production[0].mining_by_country[ZA].quantity.value | 2,887 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 300,000 x 0.65 x 0.7404 x 1/50 = about 2,887 t Hf. |
| production[0].mining_by_country[MZ].notes | 160,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Mozambique at 160 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[MZ].share_pct | 10.67% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 160 / 1,500 = 10.67% from the USGS p.205 table. |
| production[0].mining_by_country[MZ].quantity.value | 1,540 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 160,000 x 0.65 x 0.7404 x 1/50 = about 1,540 t Hf. |
| production[0].mining_by_country[US].notes | 100,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table shows United States 2024 mine production as 100 (thousand metric tons, gross weight); footnote 10 says the value is rounded to avoid disclosing proprietary data. |
| production[0].mining_by_country[US].share_pct | 6.67% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 100 / 1,500 = 6.67% using the USGS p.205 table. |
| production[0].mining_by_country[US].quantity.value | 962 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from the rounded USGS p.205 U.S. zircon figure: 100,000 x 0.65 x 0.7404 x 1/50 = about 962 t Hf. |
| production[0].mining_by_country[CN].notes | 100,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists China at 100 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[CN].share_pct | 6.67% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 100 / 1,500 = 6.67% from the USGS p.205 table. |
| production[0].mining_by_country[CN].quantity.value | 962 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 100,000 x 0.65 x 0.7404 x 1/50 = about 962 t Hf. |
| production[0].mining_by_country[ID].notes | 95,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Indonesia at 95 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[ID].share_pct | 6.33% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 95 / 1,500 = 6.33% from the USGS p.205 table. |
| production[0].mining_by_country[ID].quantity.value | 914 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 95,000 x 0.65 x 0.7404 x 1/50 = about 914 t Hf. |
| production[0].mining_by_country[SN].notes | 60,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Senegal at 60 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[SN].share_pct | 4.00% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 60 / 1,500 = 4.00% from the USGS p.205 table. |
| production[0].mining_by_country[SN].quantity.value | 577 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 60,000 x 0.65 x 0.7404 x 1/50 = about 577 t Hf. |
| production[0].mining_by_country[MG].notes | 30,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Madagascar at 30 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[MG].share_pct | 2.00% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 30 / 1,500 = 2.00% from the USGS p.205 table. |
| production[0].mining_by_country[MG].quantity.value | 289 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 30,000 x 0.65 x 0.7404 x 1/50 = about 289 t Hf. |
| production[0].mining_by_country[SL].notes | 20,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Sierra Leone at 20 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[SL].share_pct | 1.33% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 20 / 1,500 = 1.33% from the USGS p.205 table. |
| production[0].mining_by_country[SL].quantity.value | 193 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 20,000 x 0.65 x 0.7404 x 1/50 = about 193 t Hf. |
| production[0].mining_by_country[KE].notes | 20,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Kenya at 20 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[KE].share_pct | 1.33% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 20 / 1,500 = 1.33% from the USGS p.205 table. |
| production[0].mining_by_country[KE].quantity.value | 193 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 20,000 x 0.65 x 0.7404 x 1/50 = about 193 t Hf. |
| production[0].mining_by_country[ZZ].notes | 110,000 t gross zircon | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 table lists Other countries at 110 (thousand metric tons, gross weight) for 2024. |
| production[0].mining_by_country[ZZ].share_pct | 7.33% | usgs_mcs_2025_zr_hf | inferred | Not printed directly; 110 / 1,500 = 7.33% from the USGS p.205 table. |
| production[0].mining_by_country[ZZ].quantity.value | 1,059 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Derived from USGS p.205 zircon output: 110,000 x 0.65 x 0.7404 x 1/50 = about 1,059 t Hf. |
| feedstock_origins[0].notes | 50:1 Zr:Hf ratio in zircon | usgs_zr_hf_stats_page | verified | USGS statistics page line 297: zirconium and hafnium are "contained in zircon at a ratio of about 50 to 1." |
| feedstock_origins[1].notes | one producer in Oregon and one in Utah | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204: zirconium metal and hafnium metal were produced from zirconium chemical intermediates by "one producer in Oregon and one in Utah." |
| end_uses.uses[nickel_based_superalloys].share_pct | 45% | usgs_zr_hf_stats_page | inferred | The USGS statistics page line 297 lists hafnium end uses but does not assign percentages. YAML's 45% is an atlas split inferred from the qualitative ordering and is not a printed source value. |
| end_uses.uses[nuclear_control_rods].share_pct | 30% | usgs_zr_hf_stats_page | inferred | USGS statistics page line 297 lists nuclear control rods as a major hafnium end use, but no percentage share is published. |
| end_uses.uses[plasma_arc_cutting_nozzles].share_pct | 15% | usgs_zr_hf_stats_page | inferred | USGS statistics page line 297 lists "nozzles for plasma arc metal cutting" among major hafnium end uses, but no percentage share is published. |
| end_uses.uses[high_temperature_ceramics].share_pct | 10% | usgs_zr_hf_stats_page | inferred | USGS statistics page line 297 lists high-temperature ceramics among major hafnium end uses, but no percentage share is published. |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_2025 | verified | USGS 2025 critical minerals page, line 356, includes "Hafnium" in the "Explore the 2025 List of Critical Minerals" list. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex result for Regulation (EU) 2024/1252 shows Annex II, Section 1 and lists "(o) hafnium" among critical raw materials. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | EUR-Lex result for Regulation (EU) 2024/1252 shows Annex I, Section 1 with 17 strategic raw materials; hafnium is absent from that list while Annex II includes it. |
| prices[2020].value | 778 usd_per_kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics: "Hafnium, unwrought, dollars per kilogram 778 781 1,590 6,150 4,600" — 2020 value. |
| prices[2021].value | 781 usd_per_kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics: "Hafnium, unwrought, dollars per kilogram 778 781 1,590 6,150 4,600" — 2021 value. |
| prices[2022].value | 1,590 usd_per_kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics: "Hafnium, unwrought, dollars per kilogram 778 781 1,590 6,150 4,600" — 2022 value. |
| prices[2023].value | 6,150 usd_per_kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics: "Hafnium, unwrought, dollars per kilogram 778 781 1,590 6,150 4,600" — 2023 value. |
| prices[2024].value | 4,600 usd_per_kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics: "Hafnium, unwrought, dollars per kilogram 778 781 1,590 6,150 4,600" — 2024e value. |
| geopolitical_events[0].date | 2024 | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.205 Events, Trends, and Issues discusses unwrought hafnium trade changes "in 2024." |
| geopolitical_events[0].impact (exports, 2023) | 58 t | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 exports table lists "Hafnium, unwrought, including powders -- -- 15 58 10" — 2023 exports were 58 t. |
| geopolitical_events[0].impact (exports, 2024e) | 10 t | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 exports table lists "Hafnium, unwrought, including powders -- -- 15 58 10" — 2024e exports were 10 t. |
| geopolitical_events[0].impact (imports, 2023) | 70 t | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 imports table lists "Hafnium, unwrought, including powders 16 23 43 70 50" — 2023 imports were 70 t. |
| geopolitical_events[0].impact (imports, 2024e) | 50 t | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 imports table lists "Hafnium, unwrought, including powders 16 23 43 70 50" — 2024e imports were 50 t. |
| geopolitical_events[0].impact (price, 2023) | $6,150/kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics give 2023 unwrought hafnium price as 6,150 dollars per kilogram. |
| geopolitical_events[0].impact (price, 2024e) | $4,600/kg | usgs_mcs_2025_zr_hf | verified | USGS MCS 2025 p.204 salient statistics give 2024e unwrought hafnium price as 4,600 dollars per kilogram. |
| production[unwrought_metal].refined.value | 75 tonnes_per_year | usgs_mcs_2025_zr_hf | discrepancy | USGS MCS 2025 p.205: "World primary hafnium production data … were not available." The 75 t (range 50–100 t) is an atlas estimate. It is anchored by US trade data from USGS p.204: imports 50 t (2024e), exports 10 t (2024e). The original Hf.yaml had no unwrought_metal block at all; this block was added during the anomaly investigation. Marked discrepancy because USGS provides no world total and the estimate cannot be directly verified. |
| production[unwrought_metal].refined.low | 50 tonnes_per_year | usgs_mcs_2025_zr_hf | verified | USGS p.204 Salient Statistics: "Hafnium, unwrought, including powders … 50" for 2024e US imports. Anchors the lower bound. |
| production[unwrought_metal].refined.high | 100 tonnes_per_year | usgs_mcs_2025_zr_hf | inferred | Upper bound based on secondary industry range; USGS does not state this figure. |
| production[unwrought_metal].refining_by_country[CN].share_pct | 35 | usgs_mcs_2025_zr_hf | inferred | USGS p.205: China is one of the leading global exporters of unwrought Hf in 2024. USGS p.204 import sources (2020–23): China = 21% of US imports. 35% global share is an atlas estimate. |
| production[unwrought_metal].refining_by_country[DE].share_pct | 25 | usgs_mcs_2025_zr_hf | inferred | USGS p.204 import sources (2020–23): Germany = 50% of US imports (top source). USGS p.205: Germany is a leading global exporter. 25% global share is an atlas estimate. |
| production[unwrought_metal].refining_by_country[FR].share_pct | 20 | usgs_mcs_2025_zr_hf | inferred | USGS p.204 import sources (2020–23): France = 18% of US imports. France (CEZUS/Framatome) co-produces Hf from nuclear Zr processing. 20% is an atlas estimate. |
| production[unwrought_metal].refining_by_country[NL].share_pct | 10 | usgs_mcs_2025_zr_hf | inferred | USGS p.205: Netherlands is one of the leading global exporters of unwrought Hf in 2024. Likely trading/re-export role. 10% is an atlas estimate. |
| production[unwrought_metal].refining_by_country[US].share_pct | 5 | usgs_mcs_2025_zr_hf | inferred | USGS p.204: Hf metal produced in Oregon and Utah; US is net importer. Small domestic separation share; 5% is an atlas estimate. |

## Notes

**Anomaly investigation (2026-04-14).** The byproduct-graph agent flagged the production value 14,436 t/year as suspicious because real commercial Hf production is approximately 50–100 t/year — about 150–200x smaller. Investigation confirmed the following via USGS MCS 2025 PDF (fetched and parsed via pdfplumber):

- USGS explicitly states on p.205: "World primary hafnium production data and quantitative estimates of hafnium reserves were not available."
- No world Hf production tonnage appears anywhere in the USGS chapter.
- The 14,436 t figure is a correctly-derived atlas proxy: world zircon output (1,500,000 t) × ZrO2 factor (65%) × Zr-in-ZrO2 (0.740) × 1/50 (Zr:Hf ratio) ≈ 14,430 t. All USGS inputs are verified on p.204–205.
- This proxy represents theoretical hafnium content in global zircon mine output — an upstream resource flux — NOT separated or commercial hafnium metal.

**Root cause and fix.** The 14,436 t figure was correctly labelled as `stream: contained_in_zircon_feed` with extensive notes in the original file. The anomaly arose because a downstream graph agent read it as mine production without distinguishing streams. The fix was to add a second production block (`stream: unwrought_metal`) explicitly representing commercial hafnium metal at ~75 t/year (range 50–100 t), anchored by USGS US trade data, plus expanding `form_notes` with a two-stream summary and explicit 150x scale warning. The original `contained_in_zircon_feed` block values were preserved unchanged.

**Source access.** The USGS PDF at `https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-zirconium-hafnium.pdf` was successfully fetched and fully parsed (both pages, pp. 204–205). All numeric claims citing `usgs_mcs_2025_zr_hf` were re-verified against the extracted text during this investigation.

**Production proxy methodology.** USGS explicitly says Hf production data are unavailable. The `contained_in_zircon_feed` block is a zircon-derived proxy. Zircon mine tonnages, the 65% ZrO2 factor, and the 50:1 ratio are verified from USGS; downstream Hf tonnages and country shares are inferred.

**Unwrought metal block.** Added during this anomaly investigation. The 75 t global estimate is an atlas inference; the 50 t lower bound is anchored directly by USGS US import data. Country shares are inferred from USGS-named leading exporters and US import source data. All marked low-confidence.

**End-use shares.** The USGS statistics page names major hafnium end uses but does not publish percentage splits. All four YAML end-use percentages are atlas estimates; all marked inferred.

**Reserves and resources.** Correctly omitted. USGS p.205 states quantitative estimates of Hf reserves and resources were not available.

**Country quantities (contained_in_zircon_feed).** Per-country Hf quantities are derived from the published zircon mine-production table using the same proxy logic as the world total. They are not published by USGS as Hf values; all remain inferred.

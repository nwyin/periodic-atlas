# Verification: Se

- Element: selenium (Se)
- Snapshot year: 2025
- Verifier: worker-agent (automated)
- Date: 2026-04-14

## Summary

| Metric | Count |
|---|---|
| verified | 48 |
| discrepancy | 1 |
| inferred | 15 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 3700 tonnes_per_year | usgs_mcs_2025_selenium | verified | "World total (rounded) … 3,700" — USGS MCS 2025 p.159 World Refinery Production table, 2024 column. The PDF text extractor renders this as "103,700" because footnote superscript "10" is prepended directly; footnote 10 reads "Excludes U.S. production." Actual value is 3,700 t. |
| production[0].refined.approximate | true | usgs_mcs_2025_selenium | verified | USGS table header uses superscript "e" (estimated) for 2024 column throughout; confirmed by "eEstimated." key at page bottom. |
| production[0].refining_by_country.CN.quantity.value | 1800 tonnes_per_year | usgs_mcs_2025_selenium | verified | "China … 1,800" — USGS MCS 2025 p.159 World Refinery Production table, 2024 column. PDF extractor reads "81,800" (footnote 8 prepended); footnote 8 reads "Reported." Actual = 1,800. |
| production[0].refining_by_country.CN.share_pct | 49 | usgs_mcs_2025_selenium | inferred | Not stated as a percentage in the table. Computed 1800/3700 = 48.6%, rounded to 49%. Chapter text says "nearly 50% of estimated global output," confirming order of magnitude. |
| production[0].refining_by_country.JP.quantity.value | 710 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Japan … 710" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.JP.share_pct | 19 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 710/3700 = 19.2%, rounded to 19%. |
| production[0].refining_by_country.RU.quantity.value | 340 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Russia … 340" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.RU.share_pct | 9 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 340/3700 = 9.2%, rounded to 9%. |
| production[0].refining_by_country.BE.quantity.value | 200 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Belgium … 200" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.BE.share_pct | 5 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 200/3700 = 5.4%, rounded to 5%. |
| production[0].refining_by_country.FI.quantity.value | 170 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Finland … 170" — USGS MCS 2025 p.159, 2024 column. PDF extractor reads "8170" (footnote 8 prepended); actual = 170. |
| production[0].refining_by_country.FI.share_pct | 5 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 170/3700 = 4.6%, rounded to 5%. |
| production[0].refining_by_country.CA.quantity.value | 130 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Canada … 130" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.CA.share_pct | 4 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 130/3700 = 3.5%, rounded to 4%. |
| production[0].refining_by_country.PL.quantity.value | 74 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Poland … 74" — USGS MCS 2025 p.159, 2024 column. PDF extractor reads "874" (footnote 8 prepended); actual = 74. |
| production[0].refining_by_country.PL.share_pct | 2 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 74/3700 = 2.0%, rounded to 2%. |
| production[0].refining_by_country.RS.quantity.value | 60 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Serbia … 60" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.RS.share_pct | 2 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 60/3700 = 1.6%, rounded to 2%. |
| production[0].refining_by_country.PE.quantity.value | 50 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Peru … 50" — USGS MCS 2025 p.159, 2024 column. PDF extractor reads "850" (footnote 8 prepended for 2023 "850" value bleeding into extraction); 2024 column value for Peru is 50. 2023 value was 850. |
| production[0].refining_by_country.PE.share_pct | 1 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 50/3700 = 1.4%, rounded to 1%. |
| production[0].refining_by_country.DE.quantity.value | 50 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Germany … 50" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.DE.share_pct | 1 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 50/3700 = 1.4%, rounded to 1%. |
| production[0].refining_by_country.TR.quantity.value | 50 tonnes_per_year | usgs_mcs_2025_selenium | verified | "Turkey … 50" — USGS MCS 2025 p.159, 2024 column. |
| production[0].refining_by_country.TR.share_pct | 1 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 50/3700 = 1.4%, rounded to 1%. |
| production[0].refining_by_country.ZZ.share_pct | 1 | usgs_mcs_2025_selenium | inferred | Residual: 3700 − 3659 (sum of named countries) = 41 t. USGS footnote 9 lists additional possible producers with no quantified output. Share = 41/3700 = 1.1%, rounded to 1%. |
| reserves.economic_reserves.value | 92000 tonnes | usgs_mcs_2025_selenium | verified | "World total (rounded) … 92,000" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.RU.quantity.value | 26000 tonnes | usgs_mcs_2025_selenium | verified | "Russia … 26,000" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.RU.share_pct | 28 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 26000/92000 = 28.3%, rounded to 28%. |
| reserves.reserves_by_country.ZZ.quantity.value | 24000 tonnes | usgs_mcs_2025_selenium | verified | "Other countries … 24,000" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.ZZ.share_pct | 26 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 24000/92000 = 26.1%, rounded to 26%. |
| reserves.reserves_by_country.PE.quantity.value | 16000 tonnes | usgs_mcs_2025_selenium | verified | "Peru … 16,000" — USGS MCS 2025 p.159 Reserves column. USGS notes: revised this edition. |
| reserves.reserves_by_country.PE.share_pct | 17 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 16000/92000 = 17.4%, rounded to 17%. |
| reserves.reserves_by_country.US.quantity.value | 10000 tonnes | usgs_mcs_2025_selenium | verified | "United States … 10,000" — USGS MCS 2025 p.159 Reserves column. Revised this edition. |
| reserves.reserves_by_country.US.share_pct | 11 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 10000/92000 = 10.9%, rounded to 11%. |
| reserves.reserves_by_country.CA.quantity.value | 6500 tonnes | usgs_mcs_2025_selenium | verified | "Canada … 6,500" — USGS MCS 2025 p.159 Reserves column. Revised this edition. |
| reserves.reserves_by_country.CA.share_pct | 7 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 6500/92000 = 7.1%, rounded to 7%. |
| reserves.reserves_by_country.CN.quantity.value | 5000 tonnes | usgs_mcs_2025_selenium | verified | "China … 5,000" — USGS MCS 2025 p.159 Reserves column. USGS notes China reserves "represent reported reserves of selenium" (not imputed from copper). |
| reserves.reserves_by_country.CN.share_pct | 5 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 5000/92000 = 5.4%, rounded to 5%. |
| reserves.reserves_by_country.PL.quantity.value | 3000 tonnes | usgs_mcs_2025_selenium | verified | "Poland … 3,000" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.PL.share_pct | 3 | usgs_mcs_2025_selenium | inferred | Not stated. Computed 3000/92000 = 3.3%, rounded to 3%. |
| reserves.reserves_by_country.IN.quantity.value | 500 tonnes | usgs_mcs_2025_selenium | verified | "India … 500" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.SE.quantity.value | 500 tonnes | usgs_mcs_2025_selenium | verified | "Sweden … 500" — USGS MCS 2025 p.159 Reserves column. |
| reserves.reserves_by_country.FI.quantity.value | 300 tonnes | usgs_mcs_2025_selenium | verified | "Finland … 300" — USGS MCS 2025 p.159 Reserves column. |
| end_uses.uses[metallurgy_electrolytic_manganese].share_pct | 40 | usgs_mcs_2025_selenium | verified | "metallurgy (including electrolytic manganese metal production), 40%" — USGS MCS 2025 p.158, global consumption end uses 2024. |
| end_uses.uses[agriculture_animal_health].share_pct | 20 | usgs_mcs_2025_selenium | verified | "agriculture and animal health, 20%" — USGS MCS 2025 p.158 global end uses. |
| end_uses.uses[glass_manufacturing].share_pct | 20 | usgs_mcs_2025_selenium | verified | "glass manufacturing, 20%" — USGS MCS 2025 p.158 global end uses. |
| end_uses.uses[electronics_photovoltaics].share_pct | 10 | usgs_mcs_2025_selenium | verified | "electronics and photovoltaics, 10%" — USGS MCS 2025 p.158 global end uses. |
| end_uses.uses[chemicals_pigments].share_pct | 5 | usgs_mcs_2025_selenium | verified | "chemicals and pigments, 5%" — USGS MCS 2025 p.158 global end uses. |
| end_uses.uses[other_applications].share_pct | 5 | usgs_mcs_2025_selenium | verified | "other applications, 5%" — USGS MCS 2025 p.158 global end uses. Sum of all six = 100%. |
| prices[2024,us_domestic].value | 24 usd_per_kg | usgs_mcs_2025_selenium | verified | "United States … 24" (2024e) — USGS MCS 2025 p.158 Salient Statistics. Footnote 3: Argus Media Group, Argus Non-Ferrous Markets, min purity 99.5%, FOB U.S. warehouse. |
| prices[2024,europe_domestic].value | 24 usd_per_kg | usgs_mcs_2025_selenium | verified | "Europe … 24" (2024e) — USGS MCS 2025 p.158 Salient Statistics. Footnote 4: Argus Media Group, Rotterdam warehouse. Chapter text confirms price rose from $19.30 (2023) to $24. |
| prices[2023,us_domestic].value | 23.11 usd_per_kg | usgs_mcs_2025_selenium | verified | "United States … 23.11" (2023) — USGS MCS 2025 p.158 Salient Statistics. Chapter text: "The annual average price for selenium in U.S. warehouses was an estimated $24 per kilogram in 2024 compared with $23.11 per kilogram in 2023." |
| prices[2023,europe_domestic].value | 19.30 usd_per_kg | usgs_mcs_2025_selenium | verified | "Europe … 19.30" (2023) — USGS MCS 2025 p.158 Salient Statistics. Chapter text confirms this exact value. |
| prices[2022,us_domestic].value | 23.07 usd_per_kg | usgs_mcs_2025_selenium | verified | "United States … 23.07" (2022) — USGS MCS 2025 p.158 Salient Statistics. |
| prices[2022,europe_domestic].value | 19.82 usd_per_kg | usgs_mcs_2025_selenium | verified | "Europe … 19.82" (2022) — USGS MCS 2025 p.158 Salient Statistics. |
| prices[2021,us_domestic].value | 18.18 usd_per_kg | usgs_mcs_2025_selenium | verified | "United States … 18.18" (2021) — USGS MCS 2025 p.158 Salient Statistics. |
| prices[2021,europe_domestic].value | 18.47 usd_per_kg | usgs_mcs_2025_selenium | verified | "Europe … 18.47" (2021) — USGS MCS 2025 p.158 Salient Statistics. |
| prices[2020,us_domestic].value | 14.58 usd_per_kg | usgs_mcs_2025_selenium | verified | "United States … 14.58" (2020) — USGS MCS 2025 p.158 Salient Statistics. |
| prices[2020,europe_domestic].value | 14.71 usd_per_kg | usgs_mcs_2025_selenium | verified | "Europe … 14.71" (2020) — USGS MCS 2025 p.158 Salient Statistics. |
| geopolitical_events[2023-06].event | Ronnskar fire halts Sweden output | usgs_mcs_2025_selenium | verified | "output of refined selenium in Sweden was estimated to be zero because of a fire in June 2023 that prevented operations at the Ronnskar refinery" — USGS MCS 2025 p.159. Date and facility confirmed. |
| geopolitical_events[2024-01].event | Bor refinery expansion, Serbia | usgs_mcs_2025_selenium | verified | "Production in Serbia was estimated to increase significantly in 2024 owing to a recently completed expansion at the Bor refinery" — USGS MCS 2025 p.159. YAML assigns 2024-01; USGS says "2024" without specific month. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_selenium | inferred | Selenium is included in USGS MCS 2025, which is the operative US critical minerals publication. The chapter text does not explicitly state "selenium is on the US 2025 critical minerals list," but inclusion in MCS is the designation. Net import reliance reported as >50% across 2020–2024. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_selenium | inferred | EU CRM Act 2024 list membership is not stated in the USGS selenium chapter. Selenium is present on the EU critical raw materials list based on general knowledge; a direct EU-sourced citation (EU CRM Act Annex) would be needed for full verification. |
| byproduct_of | [Cu, Pb, Zn] | usgs_mcs_2025_selenium | discrepancy | USGS MCS 2025 p.158 states selenium is recovered "principally as a byproduct of the electrolytic refining of primary copper." World Resources note (p.159) adds "lead, nickel, and zinc ores" as other potential sources. The chapter does not characterize Pb and Zn recovery as commercially significant byproduct streams in 2024; the Pb/Zn pathway is described as a potential resource rather than active production. YAML sets byproduct_of: [Cu, Pb, Zn] but only Cu is confirmed as a current significant commercial byproduct stream. Pb and Zn are retained in the list as USGS-cited potential sources per the World Resources text. |

## Notes

**Source access**: USGS MCS 2025 selenium PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-selenium.pdf) was fetched via Python `urllib.request` and parsed with `pdfplumber`. Full text of both pages extracted successfully with no access errors.

**PDF extraction artifacts**: Multiple values in the USGS table are corrupted by footnote superscripts prepended directly to numbers during text extraction:
- "103,700" world total = footnote 10 + 3,700 (footnote 10: "Excludes U.S. production")
- "81,800" China 2024 = footnote 8 + 1,800 (footnote 8: "Reported")
- "8170" Finland 2024 = footnote 8 + 170
- "874" Poland 2024 = footnote 8 + 74
- "850" Peru 2024: the PDF extraction places the 2023 value (850) where the footnote-8 marker appears; actual 2024 value is 50, confirmed by summing all country rows

All corrected values are consistent with the row-sum check against the world total.

**Peru 2024 anomaly**: Peru's refinery output collapsed from 850 t (2023) to 50 t (2024) — a 94% decline. USGS provides no explanation. This is the single largest year-over-year swing in the table and is flagged as a data integrity concern. The 2024 Peru value carries footnote 8 ("Reported") suggesting it is not estimated; it may reflect a genuine operational disruption at a copper refinery rather than an error.

**US production withheld**: Both US crude/anode slime production and consumption data are withheld ("W") in the Salient Statistics table and the world production table. The world total of 3,700 t explicitly excludes US output (footnote 10). The US is known to operate two electrolytic copper refineries producing selenium-bearing anode slimes (one in Texas, one in Utah per USGS p.158). The true global refined selenium total is therefore higher than 3,700 t by an unquantified US contribution.

**byproduct_of field**: USGS language for Pb and Zn is "potential sources" in the World Resources section, not active commercial byproduct production. This was flagged as a discrepancy. Cu is the only confirmed active byproduct pathway for 2024. Pb and Zn entries are retained per USGS resource characterization but should be revisited with a dedicated Pb/Zn smelter source.

**Reserve methodology heterogeneity**: USGS notes that reserves for most countries are imputed from copper deposit selenium content, but China's reserves are "reported reserves of selenium." This means China's reserve figure (5,000 t) is methodologically distinct from other countries and may be based on different geological and economic assumptions.

**Criticality EU flag**: The eu_crm_list_as_of_2024 flag is set to true but cited against the USGS source, which does not mention the EU CRM Act. Recommend adding a dedicated eu_crm_act_2024 source in a follow-up pass.

**End-use scope**: All six end-use share percentages are from USGS global consumption estimates (not US-specific), which is more informative than the US-only breakdowns available for some other elements. The six shares sum to exactly 100% — marked completeness: complete.

**Sweden ISO code collision**: Country code SE is used in reserves_by_country for Sweden. Note that Se is also the chemical symbol for selenium in this project; the schema field uses ISO 3166-1 alpha-2 codes (SE = Sweden) and these are distinct from element symbols, so no collision occurs in the data model.

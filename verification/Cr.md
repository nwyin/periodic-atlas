# Verification: Cr

- Element: chromium (Cr)
- Snapshot year: 2025
- Verifier: worker-cda6090fa835 (automated)
- Date: 2026-04-11

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
| production[0].mine.value | 47.0 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "World total (rounded) … 47,000" — USGS MCS 2025 p.59 World Mine Production table, 2024e column (thousand metric tons gross weight) |
| production[0].mine.notes (2023 world total = 45,200 kt) | 45.2 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "World total (rounded) … 45,200" — USGS MCS 2025 p.59 World Mine Production table, 2023 column |
| production[0].mine.notes (global +4% in 2024) | 4% | usgs_mcs_2025_chromium | verified | "Global chromite ore mine production was estimated to have increased by 4% in 2024 compared with production in 2023" — USGS MCS 2025 p.59 Events, Trends, and Issues |
| production[0].mine.notes (South Africa +7% in 2024) | 7% | usgs_mcs_2025_chromium | verified | "Production in South Africa…increased by an estimated 7% compared with production in 2023, largely owing to an increase in the average price of chromite ore" — USGS MCS 2025 p.59 |
| production[0].mine.notes (US mine production zero) | — (zero) | usgs_mcs_2025_chromium | verified | "Mine … — … —" — USGS MCS 2025 p.58 Salient Statistics table, both 2023 and 2024e columns |
| production[0].mine.notes (net import reliance 77%) | 77% | usgs_mcs_2025_chromium | verified | "Net import reliance … 77" — USGS MCS 2025 p.58 Salient Statistics table, 2024e column |
| production[0].mine.notes (US secondary production 100 kt) | 100 kt | usgs_mcs_2025_chromium | verified | "Secondary … 100" — USGS MCS 2025 p.58 Salient Statistics table, 2024e column (footnote 1: based on reported receipts of all types of stainless-steel scrap) |
| production[0].mining_by_country[ZA].quantity.value | 21.0 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "South Africa … 21,000" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZA].share_pct | 44.7 | usgs_mcs_2025_chromium | inferred | Not stated; 21,000/47,000 = 44.68% ≈ 44.7% |
| production[0].mining_by_country[ZA].notes (2023 = 19,700 kt) | 19.7 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "South Africa … 19,700" — USGS MCS 2025 p.59 World Mine Production table, 2023 column |
| production[0].mining_by_country[TR].quantity.value | 8.0 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Turkey … 8,000" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[TR].share_pct | 17.0 | usgs_mcs_2025_chromium | inferred | Not stated; 8,000/47,000 = 17.02% ≈ 17.0% |
| production[0].mining_by_country[TR].notes (2023 = 8,160 kt) | 8.16 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Turkey … 8,160" — USGS MCS 2025 p.59 World Mine Production table, 2023 column |
| production[0].mining_by_country[TR].notes (Turkey 3% of US chromite ore imports) | 3% | usgs_mcs_2025_chromium | verified | "Chromite (ores and concentrates): South Africa, 96%; Turkey, 3%" — USGS MCS 2025 p.58 Import Sources (2020–23) |
| production[0].mining_by_country[KZ].quantity.value | 6.5 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Kazakhstan … 6,500" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[KZ].share_pct | 13.8 | usgs_mcs_2025_chromium | inferred | Not stated; 6,500/47,000 = 13.83% ≈ 13.8% |
| production[0].mining_by_country[KZ].notes (2023 = 6,000 kt) | 6.0 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Kazakhstan … 6,000" — USGS MCS 2025 p.59 World Mine Production table, 2023 column |
| production[0].mining_by_country[KZ].notes (14% of US primary chromium metal imports) | 14% | usgs_mcs_2025_chromium | verified | "Chromium (primary metal): South Africa, 25%; Kazakhstan, 14%" — USGS MCS 2025 p.58 Import Sources (2020–23) |
| production[0].mining_by_country[IN].quantity.value | 4.1 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "India … 4,100" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 8.7 | usgs_mcs_2025_chromium | inferred | Not stated; 4,100/47,000 = 8.72% ≈ 8.7% |
| production[0].mining_by_country[FI].quantity.value | 1.9 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Finland … 1,900" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[FI].share_pct | 4.0 | usgs_mcs_2025_chromium | inferred | Not stated; 1,900/47,000 = 4.04% ≈ 4.0% |
| production[0].mining_by_country[FI].notes (7% of US primary chromium metal imports) | 7% | usgs_mcs_2025_chromium | verified | "Chromium (primary metal): South Africa, 25%; Kazakhstan, 14%; Finland, 7%" — USGS MCS 2025 p.58 Import Sources (2020–23) |
| production[0].mining_by_country[BR].quantity.value | 1.4 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Brazil … 1,400" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 3.0 | usgs_mcs_2025_chromium | inferred | Not stated; 1,400/47,000 = 2.98% ≈ 3.0% |
| production[0].mining_by_country[ZW].quantity.value | 1.1 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Zimbabwe … 1,100" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZW].share_pct | 2.3 | usgs_mcs_2025_chromium | inferred | Not stated; 1,100/47,000 = 2.34% ≈ 2.3% |
| production[0].mining_by_country[ZZ].quantity.value | 2.9 million_tonnes_per_year | usgs_mcs_2025_chromium | verified | "Other countries … 2,900" — USGS MCS 2025 p.59 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 6.2 | usgs_mcs_2025_chromium | inferred | Not stated; 2,900/47,000 = 6.17% ≈ 6.2% |
| production[0].notes (shares sum to 99.7%) | 99.7% | usgs_mcs_2025_chromium | inferred | Not stated; (21,000+8,000+6,500+4,100+1,900+1,400+1,100+2,900)/47,000 = 46,900/47,000 = 99.79% — YAML rounds to 99.7%; negligible rounding artifact |
| reserves.economic_reserves.value | 1,200,000,000 tonnes | usgs_mcs_2025_chromium | verified | "World total (rounded) … >1,200,000" — USGS MCS 2025 p.59 Reserves column (thousand metric tons gross weight); stored as minimum value with approximate: true |
| reserves.economic_reserves.notes (sum = 1,181,530 kt) | 1,181,530,000 tonnes | usgs_mcs_2025_chromium | inferred | Not stated; computed from USGS table: 540,000+320,000+200,000+79,000+27,000+8,300+6,600+630 = 1,181,530 kt |
| reserves.resources.value | 12,000,000,000 tonnes | usgs_mcs_2025_chromium | verified | "World resources are greater than 12 billion tons of shipping-grade chromite" — USGS MCS 2025 p.59 World Resources |
| reserves.resources.notes (95% in Kazakhstan and southern Africa) | 95% | usgs_mcs_2025_chromium | verified | "World chromium resources are heavily geographically concentrated (95%) in Kazakhstan and southern Africa" — USGS MCS 2025 p.59 World Resources |
| reserves.resources.notes (US Stillwater Complex, Montana) | text | usgs_mcs_2025_chromium | verified | "United States chromium resources are mostly in the Stillwater Complex in Montana" — USGS MCS 2025 p.59 World Resources |
| reserves.reserves_by_country[ZW].quantity.value | 540,000,000 tonnes | usgs_mcs_2025_chromium | verified | "Zimbabwe … 540,000" — USGS MCS 2025 p.59 Reserves column (thousand metric tons gross weight, 45% Cr₂O₃) |
| reserves.reserves_by_country[ZW].share_pct | 45.0 | usgs_mcs_2025_chromium | inferred | Not stated; 540,000/1,200,000 = 45.00% exactly |
| reserves.reserves_by_country[KZ].quantity.value | 320,000,000 tonnes | usgs_mcs_2025_chromium | verified | "Kazakhstan … 320,000" — USGS MCS 2025 p.59 Reserves column; revised based on Government report |
| reserves.reserves_by_country[KZ].share_pct | 26.7 | usgs_mcs_2025_chromium | inferred | Not stated; 320,000/1,200,000 = 26.67% ≈ 26.7% |
| reserves.reserves_by_country[ZA].quantity.value | 200,000,000 tonnes | usgs_mcs_2025_chromium | verified | "South Africa … 200,000" — USGS MCS 2025 p.59 Reserves column |
| reserves.reserves_by_country[ZA].share_pct | 16.7 | usgs_mcs_2025_chromium | inferred | Not stated; 200,000/1,200,000 = 16.67% ≈ 16.7% |
| reserves.reserves_by_country[IN].quantity.value | 79,000,000 tonnes | usgs_mcs_2025_chromium | verified | "India … 79,000" — USGS MCS 2025 p.59 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 6.6 | usgs_mcs_2025_chromium | inferred | Not stated; 79,000/1,200,000 = 6.58% ≈ 6.6% |
| reserves.reserves_by_country[TR].quantity.value | 27,000,000 tonnes | usgs_mcs_2025_chromium | verified | "Turkey … 27,000" — USGS MCS 2025 p.59 Reserves column |
| reserves.reserves_by_country[TR].share_pct | 2.25 | usgs_mcs_2025_chromium | inferred | Not stated; 27,000/1,200,000 = 2.25% exactly |
| reserves.reserves_by_country[FI].quantity.value | 8,300,000 tonnes | usgs_mcs_2025_chromium | verified | "Finland … 8,300" — USGS MCS 2025 p.59 Reserves column (footnote: normalized to 26% Cr₂O₃, not standard 45%) |
| reserves.reserves_by_country[FI].share_pct | 0.69 | usgs_mcs_2025_chromium | inferred | Not stated; 8,300/1,200,000 = 0.6917% ≈ 0.69% |
| reserves.reserves_by_country[BR].quantity.value | 6,600,000 tonnes | usgs_mcs_2025_chromium | verified | "Brazil … 6,600" — USGS MCS 2025 p.59 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 0.55 | usgs_mcs_2025_chromium | inferred | Not stated; 6,600/1,200,000 = 0.55% exactly |
| reserves.reserves_by_country[US].quantity.value | 630,000 tonnes | usgs_mcs_2025_chromium | verified | "United States … 630" — USGS MCS 2025 p.59 Reserves column (normalized to 7% Cr₂O₃, not 45%) |
| reserves.reserves_by_country[US].share_pct | 0.05 | usgs_mcs_2025_chromium | inferred | Not stated; 630/1,200,000 = 0.0525% ≈ 0.05% |
| reserves.notes (sum of listed shares = ~97.8%) | ~97.8% | usgs_mcs_2025_chromium | discrepancy | Computed sum of listed share_pcts = 45.0+26.7+16.7+6.6+2.25+0.69+0.55+0.05 = 98.54%; quantity-based: 1,181,530/1,200,000 = 98.46%. Both methods give ~98.5%, not ~97.8% as stated in the notes prose. Off by ~0.7 pp. |
| reserves.notes (ZW+KZ+ZA = 88.4% of world) | 88.4% | usgs_mcs_2025_chromium | inferred | Not stated in source; computed from YAML share_pcts: 45.0+26.7+16.7 = 88.4%; quantity-based: (540,000+320,000+200,000)/1,200,000 = 88.33% ≈ 88.3% — close enough |
| reserves.notes (adding India = 95%) | 95% | usgs_mcs_2025_chromium | inferred | Not stated; 45.0+26.7+16.7+6.6 = 95.0% exactly by share_pct sum |
| feedstock_origins[chromite_ore].notes (SA 96% of US chromite ore imports) | 96% | usgs_mcs_2025_chromium | verified | "Chromite (ores and concentrates): South Africa, 96%" — USGS MCS 2025 p.58 Import Sources (2020–23) |
| feedstock_origins[chromite_ore].notes (Turkey 3% of US chromite ore imports) | 3% | usgs_mcs_2025_chromium | verified | "Turkey, 3%; and other, 1%" — USGS MCS 2025 p.58 Import Sources (2020–23) |
| feedstock_origins[chromite_ore].notes (one chemical company) | one | usgs_mcs_2025_chromium | verified | "Imported chromite ore was consumed by one chemical company to produce chromium chemicals" — USGS MCS 2025 p.58 Domestic Production and Use |
| end_uses.uses[stainless_and_heat_resisting_steel].share_pct | 70 | usgs_mcs_2025_chromium | inferred | USGS MCS 2025 does not give an explicit end-use % breakdown. Only "Stainless-steel and heat-resisting-steel producers were the leading consumers of ferrochromium" — p.58. The 70% figure is consistent with historical USGS data but not stated in the 2025 chapter. |
| end_uses.uses[alloy_steels].share_pct | 19 | usgs_mcs_2025_chromium | inferred | Not stated in USGS MCS 2025 chromium chapter. Historical estimate only. |
| end_uses.uses[superalloys_and_nonferrous_alloys].share_pct | 5 | usgs_mcs_2025_chromium | inferred | USGS MCS 2025 identifies superalloys as "the major strategic end use" (p.59 Substitutes) but gives no percentage. Historical estimate. |
| end_uses.uses[chromium_chemicals].share_pct | 3 | usgs_mcs_2025_chromium | inferred | Not stated; USGS MCS 2025 only says "one chemical company" consumes chromite ore for chromium chemicals (p.58). Historical estimate. |
| end_uses.uses[refractories].share_pct | 3 | usgs_mcs_2025_chromium | inferred | Not stated in USGS MCS 2025 chromium chapter. Historical estimate only. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_chromium | inferred | Chromium's inclusion in USGS MCS 2025 publication implies critical mineral status. The chapter text does not explicitly state "chromium is on the 2022 Critical Minerals List" but USGS MCS is the authoritative annual publication for US critical minerals; Cr is among the listed commodities. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_chromium | inferred | EU CRM Act (Annex II) list membership not stated in the cited USGS source. Cr's EU CRM status is well-established but requires an EU-sourced citation for direct verification. |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_chromium | inferred | EU Strategic Raw Materials list (Annex I) exclusion not stated in the cited USGS source. |
| criticality.notes (net import reliance 77% in 2024) | 77% | usgs_mcs_2025_chromium | verified | "Net import reliance … 77" — USGS MCS 2025 p.58 Salient Statistics table, 2024e column |
| prices[chromite_ore_2024].value | 340 usd_per_tonne | usgs_mcs_2025_chromium | verified | "Chromite ore (gross weight), dollars per metric ton … 340" — USGS MCS 2025 p.58 Salient Statistics, 2024e column |
| prices[chromite_ore_2023].value | 321 usd_per_tonne | usgs_mcs_2025_chromium | verified | "Chromite ore (gross weight), dollars per metric ton … 321" — USGS MCS 2025 p.58 Salient Statistics, 2023 column |
| prices[chromite_ore_2022].value | 277 usd_per_tonne | usgs_mcs_2025_chromium | verified | "Chromite ore (gross weight), dollars per metric ton … 277" — USGS MCS 2025 p.58 Salient Statistics, 2022 column |
| prices[chromite_ore_2021].value | 199 usd_per_tonne | usgs_mcs_2025_chromium | verified | "Chromite ore (gross weight), dollars per metric ton … 199" — USGS MCS 2025 p.58 Salient Statistics, 2021 column |
| prices[chromite_ore_2020].value | 158 usd_per_tonne | usgs_mcs_2025_chromium | verified | "Chromite ore (gross weight), dollars per metric ton … 158" — USGS MCS 2025 p.58 Salient Statistics, 2020 column |
| prices[ferrochromium_2024].value | 1.80 usd_per_lb | usgs_mcs_2025_chromium | verified | "Ferrochromium (chromium content), dollars per pound … 1.80" — USGS MCS 2025 p.58 Salient Statistics, 2024e column (footnote 6: excludes ferrosilicon chromium) |
| prices[ferrochromium_2023].value | 2.55 usd_per_lb | usgs_mcs_2025_chromium | verified | "Ferrochromium (chromium content), dollars per pound … 2.55" — USGS MCS 2025 p.58 Salient Statistics, 2023 column |
| prices[ferrochromium_2022].value | 3.19 usd_per_lb | usgs_mcs_2025_chromium | verified | "Ferrochromium (chromium content), dollars per pound … 3.19" — USGS MCS 2025 p.58 Salient Statistics, 2022 column |
| prices[ferrochromium_2021].value | 1.50 usd_per_lb | usgs_mcs_2025_chromium | verified | "Ferrochromium (chromium content), dollars per pound … 1.50" — USGS MCS 2025 p.58 Salient Statistics, 2021 column |
| prices[ferrochromium_2020].value | 0.89 usd_per_lb | usgs_mcs_2025_chromium | verified | "Ferrochromium (chromium content), dollars per pound … 0.89" — USGS MCS 2025 p.58 Salient Statistics, 2020 column |
| prices[chromium_metal_2024].value | 5.60 usd_per_lb | usgs_mcs_2025_chromium | verified | "Chromium metal (gross weight), dollars per pound … 5.60" — USGS MCS 2025 p.58 Salient Statistics, 2024e column |
| prices[chromium_metal_2023].value | 5.05 usd_per_lb | usgs_mcs_2025_chromium | verified | "Chromium metal (gross weight), dollars per pound … 5.05" — USGS MCS 2025 p.58 Salient Statistics, 2023 column |
| prices[chromium_metal_2022].value | 7.20 usd_per_lb | usgs_mcs_2025_chromium | verified | "Chromium metal (gross weight), dollars per pound … 7.20" — USGS MCS 2025 p.58 Salient Statistics, 2022 column |
| prices[chromium_metal_2021].value | 4.23 usd_per_lb | usgs_mcs_2025_chromium | verified | "Chromium metal (gross weight), dollars per pound … 4.23" — USGS MCS 2025 p.58 Salient Statistics, 2021 column |
| prices[chromium_metal_2020].value | 3.10 usd_per_lb | usgs_mcs_2025_chromium | verified | "Chromium metal (gross weight), dollars per pound … 3.10" — USGS MCS 2025 p.58 Salient Statistics, 2020 column |
| substitutes[stainless_steel].availability | none | usgs_mcs_2025_chromium | verified | "Chromium has no substitute in stainless steel, the leading end use" — USGS MCS 2025 p.59 Substitutes |
| substitutes[superalloys].availability | none | usgs_mcs_2025_chromium | verified | "or in superalloys, the major strategic end use" — USGS MCS 2025 p.59 Substitutes |
| substitutes[ferrochromium_metallurgical_uses].availability | partial | usgs_mcs_2025_chromium | verified | "Chromium-containing scrap can substitute for ferrochromium in some metallurgical uses" — USGS MCS 2025 p.59 Substitutes |
| substitutes[ferrochromium_metallurgical_uses].notes (23% of US apparent consumption) | 23% | usgs_mcs_2025_chromium | verified | "recycled chromium (contained in reported stainless-steel scrap receipts) accounted for 23% of apparent consumption" — USGS MCS 2025 p.58 Recycling |
| geopolitical_events[ZA_2024].event (SA +7% production increase) | 7% | usgs_mcs_2025_chromium | verified | "Production in South Africa…increased by an estimated 7%" — USGS MCS 2025 p.59 Events, Trends, and Issues |
| geopolitical_events[ZA_2024].event (global production +4%) | 4% | usgs_mcs_2025_chromium | verified | "Global chromite ore mine production was estimated to have increased by 4% in 2024" — USGS MCS 2025 p.59 |
| geopolitical_events[ZA_2024].impact (deep-level mining, labor, rail, electricity challenges) | text | usgs_mcs_2025_chromium | verified | "challenges related to deep-level mining, increased labor costs, ongoing issues with rail transportation, and an unreliable supply of electricity could affect production in South Africa" — USGS MCS 2025 p.59 |
| geopolitical_events[China_2024].event (China leading FeCr + SS producer and Cr consumer) | text | usgs_mcs_2025_chromium | verified | "China was the leading ferrochromium- and stainless-steel-producing country and the leading chromium-consuming country" — USGS MCS 2025 p.59 Events, Trends, and Issues |
| geopolitical_events[China_2024].impact (ferrochromium price $2.55→$1.80, −29%) | −29% | usgs_mcs_2025_chromium | inferred | Price values verified individually ($2.55 in 2023 and $1.80 in 2024 confirmed in Salient Statistics). The −29% change is computed: (1.80−2.55)/2.55 = −29.4%; not explicitly stated as "−29%" in source text. |
| geopolitical_events[KZ_2025].event (Kazakhstan reserves revised to 320,000 kt) | 320,000 kt | usgs_mcs_2025_chromium | verified | "Reserves for Kazakhstan were revised based on a Government report" — USGS MCS 2025 p.59; table shows 320,000 kt in Reserves column |

## Notes

**Source access**: USGS MCS 2025 Chromium PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-chromium.pdf) fetched and converted via pdftotext -layout. Both pages (pp. 58–59) fully readable. All claims trace to a single primary source.

**One discrepancy found**: The reserves_by_country notes prose states "sum of listed shares = ~97.8%." Recomputing from the listed share_pcts gives 45.0+26.7+16.7+6.6+2.25+0.69+0.55+0.05 = 98.54%; quantity-based (1,181,530/1,200,000) gives 98.46%. Both approaches yield ~98.5%, not ~97.8%. The discrepancy (~0.7 pp) is in the prose notes text only, not in any data field value.

**Zero discrepancies in data fields**: All 8 mine production quantities, all 8 reserve quantities, and all 15 price values match the USGS tables exactly. No numeric data field discrepancy found.

**All share_pcts are inferred**: USGS does not publish country percentage shares in the chromium chapter. Every share_pct value in the YAML is derived by dividing the country quantity by the stated world total (47,000 kt for mine production; 1,200,000 kt for reserves). All calculations are arithmetically correct.

**End-use percentages**: The USGS MCS 2025 chromium chapter provides no explicit end-use percentage breakdown. The chapter states only that "Stainless-steel and heat-resisting-steel producers were the leading consumers of ferrochromium" and calls superalloys "the major strategic end use." All five end-use share_pcts (70%, 19%, 5%, 3%, 3%) are historical estimates with confidence: low, and all are correctly marked as such. Treated as inferred.

**Criticality flags**: All three criticality flags (us_critical_list_as_of_2025 = true, eu_crm_list_as_of_2024 = true, eu_strategic_list_as_of_2024 = false) reference usgs_mcs_2025_chromium, but the chromium chapter text does not explicitly state list membership. These are therefore inferred from context. A direct EU CRMA Annex II citation would be needed for full verification of the EU flags.

**Grade normalization (reserves)**: Footnote 14 in the source confirms: "Units are thousand metric tons gross weight of shipping-grade chromite ore, which is deposit quantity and grade normalized to 45% Cr₂O₃, except for the United States, where grade is normalized to 7% Cr₂O₃, and Finland, where grade is normalized to 26% Cr₂O₃." This matches the YAML form_notes exactly.

**Price series completeness**: Three price series (chromite ore $/t, ferrochromium $/lb Cr content, chromium metal $/lb gross weight) × 5 years (2020–2024) = 15 values, all verified against the Salient Statistics table. Source footnote 5 confirms Argus Media Group, Argus Non-Ferrous Markets as the price source. Ferrochromium prices (footnote 6) exclude ferrosilicon chromium, as noted in YAML.

**Import sources (2020–23 average)**: Chromite ore: South Africa 96%, Turkey 3%, other 1%. Chromium primary metal: South Africa 25%, Kazakhstan 14%, Finland 7%, Russia 6%, other 48%. Total imports: South Africa 32%, Kazakhstan 11%, Canada 6%, Finland 6%, other 45%. All verified. The YAML cites these correctly — Kazakhstan's 14% refers specifically to primary metal imports, not total imports (11%).

**Consumption value**: "$900 million in 2024…a 6% increase from $846 million in 2023" — source states exactly this. Implied 6% calculation: (900−846)/846 = 6.38% ≈ 6%, consistent with statement.

**Secondary production note**: 23% of apparent consumption vs. 100 kt secondary: USGS Recycling section confirms 23% of apparent consumption. Salient Statistics shows secondary = 100 kt (2024e) and apparent consumption = 440 kt, so 100/440 = 22.7% ≈ 23%. Consistent.

**FI 2023 production (1,910 kt)**: YAML notes for Finland cite 2024e = 1,900 kt. USGS table shows 2023 = 1,910 kt. This 2023 value appears in the source but is not explicitly cited in the Cr.yaml Finland notes (which only state the 2024e value). No discrepancy in any stated value.

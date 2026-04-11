# Verification: Na

- Element: sodium (Na)
- Snapshot year: 2025
- Verifier: worker-f0bae0d62b01 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 73 |
| discrepancy | 0 |
| inferred | 29 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 280.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "World total (rounded) … 280,000" — USGS MCS 2025 p.151 World Production table, 2024e column (thousand metric tons) |
| production[0].mine.notes (2023 world total = 270,000 kt) | 270.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "World total (rounded) … 270,000" — USGS MCS 2025 p.151 World Production table, 2023 column |
| production[0].mine.notes (US 2024e = 40,000 kt) | 40.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "United States … 40,000" — p.151 World Production table 2024e; also "40 million tons" — p.150 Domestic Production text |
| production[0].mine.notes (China 2024e = 55,000 kt) | 55.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "China … 55,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[CN].quantity.value | 55.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "China … 55,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 19.64 | usgs_mcs_2025_salt | inferred | Not stated; 55,000/280,000 = 19.643% |
| production[0].mining_by_country[US].quantity.value | 40.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "United States … 40,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[US].share_pct | 14.29 | usgs_mcs_2025_salt | inferred | Not stated; 40,000/280,000 = 14.286% |
| production[0].mining_by_country[US].notes (26 companies) | 26 | usgs_mcs_2025_salt | verified | "produced by 26 companies" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (64 plants) | 64 | usgs_mcs_2025_salt | verified | "operated 64 plants" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (16 States) | 16 | usgs_mcs_2025_salt | verified | "in 16 States" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (95% from 7 States) | 95% | usgs_mcs_2025_salt | verified | "These seven States produced about 95% of the salt in the United States in 2024" — USGS MCS 2025 p.150 |
| production[0].mining_by_country[US].notes (salt in brine 42%) | 42% | usgs_mcs_2025_salt | verified | "salt in brine, 42%" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (rock salt 40%) | 40% | usgs_mcs_2025_salt | verified | "rock salt, 40%" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (solar salt 9%) | 9% | usgs_mcs_2025_salt | verified | "solar salt, 9%" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[US].notes (vacuum pan salt 9%) | 9% | usgs_mcs_2025_salt | verified | "vacuum pan salt, 9%" — USGS MCS 2025 p.150 Domestic Production and Use |
| production[0].mining_by_country[IN].quantity.value | 28.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "India … 28,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 10.00 | usgs_mcs_2025_salt | inferred | Not stated; 28,000/280,000 = 10.000% exactly |
| production[0].mining_by_country[DE].quantity.value | 16.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Germany … 16,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[DE].share_pct | 5.71 | usgs_mcs_2025_salt | inferred | Not stated; 16,000/280,000 = 5.714% |
| production[0].mining_by_country[AU].quantity.value | 13.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Australia … 13,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 4.64 | usgs_mcs_2025_salt | inferred | Not stated; 13,000/280,000 = 4.643% |
| production[0].mining_by_country[CA].quantity.value | 12.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Canada … 12,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 4.29 | usgs_mcs_2025_salt | inferred | Not stated; 12,000/280,000 = 4.286% |
| production[0].mining_by_country[CA].notes (Canada 29% of US imports) | 29% | usgs_mcs_2025_salt | verified | "Canada, 29%" — USGS MCS 2025 p.150 Import Sources (2020–23) |
| production[0].mining_by_country[CL].quantity.value | 11.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Chile … 11,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[CL].share_pct | 3.93 | usgs_mcs_2025_salt | inferred | Not stated; 11,000/280,000 = 3.929% |
| production[0].mining_by_country[CL].notes (Chile 27% of US imports) | 27% | usgs_mcs_2025_salt | verified | "Chile, 27%" — USGS MCS 2025 p.150 Import Sources (2020–23) |
| production[0].mining_by_country[TR].quantity.value | 9.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Turkey … 9,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[TR].share_pct | 3.21 | usgs_mcs_2025_salt | inferred | Not stated; 9,000/280,000 = 3.214% |
| production[0].mining_by_country[MX].quantity.value | 9.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Mexico … 9,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[MX].share_pct | 3.21 | usgs_mcs_2025_salt | inferred | Not stated; 9,000/280,000 = 3.214% |
| production[0].mining_by_country[MX].notes (Mexico 14% of US imports) | 14% | usgs_mcs_2025_salt | verified | "Mexico, 14%" — USGS MCS 2025 p.150 Import Sources (2020–23) |
| production[0].mining_by_country[RU].quantity.value | 8.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Russia … 8,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 2.86 | usgs_mcs_2025_salt | inferred | Not stated; 8,000/280,000 = 2.857% |
| production[0].mining_by_country[BR].quantity.value | 6.6 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Brazil … 6,600" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 2.36 | usgs_mcs_2025_salt | inferred | Not stated; 6,600/280,000 = 2.357% |
| production[0].mining_by_country[NL].quantity.value | 6.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Netherlands … 6,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[NL].share_pct | 2.14 | usgs_mcs_2025_salt | inferred | Not stated; 6,000/280,000 = 2.143% |
| production[0].mining_by_country[FR].quantity.value | 5.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "France … 5,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[FR].share_pct | 1.79 | usgs_mcs_2025_salt | inferred | Not stated; 5,000/280,000 = 1.786% |
| production[0].mining_by_country[PL].quantity.value | 4.6 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Poland … 4,600" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[PL].share_pct | 1.64 | usgs_mcs_2025_salt | inferred | Not stated; 4,600/280,000 = 1.643% |
| production[0].mining_by_country[ES].quantity.value | 4.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Spain … 4,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[ES].share_pct | 1.43 | usgs_mcs_2025_salt | inferred | Not stated; 4,000/280,000 = 1.429% |
| production[0].mining_by_country[BG].quantity.value | 3.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Bulgaria … 3,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[BG].share_pct | 1.07 | usgs_mcs_2025_salt | inferred | Not stated; 3,000/280,000 = 1.071% |
| production[0].mining_by_country[PK].quantity.value | 3.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Pakistan … 3,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[PK].share_pct | 1.07 | usgs_mcs_2025_salt | inferred | Not stated; 3,000/280,000 = 1.071% |
| production[0].mining_by_country[GB].quantity.value | 2.8 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "United Kingdom … 2,800" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[GB].share_pct | 1.00 | usgs_mcs_2025_salt | inferred | Not stated; 2,800/280,000 = 1.000% exactly |
| production[0].mining_by_country[IR].quantity.value | 2.7 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Iran … 2,700" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[IR].share_pct | 0.96 | usgs_mcs_2025_salt | inferred | Not stated; 2,700/280,000 = 0.964% |
| production[0].mining_by_country[SA].quantity.value | 2.4 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Saudi Arabia … 2,400" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[SA].share_pct | 0.86 | usgs_mcs_2025_salt | inferred | Not stated; 2,400/280,000 = 0.857% |
| production[0].mining_by_country[EG].quantity.value | 2.3 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Egypt … 2,300" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[EG].share_pct | 0.82 | usgs_mcs_2025_salt | inferred | Not stated; 2,300/280,000 = 0.821% |
| production[0].mining_by_country[EG].notes (Egypt 8% of US imports) | 8% | usgs_mcs_2025_salt | verified | "Egypt, 8%" — USGS MCS 2025 p.150 Import Sources (2020–23) |
| production[0].mining_by_country[BY].quantity.value | 2.1 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Belarus … 2,100" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[BY].share_pct | 0.75 | usgs_mcs_2025_salt | inferred | Not stated; 2,100/280,000 = 0.750% exactly |
| production[0].mining_by_country[IT].quantity.value | 1.9 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Italy … 1,900" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[IT].share_pct | 0.68 | usgs_mcs_2025_salt | inferred | Not stated; 1,900/280,000 = 0.679% |
| production[0].mining_by_country[ZZ].quantity.value | 28.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "Other countries … 28,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 10.00 | usgs_mcs_2025_salt | inferred | Not stated; 28,000/280,000 = 10.000% exactly |
| production[0].notes (23 named countries sum = 247,400 kt) | 247,400 kt | usgs_mcs_2025_salt | inferred | Not stated; computed from 23 named-country 2024e rows in USGS table: sum = 247,400 kt |
| production[0].notes (shares sum ~98.4%) | ~98.4% | usgs_mcs_2025_salt | inferred | Not stated; 275,400/280,000 = 98.36% — rounding artifact from stated world total vs. individual row sum |
| end_uses.uses[highway_deicing].share_pct | 41 | usgs_mcs_2025_salt | verified | "Highway deicing accounted for about 41% of total salt consumed" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[chemical_industry].share_pct | 39 | usgs_mcs_2025_salt | verified | "The chemical industry accounted for about 39% of total salt sales" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[chemical_industry].notes (91% brine for chemical feedstock) | 91% | usgs_mcs_2025_salt | verified | "with salt in brine accounting for 91% of the salt used for chemical feedstock" — USGS MCS 2025 p.150 |
| end_uses.uses[distributors].share_pct | 9 | usgs_mcs_2025_salt | verified | "distributors, 9%" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[food_processing].share_pct | 4 | usgs_mcs_2025_salt | verified | "food processing, 4%" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[agricultural].share_pct | 3 | usgs_mcs_2025_salt | verified | "agricultural, 3%" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[general_industrial].share_pct | 2 | usgs_mcs_2025_salt | verified | "general industrial, 2%" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[primary_water_treatment].share_pct | 1 | usgs_mcs_2025_salt | verified | "primary water treatment, 1%" — USGS MCS 2025 p.150 Domestic Production and Use |
| end_uses.uses[miscellaneous].share_pct | 1 | usgs_mcs_2025_salt | verified | "miscellaneous, 1%" — USGS MCS 2025 p.150 Domestic Production and Use |
| prices[vacuum_pan_2024].value | 230.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Vacuum and open pan salt … 230" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| prices[vacuum_pan_2023].value | 220.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Vacuum and open pan salt … 220" — USGS MCS 2025 p.150 Salient Statistics, 2023e column |
| prices[vacuum_pan_2022].value | 217.58 usd_per_tonne | usgs_mcs_2025_salt | verified | "Vacuum and open pan salt … 217.58" — USGS MCS 2025 p.150 Salient Statistics, 2022 column |
| prices[vacuum_pan_2021].value | 203.72 usd_per_tonne | usgs_mcs_2025_salt | verified | "Vacuum and open pan salt … 203.72" — USGS MCS 2025 p.150 Salient Statistics, 2021 column |
| prices[vacuum_pan_2020].value | 212.21 usd_per_tonne | usgs_mcs_2025_salt | verified | "Vacuum and open pan salt … 212.21" — USGS MCS 2025 p.150 Salient Statistics, 2020 column |
| prices[solar_2024].value | 140.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Solar salt … 140" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| prices[solar_2023].value | 140.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Solar salt … 140" — USGS MCS 2025 p.150 Salient Statistics, 2023e column |
| prices[solar_2022].value | 128.87 usd_per_tonne | usgs_mcs_2025_salt | verified | "Solar salt … 128.87" — USGS MCS 2025 p.150 Salient Statistics, 2022 column |
| prices[solar_2021].value | 153.52 usd_per_tonne | usgs_mcs_2025_salt | verified | "Solar salt … 153.52" — USGS MCS 2025 p.150 Salient Statistics, 2021 column |
| prices[solar_2020].value | 122.77 usd_per_tonne | usgs_mcs_2025_salt | verified | "Solar salt … 122.77" — USGS MCS 2025 p.150 Salient Statistics, 2020 column |
| prices[rock_2024].value | 56.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Rock salt … 56" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| prices[rock_2023].value | 56.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Rock salt … 56" — USGS MCS 2025 p.150 Salient Statistics, 2023e column |
| prices[rock_2022].value | 56.86 usd_per_tonne | usgs_mcs_2025_salt | verified | "Rock salt … 56.86" — USGS MCS 2025 p.150 Salient Statistics, 2022 column |
| prices[rock_2021].value | 59.88 usd_per_tonne | usgs_mcs_2025_salt | verified | "Rock salt … 59.88" — USGS MCS 2025 p.150 Salient Statistics, 2021 column |
| prices[rock_2020].value | 61.71 usd_per_tonne | usgs_mcs_2025_salt | verified | "Rock salt … 61.71" — USGS MCS 2025 p.150 Salient Statistics, 2020 column |
| prices[brine_2024].value | 10.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Salt in brine … 10" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| prices[brine_2023].value | 9.0 usd_per_tonne | usgs_mcs_2025_salt | verified | "Salt in brine … 9" — USGS MCS 2025 p.150 Salient Statistics, 2023e column |
| prices[brine_2022].value | 9.11 usd_per_tonne | usgs_mcs_2025_salt | verified | "Salt in brine … 9.11" — USGS MCS 2025 p.150 Salient Statistics, 2022 column |
| prices[brine_2021].value | 8.14 usd_per_tonne | usgs_mcs_2025_salt | verified | "Salt in brine … 8.14" — USGS MCS 2025 p.150 Salient Statistics, 2021 column |
| prices[brine_2020].value | 8.36 usd_per_tonne | usgs_mcs_2025_salt | verified | "Salt in brine … 8.36" — USGS MCS 2025 p.150 Salient Statistics, 2020 column |
| criticality.notes (net import reliance 24%) | 24% | usgs_mcs_2025_salt | verified | "Net import reliance … 24" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| geopolitical_events[2024-01].impact (apparent consumption 51 Mt) | 51 million_tonnes | usgs_mcs_2025_salt | verified | "Apparent … 51,000" — USGS MCS 2025 p.150 Salient Statistics, 2024e column |
| geopolitical_events[2024-01].impact (apparent consumption 54 Mt in 2023) | 54 million_tonnes | usgs_mcs_2025_salt | verified | "Apparent … 54,000" — USGS MCS 2025 p.150 Salient Statistics, 2023e column |
| geopolitical_events[2024-09].event (NOAA La Niña forecast, drier Gulf Coast, wetter Great Lakes) | qualitative | usgs_mcs_2025_salt | verified | "NOAA predicted a developing La Niña weather pattern … drier-than-average conditions for the Gulf Coast … wetter-than-average conditions across the Great Lakes and Northwest" — USGS MCS 2025 p.151 Events |
| geopolitical_events[2024-01].event (chloralkali demand expected to increase) | qualitative | usgs_mcs_2025_salt | verified | "Demand for salt brine used in the chloralkali industry was expected to increase in 2024 as demand for caustic soda and polyvinyl chloride increases globally, especially in Asia" — USGS MCS 2025 p.151 |
| substitutes[general].notes ("No economic substitutes…") | text | usgs_mcs_2025_salt | verified | "No economic substitutes or alternatives for salt exist in most applications" — USGS MCS 2025 p.151 Substitutes |
| substitutes[highway_deicing].notes (CaCl2, CMA, KCl for deicing at higher cost) | text | usgs_mcs_2025_salt | inferred | USGS p.151 Substitutes combines all applications: "Calcium chloride and calcium magnesium acetate, hydrochloric acid, and potassium chloride can be substituted for salt in deicing, certain chemical processes, and food flavoring, but at a higher cost." YAML splits this by application; the deicing attribution is an editorial subdivision |
| substitutes[chemical_processing].notes (HCl, KCl for chemical processes at higher cost) | text | usgs_mcs_2025_salt | inferred | USGS p.151 Substitutes provides a single combined sentence listing all substitutes across all applications; YAML's chemical-processing breakdown is an editorial subdivision of that sentence |
| substitutes[food_flavoring].notes (KCl for food flavoring at higher cost) | text | usgs_mcs_2025_salt | inferred | USGS p.151 Substitutes provides a single combined sentence; YAML's food-flavoring breakdown is an editorial subdivision |

## Notes

**Source access**: USGS MCS 2025 Salt PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-salt.pdf) fetched and converted via pdftotext -layout. Both pages (pp. 150–151) fully readable. All claims trace to a single primary source.

**Zero discrepancies**: All 24 country production quantities match the USGS World Production table exactly. All 20 price values match the Salient Statistics table exactly. All 8 end-use percentages match exactly. No numeric discrepancy found in any claim.

**All share_pcts are inferred**: USGS does not publish country percentage shares in the salt chapter. Every share_pct value in the YAML is derived by dividing the country's 2024e quantity by the stated rounded world total (280,000 kt). All calculations are arithmetically correct.

**Unit note (production)**: The USGS salt chapter header reads "(Data in thousand metric tons unless otherwise specified)". The Domestic Production narrative text says "40 million tons" for US production — USGS uses "tons" loosely in narrative text, but the table value of 40,000 (thousand metric tons = 40 million metric tons) is authoritative. The YAML's 40.0 million_tonnes_per_year is correct.

**Reserves are qualitative only**: USGS provides no numeric reserves for salt. The reserves column in the World Production table reads: "Large. Economic and subeconomic deposits of salt are substantial in principal salt-producing countries. The oceans contain a virtually inexhaustible supply of salt." The YAML correctly omits any quantitative economic_reserves value.

**Substitutes paragraph**: The USGS substitutes paragraph is a single sentence listing all substituents applicable across all three applications (deicing, chemical processes, food flavoring). The YAML subdivides this by application, which is a reasonable editorial choice but not explicitly stated in the source; those three rows are therefore marked `inferred`.

**Sum check**: The 23 named-country 2024e quantities sum to 247,400 kt; adding Other countries (28,000 kt) gives 275,400 kt. The stated world total is 280,000 kt (rounded). The ~4,600 kt gap is rounding at the world-total level; the individual country rows are summed from the table and match exactly. Shares sum to 275,400/280,000 = 98.36% ≈ 98.4%.

**Price series completeness**: Four price series (vacuum/open pan, solar, rock, brine) × 5 years (2020–2024) = 20 values, all verified against Salient Statistics table. The 2023 and 2024 values carry the "e" (estimated) superscript in the source; the YAML notes record them accordingly.

**Criticality**: Salt does not appear on any US Critical Minerals List, EU CRM List, or EU Strategic Raw Materials List. No source_id is attached to the criticality flags, consistent with their observable absence from known critical minerals frameworks. The 24% net import reliance figure is verified from the Salient Statistics table.

**Import sources (2020–23 average)**: Canada 29%, Chile 27%, Mexico 14%, Egypt 8%, other 22%. All four named shares verified. These are 4-year averages (2020–23), not 2024 data.

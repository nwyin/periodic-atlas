# Verification: Ca

- Element: calcium (Ca)
- Snapshot year: 2025
- Verifier: worker-5e1033a6035f (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 62 |
| discrepancy | 0 |
| inferred | 30 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 420.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "World total (rounded) … 420,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column (thousand metric tons) |
| production[0].mine.notes (2023 world total) | 424,000 thousand_metric_tons | usgs_mcs_2025_lime | verified | "World total (rounded) … 424,000" — USGS MCS 2025 p.109 World Lime Production table, 2023 column |
| production[0].mine.notes (US 16,000 kt, $3.2B) | 16,000 kt; $3.2 billion | usgs_mcs_2025_lime | verified | "In 2024, an estimated 16 million tons of quicklime and hydrated lime was produced … valued at about $3.2 billion" — USGS MCS 2025 p.108 Domestic Production and Use |
| production[0].mine.notes (26 companies, 73 plants, 28 states + PR) | 26 companies; 73 plants; 28 States | usgs_mcs_2025_lime | verified | "Lime was produced by 26 companies … 73 primary lime plants (plants operating quicklime kilns) in 28 States and Puerto Rico" — USGS MCS 2025 p.108 |
| production[0].mine.notes (5 leading companies = ~80% of US production) | ~80% | usgs_mcs_2025_lime | verified | "the five leading U.S. lime companies … accounted for about 80% of U.S. lime production" — USGS MCS 2025 p.108 |
| production[0].mine.notes (leading states: AL, MO, OH, TX) | Alabama, Missouri, Ohio, Texas | usgs_mcs_2025_lime | verified | "Principal producing States were Alabama, Missouri, Ohio, and Texas" — USGS MCS 2025 p.108 |
| production[0].mine.notes (China ~74% of world) | ~74% | usgs_mcs_2025_lime | inferred | Not stated explicitly; 310,000 / 420,000 = 73.81% ≈ 74%. USGS table shows CN = 310,000 kt, world total = 420,000 kt |
| production[0].mining_by_country[CN].quantity.value | 310.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "China … 310,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 73.81 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 310,000 / 420,000 = 73.810% |
| production[0].mining_by_country[IN].quantity.value | 17.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "India … 17,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 4.05 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 17,000 / 420,000 = 4.048% |
| production[0].mining_by_country[US].quantity.value | 16.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "United States … 16,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[US].share_pct | 3.81 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 16,000 / 420,000 = 3.810% |
| production[0].mining_by_country[RU].quantity.value | 11.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Russia (industrial and construction) … 11,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 2.62 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 11,000 / 420,000 = 2.619% |
| production[0].mining_by_country[BR].quantity.value | 8.1 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Brazil … 8,100" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 1.93 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 8,100 / 420,000 = 1.929% |
| production[0].mining_by_country[JP].quantity.value | 6.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Japan (quicklime only) … 6,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[JP].share_pct | 1.43 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 6,000 / 420,000 = 1.429% |
| production[0].mining_by_country[DE].quantity.value | 5.7 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Germany … 5,700" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[DE].share_pct | 1.36 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 5,700 / 420,000 = 1.357% |
| production[0].mining_by_country[KR].quantity.value | 5.1 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Korea, Republic of … 5,100" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[KR].share_pct | 1.21 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 5,100 / 420,000 = 1.214% |
| production[0].mining_by_country[TR].quantity.value | 4.1 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Turkey … 4,100" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[TR].share_pct | 0.98 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 4,100 / 420,000 = 0.976% |
| production[0].mining_by_country[IR].quantity.value | 4.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Iran … 4,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[IR].share_pct | 0.95 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 4,000 / 420,000 = 0.952% |
| production[0].mining_by_country[FR].quantity.value | 3.5 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "France … 3,500" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[FR].share_pct | 0.83 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 3,500 / 420,000 = 0.833% |
| production[0].mining_by_country[IT].quantity.value | 2.4 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Italy … 2,400" — USGS MCS 2025 p.109 World Lime Production table, 2024e column (includes hydraulic lime) |
| production[0].mining_by_country[IT].share_pct | 0.57 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 2,400 / 420,000 = 0.571% |
| production[0].mining_by_country[AU].quantity.value | 2.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Australia … 2,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 0.48 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 2,000 / 420,000 = 0.476% |
| production[0].mining_by_country[CA].quantity.value | 1.9 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Canada … 1,900" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 0.45 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,900 / 420,000 = 0.452% |
| production[0].mining_by_country[CA].notes (82% of US imports 2020–23) | 82% | usgs_mcs_2025_lime | verified | "Import Sources (2020–23): Canada, 82%" — USGS MCS 2025 p.108 |
| production[0].mining_by_country[ES].quantity.value | 1.7 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Spain … 1,700" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[ES].share_pct | 0.40 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,700 / 420,000 = 0.405% |
| production[0].mining_by_country[MY].quantity.value | 1.5 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Malaysia … 1,500" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[MY].share_pct | 0.36 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,500 / 420,000 = 0.357% |
| production[0].mining_by_country[GB].quantity.value | 1.4 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "United Kingdom … 1,400" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[GB].share_pct | 0.33 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,400 / 420,000 = 0.333% |
| production[0].mining_by_country[BG].quantity.value | 1.3 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Bulgaria … 1,300" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[BG].share_pct | 0.31 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,300 / 420,000 = 0.310% |
| production[0].mining_by_country[PL].quantity.value | 1.3 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Poland (hydrated and quicklime) … 1,300" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[PL].share_pct | 0.31 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,300 / 420,000 = 0.310% |
| production[0].mining_by_country[ZA].quantity.value | 1.1 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "South Africa … 1,100" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[ZA].share_pct | 0.26 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,100 / 420,000 = 0.262% |
| production[0].mining_by_country[UA].quantity.value | 1.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Ukraine … 1,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[UA].share_pct | 0.24 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,000 / 420,000 = 0.238% |
| production[0].mining_by_country[BE].quantity.value | 1.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Belgium … 1,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column (includes hydraulic lime) |
| production[0].mining_by_country[BE].share_pct | 0.24 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 1,000 / 420,000 = 0.238% |
| production[0].mining_by_country[ZZ].quantity.value | 17.0 million_tonnes_per_year | usgs_mcs_2025_lime | verified | "Other countries … 17,000" — USGS MCS 2025 p.109 World Lime Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 4.05 | usgs_mcs_2025_lime | inferred | Not stated explicitly; 17,000 / 420,000 = 4.048% |
| feedstock_origins[limestone].notes (depletion allowance 14%) | 14% | usgs_mcs_2025_lime | verified | "Depletion Allowance: Limestone produced and used for lime production, 14% (domestic and foreign)" — USGS MCS 2025 p.108 |
| feedstock_origins[dolomite].notes (included in production stats) | quicklime + hydrated + refractory dead-burned dolomite | usgs_mcs_2025_lime | verified | "Data are for quicklime, hydrated lime, and refractory dead-burned dolomite" — USGS MCS 2025 p.109 footnote 1 |
| feedstock_origins[dolomite].notes (3% ad valorem tariff) | 3% ad valorem | usgs_mcs_2025_lime | verified | "Calcined dolomite … 3% ad valorem" — USGS MCS 2025 p.108 Tariff table, HTS 2518.20.0000 |
| substitutes[fluxing_agriculture_sulfur_removal].notes | limestone for agriculture/fluxing/sulfur removal | usgs_mcs_2025_lime | verified | "Limestone is a substitute for lime in many applications, such as agriculture, fluxing, and sulfur removal … slower to react … considerably less expensive than lime" — USGS MCS 2025 p.109 Substitutes |
| substitutes[industrial_plasters_mortars].notes | calcined gypsum | usgs_mcs_2025_lime | verified | "Calcined gypsum is an alternative material in industrial plasters and mortars" — USGS MCS 2025 p.109 Substitutes |
| substitutes[construction].notes | cement, cement kiln dust, fly ash, lime kiln dust | usgs_mcs_2025_lime | verified | "Cement, cement kiln dust, fly ash, and lime kiln dust are potential substitutes for some construction uses of lime" — USGS MCS 2025 p.109 Substitutes |
| substitutes[ph_control].notes | magnesium hydroxide | usgs_mcs_2025_lime | verified | "Magnesium hydroxide is a substitute for lime in pH control" — USGS MCS 2025 p.109 Substitutes |
| substitutes[steelmaking_flux].notes | magnesium oxide | usgs_mcs_2025_lime | verified | "magnesium oxide is a substitute for dolomitic lime as a flux in steelmaking" — USGS MCS 2025 p.109 Substitutes |
| end_uses.uses[steelmaking] (1st listed) | steelmaking | usgs_mcs_2025_lime | verified | "Major markets for lime were, in descending order of consumption, steelmaking …" — USGS MCS 2025 p.108 Domestic Production and Use |
| end_uses.uses[steelmaking].share_pct | 35 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; USGS lists steelmaking 1st in descending order only. Share is approximate per YAML notes (confidence: low) |
| end_uses.uses[chemical_and_industrial] (2nd listed) | chemical and industrial applications | usgs_mcs_2025_lime | verified | "… steelmaking, chemical and industrial applications (such as the manufacture of fertilizer, glass, paper and pulp, and precipitated calcium carbonate, and in sugar refining) …" — USGS MCS 2025 p.108 |
| end_uses.uses[chemical_and_industrial].share_pct | 27 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; listed 2nd in descending order. Share is approximate (confidence: low) |
| end_uses.uses[flue_gas_treatment] (3rd listed) | flue gas treatment | usgs_mcs_2025_lime | verified | "… flue gas treatment …" — USGS MCS 2025 p.108 end-use list |
| end_uses.uses[flue_gas_treatment].share_pct | 15 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; listed 3rd in descending order. Share is approximate (confidence: low) |
| end_uses.uses[construction] (4th listed) | construction | usgs_mcs_2025_lime | verified | "… construction …" — USGS MCS 2025 p.108 end-use list |
| end_uses.uses[construction].share_pct | 10 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; listed 4th in descending order. Share is approximate (confidence: low) |
| end_uses.uses[water_treatment] (5th listed) | water treatment | usgs_mcs_2025_lime | verified | "… water treatment …" — USGS MCS 2025 p.108 end-use list |
| end_uses.uses[water_treatment].share_pct | 8 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; listed 5th in descending order. Share is approximate (confidence: low) |
| end_uses.uses[nonferrous_metal_mining] (6th listed) | nonferrous-metal mining | usgs_mcs_2025_lime | verified | "… and nonferrous-metal mining" — USGS MCS 2025 p.108 end-use list (6th and last) |
| end_uses.uses[nonferrous_metal_mining].share_pct | 5 (approximate) | usgs_mcs_2025_lime | inferred | Not stated explicitly; listed last (6th) in descending order. Share is approximate (confidence: low) |
| prices[year=2024, form=oxide].value | 190.0 usd_per_tonne | usgs_mcs_2025_lime | verified | "Quicklime … 190" — USGS MCS 2025 p.108 Salient Statistics, 2024e column, Price average value dollars per metric ton at plant |
| prices[year=2023, form=oxide].value | 183.1 usd_per_tonne | usgs_mcs_2025_lime | verified | "Quicklime … 183.1" — USGS MCS 2025 p.108 Salient Statistics, 2023 column |
| prices[year=2022, form=oxide].value | 151.3 usd_per_tonne | usgs_mcs_2025_lime | verified | "Quicklime … 151.3" — USGS MCS 2025 p.108 Salient Statistics, 2022 column |
| prices[year=2021, form=oxide].value | 133.4 usd_per_tonne | usgs_mcs_2025_lime | verified | "Quicklime … 133.4" — USGS MCS 2025 p.108 Salient Statistics, 2021 column |
| prices[year=2020, form=oxide].value | 131.4 usd_per_tonne | usgs_mcs_2025_lime | verified | "Quicklime … 131.4" — USGS MCS 2025 p.108 Salient Statistics, 2020 column |
| prices[year=2024, form=hydroxide].value | 240.0 usd_per_tonne | usgs_mcs_2025_lime | verified | "Hydrated … 240" — USGS MCS 2025 p.108 Salient Statistics, 2024e column |
| prices[year=2023, form=hydroxide].value | 235.0 usd_per_tonne | usgs_mcs_2025_lime | verified | "Hydrated … 235.0" — USGS MCS 2025 p.108 Salient Statistics, 2023 column |
| prices[year=2022, form=hydroxide].value | 183.1 usd_per_tonne | usgs_mcs_2025_lime | verified | "Hydrated … 183.1" — USGS MCS 2025 p.108 Salient Statistics, 2022 column |
| prices[year=2021, form=hydroxide].value | 159.6 usd_per_tonne | usgs_mcs_2025_lime | verified | "Hydrated … 159.6" — USGS MCS 2025 p.108 Salient Statistics, 2021 column |
| prices[year=2020, form=hydroxide].value | 156.0 usd_per_tonne | usgs_mcs_2025_lime | verified | "Hydrated … 156.0" — USGS MCS 2025 p.108 Salient Statistics, 2020 column |
| geopolitical_events[2024-01].event (production unchanged) | unchanged from 2023 | usgs_mcs_2025_lime | verified | "In 2024, domestic lime production was estimated to be unchanged from that in 2023" — USGS MCS 2025 p.108 Events, Trends, and Issues |
| geopolitical_events[2024-01].event (increased pricing) | higher production costs → increased pricing | usgs_mcs_2025_lime | verified | "some of the lime producers have increased product pricing owing to increased costs of production" — USGS MCS 2025 p.108 Events |
| geopolitical_events[2024-01].event (decarbonization plans) | accelerate decarbonization | usgs_mcs_2025_lime | verified | "Several companies were planning to accelerate their decarbonization efforts in the production of lime" — USGS MCS 2025 p.108 Events |
| geopolitical_events[2024-01].event (73 quicklime + 10 hydrating plants) | 73 quicklime plants; 10 hydrating plants | usgs_mcs_2025_lime | verified | "In 2024, a total of 73 quicklime plants were in operation along with 10 hydrating plants" — USGS MCS 2025 p.108 Events |
| geopolitical_events[2024-01].event (net import reliance <1%) | <1% | usgs_mcs_2025_lime | verified | "Net import reliance as a percentage of apparent consumption … <1" (2024e) — USGS MCS 2025 p.108 Salient Statistics |
| geopolitical_events[2024-01].event (Canada 82%, Mexico 13% imports) | Canada 82%; Mexico 13%; other 5% | usgs_mcs_2025_lime | verified | "Import Sources (2020–23): Canada, 82%; Mexico, 13%; and other, 5%" — USGS MCS 2025 p.108 |
| reserves.notes ("Adequate for all countries") | "Adequate for all countries with listed production" | usgs_mcs_2025_lime | verified | "Adequate for all countries with listed production" — USGS MCS 2025 p.109 Reserves column of World Lime Production table |
| reserves.notes (resources "very large") | "very large" | usgs_mcs_2025_lime | verified | "Domestic and world resources of limestone and dolomite suitable for lime manufacture are very large" — USGS MCS 2025 p.109 World Resources |

## Notes

**Source access**: USGS MCS 2025 Lime PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-lime.pdf) fetched and converted with pdftotext. Both pages (pp. 108–109) rendered cleanly. All claims trace to a single primary source.

**All claims verified or inferred — zero discrepancies**: Every quantitative value in Ca.yaml matches the USGS lime chapter exactly. All share_pct fields are marked `inferred` because USGS does not state country percentage shares explicitly.

**Production sum check**: 22 named countries plus "Other countries" sum to 424,100 kt vs. world total (rounded) of 420,000 kt. The YAML's mining_by_country notes section states the sum as "423,100 kt" — this is a minor arithmetic error in the notes prose only (off by 1,000 kt); all individual country values are correct. The actual overshoot relative to the rounded world total is 4,100 kt (not 3,100 kt as noted in the YAML). This arithmetic error in the notes prose does not affect any data fields and is flagged here for a follow-up correction pass.

**No per-country reserves**: The USGS lime chapter provides no quantitative reserves data for any country. The reserves column simply states "Adequate for all countries with listed production." Ca.yaml correctly stores no numeric reserves quantities.

**End-use share_pcts are approximations**: USGS provides only the ordering of end uses (steelmaking → chemical_and_industrial → flue_gas_treatment → construction → water_treatment → nonferrous_metal_mining) without any percentages. All six share_pct values (35, 27, 15, 10, 8, 5) are author approximations, correctly marked confidence: low and completeness: partial. These are reasonable industry estimates consistent with the ordering.

**Price series accuracy**: All ten price points (5 years × 2 products) match the Salient Statistics table exactly: quicklime series ($131.4, $133.4, $151.3, $183.1, $190) and hydrated lime series ($156.0, $159.6, $183.1, $235.0, $240) for 2020–2024.

**Recycling note confirmed**: USGS states "Large quantities of lime are regenerated by paper mills. Some municipal water-treatment plants regenerate lime from softening sludge. Quicklime is regenerated from waste hydrated lime in the carbide industry." Ca.yaml does not encode a recycling field but the notes in water_treatment end-use are consistent with this.

**CO₂ emission figure in geopolitical_events notes**: The Ca.yaml notes mention "~440 kg CO₂ per tonne of quicklime as process emissions." This is a standard chemistry fact (calcination stoichiometry for CaCO₃ → CaO + CO₂, MW ratio = 44/56 ≈ 0.786, giving ~786 kg CO₂/t quicklime total from calcination; 440 kg refers only to the process/mineral CO₂ release excluding fuel combustion) and is not directly sourced from the USGS lime chapter. It is consistent with widely-reported industry data but cannot be verified against usgs_mcs_2025_lime specifically. Not included as a claim row as it appears only in explanatory prose within the geopolitical_events impact field, not as a primary numeric claim with source_id.

**Criticality**: No source_id is attached to the criticality boolean flags (us_critical_list_as_of_2025, eu_crm_list_as_of_2024, eu_strategic_list_as_of_2024). These are negative claims (all false) consistent with the USGS characterization of lime as a non-critical, widely-available commodity. Not included in Claims table as they carry no source_id.

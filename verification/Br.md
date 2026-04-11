# Verification: Br

- Element: bromine (Br)
- Snapshot year: 2025
- Verifier: worker-316e63c9c6bf (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 47 |
| discrepancy | 0 |
| inferred | 19 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 400,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "World total (rounded) … 400,000" — USGS MCS 2025 p.51 World Production table, 2024e column (footnote 12: Excludes U.S. production) |
| production[0].mine.notes (2023 world total 395,000 t) | 395,000 | usgs_mcs_2025_bromine | verified | "World total (rounded) … 395,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[IL].quantity.value | 140,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "Israel … 140,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[IL].notes (2023 = 143,000) | 143,000 | usgs_mcs_2025_bromine | verified | "Israel … 143,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[IL].share_pct | 35.0 | usgs_mcs_2025_bromine | inferred | Not stated; 140,000 / 400,000 = 35.0% (computed against published ex-U.S. world total) |
| production[0].mining_by_country[JO].quantity.value | 120,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "Jordan … 120,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[JO].notes (2023 = 116,000) | 116,000 | usgs_mcs_2025_bromine | verified | "Jordan … 116,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[JO].share_pct | 30.0 | usgs_mcs_2025_bromine | inferred | Not stated; 120,000 / 400,000 = 30.0% |
| production[0].mining_by_country[CN].quantity.value | 100,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "China … 100,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[CN].notes (2023 = 101,000) | 101,000 | usgs_mcs_2025_bromine | verified | "China … 101,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[CN].share_pct | 25.0 | usgs_mcs_2025_bromine | inferred | Not stated; 100,000 / 400,000 = 25.0% |
| production[0].mining_by_country[JP].quantity.value | 20,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "Japan … 20,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[JP].notes (unchanged from 2023 = 20,000) | 20,000 | usgs_mcs_2025_bromine | verified | "Japan … 20,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[JP].share_pct | 5.0 | usgs_mcs_2025_bromine | inferred | Not stated; 20,000 / 400,000 = 5.0% |
| production[0].mining_by_country[UA].quantity.value | 8,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "Ukraine … 8,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[UA].notes (unchanged from 2023 = 8,000) | 8,000 | usgs_mcs_2025_bromine | verified | "Ukraine … 8,000" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[UA].share_pct | 2.0 | usgs_mcs_2025_bromine | inferred | Not stated; 8,000 / 400,000 = 2.0% |
| production[0].mining_by_country[IN].quantity.value | 7,000 tonnes_per_year | usgs_mcs_2025_bromine | verified | "India … 7,000" — USGS MCS 2025 p.51 World Production table, 2024e column |
| production[0].mining_by_country[IN].notes (2023 = 6,900) | 6,900 | usgs_mcs_2025_bromine | verified | "India … 6,900" — USGS MCS 2025 p.51 World Production table, 2023 column |
| production[0].mining_by_country[IN].share_pct | 1.75 | usgs_mcs_2025_bromine | inferred | Not stated; 7,000 / 400,000 = 1.75% |
| reserves.reserves_by_country[US].quantity.value | 11,000,000 tonnes | usgs_mcs_2025_bromine | verified | "United States … 11,000,000" — USGS MCS 2025 p.51 World Production and Reserves table, Reserves column |
| reserves.reserves_by_country[US].share_pct | 95.74 | usgs_mcs_2025_bromine | inferred | Not stated; 11,000,000 / 11,490,000 = 95.735% ≈ 95.74% (denominator = US + JO + CN quantifiable subset) |
| reserves.reserves_by_country[JO].quantity.value | 360,000 tonnes | usgs_mcs_2025_bromine | verified | "Jordan … 360,000" — USGS MCS 2025 p.51 World Production and Reserves table, Reserves column |
| reserves.reserves_by_country[JO].share_pct | 3.13 | usgs_mcs_2025_bromine | inferred | Not stated; 360,000 / 11,490,000 = 3.133% ≈ 3.13% |
| reserves.reserves_by_country[CN].quantity.value | 130,000 tonnes | usgs_mcs_2025_bromine | verified | "China … 130,000" — USGS MCS 2025 p.51 World Production and Reserves table, Reserves column |
| reserves.reserves_by_country[CN].share_pct | 1.13 | usgs_mcs_2025_bromine | inferred | Not stated; 130,000 / 11,490,000 = 1.131% ≈ 1.13% |
| reserves.notes (quantifiable subset 11,490,000 t) | 11,490,000 | usgs_mcs_2025_bromine | inferred | Not stated; arithmetic sum 11,000,000 + 360,000 + 130,000 = 11,490,000 (Israel = Large, India/Japan/Ukraine = NA) |
| reserves.notes (world total = "Large") | Large | usgs_mcs_2025_bromine | verified | "World total … Large" — USGS MCS 2025 p.51 World Production and Reserves table, Reserves column |
| reserves.notes (seawater ~65 ppm) | ~65 ppm | usgs_mcs_2025_bromine | verified | "Seawater contains about 65 parts per million bromine" — USGS MCS 2025 p.51 World Resources |
| reserves.notes (100 trillion tons seawater) | 100 trillion tons | usgs_mcs_2025_bromine | verified | "or an estimated 100 trillion tons" — USGS MCS 2025 p.51 World Resources |
| reserves.notes (Dead Sea 1 billion tons) | 1 billion tons | usgs_mcs_2025_bromine | verified | "The Dead Sea … is estimated to contain 1 billion tons of bromine" — USGS MCS 2025 p.51 World Resources |
| feedstock_origins[underground_bromide_brine].notes (two companies in Arkansas) | two companies, Arkansas | usgs_mcs_2025_bromine | verified | "Bromine was recovered from underground brines by two companies in Arkansas" — USGS MCS 2025 p.50 Domestic Production and Use |
| feedstock_origins[underground_bromide_brine].notes (Smackover Formation) | Smackover Formation | usgs_mcs_2025_bromine | inferred | Not stated in this chapter; well-established geological knowledge about Arkansas bromine production |
| feedstock_origins[underground_bromide_brine].notes (Dead Sea 1 billion tons) | 1 billion tons | usgs_mcs_2025_bromine | verified | "The Dead Sea … is estimated to contain 1 billion tons of bromine" — USGS MCS 2025 p.51 World Resources |
| feedstock_origins[seawater].notes (65 ppm) | ~65 ppm | usgs_mcs_2025_bromine | verified | "Seawater contains about 65 parts per million bromine" — USGS MCS 2025 p.51 World Resources |
| feedstock_origins[seawater].notes (100 trillion tons) | 100 trillion tons | usgs_mcs_2025_bromine | verified | "or an estimated 100 trillion tons" — USGS MCS 2025 p.51 World Resources |
| prices[2024].value | 2.70 USD/kg | usgs_mcs_2025_bromine | verified | "2.70" — USGS MCS 2025 p.50 Salient Statistics, Price row, 2024e column |
| prices[2023].value | 2.92 USD/kg | usgs_mcs_2025_bromine | verified | "2.92" — USGS MCS 2025 p.50 Salient Statistics, Price row, 2023 column |
| prices[2022].value | 3.29 USD/kg | usgs_mcs_2025_bromine | verified | "3.29" — USGS MCS 2025 p.50 Salient Statistics, Price row, 2022 column |
| prices[2021].value | 2.85 USD/kg | usgs_mcs_2025_bromine | verified | "2.85" — USGS MCS 2025 p.50 Salient Statistics, Price row, 2021 column |
| prices[2020].value | 2.67 USD/kg | usgs_mcs_2025_bromine | verified | "2.67" — USGS MCS 2025 p.50 Salient Statistics, Price row, 2020 column |
| prices[2024].notes (export unit value ~$3.30/kg) | ~$3.30/kg | usgs_mcs_2025_bromine | verified | "approximately $3.30 per kilogram" — USGS MCS 2025 p.51 Events, export unit value 2024 |
| prices[2023].notes (export unit value $3.28/kg) | $3.28/kg | usgs_mcs_2025_bromine | verified | "$3.28 per kilogram in 2023" — USGS MCS 2025 p.51 Events |
| prices[2024].notes (8% less than 2023) | 8% | usgs_mcs_2025_bromine | verified | "8% less than that in 2023" — USGS MCS 2025 p.51 Events (import unit value) |
| geopolitical_events[BVO] date July 2024 | 2024-07 | usgs_mcs_2025_bromine | verified | "In July 2024, the U.S. Food and Drug Administration (FDA) revoked the authorization for brominated vegetable oil (BVO)" — USGS MCS 2025 p.51 Events |
| geopolitical_events[BVO] FR v.89 no.128 July 3 p.55040–55045 | FR v.89 no.128 p.55040–55045 | usgs_mcs_2025_bromine | verified | Footnote 9: "Federal Register, v. 89, no. 128, July 3, p. 55040–55045" — USGS MCS 2025 p.51 |
| geopolitical_events[imports 2024] 20% increase | 20% | usgs_mcs_2025_bromine | verified | "estimated total imports … increased by 20% from those in 2023" — USGS MCS 2025 p.51 Events |
| geopolitical_events[imports 2024] imports 61,000 t 2024e | 61,000 | usgs_mcs_2025_bromine | verified | "Imports for consumption … 61,000" — USGS MCS 2025 p.50 Salient Statistics, 2024e column |
| geopolitical_events[imports 2024] imports 50,800 t 2023 | 50,800 | usgs_mcs_2025_bromine | verified | "Imports for consumption … 50,800" — USGS MCS 2025 p.50 Salient Statistics, 2023 column |
| geopolitical_events[imports 2024] Israel 87% gross imports through July 2024 | 87% | usgs_mcs_2025_bromine | verified | "leading source of imports … through July 2024 was Israel (87%)" — USGS MCS 2025 p.51 Events |
| geopolitical_events[imports 2024] Jordan 10% through July 2024 | 10% | usgs_mcs_2025_bromine | verified | "followed by Jordan (10%)" — USGS MCS 2025 p.51 Events |
| geopolitical_events[imports 2024] avg import unit value $2.70/kg | $2.70/kg | usgs_mcs_2025_bromine | verified | "average annual unit value of imported bromine … was approximately $2.70 per kilogram" — USGS MCS 2025 p.51 Events |
| geopolitical_events[imports 2024] >90% bromides/bromide oxides | >90% | usgs_mcs_2025_bromine | verified | "accounting for more than 90% of total imported bromine" — USGS MCS 2025 p.51 Events |
| geopolitical_events[exports 2024] 13% decrease | 13% | usgs_mcs_2025_bromine | verified | "estimated total exports … decreased by 13% compared with those in 2023" — USGS MCS 2025 p.51 Events |
| geopolitical_events[exports 2024] exports 34,000 t 2024e | 34,000 | usgs_mcs_2025_bromine | verified | "Exports … 34,000" — USGS MCS 2025 p.50 Salient Statistics, 2024e column |
| geopolitical_events[exports 2024] exports 38,900 t 2023 | 38,900 | usgs_mcs_2025_bromine | verified | "Exports … 38,900" — USGS MCS 2025 p.50 Salient Statistics, 2023 column |
| geopolitical_events[exports 2024] Guyana 29%, Saudi Arabia 25%, UK 14% | 29%, 25%, 14% | usgs_mcs_2025_bromine | verified | "Guyana (29%), Saudi Arabia (25%), and the United Kingdom (14%)" — USGS MCS 2025 p.51 Events |
| geopolitical_events[exports 2024] export unit value $3.30/kg | $3.30/kg | usgs_mcs_2025_bromine | verified | "approximately $3.30 per kilogram" — USGS MCS 2025 p.51 Events |
| geopolitical_events[exports 2024] export unit value $3.28/kg 2023 | $3.28/kg | usgs_mcs_2025_bromine | verified | "$3.28 per kilogram in 2023" — USGS MCS 2025 p.51 Events |
| geopolitical_events[Jordan reserve revision] company reports | reserves revised | usgs_mcs_2025_bromine | verified | "Reserves for Jordan were revised based on company reports." — USGS MCS 2025 p.51 World Production and Reserves note |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_bromine | inferred | Not stated in source; bromine absent from 2022 US Critical Minerals List (Federal Register) |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_bromine | inferred | Not stated in source; bromine absent from EU CRM Annex I/II lists |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_bromine | inferred | Not stated in source; bromine absent from EU CRMA 2024 Annex I strategic list |
| criticality.notes (net import reliance "E" 2020–21) | E (net exporter) | usgs_mcs_2025_bromine | verified | "Net import reliance … E E" — USGS MCS 2025 p.50 Salient Statistics, 2020 and 2021 columns |
| criticality.notes (net import reliance <25% in 2022–24) | <25% | usgs_mcs_2025_bromine | verified | "Net import reliance … <25 <25 <25" — USGS MCS 2025 p.50 Salient Statistics, 2022–2024e columns |
| criticality.notes (Israel 83% gross import weight 2020–23) | 83% | usgs_mcs_2025_bromine | verified | "Israel, 83%" — USGS MCS 2025 p.50 Import Sources (2020–23) |
| criticality.notes (Jordan 9%) | 9% | usgs_mcs_2025_bromine | verified | "Jordan, 9%" — USGS MCS 2025 p.50 Import Sources (2020–23) |
| criticality.notes (China 3%) | 3% | usgs_mcs_2025_bromine | verified | "China, 3%" — USGS MCS 2025 p.50 Import Sources (2020–23) |
| end_uses[brominated_flame_retardants].share_pct | 35 | usgs_mcs_2025_bromine | inferred | No explicit % in source; "leading global applications … brominated flame retardants (BFRs)" — USGS MCS 2025 p.50 |
| end_uses[clear_brine_drilling_fluids].share_pct | 35 | usgs_mcs_2025_bromine | inferred | No explicit % in source; "leading global applications … clear brine drilling fluids" — USGS MCS 2025 p.50 |
| end_uses[industrial_uses_and_intermediates].share_pct | 15 | usgs_mcs_2025_bromine | inferred | No explicit % in source; "industrial uses, as intermediates" listed as application — USGS MCS 2025 p.50 |
| end_uses[water_treatment].share_pct | 10 | usgs_mcs_2025_bromine | inferred | No explicit % in source; "water treatment" listed as application — USGS MCS 2025 p.50 |
| end_uses[other_uses].share_pct | 5 | usgs_mcs_2025_bromine | inferred | No explicit % in source; zinc-bromine batteries, photographic chemicals listed — USGS MCS 2025 p.50 Recycling |

## Notes

All numeric claims derive from a single source: USGS MCS 2025 Bromine chapter (pp. 50–51). The PDF was fetched from https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-bromine.pdf and extracted via pdftotext -layout.

Key structural facts confirmed:
- World production totals (2023: 395,000 t; 2024e: 400,000 t) explicitly EXCLUDE U.S. production per footnote 12: "Excludes U.S. production."
- U.S. production is "W" (withheld) for all five years in the Salient Statistics table.
- World reserves = "Large" (unquantified). Named quantified reserves: US 11,000,000 t; Jordan 360,000 t; China 130,000 t. Israel = "Large"; India, Japan, Ukraine = "NA."
- Share percentages (share_pct) for production and reserves are not stated in the source; all are computed as simple division and marked `inferred`.
- End-use share percentages are analyst estimates with no explicit % in the USGS chapter; all marked `inferred`.
- Criticality flags (false for all three lists) reflect external policy knowledge not stated in the USGS chapter; all marked `inferred`.
- "Smackover Formation" is geological common knowledge not mentioned by name in this USGS chapter (source says only "two companies in Arkansas"); marked `inferred`.
- No discrepancies found between YAML values and source document.

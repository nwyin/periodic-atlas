# Verification: Bi

- Element: bismuth (Bi)
- Snapshot year: 2025
- Verifier: worker-1e208fbbf48c (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 43 |
| discrepancy | 0 |
| inferred | 0 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 16000 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 60-60: "Estimated world production of bismuth was 16,000 tons in 2024". |
| production[0].refined.notes "16,200 metric tons in 2023" | 16200 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 60-60: "16,000 tons in 2024 compared with 16,200 tons in 2023." |
| production[0].refined.notes "world mine production ... not reported" | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 75-80 says reserves/resources were not reported at mine or country level and bismuth is usually a byproduct; MYB 2022 p.4, lines 142-145 adds that a world total for mined bismuth ore "was not available" and production data are available only once refined. |
| production[0].refining_by_country.shares[BO].quantity.value | 70 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 66: "Bolivia 68 70 NA". |
| production[0].refining_by_country.shares[BO].share_pct | 0.44 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 66 and 73: Bolivia 70 / world 16,000 = 0.4375%, which rounds to 0.44%. |
| production[0].refining_by_country.shares[BG].quantity.value | 50 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 67: "Bulgaria 46 50 NA". |
| production[0].refining_by_country.shares[BG].share_pct | 0.31 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 67 and 73: Bulgaria 50 / world 16,000 = 0.3125%, which rounds to 0.31%. |
| production[0].refining_by_country.shares[CN].quantity.value | 13000 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 68: "China 13,300 13,000 NA". |
| production[0].refining_by_country.shares[CN].share_pct | 81.25 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 68 and 73: China 13,000 / world 16,000 = 81.25%. |
| production[0].refining_by_country.shares[JP].quantity.value | 500 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 69: "Japan 500 500 NA". |
| production[0].refining_by_country.shares[JP].share_pct | 3.12 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 69 and 73: Japan 500 / world 16,000 = 3.125%, which rounds to 3.12%. |
| production[0].refining_by_country.shares[KZ].quantity.value | 180 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 70: "Kazakhstan 180 180 NA". |
| production[0].refining_by_country.shares[KZ].share_pct | 1.12 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 70 and 73: Kazakhstan 180 / world 16,000 = 1.125%, which rounds to 1.12%. |
| production[0].refining_by_country.shares[KR].quantity.value | 1000 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 71: "Korea, Republic of 1,000 1,000 NA". |
| production[0].refining_by_country.shares[KR].share_pct | 6.25 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 71 and 73: Republic of Korea 1,000 / world 16,000 = 6.25%. |
| production[0].refining_by_country.shares[LA].quantity.value | 1100 tonnes_per_year metal | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 72 gives Laos 2024e refinery production as 1,100 tons. |
| production[0].refining_by_country.shares[LA].share_pct | 6.88 pct | usgs_mcs_2025_bismuth | verified | Derived from USGS MCS 2025 p.2 lines 72 and 73: Laos 1,100 / world 16,000 = 6.875%, which rounds to 6.88%. |
| end_uses.uses[0].share_pct | 30 pct | usgs_myb_2022_bismuth | verified | USGS MYB 2022 p.2, lines 80-81: "Bismuth metal also was used as a major constituent of various alloys accounting for 30% of reported consumption". |
| end_uses.uses[0].notes "in 2022" | 2022 year | usgs_myb_2022_bismuth | verified | USGS MYB 2022 p.2, lines 69-70 and 80-81 place the 30% alloy share in 2022 reported consumption. |
| feedstock_origins[lead_ores].notes "most often as a byproduct during the processing of lead ores" | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 76-77: bismuth "is produced most often as a byproduct during the processing of lead ores." |
| feedstock_origins[lead_ores].notes "last domestic primary lead smelter closed at yearend 2013" | 2013 year | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, lines 4-5: "the last domestic primary lead smelter closed at yearend 2013". |
| feedstock_origins[tungsten_ores] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 77-78: "In China and Vietnam, bismuth is also produced as a byproduct or coproduct of tungsten and other metal ore processing." |
| feedstock_origins[zinc_ores] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 78-79: "In Japan and the Republic of Korea, bismuth is produced as a byproduct or coproduct of zinc ore processing." |
| feedstock_origins[other_metal_ores] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 77-78 explicitly includes "tungsten and other metal ore processing" for China and Vietnam. |
| substitutes[pharmaceuticals] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 81-82: bismuth compounds can be replaced in pharmaceutical applications by alumina, antibiotics, calcium carbonate, and magnesia. |
| substitutes[pigments] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 82-82: "Titanium-dioxide-coated mica flakes and fish-scale extracts are substitutes in certain pigment uses." |
| substitutes[low_temperature_solders] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 83-83: "Cadmium, indium, lead, and tin can partially replace bismuth in low-temperature solders." |
| substitutes[machining_holding_devices] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 83-84: "Resins can replace bismuth alloys for holding metal shapes during machining". |
| substitutes[fire_sprinkler_triggers] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 84-85: "glycerin-filled glass bulbs can replace bismuth alloys in triggering devices for fire sprinklers." |
| substitutes[free_machining_alloys] | qualitative | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 85-86: "Free-machining alloys can contain lead, selenium, or tellurium as a replacement for bismuth." |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_2025 | verified | USGS "About the 2025 List of Critical Minerals" lines 637-639 list "Bismuth" under "Explore the 2025 List of Critical Minerals". |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex cached text for CELEX 32024R1252, Annex II Section 1, lists "(f) bismuth" under "Critical raw materials". |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex cached text for CELEX 32024R1252, Annex I Section 1, lists "(b) bismuth" under "Strategic raw materials". |
| prices[2020].value | 2.73 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, line 35: "Price, average,4 dollars per pound 2.73 3.74 3.90 4.08 5.30". |
| prices[2021].value | 3.74 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, line 35: "Price, average,4 dollars per pound 2.73 3.74 3.90 4.08 5.30". |
| prices[2022].value | 3.9 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, line 35: "Price, average,4 dollars per pound 2.73 3.74 3.90 4.08 5.30". |
| prices[2023].value | 4.08 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, line 35: "Price, average,4 dollars per pound 2.73 3.74 3.90 4.08 5.30". |
| prices[2024].value | 5.3 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.1, line 35: "Price, average,4 dollars per pound 2.73 3.74 3.90 4.08 5.30". |
| geopolitical_events[0].date | 2024 | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 53 begins: "In 2024, average monthly prices for bismuth..." |
| geopolitical_events[0].impact "from $3.89 per pound in January 2024" | 3.89 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 53-54: prices increased "from $3.89 per pound in January to $6.29 per pound in October." |
| geopolitical_events[0].impact "to $6.29 per pound in October" | 6.29 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 53-54: prices increased "from $3.89 per pound in January to $6.29 per pound in October." |
| geopolitical_events[0].impact "annual average to $5.30 per pound" | 5.30 usd_per_lb | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 54-55: "The estimated annual average price in 2024 was $5.30 per pound". |
| geopolitical_events[0].impact "30% above 2023" | 30 pct | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 54-55: "$5.30 per pound, a 30% increase from that in 2023". |
| geopolitical_events[0].impact "imports ... fell 40% year over year" | 40 pct | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 58-59: imports from China "decreased by 40%". |
| geopolitical_events[0].impact "to 580 metric tons in 2024" | 580 tonnes | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, lines 58-59: imports from China "decreased by 40% to 580 tons in 2024". |
| geopolitical_events[0].impact "from 964 metric tons in 2023" | 964 tonnes | usgs_mcs_2025_bismuth | verified | USGS MCS 2025 p.2, line 59: "from 964 tons in 2023." |

## Notes

- `elements/Bi.yaml` is not present in this worktree's `HEAD`. I verified against the reachable historical file at commit `68d91a2254195f75d15a8664ead03dcc2e92ef9c`, which contains the `Bi` element payload referenced by the task.
- The direct EUR-Lex source URL returned empty content in this environment, but search-indexed text for the same CELEX document (`32024R1252`) clearly exposed Annex I and Annex II, including bismuth in both lists.
- No sourced reserve quantity claims were present in the recovered `Bi.yaml`; the reserves section is descriptive only and carries no `source_id`-tagged numeric values.

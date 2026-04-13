# Verification: H

- Element: hydrogen (H)
- Snapshot year: 2025
- Verifier: agent worker-b6397a0fab76
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 12 |
| discrepancy | 3 |
| inferred | 5 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 100 million_tonnes_per_year | iea_ghr_2025_exec | verified | IEA executive summary: global hydrogen demand increased to "almost 100 million tonnes (Mt) in 2024"; YAML uses this as the production proxy. |
| production[0].refined notes "up 2% from 2023" | 2% | iea_ghr_2025_exec | verified | IEA executive summary says 2024 demand was "up 2% from 2023". |
| production[0].refined notes "less than 1% from low-emissions pathways" | less than 1% | iea_ghr_2025_exec | verified | IEA executive summary: low-emissions hydrogen "still accounts for less than 1% of global production." |
| production[0].refining_by_country.shares[CN].share_pct | 33% | iea_ghr_2025_five_questions | inferred | Five Questions says China accounts for "nearly one-third of global demand"; 33% is the YAML's rounded proxy share, not a stated percentage in the source. |
| production[0].refining_by_country.shares[CN].quantity.value | 33 million_tonnes_per_year | iea_ghr_2025_five_questions | inferred | Derived from the YAML's global proxy of ~100 Mt multiplied by China's "nearly one-third" demand share; the source does not state 33 Mt directly. |
| production[0].refining_by_country.shares[CN].quantity notes "nearly one-third" | nearly one-third | iea_ghr_2025_five_questions | verified | Five Questions: China is "the world's largest hydrogen market, accounting for nearly one-third of global demand." |
| production[0].refining_by_country.shares[CN].notes "about 90% of global coal consumption for hydrogen production" | about 90% | iea_ghr_2025_five_questions | discrepancy | The cited Five Questions page supports the one-third demand claim, but this 90% coal-consumption figure appears on the IEA tracking page, not on the cited URL. |
| production[0].refining_by_country.shares[ZZ].share_pct | 67% | iea_ghr_2025_five_questions | inferred | Residual share after assigning China ~33%; not stated in the source. |
| production[0].refining_by_country.shares[ZZ].quantity.value | 67 million_tonnes_per_year | iea_ghr_2025_five_questions | inferred | Residual quantity from the YAML's ~100 Mt total after assigning China ~33 Mt; not stated in the source. |
| feedstock_origins[natural_gas].notes | 290 bcm natural gas | iea_ghr_2025_exec | verified | IEA executive summary says hydrogen supply in 2024 was dominated by fossil fuels, "using 290 billion cubic metres (bcm) of natural gas". |
| feedstock_origins[natural_gas].notes | around two-thirds of dedicated hydrogen production in 2023 | iea_ghr_2025_exec | discrepancy | This two-thirds claim is not on the cited executive-summary page; it appears on the IEA hydrogen tracking page instead. |
| feedstock_origins[coal].notes | around 20% of dedicated hydrogen production in 2023 | iea_hydrogen_tracking_2025 | verified | IEA tracking: "In 2023, around two-thirds of the dedicated hydrogen production was met with natural gas and around 20% with coal". |
| feedstock_origins[coal].notes | about 90% of global coal consumption for hydrogen production | iea_hydrogen_tracking_2025 | verified | IEA tracking continues that coal is "mostly used in China, which alone accounted for 90% of global coal consumption for hydrogen production". |
| feedstock_origins[refinery_and_petrochemical_process_streams].notes | around one-sixth of global hydrogen supply | iea_hydrogen_tracking_2025 | verified | IEA tracking says "around a sixth of the global hydrogen supply" comes from by-product hydrogen, mainly in petrochemicals. |
| feedstock_origins[water].notes | less than 1% of global production in 2024 | iea_ghr_2025_prod | verified | Production Highlights: hydrogen production reached almost 100 Mt in 2024, but "less than 1%" was based on low-emissions technologies. |
| end_uses.uses[oil_refining].share_pct | 68% | eia_hydrogen_consumption_2024 | verified | EIA article: "petroleum refiners used 68% of all U.S. hydrogen production". |
| end_uses.uses[ammonia_and_fertilizers].share_pct | 21% | eia_hydrogen_consumption_2024 | verified | EIA article: "nitrogenous fertilizer (ammonia and derivatives) industries used 21%". |
| end_uses.uses[other_chemicals_metals_foods_and_new_uses].share_pct | 11% | eia_hydrogen_consumption_2024 | inferred | Residual from the cited EIA split: 100 - 68 - 21 = 11. EIA does not state the 11% figure explicitly. |
| end_uses.uses[other_chemicals_metals_foods_and_new_uses].notes "all new applications still below 1% of demand in 2024" | less than 1% | eia_hydrogen_consumption_2024 | discrepancy | The cited EIA page does not discuss global new applications being below 1% in 2024; that number comes from IEA demand reporting, so the YAML source attribution is wrong here. |
| geopolitical_events[0].date | 2025-01-03 | treasury_45v_final_2025 | verified | Treasury press release is dated "January 3, 2025". |
| geopolitical_events[1].date | 2025-04-11 | imo_net_zero_framework_2025 | verified | IMO press briefing is dated "11 April 2025". |

## Notes

- `elements/H.yaml` contains no reserves, prices, or sourced criticality-flag numerics to verify in this pass.
- The structured hydrogen totals and feedstock shares are broadly supportable, but three note-level numbers are mis-attributed to the wrong cited page: the China 90% coal-consumption note under `iea_ghr_2025_five_questions`, the natural-gas "two-thirds" note under `iea_ghr_2025_exec`, and the "<1% new applications" note under `eia_hydrogen_consumption_2024`.
- Country production geography is explicitly proxy-based rather than directly published by IEA. China’s 33% and 33 Mt, and the residual 67% and 67 Mt for the rest of world, are arithmetic inferences from "nearly one-third" and the YAML’s ~100 Mt global production proxy.

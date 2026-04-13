# Verification: N

- Element: nitrogen (N)
- Snapshot year: 2025
- Verifier: worker-97f7c2a968ce (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 5 |
| discrepancy | 0 |
| inferred | 1 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 298.71 million_tonnes_per_year | mordor_liquid_nitrogen_2026 | verified | `"The Liquid Nitrogen Market size in 2026 is estimated at 309.79 Million tons, growing from 2025 value of 298.71 Million tons"` — Mordor Intelligence, Liquid Nitrogen Market Analysis |
| production[0].refined.notes (2026 market size) | 309.79 million_tonnes_per_year | mordor_liquid_nitrogen_2026 | verified | `"Market Volume (2026)309.79 Million tons"` and `"The Liquid Nitrogen Market size in 2026 is estimated at 309.79 Million tons"` — Mordor Intelligence market overview and analysis |
| production[0].refining_by_country.shares[0].share_pct | 100 | mordor_liquid_nitrogen_2026 | inferred | Mordor reports `"Largest Market Asia Pacific"` and `"By geography, Asia-Pacific led with 46.10% revenue share in 2025"` but does not publish a country-by-country world production table; the YAML's `ZZ = 100%` is a placeholder for unavailable national shares rather than a stated source figure. |
| feedstock_origins[0].typical_concentration_pct | 78.09 | grand_view_nitrogen_gas_2024 | verified | `"Nitrogen (N2) is a colorless, odorless, and tasteless gas that constitutes 78.09% (by volume) of our air."` — Grand View Research, Nitrogen Gas Market Summary |
| end_uses.uses[0].share_pct | 49.8 | grand_view_nitrogen_gas_2024 | verified | `"By application, the food and beverage segment held a revenue share of 49.8% in 2023."` — Grand View Research, Key Market Trends & Insights |
| substitutes[0].notes (-196 degrees Celsius limit) | -196 degrees_Celsius | mordor_liquid_nitrogen_2026 | verified | `"Although mechanical units cannot reach -196 °C, they satisfy many frozen food specifications"` — Mordor Intelligence, High-Efficiency Mechanical Freezers Eroding LN2 Demand |

## Notes

Nitrogen has no mined production, reserve, price, or geopolitical-event numeric claims with `source_id` in the current YAML, so the verification scope for `N.yaml` is limited to merchant liquid-nitrogen tonnage, the synthetic country-share bucket, feedstock concentration, end-use share, and the cryogenic substitute-temperature claim.

The `production[0].refining_by_country.shares[0].share_pct = 100` entry is not directly supported by the source. It is a modeling choice used because the cited source only reports regional leadership, not a country table, so it is marked `inferred` rather than `verified`.

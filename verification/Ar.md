# Verification: Ar

- Element: argon (Ar)
- Snapshot year: 2025
- Verifier: agent worker-ac282e206ebf
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 11 |
| discrepancy | 0 |
| inferred | 6 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 5000 million_m3_per_year | indexbox_china_argon_2026 | inferred | China page L92: "1.1 billion cubic meters, representing 22% of global output." 1.1 / 0.22 = 5.0 billion m3, so the YAML world total is derived rather than stated directly. |
| production[0].refining_by_country.shares[CN].share_pct | 22.0 | indexbox_china_argon_2026 | verified | China page L92: "1.1 billion cubic meters, representing 22% of global output." |
| production[0].refining_by_country.shares[CN].quantity.value | 1100 million_m3_per_year | indexbox_china_argon_2026 | verified | China page L92: "The production volume of 1.1 billion cubic meters" matches 1,100 million m3. |
| production[0].refining_by_country.shares[IN].share_pct | 8.0 | indexbox_india_argon_2026 | inferred | India page L115/L124 gives production at 398 million m3 but no explicit global-output share. Using the YAML/global implied 5,000 million m3 total gives 398 / 5,000 = 7.96%, rounded to 8.0%. |
| production[0].refining_by_country.shares[IN].quantity.value | 398 million_m3_per_year | indexbox_india_argon_2026 | verified | India page L115: "production at 398 million cubic meters"; L124 repeats "domestic output of 398 million cubic meters". |
| production[0].refining_by_country.shares[US].share_pct | 7.9 | indexbox_us_argon_2026 | verified | U.S. page L122: "The production share of 7.9% of the global total confirms the U.S. role as a major producer." |
| production[0].refining_by_country.shares[US].quantity.value | 396 million_m3_per_year | indexbox_us_argon_2026 | verified | U.S. page L122: "Domestic production, at 396 million cubic meters"; L136 repeats "reported production volume of 396 million cubic meters". |
| production[0].refining_by_country.shares[ZZ].share_pct | 62.1 | indexbox_china_argon_2026 | inferred | Residual from cited shares: 100.0 - 22.0 - 8.0 - 7.9 = 62.1%. No source states a rest-of-world percentage. |
| production[0].refining_by_country.shares[ZZ].quantity.value | 3106 million_m3_per_year | indexbox_china_argon_2026 | inferred | Residual from YAML totals: 5,000 - 1,100 - 398 - 396 = 3,106 million m3. No source states a rest-of-world production volume. |
| feedstock_origins[0].typical_concentration_pct | 0.934 | noaa_atmosphere | verified | NOAA JetStream table: "Argon | Ar | 0.934%" in the dry atmosphere. |
| end_uses.uses[0].share_pct | 33.8 | imarc_argon_market_2025 | verified | IMARC L179: "Metal manufacturing and fabrication leads the market with around 33.8% of market share in 2025." |
| prices[0].value | 0.684 usd_per_m3 | indexbox_china_argon_2026 | inferred | China page L150: export price "reached the peak level of $684 per thousand cubic meters" in 2021. YAML converts this to $0.684 per m3 by dividing by 1,000. |
| prices[1].value | 0.483 usd_per_m3 | indexbox_china_argon_2026 | inferred | China page L150: "In 2024, the average argon export price amounted to $483 per thousand cubic meters." YAML converts this to $0.483 per m3 by dividing by 1,000. |
| geopolitical_events[0].date | 2025-06 | air_liquide_vsmc_2025 | verified | Air Liquide VSMC release header L162: "Paris, France, June 02, 2025." YAML records the month as 2025-06. |
| geopolitical_events[1].date | 2025-07 | air_liquide_dresden_2025 | verified | Air Liquide Dresden release header L164: "Paris, France, July 24, 2025." YAML records the month as 2025-07. |
| geopolitical_events[1].event "more than EUR250 million" | more than EUR250 million | air_liquide_dresden_2025 | verified | Dresden release L171: "This planned investment of over 250 million euros" matches the YAML event text. |
| geopolitical_events[1].event "three new ASUs" | 3 ASUs | air_liquide_dresden_2025 | verified | Dresden release L172: "Air Liquide will build, own and operate three Air Separation Units (ASUs)". |

## Notes

Ar.yaml has no `reserves` block and no criticality flags carrying `source_id`, so there were no sourced numeric reserve or criticality claims to verify for this element.

The substitution and feedstock notes are source-backed qualitatively, but only `feedstock_origins[0].typical_concentration_pct` is a numeric claim. The Grand View source supports argon as an alternative to nitrogen and notes substitutes in general, but it does not surface a numeric substitution metric.

The IMARC source verifies the 33.8% end-use share, but the fetched page states that share for 2025, while the YAML note text says "in 2024." The numeric share itself matches; the year in the prose note appears one year early.

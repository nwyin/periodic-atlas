# Verification: Cs

- Element: cesium (Cs)
- Snapshot year: 2025
- Verifier: agent worker-c0932c4c116a
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 16 |
| discrepancy | 0 |
| inferred | 5 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 550 tonnes_per_year | usgs_mcs_2026_cesium | inferred | MCS 2026 says "11,000 tons of cesium formate were in use, with 5% being depleted and replaced per year" (p.2). 11,000 × 5% = 550. |
| production[0].refined.notes ("11,000 tons in use") | 11000 tonnes | usgs_mcs_2026_cesium | verified | "11,000 tons of cesium formate were in use" (p.2, World Mine Production and Reserves). |
| production[0].refined.notes ("5% depleted and replaced per year") | 5 pct | usgs_mcs_2026_cesium | verified | "5% being depleted and replaced per year" (p.2, World Mine Production and Reserves). |
| reserves.economic_reserves.value | 70000000 kg | usgs_cesium_profile_2004 | verified | Table 1 lists "World total 70,000,000" in the Reserves column (p.4). |
| reserves.economic_reserves.notes ("more than two-thirds at Bernic Lake") | >66.7 pct | usgs_cesium_profile_2004 | verified | USGS says the Bernic Lake deposit "accounts for more than two-thirds of world reserves" (p.1) and again "more than two-thirds of the world's reserve base is at Bernic Lake" (p.5). |
| reserves.resources.value | 110000000 kg | usgs_cesium_profile_2004 | verified | Table 1 lists "World total 110,000,000" in the Reserve base column (p.4). |
| reserves.resources.notes (Canada reserve base) | 73000000 kg | usgs_cesium_profile_2004 | verified | Table 1: "Canada 70,000,000 73,000,000" (Reserves / Reserve base, p.4). |
| reserves.resources.notes (Zimbabwe reserve base) | 23000000 kg | usgs_cesium_profile_2004 | verified | Table 1: "Zimbabwe -- 23,000,000" (Reserve base, p.4). |
| reserves.resources.notes (Namibia reserve base) | 9000000 kg | usgs_cesium_profile_2004 | verified | Table 1: "Namibia -- 9,000,000" (Reserve base, p.4). |
| reserves.reserves_by_country.shares[0].share_pct | 100 pct | usgs_cesium_profile_2004 | inferred | Table 1 gives Canada 70,000,000 reserves and world total 70,000,000 reserves (p.4), so the YAML's 100% share is a direct derivation. |
| reserves.reserves_by_country.shares[0].quantity.value | 70000000 kg | usgs_cesium_profile_2004 | verified | Table 1 lists "Canada 70,000,000" in the Reserves column (p.4). |
| prices[0] | 2024 / 98 usd_per_gram / 1 g / 99.8% metal | usgs_mcs_2026_cesium | verified | "In 2025, one company offered 1-gram ampoules of 99.8% ... cesium for $104.00, a 6% increase from $98.00 in 2024" (p.1). |
| prices[1] | 2025 / 104 usd_per_gram / 1 g / 99.8% metal | usgs_mcs_2026_cesium | verified | "In 2025, one company offered 1-gram ampoules of 99.8% ... cesium for $104.00" (p.1). |
| prices[2].value | 2.096 usd_per_gram | usgs_mcs_2026_cesium | inferred | MCS 2026 gives "$52.40" for "25 grams of 98% ... cesium formate" in 2024 (p.1). 52.40 / 25 = 2.096. |
| prices[2].notes | 2024 / 52.40 USD per 25 g / 98% | usgs_mcs_2026_cesium | verified | "The price for 25 grams of 98% ... cesium formate was $56.10, a 7% increase from $52.40 in 2024" (p.1). |
| prices[3].value | 2.244 usd_per_gram | usgs_mcs_2026_cesium | inferred | MCS 2026 gives "$56.10" for "25 grams of 98% ... cesium formate" in 2025 (p.1). 56.10 / 25 = 2.244. |
| prices[3].notes | 2025 / 56.10 USD per 25 g / 98% | usgs_mcs_2026_cesium | verified | "The price for 25 grams of 98% ... cesium formate was $56.10" (p.1). |
| geopolitical_events[0].date | 2020 | usgs_mcs_2026_cesium | verified | "One company developed a recycling program for X-ray panels in 2020" (p.2, Events, Trends, and Issues). |
| geopolitical_events[1].date | 2025 | usgs_mcs_2026_cesium | verified | "During 2025, one company in Canada reported intermittent cesium production..." (p.2, Events, Trends, and Issues). |
| geopolitical_events[2].date | 2025 | usgs_mcs_2026_cesium | inferred | The cited source verifies the 2027 target year but does not explicitly date the policy continuation as 2025; the YAML's event date is inferred from the 2025 MCS snapshot context. |
| geopolitical_events[2].impact | 2027 target year | usgs_mcs_2026_cesium | verified | "Congress set a goal ... to eliminate cesium-137 blood irradiators by 2027" (p.1). |

## Notes

`elements/Cs.yaml` was absent from this worktree, so verification used the exact file content from git commit `2bb03acdc4945425b967f9d274a9a7e68005a1d4` (`Add cesium element record`) via `git show`, without modifying element data.

The cleanest recent production-like quantity in the cited 2026 MCS chapter is not a mine or refinery tonnage but the implied annual replacement of cesium formate drilling brine. The YAML's `550 tonnes_per_year` is therefore correctly treated as a derived figure rather than a directly published production statistic.

The reserves section mixes modern and legacy USGS terminology. The 2004 profile's "reserve base" total of 110 million kilograms is what the YAML maps into `resources`; that mapping is editorial, but the underlying table values for 70 million reserves and 110 million reserve base are directly confirmed.

No sourced numeric claims were present under `feedstock_origins`, `substitutes`, `end_uses`, or `criticality`, so those sections do not add rows to the Claims table in this pass.

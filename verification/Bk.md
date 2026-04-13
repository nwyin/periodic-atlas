# Verification: Bk

- Element: berkelium (Bk)
- Snapshot year: 2025
- Verifier: agent worker-bc80bbc748b5
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 6 |
| discrepancy | 0 |
| inferred | 2 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].producers.shares[0].share_pct | 100 % | ornl_element_117_timeline | inferred | ORNL says it is the "only place in the world" that can produce enough berkelium; that supports, but does not explicitly tabulate, a 100% US share. |
| end_uses.uses[0].share_pct | 100 % | nidc_bk249_available_2020 | inferred | NIDC says Bk-249 is "of particular interest" in heavy-element chemistry and nuclear physics research. The source supports the use category, but not an explicit 100% allocation. |
| geopolitical_events[0].date | 2008 | ornl_superheavy_science_2021 | verified | ORNL caption: "led the 2008 revival" of the Cf-252 program. |
| geopolitical_events[1].date | 2020-10-27 | nidc_bk249_available_2020 | verified | The NIDC notice is dated "October 27, 2020." |
| geopolitical_events[1].impact (currently available quantity) | about 0.3 mg | nidc_bk249_available_2020 | verified | NIDC: "small quantity (~ 0.3 mg)" is currently available. |
| geopolitical_events[1].impact (next batch quantity) | less than 16 mg | nidc_bk249_available_2020 | verified | NIDC: "additional batch ... (< 16 mg)." |
| geopolitical_events[1].impact (next batch timing) | May 2021 | nidc_bk249_available_2020 | verified | NIDC says the additional batch would be ready "in May 2021." |
| geopolitical_events[2].date | 2023-04-12 | nidc_getting_purer_2023 | verified | The NIDC highlight is dated "April 12, 2023." |

## Notes

`elements/Bk.yaml` is absent from the current worktree `HEAD`, so this verification used the exact historical record from commit `8b43df5` (`git show 8b43df5:elements/Bk.yaml`) as the target dataset.

The only source-linked numeric claims in that record are two percentage allocations and six date/quantity claims under `geopolitical_events`. The `feedstock_origins` and `substitutes` entries do carry `source_id` values, but they do not make distinct numeric claims, so they do not add rows to the claims table.

Both 100% share claims are best marked `inferred`, not `verified`. The cited sources establish that ORNL is uniquely capable of supplying berkelium for this pathway and that Bk-249 is used for heavy-element chemistry and nuclear physics research, but they do not publish an explicit market-share or end-use percentage table.

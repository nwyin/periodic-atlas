# Verification: Ra

- Element: radium (Ra)
- Snapshot year: 2025
- Verifier: worker-d1f734e4f9d8 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 3 |
| discrepancy | 0 |
| inferred | 3 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].producers.shares[0].share_pct | 100% | nidc_ra223_availability_2017 | inferred | NIDC's June 1, 2017 notice says DOE distributes Ra-223 from ORNL and PNNL and that the national-lab "cows currently have the capability of producing hundreds of mCi of Ra-223 ... per month" and provide distribution "across the Nation on a regular basis." The source supports a documented U.S. DOE supply chain, but not a quantified full-global market-share table, so `100%` is an inference from the atlas modeling choice. |
| isotope_markets[1].producers.shares[0].share_pct | 100% | nidc_ra224_generator_2015 | inferred | NIDC's March 13, 2015 announcement says DOE "initiated the establishment of a production capability at the Oak Ridge National Laboratory" and that the generator "is now routinely available for ordering" through the NIDC catalog. That confirms a domestic DOE supply route, but not a published global market-share census, so `100%` is inferred rather than directly stated. |
| end_uses.uses[0].share_pct | 100% | nidc_radium_catalog_2025 | inferred | The 2025 NIDC radium catalog page lists only three radium offerings: `Radium-223`, `Radium-224`, and `Radium-224/Lead-212 Generator`, each sold in `Millicuries`. This supports the conclusion that cataloged radium commerce is entirely medical/research oriented, but it does not explicitly publish an end-use share table, so `100%` is inferred. |
| geopolitical_events[0].date | 2015-03 | nidc_ra224_generator_2015 | verified | The NIDC announcement is dated `March 13, 2015` and describes DOE establishing Ra-224/Pb-212 generator availability after a prior private effort ended. |
| geopolitical_events[1].date | 2021-09 | nidc_th228_routine_2021 | verified | The NIDC page `Thorium-228 in Routine Production` is dated `September 9, 2021`. |
| geopolitical_events[2].date | 2022-06 | nidc_ra226_available_2022 | verified | The NIDC page `Radium-226 is Available Now!` is dated `June 13, 2022`. |

## Notes

`elements/Ra.yaml` is not present in this worktree at `HEAD`; verification was performed against the authored file at commit `c6dfd849f3cc96c5f8bf7dc07de1cce63d9933fe` via `git show`.

The current Ra profile contains no sourced production tonnage, reserves, prices, or criticality-list claims. The only numeric claims that actually carry a `source_id` in the YAML are the two isotope-producer `share_pct` entries, the single end-use `share_pct`, and the three geopolitical-event dates, so those are the rows included here.

Several other numeric facts appear in `Ra.yaml` without an attached `source_id`, including half-lives, `16 mCi` monthly generator availability, `1 M HCl`, and `one inch` packaging details. They were intentionally excluded from the Claims table because this verification pass is limited to claims that explicitly carry a `source_id`.

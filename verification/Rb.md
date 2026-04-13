# Verification: Rb

- Element: rubidium (Rb)
- Snapshot year: 2025
- Verifier: worker-0f86b5a4aa0b (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 14 |
| discrepancy | 0 |
| inferred | 4 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| reserves.economic_reserves.value | 200000 tonnes | usgs_mcs_2025_rubidium | inferred | USGS gives an upper bound, not a point estimate: `"less than 200,000 tons of recoverable rubidium materials"` (MCS 2025 Rubidium, p.149). |
| feedstock_origins[substrate=pollucite_ore].notes | 1.5% rubidium oxide | usgs_mcs_2025_rubidium | verified | `"3.5% and 1.5% rubidium oxide, respectively"` for lepidolite and pollucite (MCS 2025 Rubidium, p.149). |
| feedstock_origins[substrate=lepidolite_ore].notes | 3.5% rubidium oxide | usgs_mcs_2025_rubidium | verified | `"3.5% and 1.5% rubidium oxide, respectively"` for lepidolite and pollucite (MCS 2025 Rubidium, p.149). |
| end_uses.uses[0].share_pct | 100 | usgs_profile_2003_rubidium | inferred | The profile says the market is tiny and qualitative: `"principal application is in specialty glasses"` and the U.S. market is `"1 to 2 metric tons per year"`; it does not publish a percentage split, so YAML's 100% grouped bucket is a verifier inference (USGS Profile, p.3). |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2025 | verified | The final 2025 list `"includes the following 60 minerals"` and explicitly names `"rubidium"` (Federal Register notice published November 7, 2025). |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | verified | Annex II lists the EU critical raw materials from `"antimony"` through `"vanadium"` and includes `"platinum group metals"` but not rubidium (Regulation (EU) 2024/1252, Annex II, Section 1). |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | Annex I lists the EU strategic raw materials from `"bauxite/alumina/aluminium"` through `"tungsten"` and does not include rubidium (Regulation (EU) 2024/1252, Annex I, Section 1). |
| prices[year=2024][form=metal].value | 128 usd_per_gram | usgs_mcs_2025_rubidium | verified | `"1-gram ampoules ... rubidium for $128.00"` (MCS 2025 Rubidium, p.148). |
| prices[year=2024][form=metal].notes | 1 gram; 99.75% | usgs_mcs_2025_rubidium | verified | `"1-gram ampoules of 99.75% (metal basis)"` (MCS 2025 Rubidium, p.148). |
| prices[year=2023][form=metal].value | 121 usd_per_gram | usgs_mcs_2025_rubidium | verified | `"a 6% increase from $121.00 in 2023"` (MCS 2025 Rubidium, p.148). |
| prices[year=2024][form=compound_other].value | 30.2 usd_per_gram | usgs_mcs_2025_rubidium | inferred | USGS states `"10-gram ampoules ... was $302.00"`; YAML normalizes this to $30.2/g by division. |
| prices[year=2024][form=compound_other].notes | 10 grams; 99.8%; 302 USD | usgs_mcs_2025_rubidium | verified | `"10-gram ampoules of 99.8% ... was $302.00"` (MCS 2025 Rubidium, p.148). |
| prices[year=2023][form=compound_other].value | 29 usd_per_gram | usgs_mcs_2025_rubidium | inferred | USGS states `"from $290.00 in 2023"` for the same 10-gram formate-hydrate product; YAML converts this to $29.0/g. |
| prices[year=2023][form=compound_other].notes | 290 USD | usgs_mcs_2025_rubidium | verified | `"a 4% increase from $290.00 in 2023"` (MCS 2025 Rubidium, p.148). |
| prices[year=2024][form=carbonate].value | 1244.19 usd_per_kg | usgs_mcs_2025_rubidium | verified | `"rubidium carbonate was $1,244.19 per kilogram"` (MCS 2025 Rubidium, p.148). |
| geopolitical_events[0].date and impact | 2024; past two decades | usgs_mcs_2025_rubidium | verified | `"During 2024"` and ore production outside China `"ceased within the past two decades"` (MCS 2025 Rubidium, p.149). |
| geopolitical_events[1].date and impact | 2024; 5700 tonnes_per_year; 2026 | usgs_mcs_2025_rubidium | verified | `"Throughout 2024"` one Namibia project had `"5,700 tons per year"` lithium-hydroxide capacity `"expected to commence operations in 2026"` (MCS 2025 Rubidium, p.149). |
| geopolitical_events[2].date and impact | 2024-08; 3.6 million tonnes; 7900 tonnes; 2025 | usgs_mcs_2025_rubidium | verified | `"In August 2024"` Mount Edon had `"3.6 million tons"` containing `"7,900 tons of rubidium oxide"` with a proposal planned by `"yearend 2025"` (MCS 2025 Rubidium, p.149). |

## Notes

All sourced numeric claims in `elements/Rb.yaml` were checked against the cited primary documents. No discrepancies were found.

Four claims are better classified as `inferred` rather than `verified`:
`reserves.economic_reserves.value` is encoded from a published upper bound (`less than 200,000 tons`), `end_uses.uses[0].share_pct` is a YAML grouping choice because the source gives only qualitative use descriptions, and the two formate-hydrate price rows convert quoted 10-gram list prices into per-gram values.

`elements/Rb.yaml` does not attach `source_id` fields to the production narrative block, so there are no source-backed mine/refining tonnage rows to verify in this pass. The rubidium file's sourced numerics are concentrated in reserves, feedstock grades, prices, geopolitical events, and the criticality section's boolean flags.

`substitutes` carries a source citation but no distinct numeric claim. Its wording matches the USGS substitutes paragraph: rubidium and cesium are described as interchangeable in many applications, with cesium preferred in some uses.

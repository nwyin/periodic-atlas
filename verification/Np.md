# Verification: Np

- Element: neptunium (Np)
- Snapshot year: 2025
- Verifier: worker-8fd7b11ee4d2
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 9 |
| discrepancy | 1 |
| inferred | 1 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].half_life_seconds | 67659494400000 | nidc_np237_product_2024 | verified | Product sheet states `Half-Life/Daughter 2.144 x 10⁶ years`; using 365.25 days/year gives 67,659,494,400,000 seconds, matching YAML. |
| isotope_markets[0].delivery_form (unit of sale) | grams | nidc_np237_product_2024 | verified | Product sheet lists `Unit of Sale Grams`. |
| isotope_markets[1].half_life_seconds | 48283128000000 | nndc_ensdf_np236_2022 | discrepancy | NNDC dataset gives `236NP ... 1.55E+5 Y`; using 365.25 days/year gives about 4,891,428,000,000 seconds, not 48,283,128,000,000. |
| isotope_markets[1].delivery_form (quantity) | microgram quantities | nidc_neptunium_catalog_2025 | verified | NIDC catalog page for `Neptunium-236g` shows `Quantity` = `Micrograms`. |
| isotope_markets[1].delivery_form (enrichment offer) | 8%-enriched | doe_nidc_np236_launch_2025 | verified | Launch notice states `we have currently established an enrichment level of 8%`. |
| feedstock_origins[0].notes | Np-237 reactor product from transuranic processing | nidc_np237_product_2024 | verified | Product sheet says `Processing Transuranic processing` and `Production Route Reactor product`. |
| feedstock_origins[1].notes | Np-236 from depleted uranium targets | doe_nidc_np236_launch_2025 | verified | Launch notice says DOE produced `Np-236 by irradiating a depleted uranium target with protons`. |
| end_uses.uses[0].share_pct | 100 | doe_nidc_np236_launch_2025 | inferred | Source confirms only isotope-specific uses for `Np-236` and gives no market-share split; `100` is an analyst roll-up of the described neptunium isotope market, not a published percentage. |
| geopolitical_events[0].date | 2010 | doe_pu238_startup_plan_2010 | verified | DOE report cover and title page identify the report as `June 2010`. |
| geopolitical_events[0].impact (Russian deliveries) | 2009 | doe_pu238_startup_plan_2010 | verified | Report says `In September 2009, the Russian government informed DOE` it would not deliver the existing order under the current agreement. |
| geopolitical_events[1].date | 2025-05-21 | doe_nidc_np236_launch_2025 | verified | NIDC launch page for Np-236 is dated `May 21, 2025`. |

## Notes

The worktree used for verification did not contain a local `elements/Np.yaml`; verification was performed against the task's referenced neptunium YAML content as found in a sibling worktree copy with identical source IDs and claim text.

`end_uses.uses[0].share_pct = 100` is not stated in the DOE/NIDC sources. The sources support that the commercial neptunium market described here is entirely isotope-program activity, so the YAML percentage is reasonable but remains an inference.

`isotope_markets[1].half_life_seconds` appears incorrect by roughly a factor of 10. The cited NNDC source gives a half-life of `1.55E+5 Y` for `236Np`, which converts to about `4.89e12` seconds, whereas the YAML stores `4.83e13` seconds.

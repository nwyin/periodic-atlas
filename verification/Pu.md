# Verification: Pu

- Element: plutonium (Pu)
- Snapshot year: 2025
- Verifier: worker-2b9070a9b459 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 8 |
| discrepancy | 1 |
| inferred | 1 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| feedstock_origins[0].notes | neptunium-237 / plutonium-238 target route | doe_pu238_restart_automation_2019 | verified | DOE/ORNL press release: "production of neptunium oxide-aluminum pellets" and those pellets are used when "producing plutonium-238"; after pressing, they are irradiated and "chemically processed into Pu-238." |
| substitutes[0].notes | plutonium-238 is the only qualifying radioisotope | nasa_about_pu238_2025 | verified | NASA "About Plutonium-238": "The only radioisotope that has consistently met the basic criteria is plutonium-238." |
| end_uses.uses[0].share_pct | 100 | nasa_rps_overview_2025 | inferred | NASA's RPS overview says Pu-238 fuel is used in the two RPS forms now in service: "Radioisotope Thermoelectric Generators" and "Radioisotope Heater Units." The source supports exclusive RPS use, but it does not state an explicit "100%" share. |
| end_uses.uses[0].notes | plutonium-238 used in RTGs and RHUs | nasa_rps_overview_2025 | verified | NASA overview: "Two types of Radioisotope Power Systems are currently in use by NASA" and the GPHS fuel is "plutonium-238 (Pu-238)"; the two types listed are RTGs and RHUs. |
| geopolitical_events[0].date | 2012 | doe_pu238_restart_automation_2019 | verified | DOE/ORNL press release: "In 2012, NASA reached an agreement with the Department of Energy to restart production of Pu-238." |
| geopolitical_events[0].event | roughly 30-year U.S. gap | doe_pu238_restart_automation_2019 | discrepancy | The cited DOE/ORNL 2019 page confirms the 2012 restart agreement but does not state a "roughly 30-year" gap. That duration appears on a NASA page ("After a gap of nearly 30 years") but not in this cited source. |
| geopolitical_events[1].date | 2023-07-18 | doe_pu238_shipment_2023 | verified | DOE article header date: "July 18, 2023." |
| geopolitical_events[1].event | 0.5 kg shipment | doe_pu238_shipment_2023 | verified | DOE article: "The Department of Energy (DOE) recently shipped 0.5 kilograms of heat source plutonium oxide..." |
| geopolitical_events[1].impact | largest shipment in more than a decade | doe_pu238_shipment_2023 | verified | DOE article standfirst: "Delivery of 0.5 kilograms is the largest shipment of new heat source plutonium oxide in more than a decade." |
| geopolitical_events[1].impact | 1.5 kg/year by 2026 | doe_pu238_shipment_2023 | verified | DOE article: "DOE remains on track to meet its average production target of 1.5 kilograms per year of heat source plutonium oxide by 2026." |

## Notes

`elements/Pu.yaml` contains very few sourced numeric claims. There are no sourced production, reserves, price, or criticality quantities to verify in this file; the numeric claims with `source_id` are concentrated in feedstock/isotope wording, the single end-use share, and the two geopolitical-event entries.

One discrepancy was found: the 2012 restart event is correctly sourced for the year of the DOE/NASA agreement, but the cited DOE/ORNL 2019 page does not itself support the YAML's "roughly 30-year U.S. gap" wording. That duration is supported by NASA's "About Plutonium-238" page, not by `doe_pu238_restart_automation_2019`.

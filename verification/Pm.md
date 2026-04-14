# Verification: Pm

- Element: promethium (Pm)
- Snapshot year: 2025
- Verifier: agent worker-7eae0008a0af
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 8 |
| discrepancy | 0 |
| inferred | 5 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].half_life_seconds | 82680912 s | nidc_pm147_product_2025 | inferred | NIDC product sheet: "Half-Life/Daughter 2.62 years to Sm-147." YAML back-converts to 2.6197 years, which rounds to 2.62; the exact second value is therefore an inferred unit conversion, not directly printed in the source. |
| isotope_markets[0].delivery_form (radionuclide purity) | 99.99% | nidc_pm147_product_2025 | verified | NIDC product sheet: "Radionuclide Purity 99.99%". |
| isotope_markets[0].delivery_form (specific activity, chloride) | >=483 Ci/g for 147PmCl3 | nidc_pm147_product_2025 | verified | NIDC product sheet: "Available Specific Activity ≥483 Ci/g 147PmCl3". |
| isotope_markets[0].delivery_form (specific activity, elemental) | >=834.3 Ci/g for elemental 147Pm | nidc_pm147_product_2025 | verified | NIDC product sheet: "Available Specific Activity ... (≥834.3 Ci/g 147Pm)". |
| isotope_markets[0].producers.shares[0].share_pct | 100% US | doe_science_pm147_highlight_2025 | verified | DOE Office of Science highlight: "The Department of Energy Isotope Program is currently the only global producer of promethium-147." |
| feedstock_origins[0] | Pm-147 extracted from plutonium waste stream | nidc_pm147_entering_market_2022 | verified | NIDC market-entry notice: "the radioisotope is currently being extracted from a plutonium waste stream". |
| feedstock_origins[1] | Nd-146 target route | broderick_pm147_2019 | verified | ORNL/Applied Radiation and Isotopes abstract: "highly enriched 146Nd oxide irradiated at the High Flux Isotope Reactor (HFIR)" and ScienceDirect highlights: "Pm-147 can be produced via beta-decay of 147Nd produced via 146Nd[n,gamma]147Nd ...". |
| substitutes[0].availability | partial | broderick_pm147_2019 | inferred | ScienceDirect introduction lists alternative low-energy beta emitters: "3H ... 63Ni ... 147Pm ... 155Eu ... and 171Tm." The paper confirms alternatives exist, but it does not classify substitutability as "partial"; that is an inference from the application discussion. |
| end_uses.uses[0].share_pct | 100% beta_emitter_power_and_gauge_sources | doe_science_pm147_highlight_2025 | inferred | DOE highlight says promethium is used "in luminous paint, for lighting, and in nuclear batteries" and has "potential uses in radioactive imaging and cancer treatments." The cited sources frame demand around beta-emitter applications but do not explicitly quantify a 100% share, so the single-market split is inferred. |
| criticality.us_critical_list_as_of_2025 | false | us_federal_register_critical_minerals_2025 | inferred | Federal Register final 2025 list says it "includes the following 60 minerals" and then enumerates them; promethium is not among the listed minerals. The YAML `false` value is therefore an inference from omission, not an explicit statement. |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | inferred | CRMA Annex II, Section 1 lists the EU critical raw materials from "antimony" through "vanadium"; open-text search on the regulation returns no match for "promethium". The `false` flag is inferred from absence in the annex list. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | inferred | CRMA Annex I, Section 1 lists the EU strategic raw materials, including "rare earth elements for permanent magnets (Nd, Pr, Tb, Dy, Gd, Sm, and Ce)"; open-text search on the regulation returns no match for "promethium". The `false` flag is inferred from absence in the annex list. |
| geopolitical_events[0].date | 2022-06-23 | nidc_pm147_entering_market_2022 | verified | NIDC market-entry notice header: "June 23, 2022". |

## Notes

`elements/Pm.yaml` is absent from this worktree checkout. Verification used the exact committed element record recovered from `git show e21e18e:elements/Pm.yaml`, which is the commit that added promethium.

Promethium in this repo is an isotope-market record, not a mine/refinery/reserve record. There are no production tonnage, reserve tonnage, country reserve shares, or price fields in the YAML to verify.

The strongest primary-source evidence is the DOE/NIDC product sheet and the June 23, 2022 NIDC market-entry notice. Those directly support the product form, purity, specific activities, current waste-stream feedstock origin, and the event date.

The ORNL journal article strongly supports the Nd-146 irradiation route and the existence of alternative low-energy beta emitters, but it does not explicitly label those alternatives as only "partial" substitutes. That availability assessment is a reasonable inference from the paper's application framing rather than a verbatim source claim.

Both criticality negatives are omission-based checks. The EU regulation is directly accessible and searchable, so the absence of promethium in Annex I and Annex II is robust. The US claim is also omission-based: the Federal Register notice enumerates 60 minerals and promethium is not in that list. Because neither source literally says "promethium is not critical," the report marks those rows `inferred`.

The `end_uses.share_pct = 100` row is also an inference. The cited DOE source describes a use cluster centered on beta-emitter applications but does not publish any end-use allocation table.

# Verification: Ac

- Element: actinium (Ac)
- Snapshot year: 2025
- Verifier: worker-912881ed1e0c (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 7 |
| discrepancy | 0 |
| inferred | 6 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].producers.shares[US].share_pct | 100 | nidc_ac225_decay_product | inferred | DOE/NIDC product sheet: "Production Route Decay of thorium-229" and "Availability Routinely available (weekly)" (extracted text lines 7-8). A 100% US share is inferred from this DOE/NIDC-only supply context, not stated directly. |
| isotope_markets[1].producers.shares[US].share_pct | 100 | doe_ac225_dmf_2020 | inferred | DOE DMF announcement says accelerator-produced Ac-225 is made at "Los Alamos and Brookhaven" and purified at "Oak Ridge National Laboratory" (extracted text lines 80-81). A 100% US share is inferred from this US-only supply chain description. |
| feedstock_origins[0].notes (separation repeated monthly) | every month | nidc_ac225_info | verified | NIDC Actinium-225 info page says the Th-229 milking process "is repeated every month" (extracted text line 87). |
| feedstock_origins[0].notes (batch size) | millicurie-scale batches | nidc_ac225_info | verified | The same NIDC sentence says each batch yields "millicurie quantities of Ac-225" (extracted text line 87). |
| substitutes[0].notes (used after Lu-177 therapy progression) | Lu-177 | iaea_ac225_tecdoc_2024 | verified | IAEA TECDOC 2057 trial table includes patients who had "Progressed following Lu-177-SSA Therapy" (extracted text lines 669-676). |
| substitutes[0].notes (used in combination with Lu-177-labelled radioligands) | Lu-177 | iaea_ac225_tecdoc_2024 | verified | Another IAEA TECDOC 2057 trial entry lists "Ac-225-J591 Plus Lu-177-PSMA-I&T" (extracted text lines 568-570). |
| end_uses.uses[targeted_alpha_radiopharmaceuticals].share_pct | 100 | iaea_ac225_tecdoc_2024 | inferred | IAEA TECDOC 2057 scope is "225Ac radiopharmaceutical production" (extracted text lines 411-417) and its clinical-use section is "WORLDWIDE STATUS OF CLINICAL USE OF 225Ac" (lines 520-526). The YAML's 100% medical end-use share is inferred from that framing. |
| criticality.us_critical_list_as_of_2025 | false | us_federal_register_critical_minerals_2025 | inferred | The final US notice says the list includes "60 minerals" and then enumerates them (public-inspection PDF extracted text lines 21-31); actinium is absent, so `false` is an absence inference. |
| criticality.eu_crm_list_as_of_2024 | false | eu_crma_2024 | inferred | CRMA Annex II enumerates the EU critical raw materials (extracted text lines 2698-2730); actinium is absent, so `false` is inferred. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | inferred | CRMA Annex I states "The following raw materials shall be considered strategic" and lists them (extracted text lines 2650-2671); actinium is absent, so `false` is inferred. |
| geopolitical_events[0].date | 2020-02 | doe_ac225_dmf_2020 | verified | The DOE DMF announcement is dated "February 11, 2020" (extracted text line 79). |
| geopolitical_events[1].date | 2023-03-21 | doe_ac225_nrc_roundtable_2023 | verified | NIDC says the roundtable was held "On Tuesday, March 21, 2023" (extracted text line 76). |
| geopolitical_events[1].impact (Ac-227 impurity at release) | <=2% | doe_ac225_nrc_roundtable_2023 | verified | The same NIDC sentence says the route "co-produces Ac-227 that is ≤ 2% of total activity" (extracted text line 76). |

## Notes

`elements/Ac.yaml` is absent from the current `main` worktree. Verification was performed against the last committed actinium record recoverable from git commit `25a5378` (`Add actinium isotope-market record`) without editing element data.

Most numeric actinium claims in this record are isotope-market or regulatory-timeline values rather than bulk-material tonnage. The two 100% producer shares and the three criticality booleans are correctly marked `inferred` because the cited sources establish US-only production context or publish list contents, but do not state those claims verbatim as market-share or boolean fields.

The cited `us_federal_register_critical_minerals_2025` govinfo PDF did not open directly in the browser tool, but the same final notice text was retrievable through the Federal Register public-inspection PDF and govinfo search excerpt. No discrepancy was found in the underlying claim.

# Verification: Po

- Element: polonium (Po)
- Snapshot year: 2025
- Verifier: worker-89624b643d30 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 5 |
| discrepancy | 0 |
| inferred | 3 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].production_quantity.value | 100 grams_per_year | nrc_polonium_2024 | verified | NRC: "Only about 100 grams ... is believed to be produced worldwide each year." Lines 163-164. |
| isotope_markets[0].delivery_form (exempt calibration/check sources) | 0.1 microcurie | nrc_polonium_2024 | verified | NRC: "Small polonium-210 sources ... 0.1 microcurie of radioactivity." Line 178. |
| isotope_markets[1].delivery_form | 5 M nitric acid solution | nidc_po209_product_2024 | verified | NIDC PDF: "Chemical Form 5 M nitric acid solution." |
| isotope_markets[1].delivery_form (activity concentration) | ~185 kBq (~5 microcuries/mL) | nidc_po209_product_2024 | verified | NIDC PDF: "Activity Concentration ~185 kBq (~5 uCi/mL)." |
| end_uses.uses[0].share_pct | 90 | nrc_polonium_2024 | inferred | NRC says Po-210 has "limited uses, mainly in static eliminators." Line 163; YAML's 90% is an inferred dominant-share estimate. |
| end_uses.uses[1].share_pct | 5 | nrc_polonium_2024 | inferred | NRC: "Small polonium-210 sources can also be used to check or calibrate instruments." Line 178; YAML's 5% is a residual estimate. |
| end_uses.uses[2].share_pct | 5 | nidc_po209_product_2024 | inferred | NIDC PDF lists Po-209 as "Availability Stock" and "Unit of Sale Microcuries"; YAML's 5% research share is inferred from this niche product listing. |
| geopolitical_events[0].date | 1999 | osti_static_eliminators_1999 | verified | OSTI record header: "Journal Article · 01 January 1999." Line 16. |

## Notes

`elements/Po.yaml` is an isotope-market record, not a mine/refinery record. The current file has no sourced numeric claims for production by country, reserves, prices, substitutes, or criticality booleans, so there was nothing numeric to verify in those sections.

The two end-use percentages sourced to the NRC page and the 5% research share sourced to the NIDC product sheet are not directly stated by either source. They are correctly marked `inferred` because the sources only establish relative importance: NRC says the isotope is used mainly in static eliminators and also in small calibration/check sources, while NIDC shows a much smaller research-lab Po-209 stock product.

The NEA source is cited for the Bi-209 to Bi-210 to Po-210 production route, but that citation supports qualitative feedstock/origin claims rather than a numeric value in the current YAML, so it does not appear in the claims table.

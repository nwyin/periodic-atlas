# Verification: Am

- Element: americium (Am)
- Snapshot year: 2025
- Verifier: worker-fae4d6a38bc1 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 13 |
| discrepancy | 2 |
| inferred | 11 |
| source_unreachable | 2 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].isotope | Am-241 | doe_nidc_am241_product | verified | NIDC product sheet header: "Americium-241 / Half-Life/Daughter 432.6 years to neptunium-237" |
| isotope_markets[0].half_life_seconds | 13650595560 (comment: "432.6 years * 365.25 * 86400") | doe_nidc_am241_product | discrepancy | NNDC NuDat 3.0: Am-241 t½ = 432.6 ± 0.6 y (verified); NIDC PDF: "432.6 years". But 432.6 × 365.25 × 86400 = 13,651,817,760 s, not 13,650,595,560 s. The stored value corresponds to ~432.56 y × 365.25 d/y — inline comment arithmetic is off by −1,222,200 s (≈14 days). Physics half-life value (432.6 y) is correct; only the unit conversion embedded in the YAML has an error. |
| isotope_markets[0].production_mode | stockpile_separated | doe_nidc_am241_landing | verified | NIDC landing page: "LANL is home to substantial quantities of materials from decades of defense program work. The Am-241 in these materials is now being recovered." |
| isotope_markets[0].precursor: Production Route | Decay of plutonium-241 | doe_nidc_am241_product | verified | NIDC PDF: "Production Route: Decay of plutonium-241" — verbatim match |
| isotope_markets[0].precursor: Pu-241 half-life | 14.4 years | doe_nidc_am241_product | discrepancy | NNDC NuDat 3.0: Pu-241 t½ = 14.290 ± 0.006 y. YAML states 14.4 y — overstated by 0.11 y (~40 days). Likely an older rounded figure; DOE NIDC product sheet does not state the Pu-241 half-life, so this is not citable to the given source_id. |
| isotope_markets[0].precursor: separation method | Solvent extraction or ion exchange chromatography | doe_nidc_am241_product | verified | NIDC PDF: "Processing: Solvent extraction and/or Ion exchange chromatography" — verbatim match |
| isotope_markets[0].delivery_form: chemical form | Oxide powder | doe_nidc_am241_product | verified | NIDC PDF: "Chemical Form: Oxide powder" |
| isotope_markets[0].delivery_form: chemical purity | >95% 241AmO2 by weight | doe_nidc_am241_product | verified | NIDC PDF: "Chemical Purity: > 95% 241AmO2 by weight" — verbatim match |
| isotope_markets[0].delivery_form: radioisotopic purity | >99% Am-241 of all americium | doe_nidc_am241_product | verified | NIDC PDF: "Radioisotopic Purity: >99% americium-241 of all americium by weight" — verbatim match |
| isotope_markets[0].delivery_form: Pu content | <1% by weight | doe_nidc_am241_product | verified | NIDC PDF: "Pu Content: < 1% by weight" — verbatim match |
| isotope_markets[0].delivery_form: primary container | Stainless steel screw-top container | doe_nidc_am241_product | verified | NIDC PDF: "Primary Container: Stainless steel screw top container" |
| isotope_markets[0].delivery_form: regulatory classification | DOE/NRC Form 741 | doe_nidc_am241_product | verified | NIDC PDF: "Classed as a nuclear material requiring documentation of transfer (DOE/NRC Form 741)" — verbatim match |
| isotope_markets[0].delivery_form: unit of sale | Grams | doe_nidc_am241_product | verified | NIDC PDF: "Unit of Sale: Grams" |
| isotope_markets[0].producers.shares[US].share_pct | 50 (confidence: low) | doe_nidc_am241_product | source_unreachable | DOE NIDC product information does not publish production volumes or market shares. YAML notes explicitly acknowledge 50% as a placeholder: "Exact share vs other producers is not published." No quantitative primary source exists for this figure. |
| isotope_markets[0].producers.shares[ZZ].share_pct | 50 (confidence: low) | doe_nidc_am241_product | source_unreachable | Same: NIDC does not disclose non-US supplier breakdown. Russia (Mayak PA) and UK (Sellafield) are named in the YAML notes as non-US sources; shares are unpublished. Residual 50% is a placeholder, not a sourced figure. |
| feedstock_origins: LANL legacy plutonium quote | "LANL is home to substantial quantities of materials from decades of defense program work. The Am-241 in these materials is now being recovered as an example of recycling rare and important isotopes" | doe_nidc_am241_landing | verified | NIDC landing page: "LANL is home to substantial quantities of materials from decades of defense program work. The Am-241 in these materials is now being recovered as an example of recycling rare and important isotopes that benefit U.S. citizens" — verbatim match (YAML omits the trailing clause) |
| narrative: LANL production restart year | 2012 | doe_nidc_am241_landing | verified | NIDC landing page: "in 2012 funded a team of researchers at Los Alamos National Laboratory (LANL)" — year confirmed |
| end_uses.uses[smoke_detectors_ionization].share_pct | 90 | inquiry_periodic_elements_2025 | inferred | NIDC landing confirms smoke detectors as primary commercial application ("used commercially in smoke detectors and moisture gauges") but provides no percentage breakdown. The 90% figure derives from an internal project document (inquiry_periodic_elements_2025), not a primary quantitative source. |
| end_uses.uses[smoke_detectors_ionization]: ~3 billion detectors globally | 3 billion | inquiry_periodic_elements_2025 | inferred | Widely cited industry figure but not present in DOE NIDC sources checked. Source is internal project document; no primary citation available. |
| end_uses.uses[smoke_detectors_ionization]: ~0.29 micrograms per detector | 0.29 micrograms | inquiry_periodic_elements_2025 | inferred | Standard NRC-licensed Am-241 quantity per ionization smoke detector; consistent with general industry literature (NRC regulatory value ≈ 1 µCi ≈ 0.29 µg) but not cited in DOE NIDC sources checked. Source is internal project document. |
| end_uses.uses[oil_well_logging_neutron_sources].share_pct | 8 | inquiry_periodic_elements_2025 | inferred | NIDC landing page confirms Am-Be sources are "commonly combined with beryllium … for well-logging in the oil and gas industry" but does not quantify the share. 8% from internal document; no primary source. |
| end_uses.uses[research_and_calibration].share_pct | 2 | inquiry_periodic_elements_2025 | inferred | Calibration and reference source use confirmed by NIDC availability for purchase ("routinely available"). Share pct from internal document; no primary source. |
| criticality.us_critical_list_as_of_2025 | false | (no cited source) | inferred | Am does not appear in USGS MCS 2025 or DOE critical-materials lists. YAML notes explain omission: "The market is too small in tonnage terms to trigger list inclusion criteria." No primary source explicitly states Am is absent; inferred from absence in all reviewed designations. |
| criticality.eu_crm_list_as_of_2024 | false | (no cited source) | inferred | Am does not appear in EU CRMA Regulation (EU) 2024/1252 Annex I or II per general review. YAML note gives same reasoning. Inferred from absence; no EU source directly cited. |
| criticality.eu_strategic_list_as_of_2024 | false | (no cited source) | inferred | Same reasoning as eu_crm_list_as_of_2024. |
| substitutes: photoelectric smoke detectors (availability: partial) | partial | doe_nidc_am241_product | inferred | YAML notes explicitly disclose: "None of these substitutes is cited in the DOE NIDC source; this note reflects general industry context." Photoelectric vs. ionization detector substitutability is well-established in fire safety literature but is not sourced to the cited document. |
| substitutes: Ni-63 for ionization applications | — | doe_nidc_am241_product | inferred | Same disclosure as photoelectric substitutes: general industry context, not cited in DOE NIDC. |
| substitutes: Cf-252 and Am-Be-free neutron sources for well-logging | — | doe_nidc_am241_product | inferred | Same disclosure. NIDC does not address substitutes; claim is general industry context per YAML note. |

## Notes

**Source access**: DOE NIDC Am-241 landing page (https://www.isotopes.gov/americium241) was fetched as HTML and parsed successfully. DOE NIDC Am-241 Product Information PDF (2024-11 revision) was fetched as binary; pdfplumber extracted the full one-page product sheet successfully. NNDC NuDat 3.0 Am-241 and Pu-241 decay search pages were fetched and parsed.

**Half-life seconds arithmetic error**: The YAML inline comment says `13650595560  # 432.6 years * 365.25 * 86400`, but the correct product is 432.6 × 365.25 × 86400 = 13,651,817,760 seconds. The stored value 13,650,595,560 corresponds to approximately 432.56 years × 365.25 d/y — off by 1,222,200 seconds (~14 days). This is a minor arithmetic error. The physics half-life of 432.6 years is independently confirmed by NNDC NuDat 3.0 and the NIDC product sheet. No practical consequence at the data-model level, but the comment is misleading; the formula should read `# 432.56 years × 365.25 × 86400` or the stored value should be corrected to 13,651,817,760.

**Pu-241 half-life 14.4 vs 14.3 years**: YAML precursor text states "Pu-241 has a 14.4-year half-life." NNDC NuDat 3.0 gives 14.290 ± 0.006 years (commonly rounded to 14.3 years in modern compilations). The YAML value of 14.4 years is a rounded figure from older literature (some pre-2010 sources cite 14.4 y). The discrepancy is 0.11 years (~40 days) — minor for narrative text but worth correcting to 14.3 years. The NIDC product sheet does not state the Pu-241 half-life, so `doe_nidc_am241_product` is not the correct source_id for this claim.

**Producer shares are explicit placeholders**: Both the US (50%) and ZZ (50%) producer shares are explicitly labelled `confidence: low` in the YAML and the notes block states they are "placeholder" values. `source_unreachable` is the correct status: not a case where the source contradicts the YAML, but where no primary quantitative source publishes these figures. DOE NIDC confirms LANL as a US producer and "routinely available" status; it does not publish market share or annual production volumes.

**20-year vs. decade-long supply gap**: The NIDC landing page states "for the last 20 years Americans have relied on a single foreign supplier" (written circa 2012, prior to domestic production resumption). The YAML narrative says "after a decade-long supply gap" and the criticality notes mention a "2015-2020 US supply gap." These descriptions are internally inconsistent: if domestic production ceased in 1984 and LANL restarted in 2012, the gap was ~28 years; if the "single foreign supplier" text is read as 20 years it implies the gap started around 1992. The YAML criticality notes reference "2015-2020" which contradicts both. No claim in the structured YAML fields (as opposed to narrative/notes text) hangs a numeric value on the supply-gap duration, so no row is included in the Claims table — but this inconsistency warrants follow-up.

**Gamma-ray cameras not listed**: The task description flagged gamma-ray cameras as an expected end use. Am-241 is used as a portable gamma-ray source in some industrial radiography applications, but the YAML does not include this as an end use (the three end uses are smoke detectors, well-logging, and research/calibration). The NIDC landing page mentions "moisture gauges" as a commercial use not captured in end_uses either. Both omissions should be noted for a future YAML update.

**Smoke detector quantity: NRC basis for 0.29 µg**: The US Nuclear Regulatory Commission (NRC) allows up to 1 µCi (37,000 disintegrations/second) of Am-241 per smoke detector under 10 CFR 30.15 exempt quantities. Converting: 1 µCi × (1 Ci = 3.7×10¹⁰ Bq) / (specific activity of Am-241 ≈ 3.43 Ci/g) ≈ 0.29 µg. This is a derivable figure consistent with the YAML value, but since the derivation is not cited to a primary document in Am.yaml, the claim remains inferred.

**No production_quantity field in YAML**: The task instruction noted "production_quantity.value if present (DOE NIDC)". Am.yaml has no production_quantity block, consistent with DOE NIDC not publishing annual volumes. Nothing to verify.

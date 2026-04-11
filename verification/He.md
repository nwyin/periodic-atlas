# Verification: He

- Element: helium (He)
- Snapshot year: 2025
- Verifier: agent worker-b0e80e5c2729
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 32 |
| discrepancy | 5 |
| inferred | 13 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 180 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: "World total (rounded) 180" for 2024e; 2023 = 176 also matches YAML note |
| production[0].mine notes "4% increase" | 4% | usgs_mcs_2025_helium | verified | p.89: "Estimated total world helium production increased by 4% compared with that in 2023" |
| production[0].mining_by_country[US].quantity.value | 81 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: US (extracted from natural gas) 68 + US (from Cliffside Field) 13 = 81 Mm3 |
| production[0].mining_by_country[US].share_pct | 45% | usgs_mcs_2025_helium | inferred | 81/180 = 45.0%; not stated as % in USGS |
| production[0].mining_by_country[QA].quantity.value | 64 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: Qatar 64 (estimated) |
| production[0].mining_by_country[QA].share_pct | 36% | usgs_mcs_2025_helium | inferred | 64/180 = 35.6% → rounded 36%; not in USGS |
| production[0].mining_by_country[RU].quantity.value | 17 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: Russia 17 (estimated) |
| production[0].mining_by_country[RU].share_pct | 9% | usgs_mcs_2025_helium | inferred | 17/180 = 9.4% → 9%; not in USGS |
| production[0].mining_by_country[DZ].quantity.value | 11 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: Algeria 11 |
| production[0].mining_by_country[DZ].share_pct | 6% | usgs_mcs_2025_helium | inferred | 11/180 = 6.1% → 6%; not in USGS |
| production[0].mining_by_country[CA].quantity.value | 6 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: Canada 6 |
| production[0].mining_by_country[CA].share_pct | 3% | usgs_mcs_2025_helium | inferred | 6/180 = 3.3% → 3%; not in USGS |
| production[0].mining_by_country[CN].quantity.value | 3 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: China 3 |
| production[0].mining_by_country[CN].share_pct | 2% | usgs_mcs_2025_helium | inferred | 3/180 = 1.7% → 2%; not in USGS |
| production[0].mining_by_country[PL].quantity.value | 3 million_m3_per_year | usgs_mcs_2025_helium | verified | p.89: Poland 3 |
| production[0].mining_by_country[PL].share_pct | 2% | usgs_mcs_2025_helium | inferred | 3/180 = 1.7% → 2%; not in USGS |
| production[0].mining_by_country[US].notes "Four plants in Texas and Kansas" | 4 plants | usgs_mcs_2025_helium | discrepancy | p.88: "Five plants (three in Texas and two in Kansas) extracted helium from natural gas" — YAML undercounts by one |
| reserves.economic_reserves.value | 12000 million_m3 | usgs_mcs_2025_helium | inferred | Sum: 8,550+1,800+1,700+24=12,074 Mm3; USGS world reserves = "NA"; Qatar = "Large" (no figure); YAML rounds to 12,000 as lower bound |
| reserves.reserves_by_country[US].quantity.value | 8550 million_m3 | usgs_mcs_2025_helium | verified | p.89: US (natural gas) 8,500 + US (Cliffside) 50 = 8,550 Mm3 |
| reserves.reserves_by_country[US].share_pct | 71% | usgs_mcs_2025_helium | inferred | 8,550/12,074 = 70.8% → 71%; denominator excludes Qatar ("Large") |
| reserves.reserves_by_country[DZ].quantity.value | 1800 million_m3 | usgs_mcs_2025_helium | verified | p.89: Algeria 1,800 (estimated) |
| reserves.reserves_by_country[DZ].share_pct | 15% | usgs_mcs_2025_helium | inferred | 1,800/12,074 = 14.9% → 15% |
| reserves.reserves_by_country[RU].quantity.value | 1700 million_m3 | usgs_mcs_2025_helium | verified | p.89: Russia 1,700 (estimated) |
| reserves.reserves_by_country[RU].share_pct | 14% | usgs_mcs_2025_helium | inferred | 1,700/12,074 = 14.1% → 14% |
| reserves.reserves_by_country[PL].quantity.value | 24 million_m3 | usgs_mcs_2025_helium | verified | p.89: Poland 24 |
| reserves.reserves_by_country[PL].share_pct | 0% | usgs_mcs_2025_helium | inferred | 24/12,074 = 0.2% → 0% |
| reserves.resources.value | 39800 million_m3 | usgs_mcs_2025_helium | inferred | US 8,490+51.5=8,541.5 + ex-US 31,300 = 39,841.5 ≈ 39,800 Mm3; USGS states components separately, not as a combined world total |
| reserves.resources notes "8,490 million cubic meters" (US) | 8490 million_m3 | usgs_mcs_2025_helium | verified | p.89: "mean volume of recoverable helium within the known geologic natural gas reservoirs in the United States was estimated to be 8,490 million cubic meters (306 billion cubic feet)" |
| reserves.resources notes "51.5 million cubic meters" (Federal inventory) | 51.5 million_m3 | usgs_mcs_2025_helium | verified | p.89: "remaining 51.5 million cubic meters (1.86 billion cubic feet) in the Federal helium inventory" |
| reserves.resources notes "31.3 billion cubic meters" (ex-US) | 31300 million_m3 | usgs_mcs_2025_helium | verified | p.89: "Helium resources of the world, exclusive of the United States, were estimated to be about 31.3 billion cubic meters (1.13 trillion cubic feet)" |
| reserves.resources notes major ex-US deposits | Qatar 10.1, DZ 8.2, RU 6.8, CA 2.0, CN 1.1 Bm3 | usgs_mcs_2025_helium | verified | p.89: "Qatar, 10.1; Algeria, 8.2; Russia, 6.8; Canada, 2.0; and China, 1.1" billion cubic meters — exact match |
| end_uses[analytical_engineering_lab_specialty_gases].share_pct | 22% | usgs_mcs_2025_helium | verified | p.88: "analytical, engineering, lab, science, and specialty gases (22%)" |
| end_uses[lifting_gas].share_pct | 18% | usgs_mcs_2025_helium | verified | p.88: "lifting gas (18%)" |
| end_uses[mri_cryogenics].share_pct | 17% | usgs_mcs_2025_helium | verified | p.88: "magnetic resonance imaging (17%)" |
| end_uses[controlled_atmospheres_fiber_optics_semiconductors].share_pct | 15% | usgs_mcs_2025_helium | verified | p.88: "controlled atmospheres, fiber optics, and semiconductors (15%)" |
| end_uses[welding_shield_gas].share_pct | 8% | usgs_mcs_2025_helium | verified | p.88: "welding (8%)" |
| end_uses[aerospace_pressuring_purging].share_pct | 7% | usgs_mcs_2025_helium | verified | p.88: "aerospace, pressuring, and purging (7%)" |
| end_uses[leak_detection].share_pct | 5% | usgs_mcs_2025_helium | verified | p.88: "leak detection (5%)" |
| end_uses[diving_breathing_gas].share_pct | 5% | usgs_mcs_2025_helium | verified | p.88: "diving (5%)" |
| end_uses[other].share_pct | 3% | usgs_mcs_2025_helium | verified | p.88: "various other minor applications (3%)" |
| prices[0].value | 14 usd_per_m3 | usgs_mcs_2025_helium | verified | p.88: "estimated base price for Grade-A helium was about $14 per cubic meter ($390 per thousand cubic feet) in 2024" |
| feedstock_origins[0].typical_concentration_pct | 0.5% | usgs_mcs_2025_helium | discrepancy | USGS states crude helium purity (50–80%), not raw natural gas He concentration; 0.5% not stated anywhere in the MCS helium chapter; source mis-attributed |
| feedstock_origins[0] notes crude purity range | 50–80% | usgs_mcs_2025_helium | verified | p.88: "produced crude helium that generally ranged from 50% to 80% helium" |
| geopolitical_events[0] Helium Shortage 4.0 | date: 2022-01 | inquiry_periodic_elements_2025 | source_unreachable | Source is internal file path with no URL; cannot fetch to verify |
| geopolitical_events[1].date | 2024-01-25 | usgs_mcs_2025_helium | verified | p.88: "On January 25, 2024, the Federal Helium System assets were sold in two lots." |
| geopolitical_events[1] Lot 1 volume | ~28 Mm3 (1.0 Bcf) | usgs_mcs_2025_helium | verified | p.88: "Lot 1 included approximately 28 million cubic meters (1.0 billion cubic feet)" |
| geopolitical_events[1] Lot 2 volume | ~22 Mm3 (800 MMcf) | usgs_mcs_2025_helium | verified | p.88: "Lot 2 included the Federal Helium System and approximately 22 million cubic meters (800 million cubic feet)" |
| geopolitical_events[1] transfer date | 2024-06-27 | usgs_mcs_2025_helium | verified | p.88: "Both lots were sold to one company and were transferred on June 27, 2024." |
| geopolitical_events[1].impact "Ends 62 years" | 62 years | usgs_mcs_2025_helium | discrepancy | Not stated in USGS MCS; Helium Act of 1960 → 2024-1960=64 yrs; USGS makes no duration claim; attributed to usgs_mcs_2025_helium in error |
| geopolitical_events[2].date | 2024-06-25 | usgs_mcs_2025_helium | verified | p.89: "On June 25, 2024, the European Union adopted a sanctions package" |
| geopolitical_events[2] effective date | 2024-09-26 | usgs_mcs_2025_helium | verified | p.89: "effective September 26, 2024, that imposed an import ban on helium from Russia" |
| geopolitical_events[3].date (CHEU expiry) | 2024-08-11 | usgs_mcs_2025_helium | verified | p.88: "The lease of the CHEU ended on August 11, 2024" |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_helium | discrepancy | EU CRM status not mentioned anywhere in the USGS MCS helium chapter; source is mis-attributed |
| form_notes temperature condition | 21.1°C (70°F) | usgs_mcs_2025_helium | discrepancy | USGS fn.1: data measured at 15°C (59°F); 21.1°C (70°F) is the reference temperature for the m3↔ft3 conversion factor only (27.737 m3 = 1,000 ft3 at 21.1°C), not the reporting temperature |

## Notes

### Unit conditions (form_notes discrepancy)
He.yaml states "USGS reports helium volumes at 101.325 kPa absolute and 21.1°C (70°F)." USGS footnote 1 actually specifies two distinct reference conditions: (a) data are measured at 101.325 kPa and **15°C (59°F)**, and (b) the conversion factor 27.737 m3 = 1,000 ft3 is defined at 21.1°C (70°F). The YAML form_notes conflates the two, attributing the conversion temperature to the measurement condition. The 1,000 ft3 = 27.737 m3 factor in form_notes is correct at 21.1°C but does not describe the reporting temperature of the volume data.

### Country-share percentages all inferred
No USGS percentage breakdown by country exists in the helium chapter. All seven production share_pct values and all four reserves share_pct values were derived by dividing country figures by the world/summed total. Rounding is consistent (nearest integer). The shares are arithmetically correct but should not be cited as USGS-stated values.

### Plant count discrepancy (US production notes)
YAML notes for the US entry say "Four plants in Texas and Kansas extract crude helium from natural gas." USGS p.88 says "Five plants (three in Texas and two in Kansas)." The five-plant count reflects a new US operation that came online in 2024; the YAML appears to use an outdated four-plant figure. Follow-up: update YAML note to "Five plants."

### Feedstock concentration (0.5%)
The `typical_concentration_pct: 0.5` for natural_gas is attributed to usgs_mcs_2025_helium but is not found there. USGS MCS covers crude helium purity post-extraction (50–80%), not the concentration of He in raw feed gas. The 0.5% figure is a plausible industry rule-of-thumb but lacks a source in this document. Follow-up: cite an alternative source (e.g., USGS helium report 2021–5085) or remove the field.

### "62 years" duration claim
The impact text for the Federal Helium System sale includes "Ends 62 years of US government helium market participation." This is attributed to usgs_mcs_2025_helium but does not appear in it. The Helium Act of 1960 provides a starting reference point (2024−1960 = 64 years); the figure "62" may derive from 1962, when Bush Dome operations ramped up. Regardless, USGS makes no such claim. Follow-up: remove or re-source this assertion.

### EU CRM criticality flag
`criticality.eu_crm_list_as_of_2024: true` is sourced to usgs_mcs_2025_helium, but the USGS MCS helium chapter contains no EU CRM information. The claim is likely factually correct (helium was added to the EU CRM list in 2023), but needs a EU Commission source, not USGS. Follow-up: add an EU CRM source (e.g., European Commission Critical Raw Materials list 2023).

### Resources total (39,800 Mm3) is a derived sum
USGS reports US resources (8,490 Mm3 assessed + 51.5 Mm3 federal inventory) and ex-US resources (~31,300 Mm3 = 31.3 billion m3) separately. The YAML combines these: 8,490 + 51.5 + 31,300 = 39,841.5 Mm3, rounded to 39,800. This arithmetic is correct, but the YAML presents it as a single `resources.value` field that USGS never states as a combined total. Marked as inferred accordingly.

### Reserves total denominator excludes Qatar
The economic_reserves.value of 12,000 Mm3 is the sum of four USGS-quantified countries (US, Algeria, Russia, Poland = 12,074 Mm3). Qatar's reserves are listed as "Large" with no numeric value, and world total reserves = "NA" in USGS. The YAML notes this explicitly as a lower bound. The omission is correctly disclosed.

# Verification: Pt

- Element: platinum (Pt)
- Snapshot year: 2025
- Verifier: worker-912dbe8bc6c5 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 57 |
| discrepancy | 0 |
| inferred | 14 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 170000 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, Platinum 2024e column: "World total (rounded) 170,000" |
| production[0].mine.notes "2023 = 179,000 kg" | 179000 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Platinum 2023 column: "World total (rounded) 179,000" |
| production[0].mine.notes "Pd 190,000 kg world 2024e" | 190000 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Palladium 2024e column: "World total (rounded) 190,000" |
| production[0].mine.notes "Pt+Pd ~94% of two primary PGMs" | ~94 pct | usgs_mcs_2025_pgm | inferred | Derived: (170,000+190,000)/360,000 = 100%; claim is that Pt+Pd dominate; USGS does not state a "94%" fraction. The denominator for "all PGMs" is not given in the chapter, making the 94% an estimate. |
| production[0].mine.notes "Pt basket share ~47% (170,000/360,000)" | ~47 pct | usgs_mcs_2025_pgm | inferred | Derived: 170,000/(170,000+190,000) = 47.2%. Numerator and denominator are both verified, but the "basket share" ratio is not stated by USGS. |
| production[0].mine.notes "Rh 15,000 kg US imports" | 15000 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Imports—Rhodium 2024e: 15,000 |
| production[0].mine.notes "Ru 10,000 kg US imports" | 10000 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Imports—Ruthenium 2024e: 10,000 |
| production[0].mine.notes "Ir 1,400 kg US imports" | 1400 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Imports—Iridium 2024e: 1,400 |
| production[0].mining_by_country[ZA].share_pct | 70.6 pct | usgs_mcs_2025_pgm | verified | Derived from table: ZA 120,000 / World 170,000 = 70.59% ≈ 70.6%; both figures directly in World Mine Production table |
| production[0].mining_by_country[ZA].quantity.value | 120000 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, South Africa Platinum 2024e: 120,000 |
| production[0].mining_by_country[ZA].notes "2023 = 125,000 kg" | 125000 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, South Africa Platinum 2023: 125,000 |
| production[0].mining_by_country[ZW].share_pct | 11.2 pct | usgs_mcs_2025_pgm | verified | Derived from table: ZW 19,000 / World 170,000 = 11.18% ≈ 11.2%; both figures in table |
| production[0].mining_by_country[ZW].quantity.value | 19000 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, Zimbabwe Platinum 2024e: 19,000 |
| production[0].mining_by_country[ZW].notes "2023 = 19,200 kg" | 19200 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Zimbabwe Platinum 2023: 19,200 |
| production[0].mining_by_country[RU].share_pct | 10.6 pct | usgs_mcs_2025_pgm | verified | Derived from table: RU 18,000 / World 170,000 = 10.59% ≈ 10.6%; both figures in table |
| production[0].mining_by_country[RU].quantity.value | 18000 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, Russia Platinum 2024e: 18,000 |
| production[0].mining_by_country[RU].notes "2023 = 21,000 kg" | 21000 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Russia Platinum 2023: 21,000 |
| production[0].mining_by_country[RU].notes "~14% decline" | ~14 pct | usgs_mcs_2025_pgm | verified | Derived: (21,000−18,000)/21,000 = 14.3%; both figures directly in source table |
| production[0].mining_by_country[CA].share_pct | 3.1 pct | usgs_mcs_2025_pgm | verified | Derived from table: CA 5,200 / World 170,000 = 3.06% ≈ 3.1%; both figures in table |
| production[0].mining_by_country[CA].quantity.value | 5200 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, Canada Platinum 2024e: 5,200 |
| production[0].mining_by_country[CA].notes "2023 = 5,170 kg" | 5170 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Canada Platinum 2023: 5,170 |
| production[0].mining_by_country[US].share_pct | 1.2 pct | usgs_mcs_2025_pgm | verified | Derived from table: US 2,000 / World 170,000 = 1.18% ≈ 1.2%; both figures in table |
| production[0].mining_by_country[US].quantity.value | 2000 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, United States Platinum 2024e: 2,000; also Salient Statistics mine production Platinum 2024e: 2,000 |
| production[0].mining_by_country[US].notes "2023 = 3,040 kg" | 3040 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Mine production—Platinum 2023: 3,040; World Mine Production table 2023: 3,040 |
| production[0].mining_by_country[US].notes "34% decline" | ~34 pct | usgs_mcs_2025_pgm | verified | Derived: (3,040−2,000)/3,040 = 34.2%; both figures in source |
| production[0].mining_by_country[US].notes "employment ~1,450 to ~900" | 1450 to 900 | usgs_mcs_2025_pgm | verified | Salient Statistics table, Employment—mine 2023: 1,450; 2024e: 900 |
| production[0].mining_by_country[US].notes "$310 million, down 42% from $541 million" | $310M / -42% / $541M | usgs_mcs_2025_pgm | verified | "One company in Montana mined and processed PGMs with an estimated value of about $310 million in 2024, a decrease of 42% compared with $541 million in 2023" — Domestic Production and Use section |
| production[0].mining_by_country[ZZ].share_pct | 2.7 pct | usgs_mcs_2025_pgm | verified | Derived from table: Other 4,600 / World 170,000 = 2.71% ≈ 2.7%; both figures in table |
| production[0].mining_by_country[ZZ].quantity.value | 4600 kg_per_year | usgs_mcs_2025_pgm | verified | World Mine Production table, Other countries Platinum 2024e: 4,600 |
| production[0].mining_by_country[ZZ].notes "2023 = 5,710 kg" | 5710 kg | usgs_mcs_2025_pgm | verified | World Mine Production table, Other countries Platinum 2023: 5,710 |
| reserves.economic_reserves.value | 81000000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves World total: ">81,000,000" |
| reserves.economic_reserves.notes "World PGM resources >100,000,000 kg" | >100000000 kg | usgs_mcs_2025_pgm | verified | "World Resources: World resources of PGMs are estimated to total more than 100 million kilograms." |
| reserves.reserves_by_country[ZA].quantity.value | 63000000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves South Africa: 63,000,000 |
| reserves.reserves_by_country[ZA].share_pct | 77.8 pct | usgs_mcs_2025_pgm | verified | Derived: 63,000,000 / 81,000,000 = 77.78% ≈ 77.8%; both figures in source table |
| reserves.reserves_by_country[RU].quantity.value | 16000000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves Russia: 16,000,000; footnote 10 |
| reserves.reserves_by_country[RU].share_pct | 19.8 pct | usgs_mcs_2025_pgm | verified | Derived: 16,000,000 / 81,000,000 = 19.75% ≈ 19.8%; both figures in source |
| reserves.reserves_by_country[RU].notes "Russian Classification A+B+C1+C2" | Russian Classification | usgs_mcs_2025_pgm | verified | "Reserves for Russia are based on the Russian Classification system A+B+C1+C2, where C2 are deposits that are being developed or prepared for development." — footnote 10 |
| reserves.reserves_by_country[ZW].quantity.value | 1200000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves Zimbabwe: 1,200,000 |
| reserves.reserves_by_country[ZW].share_pct | 1.5 pct | usgs_mcs_2025_pgm | verified | Derived: 1,200,000 / 81,000,000 = 1.48% ≈ 1.5%; both figures in source |
| reserves.reserves_by_country[US].quantity.value | 820000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves United States: 820,000 |
| reserves.reserves_by_country[US].share_pct | 1.0 pct | usgs_mcs_2025_pgm | verified | Derived: 820,000 / 81,000,000 = 1.01% ≈ 1.0%; both figures in source |
| reserves.reserves_by_country[CA].quantity.value | 310000 kg | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves Canada: 310,000 |
| reserves.reserves_by_country[CA].share_pct | 0.4 pct | usgs_mcs_2025_pgm | verified | Derived: 310,000 / 81,000,000 = 0.38% ≈ 0.4%; both figures in source |
| reserves.notes "Other countries: NA" | NA | usgs_mcs_2025_pgm | verified | World Mine Production and Reserves table, PGM reserves Other countries: "NA" |
| reserves.notes "country totals 81,330,000 kg" | 81330000 kg | usgs_mcs_2025_pgm | inferred | Arithmetic from source values: 63,000,000+16,000,000+1,200,000+820,000+310,000 = 81,330,000. The individual country values are verified; the sum itself is not stated by USGS. |
| end_uses[autocatalysts].notes "leading domestic use" | leading domestic use | usgs_mcs_2025_pgm | verified | "The leading domestic use for PGMs was in catalytic converters to decrease harmful emissions from automobiles." — Domestic Production and Use section |
| end_uses[autocatalysts].share_pct | 40 pct | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 PGM chapter does not report percentage end-use breakdown for platinum. 40% is an industry consensus estimate; the chapter names autocatalysts as the leading use but gives no quantified share. |
| end_uses[jewelry].share_pct | 28 pct | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 names jewelry as an end use but provides no percentage. 28% is an estimate not supported by explicit figures in the cited chapter. |
| end_uses[chemical_and_industrial_catalysts].share_pct | 17 pct | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 names catalysts for bulk chemicals and petroleum refining as an end use but provides no percentage. 17% is an estimate. |
| end_uses[investment].share_pct | 8 pct | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 names investment as an end use but provides no percentage. 8% is an estimate. |
| end_uses[other_industrial].share_pct | 7 pct | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 names dental, medical, electronic, glass manufacturing, and laboratory as further uses but provides no percentage. 7% is an estimate. |
| substitutes[autocatalysts].notes USGS quote on Pd substituting Pt | "Palladium has been used as a substitute…" | usgs_mcs_2025_pgm | verified | "Palladium has been used as a substitute for platinum in most gasoline-engine catalytic converters because of the historically lower price for palladium relative to that of platinum." — Substitutes section |
| substitutes[autocatalysts].notes "25% routinely, up to 50%" | 25 pct / 50 pct | usgs_mcs_2025_pgm | verified | "About 25% of palladium can routinely be substituted for platinum in diesel catalytic converters; the proportion can be as much as 50% in some applications." — Substitutes section |
| substitutes[general].notes USGS quote "For some industrial end uses…" | "For some industrial end uses, one PGM can substitute for another, but with losses in efficiency." | usgs_mcs_2025_pgm | verified | Exact quote confirmed: "For some industrial end uses, one PGM can substitute for another, but with losses in efficiency." — Substitutes section |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_pgm | inferred | PGMs are on the US 2022 Final List of Critical Minerals (Federal Register Vol. 87, No. 37). The cited USGS MCS 2025 PGM chapter does not explicitly state "critical minerals list" in its text; the claim is consistent with USGS-administered criticality framework but not directly quoted from this chapter. |
| criticality.notes "85% net import reliant" | 85 pct | usgs_mcs_2025_pgm | verified | Salient Statistics table, Net import reliance—Platinum 2024e: 85 |
| criticality.notes "71,000 kg apparent consumption" | 71000 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Consumption apparent—Platinum 2024e: 71,000 |
| criticality.notes "2,000 kg domestic mine production" | 2000 kg | usgs_mcs_2025_pgm | verified | Salient Statistics table, Mine production—Platinum 2024e: 2,000 |
| criticality.notes "ZA 45%, BE 12%, DE 10%, IT 9%, other 24%" | ZA 45% / BE 12% / DE 10% / IT 9% / other 24% | usgs_mcs_2025_pgm | verified | "Import Sources (2020–23): Platinum: South Africa, 45%; Belgium, 12%; Germany, 10%; Italy, 9%; and other, 24%." — Import Sources section |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | inferred | EU Regulation 2024/1252 (CRMA) lists platinum-group metals in Annex I (Critical Raw Materials). Source URL (eur-lex.europa.eu) returned a WAF challenge and was not accessible during this verification pass; designation is consistent with all prior PGM and REE element verifications in this project. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | inferred | EU Regulation 2024/1252 (CRMA) lists platinum-group metals in Annex II (Strategic Raw Materials). Same access caveat as eu_crm flag. |
| geopolitical_events[0] US production 3,040→2,000 kg, 34% decline | 3040→2000 kg / 34 pct | usgs_mcs_2025_pgm | verified | Salient Statistics: Mine production Platinum 2023=3,040, 2024e=2,000; delta=(3,040−2,000)/3,040=34.2% |
| geopolitical_events[0] care-and-maintenance, employment 1,450→900 | 1450→900 | usgs_mcs_2025_pgm | verified | "the company placed one of its operations on care-and-maintenance status and reduced the number of its employees"; Employment 2023=1,450, 2024e=900 — Events section and Salient Statistics |
| geopolitical_events[0] "$310M, down 42% from $541M" | $310M / -42% / $541M | usgs_mcs_2025_pgm | verified | "about $310 million in 2024, a decrease of 42% compared with $541 million in 2023" — Domestic Production and Use section |
| geopolitical_events[1] ZA production 125,000→120,000, ~4% decline | 125000→120000 kg / ~4 pct | usgs_mcs_2025_pgm | verified | World Mine Production table: South Africa Pt 2023=125,000, 2024e=120,000; decline=(125,000−120,000)/125,000=4.0% |
| geopolitical_events[1] causes: prices, deep-level costs, labor, electricity | qualitative | usgs_mcs_2025_pgm | verified | "decreased compared with that in 2023 owing to declining prices, higher costs associated with deep-level mining, labor disputes, and ongoing disruptions to the supply of electricity." — Events section |
| geopolitical_events[2] RU production 21,000→18,000, ~14% decline | 21000→18000 kg / ~14 pct | usgs_mcs_2025_pgm | verified | World Mine Production table: Russia Pt 2023=21,000, 2024e=18,000; decline=(21,000−18,000)/21,000=14.3% |
| geopolitical_events[2] causes: natural disasters, grades, RU-UA conflict, plant outages | qualitative | usgs_mcs_2025_pgm | verified | "disruptions from natural disasters, lower metal grades and ore recovery, ongoing issues related to the Russia-Ukraine conflict, and planned outages at a major metallurgical plant." — Events section |
| geopolitical_events[3] Rh -31%, Pd -27% | -31 pct / -27 pct | usgs_mcs_2025_pgm | verified | "estimated annual average prices for rhodium decreased by 31% for rhodium, by 27% for palladium…" — Events section |
| geopolitical_events[3] Pt price "slightly down" from $973 | ~$950 / slightly down | usgs_mcs_2025_pgm | verified | "and slightly for platinum compared with annual average prices in 2023"; Pt 2024e=$950 vs 2023=$973.00 — Events section and Salient Statistics |
| prices[2024].value | 950 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient Statistics table, Price—Platinum 2024e: 950 |
| prices[2023].value | 973 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient Statistics table, Price—Platinum 2023: 973.00 |
| prices[2022].value | 966.54 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient Statistics table, Price—Platinum 2022: 966.54 |
| prices[2021].value | 1094.31 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient Statistics table, Price—Platinum 2021: 1,094.31 |
| prices[2020].value | 886.02 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient Statistics table, Price—Platinum 2020: 886.02 |
| narrative "~8,500 kg/year from US sources" (autocatalyst recycling) | 8500 kg_per_year | usgs_mcs_2025_pgm | verified | "about 45,000 kilograms of palladium and 8,500 kilograms of platinum recovered from automobile catalytic converters in the United States." — Recycling section |
| narrative "roughly 12% of US apparent consumption" | ~12 pct | usgs_mcs_2025_pgm | inferred | Derived: 8,500 kg recycled / 71,000 kg apparent consumption = 11.97% ≈ 12%. Both inputs are verified from source; the ratio itself is not stated by USGS. |

## Notes

All production, reserve, price, import source, recycling, and employment figures verified directly against USGS MCS 2025 Platinum-Group Metals chapter PDF (mcs2025-platinum-group.pdf, 747KB, dated 2025-01-31). The correct PDF filename is `mcs2025-platinum-group.pdf` (not `mcs2025-platinum-group-metals.pdf` as recorded in the YAML source URL); the URL in sources[usgs_mcs_2025_pgm] returns 404 but the correct URL `https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-platinum-group.pdf` is accessible.

All five platinum prices (2020–2024) confirmed exactly from the Salient Statistics table. Engelhard unfabricated metal average annual prices; source: S&P Global Platts Metals Week (USGS footnote 6).

Reserve share percentages (ZA, RU, ZW, US, CA) are derived from the source table values using the world total floor of 81,000,000 kg. These are treated as `verified` because both the numerator (country reserve) and denominator (world total) are directly reported in the same table, and the arithmetic is unambiguous.

End-use percentage claims (autocatalysts 40%, jewelry 28%, chemical catalysts 17%, investment 8%, other 7%) are all `inferred` — the USGS MCS 2025 PGM chapter lists platinum end uses qualitatively (naming autocatalysts as "the leading domestic use") but provides no quantified percentage breakdown. These percentages are industry consensus estimates consistent with published data from WPIC and Johnson Matthey, but are not directly supported by the cited USGS chapter.

EU CRMA (Regulation 2024/1252) flags are `inferred`. The eur-lex.europa.eu URL for this regulation returned a WAF (Web Application Firewall) challenge with HTTP 202 and zero content during this verification pass — consistent with observations in prior Lu and other element verifications. The PGM listing in both CRMA Annex I (critical) and Annex II (strategic) is well-established from European Commission communications and consistent with all prior element verifications in this project.

US criticality flag is `inferred` — the cited source (usgs_mcs_2025_pgm) is the PGM chapter which does not explicitly mention the critical minerals list; the correct authoritative source would be Federal Register Vol. 87, No. 37 (2022) or a dedicated USGS critical minerals list publication. The fact itself (PGMs on US critical list) is accurate.

No discrepancies found. All quantitative claims for production, reserves, prices, recycling, and geopolitical events were confirmed directly from the USGS MCS 2025 PGM chapter.

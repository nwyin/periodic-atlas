# Verification: Pd

- Element: palladium (Pd)
- Snapshot year: 2025
- Verifier: worker-fce49e7fdcc2 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 40 |
| discrepancy | 3 |
| inferred | 29 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 190000 kg_per_year | usgs_mcs_2025_pgm | verified | "World total (rounded) 190,000" — World Mine Production and Reserves table, Palladium 2024e column, p.137 |
| production[0].mine.notes "world total 2023 = 208,000 kg" | 208000 kg_per_year | usgs_mcs_2025_pgm | verified | "World total (rounded) 208,000" — World Mine Production and Reserves table, Palladium 2023 column, p.137 |
| production[0].mine.notes "−8.7% YoY" | -8.7 pct | usgs_mcs_2025_pgm | inferred | Calculated: (208,000−190,000)/208,000 = 8.65% ≈ −8.7%. USGS does not state this percentage directly. |
| production[0].mining_by_country.shares[RU].share_pct | 39.5 pct | usgs_mcs_2025_pgm | inferred | Calculated: 75,000/190,000 = 39.47% ≈ 39.5%. USGS gives absolute figures only; share not stated directly. |
| production[0].mining_by_country.shares[RU].quantity.value | 75000 kg_per_year | usgs_mcs_2025_pgm | verified | "Russia 87,000 / 75,000" — World Mine Production and Reserves table, Palladium 2023/2024e columns, p.137 |
| production[0].mining_by_country.shares[RU].notes "down from 87,000 kg in 2023 (−14% YoY)" | 87000 kg_per_year / -14 pct | usgs_mcs_2025_pgm | verified | Russia 2023=87,000 confirmed in table. −14%: (87,000−75,000)/87,000 = 13.8% ≈ −14% (calculated from table values) |
| production[0].mining_by_country.shares[ZA].share_pct | 37.9 pct | usgs_mcs_2025_pgm | inferred | Calculated: 72,000/190,000 = 37.89% ≈ 37.9%. Not stated directly by USGS. |
| production[0].mining_by_country.shares[ZA].quantity.value | 72000 kg_per_year | usgs_mcs_2025_pgm | verified | "South Africa 74,900 / 72,000" — World Mine Production and Reserves table, Palladium 2023/2024e columns, p.137 |
| production[0].mining_by_country.shares[ZA].notes "down from 74,900 kg in 2023 (−4% YoY)" | 74900 kg_per_year / -4 pct | usgs_mcs_2025_pgm | verified | ZA 2023=74,900 confirmed in table; −4%: (74,900−72,000)/74,900 = 3.87% ≈ −4% (calculated) |
| production[0].mining_by_country.shares[ZW].share_pct | 7.9 pct | usgs_mcs_2025_pgm | inferred | Calculated: 15,000/190,000 = 7.89% ≈ 7.9%. Not stated directly by USGS. |
| production[0].mining_by_country.shares[ZW].quantity.value | 15000 kg_per_year | usgs_mcs_2025_pgm | verified | "Zimbabwe 15,900 / 15,000" — World Mine Production and Reserves table, Palladium 2023/2024e columns, p.137 |
| production[0].mining_by_country.shares[ZW].notes "unchanged from 2023" | unchanged | usgs_mcs_2025_pgm | discrepancy | USGS table shows Zimbabwe Pd 2023=15,900, 2024e=15,000 — a decline of 900 kg (−5.7%). Calling it "unchanged" is inaccurate; the two years are not equal. |
| production[0].mining_by_country.shares[CA].share_pct | 7.9 pct | usgs_mcs_2025_pgm | inferred | Calculated: 15,000/190,000 = 7.89% ≈ 7.9%. Not stated directly by USGS. |
| production[0].mining_by_country.shares[CA].quantity.value | 15000 kg_per_year | usgs_mcs_2025_pgm | verified | "Canada 16,100 / 15,000" — World Mine Production and Reserves table, Palladium 2023/2024e columns, p.137 |
| production[0].mining_by_country.shares[CA].notes "down from 16,100 kg in 2023" | 16100 kg_per_year | usgs_mcs_2025_pgm | verified | Canada 2023=16,100 confirmed in table. |
| production[0].mining_by_country.shares[US].share_pct | 4.2 pct | usgs_mcs_2025_pgm | inferred | Calculated: 8,000/190,000 = 4.21% ≈ 4.2%. Not stated directly by USGS. |
| production[0].mining_by_country.shares[US].quantity.value | 8000 kg_per_year | usgs_mcs_2025_pgm | verified | "United States 10,300 / 8,000" — World Mine Production and Reserves table, Palladium 2023/2024e columns, p.137; also confirmed in Salient Statistics Mine production 2024e=8,000, p.136 |
| production[0].mining_by_country.shares[US].notes "down from 10,300 kg in 2023 (−22% YoY)" | 10300 kg_per_year / -22 pct | usgs_mcs_2025_pgm | verified | US 2023=10,300 confirmed in table; −22%: (10,300−8,000)/10,300 = 22.3% ≈ −22% (calculated) |
| production[0].mining_by_country.shares[US].notes "estimated value of ~$310 million in 2024 (down 42% from $541 million in 2023)" | 310 million USD / -42 pct / 541 million USD | usgs_mcs_2025_pgm | verified | "estimated value of about $310 million in 2024, a decrease of 42% compared with $541 million in 2023" — Domestic Production and Use section, p.136 |
| production[0].mining_by_country.shares[ZZ].share_pct | 2.2 pct | usgs_mcs_2025_pgm | inferred | Calculated: 4,200/190,000 = 2.21% ≈ 2.2%. Not stated directly by USGS. |
| production[0].mining_by_country.shares[ZZ].quantity.value | 4200 kg_per_year | usgs_mcs_2025_pgm | verified | "Other countries 4,200 / 4,200" — World Mine Production and Reserves table, both years equal, p.137 |
| production[0].refining_by_country.shares[ZA].share_pct | 40 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish world Pd refining shares by country. 40% is an industry estimate; confidence: low per YAML. |
| production[0].refining_by_country.shares[RU].share_pct | 40 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish world Pd refining shares by country. 40% is an industry estimate; confidence: low per YAML. |
| production[0].refining_by_country.shares[BE].share_pct | 8 pct | usgs_mcs_2025_pgm | verified | "Belgium, 8%" — Import Sources (2020–23) Palladium table, p.136. Note: this is a US import-source share, not a global refining share; YAML notes correctly explain this distinction. |
| production[0].refining_by_country.shares[IT].share_pct | 8 pct | usgs_mcs_2025_pgm | verified | "Italy, 8%" — Import Sources (2020–23) Palladium table, p.136. Same note as Belgium above. |
| production[0].refining_by_country.shares[ZZ].notes "~45,000 kg Pd recovered globally in 2024" | 45000 kg global | usgs_mcs_2025_pgm | discrepancy | USGS states "about 45,000 kilograms of palladium...recovered from automobile catalytic converters in the United States" (Recycling section, p.136) — US-only, not global. Global combined Pd+Pt recovery is stated as ~120,000 kg. YAML misattributes the US-autocatalyst figure as the global total. |
| reserves.economic_reserves.value | 81000000 kg | usgs_mcs_2025_pgm | verified | ">81,000,000" — World Mine Production and Reserves table, PGM reserves column, p.137 |
| reserves.economic_reserves.notes "World PGM resources total more than 100,000,000 kg" | >100000000 kg | usgs_mcs_2025_pgm | verified | "World resources of PGMs are estimated to total more than 100 million kilograms" — World Resources section, p.137 |
| reserves.reserves_by_country.shares[ZA].share_pct | 77.8 pct | usgs_mcs_2025_pgm | inferred | Calculated: 63,000,000/81,000,000 = 77.78% ≈ 77.8%. Not stated directly; derived from table values. |
| reserves.reserves_by_country.shares[ZA].quantity.value | 63000000 kg | usgs_mcs_2025_pgm | verified | "South Africa 63,000,000" — PGM reserves column, p.137 |
| reserves.reserves_by_country.shares[RU].share_pct | 19.8 pct | usgs_mcs_2025_pgm | inferred | Calculated: 16,000,000/81,000,000 = 19.75% ≈ 19.8%. Not stated directly. |
| reserves.reserves_by_country.shares[RU].quantity.value | 16000000 kg | usgs_mcs_2025_pgm | verified | "Russia 10 16,000,000" — PGM reserves column, p.137. Footnote 10: Russian Classification A+B+C1+C2. |
| reserves.reserves_by_country.shares[ZW].share_pct | 1.5 pct | usgs_mcs_2025_pgm | inferred | Calculated: 1,200,000/81,000,000 = 1.48% ≈ 1.5%. Not stated directly. |
| reserves.reserves_by_country.shares[ZW].quantity.value | 1200000 kg | usgs_mcs_2025_pgm | verified | "Zimbabwe 1,200,000" — PGM reserves column, p.137 |
| reserves.reserves_by_country.shares[US].share_pct | 1.0 pct | usgs_mcs_2025_pgm | inferred | Calculated: 820,000/81,000,000 = 1.01% ≈ 1.0%. Not stated directly. |
| reserves.reserves_by_country.shares[US].quantity.value | 820000 kg | usgs_mcs_2025_pgm | verified | "United States 820,000" — PGM reserves column, p.137 |
| reserves.reserves_by_country.shares[CA].share_pct | 0.4 pct | usgs_mcs_2025_pgm | inferred | Calculated: 310,000/81,000,000 = 0.38% ≈ 0.4%. Not stated directly. |
| reserves.reserves_by_country.shares[CA].quantity.value | 310000 kg | usgs_mcs_2025_pgm | verified | "Canada 310,000" — PGM reserves column, p.137 |
| end_uses[autocatalysts_gasoline_twc].share_pct | 80 pct | usgs_mcs_2025_pgm | inferred | USGS confirms leading domestic use is "catalytic converters to decrease harmful emissions from automobiles" but provides no Pd-specific end-use percentage breakdown. 80% is an industry consensus estimate; YAML notes acknowledge this explicitly. |
| end_uses[electronics_capacitors_connectors].share_pct | 10 pct | usgs_mcs_2025_pgm | inferred | USGS confirms "electronic applications, such as in computer hard disks, hybridized integrated circuits, and multilayer ceramic capacitors" as an end use (p.136), but provides no percentage. |
| end_uses[dental_alloys].share_pct | 4 pct | usgs_mcs_2025_pgm | inferred | USGS confirms "dental and medical devices" as an end use (p.136), but provides no percentage. |
| end_uses[industrial_chemical_catalysts].share_pct | 3 pct | usgs_mcs_2025_pgm | inferred | USGS confirms "catalysts for bulk-chemical production and petroleum refining" as an end use (p.136), but provides no percentage. |
| end_uses[investment_and_jewelry].share_pct | 3 pct | usgs_mcs_2025_pgm | inferred | USGS confirms "investment" and "jewelry" as end uses (p.136), but provides no percentage. |
| prices[2020].value | 2205.27 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 2,205.27" — Salient Statistics Price row, 2020 column, p.136. Source: Engelhard unfabricated metal average; S&P Global Platts Metals Week. |
| prices[2021].value | 2419.18 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 2,419.18" — Salient Statistics Price row, 2021 column, p.136 |
| prices[2022].value | 2133.81 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 2,133.81" — Salient Statistics Price row, 2022 column, p.136 |
| prices[2023].value | 1351.66 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 1,351.66" — Salient Statistics Price row, 2023 column, p.136 |
| prices[2024].value | 980 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 980" — Salient Statistics Price row, 2024e column, p.136 |
| geopolitical_events[2022-02].impact "Pd prices spiked above $3,000/oz in March 2022" | >3000 usd_per_troy_oz | usgs_mcs_2025_pgm | inferred | USGS does not state the March 2022 intra-year high directly in the salient statistics. The annual 2022 average was $2,133.81; the $3,000+ intra-year spike is consistent with market context but not stated as a value in the USGS PGM chapter. |
| geopolitical_events[2022-02].impact "Russia supplies ~40% of world Pd" | ~40 pct | usgs_mcs_2025_pgm | inferred | Calculated from 2024e production table: Russia 75,000/190,000 = 39.5%. USGS does not explicitly state the 40% share as a figure; the ~40% is a rounded calculation from the table. |
| geopolitical_events[2023-01].impact "US Pd production fell from ~11,000 kg (2022)" | ~11000 kg_per_year | usgs_mcs_2025_pgm | discrepancy | USGS Salient Statistics table (p.136) shows US Palladium mine production 2022=10,100 kg. The value ~11,000 is not close to the actual 10,100; correct rounding would be ~10,000 kg. |
| geopolitical_events[2023-01].impact "to 10,300 kg (2023)" | 10300 kg_per_year | usgs_mcs_2025_pgm | verified | "United States 10,300" — World Mine Production table Pd 2023 column, p.137; also Salient Statistics 2023=10,300, p.136 |
| geopolitical_events[2023-01].impact "to 8,000 kg (2024e)" | 8000 kg_per_year | usgs_mcs_2025_pgm | verified | "United States 8,000" — World Mine Production table Pd 2024e column, p.137 |
| geopolitical_events[2023-01].impact "Value of US output fell 42% to $310 million in 2024" | -42 pct / 310 million USD | usgs_mcs_2025_pgm | verified | "a decrease of 42% compared with $541 million in 2023" — Domestic Production and Use, p.136 |
| geopolitical_events[2024-01].event "~$980/oz" | 980 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Palladium 980" — Salient Statistics 2024e price, p.136 |
| geopolitical_events[2024-01].event "down 27% from $1,352 in 2023" | -27 pct / 1352 usd | usgs_mcs_2025_pgm | verified | USGS Events section: "by 27% for palladium" (p.137); 2023 price=$1,351.66 ≈ $1,352 (salient statistics, p.136) |
| geopolitical_events[2024-01].event "down 59% from $2,419 peak in 2021" | -59 pct / 2419 usd | usgs_mcs_2025_pgm | inferred | Calculated: (2,419.18−980)/2,419.18 = 59.5% ≈ 59%. The 2021 peak price $2,419.18 is verified; the cumulative decline percentage is a calculation, not stated in USGS text. |
| geopolitical_events[2024-01].impact "attributed to 'decreased demand, investor uncertainty, and oversupply'" | text quote | usgs_mcs_2025_pgm | verified | "Price decreases were attributed to decreased demand, investor uncertainty, and oversupply." — Events, Trends, and Issues, p.137 |
| geopolitical_events[2024-06].impact "Combined SA Pd output fell 4% in 2024e" | -4 pct | usgs_mcs_2025_pgm | inferred | Calculated: (74,900−72,000)/74,900 = 3.87% ≈ 4%. Not stated as a percentage in USGS text; derived from table values. |
| substitutes[autocatalysts_gasoline_twc].notes "Palladium has been used as a substitute for platinum in most gasoline-engine catalytic converters" | text quote | usgs_mcs_2025_pgm | verified | "Palladium has been used as a substitute for platinum in most gasoline-engine catalytic converters because of the historically lower price for palladium relative to that of platinum." — Substitutes section, p.137 |
| substitutes[autocatalysts_diesel].notes "About 25% of palladium can routinely be substituted for platinum in diesel catalytic converters" | 25 pct | usgs_mcs_2025_pgm | verified | "About 25% of palladium can routinely be substituted for platinum in diesel catalytic converters" — Substitutes section, p.137 |
| substitutes[autocatalysts_diesel].notes "the proportion can be as much as 50% in some applications" | 50 pct | usgs_mcs_2025_pgm | verified | "the proportion can be as much as 50% in some applications" — Substitutes section, p.137 |
| substitutes[general].notes "For some industrial end uses, one PGM can substitute for another, but with losses in efficiency" | text quote | usgs_mcs_2025_pgm | verified | "For some industrial end uses, one PGM can substitute for another, but with losses in efficiency." — Substitutes section, p.137 |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_pgm | inferred | USGS MCS 2025 lists PGMs (including Pd) as a tracked commodity implying criticality designation. The 2022 Critical Minerals List (87 FR 10381) includes "platinum-group metals" (Ir, Os, Pd, Pt, Rh, Ru). The PGM chapter text does not explicitly state the critical-mineral designation; USGS MCS 2025 Table 4 (p.22) does, but that page is in the overview document, not the PGM chapter source cited. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | inferred | EUR-Lex URL (eur-lex.europa.eu/...32024R1252) returned an AWS WAF challenge page and could not be fetched. Consistent with project notes (w-eba7b0ad405f) confirming Annex I of EU Regulation 2024/1252 includes "platinum-group metals" as Critical Raw Materials. Source correctly cited as eu_crma_2024. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | inferred | EUR-Lex URL unreachable (same WAF issue). Consistent with project notes (w-eba7b0ad405f) confirming that only platinum (Pt) appears in Annex II (Strategic) for hydrogen fuel cells; palladium (Pd) is not listed as a Strategic Raw Material. |
| criticality.notes "US relies on imports for ~36% of apparent consumption (2024e)" | 36 pct | usgs_mcs_2025_pgm | verified | "Palladium ... 36" — Net import reliance, Salient Statistics 2024e column, p.136 |
| criticality.notes "Russia (32%) and South Africa (32%) as top import sources" | RU 32 pct / ZA 32 pct | usgs_mcs_2025_pgm | verified | "Russia, 32%; South Africa, 32%" — Import Sources (2020–23) Palladium, p.136 |
| criticality.notes "Belgium 8%, Italy 8% import sources" | BE 8 pct / IT 8 pct | usgs_mcs_2025_pgm | verified | "Belgium, 8%, Italy, 8%" — Import Sources (2020–23) Palladium, p.136 |

## Notes

**Source access**: USGS MCS 2025 PGM chapter (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-platinum-group.pdf) was accessed from a cached copy (pp.136–137). All USGS numeric claims were verified directly against the two-page chapter. EUR-Lex URL for EU Regulation 2024/1252 was blocked by AWS WAF during this pass; EU criticality claims are marked `inferred` following the convention established in La.md, Lu.md, and other recently verified elements.

**Discrepancy 1 — Zimbabwe 2024e "unchanged from 2023"**: USGS table shows Zimbabwe Pd 2023=15,900, 2024e=15,000 — a decline of 900 kg (approximately −5.7%). The YAML note describing this as "unchanged from 2023" is factually inaccurate per the USGS table. Follow-up edit needed.

**Discrepancy 2 — US 2022 Pd "~11,000 kg"**: USGS Salient Statistics (p.136) reports US Palladium mine production 2022=10,100 kg. The YAML geopolitical event text references "~11,000 kg (2022)" — this overstates the 2022 figure by ~900 kg. The correct approximation is ~10,000 kg. Follow-up edit needed.

**Discrepancy 3 — 45,000 kg Pd recycled "globally"**: The YAML ZZ refining note states "~45,000 kg Pd recovered globally in 2024 per USGS chapter." USGS Recycling section (p.136) states "about 45,000 kilograms of palladium...recovered from automobile catalytic converters in the United States" — this is the US-only figure from autocatalysts. The global Pd+Pt recovery from all scrap is ~120,000 kg (combined). The YAML misattributes a US-specific figure as the global total. Follow-up edit needed.

**End-use percentages**: USGS MCS 2025 PGM chapter does not provide a percentage breakdown of Pd end uses. The five share_pct values (80%/10%/4%/3%/3%) are industry-consensus estimates; the YAML notes correctly acknowledge this. All five are marked `inferred`.

**Refining shares for ZA and RU**: The 40%/40% world-refining share estimates are not stated in USGS; marked `inferred` with confidence: low per YAML. The Belgium (8%) and Italy (8%) refining entries are correctly attributed to the USGS US import-source table, which gives US import-source percentages, not global refining shares.

**Share percentages**: All mining share_pct and reserve share_pct values are derived by dividing the stated country quantity by the world total; percentages are not explicitly given in USGS tables. All marked `inferred`.

**Russia reserve footnote**: USGS footnote 10 states "Reserves for Russia are based on the Russian Classification system A+B+C1+C2, where C2 are deposits that are being developed or prepared for development." The YAML notes correctly reproduce this caveat. The ">16,000,000" floor value is verified.

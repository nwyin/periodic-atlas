# Verification: Cd

- Element: cadmium (Cd)
- Snapshot year: 2025
- Verifier: worker-0b429b4b787b (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 58 |
| discrepancy | 0 |
| inferred | 26 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 300 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "One company operating in Tennessee recovered an estimated 300 tons of primary cadmium metal" — USGS MCS 2025 p.52 Domestic Production and Use; also table p.53 US 2024e column = 300 |
| production[0].refined.notes ($1.2 million value) | $1.2 million | usgs_mcs_2025_cadmium | verified | "300 tons of primary cadmium metal valued at $1.2 million" — USGS MCS 2025 p.52 |
| production[0].refining_by_country.shares[CN].quantity.value | 9,300 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "China … 9,300" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[CN].share_pct | 38.75 | usgs_mcs_2025_cadmium | inferred | Not stated; 9,300 / 24,000 = 38.75% (computed against published world total) |
| production[0].refining_by_country.shares[KR].quantity.value | 4,500 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Korea, Republic of … 4,500" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[KR].share_pct | 18.75 | usgs_mcs_2025_cadmium | inferred | Not stated; 4,500 / 24,000 = 18.75% |
| production[0].refining_by_country.shares[CA].quantity.value | 1,700 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Canada … 1,700" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[CA].share_pct | 7.08 | usgs_mcs_2025_cadmium | inferred | Not stated; 1,700 / 24,000 = 7.083% ≈ 7.08% |
| production[0].refining_by_country.shares[JP].quantity.value | 1,700 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Japan … 1,700" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[JP].share_pct | 7.08 | usgs_mcs_2025_cadmium | inferred | Not stated; 1,700 / 24,000 = 7.083% ≈ 7.08% |
| production[0].refining_by_country.shares[MX].quantity.value | 1,200 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Mexico … 1,200" (footnote 10: Reported) — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[MX].share_pct | 5.00 | usgs_mcs_2025_cadmium | inferred | Not stated; 1,200 / 24,000 = 5.00% |
| production[0].refining_by_country.shares[KZ].quantity.value | 1,000 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Kazakhstan … 1,000" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[KZ].share_pct | 4.17 | usgs_mcs_2025_cadmium | inferred | Not stated; 1,000 / 24,000 = 4.167% ≈ 4.17% |
| production[0].refining_by_country.shares[AU].quantity.value | 900 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Australia … 900" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[AU].share_pct | 3.75 | usgs_mcs_2025_cadmium | inferred | Not stated; 900 / 24,000 = 3.75% |
| production[0].refining_by_country.shares[RU].quantity.value | 800 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Russia … 800" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[RU].share_pct | 3.33 | usgs_mcs_2025_cadmium | inferred | Not stated; 800 / 24,000 = 3.333% ≈ 3.33% |
| production[0].refining_by_country.shares[PE].quantity.value | 620 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Peru … 620" (footnote 10: Reported) — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[PE].share_pct | 2.58 | usgs_mcs_2025_cadmium | inferred | Not stated; 620 / 24,000 = 2.583% ≈ 2.58% |
| production[0].refining_by_country.shares[NL].quantity.value | 400 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Netherlands … 400" (footnote 10: Reported) — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[NL].share_pct | 1.67 | usgs_mcs_2025_cadmium | inferred | Not stated; 400 / 24,000 = 1.667% ≈ 1.67% |
| production[0].refining_by_country.shares[NO].quantity.value | 350 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Norway … 350" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[NO].share_pct | 1.46 | usgs_mcs_2025_cadmium | inferred | Not stated; 350 / 24,000 = 1.458% ≈ 1.46% |
| production[0].refining_by_country.shares[BG].quantity.value | 300 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Bulgaria … 300" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[BG].share_pct | 1.25 | usgs_mcs_2025_cadmium | inferred | Not stated; 300 / 24,000 = 1.25% |
| production[0].refining_by_country.shares[US].quantity.value | 300 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "United States … 300" (footnote 10: Reported, footnote 1: byproduct of zinc refining) — USGS MCS 2025 p.53 table, 2024e column; also confirmed in text |
| production[0].refining_by_country.shares[US].share_pct | 1.25 | usgs_mcs_2025_cadmium | inferred | Not stated; 300 / 24,000 = 1.25% |
| production[0].refining_by_country.shares[PL].quantity.value | 250 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Poland … 250" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[PL].share_pct | 1.04 | usgs_mcs_2025_cadmium | inferred | Not stated; 250 / 24,000 = 1.042% ≈ 1.04% |
| production[0].refining_by_country.shares[UZ].quantity.value | 200 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Uzbekistan … 200" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[UZ].share_pct | 0.83 | usgs_mcs_2025_cadmium | inferred | Not stated; 200 / 24,000 = 0.833% ≈ 0.83% |
| production[0].refining_by_country.shares[DE].quantity.value | 170 tonnes_per_year | usgs_mcs_2025_cadmium | verified | "Germany … 170" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| production[0].refining_by_country.shares[DE].notes (zero in 2023) | — (zero) | usgs_mcs_2025_cadmium | verified | "Germany … —" — USGS MCS 2025 p.53 World Refinery Production table, 2023 column |
| production[0].refining_by_country.shares[DE].share_pct | 0.71 | usgs_mcs_2025_cadmium | inferred | Not stated; 170 / 24,000 = 0.708% ≈ 0.71% |
| production[0].refining_by_country.shares[ZZ].quantity.value | 310 tonnes_per_year | usgs_mcs_2025_cadmium | inferred | Not stated; world total 24,000 minus sum of named countries (9300+4500+1700+1700+1200+1000+900+800+620+400+350+300+300+250+200+170 = 23,690) = 310 |
| production[0].refining_by_country.shares[ZZ].share_pct | 1.29 | usgs_mcs_2025_cadmium | inferred | Not stated; 310 / 24,000 = 1.292% ≈ 1.29% |
| production[0].notes (world refinery total 24,000 t) | 24,000 | usgs_mcs_2025_cadmium | verified | "World total (rounded) … 24,000" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| reserves.notes (no quantitative estimates available) | no quantitative estimates | usgs_mcs_2025_cadmium | verified | "Quantitative estimates of reserves were not available. The cadmium content of typical zinc ores averages about 0.03%. See the Zinc chapter for zinc reserves." — USGS MCS 2025 p.53 Reserves column |
| reserves.notes (0.03% cadmium in zinc ores) | 0.03% | usgs_mcs_2025_cadmium | verified | "The cadmium content of typical zinc ores averages about 0.03%" — USGS MCS 2025 p.53 Reserves column and World Resources paragraph |
| feedstock_origins[sphalerite_zinc_ore].typical_concentration_pct | 0.03 | usgs_mcs_2025_cadmium | verified | "The cadmium content of typical zinc ores averages about 0.03%" — USGS MCS 2025 p.53 World Resources |
| feedstock_origins[zinc_roaster_flue_dust].notes (Tennessee zinc smelter) | Tennessee, only domestic zinc smelter | usgs_mcs_2025_cadmium | verified | "byproduct of zinc leaching from roasted sulfide concentrates at the only domestic zinc smelter" — USGS MCS 2025 p.52 |
| feedstock_origins[nickel_cadmium_battery_scrap].notes (Ohio NiCd shutdown 2024) | Ohio company shut NiCd line, 2024 | usgs_mcs_2025_cadmium | verified | "In 2024, with a shift in focus to lithium-ion battery recycling, a company in Ohio that had been recovering secondary cadmium metal shut down its nickel cadmium (NiCd) battery recycling line" — USGS MCS 2025 p.52 |
| feedstock_origins[nickel_cadmium_battery_scrap].notes (Ohio company est. 2022) | Ohio company established 2022 | usgs_mcs_2025_cadmium | verified | "Another battery recycling company, established in Ohio in 2022, processed both consumer and industrial NiCd batteries for salable metals and was recovering cadmium metal in 2024" — USGS MCS 2025 p.52 |
| substitutes[nickel_cadmium_batteries].notes (lithium-ion) | lithium-ion can replace NiCd | usgs_mcs_2025_cadmium | verified | "Batteries with other chemistries, particularly lithium-ion, can replace NiCd batteries in many applications" — USGS MCS 2025 p.53 Substitutes |
| substitutes[coatings_and_plating].notes (zinc-nickel, fasteners for aircraft) | zinc-nickel coating substitute, except aircraft fasteners | usgs_mcs_2025_cadmium | verified | "Except where the surface characteristics of a coating are critical (for example, fasteners for aircraft), coatings such as zinc-nickel can be substituted for cadmium in many plating applications" — USGS MCS 2025 p.53 Substitutes |
| substitutes[pigments].notes (cerium sulfide, plastics) | cerium sulfide for cadmium pigments in plastics | usgs_mcs_2025_cadmium | verified | "Cerium sulfide is used as a replacement for cadmium pigments, mostly in plastics" — USGS MCS 2025 p.53 Substitutes |
| substitutes[pvc_stabilizers].notes (barium stabilizers, flexible PVC) | barium stabilizers for barium-cadmium stabilizers | usgs_mcs_2025_cadmium | verified | "Barium stabilizers can replace barium-cadmium stabilizers in flexible polyvinyl chloride (PVC) applications" — USGS MCS 2025 p.53 Substitutes |
| substitutes[cdte_solar_and_semiconductors].notes (CIGS/perovskite not commercially feasible) | CIGS and perovskite investigated but not commercially feasible | usgs_mcs_2025_cadmium | verified | "Thin-film technologies based on copper-indium-gallium-selenide and perovskite materials continued to be investigated but were not yet commercially feasible" — USGS MCS 2025 p.53 Substitutes |
| end_uses.uses[nickel_cadmium_batteries].share_pct | 73 | usgs_mcs_2025_cadmium | inferred | Not stated as a percentage; USGS MCS 2025 says only "mainly consumed for NiCd batteries" — 73% is consistent with international industry data but not directly quoted from this source |
| end_uses.uses[nickel_cadmium_batteries].notes (>11,400 t India imports 2023) | >11,400 t | usgs_mcs_2025_cadmium | verified | "more than 11,400 tons were imported in 2023" (India) — USGS MCS 2025 p.52 Events |
| end_uses.uses[nickel_cadmium_batteries].notes (~6,000 t India Aug 2024) | ~6,000 t | usgs_mcs_2025_cadmium | verified | "almost 6,000 tons as of August 2024" (India) — USGS MCS 2025 p.52–53 Events |
| end_uses.uses[pigments].share_pct | 10 | usgs_mcs_2025_cadmium | inferred | Not stated; pigments listed as secondary end use without quantified share |
| end_uses.uses[pigments].notes (~500 t exports 2024e) | ~500 t | usgs_mcs_2025_cadmium | verified | "Exports … Cadmium pigments and preparations … 500" — USGS MCS 2025 p.52 Salient Statistics, 2024e column |
| end_uses.uses[pigments].notes (~120 t imports 2024e) | ~120 t | usgs_mcs_2025_cadmium | verified | "Imports … Cadmium pigments and preparations based on cadmium compounds … 120" — USGS MCS 2025 p.52 Salient Statistics, 2024e column |
| end_uses.uses[coatings_and_plating].share_pct | 9 | usgs_mcs_2025_cadmium | inferred | Not stated; coatings listed as secondary end use without quantified share |
| end_uses.uses[alloys].share_pct | 4 | usgs_mcs_2025_cadmium | inferred | Not stated; alloys listed as secondary end use without quantified share |
| end_uses.uses[cdte_solar_and_semiconductors].share_pct | 4 | usgs_mcs_2025_cadmium | inferred | Not stated; CdTe/CdZnTe described as "increasing use" without quantified share |
| end_uses.uses[cdte_solar_and_semiconductors].notes (~11 GW/year, Alabama facility) | ~11 GW/year | usgs_mcs_2025_cadmium | verified | "increased manufacturing capacity to almost 11 gigawatts (GW) per year" — USGS MCS 2025 p.53 Events |
| end_uses.uses[cdte_solar_and_semiconductors].notes (5th Louisiana 3.5 GW/year H2 2025) | 3.5 GW/year | usgs_mcs_2025_cadmium | verified | "A fifth site was under construction in Louisiana and was expected to add another 3.5 GW per year in the second half of 2025" — USGS MCS 2025 p.53 Events |
| end_uses.uses[cdte_solar_and_semiconductors].notes (~21 GW/year worldwide) | ~21 GW/year | usgs_mcs_2025_cadmium | verified | "Worldwide, capacity was about 21 GW per year" — USGS MCS 2025 p.53 Events |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_cadmium | inferred | Not stated explicitly; cadmium is not mentioned as critical in this chapter; US 2022 Critical Minerals List does not include cadmium (inference by absence) |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_cadmium | inferred | Not stated; cadmium absent from EU CRM list (inference by absence of designation) |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_cadmium | inferred | Not stated; cadmium absent from EU SRMA strategic list (inference by absence of designation) |
| criticality.notes (2,800 sq cm CdZnTe FY2025 target) | 2,800 sq cm | usgs_mcs_2025_cadmium | verified | "The fiscal year (FY) 2025 potential acquisitions include 2,800 square centimeters of CdZnTe substrates" — USGS MCS 2025 p.52 Government Stockpile |
| criticality.notes (180% increase from FY2024) | 180% | usgs_mcs_2025_cadmium | verified | "a 180% increase from 1,000 square centimeters in FY 2024" — USGS MCS 2025 p.52 Government Stockpile |
| prices[2024].value | 4.10 USD/kg | usgs_mcs_2025_cadmium | verified | "4.1" — USGS MCS 2025 p.52 Salient Statistics, Price row, 2024e column (Fastmarkets MB, CIF global ports, 99.95% purity, 10-ton lots) |
| prices[2023].value | 4.06 USD/kg | usgs_mcs_2025_cadmium | verified | "4.06" — USGS MCS 2025 p.52 Salient Statistics, Price row, 2023 column |
| prices[2022].value | 3.42 USD/kg | usgs_mcs_2025_cadmium | verified | "3.42" — USGS MCS 2025 p.52 Salient Statistics, Price row, 2022 column |
| prices[2021].value | 2.56 USD/kg | usgs_mcs_2025_cadmium | verified | "2.56" — USGS MCS 2025 p.52 Salient Statistics, Price row, 2021 column |
| prices[2020].value | 2.29 USD/kg | usgs_mcs_2025_cadmium | verified | "2.29" — USGS MCS 2025 p.52 Salient Statistics, Price row, 2020 column |
| prices[2024].notes (seasonal India buying patterns) | seasonal buying patterns in India | usgs_mcs_2025_cadmium | verified | "Average prices for cadmium decreased midyear, reflecting the seasonal buying patterns in India" — USGS MCS 2025 p.52 Events |
| prices[2024].notes (ended year higher than January) | ended year higher than January | usgs_mcs_2025_cadmium | verified | "ended the year higher than those in January" — USGS MCS 2025 p.52 Events |
| prices[2024].notes (net exporter second consecutive year) | net exporter second consecutive year | usgs_mcs_2025_cadmium | verified | "For the second consecutive year, the United States was a net exporter of cadmium" — USGS MCS 2025 p.52 Events |
| geopolitical_events[US net exporter] (second consecutive year) | US net exporter second consecutive year | usgs_mcs_2025_cadmium | verified | "For the second consecutive year, the United States was a net exporter of cadmium" — USGS MCS 2025 p.52 Events |
| geopolitical_events[US net exporter].impact (375 t primary production 2023) | 375 t | usgs_mcs_2025_cadmium | verified | "United States … 375" — USGS MCS 2025 p.53 World Refinery Production table, 2023 column |
| geopolitical_events[US net exporter].impact (300 t primary production 2024e) | 300 t | usgs_mcs_2025_cadmium | verified | "United States … 300" — USGS MCS 2025 p.53 World Refinery Production table, 2024e column |
| geopolitical_events[US net exporter].impact (282 t unwrought imports 2020) | 282 t | usgs_mcs_2025_cadmium | verified | "Imports for consumption: Unwrought cadmium and powders … 282" — USGS MCS 2025 p.52 Salient Statistics, 2020 column |
| geopolitical_events[US net exporter].impact (7 t unwrought imports 2024e) | 7 t | usgs_mcs_2025_cadmium | verified | "Imports for consumption: Unwrought cadmium and powders … 7" — USGS MCS 2025 p.52 Salient Statistics, 2024e column |
| geopolitical_events[US net exporter].impact (100 t unwrought exports 2023) | 100 t | usgs_mcs_2025_cadmium | verified | "Exports: Unwrought cadmium and powders … 100" — USGS MCS 2025 p.52 Salient Statistics, 2023 column |
| geopolitical_events[US net exporter].impact (20 t unwrought exports 2024e) | 20 t | usgs_mcs_2025_cadmium | verified | "Exports: Unwrought cadmium and powders … 20" — USGS MCS 2025 p.52 Salient Statistics, 2024e column |
| geopolitical_events[China replaces India].impact (>11,400 t India imports 2023) | >11,400 t | usgs_mcs_2025_cadmium | verified | "more than 11,400 tons were imported in 2023" — USGS MCS 2025 p.52–53 Events |
| geopolitical_events[China replaces India].impact (~6,000 t India Aug 2024) | ~6,000 t | usgs_mcs_2025_cadmium | verified | "almost 6,000 tons as of August 2024" — USGS MCS 2025 p.52–53 Events |
| geopolitical_events[China replaces India] (China replaced India 2024) | China replaced India as leading consumer, 2024 | usgs_mcs_2025_cadmium | verified | "China replaced India as the leading consumer of cadmium in 2024" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama] (Q3 2024 commercial production) | Q3 2024 | usgs_mcs_2025_cadmium | verified | "began commercial production in the third quarter of 2024" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama] (fourth facility, Alabama) | fourth facility, Alabama | usgs_mcs_2025_cadmium | verified | "at a fourth facility, located in Alabama" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama].impact (~11 GW/year US capacity) | ~11 GW/year | usgs_mcs_2025_cadmium | verified | "increased manufacturing capacity to almost 11 gigawatts (GW) per year" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama].impact (fifth site Louisiana, H2 2025) | fifth site Louisiana, H2 2025 | usgs_mcs_2025_cadmium | verified | "A fifth site was under construction in Louisiana and was expected to add another 3.5 GW per year in the second half of 2025" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama].impact (3.5 GW/year addition) | 3.5 GW/year | usgs_mcs_2025_cadmium | verified | "add another 3.5 GW per year" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama].impact (~21 GW/year worldwide) | ~21 GW/year | usgs_mcs_2025_cadmium | verified | "Worldwide, capacity was about 21 GW per year" — USGS MCS 2025 p.53 Events |
| geopolitical_events[CdTe Alabama].impact (facility in India opened early 2024) | facility in India, early 2024 | usgs_mcs_2025_cadmium | verified | "including a facility in India that opened in early 2024" — USGS MCS 2025 p.53 Events |
| geopolitical_events[NREL $1.8M].impact ($1.8 million second-round contracts) | $1.8 million | usgs_mcs_2025_cadmium | verified | "$1.8 million had been awarded in a second round of contracts to support development of CdTe solar cells" — USGS MCS 2025 p.53 Events |
| geopolitical_events[NREL $1.8M].impact (3-year CdTe Photovoltaics Accelerator Program) | 3-year program | usgs_mcs_2025_cadmium | verified | "administrator of the 3-year Cadmium Telluride Photovoltaics Accelerator Program" — USGS MCS 2025 p.53 Events |
| geopolitical_events[NREL $1.8M] date (January 2024) | 2024-01 | usgs_mcs_2025_cadmium | verified | "In January, the National Renewable Energy Laboratory … announced that $1.8 million had been awarded" — USGS MCS 2025 p.53 Events |
| geopolitical_events[stockpile] (FY2025 target 2,800 sq cm CdZnTe) | 2,800 sq cm | usgs_mcs_2025_cadmium | verified | "The fiscal year (FY) 2025 potential acquisitions include 2,800 square centimeters of CdZnTe substrates" — USGS MCS 2025 p.52 Government Stockpile |
| geopolitical_events[stockpile] (180% increase from FY2024) | 180% | usgs_mcs_2025_cadmium | verified | "a 180% increase from 1,000 square centimeters in FY 2024" — USGS MCS 2025 p.52 Government Stockpile |
| geopolitical_events[stockpile] (FY2024 baseline 1,000 sq cm) | 1,000 sq cm | usgs_mcs_2025_cadmium | verified | "from 1,000 square centimeters in FY 2024" — USGS MCS 2025 p.52 Government Stockpile |
| geopolitical_events[Ohio NiCd shutdown] (Ohio company shut down NiCd line) | Ohio company shut NiCd recycling line, 2024 | usgs_mcs_2025_cadmium | verified | "In 2024, with a shift in focus to lithium-ion battery recycling, a company in Ohio that had been recovering secondary cadmium metal shut down its nickel cadmium (NiCd) battery recycling line" — USGS MCS 2025 p.52 |
| geopolitical_events[Ohio NiCd shutdown].impact (separate Ohio company est. 2022 continuing) | Ohio company established 2022, continuing NiCd and planning refine to battery-grade | usgs_mcs_2025_cadmium | verified | "Another battery recycling company, established in Ohio in 2022, processed both consumer and industrial NiCd batteries for salable metals and was recovering cadmium metal in 2024 and planned to refine it to battery-grade purity" — USGS MCS 2025 p.52 |

## Notes

**No discrepancies found.** All numeric claims in Cd.yaml that were directly verifiable against the USGS MCS 2025 cadmium chapter (pp.52–53) were confirmed. Key observations:

1. **Price formatting**: The YAML records the 2024e price as `4.10` USD/kg; the PDF salient statistics table shows `4.1`. These are numerically identical — no discrepancy.

2. **World total 24,000 t**: The 2024e world refinery production total is listed as "24,000 (rounded)" in the PDF. The 2023 total was 24,100. YAML correctly uses 24,000 as the basis for share_pct calculations and marks all shares as inferred.

3. **Footnote 10 (Reported)**: USGS MCS 2025 footnote 10 designates US, Mexico, Netherlands, and Peru as "Reported" (not estimated). The YAML correctly flags these four countries as approximate: false with noted reporting status.

4. **End-use shares unquantified**: USGS MCS 2025 does not provide explicit percentage breakdowns for cadmium end uses. The share values (73% NiCd, 10% pigments, 9% coatings, 4% alloys, 4% CdTe) are all inferred from industry sources not cited in this chapter; YAML confidence is correctly set to `low` for all end-use shares.

5. **Criticality flags**: No explicit statement of non-criticality appears in the USGS cadmium chapter; the `false` values for criticality flags are inferred from absence of designation, consistent with verification of other elements.

6. **Price basis confirmed**: Footnote 4 confirms: "Average free market price for 99.95% purity in 10-ton lots; cost, insurance, and freight; global ports. Source: Fastmarkets MB." The YAML `basis: other` with appropriate explanatory notes is correct.

7. **Germany 2023 = zero**: The PDF table shows "—" (zero) for Germany in the 2023 column. The YAML notes "(zero in 2023)" is confirmed.

8. **ZZ residual**: Named countries sum to 23,690 t; the residual "other countries" quantity of 310 t is arithmetically derived from the rounded world total of 24,000 t and is correctly labeled inferred.

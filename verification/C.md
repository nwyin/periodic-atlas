# Verification: C

- Element: carbon (C)
- Snapshot year: 2025
- Verifier: worker-85f084ccb5b3 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 42 |
| discrepancy | 1 |
| inferred | 19 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 9241.5 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Total World ... 9241.5 ... 0.9% ... 100.0%"` — EI Statistical Review 2025, Coal Production table, p.48 |
| production[0].mine.notes | 0.9% year over year | energy_institute_statistical_review_2025 | verified | `"Total World ... 9241.5 0.9% ..."` — EI Coal Production table, p.48 |
| production[0].mining_by_country[CN].quantity.value | 4780.0 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"China ... 4780.0 ... 51.7%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[CN].share_pct | 51.7 | energy_institute_statistical_review_2025 | verified | `"China ... 4780.0 ... 51.7%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[IN].quantity.value | 1085.1 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"India ... 1085.1 7.0% ... 11.7%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[IN].share_pct | 11.7 | energy_institute_statistical_review_2025 | verified | `"India ... 1085.1 7.0% ... 11.7%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[IN].notes | 7.0% output rise in 2024 | energy_institute_statistical_review_2025 | verified | `"India ... 1085.1 7.0% ... 11.7%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ID].quantity.value | 836.1 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Indonesia ... 836.1 7.6% ... 9.0%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ID].share_pct | 9.0 | energy_institute_statistical_review_2025 | verified | `"Indonesia ... 836.1 7.6% ... 9.0%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ID].notes | surpassed 800 Mt for the first time | energy_institute_statistical_review_2025 | inferred | EI table shows Indonesia at `775.2` in 2023 and `836.1` in 2024, so exceeding 800 Mt is supported by the table; "for the first time" is inferred from the 2014-2024 series shown. |
| production[0].mining_by_country[AU].quantity.value | 462.9 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Australia ... 462.9 ... 5.0%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[AU].share_pct | 5.0 | energy_institute_statistical_review_2025 | verified | `"Australia ... 462.9 ... 5.0%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[US].quantity.value | 464.6 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"US ... 464.6 -13.3% -4.2% 5.0%"` — EI Coal Production table, p.47-48 |
| production[0].mining_by_country[US].share_pct | 5.0 | energy_institute_statistical_review_2025 | verified | `"US ... 464.6 ... 5.0%"` — EI Coal Production table, p.47-48 |
| production[0].mining_by_country[US].notes | lowest level in more than four decades | energy_institute_statistical_review_2025 | discrepancy | The cited EI PDF table exposes coal production back to 2014 on the printed page and does not substantiate a four-decade comparison from the cited document alone. |
| production[0].mining_by_country[RU].quantity.value | 427.2 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Russian Federation ... 427.2 -1.1% ... 4.6%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[RU].share_pct | 4.6 | energy_institute_statistical_review_2025 | verified | `"Russian Federation ... 427.2 ... 4.6%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ZA].quantity.value | 235.0 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"South Africa ... 235.0 0.3% ... 2.5%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ZA].share_pct | 2.5 | energy_institute_statistical_review_2025 | verified | `"South Africa ... 235.0 ... 2.5%"` — EI Coal Production table, p.48 |
| production[0].mining_by_country[ZZ].share_pct | 10.5 | energy_institute_statistical_review_2025 | inferred | Not printed as a rest-of-world share in YAML's shape; `100 - (51.7 + 11.7 + 9.0 + 5.0 + 5.0 + 4.6 + 2.5) = 10.5%`. |
| production[1].mine.value | 4543 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Total World ... 4543 ... 0.6% ... 100.0%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[US].quantity.value | 858 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"US ... 858 3.1% 5.1% 18.9%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[US].share_pct | 18.9 | energy_institute_statistical_review_2025 | verified | `"US ... 858 ... 18.9%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[RU].quantity.value | 526 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Russian Federation ... 526 -3.1% -0.2% 11.6%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[RU].share_pct | 11.6 | energy_institute_statistical_review_2025 | verified | `"Russian Federation ... 526 ... 11.6%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[SA].quantity.value | 510 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Saudi Arabia ... 510 -3.8% -0.6% 11.2%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[SA].share_pct | 11.2 | energy_institute_statistical_review_2025 | verified | `"Saudi Arabia ... 510 ... 11.2%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[CA].quantity.value | 290 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Canada ... 290 4.1% 3.3% 6.4%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[CA].share_pct | 6.4 | energy_institute_statistical_review_2025 | verified | `"Canada ... 290 ... 6.4%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[IR].quantity.value | 234 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Iran ... 234 10.7% 3.0% 5.2%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[IR].share_pct | 5.2 | energy_institute_statistical_review_2025 | verified | `"Iran ... 234 ... 5.2%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[IQ].quantity.value | 216 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Iraq ... 216 0.9% 3.1% 4.7%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[IQ].share_pct | 4.7 | energy_institute_statistical_review_2025 | verified | `"Iraq ... 216 ... 4.7%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[CN].quantity.value | 213 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"China ... 213 -0.5% -2.0% 4.7%"` — EI Oil Production table, p.22-23 |
| production[1].mining_by_country[CN].share_pct | 4.7 | energy_institute_statistical_review_2025 | verified | `"China ... 213 ... 4.7%"` — EI Oil Production table, p.22-23 |
| production[1].mining_by_country[BR].quantity.value | 182 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"Brazil ... 182 -1.1% 4.0% 4.0%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[BR].share_pct | 4.0 | energy_institute_statistical_review_2025 | verified | `"Brazil ... 182 ... 4.0%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[AE].quantity.value | 180 million_tonnes_per_year | energy_institute_statistical_review_2025 | verified | `"United Arab Emirates ... 180 -0.5% 1.0% 4.0%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[AE].share_pct | 4.0 | energy_institute_statistical_review_2025 | verified | `"United Arab Emirates ... 180 ... 4.0%"` — EI Oil Production table, p.23 |
| production[1].mining_by_country[ZZ].share_pct | 29.3 | energy_institute_statistical_review_2025 | inferred | Not printed as a YAML rest-of-world share; `100 - (18.9 + 11.6 + 11.2 + 6.4 + 5.2 + 4.7 + 4.7 + 4.0 + 4.0) = 29.3%`. |
| production[2].mine.value | 4124500 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"Total World ... 4124.5 ... 100.0%"` in billion cubic metres; YAML converts 4,124.5 bcm to 4,124,500 million m3/year. |
| production[2].mine.notes | 4124.5 billion cubic metres | energy_institute_statistical_review_2025 | verified | `"Total World ... 4124.5 1.2% 1.8% 100.0%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[US].quantity.value | 1033000 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"US ... 1033.0 ... 25.0%"` in bcm; YAML converts 1,033.0 bcm to 1,033,000 million m3/year. |
| production[2].mining_by_country[US].share_pct | 25.0 | energy_institute_statistical_review_2025 | verified | `"US ... 1033.0 -0.3% 3.9% 25.0%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[RU].quantity.value | 629900 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"Russian Federation ... 629.9 7.1% 0.6% 15.3%"` in bcm; YAML converts to million m3/year. |
| production[2].mining_by_country[RU].share_pct | 15.3 | energy_institute_statistical_review_2025 | verified | `"Russian Federation ... 629.9 ... 15.3%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[IR].quantity.value | 262900 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"Iran ... 262.9 0.9% 4.1% 6.4%"` in bcm; YAML converts to million m3/year. |
| production[2].mining_by_country[IR].share_pct | 6.4 | energy_institute_statistical_review_2025 | verified | `"Iran ... 262.9 ... 6.4%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[CN].quantity.value | 248400 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"China ... 248.4 5.7% 6.6% 6.0%"` in bcm; YAML converts to million m3/year. |
| production[2].mining_by_country[CN].share_pct | 6.0 | energy_institute_statistical_review_2025 | verified | `"China ... 248.4 ... 6.0%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[CA].quantity.value | 194200 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"Canada ... 194.2 2.0% 2.0% 4.7%"` in bcm; YAML converts to million m3/year. |
| production[2].mining_by_country[CA].share_pct | 4.7 | energy_institute_statistical_review_2025 | verified | `"Canada ... 194.2 ... 4.7%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[QA].quantity.value | 179500 million_m3_per_year | energy_institute_statistical_review_2025 | inferred | EI reports `"Qatar ... 179.5 -1.1% 0.6% 4.4%"` in bcm; YAML converts to million m3/year. |
| production[2].mining_by_country[QA].share_pct | 4.4 | energy_institute_statistical_review_2025 | verified | `"Qatar ... 179.5 ... 4.4%"` — EI Natural gas Production table, p.38 |
| production[2].mining_by_country[ZZ].share_pct | 38.2 | energy_institute_statistical_review_2025 | inferred | Not printed as a YAML rest-of-world share; `100 - (25.0 + 15.3 + 6.4 + 6.0 + 4.7 + 4.4) = 38.2%`. |
| end_uses.uses[electricity_generation_and_heat].share_pct | 38 | iea_coal_2024 | inferred | The cited IEA source says `"the power sector has been the main driver of coal demand growth"` and coal-fired generation reaches `"10 700"` TWh in 2024, but it does not publish a unified carbon end-use share of 38%. |
| end_uses.uses[transport_fuels].share_pct | 31 | iea_global_energy_review_2025_oil | inferred | The cited IEA oil chapter says non-feedstock oil uses remain `"dominated by transport applications in road, aviation and shipping"`, but it does not publish a 31% cross-stream carbon share. |
| end_uses.uses[industrial_process_heat_and_reducing_agent].share_pct | 15 | iea_global_energy_review_2025_key_findings | inferred | IEA says gas demand in the EU grew `"notably for industrial use"` and electricity growth was driven partly by `"growing consumption by industry"`, but no 15% all-carbon end-use split is given. |
| end_uses.uses[petrochemicals_and_non_combusted_feedstocks].share_pct | 10 | iea_global_energy_review_2025_oil | inferred | IEA says `"chemical feedstocks and aviation each accounted for around half of oil demand growth"` and feedstocks rose `"over 12%"` since 2019, but it does not state a 10% aggregate carbon share. |
| end_uses.uses[buildings_heating_and_cooking].share_pct | 6 | iea_global_energy_review_2025_key_findings | inferred | IEA says `"Electricity use in buildings accounted for nearly 60% of overall growth in 2024"` and highlights heat pumps, but it does not state a 6% carbon end-use share. |
| prices[Northwest Europe thermal coal CIF ARA][2022].value | 291.28 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2022 ... 291.28` under `Northwest Europe`. Footnote 3 specifies `Thermal Coal CIF ARA 6,000 kcal/kg NAR`, p.51. |
| prices[Northwest Europe thermal coal CIF ARA][2023].value | 129.54 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2023 ... 129.54` under `Northwest Europe`, p.51. |
| prices[Northwest Europe thermal coal CIF ARA][2024].value | 112.00 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2024 ... 112.00` under `Northwest Europe`, p.51. |
| prices[Australia Newcastle thermal coal FOB][2022].value | 174.49 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2022 ... 174.49` under `Australia`; footnote 8 specifies `FOB Newcastle High Ash 5500 kcal/kg NAR`, p.51. |
| prices[Australia Newcastle thermal coal FOB][2023].value | 103.59 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2023 ... 103.59` under `Australia`, p.51. |
| prices[Australia Newcastle thermal coal FOB][2024].value | 89.41 usd_per_tonne | energy_institute_statistical_review_2025 | verified | EI mined energy resource prices table shows `2024 ... 89.41` under `Australia`, p.51. |
| geopolitical_events[2024-06-02].date | 2024-06-02 | opec_press_release_2024_06_02 | verified | On OPEC's current press-release page for the 2 June 2024 meeting, the group says the 1.65 mb/d cuts were extended `"until the end of December 2025"` and the 2.2 mb/d cuts would be `"gradually phased out ... until the end of September 2025"`, matching the YAML event dated 2024-06-02. |
| geopolitical_events[2024-09].date | 2024-09 | iea_coal_2024 | verified | The Coal 2024 PDF says `"The closure of the last coal power plant in the United Kingdom in September 2024"` — p.7. |
| geopolitical_events[2024].date | 2024 | iea_coal_2024 | verified | Coal 2024 says Russian producers were `"struggling amid international sanctions, low profitability and infrastructure bottlenecks"` and the trade chapter says the reshuffle continued `"more than two years after"` the EU ban, supporting the 2024 event framing. |
| feedstock_origins[natural_gas_reservoirs].notes | 15°C; 1013 mbar; 40 MJ/m3 | energy_institute_statistical_review_2025 | verified | The natural-gas methodology note states production is standardized to `"15°C and 1013 mbar"` using `"a gross calorific value of 40 MJ/m3"` — EI Statistical Review 2025 methodology / gas notes. |
| substitutes[energy_services].notes | 2.6 billion tonnes CO2 annually; 7% of global emissions | iea_global_energy_review_2025_key_findings | verified | IEA key findings: `"solar PV, wind, nuclear, electric cars and heat pumps since 2019 now prevents 2.6 billion tonnes of CO2 annually, the equivalent of 7% of global emissions."` |

## Notes

No `reserves` section is present in [elements/C.yaml](/Users/tau/projects/egotheism/inquiries/material-world/atlas/.worktrees/worker-85f084ccb5b3/elements/C.yaml), so there were no reserve totals or reserve-share numeric claims to verify for carbon in this pass.

Most production quantities were directly supported by the Energy Institute tables. The main inferred class comes from YAML conversions of natural-gas values from `billion cubic metres` in the source to `million_m3_per_year` in schema form, plus rest-of-world shares computed as the remainder to 100%.

The only clear source mismatch is the coal note claiming US output fell to its lowest level in more than four decades. The cited EI PDF page does not provide the multi-decade comparison needed to verify that statement from the cited document alone.

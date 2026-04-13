# Verification: Nb

- Element: niobium (Nb)
- Snapshot year: 2025
- Verifier: worker-b45452ef83ff (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 22 |
| discrepancy | 0 |
| inferred | 12 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 110000 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"World total (rounded) 110,000 110,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mine.notes (2023 world total; last significant US mine production; Brazil and Canada shares) | 2023=110000; 1959; BR≈92%; CA≈7% | usgs_mcs_2025_niobium | verified | `"Significant U.S. niobium mine production has not been reported since 1959."` and `"Brazil continued to be the world’s leading niobium producer, accounting for approximately 92% of global production, followed by Canada with about 7%."` — USGS MCS 2025 pp.126-127 |
| production[0].mining_by_country[BR].quantity.value | 100000 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Brazil 102,000 100,000 16,000,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[BR].share_pct | 90.91 | usgs_mcs_2025_niobium | inferred | Source states Brazil was `"approximately 92%"`; YAML exact share is computed from table values: 100000/110000 = 90.91% |
| production[0].mining_by_country[CA].quantity.value | 7100 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Canada 6,700 7,100 1,600,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[CA].share_pct | 6.45 | usgs_mcs_2025_niobium | inferred | Source states Canada had `"about 7%"`; YAML exact share is computed from table values: 7100/110000 = 6.45% |
| production[0].mining_by_country[CD].quantity.value | 700 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Congo (Kinshasa) 740 700 NA"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[CD].share_pct | 0.64 | usgs_mcs_2025_niobium | inferred | Not stated directly; 700/110000 = 0.64% from the USGS table values |
| production[0].mining_by_country[RU].quantity.value | 350 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Russia 353 350 NA"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[RU].share_pct | 0.32 | usgs_mcs_2025_niobium | inferred | Not stated directly; 350/110000 = 0.32% from the USGS table values |
| production[0].mining_by_country[RW].quantity.value | 200 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Rwanda 210 200 NA"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[RW].share_pct | 0.18 | usgs_mcs_2025_niobium | inferred | Not stated directly; 200/110000 = 0.18% from the USGS table values |
| production[0].mining_by_country[ZZ].quantity.value | 120 tonnes_per_year | usgs_mcs_2025_niobium | verified | `"Other countries 121 120 NA"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| production[0].mining_by_country[ZZ].share_pct | 0.11 | usgs_mcs_2025_niobium | inferred | Not stated directly; 120/110000 = 0.11% from the USGS table values |
| production[0].notes (named-country sum and share) | 108470 tonnes_per_year; 98.6% | usgs_mcs_2025_niobium | inferred | Not stated directly; 100000+7100+700+350+200+120 = 108470, and 108470/110000 = 98.6% |
| reserves.economic_reserves.value | 17000000 tonnes | usgs_mcs_2025_niobium | verified | `"World total (rounded) 110,000 110,000 >17,000,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table. YAML correctly treats this as an approximate lower bound. |
| reserves.reserves_by_country[BR].quantity.value | 16000000 tonnes | usgs_mcs_2025_niobium | verified | `"Brazil 102,000 100,000 16,000,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| reserves.reserves_by_country[BR].share_pct | 89.84 | usgs_mcs_2025_niobium | inferred | Not stated directly; YAML uses quantified-country denominator 17,810,000 t, so 16000000/17810000 = 89.84% |
| reserves.reserves_by_country[CA].quantity.value | 1600000 tonnes | usgs_mcs_2025_niobium | verified | `"Canada 6,700 7,100 1,600,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| reserves.reserves_by_country[CA].share_pct | 8.98 | usgs_mcs_2025_niobium | inferred | Not stated directly; YAML uses quantified-country denominator 17,810,000 t, so 1600000/17810000 = 8.98% |
| reserves.reserves_by_country[US].quantity.value | 210000 tonnes | usgs_mcs_2025_niobium | verified | `"United States — — 210,000"` — USGS MCS 2025 p.127 World Mine Production and Reserves table |
| reserves.reserves_by_country[US].share_pct | 1.18 | usgs_mcs_2025_niobium | inferred | Not stated directly; YAML uses quantified-country denominator 17,810,000 t, so 210000/17810000 = 1.18% |
| reserves.notes (quantified-country reserve sum) | 17810000 tonnes | usgs_mcs_2025_niobium | inferred | Not stated directly; 16000000 + 1600000 + 210000 = 17,810,000 t, which exceeds the source’s lower-bound world total `>17,000,000` |
| end_uses.uses[steels].share_pct | 77% | usgs_mcs_2025_niobium | verified | `"Major end-use distribution of domestic niobium consumption was estimated as follows: steels, about 77%, and superalloys, about 21%."` — USGS MCS 2025 p.126 |
| end_uses.uses[superalloys].share_pct | 21% | usgs_mcs_2025_niobium | verified | `"Major end-use distribution of domestic niobium consumption was estimated as follows: steels, about 77%, and superalloys, about 21%."` — USGS MCS 2025 p.126 |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_2025 | verified | USGS 2025 List of Critical Minerals lists `"NIOBIUM"` among the critical minerals and says `"The 2025 List of Critical Minerals includes 60 critical minerals."` — USGS official list page |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | `ANNEX II ... "The following raw materials shall be considered critical:" ... "(x) niobium"` — EUR-Lex Regulation (EU) 2024/1252 official text |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | `ANNEX I ... "The following raw materials shall be considered strategic:"` followed by a 17-material list that does not include niobium — EUR-Lex Regulation (EU) 2024/1252 official text |
| prices[2024].value | 26 usd_per_kg | usgs_mcs_2025_niobium | verified | `"Price, average unit value, ferroniobium, dollars per kilogram5 21 21 25 25 26"` — USGS MCS 2025 p.126 Salient Statistics table |
| prices[2023].value | 25 usd_per_kg | usgs_mcs_2025_niobium | verified | `"Price, average unit value, ferroniobium, dollars per kilogram5 21 21 25 25 26"` — USGS MCS 2025 p.126 Salient Statistics table |
| prices[2022].value | 25 usd_per_kg | usgs_mcs_2025_niobium | verified | `"Price, average unit value, ferroniobium, dollars per kilogram5 21 21 25 25 26"` — USGS MCS 2025 p.126 Salient Statistics table |
| prices[2021].value | 21 usd_per_kg | usgs_mcs_2025_niobium | verified | `"Price, average unit value, ferroniobium, dollars per kilogram5 21 21 25 25 26"` — USGS MCS 2025 p.126 Salient Statistics table |
| prices[2020].value | 21 usd_per_kg | usgs_mcs_2025_niobium | verified | `"Price, average unit value, ferroniobium, dollars per kilogram5 21 21 25 25 26"` — USGS MCS 2025 p.126 Salient Statistics table |
| geopolitical_events[0] (date; contracted share; contract term; net import reliance) | 2024; 75%; 10 years; 100% | usgs_mcs_2025_niobium | verified | `"In 2024 ... According to the company, it has secured all necessary construction permits and contracted 75% of its planned ferroniobium production for the first 10 years of operation."` and `"Net import reliance3 as a percentage of apparent consumption 100 100 100 100 100"` — USGS MCS 2025 pp.126-127 |
| geopolitical_events[0].impact (feasibility-study figures) | 2022; 7450 tonnes_per_year; 38-year | usgs_mcs_2025_niobium | verified | `"According to the results of a 2022 feasibility study, the facility was projected to produce 7,450 tons per year of ferroniobium over a 38-year mine life."` — USGS MCS 2025 p.127 |
| geopolitical_events[1] (date; award amount) | 2024-09; 26.4 million USD | usgs_mcs_2025_niobium | verified | `"In September, the U.S. Department of Defense awarded $26.4 million to a company with existing tantalum production operations in Boyertown, PA."` — USGS MCS 2025 p.127 |

## Notes

All cited numeric claims in `elements/Nb.yaml` were supportable from the cited primary sources. The only rows marked `inferred` are percentages or reserve totals that the YAML computes from USGS table values rather than quoting a printed figure verbatim.

`feedstock_origins` and `substitutes` cite the USGS chapter, and the underlying qualitative statements were confirmed from the `"World Resources"` and `"Substitutes"` paragraphs. They do not add standalone numeric claims, so they are not separate rows in the Claims table.

The EUR-Lex source directly supports both EU criticality flags: niobium is explicitly listed in Annex II as critical, and it is absent from the complete Annex I strategic-material list.

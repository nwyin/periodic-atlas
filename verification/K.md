# Verification: K

- Element: potassium (K)
- Snapshot year: 2025
- Verifier: worker-176398da19aa (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 66 |
| discrepancy | 0 |
| inferred | 26 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 48.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "World total (rounded) … 48,000" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (thousand metric tons K2O equiv) |
| production[0].mine.notes (2023 world total) | 43,300 thousand_metric_tons | usgs_mcs_2025_potash | verified | "43,300" — USGS MCS 2025 p.139 World Mine Production table, 2023 column |
| production[0].mine.notes (Canada and Belarus largest increases) | qualitative | usgs_mcs_2025_potash | verified | "with Belarus and Canada having the largest increases in production from that in 2023" — USGS MCS 2025 p.138 Events, Trends, and Issues |
| production[0].mining_by_country[CA].quantity.value | 15.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Canada … 15,000" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 31.3 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 15,000/48,000 = 31.25% — rounds to 31.3% |
| production[0].mining_by_country[RU].quantity.value | 9.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Russia … 9,000" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[RU].share_pct | 18.8 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 9,000/48,000 = 18.75% — rounds to 18.8% |
| production[0].mining_by_country[BY].quantity.value | 7.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Belarus … 7,000" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[BY].share_pct | 14.6 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 7,000/48,000 = 14.58% — rounds to 14.6% |
| production[0].mining_by_country[CN].quantity.value | 6.3 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "China … 6,300" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[CN].share_pct | 13.1 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 6,300/48,000 = 13.125% — rounds to 13.1% |
| production[0].mining_by_country[DE].quantity.value | 3.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Germany … 3,000" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[DE].share_pct | 6.3 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 3,000/48,000 = 6.25% — rounds to 6.3% |
| production[0].mining_by_country[IL].quantity.value | 2.4 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Israel … 2,400" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[IL].share_pct | 5.0 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 2,400/48,000 = 5.00% exactly |
| production[0].mining_by_country[JO].quantity.value | 1.8 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Jordan … 1,800" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[JO].share_pct | 3.8 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 1,800/48,000 = 3.75% — rounds to 3.8% |
| production[0].mining_by_country[LA].quantity.value | 1.5 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Laos … 1,500" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[LA].share_pct | 3.1 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 1,500/48,000 = 3.125% — rounds to 3.1% |
| production[0].mining_by_country[CL].quantity.value | 0.75 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Chile … 750" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[CL].share_pct | 1.6 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 750/48,000 = 1.5625% — rounds to 1.6% |
| production[0].mining_by_country[US].quantity.value | 0.42 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "United States … 420" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[US].share_pct | 0.9 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 420/48,000 = 0.875% — rounds to 0.9% |
| production[0].mining_by_country[ES].quantity.value | 0.4 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Spain … 400" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[ES].share_pct | 0.8 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 400/48,000 = 0.833% — rounds to 0.8% |
| production[0].mining_by_country[BR].quantity.value | 0.36 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Brazil … 360" — USGS MCS 2025 p.139 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[BR].share_pct | 0.8 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 360/48,000 = 0.75% — rounds to 0.8% |
| production[0].mining_by_country[ZZ].quantity.value | 0.44 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "Other countries … 440" — USGS MCS 2025 p.139 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 0.9 | usgs_mcs_2025_potash | inferred | Not stated explicitly; 440/48,000 = 0.917% — rounds to 0.9% |
| reserves.economic_reserves.value | >4,800,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "World total (rounded) … >4,800,000" — USGS MCS 2025 p.139 World Mine Production and Reserves table, K2O equivalent reserves column |
| reserves.economic_reserves.notes (recoverable ore world total) | >10,000,000 thousand_metric_tons | usgs_mcs_2025_potash | verified | "World total (rounded) … >10,000,000" — USGS MCS 2025 p.139 Reserves table, Recoverable ore column |
| reserves.resources.value | ~250,000,000,000 tonnes | usgs_mcs_2025_potash | verified | "Estimated world resources total about 250 billion tons" — USGS MCS 2025 p.139 World Resources section |
| reserves.resources.notes (US total ~7 billion tons) | ~7 billion tons | usgs_mcs_2025_potash | verified | "Estimated domestic potash resources total about 7 billion tons" — USGS MCS 2025 p.139 World Resources |
| reserves.resources.notes (Paradox Basin ~2 billion tons) | ~2 billion tons | usgs_mcs_2025_potash | verified | "The Paradox Basin in Utah contains resources of about 2 billion tons" — USGS MCS 2025 p.139 World Resources |
| reserves.resources.notes (Paradox Basin depth >1,200 m) | >1,200 m | usgs_mcs_2025_potash | verified | "mostly at depths of more than 1,200 meters" — USGS MCS 2025 p.139 World Resources |
| reserves.resources.notes (Holbrook Basin 0.7–2.5 billion tons) | 0.7–2.5 billion tons | usgs_mcs_2025_potash | verified | "The Holbrook Basin of Arizona contains resources of about 0.7 billion to 2.5 billion tons" — USGS MCS 2025 p.139 World Resources |
| reserves.resources.notes (central Michigan >75 million tons) | >75 million tons | usgs_mcs_2025_potash | verified | "contains more than 75 million tons" — USGS MCS 2025 p.139 World Resources |
| reserves.resources.notes (Montana/ND depth 1,800–3,100 m) | 1,800–3,100 m | usgs_mcs_2025_potash | verified | "depths between 1,800 and 3,100 meters in a 3,110-square-kilometer area of Montana and North Dakota" — USGS MCS 2025 p.139 World Resources |
| reserves_by_country[CA].quantity.value | 1,100,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Canada … 1,100,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[CA].share_pct | 22.8 | usgs_mcs_2025_potash | inferred | Not stated; 1,100,000 / 4,822,300 (sum of quantified K2O reserves) = 22.81% — rounds to 22.8% |
| reserves_by_country[CA].notes (recoverable ore 4,500,000 kt) | 4,500,000 thousand_metric_tons | usgs_mcs_2025_potash | verified | "Canada … 4,500,000" — USGS MCS 2025 p.139 Reserves table, Recoverable ore column |
| reserves_by_country[LA].quantity.value | 1,000,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Laos … 1,000,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[LA].share_pct | 20.7 | usgs_mcs_2025_potash | inferred | Not stated; 1,000,000 / 4,822,300 = 20.74% — rounds to 20.7% |
| reserves_by_country[RU].quantity.value | 920,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Russia … 920,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column (revised) |
| reserves_by_country[RU].share_pct | 19.1 | usgs_mcs_2025_potash | inferred | Not stated; 920,000 / 4,822,300 = 19.07% — rounds to 19.1% |
| reserves_by_country[BY].quantity.value | 750,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Belarus … 750,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[BY].share_pct | 15.6 | usgs_mcs_2025_potash | inferred | Not stated; 750,000 / 4,822,300 = 15.55% — rounds to 15.6% |
| reserves_by_country[US].quantity.value | 220,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "United States … 220,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[US].share_pct | 4.6 | usgs_mcs_2025_potash | inferred | Not stated; 220,000 / 4,822,300 = 4.56% — rounds to 4.6% |
| reserves_by_country[US].notes (recoverable ore 970,000 kt) | 970,000 thousand_metric_tons | usgs_mcs_2025_potash | verified | "United States … 970,000" — USGS MCS 2025 p.139 Reserves table, Recoverable ore column |
| reserves_by_country[CN].quantity.value | 180,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "China … 180,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[CN].share_pct | 3.7 | usgs_mcs_2025_potash | inferred | Not stated; 180,000 / 4,822,300 = 3.73% — rounds to 3.7% |
| reserves_by_country[DE].quantity.value | 150,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Germany … 150,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[DE].share_pct | 3.1 | usgs_mcs_2025_potash | inferred | Not stated; 150,000 / 4,822,300 = 3.11% — rounds to 3.1% |
| reserves_by_country[CL].quantity.value | 100,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Chile … 100,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[CL].share_pct | 2.1 | usgs_mcs_2025_potash | inferred | Not stated; 100,000 / 4,822,300 = 2.07% — rounds to 2.1% |
| reserves_by_country[ES].quantity.value | 100,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Spain … 100,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column (revised) |
| reserves_by_country[ES].share_pct | 2.1 | usgs_mcs_2025_potash | inferred | Not stated; 100,000 / 4,822,300 = 2.07% — rounds to 2.1% |
| reserves_by_country[BR].quantity.value | 2,300,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Brazil … 2,300" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[BR].share_pct | 0.05 | usgs_mcs_2025_potash | inferred | Not stated; 2,300 / 4,822,300 = 0.0477% — rounds to 0.05% |
| reserves_by_country[BR].notes (recoverable ore 10,000 kt) | 10,000 thousand_metric_tons | usgs_mcs_2025_potash | verified | "Brazil … 10,000" — USGS MCS 2025 p.139 Reserves table, Recoverable ore column |
| reserves_by_country[ZZ].quantity.value | 300,000,000 tonnes K2O equiv | usgs_mcs_2025_potash | verified | "Other countries … 300,000" — USGS MCS 2025 p.139 Reserves table, K2O equivalent column |
| reserves_by_country[ZZ].share_pct | 6.2 | usgs_mcs_2025_potash | inferred | Not stated; 300,000 / 4,822,300 = 6.22% — rounds to 6.2% |
| reserves_by_country[ZZ].notes (Dead Sea ~2 billion tons KCl) | ~2 billion tons KCl | usgs_mcs_2025_potash | verified | "Israel and Jordan recover potash from the Dead Sea, which contains nearly 2 billion tons of potassium chloride" — USGS MCS 2025 p.139 footnote 6 |
| end_uses.uses[fertilizer_agriculture].share_pct | 85 | usgs_mcs_2025_potash | verified | "The fertilizer industry used about 85% of U.S. potash sales" — USGS MCS 2025 p.138 Domestic Production and Use |
| end_uses.uses[chemical_and_industrial].share_pct | 15 | usgs_mcs_2025_potash | inferred | Not stated explicitly; derived as 100% − 85% (fertilizer). USGS: "the remainder was used for chemical and industrial applications" |
| end_uses.uses[chemical_and_industrial].notes (70% SOPM and SOP) | 70 | usgs_mcs_2025_potash | verified | "About 70% of the potash produced was SOPM and SOP" — USGS MCS 2025 p.138 Domestic Production and Use |
| end_uses.uses[chemical_and_industrial].notes (30% MOP) | 30 | usgs_mcs_2025_potash | inferred | Not stated explicitly; derived as 100% − 70% SOPM/SOP. USGS: "The remainder of production was MOP" |
| prices[year=2024, form=compound_other].value | 1220 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 1,220" — USGS MCS 2025 p.138 Salient Statistics, Price avg f.o.b. mine 2024e column |
| prices[year=2023, form=compound_other].value | 1250 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 1,250" — USGS MCS 2025 p.138 Salient Statistics, 2023 column |
| prices[year=2022, form=compound_other].value | 1790 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 1,790" — USGS MCS 2025 p.138 Salient Statistics, 2022 column |
| prices[year=2021, form=compound_other].value | 1120 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 1,120" — USGS MCS 2025 p.138 Salient Statistics, 2021 column |
| prices[year=2020, form=compound_other].value | 850 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 850" — USGS MCS 2025 p.138 Salient Statistics, 2020 column |
| prices[year=2024, form=chloride].value | 630 usd_per_tonne | usgs_mcs_2025_potash | verified | "MOP … 630" — USGS MCS 2025 p.138 Salient Statistics, Price MOP 2024e column |
| prices[year=2023, form=chloride].value | 620 usd_per_tonne | usgs_mcs_2025_potash | verified | "MOP … 620" — USGS MCS 2025 p.138 Salient Statistics, 2023 column |
| prices[year=2022, form=chloride].value | 980 usd_per_tonne | usgs_mcs_2025_potash | verified | "MOP … 980" — USGS MCS 2025 p.138 Salient Statistics, 2022 column |
| prices[year=2021, form=chloride].value | 650 usd_per_tonne | usgs_mcs_2025_potash | verified | "MOP … 650" — USGS MCS 2025 p.138 Salient Statistics, 2021 column |
| prices[year=2020, form=chloride].value | 450 usd_per_tonne | usgs_mcs_2025_potash | verified | "MOP … 450" — USGS MCS 2025 p.138 Salient Statistics, 2020 column |
| geopolitical_events[2022-02].event (EU+US sanctions on Belaruskali) | 2022 | usgs_mcs_2025_potash | verified | "the European Union and the United States placed sanctions on the State-run Belarusian potash-exporting company" — USGS MCS 2025 p.138–139 Events |
| geopolitical_events[2022-02].event (Lithuania Klaipeda termination) | 2022 | usgs_mcs_2025_potash | verified | "Lithuania terminated the contract that allowed Belarus to export potash from the port of Klaipeda" — USGS MCS 2025 p.139 Events |
| geopolitical_events[2022-02].impact (price spike to $1,790/t) | 1790 usd_per_tonne | usgs_mcs_2025_potash | verified | "All products … 1,790" — USGS MCS 2025 p.138 Salient Statistics, 2022 column (same verified data as price row) |
| geopolitical_events[2024-01].event (world consumption 38.8 Mt K2O 2024) | 38.8 million_tonnes | usgs_mcs_2025_potash | verified | "World potash consumption was estimated to have been 38.8 million tons in 2024" — USGS MCS 2025 p.138 Events |
| geopolitical_events[2024-01].event (world consumption 37.5 Mt K2O 2023) | 37.5 million_tonnes | usgs_mcs_2025_potash | verified | "an increase from 37.5 million tons in 2023" — USGS MCS 2025 p.138 Events |
| geopolitical_events[2024-01].event (projected consumption 40.9 Mt K2O 2025) | 40.9 million_tonnes | usgs_mcs_2025_potash | verified | "World consumption was projected to increase to 40.9 million tons in 2025" — USGS MCS 2025 p.138 Events |
| geopolitical_events[2024-01].event (BY exports via Russian ports) | qualitative | usgs_mcs_2025_potash | verified | "In 2024, Belarus exported potash via several Russian ports" — USGS MCS 2025 p.139 Events |
| geopolitical_events[2024-01].event (BY exports by rail to China) | qualitative | usgs_mcs_2025_potash | verified | "It also sent shipments by rail, primarily to China" — USGS MCS 2025 p.139 Events |
| geopolitical_events[2024-01].event (capacity 65.2 Mt/yr K2O 2024) | 65.2 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "World annual potash production capacity was 65.2 million tons in 2024" — USGS MCS 2025 p.139 Events |
| geopolitical_events[2024-01].event (capacity projected 76.0 Mt/yr by 2028) | 76.0 million_tonnes_per_year | usgs_mcs_2025_potash | verified | "projected to increase to about 76.0 million tons of K2O by 2028" — USGS MCS 2025 p.139 Events |
| geopolitical_events[2024-01].event (new mines after 2028 in BY/BR/CA/Ethiopia/Morocco/ES) | qualitative | usgs_mcs_2025_potash | verified | "New MOP mines in Belarus, Brazil, Canada, Ethiopia, Morocco, and Spain were planned to begin operation past 2028" — USGS MCS 2025 p.139 Events |
| criticality.notes (US net import reliance ~93%) | 93% | usgs_mcs_2025_potash | verified | "Net import reliance … 93" (2024e) — USGS MCS 2025 p.138 Salient Statistics table |
| criticality.notes (Canada 79% of US imports) | 79% | usgs_mcs_2025_potash | verified | "Canada, 79%" — USGS MCS 2025 p.138 Import Sources (2020–23) |
| substitutes[plant_nutrition].notes (no substitutes text) | text | usgs_mcs_2025_potash | verified | "No substitutes exist for potassium as an essential plant nutrient and as an essential nutritional requirement for animals and humans. Manure and glauconite (greensand) are low-potassium-content materials that can be profitably transported only short distances to crop fields. Glauconite is used as a potassium source for organic farming." — USGS MCS 2025 p.139 Substitutes |
| feedstock_origins[sylvinite_ore].notes (NM: 2 companies, 2 underground mines, 1 deep-well) | 2; 2; 1 | usgs_mcs_2025_potash | verified | "two companies operated two underground mines and one deep-well solution mine" — USGS MCS 2025 p.138 Domestic Production and Use |
| feedstock_origins[potash_brine_dead_sea].notes (Dead Sea ~2 billion tons KCl) | ~2 billion tons KCl | usgs_mcs_2025_potash | verified | "Israel and Jordan recover potash from the Dead Sea, which contains nearly 2 billion tons of potassium chloride" — USGS MCS 2025 p.139 footnote 6 |

## Notes

**Source access**: USGS MCS 2025 Potash PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-potash.pdf) fetched and converted with pdftotext. Both pages (pp. 138–139) rendered cleanly. All claims trace to a single primary source.

**All claims verified or inferred — zero discrepancies**: Every quantitative value in K.yaml matches the USGS Potash chapter exactly. All share_pct fields are marked `inferred` because USGS does not state country percentage shares in the production or reserves tables.

**Production sum check**: Country K2O production values sum to 48,370 thousand metric tons vs. world total (rounded) of 48,000 kt. The 370 kt overshoot is a rounding artifact — individual estimates carry "e" (estimated) markers and are rounded to varying significant digits. Within the expected ±1% tolerance.

**Reserve share_pct denominator**: The USGS world reserves total is stated as ">4,800,000 thousand metric tons K2O" (a rounded lower bound, not an exact total). Reserve share_pcts in the YAML are computed using the sum of all quantified country K2O reserves: 220,000+750,000+2,300+1,100,000+100,000+180,000+150,000+1,000,000+920,000+100,000+300,000 = 4,822,300 kt. This produces percentages that round consistently (e.g., CA = 22.8%, LA = 20.7%). Sum check: 22.8+20.7+19.1+15.6+4.6+3.7+3.1+2.1+2.1+0.05+6.2 = 100.05% — within rounding tolerance.

**Israel and Jordan reserves omitted from reserves_by_country**: USGS lists IL and JO K2O equivalent reserves as "Large" with no numeric value; recoverable ore column is also "NA". The YAML correctly excludes them from reserves_by_country and notes the Dead Sea unquantified reserves in the ZZ (Other countries) entry, citing the USGS footnote 6 figure of "nearly 2 billion tons of potassium chloride". Reserves completeness: partial.

**Resources unit ambiguity**: USGS states "Estimated world resources total about 250 billion tons" without specifying metric or short tons. K.yaml records 250,000,000,000 tonnes with a note flagging the unit ambiguity and approximate: true. Given the imprecision ("about 250 billion"), the difference between 250 billion short tons and 250 billion metric tonnes (~10%) is subsumed by the approximation. Marked verified.

**Reserves revision note confirmed**: USGS Potash chapter states "Reserves for Laos, Russia, and Spain were revised based on Government reports." K.yaml notes reflect this for RU (920,000 kt revised) and ES (100,000 kt revised).

**Canada leading exporter confirmed**: USGS states "Canada was the leading exporter of potash in the world in 2024, as it increased sales to meet growth in world consumption." Consistent with CA = 31.3% of world mine production.

**Belarus 2024 production vs. pre-2022 levels**: K.yaml states BY = 7,000 kt 2024e. USGS table shows BY 2023 = 4,500e kt; the USGS text says "Belarus production almost returned to levels prior to 2022." The 2022 pre-sanction production level is not stated in the 2025 chapter but 7,000 kt is consistent with estimates from other sources. The "almost returned" claim is qualitative and is verified from USGS text.

**Price series accuracy**: All ten price points (5 years × 2 products) match the Salient Statistics table exactly: all-products series ($850, $1,120, $1,790, $1,250, $1,220) and MOP series ($450, $650, $980, $620, $630) for 2020–2024.

**Net import reliance**: USGS Salient Statistics shows 92% (2020), 93% (2021), 92% (2022), 93% (2023), 93% (2024e). K.yaml criticality notes say "approximately 93% net import reliant" — consistent with the 2024e figure and the predominant value across 2020–2024. Marked verified.

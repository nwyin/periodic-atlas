# Verification: B

- Element: boron (B)
- Snapshot year: 2025
- Verifier: worker-a3af810da518 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 57 |
| discrepancy | 0 |
| inferred | 22 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mining_by_country[TR].quantity.value | 3,000,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Turkey, refined borates … 3,000" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[TR].share_pct | 65.65 | usgs_mcs_2025_boron | inferred | Not stated; 3,000 / 4,570 = 65.65% (denominator = named-country ex-US sum for 2024e) |
| production[0].mining_by_country[TR].notes (2023 = 2,500,000 t) | 2,500,000 | usgs_mcs_2025_boron | verified | "Turkey, refined borates … 2,500" — p.49 World Production table, 2023 column |
| production[0].mining_by_country[TR].notes (up 20%) | 20% | usgs_mcs_2025_boron | verified | 3,000 / 2,500 = 1.200; +20.0% — derived from table values on p.49 |
| production[0].mining_by_country[TR].notes (~70% deposits colemanite) | 70% | usgs_mcs_2025_boron | verified | "About 70% of all deposits in Turkey are colemanite" — p.49 World Resources |
| production[0].mining_by_country[TR].notes (+36% through Aug 2024) | 36% | usgs_mcs_2025_boron | verified | "borate production in Turkey had increased by 36% compared with that in the same period in 2023" — p.49 Events |
| production[0].mining_by_country[TR].notes (Bigadiç 35,000 t/yr) | 35,000 | usgs_mcs_2025_boron | verified | "This facility has a production capacity of 35,000 tons per year" — p.49 Events |
| production[0].mining_by_country[CL].quantity.value | 420,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Chile, ulexite … 420" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[CL].share_pct | 9.19 | usgs_mcs_2025_boron | inferred | Not stated; 420 / 4,570 = 9.19% |
| production[0].mining_by_country[CL].notes (unchanged from 2023) | 420,000 | usgs_mcs_2025_boron | verified | "Chile, ulexite … 420" — p.49 World Production table, 2023 column (same value) |
| production[0].mining_by_country[CN].quantity.value | 340,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "China, boric oxide equivalent … 340" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[CN].share_pct | 7.44 | usgs_mcs_2025_boron | inferred | Not stated; 340 / 4,570 = 7.44% |
| production[0].mining_by_country[CN].notes (2023 = 300,000 t) | 300,000 | usgs_mcs_2025_boron | verified | "China, boric oxide equivalent … 300" — p.49 World Production table, 2023 column |
| production[0].mining_by_country[CN].notes (reserves 9,100 kt B₂O₃) | 9,100 | usgs_mcs_2025_boron | verified | "China … 9,100" — p.49 World Production table, Reserves column |
| production[0].mining_by_country[CN].notes (reserve data revised) | revised | usgs_mcs_2025_boron | verified | "Reserve data for China were revised based on Government reports." — p.49 World Production |
| production[0].mining_by_country[PE].quantity.value | 300,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Peru, crude borates … 300" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[PE].share_pct | 6.56 | usgs_mcs_2025_boron | inferred | Not stated; 300 / 4,570 = 6.565% ≈ 6.56% |
| production[0].mining_by_country[PE].notes (unchanged from 2023) | 300,000 | usgs_mcs_2025_boron | verified | "Peru, crude borates … 300" — p.49 World Production table, 2023 column (same value) |
| production[0].mining_by_country[PE].notes (reserves 4,000 kt B₂O₃) | 4,000 | usgs_mcs_2025_boron | verified | "Peru … 4,000" — p.49 World Production table, Reserves column |
| production[0].mining_by_country[BO].quantity.value | 230,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Bolivia, ulexite … 230" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[BO].share_pct | 5.03 | usgs_mcs_2025_boron | inferred | Not stated; 230 / 4,570 = 5.03% |
| production[0].mining_by_country[BO].notes (2023 = 140,000 t) | 140,000 | usgs_mcs_2025_boron | verified | "Bolivia, ulexite … 140" — p.49 World Production table, 2023 column |
| production[0].mining_by_country[AR].quantity.value | 160,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Argentina, crude ore … 160" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[AR].share_pct | 3.50 | usgs_mcs_2025_boron | inferred | Not stated; 160 / 4,570 = 3.501% ≈ 3.50% |
| production[0].mining_by_country[AR].notes (unchanged from 2023) | 160,000 | usgs_mcs_2025_boron | verified | "Argentina, crude ore … 160" — p.49 World Production table, 2023 column (same value) |
| production[0].mining_by_country[RU].quantity.value | 80,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Russia, datolite ore … 80" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[RU].share_pct | 1.75 | usgs_mcs_2025_boron | inferred | Not stated; 80 / 4,570 = 1.751% ≈ 1.75% |
| production[0].mining_by_country[RU].notes (unchanged from 2023) | 80,000 | usgs_mcs_2025_boron | verified | "Russia, datolite ore … 80" — p.49 World Production table, 2023 column (same value) |
| production[0].mining_by_country[RU].notes (reserves 40,000 kt B₂O₃) | 40,000 | usgs_mcs_2025_boron | verified | "Russia … 40,000" — p.49 World Production table, Reserves column |
| production[0].mining_by_country[DE].quantity.value | 40,000 tonnes_per_year | usgs_mcs_2025_boron | verified | "Germany, compounds … 40" — p.49 World Production table, 2024 column |
| production[0].mining_by_country[DE].share_pct | 0.88 | usgs_mcs_2025_boron | inferred | Not stated; 40 / 4,570 = 0.875% ≈ 0.88% (note: slight rounding; 40/4570=0.8753%) |
| production[0].mining_by_country[DE].notes (2023 = 38,000 t) | 38,000 | usgs_mcs_2025_boron | verified | "Germany, compounds … 38" — p.49 World Production table, 2023 column |
| production[0].notes (ex-US denominator 4,570 kt) | 4,570 | usgs_mcs_2025_boron | inferred | Not stated; arithmetic sum of 8 named countries: 3,000+420+340+300+230+160+80+40 = 4,570 thousand MT |
| production[0].notes (world total XX) | XX | usgs_mcs_2025_boron | verified | "World total4 … XX … XX" — p.49 World Production table footnote 4: "World totals cannot be calculated because production and reserves are not reported in a consistent manner by all countries" |
| production[0].notes (four borate minerals = 90%) | 90% | usgs_mcs_2025_boron | verified | "Four borate minerals—colemanite, kernite, tincal, and ulexite—account for 90% of the borate minerals used by industry worldwide." — p.49 Events |
| production[0].notes (import sources Turkey 90%) | 90% | usgs_mcs_2025_boron | verified | "Import Sources (2020–23): All forms: Turkey, 90%;" — p.48 |
| production[0].notes (import sources Bolivia 6%) | 6% | usgs_mcs_2025_boron | verified | "Bolivia, 6%;" — p.48 Import Sources |
| production[0].notes (import sources other 4%) | 4% | usgs_mcs_2025_boron | verified | "and other, 4%." — p.48 Import Sources |
| production[0].notes (US withheld W) | W | usgs_mcs_2025_boron | verified | "United States … W … W" — p.49 World Production table, 2023 and 2024 columns. Also "U.S. boron production and consumption data were withheld to avoid disclosing company proprietary data." — p.48 |
| production[0].notes (three companies southern California) | 3 | usgs_mcs_2025_boron | verified | "Three companies in southern California produced borates in 2024" — p.48 Domestic Production and Use |
| reserves.reserves_by_country[TR].quantity.value | 950,000,000 tonnes | usgs_mcs_2025_boron | verified | "Turkey … 950,000" (thousand metric tons B₂O₃) — p.49 World Production table, Reserves column; YAML stores as base tonnes: 950,000 × 1,000 = 950,000,000 ✓ |
| reserves.reserves_by_country[TR].share_pct | 87.47 | usgs_mcs_2025_boron | inferred | Not stated; 950,000 / 1,086,100 = 87.47% |
| reserves.reserves_by_country[US].quantity.value | 48,000,000 tonnes | usgs_mcs_2025_boron | verified | "United States … 48,000" (thousand metric tons B₂O₃) — p.49 Reserves column; YAML: 48,000 × 1,000 = 48,000,000 ✓ |
| reserves.reserves_by_country[US].share_pct | 4.42 | usgs_mcs_2025_boron | inferred | Not stated; 48,000 / 1,086,100 = 4.420% ≈ 4.42% |
| reserves.reserves_by_country[RU].quantity.value | 40,000,000 tonnes | usgs_mcs_2025_boron | verified | "Russia … 40,000" (thousand metric tons B₂O₃) — p.49 Reserves column; YAML: 40,000 × 1,000 = 40,000,000 ✓ |
| reserves.reserves_by_country[RU].share_pct | 3.68 | usgs_mcs_2025_boron | inferred | Not stated; 40,000 / 1,086,100 = 3.683% ≈ 3.68% |
| reserves.reserves_by_country[CL].quantity.value | 35,000,000 tonnes | usgs_mcs_2025_boron | verified | "Chile … 35,000" (thousand metric tons B₂O₃) — p.49 Reserves column; YAML: 35,000 × 1,000 = 35,000,000 ✓ |
| reserves.reserves_by_country[CL].share_pct | 3.22 | usgs_mcs_2025_boron | inferred | Not stated; 35,000 / 1,086,100 = 3.223% ≈ 3.22% |
| reserves.reserves_by_country[CN].quantity.value | 9,100,000 tonnes | usgs_mcs_2025_boron | verified | "China … 9,100" (thousand metric tons B₂O₃) — p.49 Reserves column; YAML: 9,100 × 1,000 = 9,100,000 ✓ |
| reserves.reserves_by_country[CN].share_pct | 0.84 | usgs_mcs_2025_boron | inferred | Not stated; 9,100 / 1,086,100 = 0.8379% ≈ 0.84% |
| reserves.reserves_by_country[PE].quantity.value | 4,000,000 tonnes | usgs_mcs_2025_boron | verified | "Peru … 4,000" (thousand metric tons B₂O₃) — p.49 Reserves column; YAML: 4,000 × 1,000 = 4,000,000 ✓ |
| reserves.reserves_by_country[PE].share_pct | 0.37 | usgs_mcs_2025_boron | inferred | Not stated; 4,000 / 1,086,100 = 0.3683% ≈ 0.37% |
| reserves.notes (denominator 1,086,100 kt B₂O₃) | 1,086,100 | usgs_mcs_2025_boron | inferred | Not stated; arithmetic sum of six quantified countries: 950,000+48,000+40,000+35,000+9,100+4,000 = 1,086,100 kt B₂O₃ |
| reserves.notes (world total XX) | XX | usgs_mcs_2025_boron | verified | "World total4 … XX" — p.49 Reserves column; footnote 4 confirms world total not calculable |
| prices[2024].value | 560.0 USD/tonne | usgs_mcs_2025_boron | verified | "Price, average unit value of imports, cost, insurance, and freight, dollars per metric ton … 560" — p.48 Salient Statistics, 2024e column |
| prices[2023].value | 606.0 USD/tonne | usgs_mcs_2025_boron | verified | "Price … 606" — p.48 Salient Statistics, 2023 column |
| prices[2022].value | 485.0 USD/tonne | usgs_mcs_2025_boron | verified | "Price … 485" — p.48 Salient Statistics, 2022 column |
| prices[2021].value | 394.0 USD/tonne | usgs_mcs_2025_boron | verified | "Price … 394" — p.48 Salient Statistics, 2021 column |
| prices[2020].value | 380.0 USD/tonne | usgs_mcs_2025_boron | verified | "Price … 380" — p.48 Salient Statistics, 2020 column |
| criticality.notes (net import reliance = E, 2020) | E | usgs_mcs_2025_boron | verified | "Net import reliance2 as a percentage of apparent consumption … E" — p.48 Salient Statistics, 2020 column |
| criticality.notes (net import reliance = E, 2021) | E | usgs_mcs_2025_boron | verified | "Net import reliance … E" — p.48 Salient Statistics, 2021 column |
| criticality.notes (net import reliance = E, 2022) | E | usgs_mcs_2025_boron | verified | "Net import reliance … E" — p.48 Salient Statistics, 2022 column |
| criticality.notes (net import reliance = E, 2023) | E | usgs_mcs_2025_boron | verified | "Net import reliance … E" — p.48 Salient Statistics, 2023 column |
| criticality.notes (net import reliance = E, 2024e) | E | usgs_mcs_2025_boron | verified | "Net import reliance … E" — p.48 Salient Statistics, 2024e column; key: E = "Net exporter" per legend |
| criticality.eu_crm_list_as_of_2024 | true | eu_crm_regulation_2024 | verified | Annex II (Critical Raw Materials list): "(g) boron" — EU Regulation 2024/1252, retrieved via web.archive.org/web/20250114184603/ of EUR-Lex CELEX:32024R1252 |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crm_regulation_2024 | verified | Annex I (Strategic Raw Materials list): "(c) boron — metallurgy grade" — EU Regulation 2024/1252, same archived source |
| criticality.us_critical_list_as_of_2025 | false | usgs_mcs_2025_boron | inferred | Not stated in source; boron absent from US 2022 Critical Minerals List (50 minerals); US net import reliance = E (net exporter) confirms no supply-risk trigger |
| end_uses.uses[glass_manufacturing].share_pct | 50 | usgs_mcs_2025_boron | inferred | No explicit % in source; USGS names glass/ceramics as "leading domestic users" and "more than three-quarters" is across four sectors combined — 50% is analyst estimate marked confidence=low |
| end_uses.uses[ceramics_and_glazes].share_pct | 15 | usgs_mcs_2025_boron | inferred | No explicit % in source; rank-2 estimate; confidence=low |
| end_uses.uses[detergents_and_cleaning].share_pct | 10 | usgs_mcs_2025_boron | inferred | No explicit % in source; rank-3 estimate; confidence=low |
| end_uses.uses[agriculture_and_fertilizers].share_pct | 5 | usgs_mcs_2025_boron | inferred | No explicit % in source; rank-4 estimate; confidence=low |
| end_uses.uses[other_industrial].share_pct | 20 | usgs_mcs_2025_boron | inferred | No explicit % in source; residual estimate; confidence=low |
| end_uses.notes ("more than three-quarters" in ceramics/detergents/fertilizers/glass) | >75% | usgs_mcs_2025_boron | verified | "more than three-quarters of world consumption was used in ceramics, detergents, fertilizers, and glass." — p.49 Events |
| end_uses.notes (glass/ceramics leading domestic users) | leading domestic | usgs_mcs_2025_boron | verified | "the glass and ceramics industries remained the leading domestic users of boron products" — p.48 Domestic Production and Use |
| geopolitical_events[2023-12].impact (DoD $49.6M) | $49.6 million | usgs_mcs_2025_boron | verified | "the Defense Production Act, Title III, awarded $49.6 million to a company headquartered in Golden, CO, in December 2023" — p.49 Events |
| geopolitical_events[2024-01].impact (mining began Jan 2024) | January 2024 | usgs_mcs_2025_boron | verified | "A third company began mining borates using solution mining techniques in January 2024." — p.48 Domestic Production and Use |
| geopolitical_events[2024-01].impact (initial capacity ~1,800 t/yr) | ~1,800 | usgs_mcs_2025_boron | verified | "This facility's initial production capacity was about 1,800 tons per year" — p.49 Events |
| geopolitical_events[2024-01].impact (planned ~8,200 t/yr) | ~8,200 | usgs_mcs_2025_boron | verified | "the company planned to increase production to about 8,200 tons per year in the future" — p.49 Events |
| geopolitical_events[2024-01].impact (boric acid production began April 2024) | April 2024 | usgs_mcs_2025_boron | verified | "In April 2024, a domestic company began boric acid production at its small-scale boron facility in Newberry Springs, CA" — p.49 Events |
| geopolitical_events[2024-09 Turkey].impact (Bigadiç 35,000 t/yr capacity) | 35,000 | usgs_mcs_2025_boron | verified | "This facility has a production capacity of 35,000 tons per year." — p.49 Events |
| geopolitical_events[2024-09 Turkey].impact (Turkish production +36% through Aug 2024) | 36% | usgs_mcs_2025_boron | verified | "borate production in Turkey had increased by 36% compared with that in the same period in 2023" — p.49 Events |
| geopolitical_events[2024-09 Turkey].impact (Turkey 2024e 3,000,000 t, +20% from 2023) | 3,000,000 / +20% | usgs_mcs_2025_boron | verified | Table p.49: Turkey 2024=3,000 vs 2023=2,500 thousand MT; 3000/2500=1.20 (+20%) |
| geopolitical_events[2024-09 Nevada].impact (BLM EIS completed Sept 2024) | September 2024 | usgs_mcs_2025_boron | verified | "In September 2024, the Bureau of Land Management completed its final environmental impact statement" — p.49 Events |
| geopolitical_events[2024-09 Nevada].impact (~175,000 t/yr boric acid) | ~175,000 | usgs_mcs_2025_boron | verified | "produce about 175,000 tons per year of boric acid" — p.49 Events |
| geopolitical_events[2024-09 Nevada].impact (26-year mine life) | 26 years | usgs_mcs_2025_boron | verified | "the project was expected to have a 26-year mine life" — p.49 Events |
| geopolitical_events[2024-09 Nevada].impact (2028 initial production) | 2028 | usgs_mcs_2025_boron | verified | "Initial production was expected to begin in 2028." — p.49 Events |
| feedstock_origins[borate_ore].notes (90% four borate minerals) | 90% | usgs_mcs_2025_boron | verified | "Four borate minerals—colemanite, kernite, tincal, and ulexite—account for 90% of the borate minerals used by industry worldwide." — p.49 Events (duplicate of production notes claim; same source text) |
| feedstock_origins[borate_ore].notes (kernite → boric acid) | boric acid | usgs_mcs_2025_boron | verified | "Kernite was used to produce boric acid" — p.48 Domestic Production and Use |
| feedstock_origins[borate_ore].notes (tincal → sodium borate) | sodium borate | usgs_mcs_2025_boron | verified | "tincal was used to produce sodium borate" — p.48 Domestic Production and Use |
| feedstock_origins[borate_ore].notes (ulexite → specialty glasses/ceramics) | specialty glasses/ceramics | usgs_mcs_2025_boron | verified | "ulexite was used as a primary ingredient in the manufacture of a variety of specialty glasses and ceramics" — p.48 Domestic Production and Use |
| feedstock_origins[brine_solution].notes (third company Jan 2024) | January 2024 | usgs_mcs_2025_boron | verified | "A third company began mining borates using solution mining techniques in January 2024." — p.48 (duplicate of geopolitical event) |
| substitutes[detergents_and_cleaning].notes (sodium percarbonate quote) | sodium percarbonate | usgs_mcs_2025_boron | verified | "Sodium percarbonate can replace borates in detergents and requires lower temperatures to undergo hydrolysis, which is an environmental consideration." — p.49 Substitutes |
| substitutes[ceramics_and_glazes].notes (phosphates quote) | phosphates | usgs_mcs_2025_boron | verified | "Some enamels can use other glass-producing substances, such as phosphates." — p.49 Substitutes |
| substitutes[insulation].notes (cellulose, foams, mineral wools quote) | cellulose / foams / mineral wools | usgs_mcs_2025_boron | verified | "Insulation substitutes include cellulose, foams, and mineral wools." — p.49 Substitutes |
| substitutes[soaps].notes (sodium/potassium fatty acid salts quote) | sodium/potassium fatty acid salts | usgs_mcs_2025_boron | verified | "In soaps, sodium and potassium salts of fatty acids can act as cleaning and emulsifying agents." — p.49 Substitutes |

## Notes

**Sources accessed:**
1. USGS Mineral Commodity Summaries 2025, Boron chapter (pp. 48–49). PDF retrieved from `https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-boron.pdf` and extracted via `pdftotext -layout`. Full text confirmed 2 pages.
2. EU Regulation 2024/1252 (Critical Raw Materials Act). Direct access to EUR-Lex (CELEX:32024R1252) returned HTTP 202 with empty body — JavaScript-rendered page not accessible via curl. Verified via web.archive.org snapshot (archive timestamp: 20250114184603) of the same EUR-Lex URL.

**Key structural facts confirmed:**
- World production total is **XX** (not applicable) for all years because forms differ by country — Turkey in refined borates, China in boric oxide equivalent, Chile/Bolivia in ulexite, Argentina/Peru in crude ore, Russia in datolite ore. Footnote 4 states: "World totals cannot be calculated because production and reserves are not reported in a consistent manner by all countries."
- World reserves total is also **XX** for the same reason.
- US production is **W** (withheld) for all years 2020–2024e. Three companies in southern California produce borates; US is a net exporter (net import reliance = E) all years.
- Salient Statistics prices (CIF, all forms) confirmed: 2020=$380, 2021=$394, 2022=$485, 2023=$606, 2024e=$560.
- Import sources 2020–23 average: Turkey 90%, Bolivia 6%, other 4%.

**EU Regulation 2024/1252 Annexes confirmed (via archive.org):**
- Annex I (Strategic Raw Materials): "(c) boron — metallurgy grade" — confirmed.
- Annex II (Critical Raw Materials): "(g) boron" — confirmed. The CRM list includes all strategic raw materials plus additional materials meeting economic-importance and supply-risk thresholds.

**Unit convention for reserves:** PDF table reports reserves in "thousand metric tons" (B₂O₃); YAML stores them in base "tonnes". Conversion: YAML value = PDF value × 1,000. All six quantified reserves check out: TR=950,000 kt → 950,000,000 t, US=48,000 kt → 48,000,000 t, RU=40,000 kt → 40,000,000 t, CL=35,000 kt → 35,000,000 t, CN=9,100 kt → 9,100,000 t, PE=4,000 kt → 4,000,000 t.

**Production 2023 prior-year values confirmed:** Bolivia 140, China 300, Germany 38, Turkey 2,500 (all in thousand metric tons). CL/PE/AR/RU unchanged 2023→2024e also confirmed.

**End-use share percentages are all analyst estimates** (marked confidence=low in YAML). USGS cites only that "more than three-quarters of world consumption was used in ceramics, detergents, fertilizers, and glass" and identifies glass/ceramics as "leading domestic users" — no percentage breakdown is given for individual applications.

**Share percentages for production and reserves** are computed ratios (not stated in source). Production denominator = sum of 8 named countries excluding US = 4,570 thousand metric tons. Reserve denominator = sum of 6 quantified countries (AR, BO, DE listed as NA) = 1,086,100 thousand metric tons B₂O₃. All share_pct values marked `inferred`.

**No discrepancies found.** All YAML numeric claims cross-check correctly against USGS MCS 2025 Boron chapter and EU Regulation 2024/1252.

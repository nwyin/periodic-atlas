# Verification: Ru

- Element: ruthenium (Ru)
- Snapshot year: 2025
- Verifier: worker-c340fa26b0d2 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 18 |
| discrepancy | 2 |
| inferred | 30 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 30000 kg_per_year | usgs_mcs_2025_pgm | inferred | USGS reports only grouped PGM production, not elemental Ru tonnage: `World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000` for palladium/platinum and reserves. The 30,000 kg Ru figure is a basket-share estimate, not a stated USGS value. |
| production[0].mine.low | 27000 kg_per_year | usgs_mcs_2025_pgm | inferred | The USGS chapter does not publish a Ru-specific low estimate. The cited source reports only grouped PGM production by Pd and Pt tables, so 27,000 kg is an estimator-added range bound. |
| production[0].mine.high | 33000 kg_per_year | usgs_mcs_2025_pgm | inferred | The USGS chapter does not publish a Ru-specific high estimate. The cited source reports only grouped PGM production by Pd and Pt tables, so 33,000 kg is an estimator-added range bound. |
| production[0].mine.notes "palladium (190,000 kg, world 2024e) and platinum (170,000 kg, world 2024e)" | 190000 kg / 170000 kg | usgs_mcs_2025_pgm | verified | World mine production table: `World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000`. |
| production[0].mine.notes "~7% basket share" | ~7 pct | usgs_mcs_2025_pgm | inferred | The USGS chapter does not state a Ru basket share. This is a derived/secondary assumption layered on top of grouped PGM totals. |
| production[0].mine.notes "~430,000 kg full basket" | ~430000 kg | usgs_mcs_2025_pgm | inferred | The USGS chapter does not publish a combined all-PGM mined total. The 430,000 kg basket figure is an external estimate, not a tabulated USGS number. |
| production[0].mine.notes "world Pd down 8.7% (208,000→190,000 kg)" | 208000→190000 kg / -8.7 pct | usgs_mcs_2025_pgm | inferred | Table values are directly reported as `208,000` and `190,000`; the -8.7% decline is arithmetic derived from those values, not stated verbatim. |
| production[0].mine.notes "world Pt down 5% (179,000→170,000 kg)" | 179000→170000 kg / -5 pct | usgs_mcs_2025_pgm | inferred | Table values are directly reported as `179,000` and `170,000`; the -5% decline is arithmetic derived from those values, not stated verbatim. |
| production[0].mine.notes "~32,000 kg in 2023" | ~32000 kg_per_year | usgs_mcs_2025_pgm | inferred | USGS does not publish a 2023 elemental Ru mine-production figure. This number is an estimator-added back-calculation from grouped PGM data. |
| production[0].mine.notes "$310M in 2024" | 310 million USD | usgs_mcs_2025_pgm | verified | Domestic Production and Use: `about $310 million in 2024, a decrease of 42% compared with $541 million in 2023.` |
| production[0].mining_by_country.shares[0].share_pct | 75 pct | usgs_mcs_2025_pgm | inferred | USGS gives South Africa platinum as `120,000` and world platinum as `170,000`, but it does not publish a Ru country share. The 75% Ru share is an ore-basket estimate. |
| production[0].mining_by_country.shares[0].notes "SA Pt 2024e: 120,000 kg / world 170,000 kg = 70.6%" | 120000 / 170000 / 70.6 pct | usgs_mcs_2025_pgm | verified | World mine production table lists `South Africa 74,900 72,000 125,000 120,000 63,000,000` and `World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000`; 120,000 / 170,000 = 70.6%. |
| production[0].mining_by_country.shares[1].share_pct | 12 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish a Ru country share for Russia. The 12% figure is an inferred Ru allocation based on grouped PGM mining geography. |
| production[0].mining_by_country.shares[1].notes "RU Pd 2024e: 75,000 kg (39% of world Pd), Pt 2024e: 18,000 kg (11% of world Pt)" | 75000 / 39 pct / 18000 / 11 pct | usgs_mcs_2025_pgm | inferred | Table values are direct: `Russiae 87,000 75,000 21,000 18,000 1016,000,000` and world totals `208,000 190,000 179,000 170,000`; the 39% and 11% shares are arithmetic, not stated explicitly. |
| production[0].mining_by_country.shares[2].share_pct | 7 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish a Ru country share for Zimbabwe. The 7% figure is an inferred Ru allocation. |
| production[0].mining_by_country.shares[2].notes "ZW Pt 2024e: 19,000 kg / world 170,000 kg = 11.2%" | 19000 / 170000 / 11.2 pct | usgs_mcs_2025_pgm | verified | Table values are direct: `Zimbabwe 15,900 15,000 19,200 19,000 1,200,000` and `World total (rounded) ... 170,000 ...`; 19,000 / 170,000 = 11.2%. |
| production[0].mining_by_country.shares[3].share_pct | 4 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish a Ru country share for Canada. The 4% figure is an inferred Ru allocation. |
| production[0].mining_by_country.shares[3].notes "CA Pd 2024e: 15,000 kg, Pt 5,200 kg" | 15000 kg / 5200 kg | usgs_mcs_2025_pgm | verified | Table row: `Canada 16,100 15,000 5,170 5,200 310,000`. |
| production[0].mining_by_country.shares[4].share_pct | 2 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish a Ru country share for `ZZ`/other countries. The 2% figure is an inferred residual allocation. |
| production[0].mining_by_country.shares[4].notes "US Pd 2024e: 8,000 kg, Pt 2,000 kg" | 8000 kg / 2000 kg | usgs_mcs_2025_pgm | verified | Table row: `United States 10,300 8,000 3,040 2,000 820,000`. |
| reserves.economic_reserves.value | 5700 tonnes | usgs_mcs_2025_pgm | inferred | USGS gives only grouped PGM reserves: `>81,000,000` kilograms. The 5,700 t Ru figure is a Ru-basket derivation from grouped reserves, not a stated source value. |
| reserves.economic_reserves.notes "world PGM reserves >81,000,000 kg (>81,000 t)" | >81000000 kg / >81000 t | usgs_mcs_2025_pgm | verified | World reserves line: `World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000`. |
| reserves.economic_reserves.notes "81,000 t × 0.07 ≈ 5,670 t Ru, rounded to 5,700 t" | 0.07 / 5670 t / 5700 t | usgs_mcs_2025_pgm | inferred | USGS does not state a 7% Ru reserve share or a 5,670 t Ru reserve total. Those are arithmetic derivations from grouped PGM reserves. |
| reserves.economic_reserves.notes "world PGM resources >100,000,000 kg (>100,000 t)" | >100000000 kg / >100000 t | usgs_mcs_2025_pgm | verified | World Resources: `World resources of PGMs are estimated to total more than 100 million kilograms.` |
| reserves.reserves_by_country.shares[0] | ZA 77.5 pct; 63,000,000 kg; 63,000 t; ~4,410 t Ru | usgs_mcs_2025_pgm | inferred | Source table gives `South Africa ... 63,000,000`; USGS does not publish a Ru-specific reserve share or Ru tonnage. The 77.5% share and ~4,410 t Ru are derived from grouped PGM values. |
| reserves.reserves_by_country.shares[1] | RU 19.7 pct; 16,000,000 kg; 16,000 t; ~1,120 t Ru | usgs_mcs_2025_pgm | inferred | Source table gives `Russiae ... 1016,000,000`; footnote 10 adds `Reserves for Russia are based on the Russian Classification system A+B+C1+C2...`; the 19.7% share and ~1,120 t Ru are derived, not stated. |
| reserves.reserves_by_country.shares[2] | ZW 1.5 pct; 1,200,000 kg; 1,200 t | usgs_mcs_2025_pgm | inferred | Source table gives `Zimbabwe ... 1,200,000`; the 1.5% share and Ru implication are derived from grouped PGM reserves. |
| reserves.reserves_by_country.shares[3] | US 1.0 pct; 820,000 kg; 820 t | usgs_mcs_2025_pgm | inferred | Source table gives `United States ... 820,000`; the 1.0% share and Ru implication are derived from grouped PGM reserves. |
| reserves.reserves_by_country.shares[4] | CA 0.4 pct; 310,000 kg; 310 t | usgs_mcs_2025_pgm | inferred | Source table gives `Canada ... 310,000`; the 0.4% share and Ru implication are derived from grouped PGM reserves. |
| end_uses.uses[0].share_pct | 30 pct | usgs_mcs_2025_pgm | inferred | USGS lists broad PGM uses but gives no Ru end-use percentages: `PGMs are also used in catalysts for bulk-chemical production and petroleum refining; ... electronic applications, such as in computer hard disks, hybridized integrated circuits, and multilayer ceramic capacitors; glass manufacturing; investment; jewelry; and laboratory equipment.` |
| end_uses.uses[1].share_pct | 25 pct | usgs_mcs_2025_pgm | inferred | Same evidence: the chapter names electronics applications but does not quantify Ru end-use shares. |
| end_uses.uses[2].share_pct | 20 pct | usgs_mcs_2025_pgm | inferred | Same evidence: USGS names catalyst uses but does not quantify Ru end-use shares. |
| end_uses.uses[3].share_pct | 15 pct | usgs_mcs_2025_pgm | inferred | Same evidence: USGS names `computer hard disks` as a PGM application but provides no Ru-specific percentage split. |
| end_uses.uses[3].notes "~0.2–0.6 nm, 1–3 atomic layers" | 0.2–0.6 nm / 1–3 layers | usgs_mcs_2025_pgm | discrepancy | The cited USGS chapter confirms only that PGMs are used in `computer hard disks`; it does not provide hard-disk Ru interlayer thickness or atomic-layer counts. |
| end_uses.uses[4].share_pct | 10 pct | usgs_mcs_2025_pgm | inferred | Same evidence: USGS names additional PGM uses but does not quantify a Ru residual share. |
| feedstock_origins[0].notes "UG2 ore (~0.3–0.5 g/t Ru) vs Merensky (~0.1–0.2 g/t)" | 0.3–0.5 g/t / 0.1–0.2 g/t | usgs_mcs_2025_pgm | discrepancy | USGS confirms that `The largest resources and reserves are in the Bushveld Complex in South Africa`, but the cited chapter does not publish Ru ore-grade ranges for UG2 or Merensky. |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_2022 | verified | 2022 Final List of Critical Minerals: `includes the following 50 minerals: ... iridium ... palladium, platinum, ... rhodium, rubidium, ruthenium, ...` |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | Regulation (EU) 2024/1252, Annex II: `The following raw materials shall be considered critical: ... (aa) platinum group metals`. Ruthenium is part of the PGM group. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | verified | Regulation (EU) 2024/1252, Annex I: `The following raw materials shall be considered strategic: ... (m) platinum group metals`. Ruthenium is part of the PGM group. |
| geopolitical_events[0].impact "179,000→170,000 kg (−5%); 208,000→190,000 kg (−9%)" | 179000→170000 / -5 pct / 208000→190000 / -9 pct | usgs_mcs_2025_pgm | inferred | The table reports `179,000` and `170,000` for platinum, `208,000` and `190,000` for palladium. The -5% and -9% changes are derived arithmetic, not quoted as percentages. |
| geopolitical_events[0].impact "~75% of world Ru; price ~$440/troy oz" | 75 pct / 440 USD_per_troy_oz | usgs_mcs_2025_pgm | inferred | USGS directly reports Ru 2024 price `440` and South Africa Pt `120,000`/world Pt `170,000`, but it does not publish a 75% world Ru mining share. |
| geopolitical_events[1].impact "87,000→75,000 kg (−14%); 21,000→18,000 kg (−14%)" | 87000→75000 / -14 pct / 21000→18000 / -14 pct | usgs_mcs_2025_pgm | inferred | The table reports Russian palladium `87,000 75,000` and platinum `21,000 18,000`; the -14% changes are derived arithmetic, not quoted percentages. |
| geopolitical_events[1].impact "~12% of world Ru" | 12 pct | usgs_mcs_2025_pgm | inferred | USGS does not publish a 12% elemental Ru share for Russia; this is an inferred Ru allocation layered on top of grouped PGM production. |
| geopolitical_events[2].event | -6 pct / -27 pct / -31 pct | usgs_mcs_2025_pgm | verified | Events section: `the estimated annual average prices for rhodium decreased by 31% ... by 27% for palladium, by 6% for ruthenium`. |
| geopolitical_events[2].impact "466.49→440/troy oz (−6%)" | 466.49→440 USD_per_troy_oz / -6 pct | usgs_mcs_2025_pgm | verified | Salient statistics price row lists `Ruthenium 271.83 576.12 577.02 466.49 440`; the events section separately states Ru was down `6%`. |
| prices[0].value | 440 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient statistics: `Ruthenium 271.83 576.12 577.02 466.49 440`. |
| prices[1].value | 466.49 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient statistics: `Ruthenium 271.83 576.12 577.02 466.49 440`. |
| prices[2].value | 577.02 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient statistics: `Ruthenium 271.83 576.12 577.02 466.49 440`. |
| prices[3].value | 576.12 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient statistics: `Ruthenium 271.83 576.12 577.02 466.49 440`. |
| prices[4].value | 271.83 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | Salient statistics: `Ruthenium 271.83 576.12 577.02 466.49 440`. |

## Notes

Primary-source verification used the USGS Mineral Commodity Summaries 2025 platinum-group-metals chapter, the 2022 Federal Register notice for the U.S. critical-minerals list, and Regulation (EU) 2024/1252 for EU critical/strategic status.

The ruthenium file relies heavily on grouped PGM source data. USGS does not publish elemental Ru mine production, country production shares, elemental reserves, or end-use percentages in this chapter, so those claims are necessarily `inferred` when they are arithmetic/estimation layers on top of grouped Pd/Pt/PGM values.

Two numeric claims are unsupported by the cited USGS chapter and were marked `discrepancy`: the hard-disk interlayer thickness (`0.2–0.6 nm`, `1–3 atomic layers`) and the Bushveld ore-grade ranges (`0.3–0.5 g/t` and `0.1–0.2 g/t`). The underlying qualitative applications/geology are directionally consistent with broader literature, but those figures are not in the cited source.

The `usgs_critical_minerals_2022` source URL embedded in `Ru.yaml` points to a May 20, 2022 PDF that is not the actual 2022 final list notice. The official final-list document is the February 24, 2022 Federal Register notice `2022-04027`; that document explicitly lists `ruthenium`.

The `eu_crma_2024` URL in `Ru.yaml` can be flaky via the direct EUR-Lex `legal-content` path, but the regulation text is available through EUR-Lex/ELI search results and clearly lists `platinum group metals` in both Annex I (strategic) and Annex II (critical).

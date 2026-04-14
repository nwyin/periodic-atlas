# Verification: Rh

- Element: rhodium (Rh)
- Snapshot year: 2025
- Verifier: worker-8f741f462ae1 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 9 |
| discrepancy | 1 |
| inferred | 20 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 22300 kg_per_year | implats_annual_report_2024 | inferred | Implats' rhodium supply table gives `Primary ... 717` koz for 2024. The YAML's `22,300 kg` is a unit conversion from 717 koz to about 22.3 t, not a directly tabulated value. |
| production[0].mine.notes | ~5 pct basket share; 717,000 troy oz; ~22.3 tonnes | implats_annual_report_2024 | inferred | The source directly gives `Primary ... 717` koz for 2024, but it does not state a `~5%` basket share or `22.3 tonnes`; those are analyst derivations layered on the table value. |
| production[0].mining_by_country.shares[0] | ZA 82.6 pct; 18400 kg_per_year; 592 koz of 717 koz; ~18.4 tonnes | implats_annual_report_2024 | inferred | Implats' 2024 supply table lists `South Africa ... 592` and `Primary ... 717`. The `82.6%` share and `18,400 kg` / `18.4 tonnes` are arithmetic conversions from those source values. |
| production[0].mining_by_country.shares[1] | RU 8.4 pct; 1900 kg_per_year; 60 koz; ~1.9 tonnes | implats_annual_report_2024 | inferred | Implats lists `Russian sales ... 60` and `Primary ... 717`. The `8.4%` share and `1,900 kg` / `1.9 tonnes` are derived from the table, not stated verbatim. |
| production[0].mining_by_country.shares[2] | ZW 6.3 pct; 1400 kg_per_year; 45 koz; ~1.4 tonnes | implats_annual_report_2024 | inferred | Implats lists `Zimbabwe ... 45` and `Primary ... 717`. The `6.3%` share and `1,400 kg` / `1.4 tonnes` are arithmetic conversions from those values. |
| production[0].mining_by_country.shares[3] | ZZ 2.7 pct; 600 kg_per_year; North America 14 koz + Others 5 koz; ~0.6 tonnes | implats_annual_report_2024 | inferred | Implats lists `North America ... 14`, `Others ... 5`, and `Primary ... 717`. The YAML's residual `2.7%` and `600 kg` / `0.6 tonnes` are derived from combining those lines. |
| production[0].refining_by_country.shares[0] | ZA 65 pct | implats_annual_report_2024 | inferred | The source rhodium page contains a supply table with `South Africa ... 592`, `Zimbabwe ... 45`, `North America ... 14`, `Russian sales ... 60`, and `Others ... 5`, but it does not publish refinery-country shares. The `65%` refining split is estimator-added. |
| production[0].refining_by_country.shares[1] | RU 10 pct | implats_annual_report_2024 | inferred | The Implats appendix gives mined/sales supply lines, not a refinery-country table, so the `10%` Russian refining share is inferred rather than reported. |
| production[0].refining_by_country.shares[2] | BE 10 pct | implats_annual_report_2024 | inferred | No Belgium rhodium refinery share appears in the cited appendix; the `10%` figure is an analyst estimate. |
| production[0].refining_by_country.shares[3] | DE 8 pct | implats_annual_report_2024 | inferred | No Germany rhodium refinery share appears in the cited appendix; the `8%` figure is an analyst estimate. |
| production[0].refining_by_country.shares[4] | ZZ 7 pct | implats_annual_report_2024 | inferred | The appendix does not tabulate an `other refining centers` rhodium share, so the `7%` residual is inferred. |
| reserves.economic_reserves | 4200 tonnes; >81,000 tonnes; 81,000,000 kg; ~5 pct basket share | usgs_mcs_2025_pgm | inferred | USGS reports `World total (rounded) 208,000 190,000 179,000 170,000 >81,000,000` and `World resources of PGMs are estimated to total more than 100 million kilograms.` The YAML's `4,200 tonnes` is a rhodium-share derivation from grouped PGM reserves, not a reported rhodium reserve figure. |
| reserves.resources | 5200 tonnes; >100,000 tonnes; ~5 pct share | usgs_mcs_2025_pgm | inferred | USGS states `World resources of PGMs are estimated to total more than 100 million kilograms.` The YAML's `5,200 tonnes` is a derived rhodium-share estimate rather than a published rhodium resource total. |
| reserves.reserves_by_country.shares[0] | ZA 77.5 pct; 63,000 tonnes of >81,000 tonnes | usgs_mcs_2025_pgm | inferred | USGS lists `South Africa 74,900 72,000 125,000 120,000 63,000,000` and world reserves `>81,000,000`. The `77.5%` reserve share is arithmetic from grouped PGM reserves, not a stated rhodium-country share. |
| reserves.reserves_by_country.shares[1] | RU 19.7 pct; 16,000 tonnes | usgs_mcs_2025_pgm | inferred | USGS lists `Russiae 87,000 75,000 21,000 18,000 1016,000,000`; the `16,000,000` reserve line supports the note, but the YAML's `19.7%` rhodium share is derived from grouped PGM reserves. |
| reserves.reserves_by_country.shares[2] | ZW 1.5 pct; 1,200 tonnes | usgs_mcs_2025_pgm | inferred | USGS lists `Zimbabwe 15,900 15,000 19,200 19,000 1,200,000`. The `1,200 tonnes` note is consistent with the table, while `1.5%` is a derived share. |
| reserves.reserves_by_country.shares[3] | US 1.0 pct; 820 tonnes | usgs_mcs_2025_pgm | inferred | USGS lists `United States 10,300 8,000 3,040 2,000 820,000`. The `820 tonnes` note matches the grouped PGM reserve line; the `1.0%` share is derived. |
| reserves.reserves_by_country.shares[4] | CA 0.4 pct; 310 tonnes | usgs_mcs_2025_pgm | inferred | USGS lists `Canada 16,100 15,000 5,170 5,200 310,000`. The `310 tonnes` note matches the grouped reserve figure; the `0.4%` share is derived. |
| end_uses.uses[0] | 85.2 pct; automotive 918 koz of total demand 1,077 koz | implats_annual_report_2024 | inferred | Implats' demand table lists `Automotive ... 918` and `Total demand ... 1 077` for 2024. The YAML's `85.2%` is arithmetic from those table values. |
| end_uses.uses[1] | 14.8 pct; other industrial 159 koz of total demand 1,077 koz | implats_annual_report_2024 | inferred | Implats lists `Other industrial ... 159` and `Total demand ... 1 077` for 2024. The YAML's `14.8%` is derived from those values. |
| prices[0].value | 11205.06 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | USGS price row: `Rhodium 11,205.06 20,254.10 15,585.00 6,660.58 4,600`. |
| prices[1].value | 20254.10 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | USGS price row: `Rhodium 11,205.06 20,254.10 15,585.00 6,660.58 4,600`. |
| prices[2].value | 15585.00 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | USGS price row: `Rhodium 11,205.06 20,254.10 15,585.00 6,660.58 4,600`. |
| prices[3].value | 6660.58 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | USGS price row: `Rhodium 11,205.06 20,254.10 15,585.00 6,660.58 4,600`. |
| prices[4].value | 4600 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | USGS price row: `Rhodium 11,205.06 20,254.10 15,585.00 6,660.58 4,600`. |
| prices[4].notes | 31 pct decline from 2023 | usgs_mcs_2025_pgm | verified | USGS events text: `the estimated annual average prices for rhodium decreased by 31% ... compared with annual average prices in 2023.` |
| geopolitical_events[2].impact | 4000 -> 5500 -> 4650 usd_per_troy_oz | implats_annual_report_2024 | verified | Implats states: `Rhodium opened at US$4 000 per ounce ... a short-lived price squeeze in October resulted in a peak of US$5 500 per ounce. The closing price of US$4 650 per ounce...` |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_2022 | verified | The 2022 final list notice says the list `includes the following 50 minerals` and explicitly includes `... palladium, platinum, praseodymium, rhodium, rubidium, ruthenium ...`. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | Regulation (EU) 2024/1252 Annex II states `The following raw materials shall be considered critical` and includes `(aa) platinum group metals`. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | discrepancy | Regulation (EU) 2024/1252 Annex I states `The following raw materials shall be considered strategic` and includes `(m) platinum group metals`, so the YAML's `false` conflicts with the cited regulation. |

## Notes

USGS MCS 2025 was directly fetchable and supports the rhodium price series, grouped PGM reserve/resource totals, grouped country reserve figures, the 2024 rhodium price decline, and the qualitative substitute/feedstock framing. It does not publish elemental rhodium mine output, rhodium country production shares, rhodium refinery-country shares, or rhodium-specific reserve/resource tonnages, so those YAML values are necessarily `inferred` when they are conversions or basket-share allocations from grouped PGM data.

The Implats appendix content was available through search-indexed excerpts of the cited PDF URL and the matching 2024 integrated-report appendix content. Those excerpts support the rhodium demand, supply, and price-path numerators/denominators (`717`, `592`, `60`, `45`, `14`, `5`, `918`, `159`, `1 077`, `US$4 000`, `US$5 500`, `US$4 650`), but the YAML's percentages and kilogram/tonne figures are arithmetic transformations rather than direct table entries.

`criticality.eu_strategic_list_as_of_2024` appears wrong against the cited EU regulation: Annex I explicitly lists `platinum group metals` as strategic. The YAML field is also unsourced, but it is still a substantive mismatch worth flagging for a later authoring pass.

The feedstock-origins and substitutes sections carry source IDs but no distinct numeric claims, so they do not add rows under the numeric-claims invariant for this report.

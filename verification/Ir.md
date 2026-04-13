# Verification: Ir

- Element: iridium (Ir)
- Snapshot year: 2025
- Verifier: worker-4b1b8dacf505 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 28 |
| discrepancy | 3 |
| inferred | 13 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 8200 kg_per_year | doe_pgm_supply_chain_2022 | inferred | "world production of Ir was 8.17 tonnes" — DOE p.40; YAML rounds to 8,200 kg |
| production[0].mine.notes (2020 world iridium production) | 8.17 metric tons | doe_pgm_supply_chain_2022 | verified | "world production of Ir was 8.17 tonnes" — DOE p.40 |
| production[0].mine.notes (representative UG2 Pt grade) | 2.0 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (representative UG2 Pd grade) | 1.3 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (representative UG2 Rh grade) | 0.34 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (representative UG2 Ru grade) | 0.45 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (representative UG2 Ir grade) | 0.13 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (representative UG2 Os grade) | 0.05 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| production[0].mine.notes (iridium basket share) | about 3% | doe_pgm_supply_chain_2022 | inferred | Not stated directly; 0.13 / (2 + 1.3 + 0.34 + 0.45 + 0.13 + 0.05) = 3.05% from DOE Table 3 p.23 |
| production[0].mining_by_country.shares[ZA].share_pct | 83.0 | doe_pgm_supply_chain_2022 | verified | "South Africa 33.9% 67.6% 83.0%" — DOE Table A2 p.65 |
| production[0].mining_by_country.shares[ZW].share_pct | 10.2 | doe_pgm_supply_chain_2022 | verified | "Zimbabwe 5.9% 9.1% 10.2%" — DOE Table A2 p.65 |
| production[0].mining_by_country.shares[CA].share_pct | 3.7 | doe_pgm_supply_chain_2022 | verified | "Canada 9.2% 4.2% 3.7%" — DOE Table A2 p.65 |
| production[0].mining_by_country.shares[RU].share_pct | 3.1 | doe_pgm_supply_chain_2022 | verified | "Russia 42.9% 13.9% 3.1%" — DOE Table A2 p.65 |
| reserves.economic_reserves.notes (world PGM reserves) | >81,000,000 kg | usgs_mcs_2025_pgm | verified | "World total (rounded) ... >81,000,000" — USGS MCS 2025 p.140 |
| reserves.economic_reserves.value | 2430000 kg | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies ~3% basket share to USGS world PGM reserves >81,000,000 kg |
| reserves.resources.notes (world PGM resources) | >100,000,000 kg | usgs_mcs_2025_pgm | verified | "resources ... more than 100 million kilograms" — USGS MCS 2025 p.140 |
| reserves.resources.value | 3000000 kg | usgs_mcs_2025_pgm | inferred | Not stated directly; YAML applies ~3% basket share to USGS world PGM resources >100,000,000 kg |
| reserves.reserves_by_country.shares[ZA].share_pct | 77.8 | usgs_mcs_2025_pgm | inferred | Not stated directly; 63,000,000 / 81,000,000 = 77.8% from USGS p.140 |
| reserves.reserves_by_country.shares[RU].share_pct | 19.8 | usgs_mcs_2025_pgm | inferred | Not stated directly; 16,000,000 / 81,000,000 = 19.8% from USGS p.140 |
| reserves.reserves_by_country.shares[ZW].share_pct | 1.5 | usgs_mcs_2025_pgm | inferred | Not stated directly; 1,200,000 / 81,000,000 = 1.5% from USGS p.140 |
| reserves.reserves_by_country.shares[US].share_pct | 1.0 | usgs_mcs_2025_pgm | inferred | Not stated directly; 820,000 / 81,000,000 = 1.0% from USGS p.140 |
| reserves.reserves_by_country.shares[CA].share_pct | 0.4 | usgs_mcs_2025_pgm | inferred | Not stated directly; 310,000 / 81,000,000 = 0.4% from USGS p.140 |
| end_uses.uses[electrochemical_applications].share_pct | 36 | doe_pgm_supply_chain_2022 | inferred | Not stated directly; 3.0 / 8.3 = 36.1% from DOE Table A1 p.64 |
| end_uses.uses[electrochemical_applications].notes (2021 gross demand) | 3.0 metric tons | doe_pgm_supply_chain_2022 | verified | "Electrochemical ... 3" — DOE Table A1 p.64 |
| end_uses.uses[other_industrial].share_pct | 32 | doe_pgm_supply_chain_2022 | inferred | Not stated directly; 2.7 / 8.3 = 32.5% from DOE Table A1 p.64 |
| end_uses.uses[other_industrial].notes (2021 gross demand) | 2.7 metric tons | doe_pgm_supply_chain_2022 | verified | "Other ... 2.7" — DOE Table A1 p.64 |
| end_uses.uses[electronics].share_pct | 22 | doe_pgm_supply_chain_2022 | inferred | Not stated directly; 1.8 / 8.3 = 21.7% from DOE Table A1 p.64 |
| end_uses.uses[electronics].notes (2021 gross demand) | 1.8 metric tons | doe_pgm_supply_chain_2022 | verified | "Electronics ... 1.8" — DOE Table A1 p.64 |
| end_uses.uses[chemical_catalysts].share_pct | 10 | doe_pgm_supply_chain_2022 | inferred | Not stated directly; 0.8 / 8.3 = 9.6% from DOE Table A1 p.64 |
| end_uses.uses[chemical_catalysts].notes (2021 gross demand) | 0.8 metric tons | doe_pgm_supply_chain_2022 | verified | "Chemical ... 0.8" — DOE Table A1 p.64 |
| feedstock_origins[ug2_chromitite_reef].notes (Pt grade) | 2.0 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[ug2_chromitite_reef].notes (Pd grade) | 1.3 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[ug2_chromitite_reef].notes (Rh grade) | 0.34 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[ug2_chromitite_reef].notes (Ru grade) | 0.45 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[ug2_chromitite_reef].notes (Ir grade) | 0.13 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[ug2_chromitite_reef].notes (Os grade) | 0.05 g/t | doe_pgm_supply_chain_2022 | verified | "UG2 2 1.3 0.34 0.45 0.13 0.05" — DOE Table 3 p.23 |
| feedstock_origins[merensky_reef_pgm_ore].notes (Ir grade) | 0.05 g/t | doe_pgm_supply_chain_2022 | verified | "Merensky Reef 2.7 1.4 0.16 0.33 0.05 0.04" — DOE Table 3 p.23 |
| substitutes[1].notes | 85% iridium reduction | heraeus_ruthenium_pem_catalyst_2023 | verified | "85% saving on iridium" — Heraeus press release, 2023-11-14 |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2022 | verified | "includes ... iridium" — 2022 Final List of Critical Minerals notice |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_annex_2024 | verified | "Annex II ... platinum group metals" — EUR-Lex Regulation (EU) 2024/1252 |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_annex_2024 | verified | "Annex I ... platinum group metals" — EUR-Lex Regulation (EU) 2024/1252 |
| prices[2024].value | 4800 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "Price, dollars per troy ounce, average ... 4,800.00" — USGS MCS 2025 p.140 |
| prices[2024].notes | up about 3% from 2023 | usgs_mcs_2025_pgm | verified | "price for iridium in 2024 increased by 3%" — USGS MCS 2025 p.140 |
| prices[2023].value | 4672.78 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "2023 ... 4,672.78" — USGS MCS 2025 p.140 |
| prices[2022].value | 4581.93 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "2022 ... 4,581.93" — USGS MCS 2025 p.140 |
| prices[2021].value | 5158.4 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "2021 ... 5,158.40" — USGS MCS 2025 p.140 |
| prices[2020].value | 1633.51 usd_per_troy_oz | usgs_mcs_2025_pgm | verified | "2020 ... 1,633.51" — USGS MCS 2025 p.140 |
| geopolitical_events[0].date | 2024-01 | usgs_mcs_2025_pgm | discrepancy | USGS p.140 describes 2024 South African output decline but gives no January 2024 event date |
| geopolitical_events[1].date | 2024-01 | usgs_mcs_2025_pgm | discrepancy | USGS p.140 describes 2024 Russian output decline but gives no January 2024 event date |
| geopolitical_events[2].date | 2024-06 | heraeus_mccol_2024 | discrepancy | Cited page is dated "10/07/2024" and says "Recently acquired by Heraeus" rather than documenting June 2024 directly |

## Notes

Most of the iridium-specific mine-share, end-use, and ore-grade claims are supported cleanly by DOE's appendix tables and Table 3. The standalone mine quantity and the reserve/resource tonnages are not directly tabulated by the cited sources; they are derived from reported PGM totals and are correctly marked `inferred`.

All five price points match the USGS platinum-group-metals chapter. The reserve-share percentages also reconcile numerically against the USGS reserve table, but they are computed from combined PGM reserve tonnages rather than explicitly stated as iridium shares, so they remain `inferred`.

The three geopolitical event dates are the only clear source mismatches. The cited USGS page supports the underlying 2024 South Africa and Russia production-decline narratives, but not the exact `2024-01` month stamps. The cited Heraeus URL supports McCol's iridium-recycling relevance, but the page itself is an October 7, 2024 brand-integration announcement, not the June 2024 acquisition announcement.

# Verification: Ge

- Element: germanium (Ge)
- Snapshot year: 2025
- Verifier: worker-7bbacd3db2d0 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 36 |
| discrepancy | 0 |
| inferred | 4 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 210 tonnes_per_year | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 Table 1.14: "Estimated world production of primary germanium by country, in 2022" with total "210" metric tons; text says 2022 estimates were "based on the best available information" |
| production[0].refining_by_country.shares[BE].quantity.value | 4 tonnes_per_year | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 Table 1.14 row: "Belgium 4 10" |
| production[0].refining_by_country.shares[BE].share_pct | 1.9% | usgs_ofr_2024_germanium_restrictions | inferred | Source gives Belgium quantity 4 t and world total 210 t in Table 1.14; 4/210 = 1.9% |
| production[0].refining_by_country.shares[CA].quantity.value | 20 tonnes_per_year | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 Table 1.14 row: "Canada 20 30" |
| production[0].refining_by_country.shares[CA].share_pct | 9.5% | usgs_ofr_2024_germanium_restrictions | inferred | Source gives Canada quantity 20 t and world total 210 t in Table 1.14; 20/210 = 9.5% |
| production[0].refining_by_country.shares[CN].quantity.value | 180 tonnes_per_year | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 Table 1.14 row: "China 180 309" |
| production[0].refining_by_country.shares[CN].share_pct | 85.7% | usgs_ofr_2024_germanium_restrictions | inferred | Source gives China quantity 180 t and world total 210 t in Table 1.14; 180/210 = 85.7% |
| production[0].refining_by_country.shares[RU].quantity.value | 6 tonnes_per_year | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 Table 1.14 row: "Russia 6 20" |
| production[0].refining_by_country.shares[RU].share_pct | 2.9% | usgs_ofr_2024_germanium_restrictions | inferred | Source gives Russia quantity 6 t and world total 210 t in Table 1.14; 6/210 = 2.9% |
| feedstock_origins[0].substrate | zinc_smelter_residues | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 background text: "Germanium is also recovered during the leaching of certain zinc smelter residues" |
| feedstock_origins[1].substrate | coal_ash | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 background text: "Germanium is also recovered ... from coal ash" |
| feedstock_origins[2].substrate | lead_zinc_copper_sulfide_ores | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "The available resources of germanium are associated with certain zinc and lead-zinc-copper sulfide ores" |
| feedstock_origins[3].substrate | lignite_coal_deposits | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "The available resources of germanium are associated with certain ... lignite coal deposits." |
| substitutes[0].application | electronics | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "Silicon or gallium arsenide substitute for germanium in certain electronic applications." |
| substitutes[1].application | high_frequency_electronics | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "Some metallic compounds can be substituted in high-frequency electronics applications" |
| substitutes[2].application | light_emitting_diodes | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "Some metallic compounds can be substituted ... in some light-emitting-diode applications." |
| substitutes[3].application | infrared_optics | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "Chalcogenide glass has been used as a substitute for germanium metal in infrared applications." |
| substitutes[4].application | polymerization_catalysts | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "Antimony and titanium are substitutes for use as polymerization catalysts." |
| end_uses.uses[fiber_optics].share_pct | 40% | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 germanium applications text: "40 percent in fiber optics" |
| end_uses.uses[infrared_optics].share_pct | 30% | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 germanium applications text: "30 percent in infrared optics" |
| end_uses.uses[electronics_and_solar].share_pct | 20% | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 germanium applications text: "20 percent in electronics and solar applications" |
| end_uses.uses[other].share_pct | 10% | usgs_ofr_2024_germanium_restrictions | verified | OFR 2024-1057 germanium applications text: "10 percent in other uses" |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_2025_critical_minerals | verified | Federal Register final 2025 list says the 60 critical minerals include "gallium, germanium, graphite..." published 2025-11-07 |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | Regulation (EU) 2024/1252 Annex II Section 1 lists critical raw materials and includes "germanium" |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | verified | Regulation (EU) 2024/1252 Annex I Section 1 lists strategic raw materials and includes "germanium" |
| prices[2024,metal].value | 2100 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium metal 1,046 1,187 1,294 1,392 2,100" |
| prices[2023,metal].value | 1392 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium metal 1,046 1,187 1,294 1,392 2,100" |
| prices[2022,metal].value | 1294 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium metal 1,046 1,187 1,294 1,392 2,100" |
| prices[2021,metal].value | 1187 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium metal 1,046 1,187 1,294 1,392 2,100" |
| prices[2020,metal].value | 1046 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium metal 1,046 1,187 1,294 1,392 2,100" |
| prices[2024,dioxide].value | 1400 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium dioxide 724 770 828 883 1,400" |
| prices[2023,dioxide].value | 883 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium dioxide 724 770 828 883 1,400" |
| prices[2022,dioxide].value | 828 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium dioxide 724 770 828 883 1,400" |
| prices[2021,dioxide].value | 770 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium dioxide 724 770 828 883 1,400" |
| prices[2020,dioxide].value | 724 usd_per_kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.80 price table: "Germanium dioxide 724 770 828 883 1,400" |
| geopolitical_events[0].date | 2023-08 | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "In August 2023, the Government of China implemented an export licensing program for germanium." |
| geopolitical_events[0].impact | exports down 55% to 16,700 kg | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "China's reported exports of germanium metal for the year through August 2024 decreased by 55% to 16,700 kilograms" |
| geopolitical_events[1].date | 2024-04 | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "In April, the U.S. Department of Defense awarded a company $14.4 million" |
| geopolitical_events[1].event | $14.4 million wafer manufacturing award | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "awarded a company $14.4 million to expand and upgrade its germanium wafer manufacturing capabilities" |
| geopolitical_events[2].date | 2024-05 | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "In May, a germanium processor in Belgium and a company in Congo (Kinshasa) entered into a long-term agreement" |
| geopolitical_events[3].date | 2024-12 | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "In December 2024, China banned all exports of germanium to the United States." |
| geopolitical_events[3].impact | >94% of year-to-August imports from BE/DE/CA/CN | usgs_mcs_2025_germanium | verified | MCS 2025 p.81: "More than 94% of total imports of metal and dioxide ... through August were from Belgium, Germany, Canada, and China" |

## Notes

`elements/Ge.yaml` is absent from this worktree at `HEAD`, so verification was performed against the historical author version at commit `5eab3766dbb77893fc3fe1d64a195dd7d439ae22` via `git show`, consistent with prior worker notes.

No reserves rows appear in the claims table because `Ge.yaml` contains no reserve quantities with a `source_id`. The reserves section is descriptive only: MCS 2025 says reserves data are not widely reported and are difficult to quantify.

The four country `share_pct` values under `production[0].refining_by_country` are not stated in the OFR source; they are straightforward arithmetic from Table 1.14 country quantities over the reported 210 t world total, so they are marked `inferred`.

The Federal Register source confirms U.S. critical-list membership directly. The EU CRMA source confirms both Annex I strategic and Annex II critical-list membership directly.

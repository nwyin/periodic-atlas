# Verification: Be

- Element: beryllium (Be)
- Snapshot year: 2025
- Verifier: worker-6cf60668382c (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 31 |
| discrepancy | 0 |
| inferred | 8 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 180 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Production, mine shipments 165 175 175 185 180" — USGS MCS 2025 beryllium chapter, Salient Statistics table, 2024e column |
| production[0].mining_by_country[US].quantity.value | 180 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "United States 185 180" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[US].share_pct | 50.0 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; US share is inferred from table values: 180 / 360 = 50.0% using "United States 185 180" and "World total (rounded) 325 360" |
| production[0].mining_by_country[BR].quantity.value | 80 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Brazil e40 80" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 22.22 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; Brazil share is inferred from table values: 80 / 360 = 22.22% using "Brazil e40 80" and "World total (rounded) 325 360" |
| production[0].mining_by_country[CN].quantity.value | 77 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "China e74 77" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 21.39 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; China share is inferred from table values: 77 / 360 = 21.39% using "China e74 77" and "World total (rounded) 325 360" |
| production[0].mining_by_country[MZ].quantity.value | 24 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Mozambique 23 24" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[MZ].share_pct | 6.67 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; Mozambique share is inferred from table values: 24 / 360 = 6.67% using "Mozambique 23 24" and "World total (rounded) 325 360" |
| production[0].mining_by_country[MG].quantity.value | 1 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Madagascar e1 1" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[MG].share_pct | 0.28 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; Madagascar share is inferred from table values: 1 / 360 = 0.277...% ≈ 0.28% using "Madagascar e1 1" and "World total (rounded) 325 360" |
| production[0].mining_by_country[RW].quantity.value | 1 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Rwanda e1 1" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[RW].share_pct | 0.28 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; Rwanda share is inferred from table values: 1 / 360 = 0.277...% ≈ 0.28% using "Rwanda e1 1" and "World total (rounded) 325 360" |
| production[0].mining_by_country[UG].quantity.value | 1 tonnes_per_year | usgs_mcs_2025_beryllium | verified | "Uganda e1 1" — USGS MCS 2025 World Mine Production table, 2024e column |
| production[0].mining_by_country[UG].share_pct | 0.28 | usgs_mcs_2025_beryllium | inferred | Not stated explicitly; Uganda share is inferred from table values: 1 / 360 = 0.277...% ≈ 0.28% using "Uganda e1 1" and "World total (rounded) 325 360" |
| reserves.economic_reserves.value | 19000 tonnes | usgs_mcs_2025_beryllium | verified | "Proven and probable bertrandite reserves in Utah total about 19,000 tons of beryllium content." — USGS MCS 2025 Reserves section |
| reserves.resources.value | 100000 tonnes | usgs_mcs_2025_beryllium | inferred | The source gives a lower bound, not an exact point estimate: "The world’s identified resources of beryllium have been estimated to be more than 100,000 tons." YAML encodes the floor value `100000` with `approximate: true`. |
| reserves.resources.notes (about 60% in the United States) | 60% | usgs_mcs_2025_beryllium | verified | "About 60% of these resources are in the United States" — USGS MCS 2025 World Resources |
| end_uses.uses[industrial_components].share_pct | 20 | usgs_mcs_2025_beryllium | verified | "approximately 20% of beryllium products were used in industrial components" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[aerospace_and_defense].share_pct | 19 | usgs_mcs_2025_beryllium | verified | "19% in aerospace and defense applications" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[automotive_electronics].share_pct | 11 | usgs_mcs_2025_beryllium | verified | "11% in automotive electronics" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[telecommunications_infrastructure].share_pct | 8 | usgs_mcs_2025_beryllium | verified | "8% in telecommunications infrastructure" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[consumer_electronics].share_pct | 6 | usgs_mcs_2025_beryllium | verified | "6% each in consumer electronics and energy applications" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[energy_applications].share_pct | 6 | usgs_mcs_2025_beryllium | verified | "6% each in consumer electronics and energy applications" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[semiconductor_applications].share_pct | 2 | usgs_mcs_2025_beryllium | verified | "2% in semiconductor applications" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[other_applications].share_pct | 28 | usgs_mcs_2025_beryllium | verified | "28% in other applications" — USGS MCS 2025 Domestic Production and Use |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2025 | verified | "The final 2025 List of Critical Minerals ... includes the following 60 minerals: aluminum, antimony, arsenic, barite, beryllium, ..." — Federal Register final 2025 list |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | "Annex II ... The following raw materials shall be considered critical: ... (e) beryllium" — Regulation (EU) 2024/1252, Annex II, Section 1 |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | Annex I, Section 1 lists the strategic raw materials from "(a) bauxite/alumina/aluminium" through "(q) tungsten" and does not include beryllium; Annex II separately lists "(e) beryllium" as critical. |
| prices[year=2024].value | 1500 usd_per_kg | usgs_mcs_2025_beryllium | verified | "Price ... dollars per kilogram of contained beryllium 620 680 660 1,400 1,500" — USGS MCS 2025 Salient Statistics table, 2024e column |
| prices[year=2023].value | 1400 usd_per_kg | usgs_mcs_2025_beryllium | verified | "Price ... dollars per kilogram of contained beryllium 620 680 660 1,400 1,500" — USGS MCS 2025 Salient Statistics table, 2023 column |
| prices[year=2022].value | 660 usd_per_kg | usgs_mcs_2025_beryllium | verified | "Price ... dollars per kilogram of contained beryllium 620 680 660 1,400 1,500" — USGS MCS 2025 Salient Statistics table, 2022 column |
| prices[year=2021].value | 680 usd_per_kg | usgs_mcs_2025_beryllium | verified | "Price ... dollars per kilogram of contained beryllium 620 680 660 1,400 1,500" — USGS MCS 2025 Salient Statistics table, 2021 column |
| prices[year=2020].value | 620 usd_per_kg | usgs_mcs_2025_beryllium | verified | "Price ... dollars per kilogram of contained beryllium 620 680 660 1,400 1,500" — USGS MCS 2025 Salient Statistics table, 2020 column |
| geopolitical_events[0].date | 2010 | usgs_mcs_2025_beryllium | verified | "In 2010, under the Defense Production Act, Title III program, a public-private partnership ... reestablished domestic production of beryllium metal." — USGS MCS 2025 Domestic Production and Use |
| geopolitical_events[1].date | 2024 | usgs_mcs_2025_beryllium | verified | "Apparent consumption in 2024 increased by 18% from that in 2023" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[1].impact (apparent consumption rose 18%) | 18% | usgs_mcs_2025_beryllium | verified | "Apparent consumption in 2024 increased by 18% from that in 2023" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[1].impact (exports fell 56%) | 56% | usgs_mcs_2025_beryllium | verified | "owing primarily to a 56% decrease in estimated beryllium exports" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[1].impact (imports fell 20%) | 20% | usgs_mcs_2025_beryllium | verified | "offset by a 20% decrease in estimated imports" — USGS MCS 2025 Events, Trends, and Issues |

## Notes

All sourced numeric claims in `elements/Be.yaml` are either directly stated in the cited primary source or are straightforward share calculations from the USGS world mine table. No discrepancies were found.

`reserves.resources.value` is the only non-exact numeric encoding. The source says "more than 100,000 tons"; the YAML stores `100000` with `approximate: true`, so the claim is best classified as `inferred` rather than `verified`.

`feedstock_origins` and `substitutes` both carry `source_id: usgs_mcs_2025_beryllium`, but they contain no distinct numeric claims. Their qualitative wording matches the source text: feedstock origin matches "One company in Utah mined bertrandite ore and converted it, along with imported beryl, into beryllium hydroxide," and substitutes match the USGS Substitutes paragraph listing composites, aluminum, pyrolytic graphite, silicon carbide, steel, titanium, nickel-silicon/tin/titanium copper alloys, phosphor bronze, aluminum nitride, and boron nitride.

The criticality section contains boolean rather than numeric claims. They were still checked because the task scope explicitly included criticality flags. The U.S. 2025 Federal Register list explicitly names beryllium. The EU CRMA source explicitly lists beryllium in Annex II and omits it from Annex I, so `eu_crm_list_as_of_2024: true` and `eu_strategic_list_as_of_2024: false` are both supported.

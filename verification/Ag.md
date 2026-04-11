# Verification: Ag

- Element: silver (Ag)
- Snapshot year: 2025
- Verifier: worker-2ecb267925ca (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 69 |
| discrepancy | 0 |
| inferred | 28 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 25000 tonnes_per_year | usgs_mcs_2025_silver | verified | "World total (rounded) … 25,000" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mine.notes (2023 world total = 25,500) | 25500 tonnes_per_year | usgs_mcs_2025_silver | verified | "World silver mine production decreased in 2024 to an estimated 25,000 tons compared with 25,500 tons in 2023" — USGS MCS 2025 p.163 |
| production[0].mine.notes (US 2024e = 1,100) | 1100 tonnes_per_year | usgs_mcs_2025_silver | verified | "U.S. mines produced approximately 1,100 tons of silver" — USGS MCS 2025 p.162 Domestic Production; confirmed "1,100" in Salient Statistics table 2024e row |
| production[0].mine.notes (US 2023 = 1,020) | 1020 tonnes_per_year | usgs_mcs_2025_silver | verified | "Mine … 1,020" — USGS MCS 2025 p.162 Salient Statistics table, 2023 column |
| production[0].mine.notes (~6% increase US 2024) | ~6% | usgs_mcs_2025_silver | verified | "Domestic silver mine production was estimated to have increased by 6% in 2024" — USGS MCS 2025 p.163 |
| production[0].refined.value | 2400 tonnes_per_year | usgs_mcs_2025_silver | verified | "estimated total output of 2,400 tons from domestic and foreign ores and concentrates and from new and old scrap" — USGS MCS 2025 p.162; confirmed: Primary 1,200 + Secondary 1,200 = 2,400 in Salient Statistics |
| production[0].refined.notes (primary 1,200) | 1200 tonnes_per_year | usgs_mcs_2025_silver | verified | "Primary … 1,200" — USGS MCS 2025 p.162 Salient Statistics table, 2024e column |
| production[0].refined.notes (secondary 1,200) | 1200 tonnes_per_year | usgs_mcs_2025_silver | verified | "Secondary (new and old scrap) … 1,200" — USGS MCS 2025 p.162 Salient Statistics table, 2024e column |
| production[0].refined.notes (24 US refiners) | 24 | usgs_mcs_2025_silver | verified | "There were 24 U.S. refiners that reported production of commercial-grade silver" — USGS MCS 2025 p.162 |
| production[0].mining_by_country[MX].quantity.value | 6300 tonnes_per_year | usgs_mcs_2025_silver | verified | "Mexico … 6,300" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[MX].share_pct | 25.2 | usgs_mcs_2025_silver | inferred | Not stated; 6,300/25,000 = 25.20% |
| production[0].mining_by_country[CN].quantity.value | 3300 tonnes_per_year | usgs_mcs_2025_silver | verified | "China … 3,300" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 13.2 | usgs_mcs_2025_silver | inferred | Not stated; 3,300/25,000 = 13.20% |
| production[0].mining_by_country[PE].quantity.value | 3100 tonnes_per_year | usgs_mcs_2025_silver | verified | "Peru … 3,100" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[PE].share_pct | 12.4 | usgs_mcs_2025_silver | inferred | Not stated; 3,100/25,000 = 12.40% |
| production[0].mining_by_country[BO].quantity.value | 1300 tonnes_per_year | usgs_mcs_2025_silver | verified | "Bolivia … 1,300" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[BO].share_pct | 5.2 | usgs_mcs_2025_silver | inferred | Not stated; 1,300/25,000 = 5.20% |
| production[0].mining_by_country[PL].quantity.value | 1300 tonnes_per_year | usgs_mcs_2025_silver | verified | "Poland … 1,300" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[PL].share_pct | 5.2 | usgs_mcs_2025_silver | inferred | Not stated; 1,300/25,000 = 5.20% |
| production[0].mining_by_country[CL].quantity.value | 1200 tonnes_per_year | usgs_mcs_2025_silver | verified | "Chile … 1,200" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[CL].share_pct | 4.8 | usgs_mcs_2025_silver | inferred | Not stated; 1,200/25,000 = 4.80% |
| production[0].mining_by_country[RU].quantity.value | 1200 tonnes_per_year | usgs_mcs_2025_silver | verified | "Russia … 1,200" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 4.8 | usgs_mcs_2025_silver | inferred | Not stated; 1,200/25,000 = 4.80% |
| production[0].mining_by_country[US].quantity.value | 1100 tonnes_per_year | usgs_mcs_2025_silver | verified | "United States … 1,100" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[US].share_pct | 4.4 | usgs_mcs_2025_silver | inferred | Not stated; 1,100/25,000 = 4.40% |
| production[0].mining_by_country[US].notes (4 silver mines, 31 operations, 12 states) | 4 / 31 / 12 | usgs_mcs_2025_silver | verified | "Silver was produced at 4 silver mines and as a byproduct or coproduct from 31 domestic base- and precious-metal operations. Silver was produced in 12 States" — USGS MCS 2025 p.162 |
| production[0].mining_by_country[AU].quantity.value | 1000 tonnes_per_year | usgs_mcs_2025_silver | verified | "Australia … 1,000" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 4.0 | usgs_mcs_2025_silver | inferred | Not stated; 1,000/25,000 = 4.00% |
| production[0].mining_by_country[KZ].quantity.value | 1000 tonnes_per_year | usgs_mcs_2025_silver | verified | "Kazakhstan … 1,000" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[KZ].share_pct | 4.0 | usgs_mcs_2025_silver | inferred | Not stated; 1,000/25,000 = 4.00% |
| production[0].mining_by_country[IN].quantity.value | 800 tonnes_per_year | usgs_mcs_2025_silver | verified | "India … 800" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 3.2 | usgs_mcs_2025_silver | inferred | Not stated; 800/25,000 = 3.20% |
| production[0].mining_by_country[AR].quantity.value | 800 tonnes_per_year | usgs_mcs_2025_silver | verified | "Argentina … 800" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[AR].share_pct | 3.2 | usgs_mcs_2025_silver | inferred | Not stated; 800/25,000 = 3.20% |
| production[0].mining_by_country[SE].quantity.value | 400 tonnes_per_year | usgs_mcs_2025_silver | verified | "Sweden … 400" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[SE].share_pct | 1.6 | usgs_mcs_2025_silver | inferred | Not stated; 400/25,000 = 1.60% |
| production[0].mining_by_country[CA].quantity.value | 300 tonnes_per_year | usgs_mcs_2025_silver | verified | "Canada … 300" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 1.2 | usgs_mcs_2025_silver | inferred | Not stated; 300/25,000 = 1.20% |
| production[0].mining_by_country[ZZ].quantity.value | 2100 tonnes_per_year | usgs_mcs_2025_silver | verified | "Other countries … 2,100" — USGS MCS 2025 p.163 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 8.4 | usgs_mcs_2025_silver | inferred | Not stated; 2,100/25,000 = 8.40% |
| production[0].notes (country sum 25,200; world total rounded 25,000) | 25200 vs 25000 | usgs_mcs_2025_silver | verified | Individual country 2024e column sums to 25,200 mt; table header reads "World total (rounded) … 25,000" — USGS MCS 2025 p.163 |
| reserves.economic_reserves.value | 640000 tonnes | usgs_mcs_2025_silver | verified | "World total (rounded) … 640,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[PE].quantity.value | 140000 tonnes | usgs_mcs_2025_silver | verified | "Peru … 140,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[PE].share_pct | 21.9 | usgs_mcs_2025_silver | inferred | Not stated; 140,000/640,000 = 21.875% ≈ 21.9% |
| reserves.reserves_by_country[AU].quantity.value | 94000 tonnes | usgs_mcs_2025_silver | verified | "Australia … 94,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[AU].share_pct | 14.7 | usgs_mcs_2025_silver | inferred | Not stated; 94,000/640,000 = 14.688% ≈ 14.7% |
| reserves.reserves_by_country[AU].notes (JORC 27,000) | 27000 tonnes | usgs_mcs_2025_silver | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 27,000 tons" — USGS MCS 2025 p.163 footnote 10 |
| reserves.reserves_by_country[RU].quantity.value | 92000 tonnes | usgs_mcs_2025_silver | verified | "Russia … 92,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 14.4 | usgs_mcs_2025_silver | inferred | Not stated; 92,000/640,000 = 14.375% ≈ 14.4% |
| reserves.reserves_by_country[CN].quantity.value | 70000 tonnes | usgs_mcs_2025_silver | verified | "China … 70,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 10.9 | usgs_mcs_2025_silver | inferred | Not stated; 70,000/640,000 = 10.938% ≈ 10.9% |
| reserves.reserves_by_country[PL].quantity.value | 61000 tonnes | usgs_mcs_2025_silver | verified | "Poland … 61,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[PL].share_pct | 9.5 | usgs_mcs_2025_silver | inferred | Not stated; 61,000/640,000 = 9.531% ≈ 9.5% |
| reserves.reserves_by_country[ZZ].quantity.value | 57000 tonnes | usgs_mcs_2025_silver | verified | "Other countries … 57,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 8.9 | usgs_mcs_2025_silver | inferred | Not stated; 57,000/640,000 = 8.906% ≈ 8.9% |
| reserves.reserves_by_country[MX].quantity.value | 37000 tonnes | usgs_mcs_2025_silver | verified | "Mexico … 37,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[MX].share_pct | 5.8 | usgs_mcs_2025_silver | inferred | Not stated; 37,000/640,000 = 5.781% ≈ 5.8% |
| reserves.reserves_by_country[CL].quantity.value | 26000 tonnes | usgs_mcs_2025_silver | verified | "Chile … 26,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[CL].share_pct | 4.1 | usgs_mcs_2025_silver | inferred | Not stated; 26,000/640,000 = 4.063% ≈ 4.1% |
| reserves.reserves_by_country[US].quantity.value | 23000 tonnes | usgs_mcs_2025_silver | verified | "United States … 23,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[US].share_pct | 3.6 | usgs_mcs_2025_silver | inferred | Not stated; 23,000/640,000 = 3.594% ≈ 3.6% |
| reserves.reserves_by_country[BO].quantity.value | 22000 tonnes | usgs_mcs_2025_silver | verified | "Bolivia … 22,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[BO].share_pct | 3.4 | usgs_mcs_2025_silver | inferred | Not stated; 22,000/640,000 = 3.438% ≈ 3.4% |
| reserves.reserves_by_country[IN].quantity.value | 8000 tonnes | usgs_mcs_2025_silver | verified | "India … 8,000" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 1.3 | usgs_mcs_2025_silver | inferred | Not stated; 8,000/640,000 = 1.250%; YAML rounds to 1.3% (round-half-up) |
| reserves.reserves_by_country[AR].quantity.value | 6500 tonnes | usgs_mcs_2025_silver | verified | "Argentina … 6,500" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[AR].share_pct | 1.0 | usgs_mcs_2025_silver | inferred | Not stated; 6,500/640,000 = 1.016% ≈ 1.0% |
| reserves.reserves_by_country[CA].quantity.value | 4900 tonnes | usgs_mcs_2025_silver | verified | "Canada … 4,900" — USGS MCS 2025 p.163 Reserves column |
| reserves.reserves_by_country[CA].share_pct | 0.8 | usgs_mcs_2025_silver | inferred | Not stated; 4,900/640,000 = 0.766% ≈ 0.8% (rounds up) |
| end_uses.uses[physical_investment].share_pct | 30 | usgs_mcs_2025_silver | verified | "physical investment (bars), 30%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[electrical_and_electronics].share_pct | 29 | usgs_mcs_2025_silver | verified | "electrical and electronics, 29%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[coins_and_medals].share_pct | 12 | usgs_mcs_2025_silver | verified | "coins and medals, 12%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[photovoltaics].share_pct | 12 | usgs_mcs_2025_silver | verified | "photovoltaics (PV), 12%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[jewelry_and_silverware].share_pct | 6 | usgs_mcs_2025_silver | verified | "jewelry and silverware, 6%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[brazing_and_soldering].share_pct | 4 | usgs_mcs_2025_silver | verified | "brazing and solder, 4%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| end_uses.uses[other_industrial_and_photography].share_pct | 7 | usgs_mcs_2025_silver | verified | "other industrial uses and photography, 7%" — USGS MCS 2025 p.162 Domestic Production paragraph |
| prices[2024].value | 27.70 usd_per_troy_oz | usgs_mcs_2025_silver | verified | "Price, bullion, average, dollars per troy ounce … 27.70" — USGS MCS 2025 p.162 Salient Statistics table, 2024e column |
| prices[2023].value | 23.54 usd_per_troy_oz | usgs_mcs_2025_silver | verified | "Price, bullion, average, dollars per troy ounce … 23.54" — USGS MCS 2025 p.162 Salient Statistics table, 2023 column |
| prices[2022].value | 21.88 usd_per_troy_oz | usgs_mcs_2025_silver | verified | "Price, bullion, average, dollars per troy ounce … 21.88" — USGS MCS 2025 p.162 Salient Statistics table, 2022 column |
| prices[2021].value | 25.23 usd_per_troy_oz | usgs_mcs_2025_silver | verified | "Price, bullion, average, dollars per troy ounce … 25.23" — USGS MCS 2025 p.162 Salient Statistics table, 2021 column |
| prices[2020].value | 20.58 usd_per_troy_oz | usgs_mcs_2025_silver | verified | "Price, bullion, average, dollars per troy ounce … 20.58" — USGS MCS 2025 p.162 Salient Statistics table, 2020 column |
| prices[2024].notes (18% higher than 2023) | 18% | usgs_mcs_2025_silver | verified | "The estimated average silver price in 2024 was $27.70 per troy ounce, 18% higher than the average price in 2023" — USGS MCS 2025 p.162 Events, Trends, and Issues |
| prices[2024].notes (low $22.00 on Jan 22) | 22.00 usd_per_troy_oz / 2024-01-22 | usgs_mcs_2025_silver | verified | "decreased to the low of $22.00 per troy ounce on January 22" — USGS MCS 2025 p.162 Events, Trends, and Issues |
| prices[2024].notes (high $34.60 on Oct 22) | 34.60 usd_per_troy_oz / 2024-10-22 | usgs_mcs_2025_silver | verified | "the price reached a high of $34.60 per troy ounce on October 22" — USGS MCS 2025 p.162 Events, Trends, and Issues |
| geopolitical_events[2023-08] Lucky Friday fire | Aug 2023 | usgs_mcs_2025_silver | verified | "the Lucky Friday Mine in Idaho resumed production in January 2024 after a fire in August 2023" — USGS MCS 2025 p.163 |
| geopolitical_events[2024-01] Lucky Friday resumes | Jan 2024 | usgs_mcs_2025_silver | verified | "the Lucky Friday Mine in Idaho resumed production in January 2024" — USGS MCS 2025 p.163 |
| geopolitical_events[2024-01] Rochester Mine ramp-up | 2024 | usgs_mcs_2025_silver | verified | "The Rochester Mine in Nevada was ramping up an expansion project" — USGS MCS 2025 p.163 |
| geopolitical_events[2024-01-22] price low $22.00 | 22.00 / 2024-01-22 | usgs_mcs_2025_silver | verified | "decreased to the low of $22.00 per troy ounce on January 22" — USGS MCS 2025 p.162 |
| geopolitical_events[2024-10-22] price high $34.60 | 34.60 / 2024-10-22 | usgs_mcs_2025_silver | verified | "the price reached a high of $34.60 per troy ounce on October 22" — USGS MCS 2025 p.162 |
| geopolitical_events[2024-01] global consumption 37,000 mt | 37000 tonnes | silver_institute_world_survey_2024 | verified | "global consumption of silver was an estimated 37,000 tons" — USGS MCS 2025 p.162 (citing SI as footnote 8); Silver Institute survey URL returns 404 but USGS reproduces the figure directly |
| geopolitical_events[2024-01] coin/bar investment down 13% | 13% | silver_institute_world_survey_2024 | verified | "Coin and bar consumption decreased by 13% in 2024" — USGS MCS 2025 p.162 (citing SI footnote 8) |
| geopolitical_events[2024-01] industrial uses up 9% | 9% | silver_institute_world_survey_2024 | verified | "consumption of silver for industrial uses was estimated to have increased by 9% compared with that in 2023" — USGS MCS 2025 p.162 (citing SI footnote 8) |
| geopolitical_events[2024-01] jewelry up 4% | 4% | silver_institute_world_survey_2024 | verified | "Consumption of silver in jewelry … was estimated to have increased by 4%" — USGS MCS 2025 p.162 (citing SI footnote 8) |
| geopolitical_events[2024-01] silverware up 7% | 7% | silver_institute_world_survey_2024 | verified | "silverware was estimated to have increased by … 7%, respectively" — USGS MCS 2025 p.162 (citing SI footnote 8) |
| criticality.notes (net import reliance 64%) | 64% | usgs_mcs_2025_silver | verified | "Net import reliance as a percentage of apparent consumption … 64" — USGS MCS 2025 p.162 Salient Statistics table, 2024e column |
| criticality.notes (secondary recovery ~1,200 mt) | 1200 tonnes | usgs_mcs_2025_silver | verified | "approximately 1,200 tons of silver was recovered from new and old scrap" — USGS MCS 2025 p.162 Recycling paragraph |
| criticality.notes (~19% of apparent consumption) | 19% | usgs_mcs_2025_silver | verified | "accounting for about 19% of apparent consumption" — USGS MCS 2025 p.162 Recycling paragraph |

## Notes

All production quantities and reserve quantities match exactly the values in the USGS MCS 2025 silver chapter (pp.162–163). No discrepancies found.

Share percentages (28 entries) are all computed from the source table quantities divided by the world total; none are stated explicitly in the document. Share rounding is consistent throughout: India reserve share = 8,000/640,000 = 1.25%, rounded to 1.3% in YAML using round-half-up convention — acceptable.

Kazakhstan and Sweden have NA reserves in the USGS table. They are correctly absent from reserves_by_country in the YAML, and the reserves_by_country completeness is correctly marked 'partial'. The sum of listed reserves (641,400 mt) slightly exceeds the world total (640,000 mt) due to rounding, which is normal.

The silver_institute_world_survey_2024 URL (https://www.silverinstitute.org/wp-content/uploads/2024/04/World-Silver-Survey-2024.pdf) returns HTTP 404. However, all five numeric claims attributed to this source are explicitly reproduced in the USGS MCS 2025 text with "Source: Metals Focus, 2024, World silver survey 2024: Silver Institute" as footnote 8; they are marked verified via that USGS citation chain.

End-use percentages are US domestic estimates for 2024 (not global), as clearly stated in the USGS paragraph and YAML notes.

USGS Substitutes paragraph also mentions "Silver may be used to replace more costly metals in catalytic converters for off-road vehicles" — this is a silver-as-substitute-for-PGMs claim not captured in the YAML substitutes list. Not a discrepancy (YAML lists silver-replaced-by substitutes; this is the inverse direction).

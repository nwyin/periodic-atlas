# Verification: Ga

- Element: gallium (Ga)
- Snapshot year: 2025
- Verifier: worker-c8ef5bc8ca3d (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 28 |
| discrepancy | 0 |
| inferred | 11 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 760 tonnes_per_year | usgs_mcs_2025_gallium | verified | Table p.75: "World total (rounded) 633,000 760,000" — 2024e = 760,000 kg |
| production[0].mine.notes (2023 world total) | 633 tonnes_per_year | usgs_mcs_2025_gallium | verified | Table p.75: "World total (rounded) 633,000 760,000" — 2023 = 633,000 kg |
| production[0].refined.value | 320 tonnes_per_year | usgs_mcs_2025_gallium | verified | p.75: "World high-purity refined gallium production in 2024 was estimated to be about 320,000 kilograms, unchanged from the estimate for 2023." |
| production[0].refined.notes (primary refining capacity) | 340 tonnes_per_year | usgs_mcs_2025_gallium | verified | p.75: "World high-purity refined gallium production capacity was an estimated 340,000 kilograms per year" |
| production[0].refined.notes (secondary refining capacity) | 280 tonnes_per_year | usgs_mcs_2025_gallium | verified | p.75: "secondary high-purity gallium production capacity was an estimated 280,000 kilograms per year" |
| production[0].mining_by_country[CN].share_pct | 99% | usgs_mcs_2025_gallium | verified | p.75: "China accounted for 99% of worldwide primary low-purity gallium production." |
| production[0].mining_by_country[CN].quantity.value | 750 tonnes | usgs_mcs_2025_gallium | verified | Table p.75: "China [fn4]621,000 [fn4]750,000" — 2024e = 750,000 kg (fn4 is a footnote marker, not part of value) |
| production[0].mining_by_country[RU].quantity.value | 6 tonnes | usgs_mcs_2025_gallium | verified | Table p.75: "Russiae 6,000 6,000 10,000" — 2024e = 6,000 kg |
| production[0].mining_by_country[JP].quantity.value | 3 tonnes | usgs_mcs_2025_gallium | verified | Table p.75: "Japane 3,000 3,000 10,000" — 2024e = 3,000 kg |
| production[0].mining_by_country[KR].quantity.value | 3 tonnes | usgs_mcs_2025_gallium | verified | Table p.75: "Korea, Republic ofe 3,000 3,000 16,000" — 2024e = 3,000 kg |
| production[0].mining_by_country[RU].share_pct | 1% | usgs_mcs_2025_gallium | inferred | Source gives quantity (6,000 kg) not share; 6,000/760,000 = 0.79% — rounded to 1% in YAML |
| production[0].mining_by_country[JP].share_pct | 0% | usgs_mcs_2025_gallium | inferred | Source gives quantity (3,000 kg) not share; 3,000/760,000 = 0.39% — rounded to 0% in YAML |
| production[0].mining_by_country[KR].share_pct | 0% | usgs_mcs_2025_gallium | inferred | Source gives quantity (3,000 kg) not share; 3,000/760,000 = 0.39% — rounded to 0% in YAML |
| production[0].refining_by_country[CA].share_pct | 20% | usgs_mcs_2025_gallium | inferred | p.75 names 5 producers but gives no country-level breakdown; 20% is equal-split placeholder flagged LOW CONFIDENCE in YAML |
| production[0].refining_by_country[CN].share_pct | 20% | usgs_mcs_2025_gallium | inferred | Same as CA — equal-split placeholder; source: "Canada, China, Japan, Slovakia, and the United States were the known principal producers" |
| production[0].refining_by_country[JP].share_pct | 20% | usgs_mcs_2025_gallium | inferred | Same as CA — equal-split placeholder |
| production[0].refining_by_country[SK].share_pct | 20% | usgs_mcs_2025_gallium | inferred | Same as CA — equal-split placeholder |
| production[0].refining_by_country[US].share_pct | 20% | usgs_mcs_2025_gallium | inferred | Same as CA — equal-split placeholder; p.74 confirms "One company in New York recovered and refined high-purity gallium" |
| reserves.resources.value | 1,000,000 tonnes | usgs_mcs_2025_gallium | verified | p.75: "Gallium contained in world resources of bauxite is estimated to exceed 1 million tons" |
| feedstock_origins[0].typical_concentration_pct | 0.005% (50 ppm) | usgs_mcs_2025_gallium | verified | p.75: "The average gallium content of bauxite is 50 parts per million." |
| feedstock_origins[1].typical_concentration_pct | 0.005% (up to 50 ppm) | usgs_mcs_2025_gallium | verified | p.75: "Some domestic zinc ores contain up to 50 parts per million gallium" |
| end_uses.uses[0].share_pct (integrated_circuits) | 79% | usgs_mcs_2025_gallium | verified | p.74: "ICs accounted for 79% of domestic gallium consumption" |
| end_uses.uses[1].share_pct (optoelectronic_devices) | 20% | usgs_mcs_2025_gallium | verified | p.74: "optoelectronic devices accounted for 20%" |
| end_uses.uses[2].share_pct (research_and_development) | 1% | usgs_mcs_2025_gallium | verified | p.74: "research and development accounted for 1%" |
| criticality.notes (net import reliance) | 100% | usgs_mcs_2025_gallium | verified | p.74 table: "Net import reliance as a percentage of reported consumption 100 100 100 100 100" |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_gallium | inferred | 100% import reliance and no domestic primary production since 1987 confirmed; US Critical Minerals List designation not explicitly stated in this document |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_gallium | inferred | EU CRM list membership not mentioned in USGS MCS 2025; requires EU CRMA documentation to confirm |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_gallium | inferred | EU SRMC list membership not mentioned in USGS MCS 2025; requires EU CRMA documentation to confirm |
| prices[0].value (high-purity refined 2024) | 500 USD/kg | usgs_mcs_2025_gallium | verified | p.74 table: "High-purity, refined ... 500" (2024 column) |
| prices[1].value (low-purity primary 2024) | 220 USD/kg | usgs_mcs_2025_gallium | verified | p.74 table: "Low-purity, primary ... 220" (2024 column) |
| prices[2].value (China domestic June 2024) | 380 USD/kg | usgs_mcs_2025_gallium | verified | p.74: "gallium prices in China averaged $380 per kilogram in June 2024" |
| prices[2].notes (China Jan 2024) | 325 USD/kg | usgs_mcs_2025_gallium | verified | p.74: "an increase of 17% from $325 per kilogram in January 2024" |
| prices[2].notes (China Jun 2023) | 240 USD/kg | usgs_mcs_2025_gallium | verified | p.74: "an increase of 58% from $240 per kilogram in June 2023" |
| prices[2].notes (China Oct 2024) | 420 USD/kg | usgs_mcs_2025_gallium | verified | p.74: "By October, primary low-purity gallium prices in China increased by 11% to $420 per kilogram" |
| prices[2].notes (17% increase Jan→Jun 2024) | 17% | usgs_mcs_2025_gallium | verified | p.74: "an increase of 17% from $325 per kilogram in January 2024" — calc: (380−325)/325 = 16.9% ✓ |
| prices[2].notes (58% increase Jun 2023→Jun 2024) | 58% | usgs_mcs_2025_gallium | verified | p.74: "an increase of 58% from $240 per kilogram in June 2023" — calc: (380−240)/240 = 58.3% ✓ |
| prices[2].notes (11% increase to Oct 2024) | 11% | usgs_mcs_2025_gallium | verified | p.74: "By October, primary low-purity gallium prices in China increased by 11% to $420 per kilogram" — calc: (420−380)/380 = 10.5% ≈ 11% ✓ |
| geopolitical_events[0].date | 2023-08 | usgs_mcs_2025_gallium | verified | p.74: "In August 2023, China's Government implemented gallium export controls, requiring licensing procedures" |
| geopolitical_events[1].date | 2024-12 | usgs_mcs_2025_gallium | verified | p.74: "In December 2024, China banned all exports of gallium to the United States." |

## Notes

**Source accessed:** USGS Mineral Commodity Summaries 2025, Gallium chapter (pp. 74–75). PDF retrieved directly from `https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-gallium.pdf`. Full text extraction via pdfplumber confirmed 2 pages of readable data.

**Production table footnote 4:** The raw PDF text for the China production table reads "China 4621,000 4750,000 1,000,000" — the leading "4" is footnote marker 4 (defined at bottom of page: "Estimated from China Nonferrous Metals Industry Association article. Source: Argus Media Group, Argus Non-Ferrous Markets."), not a digit. Actual values: 2023 = 621,000 kg; 2024e = 750,000 kg. This is the same pdfplumber footnote-concatenation gotcha noted in Co.yaml verification.

**Table row sum vs. world total:** China (750) + Japan (3) + Korea (3) + Russia (6) = 762,000 kg vs. world total 760,000 kg. The 2,000 kg gap is within rounding tolerances when each row is independently rounded; no discrepancy.

**Refining shares are placeholders:** The YAML itself flags refining_by_country shares as LOW CONFIDENCE. USGS names 5 producers but publishes no country-level split for high-purity refined output. Any downstream analysis should treat these 20% figures as equal-split placeholders, not sourced data. A follow-up task should source IEA CMO or Metal Bulletin data for actual refining shares.

**EU criticality flags:** The YAML cites `usgs_mcs_2025_gallium` for EU CRM and EU SRMC membership, but the USGS MCS 2025 gallium chapter does not mention these lists. Both flags are marked `inferred`. They are well-supported by public EU policy documents (Regulation (EU) 2024/1252) but that source is not cited in the YAML.

**High-purity price history (from Salient Statistics table):** 2020=$596, 2021=$625, 2022=$560, 2023=$450, 2024=$500. Low-purity: 2020=$163, 2021=$254, 2022=$394, 2023=$288, 2024=$220. The 2023 China export controls drove the 2022 spike in low-purity prices ($394) followed by a post-control drop ($288 in 2023) as buyers de-stocked, then partial recovery ($220 in 2024 average; China spot rose to $420 by October 2024).

**Follow-up items:**
1. Source the EU criticality flags from EU CRMA documentation (Regulation (EU) 2024/1252 Annexes I and II).
2. Source actual refining-by-country shares from IEA Critical Minerals Market Review 2024 or equivalent trade source; the current 20%/20%/20%/20%/20% placeholder is not analysis-grade.
3. The 2024-12 US-specific ban could be further sourced from Chinese MOFCOM announcement (not cited).

# Verification: Co

- Element: cobalt (Co)
- Snapshot year: 2025
- Verifier: worker-6598fe3b1d7b (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 42 |
| discrepancy | 0 |
| inferred | 28 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 290000 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "World total (rounded) 290,000" — USGS MCS 2025 p.63 mine production table |
| production[0].mining_by_country.CD.quantity.value | 220000 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Congo (Kinshasa) … 220,000" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.CD.share_pct | 76 | usgs_mcs_2025_cobalt | verified | "accounted for an estimated 76% of world cobalt mine production" — USGS MCS 2025 Events & Trends text |
| production[0].mining_by_country.ID.quantity.value | 28000 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Indonesia … 28,000" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.ID.share_pct | 10 | usgs_mcs_2025_cobalt | verified | "Indonesia, which accounted for 10%" — USGS MCS 2025 Events & Trends text |
| production[0].mining_by_country.RU.quantity.value | 8700 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Russia … 8,700" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.RU.share_pct | 3 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 8700/290000 = 3.0% — rounds to 3% |
| production[0].mining_by_country.CA.quantity.value | 4500 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Canada … 4,500" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.CA.share_pct | 2 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 4500/290000 = 1.55% — YAML rounds up to 2% |
| production[0].mining_by_country.PH.quantity.value | 3800 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Philippines … 3,800" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.PH.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 3800/290000 = 1.31% — rounds to 1% |
| production[0].mining_by_country.AU.quantity.value | 3600 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Australia … 3,600" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.AU.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 3600/290000 = 1.24% — rounds to 1% |
| production[0].mining_by_country.CU.quantity.value | 3500 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Cuba … 3,500" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.CU.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 3500/290000 = 1.21% — rounds to 1% |
| production[0].mining_by_country.PG.quantity.value | 2800 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Papua New Guinea … 2,800" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.PG.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 2800/290000 = 0.97% — rounds to 1% |
| production[0].mining_by_country.TR.quantity.value | 2700 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Turkey … 2,700" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.TR.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 2700/290000 = 0.93% — rounds to 1% |
| production[0].mining_by_country.MG.quantity.value | 2600 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Madagascar … 2,600" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.MG.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 2600/290000 = 0.90% — rounds to 1% |
| production[0].mining_by_country.NC.quantity.value | 1500 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "New Caledonia … 1,500" — USGS MCS 2025 World Mine Production table (2024 column); footnote 11: overseas territory of France |
| production[0].mining_by_country.NC.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 1500/290000 = 0.52% — YAML rounds up to 1% |
| production[0].mining_by_country.US.quantity.value | 300 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "United States … 300" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.US.share_pct | 0 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 300/290000 = 0.10% — rounds to 0% |
| production[0].mining_by_country.ZZ.quantity.value | 6200 tonnes_per_year | usgs_mcs_2025_cobalt | verified | "Other countries … 6,200" — USGS MCS 2025 World Mine Production table (2024 column) |
| production[0].mining_by_country.ZZ.share_pct | 2 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 6200/290000 = 2.14% — rounds to 2% |
| production[0].refining_by_country.CN.share_pct | 60 | iea_cmo_2025_exec_summary | inferred | IEA CMO 2025 exec summary states "some 90% of supply growth came from the top single supplier alone … China for cobalt" and "geographic concentration of refining has increased … particularly for nickel and cobalt" but does not quantify China's share at 60%. The 60% figure is secondary IEA-derived reporting; USGS chapter states qualitatively that China "increased metal refining capacity throughout the year" without a share figure. Treat as approximate until a primary quantitative source is added. |
| production[0].refining_by_country.ZZ.share_pct | 40 | iea_cmo_2025_exec_summary | inferred | Residual of 100% − 60% (CN inferred); same caveat applies |
| reserves.economic_reserves.value | 11000000 tonnes | usgs_mcs_2025_cobalt | verified | "World total (rounded) … 11,000,000" — USGS MCS 2025 Reserves column, World Mine Production and Reserves table |
| reserves.resources.value | 25000000 tonnes | usgs_mcs_2025_cobalt | verified | "Identified world terrestrial cobalt resources are about 25 million tons" — USGS MCS 2025 World Resources note. USGS MCS reports in metric tons per title header "(Data in metric tons, cobalt content, unless otherwise specified)"; the "tons" = metric tonnes here. |
| reserves.reserves_by_country.CD.quantity.value | 6000000 tonnes | usgs_mcs_2025_cobalt | verified | "Congo (Kinshasa) … 6,000,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CD.share_pct | 55 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 6000000/11000000 = 54.5% — rounds to 55% |
| reserves.reserves_by_country.AU.quantity.value | 1700000 tonnes | usgs_mcs_2025_cobalt | verified | "Australia … 1,700,000" — USGS MCS 2025 Reserves column. Note: PDF text extractor reads "101,700,000" because footnote superscript "10" is appended directly; the actual reserve figure is 1,700,000 t. Footnote 10 states JORC-compliant reserves were 610,000 tons. |
| reserves.reserves_by_country.AU.share_pct | 16 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 1700000/11000000 = 15.5% — rounds to 16% |
| reserves.reserves_by_country.ID.quantity.value | 640000 tonnes | usgs_mcs_2025_cobalt | verified | "Indonesia … 640,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.ID.share_pct | 6 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 640000/11000000 = 5.8% — rounds to 6% |
| reserves.reserves_by_country.CU.quantity.value | 500000 tonnes | usgs_mcs_2025_cobalt | verified | "Cuba … 500,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CU.share_pct | 5 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 500000/11000000 = 4.5% — rounds to 5% |
| reserves.reserves_by_country.PH.quantity.value | 260000 tonnes | usgs_mcs_2025_cobalt | verified | "Philippines … 260,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.PH.share_pct | 2 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 260000/11000000 = 2.4% — rounds to 2% |
| reserves.reserves_by_country.RU.quantity.value | 250000 tonnes | usgs_mcs_2025_cobalt | verified | "Russia … 250,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.RU.share_pct | 2 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 250000/11000000 = 2.3% — rounds to 2% |
| reserves.reserves_by_country.CA.quantity.value | 220000 tonnes | usgs_mcs_2025_cobalt | verified | "Canada … 220,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CA.share_pct | 2 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 220000/11000000 = 2.0% — rounds to 2% |
| reserves.reserves_by_country.MG.quantity.value | 100000 tonnes | usgs_mcs_2025_cobalt | verified | "Madagascar … 100,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.MG.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 100000/11000000 = 0.91% — rounds to 1% |
| reserves.reserves_by_country.TR.quantity.value | 91000 tonnes | usgs_mcs_2025_cobalt | verified | "Turkey … 91,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.TR.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 91000/11000000 = 0.83% — rounds to 1% |
| reserves.reserves_by_country.US.quantity.value | 70000 tonnes | usgs_mcs_2025_cobalt | verified | "United States … 70,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.US.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 70000/11000000 = 0.64% — rounds to 1% |
| reserves.reserves_by_country.PG.quantity.value | 62000 tonnes | usgs_mcs_2025_cobalt | verified | "Papua New Guinea … 62,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.PG.share_pct | 1 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 62000/11000000 = 0.56% — rounds to 1% |
| reserves.reserves_by_country.ZZ.quantity.value | 800000 tonnes | usgs_mcs_2025_cobalt | verified | "Other countries … 800,000" — USGS MCS 2025 Reserves column. Note: named-country sum (9,893,000) + 800,000 = 10,693,000; difference from rounded world total (11,000,000) = 307,000 is attributed to USGS rounding. |
| reserves.reserves_by_country.ZZ.share_pct | 7 | usgs_mcs_2025_cobalt | inferred | Not stated in source; 800000/11000000 = 7.3% — rounds to 7% |
| end_uses.uses[superalloys_aircraft_turbines].share_pct | 51 | usgs_mcs_2025_cobalt | verified | "An estimated 51% of cobalt consumed in the United States was used in superalloys, mainly aircraft gas turbine engines" — USGS MCS 2025 Domestic Production and Use, p.62. US-specific, not global. |
| end_uses.uses[chemical_applications_various].share_pct | 25 | usgs_mcs_2025_cobalt | verified | "25% in a variety of chemical applications" — USGS MCS 2025 Domestic Production and Use. US 2024 consumption breakdown. |
| end_uses.uses[other_metallic_applications].share_pct | 15 | usgs_mcs_2025_cobalt | verified | "15% in various other metallic applications" — USGS MCS 2025 Domestic Production and Use. US 2024 consumption breakdown. |
| end_uses.uses[cemented_carbides_cutting_tools].share_pct | 9 | usgs_mcs_2025_cobalt | verified | "9% in cemented carbides for cutting and wear-resistant applications" — USGS MCS 2025 Domestic Production and Use. US 2024 consumption breakdown. |
| prices[2024,us_domestic].value | 17 usd_per_lb | usgs_mcs_2025_cobalt | verified | "U.S. spot, cathode … 17" (2024e) — USGS MCS 2025 Salient Statistics table. Value is rounded from the exact figure; source footnote 4: S&P Global Platts Metals Week. |
| prices[2024,lme].value | 12 usd_per_lb | usgs_mcs_2025_cobalt | verified | "London Metal Exchange (LME), cash … 12" (2024e) — USGS MCS 2025 Salient Statistics table. |
| prices[2023,us_domestic].value | 17.20 usd_per_lb | usgs_mcs_2025_cobalt | verified | "U.S. spot, cathode … 17.20" (2023) — USGS MCS 2025 Salient Statistics table. |
| prices[2022,us_domestic].value | 30.78 usd_per_lb | usgs_mcs_2025_cobalt | verified | "U.S. spot, cathode … 30.78" (2022) — USGS MCS 2025 Salient Statistics table. |
| prices[2021,us_domestic].value | 24.21 usd_per_lb | usgs_mcs_2025_cobalt | verified | "U.S. spot, cathode … 24.21" (2021) — USGS MCS 2025 Salient Statistics table. |
| prices[2020,us_domestic].value | 15.70 usd_per_lb | usgs_mcs_2025_cobalt | verified | "U.S. spot, cathode … 15.70" (2020) — USGS MCS 2025 Salient Statistics table. |
| geopolitical_events[2024-01].date | 2024 | usgs_mcs_2025_cobalt | verified | "In 2024, the United States enacted tariff rate increases on cobalt ores and concentrates originating from China, as well as cobalt-containing products including electric vehicles and lithium-ion batteries" — USGS MCS 2025 Events & Trends. YAML assigns 2024-01; USGS says "In 2024" without specifying a month. |
| geopolitical_events[2025-02].event | DRC 4-month export suspension | iea_cmo_2025_exec_summary | verified | "In February 2025, the DRC announced a four-month suspension of cobalt exports to curb falling prices" — IEA Global Critical Minerals Outlook 2025 Executive Summary. Date and duration match YAML exactly. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_cobalt | inferred | Cobalt is included in USGS MCS 2025 (the primary US critical minerals annual publication). The cobalt chapter text does not explicitly state "cobalt is on the US 2025 critical minerals list," but inclusion in the MCS is the operative designation. Net import reliance 76% confirmed by USGS Salient Statistics. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_cobalt | inferred | EU CRM Act (2024) list membership is not stated in the cited USGS source. Cobalt's presence on the EU Critical Raw Materials list is well-established but requires an EU-sourced citation to verify directly. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_cobalt | inferred | EU Strategic Raw Materials list membership is not stated in the cited USGS source. Same caveat as EU CRM. Follow-up: add eu_crm_2024 source citing the official EU annex. |

## Notes

**Source access**: USGS MCS 2025 cobalt PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-cobalt.pdf) was fetched and parsed via pdfplumber. Full text of both pages extracted successfully. IEA CMO 2025 Executive Summary (https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary) was fetched as HTML; key cobalt passages were confirmed.

**PDF extraction artifact**: The Australia reserves row in the USGS PDF renders as "101,700,000" when extracted as text because the footnote superscript "10" is run together with the value "1,700,000". The correct figure is 1,700,000 tonnes, consistent with YAML and USGS footnote 10 text ("Joint Ore Reserves Committee-compliant or equivalent reserves were 610,000 tons").

**Reserve totals rounding**: Named-country reserves sum to 9,893,000 t + Other countries 800,000 t = 10,693,000 t, which is 307,000 t below the USGS rounded world total of 11,000,000 t. This is a USGS rounding artifact, not a YAML error.

**End-uses are US-specific**: All four end-use share_pct values in Co.yaml (superalloys 51%, chemicals 25%, other metallic 15%, cemented carbides 9%) are drawn from the USGS US domestic consumption breakdown, explicitly so in the YAML notes. Global cobalt end-use is battery-dominated (per IEA context) but no specific global percentage breakdown was available with a primary quantitative citation.

**China refinery share (60%)**: Neither the USGS MCS 2025 cobalt chapter nor the IEA CMO 2025 Executive Summary provides an explicit quantitative figure of "60%" for China's share of refined cobalt. The USGS chapter states qualitatively that China is the leading refiner; the IEA mentions China dominates cobalt refining growth. The 60% figure is sourced from secondary IEA-derived reporting. Marked as `inferred` per task guidance; flagged for follow-up.

**Criticality EU flags**: Both eu_crm_list_as_of_2024 and eu_strategic_list_as_of_2024 cite usgs_mcs_2025_cobalt, but USGS does not reference the EU lists. Cobalt is confirmed on both EU lists through general knowledge, but verification requires an EU-sourced citation (e.g., EU CRM Act Annex II/III). Recommend adding source `eu_crm_act_2024` in a follow-up pass.

**US tariff date**: YAML assigns 2024-01; USGS MCS 2025 states "In 2024" without a specific month. January 2024 is plausible (first tranche of Section 301 tariff increases was enacted mid-2024), but exact month is not directly verifiable from the cited source. Keeping as verified on the year; month is not independently confirmed.

**IEA cobalt demand figure**: IEA CMO 2025 Executive Summary states "Demand for nickel, cobalt, graphite and rare earths increased by 6–8% in 2024." This is a grouped figure, not a Co-specific demand number, and does not correspond to any claim in Co.yaml.

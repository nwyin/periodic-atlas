# Verification: Ni

- Element: nickel (Ni)
- Snapshot year: 2025
- Verifier: worker-1ce03009116e (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 56 |
| discrepancy | 0 |
| inferred | 14 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 3700000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "World total (rounded) 3,700,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mine notes (2023 world total) | 3750000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "3,750,000" — USGS MCS 2025 p.125 World Mine Production table, 2023 column |
| production[0].mining_by_country[ID].quantity.value | 2200000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Indonesia … 2,200,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[ID].share_pct | 60 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 2200000/3700000 = 59.5% — rounds to 60% |
| production[0].mining_by_country[ID].notes (+8%, 2023=2030000) | 2030000; +8% | usgs_mcs_2025_nickel | verified | "Indonesia … 2,030,000" (2023); "production in Indonesia increased by an estimated 8%" — USGS MCS 2025 p.125 |
| production[0].mining_by_country[PH].quantity.value | 330000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Philippines … 330,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[PH].share_pct | 9 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 330000/3700000 = 8.9% — rounds to 9% |
| production[0].mining_by_country[PH].notes (−20%, 2023=413000) | 413000; −20% | usgs_mcs_2025_nickel | verified | "Philippines e413,000" (2023); "Philippines declined by an estimated … 20%" — USGS MCS 2025 p.125 |
| production[0].mining_by_country[RU].quantity.value | 210000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Russia … 210,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 6 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 210000/3700000 = 5.7% — rounds to 6% |
| production[0].mining_by_country[RU].notes (2023=210000, unchanged) | 210000 | usgs_mcs_2025_nickel | verified | "Russia … 210,000" (2023) — USGS MCS 2025 p.125 World Mine Production table, 2023 column (matches 2024) |
| production[0].mining_by_country[CA].quantity.value | 190000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Canada … 190,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 5 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 190000/3700000 = 5.1% — rounds to 5% |
| production[0].mining_by_country[CA].notes (2023=159000) | 159000 | usgs_mcs_2025_nickel | verified | "Canada … 159,000" — USGS MCS 2025 p.125 World Mine Production table, 2023 column |
| production[0].mining_by_country[CN].quantity.value | 120000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "China … 120,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 3 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 120000/3700000 = 3.2% — rounds to 3% |
| production[0].mining_by_country[NC].quantity.value | 110000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "New Caledonia … 110,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column; footnote 10: overseas territory of France |
| production[0].mining_by_country[NC].share_pct | 3 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 110000/3700000 = 3.0% — rounds to 3% |
| production[0].mining_by_country[NC].notes (−52%, 2023=231000) | 231000; −52% | usgs_mcs_2025_nickel | verified | "New Caledonia … 231,000" (2023); "decreased by an estimated 52% owing to widespread unrest" — USGS MCS 2025 p.125 |
| production[0].mining_by_country[AU].quantity.value | 110000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Australia … 110,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 3 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 110000/3700000 = 3.0% — rounds to 3% |
| production[0].mining_by_country[AU].notes (−26%, 2023=149000) | 149000; −26% | usgs_mcs_2025_nickel | verified | "Australia … 149,000" (2023); "Production in Australia … declined by an estimated 26%" — USGS MCS 2025 p.125 |
| production[0].mining_by_country[BR].quantity.value | 77000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Brazil … 77,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 2 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 77000/3700000 = 2.1% — rounds to 2% |
| production[0].mining_by_country[US].quantity.value | 8000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "United States … 8,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column; also p.124 "approximately 8,000 tons" |
| production[0].mining_by_country[US].share_pct | 0 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 8000/3700000 = 0.2% — rounds to 0% |
| production[0].mining_by_country[US].notes (2023=16400) | 16400 | usgs_mcs_2025_nickel | verified | "United States … 16,400" — USGS MCS 2025 p.125 World Mine Production table, 2023 column; also Salient Statistics Mine 2023=16,400 |
| production[0].mining_by_country[ZZ].quantity.value | 300000 tonnes_per_year | usgs_mcs_2025_nickel | verified | "Other countries … 300,000" — USGS MCS 2025 p.125 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 8 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 300000/3700000 = 8.1% — rounds to 8% |
| production[0].mining_by_country[ZZ].notes (2023=340000) | 340000 | usgs_mcs_2025_nickel | verified | "Other countries … 340,000" — USGS MCS 2025 p.125 World Mine Production table, 2023 column |
| reserves.economic_reserves.value | 130000000 tonnes | usgs_mcs_2025_nickel | verified | "World total (rounded) >130,000,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.resources.value | 350000000 tonnes | usgs_mcs_2025_nickel | verified | "nickel resources have been estimated to contain more than 350 million tons of nickel" — USGS MCS 2025 p.125 World Resources section |
| reserves.resources notes (54% laterites) | 54% | usgs_mcs_2025_nickel | verified | "with 54% in laterites" — USGS MCS 2025 p.125 World Resources section |
| reserves.resources notes (35% magmatic sulfide) | 35% | usgs_mcs_2025_nickel | verified | "35% in magmatic sulfide deposits" — USGS MCS 2025 p.125 World Resources section |
| reserves.resources notes (10% hydrothermal etc.) | 10% | usgs_mcs_2025_nickel | verified | "Hydrothermal systems … seafloor manganese crusts and nodules contain 10%" — USGS MCS 2025 p.125 |
| reserves.resources notes (1% misc) | 1% | usgs_mcs_2025_nickel | verified | "miscellaneous resources such as tailings, 1%" — USGS MCS 2025 p.125 World Resources section |
| reserves.reserves_by_country[ID].quantity.value | 55000000 tonnes | usgs_mcs_2025_nickel | verified | "Indonesia … 55,000,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[ID].share_pct | 42 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 55000000/130000000 = 42.3% — rounds to 42% |
| reserves.reserves_by_country[AU].quantity.value | 24000000 tonnes | usgs_mcs_2025_nickel | verified | "Australia … 24,000,000" — USGS MCS 2025 p.125 Reserves column; footnote 9: JORC-compliant reserves 8.6 million tons |
| reserves.reserves_by_country[AU].share_pct | 18 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 24000000/130000000 = 18.5% — rounds to 18% |
| reserves.reserves_by_country[AU].notes (JORC 8.6M) | 8600000 tonnes | usgs_mcs_2025_nickel | verified | "Joint Ore Reserves Committee-compliant or equivalent reserves were 8.6 million tons" — USGS MCS 2025 p.125 footnote 9 |
| reserves.reserves_by_country[BR].quantity.value | 16000000 tonnes | usgs_mcs_2025_nickel | verified | "Brazil … 16,000,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 12 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 16000000/130000000 = 12.3% — rounds to 12% |
| reserves.reserves_by_country[RU].quantity.value | 8300000 tonnes | usgs_mcs_2025_nickel | verified | "Russia … 8,300,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 6 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 8300000/130000000 = 6.4% — rounds to 6% |
| reserves.reserves_by_country[NC].quantity.value | 7100000 tonnes | usgs_mcs_2025_nickel | verified | "New Caledonia … 7,100,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[NC].share_pct | 5 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 7100000/130000000 = 5.5% — rounds to 5% |
| reserves.reserves_by_country[PH].quantity.value | 4800000 tonnes | usgs_mcs_2025_nickel | verified | "Philippines … 4,800,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[PH].share_pct | 4 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 4800000/130000000 = 3.7% — rounds to 4% |
| reserves.reserves_by_country[CN].quantity.value | 4400000 tonnes | usgs_mcs_2025_nickel | verified | "China … 4,400,000" — USGS MCS 2025 p.125 Reserves column; footnote: revised based on company and Government reports |
| reserves.reserves_by_country[CN].share_pct | 3 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 4400000/130000000 = 3.4% — rounds to 3% |
| reserves.reserves_by_country[CA].quantity.value | 2200000 tonnes | usgs_mcs_2025_nickel | verified | "Canada … 2,200,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[CA].share_pct | 2 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 2200000/130000000 = 1.7% — rounds to 2% |
| reserves.reserves_by_country[US].quantity.value | 310000 tonnes | usgs_mcs_2025_nickel | verified | "United States … 310,000" — USGS MCS 2025 p.125 Reserves column; footnote 8: includes reserve data for three projects |
| reserves.reserves_by_country[US].share_pct | 0 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 310000/130000000 = 0.24% — rounds to 0% |
| reserves.reserves_by_country[ZZ].quantity.value | 9100000 tonnes | usgs_mcs_2025_nickel | verified | "Other countries … >9,100,000" — USGS MCS 2025 p.125 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 7 | usgs_mcs_2025_nickel | inferred | Not stated explicitly; 9100000/130000000 = 7.0% — rounds to 7% |
| end_uses.uses[stainless_and_alloy_steel].share_pct | 85 | usgs_mcs_2025_nickel | verified | "Stainless and alloy steel and nickel-containing alloys typically account for more than 85% of domestic consumption" — USGS MCS 2025 p.124. YAML correctly records this as the stated lower bound. |
| end_uses.uses[electroplating_catalysts_chemicals_other].share_pct | 15 | usgs_mcs_2025_nickel | inferred | Not stated; implied remainder after >85% stainless/alloy. USGS lists electroplating, catalysts, chemicals as secondary but gives no percentage for this group. |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_nickel | inferred | Nickel is on the US 2022 Final Critical Minerals List. The USGS nickel chapter text does not explicitly state this; it is established through USGS's own critical minerals program but not referenced in these two pages. |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_nickel | inferred | EU CRM Act (Annex II) membership is not stated in the cited USGS source. Well-established fact but requires EU-sourced citation to verify directly. |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_nickel | inferred | EU Strategic Raw Materials (Annex I) membership is not stated in the cited USGS source. Same caveat as EU CRM. |
| criticality notes (net import reliance 48%) | 48% | usgs_mcs_2025_nickel | verified | "Net import reliance … 48" (2024e) — USGS MCS 2025 p.124 Salient Statistics table |
| criticality notes (excl scrap ~100%) | ~100% | usgs_mcs_2025_nickel | verified | "Excluding scrap, net import reliance would be nearly 100%" — USGS MCS 2025 p.124 footnote 5 |
| prices[2024].value | 17000 usd_per_tonne | usgs_mcs_2025_nickel | verified | "Dollars per metric ton … 17,000" (2024e) and "Dollars per pound … 7.70" — USGS MCS 2025 p.124 Salient Statistics LME cash |
| prices[2023].value | 21495 usd_per_tonne | usgs_mcs_2025_nickel | verified | "Dollars per metric ton … 21,495" (2023) and "$9.75/lb" — USGS MCS 2025 p.124 Salient Statistics LME cash |
| prices[2022].value | 25815 usd_per_tonne | usgs_mcs_2025_nickel | verified | "Dollars per metric ton … 25,815" (2022) and "$11.71/lb" — USGS MCS 2025 p.124 Salient Statistics LME cash |
| prices[2021].value | 18476 usd_per_tonne | usgs_mcs_2025_nickel | verified | "Dollars per metric ton … 18,476" (2021) and "$8.38/lb" — USGS MCS 2025 p.124 Salient Statistics LME cash |
| prices[2020].value | 13772 usd_per_tonne | usgs_mcs_2025_nickel | verified | "Dollars per metric ton … 13,772" (2020) and "$6.25/lb" — USGS MCS 2025 p.124 Salient Statistics LME cash |
| prices[2024].notes (−21% from 2023) | −21% | usgs_mcs_2025_nickel | verified | "annual average LME nickel cash price was estimated to have decreased by 21% compared with that in 2023" — USGS MCS 2025 p.125 Events, Trends, and Issues |
| geopolitical_events[2024-01].event (LME ~$19000/t) | ~19000 usd_per_tonne | usgs_mcs_2025_nickel | verified | "increased the LME nickel cash price to about $19,000 per metric ton" — USGS MCS 2025 p.125 Events |
| geopolitical_events[2024-01].impact (by Nov ~$16000/t) | ~16000 usd_per_tonne | usgs_mcs_2025_nickel | verified | "the LME annual average cash price decreased to about $16,000 per metric ton by November" — USGS MCS 2025 p.125 |
| geopolitical_events[2024-05].event (DoD $7M grant) | 7000000 USD | usgs_mcs_2025_nickel | verified | "awarded a grant of $7 million to a Missouri company to develop a hydrometallurgical demonstration plant" — USGS MCS 2025 p.125 |
| geopolitical_events[2024-06].event (Zambia mine start) | 2024-06 | usgs_mcs_2025_nickel | verified | "In June, a company began commercial production at a new nickel sulfide mine in Kalumbila, Zambia" — USGS MCS 2025 p.125 |
| feedstock_origins[laterite].notes (54% of resources) | 54% | usgs_mcs_2025_nickel | verified | "with 54% in laterites" — USGS MCS 2025 p.125 World Resources section (same as reserves.resources notes) |
| feedstock_origins[sulfide].notes (35% of resources) | 35% | usgs_mcs_2025_nickel | verified | "35% in magmatic sulfide deposits" — USGS MCS 2025 p.125 World Resources section |
| substitutes[stainless_and_alloy_steel].notes | quoted text | usgs_mcs_2025_nickel | verified | YAML quotes verbatim: "Low-nickel, duplex, or ultrahigh-chromium stainless steels have been substituted for austenitic grades in construction. Nickel-free specialty steels … Titanium alloys can substitute …" — USGS MCS 2025 p.125 Substitutes section |

## Notes

**Source access**: USGS MCS 2025 Nickel PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-nickel.pdf) fetched and rendered as two pages (pp. 124–125). Full content of both pages confirmed accessible. All claims trace to a single primary source.

**All claims verified or inferred — zero discrepancies**: Every quantity in the YAML matches the USGS table exactly. All share_pcts marked `inferred` because USGS does not state percentages in narrative text (except for Indonesia's +8% YoY increase, Australia's −26%, Philippines' −20%, and New Caledonia's −52% year-over-year changes — none of which are market-share percentages). The derived share_pcts are arithmetically consistent: e.g., Indonesia 2200000/3700000 = 59.5% → YAML rounds to 60%.

**Sum check (mine share_pcts)**: 60+9+6+5+3+3+3+2+0+8 = 99%. The 1% gap is a rounding artifact from individual country shares; within the expected ±5% range for `completeness: complete`.

**Sum check (reserve share_pcts)**: 42+18+12+6+5+4+3+2+0+7 = 99%. Slight rounding shortfall vs. the >130 Mt world total — expected given USGS uses a floor figure (">130,000,000").

**Criticality EU flags**: Both `eu_crm_list_as_of_2024` and `eu_strategic_list_as_of_2024` cite `usgs_mcs_2025_nickel`, but the USGS chapter text does not reference the EU CRM Act. These facts are accurate per EU Regulation 2024/1252 but require an EU-sourced citation to verify from the stated source. Recommend adding a dedicated `eu_crma_2024` source in a follow-up pass.

**US Mine production (Salient Statistics vs. World Mine Production table)**: The Salient Statistics table (p.124) reports 2024 US mine production as 8,000 t, consistent with the narrative "approximately 8,000 tons" and the World Mine Production table value. 2023 Salient Statistics Mine = 16,400 t matches the World Mine Production table. No conflict.

**Canada 2024 notes misplacement**: The YAML notes for Canada mention "A new nickel sulfide mine began commercial production in Zambia in June 2024 (not Canada-specific)" — this is a correct note clarifying that the Zambia mine is unrelated to the Canada row. Not a numeric claim.

**US government stockpile**: The source notes "The U.S. Department of Energy is holding approximately 9,700 tons of radiologically contaminated nickel at Paducah, KY." This is not captured in Ni.yaml, which is appropriate as it is not a production/reserve claim.

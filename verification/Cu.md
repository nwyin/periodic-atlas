# Verification: Cu

- Element: copper (Cu)
- Snapshot year: 2025
- Verifier: worker-9002f9769759 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 78 |
| discrepancy | 0 |
| inferred | 50 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 23 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "World total (rounded) … 23,000" — USGS MCS 2025 Mine production 2024e column (thousand metric tons) |
| production[0].mine.notes: 2023 total | 22,600 thousand metric tons | usgs_mcs_2025_copper | verified | "World total (rounded) … 22,600" — USGS MCS 2025 Mine production 2023 column |
| production[0].refined.value | 27 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "World total (rounded) … 27,000" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refined.notes: 2023 total | 27,000 thousand metric tons | usgs_mcs_2025_copper | verified | "World total (rounded) … 27,000" — USGS MCS 2025 Refinery production 2023 column |
| production[0].mining_by_country.CL.quantity.value | 5.3 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Chile … 5,300" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.CL.share_pct | 23.0 | usgs_mcs_2025_copper | inferred | Not stated; 5,300 / 23,000 = 23.04% — rounds to 23.0% |
| production[0].mining_by_country.CD.quantity.value | 3.3 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Congo (Kinshasa) … 3,300" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.CD.share_pct | 14.3 | usgs_mcs_2025_copper | inferred | Not stated; 3,300 / 23,000 = 14.35% — rounds to 14.3% (truncated) |
| production[0].mining_by_country.PE.quantity.value | 2.6 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Peru … 2,600" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.PE.share_pct | 11.3 | usgs_mcs_2025_copper | inferred | Not stated; 2,600 / 23,000 = 11.30% — exact match |
| production[0].mining_by_country.CN.quantity.value | 1.8 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "China … 1,800" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.CN.share_pct | 7.8 | usgs_mcs_2025_copper | inferred | Not stated; 1,800 / 23,000 = 7.83% — rounds to 7.8% (truncated) |
| production[0].mining_by_country.US.quantity.value | 1.1 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "United States … 1,100" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.US.share_pct | 4.8 | usgs_mcs_2025_copper | inferred | Not stated; 1,100 / 23,000 = 4.78% — rounds to 4.8% |
| production[0].mining_by_country.ID.quantity.value | 1.1 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Indonesia … 1,100" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.ID.share_pct | 4.8 | usgs_mcs_2025_copper | inferred | Not stated; 1,100 / 23,000 = 4.78% — rounds to 4.8% |
| production[0].mining_by_country.RU.quantity.value | 0.93 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Russia … 930" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.RU.share_pct | 4.0 | usgs_mcs_2025_copper | inferred | Not stated; 930 / 23,000 = 4.04% — rounds to 4.0% (truncated) |
| production[0].mining_by_country.AU.quantity.value | 0.8 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Australia … 800" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.AU.share_pct | 3.5 | usgs_mcs_2025_copper | inferred | Not stated; 800 / 23,000 = 3.48% — rounds to 3.5% |
| production[0].mining_by_country.KZ.quantity.value | 0.74 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Kazakhstan … 740" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.KZ.share_pct | 3.2 | usgs_mcs_2025_copper | inferred | Not stated; 740 / 23,000 = 3.22% — rounds to 3.2% (truncated) |
| production[0].mining_by_country.MX.quantity.value | 0.7 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Mexico … 700" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.MX.share_pct | 3.0 | usgs_mcs_2025_copper | inferred | Not stated; 700 / 23,000 = 3.04% — rounds to 3.0% (truncated) |
| production[0].mining_by_country.ZM.quantity.value | 0.68 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Zambia … 680" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.ZM.share_pct | 3.0 | usgs_mcs_2025_copper | inferred | Not stated; 680 / 23,000 = 2.96% — rounds to 3.0% |
| production[0].mining_by_country.CA.quantity.value | 0.45 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Canada … 450" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.CA.share_pct | 2.0 | usgs_mcs_2025_copper | inferred | Not stated; 450 / 23,000 = 1.96% — rounds to 2.0% |
| production[0].mining_by_country.PL.quantity.value | 0.41 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Poland … 410" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.PL.share_pct | 1.8 | usgs_mcs_2025_copper | inferred | Not stated; 410 / 23,000 = 1.78% — rounds to 1.8% |
| production[0].mining_by_country.IN.quantity.value | 0.03 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "India … 30" — USGS MCS 2025 Mine production 2024e column (30 kt = 0.03 Mt) |
| production[0].mining_by_country.IN.share_pct | 0.1 | usgs_mcs_2025_copper | inferred | Not stated; 30 / 23,000 = 0.13% — rounded down to 0.1% in YAML |
| production[0].mining_by_country.ZZ.quantity.value | 2.7 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Other countries … 2,700" — USGS MCS 2025 Mine production 2024e column |
| production[0].mining_by_country.ZZ.share_pct | 11.7 | usgs_mcs_2025_copper | inferred | Not stated; 2,700 / 23,000 = 11.74% — rounds to 11.7% (truncated) |
| production[0].refining_by_country.CN.quantity.value | 12.0 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "China … 12,000" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.CN.share_pct | 44.4 | usgs_mcs_2025_copper | inferred | Not stated; 12,000 / 27,000 = 44.44% — rounds to 44.4% (truncated) |
| production[0].refining_by_country.CD.quantity.value | 2.5 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Congo (Kinshasa) … 2,500" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.CD.share_pct | 9.3 | usgs_mcs_2025_copper | inferred | Not stated; 2,500 / 27,000 = 9.26% — rounds to 9.3% |
| production[0].refining_by_country.CL.quantity.value | 1.9 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Chile … 1,900" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.CL.share_pct | 7.0 | usgs_mcs_2025_copper | inferred | Not stated; 1,900 / 27,000 = 7.04% — rounds to 7.0% (truncated) |
| production[0].refining_by_country.JP.quantity.value | 1.6 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Japan … 1,600" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.JP.share_pct | 5.9 | usgs_mcs_2025_copper | inferred | Not stated; 1,600 / 27,000 = 5.93% — rounds to 5.9% (truncated) |
| production[0].refining_by_country.RU.quantity.value | 0.96 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Russia … 960" — USGS MCS 2025 Refinery production 2024e column (footnote e = estimated) |
| production[0].refining_by_country.RU.share_pct | 3.6 | usgs_mcs_2025_copper | inferred | Not stated; 960 / 27,000 = 3.56% — rounds to 3.6% |
| production[0].refining_by_country.US.quantity.value | 0.89 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "United States … 890" — USGS MCS 2025 Refinery production 2024e column; also equals primary 850 + secondary 40 from Salient Statistics |
| production[0].refining_by_country.US.share_pct | 3.3 | usgs_mcs_2025_copper | inferred | Not stated; 890 / 27,000 = 3.30% — rounds to 3.3% (truncated) |
| production[0].refining_by_country.DE.quantity.value | 0.63 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Germany … 630" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.DE.share_pct | 2.3 | usgs_mcs_2025_copper | inferred | Not stated; 630 / 27,000 = 2.33% — rounds to 2.3% (truncated) |
| production[0].refining_by_country.KR.quantity.value | 0.62 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Korea, Republic of … 620" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.KR.share_pct | 2.3 | usgs_mcs_2025_copper | inferred | Not stated; 620 / 27,000 = 2.30% — rounds to 2.3% |
| production[0].refining_by_country.PL.quantity.value | 0.59 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Poland … 590" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.PL.share_pct | 2.2 | usgs_mcs_2025_copper | inferred | Not stated; 590 / 27,000 = 2.19% — rounds to 2.2% |
| production[0].refining_by_country.IN.quantity.value | 0.51 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "India … 510" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.IN.share_pct | 1.9 | usgs_mcs_2025_copper | inferred | Not stated; 510 / 27,000 = 1.89% — rounds to 1.9% |
| production[0].refining_by_country.KZ.quantity.value | 0.47 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Kazakhstan … 470" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.KZ.share_pct | 1.7 | usgs_mcs_2025_copper | inferred | Not stated; 470 / 27,000 = 1.74% — rounds to 1.7% (truncated) |
| production[0].refining_by_country.AU.quantity.value | 0.46 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Australia … 460" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.AU.share_pct | 1.7 | usgs_mcs_2025_copper | inferred | Not stated; 460 / 27,000 = 1.70% — exact match |
| production[0].refining_by_country.PE.quantity.value | 0.39 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Peru … 390" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.PE.share_pct | 1.4 | usgs_mcs_2025_copper | inferred | Not stated; 390 / 27,000 = 1.44% — rounds to 1.4% (truncated) |
| production[0].refining_by_country.ID.quantity.value | 0.35 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Indonesia … 350" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.ID.share_pct | 1.3 | usgs_mcs_2025_copper | inferred | Not stated; 350 / 27,000 = 1.30% — exact match |
| production[0].refining_by_country.MX.quantity.value | 0.35 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Mexico … 350" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.MX.share_pct | 1.3 | usgs_mcs_2025_copper | inferred | Not stated; 350 / 27,000 = 1.30% — exact match |
| production[0].refining_by_country.CA.quantity.value | 0.32 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Canada … 320" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.CA.share_pct | 1.2 | usgs_mcs_2025_copper | inferred | Not stated; 320 / 27,000 = 1.19% — rounds to 1.2% |
| production[0].refining_by_country.ZM.quantity.value | 0.17 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Zambia … 170" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.ZM.share_pct | 0.6 | usgs_mcs_2025_copper | inferred | Not stated; 170 / 27,000 = 0.63% — rounds to 0.6% (truncated) |
| production[0].refining_by_country.ZZ.quantity.value | 2.5 million_tonnes_per_year | usgs_mcs_2025_copper | verified | "Other countries … 2,500" — USGS MCS 2025 Refinery production 2024e column |
| production[0].refining_by_country.ZZ.share_pct | 9.3 | usgs_mcs_2025_copper | inferred | Not stated; 2,500 / 27,000 = 9.26% — rounds to 9.3% |
| reserves.economic_reserves.value | 980000000 tonnes | usgs_mcs_2025_copper | verified | "World total (rounded) … 980,000" — USGS MCS 2025 Reserves column (thousand metric tons; × 1000 = 980,000,000 t) |
| reserves.reserves_by_country.CL.quantity.value | 190000000 tonnes | usgs_mcs_2025_copper | verified | "Chile … 190,000" — USGS MCS 2025 Reserves column (kt; × 1000 = 190,000,000 t) |
| reserves.reserves_by_country.CL.share_pct | 19.4 | usgs_mcs_2025_copper | inferred | Not stated; 190,000 / 980,000 = 19.39% — rounds to 19.4% |
| reserves.reserves_by_country.AU.quantity.value | 100000000 tonnes | usgs_mcs_2025_copper | verified | "Australia … 100,000" — USGS MCS 2025 Reserves column; footnote 7: JORC-compliant reserves were 27 million tons |
| reserves.reserves_by_country.AU.share_pct | 10.2 | usgs_mcs_2025_copper | inferred | Not stated; 100,000 / 980,000 = 10.20% — exact match |
| reserves.reserves_by_country.PE.quantity.value | 100000000 tonnes | usgs_mcs_2025_copper | verified | "Peru … 100,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.PE.share_pct | 10.2 | usgs_mcs_2025_copper | inferred | Not stated; 100,000 / 980,000 = 10.20% — exact match |
| reserves.reserves_by_country.RU.quantity.value | 80000000 tonnes | usgs_mcs_2025_copper | verified | "Russia … 80,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.RU.share_pct | 8.2 | usgs_mcs_2025_copper | inferred | Not stated; 80,000 / 980,000 = 8.16% — rounds to 8.2% |
| reserves.reserves_by_country.CD.quantity.value | 80000000 tonnes | usgs_mcs_2025_copper | verified | "Congo (Kinshasa) … 80,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CD.share_pct | 8.2 | usgs_mcs_2025_copper | inferred | Not stated; 80,000 / 980,000 = 8.16% — rounds to 8.2% |
| reserves.reserves_by_country.MX.quantity.value | 53000000 tonnes | usgs_mcs_2025_copper | verified | "Mexico … 53,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.MX.share_pct | 5.4 | usgs_mcs_2025_copper | inferred | Not stated; 53,000 / 980,000 = 5.41% — rounds to 5.4% (truncated) |
| reserves.reserves_by_country.US.quantity.value | 47000000 tonnes | usgs_mcs_2025_copper | verified | "United States … 47,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.US.share_pct | 4.8 | usgs_mcs_2025_copper | inferred | Not stated; 47,000 / 980,000 = 4.80% — exact match |
| reserves.reserves_by_country.CN.quantity.value | 41000000 tonnes | usgs_mcs_2025_copper | verified | "China … 41,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CN.share_pct | 4.2 | usgs_mcs_2025_copper | inferred | Not stated; 41,000 / 980,000 = 4.18% — rounds to 4.2% |
| reserves.reserves_by_country.PL.quantity.value | 34000000 tonnes | usgs_mcs_2025_copper | verified | "Poland … 34,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.PL.share_pct | 3.5 | usgs_mcs_2025_copper | inferred | Not stated; 34,000 / 980,000 = 3.47% — rounds to 3.5% |
| reserves.reserves_by_country.ID.quantity.value | 21000000 tonnes | usgs_mcs_2025_copper | verified | "Indonesia … 21,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.ID.share_pct | 2.1 | usgs_mcs_2025_copper | inferred | Not stated; 21,000 / 980,000 = 2.14% — rounds to 2.1% (truncated) |
| reserves.reserves_by_country.ZM.quantity.value | 21000000 tonnes | usgs_mcs_2025_copper | verified | "Zambia … 21,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.ZM.share_pct | 2.1 | usgs_mcs_2025_copper | inferred | Not stated; 21,000 / 980,000 = 2.14% — rounds to 2.1% (truncated) |
| reserves.reserves_by_country.KZ.quantity.value | 20000000 tonnes | usgs_mcs_2025_copper | verified | "Kazakhstan … 20,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.KZ.share_pct | 2.0 | usgs_mcs_2025_copper | inferred | Not stated; 20,000 / 980,000 = 2.04% — rounds to 2.0% (truncated) |
| reserves.reserves_by_country.CA.quantity.value | 8300000 tonnes | usgs_mcs_2025_copper | verified | "Canada … 8,300" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.CA.share_pct | 0.8 | usgs_mcs_2025_copper | inferred | Not stated; 8,300 / 980,000 = 0.847% — rounds to 0.8% (truncated) |
| reserves.reserves_by_country.IN.quantity.value | 2200000 tonnes | usgs_mcs_2025_copper | verified | "India … 2,200" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.IN.share_pct | 0.2 | usgs_mcs_2025_copper | inferred | Not stated; 2,200 / 980,000 = 0.224% — rounds to 0.2% |
| reserves.reserves_by_country.ZZ.quantity.value | 180000000 tonnes | usgs_mcs_2025_copper | verified | "Other countries … 180,000" — USGS MCS 2025 Reserves column |
| reserves.reserves_by_country.ZZ.share_pct | 18.4 | usgs_mcs_2025_copper | inferred | Not stated; 180,000 / 980,000 = 18.37% — rounds to 18.4% |
| reserves.resources.value | 1500000000 tonnes | usgs_copper_resource_assessment_2015 | verified | "identified resources contained 1.5 billion tons of unextracted copper" — USGS MCS 2025 World Resources section, citing USGS SIR 2018-5160; USGS SIR landing page shows 2,100 Mt total identified (including ~600 Mt past production), consistent with 1,500 Mt remaining |
| reserves.resources notes: undiscovered 3.5B | 3500000000 tonnes | usgs_copper_resource_assessment_2015 | verified | "undiscovered resources contained an estimated 3.5 billion tons of copper" — USGS MCS 2025 World Resources section; confirmed also by SIR 2018-5160 landing page: "at least 3,500 million metric tons of undiscovered copper" |
| feedstock_origins[porphyry_copper_ore].notes: 60% | ~60% of world copper resources | usgs_copper_resource_assessment_2015 | inferred | USGS SIR 2018-5160 landing page shows porphyry deposits = 1,800 Mt identified out of 2,100 Mt total identified (~86%), not 60%. The 60% figure is widely cited for porphyry's share of world copper production (not resources). The specific claim of "60% of world copper resources" from this source could not be directly confirmed in the accessible landing-page summary; the underlying 619-page report may use a different metric or time period. |
| feedstock_origins[secondary_copper_scrap].notes: old scrap 150,000 t | 150000 tonnes | usgs_mcs_2025_copper | verified | "Old (post-consumer) scrap … provided an estimated 150,000 tons of copper in 2024" — USGS MCS 2025 Recycling section; also shown as 150 in Salient Statistics 2024e row |
| feedstock_origins[secondary_copper_scrap].notes: new scrap 720,000 t | 720000 tonnes | usgs_mcs_2025_copper | verified | "an estimated 720,000 tons of copper was recovered from new (manufacturing) scrap derived from fabricating operations" — USGS MCS 2025 Recycling section |
| feedstock_origins[secondary_copper_scrap].notes: 35% US supply | 35% | usgs_mcs_2025_copper | verified | "Copper recovered from scrap contributed about 35% of the U.S. copper supply" — USGS MCS 2025 Recycling section |
| feedstock_origins[secondary_copper_scrap].notes: 85% brass/wire-rod mills | 85% | usgs_mcs_2025_copper | verified | "Brass and wire-rod mills accounted for approximately 85% of the total copper recovered from scrap" — USGS MCS 2025 Recycling section |
| end_uses.uses[building_construction].share_pct | 42 | usgs_mcs_2025_copper | verified | "building construction, 42%" — USGS MCS 2025 Domestic Production and Use (CDA 2024 US consumption data) |
| end_uses.uses[electrical_electronic_products].share_pct | 23 | usgs_mcs_2025_copper | verified | "electrical and electronic products, 23%" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[transportation_equipment].share_pct | 18 | usgs_mcs_2025_copper | verified | "transportation equipment, 18%" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[consumer_general_products].share_pct | 10 | usgs_mcs_2025_copper | verified | "consumer and general products, 10%" — USGS MCS 2025 Domestic Production and Use |
| end_uses.uses[industrial_machinery_equipment].share_pct | 7 | usgs_mcs_2025_copper | verified | "industrial machinery and equipment, 7%" — USGS MCS 2025 Domestic Production and Use |
| prices[2024,us_domestic].value | 4.30 usd_per_lb | usgs_mcs_2025_copper | verified | "U.S. producer, cathode (COMEX + premium) … 430" (2024e cents/lb) — USGS MCS 2025 Salient Statistics table; 430 c/lb = $4.30/lb |
| prices[2024,lme].value | 4.20 usd_per_lb | usgs_mcs_2025_copper | verified | "London Metal Exchange, grade A, cash … 420" (2024e cents/lb) — USGS MCS 2025 Salient Statistics table; 420 c/lb = $4.20/lb |
| prices[2023,us_domestic].value | 3.95 usd_per_lb | usgs_mcs_2025_copper | verified | "U.S. producer, cathode … 395.3" (2023 cents/lb) — USGS MCS 2025 Salient Statistics; 395.3 c/lb ÷ 100 = $3.953 ≈ $3.95/lb |
| prices[2023,lme].value | 3.85 usd_per_lb | usgs_mcs_2025_copper | verified | "London Metal Exchange … 384.8" (2023 cents/lb) — USGS MCS 2025 Salient Statistics; 384.8 c/lb ÷ 100 = $3.848 ≈ $3.85/lb |
| prices[2022,us_domestic].value | 4.11 usd_per_lb | usgs_mcs_2025_copper | verified | "U.S. producer, cathode … 410.8" (2022 cents/lb) — USGS MCS 2025 Salient Statistics; 410.8 c/lb ÷ 100 = $4.108 ≈ $4.11/lb |
| prices[2022,lme].value | 4.00 usd_per_lb | usgs_mcs_2025_copper | verified | "London Metal Exchange … 399.8" (2022 cents/lb) — USGS MCS 2025 Salient Statistics; 399.8 c/lb ÷ 100 = $3.998 ≈ $4.00/lb |
| prices[2021,us_domestic].value | 4.32 usd_per_lb | usgs_mcs_2025_copper | verified | "U.S. producer, cathode … 432.3" (2021 cents/lb) — USGS MCS 2025 Salient Statistics; 432.3 c/lb ÷ 100 = $4.323 ≈ $4.32/lb |
| prices[2021,lme].value | 4.23 usd_per_lb | usgs_mcs_2025_copper | verified | "London Metal Exchange … 422.5" (2021 cents/lb) — USGS MCS 2025 Salient Statistics; 422.5 c/lb ÷ 100 = $4.225 ≈ $4.23/lb |
| prices[2020,us_domestic].value | 2.87 usd_per_lb | usgs_mcs_2025_copper | verified | "U.S. producer, cathode … 286.7" (2020 cents/lb) — USGS MCS 2025 Salient Statistics; 286.7 c/lb ÷ 100 = $2.867 ≈ $2.87/lb |
| prices[2020,lme].value | 2.80 usd_per_lb | usgs_mcs_2025_copper | verified | "London Metal Exchange … 279.8" (2020 cents/lb) — USGS MCS 2025 Salient Statistics; 279.8 c/lb ÷ 100 = $2.798 ≈ $2.80/lb |
| geopolitical_events[2024-01].event: Bingham Canyon mine plan | 2024-01 | usgs_mcs_2025_copper | inferred | "changes to the mine plan required to mitigate geotechnical risks resulted in lower ore grades" confirmed for 2024 — USGS MCS 2025 Events & Trends; source says "In 2024" without specifying January; date 2024-01 is not directly confirmed by source |
| geopolitical_events[2024-01].event: Kennecott Q1 return | 2024-01 | usgs_mcs_2025_copper | verified | "The Kennecott smelter and electrolytic refinery near Salt Lake City, UT, returned to normal operations in the first quarter of 2024 following major rebuilds in 2023" — USGS MCS 2025 Events & Trends; Q1 = Jan–Mar; YAML date 2024-01 is consistent with start of Q1 |
| geopolitical_events[2024-05].event: COMEX record | 2024-05 | usgs_mcs_2025_copper | verified | "The COMEX copper price reached a record high in May 2024" — USGS MCS 2025 Events & Trends |
| geopolitical_events[2024-05].notes: COMEX +9% | +9% vs 2023 | usgs_mcs_2025_copper | verified | "was projected to average $4.20 per pound in full year 2024, an increase of 9% from the annual average price in 2023" — USGS MCS 2025 Events & Trends |
| geopolitical_events[2024-12].event: Kentucky/Georgia | 2024-12 | usgs_mcs_2025_copper | verified | "A new secondary copper refinery in Kentucky and a new secondary copper smelter in Georgia were expected to begin operating by yearend 2024" — USGS MCS 2025 Events & Trends; "yearend" consistent with YAML date 2024-12 |

## Notes

**Source access**: USGS MCS 2025 Copper PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-copper.pdf) was cached by WebFetch and extracted with `pdftotext`. Full two-page chapter text extracted successfully. USGS SIR 2018-5160 (https://doi.org/10.3133/sir20185160) was accessed via the publication landing page at https://pubs.usgs.gov/publication/sir20185160 (after resolving the DOI redirect).

**Unit conversion**: USGS MCS 2025 Copper chapter header states "Data in thousand metric tons, copper content, unless otherwise specified." All country production and reserves quantities in the YAML are in million_tonnes_per_year (production) or tonnes (reserves), converted correctly: e.g., "23,000" thousand metric tons = 23 million metric tons; "980,000" thousand metric tons = 980,000,000 tonnes. Conversions are internally consistent throughout.

**Share percentages**: No percentage shares appear in the USGS source tables — the source provides only absolute quantities. All share_pct fields in the YAML are derived by dividing each country's quantity by the world total and rounding to one decimal place. All 48 computed shares (15 mine + 18 refinery + 15 reserves) match the YAML values within standard rounding behavior. Marked `inferred` following project convention (as in Co.md).

**Porphyry 60% claim**: The YAML feedstock note states porphyry deposits account for "roughly 60% of world copper resources," citing usgs_copper_resource_assessment_2015. The USGS SIR 2018-5160 landing page reports porphyry deposits hold 1,800 Mt of identified copper resources out of 2,100 Mt total (~86%). The 60% figure may refer to world copper production share (not resources), or to a metric in the full 619-page report not available in the abstract. This is a widely cited industry figure but could not be confirmed from the accessible source text. Marked `inferred`; recommend cross-checking against a USGS Copper Fact Sheet or the SIR full text in a follow-up pass.

**Australia footnote**: USGS footnote 7 states "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 27 million tons." The YAML AU reserves note correctly cites this. The YAML reserves quantity for AU (100,000,000 t = 100,000 kt = 100 Mt) is the USGS total reserves figure, not the JORC-specific 27 Mt sub-figure; both are from the source.

**US primary + secondary refinery**: The Salient Statistics table shows US primary refinery 2024e = 850 kt and secondary 2024e = 40 kt, summing to 890 kt = 0.89 Mt, matching the YAML's refining_by_country US quantity and the country-production-table US refinery value of 890.

**Net import reliance**: USGS Salient Statistics table shows net import reliance 2024e = 45%, consistent with the YAML narrative statement. No YAML field with source_id carries this number directly; the narrative is not tabulated in the Claims table.

**End-use provenance**: USGS MCS 2025 attributes the US consumption shares to "the Copper Development Association" (CDA 2024 data). The five percentages sum to 100% (42 + 23 + 18 + 10 + 7 = 100), consistent. These are US-specific consumption percentages, not global.

**Price rounding**: USGS Salient Statistics table gives prices in cents per pound to one decimal place (e.g., 395.3, 384.8, 410.8). YAML converts to USD per pound, rounding to two decimal places ($3.95, $3.85, $4.11). All conversions are arithmetically correct within standard rounding.

**Reserves completeness**: Named-country reserves sum: 190,000 + 100,000 + 100,000 + 80,000 + 80,000 + 53,000 + 47,000 + 41,000 + 34,000 + 21,000 + 21,000 + 20,000 + 8,300 + 2,200 + 180,000 = 977,500 kt. With rounding, 977,500 + the world total is 980,000 (a difference of 2,500 kt = ~0.25%) attributable to USGS rounding of the world total figure.

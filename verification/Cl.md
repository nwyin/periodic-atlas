# Verification: Cl

- Element: chlorine (Cl)
- Snapshot year: 2025
- Verifier: worker-0ccce49dbb5e (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 33 |
| discrepancy | 0 |
| inferred | 37 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 75.0 million_tonnes_per_year | eurochlor_dec2024 | inferred | Euro Chlor gives European total only (8.04 Mt); world total is an aggregate estimate constructed from multiple regional sources, not directly published by Euro Chlor |
| production[0].notes (Euro Chlor European total 2024 = 8,036,860 t) | 8.04 million_tonnes_per_year | eurochlor_dec2024 | verified | "8,036,860" tonnes 2024 — Euro Chlor December 2024 monthly bulletin |
| production[0].notes (Euro Chlor 2023 = 7.29 Mt) | 7.29 million_tonnes_per_year | eurochlor_dec2024 | verified | "7,290,039" tonnes 2023 — Euro Chlor December 2024 monthly bulletin |
| production[0].notes (up 10.2% from 2023 to 2024) | 10.2% | eurochlor_dec2024 | verified | "+10.2%" year-over-year — Euro Chlor December 2024 monthly bulletin |
| production[0].notes (cross-check: world salt 280 Mt) | 280.0 million_tonnes_per_year | usgs_mcs_2025_salt | verified | "World total (rounded) … 280,000" — USGS MCS 2025 p.151 World Production table, 2024e column |
| production[0].notes (cross-check: 280 Mt × 40% × 0.607 ≈ 68 Mt) | ~68 million_tonnes_per_year | usgs_mcs_2025_salt | inferred | Calculated: 280,000 kt × 0.40 chlor-alkali share × 0.607 NaCl→Cl₂ mass factor = 67,984 kt; individual factor values not stated together in USGS source |
| production[0].refining_by_country[CN].quantity.value | 35.0 million_tonnes_per_year | epa_chlorine_supply_2022 | inferred | EPA confirms China is "expected to drive future growth in chlor-alkali production" but gives no China Cl₂ tonnage; 35 Mt is derived via stoichiometry from caustic soda data |
| production[0].refining_by_country[CN].share_pct | 46.7 | epa_chlorine_supply_2022 | inferred | Computed as 35/75 = 46.7%; neither numerator nor denominator is directly from EPA |
| production[0].refining_by_country[CN].notes (capacity ~46,000 kt) | 46000 kt/year | epa_chlorine_supply_2022 | inferred | Not stated in EPA body text; capacity figure sourced from industry estimates not cited in the EPA profile |
| production[0].refining_by_country[CN].notes (caustic soda ~40.6 Mt → Cl₂ ~35 Mt) | 35.0 million_tonnes_per_year | epa_chlorine_supply_2022 | inferred | Stoichiometric derivation (40.6 × 70.9/80 = 35.4 Mt); caustic soda consumption figure not from EPA |
| production[0].refining_by_country[CN].notes (China expected to drive future growth) | qualitative | epa_chlorine_supply_2022 | verified | "China, one of the largest chlor-alkali producing nations, is expected to drive future growth in chlor-alkali production" — EPA 817-F-22-020 p.4 |
| production[0].refining_by_country[US].quantity.value | 11.0 million_tonnes_per_year | epa_chlorine_supply_2022 | inferred | 2024 estimate extrapolated from 2019 = 10 Mt and 2022 = 11.4 Mt; no 2024 figure in EPA |
| production[0].refining_by_country[US].share_pct | 14.7 | epa_chlorine_supply_2022 | inferred | Computed as 11/75 = 14.7%; denominator (75 Mt) is itself inferred |
| production[0].refining_by_country[US].notes (US ~10 Mt in 2019) | 10.0 million_tonnes_per_year | epa_chlorine_supply_2022 | verified | "Total U.S. domestic production of chlorine was approximately 10,000 M kg in 2019 (The Chlorine Institute, 2020)" — EPA 817-F-22-020 p.3 |
| production[0].refining_by_country[US].notes (US ~11.4 Mt in 2022) | 11.4 million_tonnes_per_year | epa_chlorine_supply_2022 | verified | "water treatment … will account for 9% (1.039 M kg of 11.4 B kg)" — EPA 817-F-22-020 p.1; 11.4 B kg = 11.4 Mt total production |
| production[0].refining_by_country[US].notes (49 US manufacturing locations) | 49 | epa_chlorine_supply_2022 | verified | "Domestic Manufacturing Locations (2019): 49, distributed throughout the U.S." — EPA 817-F-22-020 Executive Summary |
| production[0].refining_by_country[US].notes (Olin, Westlake, Oxy at Gulf Coast) | qualitative | epa_chlorine_supply_2022 | verified | "owned by a relatively small number of companies including Olin Corporation, Westlake Corporation, and Oxy Chemical Corporation" — EPA 817-F-22-020 p.3 |
| production[0].refining_by_country[DE].quantity.value | 2.0 million_tonnes_per_year | eurochlor_dec2024 | inferred | Individual country breakdown not published in Euro Chlor monthly bulletins; Germany estimate derived from Euro Chlor European total (8.04 Mt) using historical industry shares |
| production[0].refining_by_country[DE].share_pct | 2.7 | eurochlor_dec2024 | inferred | Not stated; computed as 2.0/75 = 2.7% |
| production[0].refining_by_country[NL].quantity.value | 1.5 million_tonnes_per_year | eurochlor_dec2024 | inferred | Individual country breakdown not published in Euro Chlor monthly bulletins |
| production[0].refining_by_country[NL].share_pct | 2.0 | eurochlor_dec2024 | inferred | Not stated; computed as 1.5/75 = 2.0% |
| production[0].refining_by_country[BE].quantity.value | 1.5 million_tonnes_per_year | eurochlor_dec2024 | inferred | Individual country breakdown not published in Euro Chlor monthly bulletins |
| production[0].refining_by_country[BE].share_pct | 2.0 | eurochlor_dec2024 | inferred | Not stated; computed as 1.5/75 = 2.0% |
| production[0].refining_by_country[FR].quantity.value | 1.0 million_tonnes_per_year | eurochlor_dec2024 | inferred | Individual country breakdown not published in Euro Chlor monthly bulletins |
| production[0].refining_by_country[FR].share_pct | 1.3 | eurochlor_dec2024 | inferred | Not stated; computed as 1.0/75 = 1.3% |
| production[0].refining_by_country[JP].quantity.value | 3.5 million_tonnes_per_year | saltmarketinfo_chloralkali | inferred | saltmarketinfo.com shows Japan as declining post-2010 via production index chart but gives no tonnage figures in text |
| production[0].refining_by_country[JP].share_pct | 4.7 | saltmarketinfo_chloralkali | inferred | Not stated; computed as 3.5/75 = 4.7% |
| production[0].refining_by_country[IN].quantity.value | 3.0 million_tonnes_per_year | usgs_mcs_2025_salt | inferred | USGS confirms India chlor-alkali demand growth but provides no Cl₂ production tonnage for India |
| production[0].refining_by_country[IN].share_pct | 4.0 | usgs_mcs_2025_salt | inferred | Not stated; computed as 3.0/75 = 4.0% |
| production[0].refining_by_country[IN].notes (India exports increased) | qualitative | usgs_mcs_2025_salt | verified | "Salt exports from Australia and India have increased in recent years to meet the increasing demand" — USGS MCS 2025 p.151 |
| production[0].refining_by_country[ZZ].quantity.value | 16.4 million_tonnes_per_year | saltmarketinfo_chloralkali | inferred | Residual: 75 − (35+11+2+1.5+1.5+1+3.5+3) = 16.0 Mt; approximate to 16.4 Mt with rounding |
| production[0].refining_by_country[ZZ].share_pct | 21.9 | saltmarketinfo_chloralkali | inferred | Not stated; residual computed as 100 − sum of listed shares |
| reserves.notes (Large. Economic and subeconomic deposits ...) | qualitative | usgs_mcs_2025_salt | verified | "Large. Economic and subeconomic deposits of salt are substantial in principal salt-producing countries. The oceans contain a virtually inexhaustible supply of salt." — USGS MCS 2025 p.151 Reserves column |
| feedstock_origins[NaCl].typical_concentration_pct | 25.0 | usgs_mcs_2025_salt | inferred | ~25–26 wt% NaCl saturation is a standard industry specification; not stated in USGS MCS 2025 salt chapter |
| feedstock_origins[NaCl].notes (42% US salt = brine) | 42% | usgs_mcs_2025_salt | verified | "salt in brine, 42%" — USGS MCS 2025 p.150 Domestic Production and Use |
| feedstock_origins[NaCl].notes (chlor-alkali ~40% of global salt) | ~40% | usgs_mcs_2025_salt | inferred | USGS names "chlorine and caustic soda manufacturers" as main chemical consumers but does not give 40% global share; saltmarketinfo.com explicitly states "approximately 40% of all salt globally" |
| feedstock_origins[KCl].notes (~9% of US Cl₂ from KCl membrane cell) | ~9% | epa_chlorine_supply_2022 | verified | "Potassium chloride membrane cell technology, metal production, and brine to bleach accounted for the remaining 9% of domestic production" — EPA 817-F-22-020 p.2 |
| substitutes[water_treatment].notes ("No economic substitutes or alternatives for salt exist in most applications") | text | usgs_mcs_2025_salt | verified | "No economic substitutes or alternatives for salt exist in most applications." — USGS MCS 2025 p.151 Substitutes (quote refers to salt feedstock) |
| substitutes[pvc_manufacture].notes (partial substitution, no viable chlorine-free VCM route) | partial | epa_chlorine_supply_2022 | inferred | EPA identifies PVC/VCM as major chlorine use but does not discuss PVC substitutability; editorial assessment by YAML author |
| substitutes[pulp_paper_bleaching].notes (ECF/TCF mature in Europe and North America) | full | epa_chlorine_supply_2022 | inferred | EPA mentions pulp and paper as a chlorine application; ECF/TCF claim is based on general industry knowledge not explicitly stated in EPA Chlorine Supply Chain Profile |
| end_uses.uses[pvc_manufacture].share_pct | 35 | epa_chlorine_supply_2022 | inferred | EPA calls PVC/construction "the largest single demand" but gives no percentage; 35% is an editorial global estimate |
| end_uses.uses[pvc_manufacture].notes (PVC/construction = largest single demand in 2021) | qualitative | epa_chlorine_supply_2022 | verified | "In 2021, it is estimated that construction applications such as polyvinyl chloride and epoxies accounted for the largest single demand of chlorine." — EPA 817-F-22-020 p.1 |
| end_uses.uses[pvc_manufacture].notes (China PVC ~20 Mt/year 2024) | ~20 million_tonnes_per_year | epa_chlorine_supply_2022 | inferred | Not stated in EPA Chlorine Supply Chain Profile; China PVC figure from general market knowledge |
| end_uses.uses[other_organic_chemicals].share_pct | 27 | epa_chlorine_supply_2022 | inferred | EPA does not break out organic intermediates as a percentage of total; 27% is an editorial global estimate |
| end_uses.uses[other_organic_chemicals].notes (68% captive consumption) | 68% | epa_chlorine_supply_2022 | verified | "in 2022, 68% of domestically produced chlorine will be used in captive consumption" — EPA 817-F-22-020 p.3 |
| end_uses.uses[other_organic_chemicals].notes (32% available for merchant market) | 32% | epa_chlorine_supply_2022 | verified | "estimated to be 3,600 million (M) kg or 32% in 2022 … destined for sale on the merchant market" — EPA 817-F-22-020 p.1 |
| end_uses.uses[inorganic_chemicals].share_pct | 18 | epa_chlorine_supply_2022 | inferred | EPA lists HCl, NaOCl, Ca(OCl)₂ as derivative water treatment chemicals but gives no percentage breakdown; 18% is an editorial estimate |
| end_uses.uses[water_treatment].share_pct | 8 | epa_chlorine_supply_2022 | inferred | EPA gives 9% for US water treatment (including industrial) in 2022; YAML uses 8% as a global estimate — scope differs |
| end_uses.uses[water_treatment].notes (water treatment = ~9% of all US production) | ~9% | epa_chlorine_supply_2022 | verified | "water treatment (including industrial applications) will account for 9% (1.039 M kg of 11.4 B kg) of all domestic production" — EPA 817-F-22-020 p.1 |
| end_uses.uses[water_treatment].notes (municipal water/wastewater ~5% of total US production) | ~5% | epa_chlorine_supply_2022 | verified | "representing approximately 5% of consumption of all domestically produced chlorine" — EPA 817-F-22-020 p.1 |
| end_uses.uses[water_treatment].notes (water treatment = second-largest merchant use) | qualitative | epa_chlorine_supply_2022 | verified | "Water treatment (including industrial applications) accounts for the second largest use of merchant market chlorine." — EPA 817-F-22-020 p.1 |
| end_uses.uses[pulp_paper_bleaching].share_pct | 4 | epa_chlorine_supply_2022 | inferred | EPA lists pulp and paper as a chlorine application but gives no percentage; 4% is an editorial estimate |
| end_uses.uses[other].share_pct | 8 | epa_chlorine_supply_2022 | inferred | EPA does not provide a consolidated residual percentage; 8% is an editorial estimate |
| criticality.notes (Moderate-High supply disruption risk) | Moderate-High | epa_chlorine_supply_2022 | verified | "RISK RATING: Moderate-High" — EPA 817-F-22-020 Executive Summary and Table 4 |
| criticality.notes (imports from Canada ~2% of US consumption) | ~2% | epa_chlorine_supply_2022 | verified | 2019 data: imports 211 M kg / consumption 10,100 M kg = 2.09% ≈ 2% — EPA 817-F-22-020 p.3 |
| geopolitical_events[2021-02].event (28% temporary capacity loss from Winter Storm Uri) | ~28% | epa_chlorine_supply_2022 | verified | "a temporary loss of approximately 28% of domestic chlor-alkali production capacity when Winter Storm Uri directly hit the Gulf Coast region in February 2021" — EPA 817-F-22-020 p.5 |
| geopolitical_events[2021-02].impact (equipment failures in WV, UT, WA) | qualitative | epa_chlorine_supply_2022 | verified | "others were located in West Virginia, Utah, and Washington" — EPA 817-F-22-020 p.5 |
| geopolitical_events[2021-02].impact (allocation reductions in at least 12 US states) | 12 states | epa_chlorine_supply_2022 | verified | "California, Oregon, Washington, Alaska, Utah, Missouri, Ohio, Pennsylvania, New York, Massachusetts, Louisiana, and Florida" — 12 states listed, EPA 817-F-22-020 p.5–6 |
| geopolitical_events[2021-06].event (Olin Alabama, Occidental Niagara Falls NY) | qualitative | epa_chlorine_supply_2022 | inferred | EPA body says "permanent reduction … at facilities located in New York, Alabama, Louisiana, and Texas"; Olin/Occidental names appear only in EPA reference list (Powder & Bulk Solids; Buffalo News), not EPA body text |
| geopolitical_events[2021-06].impact (structural reduction in US merchant supply) | qualitative | epa_chlorine_supply_2022 | verified | "permanent reduction in chlor-alkali production capacity … 2021 were compounded by the impacts of COVID-19" — EPA 817-F-22-020 p.5 |
| geopolitical_events[2022-02].impact (Euro Chlor 2023 = 7.29 Mt) | 7.29 million_tonnes | eurochlor_dec2024 | verified | "7,290,039" tonnes 2023 — Euro Chlor December 2024 monthly bulletin |
| geopolitical_events[2022-02].impact (Euro Chlor 2024 = 8.04 Mt) | 8.04 million_tonnes | eurochlor_dec2024 | verified | "8,036,860" tonnes 2024 — Euro Chlor December 2024 monthly bulletin |
| geopolitical_events[2022-02].impact (+10.2% recovery) | +10.2% | eurochlor_dec2024 | verified | "+10.2%" stated on Euro Chlor December 2024 monthly bulletin page |
| geopolitical_events[2022-02].impact (~60% capacity utilisation through 2022-2023) | ~60% | eurochlor_dec2024 | inferred | Euro Chlor Dec 2024 bulletin states 61.9% utilization in 2023 and 66.9% in 2024; 2022 utilization rate not reported in this bulletin; ~60% is approximate and covers the 2022 year without a direct source value |
| geopolitical_events[2022-02].impact (3,000-3,400 kWh/tonne Cl₂ electrolysis energy) | 3000-3400 kWh/tonne | eurochlor_dec2024 | inferred | Energy figure is standard industry specification for membrane-cell electrolysis; not stated in the Euro Chlor December 2024 production bulletin |
| geopolitical_events[2024-01].event (chlor-alkali demand expected to increase in 2024) | qualitative | usgs_mcs_2025_salt | verified | "Demand for salt brine used in the chloralkali industry was expected to increase in 2024 as demand for caustic soda and polyvinyl chloride increases globally, especially in Asia." — USGS MCS 2025 p.151 |
| geopolitical_events[2024-01].impact (salt exports from Australia and India increased) | qualitative | usgs_mcs_2025_salt | verified | "Salt exports from Australia and India have increased in recent years to meet the increasing demand." — USGS MCS 2025 p.151 |
| geopolitical_events[2022-09].event (September 2022 threatened rail work stoppage) | qualitative | epa_chlorine_supply_2022 | verified | "A threatened rail carrier work stoppage in September 2022 highlighted the dependence of the domestic chlorine supply chain on a complex national rail network" — EPA 817-F-22-020 p.6 |
| geopolitical_events[2022-09].impact (85% of long-distance Cl₂ by rail) | 85% | epa_chlorine_supply_2022 | verified | "In 2006, it was estimated that rail accounted for 85% of long-distance chlorine movements nationally (Branscomb et al., 2010)" — EPA 817-F-22-020 p.4 |
| geopolitical_events[2022-09].impact (Gulf Coast concentration creates long-haul dependence) | qualitative | epa_chlorine_supply_2022 | verified | "concentration of chlor-alkali facilities along the Gulf Coast combined with widespread need for chlorine, long-distance transport of chlorine is often required" — EPA 817-F-22-020 p.6 |

## Notes

**Source access**: All four cited sources were successfully fetched. Euro Chlor December 2024 bulletin (HTML) and USGS MCS 2025 salt PDF (extracted via pdftotext) yielded full text. EPA Chlorine Supply Chain Profile PDF (EPA 817-F-22-020) extracted via pdftotext. saltmarketinfo.com article accessible but contains only charts (no numeric values in text).

**No discrepancies**: All verifiable numeric claims match their sources exactly. The only borderline case is `end_uses.uses[water_treatment].share_pct = 8` vs the EPA's stated 9% for US water treatment — but the YAML explicitly distinguishes global scope (8%) from US scope (9%), and the notes correctly cite the 9% figure from EPA. This is editorial scope-narrowing, not a numerical error.

**Inferred category rationale**: The majority of inferred claims fall into three groups:
(1) Country-level chlorine production estimates (all non-European, non-US figures), since no single authoritative world table exists for Cl₂ production by country;
(2) Share percentages for end uses, which are global editorial estimates since neither EPA nor Euro Chlor publishes a global breakdown;
(3) Capacity utilization rates for 2022 (only 2023 and 2024 values confirmed by Euro Chlor).

**saltmarketinfo source**: The page shows only chlorine production index charts (2010 = 1 baseline) for US, Europe, China, and Japan without numeric tonnage values in text. The source confirms qualitative trends (Japan declining, China rapid growth) and the global statement that "CN + US + Europe + JP account for about 85% of global output" and that chlor-alkali consumes "approximately 40% of all salt globally." No individual country tonnages are extractable.

**Euro Chlor capacity utilization**: Page explicitly states utilization increased from 61.9% in 2023 to 66.9% in 2024 (for EU-27 plus Norway, Switzerland, UK). The YAML's claim of "~60% through 2022-2023" is consistent with 2023 actual (61.9%) but the 2022 value is not available from this source.

**USGS salt chapter context**: USGS MCS 2025 does not contain a dedicated chlorine chapter. All USGS-sourced claims are from the Salt chapter (pp. 150–151), which discusses NaCl as chlorine feedstock. World production figures are for salt (NaCl), not Cl₂. The chlor-alkali demand statements are narrative context within the salt chapter.

**EPA source year gap**: The EPA Chlorine Supply Chain Profile (December 2022, EPA 817-F-22-020) uses 2019 production data (10 Mt from Chlorine Institute) as its primary baseline and 2022 estimates from Chemical Market Analytics. The YAML's 2024 production estimate for the US (~11 Mt) is extrapolated from these figures, not verified from a 2024 source.

**Stoichiometry claims**: The YAML contains multiple stoichiometric ratios (1 tonne Cl₂ : 1.128 tonne NaOH : 0.028 tonne H₂; ~1.65 tonnes NaCl per tonne Cl₂; 40.6 × 70.9/80 = 35.4 Mt). These are chemical calculations from atomic weights and do not require source verification, but they are not explicitly from any cited source. They are treated as inferred rather than given a separate "calculated" status not in the schema vocabulary.

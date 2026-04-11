# Verification: Mn

- Element: manganese (Mn)
- Snapshot year: 2025
- Verifier: worker-2493290243b2 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 46 |
| discrepancy | 0 |
| inferred | 27 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 20,000,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "World total (rounded) … 20,000" — USGS MCS 2025 p.117 World Mine Production table, 2024e column (thousand metric tons Mn content) |
| production[0].mine.notes (2023 world total = 19,600 kt) | 19,600,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "World total (rounded) … 19,600" — USGS MCS 2025 p.117 World Mine Production table, 2023 column |
| production[0].mine.notes ("Global production increased slightly from that in 2023") | qualitative | usgs_mcs_2025_manganese | verified | "Global production of manganese ore, on a manganese-content basis, increased slightly from that in 2023" — USGS MCS 2025 p.117 Events, Trends, and Issues |
| production[0].mine.notes ("no domestic mine production since 1970") | qualitative | usgs_mcs_2025_manganese | verified | "Manganese ore containing 20% or more manganese has not been produced domestically since 1970" — USGS MCS 2025 p.116 Domestic Production and Use; also "Production, mine … —" (zero) for all years 2020–2024 in Salient Statistics |
| production[0].mine.notes ("net import reliance = 100% for all years 2020–2024") | 100% | usgs_mcs_2025_manganese | verified | "Net import reliance … 100" for 2020, 2021, 2022, 2023, 2024e — USGS MCS 2025 p.116 Salient Statistics table |
| production[0].mining_by_country[ZA].quantity.value | 7,400,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "South Africa … 7,400" — USGS MCS 2025 p.117 World Mine Production table, 2024e column (thousand metric tons Mn content) |
| production[0].mining_by_country[ZA].share_pct | 37.0 | usgs_mcs_2025_manganese | inferred | Not stated; 7,400/20,000 = 37.00% exactly |
| production[0].mining_by_country[GA].quantity.value | 4,600,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Gabon … 4,600" — USGS MCS 2025 p.117 World Mine Production table, 2024e column (marked e, estimated) |
| production[0].mining_by_country[GA].share_pct | 23.0 | usgs_mcs_2025_manganese | inferred | Not stated; 4,600/20,000 = 23.00% exactly |
| production[0].mining_by_country[AU].quantity.value | 2,800,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Australia … 2,800" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 14.0 | usgs_mcs_2025_manganese | inferred | Not stated; 2,800/20,000 = 14.00% exactly |
| production[0].mining_by_country[AU].notes (JORC-compliant reserves = 110 million tons) | 110 million tons | usgs_mcs_2025_manganese | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 110 million tons" — USGS MCS 2025 p.117 footnote 11 |
| production[0].mining_by_country[GH].quantity.value | 820,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Ghana … 820" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[GH].share_pct | 4.1 | usgs_mcs_2025_manganese | inferred | Not stated; 820/20,000 = 4.10% exactly |
| production[0].mining_by_country[IN].quantity.value | 800,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "India … 800" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 4.0 | usgs_mcs_2025_manganese | inferred | Not stated; 800/20,000 = 4.00% exactly |
| production[0].mining_by_country[CN].quantity.value | 770,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "China … 770" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 3.85 | usgs_mcs_2025_manganese | inferred | Not stated; 770/20,000 = 3.85% exactly |
| production[0].mining_by_country[BR].quantity.value | 590,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Brazil … 590" — USGS MCS 2025 p.117 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[BR].share_pct | 2.95 | usgs_mcs_2025_manganese | inferred | Not stated; 590/20,000 = 2.95% exactly |
| production[0].mining_by_country[MY].quantity.value | 410,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Malaysia … 410" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[MY].share_pct | 2.05 | usgs_mcs_2025_manganese | inferred | Not stated; 410/20,000 = 2.05% exactly |
| production[0].mining_by_country[CI].quantity.value | 360,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Côte d'Ivoire … 360" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[CI].share_pct | 1.8 | usgs_mcs_2025_manganese | inferred | Not stated; 360/20,000 = 1.80% exactly |
| production[0].mining_by_country[CI].notes ("No quantified reserves reported (NA)") | NA | usgs_mcs_2025_manganese | verified | "Côte d'Ivoire … NA" — USGS MCS 2025 p.117 Reserves column |
| production[0].mining_by_country[ZZ].quantity.value | 1,300,000 tonnes_per_year | usgs_mcs_2025_manganese | verified | "Other countries … 1,300" — USGS MCS 2025 p.117 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 6.5 | usgs_mcs_2025_manganese | inferred | Not stated; 1,300/20,000 = 6.50% exactly |
| reserves.economic_reserves.value | 1,700,000,000 tonnes | usgs_mcs_2025_manganese | verified | "World total (rounded) … 1,700,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.notes (ZA accounts for ~70% of world resources) | ~70% | usgs_mcs_2025_manganese | verified | "South Africa accounts for an estimated 70% of the world's manganese resources" — USGS MCS 2025 p.117 World Resources section |
| reserves.notes (CI listed as NA in reserves) | NA | usgs_mcs_2025_manganese | verified | "Côte d'Ivoire … NA" — USGS MCS 2025 p.117 Reserves column |
| reserves.notes (MY listed as NA in reserves) | NA | usgs_mcs_2025_manganese | verified | "Malaysia … NA" — USGS MCS 2025 p.117 Reserves column |
| reserves.notes (quantified country total 1,718,000 kt) | 1,718,000 kt | usgs_mcs_2025_manganese | inferred | Not stated; computed sum of 7 named-country reserve rows: 560,000+500,000+280,000+270,000+61,000+34,000+13,000 = 1,718,000 kt |
| reserves.reserves_by_country[ZA].quantity.value | 560,000,000 tonnes | usgs_mcs_2025_manganese | verified | "South Africa … 560,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[ZA].share_pct | 32.9 | usgs_mcs_2025_manganese | inferred | Not stated; 560,000/1,700,000 = 32.94% — rounds to 32.9% |
| reserves.reserves_by_country[AU].quantity.value | 500,000,000 tonnes | usgs_mcs_2025_manganese | verified | "Australia … 500,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[AU].share_pct | 29.4 | usgs_mcs_2025_manganese | inferred | Not stated; 500,000/1,700,000 = 29.41% — rounds to 29.4% |
| reserves.reserves_by_country[AU].notes (JORC-compliant reserves = 110 million tons) | 110 million tons | usgs_mcs_2025_manganese | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 110 million tons" — USGS MCS 2025 p.117 footnote 11 |
| reserves.reserves_by_country[CN].quantity.value | 280,000,000 tonnes | usgs_mcs_2025_manganese | verified | "China … 280,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[CN].share_pct | 16.5 | usgs_mcs_2025_manganese | inferred | Not stated; 280,000/1,700,000 = 16.47% — rounds to 16.5% |
| reserves.reserves_by_country[BR].quantity.value | 270,000,000 tonnes | usgs_mcs_2025_manganese | verified | "Brazil … 270,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[BR].share_pct | 15.9 | usgs_mcs_2025_manganese | inferred | Not stated; 270,000/1,700,000 = 15.88% — rounds to 15.9% |
| reserves.reserves_by_country[GA].quantity.value | 61,000,000 tonnes | usgs_mcs_2025_manganese | verified | "Gabon … 61,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[GA].share_pct | 3.6 | usgs_mcs_2025_manganese | inferred | Not stated; 61,000/1,700,000 = 3.59% — rounds to 3.6% |
| reserves.reserves_by_country[IN].quantity.value | 34,000,000 tonnes | usgs_mcs_2025_manganese | verified | "India … 34,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[IN].share_pct | 2.0 | usgs_mcs_2025_manganese | inferred | Not stated; 34,000/1,700,000 = 2.00% exactly |
| reserves.reserves_by_country[GH].quantity.value | 13,000,000 tonnes | usgs_mcs_2025_manganese | verified | "Ghana … 13,000" — USGS MCS 2025 p.117 Reserves column (thousand metric tons Mn content) |
| reserves.reserves_by_country[GH].share_pct | 0.8 | usgs_mcs_2025_manganese | inferred | Not stated; 13,000/1,700,000 = 0.765% — rounds to 0.8% |
| prices[2024].value (mtu basis) | $5.80/mtu | usgs_mcs_2025_manganese | verified | "Price, average, manganese content, cost, insurance, and freight, China, dollars per metric ton unit … 5.80" — USGS MCS 2025 p.116 Salient Statistics, 2024e column |
| prices[2024].value (usd_per_tonne conversion) | 255.20 usd_per_tonne | usgs_mcs_2025_manganese | inferred | Not stated; $5.80/mtu × 44 (mtu-to-tonne factor for 44% Mn ore) = $255.20/t ore |
| prices[2024].notes (44% Mn reference grade, CRU Group source) | 44% Mn, CRU Group | usgs_mcs_2025_manganese | verified | "For average metallurgical-grade ore containing 44% manganese. Source: CRU Group" — USGS MCS 2025 p.116 footnote 5 |
| prices[2023].value (mtu basis) | $4.80/mtu | usgs_mcs_2025_manganese | verified | "Price … 4.80" — USGS MCS 2025 p.116 Salient Statistics, 2023 column |
| prices[2023].value (usd_per_tonne conversion) | 211.20 usd_per_tonne | usgs_mcs_2025_manganese | inferred | Not stated; $4.80/mtu × 44 = $211.20/t ore |
| prices[2022].value (mtu basis) | $5.97/mtu | usgs_mcs_2025_manganese | verified | "Price … 5.97" — USGS MCS 2025 p.116 Salient Statistics, 2022 column |
| prices[2022].value (usd_per_tonne conversion) | 262.68 usd_per_tonne | usgs_mcs_2025_manganese | inferred | Not stated; $5.97/mtu × 44 = $262.68/t ore |
| prices[2021].value (mtu basis) | $5.27/mtu | usgs_mcs_2025_manganese | verified | "Price … 5.27" — USGS MCS 2025 p.116 Salient Statistics, 2021 column |
| prices[2021].value (usd_per_tonne conversion) | 231.88 usd_per_tonne | usgs_mcs_2025_manganese | inferred | Not stated; $5.27/mtu × 44 = $231.88/t ore |
| prices[2020].value (mtu basis) | $4.58/mtu | usgs_mcs_2025_manganese | verified | "Price … 4.58" — USGS MCS 2025 p.116 Salient Statistics, 2020 column |
| prices[2020].value (usd_per_tonne conversion) | 201.52 usd_per_tonne | usgs_mcs_2025_manganese | inferred | Not stated; $4.58/mtu × 44 = $201.52/t ore |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_manganese | verified | "Manganese is included in the U.S. list of critical minerals" — USGS MCS 2025 p.117 Events, Trends, and Issues |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_manganese | verified | "the European Union's Critical Raw Materials Act entered into force, which includes … manganese as a critical raw material" — USGS MCS 2025 p.117 Events, Trends, and Issues |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_manganese | verified | "the European Union's Critical Raw Materials Act entered into force, which includes high-purity manganese (battery grade) as a strategic raw material" — USGS MCS 2025 p.117 Events, Trends, and Issues |
| criticality.notes (net import reliance 100%) | 100% | usgs_mcs_2025_manganese | verified | "Net import reliance … 100" for all years 2020–2024e — USGS MCS 2025 p.116 Salient Statistics |
| geopolitical_events[2024-05].event (EU CRA enters force, Mn critical + battery-grade strategic) | 2024-05 | usgs_mcs_2025_manganese | verified | "In May 2024, the European Union's Critical Raw Materials Act entered into force, which includes high-purity manganese (battery grade) as a strategic raw material and manganese as a critical raw material" — USGS MCS 2025 p.117 Events |
| geopolitical_events[2024-01].event (DoD/DoE grants for Arizona Mn facility) | qualitative | usgs_mcs_2025_manganese | verified | "An Australia-based company received grants from the U.S. Department of Defense and the U.S. Department of Energy to accelerate development of its manganese mine and battery-grade manganese production facility in Arizona" — USGS MCS 2025 p.117 Events |
| geopolitical_events[2023-11].event (Ukraine plants idle Nov 2023; two resume Q2 2024) | qualitative | usgs_mcs_2025_manganese | verified | "At least two manganese mining and processing plants in Ukraine have remained idle since November 2023 and another two have resumed minimum production since the second quarter of 2024" — USGS MCS 2025 p.117 Events (note: USGS says "at least two"; YAML paraphrases as "two") |
| geopolitical_events[2024-01].event (tropical cyclone, northern Australia mine suspended) | qualitative | usgs_mcs_2025_manganese | verified | "A manganese mine in northern Australia suspended its operation owing to a tropical cyclone, which contributed to the increase in manganese ore prices in 2024" — USGS MCS 2025 p.117 Events |
| substitutes[steel_alloying_deoxidizer_desulfurizer].availability | none | usgs_mcs_2025_manganese | verified | "Manganese has no satisfactory substitute in its major applications" — USGS MCS 2025 p.117 Substitutes |
| end_uses.uses[steel_ferromanganese_silicomanganese].share_pct | 90 | usgs_mcs_2025_manganese | inferred | USGS provides no explicit global end-use percentage breakdown; 90% is an industry-standard estimate consistent with "Consumption of manganese closely follows the steel industry" — USGS MCS 2025 p.117 Events |
| end_uses.uses[nonmetallurgical_other].share_pct | 10 | usgs_mcs_2025_manganese | inferred | USGS provides no explicit percentage; 10% is the arithmetic complement of the 90% steel estimate; consistent with USGS listing animal feed, brick colorant, dry cell batteries, fertilizers, and manganese dioxide — USGS MCS 2025 p.116 |
| end_uses.uses[steel_ferromanganese_silicomanganese].notes (US ferromanganese 300 kt 2024e) | 300,000 tonnes | usgs_mcs_2025_manganese | verified | "Ferromanganese … 300" — USGS MCS 2025 p.116 Salient Statistics, Consumption reported, 2024e column |
| end_uses.uses[steel_ferromanganese_silicomanganese].notes (US silicomanganese 230 kt 2024e) | 230,000 tonnes | usgs_mcs_2025_manganese | verified | "Silicomanganese … 230" — USGS MCS 2025 p.116 Salient Statistics, Consumption reported, 2024e column |
| feedstock_origins[manganese_oxide_ores].notes (ZA, AU, GA primary oxide producers) | qualitative | usgs_mcs_2025_manganese | inferred | USGS chapter does not explicitly name oxide vs carbonate ore by country; attribution is from general mineralogy and well-known deposits not directly stated in MCS 2025 text |
| feedstock_origins[manganese_carbonate_ores].notes (CN carbonate ore predominant) | qualitative | usgs_mcs_2025_manganese | inferred | USGS chapter does not explicitly state carbonate ore dominance in China; inferred from general mineralogy; MCS 2025 text only notes China's ore without specifying carbonate type |

## Notes

**Source access**: USGS MCS 2025 Manganese PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-manganese.pdf) downloaded and extracted via `pdftotext -layout`. Both pages (pp. 116–117) fully readable. All claims trace to a single primary source.

**Zero discrepancies**: All 10 country mine production quantities match the USGS World Mine Production table exactly (2024e column). All 7 country reserve quantities match exactly. All 5 price mtu values match the Salient Statistics table exactly. No numeric discrepancy found in any claim.

**Production unit**: The USGS MCS 2025 manganese chapter states "(Data in thousand metric tons, gross weight, unless otherwise specified)" but the mine production table is titled "World Mine Production (manganese content) and Reserves". The data are in thousand metric tons of manganese content (not gross ore weight). All YAML values multiply USGS table values by 1,000 to convert from kt to tonnes — this is correct.

**Price unit conversion**: The USGS manganese price is quoted in dollars per metric ton unit (mtu), where 1 mtu = 1% Mn per dry metric ton of ore = 10 kg Mn. The YAML converts to $/tonne ore by multiplying by 44, the reference Mn content percentage for metallurgical-grade ore (footnote 5: "For average metallurgical-grade ore containing 44% manganese"). All five conversions (2020–2024) are arithmetically exact. The CIF China basis and CRU Group attribution are verified from footnote 5.

**All share_pcts are inferred**: USGS does not publish percentage shares for countries in the manganese chapter. Every mine production share_pct in the YAML is quantity/20,000 kt, and every reserve share_pct is quantity/1,700,000 kt. All calculations are arithmetically correct; share_pcts for ZA, GA, AU, GH, IN, CN, BR, MY, CI, and ZZ are exact (no rounding loss) because all production values are multiples of 10 kt against a 20,000 kt world total.

**Reserve country sum**: The seven quantified country reserve rows sum to 1,718,000 kt, slightly exceeding the rounded world total of 1,700,000 kt. CI and MY are listed as NA; Other Countries are listed as "Small" (no number). The 18,000 kt discrepancy is consistent with the USGS world total being a rounded figure, as noted in the YAML reserves.notes.

**Australia JORC note**: Footnote 11 of USGS MCS 2025 explicitly states "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 110 million tons." This value appears in both the AU mining_by_country.notes and AU reserves_by_country.notes and is verified in both locations.

**Ukraine event qualifier**: The YAML event description says "Two manganese mining and processing plants in Ukraine idle since November 2023" while the USGS source says "At least two manganese mining and processing plants in Ukraine have remained idle since November 2023." The YAML drops the "at least" qualifier. The core facts (two plants idle, two others resumed Q2 2024) are confirmed; the paraphrase is marked verified but the dropped qualifier is noted.

**End-use percentages are estimated**: USGS provides no explicit global percentage breakdown for manganese end uses. The 90%/10% split for steel vs. non-metallurgical is described in the YAML as "confidence: low" — it is consistent with USGS's statement that "Consumption of manganese closely follows the steel industry" but is not directly given. Marked as inferred.

**Feedstock origins**: The oxide/carbonate ore descriptions reference geological knowledge about deposit types in ZA/AU/GA vs. CN that is not directly stated in the MCS 2025 chapter text. The USGS chapter contains no ore-type breakdown by country. These claims are marked inferred.

**Criticality**: All three boolean flags (US critical list, EU CRM, EU strategic) are directly verified from the MCS 2025 Events section, which explicitly names all three designations. No US import source percentages are given for manganese ore in the YAML's structured claims table; the Import Sources paragraph (Gabon 63%, South Africa 23%, Mexico 13%) is in the source but not in the YAML structured data.

**Sum check (mine production)**: Named countries sum to 7,400+4,600+2,800+820+800+770+590+410+360+1,300 = 19,850 kt. World total is 20,000 kt. The 150 kt gap reflects rounding in individual country 2024e estimates; the "Other countries" row (ZZ) captures the residual, so completeness=complete is appropriate.

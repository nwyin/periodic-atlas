# Verification: Sb

- Element: antimony (Sb)
- Snapshot year: 2025
- Verifier: worker-4992f077e2d3 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 50 |
| discrepancy | 0 |
| inferred | 29 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 100000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 World Mine Production table: `"World total (rounded) 100,000"` |
| production[0].mine.notes secondary production | 3500 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Salient Statistics table, Secondary 2024e: `"3,500"` |
| production[0].mining_by_country[CN].quantity.value | 60000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"China ... 60,000"` |
| production[0].mining_by_country[CN].share_pct | 60.0 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 60,000 / 100,000 = 60.0%. |
| production[0].mining_by_country[TJ].quantity.value | 17000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Tajikistan ... 17,000"` |
| production[0].mining_by_country[TJ].share_pct | 17.0 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 17,000 / 100,000 = 17.0%. |
| production[0].mining_by_country[RU].quantity.value | 13000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Russia ... 13,000"` |
| production[0].mining_by_country[RU].share_pct | 13.0 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 13,000 / 100,000 = 13.0%. |
| production[0].mining_by_country[MM].quantity.value | 4500 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Burma ... e4,500"` |
| production[0].mining_by_country[MM].share_pct | 4.5 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 4,500 / 100,000 = 4.5%. |
| production[0].mining_by_country[BO].quantity.value | 3700 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Bolivia ... 3,700"` |
| production[0].mining_by_country[BO].share_pct | 3.7 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 3,700 / 100,000 = 3.7%. |
| production[0].mining_by_country[AU].quantity.value | 2000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Australia ... 2,000"` |
| production[0].mining_by_country[AU].share_pct | 2.0 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 2,000 / 100,000 = 2.0%. |
| production[0].mining_by_country[TR].quantity.value | 1600 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Turkey ... e1,600"` |
| production[0].mining_by_country[TR].share_pct | 1.6 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 1,600 / 100,000 = 1.6%. |
| production[0].mining_by_country[MX].quantity.value | 800 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Mexico ... 800"` |
| production[0].mining_by_country[MX].share_pct | 0.8 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 800 / 100,000 = 0.8%. |
| production[0].mining_by_country[IR].quantity.value | 500 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Iran ... e500"` |
| production[0].mining_by_country[IR].share_pct | 0.5 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 500 / 100,000 = 0.5%. |
| production[0].mining_by_country[VN].quantity.value | 300 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Vietnam ... 300"` |
| production[0].mining_by_country[VN].share_pct | 0.3 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 300 / 100,000 = 0.3%. |
| production[0].mining_by_country[PK].quantity.value | 250 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Pakistan ... 250"` |
| production[0].mining_by_country[PK].share_pct | 0.25 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 250 / 100,000 = 0.25%. |
| production[0].mining_by_country[LA].quantity.value | 200 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Laos ... e200"` |
| production[0].mining_by_country[LA].share_pct | 0.2 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 200 / 100,000 = 0.2%. |
| production[0].mining_by_country[GT].quantity.value | 50 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Guatemala ... 50"` |
| production[0].mining_by_country[GT].share_pct | 0.05 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 50 / 100,000 = 0.05%. |
| production[0].mining_by_country[KZ].quantity.value | 40 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Kazakhstan ... e40"` |
| production[0].mining_by_country[KZ].share_pct | 0.04 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 40 / 100,000 = 0.04%. |
| production[0].mining_by_country[KG].quantity.value | 20 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 table: `"Kyrgyzstan ... 20"` |
| production[0].mining_by_country[KG].share_pct | 0.02 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from p.35 table values 20 / 100,000 = 0.02%. |
| reserves.economic_reserves.value | 2000000 tonnes | usgs_mcs_2025_antimony | inferred | Source gives a lower bound, not an exact reserve total: USGS MCS 2025 p.35 reserves column shows `" >2,000,000 "` for world total. |
| reserves.reserves_by_country[CN].quantity.value | 670000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"China ... 670,000"` |
| reserves.reserves_by_country[CN].share_pct | 29.71 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 670,000 / 2,255,000 = 29.71%. |
| reserves.reserves_by_country[RU].quantity.value | 350000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Russia ... 350,000"` |
| reserves.reserves_by_country[RU].share_pct | 15.52 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 350,000 / 2,255,000 = 15.52%. |
| reserves.reserves_by_country[BO].quantity.value | 310000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Bolivia ... 310,000"` |
| reserves.reserves_by_country[BO].share_pct | 13.75 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 310,000 / 2,255,000 = 13.75%. |
| reserves.reserves_by_country[KG].quantity.value | 260000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Kyrgyzstan ... 260,000"` |
| reserves.reserves_by_country[KG].share_pct | 11.53 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 260,000 / 2,255,000 = 11.53%. |
| reserves.reserves_by_country[AU].quantity.value | 140000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Australia ... 140,000"` |
| reserves.reserves_by_country[AU].share_pct | 6.21 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 140,000 / 2,255,000 = 6.21%. |
| reserves.reserves_by_country[AU].notes JORC-compliant reserves | 20000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 footnote 9: `"reserves were 20,000 tons"` |
| reserves.reserves_by_country[MM].quantity.value | 140000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Burma ... 140,000"` |
| reserves.reserves_by_country[MM].share_pct | 6.21 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 140,000 / 2,255,000 = 6.21%. |
| reserves.reserves_by_country[TR].quantity.value | 99000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Turkey ... 99,000"` |
| reserves.reserves_by_country[TR].share_pct | 4.39 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 99,000 / 2,255,000 = 4.39%. |
| reserves.reserves_by_country[CA].quantity.value | 78000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Canada ... 78,000"` |
| reserves.reserves_by_country[CA].share_pct | 3.46 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 78,000 / 2,255,000 = 3.46%. |
| reserves.reserves_by_country[US].quantity.value | 60000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column shows United States footnote 8 with `"60,000"`; footnote 8 identifies Stibnite probable reserves. |
| reserves.reserves_by_country[US].share_pct | 2.66 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 60,000 / 2,255,000 = 2.66%. |
| reserves.reserves_by_country[VN].quantity.value | 54000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Vietnam ... 54,000"` |
| reserves.reserves_by_country[VN].share_pct | 2.39 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 54,000 / 2,255,000 = 2.39%. |
| reserves.reserves_by_country[TJ].quantity.value | 50000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Tajikistan ... 50,000"` |
| reserves.reserves_by_country[TJ].share_pct | 2.22 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 50,000 / 2,255,000 = 2.22%. |
| reserves.reserves_by_country[PK].quantity.value | 26000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Pakistan ... 26,000"` |
| reserves.reserves_by_country[PK].share_pct | 1.15 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 26,000 / 2,255,000 = 1.15%. |
| reserves.reserves_by_country[MX].quantity.value | 18000 tonnes | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 reserves column: `"Mexico ... 18,000"` |
| reserves.reserves_by_country[MX].share_pct | 0.8 | usgs_mcs_2025_antimony | inferred | Not stated directly; computed from quantified-country subtotal 18,000 / 2,255,000 = 0.80%. |
| feedstock_origins[antimony_ore_and_concentrates].notes ore imports | 310 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Imports for consumption, Ore and concentrates 2024e: `"310"` |
| feedstock_origins[antimony_ore_and_concentrates].notes oxide imports | 20000 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Imports for consumption, Oxide 2024e: `"20,000"` |
| feedstock_origins[antimony_ore_and_concentrates].notes unwrought metal and powder imports | 4100 tonnes_per_year | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Imports for consumption, Unwrought, powder 2024e: `"4,100"` |
| feedstock_origins[spent_lead_acid_batteries].notes recycling share | 15 pct | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Domestic Production and Use: `"Recycling supplied about 15%"` |
| end_uses[metal_products].share_pct | 40 | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Domestic Production and Use: `"metal products ... 40%"` |
| end_uses[flame_retardants].share_pct | 39 | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Domestic Production and Use: `"flame retardants, 39%"` |
| end_uses[nonmetal_products].share_pct | 21 | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Domestic Production and Use: `"nonmetal products ... 21%"` |
| criticality.us_critical_list_as_of_2025 | true | usgs_2025_critical_minerals_list | verified | Federal Register public-inspection notice for `2025-19813`: `"includes the following 60 minerals: aluminum, antimony..."` |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | EUR-Lex search snippet for Regulation (EU) 2024/1252 Annex II: `"(a) antimony"` under “List of critical raw materials.” |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | verified | EUR-Lex search snippet for Annex I strategic list names items from `"bauxite/alumina/aluminium"` through `"tungsten"` and does not include antimony. |
| prices[2024].value | 9.5 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Price, metal, average 2024e: `"9.50"` dollars per pound |
| prices[2023].value | 5.49 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Price, metal, average 2023: `"5.49"` dollars per pound |
| prices[2022].value | 6.18 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Price, metal, average 2022: `"6.18"` dollars per pound |
| prices[2021].value | 5.31 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Price, metal, average 2021: `"5.31"` dollars per pound |
| prices[2020].value | 2.67 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Price, metal, average 2020: `"2.67"` dollars per pound |
| geopolitical_events[2024-02].impact DoD funding | 59.4 million usd | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 Events, Trends, and Issues: `"total Department of Defense funding to $59.4 million"` |
| geopolitical_events[2024-02].impact net import reliance | 85 pct | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Salient Statistics, Net import reliance 2024e: `"85"` |
| geopolitical_events[2024-08].impact July price | 8.91 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 Events, Trends, and Issues: `"from $8.91 per pound in July"` |
| geopolitical_events[2024-08].impact November price | 17.50 usd_per_lb | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.35 Events, Trends, and Issues: `"to $17.50 per pound in November"` |
| geopolitical_events[2024-12].impact China world mine share | 60 pct | usgs_mcs_2025_antimony | inferred | Not stated as a percentage in the event text; computed from p.35 table values China 60,000 / world 100,000 = 60%. |
| geopolitical_events[2024-12].impact China share of US metal-and-oxide imports | 63 pct | usgs_mcs_2025_antimony | verified | USGS MCS 2025 p.34 Import Sources (2020–23): `"Total metal and oxide: China ... 63%"` |

## Notes

USGS MCS 2025 antimony chapter PDF was reachable and provided direct evidence for all production, reserve, price, feedstock, end-use, and geopolitical-event figures. The key evidence is concentrated on p.34 (domestic production/use, imports, prices, import reliance) and p.35 (world mine production, reserves, events, substitutes).

All `share_pct` values in `production.mining_by_country` are inferred from the p.35 world-total figure of 100,000 metric tons. All `share_pct` values in `reserves.reserves_by_country` are inferred from the YAML’s stated subtotal basis of 2,255,000 metric tons, because the USGS world reserve figure is reported only as `>2,000,000` and several countries are `NA`.

`reserves.economic_reserves.value` is marked `inferred`, not `verified`, because the YAML models the lower bound `2,000,000` from the source’s `>2,000,000` rather than an exact published total.

The EU criticality flags were checked from a search-indexed EUR-Lex rendering of Regulation (EU) 2024/1252. Annex II explicitly includes antimony as a critical raw material, while Annex I’s strategic list does not include antimony, so `eu_crm_list_as_of_2024: true` and `eu_strategic_list_as_of_2024: false` are both supported.

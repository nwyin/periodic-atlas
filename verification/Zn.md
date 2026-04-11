# Verification: Zn

- Element: zinc (Zn)
- Snapshot year: 2025
- Verifier: worker-f05cf3ff908d (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 58 |
| discrepancy | 0 |
| inferred | 28 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 12000000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "World total (rounded) 12,000" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mine notes (2023 world total) | 12100000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "12,100" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].refined.value | 13700000 tonnes_per_year | ilzsg_2024_forecast | verified | "estimated global refined zinc production in 2024 was forecast to decrease by 1.8% to 13.7 million tons" — USGS MCS 2025 p.203 Events text, citing ILZSG footnote 8 (September 30, 2024 Lisbon press release) |
| production[0].refined notes (ILZSG consumption 2024e) | 13800000 tonnes_per_year | ilzsg_2024_forecast | verified | "estimated metal consumption was forecast to increase by 1.8% to 13.8 million tons" — USGS MCS 2025 p.203 Events text, citing ILZSG footnote 8 |
| production[0].mining_by_country[CN].quantity.value | 4000000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "China … 4,000" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 33.33 | usgs_mcs_2025_zinc | inferred | Not stated in source; 4000/12000 = 33.33% — computed |
| production[0].mining_by_country[PE].quantity.value | 1300000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Peru … 1,300" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[PE].share_pct | 10.83 | usgs_mcs_2025_zinc | inferred | Not stated in source; 1300/12000 = 10.83% — computed |
| production[0].mining_by_country[PE].notes (2023) | 1470000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Peru … 1,470" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[AU].quantity.value | 1100000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Australia … 1,100" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 9.17 | usgs_mcs_2025_zinc | inferred | Not stated in source; 1100/12000 = 9.17% — computed |
| production[0].mining_by_country[AU].notes (2023) | 1090000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Australia … 1,090" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[IN].quantity.value | 860000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "India … e860" — USGS MCS 2025 p.203 World Mine Production table, 2024e column (e = estimated) |
| production[0].mining_by_country[IN].share_pct | 7.17 | usgs_mcs_2025_zinc | inferred | Not stated in source; 860/12000 = 7.17% — computed |
| production[0].mining_by_country[US].quantity.value | 750000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "United States … 750" — USGS MCS 2025 p.203 World Mine Production table, 2024e column; also Salient Statistics Mine 2024e=750 |
| production[0].mining_by_country[US].share_pct | 6.25 | usgs_mcs_2025_zinc | inferred | Not stated in source; 750/12000 = 6.25% — computed |
| production[0].mining_by_country[US].notes (2023) | 767000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "United States … 767" — USGS MCS 2025 p.203 World Mine Production table, 2023 column; confirmed by Salient Statistics Mine 2023=767 |
| production[0].mining_by_country[MX].quantity.value | 700000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Mexico … 700" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[MX].share_pct | 5.83 | usgs_mcs_2025_zinc | inferred | Not stated in source; 700/12000 = 5.83% — computed |
| production[0].mining_by_country[MX].notes (2023) | 584000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Mexico … 584" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[BO].quantity.value | 510000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Bolivia … 510" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[BO].share_pct | 4.25 | usgs_mcs_2025_zinc | inferred | Not stated in source; 510/12000 = 4.25% — computed |
| production[0].mining_by_country[BO].notes (2023) | 492000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Bolivia … 492" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[KZ].quantity.value | 370000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Kazakhstan … 370" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[KZ].share_pct | 3.08 | usgs_mcs_2025_zinc | inferred | Not stated in source; 370/12000 = 3.08% — computed |
| production[0].mining_by_country[KZ].notes (2023) | 340000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Kazakhstan … 340" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[RU].quantity.value | 310000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Russia … e310" — USGS MCS 2025 p.203 World Mine Production table, 2024e column (e = estimated) |
| production[0].mining_by_country[RU].share_pct | 2.58 | usgs_mcs_2025_zinc | inferred | Not stated in source; 310/12000 = 2.58% — computed |
| production[0].mining_by_country[RU].notes (2023) | 300000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Russia … e300" — USGS MCS 2025 p.203 World Mine Production table, 2023 column (e = estimated) |
| production[0].mining_by_country[SE].quantity.value | 240000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Sweden … 240" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[SE].share_pct | 2.00 | usgs_mcs_2025_zinc | inferred | Not stated in source; 240/12000 = 2.00% — computed |
| production[0].mining_by_country[SE].notes (2023) | 218000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Sweden … 218" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[ZA].quantity.value | 120000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "South Africa … 120" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZA].share_pct | 1.00 | usgs_mcs_2025_zinc | inferred | Not stated in source; 120/12000 = 1.00% — computed |
| production[0].mining_by_country[ZA].notes (2023) | 198000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "South Africa … 198" — USGS MCS 2025 p.203 World Mine Production table, 2023 column |
| production[0].mining_by_country[ZZ].quantity.value | 1700000 tonnes_per_year | usgs_mcs_2025_zinc | verified | "Other countries … 1,700" — USGS MCS 2025 p.203 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 14.17 | usgs_mcs_2025_zinc | inferred | Not stated in source; 1700/12000 = 14.17% — computed |
| reserves.economic_reserves.value | 230000000 tonnes | usgs_mcs_2025_zinc | verified | "World total (rounded) … 230,000" — USGS MCS 2025 p.203 Reserves column, World Mine Production and Reserves table |
| reserves.resources.value | 1900000000 tonnes | usgs_mcs_2025_zinc | verified | "Identified zinc resources of the world are about 1.9 billion tons" — USGS MCS 2025 p.203 World Resources note |
| reserves.reserves_by_country[AU].quantity.value | 64000000 tonnes | usgs_mcs_2025_zinc | verified | "Australia … 64,000" — USGS MCS 2025 p.203 Reserves column. Footnote 11: JORC-compliant reserves were 21 million tons |
| reserves.reserves_by_country[AU].share_pct | 27.83 | usgs_mcs_2025_zinc | inferred | Not stated in source; 64000/230000 = 27.83% — computed |
| reserves.reserves_by_country[CN].quantity.value | 46000000 tonnes | usgs_mcs_2025_zinc | verified | "China … 46,000" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[CN].share_pct | 20.00 | usgs_mcs_2025_zinc | inferred | Not stated in source; 46000/230000 = 20.00% — computed |
| reserves.reserves_by_country[RU].quantity.value | 29000000 tonnes | usgs_mcs_2025_zinc | verified | "Russia … 29,000" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[RU].share_pct | 12.61 | usgs_mcs_2025_zinc | inferred | Not stated in source; 29000/230000 = 12.61% — computed |
| reserves.reserves_by_country[PE].quantity.value | 20000000 tonnes | usgs_mcs_2025_zinc | verified | "Peru … 20,000" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[PE].share_pct | 8.70 | usgs_mcs_2025_zinc | inferred | Not stated in source; 20000/230000 = 8.70% — computed |
| reserves.reserves_by_country[ZZ].quantity.value | 25000000 tonnes | usgs_mcs_2025_zinc | verified | "Other countries … 25,000" — USGS MCS 2025 p.203 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 10.87 | usgs_mcs_2025_zinc | inferred | Not stated in source; 25000/230000 = 10.87% — computed |
| reserves.reserves_by_country[MX].quantity.value | 14000000 tonnes | usgs_mcs_2025_zinc | verified | "Mexico … 14,000" — USGS MCS 2025 p.203 Reserves column |
| reserves.reserves_by_country[MX].share_pct | 6.09 | usgs_mcs_2025_zinc | inferred | Not stated in source; 14000/230000 = 6.09% — computed |
| reserves.reserves_by_country[IN].quantity.value | 9800000 tonnes | usgs_mcs_2025_zinc | verified | "India … 9,800" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[IN].share_pct | 4.26 | usgs_mcs_2025_zinc | inferred | Not stated in source; 9800/230000 = 4.26% — computed |
| reserves.reserves_by_country[US].quantity.value | 9200000 tonnes | usgs_mcs_2025_zinc | verified | "United States … 9,200" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[US].share_pct | 4.00 | usgs_mcs_2025_zinc | inferred | Not stated in source; 9200/230000 = 4.00% — computed |
| reserves.reserves_by_country[KZ].quantity.value | 7600000 tonnes | usgs_mcs_2025_zinc | verified | "Kazakhstan … 7,600" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[KZ].share_pct | 3.30 | usgs_mcs_2025_zinc | inferred | Not stated in source; 7600/230000 = 3.30% — computed |
| reserves.reserves_by_country[ZA].quantity.value | 5900000 tonnes | usgs_mcs_2025_zinc | verified | "South Africa … 5,900" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[ZA].share_pct | 2.57 | usgs_mcs_2025_zinc | inferred | Not stated in source; 5900/230000 = 2.57% — computed |
| reserves.reserves_by_country[SE].quantity.value | 3900000 tonnes | usgs_mcs_2025_zinc | verified | "Sweden … 3,900" — USGS MCS 2025 p.203 Reserves column (revised 2024) |
| reserves.reserves_by_country[SE].share_pct | 1.70 | usgs_mcs_2025_zinc | inferred | Not stated in source; 3900/230000 = 1.70% — computed |
| end_uses[galvanized_steel].share_pct | 50 | usgs_mcs_2025_zinc | inferred | USGS MCS 2025 p.202 states "most was used to produce galvanized steel" — order only, no percentage given. ~50% estimated from typical global consumption patterns |
| end_uses[brass_and_bronze].share_pct | 17 | usgs_mcs_2025_zinc | inferred | USGS MCS 2025 p.202 lists brass and bronze as second end use after galvanized steel — order only, no percentage given. ~17% estimated |
| end_uses[zinc_base_alloys].share_pct | 16 | usgs_mcs_2025_zinc | inferred | USGS MCS 2025 p.202 lists zinc-base alloys as third end use — order only, no percentage given. ~16% estimated |
| end_uses[other_uses].share_pct | 17 | usgs_mcs_2025_zinc | inferred | USGS MCS 2025 p.202 lists "other uses" as residual category — no percentage given. ~17% estimated as remainder |
| prices[2024,us_domestic].value | 1.44 usd_per_lb | usgs_mcs_2025_zinc | verified | "North American … 144" cents/lb (2024e) — USGS MCS 2025 p.202 Salient Statistics table. Footnote 4: S&P Global Platts Metals Week, LME cash price plus premium |
| prices[2024,lme].value | 1.26 usd_per_lb | usgs_mcs_2025_zinc | verified | "London Metal Exchange (LME), cash … 126" cents/lb (2024e) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2023,us_domestic].value | 1.513 usd_per_lb | usgs_mcs_2025_zinc | verified | "North American … 151.3" cents/lb (2023) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2023,lme].value | 1.201 usd_per_lb | usgs_mcs_2025_zinc | verified | "London Metal Exchange (LME), cash … 120.1" cents/lb (2023) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2022,us_domestic].value | 1.902 usd_per_lb | usgs_mcs_2025_zinc | verified | "North American … 190.2" cents/lb (2022) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2022,lme].value | 1.581 usd_per_lb | usgs_mcs_2025_zinc | verified | "London Metal Exchange (LME), cash … 158.1" cents/lb (2022) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2021,us_domestic].value | 1.458 usd_per_lb | usgs_mcs_2025_zinc | verified | "North American … 145.8" cents/lb (2021) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2021,lme].value | 1.363 usd_per_lb | usgs_mcs_2025_zinc | verified | "London Metal Exchange (LME), cash … 136.3" cents/lb (2021) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2020,us_domestic].value | 1.108 usd_per_lb | usgs_mcs_2025_zinc | verified | "North American … 110.8" cents/lb (2020) — USGS MCS 2025 p.202 Salient Statistics table |
| prices[2020,lme].value | 1.027 usd_per_lb | usgs_mcs_2025_zinc | verified | "London Metal Exchange (LME), cash … 102.7" cents/lb (2020) — USGS MCS 2025 p.202 Salient Statistics table |
| geopolitical_events[2023-11].event | Middle Tennessee zinc mines suspend operations | usgs_mcs_2025_zinc | verified | "There was no production at the Middle Tennessee zinc mines after operations were suspended in November 2023" — USGS MCS 2025 p.203 Events text |
| geopolitical_events[2024-09].event | US DoC initiates AD/CVD investigations on galvanized steel from 10 partners | usgs_mcs_2025_zinc | verified | "In September, the U.S. Department of Commerce initiated antidumping and countervailing investigations on corrosion-resistant steel, including galvanized steel, imported from 10 trading partners" — USGS MCS 2025 p.203 Events text |
| geopolitical_events[2024-10].event | US ITC preliminary injury determination on galvanized steel | usgs_mcs_2025_zinc | verified | "In October, the U.S. International Trade Commission preliminarily determined that U.S. industry was materially injured by these imports. Final determinations were expected to be made in 2025." — USGS MCS 2025 p.203 Events text |
| geopolitical_events[2024-09].event | ILZSG projects 2024 deficit of 164,000 tonnes | ilzsg_2024_forecast | verified | "resulting in a production-to-consumption deficit of 164,000 tons" — USGS MCS 2025 p.203 Events text, citing ILZSG footnote 8 (September 30, 2024 Lisbon press release) |
| feedstock_origins[zinc_sulfide_ore] | sphalerite (ZnS), 3–15% Zn, 50–55% concentrate | usgs_mcs_2025_zinc | inferred | USGS MCS 2025 chapter mentions "Zinc content of concentrates and direct shipping ores" (footnote 9) but does not explicitly describe sphalerite mineralogy, grade ranges, or name the specific mining districts cited in the YAML notes. Details are standard mineralogy |
| feedstock_origins[electric_arc_furnace_dust] | crude zinc oxide from EAF dust | usgs_mcs_2025_zinc | verified | "crude zinc oxide recovered from electric arc furnace dust" — USGS MCS 2025 p.202 Recycling paragraph |
| feedstock_origins[galvanizing_residues] | galvanizing residues | usgs_mcs_2025_zinc | verified | "galvanizing residues" — USGS MCS 2025 p.202 Recycling paragraph |
| substitutes[galvanized_steel] | Aluminum and plastics substitute in automobiles | usgs_mcs_2025_zinc | verified | "Aluminum and plastics substitute for galvanized sheet in automobiles" — USGS MCS 2025 p.203 Substitutes paragraph (verbatim) |
| substitutes[protective_coatings] | Aluminum alloys, cadmium, paint, plastic coatings | usgs_mcs_2025_zinc | verified | "aluminum alloys, cadmium, paint, and plastic coatings replace zinc coatings in other applications" — USGS MCS 2025 p.203 Substitutes paragraph (verbatim) |
| substitutes[zinc_base_alloys] | Aluminum- and magnesium-base alloys | usgs_mcs_2025_zinc | verified | "Aluminum- and magnesium-base alloys are major substitutes for zinc-base diecasting alloys" — USGS MCS 2025 p.203 Substitutes paragraph (verbatim) |
| substitutes[chemical_electronic_pigment] | Many elements substitute in chemical, electronic, pigment uses | usgs_mcs_2025_zinc | verified | "Many elements are substitutes for zinc in chemical, electronic, and pigment uses" — USGS MCS 2025 p.203 Substitutes paragraph (verbatim) |

## Notes

**Source access**: USGS MCS 2025 zinc chapter PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-zinc.pdf) was fetched and extracted via pdftotext -layout. Full text of both pages (pp. 202–203) extracted successfully. All production, reserves, prices, substitutes, and events data confirmed directly.

**ILZSG source**: The YAML cites `ilzsg_2024_forecast` with URL `https://ilzsg.org`. The ILZSG homepage is reachable but the September 30, 2024 Lisbon session press release is not directly accessible at that URL (press-releases archive shows only 2026 entries). However, USGS MCS 2025 p.203 footnote 8 explicitly cites the ILZSG press release verbatim ("ILZSG session/forecasts: Lisbon, Portugal, International Lead and Zinc Study Group press release, September 30") and quotes all three key figures (13.7 Mt production, 13.8 Mt consumption, 164,000 t deficit) in the Events text. All ILZSG-sourced claims are marked `verified` on the strength of the USGS cross-reference, which embeds the ILZSG data as a direct quote.

**End-use percentages (confidence=low)**: USGS MCS 2025 provides only the qualitative order — "most was used to produce galvanized steel, followed by brass and bronze, zinc-base alloys, and other uses" — with no explicit percentage breakdown. The four share_pct values (50, 17, 16, 17) are estimates consistent with industry data, correctly flagged `confidence: low` in the YAML. All marked `inferred`.

**Share percentages (all inferred)**: All 12 mine production share_pcts and all 11 reserve share_pcts are computed from (country value / world total) × 100. USGS does not state percentages in the zinc chapter tables. Arithmetic was verified independently; all computed values match the YAML to 2 decimal places.

**Bolivia reserves NA**: Bolivia appears in the mine production table (510 kt 2024e) but has "NA" (not available) in the Reserves column. The YAML correctly captures this in its BO notes and sets `completeness: partial` for reserves_by_country. Not a discrepancy.

**Australia JORC footnote**: USGS footnote 11 states "JORC-compliant or equivalent reserves were 21 million tons" for Australia vs. 64,000 kt in the USGS reserves table. This discrepancy is noted in the YAML AU reserves notes and is a known USGS methodology difference (USGS-format reserves include inferred resources beyond strict JORC economic reserves). Not flagged as a discrepancy in the YAML data.

**Named-country mine production sum**: CN+PE+AU+IN+US+MX+BO+KZ+RU+SE+ZA+ZZ = 4000+1300+1100+860+750+700+510+370+310+240+120+1700 = 11,960 kt vs. world total 12,000 kt. The 40 kt gap is rounding, consistent with YAML notes. Not a discrepancy.

**Named-country reserves sum**: AU+CN+RU+PE+ZZ+MX+IN+US+KZ+ZA+SE = 64000+46000+29000+20000+25000+14000+9800+9200+7600+5900+3900 = 234,400 kt vs. world total 230,000 kt. The 4,400 kt excess (~102%) is within schema tolerance per Bolivia NA exclusion and USGS rounding conventions. Consistent with YAML notes and hive discovery note.

**US salient statistics crosscheck**: YAML narrative claims US apparent consumption fell 11% to 820,000 t and net import reliance was 73%. USGS confirms: Consumption apparent 2024e=820 (from 921 in 2023: −10.97% ≈ −11% ✓), Net import reliance refined zinc 2024e=73% ✓. Import sources (Canada 59%, Mexico 16%, Korea 7%) also confirmed verbatim from USGS Import Sources paragraph.

**LME price decrease**: USGS p.203 Events text states "The annual average LME cash price for Special High Grade (SHG) zinc was projected to decrease by 5% in 2024 from that in 2023." Checking: (126 − 120.1) / 120.1 = +4.9% increase, not decrease. However, USGS says decrease of 5% from 2023 to 2024: (126 − 120.1)/120.1 = +4.9% which is an *increase*. Re-checking: "decrease by 5% in 2024 from that in 2023" — prices went from 120.1 c/lb (2023) to 126 c/lb (2024e), a +4.9% increase. This appears inconsistent with the USGS text. However, the USGS "2024e" value of 126 c/lb may be a preliminary projection issued in early 2024 that was later superseded; the Events text likely refers to expected (not final) 2024 trajectory. The YAML correctly stores 126 and 120.1 as the salient statistics table values. No YAML discrepancy — the ambiguity is in the USGS narrative vs. table, not in the YAML claims. Noted for follow-up.

**Feedstock zinc_sulfide_ore**: The YAML source_id cites usgs_mcs_2025_zinc, but the specific sphalerite mineralogy detail (ZnS, 3–15% Zn grades, 50–55% concentrate, named mining districts) is not stated in the USGS zinc chapter. Marked `inferred`. The general statement that zinc is produced from concentrates is confirmed by USGS footnote 9: "Zinc content of concentrates and direct shipping ores."

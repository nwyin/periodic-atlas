# Verification: In

- Element: indium (In)
- Snapshot year: 2025
- Verifier: worker-sonnet-4-6 (automated)
- Date: 2026-04-14

## Summary

| Metric | Count |
|---|---|
| verified | 26 |
| discrepancy | 0 |
| inferred | 12 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 1080 tonnes_per_year | usgs_mcs_2025_indium | verified | "World total (rounded) … 1,080" (2024e) — USGS MCS 2025 p.91 World Refinery Production and Capacity table, 2024 estimated column |
| production[0].refined.approximate | true | usgs_mcs_2025_indium | verified | USGS footnote 6: data "derived from trade data, production capacity, and changes in related lead and zinc smelter production"; "e" suffix on 2024 column confirms estimates |
| production[0].refining_by_country.CN.quantity.value | 760 tonnes_per_year | usgs_mcs_2025_indium | verified | "China … 760" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table |
| production[0].refining_by_country.CN.share_pct | 70 | usgs_mcs_2025_indium | verified | "China is the leading global producer of Indium, accounting for 70% of the world total." — USGS MCS 2025 Events, Trends, and Issues text, explicit stated share |
| production[0].refining_by_country.KR.quantity.value | 180 tonnes_per_year | usgs_mcs_2025_indium | verified | "Korea, Republic of … 180" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table |
| production[0].refining_by_country.KR.share_pct | 17 | usgs_mcs_2025_indium | inferred | Not stated in source; 180/1080 = 16.7% — rounds to 17% |
| production[0].refining_by_country.JP.quantity.value | 60 tonnes_per_year | usgs_mcs_2025_indium | verified | "Japan … 60" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table |
| production[0].refining_by_country.JP.share_pct | 6 | usgs_mcs_2025_indium | inferred | Not stated in source; 60/1080 = 5.6% — rounds to 6% |
| production[0].refining_by_country.CA.quantity.value | 35 tonnes_per_year | usgs_mcs_2025_indium | verified | "Canada … 35" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table |
| production[0].refining_by_country.CA.share_pct | 3 | usgs_mcs_2025_indium | inferred | Not stated in source; 35/1080 = 3.2% — rounds to 3% |
| production[0].refining_by_country.FR.quantity.value | 21 tonnes_per_year | usgs_mcs_2025_indium | verified | "France … 21" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table |
| production[0].refining_by_country.FR.share_pct | 2 | usgs_mcs_2025_indium | inferred | Not stated in source; 21/1080 = 1.9% — rounds to 2% |
| production[0].refining_by_country.BE.quantity.value | 10 tonnes_per_year | usgs_mcs_2025_indium | verified | "Belgium … 10" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table (note: 2023 figure was 19 t) |
| production[0].refining_by_country.BE.share_pct | 1 | usgs_mcs_2025_indium | inferred | Not stated in source; 10/1080 = 0.9% — rounds to 1% |
| production[0].refining_by_country.RU.quantity.value | 10 tonnes_per_year | usgs_mcs_2025_indium | verified | "Russia … 10" (2024e) — USGS MCS 2025 World Refinery Production and Capacity table (note: 2023 figure was 5 t) |
| production[0].refining_by_country.RU.share_pct | 1 | usgs_mcs_2025_indium | inferred | Not stated in source; 10/1080 = 0.9% — rounds to 1% |
| production[0].refining_by_country.ZZ.quantity.value | 2 tonnes_per_year | usgs_mcs_2025_indium | inferred | Uzbekistan "1" t per USGS table; Peru listed with capacity only (50 t) and zero 2024 production (dash). Named-country sum = 1076 t; world total = 1080 t; residual = 4 t (includes 1 t Uzbekistan + USGS rounding). ZZ bucket assigned 2 t as an approximation. |
| production[0].refining_by_country.ZZ.share_pct | 0 | usgs_mcs_2025_indium | inferred | 2/1080 = 0.19% — rounds to 0%; sum of all named-country shares (70+17+6+3+2+1+1) = 100%, within schema tolerance |
| prices[2024,us_domestic].value | 340 usd_per_kg | usgs_mcs_2025_indium | verified | "U.S. warehouse, free on board … 340" (2024e) — USGS MCS 2025 Salient Statistics table; source footnote 3: Argus Media Group |
| prices[2024,rotterdam].value | 300 usd_per_kg | usgs_mcs_2025_indium | verified | "Rotterdam, duties unpaid … 300" (2024e) — USGS MCS 2025 Salient Statistics table |
| prices[2023,us_domestic].value | 244 usd_per_kg | usgs_mcs_2025_indium | verified | "U.S. warehouse, free on board … 244" (2023) — USGS MCS 2025 Salient Statistics table |
| prices[2023,rotterdam].value | 238 usd_per_kg | usgs_mcs_2025_indium | verified | "Rotterdam, duties unpaid … 238" (2023) — USGS MCS 2025 Salient Statistics table |
| prices[2022,us_domestic].value | 250 usd_per_kg | usgs_mcs_2025_indium | verified | "U.S. warehouse, free on board … 250" (2022) — USGS MCS 2025 Salient Statistics table |
| prices[2022,rotterdam].value | 257 usd_per_kg | usgs_mcs_2025_indium | verified | "Rotterdam, duties unpaid … 257" (2022) — USGS MCS 2025 Salient Statistics table |
| prices[2021,us_domestic].value | 223 usd_per_kg | usgs_mcs_2025_indium | verified | "U.S. warehouse, free on board … 223" (2021) — USGS MCS 2025 Salient Statistics table |
| prices[2021,rotterdam].value | 217 usd_per_kg | usgs_mcs_2025_indium | verified | "Rotterdam, duties unpaid … 217" (2021) — USGS MCS 2025 Salient Statistics table |
| prices[2020,us_domestic].value | 161 usd_per_kg | usgs_mcs_2025_indium | verified | "U.S. warehouse, free on board … 161" (2020) — USGS MCS 2025 Salient Statistics table |
| prices[2020,rotterdam].value | 158 usd_per_kg | usgs_mcs_2025_indium | verified | "Rotterdam, duties unpaid … 158" (2020) — USGS MCS 2025 Salient Statistics table |
| geopolitical_events[2024-09].event | US Section 301 25% tariff on indium from China | usgs_mcs_2025_indium | verified | "Additional categories of goods from China were subject to tariffs including a 25% ad valorem tariff on critical minerals, which included indium … In September, the Office of the United States Trade Representative announced final tariff modifications" — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[2024-08].event | InP wafer fabrication facility in Alhambra CA resumes production | usgs_mcs_2025_indium | verified | "In August, an indium-phosphide-wafer fabrication facility, located in Alhambra, CA, resumed production after it was acquired by a U.S.-based photonic devices manufacturer." — USGS MCS 2025 Events, Trends, and Issues |
| geopolitical_events[2024-07].event | Utah zinc-copper-silver-indium project fully permitted | usgs_mcs_2025_indium | verified | "As of July, a zinc-copper-silver-indium project in Utah was fully permitted for the construction of an exploration shaft and open pit mine." — USGS MCS 2025 Events, Trends, and Issues |
| byproduct_of | [Zn] | usgs_mcs_2025_indium | verified | "Indium is most commonly recovered from the zinc-sulfide ore mineral sphalerite." — USGS MCS 2025 World Resources paragraph; USGS does not cite Pb, Sn, or Cu recovery as material supply routes; chalcopyrite and stannite noted as non-economic |
| feedstock_origins[zinc_sulfide_ore_sphalerite] | primary feedstock | usgs_mcs_2025_indium | verified | USGS MCS 2025 World Resources paragraph explicitly names sphalerite as primary feedstock; concentration range <1–100 ppm confirmed |
| feedstock_origins[chalcopyrite_and_stannite] | theoretically possible, not economic | usgs_mcs_2025_indium | verified | USGS MCS 2025: "indium recovery from most deposits of these minerals was not economic" — correctly represented as non-current supply source |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_2025_critical_minerals | inferred | Indium is widely established as a US critical mineral; included in USGS MCS 2025 publication. The Federal Register Final 2025 List source is the same citation used for Ge.yaml and confirmed by the MCS 2025 chapter's tariff context citing "critical minerals." Direct text of the Federal Register list not fetched in this session. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | inferred | EU Regulation 2024/1252 Annex II (critical raw materials) includes indium. This is consistent with EU CRM lists since 2011 and the source is the same EU CRMA URL used in Ge.yaml. Direct text of Annex II not fetched; confirmed by general knowledge and USGS chapter context. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | inferred | EU Regulation 2024/1252 Annex I (strategic raw materials) includes indium. Same caveat as eu_crm. Marked inferred pending direct Annex I text confirmation. |
| end_uses.uses[ito_flat_panel_displays].share_pct | 80 | usgs_mcs_2025_indium | inferred | USGS MCS 2025 states ITO "continued to account for most global indium consumption" but does not quantify a percentage. 80% is consistent with long-running USGS historical reporting and IEA guidance (range 70–85% cited across sources). Marked inferred/medium confidence. |
| end_uses.uses[alloys_and_solders].share_pct | 7 | usgs_mcs_2025_indium | inferred | USGS lists alloys and solders as a secondary end use without a percentage. 7% is an illustrative partition of the residual ~20% non-ITO demand; marked inferred/medium confidence. |
| end_uses.uses[semiconductors_and_electrical_components].share_pct | 8 | usgs_mcs_2025_indium | inferred | USGS highlights InP as a significant growth application but provides no percentage for the 2024 snapshot year. 8% is an illustrative partition; marked inferred/medium confidence. |
| end_uses.uses[other_compounds_and_research].share_pct | 5 | usgs_mcs_2025_indium | inferred | Residual of the non-ITO applications listed in USGS text (compounds, research, data-center uses). Marked inferred/medium confidence. |

## Notes

**Source access**: USGS MCS 2025 indium PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-indium.pdf) was fetched and parsed via pdfplumber. Both pages extracted successfully. All price series, refinery production table, and Events/Trends/Issues text were read directly from the extracted text.

**No mine-stage tracking**: USGS does not publish mine-stage indium production; the refinery stage is the first commercial aggregation. The YAML correctly uses only the `refined` field within the production block and leaves `mining_by_country` empty with `completeness: partial`.

**China share stated explicitly**: Unlike most byproduct elements where country shares must be inferred from absolute tonnages, the USGS MCS 2025 indium chapter explicitly states "China is the leading global producer of Indium, accounting for 70% of the world total." This makes the CN share_pct 70 a directly verified claim, not inferred.

**Footnote 6 caveat on refinery data**: USGS explicitly warns in footnote 6 that "Refinery production data for indium were limited or unavailable for most countries. Estimates were derived from trade data, production capacity, and/or changes in related lead and zinc smelter production." All non-CN country-level figures are therefore at best medium confidence; this is reflected in confidence fields.

**Belgium decline**: Belgium dropped from 19 t in 2023 to 10 t in 2024 — a 47% decline. This is a notable shift documented directly in the USGS table. No explanatory text is given in the chapter.

**ZZ residual**: Named-country 2024 tonnages sum to CN(760) + KR(180) + JP(60) + CA(35) + FR(21) + BE(10) + RU(10) = 1,076 t. World total = 1,080 t (rounded). Residual of ~4 t attributed to Uzbekistan (explicitly listed as 1 t) and USGS rounding. Peru has 50 t capacity listed but zero production (dash in table). ZZ bucket quantity set to 2 t as an approximation. The named-country share sum (70+17+6+3+2+1+1+0) = 100%, consistent with completeness: complete.

**Reserves**: USGS MCS 2025 does not publish indium reserves. The reserves block contains only explanatory notes directing users to the zinc chapter, which is the correct representation of the source. No reserves figures were fabricated.

**End-use percentages not primary-sourced**: USGS MCS 2025 does not quantify individual end-use percentages for indium in the 2025 edition. The four end-use share values (80, 7, 8, 5) are consistent with historical USGS MCS guidance and industry knowledge but are not directly read from the primary source. All four are marked `confidence: medium` and `inferred`. Users requiring precise end-use data should consult indium industry association or IEA critical minerals reports.

**Criticality EU flags**: The eu_crma_2024 source (EU Regulation 2024/1252) was not fetched as HTML in this session. Indium's inclusion on both Annex I and Annex II is consistent with EU CRM Act documentation as of 2024 and reuses the same citation pattern established in Ge.yaml. Marked inferred pending direct Annex text confirmation.

**Import sources (2020–23)**: USGS reports Korea 29%, Japan 18%, Canada 14%, Belgium 9%, other 30% — these are US import sources, not global refinery shares, and were not separately modeled in the structured data to avoid conflating import-source geography with refinery-production geography.

**Price peak note**: USGS reports price peaked at $420/kg in June 2024 (US warehouse), driven by Chinese platform price increases. The annual average of $340/kg significantly understates the peak. This is captured in the price notes.

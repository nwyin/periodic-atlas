# Verification: W

- Element: tungsten (W)
- Snapshot year: 2025
- Verifier: worker-d5e25323f414 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 34 |
| discrepancy | 0 |
| inferred | 28 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 81000 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "World total (rounded) 79,500 81,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mine.notes (2023 world mine production) | 79500 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "World total (rounded) 79,500 81,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mine.notes (US mine production 2023 and 2024) | 0 / 0 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "United States — — NA" and "Mine — — — — —" — USGS MCS 2025 pp.193-194 |
| production[0].mine.notes (US has not mined commercially since 2015) | 2015 | usgs_mcs_2025_tungsten | verified | "Tungsten has not been mined commercially in the United States since 2015." — USGS MCS 2025 p.193 Domestic Production and Use |
| production[0].mine.notes (two new Australian operations) | 2 operations | usgs_mcs_2025_tungsten | verified | "owing in part to the addition of two new operations in Australia" — USGS MCS 2025 p.194 Events, Trends, and Issues |
| production[0].mining_by_country[CN].quantity.value | 67000 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "China 66,000 67,000 2,400,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[CN].share_pct | 82.72 | usgs_mcs_2025_tungsten | inferred | Not stated; 67,000 / 81,000 = 82.72% using the published 2024 world total. |
| production[0].mining_by_country[VN].quantity.value | 3400 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Vietnam 3,500 3,400 140,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[VN].share_pct | 4.2 | usgs_mcs_2025_tungsten | inferred | Not stated; 3,400 / 81,000 = 4.20%. |
| production[0].mining_by_country[VN].notes (reserve revision year) | 2025 | usgs_mcs_2025_tungsten | verified | "Reserves for China, Portugal, and Vietnam were revised based on Government reports." — USGS MCS 2025 p.194 (2025 edition) |
| production[0].mining_by_country[RU].quantity.value | 2000 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Russia 2,000 2,000 400,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[RU].share_pct | 2.47 | usgs_mcs_2025_tungsten | inferred | Not stated; 2,000 / 81,000 = 2.47%. |
| production[0].mining_by_country[KP].quantity.value | 1700 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Korea, North 1,600 1,700 29,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[KP].share_pct | 2.1 | usgs_mcs_2025_tungsten | inferred | Not stated; 1,700 / 81,000 = 2.10%. |
| production[0].mining_by_country[BO].quantity.value | 1600 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Bolivia 1,500 1,600 NA" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[BO].share_pct | 1.98 | usgs_mcs_2025_tungsten | inferred | Not stated; 1,600 / 81,000 = 1.98%. |
| production[0].mining_by_country[ZZ].quantity.value | 1500 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Other countries 1,320 1,500 950,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[ZZ].share_pct | 1.85 | usgs_mcs_2025_tungsten | inferred | Not stated; 1,500 / 81,000 = 1.85%. |
| production[0].mining_by_country[RW].quantity.value | 1200 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Rwanda 1,200 1,200 NA" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[RW].share_pct | 1.48 | usgs_mcs_2025_tungsten | inferred | Not stated; 1,200 / 81,000 = 1.48%. |
| production[0].mining_by_country[AU].quantity.value | 1000 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Australia 430 1,000 11570,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[AU].share_pct | 1.23 | usgs_mcs_2025_tungsten | inferred | Not stated; 1,000 / 81,000 = 1.23%. |
| production[0].mining_by_country[AU].notes (2023 mine production) | 430 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Australia 430 1,000 11570,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[AT].quantity.value | 800 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Austria 850 800 10,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[AT].share_pct | 0.99 | usgs_mcs_2025_tungsten | inferred | Not stated; 800 / 81,000 = 0.99%. |
| production[0].mining_by_country[ES].quantity.value | 700 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Spain 650 700 66,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[ES].share_pct | 0.86 | usgs_mcs_2025_tungsten | inferred | Not stated; 700 / 81,000 = 0.86%. |
| production[0].mining_by_country[PT].quantity.value | 500 tonnes_per_year | usgs_mcs_2025_tungsten | verified | "Portugal 450 500 3,400" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| production[0].mining_by_country[PT].share_pct | 0.62 | usgs_mcs_2025_tungsten | inferred | Not stated; 500 / 81,000 = 0.62%. |
| production[0].mining_by_country[PT].notes (reserve revision year) | 2025 | usgs_mcs_2025_tungsten | verified | "Reserves for China, Portugal, and Vietnam were revised based on Government reports." — USGS MCS 2025 p.194 (2025 edition) |
| reserves.economic_reserves.value | 4600000 tonnes | usgs_mcs_2025_tungsten | inferred | Source states a lower bound, not a point estimate: "World total (rounded) 79,500 81,000 >4,600,000" — USGS MCS 2025 p.194 |
| reserves.economic_reserves.notes (Australia total reserves) | 570000 tonnes | usgs_mcs_2025_tungsten | inferred | The table prints "Australia 430 1,000 11570,000" and footnote 11 says "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 220,000 tons." The YAML interpretation is that the leading "11" is the footnote marker and the reserve figure is 570,000 t. |
| reserves.economic_reserves.notes (Australia JORC-compliant reserves) | 220000 tonnes | usgs_mcs_2025_tungsten | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 220,000 tons." — USGS MCS 2025 p.194 footnote 11 |
| reserves.reserves_by_country[CN].quantity.value | 2400000 tonnes | usgs_mcs_2025_tungsten | verified | "China 66,000 67,000 2,400,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[CN].share_pct | 52.17 | usgs_mcs_2025_tungsten | inferred | Not stated; 2,400,000 / 4,600,000 = 52.17% using the source's lower-bound world total, so this is an upper-bound share. |
| reserves.reserves_by_country[ZZ].quantity.value | 950000 tonnes | usgs_mcs_2025_tungsten | verified | "Other countries 1,320 1,500 950,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[ZZ].share_pct | 20.65 | usgs_mcs_2025_tungsten | inferred | Not stated; 950,000 / 4,600,000 = 20.65% using the source's lower-bound world total. |
| reserves.reserves_by_country[AU].quantity.value | 570000 tonnes | usgs_mcs_2025_tungsten | inferred | Same Australia-table interpretation as the world-reserve note: printed as "11570,000" with footnote 11; YAML reads this as 570,000 t total reserves. |
| reserves.reserves_by_country[AU].share_pct | 12.39 | usgs_mcs_2025_tungsten | inferred | Not stated; 570,000 / 4,600,000 = 12.39% using the source's lower-bound world total. |
| reserves.reserves_by_country[AU].notes (JORC-compliant reserves) | 220000 tonnes | usgs_mcs_2025_tungsten | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 220,000 tons." — USGS MCS 2025 p.194 footnote 11 |
| reserves.reserves_by_country[RU].quantity.value | 400000 tonnes | usgs_mcs_2025_tungsten | verified | "Russia 2,000 2,000 400,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[RU].share_pct | 8.7 | usgs_mcs_2025_tungsten | inferred | Not stated; 400,000 / 4,600,000 = 8.70% using the source's lower-bound world total. |
| reserves.reserves_by_country[VN].quantity.value | 140000 tonnes | usgs_mcs_2025_tungsten | verified | "Vietnam 3,500 3,400 140,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[VN].share_pct | 3.04 | usgs_mcs_2025_tungsten | inferred | Not stated; 140,000 / 4,600,000 = 3.04% using the source's lower-bound world total. |
| reserves.reserves_by_country[ES].quantity.value | 66000 tonnes | usgs_mcs_2025_tungsten | verified | "Spain 650 700 66,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[ES].share_pct | 1.43 | usgs_mcs_2025_tungsten | inferred | Not stated; 66,000 / 4,600,000 = 1.43% using the source's lower-bound world total. |
| reserves.reserves_by_country[KP].quantity.value | 29000 tonnes | usgs_mcs_2025_tungsten | verified | "Korea, North 1,600 1,700 29,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[KP].share_pct | 0.63 | usgs_mcs_2025_tungsten | inferred | Not stated; 29,000 / 4,600,000 = 0.63% using the source's lower-bound world total. |
| reserves.reserves_by_country[AT].quantity.value | 10000 tonnes | usgs_mcs_2025_tungsten | verified | "Austria 850 800 10,000" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[AT].share_pct | 0.22 | usgs_mcs_2025_tungsten | inferred | Not stated; 10,000 / 4,600,000 = 0.22% using the source's lower-bound world total. |
| reserves.reserves_by_country[PT].quantity.value | 3400 tonnes | usgs_mcs_2025_tungsten | verified | "Portugal 450 500 3,400" — USGS MCS 2025 p.194 World Mine Production and Reserves table |
| reserves.reserves_by_country[PT].share_pct | 0.07 | usgs_mcs_2025_tungsten | inferred | Not stated; 3,400 / 4,600,000 = 0.07% using the source's lower-bound world total. |
| feedstock_origins[tungsten_concentrate].notes (US companies with conversion capability) | 7 companies | usgs_mcs_2025_tungsten | verified | "There were seven U.S. companies that have the capability to convert tungsten concentrates, ammonium paratungstate (APT), tungsten oxide, and (or) scrap..." — USGS MCS 2025 p.193 |
| end_uses.uses[cemented_carbides].share_pct | 60 | usgs_mcs_2025_tungsten | verified | "An estimated 60% of the tungsten consumed in the United States was used in cemented carbide parts" — USGS MCS 2025 p.193 |
| end_uses.uses[other_alloys_electrical_and_chemical_applications].share_pct | 40 | usgs_mcs_2025_tungsten | inferred | Source says "The remainder was used..." after stating 60% for cemented carbide parts; 40% is the residual. — USGS MCS 2025 p.193 |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2022 | inferred | The 2022 Federal Register notice lists "tungsten" among the 50 critical minerals, but the cited document is dated 2022, so the "as_of_2025" timestamp is not directly stated in-source. Evidence: "includes the following 50 minerals: ... tungsten ..." — Federal Register public-inspection PDF for 2022-04027 p.1 |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_annex_2024 | verified | Official EUR-Lex search snippet for CELEX 32024R1252 lists tungsten in Annex II: "Critical Raw Materials ... 16. Tungsten". |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_annex_2024 | verified | Official EUR-Lex search snippet for CELEX 32024R1252 lists tungsten in Annex I: "Strategic Raw Materials ... 17. Tungsten". |
| prices[2024].value | 31.53 usd_per_kg | usgs_mcs_2025_tungsten | inferred | Not stated directly; USGS gives 2024 price "250" dollars per dry metric ton unit WO3 and footnote 6 states "A metric ton unit of tungsten trioxide contains 7.93 kilograms of tungsten." 250 / 7.93 = 31.53. — USGS MCS 2025 pp.193-194 |
| prices[2024].notes (raw USGS quote) | 250 dollars_per_dmtu_wo3 | usgs_mcs_2025_tungsten | verified | "Price ... 172 225 275 258 250" — USGS MCS 2025 p.193 Salient Statistics table |
| prices[2024].notes (conversion factor) | 7.93 kilograms_per_dmtu | usgs_mcs_2025_tungsten | verified | "A metric ton unit of tungsten trioxide contains 7.93 kilograms of tungsten." — USGS MCS 2025 p.194 footnote 6 |
| prices[2023].value | 32.53 usd_per_kg | usgs_mcs_2025_tungsten | inferred | Not stated directly; USGS gives 2023 price "258" dollars per dry metric ton unit WO3. 258 / 7.93 = 32.53. — USGS MCS 2025 pp.193-194 |
| prices[2023].notes (raw USGS quote) | 258 dollars_per_dmtu_wo3 | usgs_mcs_2025_tungsten | verified | "Price ... 172 225 275 258 250" — USGS MCS 2025 p.193 Salient Statistics table |
| prices[2022].value | 34.68 usd_per_kg | usgs_mcs_2025_tungsten | inferred | Not stated directly; USGS gives 2022 price "275" dollars per dry metric ton unit WO3. 275 / 7.93 = 34.68. — USGS MCS 2025 pp.193-194 |
| prices[2022].notes (raw USGS quote) | 275 dollars_per_dmtu_wo3 | usgs_mcs_2025_tungsten | verified | "Price ... 172 225 275 258 250" — USGS MCS 2025 p.193 Salient Statistics table |
| prices[2021].value | 28.37 usd_per_kg | usgs_mcs_2025_tungsten | inferred | Not stated directly; USGS gives 2021 price "225" dollars per dry metric ton unit WO3. 225 / 7.93 = 28.37. — USGS MCS 2025 pp.193-194 |
| prices[2021].notes (raw USGS quote) | 225 dollars_per_dmtu_wo3 | usgs_mcs_2025_tungsten | verified | "Price ... 172 225 275 258 250" — USGS MCS 2025 p.193 Salient Statistics table |
| prices[2020].value | 21.69 usd_per_kg | usgs_mcs_2025_tungsten | inferred | Not stated directly; USGS gives 2020 price "172" dollars per dry metric ton unit WO3. 172 / 7.93 = 21.69. — USGS MCS 2025 pp.193-194 |
| prices[2020].notes (raw USGS quote) | 172 dollars_per_dmtu_wo3 | usgs_mcs_2025_tungsten | verified | "Price ... 172 225 275 258 250" — USGS MCS 2025 p.193 Salient Statistics table |
| geopolitical_events[0].date | 2024 | usgs_mcs_2025_tungsten | verified | The statement appears in the "Events, Trends, and Issues" section for the 2024e edition and says production outside China "was estimated to have increased in 2024". — USGS MCS 2025 p.194 |
| geopolitical_events[0].event (two new Australian operations) | 2 operations | usgs_mcs_2025_tungsten | verified | "owing in part to the addition of two new operations in Australia" — USGS MCS 2025 p.194 Events, Trends, and Issues |
| geopolitical_events[1].date | 2024-12-11 | ustr_section_301_tungsten_2024 | verified | The USTR press release is dated "December 11, 2024." — USTR press release |
| geopolitical_events[1].event (tariff increase) | 25% | ustr_section_301_tungsten_2024 | verified | "the rates for certain tungsten products will increase to 25 percent." — USTR press release, December 11, 2024 |
| geopolitical_events[1].event (effective date) | 2025-01-01 | ustr_section_301_tungsten_2024 | verified | "These tariff increases will take effect on January 1, 2025." — USTR press release, December 11, 2024 |

## Notes

- The direct USGS evidence is strong for production quantities, end uses, feedstocks, substitutes, the `>50%` import-reliance context, and the raw dmtu price series.
- `prices[*].value` are conversions, not directly published USGS figures, so they are marked `inferred` even though the arithmetic is exact from the cited footnote 6 conversion factor.
- `reserves.economic_reserves.value` is a floor because the source prints `>4,600,000`; every reserve share is therefore an approximate upper bound.
- Australia's reserve figure is not cleanly typeset in the PDF (`11570,000`). The YAML interpretation of `570,000` is plausible and internally consistent with footnote 11, but it is still an inference from a malformed source rendering rather than a cleanly printed value.
- I treated the U.S. critical-mineral flag as `inferred` because the cited Federal Register document proves tungsten is on the 2022 list, but the field name says `as_of_2025`.

## ZZ-bucket decomposition (2026-04-14)

Per `atlas/zz-decomposition-plan.md`, the USGS "Other countries" residual (1,500 t / 1.85% of 2024 world production) was decomposed using BGS World Mineral Production 2019-2023 and USGS Minerals Yearbook country chapters. Three producers were named on the 2-secondary-sources rule (the 1% threshold = 810 t, which no single candidate clears).

| Country | ISO2 | 2023 t W | share_pct | Confidence | Primary source | Corroborating |
|---|---|---|---|---|---|---|
| DR Congo | CD | 400 | 0.49 | medium | `bgs_wmp_2019_2023_tungsten` (BGS 418 t) | `usgs_myb_congo_kinshasa_2022_tungsten` |
| Mongolia | MN | 300 | 0.37 | medium | `bgs_wmp_2019_2023_tungsten` (BGS 320 t) | `usgs_myb_mongolia_2022_tungsten` |
| Brazil | BR | 280 | 0.35 | medium | `bgs_wmp_2019_2023_tungsten` (BGS 284 t) | MNB Mineração Nordeste Brasil (scheelite, Rio Grande do Norte) |

**Sum of new named shares:** 980 t / 1.21%. **Remaining ZZ:** 520 t / 0.64%.

**Non-qualifying countries researched (stay in ZZ):** Malaysia (~100 t), Kyrgyzstan (~100 t, BGS estimate), Burundi (~70 t, 3TG-adjacent, declining), Mexico (~50 t), Nigeria (~50 t, rising), Thailand (~40 t, scheelite byproduct), Uganda (~30 t, artisanal, 3TG-adjacent), Myanmar (~20 t, collapsed from 220 t in 2019 due to civil war), Uzbekistan (~15 t).

**Caveats:**
- **BGS vs USGS world total divergence:** BGS 2023 reports 85,700 t vs USGS 2024e 81,000 t. The gap is dominated by Vietnam reporting basis — BGS appears to report gross concentrate mass; USGS reports contained W. **Do not blindly reconcile.**
- **Rwanda overstatement risk:** Rwanda's BGS 2023 figure (1,800 t) exceeds USGS 2024e (1,200 t) by ~50%; discrepancy is consistent with DRC→Rwanda smuggling documented by Global Witness's "ITSCI laundromat" investigation. USGS's lower figure may reflect discounting of laundered volumes.
- **ITSCI credibility** is impaired (RMI suspension 2022/2024) — affects confidence in all Rwanda/DRC/Burundi/Uganda tonnages.
- **Reporting year lag:** BGS WMP 2019-2023 reports 2023 data, so long-tail shares are on a 2023 basis while USGS-named rows are on 2024e. Within-year changes may introduce drift; noted per row.
- **Post-snapshot:** South Korea's Sangdong mine (Almonty Industries) restarted December 2025 — will appear in USGS MCS 2026+ at ~2–3% of world output.

**Methodology:** `atlas/zz-decomposition-plan.md`.


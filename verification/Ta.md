# Verification: Ta

- Element: tantalum (Ta)
- Snapshot year: 2025
- Verifier: worker-28b43b10c26e (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 36 |
| discrepancy | 0 |
| inferred | 18 |
| source_unreachable | 3 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 2100 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "World total (rounded) 2,040 2,100 NA" — USGS MCS 2025 tantalum table, 2024e mine-production column, p.177 |
| production[0].mine.notes (2023 world total) | 2040 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "World total (rounded) 2,040 2,100 NA" — USGS MCS 2025 tantalum table, 2023 mine-production column, p.177 |
| production[0].mine.notes (no U.S. mine production since 1959) | since 1959 | usgs_mcs_2025_tantalum | verified | "Tantalum has not been mined in the United States since 1959." — USGS MCS 2025 p.176 Domestic Production and Use |
| production[0].mine.notes (U.S. apparent consumption) | 770 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Consumption, apparent ... 770" — USGS MCS 2025 Salient Statistics 2024e column, p.176 |
| production[0].mine.notes (net import reliance) | 100% | usgs_mcs_2025_tantalum | verified | "Net import reliance ... 100 100 100 100 100" — USGS MCS 2025 Salient Statistics, 2024e column, p.176 |
| production[0].mining_by_country.shares[AU].quantity.value | 52 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Australia 44 52 10110,000" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[AU].share_pct | 2.48% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 52 / 2,100 = 2.48%. |
| production[0].mining_by_country.shares[BO].quantity.value | 2 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Bolivia 1 2 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[BO].share_pct | 0.10% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 2 / 2,100 = 0.10%. |
| production[0].mining_by_country.shares[BR].quantity.value | 210 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Brazil 138 210 40,000" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[BR].share_pct | 10.0% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 210 / 2,100 = 10.00%. |
| production[0].mining_by_country.shares[BI].quantity.value | 2 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Burundi e1 2 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[BI].share_pct | 0.10% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 2 / 2,100 = 0.10%. |
| production[0].mining_by_country.shares[CN].quantity.value | 76 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "China e78 76 240,000" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[CN].share_pct | 3.62% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 76 / 2,100 = 3.62%. |
| production[0].mining_by_country.shares[CD].quantity.value | 880 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Congo (Kinshasa) e920 880 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[CD].share_pct | 41.90% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 880 / 2,100 = 41.90%. |
| production[0].mining_by_country.shares[ET].quantity.value | 40 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Ethiopia e40 40 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[ET].share_pct | 1.90% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 40 / 2,100 = 1.90%. |
| production[0].mining_by_country.shares[MZ].quantity.value | 55 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Mozambique 51 55 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[MZ].share_pct | 2.62% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 55 / 2,100 = 2.62%. |
| production[0].mining_by_country.shares[NG].quantity.value | 390 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Nigeria e390 390 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[NG].share_pct | 18.57% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 390 / 2,100 = 18.57%. |
| production[0].mining_by_country.shares[RU].quantity.value | 29 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Russia e23 29 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[RU].share_pct | 1.38% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 29 / 2,100 = 1.38%. |
| production[0].mining_by_country.shares[RW].quantity.value | 350 tonnes_per_year | usgs_mcs_2025_tantalum | verified | "Rwanda e350 350 NA" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| production[0].mining_by_country.shares[RW].share_pct | 16.67% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from USGS table as 350 / 2,100 = 16.67%. |
| production[0].notes (named-country sum) | 2086 tonnes_per_year | usgs_mcs_2025_tantalum | inferred | Not stated directly; sum of the 11 USGS 2024e country rows listed above is 2,086 t. |
| production[0].notes (named-country share of world total) | 99.33% | usgs_mcs_2025_tantalum | inferred | Not stated directly; computed from the same USGS rows as 2,086 / 2,100 = 99.33%. |
| reserves.notes (world economic reserves) | NA | usgs_mcs_2025_tantalum | verified | "World total (rounded) 2,040 2,100 NA" — USGS MCS 2025 World Mine Production and Reserves table, reserves column, p.177 |
| reserves.reserves_by_country.shares[CN].quantity.value | 240000 tonnes | usgs_mcs_2025_tantalum | verified | "China e78 76 240,000" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| reserves.reserves_by_country.shares[CN].share_pct | 61.54% | usgs_mcs_2025_tantalum | inferred | Not stated directly; YAML notes define the denominator as the reported-country subtotal, and 240,000 / 390,000 = 61.54%. |
| reserves.reserves_by_country.shares[AU].quantity.value | 110000 tonnes | usgs_mcs_2025_tantalum | verified | "Australia 44 52 10110,000" with footnote 10 — USGS MCS 2025 table, p.177. The PDF line merges the footnote marker into the reserve value; YAML's 110,000 t matches the table plus footnote context. |
| reserves.reserves_by_country.shares[AU].notes (JORC/equivalent reserves) | 28000 tonnes | usgs_mcs_2025_tantalum | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 28,000 tons." — USGS MCS 2025 footnote 10, p.177 |
| reserves.reserves_by_country.shares[AU].share_pct | 28.21% | usgs_mcs_2025_tantalum | inferred | Not stated directly; YAML notes define the denominator as the reported-country subtotal, and 110,000 / 390,000 = 28.21%. |
| reserves.reserves_by_country.shares[BR].quantity.value | 40000 tonnes | usgs_mcs_2025_tantalum | verified | "Brazil 138 210 40,000" — USGS MCS 2025 World Mine Production and Reserves table, p.177 |
| reserves.reserves_by_country.shares[BR].share_pct | 10.26% | usgs_mcs_2025_tantalum | inferred | Not stated directly; YAML notes define the denominator as the reported-country subtotal, and 40,000 / 390,000 = 10.26%. |
| reserves.notes (reported-country reserve subtotal) | 390000 tonnes | usgs_mcs_2025_tantalum | inferred | Not stated directly; subtotal of reported reserve rows is 240,000 + 110,000 + 40,000 = 390,000 t. |
| reserves.notes (U.S. identified resources) | 55000 tonnes | usgs_mcs_2025_tantalum | verified | "The United States has about 55,000 tons of tantalum resources in identified deposits" — USGS MCS 2025 World Resources, p.177 |
| end_uses.uses[electronic_capacitors].share_pct | 60% | usgs_pp_1802m_niobium_tantalum | verified | Search snippet for USGS PP 1802-M states: "Approximately 60 percent of global tantalum consumption is in the electronics industry." This matches the YAML's 60% electronics bucket. |
| end_uses.uses[other_industrial_uses].share_pct | 40% | usgs_pp_1802m_niobium_tantalum | inferred | Not stated directly; residual share computed from the same USGS statement as 100% - 60% = 40%. |
| prices[2024].value | 170 usd_per_kg | usgs_mcs_2025_tantalum | verified | "Price, tantalite ... 158 158 196 170 170" — USGS MCS 2025 Salient Statistics table, 2024e column, p.176 |
| prices[2023].value | 170 usd_per_kg | usgs_mcs_2025_tantalum | verified | "Price, tantalite ... 158 158 196 170 170" — USGS MCS 2025 Salient Statistics table, 2023 column, p.176 |
| prices[2022].value | 196 usd_per_kg | usgs_mcs_2025_tantalum | verified | "Price, tantalite ... 158 158 196 170 170" — USGS MCS 2025 Salient Statistics table, 2022 column, p.176 |
| prices[2021].value | 158 usd_per_kg | usgs_mcs_2025_tantalum | verified | "Price, tantalite ... 158 158 196 170 170" — USGS MCS 2025 Salient Statistics table, 2021 column, p.176 |
| prices[2020].value | 158 usd_per_kg | usgs_mcs_2025_tantalum | verified | "Price, tantalite ... 158 158 196 170 170" — USGS MCS 2025 Salient Statistics table, 2020 column, p.176 |
| geopolitical_events[0].date | 2024-10 | usgs_mcs_2025_tantalum | verified | "as of October 2024" — USGS MCS 2025 CHIPS and Science Act paragraph, p.177 |
| geopolitical_events[0].impact (preliminary agreements) | 20 companies | usgs_mcs_2025_tantalum | verified | "preliminary agreements with 20 companies" — USGS MCS 2025 p.177 |
| geopolitical_events[0].impact (semiconductor projects) | 32 projects | usgs_mcs_2025_tantalum | verified | "for 32 semiconductor manufacturing projects" — USGS MCS 2025 p.177 |
| geopolitical_events[0].impact (States) | 20 States | usgs_mcs_2025_tantalum | verified | "in 20 States" — USGS MCS 2025 p.177 |
| geopolitical_events[0].impact (direct funding) | almost $34 billion | usgs_mcs_2025_tantalum | verified | "almost $34 billion ... in direct funding" — USGS MCS 2025 p.177 |
| geopolitical_events[0].impact (loans) | almost $29 billion | usgs_mcs_2025_tantalum | verified | "almost $29 billion in loans" — USGS MCS 2025 p.177 |
| geopolitical_events[1].date | 2024-09 | usgs_mcs_2025_tantalum | verified | "In September, the Office of the United States Trade Representative announced" — USGS MCS 2025 p.177 |
| geopolitical_events[1].impact (additional tariff) | 25% ad valorem | usgs_mcs_2025_tantalum | verified | "including a 25% ad valorem tariff on critical minerals, which included tantalum" — USGS MCS 2025 p.177 |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_critical_minerals_2022 | source_unreachable | The cited Federal Register URL could not be opened directly in the web tool during this pass. Secondary search snippets indicate the 2022 list includes tantalum among the 50 minerals, but the cited source page itself was not retrievable, so this row remains source_unreachable. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | source_unreachable | The cited EUR-Lex URL was blocked by a JavaScript / robot-check page in the web tool. The search snippet confirms Regulation (EU) 2024/1252 is the CRM Act, but the annex text listing tantalum was not directly accessible from the cited source URL. |
| criticality.eu_strategic_list_as_of_2024 | false | eu_crma_2024 | source_unreachable | Same EUR-Lex access issue as the prior row. Because Annex I text was not directly retrievable from the cited URL, the negative claim that tantalum is not strategic remains source_unreachable rather than inferred from an inaccessible list. |

## Notes

No numeric discrepancies were found in the USGS MCS 2025 tantalum production, reserve, price, or event figures. All explicit table values matched the YAML. The mine-country shares, reserve-country shares, the 2,086 t named-country subtotal, the 99.33% production subtotal share, the 390,000 t reserve subtotal, and the 40% non-electronics end-use bucket are all calculations derived from explicit source values rather than figures printed in the cited documents, so they are marked `inferred`.

`usgs_pp_1802m_niobium_tantalum` was directly accessible as a USGS publication page, but not as the underlying PDF text. The accessible USGS page confirms that electronic capacitors are the leading tantalum use, and web search snippets tied to the same USGS publication supply the explicit "approximately 60 percent" wording used for the end-use split.

The scoped `feedstock_origins` and `substitutes` entries all carry source IDs, but they are qualitative in `Ta.yaml` and do not add distinct numeric claims. They were reviewed against the accessible source text and did not require Claims-table rows to satisfy the numeric-claim invariant.

## ZZ-bucket decomposition (2026-04-14) — not applied

Per `atlas/zz-decomposition-plan.md`, the USGS "Other countries" residual was reviewed. **The Ta ZZ bucket is only 14 t / 0.67%** of the 2,100 t 2024 world total — USGS already names 11 producers down to Bolivia and Burundi at 2 t each (0.1%). No new country clears the 1%-or-two-sources threshold. **No YAML decomposition was applied.** This verification note documents the review.

**Candidates researched, all non-qualifying:**
- **Canada** (Tanco): Sinomine-owned since 2019; primarily Li/Cs with sporadic Ta output well below 21-t threshold.
- **Egypt** (Abu Dabbab, Nuweibi): development-stage projects, no 2024 commercial production.
- **Malaysia, Thailand**: downstream processors / import hubs for US, not mine producers.
- **Kazakhstan** (Ulba Metallurgical): processes imported feedstock, no primary mine production.
- **Uganda, Madagascar, Namibia, Zimbabwe, DPRK**: historical ASM/small-mine presence but none surface above 1% in authoritative 2023–2024 sources.

**Analytical findings flagged for follow-up (separate pass):**
1. **USGS year-over-year revisions are large for ASM-dominated rows.** Rwanda 2023e published as 520 t in MCS 2024 then revised down to 350 t in MCS 2025. Burundi: MCS 2024 printed 36 t for 2023 but MCS 2025 shows 2 t for 2024. These revisions exceed the 1% threshold, so 1–2% rows are vintage-sensitive. Consider a narrative caveat.
2. **Rubaya under M23 control from early 2024.** Rubaya is estimated to produce ~15% of world coltan on its own; analytically significant for the CD row and its interaction with smuggling flows. Argus Media and UN Group of Experts (S/2024/969) document the shift. Not in current Ta.yaml geopolitical_events.
3. **DRC↔Rwanda attribution uncertainty.** UN GoE (S/2024/969) and Global Witness document ~120 t/month of coltan smuggled Masisi→Rwanda from May–Oct 2024. This flow is already inside the aggregated USGS CD+RW figure but its attribution between the two countries is unstable year-over-year. The interesting decomposition is **formal-vs-informal within DRC/Rwanda, not new countries** — same architectural problem as the deferred cobalt case.
4. **ITSCI unit-basis confusion.** ITSCI Annex 1 (Feb 2025) documents only +12% YoY Rwanda tantalum concentrate exports (2,297 t *concentrate*, not Ta content) — explicitly flags confusion with USGS Ta-content tonnages. Any narrative using Rwanda export figures needs unit-basis discipline.
5. **Kenticha (Ethiopia) operational status contested** — license surrender notice May 2024 (The Reporter Ethiopia). USGS still attributes 40 t to Ethiopia for 2024e.

**Conclusion:** No data change warranted in this pass. `Ta.yaml` mining_by_country shares stand as published. Recommended follow-up: add 2–3 `geopolitical_events` entries covering Rubaya / M23 / ITSCI and a narrative sentence on inter-MCS-vintage revision risk for 1–2% producers.

**Methodology:** `atlas/zz-decomposition-plan.md`.


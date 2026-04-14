# Verification: Li

- Element: lithium (Li)
- Snapshot year: 2025
- Verifier: worker-5570a6017bc2 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 44 |
| discrepancy | 0 |
| inferred | 9 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 240000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "worldwide lithium production in 2024 increased by 18% to approximately 240,000 tons" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| production[0].mine.notes (2023 production) | 204000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "approximately 240,000 tons from 204,000 tons in 2023" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| production[0].mine.notes (increase) | 18% | usgs_mcs_2025_lithium | verified | "increased by 18% to approximately 240,000 tons" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| production[0].mine.notes (U.S. excluded) | Excludes withheld U.S. production | usgs_mcs_2025_lithium | verified | "Excludes U.S. production." — USGS MCS 2025 lithium, footnote 7 to World Mine Production table |
| production[0].mining_by_country[AU].quantity.value | 88000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Australia 91,700 88,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 36.7 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 88,000 / 240,000 = 36.7% using "\"Australia 91,700 88,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[CL].quantity.value | 49000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Chile 41,400 49,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[CL].share_pct | 20.4 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 49,000 / 240,000 = 20.4% using "\"Chile 41,400 49,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[CN].quantity.value | 41000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"China e35,700 41,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 17.1 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 41,000 / 240,000 = 17.1% using "\"China e35,700 41,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[ZW].quantity.value | 22000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Zimbabwe e14,900 22,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[ZW].share_pct | 9.2 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 22,000 / 240,000 = 9.2% using "\"Zimbabwe e14,900 22,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[AR].quantity.value | 18000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Argentina 8,630 18,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[AR].share_pct | 7.5 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 18,000 / 240,000 = 7.5% using "\"Argentina 8,630 18,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[AR].notes (2023 production) | 8630 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Argentina 8,630 18,000\"" — USGS MCS 2025 lithium, World Mine Production table |
| production[0].mining_by_country[BR].quantity.value | 10000 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Brazil e5,260 10,000\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 4.2 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 10,000 / 240,000 = 4.2% using "\"Brazil e5,260 10,000\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[CA].quantity.value | 4300 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Canada e3,240 4,300\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 1.8 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 4,300 / 240,000 = 1.79...% ≈ 1.8% using "\"Canada e3,240 4,300\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[NA].quantity.value | 2700 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Namibia e2,700 2,700\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[NA].share_pct | 1.1 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 2,700 / 240,000 = 1.125% ≈ 1.1% using "\"Namibia e2,700 2,700\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| production[0].mining_by_country[PT].quantity.value | 380 tonnes_per_year | usgs_mcs_2025_lithium | verified | "\"Portugal e380 380\"" — USGS MCS 2025 lithium, World Mine Production table, 2024e column |
| production[0].mining_by_country[PT].share_pct | 0.2 | usgs_mcs_2025_lithium | inferred | Not stated explicitly; inferred from the table values 380 / 240,000 = 0.158...% ≈ 0.2% using "\"Portugal e380 380\"" and "\"World total (rounded) 7204,000 7240,000\"" in the USGS World Mine Production table. |
| reserves.economic_reserves.value | 30000000 tonnes | usgs_mcs_2025_lithium | verified | "\"World total (rounded) 7204,000 7240,000 30,000,000\"" — USGS MCS 2025 lithium, World Mine Production and Reserves table |
| reserves.resources.value | 115000000 tonnes | usgs_mcs_2025_lithium | verified | "\"measured and indicated lithium resources have increased substantially worldwide and total about 115 million tons\"" — USGS MCS 2025 lithium, World Resources |
| reserves.resources.notes (United States) | 19000000 tonnes | usgs_mcs_2025_lithium | verified | "\"Measured and indicated lithium resources in the United States ... are 19 million tons.\"" — USGS MCS 2025 lithium, World Resources |
| reserves.resources.notes (other countries) | 96000000 tonnes | usgs_mcs_2025_lithium | verified | "\"Measured and indicated lithium resources in other countries have been revised to 96 million tons.\"" — USGS MCS 2025 lithium, World Resources |
| end_uses.uses[batteries].share_pct | 87 | usgs_mcs_2025_lithium | verified | "\"batteries, 87%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[ceramics_and_glass].share_pct | 5 | usgs_mcs_2025_lithium | verified | "\"ceramics and glass, 5%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[lubricating_greases].share_pct | 2 | usgs_mcs_2025_lithium | verified | "\"lubricating greases, 2%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[air_treatment].share_pct | 1 | usgs_mcs_2025_lithium | verified | "\"air treatment, 1%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[continuous_casting_mold_flux_powders].share_pct | 1 | usgs_mcs_2025_lithium | verified | "\"continuous casting mold flux powders, 1%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[medical].share_pct | 1 | usgs_mcs_2025_lithium | verified | "\"medical, 1%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| end_uses.uses[other].share_pct | 3 | usgs_mcs_2025_lithium | verified | "\"other uses, 3%\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| criticality.us_critical_list_as_of_2025 | true | usgs_critical_minerals_list_2025 | verified | "\"includes the following 60 minerals: aluminum, antimony, arsenic, ... lead, lithium, ... zirconium.\"" — Federal Register, Final 2025 List of Critical Minerals |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | verified | "\"ANNEX II ... The following raw materials shall be considered critical: ... (s) lithium\"" — Regulation (EU) 2024/1252, Annex II, Section 1 |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | verified | "\"ANNEX I ... The following raw materials shall be considered strategic: ... (h) lithium — battery grade\"" — Regulation (EU) 2024/1252, Annex I, Section 1 |
| prices[year=2024].value | 14000 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"10,100 14,200 71,100 41,300 14,000\"" — USGS MCS 2025 lithium, Salient Statistics price row, 2024e column |
| prices[year=2023].value | 41300 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"10,100 14,200 71,100 41,300 14,000\"" — USGS MCS 2025 lithium, Salient Statistics price row, 2023 column |
| prices[year=2022].value | 71100 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"10,100 14,200 71,100 41,300 14,000\"" — USGS MCS 2025 lithium, Salient Statistics price row, 2022 column |
| prices[year=2021].value | 14200 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"10,100 14,200 71,100 41,300 14,000\"" — USGS MCS 2025 lithium, Salient Statistics price row, 2021 column |
| prices[year=2020].value | 10100 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"10,100 14,200 71,100 41,300 14,000\"" — USGS MCS 2025 lithium, Salient Statistics price row, 2020 column |
| geopolitical_events[0].date | 2024 | usgs_mcs_2025_lithium | verified | "\"during the first half of 2024 caused the price for lithium to decrease considerably throughout the year\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (China spot carbonate, January) | 14500 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"Spot lithium carbonate prices in China ... decreased from approximately $14,500 per ton in January\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (China spot carbonate, November) | 9400 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"to approximately $9,400 per ton in November\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (China spot hydroxide, January) | 17000 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"Spot lithium hydroxide prices in China ... decreased from approximately $17,000 per ton in January\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (China spot hydroxide, November) | 9900 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"to approximately $9,900 per ton in November\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (Australia spodumene, January) | 1250 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"Spodumene (6% lithium oxide) prices in Australia ... decreased from approximately $1,250 per ton in January\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[0].impact (Australia spodumene, November) | 730 usd_per_tonne | usgs_mcs_2025_lithium | verified | "\"to approximately $730 per ton in November\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[1].date | 2024 | usgs_mcs_2025_lithium | verified | "\"Owing to lower lithium prices in 2024, commercial production from the brine-sourced waste tailings of a Utah-based magnesium producer was idled.\"" — USGS MCS 2025 lithium, Domestic Production and Use |
| geopolitical_events[2].date | 2024 | usgs_mcs_2025_lithium | verified | "\"In 2024, the U.S. Department of Energy announced $3 billion in funding across 25 projects\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[2].event (funding) | $3 billion | usgs_mcs_2025_lithium | verified | "\"announced $3 billion in funding across 25 projects\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |
| geopolitical_events[2].event (project count) | 25 projects | usgs_mcs_2025_lithium | verified | "\"announced $3 billion in funding across 25 projects\"" — USGS MCS 2025 lithium, Events, Trends, and Issues |

## Notes

All numeric lithium claims with a `source_id` in `elements/Li.yaml` were checked against the cited primary sources. No discrepancies were found.

The nine country `share_pct` values are `inferred` rather than `verified` because the USGS chapter lists country tonnages and the world total, but not percentage shares. The YAML percentages are arithmetic derivations from those table values.

`feedstock_origins` and `substitutes` both cite `usgs_mcs_2025_lithium`, but those sections contain qualitative statements only and no distinct numeric claims to tabulate. `reserves_by_country` is absent in the YAML, so there were no country-reserve-share claims to verify in this pass.

## ZZ-bucket decomposition (2026-04-14)

Per `atlas/zz-decomposition-plan.md`, the USGS residual (implicit ~4,520 t / ~1.9% of 2024 world output; the original YAML used `completeness: top_producers_only` without an explicit ZZ row) was decomposed. Only one producer cleared the threshold: the United States, whose output USGS explicitly withheld (W-code in the country table).

| Country | ISO2 | 2024e t Li | share_pct | Confidence | Primary source | Corroborating |
|---|---|---|---|---|---|---|
| United States | US | 3,500 | 1.5 | medium | `nevada_independent_silver_peak_2024` (Nevada Division of Minerals data) | `albemarle_silver_peak_10k_2024` (SEC Exhibit 96.4, Albemarle FY2024 10-K) |

**Reconstruction:** Nevada state filings report Silver Peak (Albemarle) at ~3,200 t Li for 2024, down from ~4,500 t in 2023 on price weakness. The Utah lithium-bearing tailings stream was idled in 2024. Central estimate 3,500 t; range 1,000–4,500 t. Confidence medium given wide reconstruction range and USGS's own withholding.

**Share list transition:** completeness changed from `top_producers_only` to `complete` after adding US + explicit ZZ residual (~1,000 t / 0.4%). Share totals: 98.2% (pre) + 1.5% (US) + 0.4% (explicit ZZ) = 100.1%.

**Non-qualifying candidates researched (stay in ZZ):**
- **Mali (ML):** Goulamina (Ganfeng) first production 15 Dec 2024; first shipment June 2025 — 2024 Li contribution effectively zero. Material for 2025+ data.
- **Nigeria (NG):** ASM DSO flows to Chinese processors, ~15–20 kt LCE/month across African ASM per CRU Group 2024 (~2.8–3.8 kt Li/month aggregate). Not country-decomposed by USGS; partially hidden inside Zimbabwe (22,000 t) and Chinese feed imports. Confidence too low to attribute standalone tonnage in 2024.
- **Bolivia (BO):** ~400 t Li from YLB Llipi pilot plant — below threshold and sparsely sourced.
- **Mexico (MX), Ghana (GH), Czech Republic (CZ), Ethiopia (ET), Mozambique (MZ), Malawi (MW), Burundi (BI), Tanzania (TZ):** All pre-production or dormant in 2024.

**Caveats:**
- USGS narrative attributes the residual to "additional smaller operations in Australia, Brazil, China, Namibia, Portugal, and the United States" — countries already named at their primary figures. The explicit ZZ row therefore represents sub-operational increments within named countries, not distinct unnamed producers.
- Schema: Li.yaml has a single `production` block (not stream-split). USGS also does not split its country table by brine / spodumene / lepidolite — that distinction lives in narrative only. Decomposition was applied at the single-block level.
- **Market shift context:** 2024 saw the sharp transition from scarcity to glut (China spot carbonate $14,500 → $9,400/t; spodumene $1,250 → $730/t). Numerous curtailments and expansion delays occurred; reconstruction figures reflect that environment.
- **Out-of-scope but flagged:** Sinomine's partial idling of Bikita petalite (Zimbabwe, Oct 2024) is already captured in Zimbabwe's 22,000 t USGS-named figure. Mali Goulamina is a 2025 decomposition candidate.

**Methodology:** `atlas/zz-decomposition-plan.md`.


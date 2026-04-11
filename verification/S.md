# Verification: S

- Element: sulfur (S)
- Snapshot year: 2025
- Verifier: worker-b50bfd0b9410 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 47 |
| discrepancy | 0 |
| inferred | 21 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 85.0 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "World total (rounded) … 85,000" — USGS MCS 2025 p.173 World Production table, 2024e column (1,000 kt = 1 Mt) |
| production[0].mine.notes (2023 world total) | 85.8 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "85,800" — USGS MCS 2025 p.173 World Production table, 2023 column |
| production[0].mining_by_country[CN].quantity.value | 19.0 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "China … 19,000" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 22.4 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 19,000/85,000 = 22.35% — rounds to 22.4% |
| production[0].mining_by_country[US].quantity.value | 8.2 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "United States … 8,200" — USGS MCS 2025 p.173 World Production table, 2024e column; also Salient Statistics Total (rounded) 2024e = 8,200 |
| production[0].mining_by_country[US].share_pct | 9.6 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 8,200/85,000 = 9.65% — rounds to 9.6% |
| production[0].mining_by_country[US].notes (52% from LA/TX) | 52% | usgs_mcs_2025_sulfur | verified | "Louisiana and Texas accounted for about 52% of domestic production" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (81 elemental plants) | 81 | usgs_mcs_2025_sulfur | verified | "by 31 companies at 81 plants in 25 States" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (31 companies) | 31 | usgs_mcs_2025_sulfur | verified | "by 31 companies at 81 plants in 25 States" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (25 States, elemental plants) | 25 | usgs_mcs_2025_sulfur | verified | "by 31 companies at 81 plants in 25 States" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (~8% byproduct sulfuric acid) | ~8% | usgs_mcs_2025_sulfur | verified | "representing about 8% of production of sulfur in all forms" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (5 nonferrous smelters) | 5 | usgs_mcs_2025_sulfur | verified | "five nonferrous-metal smelters in four States by four companies" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (4 States, smelters) | 4 | usgs_mcs_2025_sulfur | verified | "five nonferrous-metal smelters in four States by four companies" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[US].notes (4 companies, smelters) | 4 | usgs_mcs_2025_sulfur | verified | "five nonferrous-metal smelters in four States by four companies" — USGS MCS 2025 p.172 Domestic Production and Use |
| production[0].mining_by_country[RU].quantity.value | 7.5 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Russia … 7,500" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 8.8 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 7,500/85,000 = 8.82% — rounds to 8.8% |
| production[0].mining_by_country[SA].quantity.value | 7.5 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Saudi Arabia … 7,500" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[SA].share_pct | 8.8 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 7,500/85,000 = 8.82% — rounds to 8.8% |
| production[0].mining_by_country[AE].quantity.value | 6.0 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "United Arab Emirates … 6,000" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[AE].share_pct | 7.1 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 6,000/85,000 = 7.06% — rounds to 7.1% |
| production[0].mining_by_country[KZ].quantity.value | 5.1 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Kazakhstan … 5,100" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[KZ].share_pct | 6.0 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 5,100/85,000 = 6.00% exactly |
| production[0].mining_by_country[CA].quantity.value | 5.0 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Canada … 5,000" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[CA].share_pct | 5.9 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 5,000/85,000 = 5.88% — rounds to 5.9% |
| production[0].mining_by_country[CA].notes (Canada 79% of US elemental imports) | 79% | usgs_mcs_2025_sulfur | verified | "Elemental: Canada, 79%" — USGS MCS 2025 p.172 Import Sources (2020–23) |
| production[0].mining_by_country[IN].quantity.value | 3.7 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "India … 3,700" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 4.4 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 3,700/85,000 = 4.35% — rounds to 4.4% |
| production[0].mining_by_country[JP].quantity.value | 3.1 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Japan … 3,100" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[JP].share_pct | 3.6 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 3,100/85,000 = 3.65% — rounds to 3.6% |
| production[0].mining_by_country[KR].quantity.value | 3.1 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Korea, Republic of … 3,100" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[KR].share_pct | 3.6 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 3,100/85,000 = 3.65% — rounds to 3.6% |
| production[0].mining_by_country[QA].quantity.value | 3.1 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Qatar … 3,100" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[QA].share_pct | 3.6 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 3,100/85,000 = 3.65% — rounds to 3.6% |
| production[0].mining_by_country[IR].quantity.value | 2.0 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Iran … 2,000" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[IR].share_pct | 2.4 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 2,000/85,000 = 2.35% — rounds to 2.4% |
| production[0].mining_by_country[CL].quantity.value | 1.3 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Chile … 1,300" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[CL].share_pct | 1.5 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 1,300/85,000 = 1.53% — rounds to 1.5% |
| production[0].mining_by_country[KW].quantity.value | 1.3 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Kuwait … 1,300" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[KW].share_pct | 1.5 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 1,300/85,000 = 1.53% — rounds to 1.5% |
| production[0].mining_by_country[PL].quantity.value | 1.1 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Poland … 1,100" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[PL].share_pct | 1.3 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 1,100/85,000 = 1.29% — rounds to 1.3% |
| production[0].mining_by_country[AU].quantity.value | 0.9 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Australia … 900" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 1.1 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 900/85,000 = 1.06% — rounds to 1.1% |
| production[0].mining_by_country[TM].quantity.value | 0.9 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Turkmenistan … 900" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[TM].share_pct | 1.1 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 900/85,000 = 1.06% — rounds to 1.1% |
| production[0].mining_by_country[ZZ].quantity.value | 6.4 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "Other countries … 6,400" — USGS MCS 2025 p.173 World Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 7.5 | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; 6,400/85,000 = 7.53% — rounds to 7.5% |
| reserves.resources.value | 5,000,000,000 tonnes | usgs_mcs_2025_sulfur | verified | "Resources of elemental sulfur … total about 5 billion tons" — USGS MCS 2025 p.173 World Resources section |
| prices[2024].value | 50.00 usd_per_tonne | usgs_mcs_2025_sulfur | verified | "50.00" — USGS MCS 2025 p.172 Salient Statistics, Price average unit value 2024e row |
| prices[2023].value | 58.90 usd_per_tonne | usgs_mcs_2025_sulfur | verified | "58.90" — USGS MCS 2025 p.172 Salient Statistics, Price average unit value 2023 row |
| prices[2022].value | 177.80 usd_per_tonne | usgs_mcs_2025_sulfur | verified | "177.8" — USGS MCS 2025 p.172 Salient Statistics, Price average unit value 2022 row (YAML records as 177.80 = same value) |
| prices[2021].value | 90.40 usd_per_tonne | usgs_mcs_2025_sulfur | verified | "90.40" — USGS MCS 2025 p.172 Salient Statistics, Price average unit value 2021 row |
| prices[2020].value | 24.90 usd_per_tonne | usgs_mcs_2025_sulfur | verified | "24.90" — USGS MCS 2025 p.172 Salient Statistics, Price average unit value 2020 row |
| end_uses.uses[sulfuric_acid_production].share_pct | 90 | usgs_mcs_2025_sulfur | verified | "About 90% of sulfur consumed was in the form of sulfuric acid" — USGS MCS 2025 p.172 Domestic Production and Use |
| end_uses.uses[other_industrial_uses].share_pct | 10 | usgs_mcs_2025_sulfur | inferred | Not stated; derived as 100% − 90% sulfuric acid. USGS lists other uses (rubber vulcanization, fungicides, pharmaceuticals) without assigning a percentage |
| criticality.notes (net import reliance 7%) | 7% | usgs_mcs_2025_sulfur | verified | "Net import reliance … 7" (2024e) — USGS MCS 2025 p.172 Salient Statistics table |
| criticality.notes (Canada 70% of total imports) | 70% | usgs_mcs_2025_sulfur | verified | "Total sulfur imports: Canada, 70%" — USGS MCS 2025 p.172 Import Sources (2020–23) |
| geopolitical_events[2024-01].event (US production 5% below 2023) | 5% | usgs_mcs_2025_sulfur | verified | "Total U.S. sulfur production and shipments in 2024 were each estimated to be 5% less than that in 2023" — USGS MCS 2025 p.172–173 Events, Trends, and Issues |
| geopolitical_events[2024-01].event (elemental sulfur from petroleum/gas down 6%) | 6% | usgs_mcs_2025_sulfur | verified | "Domestic production of elemental sulfur from petroleum refineries and recovery from natural gas operations was estimated to have decreased by 6%" — USGS MCS 2025 p.172 Events |
| geopolitical_events[2024-01].event (Tampa price $69/long ton start of 2024) | $69/long ton | usgs_mcs_2025_sulfur | verified | "Contract sulfur prices in Tampa, FL, began 2024 at $69 per long ton" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2024-01].event (Tampa price $81/long ton early March) | $81/long ton | usgs_mcs_2025_sulfur | verified | "The sulfur price increased to $81 per long ton in early March" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2024-01].event (Tampa price $76/long ton early July) | $76/long ton | usgs_mcs_2025_sulfur | verified | "then decreased to $76 per long ton in early July" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2024-01].event (Tampa price $116/long ton Q4 2024) | $116/long ton | usgs_mcs_2025_sulfur | verified | "fourth quarter 2024 prices increased to $116 per long ton" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2024-01].event (world production 85 Mt 2024) | 85 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "World sulfur production in 2024 was an estimated 85 million tons" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2024-01].event (world production 85.8 Mt 2023) | 85.8 million_tonnes_per_year | usgs_mcs_2025_sulfur | verified | "compared with 85.8 million tons in 2023" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2025-01].event (Middle East production increase from 2025) | 2025 | usgs_mcs_2025_sulfur | verified | "Starting in 2025, sulfur production from the Middle East was expected to increase owing to upgrades and new refining projects" — USGS MCS 2025 p.173 Events |
| geopolitical_events[2025-01].impact (Middle East ~21% of world production) | ~21% | usgs_mcs_2025_sulfur | inferred | Not stated explicitly; SA(7,500)+AE(6,000)+QA(3,100)+KW(1,300) = 17,900 kt; 17,900/85,000 = 21.1% — derived from USGS 2024e table values |
| geopolitical_events[2024-01].event (HPAL nickel demand increase) | qualitative | usgs_mcs_2025_sulfur | verified | "an increase in nickel production from high-pressure acid leach projects to produce battery materials was expected to increase sulfur demand" — USGS MCS 2025 p.173 Events |
| feedstock_origins[metal_sulfide_ore].notes (~8% of US production, 5 smelters, 4 States, 4 companies) | ~8%; 5; 4; 4 | usgs_mcs_2025_sulfur | verified | "five nonferrous-metal smelters in four States by four companies … representing about 8% of production of sulfur in all forms" — USGS MCS 2025 p.172 Domestic Production and Use |
| substitutes[general].notes (quoted verbatim) | text | usgs_mcs_2025_sulfur | verified | "Substitutes for sulfur at present or anticipated price levels are not satisfactory; some acids, in certain applications, may be substituted for sulfuric acid, but usually at a higher cost" — USGS MCS 2025 p.173 Substitutes section |

## Notes

**Source access**: USGS MCS 2025 Sulfur PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-sulfur.pdf) fetched successfully and rendered as two pages (pp. 172–173) via pdftotext. Full content of both pages confirmed accessible. All claims trace to a single primary source.

**All claims verified or inferred — zero discrepancies**: Every quantity in the YAML matches the USGS table exactly. All share_pct fields marked `inferred` because USGS does not state country percentage shares in the sulfur chapter narrative or table.

**No quantitative reserves**: USGS MCS 2025 does not provide country-level or world economic reserves for sulfur. The reserves section states only "Reserves of sulfur in crude oil, natural gas, and sulfide ores are large" without quantification. The YAML correctly sets economic_reserves = null and provides only the resources figure (~5 billion tons from the World Resources paragraph). This is consistent with project notes from worker w-d94d04e4a2ac.

**Sum check (mine share_pcts)**: CN(22.4)+US(9.6)+RU(8.8)+SA(8.8)+AE(7.1)+KZ(6.0)+CA(5.9)+IN(4.4)+JP(3.6)+KR(3.6)+QA(3.6)+IR(2.4)+CL(1.5)+KW(1.5)+PL(1.3)+AU(1.1)+TM(1.1)+ZZ(7.5) = 100.2%. Slight overshoot is a rounding artifact (individual quantities sum to 85,200 kt vs. rounded world total of 85,000 kt); within expected ±1% range.

**Price values match exactly**: The five-year US average unit value series ($24.90, $90.40, $177.80, $58.90, $50.00 for 2020–2024) matches the Salient Statistics table precisely. The USGS table shows "177.8" for 2022; the YAML records 177.80 — numerically identical.

**China production footnote confirmed**: USGS MCS 2025 footnote 4 states "Sulfur production in China includes byproduct elemental sulfur recovered from natural gas and petroleum, the estimated sulfur content of byproduct sulfuric acid from metallurgy, and the sulfur content of sulfuric acid from pyrite." The YAML notes field for CN is consistent with this.

**Criticality flags (false)**: The YAML correctly records sulfur as not on any critical minerals list. Sulfur appears on no USGS, EU CRM, or EU Strategic Raw Materials list. The criticality flags carry no per-flag source_id; no source is cited for the list membership status itself, but the designation (false) aligns with the observable absence of sulfur from known critical minerals frameworks as of 2025.

**Middle East 21% claim**: The impact text for the 2025-01 Middle East event states Saudi Arabia, UAE, Qatar, and Kuwait "already account for ~21% of world sulfur production." This is derived from USGS table data (17,900/85,000 = 21.1%), not explicitly stated in the USGS text. Marked `inferred`.

**Tampa contract prices vs. annual average**: The geopolitical event for 2024-01 notes both Tampa long-ton contract prices ($69–$116 range intra-year) and the annual average unit value ($50.00/t FOB mine/plant). These are distinct pricing benchmarks; the Tampa prices are quoted per long ton (≈ 1.016 metric tons), while the FOB price is per metric ton. The narrative correctly distinguishes these.

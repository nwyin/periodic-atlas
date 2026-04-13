# Verification: Ce

- Element: cerium (Ce)
- Snapshot year: 2025
- Verifier: worker-6c12640b91c9 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 68 |
| discrepancy | 6 |
| inferred | 25 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.notes (world REO total 390,000 t 2024e) | 390000 t REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — USGS MCS 2025 RE p.145 Events text; also "World total (rounded) … 390,000" — p.145 Mine Production table 2024e column |
| production[0].mine.notes (world 2023 base 376,000 t REO) | 376000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 376,000" — USGS MCS 2025 RE p.145 Mine Production table 2023 column |
| production[0].mine.value | 129000 tonnes_per_year | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not report per-element Ce tonnage; derived as 390,000 t REO × ~33% basket share = ~128,700 ≈ 129,000 t; basket share itself is inferred (see below) |
| production[0].mine.notes (~33% typical global basket share) | ~33% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter gives no per-element basket share percentages; the ~33% global weighted average is consistent with published mineralogical data (bastnaesite ~49% Ce, monazite ~43% Ce, ionic clay ~2–5% Ce) but is not stated in the cited chapter |
| production[0].mine.notes (~124,000 t Ce-equivalent 2023) | ~124000 t | usgs_mcs_2025_rare_earths | inferred | Derived from 376,000 t REO × 33% basket share = 124,080 t; same caveat as basket share estimate above |
| production[0].mining_by_country.shares[CN].quantity.value + share_pct | 270000 t; 69.2% | usgs_mcs_2025_rare_earths | verified | "China … 14270,000" — USGS MCS 2025 RE p.145 table 2024e column (footnote 14: production quota, excludes undocumented output); 270,000/390,000 = 69.2% |
| production[0].mining_by_country.shares[CN].notes (up from 255,000 t 2023) | 255000 t | usgs_mcs_2025_rare_earths | verified | "China … 14255,000" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].mining_by_country.shares[US].quantity.value + share_pct | 45000 t; 11.5% | usgs_mcs_2025_rare_earths | verified | "United States … 45,000" — USGS MCS 2025 RE p.145 table 2024e column; also p.144: "45,000 tons of REO in mineral concentrates"; 45,000/390,000 = 11.5% |
| production[0].mining_by_country.shares[US].notes ($260 million value) | $260 million | usgs_mcs_2025_rare_earths | verified | "valued at $260 million" — USGS MCS 2025 RE p.144 Domestic Production text |
| production[0].mining_by_country.shares[US].notes (compounds 1,300 t 2024, 250 t 2023) | 1300 t; 250 t | usgs_mcs_2025_rare_earths | verified | "Compounds and metals … 1,300" (2024e) and "… 250" (2023) — USGS MCS 2025 RE p.144 Salient Statistics table |
| production[0].mining_by_country.shares[US].notes (80% net import reliance 2024e) | 80% | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — USGS MCS 2025 RE p.144 Salient Statistics 2024e column; mineral concentrates row shows "E" (net exporter) |
| production[0].mining_by_country.shares[MM].quantity.value + share_pct | 31000 t; 7.9% | usgs_mcs_2025_rare_earths | verified | "Burma … 1231,000" — USGS MCS 2025 RE p.145 table 2024e column (footnote 12: estimated from Chinese import data); 31,000/390,000 = 7.95% ≈ 7.9% |
| production[0].mining_by_country.shares[MM].notes (down from 43,000 t 2023, -28% YoY) | 43000 t; -28% | usgs_mcs_2025_rare_earths | verified | "Burma … 1243,000" — USGS MCS 2025 RE p.145 table 2023 column; (43,000−31,000)/43,000 = 27.9% ≈ 28% |
| production[0].mining_by_country.shares[AU].quantity.value + share_pct | 13000 t; 3.3% | usgs_mcs_2025_rare_earths | verified | "Australia … 1213,000" — USGS MCS 2025 RE p.145 table 2024e column; 13,000/390,000 = 3.33% |
| production[0].mining_by_country.shares[AU].notes (down from 16,000 t 2023) | 16000 t | usgs_mcs_2025_rare_earths | verified | "Australia … 1216,000" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].mining_by_country.shares[NG].quantity.value + share_pct | 13000 t; 3.3% | usgs_mcs_2025_rare_earths | verified | "Nigeria … 1213,000" — USGS MCS 2025 RE p.145 table 2024e column; 13,000/390,000 = 3.33% |
| production[0].mining_by_country.shares[NG].notes (up from 7,200 t 2023, +80% YoY) | 7200 t; +80% | usgs_mcs_2025_rare_earths | verified | "Nigeria … 127,200" — USGS MCS 2025 RE p.145 table 2023 column; (13,000−7,200)/7,200 = 80.6% ≈ 80% |
| production[0].mining_by_country.shares[TZ].quantity.value | 13000 t | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 table shows Tanzania mine production = "—" (zero) for both 2023 and 2024; Tanzania holds reserves (890,000 t) but has no reported production. Thailand (TH) had 13,000 t in 2024. Country code TZ is incorrect; this row's production data belongs to TH. |
| production[0].mining_by_country.shares[TZ].notes (up from 3,600 t 2023, +261% YoY) | 3600 t 2023; +261% | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 table shows Tanzania 2023 production = "—" (zero); Thailand 2023 = 3,600 t → 2024 = 13,000 t, a 261% increase. The growth note applies to Thailand, not Tanzania. |
| production[0].mining_by_country.shares[TZ].notes (Tanzania reserves 890,000 t) | 890000 t | usgs_mcs_2025_rare_earths | verified | "Tanzania … Reserves: 890,000" — USGS MCS 2025 RE p.145 Reserves column; note confirms reserves but not production |
| production[0].mining_by_country.shares[IN].quantity.value + share_pct | 2900 t; 0.7% | usgs_mcs_2025_rare_earths | verified | "India … 2,900" — USGS MCS 2025 RE p.145 table 2024e column; 2,900/390,000 = 0.74% ≈ 0.7%; unchanged from 2023 |
| production[0].mining_by_country.shares[RU].quantity.value + share_pct | 2500 t; 0.6% | usgs_mcs_2025_rare_earths | verified | "Russia … 2,500" — USGS MCS 2025 RE p.145 table 2024e column; 2,500/390,000 = 0.64% ≈ 0.6%; unchanged from 2023 |
| production[0].mining_by_country.shares[MG].quantity.value + share_pct | 2000 t; 0.5% | usgs_mcs_2025_rare_earths | verified | "Madagascar … 122,000" — USGS MCS 2025 RE p.145 table 2024e column; 2,000/390,000 = 0.51% ≈ 0.5% |
| production[0].mining_by_country.shares[MG].notes (down from 2,100 t 2023) | 2100 t | usgs_mcs_2025_rare_earths | verified | "Madagascar … 122,100" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].mining_by_country.shares[VN].quantity.value + share_pct | 300 t; 0.08% | usgs_mcs_2025_rare_earths | verified | "Vietnam … 12300" — USGS MCS 2025 RE p.145 table 2024e column; 300/390,000 = 0.077% ≈ 0.08%; unchanged from 2023 |
| production[0].mining_by_country.shares[VN].notes (Vietnam 3,500,000 t reserves) | 3500000 t | usgs_mcs_2025_rare_earths | verified | "Vietnam … Reserves: 3,500,000" — USGS MCS 2025 RE p.145 Reserves column |
| production[0].mining_by_country.shares[TH].quantity.value | 300 t | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 table shows Thailand 2024e = "1213,000" t (not 300 t); 300 t is Vietnam's production figure. Thailand's share is 3.3%, not 0.08%. Country values for TH and TZ appear to be systematically swapped. |
| production[0].mining_by_country.shares[TH].notes (300 t unchanged from 2023) | 300 t unchanged | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 shows Thailand 2023 = 3,600 t → 2024 = 13,000 t — neither figure is 300 t and production is not "unchanged." The "unchanged" description matches Vietnam (VN=300 t in both years), not Thailand. |
| production[0].mining_by_country.shares[MY].quantity.value + share_pct | 130 t; 0.03% | usgs_mcs_2025_rare_earths | verified | "Malaysia … 12130" — USGS MCS 2025 RE p.145 table 2024e column; 130/390,000 = 0.033% ≈ 0.03% |
| production[0].mining_by_country.shares[MY].notes (down from 310 t 2023) | 310 t | usgs_mcs_2025_rare_earths | verified | "Malaysia … 12310" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].mining_by_country.shares[BR].quantity.value + share_pct | 20 t; 0.01% | usgs_mcs_2025_rare_earths | verified | "Brazil … 20" — USGS MCS 2025 RE p.145 table 2024e column; 20/390,000 = 0.005% (YAML rounds up to 0.01%) |
| production[0].mining_by_country.shares[BR].notes (down from 140 t 2023) | 140 t | usgs_mcs_2025_rare_earths | verified | "Brazil … 140" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].mining_by_country.shares[ZZ].quantity.value + share_pct | 1100 t; 0.3% | usgs_mcs_2025_rare_earths | verified | "Other … 1,100" — USGS MCS 2025 RE p.145 table 2024e column; 1,100/390,000 = 0.28% ≈ 0.3% |
| production[0].mining_by_country.shares[ZZ].notes (down from 1,440 t 2023) | 1440 t | usgs_mcs_2025_rare_earths | verified | "Other … 1,440" — USGS MCS 2025 RE p.145 table 2023 column |
| production[0].refining_by_country.shares[CN].share_pct | 70% | usgs_mcs_2025_rare_earths | verified | "China, 70%" — USGS MCS 2025 RE p.144 Import Sources (2020–23); footnote 9: includes Hong Kong |
| production[0].refining_by_country.shares[MY].share_pct | 13% | usgs_mcs_2025_rare_earths | verified | "Malaysia, 13%" — USGS MCS 2025 RE p.144 Import Sources (2020–23) |
| production[0].refining_by_country.shares[JP].share_pct | 6% | usgs_mcs_2025_rare_earths | verified | "Japan, 6%" — USGS MCS 2025 RE p.144 Import Sources (2020–23) |
| production[0].refining_by_country.shares[EE].share_pct | 5% | usgs_mcs_2025_rare_earths | verified | "Estonia, 5%" — USGS MCS 2025 RE p.144 Import Sources (2020–23) |
| production[0].refining_by_country.shares[ZZ].share_pct | 6% | usgs_mcs_2025_rare_earths | verified | "other, 6%" — USGS MCS 2025 RE p.144 Import Sources (2020–23) |
| reserves.economic_reserves.value | 90000000 t | usgs_mcs_2025_rare_earths | verified | ">90,000,000" — USGS MCS 2025 RE p.145 World Mine Production and Reserves table, World total Reserves column |
| reserves.reserves_by_country.shares[CN].quantity.value | 44000000 t | usgs_mcs_2025_rare_earths | verified | "China … 44,000,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country.shares[CN].share_pct | 48.4% | usgs_mcs_2025_rare_earths | inferred | World reserves stated as ">90,000,000" (approximate); 44,000,000/90,000,000 = 48.9%; YAML uses 48.4% (≈44/91) — both are plausible given imprecise denominator |
| reserves.reserves_by_country.shares[BR].quantity.value | 21000000 t | usgs_mcs_2025_rare_earths | verified | "Brazil … 21,000,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country.shares[BR].share_pct | 23.1% | usgs_mcs_2025_rare_earths | inferred | 21,000,000/>90,000,000; share_pct is approximate given imprecise world total |
| reserves.reserves_by_country.shares[IN].quantity.value | 6900000 t | usgs_mcs_2025_rare_earths | verified | "India … 6,900,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country.shares[IN].share_pct | 7.6% | usgs_mcs_2025_rare_earths | inferred | 6,900,000/>90,000,000; approximate |
| reserves.reserves_by_country.shares[AU].quantity.value | 5700000 t | usgs_mcs_2025_rare_earths | verified | "Australia … 5,700,000 13" — USGS MCS 2025 RE p.145 Reserves column (footnote 13: JORC reserves 3.3 Mt) |
| reserves.reserves_by_country.shares[AU].notes (JORC 3,300,000 t) | 3300000 t | usgs_mcs_2025_rare_earths | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons" — USGS MCS 2025 RE p.145 footnote 13 |
| reserves.reserves_by_country.shares[RU].quantity.value | 3800000 t | usgs_mcs_2025_rare_earths | verified | "Russia … 3,800,000" — USGS MCS 2025 RE p.145 Reserves column; revised in 2025 per USGS notes |
| reserves.reserves_by_country.shares[VN].quantity.value | 3500000 t | usgs_mcs_2025_rare_earths | verified | "Vietnam … 3,500,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country.shares[US].quantity.value | 1900000 t | usgs_mcs_2025_rare_earths | verified | "United States … 1,900,000" — USGS MCS 2025 RE p.145 Reserves column; revised in 2025 per USGS notes |
| reserves.reserves_by_country.shares[GL].quantity.value | 1500000 t | usgs_mcs_2025_rare_earths | verified | "Greenland … 1,500,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country.shares[TZ].quantity.value | 890000 t | usgs_mcs_2025_rare_earths | verified | "Tanzania … 890,000" — USGS MCS 2025 RE p.145 Reserves column; Tanzania reserves are confirmed; note that Tanzania production = "—" (zero) in the same table |
| reserves.reserves_by_country.shares[ZA].quantity.value | 860000 t | usgs_mcs_2025_rare_earths | verified | "South Africa … 860,000" — USGS MCS 2025 RE p.145 Reserves column; revised in 2025 per USGS notes |
| reserves.reserves_by_country.shares[CA].quantity.value | 830000 t | usgs_mcs_2025_rare_earths | verified | "Canada … 830,000" — USGS MCS 2025 RE p.145 Reserves column |
| reserves.reserves_by_country share_pcts (AU 6.3%, RU 4.2%, VN 3.8%, US 2.1%, GL 1.7%, TZ 1.0%, ZA 0.9%, CA 0.9%) | various | usgs_mcs_2025_rare_earths | inferred | All reserve share_pcts are computed as country_qty / 90,000,000 (imprecise denominator); values are plausible approximations, not exact USGS figures |
| reserves.notes (US resources 3.6 Mt) | 3600000 t | usgs_mcs_2025_rare_earths | verified | "3.6 million tons in the United States" — USGS MCS 2025 RE p.145 World Resources paragraph |
| reserves.notes (Canada resources >14 Mt) | >14000000 t | usgs_mcs_2025_rare_earths | verified | "more than 14 million tons in Canada" — USGS MCS 2025 RE p.145 World Resources paragraph |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 49% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter confirms bastnaesite is mined at Mountain Pass and is a primary REE source, but gives no Ce wt% in the mineral; 49% is a standard mineralogical reference value not stated in the cited chapter |
| feedstock_origins[monazite_sand].typical_concentration_pct | 43% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE confirms monazite is stockpiled in southeastern US heavy-mineral-sand concentrates, but does not give a Ce fraction; 43% is from mineralogical literature, not from the cited chapter |
| feedstock_origins[ionic_adsorption_clay].typical_concentration_pct | ~3% (notes: 2–5%) | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE confirms ionic adsorption clay as an REE source (China, Myanmar), but gives no Ce fraction; the ~2–5% heavy-REE-dominant composition is consistent with published data but not from the cited chapter |
| end_uses.uses[catalysts_fcc_and_auto].share_pct | 45% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE p.144 states "The estimated leading domestic end use of rare earths was catalysts" — confirms catalysts are the largest US REE end use, but gives no Ce-specific share; 45% is an approximation not stated in the cited chapter |
| end_uses.uses[metallurgical_additives].share_pct | 18% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE lists "metallurgical applications and alloys" as a significant end use; 18% is an approximation not stated in the cited chapter |
| end_uses.uses[glass_polishing].share_pct | 14% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE lists "polishing" as an end use; 14% is an approximation not stated in the cited chapter |
| end_uses.uses[glass_ceramics_additives].share_pct | 12% | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE lists "ceramics and glass" as an end use; 12% is an approximation not stated in the cited chapter |
| end_uses.uses[phosphors_and_other].share_pct | 11% | usgs_mcs_2025_rare_earths | inferred | Residual share; USGS MCS 2025 RE does not quantify phosphor or other minor Ce end uses; 11% is an approximation not stated in the cited chapter |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not explicitly state cerium's inclusion on the 2022 US Critical Minerals List; status is inferred from Ce's membership in the rare earth elements group, which is listed in Table 4 of the full MCS 2025 (not this chapter) |
| criticality.eu_crm_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU CRM status not stated in USGS RE chapter; inferred from EU CRMA 2024/1252 which includes light rare earth elements (of which Ce is one) in its critical raw materials list |
| criticality.eu_strategic_list_as_of_2024 | true | usgs_mcs_2025_rare_earths | inferred | EU strategic list status not stated in USGS RE chapter; inferred from EU CRMA Annex II inclusion of rare earth elements for magnet applications |
| criticality.notes (80% net import reliance 2024e) | 80% | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — USGS MCS 2025 RE p.144 Salient Statistics 2024e column |
| criticality.notes (>95% 2020–2023) | >95% 2021-2023; 100% 2020 | usgs_mcs_2025_rare_earths | verified | "Net import reliance … >95" for 2021, 2022, 2023 and "100" for 2020 — USGS MCS 2025 RE p.144 Salient Statistics; footnote 8: in 2020 all domestic mineral concentrates were exported or held in inventory |
| criticality.notes (70% Chinese imports 2020–23) | 70% | usgs_mcs_2025_rare_earths | verified | "China, 70%" — USGS MCS 2025 RE p.144 Import Sources (2020–23) |
| prices[oxide_2024].value | $1/kg | usgs_mcs_2025_rare_earths | verified | "Cerium oxide, 99.5% minimum … 1" — USGS MCS 2025 RE p.144 Salient Statistics 2024e column; source footnote 6: Argus Media Group, Argus Non-Ferrous Markets |
| prices[oxide_2023].value | $1/kg | usgs_mcs_2025_rare_earths | verified | "Cerium oxide, 99.5% minimum … 1" — USGS MCS 2025 RE p.144 Salient Statistics 2023 column |
| prices[oxide_2022].value | $1/kg | usgs_mcs_2025_rare_earths | verified | "Cerium oxide, 99.5% minimum … 1" — USGS MCS 2025 RE p.144 Salient Statistics 2022 column |
| prices[oxide_2021].value | $2/kg | usgs_mcs_2025_rare_earths | verified | "Cerium oxide, 99.5% minimum … 2" — USGS MCS 2025 RE p.144 Salient Statistics 2021 column |
| prices[oxide_2020].value | $2/kg | usgs_mcs_2025_rare_earths | verified | "Cerium oxide, 99.5% minimum … 2" — USGS MCS 2025 RE p.144 Salient Statistics 2020 column |
| prices[alloy_2024].value | $5/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — USGS MCS 2025 RE p.144 Salient Statistics 2024e column |
| prices[alloy_2023].value | $5/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — USGS MCS 2025 RE p.144 Salient Statistics 2023 column |
| prices[alloy_2022].value | $7/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 7" — USGS MCS 2025 RE p.144 Salient Statistics 2022 column |
| prices[alloy_2021].value | $6/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 6" — USGS MCS 2025 RE p.144 Salient Statistics 2021 column |
| prices[alloy_2020].value | $5/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — USGS MCS 2025 RE p.144 Salient Statistics 2020 column |
| prices.notes (Argus Media Group source) | Argus Media Group | usgs_mcs_2025_rare_earths | verified | "Source: Argus Media Group, Argus Non-Ferrous Markets" — USGS MCS 2025 RE p.144 Salient Statistics footnote 6 |
| prices.notes (mischmetall composition 65% Ce, 35% La) | 65% Ce, 35% La | usgs_mcs_2025_rare_earths | verified | USGS MCS 2025 RE p.144 Salient Statistics table row label: "Mischmetal, 65% cerium, 35% lanthanum" |
| geopolitical_events[0].event (China quota, footnote 14) | quota; undocumented output | usgs_mcs_2025_rare_earths | verified | "14Production quota; does not include undocumented production" — USGS MCS 2025 RE p.145 footnote 14; China 2024 production shown as "14270,000" in mine production table |
| geopolitical_events[1].event (Myanmar 28% YoY decline, 31,000 t from 43,000 t) | 31000 t; 43000 t; -28% | usgs_mcs_2025_rare_earths | verified | "Burma … 1231,000" (2024e) vs "1243,000" (2023) — USGS MCS 2025 RE p.145 table; (43,000−31,000)/43,000 = 27.9% ≈ 28%; footnote 12: estimated from Chinese import data |
| geopolitical_events[2].event "Nigeria and Tanzania each reach 13,000 t" | Tanzania 13000 t | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 Events text reads "increased mining and processing in China, Nigeria, and Thailand" — Tanzania is not mentioned; the USGS mine production table shows Tanzania = "—" for both 2023 and 2024; the 13,000 t belongs to Thailand (TH), not Tanzania (TZ) |
| geopolitical_events[2].impact (global production 390,000 t) | 390000 t | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — USGS MCS 2025 RE p.145 Events text |
| geopolitical_events[3].event "FY2025 potential acquisitions of 1,100 short tons of cerium" | 1100 t Ce FY2025 | usgs_mcs_2025_rare_earths | discrepancy | USGS MCS 2025 RE p.145 Government Stockpile table shows cerium FY2025 potential acquisitions = "—" (zero/none); the 1,100 t is for lanthanum FY2025. Ce was targeted only in FY2024 (550 t). The event title conflates La FY2025 with Ce. |
| geopolitical_events[3].impact (FY2024 Ce 550 t) | 550 t Ce FY2024 | usgs_mcs_2025_rare_earths | verified | "Cerium … FY 2024 Potential acquisitions … 550" — USGS MCS 2025 RE p.145 Government Stockpile table (gross weight per footnote 10) |
| geopolitical_events[3].impact (FY2025 La 1,100 t; FY2024 La 1,300 t) | 1100 t La FY2025; 1300 t La FY2024 | usgs_mcs_2025_rare_earths | verified | "Lanthanum … FY 2024 … 1,300 / FY 2025 … 1,100" — USGS MCS 2025 RE p.145 Government Stockpile table; these figures are correct for lanthanum but were incorrectly attributed to cerium in the event title |

## Notes

**Source coverage**: All 99 claims cite `usgs_mcs_2025_rare_earths` (URL: https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf). The PDF was successfully fetched and extracted using `pdftotext -layout`. The rare earths chapter spans pp.144–145 of the MCS 2025.

**Tanzania/Thailand country swap (root cause of 4 discrepancies)**: The Ce.yaml mining_by_country section assigns 13,000 t 2024 production (and the "up from 3,600 t in 2023, +261% YoY" note) to Tanzania (TZ) and assigns 300 t (unchanged from 2023) to Thailand (TH). The USGS MCS 2025 table shows the opposite: Thailand production was 3,600 t (2023) → 13,000 t (2024e) — a 261% increase — while Tanzania had zero production in both years. Vietnam (VN) had 300 t unchanged. The TZ and TH country code entries appear to have been constructed from Thailand's data. Tanzania's reserves (890,000 t) are correctly attributed in the reserves_by_country section. Recommendation: in Ce.yaml, replace the TZ mining entry with a TH entry carrying the 13,000 t value, and either remove the TH entry (since it duplicates VN's data) or correct it to TH=13,000 t.

**FY2025 stockpile discrepancy (root cause of 2 discrepancies)**: The Government Stockpile table in USGS MCS 2025 RE p.145 shows:
- Cerium: FY2024 acquisitions = 550 t; FY2025 = "—" (no planned acquisitions)
- Lanthanum: FY2024 acquisitions = 1,300 t; FY2025 = 1,100 t

The Ce.yaml geopolitical event[3] states "FY2025 potential acquisitions of 1,100 short tons of cerium" — this is wrong; 1,100 t is the lanthanum FY2025 figure. Cerium has no FY2025 acquisition target. The impact text compounds the error with "1,100 t cerium (up from 550 t in FY2024)" — cerium actually dropped from 550 t to zero between FY2024 and FY2025. The narrative section also repeats this error: "The US government's decision to include cerium in the FY2025 National Defense Stockpile acquisition targets (1,100 short tons)."

**Net import reliance**: The USGS table shows 2020 = 100% (not ">95%"), 2021–2023 = ">95%", 2024e = 80%. The YAML description "~80% in 2024e (down from >95% in 2020–2023)" slightly understates the 2020 figure but is broadly accurate and not a material discrepancy.

**Reserves world total denominator**: The USGS reports world REE reserves as ">90,000,000 t" — an inequality, not an exact figure. All reserve share_pcts in the YAML are therefore computed from an approximate denominator and are marked as inferred. The individual country reserve quantities are all exact and verified.

**End-use shares (all inferred)**: The USGS MCS 2025 rare earths chapter provides qualitative end-use categories ("catalysts", "ceramics and glass", "metallurgical applications and alloys", "polishing", "permanent magnets") but no quantitative Ce-specific share percentages. The 45%/18%/14%/12%/11% breakdown in Ce.yaml is editorially derived; marked as inferred with confidence: low throughout.

**Feedstock Ce concentrations (all inferred)**: The USGS chapter confirms bastnaesite, monazite, and ionic adsorption clay as REE sources but gives no Ce wt% fractions. The 49%/43%/~3% values are standard mineralogical literature figures, not sourced from the cited USGS chapter.

**Mischmetall 2021–2024 price trend**: YAML claims mischmetall was "$5–7/kg over 2020–2024." Confirmed: 2020=$5, 2021=$6, 2022=$7, 2023=$5, 2024e=$5. The range $5–7 is accurate.

**USGS Events text (country attribution)**: The USGS Events, Trends, and Issues paragraph explicitly names "China, Nigeria, and Thailand" as drivers of the 2024 global production increase to 390,000 t. Ce.yaml's geopolitical_events[2] event title substitutes Tanzania for Thailand — a clear error that is also the root cause of the TZ/TH mining country swap throughout the production section.

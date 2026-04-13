# Verification: La

- Element: lanthanum (La)
- Snapshot year: 2025
- Verifier: worker-028a4d2216de (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 53 |
| discrepancy | 0 |
| inferred | 27 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 113100 tonnes_per_year | usgs_mcs_2025_rare_earths | inferred | USGS does not report per-element La production. Derived: 390,000 t REO × ~29% basket share = ~113,100 t La2O3. Basket share is itself inferred (see below). |
| production[0].mine.notes "world total REO 2024e = 390,000" | 390000 t REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — p.145 Events, Trends, and Issues |
| production[0].mine.notes "2023 total = 376,000" | 376000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 376,000" — p.145 Mine production table, 2023 column |
| production[0].mine.notes "~29% basket share used as central estimate" | ~29 pct | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not report per-element basket shares. The 27–32% La2O3 range is consistent with published mineralogical data for bastnaesite and monazite deposits; 29% used as midpoint estimate. Not directly verifiable from cited source. |
| production[0].mining_by_country[CN].share_pct | 69.2 | usgs_mcs_2025_rare_earths | verified | Computed: China 270,000 t / 390,000 t world total = 69.23% ≈ 69.2%. Values confirmed — p.145 Mine production table. |
| production[0].mining_by_country[CN].notes "China 2024e: 270,000 t REO" | 270000 t REO | usgs_mcs_2025_rare_earths | verified | "China … 270,000" — p.145 Mine production table, 2024 column (footnote 14: "Production quota; does not include undocumented production.") |
| production[0].mining_by_country[CN].notes "255,000 t in 2023" | 255000 t REO | usgs_mcs_2025_rare_earths | verified | "China … 255,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[US].share_pct | 11.5 | usgs_mcs_2025_rare_earths | verified | Computed: 45,000 / 390,000 = 11.54% ≈ 11.5%. Values confirmed — p.145. |
| production[0].mining_by_country[US].notes "US 2024e: 45,000 t REO" | 45000 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 45,000" — p.145 Mine production table, 2024 column. Also confirmed p.144 Domestic Production and Use: "An estimated 45,000 tons of REO in mineral concentrates were produced." |
| production[0].mining_by_country[US].notes "41,600 t REO in 2023" | 41600 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 41,600" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[MM].share_pct | 7.9 | usgs_mcs_2025_rare_earths | verified | Computed: 31,000 / 390,000 = 7.95% ≈ 7.9%. Values confirmed — p.145. |
| production[0].mining_by_country[MM].notes "Burma 2024e: 31,000 t REO" | 31000 t REO | usgs_mcs_2025_rare_earths | verified | "Burma … 31,000" — p.145 Mine production table, 2024 column (footnote 12: "Estimated based on reported import data for China. Source: Zen Innovations, Global Trade Tracker.") |
| production[0].mining_by_country[MM].notes "43,000 t in 2023" | 43000 t REO | usgs_mcs_2025_rare_earths | verified | "Burma … 43,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[AU].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[AU].notes "Australia 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Australia … 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[AU].notes "16,000 t in 2023" | 16000 t REO | usgs_mcs_2025_rare_earths | verified | "Australia … 16,000" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[AU].notes "JORC-compliant reserves 3.3 Mt" | 3.3 Mt REO | usgs_mcs_2025_rare_earths | verified | Footnote 13: "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 3.3 million tons." — p.145 |
| production[0].mining_by_country[NG].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[NG].notes "Nigeria 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Nigeria … 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[NG].notes "7,200 t in 2023" | 7200 t REO | usgs_mcs_2025_rare_earths | verified | "Nigeria … 7,200" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[TH].share_pct | 3.3 | usgs_mcs_2025_rare_earths | verified | Computed: 13,000 / 390,000 = 3.33% ≈ 3.3%. Values confirmed — p.145. |
| production[0].mining_by_country[TH].notes "Thailand 2024e: 13,000 t REO" | 13000 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand … 13,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[TH].notes "3,600 t in 2023" | 3600 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand … 3,600" — p.145 Mine production table, 2023 column |
| production[0].mining_by_country[ZZ].notes "India 2,900" | 2900 t REO | usgs_mcs_2025_rare_earths | verified | "India … 2,900" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Russia 2,500" | 2500 t REO | usgs_mcs_2025_rare_earths | verified | "Russia … 2,500" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Madagascar 2,000" | 2000 t REO | usgs_mcs_2025_rare_earths | verified | "Madagascar … 2,000" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Other 1,100" | 1100 t REO | usgs_mcs_2025_rare_earths | verified | "Other … 1,100" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].notes "Vietnam 300" | 300 t REO | usgs_mcs_2025_rare_earths | verified | "Vietnam … 300" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Malaysia 130" | 130 t REO | usgs_mcs_2025_rare_earths | verified | "Malaysia … 130" — p.145 Mine production table, 2024 column (footnote 12) |
| production[0].mining_by_country[ZZ].notes "Brazil 20" | 20 t REO | usgs_mcs_2025_rare_earths | verified | "Brazil … 20" — p.145 Mine production table, 2024 column |
| production[0].mining_by_country[ZZ].share_pct | 2.5 | usgs_mcs_2025_rare_earths | inferred | Rest-of-world sum: 2,900+2,500+2,000+1,100+300+130+20 = 8,950 t → 8,950/390,000 = 2.295% ≈ 2.3%. YAML states 2.5% "for share arithmetic." The 2.5% causes share total to slightly exceed 100% (CN 69.2+US 11.5+MM 7.9+AU 3.3+NG 3.3+TH 3.3+ZZ 2.5 = 101.0%). Share percentage is not stated in source. |
| production[0].refining_by_country[CN].share_pct | 91 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not state an explicit refining/separation percentage for China. Import sources (2020-23): China 70%, Malaysia 13%, Japan 6%, Estonia 5% — these are US import shares, not global refining shares. The 91% figure is widely cited from DOE/IEA sources but not directly stated in the cited USGS chapter. |
| production[0].refining_by_country[ZZ].share_pct | 9 | usgs_mcs_2025_rare_earths | inferred | Residual: 100% − 91% inferred CN; same caveat applies. |
| production[0].refining_by_country.notes "Malaysia 13%, Japan 6%, Estonia 5% of US imports" | Malaysia 13 / Japan 6 / Estonia 5 pct | usgs_mcs_2025_rare_earths | verified | "Import Sources (2020–23): Rare-earth compounds and metals: China, 70%; Malaysia, 13%; Japan, 6%; Estonia, 5%; and other, 6%." — p.144 |
| reserves.economic_reserves.value | 26100000 t La2O3 | usgs_mcs_2025_rare_earths | inferred | Derived: 90,000,000 t REO floor × ~29% basket share = 26,100,000 t La2O3. Floor value confirmed (see below); 29% basket share is inferred. Confidence is low. |
| reserves.notes "USGS world REE reserves >90,000,000 t REO" | >90000000 t REO | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … >90,000,000" — p.145 Reserves column |
| reserves.notes "revised for Russia, South Africa, United States, Vietnam" | revised countries | usgs_mcs_2025_rare_earths | verified | "Reserves for Russia, South Africa, the United States, and Vietnam were revised based on company and Government reports." — p.145 World Mine Production and Reserves |
| reserves.reserves_by_country[CN].notes "China: 44,000,000 t REO" | 44000000 t REO | usgs_mcs_2025_rare_earths | verified | "China … 44,000,000" — p.145 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 48.9 | usgs_mcs_2025_rare_earths | inferred | Computed: 44,000,000 / 90,000,000 = 48.89% ≈ 48.9%. Denominator is the stated floor; not given in source. |
| reserves.reserves_by_country[BR].notes "Brazil: 21,000,000 t REO" | 21000000 t REO | usgs_mcs_2025_rare_earths | verified | "Brazil … 21,000,000" — p.145 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 23.3 | usgs_mcs_2025_rare_earths | inferred | Computed: 21,000,000 / 90,000,000 = 23.33% ≈ 23.3%. |
| reserves.reserves_by_country[IN].notes "India: 6,900,000 t REO" | 6900000 t REO | usgs_mcs_2025_rare_earths | verified | "India … 6,900,000" — p.145 Reserves column |
| reserves.reserves_by_country[IN].share_pct | 7.7 | usgs_mcs_2025_rare_earths | inferred | Computed: 6,900,000 / 90,000,000 = 7.67% ≈ 7.7%. |
| reserves.reserves_by_country[AU].notes "Australia: 5,700,000 t REO (JORC 3.3 Mt)" | 5700000 t REO | usgs_mcs_2025_rare_earths | verified | "Australia … 5,700,000" — p.145 Reserves column; JORC 3.3 Mt in footnote 13 |
| reserves.reserves_by_country[AU].share_pct | 6.3 | usgs_mcs_2025_rare_earths | inferred | Computed: 5,700,000 / 90,000,000 = 6.33% ≈ 6.3%. |
| reserves.reserves_by_country[RU].notes "Russia: 3,800,000 t REO (revised)" | 3800000 t REO | usgs_mcs_2025_rare_earths | verified | "Russia … 3,800,000" — p.145 Reserves column (revised in MCS 2025) |
| reserves.reserves_by_country[RU].share_pct | 4.2 | usgs_mcs_2025_rare_earths | inferred | Computed: 3,800,000 / 90,000,000 = 4.22% ≈ 4.2%. |
| reserves.reserves_by_country[VN].notes "Vietnam: 3,500,000 t REO (revised)" | 3500000 t REO | usgs_mcs_2025_rare_earths | verified | "Vietnam … 3,500,000" — p.145 Reserves column (revised in MCS 2025) |
| reserves.reserves_by_country[VN].share_pct | 3.9 | usgs_mcs_2025_rare_earths | inferred | Computed: 3,500,000 / 90,000,000 = 3.89% ≈ 3.9%. |
| reserves.reserves_by_country[ZZ].notes "US 1,900,000" | 1900000 t REO | usgs_mcs_2025_rare_earths | verified | "United States … 1,900,000" — p.145 Reserves column (revised) |
| reserves.reserves_by_country[ZZ].notes "Greenland 1,500,000" | 1500000 t REO | usgs_mcs_2025_rare_earths | verified | "Greenland … 1,500,000" — p.145 Reserves column |
| reserves.reserves_by_country[ZZ].notes "Tanzania 890,000" | 890000 t REO | usgs_mcs_2025_rare_earths | verified | "Tanzania … 890,000" — p.145 Reserves column |
| reserves.reserves_by_country[ZZ].notes "South Africa 860,000" | 860000 t REO | usgs_mcs_2025_rare_earths | verified | "South Africa … 860,000" — p.145 Reserves column (revised) |
| reserves.reserves_by_country[ZZ].notes "Canada 830,000" | 830000 t REO | usgs_mcs_2025_rare_earths | verified | "Canada … 830,000" — p.145 Reserves column |
| reserves.reserves_by_country[ZZ].notes "Thailand 4,500" | 4500 t REO | usgs_mcs_2025_rare_earths | verified | "Thailand … 4,500" — p.145 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 5.7 | usgs_mcs_2025_rare_earths | inferred | The 5.7% corresponds to (90,000,000 − sum of top-6 countries) / 90,000,000 = 5,100,000 / 90,000,000 = 5.67%. However the listed ZZ country sum (1,900,000+1,500,000+890,000+860,000+830,000+4,500 = 5,984,500) gives 5,984,500/90,000,000 = 6.65%. Minor internal inconsistency in YAML notes (states ~5.7% but sum of listed countries implies 6.65%). Not a source discrepancy — both values are derived. |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 32 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter names bastnaesite as the primary REE ore at Mountain Pass but does not state La2O3 content percentage. The 32-34% figure for La2O3 in Mountain Pass bastnaesite is consistent with published mineralogical data but not directly in the cited source. |
| feedstock_origins[monazite_sand].typical_concentration_pct | 23 | usgs_mcs_2025_rare_earths | inferred | USGS mentions monazite as an accessory mineral and stockpiled concentrate but gives no La% content in the RE chapter. 20-25% is consistent with literature; 23% is a midpoint estimate. |
| feedstock_origins[ion_adsorption_clay].typical_concentration_pct | 10 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not specifically name ion-adsorption clays as a mineral type or give La% concentration. The 5-15% range and 10% midpoint are consistent with the mineralogical literature on Chinese HREE clay deposits. |
| prices[oxide][2024].value | 1 USD/kg | usgs_mcs_2025_rare_earths | verified | "Lanthanum oxide, 99.5% minimum … 1" — p.144 Salient Statistics, 2024e column (source footnote 6: Argus Media Group, Argus Non-Ferrous Markets) |
| prices[oxide][2023].value | 1 USD/kg | usgs_mcs_2025_rare_earths | verified | "Lanthanum oxide, 99.5% minimum … 1" — p.144 Salient Statistics, 2023 column |
| prices[oxide][2022].value | 1 USD/kg | usgs_mcs_2025_rare_earths | verified | "Lanthanum oxide, 99.5% minimum … 1" — p.144 Salient Statistics, 2022 column |
| prices[oxide][2021].value | 2 USD/kg | usgs_mcs_2025_rare_earths | verified | "Lanthanum oxide, 99.5% minimum … 2" — p.144 Salient Statistics, 2021 column |
| prices[oxide][2020].value | 2 USD/kg | usgs_mcs_2025_rare_earths | verified | "Lanthanum oxide, 99.5% minimum … 2" — p.144 Salient Statistics, 2020 column |
| prices[alloy][2024].value | 5 USD/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — p.144 Salient Statistics, 2024e column |
| prices[alloy][2023].value | 5 USD/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — p.144 Salient Statistics, 2023 column |
| prices[alloy][2022].value | 7 USD/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 7" — p.144 Salient Statistics, 2022 column |
| prices[alloy][2021].value | 6 USD/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 6" — p.144 Salient Statistics, 2021 column |
| prices[alloy][2020].value | 5 USD/kg | usgs_mcs_2025_rare_earths | verified | "Mischmetal, 65% cerium, 35% lanthanum … 5" — p.144 Salient Statistics, 2020 column |
| end_uses.uses[fcc_catalysts] (leading domestic end use) | catalysts = leading | usgs_mcs_2025_rare_earths | verified | "The estimated leading domestic end use of rare earths was catalysts." — p.144 Domestic Production and Use |
| end_uses.uses[ceramics_glass_optical] (listed end use) | ceramics and glass | usgs_mcs_2025_rare_earths | verified | "Other end uses were ceramics and glass, metallurgical applications and alloys, and polishing." — p.144 Domestic Production and Use |
| end_uses.uses[metallurgical_alloys] (listed end use) | metallurgical applications and alloys | usgs_mcs_2025_rare_earths | verified | "Other end uses were ceramics and glass, metallurgical applications and alloys, and polishing." — p.144 Domestic Production and Use |
| end_uses.uses[polishing_powders] (listed end use) | polishing | usgs_mcs_2025_rare_earths | verified | "Other end uses were ceramics and glass, metallurgical applications and alloys, and polishing." — p.144 Domestic Production and Use |
| end_uses.uses[fcc_catalysts].share_pct | 45 | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 does not provide explicit per-application La percentage breakdown. USGS states catalysts is leading end use qualitatively. The 45% estimate is analyst-derived. |
| end_uses.uses[battery_alloys_nimh].share_pct | 25 | usgs_mcs_2025_rare_earths | inferred | No explicit % in USGS MCS 2025 RE chapter. Analyst estimate based on NiMH market share context. |
| end_uses.uses[ceramics_glass_optical].share_pct | 12 | usgs_mcs_2025_rare_earths | inferred | No explicit % in source. Analyst estimate. |
| end_uses.uses[polishing_powders].share_pct | 10 | usgs_mcs_2025_rare_earths | inferred | No explicit % in source. Analyst estimate. |
| end_uses.uses[metallurgical_alloys].share_pct | 5 | usgs_mcs_2025_rare_earths | inferred | No explicit % in source. Analyst estimate. |
| end_uses.uses[other_uses].share_pct | 3 | usgs_mcs_2025_rare_earths | inferred | No explicit % in source. Residual (100-45-25-12-10-5=3%). |
| substitutes.notes "generally are less effective" | substitutes generally less effective | usgs_mcs_2025_rare_earths | verified | "Substitutes are available for many applications but generally are less effective." — p.145 Substitutes |
| criticality.us_critical_list_as_of_2025 | true | usgs_mcs_2025_rare_earths | verified | USGS MCS 2025 Table 4 (p.17) explicitly lists "Lanthanum" with footnote 2: "Included in the Rare Earths chapter." Application noted as "Batteries, catalysts, ceramics, glass, and metallurgy." 2022 Final Critical Minerals List (87 FR 10381) was operative at MCS 2025 publication. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | inferred | EU CRMA URL (eur-lex.europa.eu) blocked by AWS WAF during this verification pass. Based on Regulation (EU) 2024/1252 content: Annex I lists "light rare earth elements" (which includes La) as a Critical Raw Material. Consistent with hive-notes from prior worker w-b250b9d694b0 who confirmed La falls under light REEs in both Annexes. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | inferred | Same source access issue. Annex II of Regulation (EU) 2024/1252 lists "light rare earth elements" as Strategic Raw Materials. Inferred from prior worker confirmation; direct URL verification was not possible during this pass. |
| criticality.notes "stockpile 1,300 t La FY2024 potential acquisitions" | 1300 t | usgs_mcs_2025_rare_earths | verified | "Lanthanum … 1,300 … —" — p.145 Government Stockpile table, FY 2024 column (Potential acquisitions / Potential disposals) |
| criticality.notes "stockpile 1,100 t La FY2025 potential acquisitions" | 1100 t | usgs_mcs_2025_rare_earths | verified | "Lanthanum … 1,100 … —" — p.145 Government Stockpile table, FY 2025 column |
| criticality.notes "Ce stockpile 550 t FY2024 only" | 550 t Ce FY2024 | usgs_mcs_2025_rare_earths | verified | "Cerium … 550 … —" FY2024; "Cerium … — … —" FY2025 — p.145 Government Stockpile table |
| criticality.notes "net import reliance 80% 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | "Net import reliance … Compounds and metals … 80" — p.144 Salient Statistics, 2024e column |
| geopolitical_events[2024-01 production].event "global REE production rises to 390,000 t REO 2024e" | 390000 t REO | usgs_mcs_2025_rare_earths | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent largely owing to increased mining and processing in China, Nigeria, and Thailand." — p.145 Events, Trends, and Issues |
| geopolitical_events[2024-01 production].impact "376,000 t in 2023" | 376000 t | usgs_mcs_2025_rare_earths | verified | "World total (rounded) … 376,000" — p.145 Mine production table, 2023 column |
| geopolitical_events[2024-01 production].impact "China 255,000→270,000, +6%" | CN 255000 to 270000 / +6 pct | usgs_mcs_2025_rare_earths | verified | CN 2023=255,000, CN 2024=270,000 — p.145; increase = (270,000-255,000)/255,000 = 5.88% ≈ +6% |
| geopolitical_events[2024-01 production].impact "Nigeria 7,200→13,000, +81%" | NG 7200 to 13000 / +81 pct | usgs_mcs_2025_rare_earths | verified | NG 2023=7,200, NG 2024=13,000 — p.145; increase = (13,000-7,200)/7,200 = 80.6% ≈ +81% |
| geopolitical_events[2024-01 production].impact "Thailand 3,600→13,000, +261%" | TH 3600 to 13000 / +261 pct | usgs_mcs_2025_rare_earths | verified | TH 2023=3,600, TH 2024=13,000 — p.145; increase = (13,000-3,600)/3,600 = 261.1% ≈ +261% |
| geopolitical_events[2024-01 production].impact "Burma 43,000→31,000" | MM 43000 to 31000 | usgs_mcs_2025_rare_earths | verified | "Burma … 43,000" (2023) / "Burma … 31,000" (2024) — p.145 Mine production table |
| geopolitical_events[2024-01 production].impact "La2O3 ~113,100 t 2024e, ~109,000 t 2023" | 113100 t / 109000 t | usgs_mcs_2025_rare_earths | inferred | Derived: 390,000×0.29=113,100; 376,000×0.29=109,040≈109,000. Basket share inferred (see mine.value row). |
| geopolitical_events[2024-01 stockpile].impact "1,300 t La FY2024, 1,100 t FY2025" | 1300 t / 1100 t | usgs_mcs_2025_rare_earths | verified | Government Stockpile table — p.145 (see criticality rows above) |
| geopolitical_events[2024-01 stockpile].impact "cerium 550 t FY2024 only" | 550 t Ce FY2024 | usgs_mcs_2025_rare_earths | verified | Government Stockpile table — p.145: Cerium 550 FY2024, no FY2025 acquisition |
| geopolitical_events[2024-01 stockpile].impact "80% net import reliance 2024e" | 80 pct | usgs_mcs_2025_rare_earths | verified | "Net import reliance … 80" — p.144 Salient Statistics, 2024e column |
| geopolitical_events[2024-01 stockpile].impact "China ~91% refining" | ~91 pct refining | usgs_mcs_2025_rare_earths | inferred | USGS MCS 2025 RE chapter does not state explicit Chinese refining share. Import sources (China 70%) are US import shares, not global refining shares. 91% is a widely cited figure from DOE/IEA not verifiable from cited USGS source. |
| geopolitical_events[2022-01 price].impact "La oxide $2/kg 2020-2021, fell to $1/kg 2022, remained at $1/kg 2024e" | $2/kg 2020-21 / $1/kg 2022-2024 | usgs_mcs_2025_rare_earths | verified | Salient Statistics p.144: La oxide 99.5% = 2 (2020), 2 (2021), 1 (2022), 1 (2023), 1 (2024e) |

## Notes

**Source situation**: All claims in La.yaml cite one of two sources: `usgs_mcs_2025_rare_earths` (URL: https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf, PDF fetched and extracted with pdftotext -layout) and `eu_crma_2024` (URL: eur-lex.europa.eu, blocked by AWS WAF during this verification pass). Primary verification was conducted against the USGS MCS 2025 Rare Earths chapter (pp.144-145) with additional confirmation from the USGS MCS 2025 overview document (Table 4/5 for US Critical Minerals List).

**La criticality confirmed**: USGS MCS 2025 Table 4 explicitly lists "Lanthanum" individually (not just as part of "Rare Earths") with footnote 2 "Included in the Rare Earths chapter." Application note: "Batteries, catalysts, ceramics, glass, and metallurgy." The 2022 Critical Minerals List (87 FR 10381) was operative at MCS 2025 publication date. `us_critical_list_as_of_2025 = true` is verified.

**EU CRMA flags (inferred, not source_unreachable)**: The EUR-Lex URL for Regulation (EU) 2024/1252 returned an AWS WAF challenge page, preventing direct verification. However, prior worker w-b250b9d694b0 explicitly confirmed that the regulation lists "light rare earth elements" (including La) in both Annex I (Critical) and Annex II (Strategic). The eu_crm and eu_strategic flags are marked `inferred` — consistent with available knowledge, but not directly verified against the live URL.

**Basket share and derived values**: USGS MCS 2025 reports REE as a single grouped commodity; no per-element breakdown is published. All La-specific production tonnages (mine.value, country-level La2O3 figures) and the derived reserve figure are computed using the ~29% basket share assumption. These are marked `inferred` with low confidence per the YAML's own confidence flags.

**Mischmetal composition confirmed**: The salient statistics table explicitly prices "Mischmetal, 65% cerium, 35% lanthanum" — the 65%Ce/35%La composition stated in the YAML's price section is verified against the table column header.

**ZZ share_pct arithmetic note**: The ZZ mining share (2.5% stated in YAML) is slightly higher than the arithmetic result (8,950/390,000 = 2.295%). The YAML notes acknowledge 2.3% but use 2.5% for rounding, causing shares to sum to 101.0% instead of 100%. This is an internal YAML inconsistency, not a source discrepancy. Similarly, the ZZ reserves share_pct (5.7%) corresponds to the floor-residual method (90M − top-6 = 5.1M → 5.67%) rather than the sum of listed ZZ countries (~5.985M → 6.65%); both are inferred derivations.

**Government Stockpile footnote**: USGS p.145 notes: "Gross weight. See Appendix B for definitions." The stockpile figures (1,300 and 1,100 t La) are gross-weight acquisitions. FY2025 cerium acquisitions and all disposals are listed as "—" (zero), confirming the YAML's "cerium 550 t FY2024 only" claim.

**End-use share percentages**: USGS MCS 2025 does not provide percentage breakdowns for individual La end uses. All share_pct values (45%, 25%, 12%, 10%, 5%, 3%) are analyst estimates and are marked `inferred`. The qualitative ordering (catalysts first, then others) is confirmed by USGS text.

**No discrepancies found**: All directly verifiable numeric values in La.yaml match the USGS MCS 2025 Rare Earths chapter (pp.144-145). The YAML was evidently written by careful reading of the same source document.

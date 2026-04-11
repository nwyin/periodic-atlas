# Verification: Nd

- Element: neodymium (Nd)
- Snapshot year: 2025
- Verifier: worker-ebe13a377d25 (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 4 |
| discrepancy | 3 |
| inferred | 16 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.notes "~390 kt 2024 total REE oxide production" | 390000 t REO | inquiry_periodic_elements_2025 | verified | "Global mine production was estimated to have increased to 390,000 tons of REO equivalent" — USGS MCS 2025 rare earths chapter, Events/Trends text |
| production[0].mine.value | 75000 tonnes_per_year | inquiry_periodic_elements_2025 | inferred | USGS does not report Nd-specific production. Derived: 390,000 t total REO × ~19.2% Nd basket share = ~74,900 t ≈ 75,000 t. Nd basket share itself is inferred (see below). |
| production[0].mine.notes "Nd's ~18-20% share of the global REE basket" | 18–20 pct | inquiry_periodic_elements_2025 | inferred | USGS MCS 2025 does not give per-element basket shares. The 18-20% figure for Nd in bastnaesite-dominated REE production is consistent with published mineralogical data but no URL source was provided or accessible. |
| production[0].mining_by_country.shares[CN].share_pct | 70 | inquiry_periodic_elements_2025 | verified | USGS MCS 2025 REE: China 270,000 t (2024) / 390,000 t world total = 69.2% ≈ 70%. Source note: "14Production quota; does not include undocumented production." |
| production[0].mining_by_country.shares[US].share_pct | 12 | inquiry_periodic_elements_2025 | verified | USGS MCS 2025 REE: USA 45,000 t (2024) / 390,000 t = 11.5% ≈ 12%. |
| production[0].mining_by_country.shares[MM].share_pct | 11 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025 REE: Burma/Myanmar 31,000 t (2024) / 390,000 t = 7.9%, not 11%. YAML figure matches the 2023 ratio (43,000/376,000 = 11.4%) — appears to use prior-year data for 2024 snapshot. |
| production[0].mining_by_country.shares[AU].share_pct | 5 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025 REE: Australia 13,000 t (2024) / 390,000 t = 3.3%, not 5%. Even 2023 figure (16,000/376,000 = 4.3%) does not reach 5%. |
| production[0].mining_by_country.shares[ZZ].share_pct | 2 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025 REE: true rest-of-world (excl. CN/US/MM/AU) = Nigeria 13,000 + Thailand 13,000 + India 2,900 + Russia 2,500 + Madagascar 2,000 + Other 1,100 + Vietnam 300 + Malaysia 130 + Brazil 20 = ~34,950 t → 9.0% of 390,000, not 2%. Overcounting of MM and AU in YAML inflates those shares and correspondingly underestimates ZZ. |
| production[0].refining_by_country.shares[CN].share_pct | 91 | inquiry_periodic_elements_2025 | inferred | USGS MCS 2025 REE chapter does not state a percentage for China's REE separation/refining share. The 91% figure is widely cited from DOE Critical Materials Assessments and IEA reports but cannot be verified against the cited null-URL source. DOE CMA PDFs were not accessible during this verification pass. Treat as approximate until a primary URL source is added. |
| production[0].refining_by_country.shares[ZZ].share_pct | 9 | inquiry_periodic_elements_2025 | inferred | Residual of 100% − 91% (CN inferred); same caveat applies. |
| end_uses.uses[magnets_ndfeb_permanent].share_pct | 85 | inquiry_periodic_elements_2025 | inferred | USGS MCS 2025 REE: "The estimated leading domestic end use of rare earths was catalysts" (US domestic; all REEs). For Nd globally, NdFeB magnets are the dominant end use and the ~85% figure is broadly consistent with DOE/IEA published data, but no direct primary URL source was provided or accessible for the Nd-specific global breakdown. |
| end_uses.uses[magnets_ndfeb_permanent].notes "1-2 kg/vehicle EV traction motor" | 1–2 kg/vehicle | inquiry_periodic_elements_2025 | inferred | Source URL null. The 1-2 kg NdFeB per EV motor is a widely cited figure in DOE and IEA clean-energy mineral reports but no primary URL was accessible for verification. |
| end_uses.uses[magnets_ndfeb_permanent].notes "~600 kg/turbine wind" | ~600 kg/turbine | inquiry_periodic_elements_2025 | inferred | Source URL null. ~600 kg NdFeB per direct-drive wind turbine generator is cited in multiple DOE/IEA reports; direct-drive designs use more than geared designs. Not verifiable against cited null source. |
| end_uses.uses[metallurgical_additives].share_pct | 5 | inquiry_periodic_elements_2025 | inferred | Source URL null; USGS MCS 2025 REE chapter lists metallurgical applications as a US end use category but does not give a Nd-specific percentage. |
| end_uses.uses[catalysts].share_pct | 5 | inquiry_periodic_elements_2025 | inferred | Source URL null. Note: USGS MCS 2025 states catalysts are the leading US domestic end use for all REEs collectively; for Nd specifically, catalysts play a small role compared with magnets. The 5% Nd-to-catalysts figure is plausible but unverified. |
| end_uses.uses[other].share_pct | 5 | inquiry_periodic_elements_2025 | inferred | Residual: 100% − 85% − 5% − 5% = 5%. Source URL null. |
| feedstock_origins[bastnaesite_ore].typical_concentration_pct | 4 | inquiry_periodic_elements_2025 | inferred | Source URL null. Context is ambiguous: notes say "NdPr typically 18-22% of the REE basket in bastnaesite." If typical_concentration_pct = Nd mass fraction of raw ore (not basket share), ~4% is possible for a high-grade bastnaesite concentrate feed but low for run-of-mine ore (~8-9% TREO × 12-14% Nd share ≈ 1-1.3% Nd). Not verifiable from cited source. |
| feedstock_origins[monazite_sand].typical_concentration_pct | 18 | inquiry_periodic_elements_2025 | inferred | Source URL null. Monazite contains Nd at roughly 15-20% of total REO content; 18% is plausible and broadly consistent with published mineralogical data. USGS MCS 2025 confirms monazite as a significant Nd-bearing mineral but gives no percentage. |
| criticality.us_critical_list_as_of_2025 | true | inquiry_periodic_elements_2025 | verified | USGS MCS 2025 Table 4 ("The 2022 U.S. Critical Minerals List", p.17) explicitly lists "Neodymium" with footnote "Included in the Rare Earths chapter." 2022 list was still operative as of MCS 2025 publication (January 2025). |
| criticality.eu_crm_list_as_of_2024 | true | inquiry_periodic_elements_2025 | inferred | EU Critical Raw Materials Act (CRMA, Regulation 2024/1252) includes rare earth elements for magnets (including NdPr) as critical raw materials. Source URL is null; EU CRMA annexes were not accessible during this pass. Cobalt verification pass (worker-6598fe3b1d7b) made the same observation about EU CRM flags. |
| criticality.eu_strategic_list_as_of_2024 | true | inquiry_periodic_elements_2025 | inferred | EU CRMA Annex II (strategic raw materials) lists NdPr and other REEs for magnets as strategic. Source URL null; same caveat as eu_crm flag. Recommend adding eu_crm_act_2024 source with URL to both flags. |
| criticality.doe_short_term_criticality_rank | 2 | inquiry_periodic_elements_2025 | inferred | Source URL null. DOE Critical Materials Assessment PDFs (2020, 2023) were not accessible during this pass (all tried URLs returned 404). DOE CMAs typically rank NdPr as a top-2 short-term critical material, consistent with this claim, but the specific rank of "2" cannot be confirmed against a primary URL. |
| geopolitical_events[2025-04].event "7 REEs including Sm, Gd, Tb, Dy, Lu, Sc, Y" | Sm, Gd, Tb, Dy, Lu, Sc, Y | inquiry_periodic_elements_2025 | inferred | Source URL null. USGS MCS 2025 (January 2025) covers through 2024 and does not mention April 2025 controls. Multiple news URLs attempted during this pass returned 403/404. The April 2025 China REE export control announcement is consistent with publicly reported events, but the exact 7-element list could not be confirmed from an accessible primary source. |
| geopolitical_events[2025-10].event "5 additional elements plus processing equipment" | 5 elements + tech | inquiry_periodic_elements_2025 | source_unreachable | October 2025 is beyond the verifier's knowledge cutoff (August 2025) and beyond USGS MCS 2025 coverage. Source URL is null. Cannot verify or refute this claim from any accessible primary source. |

## Notes

**Source situation**: All claims in Nd.yaml cite `inquiry_periodic_elements_2025` (URL: null). Primary verification was conducted against USGS MCS 2025 Rare Earths chapter (pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf, extracted via pdfplumber). DOE Critical Materials Assessment PDFs (2020, 2023) were not accessible (404 on all tried URLs). EU CRMA annexes and news sources for April 2025 China export controls returned 403/404. Full MCS 2025 (pubs.usgs.gov/periodicals/mcs2025/mcs2025.pdf) was also extracted.

**Myanmar production discrepancy (key finding)**: Myanmar's mining share is given as 11% in the YAML (snapshot_year: 2025, reporting_year: 2024) but USGS MCS 2025 shows Burma 31,000 t / 390,000 t = 7.9% for 2024. Myanmar's 2023 production (43,000 t / 376,000 t = 11.4%) matches the YAML figure, suggesting the snapshot may have been written using 2023 data. Myanmar's 2024 production fell 28% year-on-year per USGS.

**Australia production discrepancy**: Australia 13,000 t / 390,000 t = 3.3% in 2024, vs. YAML's 5%. The 2023 figure (16,000/376,000 = 4.3%) also does not support 5%. Source note from USGS: Lynas Rare Earths operates at Mt Weld, WA; production fluctuates.

**ZZ rest-of-world discrepancy**: Follows from MM/AU overcounting. The true 2024 rest-of-world (Nigeria + Thailand + India + Russia + Madagascar + Others = ~35,000 t) is ~9%, not 2%.

**Missing prices section**: Nd.yaml has no `prices` section. USGS MCS 2025 Salient Statistics table provides neodymium oxide (99.5% min) prices: 2024e $56/kg, 2023 $78/kg, 2022 $134/kg, 2021 $98/kg, 2020 $49/kg. NdPr oxide pricing trends are material to supply-chain analysis; recommend adding a prices block with USGS as source.

**Missing reserves section**: Nd.yaml has no `reserves` section. USGS MCS 2025 gives world REE reserves of >90,000,000 t REO (China 44 Mt, Brazil 21 Mt, Australia 5.7 Mt, India 6.9 Mt, Russia 3.8 Mt, USA 1.9 Mt). Grouped reserves are available and should be added if the schema supports it.

**China refining 91% + 94% NdFeB**: These figures (cited in both the production section and the narrative) are qualitatively consistent with IEA and DOE secondary sources but require a primary URL citation. USGS MCS 2025 confirms China is the dominant producer/processor without giving an explicit percentage.

**Nd basket share (18-20%)**: Not given by USGS directly. Values in the literature range from 12-16% for bastnaesite (Mountain Pass) to up to 18-22% for mixed LREE-rich deposits. The YAML range of 18-20% is on the high end; applying the midpoint of 19% to 390,000 t gives 74,100 t ≈ 75,000 t, consistent with the mine.value claim.

**US end-use note**: USGS MCS 2025 says the leading US domestic end use for all REEs was catalysts (consistent with Ce/La-dominated cerium catalyst usage). For Nd specifically, NdFeB magnet manufacturing is the dominant global demand driver; the US-centric USGS statement does not contradict the 85% magnets claim for Nd.

**Geopolitical events**: Both events are post-USGS-MCS-2025 (January 2025 publication), so USGS cannot be used as a verification source. The April 2025 event is inferred from general knowledge; the October 2025 event is beyond knowledge cutoff and is source_unreachable.

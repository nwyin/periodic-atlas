# Verification: F

- Element: fluorine (F)
- Snapshot year: 2025
- Verifier: worker-8f9f2db0978f (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 2 |
| discrepancy | 3 |
| inferred | 7 |
| source_unreachable | 6 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 9500000 tonnes_per_year | inquiry_periodic_elements_2025 | verified | "world production of fluorspar was an estimated 9.5 million tons" / "World total (rounded) … 9,500" (thousand metric tons) — USGS MCS 2025 p.73 Events & Trends + World Mine Production table |
| reserves.economic_reserves.value | 320000000 tonnes | inquiry_periodic_elements_2025 | verified | "World total (rounded) … 320,000" (thousand metric tons, CaF2 basis) = 320,000,000 t — USGS MCS 2025 p.73 Reserves column |
| production[0].mining_by_country.CN.share_pct | 63 | inquiry_periodic_elements_2025 | inferred | USGS 2024: China 5,900 kt / world 9,500 kt = 62.1%; rounds to 62%, not 63%. Using 2023 data (6,000/9,530 = 63.0%) gives 63%. Value plausible but depends on reference year; cited source has url: null |
| production[0].mining_by_country.ZA.share_pct | 4 | inquiry_periodic_elements_2025 | inferred | USGS 2024: South Africa 380 kt / 9,500 kt = 4.0% — derived value matches exactly; not stated as a percentage in USGS |
| production[0].mining_by_country.ZZ.share_pct | 9 | inquiry_periodic_elements_2025 | inferred | USGS 2024 residual (all countries except CN/MX/MN/ZA) = Germany 100 + Iran 120 + Pakistan 52 + Spain 160 + Thailand 76 + Vietnam 110 + Other 170 = 788 kt; 788/9,500 = 8.3%; if computed as 9,500 − 5,900 − 1,200 − 1,200 − 380 = 820 kt, then 820/9,500 = 8.6% ≈ 9%. Approx match depending on grouping; not stated as % in USGS |
| feedstock_origins[fluorspar_ore].typical_concentration_pct | 48.7 | inquiry_periodic_elements_2025 | inferred | Chemically derived: 2 × F atomic mass / CaF2 molecular mass = 38.00/78.08 = 48.7%. Correct; consistent with USGS form_notes standard chemistry |
| criticality.us_critical_list_as_of_2025 | true | inquiry_periodic_elements_2025 | inferred | Fluorspar confirmed on USGS/DOI 2022 Final Critical Minerals List (50 mineral commodities, per Federal Register Vol. 87 No. 37). Not explicitly stated in MCS 2025 fluorspar chapter text but inclusion in MCS is the operative critical-mineral designation |
| criticality.eu_crm_list_as_of_2024 | true | inquiry_periodic_elements_2025 | inferred | Fluorspar appears on EU Commission CRM assessments in 2011, 2014, 2017, 2020, and 2023; carried forward as Annex II CRM in EU CRMA 2024 (Regulation EU 2024/1252). Not stated in USGS MCS; EUR-Lex HTML returned empty content during fetch; consistent with multiple independent sources |
| criticality.eu_strategic_list_as_of_2024 | false | inquiry_periodic_elements_2025 | inferred | Fluorspar is NOT on EU CRMA 2024 Annex I (Strategic Raw Materials); Annex I SRM list targets energy/digital-transition minerals (Li, Co, Ni, Mn, graphite, REEs, Si, etc.). Fluorspar is Annex II (CRM) only. F.yaml value false is consistent with available knowledge; EU source not directly fetched |
| production[0].mining_by_country.MX.share_pct | 16 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025: Mexico mine production 1,200 kt (2024e) / 9,500 kt world = 12.6% ≈ 13%. F.yaml value of 16% is ~3 pp high. Even using 2023 data: Mexico 1,160 kt / 9,530 kt = 12.2%. No USGS edition gives ~16% for Mexico |
| production[0].mining_by_country.MN.share_pct | 8 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025: Mongolia mine production 1,200 kt (2024e) / 9,500 kt world = 12.6% ≈ 13%. F.yaml value of 8% is ~5 pp low. Mongolia and Mexico had identical 2024 production; both should be ~12–13%, not 16%/8% |
| feedstock_origins[phosphate_rock].typical_concentration_pct | 3 | inquiry_periodic_elements_2025 | discrepancy | USGS MCS 2025 p.73 World Resources: "assuming an average fluorine content of 3.5% in the phosphate rock." F.yaml states 3%; USGS primary source states 3.5% |
| end_uses.uses[fluorochemicals].share_pct | 60 | inquiry_periodic_elements_2025 | source_unreachable | USGS MCS 2025 gives no global end-use percentage breakdown (US domestic chapter only describes HF as leading acid-grade use without %). Cited source has url: null. Value is broadly consistent with industry-wide estimates (55–65% for HF/fluorochemicals) but no primary URL citation exists |
| end_uses.uses[aluminum_smelting_flux].share_pct | 15 | inquiry_periodic_elements_2025 | source_unreachable | USGS confirms aluminum processing (AlF3, cryolite) as a key fluorspar application but provides no global percentage. Source url: null; cannot cross-check |
| end_uses.uses[steel_fluxing].share_pct | 15 | inquiry_periodic_elements_2025 | source_unreachable | USGS mentions steel fluxing as a use; no global % given. Source url: null |
| end_uses.uses[uranium_hexafluoride_enrichment].share_pct | 3 | inquiry_periodic_elements_2025 | source_unreachable | USGS references uranium processing (UF6) as a fluorspar-derived application; no % given. Source url: null |
| end_uses.uses[semiconductor_etching].share_pct | 2 | inquiry_periodic_elements_2025 | source_unreachable | Semiconductor etching (NF3, SF6, WF6) is a downstream fluorochemical use not separately broken out in USGS MCS. Source url: null |
| end_uses.uses[other].share_pct | 5 | inquiry_periodic_elements_2025 | source_unreachable | Residual; not independently verifiable. Source url: null |

## Notes

**Source access**: USGS MCS 2025 fluorspar chapter (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-fluorspar.pdf) fetched as PDF and rendered via the Read tool. Both pages (p.72 Domestic Production and Use + p.73 World Mine Production / Events) extracted in full. US Critical Minerals List verified via USGS news release. EU CRMA 2024 (EUR-Lex, Regulation EU 2024/1252) returned empty content on fetch; EU list status confirmed via historical CRM assessment records only.

**All claims cite an internal source with url: null**: F.yaml cites only `inquiry_periodic_elements_2025` (an egotheism project internal document). Because the URL is null, direct source verification is impossible. All claims have been cross-checked against USGS MCS 2025 instead.

**Mexico / Mongolia share discrepancy (significant)**: The most impactful finding. F.yaml assigns Mexico 16% and Mongolia 8%, but USGS MCS 2025 shows both at 1,200 kt in 2024 (each ~12.6%). The likely source of error is stale data: in MCS 2022 / MCS 2021 editions, Mexico was a larger producer than Mongolia (~16% vs ~8% was plausible before Mongolia's rapid ramp-up). The figures appear to be from an older USGS edition rather than MCS 2025.

**Phosphate rock fluorine content (3% vs 3.5%)**: USGS MCS 2025 states 3.5% average fluorine content in phosphate rock (World Resources note). F.yaml says 3%. This is a minor but directly verifiable discrepancy.

**China share 63% vs 62%**: With 2024 data, China's derived share is 62.1%. The 63% figure matches 2023 production data (6,000/9,530 = 63.0%). The YAML snapshot_year is 2025 (reporting 2024 data), so the correct derived share is 62%. Difference is 1 pp; marked inferred rather than discrepancy.

**Internal YAML inconsistency (elemental F fraction)**: F.yaml's production notes state "Elemental F equivalent is ~51% of this figure," but feedstock_origins correctly states 48.7% (chemically exact: 2×19/78.08 = 48.67%). The 51% figure in production notes is inconsistent with the 48.7% stated elsewhere in the same file. The 48.7% value is chemically correct; 51% appears to be a rounding or calculation error in the production note. This is not verified against a source but is internally inconsistent. (Do not edit the YAML — noted for follow-up.)

**Units confirmed CaF2 basis**: USGS MCS 2025 header states "(Data in thousand metric tons unless otherwise specified)." All production and reserve figures are fluorspar concentrate (CaF2 basis), consistent with F.yaml's form: halide notation and form_notes.

**End-uses not quantified in USGS MCS 2025**: The USGS fluorspar chapter does not publish a global end-use percentage breakdown. The US Domestic Production and Use section only gives qualitative language ("by far the leading use"). Global end-use percentages (fluorochemicals ~60%, aluminum ~15%, steel ~15%) are commonly cited in industry sources (e.g., CRU, Roskill, IEA CMO) but the cited egotheism-internal source has no URL. Recommend adding a primary source with URL (e.g., IEA CMO 2024 or CRU fluorspar report) in a follow-up.

**Geopolitical events not present in F.yaml**: USGS MCS 2025 reports two significant 2024 events: (1) China-wide safety inspections March–August 2024 idled mines and drove a 55% surge in Chinese fluorspar imports from Mongolia; (2) China eliminated its 3% import tax on low-arsenic fluorspar. These are absent from F.yaml (no geopolitical_events section). Recommend adding for completeness.

**No prices section in F.yaml**: USGS MCS 2025 reports US import prices (CIF, $/metric ton): acid grade $470e (2024), $429 (2023); metallurgical grade $400e (2024), $296 (2023). These are not present in F.yaml.

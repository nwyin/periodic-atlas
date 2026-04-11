# Verification: Tc

- Element: technetium (Tc)
- Snapshot year: 2025
- Verifier: agent worker-86ce3b67f50a
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 4 |
| discrepancy | 0 |
| inferred | 7 |
| source_unreachable | 1 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| isotope_markets[0].half_life_seconds | 21624 s | wikipedia_tc99m | verified | Wikipedia: "Half-life (t1/2): 6.0066 h" → 6.0066 × 3600 = 21623.76 ≈ 21624 s |
| isotope_markets[0].precursor (Mo-99 half-life) | 65.932 hours | wikipedia_tc99m | verified | Wikipedia decay parent entry: "99Mo (65.932 h)" |
| end_uses[0].notes (Tc-99m share of nuclear medicine) | 85 % | wikipedia_tc99m | verified | Wikipedia: "Approximately 85% of diagnostic imaging procedures in nuclear medicine use this isotope" |
| end_uses[0].notes (annual Tc-99m procedures) | 20 million/year | wikipedia_tc99m | verified | Wikipedia: "Technetium-99m is used in 20 million diagnostic nuclear medical procedures every year" |
| isotope_markets[0].producers.shares[NL].share_pct | 25 % | wikipedia_tc99m | inferred | Wikipedia confirms HFR Petten as a major Mo-99 producer but provides no percentage; YAML itself flags this as a placeholder |
| isotope_markets[0].producers.shares[BE].share_pct | 25 % | wikipedia_tc99m | inferred | Wikipedia lists BR2 Mol as a major producer but provides no percentage breakdown |
| isotope_markets[0].producers.shares[ZA].share_pct | 20 % | wikipedia_tc99m | inferred | Wikipedia lists SAFARI-1 as a producer but provides no percentage |
| isotope_markets[0].producers.shares[AU].share_pct | 15 % | wikipedia_tc99m | inferred | Wikipedia lists OPAL/ANSTO but provides no percentage; ANSTO website returned no quantitative share data |
| isotope_markets[0].producers.shares[PL].share_pct | 5 % | wikipedia_tc99m | inferred | Wikipedia lists Maria reactor but provides no percentage |
| isotope_markets[0].producers.shares[ZZ].share_pct | 10 % | wikipedia_tc99m | inferred | Rest-of-world placeholder (MPR, RA-3, LVR-15); no primary quantitative source in Wikipedia or OECD/NEA pages reached |
| end_uses[0].share_pct | 100 % | wikipedia_tc99m | inferred | Derived from Tc-99m having no known non-medical uses; Wikipedia does not state "100%" explicitly — it is a logical inference from the medical-only description |
| isotope_markets[0].notes / narrative (2024 HFR ~50 % Mo-99 shortfall, ~3 weeks) | ~50 % shortage, ~3 weeks | wikipedia_tc99m | source_unreachable | Wikipedia article has no mention of a 2024 HFR pipe-deformation event; OECD/NEA HLG-MR reports, NRG/Pallas website, and World Nuclear News returned 404 or no relevant data; no accessible primary source found |

## Notes

**Half-life arithmetic check:** YAML value 21624 s is derived from Wikipedia's authoritative 6.0066 h figure (6.0066 × 3600 = 21623.76, rounded to 21624). This is a clean rounding, not a transcription error.

**Mo-99 precursor half-life:** Wikipedia's decay-chain notation "99Mo (65.932 h)" is an exact match for the YAML claim.

**Producer shares — low confidence confirmed:** The YAML self-identifies these six shares (NL 25, BE 25, ZA 20, AU 15, PL 5, ZZ 10) as "placeholders derived from qualitative importance." The Wikipedia article (the only cited source) confirms the named reactors as significant Mo-99 producers but publishes no percentage table. OECD/NEA HLG-MR progress reports that would contain authoritative supply-share data were all unreachable (404 or non-content pages) during this verification pass. The `low` confidence tags on all producer entries are well-founded.

**Wikipedia vs. 2024 HFR incident:** The Wikipedia article for Technetium-99m (as of retrieval 2026-04-11) covers only a 2010 HFR repair event, not a 2024 pipe-deformation incident. The ~50 % / three-week shortfall claim appears in the YAML notes and narrative without a stable primary citation. Multiple attempted sources (NRG/Pallas, WNN, OECD/NEA, SNMMI) were unreachable or lacked the relevant content. This specific numeric claim should be replaced with a dated press release or NEA advisory when one becomes accessible.

**85 % / 20 million figures:** Both Wikipedia-sourced statistics in the `end_uses` notes section are directly confirmed by the cited page. These are the two most robustly sourced numeric claims in the YAML.

**Recommendation:** Replace or supplement `wikipedia_tc99m` with an OECD/NEA HLG-MR Progress Report (e.g., the 2023 edition) as the primary source for producer shares once accessible. Until then, `inferred` / `low confidence` tags are appropriate for all six share entries.

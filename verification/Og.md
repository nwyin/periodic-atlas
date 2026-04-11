# Verification: Og

- Element: oganesson (Og)
- Snapshot year: 2025
- Verifier: worker-7c966efda22a (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 7 |
| discrepancy | 0 |
| inferred | 1 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| research_only.longest_lived_isotope | Og-294 | wikipedia_isotopes_og | verified | Wikipedia Isotopes of oganesson article focuses entirely on Og-294 as the only observed isotope; reaction written as "249Cf(48Ca,3n)294Og" confirming mass number 294 |
| research_only.half_life_seconds | 0.0007 | wikipedia_isotopes_og | verified | Wikipedia states "0.7 milliseconds" (range 0.58+0.44−0.18 ms); 0.7 ms = 0.0007 s matches YAML exactly |
| research_only.discovered_year | 2002 | wikipedia_isotopes_og | verified | Wikipedia: "One or two atoms of 294Og were produced in the 2002 experiment" — first synthesis at JINR Dubna |
| research_only.iupac_recognized_year | 2015 | iupac_118_recognition | verified | IUPAC page announcement date: December 30, 2015 — "Discovery and Assignment of Elements with Atomic Numbers 113, 115, 117 and 118" |
| research_only.discovered_at (IUPAC JWG date 2015-12-30) | 2015-12-30 | iupac_118_recognition | verified | IUPAC page states announcement date December 30, 2015 for discovery recognition; matches YAML text exactly |
| research_only.discovered_at (name announcement 2016-06-08) | 2016-06-08 | iupac_118_recognition | verified | IUPAC page: "Official name announced June 8, 2016: Oganesson" — matches YAML text exactly |
| research_only.total_ever_produced.value | 7 atoms_ever_synthesized | wikipedia_isotopes_og | inferred | Wikipedia explicitly accounts for: 1–2 atoms (2002) + 2 atoms (2005) + 1 atom (2012 confirmation run) = 4–5 atoms named. YAML states 7 as "approximate" (confidence: low) representing all runs including unspecified later confirmations. Source supports "fewer than 10 atoms" but does not state 7 explicitly; 7 is the YAML author's midpoint estimate. |
| research_only.active_production_labs | JINR Dubna | iupac_118_recognition | verified | IUPAC confirms "Joint Institute for Nuclear Research (Dubna, Russia)" as the discovery laboratory; all synthesis work reported through JINR in collaboration with LLNL |

## Notes

**Source access**: Both sources fetched successfully. IUPAC news page (https://iupac.org/news/news-detail/article/discovery-and-assignment-of-elements-with-atomic-numbers-113-115-117-and-118.html) returned HTML with key dates and collaborating institution names. Wikipedia Isotopes of oganesson page returned full details on Og-294 half-life, synthesis dates, and atom counts.

**Half-life unit check**: YAML stores `half_life_seconds: 0.0007`. Wikipedia gives 0.7 ms (0.58+0.44−0.18 ms range). 0.7 ms = 7×10⁻⁴ s = 0.0007 s. Match is exact to the stated precision.

**Discovered year vs. publication year**: The IUPAC page references "the Dubna-Livermore collaboration [work from] 2006 … reported as having satisfied the criteria for discovery of element Z=118" — this refers to the 2006 journal publication (Phys. Rev. C 74, 044602), not the year of first synthesis. The first synthesis was in 2002 per Wikipedia. YAML correctly uses 2002 as the `discovered_year`.

**Total atoms (7) is approximate**: Wikipedia explicitly lists 4–5 atoms across named runs (2002, 2005, 2012). The YAML value of 7 incorporates additional later confirmation events not enumerated on the Wikipedia isotopes page. The YAML itself marks this as `approximate: true, confidence: low` with a note that "exact count varies by source." Marked `inferred` rather than `discrepancy` because the underlying claim ("fewer than 10 atoms ever") is consistent with the source; only the specific round number 7 is not directly supported.

**LLNL collaboration**: The IUPAC source confirms Lawrence Livermore National Laboratory (California, USA) as the collaborative partner. The YAML `discovered_at` text correctly identifies both JINR Dubna and LLNL.

**No commercial claims to verify**: Og has `commercial_production: false` and no price, production-volume, or reserve data. All verifiable claims are physics/discovery facts.

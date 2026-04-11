# Verification: Ne

- Element: neon (Ne)
- Snapshot year: 2025
- Verifier: worker-3cf0de0b183a (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 2 |
| discrepancy | 0 |
| inferred | 7 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 600 million_L_per_year | asianometry_neon_2022 | inferred | Asianometry article (fetched) contains no global production volume figure. YAML itself labels this "PLACEHOLDER" from a 600–800 M L/yr trade-press range. The internal inquiry_periodic_elements_2025 doc gives ~800 M L/yr. Value is order-of-magnitude only; cited source does not support the specific 600 figure. |
| production[0].mining_by_country.UA.share_pct | 50 | asianometry_neon_2022 | verified | Asianometry (March 2022): "Over 50% of the world's neon is produced in Ukraine, which houses several large air separation units." YAML uses 50 as the canonical lower bound of ">50%"; confidence=low is appropriate. inquiry_periodic_elements_2025 gives a wider "50–70%" range. |
| production[0].mining_by_country.CN.share_pct | 30 | inquiry_periodic_elements_2025 | inferred | No cited source gives a specific post-2022 percentage for China. inquiry_periodic_elements_2025 calls China "a growing supplier" after the 2022 disruption but provides no quantitative share. Asianometry (2022) describes China only as "a growing supplier" with no percentage. YAML correctly flags confidence=low and notes this as PLACEHOLDER. |
| production[0].mining_by_country.ZZ.share_pct | 20 | inquiry_periodic_elements_2025 | inferred | Residual of 100% − 50% (UA) − 30% (CN). No source cites a rest-of-world share. |
| feedstock_origins[0].typical_concentration_pct | 0.00182 | asianometry_neon_2022 | verified | Asianometry: "Neon is found naturally in the air at very low concentrations - roughly at levels of 18.2 parts per million." 18.2 ppm = 0.00182%; YAML notes give 18.18 ppm = 0.001818%. Values match within rounding. |
| end_uses.uses[duv_excimer_laser_buffer_gas].share_pct | 85 | inquiry_periodic_elements_2025 | inferred | No cited source gives an explicit 85% figure. YAML notes acknowledge: "it is not directly cited from a primary source in this file." inquiry_periodic_elements_2025 confirms neon is "essential for DUV excimer lasers that perform the majority of semiconductor lithography" but provides no end-use share breakdown. Asianometry confirms neon's central role in ArF 193 nm excimer lasers (comprising ">95% of the laser gas mix") without quantifying the share of total neon demand. |
| end_uses.uses[gas_discharge_lighting_signage].share_pct | 10 | inquiry_periodic_elements_2025 | inferred | Not cited in any accessed source. inquiry_periodic_elements_2025 does not contain end-use share breakdowns for neon. Asianometry mentions gas discharge lighting only in passing with no percentage. |
| end_uses.uses[cryogenic_refrigerants_and_other].share_pct | 5 | inquiry_periodic_elements_2025 | inferred | Not cited in any accessed source. Residual of 100% − 85% − 10%. No primary source is available; the three end-use shares together (85 + 10 + 5 = 100) are a self-consistent industry-convention estimate rather than a cited breakdown. |
| prices[0].value | 2000 usd_per_m3 | inquiry_periodic_elements_2025 | inferred | YAML labels this "PLACEHOLDER spot price." inquiry_periodic_elements_2025 states "prices spiked 5,000% when production halted" but gives no dollar figure per m3. Asianometry quotes January 2022 prices in USD per liter: baseline ~$3/liter (= ~$3,000/m3), rising to "almost $9/liter" (= ~$9,000/m3) by end of January 2022 — before the invasion. These $/liter figures are for small-quantity specialty-grade spot gas and suggest the 2022 peak price was substantially above $2,000/m3 rather than below it, though bulk contract pricing for large fabs operates on different terms. No cited source directly states the $2,000/m3 figure. |

## Notes

**Source tier**: Both cited sources are secondary. `asianometry_neon_2022` is a Substack blog post (Asianometry by Jon Y, March 2022) summarizing industry reporting; it is explicitly a secondary synthesis, not a primary data release. `inquiry_periodic_elements_2025` is an internal egotheism project document — tertiary, derived from trade press and analyst reports without individual citations for neon-specific figures. USGS does not publish a neon chapter in Mineral Commodity Summaries; no primary government data source exists for this element.

**Production volume discrepancy between sources**: The Asianometry article (asianometry_neon_2022) gives no production volume. The internal document (inquiry_periodic_elements_2025) gives ~800 M L/yr. The YAML's 600 M L/yr is the low end of a historical "600–800 M L/yr" range the YAML itself attributes to trade press without a direct citation. These three data points are mutually consistent at the order-of-magnitude level.

**Price data caveat**: Asianometry quotes January 2022 prices of $3/liter (baseline) and ~$9/liter (end of January, pre-invasion) for specialty-grade neon — equivalent to $3,000–$9,000/m3. The YAML's placeholder price of $2,000/m3 is lower than these pre-invasion spot prices from Asianometry. The discrepancy likely reflects different market segments: large-fab long-term contract prices vs. spot small-lot specialty gas. Neither source directly gives a 2022 spot price in $/m3, so the $2,000 value remains unsupported and is correctly labeled PLACEHOLDER.

**Substitutability nuance**: The YAML claims `availability: none` for neon as a DUV excimer laser buffer gas substitute. Asianometry states: "It can be replaced with helium and other noble gases but this either does not work as well or has more substantial cost issues." This is a soft discrepancy — the YAML's claim of "none" is best understood as "no practical near-term substitute without full lithography line requalification" rather than a claim that no substitute gas exists in principle. The YAML notes clarify this explicitly and are internally consistent.

**Ingas/Cryoin company names**: The geopolitical_events entry names "Ingas (Mariupol) and Cryoin (Odesa)" as the disrupted Ukrainian producers. The Asianometry article (the cited source for this event) does not mention either company by name. These names appear in the YAML narrative section without a direct citation; they are well-established in industry reporting but are not verifiable against the cited source.

**Criticality flags**: Ne.yaml marks `us_critical_list_as_of_2025: false`, `eu_crm_list_as_of_2024: false`, and `eu_strategic_list_as_of_2024: false`. Neither cited source addresses these lists. These boolean flags are noted as notable absences in the YAML criticality notes: "Neon is not on the US Critical Minerals List or the EU CRM list despite the 2022 Ukraine war supply shock." This is consistent with current knowledge (neon as an industrial gas falls under different regulatory frameworks than mineral commodities), but no cited source directly verifies the absence from these specific lists.

**Edge-case element**: Ne.yaml is explicitly designated an "edge case for no USGS chapter" element. All nine numeric claims land as inferred or verified-from-secondary-source. This is the expected outcome given the source tier available — the file correctly carries `confidence: low` on all country share claims and marks the production volume and price as PLACEHOLDER.

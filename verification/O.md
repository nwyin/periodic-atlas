# Verification: O

- Element: oxygen (O)
- Snapshot year: 2025
- Verifier: Codex agent worker-ea78b8b27b68
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 4 |
| discrepancy | 1 |
| inferred | 23 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 106.6 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel says "Total world crude steel production was 1,882.6 Mt in 2024" and lists country steel totals, but it does not publish any oxygen-production figure; 106.6 Mt is a steel-linked oxygen estimate derived in YAML notes, not a source quote. |
| production[0].refining_by_country.shares[0].share_pct | 55 | worldsteel_2024_global_steel | inferred | worldsteel lists China at "1,005.1" Mt out of world "1,882.6" Mt crude steel in 2024. The source supports China as the largest steel producer, but not a published 55% oxygen share. |
| production[0].refining_by_country.shares[0].quantity.value | 58.6 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | Source evidence is steel output, not oxygen: "China ... 1,005.1" Mt and "World ... 1,882.6" Mt. The 58.6 Mt oxygen quantity is an inferred route-weighted calculation, not stated by worldsteel. |
| production[0].refining_by_country.shares[1].share_pct | 10 | worldsteel_2024_global_steel | inferred | worldsteel gives India at "149.6" Mt in 2024. It does not provide a 10% oxygen-demand share. |
| production[0].refining_by_country.shares[1].quantity.value | 10.7 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives India at "149.6" Mt crude steel in 2024, but no oxygen quantity; 10.7 Mt is inferred from the YAML methodology. |
| production[0].refining_by_country.shares[2].share_pct | 6 | worldsteel_2024_global_steel | inferred | worldsteel gives Japan at "84.0" Mt crude steel in 2024. The source does not state a 6% oxygen share. |
| production[0].refining_by_country.shares[2].quantity.value | 6.4 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives Japan at "84.0" Mt crude steel, but no oxygen tonnage. The 6.4 Mt value is derived, not directly sourced. |
| production[0].refining_by_country.shares[3].share_pct | 5 | worldsteel_2024_global_steel | inferred | worldsteel says "Russia (e) ... 70.7" Mt in 2024. It does not publish a 5% oxygen share. |
| production[0].refining_by_country.shares[3].quantity.value | 5.3 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives Russia at "70.7" Mt crude steel, but the 5.3 Mt oxygen quantity is an inference not present in the source. |
| production[0].refining_by_country.shares[4].share_pct | 5 | worldsteel_2024_global_steel | inferred | worldsteel gives South Korea at "63.5" Mt crude steel in 2024. No 5% oxygen-share figure is published. |
| production[0].refining_by_country.shares[4].quantity.value | 5.3 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives South Korea at "63.5" Mt crude steel; the oxygen quantity "5.3" Mt is inferred and not directly stated. |
| production[0].refining_by_country.shares[5].share_pct | 3 | worldsteel_2024_global_steel | inferred | worldsteel gives Germany at "37.2" Mt crude steel in 2024. The source does not publish a 3% oxygen share. |
| production[0].refining_by_country.shares[5].quantity.value | 3.2 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives Germany at "37.2" Mt crude steel, but no oxygen tonnage. The YAML quantity is inferred. |
| production[0].refining_by_country.shares[6].share_pct | 3 | worldsteel_2024_global_steel | inferred | worldsteel gives Brazil at "33.7" Mt crude steel in 2024. It does not provide a 3% oxygen share. |
| production[0].refining_by_country.shares[6].quantity.value | 3.2 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives Brazil at "33.7" Mt crude steel; 3.2 Mt oxygen is derived, not quoted. |
| production[0].refining_by_country.shares[7].share_pct | 2 | worldsteel_2024_global_steel | inferred | worldsteel gives Iran at "31.0" Mt crude steel in 2024. No 2% oxygen share is stated. |
| production[0].refining_by_country.shares[7].quantity.value | 2.1 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel gives Iran at "31.0" Mt crude steel; the 2.1 Mt oxygen quantity is inferred from YAML methodology. |
| production[0].refining_by_country.shares[8].share_pct | 11 | worldsteel_2024_global_steel | inferred | worldsteel lists other major producers including "Türkiye 36.9", "Viet Nam (e) 22.1", "Italy 20.0", "Taiwan, China (e) 19.1", "Indonesia (e) 17.0", and "Mexico (e) 13.7" Mt. It does not publish an aggregate 11% oxygen share for a residual bucket. |
| production[0].refining_by_country.shares[8].quantity.value | 11.7 million_tonnes_per_year | worldsteel_2024_global_steel | inferred | worldsteel provides remaining steel-country totals, but no residual oxygen quantity; 11.7 Mt is an inferred catch-all value in YAML. |
| feedstock_origins[0].typical_concentration_pct | 20.95 | who_oxygen_topic_2025 | discrepancy | WHO's oxygen page says a concentrator should provide oxygen "> 82% from room air (21%)." The cited page supports about 21% oxygen in air, not the YAML's more precise 20.95%. |
| end_uses.uses[0].share_pct | 55 | iea_breakthrough_2025_steel | inferred | The IEA page says "Blast furnace-basic oxygen furnace (BF-BOF) routes make up about 70% of global steel production today." It supports steel as a dominant oxygen-using route, but not a published 55% share of total oxygen end use. |
| end_uses.uses[1].share_pct | 20 | airliquide_secunda_2018 | inferred | Air Liquide says the Secunda ASU has "5,000 tonnes of oxygen per day" and the Sasol partnership totals "greater than 45,000 tonnes per day." That supports chemicals and fuels as a major oxygen sink, but not a global 20% end-use share. |
| end_uses.uses[2].share_pct | 10 | who_oxygen_topic_2025 | inferred | WHO says oxygen is an "essential medicine" used for COVID-19, pneumonia, surgery, and trauma, but the page gives no global tonnage or market-share figure for a 10% end use. |
| end_uses.uses[3].share_pct | 15 | linde_annual_2024 | inferred | Linde describes three distribution modes, including merchant and packaged gases, with merchant deliveries from plants and packaged gases in cylinders. That supports a broad residual industrial market, but not a quantified 15% global oxygen end-use share. |
| geopolitical_events[0].date | 2021-02 | who_covid_oxygen_emergency_2021 | verified | WHO news release headline date is "25 February 2021," which matches YAML month `2021-02`. |
| geopolitical_events[0].impact | more than half a million COVID-19 patients in LMICs needed oxygen treatment every day | who_covid_oxygen_emergency_2021 | verified | WHO states: "More than half a million COVID-19 patients in LMICs estimated to need oxygen treatment every day." |
| geopolitical_events[1].date | 2024-05 | linde_h2greensteel_2024 | verified | Linde press release is dated "May 1, 2024," matching YAML month `2024-05`. |
| geopolitical_events[1].impact | up to 95% lower carbon emissions compared to traditional steelmaking | linde_h2greensteel_2024 | verified | Linde says the plant "will use the latest technology to reduce carbon emissions by up to 95% compared to traditional steelmaking." |

## Notes

Most numeric claims in `elements/O.yaml` are explicitly framed as estimates, and the cited sources generally support the underlying industrial context rather than the exact oxygen values or shares. I therefore marked the steelmaking production total, the country oxygen shares and quantities, and all end-use shares as `inferred` rather than `verified`.

The `airliquide_secunda_2018` regional URL returned `403` when opened directly via the browser tool, but the same press-release text was reachable through Air Liquide search results and a global-domain mirror with the same title and quoted figures. I used that mirrored content for evidence instead of marking the claim rows `source_unreachable`.

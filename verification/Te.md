# Verification: Te

- Element: tellurium (Te)
- Snapshot year: 2025
- Verifier: worker-be32aee10193 (automated)
- Date: 2026-04-13

## Summary

| Metric | Count |
|---|---|
| verified | 41 |
| discrepancy | 0 |
| inferred | 15 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].refined.value | 980 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 World Refinery Production and Reserves table: `"World total (rounded) ... 980 ... 35,000"` |
| production[0].refined.notes (historical feedstock share) | >90% | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 World Resources: `"More than 90% of tellurium has been produced from anode slimes"` |
| production[0].refining_by_country.shares[BG].quantity.value | 1 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Bulgaria 1 1 NA"` |
| production[0].refining_by_country.shares[BG].share_pct | 0.1 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis described in YAML: 1 / (1 + 27 + 750 + 70 + 70 + 4 + 46 + 13) = 0.10%. |
| production[0].refining_by_country.shares[CA].quantity.value | 27 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Canada e27 27 900"` |
| production[0].refining_by_country.shares[CA].share_pct | 2.75 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 27 / 981 = 2.75%. |
| production[0].refining_by_country.shares[CN].quantity.value | 750 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"China 725 750 3,100"` |
| production[0].refining_by_country.shares[CN].share_pct | 76.45 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 750 / 981 = 76.45%. |
| production[0].refining_by_country.shares[CN].notes (global output share) | approximately 75% | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179: `"China was the leading producer of refined tellurium in 2024 and accounted for approximately 75% of estimated global output"` |
| production[0].refining_by_country.shares[JP].quantity.value | 70 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Japan e65 70 NA"` |
| production[0].refining_by_country.shares[JP].share_pct | 7.14 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 70 / 981 = 7.14%. |
| production[0].refining_by_country.shares[RU].quantity.value | 70 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Russia e73 70 5,800"` |
| production[0].refining_by_country.shares[RU].share_pct | 7.14 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 70 / 981 = 7.14%. |
| production[0].refining_by_country.shares[ZA].quantity.value | 4 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"South Africa e4 4 800"` |
| production[0].refining_by_country.shares[ZA].share_pct | 0.41 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 4 / 981 = 0.41%. |
| production[0].refining_by_country.shares[SE].quantity.value | 46 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Sweden (concentrates) 36 46 740"` |
| production[0].refining_by_country.shares[SE].share_pct | 4.69 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 46 / 981 = 4.69%. |
| production[0].refining_by_country.shares[UZ].quantity.value | 13 tonnes_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Uzbekistan e13 13 NA"` |
| production[0].refining_by_country.shares[UZ].share_pct | 1.33 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the p.179 country subtotal basis 13 / 981 = 1.33%. |
| reserves.economic_reserves.value | 35000 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 World Refinery Production and Reserves table: `"World total (rounded) ... 980 35,000"` |
| reserves.reserves_by_country.shares[US].quantity.value | 3800 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"United States (copper telluride) W W 3,800"` |
| reserves.reserves_by_country.shares[US].share_pct | 10.81 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 3,800 / 35,140 = 10.81%. |
| reserves.reserves_by_country.shares[CA].quantity.value | 900 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Canada e27 27 900"` |
| reserves.reserves_by_country.shares[CA].share_pct | 2.56 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 900 / 35,140 = 2.56%. |
| reserves.reserves_by_country.shares[CN].quantity.value | 3100 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"China 725 750 3,100"` |
| reserves.reserves_by_country.shares[CN].share_pct | 8.82 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 3,100 / 35,140 = 8.82%. |
| reserves.reserves_by_country.shares[RU].quantity.value | 5800 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Russia e73 70 5,800"` |
| reserves.reserves_by_country.shares[RU].share_pct | 16.51 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 5,800 / 35,140 = 16.51%. |
| reserves.reserves_by_country.shares[ZA].quantity.value | 800 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"South Africa e4 4 800"` |
| reserves.reserves_by_country.shares[ZA].share_pct | 2.28 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 800 / 35,140 = 2.28%. |
| reserves.reserves_by_country.shares[SE].quantity.value | 740 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Sweden (concentrates) 36 46 740"` |
| reserves.reserves_by_country.shares[SE].share_pct | 2.11 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 740 / 35,140 = 2.11%. |
| reserves.reserves_by_country.shares[ZZ].quantity.value | 20000 tonnes | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 table: `"Other countries9 NA NA 20,000"` |
| reserves.reserves_by_country.shares[ZZ].share_pct | 56.92 | usgs_mcs_2025_tellurium | inferred | Not stated directly; computed from the quantified-country subtotal 20,000 / 35,140 = 56.92%. |
| end_uses.uses[solar_power_cells].share_pct | 60 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"solar power cells, 60%"` |
| end_uses.uses[thermoelectric_devices].share_pct | 20 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"thermoelectric devices, 20%"` |
| end_uses.uses[metallurgy].share_pct | 15 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"metallurgy, 15%"` |
| end_uses.uses[other_applications].share_pct | 5 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"other applications, 5%"` |
| criticality.us_critical_list_as_of_2025 | true | us_federal_register_2025_critical_minerals | verified | Federal Register notice lines 242 and 266 list tellurium among the `"final 2025 List of Critical Minerals"` and state the Secretary `"hereby includes ... tellurium"` on the final list. |
| prices[us_domestic,2024].value | 75 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"United States4 59.37 69.72 70.34 79.09 75"` |
| prices[us_domestic,2023].value | 79.09 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"United States4 59.37 69.72 70.34 79.09 75"` |
| prices[us_domestic,2022].value | 70.34 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"United States4 59.37 69.72 70.34 79.09 75"` |
| prices[us_domestic,2021].value | 69.72 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"United States4 59.37 69.72 70.34 79.09 75"` |
| prices[us_domestic,2020].value | 59.37 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"United States4 59.37 69.72 70.34 79.09 75"` |
| prices[us_domestic].notes (minimum purity) | 99.95% | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 footnote 4: `"Minimum purity of 99.95%, free on board, U.S. warehouse."` |
| prices[europe_domestic,2024].value | 80 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"Europe5 56.05 67.26 68.10 76.74 80"` |
| prices[europe_domestic,2023].value | 76.74 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"Europe5 56.05 67.26 68.10 76.74 80"` |
| prices[europe_domestic,2022].value | 68.1 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"Europe5 56.05 67.26 68.10 76.74 80"` |
| prices[europe_domestic,2021].value | 67.26 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"Europe5 56.05 67.26 68.10 76.74 80"` |
| prices[europe_domestic,2020].value | 56.05 usd_per_kg | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178 price table: `"Europe5 56.05 67.26 68.10 76.74 80"` |
| prices[europe_domestic].notes (minimum purity) | 99.99% | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.179 footnote 5: `"Minimum purity of 99.99%, in warehouse, Rotterdam."` |
| geopolitical_events[0].date | 2024 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"opened its fourth domestic manufacturing facility in 2024"` |
| geopolitical_events[0].event (facility count) | fourth U.S. module factory | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"opened its fourth domestic manufacturing facility"` |
| geopolitical_events[0].event (next plant count) | fifth plant | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"constructing a fifth plant"` |
| geopolitical_events[0].event (commissioning year) | 2025 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"projected to be commissioned in 2025"` |
| geopolitical_events[0].impact (expected capacity) | 14 gigawatts_per_year | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"production capacity in the United States to reach 14 gigawatts per year"` |
| geopolitical_events[0].impact (capacity timing) | end of 2026 | usgs_mcs_2025_tellurium | verified | USGS MCS 2025 p.178: `"by the end of 2026"` |

## Notes

The USGS Tellurium chapter PDF was reachable through the built-in web fetch path, but local `defuddle` could not resolve external hosts in this sandbox (`getaddrinfo ENOTFOUND`), so the verification relies on direct web/PDF retrieval rather than local CLI extraction.

All refinery-country `share_pct` values are inferred rather than verified because the USGS publishes country tonnages plus a rounded world total of 980 metric tons, while the named-country subtotal is 981 metric tons. The YAML explicitly uses the named-country subtotal as its denominator, and each percentage reconciles to that basis.

All reserve-country `share_pct` values are likewise inferred from the quantified-country subtotal of 35,140 metric tons rather than the rounded world total of 35,000 metric tons. The underlying country reserve quantities all match the USGS table directly.

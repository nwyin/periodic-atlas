# Verification: P

- Element: phosphorus (P)
- Snapshot year: 2025
- Verifier: worker-1810ab1fd7cd (automated)
- Date: 2026-04-11

## Summary

| Metric | Count |
|---|---|
| verified | 74 |
| discrepancy | 1 |
| inferred | 52 |
| source_unreachable | 2 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 240 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "World total (rounded) … 240,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column (data in thousand metric tons) |
| production[0].mine.notes (2023 world total) | 233,000 kt | usgs_mcs_2025_phosphate | verified | "233,000" — USGS MCS 2025 p.135 World Mine Production table, 2023 column, World total (rounded) row |
| production[0].mining_by_country[CN].quantity.value | 110 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "China … 110,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[CN].share_pct | 45.8 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 110,000/240,000 = 45.83% — rounds to 45.8% |
| production[0].mining_by_country[MA].quantity.value | 30 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Morocco … 30,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[MA].share_pct | 12.5 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 30,000/240,000 = 12.5% exactly |
| production[0].mining_by_country[US].quantity.value | 20 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "United States … 20,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column; also confirmed by narrative "estimated 20 million tons of marketable product" p.134 |
| production[0].mining_by_country[US].share_pct | 8.3 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 20,000/240,000 = 8.33% — rounds to 8.3% |
| production[0].mining_by_country[RU].quantity.value | 14 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Russia … 14,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[RU].share_pct | 5.8 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 14,000/240,000 = 5.83% — rounds to 5.8% |
| production[0].mining_by_country[JO].quantity.value | 12 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Jordan … 12,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[JO].share_pct | 5.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 12,000/240,000 = 5.00% exactly |
| production[0].mining_by_country[SA].quantity.value | 9.5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Saudi Arabia … 9,500" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[SA].share_pct | 4.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 9,500/240,000 = 3.96% — rounds to 4.0% |
| production[0].mining_by_country[BR].quantity.value | 5.3 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Brazil … 5,300" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 2.2 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 5,300/240,000 = 2.21% — rounds to 2.2% |
| production[0].mining_by_country[EG].quantity.value | 5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Egypt … 5,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[EG].share_pct | 2.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 5,000/240,000 = 2.08% — rounds to 2.1% |
| production[0].mining_by_country[PE].quantity.value | 5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Peru … 5,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[PE].share_pct | 2.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 5,000/240,000 = 2.08% — rounds to 2.1% |
| production[0].mining_by_country[TN].quantity.value | 3.3 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Tunisia … 3,300" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[TN].share_pct | 1.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 3,300/240,000 = 1.375% — rounds to 1.4% |
| production[0].mining_by_country[VN].quantity.value | 2.6 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Vietnam … 2,600" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[VN].share_pct | 1.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,600/240,000 = 1.08% — rounds to 1.1% |
| production[0].mining_by_country[AU].quantity.value | 2.5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Australia … 2,500" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 1.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,500/240,000 = 1.04% — rounds to 1.0% |
| production[0].mining_by_country[SN].quantity.value | 2.5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Senegal … 2,500" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[SN].share_pct | 1.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,500/240,000 = 1.04% — rounds to 1.0% |
| production[0].mining_by_country[IL].quantity.value | 2.3 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Israel … 2,300" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[IL].share_pct | 1.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,300/240,000 = 0.96% — rounds to 1.0% |
| production[0].mining_by_country[ZA].quantity.value | 2.2 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "South Africa … 2,200" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZA].share_pct | 0.9 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,200/240,000 = 0.92% — rounds to 0.9% |
| production[0].mining_by_country[SY].quantity.value | 2 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Syria … 2,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[SY].share_pct | 0.8 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,000/240,000 = 0.83% — rounds to 0.8% |
| production[0].mining_by_country[DZ].quantity.value | 2 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Algeria … 2,000" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[DZ].share_pct | 0.8 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,000/240,000 = 0.83% — rounds to 0.8% |
| production[0].mining_by_country[KZ].quantity.value | 1.7 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Kazakhstan … 1,700" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[KZ].share_pct | 0.7 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,700/240,000 = 0.71% — rounds to 0.7% |
| production[0].mining_by_country[IN].quantity.value | 1.6 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "India … 1,600" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[IN].share_pct | 0.7 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,600/240,000 = 0.67% — rounds to 0.7% |
| production[0].mining_by_country[TG].quantity.value | 1.5 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Togo … 1,500" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[TG].share_pct | 0.6 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,500/240,000 = 0.625% — rounds to 0.6% |
| production[0].mining_by_country[FI].quantity.value | 0.9 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Finland … 900" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[FI].share_pct | 0.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 900/240,000 = 0.375% — rounds to 0.4% |
| production[0].mining_by_country[UZ].quantity.value | 0.9 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Uzbekistan … 900" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[UZ].share_pct | 0.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 900/240,000 = 0.375% — rounds to 0.4% |
| production[0].mining_by_country[TR].quantity.value | 0.8 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Turkey … 800" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[TR].share_pct | 0.3 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 800/240,000 = 0.333% — rounds to 0.3% |
| production[0].mining_by_country[MX].quantity.value | 0.36 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Mexico … 360" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[MX].share_pct | 0.2 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 360/240,000 = 0.15% — rounds to 0.2% (YAML rounds up from 0.15%) |
| production[0].mining_by_country[ZZ].quantity.value | 0.77 million_tonnes_per_year | usgs_mcs_2025_phosphate | verified | "Other countries … 770" — USGS MCS 2025 p.135 World Mine Production table, 2024e column |
| production[0].mining_by_country[ZZ].share_pct | 0.3 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 770/240,000 = 0.321% — rounds to 0.3% |
| reserves.economic_reserves.value | 74,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "World total (rounded) … 74,000,000" — USGS MCS 2025 p.135 World Mine Production and Reserves table, Reserves column (data in thousand metric tons; ×1000 = 74,000,000,000 tonnes) |
| reserves.reserves_by_country[MA].quantity.value | 50,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Morocco … 50,000,000" — USGS MCS 2025 p.135 Reserves column (50,000,000 kt × 1000 = 50,000,000,000 tonnes) |
| reserves.reserves_by_country[MA].share_pct | 67.6 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 50,000,000/74,000,000 = 67.57% — rounds to 67.6% |
| reserves.reserves_by_country[CN].quantity.value | 3,700,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "China … 3,700,000" — USGS MCS 2025 p.135 Reserves column (3,700,000 kt × 1000 = 3,700,000,000 tonnes) |
| reserves.reserves_by_country[CN].share_pct | 5.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 3,700,000/74,000,000 = 5.00% exactly |
| reserves.reserves_by_country[EG].quantity.value | 2,800,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Egypt … 2,800,000" — USGS MCS 2025 p.135 Reserves column (2,800,000 kt × 1000 = 2,800,000,000 tonnes) |
| reserves.reserves_by_country[EG].share_pct | 3.8 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,800,000/74,000,000 = 3.78% — rounds to 3.8% |
| reserves.reserves_by_country[TN].quantity.value | 2,500,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Tunisia … 2,500,000" — USGS MCS 2025 p.135 Reserves column (2,500,000 kt × 1000 = 2,500,000,000 tonnes) |
| reserves.reserves_by_country[TN].share_pct | 3.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,500,000/74,000,000 = 3.38% — rounds to 3.4% |
| reserves.reserves_by_country[RU].quantity.value | 2,400,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Russia … 2,400,000" — USGS MCS 2025 p.135 Reserves column (2,400,000 kt × 1000 = 2,400,000,000 tonnes) |
| reserves.reserves_by_country[RU].share_pct | 3.2 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,400,000/74,000,000 = 3.24% — rounds to 3.2% |
| reserves.reserves_by_country[DZ].quantity.value | 2,200,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Algeria … 2,200,000" — USGS MCS 2025 p.135 Reserves column (2,200,000 kt × 1000 = 2,200,000,000 tonnes) |
| reserves.reserves_by_country[DZ].share_pct | 3.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 2,200,000/74,000,000 = 2.97% — rounds to 3.0% |
| reserves.reserves_by_country[BR].quantity.value | 1,600,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Brazil … 1,600,000" — USGS MCS 2025 p.135 Reserves column (1,600,000 kt × 1000 = 1,600,000,000 tonnes) |
| reserves.reserves_by_country[BR].share_pct | 2.2 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,600,000/74,000,000 = 2.16% — rounds to 2.2% |
| reserves.reserves_by_country[ZA].quantity.value | 1,500,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "South Africa … 1,500,000" — USGS MCS 2025 p.135 Reserves column (1,500,000 kt × 1000 = 1,500,000,000 tonnes) |
| reserves.reserves_by_country[ZA].share_pct | 2.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,500,000/74,000,000 = 2.03% — rounds to 2.0% |
| reserves.reserves_by_country[AU].quantity.value | 1,100,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Australia … 1,100,000" — USGS MCS 2025 p.135 Reserves column (footnote 5); USGS estimate (1,100,000 kt × 1000 = 1,100,000,000 tonnes) |
| reserves.reserves_by_country[AU].notes (JORC 120 million tons) | 120,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 120 million tons" — USGS MCS 2025 p.135 footnote 5 |
| reserves.reserves_by_country[AU].share_pct | 1.5 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,100,000/74,000,000 = 1.49% — rounds to 1.5% |
| reserves.reserves_by_country[US].quantity.value | 1,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "United States … 1,000,000" — USGS MCS 2025 p.135 Reserves column (1,000,000 kt × 1000 = 1,000,000,000 tonnes) |
| reserves.reserves_by_country[US].share_pct | 1.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,000,000/74,000,000 = 1.35% — rounds to 1.4% |
| reserves.reserves_by_country[JO].quantity.value | 1,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Jordan … 1,000,000" — USGS MCS 2025 p.135 Reserves column (1,000,000 kt × 1000 = 1,000,000,000 tonnes) |
| reserves.reserves_by_country[JO].share_pct | 1.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,000,000/74,000,000 = 1.35% — rounds to 1.4% |
| reserves.reserves_by_country[FI].quantity.value | 1,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Finland … 1,000,000" — USGS MCS 2025 p.135 Reserves column (1,000,000 kt × 1000 = 1,000,000,000 tonnes) |
| reserves.reserves_by_country[FI].share_pct | 1.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,000,000/74,000,000 = 1.35% — rounds to 1.4% |
| reserves.reserves_by_country[SA].quantity.value | 1,000,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Saudi Arabia … 1,000,000" — USGS MCS 2025 p.135 Reserves column (1,000,000 kt × 1000 = 1,000,000,000 tonnes); revised per company and Government reports |
| reserves.reserves_by_country[SA].share_pct | 1.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 1,000,000/74,000,000 = 1.35% — rounds to 1.4% |
| reserves.reserves_by_country[KZ].quantity.value | 260,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Kazakhstan … 260,000" — USGS MCS 2025 p.135 Reserves column (260,000 kt × 1000 = 260,000,000 tonnes) |
| reserves.reserves_by_country[KZ].share_pct | 0.4 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 260,000/74,000,000 = 0.351% — rounds to 0.4% |
| reserves.reserves_by_country[SY].quantity.value | 250,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Syria … 250,000" — USGS MCS 2025 p.135 Reserves column (250,000 kt × 1000 = 250,000,000 tonnes) |
| reserves.reserves_by_country[SY].share_pct | 0.3 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 250,000/74,000,000 = 0.338% — rounds to 0.3% |
| reserves.reserves_by_country[PE].quantity.value | 210,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Peru … 210,000" — USGS MCS 2025 p.135 Reserves column (210,000 kt × 1000 = 210,000,000 tonnes) |
| reserves.reserves_by_country[PE].share_pct | 0.3 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 210,000/74,000,000 = 0.284% — rounds to 0.3% |
| reserves.reserves_by_country[UZ].quantity.value | 100,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Uzbekistan … 100,000" — USGS MCS 2025 p.135 Reserves column (100,000 kt × 1000 = 100,000,000 tonnes) |
| reserves.reserves_by_country[UZ].share_pct | 0.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 100,000/74,000,000 = 0.135% — rounds to 0.1% |
| reserves.reserves_by_country[TR].quantity.value | 71,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Turkey … 71,000" — USGS MCS 2025 p.135 Reserves column (71,000 kt × 1000 = 71,000,000 tonnes) |
| reserves.reserves_by_country[TR].share_pct | 0.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 71,000/74,000,000 = 0.096% — rounds to 0.1% |
| reserves.reserves_by_country[IL].quantity.value | 60,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Israel … 60,000" — USGS MCS 2025 p.135 Reserves column (60,000 kt × 1000 = 60,000,000 tonnes) |
| reserves.reserves_by_country[IL].share_pct | 0.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 60,000/74,000,000 = 0.081% — rounds to 0.1% |
| reserves.reserves_by_country[SN].quantity.value | 50,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Senegal … 50,000" — USGS MCS 2025 p.135 Reserves column (50,000 kt × 1000 = 50,000,000 tonnes) |
| reserves.reserves_by_country[SN].share_pct | 0.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 50,000/74,000,000 = 0.068% — rounds to 0.1% |
| reserves.reserves_by_country[IN].quantity.value | 31,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "India … 31,000" — USGS MCS 2025 p.135 Reserves column (31,000 kt × 1000 = 31,000,000 tonnes) |
| reserves.reserves_by_country[IN].share_pct | 0.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 31,000/74,000,000 = 0.042% — rounds to 0.0% |
| reserves.reserves_by_country[MX].quantity.value | 30,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Mexico … 30,000" — USGS MCS 2025 p.135 Reserves column (30,000 kt × 1000 = 30,000,000 tonnes) |
| reserves.reserves_by_country[MX].share_pct | 0.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 30,000/74,000,000 = 0.041% — rounds to 0.0% |
| reserves.reserves_by_country[TG].quantity.value | 30,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Togo … 30,000" — USGS MCS 2025 p.135 Reserves column (30,000 kt × 1000 = 30,000,000 tonnes) |
| reserves.reserves_by_country[TG].share_pct | 0.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 30,000/74,000,000 = 0.041% — rounds to 0.0% |
| reserves.reserves_by_country[VN].quantity.value | 30,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Vietnam … 30,000" — USGS MCS 2025 p.135 Reserves column (30,000 kt × 1000 = 30,000,000 tonnes) |
| reserves.reserves_by_country[VN].share_pct | 0.0 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 30,000/74,000,000 = 0.041% — rounds to 0.0% |
| reserves.reserves_by_country[ZZ].quantity.value | 800,000,000 tonnes | usgs_mcs_2025_phosphate | verified | "Other countries … 800,000" — USGS MCS 2025 p.135 Reserves column (800,000 kt × 1000 = 800,000,000 tonnes) |
| reserves.reserves_by_country[ZZ].share_pct | 1.1 | usgs_mcs_2025_phosphate | inferred | Not stated explicitly; 800,000/74,000,000 = 1.08% — rounds to 1.1% |
| reserves.resources.value | 300,000,000,000,000 tonnes | usgs_mcs_2025_phosphate | discrepancy | Source says "World resources of phosphate rock are more than 300 billion tons" — 300 billion = 3×10^11 tonnes; YAML value 300,000,000,000,000 = 3×10^14 tonnes (300 trillion), off by factor of 1,000. YAML notes field correctly quotes "300 billion" but the numeric value field is 1,000× too large. |
| feedstock_origins[sedimentary_marine_phosphorite].typical_concentration_pct | 28.0 | usgs_mcs_2025_phosphate | inferred | Not explicitly stated in the 2-page USGS phosphate chapter; 28% P2O5 is a standard industry threshold for marketable product referenced in general phosphate mineralogy. |
| end_uses.uses[fertilizer_phosphoric_acid].share_pct | 95 | usgs_mcs_2025_phosphate | verified | "More than 95% of the phosphate rock mined in the United States was used to manufacture wet-process phosphoric acid and superphosphoric acid" — USGS MCS 2025 p.134 Domestic Production and Use |
| end_uses.uses[industrial_elemental_phosphorus].share_pct | 5 | usgs_mcs_2025_phosphate | inferred | Not stated; derived as 100% − >95% fertilizer. USGS: "The balance of the phosphate rock mined was for the manufacture of elemental phosphorus." No percentage given. |
| criticality.eu_crm_list_as_of_2024 | true | eu_crma_2024 | source_unreachable | EU Regulation 2024/1252 Annex II text not accessible via WebFetch — page returns empty or truncated content. Prior worker (w-5fb179e6c856) confirmed phosphate rock in Annex II Critical; consistent with publicly known EU CRM list since 2014. |
| criticality.eu_strategic_list_as_of_2024 | true | eu_crma_2024 | source_unreachable | EU Regulation 2024/1252 Annex I text not accessible via WebFetch — page returns empty or truncated content. Prior worker (w-5fb179e6c856) confirmed phosphorus in Annex I Strategic. |
| prices[2024].value | 100 usd_per_tonne | usgs_mcs_2025_phosphate | verified | "Price, average value, f.o.b. mine … 100" — USGS MCS 2025 p.134 Salient Statistics, 2024e column (dollars per metric ton) |
| prices[2023].value | 101 usd_per_tonne | usgs_mcs_2025_phosphate | verified | "Price, average value, f.o.b. mine … 101" — USGS MCS 2025 p.134 Salient Statistics, 2023 column (estimated) |
| prices[2022].value | 99 usd_per_tonne | usgs_mcs_2025_phosphate | verified | "Price, average value, f.o.b. mine … 99" — USGS MCS 2025 p.134 Salient Statistics, 2022 column (estimated) |
| prices[2021].value | 83 usd_per_tonne | usgs_mcs_2025_phosphate | verified | "Price, average value, f.o.b. mine … 83" — USGS MCS 2025 p.134 Salient Statistics, 2021 column |
| prices[2020].value | 76 usd_per_tonne | usgs_mcs_2025_phosphate | verified | "Price, average value, f.o.b. mine … 76" — USGS MCS 2025 p.134 Salient Statistics, 2020 column |
| geopolitical_events[2024-09].impact (facilities closed 2 weeks) | 2 weeks | usgs_mcs_2025_phosphate | verified | "Several facilities were closed for as much as 2 weeks" — USGS MCS 2025 p.134 Events, Trends, and Issues |
| geopolitical_events[2024-01] LFP batteries >90% in China 2024 | >90% | usgs_mcs_2025_phosphate | verified | "In 2024, more than 90% of all LFP batteries were manufactured in China" — USGS MCS 2025 p.134 Events |
| geopolitical_events[2024-01] P2O5 consumption 47.5 Mt 2024 | 47.5 million tons | usgs_mcs_2025_phosphate | verified | "World consumption of P2O5 contained in fertilizers was estimated to have been 47.5 million tons in 2024" — USGS MCS 2025 p.134 Events |
| geopolitical_events[2024-01] P2O5 consumption 45.8 Mt 2023 | 45.8 million tons | usgs_mcs_2025_phosphate | verified | "compared with 45.8 million tons in 2023" — USGS MCS 2025 p.134 Events |
| geopolitical_events[2024-01] P2O5 projected 51.8 Mt by 2028 | 51.8 million tons | usgs_mcs_2025_phosphate | verified | "World consumption of P2O5 in fertilizers was projected to increase to 51.8 million tons by 2028" — USGS MCS 2025 p.134 Events |
| geopolitical_events[2024-01] P2O5 capacity 65.0 Mt in 2024 | 65.0 million tons | usgs_mcs_2025_phosphate | verified | "Global phosphate production capacity … was projected to increase to 70.6 million tons by 2028 compared with 65.0 million tons in 2024" — USGS MCS 2025 p.135 |
| geopolitical_events[2024-01] P2O5 capacity 70.6 Mt by 2028 | 70.6 million tons | usgs_mcs_2025_phosphate | verified | "projected to increase to 70.6 million tons by 2028" — USGS MCS 2025 p.135 |
| geopolitical_events[2024-01] imports increased 35% | 35% | usgs_mcs_2025_phosphate | verified | "Imports were estimated to have increased by 35% to 3.5 million tons in 2024" — USGS MCS 2025 p.134 Events |
| geopolitical_events[2024-01] imports 3.5 million tons 2024 | 3.5 million tons | usgs_mcs_2025_phosphate | verified | "increased by 35% to 3.5 million tons in 2024" — USGS MCS 2025 p.134 Events; also Salient Stats: Imports 3,500 kt (2024e) |
| geopolitical_events[2024-01] net import reliance 13% 2024 | 13% | usgs_mcs_2025_phosphate | verified | "Net import reliance … 13" — USGS MCS 2025 p.134 Salient Statistics, 2024e column |
| geopolitical_events[2024-01] net import reliance 16% 2023 | 16% | usgs_mcs_2025_phosphate | verified | "Net import reliance … 16" — USGS MCS 2025 p.134 Salient Statistics, 2023 column |
| geopolitical_events[2024-01] Peru 98% of US imports | 98% | usgs_mcs_2025_phosphate | verified | "Peru, 98%" — USGS MCS 2025 p.134 Import Sources (2020–23) |
| geopolitical_events[2024-01] Morocco 2% of US imports | 2% | usgs_mcs_2025_phosphate | verified | "Morocco, 2%" — USGS MCS 2025 p.134 Import Sources (2020–23) |

## Notes

**Source access**: USGS MCS 2025 Phosphate Rock PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-phosphate.pdf) downloaded successfully (742,719 bytes) and rendered via `pdftotext -layout`, producing two pages (pp. 134–135). Full content confirmed accessible. All production and reserves claims trace to this single primary source.

**EU CRMA source unreachable**: EUR-Lex URL https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401252 consistently returns empty or truncated content via WebFetch — the full annex text cannot be directly verified this way. The eu_crm and eu_strategic flags are marked `source_unreachable`. However, prior worker w-5fb179e6c856 explicitly confirmed these designations via direct source access; phosphate rock has appeared on EU CRM lists since 2014 and the CRMA 2024 listing is a well-established public fact.

**Critical discrepancy — resources.value 1,000× too large**: The YAML `reserves.resources.value` is 300,000,000,000,000 (300 trillion tonnes). The USGS source states "World resources of phosphate rock are more than 300 billion tons," which equals 300,000,000,000 tonnes (300 billion). The YAML `notes` field correctly quotes the source text, but the numeric `value` field is wrong by a factor of 1,000. Corrected value should be 300,000,000,000. Do NOT edit `elements/P.yaml` during this verification pass.

**All mine production values exact**: Every country-level 2024 production figure in the YAML matches the USGS World Mine Production table exactly. The world total of 240,000 kt (240 Mt) and all 24 named country rows plus "Other countries" (770 kt) reproduce without error. Sum check: 110,000+30,000+20,000+14,000+12,000+9,500+5,300+5,000+5,000+3,300+2,600+2,500+2,500+2,300+2,200+2,000+2,000+1,700+1,600+1,500+900+900+800+360+770 = 239,230 kt; "Other countries" 770 kt brings sub-sum to match rounded world total 240,000 kt within expected rounding.

**All reserve values exact**: Every country reserve figure reproduces the USGS Reserves column exactly. The unit conversion from thousand metric tons (USGS) to tonnes (YAML) is consistent: multiply by 1,000. Morocco's 50,000,000 kt = 50,000,000,000 tonnes (50 billion), world total 74,000,000 kt = 74,000,000,000 tonnes (74 billion) — both verified.

**Australia footnote 5**: USGS footnote 5 states JORC-compliant reserves were 120 million tons. The USGS table entry of 1,100,000 kt = 1.1 billion tonnes is a USGS estimate (not JORC-compliant). The YAML correctly documents both figures in the AU reserves notes field.

**2023 production comparisons in notes**: All 25 country notes fields contain 2023 production comparison values (e.g., CN 105,000 kt, MA 33,000 kt, US 19,600 kt). Each matches the corresponding 2023 column in the USGS World Mine Production table exactly. These are not included as individual claim rows above but are fully verified from the same source.

**Prices match exactly**: The five-year US average f.o.b. mine price series ($76, $83, $99, $101, $100 for 2020–2024) matches the Salient Statistics table precisely. The 2022 and 2023 values are marked estimated (e) in both source and YAML.

**Share percentage arithmetic**: All mine share_pcts and reserve share_pcts are marked `inferred` because USGS does not explicitly state country percentage shares in the phosphate chapter. Computed values match the stated share_pcts within normal rounding. Sum of mine share_pcts: 45.8+12.5+8.3+5.8+5.0+4.0+2.2+2.1+2.1+1.4+1.1+1.0+1.0+1.0+0.8+0.9+0.8+0.7+0.7+0.6+0.4+0.4+0.3+0.2+0.3 = 99.4%. Slight shortfall is a rounding artifact (individual quantities sum to 239,230 kt vs. rounded world total 240,000 kt).

**Feedstock origins**: The USGS narrative confirms the country-level geography of sedimentary phosphorite deposits (northern Africa, Middle East, China, US) and igneous apatite deposits (Brazil, Canada, Finland, Russia, South Africa). The 28.0% typical_concentration_pct for sedimentary marine phosphorite is a standard industry threshold for marketable phosphate rock beneficiation; it is not explicitly stated in the two-page USGS chapter and is therefore marked `inferred`.

**Substitutes**: USGS states verbatim "Substitutes: There are no substitutes for phosphorus in agriculture." The YAML availability: none maps directly to this. This qualitative flag carries no numeric value but is fully verified.

**US domestic production note claims**: The USGS narrative confirms: five companies, 10 mines, four States (Florida, Idaho, North Carolina, Utah), valued at $2 billion f.o.b. mine. About 25% of wet-process phosphoric acid exported. Salient Statistics: production marketable 2024e = 20,000 kt (= 20 million tons, consistent with YAML production quantity).

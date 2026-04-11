# Verification: Sn

- Element: tin (Sn)
- Snapshot year: 2025
- Verifier: worker-fe9912f517a1 (automated)
- Date: 2026-04-12

## Summary

| Metric | Count |
|---|---|
| verified | 96 |
| discrepancy | 0 |
| inferred | 38 |
| source_unreachable | 0 |

## Claims

| Claim location | Value in YAML | Source id | Status | Evidence |
|---|---|---|---|---|
| production[0].mine.value | 300,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "World total (rounded) … 300,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (metric tons, tin content) |
| production[0].mine.notes (2023 world total = 305,000) | 305,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "World total (rounded) … 305,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mine.notes (US no mining since 1993, no smelting since 1989) | qualitative | usgs_mcs_2025_tin | verified | "Tin has not been mined or smelted in the United States since 1993 or 1989, respectively" — USGS MCS 2025 p.184 Domestic Production and Use |
| production[0].mine.notes (net import reliance 73% in 2024) | 73% | usgs_mcs_2025_tin | verified | "Net import reliance … 73" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| production[0].mine.notes (net import reliance same as 2023) | 73% | usgs_mcs_2025_tin | verified | "Net import reliance … 73" — USGS MCS 2025 p.184 Salient Statistics, 2023 column (both years = 73%) |
| production[0].mine.notes (apparent consumption 2024e = 37,000) | 37,000 tonnes | usgs_mcs_2025_tin | verified | "Consumption, apparent, refined … 37,000" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| production[0].mine.notes (US refined tin imports 2024e = 25,000) | 25,000 tonnes | usgs_mcs_2025_tin | verified | "Imports for consumption: Refined … 25,000" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| production[0].mining_by_country[CN].quantity.value | 69,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "China … 69,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e, estimated) |
| production[0].mining_by_country[CN].share_pct | 23.0 | usgs_mcs_2025_tin | inferred | Not stated; 69,000/300,000 = 23.00% exactly |
| production[0].mining_by_country[CN].notes (2023 = 70,000) | 70,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "China … 70,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[ID].quantity.value | 50,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Indonesia … 50,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[ID].share_pct | 16.7 | usgs_mcs_2025_tin | inferred | Not stated; 50,000/300,000 = 16.67% ≈ 16.7% |
| production[0].mining_by_country[ID].notes (2023 = 69,000) | 69,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Indonesia … 69,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[ID].notes (−28% decline) | −28% | usgs_mcs_2025_tin | inferred | Not stated; (50,000 − 69,000)/69,000 = −27.5% ≈ −28%; table shows both values but no % change stated |
| production[0].mining_by_country[MM].quantity.value | 34,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Burma … 34,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[MM].share_pct | 11.3 | usgs_mcs_2025_tin | inferred | Not stated; 34,000/300,000 = 11.33% ≈ 11.3% |
| production[0].mining_by_country[MM].notes (2023 = 34,000) | 34,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Burma … 34,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[PE].quantity.value | 31,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Peru … 31,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column |
| production[0].mining_by_country[PE].share_pct | 10.3 | usgs_mcs_2025_tin | inferred | Not stated; 31,000/300,000 = 10.33% ≈ 10.3% |
| production[0].mining_by_country[PE].notes (2023 = 26,200) | 26,200 tonnes_per_year | usgs_mcs_2025_tin | verified | "Peru … 26,200" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mining_by_country[PE].notes (30% of US refined tin imports 2020–23) | 30% | usgs_mcs_2025_tin | verified | "Refined tin: Peru, 30%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].mining_by_country[BR].quantity.value | 29,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Brazil … 29,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column |
| production[0].mining_by_country[BR].share_pct | 9.7 | usgs_mcs_2025_tin | inferred | Not stated; 29,000/300,000 = 9.67% ≈ 9.7% |
| production[0].mining_by_country[BR].notes (2023 = 29,300) | 29,300 tonnes_per_year | usgs_mcs_2025_tin | verified | "Brazil … 29,300" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mining_by_country[BR].notes (11% of US imports 2020–23) | 11% | usgs_mcs_2025_tin | verified | "Refined tin: … Brazil, 11%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].mining_by_country[CD].quantity.value | 25,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Congo (Kinshasa) … 25,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[CD].share_pct | 8.3 | usgs_mcs_2025_tin | inferred | Not stated; 25,000/300,000 = 8.33% ≈ 8.3% |
| production[0].mining_by_country[CD].notes (2023 = 20,000) | 20,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Congo (Kinshasa) … 20,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[CD].notes (North Kivu output 12,000→20,000 t) | 12,000–20,000 tonnes | usgs_mcs_2025_tin | verified | "Annual tin production was expected to increase to approximately 20,000 tons from the current 12,000 tons" — USGS MCS 2025 p.185 Events, Trends, and Issues |
| production[0].mining_by_country[BO].quantity.value | 21,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Bolivia … 21,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column |
| production[0].mining_by_country[BO].share_pct | 7.0 | usgs_mcs_2025_tin | inferred | Not stated; 21,000/300,000 = 7.00% exactly |
| production[0].mining_by_country[BO].notes (2023 = 18,700) | 18,700 tonnes_per_year | usgs_mcs_2025_tin | verified | "Bolivia … 18,700" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mining_by_country[BO].notes (23% of US imports 2020–23) | 23% | usgs_mcs_2025_tin | verified | "Refined tin: … Bolivia, 23%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].mining_by_country[AU].quantity.value | 9,900 tonnes_per_year | usgs_mcs_2025_tin | verified | "Australia … 9,900" — USGS MCS 2025 p.185 World Mine Production table, 2024e column |
| production[0].mining_by_country[AU].share_pct | 3.3 | usgs_mcs_2025_tin | inferred | Not stated; 9,900/300,000 = 3.30% exactly |
| production[0].mining_by_country[AU].notes (2023 = 9,850) | 9,850 tonnes_per_year | usgs_mcs_2025_tin | verified | "Australia … 9,850" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mining_by_country[AU].notes (JORC reserves = 320,000 t) | 320,000 tonnes | usgs_mcs_2025_tin | verified | "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 320,000 tons" — USGS MCS 2025 p.185 footnote 7 |
| production[0].mining_by_country[AU].notes (total reserves = 620,000 t) | 620,000 tonnes | usgs_mcs_2025_tin | verified | "Australia … 620,000" — USGS MCS 2025 p.185 Reserves column |
| production[0].mining_by_country[NG].quantity.value | 7,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Nigeria … 7,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[NG].share_pct | 2.3 | usgs_mcs_2025_tin | inferred | Not stated; 7,000/300,000 = 2.33% ≈ 2.3% |
| production[0].mining_by_country[NG].notes (2023 = 7,000) | 7,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Nigeria … 7,000" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[VN].quantity.value | 6,700 tonnes_per_year | usgs_mcs_2025_tin | verified | "Vietnam … 6,700" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[VN].share_pct | 2.2 | usgs_mcs_2025_tin | inferred | Not stated; 6,700/300,000 = 2.23% ≈ 2.2% |
| production[0].mining_by_country[VN].notes (2023 = 7,600) | 7,600 tonnes_per_year | usgs_mcs_2025_tin | verified | "Vietnam … 7,600" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[VN].notes (reserves revised) | qualitative | usgs_mcs_2025_tin | verified | "Reserves for China and Vietnam were revised based on company and Government reports" — USGS MCS 2025 p.185 World Mine Production and Reserves header note |
| production[0].mining_by_country[RW].quantity.value | 3,600 tonnes_per_year | usgs_mcs_2025_tin | verified | "Rwanda … 3,600" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[RW].share_pct | 1.2 | usgs_mcs_2025_tin | inferred | Not stated; 3,600/300,000 = 1.20% exactly |
| production[0].mining_by_country[RW].notes (2023 = 3,600) | 3,600 tonnes_per_year | usgs_mcs_2025_tin | verified | "Rwanda … 3,600" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[MY].quantity.value | 3,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Malaysia … 3,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[MY].share_pct | 1.0 | usgs_mcs_2025_tin | inferred | Not stated; 3,000/300,000 = 1.00% exactly |
| production[0].mining_by_country[MY].notes (2023 = 3,770) | 3,770 tonnes_per_year | usgs_mcs_2025_tin | verified | "Malaysia … 3,770" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].mining_by_country[RU].quantity.value | 3,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "Russia … 3,000" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[RU].share_pct | 1.0 | usgs_mcs_2025_tin | inferred | Not stated; 3,000/300,000 = 1.00% exactly |
| production[0].mining_by_country[RU].notes (2023 = 2,700) | 2,700 tonnes_per_year | usgs_mcs_2025_tin | verified | "Russia … 2,700" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[LA].quantity.value | 1,500 tonnes_per_year | usgs_mcs_2025_tin | verified | "Laos … 1,500" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[LA].share_pct | 0.5 | usgs_mcs_2025_tin | inferred | Not stated; 1,500/300,000 = 0.50% exactly |
| production[0].mining_by_country[LA].notes (2023 = 1,700) | 1,700 tonnes_per_year | usgs_mcs_2025_tin | verified | "Laos … 1,700" — USGS MCS 2025 p.185 World Mine Production table, 2023 column (marked e) |
| production[0].mining_by_country[ZZ].quantity.value | 1,800 tonnes_per_year | usgs_mcs_2025_tin | verified | "Other countries … 1,800" — USGS MCS 2025 p.185 World Mine Production table, 2024e column (marked e) |
| production[0].mining_by_country[ZZ].share_pct | 0.6 | usgs_mcs_2025_tin | inferred | Not stated; 1,800/300,000 = 0.60% exactly |
| production[0].mining_by_country[ZZ].notes (2023 = 1,840) | 1,840 tonnes_per_year | usgs_mcs_2025_tin | verified | "Other countries … 1,840" — USGS MCS 2025 p.185 World Mine Production table, 2023 column |
| production[0].notes (country sum = 295,500 vs 300,000) | 295,500 tonnes | usgs_mcs_2025_tin | inferred | Not stated; 69,000+50,000+34,000+31,000+29,000+25,000+21,000+9,900+7,000+6,700+3,600+3,000+3,000+1,500+1,800 = 295,500; world total stated as 300,000 |
| production[0].notes (US import sources Peru 30%) | 30% | usgs_mcs_2025_tin | verified | "Refined tin: Peru, 30%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].notes (US import sources Bolivia 23%) | 23% | usgs_mcs_2025_tin | verified | "Bolivia, 23%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].notes (US import sources Indonesia 20%) | 20% | usgs_mcs_2025_tin | verified | "Indonesia, 20%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| production[0].notes (US import sources Brazil 11%) | 11% | usgs_mcs_2025_tin | verified | "Brazil, 11%" — USGS MCS 2025 p.184 Import Sources (2020–23) |
| reserves.economic_reserves.value | 4,200,000 tonnes | usgs_mcs_2025_tin | verified | "World total (rounded) … >4,200,000" — USGS MCS 2025 p.185 Reserves column (minimum value; stored with approximate: true) |
| reserves.resources.notes (world resources extensive) | qualitative | usgs_mcs_2025_tin | verified | "World resources … are extensive and, if developed, could sustain recent annual production rates well into the future" — USGS MCS 2025 p.185 World Resources |
| reserves.resources.notes (principally western Africa, SE Asia, Australia, Bolivia, Brazil, Indonesia, Russia) | qualitative | usgs_mcs_2025_tin | verified | "World resources, principally in western Africa, southeastern Asia, Australia, Bolivia, Brazil, Indonesia, and Russia" — USGS MCS 2025 p.185 World Resources |
| reserves.resources.notes (US primarily Alaska, insignificant) | qualitative | usgs_mcs_2025_tin | verified | "Identified resources of tin in the United States, primarily in Alaska, were insignificant compared with those in the rest of the world" — USGS MCS 2025 p.185 World Resources |
| reserves.notes (Indonesia, Laos, Malaysia, Nigeria, Rwanda = NA) | NA | usgs_mcs_2025_tin | verified | "Indonesia … NA; Laos … NA; Malaysia … NA; Nigeria … NA; Rwanda … NA" — USGS MCS 2025 p.185 Reserves column |
| reserves.notes (CN reserves revised) | qualitative | usgs_mcs_2025_tin | verified | "Reserves for China and Vietnam were revised based on company and Government reports" — USGS MCS 2025 p.185 World Mine Production and Reserves header note |
| reserves.notes (quantified reserves sum = 4,183,000) | 4,183,000 tonnes | usgs_mcs_2025_tin | inferred | Not stated; 1,000,000+700,000+620,000+420,000+400,000+460,000+130,000+120,000+23,000+310,000 = 4,183,000 |
| reserves.reserves_by_country[CN].quantity.value | 1,000,000 tonnes | usgs_mcs_2025_tin | verified | "China … 1,000,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[CN].share_pct | 23.8 | usgs_mcs_2025_tin | inferred | Not stated; 1,000,000/4,200,000 = 23.81% ≈ 23.8% |
| reserves.reserves_by_country[MM].quantity.value | 700,000 tonnes | usgs_mcs_2025_tin | verified | "Burma … 700,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[MM].share_pct | 16.7 | usgs_mcs_2025_tin | inferred | Not stated; 700,000/4,200,000 = 16.67% ≈ 16.7% |
| reserves.reserves_by_country[AU].quantity.value | 620,000 tonnes | usgs_mcs_2025_tin | verified | "Australia … 620,000" — USGS MCS 2025 p.185 Reserves column; footnote 7: JORC subset = 320,000 t |
| reserves.reserves_by_country[AU].share_pct | 14.8 | usgs_mcs_2025_tin | inferred | Not stated; 620,000/4,200,000 = 14.76% ≈ 14.8% |
| reserves.reserves_by_country[BR].quantity.value | 420,000 tonnes | usgs_mcs_2025_tin | verified | "Brazil … 420,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[BR].share_pct | 10.0 | usgs_mcs_2025_tin | inferred | Not stated; 420,000/4,200,000 = 10.00% exactly |
| reserves.reserves_by_country[RU].quantity.value | 460,000 tonnes | usgs_mcs_2025_tin | verified | "Russia … 460,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[RU].share_pct | 11.0 | usgs_mcs_2025_tin | inferred | Not stated; 460,000/4,200,000 = 10.95% ≈ 11.0% |
| reserves.reserves_by_country[BO].quantity.value | 400,000 tonnes | usgs_mcs_2025_tin | verified | "Bolivia … 400,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[BO].share_pct | 9.5 | usgs_mcs_2025_tin | inferred | Not stated; 400,000/4,200,000 = 9.52% ≈ 9.5% |
| reserves.reserves_by_country[PE].quantity.value | 130,000 tonnes | usgs_mcs_2025_tin | verified | "Peru … 130,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[PE].share_pct | 3.1 | usgs_mcs_2025_tin | inferred | Not stated; 130,000/4,200,000 = 3.095% ≈ 3.1% |
| reserves.reserves_by_country[CD].quantity.value | 120,000 tonnes | usgs_mcs_2025_tin | verified | "Congo (Kinshasa) … 120,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[CD].share_pct | 2.9 | usgs_mcs_2025_tin | inferred | Not stated; 120,000/4,200,000 = 2.857% ≈ 2.9% |
| reserves.reserves_by_country[VN].quantity.value | 23,000 tonnes | usgs_mcs_2025_tin | verified | "Vietnam … 23,000" — USGS MCS 2025 p.185 Reserves column; note: revised per company/Govt reports |
| reserves.reserves_by_country[VN].share_pct | 0.5 | usgs_mcs_2025_tin | inferred | Not stated; 23,000/4,200,000 = 0.548% ≈ 0.5% |
| reserves.reserves_by_country[ZZ].quantity.value | 310,000 tonnes | usgs_mcs_2025_tin | verified | "Other countries … 310,000" — USGS MCS 2025 p.185 Reserves column |
| reserves.reserves_by_country[ZZ].share_pct | 7.4 | usgs_mcs_2025_tin | inferred | Not stated; 310,000/4,200,000 = 7.381% ≈ 7.4% |
| end_uses.uses[tinplate_cans_containers].share_pct | 23 | usgs_mcs_2025_tin | verified | "tinplate, 23%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[tin_chemicals].share_pct | 22 | usgs_mcs_2025_tin | verified | "chemicals, 22%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[solder].share_pct | 11 | usgs_mcs_2025_tin | verified | "solder, 11%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[alloys_other].share_pct | 10 | usgs_mcs_2025_tin | verified | "alloys, 10%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[babbitt_brass_bronze_tinning].share_pct | 6 | usgs_mcs_2025_tin | verified | "babbitt, brass and bronze, and tinning, 6%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[bar_tin].share_pct | 2 | usgs_mcs_2025_tin | verified | "bar tin, 2%" — USGS MCS 2025 p.184 Domestic Production and Use |
| end_uses.uses[other_uses].share_pct | 26 | usgs_mcs_2025_tin | verified | "other, 26%" — USGS MCS 2025 p.184 Domestic Production and Use |
| criticality.us_critical_list_as_of_2025 | true | usgs_2022_critical_minerals_list | verified | Tin appears on "2022 Final List of Critical Minerals" (Federal Register Vol. 87, No. 37, February 22, 2022); confirmed via USGS news release listing all 50 minerals including Tin |
| criticality.notes (US no smelting since 1989, no mining since 1993) | qualitative | usgs_mcs_2025_tin | verified | "Tin has not been mined or smelted in the United States since 1993 or 1989, respectively" — USGS MCS 2025 p.184 Domestic Production and Use |
| criticality.notes (net import reliance 73% refined 2024) | 73% | usgs_mcs_2025_tin | verified | "Net import reliance … 73" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| criticality.eu_crm_list_as_of_2024 | false | usgs_mcs_2025_tin | inferred | USGS MCS 2025 tin chapter contains no mention of EU Critical Raw Materials listing; unlike manganese or cobalt chapters, no EU CRM designation is noted. Consistent with EU Regulation (EU) 2024/1252 not including tin, but not directly stated. |
| criticality.eu_strategic_list_as_of_2024 | false | usgs_mcs_2025_tin | inferred | Same basis as eu_crm_list: absence of any EU strategic designation in the USGS chapter; not explicitly confirmed from EU regulatory text |
| prices[2024].value | 30,865 usd_per_tonne | usgs_mcs_2025_tin | inferred | Not stated; 1,400 c/lb × 22.0462 = $30,864.68/t ≈ $30,865/t; conversion factor derived from 2,204.623 lb/tonne ÷ 100 c/USD |
| prices[2024].notes (LME cash 2024e = 1,400 c/lb) | 1,400 c/lb | usgs_mcs_2025_tin | verified | "London Metal Exchange (LME), cash … 1,400" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| prices[2024].notes (LME +19% vs 2023) | 19% | usgs_mcs_2025_tin | verified | "The estimated annual average LME cash price for refined tin in 2024 was 1,400 cents per pound, a 19% increase compared with that in 2023" — USGS MCS 2025 p.185 Events, Trends, and Issues |
| prices[2024].notes (NY dealer 2024e = 1,400 c/lb) | 1,400 c/lb | usgs_mcs_2025_tin | verified | "New York dealer … 1,400" — USGS MCS 2025 p.184 Salient Statistics, 2024e column |
| prices[2024].notes (NY dealer +11% vs 2023) | 11% | usgs_mcs_2025_tin | verified | "The estimated annual average New York dealer price for refined tin in 2024 was 1,400 cents per pound, an 11% increase compared with that in 2023" — USGS MCS 2025 p.185 Events, Trends, and Issues |
| prices[2024].notes (Source: S&P Global Platts Metals Week) | source | usgs_mcs_2025_tin | verified | "Source: S&P Global Platts Metals Week" — USGS MCS 2025 p.184 footnote 3 |
| prices[2023].value | 25,948 usd_per_tonne | usgs_mcs_2025_tin | inferred | Not stated; 1,177 c/lb × 22.0462 = $25,948.4/t ≈ $25,948/t |
| prices[2023].notes (LME cash 2023 = 1,177 c/lb) | 1,177 c/lb | usgs_mcs_2025_tin | verified | "London Metal Exchange (LME), cash … 1,177" — USGS MCS 2025 p.184 Salient Statistics, 2023 column |
| prices[2023].notes (NY dealer 2023 = 1,256 c/lb) | 1,256 c/lb | usgs_mcs_2025_tin | verified | "New York dealer … 1,256" — USGS MCS 2025 p.184 Salient Statistics, 2023 column |
| prices[2022].value | 31,372 usd_per_tonne | usgs_mcs_2025_tin | inferred | Not stated; 1,423 c/lb × 22.0462 = $31,371.8/t ≈ $31,372/t |
| prices[2022].notes (LME cash 2022 = 1,423 c/lb) | 1,423 c/lb | usgs_mcs_2025_tin | verified | "London Metal Exchange (LME), cash … 1,423" — USGS MCS 2025 p.184 Salient Statistics, 2022 column |
| prices[2022].notes (NY dealer 2022 = 1,546 c/lb) | 1,546 c/lb | usgs_mcs_2025_tin | verified | "New York dealer … 1,546" — USGS MCS 2025 p.184 Salient Statistics, 2022 column |
| prices[2021].value | 32,584 usd_per_tonne | usgs_mcs_2025_tin | inferred | Not stated; 1,478 c/lb × 22.0462 = $32,584.3/t ≈ $32,584/t |
| prices[2021].notes (LME cash 2021 = 1,478 c/lb) | 1,478 c/lb | usgs_mcs_2025_tin | verified | "London Metal Exchange (LME), cash … 1,478" — USGS MCS 2025 p.184 Salient Statistics, 2021 column |
| prices[2021].notes (NY dealer 2021 = 1,580 c/lb) | 1,580 c/lb | usgs_mcs_2025_tin | verified | "New York dealer … 1,580" — USGS MCS 2025 p.184 Salient Statistics, 2021 column |
| prices[2020].value | 17,130 usd_per_tonne | usgs_mcs_2025_tin | inferred | Not stated; 777 c/lb × 22.0462 = $17,129.9/t ≈ $17,130/t |
| prices[2020].notes (LME cash 2020 = 777 c/lb) | 777 c/lb | usgs_mcs_2025_tin | verified | "London Metal Exchange (LME), cash … 777" — USGS MCS 2025 p.184 Salient Statistics, 2020 column |
| prices[2020].notes (NY dealer 2020 = 799 c/lb) | 799 c/lb | usgs_mcs_2025_tin | verified | "New York dealer … 799" — USGS MCS 2025 p.184 Salient Statistics, 2020 column |
| geopolitical_events[2024-09 DoD].event ($19M DPA Title III, Coatesville PA) | $19 million | usgs_mcs_2025_tin | verified | "In September 2024, $19 million was awarded by the U.S. Department of Defense under the Defense Production Act, Title III, to establish a tin smelting, refining, and recycling facility in Coatesville, PA" — USGS MCS 2025 p.185 Events, Trends, and Issues |
| geopolitical_events[2024-09 CN+ID].event (strategic partnership, scope) | qualitative | usgs_mcs_2025_tin | verified | "In September, two state-owned leading refined-tin producers from China and Indonesia entered into a strategic partnership to collaborate in mining, smelting and refining, trading, and downstream product development" — USGS MCS 2025 p.185 Events, Trends, and Issues |
| geopolitical_events[2024-05 DRC].event (Mauritius company, North Kivu, 12,000→20,000 t) | 12,000–20,000 tonnes | usgs_mcs_2025_tin | verified | "In May, a Mauritius-based company announced that it began production at its new processing plant in North Kivu Province, Congo (Kinshasa). Annual tin production was expected to increase to approximately 20,000 tons from the current 12,000 tons" — USGS MCS 2025 p.185 Events |
| geopolitical_events[2024-04 Uganda].event (Mbarara refinery, ~1,000 t/yr, >99%) | ~1,000 tonnes_per_year | usgs_mcs_2025_tin | verified | "In April, a Uganda-based tin-mining company commissioned a tin refinery in Mbarara, Uganda. The refinery was expected to produce approximately 1,000 tons per year of more-than-99%-pure tin ingots" — USGS MCS 2025 p.185 Events |
| geopolitical_events[2024-01 antidumping].event (Canada, China, Germany, Korea) | qualitative | usgs_mcs_2025_tin | verified | "the United States Department of Commerce proposed antidumping and countervailing duties on tin mill product imports from Canada, China, Germany, and the Republic of Korea" — USGS MCS 2025 p.185 Events |
| geopolitical_events[2024-01 antidumping].event (ITC no injury, duties not implemented) | qualitative | usgs_mcs_2025_tin | verified | "the U.S. International Trade Commission concluded that these imports did not materially injure the domestic tin mill products industry; therefore, the duties were not implemented" — USGS MCS 2025 p.185 Events |
| geopolitical_events[2024-01 antidumping].date | 2024-01 | usgs_mcs_2025_tin | inferred | Source only says "In 2024"; specific month (January) not stated in USGS chapter |
| substitutes[cans_containers] (aluminum, glass, paper, plastic, tin-free steel) | qualitative | usgs_mcs_2025_tin | verified | "Aluminum, glass, paper, plastic, or tin-free steel substitute for tin in cans and containers" — USGS MCS 2025 p.185 Substitutes |
| substitutes[solder] (epoxy resins) | qualitative | usgs_mcs_2025_tin | verified | "epoxy resins for solder" — USGS MCS 2025 p.185 Substitutes |
| substitutes[bronze_copper_alloys] (aluminum alloys, copper-base alloys, plastics) | qualitative | usgs_mcs_2025_tin | verified | "aluminum alloys, alternative copper-base alloys, and plastics for bronze" — USGS MCS 2025 p.185 Substitutes |
| substitutes[bearing_metals] (plastics) | qualitative | usgs_mcs_2025_tin | verified | "plastics for bearing metals that contain tin" — USGS MCS 2025 p.185 Substitutes |
| substitutes[tin_chemicals] (lead and sodium compounds) | qualitative | usgs_mcs_2025_tin | verified | "compounds of lead and sodium for some tin chemicals" — USGS MCS 2025 p.185 Substitutes |
| feedstock_origins[cassiterite].notes | qualitative | usgs_mcs_2025_tin | inferred | USGS MCS 2025 tin chapter does not explicitly describe cassiterite as ore mineral; inferred from standard mineralogical knowledge and general context of chapter (country list aligns with known cassiterite provinces) |
| feedstock_origins[stannite_polymetallic_ores].notes | qualitative | usgs_mcs_2025_tin | inferred | USGS MCS 2025 tin chapter does not describe stannite ores; Bolivia's polymetallic vein context is consistent with the chapter but not explicitly stated |

## Notes

**Source access**: USGS MCS 2025 Tin PDF (https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-tin.pdf) downloaded (752.8 KB binary) and extracted via `pdftotext -layout`. Both pages (pp. 184–185) fully readable. Federal Register 2022 Critical Minerals List confirmed via USGS news release (USGS press page listing all 50 critical minerals including tin). All primary numeric claims trace to a single USGS source.

**Zero discrepancies**: All 15 country mine production quantities match the USGS World Mine Production table exactly (2024e column). All 10 quantified country reserve values match the Reserves column exactly. All 5 LME cash price values and 5 NY dealer price values match the Salient Statistics table exactly. All 7 end-use percentages match the Domestic Production and Use paragraph exactly. No numeric discrepancy found in any claim.

**Production unit**: USGS MCS 2025 tin chapter header states "(Data in metric tons, tin content, unless otherwise specified)." All mine production values are in metric tons of tin content. The YAML stores these directly in tonnes (no unit conversion needed, unlike the Mn chapter which uses kt).

**Country sum vs. world total**: The sum of all 15 named-country rows plus Other countries (ZZ) = 295,500 metric tons, against a rounded world total of 300,000 metric tons — a 4,500 t (1.5%) gap attributable to rounding of individually estimated country values. This is consistent with the prior hive note [gotcha] from worker-d58ea70af12d. Share percentages are correctly computed with denominator = 300,000.

**Price conversion**: All USD/tonne values are computed from c/lb using the standard conversion factor 22.0462 (= 2,204.623 lb/tonne ÷ 100). The YAML's `form_notes` documents this conversion. All five conversions (2020–2024) produce values matching the YAML to the nearest dollar: 1,400 × 22.0462 = $30,864.68 (YAML: $30,865); 1,177 × 22.0462 = $25,948.4 (YAML: $25,948); 1,423 × 22.0462 = $31,371.8 (YAML: $31,372); 1,478 × 22.0462 = $32,584.3 (YAML: $32,584); 777 × 22.0462 = $17,129.9 (YAML: $17,130). All marked inferred; the c/lb source values are verified.

**All share_pcts inferred**: USGS does not publish percentage shares for country rows. All mine production share_pcts are quantity/300,000 and all reserve share_pcts are quantity/4,200,000. All calculations are arithmetically correct.

**Reserves denominator**: YAML uses 4,200,000 as denominator for share_pct calculations, matching the stated world total (">4,200,000"). The sum of quantified country reserves = 4,183,000 metric tons, which is 17,000 t below the stated minimum. The ">" qualifier implies additional reserves exist in NA-listed countries (Indonesia, Laos, Malaysia, Nigeria, Rwanda), making the stated world minimum consistent with the sum.

**Antidumping event month**: The YAML gives `date: 2024-01` for the antidumping/countervailing duties event. The USGS chapter only says "In 2024"; no specific month is mentioned. The January date is marked as inferred; it may reflect when the Commerce investigation was formally initiated, but this is not verifiable from the USGS chapter alone.

**Criticality**: The US criticality flag (true) is confirmed via the USGS news release listing 50 critical minerals including tin. The EU flags (false for both CRM and Strategic) are marked inferred — the USGS chapter contains no EU CRM or Strategic designation for tin, consistent with the EU CRM Act (Regulation (EU) 2024/1252) not listing tin, but the absence-of-mention in the USGS chapter cannot alone confirm the EU regulatory status.

**Feedstock origins**: Neither cassiterite nor stannite is mentioned by name in the USGS MCS 2025 tin chapter text. These descriptions represent standard mineralogical knowledge about tin ore types applied to the producing-country context. Marked inferred; they are not contradicted by anything in the chapter.

**Recycling data** (in narrative, not in structured YAML fields): The USGS chapter states "About 18,000 tons of tin from old and new scrap was estimated to have been recycled in 2024 … accounting for 27% of apparent consumption." These values appear in the YAML narrative only, which has no source_id tags; they are not included in the Claims table but are confirmed by the source (Salient Statistics: old scrap 10,000 + new scrap 7,900 = 17,900 ≈ 18,000).

**Australia JORC footnote**: Footnote 7 of USGS MCS 2025 tin explicitly states "For Australia, Joint Ore Reserves Committee-compliant or equivalent reserves were 320,000 tons." This value appears in both the AU mining_by_country.notes (row 37) and the reserves_by_country[AU].notes (row 74) and is verified in both locations.

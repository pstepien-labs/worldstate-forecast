# Stage 06 — Aggregation (edition 01, state 23.09.2026)

Input: `registry/questions.csv` (73 ACTIVE questions), `registry/forecasts.csv` (runs A, B, C from edition 01), `05_red_team.md` §3.
Completeness check: all 73 active questions have a forecast from each of the three lenses — aggregation permitted.

Recording convention: AGG = arithmetic mean of A, B, C, recorded to 0.001 (no additional rounding). AGG_RT = AGG + accepted adjustment (exact, 0.001), clipped to 0.01–0.99; without an adjustment AGG_RT = AGG. The values in table 05 §3 (e.g. 0.94 for Q-0013) are presentational roundings of the same numbers. Analytic confidence of AGG and AGG_RT = median of the three lenses' confidence.

## 1. Red-team adjustments — decisions

Acceptance criteria (methodology §5, prompt 06 step 1.2): |adjustment| ≤ 0.15 and specific evidence or an identified logical error.

| ID | AGG | adjustment | AGG_RT | type (05) | decision | basis |
|---|---|---|---|---|---|---|
| Q-0054 | 0.820 | +0.12 | 0.940 | evidence | ACCEPTED | SR result rose with the count (4.96% → 5.00%); Meduza report of 22.09 on added votes; B did not know C-01 |
| Q-0013 | 0.843 | +0.10 | 0.943 | logic + evidence | ACCEPTED | CPI base IX 2025 = 0.0% m/m (GUS); the lenses' own arithmetic gives approx. 4.2–4.4% y/y |
| Q-0040 | 0.567 | +0.10 | 0.667 | evidence | ACCEPTED | documented reference class (3 of 3 winters with an incident and an investigation); A without an argument for NO |
| Q-0062 | 0.433 | +0.08 | 0.513 | logic | ACCEPTED | a collection gap (03 §1.7 item 10) treated by the lenses as absence of events; VII–VIII pace |
| Q-0003 | 0.333 | +0.07 | 0.403 | evidence + consistency | ACCEPTED | G1-031: §1249 is a certification procedure; inconsistency with ACH-3 (03) |
| Q-0050 | 0.333 | +0.05 | 0.383 | evidence | ACCEPTED | quotation of 23.09: 8.99 PLN/l (C-04) against the starting 8.89 PLN/l in A and B |
| Q-0002 | 0.050 | +0.01 | 0.060 | logic | ACCEPTED | double counting of the same evidence in lens B |
| Q-0031 | 0.157 | −0.05 | 0.107 | logic | ACCEPTED | the C rationale points to a lower p than the one given |
| Q-0039 | 0.217 | −0.07 | 0.147 | evidence | ACCEPTED | ACP data (tightening from 01.10), rainfall −34%, El Niño; A without data |

**Rejected adjustments: none.** None of the 9 proposals exceeds ±0.15 and each has identified evidence or a logical error. Questions that the red team considered and itself rejected (Q-0004, Q-0016, Q-0067, Q-0070, Q-0055, Q-0060, Q-0008) have AGG_RT = AGG.

Note on the record: accepting an adjustment does not mean the evidence was verified in stage 06 — the stage checks the formal requirements (limit, presence of evidence or an error). The Q-0054 adjustment rests partly on the value of 5.13% (C-01), which the red team did not confirm; the direction of the adjustment is supported by the confirmed 5.00% at 96.95% of protocols.

## 2. Table of AGG and AGG_RT (73 questions)

| ID | vector | cluster | A | B | C | spread | AGG | RT adjustment | AGG_RT | confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | MIL | RU_MOBILIZATION | 0.03 | 0.03 | 0.03 | 0.00 | 0.030 | — | **0.030** | medium |
| Q-0002 | MIL | EASTERN_FLANK | 0.05 | 0.05 | 0.05 | 0.00 | 0.050 | +0.01 | **0.060** | medium |
| Q-0003 | MIL | US_EUROPE | 0.35 | 0.35 | 0.30 | 0.05 | 0.333 | +0.07 | **0.403** | low |
| Q-0004 | MIL | UA_FRONT | 0.18 | 0.15 | 0.35 | 0.20 | 0.227 | — | **0.227** | medium |
| Q-0005 | MIL | TAIWAN | 0.25 | 0.35 | 0.40 | 0.15 | 0.333 | — | **0.333** | low |
| Q-0006 | ENE | OIL_PRICE | 0.35 | 0.45 | 0.40 | 0.10 | 0.400 | — | **0.400** | medium |
| Q-0007 | ENE | OIL_PRICE | 0.12 | 0.25 | 0.20 | 0.13 | 0.190 | — | **0.190** | low |
| Q-0008 | ENE | OIL_PRICE | 0.15 | 0.30 | 0.15 | 0.15 | 0.200 | — | **0.200** | low |
| Q-0009 | ENE | EU_ENERGY | 0.25 | 0.35 | 0.30 | 0.10 | 0.300 | — | **0.300** | low |
| Q-0010 | ENE | EU_ENERGY | 0.40 | 0.25 | 0.40 | 0.15 | 0.350 | — | **0.350** | low |
| Q-0011 | ECO | US_CHINA_TRADE | 0.72 | 0.75 | 0.78 | 0.06 | 0.750 | — | **0.750** | medium |
| Q-0012 | ECO | RU_SANCTIONS_US | 0.20 | 0.15 | 0.22 | 0.07 | 0.190 | — | **0.190** | low |
| Q-0013 | ECO | PL_INFLATION | 0.80 | 0.85 | 0.88 | 0.08 | 0.843 | +0.10 | **0.943** | medium |
| Q-0014 | ECO | FOOD | 0.55 | 0.55 | 0.58 | 0.03 | 0.560 | — | **0.560** | low |
| Q-0015 | ECO | US_EU_TRADE | 0.12 | 0.12 | 0.08 | 0.04 | 0.107 | — | **0.107** | medium |
| Q-0016 | FIN | RATES_PL | 0.15 | 0.10 | 0.30 | 0.20 | 0.183 | — | **0.183** | medium |
| Q-0017 | FIN | RATES_ECB | 0.45 | 0.45 | 0.40 | 0.05 | 0.433 | — | **0.433** | low |
| Q-0018 | FIN | CN_SECONDARY_SANCTIONS | 0.10 | 0.08 | 0.08 | 0.02 | 0.087 | — | **0.087** | medium |
| Q-0019 | FIN | RU_SANCTIONS_EU | 0.55 | 0.50 | 0.40 | 0.15 | 0.483 | — | **0.483** | low |
| Q-0020 | FIN | RATES_RU | 0.30 | 0.25 | 0.20 | 0.10 | 0.250 | — | **0.250** | medium |
| Q-0021 | TEC | CN_RARE_EARTHS | 0.63 | 0.70 | 0.72 | 0.09 | 0.683 | — | **0.683** | medium |
| Q-0022 | TEC | CN_RARE_EARTHS | 0.60 | 0.72 | 0.72 | 0.12 | 0.680 | — | **0.680** | medium |
| Q-0023 | TEC | US_CHINA_TECH | 0.35 | 0.50 | 0.45 | 0.15 | 0.433 | — | **0.433** | low |
| Q-0024 | TEC | US_CHINA_TECH | 0.15 | 0.15 | 0.20 | 0.05 | 0.167 | — | **0.167** | low |
| Q-0025 | TEC | CN_RARE_EARTHS | 0.45 | 0.60 | 0.45 | 0.15 | 0.500 | — | **0.500** | low |
| Q-0026 | DIP | UA_TALKS | 0.45 | 0.45 | 0.45 | 0.00 | 0.450 | — | **0.450** | low |
| Q-0027 | DIP | EASTERN_FLANK | 0.10 | 0.12 | 0.12 | 0.02 | 0.113 | — | **0.113** | medium |
| Q-0028 | DIP | HORMUZ | 0.35 | 0.25 | 0.30 | 0.10 | 0.300 | — | **0.300** | low |
| Q-0029 | DIP | US_CHINA_SUMMITS | 0.50 | 0.60 | 0.50 | 0.10 | 0.533 | — | **0.533** | low |
| Q-0030 | DIP | UA_TALKS | 0.30 | 0.25 | 0.25 | 0.05 | 0.267 | — | **0.267** | low |
| Q-0031 | DOM | US_ELECTIONS | 0.15 | 0.12 | 0.20 | 0.08 | 0.157 | -0.05 | **0.107** | medium |
| Q-0032 | DOM | IRAN_LEADERSHIP | 0.15 | 0.12 | 0.15 | 0.03 | 0.140 | — | **0.140** | low |
| Q-0033 | DOM | BRAZIL_ELECTIONS | 0.55 | 0.57 | 0.55 | 0.02 | 0.557 | — | **0.557** | low |
| Q-0034 | DOM | VENEZUELA | 0.30 | 0.35 | 0.35 | 0.05 | 0.333 | — | **0.333** | low |
| Q-0035 | DOM | SAHEL | 0.08 | 0.10 | 0.10 | 0.02 | 0.093 | — | **0.093** | low |
| Q-0036 | INF | HORMUZ | 0.30 | 0.20 | 0.22 | 0.10 | 0.240 | — | **0.240** | low |
| Q-0037 | INF | HORMUZ | 0.10 | 0.12 | 0.12 | 0.02 | 0.113 | — | **0.113** | low |
| Q-0038 | INF | HORMUZ | 0.32 | 0.22 | 0.30 | 0.10 | 0.280 | — | **0.280** | low |
| Q-0039 | INF | PANAMA | 0.35 | 0.10 | 0.20 | 0.25 | 0.217 | -0.07 | **0.147** | low |
| Q-0040 | INF | BALTIC_INFRA | 0.40 | 0.75 | 0.55 | 0.35 | 0.567 | +0.10 | **0.667** | low |
| Q-0041 | MIL | IRAN_WAR | 0.05 | 0.08 | 0.05 | 0.03 | 0.060 | — | **0.060** | medium |
| Q-0042 | DIP | HORMUZ | 0.55 | 0.45 | 0.45 | 0.10 | 0.483 | — | **0.483** | low |
| Q-0043 | MIL | BAB_EL_MANDAB | 0.40 | 0.35 | 0.35 | 0.05 | 0.367 | — | **0.367** | low |
| Q-0044 | MIL | US_EUROPE | 0.20 | 0.20 | 0.20 | 0.00 | 0.200 | — | **0.200** | low |
| Q-0045 | MIL | EASTERN_FLANK | 0.25 | 0.15 | 0.15 | 0.10 | 0.183 | — | **0.183** | low |
| Q-0046 | MIL | KOREA | 0.50 | 0.45 | 0.40 | 0.10 | 0.450 | — | **0.450** | low |
| Q-0047 | MIL | TAIWAN | 0.40 | 0.40 | 0.55 | 0.15 | 0.450 | — | **0.450** | low |
| Q-0048 | ENE | EU_ENERGY | 0.35 | 0.37 | 0.40 | 0.05 | 0.373 | — | **0.373** | low |
| Q-0049 | ENE | EU_ENERGY | 0.70 | 0.60 | 0.55 | 0.15 | 0.617 | — | **0.617** | low |
| Q-0050 | ENE | PL_FUELS | 0.30 | 0.35 | 0.35 | 0.05 | 0.333 | +0.05 | **0.383** | low |
| Q-0051 | ENE | OPEC | 0.30 | 0.30 | 0.25 | 0.05 | 0.283 | — | **0.283** | low |
| Q-0052 | FIN | PLN | 0.45 | 0.47 | 0.45 | 0.02 | 0.457 | — | **0.457** | low |
| Q-0053 | FIN | RU_FINANCE | 0.50 | 0.45 | 0.52 | 0.07 | 0.490 | — | **0.490** | low |
| Q-0054 | DOM | RU_DOMESTIC | 0.85 | 0.68 | 0.93 | 0.25 | 0.820 | +0.12 | **0.940** | medium |
| Q-0055 | DOM | LATVIA_ELECTIONS | 0.75 | 0.88 | 0.82 | 0.13 | 0.817 | — | **0.817** | medium |
| Q-0056 | DOM | BRAZIL_ELECTIONS | 0.08 | 0.04 | 0.07 | 0.04 | 0.063 | — | **0.063** | medium |
| Q-0057 | ECO | US_CHINA_TRADE | 0.12 | 0.12 | 0.15 | 0.03 | 0.130 | — | **0.130** | medium |
| Q-0058 | ECO | US_CHINA_TRADE | 0.45 | 0.45 | 0.45 | 0.00 | 0.450 | — | **0.450** | low |
| Q-0059 | DIP | UA_TALKS | 0.15 | 0.10 | 0.10 | 0.05 | 0.117 | — | **0.117** | medium |
| Q-0060 | FIN | CN_SECONDARY_SANCTIONS | 0.55 | 0.68 | 0.45 | 0.23 | 0.560 | — | **0.560** | low |
| Q-0061 | FIN | RU_SANCTIONS_US | 0.25 | 0.15 | 0.25 | 0.10 | 0.217 | — | **0.217** | low |
| Q-0062 | INF | BAB_EL_MANDAB | 0.45 | 0.45 | 0.40 | 0.05 | 0.433 | +0.08 | **0.513** | low |
| Q-0063 | INF | HORMUZ | 0.45 | 0.40 | 0.40 | 0.05 | 0.417 | — | **0.417** | low |
| Q-0064 | DIP | UA_USA | 0.25 | 0.25 | 0.30 | 0.05 | 0.267 | — | **0.267** | low |
| Q-0065 | MIL | IRAN_WAR | 0.25 | 0.28 | 0.25 | 0.03 | 0.260 | — | **0.260** | low |
| Q-0066 | FIN | RATES_FED | 0.30 | 0.40 | 0.30 | 0.10 | 0.333 | — | **0.333** | low |
| Q-0067 | ENE | EU_ENERGY | 0.30 | 0.45 | 0.30 | 0.15 | 0.350 | — | **0.350** | medium |
| Q-0068 | MIL | BAB_EL_MANDAB | 0.25 | 0.25 | 0.20 | 0.05 | 0.233 | — | **0.233** | low |
| Q-0069 | MIL | TAIWAN | 0.15 | 0.15 | 0.20 | 0.05 | 0.167 | — | **0.167** | low |
| Q-0070 | FIN | PL_FINANCE | 0.30 | 0.33 | 0.30 | 0.03 | 0.310 | — | **0.310** | low |
| Q-0071 | FIN | UA_FUNDING | 0.20 | 0.12 | 0.20 | 0.08 | 0.173 | — | **0.173** | low |
| Q-0072 | DIP | CAUCASUS | 0.12 | 0.15 | 0.12 | 0.03 | 0.130 | — | **0.130** | medium |
| Q-0073 | MIL | UA_FRONT | 0.10 | 0.10 | 0.15 | 0.05 | 0.117 | — | **0.117** | medium |

Mean AGG: 0.332 · mean AGG_RT: 0.338 · min AGG_RT 0.030 · max AGG_RT 0.943

## 3. Triviality test (§3.8)

- AGG_RT < 0.05 or > 0.95: **1 of 73 questions (1.4%)** — Q-0001 (0.030). Limit: 20% (14 questions).
- Closest to the upper threshold: Q-0013 (0.943), Q-0054 (0.940) — below 0.95.
- **Result: rule met.** There is no obligation to add harder questions in edition 02.

## 4. Registry

146 rows appended to `registry/forecasts.csv` (73 × AGG, 73 × AGG_RT), date 2026-09-23, edition 01. Existing rows unchanged (checked by byte comparison). Number of accepted adjustments: 9; questions with AGG_RT ≠ AGG: 9.

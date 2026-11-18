# Stage 06 — Aggregation (edition 03, state 16.11.2026)

Input: `registry/questions.csv` (83 ACTIVE questions), `registry/forecasts.csv` (runs A, B, C of edition 03), `05_red_team.md` §3, evidence records cited there (A-01 in `04_forecasts_A.md`; B-03, B-04, B-05, B-07 in `04_forecasts_B.md`; C-02 in `04_forecasts_C.md`; R-01 in `05_red_team.md` §7; R-03 in the edition 02 red-team file). Stage run on 18.11.2026 from 08:27 (CET), AUTO mode (autopilot), model claude-opus-5-5.
Completeness check: all 83 active questions have a forecast from each of the three lenses (A, B, C), all dated 2026-11-17; no lens row for a non-active question; no edition 03 AGG or AGG_RT row existed before this stage — aggregation permitted. The AGG values recomputed here match table 05 §2.1 for all 83 questions.

Recording convention (as in editions 01 and 02): AGG = arithmetic mean of A, B, C, recorded to 0.001 (no additional rounding). AGG_RT = AGG + accepted adjustment (exact, 0.001), clipped to 0.01–0.99; without an adjustment AGG_RT = AGG. The AGG_RT values in table 05 §3 (e.g. 0.69 for Q-0017) are presentational roundings of the same numbers. Analytic confidence of AGG and AGG_RT = median of the three lenses' confidence. Key indicator = the question's `key_indicator` in `questions.csv`. Registry date of the AGG/AGG_RT rows: 2026-11-17 (date of INFO_CUTOFF 17.11.2026 15:08, the same as the lens rows).

## 1. Red-team adjustments — decisions

Acceptance criteria (methodology §5, prompt 06 step 1.2): |adjustment| ≤ 0.15 and specific evidence or an identified logical error.

| ID | AGG | adjustment | AGG_RT | type (05) | decision | basis |
|---|---|---|---|---|---|---|
| Q-0017 | 0.543 | +0.15 | 0.693 | evidence | ACCEPTED | Reuters poll of 10–12.11, after the oil fall: all 71 economists expect a December hike (R-01, opened by the red team; B-04); ECB expects inflation above 4% for much of H1 2027 (B-05); hike debated in October (G3-040). Adjustment equals the limit, does not exceed it |
| Q-0136 | 0.457 | −0.15 | 0.307 | evidence | ACCEPTED | Finance Committee MP, 17.11 07:46 CET (before the cutoff): no final vote on 23–26.11, "probably" 07–10.12 (A-01); supersedes the same MP's earlier schedule used by B and C (B-07, C-02). Adjustment equals the limit |
| Q-0040 | 0.557 | +0.10 | 0.657 | evidence | ACCEPTED | reference class verified in edition 02 (R-03): a qualifying Baltic subsea incident with investigation or detention in each of the last three winters, mostly November–January; lens A gives no counter-evidence |
| Q-0145 | 0.360 | +0.07 | 0.430 | evidence | ACCEPTED | economists polled after the oil fall see headline inflation around twice the target until at least Q2 2027 (R-01); Pantheon 4.1% for November (B-03, dated 04.11); ECB above 4% in H1 2027 (B-05); threshold includes 4.0% |

**Rejected adjustments: none.** None of the 4 proposals exceeds ±0.15 and each cites identified evidence records, all dated on or before INFO_CUTOFF. Questions the red team considered and itself left unadjusted (Q-0123, Q-0144, Q-0129, Q-0125, Q-0114) have AGG_RT = AGG.

Notes on the record:
- Accepting an adjustment does not mean the evidence was re-verified in stage 06 — the stage checks the formal requirements (limit, presence of evidence or an error) and that the cited records exist in the edition files (all seven do). R-01 rests on a Reuters page opened by the red team (B/2); A-01 on an MP's statement reported before the cutoff.
- Q-0017 and Q-0136: the ±0.15 limit, not the evidence, determines the size (05 §3). Methodology v1.0 is frozen — no deviation.
- Q-0040: the same adjustment (+0.10 on a similar AGG) was accepted in edition 02 on the same reference class; lens A again repeats its earlier value. Repeated identical correction of one lens on one question is material for learning step L2/L3 and the quarterly review.
- Net sum of accepted adjustments: +0.17; the mean over 83 questions shifts by +0.002. Questions with AGG_RT ≠ AGG: 4.

## 2. Table of AGG and AGG_RT (83 questions)

| ID | vector | cluster | A | B | C | spread | AGG | RT adjustment | AGG_RT | confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | MIL | RU_MOBILIZATION | 0.02 | 0.02 | 0.02 | 0.00 | 0.020 | — | **0.020** | medium |
| Q-0002 | MIL | EASTERN_FLANK | 0.06 | 0.09 | 0.06 | 0.03 | 0.070 | — | **0.070** | low |
| Q-0003 | MIL | US_EUROPE | 0.10 | 0.15 | 0.10 | 0.05 | 0.117 | — | **0.117** | medium |
| Q-0005 | MIL | TAIWAN | 0.25 | 0.22 | 0.30 | 0.08 | 0.257 | — | **0.257** | low |
| Q-0007 | ENE | OIL_PRICE | 0.07 | 0.05 | 0.04 | 0.03 | 0.053 | — | **0.053** | medium |
| Q-0008 | ENE | OIL_PRICE | 0.25 | 0.27 | 0.15 | 0.12 | 0.223 | — | **0.223** | low |
| Q-0010 | ENE | EU_ENERGY | 0.45 | 0.40 | 0.40 | 0.05 | 0.417 | — | **0.417** | low |
| Q-0012 | ECO | RU_SANCTIONS_US | 0.04 | 0.03 | 0.03 | 0.01 | 0.033 | — | **0.033** | high |
| Q-0015 | ECO | US_EU_TRADE | 0.08 | 0.08 | 0.06 | 0.02 | 0.073 | — | **0.073** | medium |
| Q-0016 | FIN | RATES_PL | 0.12 | 0.10 | 0.10 | 0.02 | 0.107 | — | **0.107** | medium |
| Q-0017 | FIN | RATES_ECB | 0.40 | 0.88 | 0.35 | 0.53 | 0.543 | +0.15 | **0.693** | low |
| Q-0018 | FIN | CN_SECONDARY_SANCTIONS | 0.06 | 0.05 | 0.06 | 0.01 | 0.057 | — | **0.057** | medium |
| Q-0019 | FIN | RU_SANCTIONS_EU | 0.33 | 0.40 | 0.30 | 0.10 | 0.343 | — | **0.343** | low |
| Q-0022 | TEC | CN_RARE_EARTHS | 0.72 | 0.80 | 0.70 | 0.10 | 0.740 | — | **0.740** | medium |
| Q-0023 | TEC | US_CHINA_TECH | 0.12 | 0.12 | 0.15 | 0.03 | 0.130 | — | **0.130** | low |
| Q-0024 | TEC | US_CHINA_TECH | 0.08 | 0.05 | 0.06 | 0.03 | 0.063 | — | **0.063** | medium |
| Q-0027 | DIP | EASTERN_FLANK | 0.06 | 0.06 | 0.08 | 0.02 | 0.067 | — | **0.067** | medium |
| Q-0028 | DIP | HORMUZ | 0.07 | 0.05 | 0.05 | 0.02 | 0.057 | — | **0.057** | medium |
| Q-0029 | DIP | US_CHINA_SUMMITS | 0.93 | 0.80 | 0.93 | 0.13 | 0.887 | — | **0.887** | high |
| Q-0030 | DIP | UA_TALKS | 0.93 | 0.93 | 0.92 | 0.01 | 0.927 | — | **0.927** | high |
| Q-0032 | DOM | IRAN_LEADERSHIP | 0.12 | 0.05 | 0.10 | 0.07 | 0.090 | — | **0.090** | low |
| Q-0034 | DOM | VENEZUELA | 0.30 | 0.28 | 0.38 | 0.10 | 0.320 | — | **0.320** | low |
| Q-0035 | DOM | SAHEL | 0.05 | 0.05 | 0.07 | 0.02 | 0.057 | — | **0.057** | low |
| Q-0036 | INF | HORMUZ | 0.05 | 0.03 | 0.02 | 0.03 | 0.033 | — | **0.033** | high |
| Q-0038 | INF | HORMUZ | 0.06 | 0.05 | 0.04 | 0.02 | 0.050 | — | **0.050** | medium |
| Q-0040 | INF | BALTIC_INFRA | 0.40 | 0.72 | 0.55 | 0.32 | 0.557 | +0.10 | **0.657** | low |
| Q-0068 | MIL | BAB_EL_MANDAB | 0.12 | 0.07 | 0.10 | 0.05 | 0.097 | — | **0.097** | medium |
| Q-0069 | MIL | TAIWAN | 0.07 | 0.07 | 0.05 | 0.02 | 0.063 | — | **0.063** | medium |
| Q-0070 | FIN | PL_FINANCE | 0.35 | 0.37 | 0.35 | 0.02 | 0.357 | — | **0.357** | low |
| Q-0071 | FIN | UA_FUNDING | 0.10 | 0.06 | 0.08 | 0.04 | 0.080 | — | **0.080** | medium |
| Q-0072 | DIP | CAUCASUS | 0.12 | 0.12 | 0.10 | 0.02 | 0.113 | — | **0.113** | medium |
| Q-0073 | MIL | UA_FRONT | 0.04 | 0.04 | 0.04 | 0.00 | 0.040 | — | **0.040** | medium |
| Q-0077 | ECO | US_CHINA_TRADE | 0.75 | 0.70 | 0.75 | 0.05 | 0.733 | — | **0.733** | medium |
| Q-0096 | DOM | IRAN_LEADERSHIP | 0.05 | 0.05 | 0.05 | 0.00 | 0.050 | — | **0.050** | medium |
| Q-0097 | MIL | EASTERN_FLANK | 0.25 | 0.40 | 0.25 | 0.15 | 0.300 | — | **0.300** | low |
| Q-0100 | DIP | US_CHINA_SUMMITS | 0.75 | 0.82 | 0.85 | 0.10 | 0.807 | — | **0.807** | medium |
| Q-0103 | TEC | URANIUM | 0.18 | 0.22 | 0.18 | 0.04 | 0.193 | — | **0.193** | low |
| Q-0104 | FIN | RU_SANCTIONS_EU | 0.05 | 0.03 | 0.03 | 0.02 | 0.037 | — | **0.037** | high |
| Q-0106 | ENE | OIL_PRICE | 0.03 | 0.02 | 0.04 | 0.02 | 0.030 | — | **0.030** | high |
| Q-0107 | ENE | PL_FUELS | 0.12 | 0.08 | 0.12 | 0.04 | 0.107 | — | **0.107** | medium |
| Q-0108 | ECO | US_CHINA_TRADE | 0.10 | 0.08 | 0.10 | 0.02 | 0.093 | — | **0.093** | medium |
| Q-0109 | DOM | US_EUROPE | 0.55 | 0.58 | 0.55 | 0.03 | 0.560 | — | **0.560** | low |
| Q-0110 | DIP | UA_TALKS | 0.08 | 0.07 | 0.09 | 0.02 | 0.080 | — | **0.080** | medium |
| Q-0111 | DIP | GREENLAND | 0.80 | 0.65 | 0.85 | 0.20 | 0.767 | — | **0.767** | medium |
| Q-0112 | FIN | US_CHINA_FIN | 0.03 | 0.03 | 0.03 | 0.00 | 0.030 | — | **0.030** | medium |
| Q-0113 | MIL | UA_FRONT | 0.18 | 0.15 | 0.15 | 0.03 | 0.160 | — | **0.160** | low |
| Q-0114 | MIL | US_EUROPE | 0.55 | 0.40 | 0.45 | 0.15 | 0.467 | — | **0.467** | low |
| Q-0115 | ENE | OIL_PRICE | 0.30 | 0.35 | 0.22 | 0.13 | 0.290 | — | **0.290** | low |
| Q-0116 | MIL | UA_FRONT | 0.50 | 0.50 | 0.45 | 0.05 | 0.483 | — | **0.483** | low |
| Q-0117 | ENE | EU_ENERGY | 0.30 | 0.33 | 0.30 | 0.03 | 0.310 | — | **0.310** | low |
| Q-0118 | FIN | RATES_RU | 0.22 | 0.25 | 0.20 | 0.05 | 0.223 | — | **0.223** | medium |
| Q-0119 | TEC | CN_RARE_EARTHS | 0.74 | 0.75 | 0.75 | 0.01 | 0.747 | — | **0.747** | medium |
| Q-0120 | TEC | CN_RARE_EARTHS | 0.10 | 0.07 | 0.12 | 0.05 | 0.097 | — | **0.097** | medium |
| Q-0121 | DIP | UA_TALKS | 0.65 | 0.55 | 0.55 | 0.10 | 0.583 | — | **0.583** | low |
| Q-0122 | DOM | US_ELECTIONS | 0.18 | 0.13 | 0.22 | 0.09 | 0.177 | — | **0.177** | low |
| Q-0123 | DOM | RS_GOVERNMENT | 0.50 | 0.25 | 0.35 | 0.25 | 0.367 | — | **0.367** | low |
| Q-0124 | INF | HORMUZ | 0.15 | 0.07 | 0.12 | 0.08 | 0.113 | — | **0.113** | medium |
| Q-0125 | INF | PANAMA | 0.45 | 0.40 | 0.25 | 0.20 | 0.367 | — | **0.367** | low |
| Q-0126 | ENE | OIL_PRICE | 0.52 | 0.55 | 0.50 | 0.05 | 0.523 | — | **0.523** | low |
| Q-0127 | ECO | PL_INFLATION | 0.40 | 0.30 | 0.35 | 0.10 | 0.350 | — | **0.350** | low |
| Q-0128 | ECO | FOOD | 0.55 | 0.57 | 0.60 | 0.05 | 0.573 | — | **0.573** | low |
| Q-0129 | MIL | IRAN_WAR | 0.55 | 0.55 | 0.60 | 0.05 | 0.567 | — | **0.567** | low |
| Q-0130 | MIL | TAIWAN | 0.55 | 0.50 | 0.45 | 0.10 | 0.500 | — | **0.500** | low |
| Q-0131 | FIN | PLN | 0.53 | 0.50 | 0.52 | 0.03 | 0.517 | — | **0.517** | low |
| Q-0132 | DIP | US_CHINA_SUMMITS | 0.38 | 0.20 | 0.35 | 0.18 | 0.310 | — | **0.310** | low |
| Q-0133 | DOM | ES_ELECTIONS | 0.66 | 0.70 | 0.70 | 0.04 | 0.687 | — | **0.687** | low |
| Q-0134 | INF | EASTERN_FLANK | 0.85 | 0.85 | 0.85 | 0.00 | 0.850 | — | **0.850** | medium |
| Q-0135 | DIP | KOREA | 0.06 | 0.05 | 0.10 | 0.05 | 0.070 | — | **0.070** | medium |
| Q-0136 | FIN | UA_FUNDING | 0.12 | 0.65 | 0.60 | 0.53 | 0.457 | −0.15 | **0.307** | medium |
| Q-0137 | DIP | UA_TALKS | 0.45 | 0.35 | 0.45 | 0.10 | 0.417 | — | **0.417** | low |
| Q-0138 | FIN | RU_SANCTIONS_US | 0.12 | 0.07 | 0.15 | 0.08 | 0.113 | — | **0.113** | medium |
| Q-0139 | INF | BLACK_SEA | 0.65 | 0.55 | 0.60 | 0.10 | 0.600 | — | **0.600** | low |
| Q-0140 | MIL | IRAN_WAR | 0.58 | 0.55 | 0.55 | 0.03 | 0.560 | — | **0.560** | low |
| Q-0141 | DIP | HORMUZ | 0.15 | 0.12 | 0.08 | 0.07 | 0.117 | — | **0.117** | medium |
| Q-0142 | FIN | RATES_FED | 0.55 | 0.60 | 0.60 | 0.05 | 0.583 | — | **0.583** | low |
| Q-0143 | ECO | US_FISCAL | 0.15 | 0.22 | 0.25 | 0.10 | 0.207 | — | **0.207** | low |
| Q-0144 | MIL | US_EUROPE | 0.20 | 0.25 | 0.25 | 0.05 | 0.233 | — | **0.233** | low |
| Q-0145 | ECO | RATES_ECB | 0.28 | 0.55 | 0.25 | 0.30 | 0.360 | +0.07 | **0.430** | low |
| Q-0146 | DOM | IL_GOVERNMENT | 0.40 | 0.35 | 0.40 | 0.05 | 0.383 | — | **0.383** | low |
| Q-0147 | TEC | US_CHINA_TECH | 0.68 | 0.68 | 0.70 | 0.02 | 0.687 | — | **0.687** | medium |
| Q-0148 | ENE | PL_FUELS | 0.50 | 0.50 | 0.45 | 0.05 | 0.483 | — | **0.483** | low |
| Q-0149 | DIP | UA_TALKS | 0.22 | 0.15 | 0.30 | 0.15 | 0.223 | — | **0.223** | low |
| Q-0150 | TEC | URANIUM | 0.60 | 0.60 | 0.70 | 0.10 | 0.633 | — | **0.633** | low |

Mean AGG: 0.316 · mean AGG_RT: 0.318 · min AGG_RT 0.020 · max AGG_RT 0.927

## 3. Triviality test (§3.8)

- AGG_RT < 0.05 or > 0.95: **7 of 83 questions (8.4%)** — Q-0001, Q-0012, Q-0036, Q-0073, Q-0104, Q-0106, Q-0112 (values in table §2). Limit: 20% (16 questions).
- Closest to the thresholds: Q-0038 and Q-0096 exactly at 0.050 (not below), Q-0007 (0.053), Q-0018, Q-0028, Q-0035 (0.057) at the lower end; Q-0030 (0.927) at the upper end — inside the range.
- No ACTIVE question is past its deadline (earliest deadline 19.11.2026: Q-0029, Q-0100); none was determined before the cutoff (03 §1.8, 05 §6).
- **Result: rule met.** There is no obligation to add harder questions in edition 04. ASSESSMENT: the share rose from 3.4% (edition 02) to 8.4%; still well below the limit.

## 4. Registry

166 rows appended to `registry/forecasts.csv` (83 × AGG, 83 × AGG_RT), date 2026-11-17, edition 03, LF line endings as in the existing file. Existing rows unchanged (checked by byte comparison of the file prefix; `git diff --numstat`: 166 insertions, 0 deletions). Number of accepted adjustments: 4; questions with AGG_RT ≠ AGG: 4. Before freezing, no forecasting service, prediction market or `registry/benchmarks.csv` content was opened in this stage. Computation by a one-off script in the git-ignored `data/tmp_oneoff/`, deleted afterwards.

# Accuracy scores

Resolved and scored questions: **67** (of which auto-verified: 13) · awaiting verification: 0 · void: 0

## Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |
|---|---|---|---|---|---|
| A | 78 | 0.182 | 0.380 | 0.522 | 0.176 |
| B | 78 | 0.177 | 0.380 | 0.536 | 0.169 |
| C | 78 | 0.177 | 0.380 | 0.536 | 0.169 |
| AGG | 78 | 0.176 | 0.380 | 0.536 | 0.169 |
| AGG_RT | 78 | 0.177 | 0.380 | 0.534 | 0.170 |

## AGG_RT vs crowd (EXACT matches only)

N pairs: 18 · Brier AGG_RT: 0.127 · Brier crowd: 0.143 · BSS vs crowd: 0.116

## AGG_RT calibration

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 5 | 0.07 | 0.00 |
| 10–20% | 16 | 0.13 | 0.06 |
| 20–30% | 14 | 0.26 | 0.29 |
| 30–40% | 9 | 0.35 | 0.67 |
| 40–50% | 14 | 0.45 | 0.86 |
| 50–60% | 8 | 0.54 | 0.75 |
| 60–70% | 4 | 0.64 | 0.50 |
| 70–80% | 3 | 0.75 | 1.00 |
| 80–90% | 1 | 0.82 | 1.00 |
| 90–100% | 4 | 0.93 | 1.00 |

## AGG_RT directional bias (mean p − outcome; neutral ≈ 0)

| who_benefits | N | Mean signed error |
|---|---|---|
| US_WEST | 0 | n/a |
| EU | 1 | -0.100 |
| UKRAINE | 1 | 0.267 |
| RUSSIA | 2 | 0.177 |
| CHINA | 0 | n/a |
| IRAN | 0 | n/a |
| COMPROMISE | 7 | -0.193 |

## Clusters

| Group | N | Brier AGG_RT |
|---|---|---|
| BAB_EL_MANDAB | 4 | 0.308 |
| BG_ELECTIONS | 1 | 0.071 |
| BLACK_SEA | 1 | 0.218 |
| BRAZIL_ELECTIONS | 3 | 0.235 |
| CN_RARE_EARTHS | 5 | 0.135 |
| CN_SECONDARY_SANCTIONS | 1 | 0.194 |
| EASTERN_FLANK | 1 | 0.033 |
| EU_ENERGY | 7 | 0.301 |
| FOOD | 2 | 0.254 |
| HORMUZ | 5 | 0.121 |
| IL_ELECTIONS | 1 | 0.284 |
| IRAN_WAR | 4 | 0.314 |
| KOREA | 1 | 0.303 |
| LATVIA_ELECTIONS | 1 | 0.033 |
| OIL_PRICE | 2 | 0.247 |
| OPEC | 1 | 0.080 |
| PANAMA | 2 | 0.367 |
| PLN | 2 | 0.180 |
| PL_FINANCE | 1 | 0.453 |
| PL_FUELS | 2 | 0.079 |
| PL_INFLATION | 2 | 0.208 |
| RATES_FED | 2 | 0.071 |
| RATES_RU | 3 | 0.030 |
| RU_DOMESTIC | 1 | 0.004 |
| RU_FINANCE | 1 | 0.260 |
| RU_SANCTIONS_EU | 1 | 0.010 |
| RU_SANCTIONS_US | 3 | 0.030 |
| TAIWAN | 2 | 0.190 |
| UA_EU | 1 | 0.267 |
| UA_FRONT | 2 | 0.034 |
| UA_TALKS | 4 | 0.210 |
| UA_USA | 1 | 0.071 |
| US_CHINA_TECH | 1 | 0.062 |
| US_CHINA_TRADE | 3 | 0.127 |
| US_ELECTIONS | 3 | 0.068 |
| US_EUROPE | 1 | 0.040 |

Brier AGG_RT with a weight of 1 per cluster: **0.164**

## Vectors

| Group | N | Brier AGG_RT |
|---|---|---|
| DIP | 8 | 0.178 |
| DOM | 10 | 0.130 |
| ECO | 8 | 0.165 |
| ENE | 12 | 0.237 |
| FIN | 13 | 0.122 |
| INF | 9 | 0.238 |
| MIL | 12 | 0.207 |
| TEC | 6 | 0.123 |

## Editions (forecast made in)

| Group | N | Brier AGG_RT |
|---|---|---|
| 01 | 41 | 0.189 |
| 02 | 37 | 0.164 |

## Framework versions (registry/editions.csv)

| Group | N | Brier AGG_RT |
|---|---|---|
| 1.0.0 | 41 | 0.189 |
| 1.4.0 | 37 | 0.164 |

## Horizons (from forecast date to deadline)

| Group | N | Brier AGG_RT |
|---|---|---|
| ≤100 days | 36 | 0.217 |
| ≤14 days | 42 | 0.144 |

## Auto-verified (independent automatic re-check, not reviewed by the user)

Q-0025, Q-0039, Q-0042, Q-0049, Q-0065, Q-0083, Q-0084, Q-0087, Q-0088, Q-0094, Q-0095, Q-0102, Q-0105

## Left out: forecast on or after the resolution date

Q-0037 (edition 02), Q-0049 (edition 02), Q-0080 (edition 02)

## Diagnostics (not the official measure)

Methodology §1 keeps BSS vs status quo and vs the crowd as the official measures. These lines show how hard those baselines are and how independent the lenses are.

### YES rate by p_status_quo (scored questions)

| p_status_quo | N questions | YES rate |
|---|---|---|
| 0.10 | 55 | 0.45 |
| 0.50 | 7 | 0.71 |
| 0.90 | 4 | 0.50 |

### AGG_RT against other reference baselines

| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |
|---|---|---|---|---|
| status quo (official) | 78 | 0.177 | 0.380 | 0.534 |
| constant 0.50 | 78 | 0.177 | 0.250 | 0.291 |
| YES rate of earlier resolutions (≥ 10) | 37 | 0.164 | 0.254 | 0.354 |
| previous edition's AGG_RT | 12 | 0.186 | 0.248 | 0.250 |

### Lens diversity by edition (all forecasts, resolved or not)

| Edition | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |
|---|---|---|---|---|---|---|
| 01 | 73 | 0.91 | 0.94 | 0.92 | 0.06 | 1 |
| 02 | 88 | 0.93 | 0.95 | 0.90 | 0.06 | 2 |
| 03 | 83 | 0.91 | 0.96 | 0.94 | 0.05 | 4 |

### Closed cohort (questions whose deadline has passed)

A YES resolves on the day the event happens and a NO only at the deadline, so the set of resolved questions over-represents YES while many deadlines are still open. The closed cohort counts only questions with a deadline before 22.11.2026.

| Set | N questions | YES rate | Brier AGG_RT | Brier SQ | BSS vs SQ |
|---|---|---|---|---|---|
| all resolved | 66 | 0.48 | 0.177 | 0.380 | 0.534 |
| closed cohort | 58 | 0.45 | 0.154 | 0.302 | 0.489 |

Active questions past their deadline and not yet resolved: 2 · awaiting verification: 0

### Runs with 90% intervals (cluster bootstrap, 2000 resamples, fixed seed)

| Run | N | Brier | 90% interval | BSS vs SQ | 90% interval |
|---|---|---|---|---|---|
| A | 78 | 0.182 | [0.146, 0.218] | 0.522 | [0.412, 0.620] |
| B | 78 | 0.177 | [0.144, 0.210] | 0.536 | [0.428, 0.628] |
| C | 78 | 0.177 | [0.145, 0.207] | 0.536 | [0.434, 0.621] |
| AGG | 78 | 0.176 | [0.144, 0.208] | 0.536 | [0.434, 0.627] |
| AGG_RT | 78 | 0.177 | [0.144, 0.211] | 0.534 | [0.429, 0.626] |
| derived:logodds | 78 | 0.176 | [0.143, 0.209] | 0.537 | [0.435, 0.627] |
| derived:logodds^1.5 | 78 | 0.183 | [0.139, 0.226] | 0.518 | [0.398, 0.630] |
| derived:median | 78 | 0.180 | [0.146, 0.213] | 0.527 | [0.426, 0.619] |

### Paired difference against AGG_RT (same question and edition)

Negative = the run was more accurate than the official forecast. An interval containing 0 = no evidence of a difference.

| Run | N pairs | Mean Brier difference | 90% interval | closer than AGG_RT / further |
|---|---|---|---|---|
| A | 78 | 0.005 | [-0.007, 0.014] | 29 / 44 |
| B | 78 | -0.001 | [-0.008, 0.009] | 38 / 33 |
| C | 78 | -0.001 | [-0.007, 0.006] | 36 / 35 |
| AGG | 78 | -0.001 | [-0.005, 0.002] | 3 / 7 |
| derived:logodds | 78 | -0.001 | [-0.004, 0.001] | 44 / 30 |
| derived:logodds^1.5 | 78 | 0.006 | [-0.005, 0.016] | 50 / 28 |
| derived:median | 78 | 0.002 | [-0.001, 0.006] | 30 / 37 |

### Mean forecast against YES rate (AGG_RT)

| Group | N | Mean p | YES rate | Difference |
|---|---|---|---|---|
| all | 78 | 0.37 | 0.50 | -0.13 |
| closed cohort | 66 | 0.38 | 0.45 | -0.08 |
| horizon <=14 days | 42 | 0.34 | 0.40 | -0.06 |
| horizon <=100 days | 36 | 0.41 | 0.61 | -0.20 |
| vector DIP | 8 | 0.29 | 0.38 | -0.09 |
| vector DOM | 10 | 0.40 | 0.50 | -0.10 |
| vector ECO | 8 | 0.52 | 0.50 | 0.02 |
| vector ENE | 12 | 0.36 | 0.50 | -0.14 |
| vector FIN | 13 | 0.33 | 0.38 | -0.05 |
| vector INF | 9 | 0.36 | 0.56 | -0.20 |
| vector MIL | 12 | 0.28 | 0.50 | -0.22 |
| vector TEC | 6 | 0.56 | 0.83 | -0.28 |

## Methodology v1.1 measures (auxiliary, §1)

Indicative below about 30 resolved questions per group. Cohort v1.1 = questions with a NEW metadata row; v1.0 = the rest.

Cohort v1.0: N 78 · Brier AGG_RT 0.177 · BSS vs SQ 0.534 · without the tail group: N 78, BSS vs SQ 0.534

Cohort v1.1: no resolved questions yet.

## Drivers

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| D1 | 2 | 0.034 | 0 | n/a |
| D3 | 3 | 0.126 | 0 | n/a |
| D4 | 2 | 0.168 | 0 | n/a |
| D5 | 22 | 0.222 | 0 | n/a |
| D6 | 6 | 0.123 | 0 | n/a |
| D7 | 8 | 0.084 | 0 | n/a |
| D8 | 11 | 0.157 | 0 | n/a |
| D9 | 10 | 0.130 | 0 | n/a |
| D10 | 2 | 0.367 | 0 | n/a |
| D11 | 6 | 0.273 | 0 | n/a |
| D12 | 2 | 0.254 | 0 | n/a |
| D13 | 4 | 0.210 | 0 | n/a |

## Forms

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| EVENT (no metadata) | 78 | 0.177 | 0 | n/a |

## Horizon classes (creation to deadline: Q ≤90 days, Y 91–365, M >365)

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| Q | 72 | 0.166 | 0 | n/a |
| Y | 6 | 0.313 | 0 | n/a |

## Origins

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| V1.0 | 78 | 0.177 | 0 | n/a |

## Importance-weighted Brier (AGG_RT; NEW metadata only; weight = impact)

No resolved questions with a NEW importance rating yet.

## Actor models (CONDITIONAL questions by responding actor, AGG_RT)

No resolved CONDITIONAL questions yet.

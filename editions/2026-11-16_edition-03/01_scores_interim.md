# Accuracy scores

Resolved and scored questions: **71** (of which auto-verified: 14) · awaiting verification: 0 · void: 0

## Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |
|---|---|---|---|---|---|
| A | 85 | 0.178 | 0.383 | 0.534 | 0.175 |
| B | 85 | 0.176 | 0.383 | 0.539 | 0.172 |
| C | 85 | 0.173 | 0.383 | 0.547 | 0.168 |
| AGG | 85 | 0.174 | 0.383 | 0.545 | 0.170 |
| AGG_RT | 85 | 0.175 | 0.383 | 0.543 | 0.171 |

## AGG_RT vs crowd (EXACT matches only)

N pairs: 18 · Brier AGG_RT: 0.127 · Brier crowd: 0.143 · BSS vs crowd: 0.116

## AGG_RT calibration

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 5 | 0.07 | 0.00 |
| 10–20% | 16 | 0.13 | 0.06 |
| 20–30% | 14 | 0.26 | 0.29 |
| 30–40% | 10 | 0.35 | 0.70 |
| 40–50% | 14 | 0.45 | 0.86 |
| 50–60% | 9 | 0.54 | 0.78 |
| 60–70% | 6 | 0.64 | 0.67 |
| 70–80% | 3 | 0.75 | 1.00 |
| 80–90% | 4 | 0.84 | 1.00 |
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
| EASTERN_FLANK | 2 | 0.028 |
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
| US_CHINA_SUMMITS | 6 | 0.170 |
| US_CHINA_TECH | 1 | 0.062 |
| US_CHINA_TRADE | 3 | 0.127 |
| US_ELECTIONS | 3 | 0.068 |
| US_EUROPE | 1 | 0.040 |

Brier AGG_RT with a weight of 1 per cluster: **0.164**

## Vectors

| Group | N | Brier AGG_RT |
|---|---|---|
| DIP | 14 | 0.174 |
| DOM | 10 | 0.130 |
| ECO | 8 | 0.165 |
| ENE | 12 | 0.237 |
| FIN | 13 | 0.122 |
| INF | 10 | 0.217 |
| MIL | 12 | 0.207 |
| TEC | 6 | 0.123 |

## Editions (forecast made in)

| Group | N | Brier AGG_RT |
|---|---|---|
| 01 | 42 | 0.190 |
| 02 | 39 | 0.163 |
| 03 | 4 | 0.137 |

## Framework versions (registry/editions.csv)

| Group | N | Brier AGG_RT |
|---|---|---|
| 1.0.0 | 42 | 0.190 |
| 1.4.0 | 39 | 0.163 |
| 1.8.0 | 4 | 0.137 |

## Horizons (from forecast date to deadline)

| Group | N | Brier AGG_RT |
|---|---|---|
| ≤100 days | 39 | 0.213 |
| ≤14 days | 46 | 0.143 |

## Auto-verified (independent automatic re-check, not reviewed by the user)

Q-0025, Q-0029, Q-0039, Q-0042, Q-0049, Q-0065, Q-0083, Q-0084, Q-0087, Q-0088, Q-0094, Q-0095, Q-0102, Q-0105

## Left out: forecast on or after the resolution date

Q-0037 (edition 02), Q-0049 (edition 02), Q-0080 (edition 02)

## Diagnostics (not the official measure)

Methodology §1 keeps BSS vs status quo and vs the crowd as the official measures. These lines show how hard those baselines are and how independent the lenses are.

### YES rate by p_status_quo (scored questions)

| p_status_quo | N questions | YES rate |
|---|---|---|
| 0.10 | 57 | 0.47 |
| 0.50 | 9 | 0.78 |
| 0.90 | 4 | 0.50 |

### AGG_RT against other reference baselines

| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |
|---|---|---|---|---|
| status quo (official) | 85 | 0.175 | 0.383 | 0.543 |
| constant 0.50 | 85 | 0.175 | 0.250 | 0.300 |
| YES rate of earlier resolutions (≥ 10) | 43 | 0.160 | 0.252 | 0.365 |
| previous edition's AGG_RT | 15 | 0.160 | 0.231 | 0.306 |

### Lens diversity by edition (all forecasts, resolved or not)

| Edition | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |
|---|---|---|---|---|---|---|
| 01 | 73 | 0.91 | 0.94 | 0.92 | 0.06 | 1 |
| 02 | 88 | 0.93 | 0.95 | 0.90 | 0.06 | 2 |
| 03 | 83 | 0.91 | 0.96 | 0.94 | 0.05 | 4 |

### Closed cohort (questions whose deadline has passed)

A YES resolves on the day the event happens and a NO only at the deadline, so the set of resolved questions over-represents YES while many deadlines are still open. The closed cohort counts only questions with a deadline before 23.11.2026.

| Set | N questions | YES rate | Brier AGG_RT | Brier SQ | BSS vs SQ |
|---|---|---|---|---|---|
| all resolved | 70 | 0.51 | 0.175 | 0.383 | 0.543 |
| closed cohort | 61 | 0.48 | 0.156 | 0.306 | 0.491 |

Active questions past their deadline and not yet resolved: 0 · awaiting verification: 0

### Runs with 90% intervals (cluster bootstrap, 2000 resamples, fixed seed)

| Run | N | Brier | 90% interval | BSS vs SQ | 90% interval |
|---|---|---|---|---|---|
| A | 85 | 0.178 | [0.145, 0.211] | 0.534 | [0.431, 0.624] |
| B | 85 | 0.176 | [0.145, 0.207] | 0.539 | [0.438, 0.626] |
| C | 85 | 0.173 | [0.144, 0.202] | 0.547 | [0.454, 0.627] |
| AGG | 85 | 0.174 | [0.144, 0.204] | 0.545 | [0.450, 0.628] |
| AGG_RT | 85 | 0.175 | [0.143, 0.206] | 0.543 | [0.449, 0.628] |
| derived:logodds | 85 | 0.174 | [0.143, 0.204] | 0.546 | [0.451, 0.629] |
| derived:logodds^1.5 | 85 | 0.180 | [0.140, 0.220] | 0.529 | [0.419, 0.631] |
| derived:median | 85 | 0.177 | [0.146, 0.207] | 0.538 | [0.444, 0.621] |

### Paired difference against AGG_RT (same question and edition)

Negative = the run was more accurate than the official forecast. An interval containing 0 = no evidence of a difference.

| Run | N pairs | Mean Brier difference | 90% interval | closer than AGG_RT / further |
|---|---|---|---|---|
| A | 85 | 0.003 | [-0.007, 0.012] | 33 / 46 |
| B | 85 | 0.001 | [-0.007, 0.011] | 40 / 37 |
| C | 85 | -0.002 | [-0.007, 0.005] | 40 / 37 |
| AGG | 85 | -0.001 | [-0.004, 0.002] | 3 / 7 |
| derived:logodds | 85 | -0.001 | [-0.004, 0.001] | 48 / 32 |
| derived:logodds^1.5 | 85 | 0.005 | [-0.004, 0.015] | 56 / 29 |
| derived:median | 85 | 0.002 | [-0.002, 0.006] | 34 / 39 |

### Mean forecast against YES rate (AGG_RT)

| Group | N | Mean p | YES rate | Difference |
|---|---|---|---|---|
| all | 85 | 0.40 | 0.54 | -0.14 |
| closed cohort | 72 | 0.40 | 0.50 | -0.10 |
| horizon <=14 days | 46 | 0.38 | 0.46 | -0.08 |
| horizon <=100 days | 39 | 0.42 | 0.64 | -0.22 |
| vector DIP | 14 | 0.44 | 0.64 | -0.21 |
| vector DOM | 10 | 0.40 | 0.50 | -0.10 |
| vector ECO | 8 | 0.52 | 0.50 | 0.02 |
| vector ENE | 12 | 0.36 | 0.50 | -0.14 |
| vector FIN | 13 | 0.33 | 0.38 | -0.05 |
| vector INF | 10 | 0.41 | 0.60 | -0.19 |
| vector MIL | 12 | 0.28 | 0.50 | -0.22 |
| vector TEC | 6 | 0.56 | 0.83 | -0.28 |

## Methodology v1.1 measures (auxiliary, §1)

Indicative below about 30 resolved questions per group. Cohort v1.1 = questions with a NEW metadata row; v1.0 = the rest.

Cohort v1.0: N 85 · Brier AGG_RT 0.175 · BSS vs SQ 0.543 · without the tail group: N 85, BSS vs SQ 0.543

Cohort v1.1: no resolved questions yet.

## Drivers

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| D1 | 2 | 0.034 | 0 | n/a |
| D3 | 3 | 0.126 | 0 | n/a |
| D4 | 3 | 0.119 | 0 | n/a |
| D5 | 22 | 0.222 | 0 | n/a |
| D6 | 6 | 0.123 | 0 | n/a |
| D7 | 8 | 0.084 | 0 | n/a |
| D8 | 11 | 0.157 | 0 | n/a |
| D9 | 10 | 0.130 | 0 | n/a |
| D10 | 2 | 0.367 | 0 | n/a |
| D11 | 6 | 0.273 | 0 | n/a |
| D12 | 2 | 0.254 | 0 | n/a |
| D13 | 10 | 0.186 | 0 | n/a |

## Forms

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| EVENT (no metadata) | 85 | 0.175 | 0 | n/a |

## Horizon classes (creation to deadline: Q ≤90 days, Y 91–365, M >365)

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| Q | 79 | 0.164 | 0 | n/a |
| Y | 6 | 0.313 | 0 | n/a |

## Origins

| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |
|---|---|---|---|---|
| V1.0 | 85 | 0.175 | 0 | n/a |

## Importance-weighted Brier (AGG_RT; NEW metadata only; weight = impact)

No resolved questions with a NEW importance rating yet.

## Actor models (CONDITIONAL questions by responding actor, AGG_RT)

No resolved CONDITIONAL questions yet.

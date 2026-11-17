# Accuracy scores

Resolved and scored questions: **66** (of which auto-verified: 13) · awaiting verification: 1 · void: 0

## Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |
|---|---|---|---|---|---|
| A | 77 | 0.176 | 0.375 | 0.529 | 0.170 |
| B | 77 | 0.174 | 0.375 | 0.536 | 0.166 |
| C | 77 | 0.172 | 0.375 | 0.542 | 0.163 |
| AGG | 77 | 0.172 | 0.375 | 0.541 | 0.164 |
| AGG_RT | 77 | 0.173 | 0.375 | 0.538 | 0.165 |

## AGG_RT vs crowd (EXACT matches only)

N pairs: 18 · Brier AGG_RT: 0.127 · Brier crowd: 0.143 · BSS vs crowd: 0.116

## AGG_RT calibration

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 5 | 0.07 | 0.00 |
| 10–20% | 16 | 0.13 | 0.06 |
| 20–30% | 13 | 0.25 | 0.23 |
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
| BAB_EL_MANDAB | 3 | 0.239 |
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

Brier AGG_RT with a weight of 1 per cluster: **0.162**

## Vectors

| Group | N | Brier AGG_RT |
|---|---|---|
| DIP | 8 | 0.178 |
| DOM | 10 | 0.130 |
| ECO | 8 | 0.165 |
| ENE | 12 | 0.237 |
| FIN | 13 | 0.122 |
| INF | 8 | 0.204 |
| MIL | 12 | 0.207 |
| TEC | 6 | 0.123 |

## Editions (forecast made in)

| Group | N | Brier AGG_RT |
|---|---|---|
| 01 | 41 | 0.189 |
| 02 | 36 | 0.154 |

## Framework versions (registry/editions.csv)

| Group | N | Brier AGG_RT |
|---|---|---|
| 1.0.0 | 41 | 0.189 |
| 1.4.0 | 36 | 0.154 |

## Horizons (from forecast date to deadline)

| Group | N | Brier AGG_RT |
|---|---|---|
| ≤100 days | 36 | 0.217 |
| ≤14 days | 41 | 0.135 |

## Awaiting user verification

Q-0079

## Auto-verified (independent automatic re-check, not reviewed by the user)

Q-0025, Q-0039, Q-0042, Q-0049, Q-0065, Q-0083, Q-0084, Q-0087, Q-0088, Q-0094, Q-0095, Q-0102, Q-0105

## Left out: forecast on or after the resolution date

Q-0037 (edition 02), Q-0049 (edition 02), Q-0080 (edition 02)

## Diagnostics (not the official measure)

Methodology §1 keeps BSS vs status quo and vs the crowd as the official measures. These lines show how hard those baselines are and how independent the lenses are.

### YES rate by p_status_quo (scored questions)

| p_status_quo | N questions | YES rate |
|---|---|---|
| 0.10 | 54 | 0.44 |
| 0.50 | 7 | 0.71 |
| 0.90 | 4 | 0.50 |

### AGG_RT against other reference baselines

| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |
|---|---|---|---|---|
| status quo (official) | 77 | 0.173 | 0.375 | 0.538 |
| constant 0.50 | 77 | 0.173 | 0.250 | 0.308 |
| YES rate of earlier resolutions (≥ 10) | 36 | 0.154 | 0.255 | 0.395 |
| previous edition's AGG_RT | 12 | 0.186 | 0.248 | 0.250 |

### Lens diversity by edition (all forecasts, resolved or not)

| Edition | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |
|---|---|---|---|---|---|---|
| 01 | 73 | 0.91 | 0.94 | 0.92 | 0.06 | 1 |
| 02 | 88 | 0.93 | 0.95 | 0.90 | 0.06 | 2 |

# Accuracy scores

Resolved and scored questions: **53** (of which auto-verified: 0) · awaiting verification: 14 · void: 0

## Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |
|---|---|---|---|---|---|
| A | 61 | 0.154 | 0.322 | 0.523 | 0.150 |
| B | 61 | 0.152 | 0.322 | 0.528 | 0.149 |
| C | 61 | 0.150 | 0.322 | 0.535 | 0.146 |
| AGG | 61 | 0.150 | 0.322 | 0.534 | 0.147 |
| AGG_RT | 61 | 0.150 | 0.322 | 0.536 | 0.146 |

## AGG_RT vs crowd (EXACT matches only)

N pairs: 15 · Brier AGG_RT: 0.121 · Brier crowd: 0.146 · BSS vs crowd: 0.171

## AGG_RT calibration

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 4 | 0.07 | 0.00 |
| 10–20% | 15 | 0.13 | 0.00 |
| 20–30% | 11 | 0.25 | 0.18 |
| 30–40% | 7 | 0.35 | 0.57 |
| 40–50% | 10 | 0.45 | 1.00 |
| 50–60% | 6 | 0.55 | 0.67 |
| 60–70% | 3 | 0.65 | 0.67 |
| 70–80% | 2 | 0.74 | 1.00 |
| 80–90% | 1 | 0.82 | 1.00 |
| 90–100% | 2 | 0.94 | 1.00 |

## AGG_RT directional bias (mean p − outcome; neutral ≈ 0)

| who_benefits | N | Mean signed error |
|---|---|---|
| US_WEST | 0 | n/a |
| EU | 0 | n/a |
| UKRAINE | 1 | 0.267 |
| RUSSIA | 2 | 0.177 |
| CHINA | 0 | n/a |
| IRAN | 0 | n/a |
| COMPROMISE | 6 | -0.183 |

## Clusters

| Group | N | Brier AGG_RT |
|---|---|---|
| BAB_EL_MANDAB | 3 | 0.239 |
| BG_ELECTIONS | 1 | 0.071 |
| BLACK_SEA | 1 | 0.218 |
| BRAZIL_ELECTIONS | 3 | 0.235 |
| CN_RARE_EARTHS | 3 | 0.065 |
| CN_SECONDARY_SANCTIONS | 1 | 0.194 |
| EASTERN_FLANK | 1 | 0.033 |
| EU_ENERGY | 5 | 0.281 |
| FOOD | 2 | 0.254 |
| HORMUZ | 4 | 0.093 |
| IRAN_WAR | 2 | 0.144 |
| KOREA | 1 | 0.303 |
| LATVIA_ELECTIONS | 1 | 0.033 |
| OIL_PRICE | 2 | 0.247 |
| OPEC | 1 | 0.080 |
| PLN | 2 | 0.180 |
| PL_FUELS | 2 | 0.079 |
| PL_INFLATION | 2 | 0.208 |
| RATES_FED | 2 | 0.071 |
| RATES_RU | 2 | 0.041 |
| RU_DOMESTIC | 1 | 0.004 |
| RU_FINANCE | 1 | 0.260 |
| RU_SANCTIONS_US | 3 | 0.030 |
| TAIWAN | 1 | 0.303 |
| UA_EU | 1 | 0.267 |
| UA_FRONT | 2 | 0.034 |
| UA_TALKS | 4 | 0.210 |
| UA_USA | 1 | 0.071 |
| US_CHINA_TRADE | 3 | 0.127 |
| US_ELECTIONS | 2 | 0.011 |
| US_EUROPE | 1 | 0.040 |

Brier AGG_RT with a weight of 1 per cluster: **0.143**

## Vectors

| Group | N | Brier AGG_RT |
|---|---|---|
| DIP | 7 | 0.170 |
| DOM | 8 | 0.104 |
| ECO | 8 | 0.165 |
| ENE | 10 | 0.214 |
| FIN | 10 | 0.111 |
| INF | 6 | 0.149 |
| MIL | 9 | 0.159 |
| TEC | 3 | 0.065 |

## Editions (forecast made in)

| Group | N | Brier AGG_RT |
|---|---|---|
| 01 | 36 | 0.156 |
| 02 | 25 | 0.140 |

## Framework versions (registry/editions.csv)

| Group | N | Brier AGG_RT |
|---|---|---|
| 1.0.0 | 36 | 0.156 |
| 1.4.0 | 25 | 0.140 |

## Horizons (from forecast date to deadline)

| Group | N | Brier AGG_RT |
|---|---|---|
| ≤100 days | 27 | 0.180 |
| ≤14 days | 34 | 0.125 |

## Awaiting user verification

Q-0025, Q-0039, Q-0042, Q-0049, Q-0065, Q-0079, Q-0083, Q-0084, Q-0087, Q-0088, Q-0094, Q-0095, Q-0102, Q-0105

## Left out: forecast on or after the resolution date

Q-0037 (edition 02), Q-0080 (edition 02)

## Diagnostics (not the official measure)

Methodology §1 keeps BSS vs status quo and vs the crowd as the official measures. These lines show how hard those baselines are and how independent the lenses are.

### YES rate by p_status_quo (scored questions)

| p_status_quo | N questions | YES rate |
|---|---|---|
| 0.10 | 43 | 0.40 |
| 0.50 | 6 | 0.67 |
| 0.90 | 3 | 0.67 |

### AGG_RT against other reference baselines

| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |
|---|---|---|---|---|
| status quo (official) | 61 | 0.150 | 0.322 | 0.536 |
| constant 0.50 | 61 | 0.150 | 0.250 | 0.402 |
| YES rate of earlier resolutions (≥ 10) | 25 | 0.140 | 0.281 | 0.502 |
| previous edition's AGG_RT | 9 | 0.174 | 0.161 | -0.082 |

### Lens diversity by edition (all forecasts, resolved or not)

| Edition | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |
|---|---|---|---|---|---|---|
| 01 | 73 | 0.91 | 0.94 | 0.92 | 0.06 | 1 |
| 02 | 88 | 0.93 | 0.95 | 0.90 | 0.06 | 2 |

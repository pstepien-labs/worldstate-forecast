# Accuracy scores

Resolved and scored questions: **17** · awaiting user verification: 10 · void: 0

> Fewer than 30 resolved questions — indicative scores, no conclusions about the method.

## Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |
|---|---|---|---|---|---|
| A | 17 | 0.121 | 0.302 | 0.600 | 0.121 |
| B | 17 | 0.117 | 0.302 | 0.611 | 0.117 |
| C | 17 | 0.122 | 0.302 | 0.595 | 0.122 |
| AGG | 17 | 0.118 | 0.302 | 0.610 | 0.118 |
| AGG_RT | 17 | 0.117 | 0.302 | 0.613 | 0.117 |

## AGG_RT vs crowd (EXACT matches only)

N pairs: 3 · Brier AGG_RT: 0.014 · Brier crowd: 0.005 · BSS vs crowd: -1.974

## AGG_RT calibration

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 1 | 0.06 | 0.00 |
| 10–20% | 3 | 0.14 | 0.00 |
| 20–30% | 4 | 0.24 | 0.00 |
| 30–40% | 2 | 0.38 | 0.50 |
| 40–50% | 3 | 0.45 | 1.00 |
| 50–60% | 1 | 0.56 | 1.00 |
| 60–70% | 0 | n/a | n/a |
| 70–80% | 0 | n/a | n/a |
| 80–90% | 1 | 0.82 | 1.00 |
| 90–100% | 2 | 0.94 | 1.00 |

## AGG_RT directional bias (mean p − outcome; neutral ≈ 0)

| who_benefits | N | Mean signed error |
|---|---|---|
| US_WEST | 0 | n/a |
| EU | 0 | n/a |
| UKRAINE | 1 | 0.267 |
| RUSSIA | 0 | n/a |
| CHINA | 0 | n/a |
| IRAN | 0 | n/a |
| COMPROMISE | 1 | 0.117 |

## Clusters

| Group | N | Brier AGG_RT |
|---|---|---|
| BAB_EL_MANDAB | 1 | 0.401 |
| BRAZIL_ELECTIONS | 1 | 0.004 |
| CN_SECONDARY_SANCTIONS | 1 | 0.194 |
| EASTERN_FLANK | 1 | 0.033 |
| KOREA | 1 | 0.303 |
| LATVIA_ELECTIONS | 1 | 0.033 |
| OPEC | 1 | 0.080 |
| PLN | 1 | 0.295 |
| PL_FUELS | 1 | 0.147 |
| PL_INFLATION | 1 | 0.003 |
| RU_DOMESTIC | 1 | 0.004 |
| RU_SANCTIONS_US | 1 | 0.047 |
| TAIWAN | 1 | 0.303 |
| UA_TALKS | 1 | 0.014 |
| UA_USA | 1 | 0.071 |
| US_CHINA_TRADE | 1 | 0.017 |
| US_EUROPE | 1 | 0.040 |

Brier AGG_RT with a weight of 1 per cluster: **0.117**

## Vectors

| Group | N | Brier AGG_RT |
|---|---|---|
| DIP | 2 | 0.042 |
| DOM | 3 | 0.014 |
| ECO | 2 | 0.010 |
| ENE | 2 | 0.113 |
| FIN | 3 | 0.179 |
| MIL | 5 | 0.216 |

## Editions (forecast made in)

| Group | N | Brier AGG_RT |
|---|---|---|
| 01 | 17 | 0.117 |

## Framework versions (registry/editions.csv)

| Group | N | Brier AGG_RT |
|---|---|---|
| 1.0.0 | 17 | 0.117 |

## Horizons (from forecast date to deadline)

| Group | N | Brier AGG_RT |
|---|---|---|
| ≤100 days | 1 | 0.033 |
| ≤14 days | 16 | 0.122 |

## Awaiting user verification

Q-0006, Q-0011, Q-0014, Q-0041, Q-0042, Q-0048, Q-0053, Q-0058, Q-0062, Q-0063

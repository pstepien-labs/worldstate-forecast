# QNT back-test (framework 1.9, WP-10)

QNT computed for resolved mapped questions from harvested data up to the date of each edition's forecasts, scored against that edition's runs. Legitimate as a back-test because the method uses no model knowledge, only the data before the forecast date. Small N: indicative only.

| Question | Edition | Outcome | QNT | A | B | C | AGG_RT | note |
|---|---|---|---|---|---|---|---|---|
| Q-0006 | 01 | 1 | 0.96 | 0.35 | 0.45 | 0.40 | 0.40 |  |
| Q-0052 | 01 | 1 | 0.57 | 0.45 | 0.47 | 0.45 | 0.46 |  |
| Q-0074 | 02 | 1 | 0.99 | 0.65 | 0.65 | 0.60 | 0.63 |  |
| Q-0086 | 02 | 0 | 0.21 | 0.22 | 0.25 | 0.30 | 0.26 |  |

| Run | N | Brier (same questions) |
|---|---|---|
| QNT | 4 | 0.058 |
| A | 4 | 0.224 |
| B | 4 | 0.192 |
| C | 4 | 0.228 |
| AGG_RT | 4 | 0.214 |

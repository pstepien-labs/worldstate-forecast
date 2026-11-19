# L2 — Forecast performance (scope `latest`)

Run: 19.11.2026 · stage L2 · framework 1.9.2 · methodology v1.0 · model claude-opus-5-5 · commit at start 02ec5b4 · unattended autopilot run (AUTO mode of `prompts/RUN_learning.md`).

**Scope resolution.** `latest` was resolved to the **forecasts made in edition 02** (state date 07.10.2026, forecasts dated 09.10.2026). This is the latest edition with scored resolutions. Edition 03 (state date 16.11.2026) is the latest closed edition, but none of its 83 questions has a resolution yet: all 83 deadlines are still open (18 in XI, 39 in XII 2026, 26 in 2027). For edition 03 this file reports only lens diversity (§3.3), which needs no outcomes. This matches the L1 choice of the same folder (L1 audited edition 02).

**Questions covered.** Edition 02 forecast 88 questions. As of 19.11.2026:
- **36 questions scored** (the official set below).
- 3 were left out because the edition 02 forecast was made on or after the resolution date: Q-0037, Q-0049, Q-0080 (framework 1.5 rule in `tools/scores.py`).
- 1 is awaiting verification and is not scored: Q-0079 (BAB_EL_MANDAB; stage V dispute, `user_approved = N`).
- 48 are unresolved with open deadlines.

Of the 36 scored questions, 12 resolutions are **auto-verified** (stage V agreement, `user_approved = A`, not reviewed by the user): Q-0025, Q-0039, Q-0042, Q-0065, Q-0083, Q-0084, Q-0087, Q-0088, Q-0094, Q-0095, Q-0102, Q-0105. The other 24 had no VERIFY flag. Resolutions come from stage 01 of edition 03 (16.11.2026) and from interim stage I.

**Sample size.** N = 36 scored questions in 26 clusters. That is above the threshold of 30 for the headline measure (AGG_RT vs status quo). Every subgroup (vector, cluster, horizon, confidence, calibration bin, crowd pairs) has N < 30 and is **indicative only** (learning rule 2). The line "Resolved and scored questions: 66" in the `scores.py` output counts every edition in the registry, not this scope.

**Versions.** All forecasting stages of edition 02 (03, 04 A/B/C, 05, 06) ran under **framework 1.4.0**, methodology v1.0, model **claude-opus-5-5** (`editions/2026-10-07_edition-02/provenance.md`). Only stage E ran under 1.6.0, and it does not touch forecasts. The scope therefore holds **one framework version and one model**. Edition 01 (framework 1.0.0, model "not recorded") appears only as context in §6, where it is clearly marked.

Read-only: no edition file, forecast, resolution or registry row was changed (learning rule 4). The tables are copied from `python3 tools/scores.py --editions 02` and `--framework 1.4.0`, which give identical output for this scope. Breakdowns that `scores.py` does not print were computed with one-off commands using the same selection rules and the same `cluster_boot` function (2000 resamples, fixed seed 20261117). Those commands were not saved in the repository.

---

## 1. Scores (edition 02, framework 1.4.0)

### 1.1 Runs

| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | 90% interval of Brier (cluster bootstrap) | 90% interval of BSS vs SQ |
|---|---|---|---|---|---|---|
| A | 36 | 0.159 | 0.357 | 0.554 | [0.113, 0.207] | [0.346, 0.687] |
| B | 36 | 0.159 | 0.357 | 0.554 | [0.111, 0.209] | [0.335, 0.686] |
| C | 36 | 0.157 | 0.357 | 0.560 | [0.114, 0.202] | [0.353, 0.691] |
| AGG | 36 | 0.156 | 0.357 | 0.562 | [0.112, 0.203] | [0.354, 0.691] |
| **AGG_RT** | 36 | **0.154** | 0.357 | **0.568** | [0.108, 0.201] | [0.363, 0.696] |
| derived: log-odds mean | 36 | 0.156 | 0.357 | 0.563 | [0.111, 0.202] | [0.356, 0.692] |
| derived: log-odds ×1.5 | 36 | 0.162 | 0.357 | 0.547 | [0.103, 0.221] | [0.314, 0.702] |
| derived: median | 36 | 0.160 | 0.357 | 0.552 | [0.114, 0.207] | [0.342, 0.683] |

The derived runs are computed by `scores.py` from A, B and C at scoring time. They are diagnostics, not registry runs. Shadow runs B2 and QNT do not exist in scope: they began with framework 1.9, after edition 02, and edition 03 (framework 1.8.0) has none either.

Brier of AGG_RT with weight 1 per cluster: **0.158**. Status quo with the same weighting: 0.331 (26 clusters).

### 1.2 AGG_RT calibration (10-point bins)

| Bin | N | Mean p | YES frequency |
|---|---|---|---|
| 0–10% | 3 | 0.08 | 0.00 |
| 10–20% | 10 | 0.13 | 0.00 |
| 20–30% | 6 | 0.27 | 0.33 |
| 30–40% | 3 | 0.35 | 1.00 |
| 40–50% | 5 | 0.46 | 0.80 |
| 50–60% | 3 | 0.54 | 0.67 |
| 60–70% | 2 | 0.64 | 0.50 |
| 70–80% | 2 | 0.74 | 1.00 |
| 80–90% | 0 | n/a | n/a |
| 90–100% | 2 | 0.91 | 1.00 |

### 1.3 Vectors, horizons, clusters (AGG_RT)

| Vector | N | Brier AGG_RT | Mean p | YES rate | Mean p − YES rate |
|---|---|---|---|---|---|
| DIP | 4 | 0.201 | 0.24 | 0.50 | −0.26 |
| DOM | 5 | 0.211 | 0.31 | 0.40 | −0.09 |
| ECO | 3 | 0.248 | 0.44 | 0.00 | +0.44 |
| ENE | 5 | 0.173 | 0.32 | 0.60 | −0.28 |
| FIN | 7 | 0.087 | 0.29 | 0.29 | +0.01 |
| INF | 4 | 0.071 | 0.44 | 0.50 | −0.06 |
| MIL | 4 | 0.200 | 0.31 | 0.50 | −0.19 |
| TEC | 4 | 0.097 | 0.54 | 0.75 | −0.21 |

| Horizon (forecast date → deadline) | N | Brier AGG_RT | Brier SQ | Mean p | YES rate |
|---|---|---|---|---|---|
| ≤14 days | 15 | 0.068 | 0.170 | 0.28 | 0.27 |
| ≤100 days | 21 | 0.216 | 0.490 | 0.40 | 0.57 |

| Cluster | N | Brier AGG_RT |
|---|---|---|
| BAB_EL_MANDAB | 1 | 0.054 |
| BG_ELECTIONS | 1 | 0.071 |
| BLACK_SEA | 1 | 0.218 |
| BRAZIL_ELECTIONS | 1 | 0.504 |
| CN_RARE_EARTHS | 3 | 0.109 |
| EU_ENERGY | 3 | 0.239 |
| FOOD | 1 | 0.314 |
| HORMUZ | 2 | 0.009 |
| IL_ELECTIONS | 1 | 0.284 |
| IRAN_WAR | 2 | 0.353 |
| OIL_PRICE | 1 | 0.135 |
| PANAMA | 1 | 0.006 |
| PLN | 1 | 0.066 |
| PL_FINANCE | 1 | 0.453 |
| PL_FUELS | 1 | 0.012 |
| PL_INFLATION | 1 | 0.413 |
| RATES_FED | 1 | 0.031 |
| RATES_RU | 2 | 0.014 |
| RU_SANCTIONS_EU | 1 | 0.010 |
| RU_SANCTIONS_US | 2 | 0.021 |
| TAIWAN | 1 | 0.077 |
| UA_EU | 1 | 0.267 |
| UA_FRONT | 1 | 0.016 |
| UA_TALKS | 2 | 0.263 |
| US_CHINA_TECH | 1 | 0.062 |
| US_ELECTIONS | 2 | 0.097 |

### 1.4 Directional bias (`who_benefits`, mean p − outcome)

| who_benefits | N | Mean signed error |
|---|---|---|
| US_WEST, UKRAINE, CHINA, IRAN | 0 | n/a |
| EU | 1 | −0.100 |
| RUSSIA | 1 | +0.127 |
| COMPROMISE | 3 | −0.117 |
| NONE (not in the `scores.py` table; one-off) | 31 | −0.10 (mean p 0.32, YES rate 0.42) |

31 of 36 scored questions carry `who_benefits = NONE`. With 5 directional questions **no directional bias can be measured** in this scope.

---

## 2. Against baselines

### 2.1 Status quo (official measure, methodology §1)

- AGG_RT Brier 0.154 vs status quo 0.357. **BSS 0.568, 90% cluster interval [0.363, 0.696]** (N = 36, 26 clusters).
- Paired mean Brier difference AGG_RT − SQ: **−0.202**, 90% interval [−0.308, −0.093], 95% interval [−0.330, −0.070]. The interval excludes zero, so the official forecast beats the status quo in this scope.
- By count, AGG_RT was closer to the outcome than SQ on 19 questions and further on 17. The mean gain comes from a minority of questions where SQ = 0.10 and the event happened (each such miss costs SQ 0.81).
- Closed cohort (deadline before 19.11.2026, which removes the early-YES selection): N = 28, YES rate 0.36, Brier AGG_RT 0.116 vs SQ 0.227, **BSS 0.488**.

### 2.2 Crowd (EXACT matches only)

N pairs = 9. Brier AGG_RT 0.165 vs crowd 0.156, **BSS vs crowd −0.059**, paired mean difference +0.009. `scores.py` has no bootstrap for the crowd. With N = 9 there is **no evidence of a difference** in either direction. (Cumulative editions 01–02: N = 18, BSS vs crowd +0.116. Context only, mixed versions.)

### 2.3 Diagnostics (framework 1.5; evidence for P-0007)

YES rate by `p_status_quo` (scored questions in scope):

| p_status_quo | N questions | YES rate |
|---|---|---|
| 0.10 | 30 | 0.43 |
| 0.50 | 2 | 0.50 |
| 0.90 | 4 | 0.50 |

**The status-quo baseline is weak.** Of the questions written with SQ = 0.10, 13 of 30 (43%) resolved YES. Of those written with SQ = 0.90, 2 of 4 resolved NO. The question-writing process produces many questions where change is close to a coin flip, and the mechanical SQ scores them as near-certain.

AGG_RT against other reference baselines:

| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |
|---|---|---|---|---|
| status quo (official) | 36 | 0.154 | 0.357 | 0.568 |
| constant 0.50 | 36 | 0.154 | 0.250 | 0.383 |
| YES rate of earlier resolutions (≥ 10) | 36 | 0.154 | 0.255 | 0.395 |
| previous edition's AGG_RT (same question, edition 01) | 12 | 0.186 | 0.248 | 0.250 |

- Against the constant 0.50 and the running YES rate, AGG_RT still keeps a positive BSS of about 0.38–0.40. Roughly a third of the headline BSS vs SQ (0.568) reflects how weak the SQ baseline is, not skill.
- **Did updating help?** On the 12 questions forecast in both editions (10 clusters), the paired mean difference edition 02 − edition 01 AGG_RT was −0.062, 90% interval [−0.188, +0.044]. The interval includes zero: **no evidence of a difference**. 9 of 12 forecasts moved toward the outcome, 2 moved away (Q-0026, Q-0033) and 1 was unchanged (Q-0031). The two moves away are the two largest errors of the edition (§7).

---

## 3. Pipeline components

### 3.1 Lenses and aggregation (paired cluster bootstrap, N = 36, 26 clusters, 95% interval)

| Comparison | Mean Brier difference | 95% interval | Reading |
|---|---|---|---|
| A − B | −0.000 | [−0.024, 0.023] | no evidence of a difference |
| A − C | +0.002 | [−0.016, 0.018] | no evidence of a difference |
| B − C | +0.002 | [−0.018, 0.026] | no evidence of a difference |
| AGG − C (best single lens, Brier 0.157) | −0.001 | [−0.010, 0.011] | no evidence that aggregation helps |
| AGG_RT − AGG | −0.002 | [−0.005, 0.000] (90%: [−0.0046, −0.0003]) | see 3.2 |

- Best lens: C (0.157). Worst lenses: A and B (0.159). The gap is 0.002 and well inside the intervals.
- Paired differences against AGG_RT, from the `scores.py` diagnostics (90% intervals):
  - log-odds mean: +0.001 [0.000, 0.003]
  - median: +0.006 [0.001, 0.010]. The median of the lenses was slightly worse than the official forecast; this interval excludes zero.
  - log-odds ×1.5 (extremised): +0.007 [−0.006, 0.021]

### 3.2 Red team (AGG_RT vs AGG)

- In edition 02 the red team changed **4 of 36** scored forecasts: Q-0004, Q-0066, Q-0090 and Q-0091. All four were lowered and all four resolved NO. The paired difference is −0.002: the 90% interval [−0.0046, −0.0003] excludes zero, and the 95% interval [−0.005, 0.000] touches it.
- Edition 01 (context, framework 1.0.0) shows the opposite sign: 6 changes, +0.004, 90% interval [−0.001, +0.010]. Pooled editions 01–02: +0.001, 95% interval [−0.002, +0.006], N = 77, 36 clusters.
- Reading: the edition 02 gain is tiny (about 1% of the Brier) and rests on 4 questions. **No evidence of a general red-team effect.**

### 3.3 Lens diversity by edition (all forecasts, resolved or not; evidence for P-0008)

| Edition | Framework | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |
|---|---|---|---|---|---|---|---|
| 01 | 1.0.0 | 73 | 0.91 | 0.94 | 0.92 | 0.06 | 1 |
| 02 | 1.4.0 | 88 | 0.93 | 0.95 | 0.90 | 0.06 | 2 |
| 03 | 1.8.0 | 83 | 0.91 | 0.96 | 0.94 | 0.05 | 4 |

On the 36 scored questions of edition 02, the median spread (max − min of A, B, C) was 0.06 and the largest was 0.26. Every pairwise correlation is ≥ 0.90 in all three editions. Edition 03 is the first to show more than two questions with a spread above 0.30 (4 of 83), but the median spread fell to 0.05. Near-identical lenses cannot gain from averaging, and the AGG vs best-lens result in 3.1 is consistent with that.

---

## 4. Where it fails (indicative; every subgroup N < 30)

- **Horizon.** Brier ≤100 days 0.216 (N = 21) vs ≤14 days 0.068 (N = 15). The difference of +0.148 has a 90% interval of [0.074, 0.224]. But measured against the status quo, the difference (Brier − SQ, long − short) is −0.172, 90% interval [−0.349, +0.026], which includes zero. Long-horizon questions are harder. There is **no evidence that skill relative to SQ is lower** at long horizons.
- **Resolution timing.** Mean p − YES rate is −0.17 at ≤100 days, mostly because YES resolves early and NO only at the deadline. In the closed cohort the gap is −0.01 (mean p 0.35, YES rate 0.36, N = 28).
- **Analytic confidence.**

  | Confidence | N | Brier | Brier SQ | Mean p | YES rate |
  |---|---|---|---|---|---|
  | high | 2 | 0.007 | 0.410 | 0.48 | 0.50 |
  | medium | 15 | 0.080 | 0.223 | 0.30 | 0.27 |
  | low | 19 | 0.228 | 0.456 | 0.38 | 0.58 |

  The low − medium difference in raw Brier is +0.147, 90% interval [0.045, 0.235]. Relative to SQ it is −0.086, 90% interval [−0.276, +0.109]. Confidence ranks absolute accuracy as intended: the medium and high forecasts were more accurate. It does this by tracking question difficulty, though, and there is no evidence of a difference in skill over SQ between levels. Edition 01 (context) shows the same order: low 0.256 (N = 27) vs medium 0.061 (N = 14).
- **Question type.** OPEN: N = 24, Brier 0.122 (SQ 0.330). PANEL: N = 12, Brier 0.219 (SQ 0.410).
- **Vectors.** ECO (N = 3) is the only vector where AGG_RT over-forecast YES (+0.44). Two of its three questions are economic-data thresholds that resolved NO: Q-0075 (Polish CPI flash) and Q-0076 (FAO index). ENE, DIP, TEC and MIL under-forecast change (−0.19 to −0.28), each with N = 4–5. Only FIN (N = 7) is close to unbiased.
- **Clusters.** The worst were BRAZIL_ELECTIONS (0.504, N = 1), PL_FINANCE (0.453, N = 1), PL_INFLATION (0.413, N = 1), IRAN_WAR (0.353, N = 2), FOOD (0.314, N = 1) and UA_TALKS (0.263, N = 2). No cluster has N > 3, so no cluster-level rule is allowed (overfitting check).
- **Model.** One model (claude-opus-5-5) for every forecasting stage. **No model comparison is possible.**

---

## 5. Calibration (edition 02, AGG_RT)

- **Shape.** Forecasts in 10–20% resolved YES 0 times in 10. Forecasts in 30–50% resolved YES 7 times in 8.
  - The ordering is right: higher p, more YES.
  - Both groups are miscalibrated toward the middle. The low forecasts were too high and the 30–50% forecasts too low. This points to **under-confidence (compression)** in the 0.10–0.50 range. It is indicative only: N = 18 across these bins.
  - Some of the 30–50% YES outcomes are long-horizon questions that resolved early (§4), so part of the pattern is timing selection.
- **Extremes** (p ≤ 0.10 or ≥ 0.90): **5 forecasts, 0 wrong**. Q-0039 and Q-0083 resolved YES. Q-0067, Q-0078 and Q-0088 resolved NO. Edition 01 (context): 4 extremes, 0 wrong.
- **Mean.** Mean p 0.35 vs YES rate 0.44 on the full set (−0.09). On the closed cohort it is −0.01, so there is no overall level bias once the timing selection is removed.

---

## 6. Version comparison

**Not applicable within scope.** Every forecasting stage in scope ran under framework 1.4.0.

Context only, outside scope: edition 01 (framework 1.0.0) scored 0.189 on 41 questions and edition 02 scored 0.154 on 36. The question sets differ and so do their horizon mixes, so this is not a like-for-like comparison. The only like-for-like set is the 12 questions forecast in both editions (§2.3). There the difference is −0.062, 90% interval [−0.188, +0.044]. The interval includes zero, and the difference is also confounded with the information update between 23.09 and 09.10. **No difference may be attributed to the version change.**

---

## 7. Input list for L3

### 7.1 Ten largest errors (highest AGG_RT Brier, edition 02)

| # | Question | Cluster / vector | Confidence | A / B / C | SQ | Outcome (resolution date) | Brier | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | Q-0026 US–UA–RU trilateral of government delegations by 30.11 | UA_TALKS / DIP | low | 0.30 / 0.30 / 0.25 | 0.10 | YES (10.11) | 0.514 | Lowered from edition 01; L1 §4: rested on Ryabkov 07.10, reversed 22.10 |
| 2 | Q-0033 Lula wins the 2026 Brazilian presidential election | BRAZIL_ELECTIONS / DOM | medium | 0.30 / 0.25 / 0.32 | 0.90 | YES (25.10) | 0.504 | Moved against SQ and away from edition 01; all three lenses agreed |
| 3 | Q-0105 S&P downgrade or negative outlook for Poland by 06.11 | PL_FINANCE / FIN | low | 0.40 / 0.28 / 0.30 | 0.10 | YES (06.11; auto-verified) | 0.453 | L1 surprise #1 (Tribunal crisis) is related |
| 4 | Q-0065 CENTCOM/Pentagon announces a US strike on Iranian land by 31.12 | IRAN_WAR / MIL | low | 0.33 / 0.32 / 0.40 | 0.10 | YES (06.11; auto-verified) | 0.423 | L1 KA1 failed by one day |
| 5 | Q-0075 Polish October CPI flash below 3.5% y/y | PL_INFLATION / ECO | medium | 0.68 / 0.65 / 0.60 | 0.10 | NO (31.10) | 0.413 | Data threshold |
| 6 | Q-0009 TTF front-month above 90 EUR/MWh by 31.12 | EU_ENERGY / ENE | low | 0.33 / 0.45 / 0.33 | 0.10 | YES (22.10) | 0.397 | Raised from edition 01, but not enough |
| 7 | Q-0084 TTF front-month above 80.00 EUR/MWh on 20.10 | EU_ENERGY / ENE | low | 0.36 / 0.50 / 0.45 | 0.10 | YES (20.10; auto-verified) | 0.317 | Same cluster as #6 |
| 8 | Q-0076 FAO Food Price Index for October above 136.0 | FOOD / ECO | low | 0.55 / 0.58 / 0.55 | 0.10 | NO (09.11) | 0.314 | Data threshold |
| 9 | Q-0094 Likud wins the most Knesset seats on 27.10 | IL_ELECTIONS / DOM | low | 0.45 / 0.47 / 0.48 | 0.50 | YES (30.10; auto-verified) | 0.284 | Close to SQ; low-information miss |
| 10 | Q-0099 USNI shows ≥ 3 US carriers in the CENTCOM area | IRAN_WAR / MIL | low | 0.45 / 0.45 / 0.50 | 0.10 | YES (16.11) | 0.284 | L1 fact #5: a declared third carrier group became a fact |

The A / B / C values are lens forecasts, given for L3's reasoning trace. In all 10 the three lenses were within 0.14 of each other: **the misses were shared, not lens-specific**. The widest spreads are in #7 (0.14), #3 (0.12) and #6 (0.12).

### 7.2 Ten best calls (lowest Brier among |p − p_status_quo| ≥ 0.20; 19 questions eligible)

| # | Question | Cluster / vector | Confidence | SQ | Outcome (resolution date) | Brier |
|---|---|---|---|---|---|---|
| 1 | Q-0039 Panama Canal daily transit limit above 32 by 31.10 | PANAMA / INF | medium | 0.10 | YES (15.10; auto-verified) | 0.006 |
| 2 | Q-0083 EU lists ≥ 1,500 new persons and entities by 21.10 | RU_SANCTIONS_EU / FIN | high | 0.10 | YES (12.10; auto-verified) | 0.010 |
| 3 | Q-0031 Republicans win ≥ 218 House seats on 03.11 | US_ELECTIONS / DOM | medium | 0.90 | NO (04.11) | 0.011 |
| 4 | Q-0102 BIS extends or rescinds the Affiliates rule suspension by 09.11 | US_CHINA_TECH / TEC | medium | 0.10 | YES (09.11; auto-verified) | 0.062 |
| 5 | Q-0021 PRC extends or repeals the rare-earth control suspension by 10.11 | CN_RARE_EARTHS / TEC | medium | 0.10 | YES (09.11) | 0.068 |
| 6 | Q-0093 Iotova above 50% in Bulgaria's first round, 25.10 | BG_ELECTIONS / DOM | low | 0.50 | NO (31.10) | 0.071 |
| 7 | Q-0074 Brent front-month above 100.00 USD/bbl on 20.10 | OIL_PRICE / ENE | low | 0.90 | YES (20.10) | 0.135 |
| 8 | Q-0095 Republicans hold ≥ 50 Senate seats after 03.11 | US_ELECTIONS / DOM | low | 0.90 | NO (04.11; auto-verified) | 0.182 |
| 9 | Q-0098 Romania, Bulgaria or Türkiye confirm a drone or missile hit on a merchant ship | BLACK_SEA / INF | low | 0.10 | YES (28.10) | 0.218 |
| 10 | Q-0025 PRC magnet exports to the USA in September above 512 t | CN_RARE_EARTHS / TEC | low | 0.10 | YES (20.10; auto-verified) | 0.233 |

Only #1–#6 are clear hits (Brier ≤ 0.071). Items #7–#10 departed from SQ in the right direction but stayed near 0.5. Q-0039 is also the largest update between editions: the edition 01 forecast was far from the outcome (§2.3).

---

## 8. Findings (at most 5)

1. **The official forecast beats the status quo, but a third of that margin reflects a weak baseline.** BSS vs SQ is 0.568 (90% [0.363, 0.696]; N = 36, 26 clusters). The paired difference is −0.202 (90% [−0.308, −0.093]).
   - At SQ = 0.10, 13 of 30 questions resolved YES.
   - Against a constant 0.50 the BSS is 0.383 (N = 36), and against the running YES rate it is 0.395 (N = 36).
   - Against the crowd: N = 9, BSS −0.059, no bootstrap available. **No evidence of a difference.**
   - Evidence for P-0007.
2. **Aggregation adds nothing measurable, because the lenses barely differ.** AGG − best lens (C) is −0.001 (95% [−0.010, 0.011]). Every pairwise lens difference has an interval including zero (N = 36). Correlations are 0.90–0.96 and the median spread is 0.05–0.06 in editions 01, 02 and 03 (73, 88 and 83 questions). **No evidence of a difference.** Evidence for P-0008.
3. **The red team has no demonstrated general effect.** In edition 02 it changed 4 of 36 forecasts, all downward and all correct: −0.002 (90% [−0.0046, −0.0003]; 95% touches 0). In edition 01 the sign is opposite (+0.004), and pooled 01–02 it is +0.001 (95% [−0.002, 0.006], N = 77). **No evidence of a difference** across editions.
4. **Compression in the 0.10–0.50 range, with clean extremes (indicative).** Forecasts in 10–20% went 0 of 10 YES and forecasts in 30–50% went 7 of 8 YES (N = 18). The 5 extreme forecasts were all right. The overall level bias disappears in the closed cohort (−0.01, N = 28), so the full-set gap of −0.09 is resolution-timing selection, not bias.
5. **Errors concentrate on long horizons, low confidence and shared lens judgements, not on lower skill (indicative).**
   - Raw Brier, long vs short horizon: +0.148 (90% [0.074, 0.224]). Raw Brier, low vs medium confidence: +0.147 (90% [0.045, 0.235]).
   - Relative to SQ, both differences have intervals including zero: **no evidence of lower skill**.
   - All ten largest errors were shared by the three lenses (spread ≤ 0.14).
   - Two of the ten were updates away from the outcome between editions: Q-0026 and Q-0033.
   - Two rested on a single government course that later reversed: Q-0026 and Q-0065 (L1 lesson 2).

---

## 9. Process notes

- Provenance: `python3 tools/pipeline.py stage-start L2 --arg latest --model "claude-opus-5-5"` (19.11.2026, commit 02ec5b4) … `stage-end L2 --arg latest`.
- Commands:
  - `python3 tools/scores.py` (all editions, for context)
  - `--editions 02`
  - `--framework 1.4.0` (identical to `--editions 02`)
  - `--editions 02 --bootstrap` for A B, A C, B C, AGG_RT AGG, AGG C and AGG_RT C
  - `--editions 01,02 --bootstrap AGG_RT AGG`
- One-off breakdowns: confidence, type, extremes, the paired AGG_RT − SQ interval, the updating pairs, the group-difference intervals, and the error and best-call lists. They used scratch scripts in the git-ignored `data/` folder, which were deleted after the run.
- Data used: `registry/forecasts.csv`, `questions.csv`, `resolutions.csv`, `benchmarks.csv` (via `scores.py` only), `editions.csv`, the edition 02 `provenance.md` and L1 of this folder. No web search was needed. No forecasting service or market was visited.
- Gaps:
  - `scores.py` gives no bootstrap for the crowd comparison and no analytic-confidence breakdown. Both were handled as described above.
  - The `scores.py` header counts resolutions of all editions (66), not the scope (36).
  - 12 of the 36 scored resolutions are auto-verified, not user-reviewed.
  - Q-0079 is still disputed and unscored.

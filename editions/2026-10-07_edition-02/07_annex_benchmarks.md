# Annex: comparison with the crowd and markets — edition 02 (state 07.10.2026)

> **File forbidden to stages 03, 04 and 05 in all future editions** (CLAUDE.md item 8). It is not part of the main report (methodology §6). Material for reviewing the method, not grounds for changing forecasts.

Framework 1.4.0 · methodology v1.0 · commit 75c4c51 · models: claude-opus-5-5

Source: `06_benchmarks.md` and `registry/benchmarks.csv` (edition 02: 68 rows for 40 questions; 32 EXACT rows for 16 questions). Quotes were collected **after** the "forecasts frozen" commit (f09a1d4): Polymarket, Kalshi and Manifold on 09.10.2026 at about 23:40–23:55 Warsaw time, Good Judgment Open on 10.10.2026 at about 02:20–02:40. No forecast was changed. Δ = crowd − AGG_RT. Where a question has several sources, `scores.py` averages them — and so does the "crowd (mean)" column.

## 0. Score against the crowd (from `01_scores.md`)

AGG_RT vs crowd on resolved questions with an EXACT match (edition 01 forecasts, resolved in stage 01 of this edition, VERIFY flags excluded): **N = 3** pairs (Q-0054, Q-0055, Q-0056) · Brier AGG_RT 0.014 · Brier crowd 0.005 · **BSS vs crowd −1.974**. With three pairs, all of them questions both sides judged with high confidence, the number is not informative; it is recorded for the series. Pending among the edition 01 EXACT pairs: Q-0006 (resolved, awaiting the user's verification), Q-0037 (deadline passed, data missing); the others have later deadlines.

## 1. Access to sources

| Source | Access | Rows |
|---|---|---|
| Polymarket | public read-only API | 32 |
| Kalshi | public read-only API | 18 |
| Manifold | public API (play currency, usually low liquidity) | 10 |
| Good Judgment Open | public challenge pages and site-restricted web searches, no login (the full question list needs a login) | 8 |
| Metaculus | API requires an account (HTTP 403); no login | 0 |
| RAND Forecasting Initiative | platform closed (edition 01 finding; not re-checked) | 0 |

Of the six sources in methodology §6, four were read — as in edition 01. Note for the quarterly review.

## 2. Questions with an EXACT match (enter the BSS vs crowd once resolved)

| ID | Question (short) | Deadline | AGG_RT | Sources (p) | Crowd (mean) | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Russian mobilisation decree by 31.12 | 31.12.2026 | 0.030 | Manifold 0.305 | 0.305 | **+0.28** |
| Q-0020 | Bank of Russia cuts on 23.10 | 23.10.2026 | 0.143 | Polymarket 0.125; Kalshi 0.135 | 0.130 | −0.01 |
| Q-0027 | NATO Art. 4 request by 31.12 | 31.12.2026 | 0.107 | Polymarket 0.255 | 0.255 | +0.15 |
| Q-0028 | US–Iran agreement opening Hormuz by 31.12 | 31.12.2026 | 0.157 | Polymarket 0.355 | 0.355 | +0.20 (0.198, below the threshold) |
| Q-0031 | Republicans ≥ 218 House seats | 31.12.2026 | 0.107 | Polymarket 0.095; Kalshi 0.105; Manifold 0.070; GJO 0.204 | 0.118 | +0.01 |
| Q-0033 | Lula wins the presidency | 31.10.2026 | 0.290 | Polymarket 0.105; Kalshi 0.115; Manifold 0.140; GJO 0.260 | 0.155 | −0.14 |
| Q-0036 | Hormuz 7-day mean > 40 by 31.12 | 31.12.2026 | 0.103 | Kalshi 0.170 | 0.170 | +0.07 |
| Q-0038 | US lifts or suspends the Iran blockade by 31.12 | 31.12.2026 | 0.143 | Polymarket 0.479 | 0.479 | **+0.34** |
| Q-0066 | FOMC hike on 28.10 | 28.10.2026 | 0.177 | Polymarket 0.159; Kalshi 0.160; Manifold 0.180; GJO 0.158 | 0.164 | −0.01 |
| Q-0074 | Brent > 100 USD on 20.10 | 20.10.2026 | 0.633 | Kalshi 0.665 | 0.665 | +0.03 |
| Q-0076 | FAO FFPI for October > 136.0 | 09.11.2026 | 0.560 | Kalshi 0.350 | 0.350 | **−0.21** |
| Q-0088 | Bank of Russia hikes on 23.10 | 23.10.2026 | 0.083 | Polymarket 0.026; Kalshi 0.025 | 0.026 | −0.06 |
| Q-0094 | Likud the largest list on 27.10 | 06.11.2026 | 0.467 | Polymarket 0.515; Kalshi 0.505; Manifold 0.500 | 0.507 | +0.04 |
| Q-0095 | Republicans ≥ 50 Senate seats | 31.12.2026 | 0.427 | Polymarket 0.365; Kalshi 0.395; Manifold 0.345; GJO 0.470 | 0.394 | −0.03 |
| Q-0096 | Araghchi ceases to be FM by 31.12 | 31.12.2026 | 0.150 | Polymarket 0.115 | 0.115 | −0.04 |
| Q-0113 | ISW: Russia controls all of Kostiantynivka by 31.03.2027 | 31.03.2027 | 0.240 | Polymarket 0.410 | 0.410 | +0.17 |

Mean |Δ| over 16 questions: 0.11 (edition 01: 0.12 over 12). The crowd is above AGG_RT in 9 of 16 questions and below in 7. Discrepancies ≥ 0.20: 3 (Q-0038, Q-0001, Q-0076); Q-0028 sits just below the threshold. On the liquid markets with several sources (Q-0020, Q-0031, Q-0066, Q-0088, Q-0094, Q-0095) all differences are within 0.06. With n = 16 these are indicative observations, not conclusions about the method.

## 3. All matches (EXACT and APPROX)

| ID | Question (short) | AGG_RT | Source | Crowd p | Match | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Russian mobilisation decree by 31.12 | 0.030 | Polymarket (broader criterion) / Manifold | 0.100 / 0.305 | APPROX / EXACT | +0.07 / **+0.28** |
| Q-0007 | Brent > 120 USD on any day by 31.12 | 0.230 | GJO (EIA spot series, window from 19.07) | 0.840 | APPROX | **+0.61** |
| Q-0015 | US tariff on EU goods above the 15% ceiling | 0.103 | Kalshi (rate ≥ 20% on 01.01.2027) | 0.395 | APPROX | **+0.29** |
| Q-0016 | MPC changes the rate by 31.12 | 0.267 | Kalshi | 0.365 | APPROX | +0.10 |
| Q-0017 | ECB hike between 24.09 and 31.12 | 0.493 | Polymarket (XII) / Kalshi (XII) / GJO (X only) / GJO (XII only) | 0.773 / 0.785 / 0.193 / 0.406 | APPROX | **+0.28 / +0.29 / −0.30** / −0.09 |
| Q-0018 | PRC bank on the SDN list by 31.03.2027 | 0.077 | Kalshi | 0.255 | APPROX | +0.18 |
| Q-0020 | Bank of Russia cuts on 23.10 | 0.143 | Polymarket / Kalshi | 0.125 / 0.135 | EXACT | −0.02 / −0.01 |
| Q-0021 | PRC extends or repeals the rare-earth suspension by 10.11 | 0.740 | Manifold | 0.870 | APPROX | +0.13 |
| Q-0026 | Trilateral US–UA–RU meeting by 30.11 | 0.283 | Polymarket (any RU–UA meeting) / Kalshi (leaders) | 0.480 / 0.040 | APPROX | +0.20 (0.197) / **−0.24** |
| Q-0027 | NATO Art. 4 request by 31.12 | 0.107 | Polymarket | 0.255 | EXACT | +0.15 |
| Q-0028 | US–Iran agreement opening Hormuz by 31.12 | 0.157 | Polymarket / Kalshi (nuclear deal) | 0.355 / 0.115 | EXACT / APPROX | +0.20 (0.198) / −0.04 |
| Q-0029 | Trump at APEC Shenzhen | 0.643 | Polymarket | 0.810 | APPROX | +0.17 |
| Q-0030 | Putin–Trump meeting by 31.03.2027 | 0.317 | Polymarket (by 31.12) / Manifold | 0.810 / 0.274 | APPROX | **+0.49** / −0.04 |
| Q-0031 | Republicans ≥ 218 House seats | 0.107 | Polymarket / Kalshi / Manifold / GJO | 0.095 / 0.105 / 0.070 / 0.204 | EXACT | −0.01 / −0.00 / −0.04 / +0.10 |
| Q-0032 | New recording of Mojtaba Khamenei | 0.103 | Polymarket | 0.185 | APPROX | +0.08 |
| Q-0033 | Lula wins | 0.290 | Polymarket / Kalshi / Manifold / GJO | 0.105 / 0.115 / 0.140 / 0.260 | EXACT | −0.18 / −0.17 / −0.15 / −0.03 |
| Q-0034 | Venezuela election date by 31.03.2027 | 0.320 | Polymarket (by 31.12) | 0.105 | APPROX | **−0.22** |
| Q-0035 | Goïta loses power by 31.03.2027 | 0.070 | Polymarket | 0.050 | APPROX | −0.02 |
| Q-0036 | Hormuz 7-day mean > 40 by 31.12 | 0.103 | Kalshi / Polymarket ("normal") / GJO (≥ 35 by 11.01) | 0.170 / 0.175 / 0.150 | EXACT / APPROX / APPROX | +0.07 / +0.07 / +0.05 |
| Q-0038 | US lifts or suspends the blockade by 31.12 | 0.143 | Polymarket | 0.479 | EXACT | **+0.34** |
| Q-0065 | US strike on Iranian land by 31.12 | 0.350 | Polymarket (converted from a ceasefire-breakdown market) | 0.665 | APPROX | **+0.32** |
| Q-0066 | FOMC hike on 28.10 | 0.177 | Polymarket / Kalshi / Manifold / GJO | 0.159 / 0.160 / 0.180 / 0.158 | EXACT | −0.02 / −0.02 / +0.00 / −0.02 |
| Q-0068 | US strike on the Houthis by 31.12 | 0.233 | Polymarket | 0.170 | APPROX | −0.06 |
| Q-0069 | DSCA ≥ 1 bn USD for Taiwan by 31.12 | 0.120 | Manifold | 0.169 | APPROX | +0.05 |
| Q-0073 | Kramatorsk or Sloviansk by 30.06.2027 | 0.070 | Polymarket / Manifold | 0.160 / 0.147 | APPROX | +0.09 / +0.08 |
| Q-0074 | Brent > 100 USD on 20.10 | 0.633 | Kalshi | 0.665 | EXACT | +0.03 |
| Q-0076 | FFPI October > 136.0 | 0.560 | Kalshi | 0.350 | EXACT | **−0.21** |
| Q-0078 | ≥ 10 Hormuz transits on a day 08–17.10 | 0.083 | Kalshi / Polymarket (whole October) | 0.350 / 0.365 | APPROX | **+0.27 / +0.28** |
| Q-0081 | In-person US–Iran meeting 08–21.10 | 0.103 | Polymarket / Kalshi | 0.175 / 0.155 | APPROX | +0.07 / +0.05 |
| Q-0082 | Trilateral meeting 08–31.10 | 0.107 | Polymarket (any RU–UA meeting) | 0.460 | APPROX | **+0.35** |
| Q-0088 | Bank of Russia hikes on 23.10 | 0.083 | Polymarket / Kalshi | 0.026 / 0.025 | EXACT | −0.06 / −0.06 |
| Q-0093 | Iotova > 50% in round one | 0.267 | Polymarket (also requires turnout > 50%) | 0.085 | APPROX | −0.18 |
| Q-0094 | Likud the largest list | 0.467 | Polymarket / Kalshi / Manifold | 0.515 / 0.505 / 0.500 | EXACT | +0.05 / +0.04 / +0.03 |
| Q-0095 | Republicans ≥ 50 Senate seats | 0.427 | Polymarket / Kalshi / Manifold / GJO | 0.365 / 0.395 / 0.345 / 0.470 | EXACT | −0.06 / −0.03 / −0.08 / +0.04 |
| Q-0096 | Araghchi ceases to be FM by 31.12 | 0.150 | Polymarket | 0.115 | EXACT | −0.03 |
| Q-0099 | ≥ 3 US carriers in CENTCOM by 30.11 | 0.467 | Polymarket (on 30.11 only) | 0.220 | APPROX | **−0.25** |
| Q-0100 | Putin at APEC Shenzhen | 0.617 | Polymarket | 0.810 | APPROX | +0.19 |
| Q-0106 | US ban or quota on distillate exports by 31.12 | 0.067 | Polymarket | 0.110 | APPROX | +0.04 |
| Q-0110 | Signed full-front ceasefire by 30.06.2027 | 0.083 | Polymarket (broader criterion) | 0.505 | APPROX | **+0.42** |
| Q-0113 | Kostiantynivka by 31.03.2027 | 0.240 | Polymarket | 0.410 | EXACT | +0.17 |

No counterparts for 48 questions, including the whole TTF and AGSI+ energy cluster, Brent thresholds over long windows, H.R. 5334 tariffs, the Russia SDN and EU package questions, Taiwan (exercises, MND counts, DSCA), Polish macro and rating questions, the Baltic and Black Sea infrastructure questions, and the US–PRC truce formalisation questions (Q-0102, Q-0108, Q-0077). Full list: `06_benchmarks.md` §2.

## 4. Discrepancies |Δ| ≥ 0.20 — hypotheses about causes

Working hypotheses from stage 06; they do not decide who is right. The outcome will decide.

**EXACT**
1. **Q-0038 — US lifts or suspends the Iran blockade by 31.12** (0.143 vs 0.479; option volume about 3.1 mn USD). The lenses tied a blockade lift to a US–Iran deal (05 §2.3). The market prices the deal path higher (Q-0028: 0.355 vs 0.157) and probably a unilateral suspension as a bargaining step after 03.11. Kalshi's "US–Iran nuclear deal" (0.115) is close to our Q-0028 — the market separates a Hormuz or shipping arrangement from a nuclear deal; the lenses did not. Hypothesis: an omitted path (a narrow shipping arrangement without a nuclear deal) — the same type of error as Q-0030 in edition 01.
2. **Q-0001 — Russian mobilisation decree** (0.03 vs 0.305 Manifold, 18 traders, play currency). Same as edition 01. The liquid Polymarket market (broader criterion) has fallen to 0.10, within 0.07 of our forecast. Hypothesis: an illiquid market with a tail premium; not informative.
3. **Q-0076 — FAO index for October above 136.0** (0.56 vs 0.35; Kalshi, 200 contracts, spread 0.31/0.39). The Kalshi ladder puts the median near 135, a small decline; the lenses expected a small rise. Hypothesis: the lenses weighted energy and freight pass-through (Brent about 100), the market seasonal harvest pressure on cereals and vegetable oils; low liquidity makes the market a weak signal.

**APPROX (outside the scores)**
4. **Q-0007 — Brent above 120** (GJO 0.84): a different series (EIA spot, 135.51 on 02.10 and 125.44 on 06.10 per FRED) and a window from 19.07 — the crowd value records an already observed spot peak. Uninformative. Note for resolution: Q-0007 resolves on ICE front-month settlements, not on the EIA spot series.
5. **Q-0030 — Putin–Trump meeting** (0.317 vs 0.81 by 31.12). The same discrepancy as edition 01 (then 0.765). The market assumes both leaders at APEC Shenzhen and a meeting there; the red team estimated joint presence at about 0.40–0.45 from Q-0029 (0.643) and Q-0100 (0.617), both below the market's implied attendance (+0.17 and +0.19). Hypothesis: the lenses treat each leader's attendance as independently uncertain, the market as coordinated. The resolution risk (does a shared plenary count as a meeting) applies.
6. **Q-0110 — signed full-front ceasefire by 30.06.2027** (0.083 vs 0.505). The market criterion is broader (any mutually agreed suspension of direct military engagement), which explains part of the gap but hardly a factor of six. Hypothesis: the lenses anchored on the October stalemate; the market prices a nine-month window in which a post-election US push may succeed. Our nested Ukraine questions (Q-0026, Q-0082) are also below the markets.
7. **Q-0082 and Q-0026 — trilateral meetings.** Polymarket measures any RU–UA meeting, Kalshi a leaders' trilateral; our questions lie between them. A discrepancy of criteria, as in edition 01.
8. **Q-0065 — US land strike on Iran by 31.12** (0.35 vs 0.665 converted from a ceasefire-breakdown market — an upper bound). The gap (+0.32) is similar to edition 01 (+0.29). Hypothesis: the market prices a higher post-03.11 breakdown risk than the "electoral brake" assumption KA1 allows (05 §1 item 3).
9. **Q-0017 — ECB hike in X–XII** (December markets 0.77–0.79 vs 0.493). The direction repeats edition 01 (+0.21 then). GJO disagrees with the markets (October only 0.193; December only 0.406; combined as if independent about 0.52, close to AGG_RT), so the gap to the markets is not a consensus signal. Worth checking in L2/L3 once Q-0017 resolves.
10. **Q-0078 — ≥ 10 Hormuz transits on a day 08–17.10.** Both counterparts cover the whole of October; Kalshi's weekly "above 10" markets (0.045 for 05–11.10, 0.065 for 12–18.10) are close to our value. Window and threshold mismatch — uninformative.
11. **Q-0099 — three US carriers in CENTCOM by 30.11** (single-date market 0.22, a lower bound; volume about 4k USD). Partly a criterion effect; the lenses weighted the third-carrier signal and eight weekly observation points.
12. **Q-0034 — Venezuela election date** (market by 31.12 only: 0.105). Three months of our window are missing from the market.
13. **Q-0015 — US tariff on EU goods above 15%** (Kalshi "rate ≥ 20%" on 01.01.2027, 81 contracts, rate definition unchecked — possibly including s.232 duties, which our criterion excludes). Uninformative.

**Below the threshold, worth noting.** Q-0033 Lula: three markets (0.105–0.14) and GJO (0.26) against our 0.29 after the first round — the gap narrowed from edition 01 and kept its sign (we rate Lula higher than the markets; GJO is close to us). Q-0031 House: GJO (0.20) is the outlier against markets (0.07–0.105) and us (0.107). Q-0113 Kostiantynivka (+0.17) and Q-0027 Article 4 (+0.15): markets higher than us, as in edition 01 for Article 4. Q-0093 Bulgaria: the market also requires turnout above 50% — a lower bound, not comparable.

## 5. Consistency of the benchmarks

- Agreement on the liquid EXACT markets: Q-0066 (FOMC — the large edition 01 discrepancy of +0.31 has disappeared after the red-team adjustment), Q-0020/Q-0088 (Bank of Russia), Q-0031, Q-0094, Q-0095, Q-0096, Q-0074 — all within 0.08.
- Cross-market inconsistencies: Hormuz — Polymarket "normal by 31.12" (0.175) vs Kalshi > 40 (0.17) and > 60 (0.095), the narrower event priced higher, as in edition 01; GJO ≥ 35 by 11.01 (0.15) below Kalshi > 40 by 31.12 (0.17) although the GJO event is broader. ECB December: GJO 0.41 vs Polymarket and Kalshi 0.77–0.79. House: GJO 0.20 vs markets 0.07–0.105.

## 6. Conclusions for the quarterly review (no change to forecasts)

- As in edition 01, the largest EXACT and APPROX gaps cluster around one mechanism: the "electoral brake" of 03.11 and the post-election US course toward Iran (Q-0038, Q-0065, Q-0028), and around omitted narrow paths (a shipping arrangement without a nuclear deal; joint attendance at APEC). These outcomes should be read as one correlated bet.
- The edition 01 FOMC gap (Q-0066) closed once the lenses had Fed speakers' statements (A-14, C-11) — consistent with the edition 01 note that the lenses lacked rate-futures pricing; whether to admit financial-instrument pricing (not prediction markets) as lens B input remains a decision for the quarterly review.
- Shallow single quotes carry noise of the order of 0.05–0.10 (cross-market inconsistencies above); a single-source EXACT match (Q-0001 Manifold, Q-0076 Kalshi) should not be over-weighted when the BSS vs crowd is read.
- Coverage: four of six sources; GJO only through public challenge pages; Metaculus needs an account. The BSS vs crowd will rest on few pairs until the quarterly review (3 pairs now).

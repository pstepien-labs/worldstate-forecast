# Annex: comparison with the crowd and markets — edition 03 (state 16.11.2026)

> **File forbidden to stages 03, 04 and 05 in all future editions** (CLAUDE.md item 8). It is not part of the main report (methodology §6). Material for reviewing the method, not grounds for changing forecasts.

Framework 1.8.0 · methodology v1.0 · commit 045c4fa · models: claude-opus-5-5

Source: `06_benchmarks.md` and `registry/benchmarks.csv` (edition 03: 31 rows for 25 questions; 12 EXACT rows for 10 questions). Quotes were collected **after** the "forecasts frozen" commit (7840589, 18.11.2026 08:29), on 18.11.2026 at about 08:30–09:30 Warsaw time — after the information cutoff of the forecasts (17.11.2026 15:08) and on the first day of the APEC leaders' meeting in Shenzhen. Crowd prices therefore carry information the lenses could not use, most visibly on the Shenzhen questions (Q-0029, Q-0030, Q-0100, Q-0132) and on the December central-bank meetings. No forecast was changed. Δ = crowd − AGG_RT. Where a question has several sources, `scores.py` averages them — and so does the "crowd (mean)" column.

## 0. Score against the crowd (from `01_scores.md`)

AGG_RT vs crowd on resolved questions with an EXACT match (forecasts of editions 01 and 02, resolved by stage 01 of this edition, unverified resolutions excluded): **N = 18** pairs · Brier AGG_RT **0.127** · Brier crowd **0.143** · **BSS vs crowd 0.116**. Edition 02 recorded N = 3 pairs and BSS −1.974; the larger sample now puts the official forecast slightly ahead of the crowd. ASSESSMENT (confidence: low, n = 18): the sign is the first usable reading of the second official measure (methodology §1 b); it is not yet stable — one or two large misses on either side would change it.

## 1. Access to sources

| Source | Access | Rows |
|---|---|---|
| Kalshi | public read-only API (the website refused the connection) | 21 |
| Manifold | public API (play currency, usually low liquidity) | 8 |
| Good Judgment Open | public question pages and challenge lists, no login (the full question list needs a login) | 2 |
| Polymarket | not reachable on 18.11.2026 (DNS failure, connection refused) | 0 |
| Metaculus | API and question pages HTTP 403 (accounts only); no login | 0 |
| RAND Forecasting Initiative | platform closed (edition 01 finding; not re-checked) | 0 |

Three of the six sources in methodology §6 were read (edition 02: four). The loss of Polymarket (32 rows in edition 02) halves the coverage: 58 of 83 active questions have no counterpart. Note for the quarterly review.

## 2. Questions with an EXACT match (enter the BSS vs crowd once resolved)

| ID | Question (short) | Deadline | AGG_RT | Sources (p) | Crowd (mean) | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Russian mobilisation decree by 31.12 | 31.12.2026 | 0.020 | Manifold 0.080 | 0.080 | +0.06 |
| Q-0016 | MPC changes the NBP reference rate, 24.09–31.12 | 31.12.2026 | 0.107 | Kalshi 0.150 | 0.150 | +0.04 |
| Q-0017 | ECB raises the deposit rate, 24.09–31.12 | 31.12.2026 | 0.693 | GJO 0.749; Kalshi 0.985 | 0.867 | +0.17 |
| Q-0034 | Venezuela announces a presidential election date by 31.03.2027 | 31.03.2027 | 0.320 | Kalshi 0.280 | 0.280 | −0.04 |
| Q-0036 | PortWatch Hormuz 7-day mean above 40 by 31.12 | 31.12.2026 | 0.033 | Kalshi 0.095 | 0.095 | +0.06 |
| Q-0118 | Bank of Russia cut on 18.12 | 18.12.2026 | 0.223 | Kalshi 0.075 | 0.075 | −0.15 |
| Q-0122 | Hegseth leaves office, 18.11–31.03.2027 | 31.03.2027 | 0.177 | Kalshi 0.555 | 0.555 | **+0.38** |
| Q-0133 | PP wins the most seats in Spain, 29.11 | 30.11.2026 | 0.687 | Manifold 0.893 | 0.893 | **+0.21** |
| Q-0142 | FOMC hike on 09.12 | 09.12.2026 | 0.583 | GJO 0.890; Kalshi 0.970 | 0.930 | **+0.35** |
| Q-0146 | Knesset approves a new government, 18.11–20.12 | 20.12.2026 | 0.383 | Kalshi 0.300 | 0.300 | −0.08 |

Direction across the 12 EXACT rows: the crowd is above AGG_RT in 9, below in 3. Mean |Δ| over the 10 questions (crowd means): 0.15.

## 3. Questions with an APPROX match (not scored)

| ID | Question (short) | AGG_RT | Source (event priced) | Crowd p | Δ |
|---|---|---|---|---|---|
| Q-0015 | US tariff on EU goods above 15% by 31.03.2027 | 0.073 | Kalshi | 0.075 | +0.00 |
| Q-0018 | PRC bank on the SDN list by 31.03.2027 | 0.057 | Kalshi | 0.120 | +0.06 |
| Q-0028 | US–Iran agreement opening Hormuz by 31.12 | 0.057 | Kalshi; Manifold | 0.036; 0.119 | −0.02; +0.06 |
| Q-0029 | Trump at APEC Shenzhen in person | 0.887 | Kalshi (trilateral meeting) | 0.990 | +0.10 |
| Q-0030 | Putin–Trump meeting in person by 31.03.2027 | 0.927 | Kalshi (trilateral meeting); Manifold | 0.990; 0.943 | +0.06; +0.02 |
| Q-0069 | DSCA Taiwan notification ≥ 1 bn USD by 31.12 | 0.063 | Manifold | 0.167 | +0.10 |
| Q-0073 | ISW: Kramatorsk or Sloviansk taken by 30.06.2027 | 0.040 | Manifold | 0.026 | −0.01 |
| Q-0100 | Putin at APEC Shenzhen in person | 0.807 | Kalshi (trilateral meeting) | 0.990 | +0.18 |
| Q-0121 | Another US–UA–RU delegation meeting by 31.12 | 0.583 | Kalshi (Trump–Zelensky–Putin in person) | 0.060 | **−0.52** |
| Q-0122 | Hegseth leaves office (other horizons) | 0.177 | Kalshi (leaves or announces before 01.01.2027); Manifold (out by end-2026) | 0.185; 0.125 | +0.01; −0.05 |
| Q-0124 | PortWatch ≥ 10 Hormuz transits on a day, 18–30.11 | 0.113 | Kalshi | 0.065 | −0.05 |
| Q-0126 | Brent spot (FRED) above 90 on 30.11 | 0.523 | Kalshi | 0.440 | −0.08 |
| Q-0132 | Joint statement of the US, PRC and Russian leaders, 18–22.11 | 0.310 | Kalshi (trilateral meeting) | 0.990 | **+0.68** |
| Q-0135 | Trump–Kim meeting, 18–30.11 | 0.070 | Kalshi | 0.155 | +0.08 |
| Q-0141 | Same-room US–Iran meeting by 31.12 | 0.117 | Kalshi | 0.180 | +0.06 |
| Q-0143 | US shutdown begins 12.12–31.12 | 0.207 | Kalshi | 0.305 | +0.10 |

Counterparts looked for and not recorded (06 §2): Q-0007 (the GJO Brent-maximum question puts its weight on a maximum reached before our window), Q-0117 (Kalshi prices only a point TTF value on 30.11), Q-0077 (Kalshi truce market without a usable price), Q-0145 (no open euro-area inflation event), Q-0110 (Metaculus HTTP 403; Manifold only end-2027 with 14 traders).

## 4. Discrepancies |Δ| ≥ 0.20 — hypotheses (not grounds for changing forecasts)

| ID | AGG_RT | Crowd | Δ | Match | Hypothesis |
|---|---|---|---|---|---|
| Q-0142 (Fed hike 09.12) | 0.583 | Kalshi 0.970; GJO 0.890 | +0.39 / +0.31 | EXACT | ASSESSMENT: the deepest market in the set prices a hike as near-certain. Either the lenses lacked the pricing-relevant signals after the October meeting (Fed speakers, data), or the market holds information after the cutoff; not checked. The lens spread was small (0.55–0.60), so all three lenses shared one evidence gap. A clean test case on 09.12. |
| Q-0122 (Hegseth out by 31.03.2027) | 0.177 | Kalshi 0.555 | +0.38 | EXACT | ASSESSMENT: the Kalshi term structure is steep (before 01.01.2027 about 0.15; before 01.02 about 0.27; before 01.04 about 0.56) — traders expect a departure tied to an early-2027 event, most plausibly the Democratic House from 03.01.2027. Our 18.11–31.12 portion agrees with the market; the gap is in Q1 2027. The lenses may have under-weighted the post-January Congress. |
| Q-0017 (ECB hike by 31.12) | 0.693 | Kalshi 0.985; GJO 0.749 | +0.29 / +0.06 | EXACT | ASSESSMENT: the red team's +0.15 moved AGG toward the market, and the ±0.15 limit, not the evidence, capped it (05 §3). Kalshi agrees with the unanimous Reuters poll (R-01); GJO's slower-updating crowd sits near our value. Evidence for L3: the limit can bind when the evidence is strong. |
| Q-0133 (PP most seats, 29.11) | 0.687 | Manifold 0.893 | +0.21 | EXACT | ASSESSMENT: a low-liquidity play-money market (11 traders, no written criterion, tie treatment unstated). The lenses may discount polling leads more than the crowd. Weak benchmark. |
| Q-0132 (joint leaders' statement, 18–22.11) | 0.310 | Kalshi 0.990 (meeting) | +0.68 | APPROX | Different event: the market prices the three-leader meeting (under way at quote time); a meeting is necessary, not sufficient, for a joint statement. Not evidence of an error. |
| Q-0121 (US–UA–RU delegations by 31.12) | 0.583 | Kalshi 0.060 (three presidents in one room) | −0.52 | APPROX | Different event: our question counts any level of government delegations. The market value is a lower bound, not a counterpart. Not evidence of an error. |

Below the threshold but worth noting: Q-0100 (+0.18, APPROX) — the trilateral market at 0.99 during the summit window shows Putin's attendance priced as near-certain on 18.11, information after the cutoff; Q-0118 (−0.15, EXACT) — the market puts a December Bank of Russia cut lower than our lenses, on low volume.

## 5. Summary

- 10 questions have an EXACT counterpart (12 rows); they enter the crowd BSS after resolution. Three EXACT questions with deep markets show |Δ| ≥ 0.20 (Q-0142, Q-0122, Q-0017), all in the direction "the crowd is more confident of change than we are"; one more with a shallow play-money market (Q-0133).
- ASSESSMENT (confidence: low, n = 10 questions): on scheduled central-bank decisions the lenses sit closer to 0.5 than the markets — consistent with the calibration finding in section 0 of the report (forecasts between 30% and 50% resolved YES in 18 of 23 cases). A pattern to test in L2 against the December resolutions (Q-0017, Q-0142, Q-0118).
- The timing caveat applies to all rows: every quote is later than the information cutoff by about 17–18 hours, during a summit.
- No forecast was changed after the benchmarks were seen.

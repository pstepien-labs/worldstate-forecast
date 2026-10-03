# Annex: comparison with the crowd and markets — edition 01 (state 23.09.2026)

> **File forbidden to stages 03, 04 and 05 in all future editions** (CLAUDE.md item 8). It is not part of the main report (methodology §6). Material for reviewing the method, not grounds for changing forecasts.

Source: `06_benchmarks.md` and `registry/benchmarks.csv` (43 rows, 26 questions). Quotes were collected on 23.09.2026 in the evening (Polish time), **after** the "forecasts frozen" commit (32a635e). No forecast was changed. Δ = crowd − AGG_RT.

## 1. Access to sources

| Source | Access | Rows |
|---|---|---|
| Polymarket | public read-only API (site: ECONNREFUSED for the tool) | 25 |
| Kalshi | public read-only API | 13 |
| Manifold | public API (play currency, usually low liquidity) | 9 |
| Good Judgment Open | public pages, no login | 2 |
| Metaculus | API requires an account, pages HTTP 403; no login | 0 |
| RAND Forecasting Initiative | platform closed (archive only) | 0 |

Of the six sources in methodology §6, four work — a note for the quarterly review.

## 2. Questions with an EXACT match (enter the BSS vs crowd)

When a question has several sources, `scores.py` averages them — and so does the "crowd (mean)" column.

| ID | Question (short) | Deadline | AGG_RT | Sources (p) | Crowd (mean) | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Russian mobilisation decree | 31.12.2026 | 0.03 | Manifold 0.27 | 0.270 | **+0.24** |
| Q-0006 | Brent > 100 USD on 06.10 | 06.10.2026 | 0.40 | Kalshi 0.42 (deadline 30.09) | 0.420 | +0.02 |
| Q-0020 | Bank of Russia cuts the rate on 23.10 | 23.10.2026 | 0.25 | Polymarket 0.275 | 0.275 | +0.03 |
| Q-0027 | NATO Art. 4 request | 31.12.2026 | 0.113 | Polymarket 0.47 | 0.470 | **+0.36** |
| Q-0031 | Republicans ≥ 218 seats | 31.12.2026 | 0.107 | Polymarket 0.075; Kalshi 0.082; Manifold 0.062 | 0.073 | −0.03 |
| Q-0033 | Lula wins the election | 31.10.2026 | 0.557 | Polymarket 0.405; Kalshi 0.435; Manifold 0.373; GJO 0.50 | 0.428 | −0.13 |
| Q-0036 | Hormuz: 7-day average > 40 | 31.12.2026 | 0.24 | Kalshi 0.18 | 0.180 | −0.06 |
| Q-0037 | Hormuz: ≥ 20 transits in a day | 07.10.2026 | 0.113 | Polymarket 0.041 (deadline 30.09) | 0.041 | −0.07 |
| Q-0054 | A Just Russia ≥ 5.00% | 30.09.2026 | 0.94 | Polymarket 0.99 | 0.990 | +0.05 |
| Q-0055 | United List wins in Latvia | 10.10.2026 | 0.817 | Polymarket 0.95; Kalshi 0.925 | 0.938 | +0.12 |
| Q-0056 | Lula > 50% in the first round | 05.10.2026 | 0.063 | Manifold 0.099 | 0.099 | +0.04 |
| Q-0066 | FOMC raises the rate on 28.10 | 28.10.2026 | 0.333 | Polymarket 0.65; Kalshi 0.67; Manifold 0.618 | 0.646 | **+0.31** |

Mean |Δ| over 12 questions: 0.12. Discrepancies ≥ 0.20: 3 (Q-0027, Q-0066, Q-0001). The crowd is above AGG_RT in 8 of 12 questions and below in 4. All three differences ≥ 0.20 have the same sign: the crowd gives higher p to rare events or institutional decisions (mobilisation, Art. 4, a Fed hike). With n = 12 this is an indicative observation, not a conclusion about the method.

## 3. All matches (EXACT and APPROX)

| ID | Question (short) | AGG_RT | Source | Crowd p | Match | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Russian mobilisation decree by 31.12 | 0.030 | Polymarket | 0.26 | APPROX | **+0.23** |
| Q-0001 | | | Manifold | 0.27 | EXACT | **+0.24** |
| Q-0006 | Brent > 100 USD on 06.10 | 0.400 | Kalshi (30.09) | 0.42 | EXACT | +0.02 |
| Q-0011 | Extension of the US–PRC truce by 10.11 | 0.750 | Kalshi (by 01.11) | 0.505 | APPROX | **−0.25** |
| Q-0011 | | | Polymarket (by 31.10) | 0.835 | APPROX | +0.09 |
| Q-0016 | MPC changes the rate by 31.12 | 0.183 | Kalshi (X only) | 0.075 | APPROX | −0.11 |
| Q-0017 | ECB raises the rate X–XII | 0.433 | Polymarket (XII) | 0.64 | APPROX | **+0.21** |
| Q-0018 | PRC bank on the SDN by 31.03.2027 | 0.087 | Kalshi (by 01.01.2027) | 0.315 | APPROX | **+0.23** |
| Q-0020 | Bank of Russia cuts the rate on 23.10 | 0.250 | Polymarket | 0.275 | EXACT | +0.03 |
| Q-0026 | Trilateral US–UA–RU meeting by 30.11 | 0.450 | Kalshi (leaders, by 01.01) | 0.035 | APPROX | **−0.42** |
| Q-0026 | | | Polymarket (RU–UA, by 31.10) | 0.645 | APPROX | +0.195 (below the threshold) |
| Q-0027 | NATO Art. 4 request by 31.12 | 0.113 | Polymarket | 0.47 | EXACT | **+0.36** |
| Q-0030 | Putin–Trump meeting by 31.03.2027 | 0.267 | Polymarket (by 31.12) | 0.765 | APPROX | **+0.50** |
| Q-0030 | | | Manifold (2026) | 0.274 | APPROX | +0.01 |
| Q-0031 | Republicans ≥ 218 seats | 0.107 | Polymarket / Kalshi / Manifold | 0.075 / 0.082 / 0.062 | EXACT | −0.03 / −0.03 / −0.05 |
| Q-0032 | New recording of Mojtaba Khamenei | 0.140 | Polymarket (photo/video) | 0.195 | APPROX | +0.06 |
| Q-0033 | Lula wins the election | 0.557 | Polymarket / Kalshi / Manifold / GJO | 0.405 / 0.435 / 0.373 / 0.50 | EXACT | −0.15 / −0.12 / −0.18 / −0.06 |
| Q-0034 | Venezuela: election date by 31.03.2027 | 0.333 | Polymarket | 0.165 | APPROX | −0.17 |
| Q-0035 | Goïta loses power by 31.03.2027 | 0.093 | Polymarket (by 31.12) | 0.075 | APPROX | −0.02 |
| Q-0036 | Hormuz: 7-day average > 40 by 31.12 | 0.240 | Kalshi | 0.18 | EXACT | −0.06 |
| Q-0036 | | | Polymarket (≥ 60) / GJO (≥ 35, by 11.01) | 0.205 / 0.333 | APPROX | −0.04 / +0.09 |
| Q-0037 | Hormuz: ≥ 20 transits in a day by 07.10 | 0.113 | Polymarket (by 30.09) | 0.041 | EXACT | −0.07 |
| Q-0037 | | | Kalshi (September) | 0.045 | APPROX | −0.07 |
| Q-0041 | US strike on Iran by 07.10 | 0.060 | Polymarket (ceasefire breakdown by 30.09) | 0.135 | APPROX | +0.08 |
| Q-0042 | US–Iran round of talks by 07.10 | 0.483 | Polymarket (by 30.09, high level) | 0.435 | APPROX | −0.05 |
| Q-0054 | SR ≥ 5.00% | 0.940 | Polymarket | 0.99 | EXACT | +0.05 |
| Q-0055 | AS wins in Latvia | 0.817 | Polymarket / Kalshi | 0.95 / 0.925 | EXACT | +0.13 / +0.11 |
| Q-0056 | Lula > 50% in the first round | 0.063 | Manifold | 0.099 | EXACT | +0.04 |
| Q-0058 | Extension of the US–PRC truce by 07.10 | 0.450 | Kalshi / Polymarket (by 30.09–01.10) | 0.36 / 0.765 | APPROX | −0.09 / **+0.32** |
| Q-0065 | US strike on Iran by 31.12 | 0.260 | Polymarket (ceasefire breakdown) | 0.545 | APPROX | **+0.29** |
| Q-0066 | FOMC raises the rate on 28.10 | 0.333 | Polymarket / Kalshi / Manifold | 0.65 / 0.67 / 0.618 | EXACT | **+0.32 / +0.34 / +0.29** |
| Q-0073 | Full Russian control of Kramatorsk or Sloviansk by 30.06.2027 | 0.117 | Polymarket (entry, by 31.12) / Manifold | 0.19 / 0.147 | APPROX | +0.07 / +0.03 |

No counterparts for 47 questions, including the whole ENE panel apart from Brent on 06.10 (TTF, AGSI+ storage, diesel), CPI in Poland, EUR/PLN, the Russian budget, H.R. 5334 tariffs, magnets, Blackwell, Baltic cables, the Panama Canal, the DPRK, Taiwan, the EU's 22nd package, the Bank of Russia's assets, Armenia and Azerbaijan.

## 4. Discrepancies |Δ| ≥ 0.20 — hypotheses about causes

Working hypotheses from stage 06; they do not decide who is right. The outcome will decide.

**EXACT**
1. **Q-0066 FOMC 28.10** (0.333 vs 0.62–0.67; three markets agree, Kalshi approx. 770k contracts). Lenses A and C assumed the hike would be postponed to XII because of the 03.11 elections. Hypothesis: no fed funds futures pricing in the lenses' material and an overweighting of the electoral argument — the same "electoral brake" mechanism (KA1) that the red team flagged as a risk of correlated error.
2. **Q-0027 NATO Art. 4** (0.113 vs 0.47; low liquidity, spread 0.41/0.53). The base rate from 2022–2025 (approx. 0.65/year) gives approx. 0.16 for 3.3 months, not 0.47. Hypothesis: a shallow market or information about incidents that the lenses did not have. Check in stage 01 of edition 02.
3. **Q-0001 Russian mobilisation** (0.03 vs 0.27 Manifold, 17 traders; Polymarket 0.26 with a broader criterion). Hypothesis: (a) the Polymarket market counts an extension of categories under the IX 2022 decree — a cheaper event for the Kremlin than a new decree; (b) a tail premium on war markets.

**APPROX (outside the scores)**
4. **Q-0030 Putin–Trump** (0.267 vs 0.765 by 31.12). The market assumes a meeting at APEC in Shenzhen (18–19.11), where a handshake suffices; the lenses treated the meeting as a separate summit and did not consider joint presence at APEC. **The most serious discrepancy of the edition — an omitted scenario, not a difference in judgement.** For review: consistency with Q-0029 (Trump at APEC, 0.533).
5. **Q-0026 trilateral meeting** (0.45 vs 0.035 Kalshi — leader level; 0.645 Polymarket — RU–UA contact). A discrepancy of criteria.
6. **Q-0058 and Q-0011 US–PRC truce** — the markets differ from each other by 0.40; shallow and distant in their criteria.
7. **Q-0065 US strike on Iran by 31.12** (0.26 vs 0.545 for a "ceasefire breakdown") — the market is an upper bound for our question, but the discrepancy is large; in line with the risks of KA1 and the omission of Israel.
8. **Q-0017 ECB** (0.433 vs 0.64 for XII, liquidity approx. 4k USD; X market: 0.48) — the lenses weighted the economists' consensus above futures pricing.
9. **Q-0018 PRC bank on the SDN** (0.087 vs 0.315) — the market's criterion is broader; an uninformative discrepancy.

**Below the threshold, worth noting:** Q-0033 Lula (markets 0.37–0.44 with high liquidity vs 0.557); Q-0055 Latvia (0.93–0.95 vs 0.817).

## 5. Conclusions for the quarterly review (no change to forecasts)

- One of the three EXACT discrepancies (Q-0066) and two APPROX ones (Q-0065, indirectly Q-0030) concern the same risk area: a correlated assumption about the electoral brake and about the summit calendar. The outcomes of these questions should be read as one bet.
- The lenses did not use the pricing of financial instruments (rate futures), although these are not prediction markets within the meaning of CLAUDE.md item 9. Whether to admit them as input data for lens B — a decision for the quarterly review, not for this edition.
- The cross-market inconsistency (Hormuz: Polymarket P(≥ 60) = 0.205 > Kalshi P(> 40) = 0.18) shows that single quotes on shallow markets carry noise of the order of 0.05–0.10.

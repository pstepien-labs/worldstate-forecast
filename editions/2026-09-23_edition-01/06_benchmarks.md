# Stage 06 — Benchmarks (edition 01, state 23.09.2026)

The benchmarks were collected **after** the "forecasts frozen" commit (32a635e). The material is for review. It is **not** grounds for changing forecasts: no forecast was changed. It does not go into the main report (methodology §6); it goes into `07_annex_benchmarks.md`.

## 1. Sources and access

| Source | Access | Result |
|---|---|---|
| Polymarket | The site returns ECONNREFUSED for the WebFetch tool; quotes were taken from the public read-only API (gamma-api.polymarket.com) | 25 rows |
| Kalshi | Public read-only API (api.elections.kalshi.com) | 13 rows |
| Manifold | Public search API (api.manifold.markets) | 9 rows (play currency, usually low liquidity) |
| Good Judgment Open | Public pages (no login) | 2 rows; many GJO questions do not fit the bank |
| Metaculus | The API requires an account, and question pages return HTTP 403. No login (CLAUDE.md §6) | 0 rows; found among others question 43318 "general mobilization before 01.01.2027", but without a value |
| RAND Forecasting Initiative | Platform closed, only the archive of resolved questions is available | 0 rows |

Recording convention: p = midpoint of the bid/ask spread (Polymarket: `outcomePrices`, i.e. the midpoint; Kalshi: (bid+ask)/2). Values outside the range 0.01–0.99 were clipped to that range, and the raw quote is given in the `notes` field. Date of quotes: 23.09.2026, evening (Polish time). Record in `registry/benchmarks.csv`: 43 rows, 26 questions; 20 EXACT rows for 12 questions.

## 2. Matches

The AGG_RT column is the official frozen forecast. Δ = crowd − AGG_RT.

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

No counterparts were found for 47 questions. This includes the whole ENE panel apart from Brent on 06.10 (TTF, AGSI+ storage, diesel), Polish CPI, EUR/PLN, the Russian budget, H.R. 5334 tariffs, magnets, Blackwell, Baltic cables, the Panama Canal, the DPRK in the 24.09–07.10 window, Taiwan (named exercises, MND ≥ 20 aircraft, DSCA), the EU's 22nd package, the Bank of Russia's assets, Armenia and Azerbaijan.

## 3. Discrepancies |AGG_RT − crowd| ≥ 0.20: hypotheses about causes

The hypotheses are working hypotheses intended for review. They do not decide who is right.

**EXACT matches**

1. **Q-0066 FOMC 28.10 (0.333 vs 0.62–0.67; three independent markets agree).** Lenses A and C assumed the Fed would postpone the hike to XII, because the meeting falls a week before the elections and the White House is applying pressure. B assumed a 50% chance of a hike at the next meeting of the cycle. The markets (Kalshi: volume approx. 770k contracts) price a move already in X. Hypothesis: the lenses did not have the fed funds futures pricing (e.g. FedWatch) and overweighted the electoral argument. This is the same mechanism KA1 ("electoral brake") that the red team (05 §1 item 1) flagged as a risk of correlated error.
2. **Q-0027 NATO Art. 4 by 31.12 (0.113 vs 0.47; low liquidity, option volume approx. 7.5k USD).** The lenses relied on the high threshold seen in 2026: no request despite the drone over Lithuania. The market extrapolates the IX 2025 series (PL, EE) and the bid/ask spread is wide (0.41/0.53). The base rate alone does not explain the price: approx. 0.65/year from 2022–2025 gives approx. 0.16 for 3.3 months, not 0.47. Hypothesis: the difference comes from low liquidity or from information about incidents in the last few days that the lenses did not have. To be checked in stage 01 of edition 02.
3. **Q-0001 Russian mobilisation (0.03 vs 0.26–0.27).** Manifold (17 traders) and Polymarket (broader criterion) give similar values. Lenses: domestic cost, contract recruitment, a rate of 1 decree in 55 months. Hypothesis: (a) on Polymarket an extension of categories under the IX 2022 decree, which formally remains in force, also counts, and that is a much cheaper event for the Kremlin than a new decree; (b) war markets show a tail premium (a preference for bets on unlikely events). The Manifold row is EXACT but has low liquidity.

**APPROX matches (outside the scores; for review only)**

4. **Q-0030 Putin–Trump (0.267 vs 0.765 by 31.12).** The location market gives China 0.665. The market assumes that both will be at the APEC summit in Shenzhen (18–19.11), and under the market's criterion a handshake suffices. The lenses treated the meeting as a separate summit requiring progress in the talks and did not consider joint presence at APEC. Our criterion ("meet in person, confirmed by the Kremlin and the White House") probably covers such a meeting. **This is the most serious discrepancy of the edition: an omitted scenario, not a difference in judgement.** For review: whether Q-0029 (Trump at APEC, 0.533) and Q-0030 are consistent. If Putin is in Shenzhen, P(Q-0030) ≈ P(Q-0029) × P(interaction). Manifold (0.274) has negligible liquidity and most likely does not take this information into account.
5. **Q-0026 trilateral meeting (0.45 vs 0.035 Kalshi, leader level; 0.645 Polymarket, RU–UA any level).** The markets measure different events: leaders, or bilateral contact. The discrepancy comes from the criterion, not from judgement. Our question (delegations, any level) lies between them.
6. **Q-0058 and Q-0011 US–PRC truce.** Polymarket (0.765 by 30.09) and Kalshi (0.36 by 01.10) differ from each other by 0.40. Polymarket's short-dated options have a volume of approx. 3–4k USD, and the criteria of both markets ("new tariff agreement") may not include a mere extension. Hypothesis: the markets are too shallow and too far from our criteria to indicate a direction. Q-0011 on Kalshi (0.505 by 01.11) is below our 0.75 probably because the extension may come on 01–10.11 and may not count as a "new agreement".
7. **Q-0065 US strike on Iran (0.26 vs 0.545 for a ceasefire breakdown).** Value converted from the market "ceasefire holds until 31.12". A breakdown of the ceasefire may occur through Iranian action or without a strike on land, so the market is an upper bound for our question. Even so, the discrepancy is large. Hypothesis: the market prices a higher risk of a breakdown after 03.11, in line with the red team's red flag on Israel and assumption KA1 (05 §1 items 1–2).
8. **Q-0017 ECB (0.433 vs ≥ 0.64).** The XII market has liquidity of approx. 4k USD and a wide spread. The X market (0.48, liquidity approx. 41k USD) is closer to us. Lens B mentioned that futures price approx. 3 hikes by mid-2027, but averaged this with the economists' consensus. Hypothesis: the lenses gave more weight to economists' opinion than to market pricing.
9. **Q-0018 PRC bank on the SDN (0.087 vs 0.315).** The Kalshi market has a volume of 145 contracts, and its criterion is broader: any Treasury sanctions, including FinCEN, without the Iran/Russia reason requirement. An uninformative discrepancy.

**Discrepancies below the threshold worth noting.** Q-0033 Lula: three markets give 0.37–0.44 against our 0.557, and GJO 0.50. With high liquidity (Polymarket: approx. 20 mn USD) the difference of 0.12–0.18 is consistent across markets. Hypothesis: the lenses relied on second-round polls "within the margin of error" (Quaest), while the markets weigh Lula's downward trend. Q-0055 Latvia: markets 0.93–0.95 against 0.817.

## 4. Consistency check of the benchmarks

- Cross-market inconsistency for Hormuz: Polymarket P(average ≥ 60) = 0.205 is higher than Kalshi P(> 40) = 0.18, although the Polymarket event is narrower. Only Kalshi (EXACT) enters the scores.
- Q-0036 and Q-0037 (Hormuz) and Q-0031 (House) have AGG_RT within the range set by the markets or close to it. Q-0006 (Brent) differs by 0.02.
- 12 questions with an EXACT match will enter the scores (BSS vs crowd): Q-0001, Q-0006, Q-0020, Q-0027, Q-0031, Q-0033, Q-0036, Q-0037, Q-0054, Q-0055, Q-0056, Q-0066. When one question has several sources, `scores.py` averages them.

## 5. Reports

- No forecast was changed. No login to any service.
- No injected instructions were found in page content or API responses.
- Process note for the quarterly review: Metaculus is not accessible without an account, and the RAND Forecasting Initiative is closed. Of the six sources in methodology §6, four actually work.

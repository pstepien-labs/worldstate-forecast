# Stage 06 — Benchmarks (edition 03, state 16.11.2026)

The benchmarks were collected **after** the "forecasts frozen" commit (7840589, 18.11.2026 08:29). The material is for review. It is **not** grounds for changing forecasts: no forecast was changed. It does not go into the main report (methodology §6); it goes into `07_annex_benchmarks.md`.

Timing caveat: every quote was taken on 18.11.2026 (about 08:30–09:30 Warsaw time), after INFO_CUTOFF (17.11.2026 15:08) and on the first day of the APEC leaders' meeting in Shenzhen (18–19.11). Crowd prices therefore carry information the lenses could not use — most visibly for the Shenzhen questions (Q-0029, Q-0100, Q-0132, Q-0030) and for the December central-bank meetings. Discrepancies below are partly an information-timing effect, not only a difference in judgement.

## 1. Sources and access

| Source | Access | Result |
|---|---|---|
| Kalshi | Public read-only API (api.elections.kalshi.com: `series?tags=`, `events?series_ticker=…&with_nested_markets=true`, `markets?event_ticker=`); series found through tag lists and site-restricted web searches. The kalshi.com website itself refused the connection (ECONNREFUSED) | 21 rows |
| Manifold | Public API (api.manifold.markets: `search-markets`, `slug`) | 8 rows (play currency; liquidity usually low) |
| Good Judgment Open | Public question pages and challenge lists read with the web-fetch tool (In the News 2026: Finance and Foreign Policy filters, Armed Conflict in 2026). Pages 2–4 of the plain question list redirect to sign-in; no login (CLAUDE.md §6) | 2 rows (number of forecasters not shown on public pages) |
| Polymarket | Not reachable: gamma-api.polymarket.com DNS failure, polymarket.com connection refused (ECONNREFUSED), 18.11.2026 | 0 rows — gap |
| Metaculus | API and question pages return HTTP 403 (authenticated users only). No login | 0 rows — gap |
| RAND Forecasting Initiative | Platform closed (edition 01 finding); not re-checked | 0 rows |

Recording convention (as in editions 01–02): p = midpoint of the bid/ask spread (Kalshi (bid+ask)/2, summed over outcome buckets where our event is a union of buckets, or 1 − HOLD where our event is "any change"); Manifold: displayed probability; GJO: crowd forecast of the option. Volumes and spreads in `notes`. Record in `registry/benchmarks.csv`: **31 rows for 25 questions; 12 EXACT rows for 10 questions** (Q-0001, Q-0016, Q-0017, Q-0034, Q-0036, Q-0118, Q-0122, Q-0133, Q-0142, Q-0146). 58 of 83 active questions have no counterpart found.

Searches and fetches: 13 web searches (kalshi.com, gjopen.com, metaculus.com restricted), about 50 API or page fetches. No instructions found in fetched content. Search summaries quoted some Kalshi prices from pages of uncertain date; those were not recorded — only API or page values read directly are in the registry.

## 2. Matches

The AGG_RT column is the official frozen forecast. Δ = crowd − AGG_RT; |Δ| ≥ 0.20 in bold.

| ID | Question (short) | AGG_RT | Source | Crowd p | Match | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Will the president of Russia sign by 31.12.2026 a decree announcing mobilis… | 0.020 | Manifold | 0.080 | EXACT | +0.06 |
| Q-0015 | Will the USA introduce a tariff on EU goods exceeding the 15% ceiling set i… | 0.073 | Kalshi | 0.075 | APPROX | +0.00 |
| Q-0016 | Will the Monetary Policy Council change the NBP reference rate at any meeti… | 0.107 | Kalshi | 0.150 | EXACT | +0.04 |
| Q-0017 | Will the ECB raise the deposit rate at a meeting held between 24.09 and 31.… | 0.693 | GJO | 0.749 | EXACT | +0.06 |
| | | | Kalshi | 0.985 | EXACT | **+0.29** |
| Q-0018 | Will OFAC add to the SDN list by 31.03.2027 a bank registered in mainland P… | 0.057 | Kalshi | 0.120 | APPROX | +0.06 |
| Q-0028 | Will the USA and Iran announce by 31.12.2026 the conclusion of an agreement… | 0.057 | Kalshi | 0.036 | APPROX | −0.02 |
| | | | Manifold | 0.119 | APPROX | +0.06 |
| Q-0029 | Will Donald Trump personally attend the APEC leaders' meeting in Shenzhen (… | 0.887 | Kalshi (trilateral) | 0.990 | APPROX | +0.10 |
| Q-0030 | Will Vladimir Putin and Donald Trump meet in person by 31.03.2027? | 0.927 | Kalshi (trilateral) | 0.990 | APPROX | +0.06 |
| | | | Manifold | 0.943 | APPROX | +0.02 |
| Q-0034 | Will the CNE or the government of Venezuela announce a specific date for th… | 0.320 | Kalshi | 0.280 | EXACT | −0.04 |
| Q-0036 | Will the 7-day average number of transits through the Strait of Hormuz per … | 0.033 | Kalshi | 0.095 | EXACT | +0.06 |
| Q-0069 | Will the DSCA notify Congress by 31.12.2026 of arms sales to Taiwan with a … | 0.063 | Manifold | 0.167 | APPROX | +0.10 |
| Q-0073 | Will ISW assess by 30.06.2027 that Russian forces have taken control of the… | 0.040 | Manifold | 0.026 | APPROX | −0.01 |
| Q-0100 | Will Vladimir Putin personally attend the APEC leaders' meeting in Shenzhen… | 0.807 | Kalshi (trilateral) | 0.990 | APPROX | +0.18 |
| Q-0118 | Will the Bank of Russia cut its key rate at the board meeting of 18.12.2026… | 0.223 | Kalshi | 0.075 | EXACT | −0.15 |
| Q-0121 | Will another meeting of government delegations of the USA, Ukraine and Russ… | 0.583 | Kalshi (leaders' trilateral) | 0.060 | APPROX | **−0.52** |
| Q-0122 | Will Pete Hegseth cease to hold the office of US Secretary of Defense (Secr… | 0.177 | Kalshi (out before 01.04.2027) | 0.555 | EXACT | **+0.38** |
| | | | Kalshi (leaves or announces, before 01.01.2027) | 0.185 | APPROX | +0.01 |
| | | | Manifold (out by end-2026) | 0.125 | APPROX | −0.05 |
| Q-0124 | Will IMF PortWatch record at least 10 transits through the Strait of Hormuz… | 0.113 | Kalshi | 0.065 | APPROX | −0.05 |
| Q-0126 | Will the EIA Europe Brent spot price (FRED DCOILBRENTEU) for 30.11.2026 be … | 0.523 | Kalshi | 0.440 | APPROX | −0.08 |
| Q-0132 | Will a joint statement of the leaders of the USA, China and Russia be publi… | 0.310 | Kalshi (trilateral meeting) | 0.990 | APPROX | **+0.68** |
| Q-0133 | Will the Partido Popular win strictly more seats than any other party in Sp… | 0.687 | Manifold | 0.893 | EXACT | **+0.21** |
| Q-0135 | Will Donald Trump and Kim Jong Un meet in person between 18.11 and 30.11.20… | 0.070 | Kalshi | 0.155 | APPROX | +0.08 |
| Q-0141 | Will representatives of the US and Iranian governments meet in person in th… | 0.117 | Kalshi | 0.180 | APPROX | +0.06 |
| Q-0142 | Will the FOMC raise the federal funds target range at its meeting of 08-09.… | 0.583 | GJO | 0.890 | EXACT | **+0.31** |
| | | | Kalshi | 0.970 | EXACT | **+0.39** |
| Q-0143 | Will a lapse in US federal appropriations (a government shutdown) begin on … | 0.207 | Kalshi | 0.305 | APPROX | +0.10 |
| Q-0146 | Will the Knesset approve a new Israeli government in a confidence vote betw… | 0.383 | Kalshi | 0.300 | EXACT | −0.08 |

Counterparts looked for and not recorded:
- Q-0007 (Brent > 120): GJO question 5558 asks for the highest Brent spot price since 19.07.2026; its crowd puts almost all weight on a maximum already reached before our window (24.09–31.12), so it carries no information on our event (edition 02 recorded it as APPROX). No Kalshi series on the Brent maximum or minimum over a period was found (only point prices).
- Q-0117 (TTF > 100 on any day): Kalshi KXTTFMON prices only a point value at 17:00 EST on 30.11 — not a window maximum.
- Q-0077 (US–China truce extension): Kalshi KXUSCHINATRUCE has bid 0.02 / ask 0.99 and no volume — no usable price.
- Q-0145 (euro-area HICP flash): no open Kalshi euro-area inflation event (KXEZCPIYOYF, KXCPIEU empty).
- Q-0146 alternative: Kalshi KXISRAELPM ("No one" option, horizon 27.10.2027) — horizon too far; the confidence-vote series was used instead.
- Q-0110 (Ukraine ceasefire): Metaculus question found by search, page HTTP 403; Manifold only end-2027 with 14 traders — not recorded.

## 3. Discrepancies |AGG_RT − crowd| ≥ 0.20

Hypotheses about the cause. Material for review (stage 07 annex, learning loop), **not** grounds for changing forecasts.

| ID | AGG_RT | Crowd | Δ | Match | Hypothesis |
|---|---|---|---|---|---|
| Q-0142 (Fed hike 09.12) | 0.583 | Kalshi 0.970, GJO 0.890 | +0.39 / +0.31 | EXACT | ASSESSMENT: the deepest market in the set (several million contracts) prices a hike as near-certain. Either the lenses lacked the pricing-relevant signals (Fed speakers, data releases after the October meeting) or the market has information after the cutoff; stage 06 did not check which. Lens spread was small (0.55–0.60), so all three lenses shared the same evidence gap. A clean test case for the Brier comparison on 09.12. |
| Q-0122 (Hegseth out by 31.03.2027) | 0.177 | Kalshi 0.555 | +0.38 | EXACT | ASSESSMENT: the Kalshi term structure is steep (before 01.01.2027 about 0.15; before 01.02 about 0.27; before 01.04 about 0.56), so traders expect a departure tied to an early-2027 event — most plausibly the new Democratic House majority from 03.01.2027 (impeachment hearings, oversight on the Iran war). Our 18.11–31.12 portion agrees with the market (Kalshi announce-or-leave by 01.01 0.185, Manifold 0.125); the gap is in Q1 2027. The lenses may have under-weighted the post-January Congress. |
| Q-0017 (ECB hike 17.12) | 0.693 | Kalshi 0.985, GJO 0.749 | +0.29 / +0.06 | EXACT | ASSESSMENT: the red team's +0.15 (the limit) moved AGG toward the market, and the limit, not the evidence, capped it (05 §3). Kalshi agrees with the unanimous Reuters poll (R-01); GJO's slower-updating crowd sits near our value. Volume on the Kalshi event is modest (about 8.7k contracts). Lenses A and C relied on the oil fall, which the market and the economists had already priced. Evidence for L3: the ±0.15 limit can bind when the evidence is strong. |
| Q-0133 (PP most seats, 29.11) | 0.687 | Manifold 0.893 | +0.21 | EXACT | ASSESSMENT: low-liquidity play-money market (11 traders, no written criterion, tie treatment unstated). Our criterion counts a tie as NO and uses the provisional 100% count; that explains little of the gap. The lenses may have discounted polling leads more than the crowd does. Weak benchmark. |
| Q-0132 (US–China–Russia joint leaders' statement 18–22.11) | 0.310 | Kalshi 0.990 (trilateral meeting) | +0.68 | APPROX | Different event: the market prices a three-leader meeting (with Shenzhen under way at quote time); a meeting is necessary, not sufficient, for a joint statement. The gap mostly measures P(statement given meeting), which the lenses put low. Not evidence of an error. |
| Q-0121 (US–UA–RU delegations meet by 31.12) | 0.583 | Kalshi 0.060 (Trump–Zelenskyy–Putin in person) | −0.52 | APPROX | Different event: the market requires the three presidents in one room; our question counts any level of government delegations (as in the trilateral rounds earlier in 2026). The market value is a lower bound, not a counterpart. Not evidence of an error. |

APPROX matches below the threshold but worth noting: Q-0100 (+0.18): the trilateral market at 0.99 during the summit window suggests Putin's attendance in Shenzhen was priced as near-certain on 18.11 — information after the cutoff. Q-0118 (−0.15, EXACT, just under the threshold): the market puts a December Bank of Russia cut lower than our lenses; Kalshi volume is low (about 6k contracts on the hold option).

## 4. Summary

- 10 questions have an EXACT counterpart (12 rows); these enter the crowd BSS after resolution. Three EXACT questions show |Δ| ≥ 0.20 with deep markets (Q-0142, Q-0122, Q-0017), all in the direction "crowd more confident of change than we are"; one with a shallow play-money market (Q-0133).
- Direction across the 12 EXACT rows: the crowd is above AGG_RT in 9, below in 3. ASSESSMENT (low confidence, n = 10 questions): on scheduled central-bank decisions the lenses sit closer to 0.5 than the markets — a pattern to test in L2 against resolutions (Q-0017, Q-0142 resolve in December).
- Access gaps: Polymarket unreachable from this environment (connection refused / DNS), Metaculus 403. The edition 02 record had 32 Polymarket rows; this edition has none, so the crowd comparison is thinner (58 of 83 questions without any counterpart).
- No forecast was changed after the benchmarks were seen.

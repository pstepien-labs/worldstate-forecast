# Stage 06 — Benchmarks (edition 02, state 07.10.2026)

The benchmarks were collected **after** the "forecasts frozen" commit (f09a1d4). The material is for review. It is **not** grounds for changing forecasts: no forecast was changed. It does not go into the main report (methodology §6); it goes into `07_annex_benchmarks.md`.

## 1. Sources and access

| Source | Access | Result |
|---|---|---|
| Polymarket | Public read-only API (gamma-api.polymarket.com: `events?slug=`, `public-search`) | 32 rows |
| Kalshi | Public read-only API (api.elections.kalshi.com: `series`, `events?series_ticker=`) | 18 rows |
| Manifold | Public API (api.manifold.markets: `search-markets`, `slug`) | 10 rows (play currency; liquidity usually low) |
| Good Judgment Open | Public pages read with the web-fetch tool in the stage re-run of 10.10.2026 (the first attempt of 09.10 got a login redirect / HTTP 406 for the command-line client). The general question list shows only page 1 without login; questions were found through public challenge pages (In the News 2026 with tag filters, Iran & Energy, Global Armed Conflict in 2026, A Challenge of Interest!, Q4 Finance and Economics, 2026 US Midterms, 2026 World Elections) and site-restricted web searches. No login (CLAUDE.md §6) | 8 rows (crowd forecasts; numbers of forecasters not shown on public pages) |
| Metaculus | API returns HTTP 403 "only available to authenticated users". No login | 0 rows |
| RAND Forecasting Initiative | Platform closed (edition 01 finding); not re-checked | 0 rows |

Recording convention (as in edition 01): p = midpoint of the bid/ask spread (Polymarket `outcomePrices`; Kalshi (bid+ask)/2, summed over outcome buckets where our event is a union of buckets); converted values (1 − p) are stated in `notes`. Values outside 0.01–0.99 would be clipped (none needed). GJO: crowd forecast of the option, or the sum of options where our event is a union of bins. Date of quotes: Polymarket, Kalshi, Manifold 09.10.2026, about 23:40–23:55 Warsaw time; GJO 10.10.2026, about 02:20–02:40 Warsaw time. Record in `registry/benchmarks.csv`: **68 rows for 40 questions; 32 EXACT rows for 16 questions.**

## 2. Matches

The AGG_RT column is the official frozen forecast. Δ = crowd − AGG_RT; |Δ| ≥ 0.20 in bold (Q-0026 Polymarket +0.197 and Q-0028 Polymarket +0.198 display as +0.20 but are below the threshold).

| ID | Question (short) | AGG_RT | Source | Crowd p | Match | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Will the president of Russia sign by 31.12.2026 a decree announcing mobilis… | 0.030 | Polymarket | 0.100 | APPROX | +0.07 |
| | | | Manifold | 0.305 | EXACT | **+0.28** |
| Q-0007 | Will the settlement price of the ICE Brent front-month contract exceed 120… | 0.230 | GJO | 0.840 | APPROX | **+0.61** |
| Q-0015 | Will the USA introduce a tariff on EU goods exceeding the 15% ceiling set i… | 0.103 | Kalshi | 0.395 | APPROX | **+0.29** |
| Q-0016 | Will the Monetary Policy Council change the NBP reference rate at any meeti… | 0.267 | Kalshi | 0.365 | APPROX | +0.10 |
| Q-0017 | Will the ECB raise the deposit rate at a meeting held between 24.09 and 31.… | 0.493 | Polymarket | 0.773 | APPROX | **+0.28** |
| | | | Kalshi | 0.785 | APPROX | **+0.29** |
| | | | GJO (October only) | 0.193 | APPROX | **−0.30** |
| | | | GJO (December only) | 0.406 | APPROX | −0.09 |
| Q-0018 | Will OFAC add to the SDN list by 31.03.2027 a bank registered in mainland P… | 0.077 | Kalshi | 0.255 | APPROX | +0.18 |
| Q-0020 | Will the Bank of Russia cut its key rate at the meeting scheduled for 23.10… | 0.143 | Polymarket | 0.125 | EXACT | −0.02 |
| | | | Kalshi | 0.135 | EXACT | −0.01 |
| Q-0021 | Will the PRC announce by 10.11.2026 an extension or repeal of the suspensio… | 0.740 | Manifold | 0.870 | APPROX | +0.13 |
| Q-0026 | Will a trilateral meeting of government delegations of the USA, Ukraine and… | 0.283 | Polymarket | 0.480 | APPROX | +0.20 |
| | | | Kalshi | 0.040 | APPROX | **−0.24** |
| Q-0027 | Will any NATO state submit a request for consultations under Article 4 of t… | 0.107 | Polymarket | 0.255 | EXACT | +0.15 |
| Q-0028 | Will the USA and Iran announce by 31.12.2026 the conclusion of an agreement… | 0.157 | Polymarket | 0.355 | EXACT | +0.20 |
| | | | Kalshi | 0.115 | APPROX | −0.04 |
| Q-0029 | Will Donald Trump personally attend the APEC leaders' meeting in Shenzhen (… | 0.643 | Polymarket | 0.810 | APPROX | +0.17 |
| Q-0030 | Will Vladimir Putin and Donald Trump meet in person by 31.03.2027? | 0.317 | Polymarket | 0.810 | APPROX | **+0.49** |
| | | | Manifold | 0.274 | APPROX | −0.04 |
| Q-0031 | Will the Republican Party win at least 218 seats in the House of Representa… | 0.107 | Polymarket | 0.095 | EXACT | −0.01 |
| | | | Kalshi | 0.105 | EXACT | −0.00 |
| | | | Manifold | 0.070 | EXACT | −0.04 |
| | | | GJO | 0.204 | EXACT | +0.10 |
| Q-0032 | Will a new video or audio recording of Mojtaba Khamenei speaking be publish… | 0.103 | Polymarket | 0.185 | APPROX | +0.08 |
| Q-0033 | Will Luiz Inácio Lula da Silva win the 2026 presidential election in Brazil… | 0.290 | Polymarket | 0.105 | EXACT | −0.18 |
| | | | Kalshi | 0.115 | EXACT | −0.17 |
| | | | Manifold | 0.140 | EXACT | −0.15 |
| | | | GJO | 0.260 | EXACT | −0.03 |
| Q-0034 | Will the CNE or the government of Venezuela announce a specific date for th… | 0.320 | Polymarket | 0.105 | APPROX | **−0.22** |
| Q-0035 | Will Assimi Goïta cease to hold power in Mali by 31.03.2027 (coup, resignat… | 0.070 | Polymarket | 0.050 | APPROX | −0.02 |
| Q-0036 | Will the 7-day average number of transits through the Strait of Hormuz per … | 0.103 | Kalshi | 0.170 | EXACT | +0.07 |
| | | | Polymarket | 0.175 | APPROX | +0.07 |
| | | | GJO (≥ 35, by 11.01) | 0.150 | APPROX | +0.05 |
| Q-0038 | Will the USA officially lift or suspend the naval blockade of Iranian ports… | 0.143 | Polymarket | 0.479 | EXACT | **+0.34** |
| Q-0065 | Will CENTCOM or the Pentagon announce a US strike on a target on Iranian la… | 0.350 | Polymarket | 0.665 | APPROX | **+0.32** |
| Q-0066 | Will the FOMC raise the target range for the federal funds rate at the 27–2… | 0.177 | Polymarket | 0.159 | EXACT | −0.02 |
| | | | Kalshi | 0.160 | EXACT | −0.02 |
| | | | Manifold | 0.180 | EXACT | +0.00 |
| | | | GJO | 0.158 | EXACT | −0.02 |
| Q-0068 | Will US forces carry out a strike on Houthi targets in Yemen by 31.12.2026? | 0.233 | Polymarket | 0.170 | APPROX | −0.06 |
| Q-0069 | Will the DSCA notify Congress by 31.12.2026 of arms sales to Taiwan with a … | 0.120 | Manifold | 0.169 | APPROX | +0.05 |
| Q-0073 | Will ISW assess by 30.06.2027 that Russian forces have taken control of the… | 0.070 | Polymarket | 0.160 | APPROX | +0.09 |
| | | | Manifold | 0.147 | APPROX | +0.08 |
| Q-0074 | Will the settlement price of the ICE Brent front-month contract on 20.10.20… | 0.633 | Kalshi | 0.665 | EXACT | +0.03 |
| Q-0076 | Will the FAO Food Price Index (FFPI) for October 2026 be higher than 136.0 … | 0.560 | Kalshi | 0.350 | EXACT | **−0.21** |
| Q-0078 | Will IMF PortWatch record at least 10 transits through the Strait of Hormuz… | 0.083 | Kalshi | 0.350 | APPROX | **+0.27** |
| | | | Polymarket | 0.365 | APPROX | **+0.28** |
| Q-0081 | Will representatives of the US and Iranian governments meet in person in th… | 0.103 | Polymarket | 0.175 | APPROX | +0.07 |
| | | | Kalshi | 0.155 | APPROX | +0.05 |
| Q-0082 | Will a trilateral meeting of government delegations of the USA, Ukraine and… | 0.107 | Polymarket | 0.460 | APPROX | **+0.35** |
| Q-0088 | Will the Bank of Russia raise its key rate at the board meeting scheduled f… | 0.083 | Polymarket | 0.026 | EXACT | −0.06 |
| | | | Kalshi | 0.025 | EXACT | −0.06 |
| Q-0093 | Will Iliana Iotova win more than 50% of valid votes in the first round of B… | 0.267 | Polymarket | 0.085 | APPROX | −0.18 |
| Q-0094 | Will Likud win the largest number of seats in the Knesset election of 27.10… | 0.467 | Polymarket | 0.515 | EXACT | +0.05 |
| | | | Kalshi | 0.505 | EXACT | +0.04 |
| | | | Manifold | 0.500 | EXACT | +0.03 |
| Q-0095 | Will the Republican Party hold at least 50 seats in the US Senate after the… | 0.427 | Polymarket | 0.365 | EXACT | −0.06 |
| | | | Kalshi | 0.395 | EXACT | −0.03 |
| | | | Manifold | 0.345 | EXACT | −0.08 |
| | | | GJO | 0.470 | EXACT | +0.04 |
| Q-0096 | Will Abbas Araghchi cease to be Iran's foreign minister by 31.12.2026? | 0.150 | Polymarket | 0.115 | EXACT | −0.03 |
| Q-0099 | Will a USNI News Fleet and Marine Tracker show at least three US aircraft c… | 0.467 | Polymarket | 0.220 | APPROX | **−0.25** |
| Q-0100 | Will Vladimir Putin personally attend the APEC leaders' meeting in Shenzhen… | 0.617 | Polymarket | 0.810 | APPROX | +0.19 |
| Q-0106 | Will the US government impose a ban or mandatory quota on exports of diesel… | 0.067 | Polymarket | 0.110 | APPROX | +0.04 |
| Q-0110 | Will Russia and Ukraine both confirm by 30.06.2027 a signed agreement on a … | 0.083 | Polymarket | 0.505 | APPROX | **+0.42** |
| Q-0113 | Will ISW assess by 31.03.2027 that Russian forces have taken control of the… | 0.240 | Polymarket | 0.410 | EXACT | +0.17 |

No counterparts were found for 48 questions: Q-0002, Q-0003, Q-0004, Q-0005, Q-0008, Q-0009, Q-0010, Q-0012, Q-0019, Q-0022, Q-0023, Q-0024, Q-0025, Q-0037 (past its deadline, markets closed), Q-0039, Q-0040, Q-0049 (past its deadline), Q-0067, Q-0070, Q-0071, Q-0072, Q-0075, Q-0077, Q-0079, Q-0080, Q-0083, Q-0084, Q-0085, Q-0086, Q-0087, Q-0089, Q-0090, Q-0091, Q-0092, Q-0097, Q-0098, Q-0101, Q-0102, Q-0103, Q-0104, Q-0105, Q-0107, Q-0108, Q-0109, Q-0111, Q-0112, Q-0114, Q-0115. This includes the whole TTF/AGSI+ energy cluster, Brent thresholds over long windows (Polymarket lists WTI only; GJO's Brent questions use the EIA spot series or single dates), H.R. 5334 tariffs and the Russia SDN/EU package questions, Taiwan (exercises, MND counts, DSCA ≥ 1 bn USD), Polish macro and rating questions, the Baltic and Black Sea infrastructure questions, and the US–PRC truce formalisation questions (Q-0102, Q-0108, Q-0077). GJO questions seen but not matched: EU gas storage maximum in TWh 15.09–15.11 (Q-0067 is in percent on one day; conversion needs the storage capacity, not verified), Likud seat count and first mandate to Likud (Q-0094 is about the largest party), US deployment of forces to mainland Iran or Kharg (Q-0065 is about strikes), Article 5 invocation (Q-0027 is Article 4); the GJO Russia–Ukraine agreement question closed on 01.10.2026.

## 3. Discrepancies |AGG_RT − crowd| ≥ 0.20: hypotheses about causes

The hypotheses are working hypotheses intended for review. They do not decide who is right.

**EXACT matches**

1. **Q-0038 — US lifts or suspends the Iran blockade by 31.12 (Polymarket, option volume approx. 3.1 mn USD).** The lenses tied a blockade lift to a US–Iran deal (05 §2.3: lift and Hormuz opening "both below the deal probability, with a small unilateral share"). The market prices the deal path itself much higher (US–Iran Hormuz agreement by 31.12: 0.355 vs our Q-0028, a gap just below the threshold) and probably a unilateral suspension as a bargaining step after 03.11. Note the internal consistency of the market: Kalshi's "US–Iran nuclear deal" (0.115) is close to our Q-0028 — the market separates a Hormuz/shipping arrangement from a nuclear deal; our lenses did not make this split. Hypothesis: an omitted path (a narrow shipping arrangement without a nuclear deal), the same type of error as Q-0030 in edition 01.
2. **Q-0001 — Russian mobilisation decree (Manifold 18 traders, play currency).** Same discrepancy as in edition 01. The liquid Polymarket market (broader criterion) has fallen to 0.10 and is now within 0.07 of our forecast. Hypothesis: illiquid market with a tail premium; not informative.
3. **Q-0076 — FAO Food Price Index for October above 136.0 (Kalshi, 200 contracts, spread 0.31/0.39).** The Kalshi ladder puts the median of the October index near 135, i.e. a small decline from September; the lenses expected a small rise. Hypothesis: the lenses weighted energy and freight cost pass-through (Brent about 100) while the market weights seasonal harvest pressure on cereals and vegetable oils; low liquidity makes the market a weak signal.

**APPROX matches (outside the scores; for review only)**

4. **Q-0007 — Brent above 120 (GJO: highest EIA Brent spot close 19.07–04.12 at least 120 USD, 0.84).** Different series: the EIA/FRED spot series (DCOILBRENTEU) stood at 135.51 on 02.10.2026 and 125.44 on 06.10.2026, far above the ICE front-month settlement that our question uses, and the GJO window starts on 19.07. Hypothesis: series and window mismatch — the crowd value records an already observed spot peak; uninformative for our criterion. Note for resolution: Q-0007 must be resolved on ICE settlements, not on the EIA spot series.
5. **Q-0030 — Putin–Trump meeting by 31.03.2027 (Polymarket by 31.12: 0.81; location market: China 0.735).** The same discrepancy as edition 01 (then 0.765). The market assumes both leaders at APEC Shenzhen and a meeting there; the "Trump, Putin and Xi seen together before 2027" market (0.81) implies the market puts joint presence near 0.8, while the red team estimated joint presence at about 0.40–0.45 from our Q-0029 (0.643) and Q-0100 (0.617), both of which sit below the market's implied attendance (gaps +0.17 and +0.19). Hypothesis: the lenses treat each leader's attendance as independently uncertain, the market treats it as coordinated. The resolution risk flagged in 05 §2.3 (does a shared plenary count as a meeting) still applies.
6. **Q-0110 — signed full-front ceasefire confirmed by both sides by 30.06.2027 (Polymarket 0.505).** The market criterion is broader (any mutually agreed suspension of direct military engagement, including a framework with an effective date), which explains part of the gap but hardly a factor of six. Hypothesis: the lenses anchored on the October stalemate (Moscow's "no current plans" for a trilateral; talks "declined for now"), the market prices a nine-month window in which a post-election US push may succeed. Our nested Ukraine questions (Q-0026, Q-0082) are also below the markets.
7. **Q-0082 and Q-0026 — trilateral delegation meetings.** Polymarket measures any RU–UA meeting (bilateral or via mediators), Kalshi a leaders' trilateral. Our questions lie between them; the discrepancies come from the criterion, not from judgement (as in edition 01).
8. **Q-0065 — US strike on Iranian land by 31.12 (converted from a ceasefire-breakdown market, 0.665).** A breakdown can occur through Iranian action or strikes at sea, so the market is an upper bound; the gap (+0.32) is similar to edition 01 (+0.29). Hypothesis: as in edition 01, the market prices a higher post-03.11 breakdown risk than the "electoral brake" assumption KA1 allows (05 §1 item 3).
9. **Q-0017 — ECB hike at a meeting in X–XII (December market 0.77–0.79).** Repeated direction from edition 01 (+0.21 then, +0.28/+0.29 now) with the December market only (a lower bound for our union of two meetings). Hypothesis: the lenses keep weighting economists' and ECB speakers' caution over market pricing — a recurring pattern worth checking in L2/L3 once Q-0017 resolves. The GJO crowd disagrees with the markets: October only 0.193 (the −0.30 gap is a window effect — one of our two meetings), December only 0.406 against 0.77–0.79 on Polymarket and Kalshi; combined as if independent the two GJO questions give about 0.52, close to AGG_RT. The crowd sources are split on this question, so the discrepancy with the markets is not a consensus signal.
10. **Q-0078 — ≥ 10 Hormuz transits on a day in 08–17.10.** Both counterparts cover the whole of October; Kalshi's weekly peak markets ("above 10": 0.045 for 05–11.10, 0.065 for 12–18.10) are close to our value. Hypothesis: window and threshold mismatch — uninformative.
11. **Q-0099 — three US carriers in CENTCOM at once by 30.11 (market for 30.11 only: 0.22).** A single-date market is a lower bound for "any weekly tracker"; event volume approx. 4k USD. Hypothesis: the lenses gave weight to the third carrier group signal of 03 (CRIS) and to eight weekly observation points; partly a criterion effect.
12. **Q-0034 — Venezuela election date announced by 31.03.2027 (Polymarket by 31.12: 0.105).** Three months of the window are missing from the market; hypothesis: the rest of the gap reflects the lenses' weight on political statements about elections, which the market discounts.
13. **Q-0015 — US tariff on EU goods above the 15% ceiling (Kalshi "tariff rate ≥ 20%" on 01.01.2027).** Volume 81 contracts and an unchecked rate definition (possibly an average including section 232 duties, which our criterion excludes). Uninformative.

**Discrepancies below the threshold worth noting.** Q-0033 Lula: three markets (0.105–0.14) and GJO (0.26; the parallel GJO question 5169: 0.23) against our 0.29 after the first round — the gap narrowed from edition 01 but keeps the same sign (we overrate Lula relative to markets; GJO is close to us). Q-0031 House: GJO 0.20 (converted) against markets 0.07–0.105 and our 0.107 — GJO is the outlier. Q-0113 Kostiantynivka (EXACT, +0.17) and Q-0027 Article 4 (EXACT, +0.15): markets higher than us, as in edition 01 for Article 4. Q-0093 Bulgaria: the market counterpart also requires turnout above 50%, so it is a lower bound; not comparable.

## 4. Consistency check of the benchmarks

- Agreement on the liquid EXACT markets: Q-0066 (FOMC 28.10 — the large edition 01 discrepancy has disappeared; three markets and GJO within 0.02 of AGG_RT after the red-team adjustment), Q-0020/Q-0088 (Bank of Russia), Q-0031 (House), Q-0094 (Likud most seats), Q-0095 (Senate), Q-0096, Q-0074 — all within 0.08.
- Cross-market inconsistencies: Hormuz — Polymarket "normal by 31.12" (0.175) vs Kalshi > 40 (0.17) and > 60 (0.095): Polymarket's narrower event is priced higher, as in edition 01. Bulgaria — Polymarket first-round winner (Iotova 0.965) and "outright win" (0.085) are consistent only because of the turnout condition. ECB December — GJO 0.41 against Polymarket/Kalshi 0.77–0.79 (see §3 item 9). House — GJO 0.20 against markets 0.07–0.105. Hormuz — GJO ≥ 35 by 11.01 (0.15) is below Kalshi > 40 by 31.12 (0.17), although the GJO event is broader.
- 16 questions with an EXACT match will enter the scores (BSS vs crowd): Q-0001, Q-0020, Q-0027, Q-0028, Q-0031, Q-0033, Q-0036, Q-0038, Q-0066, Q-0074, Q-0076, Q-0088, Q-0094, Q-0095, Q-0096, Q-0113. When one question has several sources, `scores.py` averages them. GJO adds EXACT rows to Q-0031, Q-0033, Q-0066 and Q-0095 (no new question).

## 5. Reports

- No forecast was changed. No login to any service; only public read-only APIs and public web pages (GJO, FRED) were read.
- No injected instructions were found in API responses or page content.
- Gaps: Good Judgment Open was read in the re-run of 10.10.2026 (public challenge pages; the full question list needs a login, so GJO questions outside the challenges and searches used may have been missed; numbers of forecasters are not shown on public pages). Metaculus still requires an account; RAND Forecasting Initiative closed. Of the six sources in methodology §6, four were read in this edition.
- Post-freeze facts recorded only as benchmark context: FRED DCOILBRENTEU 135.51 (02.10.2026) and 125.44 (06.10.2026), read 10.10.2026 for the Q-0007 note; not used for any forecast.

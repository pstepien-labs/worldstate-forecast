# L3 — Reasoning trace of misses and hits (scope `latest`)

Run: 19.11.2026 · stage L3 · framework 1.9.2 · methodology v1.0 · model claude-opus-5-5 · commit at start be65911 · unattended autopilot run (AUTO mode of `prompts/RUN_learning.md`).

**Scope resolution.** `latest` was resolved to **edition 02**: state date 07.10.2026, forecasts dated 09.10.2026. This is the same reading as L1 and L2 in this folder. Edition 03 (state date 16.11.2026) has no resolved questions, so there is nothing to trace.

**Versions.** Every stage traced here (H, 02, 03, 04 A/B/C, 05, 06) ran under **framework 1.4.0**, methodology v1.0, model **claude-opus-5-5** (`editions/2026-10-07_edition-02/provenance.md`). The resolutions come from stage 01 of edition 03 (framework 1.8.0, 16.11.2026), and some were confirmed by stage V. No version comparison is possible.

**Selection.**
- **Misses:** the ten largest AGG_RT errors from `L2_performance.md` §7.1.
- **Hits:** the five lowest-Brier calls from L2 §7.2: Q-0039, Q-0083, Q-0031, Q-0102 and Q-0021. All five departed from the status quo by at least 0.20. Q-0093 (rank 6, Brier 0.071) was left out because the prompt limits hits to 5.
- **Sample.** 15 questions in 12 clusters. This is far below 30 (learning rule 2), so the findings describe and do not conclude.
- **L1 links.** L1 surprises that bear on the selected questions are cited: #1 Tribunal crisis → Q-0105; lesson 2 single statements → Q-0026 and Q-0065.

**Method.**
- The chain was read only from edition 02 files: `02_harvest/` digests, `coverage.md` and `indicators.md`; `02_facts/G1–G4.md`; `03_analysis.md` (KA, ACH, I&W); `04_forecasts_A/B/C.md`; `05_red_team.md`; `06_aggregation.md`; and the registry rows.
- The harvest corpus was searched for 23.09–09.10.2026 with `python3 -m tools.harvester search`.
- Each question was then compared with the edition 03 `01_resolutions.md` and the edition 03 fact records, which are dated hindsight.
- Lens values are quoted because L3 traces the reasoning. This file is under `reviews/learning/` and is closed to stages 03–05 (CLAUDE.md rule 3.8). No benchmark or crowd value is used.

**Hindsight is dated** (learning rule 3). "Knowable on 09.10" means public on or before the forecast date of 09.10.2026. The lenses were allowed to search after the state date, and they recorded those finds as additional facts A-/B-/C-xx.

---

## 1. Traces — misses

Notation for each question: lens values A / B / C → AGG → AGG_RT; SQ = p_status_quo; outcome.

### M1 · Q-0026 US–UA–RU trilateral of government delegations by 30.11 (UA_TALKS / DIP)

0.30 / 0.30 / 0.25 → 0.283 → 0.283; SQ 0.10. **YES** on 10.11 (Abu Dhabi, 10–11.11).
Edition 01 had AGG_RT 0.45. The forecast moved away from the outcome.

| Step | Finding |
|---|---|
| Harvest | **The decisive signals were in the corpus before the forecasts were made, but after the digest window closed.** Axios via TASS (08.10 22:22) and Meduza (09.10 06:55): Witkoff and Kushner have "new ideas" and plan to visit Moscow in late October. TASS 09.10: "Witkoff, Kushner always welcome in Moscow", plus a summary on a future Putin–Trump call. Polsat 09.10, Ukrainska Pravda 09.10: US–Ukraine talks in Florida on a new proposal. The G4 digest ends on 07.10 and holds only the NYT/Lukoil item. Sides: A-RU (TASS), A-UA, W, exile |
| Facts | G4-019 (Putin at Valdai, A/1), G4-021 (Zelensky: US proposes a trilateral, B/2, A), G4-022 (Ryabkov: "no current plans", B/1, A). All three are correctly marked as facts about statements (rule 3.4). The perspective is A-only on both sides. No T record (for example a Turkish or UAE host) |
| Analysis | ACH Q2: H1 "return to structured talks" had the most I ratings (6), all from Russian statements. H2 "bilateral channel only" was least refuted. Indicator I14 was changed to "declined for now". The mirror test asked nothing about whether Moscow's refusal of the format was a bargaining position |
| Lenses | **A** 0.30: Moscow "uses the format as a reward"; that rises only if Trump trades it. **B** 0.30: reference class "resumption within ~7 weeks after an explicit 'no current plans'" put at 0.25–0.35, with no cases cited. **C** 0.25: the 09.10 call (C-01) "produced only an agreement to keep leader contacts". A and B tie as closest. All three anchored on Ryabkov. None found the Axios/Witkoff item |
| Red team | Considered the question (§3, line "Q-0026 / Q-0082 / Q-0030") and said the 09.10 call "produced no trilateral date" — **no adjustment**. Its own point 1 found the US easing toward Moscow (GL 135) but did not carry it over to the talks questions |
| Aggregation | AGG = AGG_RT. Nothing rejected |
| Resolution | Clean, high confidence: Kyiv Independent and ABC, with Peskov naming the Russian delegation |
| Hindsight | Witkoff–Putin meeting on 21.10. Putin accepted the trilateral on 22.10 (ed.03 G4-015, G4-016). The Axios plan of 08.10 came true |

- **Signal lost at:** Lenses. Secondary: Red team. The lenses' post-state-date searches did not cover the corpus between 07.10 and 09.10.
- **Cause:**
  - Primary: **source bias**. One party's statement of present intent ("no current plans") was treated as a forecast of its behaviour seven weeks later (L1 lesson 2).
  - Secondary: **information collected but not used**. The Axios item was in the corpus 10–20 hours before the lenses ran.
- **Counterfactual:** a lens-stage "corpus delta" read, i.e. a corpus search on each question's key indicator for state date → forecast date. Add a stated base rate for how often an explicit refusal by a government is reversed within the question window.
  - Effect on hits: none. For Q-0083 the same delta read would only have confirmed the Council date.

### M2 · Q-0033 Lula wins the 2026 Brazilian presidential election (BRAZIL_ELECTIONS / DOM)

0.30 / 0.25 / 0.32 → 0.29 → 0.29; SQ 0.90. **YES** on 25.10 (51.79% vs 48.21%).
Edition 01 had AGG_RT 0.557. The forecast moved away, on genuine new information.

| Step | Finding |
|---|---|
| Harvest | Rich coverage: Brazil 1,356 items from 3 feeds, pt-BR, independent (`coverage.md`). The corpus on 05–09.10 pointed one way: endorsements for F. Bolsonaro, a Datafolha runoff poll of 52–48, FT "eyeing victory". **The decisive information was not collectable on 09.10.** The eve-of-runoff Datafolha (24.10, G1 Globo, corpus) still had F. Bolsonaro at 51–49. The polls missed by about 3.6 points toward Lula |
| Facts | G4-029 (TSE result, A/1, A/W), G4-030 (endorsements, B/2), G4-031 (Trump, B/2), G4-032 (pre-election polls had understated the right, B/2, T/A). Good three-perspective coverage |
| Analysis | E — Brazil: "PIR-7's largest orientation change". L1 §4.1 #19 found that the report framed a rightward shift as the likely outcome. There was no ACH on Brazil |
| Lenses | **A** 0.30 and **C** 0.32: "polls understated the right in round one", which assumes the polling error keeps its direction. **B** 0.25: reference class "the first-round leader won 7 of 7 runoffs since 1989". C was closest. All three had medium confidence |
| Red team | Checked it and called it "consistent with the facts" (§3) |
| Aggregation | AGG = AGG_RT |
| Resolution | Clean, high confidence. TSE confirmation via NPR and Al Jazeera |

- **Signal lost at:** not lost. The signal did not exist on 09.10.
- **Cause:**
  - Primary: **noise**. The forecast was reasoned well because it used the actual first-round result, every endorsement and the only runoff poll. Even the poll taken on the eve of the vote pointed the same way.
  - Secondary: **reaction**. Two lenses assumed the round-one polling bias would persist in the same direction. B's 7-of-7 reference class is small (N = 7) and ignores how narrow this lead was (1.9 pp).
- **Counterfactual:** cap analytic confidence at "low" when the poll margin is smaller than the polling error recently observed in the same election. Do not assume that a polling error keeps its direction.
  - This would have moved the forecast slightly toward 0.5 and would not have flipped it.
  - Effect on hits: none. Q-0031 rested on a 7-point generic-ballot margin, far above the polling error.

### M3 · Q-0105 S&P downgrade or negative outlook for Poland by 06.11 (PL_FINANCE / FIN)

0.40 / 0.28 / 0.30 → 0.327 → 0.327; SQ 0.10. **YES** on 06.11: local-currency rating to A-, outlook to negative. Auto-verified.

| Step | Finding |
|---|---|
| Harvest | No item in the corpus about S&P and Poland between 23.09 and 09.10. The G3 digest has 19 "rating" lines and none is about Poland. **Rule-of-law and veto precursors were in the Polish corpus but did not reach a digest** (L1 §6 #1: TVN24, Polsat and Bankier, 05–07.10). On 02.11 Bankier asked whether "the dispute over the Tribunal will hit Poland's rating?" (corpus). S&P's stated reasons on 06.11 were high deficits, political polarisation and presidential vetoes that obstruct consolidation (Notes from Poland 07.11, https://notesfrompoland.com/2026/11/07/rating-agency-sp-shifts-polands-credit-outlook-to-negative-and-lowers-currency-rating/; search 19.11) |
| Facts | G3-046 (MF vs Fiscal Council, B/2, A), G3-047 (Domański, B/1, A), G3-048 (World Bank growth upgrade, C/3), G3-049 (rating state: Moody's A3 after the 09.2026 cut, Fitch A− negative, S&P A− stable, S&P deficit forecast raised to 7.0%, review on 06.11, B/1, A). **The W perspective gap was recorded** ("no foreign-press item on Polish public finances"). The polarisation and veto risk had no record |
| Analysis | Not covered: no KA, ACH or indicator on Poland's sovereign rating. I18 (EUR/PLN) is the only Polish financial indicator |
| Lenses | **A** 0.40, the closest: "close to even" given the deficit and peer moves. **B** 0.28: generic reference class "outlook changes at scheduled S&P reviews 10–15%", adjusted up. **C** 0.30: "kept the outlook stable through earlier deterioration". The World Bank upgrade (C/3, numbers inconsistent) was used against YES by A and C |
| Red team | Consistency check only, against Q-0070 (not nested; OK) |
| Aggregation | AGG = AGG_RT |
| Resolution | **Ambiguous** (stage 01 §ambiguous): the scope of the outlook change between FC and LC. Confirmed by stage V (user_approved = A). Reports differ on whether the negative outlook covers the FC rating (kurs.com.ua vs Notes from Poland; search 19.11) |

- **Signal lost at:** Lenses (reference class). Secondary: Harvest digest, because the polarisation precursors never reached the facts.
- **Cause:**
  - Primary: **base rate**, wrong reference class. The generic outlook-change rate ignores the conditional case: an agency still on stable when both peers have already moved (Fitch negative since 09.2025, Moody's downgrade 09.2026), and right after it raised its own deficit forecast.
  - Secondary: **information collected but not used** (L1 surprise #1).
- **Counterfactual:** for rating questions, B uses the conditional reference class "last agency after peer action plus its own adverse forecast revision". The digest routes Polish rule-of-law and veto items to G3/PIR-6 (an L4 topic).
  - Effect on hits: none. No hit is a rating question.
- **Caveat:** if a later reading of the S&P release shows the FC outlook unchanged, this would become a resolution error, not a forecasting miss.

### M4 · Q-0065 CENTCOM/Pentagon/White House confirms a US strike on Iranian land by 31.12 (IRAN_WAR / MIL)

0.33 / 0.32 / 0.40 → 0.35 → 0.35; SQ 0.10. **YES** on 06.11. Auto-verified.
Edition 01 had AGG_RT 0.26. The forecast moved toward the outcome, but not far enough.

| Step | Finding |
|---|---|
| Harvest | Collected. Al Jazeera 02.10, CGTN 03.10 and Maritime Executive 02.10 on the third carrier group; the "after the elections" strike options (CBS/Fox via Iran International, Al Jazeera Arabic). Sides: W, T, exile; no Iranian state account of US intent |
| Facts | G1-009 (B/2; departures DONE, end-state DECL), G1-010 (C/3, an exile outlet as W), G4-008 (B/2: Trump, renewed strikes after the midterms "possible") |
| Analysis | **KA1** "no strike before 03.11" (medium); ACH Q1: H3 "weakened before 03.11, not after"; I3; mirror test item 3 ("brake, then release"). The analysis saw the post-election window |
| Lenses | **A** 0.33, **B** 0.32 (hazard of 4–5% per two weeks, adjusted up), **C** 0.40 (Trump "reportedly told aides he expects to resume bombing", C-04). C was closest. **All three reasoned about the costs of a resumed bombing campaign**: diesel prices, 32% approval, the APEC/G20 summits. The criterion is met by any confirmed strike on a land target, however small |
| Red team | Point 3: KA1 makes Q-0065, Q-0007, Q-0068, Q-0099, Q-0074, Q-0084 and others "one correlated bet". **No adjustment**, for lack of counter-evidence |
| Aggregation | AGG = AGG_RT |
| Resolution | **Ambiguous.** The President's remarks to reporters on 06.11 count as a White House statement; CENTCOM declined to comment. Confirmed by stage V. The event: "minor strikes" on an anti-aircraft site on Qeshm, called "defensive" (02.11), during the sea war over Hormuz (ed.03 G1-005) |

- **Signal found but under-weighted at:** Lenses.
- **Cause:**
  - Primary: **base rate**, a reference class that did not match the criterion. The lenses priced a decision to restart a campaign. The question resolves on the smallest confirmed land strike, and a small strike is likely in a live blockade and tanker war with three carriers arriving.
  - Secondary: **correlation**. KA1 was flagged by the red team as one shared bet and was carried unchanged.
- **Counterfactual:** before a lens gives p, it writes down "the smallest event that resolves YES" and asks how likely that event is, not the event the question title suggests.
  - Effect on hits: for Q-0083 and Q-0102 the smallest resolving event is a routine document, so the step would only reinforce them. No hit is hurt.

### M5 · Q-0075 Polish October CPI flash below 3.5% y/y (PL_INFLATION / ECO)

0.68 / 0.65 / 0.60 → 0.643 → 0.643; SQ 0.10. **NO** on 31.10: the flash was **exactly 3.5%** (−0.4% m/m; fuels −9.7% m/m). The PAP consensus before the release was 3.7%.

| Step | Finding |
|---|---|
| Harvest | GUS CPI is not in `indicators.md` (no primary dataset). The corpus has no economist previews of October CPI on 23.09–09.10. The search "inflacja październik" finds only Glapiński on 08.10 (TVN24) |
| Facts | G3-039 (September flash 4.0%, +0.7% m/m, A/1), G2-026/027 (CPN III caps; pump prices −1.36 to −1.40 PLN/l, B/2, A), G3-040 (MPC names "regulatory decisions on energy prices" as a risk). A-only (Polish sources) |
| Analysis | Not covered by a KA or indicator. The question came from G2 candidates |
| Lenses | **A** 0.68 and **C** 0.60 both cite **Glapiński's expectation** (A-02, C-02) that inflation returns to the band in October. **B** 0.65: mechanics only, fuel weight × cut → "about 3.0–3.4%", **no error band**. All three named the band edge as a risk. C was closest |
| Red team | Consistency check against Q-0016 only (OK) |
| Aggregation | AGG = AGG_RT |
| Resolution | Clean, high confidence. The threshold "< 3.5; 3.5 = NO" was explicit in the criterion |

- **Signal lost at:** Lenses.
- **Cause:**
  - Primary: **base rate**. A point estimate was given with no error distribution. The fuel effect was modelled; the non-fuel momentum (+0.7% m/m in September) was not. A central estimate near 3.3% with a normal flash-forecast error of 0.2–0.3 pp lies close to an even chance against a threshold of 3.5.
  - Secondary: **source bias**. The central bank governor's expectation, a fact about a statement, became a shared anchor in two lenses.
  - The outcome landing exactly on the threshold adds a **noise** component.
- **Counterfactual:** for data-threshold questions, the lens states a central estimate and an error band taken from the history of the series, then reads p from that band. Questions should avoid thresholds that sit on a reported rounding point, or should state how ties are handled (this one did).
  - Effect on hits: none. Q-0074 (Brent, a partial hit) sits close to the spot level, where a band gives a similar value.

### M6 · Q-0009 TTF front-month above 90 EUR/MWh on any day by 31.12 (EU_ENERGY / ENE)

0.33 / 0.45 / 0.33 → 0.37 → 0.37; SQ 0.10. **YES** on 22.10 (90.04; peak 103.94 on 30.10).
Edition 01 had AGG_RT 0.30. The forecast moved toward the outcome, but not far enough.

| Step | Finding |
|---|---|
| Harvest | TTF and AGSI+ are **not in the harvested datasets**: no AGSI+ key, and ICE Endex returned 403 (`indicators.md`, `sources_health.md`). Prices were read from a vendor (Investing.com) |
| Facts | G2-014 (TTF closes, C/2, with a vendor data-quality note), G2-016 (storage 72.83%, lowest since 2011, injection +0.22 pp/day, C/2), G2-020 (JKM premium, C/3, TASS analysis, T), G2-021 (Qatar force majeure, B/3). The fundamentals were all recorded |
| Analysis | KA6 "fragile for DE". D projects storage "high 70s" by 01.11; this failed at 74.6% (L1 §4.1 #17). I7 threshold > 90 → CRIS |
| Lenses | **B** 0.45, the closest: a random walk with σ 55% gives a touch probability of about 0.65, which B then **adjusted down for "mean reversion"** because the September peak of 84 "did not break 90". That is one observation. **A** 0.33: "the lens adds the political trigger", a post-election Gulf escalation. **C** 0.33: needs "a cold spell". Neither A nor C used a volatility anchor |
| Red team | Scenario check: "CRIS elements carry roughly one-in-three weights". No adjustment |
| Aggregation | AGG = AGG_RT. Spread 0.12 |
| Resolution | Clean on the outcome, high confidence. ICE settlement not reached; vendor closes used |
| Hindsight | TTF reached 88 on 19.10 and passed 90 on 22.10, **before** any US strike (02.11), and fell after the strike (ed.03 G2-011). Storage peaked at 74.96% and the injection rate fell (ed.03 G2-012). Fundamentals drove the move, not the political trigger |

- **Signal lost at:** Lenses.
- **Cause:**
  - Primary: **base rate**. The quantitative anchor B had computed was overridden without evidence, and A and C had no anchor at all.
  - Secondary: **reaction**. The lenses under-reacted to a trend: storage was at a record low, with the injection rate already below the projection.
- **Counterfactual:** for price-touch questions, the volatility touch probability is the starting point, and any adjustment needs a cited mechanism. The shadow run QNT (framework 1.9) computes exactly this. Its value should be judged on these questions at the quarterly review.
  - Effect on hits: none.

### M7 · Q-0084 TTF front-month above 80.00 EUR/MWh on 20.10 (EU_ENERGY / ENE)

0.36 / 0.50 / 0.45 → 0.437 → 0.437; SQ 0.10. **YES**: Investing.com close of 85.06 on 20.10. Auto-verified.

| Step | Finding |
|---|---|
| Harvest, Facts | As M6. Vendor series differed by 2–5% on the same day: 79.74 vs 77.375 vs 80.20 on 08.10 (red team point 9) |
| Analysis | KA1 (no Gulf escalation before 03.11); I7 |
| Lenses | **B** 0.50, the closest: random walk with z ≈ 0.03. **A** 0.36: "Trump's pre-election no-strike pledge lowers the Gulf premium until 20.10", which is KA1. **C** 0.45: injection slows, Asian competition |
| Red team | Point 3 put Q-0084 in the KA1 correlated bet. Point 9 flagged a resolution risk over which vendor series to use. No adjustment |
| Aggregation | AGG = AGG_RT. Spread 0.14, the widest among the misses |
| Resolution | Medium confidence. ICE not reached; Investing.com fallback. Confirmed by stage V. The 85.06 close is far above the threshold, so the vendor choice does not matter |

- **Signal lost at:** Lenses (A).
- **Cause:**
  - Primary: **noise**. The threshold sat at the spot level with 8 sessions left, a coin flip. Even 0.50 would have scored 0.25.
  - Secondary: **correlation**. KA1 was carried into a gas-price question where the actual driver was storage.
- **Counterfactual:** the same as M6. With A at B's anchor, AGG would have been about 0.48, a gain of about 0.04 Brier.
  - Effect on hits: none.

### M8 · Q-0076 FAO Food Price Index for October above 136.0 (FOOD / ECO)

0.55 / 0.58 / 0.55 → 0.56 → 0.56; SQ 0.10. **NO**: 133.9, −1.2% m/m (FAO, 06.11).

| Step | Finding |
|---|---|
| Harvest | FFPI is not a harvested dataset. The "Food and fertilisers" concept had 36 items (`coverage.md`) |
| Facts | G2-036 (FFPI September, A/1, T), G2-038 (record Russian wheat exports, B/2, A-RU), G2-039 (ICC "+80%" warning, C/3, a TASS relay) |
| Analysis | No KA or indicator |
| Lenses | **B** 0.58: monthly sign about 50/50 with positive autocorrelation. **A** 0.55 and **C** 0.55: narrative tilt from Black Sea and Hormuz input costs. A and C were closest. All three cited G2-038 (supply up) only as a cap |
| Red team, Aggregation | None |
| Resolution | Clean, high confidence |

- **Signal lost at:** Lenses (small tilt).
- **Cause:**
  - Primary: **noise**. The question was close to a coin flip, and every lens stayed within 0.08 of 0.5.
  - Secondary: **reaction**. The headline disruption narrative was weighted over a supply fact already in the records.
- **Counterfactual:** the M5 rule (state the central estimate and error band). Here it would give about 0.5. Gain about 0.06 Brier.
  - Effect on hits: none.

### M9 · Q-0094 Likud wins the most Knesset seats on 27.10 (IL_ELECTIONS / DOM)

0.45 / 0.47 / 0.48 → 0.467 → 0.467; SQ 0.50. **YES**: Likud 27, Yashar 21. Auto-verified.

| Step | Finding |
|---|---|
| Harvest | **Weak.** Israel had 173 items from 2 independent feeds, with no official, no state-loyal and no Western feed (`coverage.md`). No digest line mentions Likud or Eisenkot. Every poll came through web search |
| Facts | G4-034: the five-poll average gave Likud 23 vs Yashar 22.2. Channel 12 (05.10) had Yashar 23 vs Likud 21, from an aggregator summary that was not opened. Single perspective |
| Analysis | Israel was left "unresolved" (red team point 4). No KA or indicator on the election |
| Lenses | **A** 0.45 and **B** 0.47 weighted the **non-Channel-14 subset**, where Yashar was level or ahead. B noted that "Likud has historically matched or slightly beaten its polls" but did not move above 0.5. **C** 0.48 was closest. Tie = NO and the postponement path were priced in |
| Red team | Point 4 flagged postponement risk toward **NO**, which was the wrong direction. Single headline; no adjustment |
| Aggregation | AGG = AGG_RT |
| Resolution | Clean, high confidence. Random-sample check; confirmed by stage V |

- **Signal lost at:** Lenses. Secondary: Harvest (coverage).
- **Cause:**
  - Primary: **base rate**. Two reference classes went unused: the largest-list record (Likud first in 5 of the 7 elections from 2013 to 2022, by our count from election results; April 2019 was a tie) and B's own note on how Likud's results compare with its polls.
  - Secondary: **source bias**. A subset of pollsters was preferred over the full average, which had Likud ahead.
- **Counterfactual:** for "largest party" questions, start from the full poll average and the party's record of being the largest list, then adjust. This would have put the forecast slightly above 0.5.
  - Effect on hits: none.

### M10 · Q-0099 USNI shows at least 3 US carriers in the CENTCOM area by 30.11 (IRAN_WAR / MIL)

0.45 / 0.45 / 0.50 → 0.467 → 0.467; SQ 0.10. **YES** on 16.11: Washington, Bush and Roosevelt all in the Arabian Sea.

| Step | Finding |
|---|---|
| Harvest | Collected well: USNI, The War Zone, gCaptain and Maritime Executive (W); Anadolu (T); CGTN (A-CN). The corpus on 04–05.10 said that Bush had made a port call in Phuket "after six-month Middle East deployment" (gCaptain, Anadolu). **The decisive fact, that the Navy sent Bush back to the Middle East on 15.10, was not collectable on 09.10** (corpus item 15.10) |
| Facts | G1-009: three carriers by end-XI, **DECL**, with the Roosevelt departure **DONE** (B/2). G1-057: Bush "in Phuket port call", **B/3, page not opened (USNI 403)** |
| Analysis | Indicator I3a: three carriers simultaneously → CRIS. KA1 placed the use of the build-up after 03.11 |
| Lenses | **A** 0.45: "Bush has left the area". **C** 0.50, the closest: "Bush is leaving". Both read the port call as the end of the deployment. **B** 0.45: "announced US carrier end-states are usually reached, but with slips of weeks". B stated that its own reference class leans YES and then went below 0.5 |
| Red team | KA1 correlated bet (point 3). No adjustment |
| Aggregation | AGG = AGG_RT |
| Resolution | Medium confidence. USNI 403; read from search excerpts. No dispute |

- **Signal lost at:** not collectable (the main part). Secondary: Lenses.
- **Cause:**
  - Primary: **information not collectable**. The Bush redeployment happened on 15.10.
  - Secondary: **actor model**. A declared and already resourced US end-state was discounted on an inference drawn from a port call.
- **Counterfactual:** separate a declaration that is backed by executed steps (DECL + DONE) from a bare declaration. Read a port call as a pause, not a departure, unless a source says so. This would have put the forecast slightly above 0.5.
  - Effect on hits: none. Q-0039 and Q-0083 are the same kind of resourced declaration, and the rule would reinforce them.

---

## 2. Traces — hits

### H1 · Q-0039 Panama Canal daily transit limit above 32 by 31.10 (PANAMA / INF)

0.92 / 0.92 / 0.92 → 0.92; SQ 0.10. **YES** on 15.10. Edition 01 had 0.147.

- **Found at:** Facts. Stage 01 read the ACP advisory of 28.09 (33 slots from 15.10), which became G1-061 (B/2, A-PA).
- **Lenses:** identical values, a **shared anchor** that was correct here. No ACH or KA was needed.
- **Resolution:** medium confidence. The ACP advisory was read; nothing confirmed after it took effect.
- **Cause of the hit:** information collected from a primary source. The official decision already existed; the forecast only had to assume it would take effect.
- **Skill content:** low. The SQ of 0.10 was fixed on 23.09, before the advisory. The edition 01 miss happened because the advisory did not yet exist.

### H2 · Q-0083 EU lists at least 1,500 new persons and entities by 21.10 (RU_SANCTIONS_EU / FIN)

0.90 / 0.92 / 0.88 → 0.90; SQ 0.10. **YES** on 12.10 (1,569 + 77).

- **Found at:** Facts and Lenses.
  - G3-022: Coreper agreement on 07.10, four outlets across W, A and exile.
  - B's reference class: acts agreed in Coreper are almost always adopted at the announced Council meeting.
- **Red team:** called the value "consistent". It noted that SQ = 0.10 understates the status quo for formalisation questions (§bias).
- **Cause of the hit:** a procedural follow-through base rate applied to a decision that had already been taken.

### H3 · Q-0031 Republicans win at least 218 House seats (US_ELECTIONS / DOM)

0.12 / 0.08 / 0.12 → 0.107; SQ 0.90. **NO** on 04.11 (D 254 by the AP count of 09.11).

- **Found at:** Lenses.
  - B's reference class: the president's party lost the House in 1994, 2006, 2010 and 2018 under comparable conditions.
  - Polls: approval 32% (B/2) and a generic ballot of D+7 (C/3, possibly a repeat).
- **Red team:** the edition 01 adjustment of −0.05 already applied this reference class. Edition 02 kept it.
- **Cause of the hit:** a strong, relevant base rate and a margin far above the polling error.

### H4 · Q-0102 BIS extends or rescinds the Affiliates rule suspension by 09.11 (US_CHINA_TECH / TEC)

0.78 / 0.72 / 0.75 → 0.75; SQ 0.10. **YES** on 09.11 (FR 2026-22793).

- **Found at:** Analysis. KA3 and indicator I9 named "US FR notices on 09–10.11" as the explicit test. G3-010 is the MOFCOM readout of the extension to 10.01.2027 (A-CN).
- **B's reference class:** US Federal Register texts appear at or just before the expiry date.
- **Cause of the hit:** a procedural follow-through base rate, plus an indicator that pointed exactly at the test date.
- **Residual risk the lenses named:** late publication (on 10.11) would resolve NO. The text appeared on the last eligible day.

### H5 · Q-0021 PRC extends or repeals the rare-earth control suspension by 10.11 (CN_RARE_EARTHS / TEC)

0.72 / 0.75 / 0.75 → 0.74; SQ 0.10. **YES** on 09.11 (Announcement No. 58).

- **Found at:** Facts and Analysis.
  - G3-010 (the MOFCOM extension "including related Chinese export controls") and G2-041 (the 2025 precedent: a text three days before expiry).
  - I17 flagged that "the extension of the truce does not settle it" legally, which L1 judged correct.
- **Lenses:** C cited the 2025 timing; B gave a reference class of about 0.8.
- **Cause of the hit:** procedural follow-through, plus a precedent read from a primary text.

---

## 3. Synthesis

### 3.1 Table

| # | Question | Cluster / vector | Step lost (miss) / found (hit) | Primary cause | Secondary cause | Counterfactual (smallest change) | Hurts a hit? |
|---|---|---|---|---|---|---|---|
| M1 | Q-0026 | UA_TALKS / DIP | Lenses (+ red team) | source bias | collected not used | corpus delta read to forecast date; base rate of reversed refusals | no |
| M2 | Q-0033 | BRAZIL_ELECTIONS / DOM | not lost (not collectable) | noise | reaction | confidence cap when margin < recent polling error | no |
| M3 | Q-0105 | PL_FINANCE / FIN | Lenses (+ digest) | base rate | collected not used | conditional reference class (last agency after peers) | no |
| M4 | Q-0065 | IRAN_WAR / MIL | Lenses | base rate (criterion mismatch) | correlation (KA1) | write out the smallest resolving event | no |
| M5 | Q-0075 | PL_INFLATION / ECO | Lenses | base rate (no error band) | source bias (governor) | central estimate plus error band | no |
| M6 | Q-0009 | EU_ENERGY / ENE | Lenses | base rate (anchor overridden) | reaction (trend) | volatility touch anchor; adjustments need a cited mechanism (QNT) | no |
| M7 | Q-0084 | EU_ENERGY / ENE | Lenses (A) | noise | correlation (KA1) | as M6 | no |
| M8 | Q-0076 | FOOD / ECO | Lenses | noise | reaction | as M5 | no |
| M9 | Q-0094 | IL_ELECTIONS / DOM | Lenses (+ coverage) | base rate | source bias (poll subset) | full average plus largest-list record | no |
| M10 | Q-0099 | IRAN_WAR / MIL | not collectable | not collectable | actor model | DECL + DONE vs DECL; port call ≠ departure | no |
| H1 | Q-0039 | PANAMA / INF | Facts (primary source) | primary source read | — | — | — |
| H2 | Q-0083 | RU_SANCTIONS_EU / FIN | Facts + Lenses (B) | follow-through base rate | — | — | — |
| H3 | Q-0031 | US_ELECTIONS / DOM | Lenses (B) | strong reference class | — | — | — |
| H4 | Q-0102 | US_CHINA_TECH / TEC | Analysis (KA3, I9) | follow-through base rate | — | — | — |
| H5 | Q-0021 | CN_RARE_EARTHS / TEC | Facts + Analysis (I17) | follow-through base rate plus precedent | — | — | — |

### 3.2 Cause frequencies (10 misses)

| Cause | Primary | Secondary | Total | Vectors (clusters) |
|---|---|---|---|---|
| base rate | 5 (M3, M4, M5, M6, M9) | 0 | 5 | FIN, MIL, ECO, ENE, DOM (5 clusters) |
| noise | 3 (M2, M7, M8) | 0 | 3 | DOM, ENE, ECO |
| source bias | 1 (M1) | 2 (M5, M9) | 3 | DIP, ECO, DOM |
| information not collectable | 1 (M10) | 0 | 1 | MIL |
| information collected but not used | 0 | 2 (M1, M3) | 2 | DIP, FIN |
| reaction | 0 | 3 (M2, M6, M8) | 3 | DOM, ENE, ECO |
| correlation | 0 | 2 (M4, M7) | 2 | MIL, ENE (both through KA1) |
| actor model | 0 | 1 (M10) | 1 | MIL |
| timing, question design | 0 | 0 | 0 | — (two resolutions were ambiguous, M3 and M4, but neither caused the miss) |

**Where the signal was lost:**
- Lenses: 8 of 10 (M1, M3–M9).
- Not collectable on 09.10: 2 (M2, M10).
- The red team made no adjustment on any of the 10 misses. It flagged three of them (M4, M7, M10) as one KA1-correlated bet, and it flagged M9 in the wrong direction.
- None was lost at aggregation. AGG = AGG_RT for all 15 questions, and no adjustment was rejected.

**By lens.** In every case the three lenses were within 0.14 of each other, so "closest lens" differences are small.
- C was closest outright on 5 misses: M2, M4, M5, M9, M10.
- B was closest on 2: M6, M7.
- A was closest on 1: M3.
- There were ties on M1 (A and B) and M8 (A and C).
- **B's reference class was right but over-ridden** on M6 (touch about 0.65, reduced to 0.45) and M10 (its stated class leaned YES, yet it gave 0.45). **B chose a generic class** on M3 and M9.

All of this is indicative only (N = 10).

### 3.3 Patterns (at least 3 questions from at least 2 clusters)

1. **Reference class missing, generic, or overridden without evidence: 5 misses in 5 clusters and 5 vectors (M3, M4, M5, M6, M9). This is a pattern.** Two sub-types, each meeting the threshold:
   - **(a) Data and price thresholds with no error distribution:** M5, M6, M7, M8, which are 4 questions in 3 clusters (PL_INFLATION, EU_ENERGY, FOOD). The lenses argued from narrative tilts or point mechanics. Where B did compute a volatility anchor, the forecast was better (M6, M7), but B adjusted away from it without a cited mechanism. None of the four series (TTF, AGSI+, GUS CPI, FAO FFPI) is a harvested primary dataset (`indicators.md`), so the lenses had no series to compute from. This fits L2 finding 4 (compression in the 0.10–0.50 range) and L2 §4 (ECO over-forecast YES). The framework 1.9 shadow run QNT is the existing test of this counterfactual.
   - **(b) Political events forecast against the wrong event class:** M3 (rating, conditional on peers), M4 (the smallest strike vs a campaign) and M9 (largest list), which are 3 questions in 3 clusters. In each case the event the lenses priced was harder to reach than the event the criterion requires.
2. **One actor's statement of present intent used as a forecast of later behaviour, with no base rate for how often such statements hold: 4 misses in 3 clusters (M1 Ryabkov; M4 Trump's pre-election pledge via KA1; M5 Glapiński; M10 the declared end-state, discounted). This is a pattern.** The direction is not consistent: statements that supported the status quo were over-weighted (M1, M4 before 03.11), and declared changes were under-weighted (M10, M4 after 03.11). The common failure is the missing base rate, not one direction. **Contrast with the hits:** 4 of 5 (H1, H2, H4, H5) are formal follow-through of a decision already taken, where the lenses did apply a follow-through base rate. The pipeline has base rates for procedures but none for political statements. This matches L1 lesson 2.
3. **Shared assumption KA1 carried through a flagged correlated bet: 3 misses in 2 clusters (M4, M10 IRAN_WAR; M7 EU_ENERGY).** This meets the count but rests on **one assumption** in one edition, and the red team flagged it without being able to act. Read it as one event, not a general rule.

**Anecdotes** (below the threshold, recorded for L4 and L5):
- **Collected but not used:** M1 (Axios item in the corpus before the forecasts) and M3 (Polish rule-of-law precursors). Two questions in two clusters. Within L3 this is an anecdote, but it matches L1 lesson 1 (4 of 10 surprises), so the combined evidence is stronger.
- **Polling error assumed to keep its direction:** M2 and M9 (2 questions).
- **Thin single-perspective coverage of a country with a scored question:** Israel (M9), and Polish public finance with no W source (M3).

**Overfitting check.** Pattern 1 spans five vectors. Pattern 2 spans three clusters, but two of its four cases are IRAN_WAR. Pattern 3 is a single assumption. No cluster contributes more than two misses: EU_ENERGY and IRAN_WAR have two each.

### 3.4 What the counterfactuals would have done (indicative, not a rescoring)

- If every lens had applied the counterfactuals, five misses would have moved toward the outcome by roughly 0.05–0.20 each: M1, M3, M4, M6 and M9.
- Three would have moved to about 0.5: M5, M7 and M8.
- Two not-collectable or noise cases (M2, M10) would have moved little.
- None of the counterfactuals lowers a hit: they leave the hits unchanged or reinforce them.
- These are judgements, not recomputed forecasts. No forecast or registry row was changed (learning rule 4).

---

## 4. Process notes

- Provenance: `python3 tools/pipeline.py stage-start L3 --arg latest --model "claude-opus-5-5"` (19.11.2026, commit be65911) … `stage-end L3 --arg latest`.
- Read:
  - L1 and L2 of this folder.
  - The edition 02 files listed under "Method".
  - Edition 03 `01_resolutions.md` and `02_facts/G1, G2, G4.md`, used for hindsight only.
  - `registry/forecasts.csv` (edition 01 and 02 rows of the selected questions) and `registry/questions.csv`.
- Corpus searches (`python3 -m tools.harvester search`): trilateral; Witkoff; Lula; Datafolha runoff (10–25.10); Quaest; Likud; S&P / rating / Moody's; inflacja; George H.W. Bush; carrier strike group.
- Web: one search, on S&P's 06.11 rationale (Notes from Poland; kurs.com.ua). No forecasting service or market was visited or searched.
- Blindness: no benchmark, crowd or `07_annex_benchmarks.md` value is used.
- Gaps:
  - The S&P release itself was not read (spglobal.com). The FC/LC scope of the outlook change is still open, as recorded in stage 01.
  - The Israeli largest-list record (5 of 7, 2013–2022) is our count from election results and was not checked against a source in this run.
  - No harvested series exists for TTF, AGSI+, GUS CPI or FAO FFPI, so the "error band" counterfactuals were not computed.
  - Hindsight on the Brazil polls rests on corpus headlines (G1 Globo, 24.10).
- No instruction-like content was found in harvested items or search results.

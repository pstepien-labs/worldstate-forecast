# Stage 05 — Red team (edition 01, state 23.09.2026)

Input: `03_analysis.md`, `04_forecasts_A.md`, `04_forecasts_B.md`, `04_forecasts_C.md`, `02_facts/G1–G4.md`, `registry/questions.csv`, `registry/forecasts.csv` (runs A, B, C). No `06_*` files, `07_annex_benchmarks.md`, `registry/benchmarks.csv` or forecasting services were opened. Searches: 4 + 1 fetch (fact verification, with the domains from CLAUDE.md item 9 blocked; UKMTO — HTTP 403).
Role: refute, not confirm. Adjustments only with specific evidence or a logical error, limit ±0.15 per question (methodology §5).
Convention: AGG = mean of A, B, C (3 decimal places); AGG_RT = AGG + adjustment, rounded to 0.01. Without an adjustment AGG_RT = AGG (stage 06).
Labels from 03_analysis: KA# — key assumptions (§1.3), I# — indicators (§1.5), H# — hypotheses (§1.4); scenarios BASE / FAV / CRIS.

---

## 1. Ten weakest points of the analysis

| # | Weak point | Type | Evidence or argument | Questions affected |
|---|---|---|---|---|
| 1 | **One mechanism explains too much: the "electoral brake of 03.11".** Assumption KA1 and lenses A and C use it to explain approx. 10 questions at once (C itself lists 7). The mirror test in 03 (§1.6 item 6) pointed to the opposite logic (a quick operation mobilises voters), but no lens considered it. Basis: a run of 15 periods without strikes (G1-005, source C/3) and an Interia report of an agreement "after the elections" (G4-055, second-hand account). | assumption without evidence; mirror | An error in this assumption will shift all the questions at once — risk of correlated error in the IRAN_WAR, HORMUZ, OIL_PRICE, BAB_EL_MANDAB clusters. I do not adjust (no counter-evidence), but the outcomes of these questions should be read as one bet. | Q-0007, Q-0012, Q-0028, Q-0038, Q-0041, Q-0065, Q-0068 |
| 2 | **Omitted actor: Israel.** The analysis of the war with Iran (A, B, ACH-1, I1–I5) does not mention Israel as a party able to strike on its own or to break the US–Iran track; in 02 it appears only in the context of Lebanon and Gaza (G1-063, G4-014). Pezeshkian at the UN on 23.09 speaks directly about Israel (A's additional facts). | omitted actor | An Israeli strike does not resolve Q-0041/Q-0065 (USA only), but may break the talks and push oil up — ACH-1 has a gap on the H3 side. | Q-0007, Q-0028, Q-0038, Q-0042, Q-0063 |
| 3 | **Hormuz: both measurement series come from parties to the dispute or from aggregators.** CENTCOM/UKMTO (G2-006) is a party to the conflict marked as perspective W; PortWatch comes via the Straits Daily Brief aggregator (G1-001, C/2), not directly from the IMF. No independent T perspective. Questions Q-0036 and Q-0037 are resolved by PortWatch (AIS), so they measure "open" traffic, not scenario H4. | one-sided sources | The lenses correctly keep Q-0036/Q-0037 low; I do not adjust. Risk: Q-0037 = NO even under H4. | Q-0036, Q-0037 |
| 4 | **Lack of data treated as absence of events.** 03 §1.7 item 10 records a gap: "no data on Houthi attacks on merchant ships in IX". All three lenses lower Q-0062 precisely for this reason (A: "the absence of data… suggests"; B: "adj. down — no incidents found"; C: "no data"). A collection gap is not evidence of calm. Likewise Q-0047 (no Taiwan MND reports for 15–23.09). | overreaction to the absence of headlines | Adjustment to Q-0062 (table §3). Q-0047 — no adjustment (p_status_quo 0.50 already reflects this). | Q-0062, Q-0047 |
| 5 | **US posture review: the congressional "brake" overrated.** Lenses A and C treat §1249 NDAA as a block. G1-031 says otherwise: §1249 prohibits a reduction below 76k for more than 45 days *without certification* by the Secretary of Defense and the EUCOM commander, and according to an analysis (grosswald.org) the threshold may not apply from 01.10 until the NDAA FY2027 is passed (C-10: draft §1232 — also a threshold with certification). It is a procedure, not a ban. Moreover, ACH-3 in 03 identifies H1 and H2 as the least refuted — both hypotheses assume a reduction; H3 (status quo) is weakened by the numerical options and the precedent of V 2026. | assumption without evidence; consistency with the scenario | Adjustment to Q-0003 (§3). | Q-0003, Q-0044 |
| 6 | **US base in Poland: Polish and presidential sources only.** Trump, Nawrocki and the Polish MoD (G1-025…027); no Pentagon details and no troop numbers (03 §1.7 item 4). This is the source of the "opposite" signal in I13 — it is not confirmed. | one-sided sources | Q-0044 (0.20) needs no adjustment; I13 should not offset the reduction in Europe without a number of soldiers. | Q-0044, Q-0003 |
| 7 | **Ukrainian front: divergent pace series, and the lenses chose one.** G1-044 gives three values: DeepState approx. 150 km²/4 weeks, The Economist approx. 78 km²/30 days (15.09) and approx. 200 km² (08.09). A and B use a pace of "36–150 km²/month", omitting the approx. 200 km² reading. C's rationale ("rasputitsa… requires acceleration") points to NO, and yet C gives the highest p (0.35) — an internal inconsistency of the lens. The two errors work in opposite directions. | single-series source; inconsistency | No adjustment to Q-0004 (the errors cancel out, AGG 0.227 lies between B's base rate and the 200 km² reading). | Q-0004, Q-0073 |
| 8 | **An out-of-date fact in lens A: Hungary as a sanctions blocker.** A (Q-0019): "France, Slovakia and Hungary extract concessions". C-13 (RFE/RL 08.09): after the change of government in Hungary (V 2026) Slovakia took over the blocking role. 03 does not record this change. | out-of-date assumption | Direction of impact ambiguous (fewer blockers, but Slovakia managed to delay the 18th package by approx. 5 weeks). No adjustment. | Q-0019, Q-0071 |
| 9 | **Gas storage: an arithmetic error in C-12 (lens C).** C: "reaching 80% on 01.11 requires approx. 5.5 TWh/d against approx. 2.8 TWh/d". From G2-017: 9.7 pp × approx. 1130 TWh ≈ 110 TWh are missing over 40 days ≈ 2.7 TWh/d — that is, as much as current injection (2790 GWh/d). 5.4 TWh/d is, according to G2-017, the requirement for the **90%** target. The 80% threshold is achievable if the pace does not fall; the 78.2% projection (G2-018) assumes a fall. | data error | C = 0.30 relied partly on the error, but A (0.30) reached the same value by a different route, and B (0.45) has a correct extrapolation. AGG 0.35 remains within a reasonable range of 0.30–0.45 — no adjustment. | Q-0067, Q-0049, Q-0010 |
| 10 | **Overinterpretation of single observations as signals of intent.** (a) Magnet exports −21% m/m in VIII as a "signal before the summit" (03 §A, low confidence as to intent) — lenses A and C build Q-0025 on this; B rightly points to mean reversion (I–VIII +23% y/y). (b) "Second round on 23.09" — The National says only "probably", A uses it in Q-0006 as a fact. (c) The offer to open Hormuz "within 7 days" (G1-007) — disputed, denied by the IRGC. | overreaction to headlines | No adjustments: the effect on AGG is small, and B offsets A and C in Q-0025. | Q-0025, Q-0006, Q-0037 |

Additional notes (below the threshold of ten):
- **Blindness exposure of lens B** (log 04-B): B saw A's rows for Q-0001 and Q-0002 and gave exactly the same values (0.03, 0.05). For Q-0001 B's downward adjustment (0.06 → 0.03) has its own rationale (contract recruitment). For Q-0002 B's adjustment (0.07 → 0.05) on account of "no event despite many incidents" counts the same evidence twice — Laplace's rule (0 events in 43 months) already contains it. Adjustment +0.01 in §3.
- **Lens C, Q-0031:** the rationale ("the Democrats are approx. 3–5 seats short", Trump's approval at 39%) points to a p lower than 0.20. Adjustment in §3.
- **Lens A, Q-0039:** "the lens says nothing here", and yet p = 0.35, the highest of all three — without support in hydrological data.
- 03 §1.6 B rightly lists the parties' wartime figures (Russian MoD, Ukrainian General Staff, Houthis) as uncertain. The lenses comply (e.g. > 45% of refinery capacity only as "per the Ukrainian General Staff").

---

## 2. Forecast review

### 2.1 AGG for all questions

| ID | A | B | C | AGG | spread | ID | A | B | C | AGG | spread |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | 0.03 | 0.03 | 0.03 | 0.030 | 0.00 | Q-0038 | 0.32 | 0.22 | 0.30 | 0.280 | 0.10 |
| Q-0002 | 0.05 | 0.05 | 0.05 | 0.050 | 0.00 | Q-0039 | 0.35 | 0.10 | 0.20 | 0.217 | 0.25 |
| Q-0003 | 0.35 | 0.35 | 0.30 | 0.333 | 0.05 | Q-0040 | 0.40 | 0.75 | 0.55 | 0.567 | **0.35** |
| Q-0004 | 0.18 | 0.15 | 0.35 | 0.227 | 0.20 | Q-0041 | 0.05 | 0.08 | 0.05 | 0.060 | 0.03 |
| Q-0005 | 0.25 | 0.35 | 0.40 | 0.333 | 0.15 | Q-0042 | 0.55 | 0.45 | 0.45 | 0.483 | 0.10 |
| Q-0006 | 0.35 | 0.45 | 0.40 | 0.400 | 0.10 | Q-0043 | 0.40 | 0.35 | 0.35 | 0.367 | 0.05 |
| Q-0007 | 0.12 | 0.25 | 0.20 | 0.190 | 0.13 | Q-0044 | 0.20 | 0.20 | 0.20 | 0.200 | 0.00 |
| Q-0008 | 0.15 | 0.30 | 0.15 | 0.200 | 0.15 | Q-0045 | 0.25 | 0.15 | 0.15 | 0.183 | 0.10 |
| Q-0009 | 0.25 | 0.35 | 0.30 | 0.300 | 0.10 | Q-0046 | 0.50 | 0.45 | 0.40 | 0.450 | 0.10 |
| Q-0010 | 0.40 | 0.25 | 0.40 | 0.350 | 0.15 | Q-0047 | 0.40 | 0.40 | 0.55 | 0.450 | 0.15 |
| Q-0011 | 0.72 | 0.75 | 0.78 | 0.750 | 0.06 | Q-0048 | 0.35 | 0.37 | 0.40 | 0.373 | 0.05 |
| Q-0012 | 0.20 | 0.15 | 0.22 | 0.190 | 0.07 | Q-0049 | 0.70 | 0.60 | 0.55 | 0.617 | 0.15 |
| Q-0013 | 0.80 | 0.85 | 0.88 | 0.843 | 0.08 | Q-0050 | 0.30 | 0.35 | 0.35 | 0.333 | 0.05 |
| Q-0014 | 0.55 | 0.55 | 0.58 | 0.560 | 0.03 | Q-0051 | 0.30 | 0.30 | 0.25 | 0.283 | 0.05 |
| Q-0015 | 0.12 | 0.12 | 0.08 | 0.107 | 0.04 | Q-0052 | 0.45 | 0.47 | 0.45 | 0.457 | 0.02 |
| Q-0016 | 0.15 | 0.10 | 0.30 | 0.183 | 0.20 | Q-0053 | 0.50 | 0.45 | 0.52 | 0.490 | 0.07 |
| Q-0017 | 0.45 | 0.45 | 0.40 | 0.433 | 0.05 | Q-0054 | 0.85 | 0.68 | 0.93 | 0.820 | 0.25 |
| Q-0018 | 0.10 | 0.08 | 0.08 | 0.087 | 0.02 | Q-0055 | 0.75 | 0.88 | 0.82 | 0.817 | 0.13 |
| Q-0019 | 0.55 | 0.50 | 0.40 | 0.483 | 0.15 | Q-0056 | 0.08 | 0.04 | 0.07 | 0.063 | 0.04 |
| Q-0020 | 0.30 | 0.25 | 0.20 | 0.250 | 0.10 | Q-0057 | 0.12 | 0.12 | 0.15 | 0.130 | 0.03 |
| Q-0021 | 0.63 | 0.70 | 0.72 | 0.683 | 0.09 | Q-0058 | 0.45 | 0.45 | 0.45 | 0.450 | 0.00 |
| Q-0022 | 0.60 | 0.72 | 0.72 | 0.680 | 0.12 | Q-0059 | 0.15 | 0.10 | 0.10 | 0.117 | 0.05 |
| Q-0023 | 0.35 | 0.50 | 0.45 | 0.433 | 0.15 | Q-0060 | 0.55 | 0.68 | 0.45 | 0.560 | 0.23 |
| Q-0024 | 0.15 | 0.15 | 0.20 | 0.167 | 0.05 | Q-0061 | 0.25 | 0.15 | 0.25 | 0.217 | 0.10 |
| Q-0025 | 0.45 | 0.60 | 0.45 | 0.500 | 0.15 | Q-0062 | 0.45 | 0.45 | 0.40 | 0.433 | 0.05 |
| Q-0026 | 0.45 | 0.45 | 0.45 | 0.450 | 0.00 | Q-0063 | 0.45 | 0.40 | 0.40 | 0.417 | 0.05 |
| Q-0027 | 0.10 | 0.12 | 0.12 | 0.113 | 0.02 | Q-0064 | 0.25 | 0.25 | 0.30 | 0.267 | 0.05 |
| Q-0028 | 0.35 | 0.25 | 0.30 | 0.300 | 0.10 | Q-0065 | 0.25 | 0.28 | 0.25 | 0.260 | 0.03 |
| Q-0029 | 0.50 | 0.60 | 0.50 | 0.533 | 0.10 | Q-0066 | 0.30 | 0.40 | 0.30 | 0.333 | 0.10 |
| Q-0030 | 0.30 | 0.25 | 0.25 | 0.267 | 0.05 | Q-0067 | 0.30 | 0.45 | 0.30 | 0.350 | 0.15 |
| Q-0031 | 0.15 | 0.12 | 0.20 | 0.157 | 0.08 | Q-0068 | 0.25 | 0.25 | 0.20 | 0.233 | 0.05 |
| Q-0032 | 0.15 | 0.12 | 0.15 | 0.140 | 0.03 | Q-0069 | 0.15 | 0.15 | 0.20 | 0.167 | 0.05 |
| Q-0033 | 0.55 | 0.57 | 0.55 | 0.557 | 0.02 | Q-0070 | 0.30 | 0.33 | 0.30 | 0.310 | 0.03 |
| Q-0034 | 0.30 | 0.35 | 0.35 | 0.333 | 0.05 | Q-0071 | 0.20 | 0.12 | 0.20 | 0.173 | 0.08 |
| Q-0035 | 0.08 | 0.10 | 0.10 | 0.093 | 0.02 | Q-0072 | 0.12 | 0.15 | 0.12 | 0.130 | 0.03 |
| Q-0036 | 0.30 | 0.20 | 0.22 | 0.240 | 0.10 | Q-0073 | 0.10 | 0.10 | 0.15 | 0.117 | 0.05 |
| Q-0037 | 0.10 | 0.12 | 0.12 | 0.113 | 0.02 | | | | | | |

Five questions have identical p in all lenses (Q-0001, Q-0002, Q-0026, Q-0044, Q-0058) — possible anchoring on a shared input (03); for Q-0001 and Q-0002 there is additionally the reported exposure of B to A's rows.

### 2.2 AGG inconsistent with the facts in `02_facts` (and facts fetched in stage 04)

| ID | AGG | Inconsistency | Source |
|---|---|---|---|
| Q-0054 | 0.820 | Lenses A and B did not know the reading at 97.64% of protocols (5.13%, C-01; in my verification on 23.09 I did not find this figure — what is confirmed is 5.00% at 96.95%, RIA/Meduza). Meduza 22.09: an election analyst indicates that SR "had approx. 60k votes added" at the last stage — a signal of an administrative decision on SR entering the Duma (fact about a statement, interpretation disputed). Counting trend + political decision → B (0.68, pure extrapolation) is too low. | G4-028; C-01; Meduza 22.09 |
| Q-0013 | 0.843 | The arithmetic of all three lenses gives +0.8–1.0 pp to the m/m index from fuel alone. Base effect: in IX 2025 CPI m/m was 0.0% (GUS, flash estimate and final data), so the y/y change ≈ the m/m change in IX 2026. From 3.4% this gives approx. 4.2–4.4% y/y. For the result to fall below 3.5%, the rest of the basket would have to give approx. −0.7 to −0.9 pp m/m (in IX 2025 food: −0.5% m/m, i.e. approx. −0.13 pp contribution). The lenses do not justify an approx. 16% chance of NO. | G2-022, G3-027, C-06; GUS IX 2025 |
| Q-0050 | 0.333 | A and B relied on 8.89 PLN/l (16.09); the e-petrol quotation of 23.09 is 8.99 PLN/l (C-04), 1 grosz below the threshold. Direction over 2 weeks: Orlen's wholesale cut on 23.09 and six sessions of falling Brent work downwards. | G2-024; C-04 |
| Q-0039 | 0.217 | A (0.35) gives no data. B has them: the ACP reduces draught from 01.10 (tightening, not easing), rainfall V–VIII −34%, El Niño until 2027; in the 2023–24 drought the limit was tightened until XI and eased only in 2024. | G1-058; B's facts (DTN, Maritime Executive) |
| Q-0062 | 0.433 | The lenses treated the lack of data for IX (a gap) as absence of events. The criterion includes boarding in the Gulf of Aden, and according to B (VII–VIII: 05.07 Hodeidah, VIII "Amzan", 20.08 boarding of Seamull 136 nm from Al-Mukalla) the pace is 2–3 events/month → 14 days ≈ 0.6–0.7 at a constant pace. After the end of the south-west monsoon (IX) Somali piracy seasonally increases (ASSESSMENT, confidence: medium). Verification on 23.09: no UKMTO notices from IX found (UKMTO site — HTTP 403), so the gap remains open. | G1-023, §1.7 item 10 in 03; B's facts |

### 2.3 Logical inconsistencies between questions

Relations checked:

| Relation | AGG values | Result |
|---|---|---|
| Q-0058 (by 07.10) ≤ Q-0011 (by 10.11) — the same event, shorter deadline | 0.450 ≤ 0.750 | consistent |
| Q-0041 (2 weeks) ≤ Q-0065 (by 31.12) | 0.060 ≤ 0.260 | consistent |
| Q-0021 ≤ Q-0011 (extension of the control suspension usually in a package with the truce) | 0.683 ≤ 0.750 → P(Q-0021 \| Q-0011) ≈ 0.9 | consistent; see §5 (ACH-2) |
| Q-0022 ≈ Q-0021 (same package, longer deadline) | 0.680 vs 0.683 | consistent |
| Q-0038 (lifting the blockade) ≤ Q-0028 (agreement) + premium for suspension without an agreement | 0.280 vs 0.300 | consistent |
| Q-0036 (PortWatch > 40) ≤ P(agreement) × P(rebuilding of AIS traffic) + de facto opening | 0.240 vs 0.30 × approx. 0.6 + approx. 0.05 ≈ 0.23 | consistent |
| Q-0008 (Brent < 80) vs Q-0028: a fall < 80 without an agreement is unlikely | 0.200 vs 0.300 | borderline (implies P(< 80 \| agreement) ≈ 0.5–0.6); no adjustment — B's volatility model is justified |
| Q-0007 + Q-0008 (two opposite tails, both possible within 3 months) | 0.19 + 0.20 = 0.39 | consistent |
| Q-0026 (trilateral meeting) ≥ Q-0059 (energy ceasefire, 2 weeks) | 0.450 ≥ 0.117 | consistent |
| Q-0033 (Lula wins) ≥ Q-0056 (Lula > 50% in the first round) | 0.557 ≥ 0.063 | consistent |
| Storage path: Q-0049 (> 73% on 06.10) → Q-0067 (≥ 80% on 01.11) → Q-0010 (< 55% on 01.01) | 0.617 / 0.350 / 0.350 | consistent (path approx. 73.5% → approx. 78–79% → approx. 55–58%) |
| Q-0023 (MOFCOM listing) vs the triggers Q-0069 (DSCA ≥ 1 bn) and Q-0012 (H.R. 5334 tariffs) | 0.433 vs 0.167, 0.190 | consistent (listings may also have other reasons) |
| Q-0013 (CPI ≥ 3.5%) vs Q-0016 (MPC rate change) | 0.843 (after adjustment 0.94) vs 0.183 | tension, not contradiction: CPI of approx. 4.3% is above the target band (2.5 ± 1), but the MPC chair announces stability (G3-027). No adjustment to Q-0016 — C (0.30) has evidence (C-07), A and B have counter-evidence (G3-027). |

No pair of mutually exclusive questions with a sum > 1 and no case of P(A and B) > P(A) was found.

### 2.4 Lens spread > 0.30

Only **Q-0040** (Baltic — cable or pipeline with an investigation by 31.03.2027): A 0.40, B 0.75, C 0.55.
- **B has the better basis.** An explicit reference class: in each of the last three winters at least one such incident with an investigation or detention of a ship (Balticconnector X 2023; Eagle S XII 2024; Fitburg 31.12.2025 — B's fact: Euronews, The Moscow Times; since X 2023 at least 11 damaged cables). The question window covers the whole X–III season.
- **A** gives a mechanism ("shadow fleet in winter", "quick proceedings") that supports YES, and yet p = 0.40 — the rationale contains no argument for NO apart from "low confidence". **C** itself marks the lens as weak.
- Counter-argument for B: reinforced NATO patrols since 2025 (Baltic Sentry) and Danish inspections (G1-062) may lower the frequency — B already takes this into account (0.80 → 0.75).
- Conclusion: adjustment upwards (§3), but not to B's level — three observations is a small sample.

Spreads of 0.20–0.25 (below the threshold, for completeness): Q-0039 (A without data — adjustment), Q-0054 (B without fact C-01 — adjustment), Q-0060 (A/C vs B — a difference in judging the length of OFAC's pause after Xi's visit; both sides have an argument, no adjustment), Q-0004 and Q-0016 (§1 item 7, §2.3).

---

## 3. Proposed AGG adjustments

| ID | AGG | proposed adjustment | AGG_RT | rationale | type |
|---|---|---|---|---|---|
| Q-0054 | 0.820 | +0.12 | 0.94 | The SR result rose with the count (4.96% → 5.00%; per C-01 5.13% at 97.64%). Meduza 22.09: approx. 60k votes added at the last stage (interpretation disputed, but indicates a decision on SR's entry). Lens B (0.68) did not have C-01; A and C (0.85, 0.93) have a better basis. I leave approx. 6% for the unpredictability of the final CEC protocol. | evidence |
| Q-0013 | 0.843 | +0.10 | 0.94 | The lenses' arithmetic: fuel +0.8–1.0 pp m/m; base IX 2025 = 0.0% m/m (GUS) → y/y approx. 4.2–4.4%. NO requires approx. −0.8 pp m/m from the rest of the basket — in IX 2025 food alone gave only approx. −0.13 pp. The lenses gave no argument for NO that would correspond to 16%. | logic (inconsistency of the arithmetic with p) + evidence (GUS base) |
| Q-0040 | 0.567 | +0.10 | 0.67 | The only spread > 0.30. B's reference class (3 of 3 winters with an incident and an investigation) is documented. A gives no argument for NO. Adjustment only to about half the distance to B — small sample and reinforced patrols. | evidence |
| Q-0003 | 0.333 | +0.07 | 0.40 | (1) Lenses A and C treat §1249 as a brake, while G1-031 describes a certification procedure (not a ban), with a possible gap after 30.09. (2) ACH-3 in 03: the least refuted are H1 and H2 — both assume a reduction in Europe; the options of 25–40k (G1-030) exceed the 10k threshold by a wide margin; precedent of V 2026 (5k from Germany). AGG 0.333 assumes that the status quo or a postponement beyond 31.03.2027 is twice as likely as a decision — contrary to ACH-3. Moderate adjustment, because the recommendation comes only on 06.11, and H1 may mean a net reduction < 10k. | evidence + consistency |
| Q-0062 | 0.433 | +0.08 | 0.51 | All lenses lowered p because of the lack of data for IX — that is a collection gap (03 §1.7 item 10), not an observation. The VII–VIII pace of 2–3 events/month (including boardings, which the criterion counts) → approx. 0.6–0.7 for 14 days. The adjustment is smaller than full, because the Houthi blockade may actually work through deterrence (A). | logic |
| Q-0039 | 0.217 | −0.07 | 0.15 | A (0.35) without data ("the lens says nothing here"). B's data: the ACP is tightening (draught from 01.10), rainfall −34%, El Niño until 2027, analogy with 2023–24: tightening lasted through the rainy season. Nothing in 02 indicates an improvement in Gatún Lake by 31.10. | evidence |
| Q-0031 | 0.157 | −0.05 | 0.11 | C's rationale (0.20): the Democrats are 3–5 seats short (G4-035), Trump's approval 39%, generic ballot D +7–8 — all of this argues for a lower p, and C gives no argument for a higher one. B's reference class (a president's party with approval < 45% loses at least several seats in almost every midterm) gives approx. 0.10–0.12. Redistricting (Missouri) already included in B. | logic (inconsistency of C's rationale) |
| Q-0050 | 0.333 | +0.05 | 0.38 | A and B started from 8.89 PLN/l (16.09); state on 23.09: 8.99 PLN/l (C-04), threshold 9.00. Only a partial adjustment: Orlen wholesale cut on 23.09, and Brent is falling — retail usually follows wholesale with a lag of approx. a week. | evidence |
| Q-0002 | 0.050 | +0.01 | 0.06 | B: Laplace's rule (0 events in 43 months) → 0.07, then a downward adjustment for "no event despite many incidents" — the same evidence counted twice. After removing the double counting B = 0.07, AGG ≈ 0.057. In addition, B saw A's value before forecasting (log 04-B). | logic |

The remaining 64 questions: **no adjustment** (AGG_RT = AGG). No adjustments "to be safe" and none towards 0.5 without a reason: 5 of 9 adjustments move p away from 0.5 (Q-0054, Q-0013, Q-0040, Q-0039, Q-0031); 4 move it closer (Q-0003, Q-0062, Q-0050, Q-0002) — each with specific evidence or an identified error.

Considered and rejected (evidence insufficient for an adjustment): Q-0004 (§1 item 7), Q-0016 (§2.3), Q-0067 (§1 item 9), Q-0070 (Fitch 2027 calendar unknown — usually February, within the window; A, B, C converge), Q-0055 (B 0.88 on the PolitPro poll average; A 0.75 without new evidence; spread 0.13), Q-0060 (§2.4), Q-0008 (§2.3).

Triviality check (§3.8) after the adjustments: AGG_RT < 0.05 or > 0.95 — 1 question (Q-0001, 0.03) = 1.4% of active questions (limit 20%). Q-0013 and Q-0054 (0.94) below the 0.95 threshold.

---

## 4. Directional bias test

All questions with who_benefits ≠ NONE have p_status_quo = 0.10 (YES requires a change).

| who_benefits | n | mean p_status_quo | mean AGG | mean AGG_RT | AGG − SQ | Questions |
|---|---|---|---|---|---|---|
| US_WEST | 1 | 0.10 | 0.167 | 0.17 | +0.07 | Q-0069 |
| EU | 1 | 0.10 | 0.483 | 0.48 | +0.38 | Q-0019 |
| UKRAINE | 2 | 0.10 | 0.220 | 0.22 | +0.12 | Q-0064 (0.267), Q-0071 (0.173) |
| RUSSIA | 3 | 0.10 | 0.226 | 0.25 | +0.13 (RT: +0.15) | Q-0003 (0.333), Q-0004 (0.227), Q-0073 (0.117) |
| CHINA | 1 | 0.10 | 0.167 | 0.17 | +0.07 | Q-0024 |
| COMPROMISE | 7 | 0.10 | 0.444 | 0.44 | +0.34 | Q-0011 (0.75), Q-0021 (0.683), Q-0022 (0.68), Q-0058 (0.45), Q-0028 (0.30), Q-0072 (0.13), Q-0059 (0.117) |
| NONE | 58 | 0.169 | 0.331 | 0.34 | — | — |

Blocs: the Western side (US_WEST + EU + UKRAINE, n = 4): mean AGG 0.273; the Russian-Chinese side (RUSSIA + CHINA, n = 4): mean AGG 0.211 (after the Q-0003 adjustment: 0.228). IRAN group — 0 questions.

**Conclusion (confidence: low — n = 4 per bloc).** No systematic favouring of either side. The difference between the blocs (approx. 0.05–0.06) comes entirely from one question: Q-0019 (the EU's 22nd package, 0.483). This question has real procedural support: a rhythm of packages every approx. 2.6 months and 4–6 weeks from proposal to adoption. Without Q-0019 the Western bloc has 0.202 — less than the Russian-Chinese one. All groups lie above p_status_quo, because SQ = 0.10 is mechanical and does not take announced decisions into account.
**COMPROMISE** deviates most from SQ (+0.34). Cause: Q-0011, Q-0021, Q-0022 ask about extending an existing truce. Formally YES requires a new decision (SQ 0.10), but in practice an extension is a continuation of the state. This is a feature of how p_status_quo is constructed (§3.5), not a bias in the forecasts. Note for the quarterly review: BSS relative to SQ on these questions will be very sensitive to a single resolution.
Reverse check: the questions in which AGG could reflect Western "wishful thinking" are Q-0071 (Bank of Russia assets) and Q-0064 (drone agreement). Both have low AGG with rationales that run against the wish — no bias is visible.

---

## 5. Consistency with the analysis scenarios

Stage 03 gives no numerical probabilities for scenarios (stage rule). I therefore compare the forecasts with the qualitative conclusions of the ACH and the assessment of scenarios in §1.2.

| Conclusion of the analysis | Implication in the forecasts | Assessment |
|---|---|---|
| The base scenario (BASE "protracted crisis without resolution") remains valid (§1.2) | US–Iran agreement by 31.12: 0.30; US strike: 0.26; Brent > 120: 0.19; Brent < 80: 0.20; TTF > 90: 0.30; US–PRC truce extended: 0.75; Putin–Trump meeting: 0.27 | **consistent** — every marker of FAV and CRIS has p < 0.35, BASE dominates |
| ACH-1 (Iran): least refuted H2 (freeze), then H4; H1 weakened, H3 weakened | H1 ≈ Q-0028 = 0.30; H3 ≈ Q-0065 = 0.26; H2+H4 ≈ 0.44 | **consistent in ordering**; caveat §1 item 2 (Israel) — H3 may be underestimated, but without evidence I do not adjust |
| ACH-2 (USA–PRC): least refuted H2 (short extension, "without resolving rare earths"), H3 (escalation) — the most inconsistent evidence | Q-0011 = 0.75 (H1+H2+H4); P(no extension) ≈ 0.25; Q-0021 = 0.683 | **mostly consistent**. Tension: if H2 means "without resolving rare earths", Q-0021 (extension of the control suspension) could be lower. But not extending the suspension with an extended truce would mean a return of the 09.10.2025 controls, i.e. an escalation contrary to H2. I read "without resolution" as no agreement on licences — no adjustment. |
| ACH-3 (US troops): least refuted H1 and H2 (both with a reduction in Europe); H3 weakened | Q-0003 = 0.333 implied a predominance of H3 | **inconsistent** → adjustment to Q-0003 +0.07 (§3) |
| I16/KA8: stalemate with slow Russian progress | Q-0004 = 0.227; Q-0073 = 0.117 | consistent |
| KA4 (Russia below the threshold of casualties on NATO territory) | Q-0002 = 0.06; Q-0027 = 0.113 | consistent |
| KA6 (EU without a physical shortage; fragile for DE) | Q-0010 = 0.35; Q-0009 = 0.30 | consistent |

---

## 6. Summary

- Adjustments: 9 of 73 questions (+0.12, +0.10, +0.10, +0.08, +0.07, +0.05, +0.01, −0.05, −0.07); none exceeds ±0.15. Types: evidence — 5 (Q-0054, Q-0040, Q-0003 with an element of consistency, Q-0039, Q-0050), logic — 3 (Q-0062, Q-0031, Q-0002), mixed logic + evidence — 1 (Q-0013).
- Spread > 0.30: 1 question (Q-0040) — lens B has the edge.
- Directional bias: not detectable with the current number of questions; COMPROMISE is high because of how SQ is constructed for extensions.
- The largest risk not covered by adjustments: a correlated error in assumption KA1 ("electoral brake") across approx. 10 questions (§1 item 1) and the omission of Israel (§1 item 2).

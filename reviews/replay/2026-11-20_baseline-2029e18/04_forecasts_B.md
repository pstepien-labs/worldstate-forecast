# Replay baseline-2029e18 — lens B "Outside view", edition 02 (cutoff 07.10.2026)

Prompt: `reviews/replay/prompts/04_forecasts_2029e18.md` (lens B section, way of working, tasks). Replay rules (`prompts/R_replay.md`): no web, no registry, no earlier forecasts. Inputs: `questions.csv` of this folder, `02_facts/G1–G4.md`, `03_analysis.md`. Searches used: 0 (none permitted in a replay). Change vs own previous forecast: not available in a replay (no access to earlier rows) — recorded once here, not repeated per question.

Per question: reference class and base rate → persistence and time left (p ≈ 1 − (1 − r)^t, or a barrier/volatility estimate for price thresholds) → cautious case adjustment. Then: reasons for YES, reasons for NO, "by now we would expect …", p. Post-cutoff items seen in the inputs (03_analysis header, G3-069, G4 §15 note): not used.

## Batch 1 — OIL_PRICE, EU_ENERGY, URANIUM (11 questions)

**Q-0007 Brent settlement > 120 any day 24.09–31.12.** Reference: barrier crossing for a ~40% annualised vol series (realised daily moves 2–4%, G2-001). Barrier +18% (log) from 100.2 over ~0.23 y: σ√t ≈ 0.19 → reflection ≈ 0.35, discounted for discrete settlements and the mean-reversion seen in IX ("topped out near 110"). YES: Dated spot already 114–121 (G2-003); escalation options after 03.11 (G1-010); Houthis in range of Yanbu (G2-050). NO: futures 97–103 for two weeks despite ≥10 tanker strikes; flow estimates near pre-war (G2-005); G7/IEA releases (G2-009/010). By now we would expect closes trending above 105 — not seen. **p = 0.25** (medium).

**Q-0008 Brent < 80 any day 24.09–31.12.** Barrier −22% (log) → reflection ≈ 0.24; in practice needs a Hormuz deal (≈ 0.12 by mid-XII, see Q-0028) or a demand collapse. YES: banks see flows near pre-war (G2-005); Aramco's widest Asian discount since 2020 (G2-050). NO: EIA 4Q26 105 (G2-004); spot premium 13–20; no deal track. By now: Brent below 95 with talks advancing — not seen (low close 97.09). **p = 0.15** (medium).

**Q-0074 Brent settlement 20.10 > 100.00.** 9-trading-day walk from 100.20 on the same December contract → ≈ 0.50. YES: physical premium, EIA path. NO: last close fell "as flows recover"; G7 diesel release front-loaded. **p = 0.48** (low).

**Q-0115 Brent < 70 any day 08.10.2026–30.06.2027.** Barrier −36% over ~0.73 y at 35% vol → ≈ 0.23. Check: pre-war Brent in the 60s; wars of this kind end within a year in roughly one case in three; stocks drawn by 325+ mn bbl need refilling (EIA 2027 average 84). **p = 0.25** (low).

**Q-0009 TTF settlement > 90 any day 24.09–31.12.** Barrier +14% at ≈ 50% vol over 12 weeks → reflection ≈ 0.55; discount for discrete settlements. YES: storage lowest for the date since 2011 (G2-016); Qatar force majeure extended (G2-021); JKM premium (G2-020); winter ahead. NO: closes 69.8–78.5; demand response. By now: rising trend — yes, 07.10 is the window high. **p = 0.45** (medium).

**Q-0084 TTF settlement 20.10 > 80.00.** Needs +1.9% in 9 days at ≈ 9% period sd → ≈ 0.42; slight momentum (G2-015). **p = 0.43** (low).

**Q-0010 EU storage 01.01.2027 < 55.0%.** Reference: 01.11→01.01 drawdowns of about 15–24 pp in recent winters (2021/22 ≈ 77 → 54; 2024/25 ≈ 95 → 72). Start ≈ 78–79% (G2-016) → central 57–60%. YES: Qatar constrained, Germany 59%, the 2021/22 analogue. NO: price-driven demand cuts; possible injection into early XI. **p = 0.33** (medium).

**Q-0049 EU storage gas day 06.10 > 73.0%.** 72.83% (05.10) + 0.22 pp/day mean → 73.05; cooler weather 06–07.10 lowers injection. **p = 0.55** (low — threshold at the expected value).

**Q-0067 EU storage gas day 01.11 ≥ 80.0%.** Needs 0.27 pp/day for 27 days vs 0.22 recent; October injection usually slows. **p = 0.12** (medium).

**Q-0103 Cameco month-end U3O8 spot > 95 (X, XI or XII).** Spot flat at ≈ 89.8 for three weeks (G2-048); +6% at one of three month-ends ≈ one in three; record term price a mild pull. **p = 0.30** (low).

**Q-0106 US diesel export ban/quota in force by 31.12.** Reference: no US refined-product export restriction in the modern era; threats used as leverage; the threat was withdrawn 02.10 (G2-009). YES: East Coast distillates 32% below average (G2-004). NO: retraction, industry opposition. By now: a draft order — not seen. **p = 0.06** (medium).

Batch 1 consistency re-read: done. Minutes: ~15. Searches: 0.

## Batch 2 — HORMUZ, IRAN_WAR, IRAN_LEADERSHIP, BAB_EL_MANDAB (14 questions)

**Q-0037 PortWatch Hormuz ≥ 20 transits on any day 24.09–07.10.** Rows to 04.10 known: max 5 (G1-001); only 05–07.10 unpublished. Three days would each need 4× the window maximum; IRGC's own figure is ≈ 10/day "most with permission" (G1-005). **p = 0.03** (high).

**Q-0078 PortWatch Hormuz ≥ 10 on any day 08–17.10.** Reference: last 15 published days, max 5, mean 2.7. Needs double the recent maximum within 10 days. YES: 12 empty Qatari LNG carriers staged near Qatar (G2-022); a clearance regime could make some traffic AIS-visible. NO: route rule plus tanker strikes push traffic dark (03 §C mechanism). By now: a rising AIS series — not seen (1 → 4). **p = 0.12** (medium).

**Q-0036 PortWatch 7-day mean > 40 on any day to 31.12.** Requires a near-normal reopening (pre-war ≈ 85–125/day) lasting a week. Only via an agreement or de facto erosion of the clearance rule — H1/H4, the least supported hypotheses (03 §1.4). **p = 0.08** (medium).

**Q-0028 US–Iran agreement incl. Hormuz opening, confirmed by both, by 31.12.** Reference: this war has already produced one mediated arrangement (17.06 memorandum, G4-086), so the class "wartime US–Iran interim deal" is not empty; but positions widened (7-day plan rejected, "seven conditions", G4-002/003), talks are indirect only, the Iranian mandate is contested (G4-009). Twelve weeks. YES: Vance's softer enrichment line (G4-007); Pezeshkian "not out of reach" (G4-014); Iran's exports at zero (G2-012). NO: build-up and post-election strike options (G1-009/010); IRGC formalised the strait as an instrument (G1-004). By now: a face-to-face round or text — not seen. **p = 0.11** (medium).

**Q-0038 US lifts or suspends the blockade by 31.12.** Almost only as part of a deal (Q-0028), possibly phased after it. **p = 0.09** (medium).

**Q-0065 US strike on Iranian land by 31.12.** Reference: this war saw US strikes on Iran in three episodes after rounds of talks (Pezeshkian, G4-005), none since 01.09 — a hazard of very roughly one episode per two months while active, lower in a freeze. Build-ups of carrier groups with stated end-states have often preceded strikes. YES: third carrier group and 9–10k personnel due by end-XI (G1-009); options "after the elections" (G1-010); Trump "nice way or not-so-nice way" (G4-008); Iran preparing for a "major round" (G4-016). NO: domestic constraint (approval 32%, diesel); the freeze is the least refuted hypothesis (03 §1.4); 5 weeks without a strike. By now: positioning — yes, under way. **p = 0.40** (medium).

**Q-0081 US–Iran in-person meeting in the same room 08–21.10.** Last direct contact 22.09; since then only Qatari shuttle (G4-001, G4-006); the 22.09 meeting triggered an impeachment motion, raising the cost of another. Two weeks. **p = 0.10** (medium).

**Q-0099 USNI tracker: ≥ 3 US carriers in CENTCOM waters by 30.11.** Stated end-state: three carriers around Iran by end-XI (G1-009) — officials' deployment end-states are usually met but often slip by weeks. Now: George Washington in the Arabian Sea; Roosevelt crossing the Pacific (≈ 4–5 weeks' transit → early XI); Bush in Phuket after five months in CENTCOM — a Norfolk carrier at a liberty port east of CENTCOM is consistent with a return to station (G1-057). Tracker must list them in the named waters. **p = 0.42** (low).

**Q-0032 New video/audio of Mojtaba Khamenei by 31.12.** Reference: he has communicated only in writing for months (G4-012); prolonged absence of recordings is persistent (incapacity or security). Hazard per quarter low. **p = 0.10** (medium).

**Q-0096 Araghchi ceases to be FM by 31.12.** Reference: Majlis impeachment motions are often registered and seldom reach the floor; those that do usually succeed (ministers removed in 2022 and 2025). Motion registered, not referred (G4-009); he answered MPs for 3 hours. Twelve weeks. **p = 0.12** (low).

**Q-0068 US strike on Houthi targets by 31.12.** Reference: the US struck the Houthis in 2024 and in III–V 2025, then held a ceasefire; currently "not for now" (G1-021). YES: Saudi pressure and Camp David Yemen options (G1-010); Saudi fatalities (G1-018). NO: US abstention is a deliberate regionalisation (Mecca Alliance, G1-020). **p = 0.28** (low).

**Q-0079 PortWatch Bab el-Mandeb < 20 on any day 08–17.10.** Window range 22–37, mean ≈ 29, sd ≈ 4 (G1-012): a value below 20 is a ~2-sd day; over 10 days ≈ 0.08 under normal tails; fat tails, ground fighting at Dhubab and a first incident since VIII (G1-022) add risk. **p = 0.14** (medium).

**Q-0080 Saudi official: ≥ 1 killed by an attack from Yemen 08–21.10.** Reference: in the escalation since mid-IX, one fatal episode (06–07.10, 3 dead) among ≈ 6 attack episodes in three weeks; the trend is rising (warning to airlines, G1-017; coalition offensive, G1-015). Two weeks → Poisson ≈ 0.35–0.45. **p = 0.40** (low).

**Q-0092 UKMTO/JMIC: merchant ship struck in Red Sea/BeM/GoA 08–21.10.** Reference: physical hits rare since VIII (Amzan 24.08; 04.10 a near miss without damage) → ≈ one per 6 weeks → two weeks ≈ 0.25–0.3; Houthi focus is Saudi land targets. **p = 0.25** (low).

Batch 2 consistency re-read: Q-0038 ≤ Q-0028 (blockade lifting follows a deal); Q-0036 < Q-0028 (reopening must also show in AIS within the window). Minutes: ~15. Searches: 0.

## Batch 3 — RU_MOBILIZATION, UA_FRONT, UA_TALKS, EASTERN_FLANK, BLACK_SEA, BALTIC_INFRA (13 questions)

**Q-0001 Russian mobilisation decree by 31.12.** Reference: one mobilisation decree in 4.5 years of war (IX 2022); the Kremlin funds contract recruitment instead (17.15 trn RUB defence 2027, G3-016). Duma elections passed (brake removed), but no signal. **p = 0.03** (high).

**Q-0002 Person killed on NATO territory by a Russian drone/missile, government-attributed, by 31.12.** Reference: zero such cases since 2022 (Przewodów 2022 was a Ukrainian missile; 2025 drone incursions caused no deaths). New: two dead on a ship in Romania's EEZ — but EEZ is not territory and Romania did not attribute (G1-031). Intensity on the south-east flank is rising (Moldova overflights, G1-034). Twelve weeks. **p = 0.05** (medium).

**Q-0004 DeepState net Russian gain in X > 200 km².** Reference: 2026 monthly net gains 63 (VII), 124 (VIII), 154 (IX, first published as 66) — none above 200; 2024–25 months were often 300–600, but 2026 pace is lower. DeepState holds back 270–320 km² of Ukrainian gains, which can depress later months when published (G1-043); first publications run low. YES: rising trend 63 → 124 → 154; heavy fighting near Kostiantynivka and Pokrovsk (G1-046). NO: Vivaldi counteroffensive (G1-045); ISW shows a net Ukrainian gain in IX (G1-044). **p = 0.20** (low).

**Q-0026 Trilateral US–UA–RU government meeting by 30.11.** Reference: the format has met before (it was "agreed in principle" in ed.01 and has precedent earlier in 2026), so not a novelty; but Moscow says "no current plans" (G4-022). Seven weeks. YES: US proposal of a technical meeting by end-X (G4-021); bilateral channel active (G4-020). NO: Putin's terms unchanged (G4-019); Russia blames Kyiv's strikes. By now: a date or venue — not seen. **p = 0.18** (low).

**Q-0082 Trilateral meeting 08–31.10.** Subset of Q-0026 over 3.5 weeks, with Moscow's explicit "no current plans" of 07.10. **p = 0.07** (medium).

**Q-0030 Putin–Trump in-person meeting by 31.03.2027.** Reference: one in-person meeting in 2025 (Alaska), one planned summit cancelled. Concrete path: APEC Shenzhen 18–19.11, where Trump is committed (fact sheet "mutual attendance", G3-008) and Putin is welcomed by Beijing (G4-027); a trilateral with Xi is "in the air". Joint attendance ≈ 0.65 × 0.50 with correlation; conditional meeting ≈ 0.8; plus other routes over six months. FT: part of APEC may go online (G4-077). **p = 0.33** (low).

**Q-0073 ISW: Russia controls all of Kramatorsk or Sloviansk by 30.06.2027.** Reference: capture of a large defended city has taken 12–18 months (Bakhmut, Avdiivka, Pokrovsk); Kostiantynivka (south of Kramatorsk) is not yet taken; Russian push toward the rear of Sloviansk–Kramatorsk stopped (G1-045); 2026 monthly gains of 60–150 km². **p = 0.03** (high).

**Q-0113 ISW: Russia controls all of Kostiantynivka by 31.03.2027.** Reference: Kostiantynivka has been a main axis for a long time and is the heaviest fighting (G1-046); cities under multi-sided pressure have fallen within 6–12 months of becoming the main effort (Pokrovsk). But the 2026 pace is slow and ISW requires the whole town. Six months. **p = 0.20** (low).

**Q-0110 Signed full-front ceasefire, confirmed by both, by 30.06.2027.** Reference: no general ceasefire in 4.5 years despite several pushes; Russia's terms (rest of Donbas, neutrality) unchanged (G4-019); defence budget up 27% for 2027. Nine months; yearly hazard of a war-ending ceasefire in long attritional wars ≈ 10–15%. **p = 0.08** (medium).

**Q-0027 Article 4 request 24.09–31.12.** Reference: about eight requests since 1949, clustered in crises; two in IX 2025. Rate in the current period ≈ 1–2 per year → 12 weeks ≈ 0.2–0.3. But allies chose national responses to the IX–X 2026 incidents (Mi-8, EEZ sinkings; G1-036). **p = 0.15** (medium).

**Q-0097 DO RSZ/MoD confirms an airspace violation from Russia or Belarus 08.10–31.12.** Reference: officially confirmed violations by Russian/Belarusian aircraft, drones or missiles ≈ 2–4 per year in 2023–26 (latest Mi-8 23.09); the criterion requires the object to come from Russian or Belarusian territory/airspace, which excludes drones entering from Ukraine. Twelve weeks, winter strike campaign on western Ukraine. **p = 0.40** (low).

**Q-0098 RO/BG/TR confirm a merchant ship hit by drone/missile in their waters/EEZ 08.10–31.12.** Reference: Bulgaria already stated a drone attack in its EEZ on 06.10 (G1-032); the Russian MoD runs a declared campaign against ships serving Ukraine (G1-033); strikes on tankers in Turkey's EEZ have precedent (2025). Twelve weeks with an active campaign. **p = 0.55** (low).

**Q-0040 Baltic cable/pipeline damage with proceedings on external action by 31.03.2027.** Reference: such cases in X 2023, XI 2024, XII 2024, I 2025, II 2025 and around the turn of 2025/26 — clustered in winter, ≈ 2 per year → six months incl. winter ≈ 0.6. **p = 0.55** (medium).

Batch 3 consistency re-read: Q-0082 < Q-0026; Q-0073 < Q-0113 (Kramatorsk lies behind Kostiantynivka). Minutes: ~15. Searches: 0.

## Batch 4 — CN_RARE_EARTHS, US_CHINA_TRADE, US_CHINA_TECH, US_CHINA_FIN (10 questions)

**Q-0021 PRC announces extension/repeal of the rare-earth suspension by 10.11.** Reference: in each US–China truce cycle since V 2025 both sides formalised agreed extensions before the expiry date (e.g. MOFCOM's suspension announcement of 07.11.2025, days after Busan). MOFCOM's 28.09 readout extends the Kuala Lumpur arrangement — including "related Chinese export controls" — to 10.01.2027 (G3-010); a lapse on 10.11 would revive the 09.10.2025 controls and break a truce both sides just extended. YES: precedent of near-deadline formalisation; both sides publicly committed. NO: Beijing keeps the legal date as leverage (G2-041; 03 mirror test 6); the readout names no rare earths. By now: a text — not yet, but not expected this early. **p = 0.80** (medium).

**Q-0089 Same, published 08–21.10.** Precedent says formalisation comes close to the deadline and after the US side moves (US Federal Register notices still pending, G3-011, G2-045). **p = 0.15** (low).

**Q-0022 PRC extends the Ga/Ge/Sb/superhard ban suspension by 27.11.** Same truce package, later deadline (G2-042); same logic. **p = 0.78** (medium).

**Q-0102 BIS Federal Register document extending/rescinding the Affiliates-rule suspension, published 08.10–09.11.** The US side of the same bargain; practitioners expect it (G2-045). Risk is timing: last year's suspension was formalised around the deadline itself, and a document dated 10.11 or later would resolve NO. **p = 0.70** (medium).

**Q-0077 Both governments announce extension beyond 10.01.2027 or a replacement deal, 08.10–10.01.2027.** Reference: the truce has been extended at every expiry since V 2025 (VIII 2025, XI 2025, IX 2026), each time by both sides before the deadline; MOFCOM says both seek a further extension "through high-level interaction before year-end" (G3-010); APEC in XI is a venue. NO: tensions over rare-earth deliveries (two-thirds met, G2-041); an announcement could slip past 10.01. **p = 0.72** (medium).

**Q-0108 Both sides put 30-for-30 tariff cuts into effect by 31.12.** Greer: no start date, publication, comment period and legal determination needed (G3-063); twelve weeks for both sides' procedures. Reference: US notice-and-comment tariff actions usually take more than three months. **p = 0.10** (medium).

**Q-0023 MOFCOM lists a US entity (export-control list or UEL) 24.09–31.12.** Reference: MOFCOM listed US entities several times a year in 2024–25, and even during the truce (announcement 23/2026 of 22.06.2026, G3-032); triggers are mainly US arms sales to Taiwan. None since 22.06 (3.5 months). Twelve weeks. **p = 0.33** (low).

**Q-0024 US permits export of Blackwell (or newer) Nvidia chips to PRC by 31.12.** Reference: the administration moved stepwise (H20, then H200 licences with revenue share); Blackwell refused so far (G2-047); smuggling prosecutions continue (G2-046). AI dialogue next session late XI (G3-010). **p = 0.10** (medium).

**Q-0025 PRC magnet exports to the US in IX > 512 t (VIII value).** Reference: month-on-month change is close to a coin flip; September exports usually exceed August seasonally; ed.01 read the VIII drop as a pre-summit signal, and the truce was then extended. **p = 0.57** (low).

**Q-0112 Fed restricts HKMA's FIMA access by 31.03.2027.** Reference: the Fed has not altered a central bank's FIMA access on political request; one congressional letter (G3-064); the Fed replies but does not act. **p = 0.03** (high).

Batch 4 consistency re-read: Q-0089 ≪ Q-0021 (timing); Q-0102 < Q-0021 because the US document must appear by 09.11, one day earlier, and US formalisation has lagged. Minutes: ~12. Searches: 0.

## Batch 5 — TAIWAN, US_CHINA_SUMMITS, RU_SANCTIONS_US, US_EU_TRADE, CN_SECONDARY_SANCTIONS (10 questions)

**Q-0005 Named PLA exercise around Taiwan by 31.03.2027.** Reference: named exercises V 2024, X 2024, IV 2025, XII 2025 — about two a year → six months ≈ 0.6 at the base rate. Adjustment down: a summit cycle (Xi's state visit IX, APEC XI, truce to 10.01) during which Beijing kept Taiwan quiet (peak 23 sorties, G1-053) and shifted pressure to the Philippines (G1-055). Up: F-16V deliveries, Yonaguni deployment, US House visit (G1-054/056, G4-078). **p = 0.38** (low).

**Q-0069 DSCA notifications for TECRO ≥ 1 bn USD by 31.12.** Reference: Taiwan notifications come in irregular bursts, a few per year, some very large (XII 2025); in a summit cycle the administration has held sales back. Twelve weeks. **p = 0.18** (low).

**Q-0087 MND daily report ≥ 30 PLA aircraft 08–21.10.** Reference: in 2024–25 days with 30+ aircraft occurred several times a month (joint combat-readiness patrols), especially around 10.10; in the last two weeks the peak was 23 (G1-053). Lai's National Day speech is a usual trigger, but the détente lowers it. **p = 0.35** (low).

**Q-0029 Trump physically attends APEC Shenzhen.** Reference: Trump attended APEC 2025; the 25.09 fact sheet records "mutual attendance at G20 and APEC" (G3-008). Down: Iran war, post-election period, FT on parts moved online (G4-077). **p = 0.65** (medium).

**Q-0100 Putin physically attends APEC Shenzhen.** Reference: Putin skipped APEC leaders' meetings 2022–25 but travels to China often (it is safe from the ICC warrant); PRC MFA welcomed his attendance (G4-027); Kremlin floats a three-way meeting. Partial online format is a risk. **p = 0.50** (low).

**Q-0012 Tariff under H.R. 5334 on a non-Russian country, effective by 31.12.** Reference: Trump imposed a Russian-oil penalty tariff on India in VIII 2025 (later removed, G3-004), so the class is not empty; but statutory "shall" deadlines are often met by waiver or silence (03 §1.4 Q3: H2/H5 least refuted); China excluded by the truce; Trump weighing relief for prisoners (G3-002). YES: Greer will "name names"; India talks deadlocked (G3-005); bipartisan pressure (G3-006). NO: no 10-day notice to Congress seen by 07.10 (G3-001). **p = 0.18** (low).

**Q-0090 Sec. 112 duty on Russian goods, act published 08–21.10.** Cheap compliance (Russian imports are small) and no 10-day notice needed for Sec. 112, but the US–Russia economic channel (Lukoil, G4-020) and Wright's "decision till the end" (G3-003) point to deferral; statutory deadlines are often missed silently. **p = 0.20** (low).

**Q-0091 OFAC Russia-programme SDN addition 08–21.10.** Reference: under this administration Russia designations have been rare (none 24.09–07.10, G3-026), yet H.R. 5334 Sec. 103 requires sanctions on state-owned banks by 18.10, which could produce new entries; small EO 14024 evasion-network actions also occur. Two weeks. **p = 0.30** (low).

**Q-0015 US tariff on EU goods above the 15% ceiling by 31.03.2027.** Reference: the US has kept the ceiling since 01.07.2026 (G3-058); Trump threatens allies often but breaking a signed deal by formal act is rarer; a possible trigger is the EU's end-2026 steel-derivative deadline. Six months. **p = 0.12** (medium).

**Q-0018 OFAC lists a mainland PRC bank (Iran/Russia) by 31.03.2027.** Reference: OFAC has not SDN-listed a mainland PRC bank in this context in years; Iran-related listings target trading firms (G3-026); the truce makes it costlier. **p = 0.04** (high).

Batch 5 consistency re-read: Q-0030 (0.33) < Q-0029 × Q-0100 path plus other routes — consistent. Minutes: ~12. Searches: 0.

## Batch 6 — RATES_FED, RATES_ECB, RATES_RU, RATES_PL, PL_INFLATION, PLN, PL_FUELS, PL_FINANCE, FOOD (12 questions)

**Q-0066 FOMC hike at 27–28.10.** Reference: the Fed hiked in IX; minutes: "most participants" see another hike "by year end" (G3-033) — two meetings left (X, XII); December carries projections and a hiking cycle of the "measured" kind tends to move at projection meetings. Weak payrolls (+29k, G3-034) and 10Y at 5.3% (G3-035) argue for waiting. **p = 0.33** (medium).

**Q-0017 ECB deposit rate above 2.50% after 29.10 or 17.12.** Reference: this cycle hiked in VI and IX — quarterly, at projection meetings — so XII is the natural next step if energy stays high; HICP 3.8% with energy 18.8% (G3-076); "measured response appropriate" (G3-075). NO: Lane — long yields are "a material tightening", no wage response, no pre-commitment. **p = 0.55** (low).

**Q-0020 Bank of Russia cut on 23.10.** Guidance: average 13.7–14% for the rest of 2026 (G3-065) — consistent with a hold now (a 100 bp cut on 23.10 alone would breach it); inflation 7.1–7.2% above range (G3-067); larger deficit. Reference: the Bank's guidance has been a good guide to the next decision. **p = 0.13** (medium).

**Q-0088 Bank of Russia hike on 23.10.** Reversal after a cutting cycle is rare without a currency or inflation shock; Zabotkin says the budget fits the Bank's assumptions (G3-066). **p = 0.10** (medium). Hold ≈ 0.77.

**Q-0016 MPC changes the NBP rate at any meeting 24.09–31.12.** Meetings left: 03–04.11 (new projection) and XII. CPI 4.0% above band, hawkish wording change, Pekao expects a hike in XI (G3-040). NO: CPN cuts measured CPI in X (see Q-0075); weak employment; policy reversals are rare. **p = 0.40** (low).

**Q-0075 GUS flash CPI X < 3.5% y/y.** Arithmetic: fuels ≈ 6% of the basket; CPN cut pump prices 13–17% from the IX average (G2-026/027) → ≈ −0.7 to −0.8 pp m/m; other components ≈ +0.3 pp; base month X 2025 m/m ≈ +0.1 → y/y ≈ 3.4–3.5. YES: the size of the fuel cut. NO: food pressure (FFPI rising), energy-tariff risk named by the MPC. The threshold sits at my central estimate. **p = 0.50** (low).

**Q-0076 FAO FFPI X > 136.0.** Reference: monthly FFPI changes have mild positive autocorrelation; IX +1.5% with cereals and sugar rising (G2-036); Hormuz fertiliser risk (G2-039); first publications tend to be revised up (VIII 133.3 → 134.0), which helps the October figure relative to a fixed 136.0. **p = 0.60** (low).

**Q-0086 NBP EUR/PLN on 21.10 > 4.4000.** Needs +0.46% in 10 sessions; EUR/PLN daily sd ≈ 0.3% → period sd ≈ 1% → ≈ 0.32; window range 4.3588–4.3900 never touched 4.40; hawkish MPC supports PLN. **p = 0.27** (medium).

**Q-0085 e-petrol diesel 21.10 < 7.70.** Prices sit 2–4 gr below the daily maximum, which has been falling: 7.88 → 7.82 → 7.80 → 7.74 (G2-026); the G7 diesel release is front-loaded into the first 20 days (G2-009). Needs the cap near ≤ 7.72 around 20–21.10, i.e. continuation of the trend. **p = 0.55** (low).

**Q-0105 S&P lowers Poland or moves outlook to negative, decision 08.10–06.11.** Reference: at a scheduled sovereign review an outlook change happens in a minority of cases (≈ 15–20%); here pressure is higher — deficit about 7% (G3-047), S&P raised its deficit forecast, Moody's cut to A3 on 18.09 and Fitch is on negative (G3-049). **p = 0.33** (low).

**Q-0070 Fitch or S&P downgrade Poland below A− by 31.03.2027.** Reference: sovereigns on negative outlook are downgraded within 12–18 months in roughly 40–50% of cases; Fitch's next scheduled review likely falls in I–III 2027; S&P is on stable and normally moves outlook first. **p = 0.30** (low).

**Q-0107 Commission letter of formal notice to Poland on fuel VAT by 31.12.** Reference: the Commission sent only a warning letter for earlier CPN editions (G2-028) and is slow to open infringements over temporary crisis measures; packages in X, XI, XII; the measure is meant to end 31.12. **p = 0.15** (medium).

Batch 6 consistency re-read: Q-0020 + Q-0088 = 0.23 (hold 0.77) — consistent with guidance; Q-0016 0.40 sits between the hike expectation and the CPN effect on X CPI. Minutes: ~15. Searches: 0.

## Batch 7 — RU_SANCTIONS_EU, UA_FUNDING, UA_EU, US_EUROPE, GREENLAND (9 questions)

**Q-0083 Council adopts ≥ 1,500 new Russia listings 08–21.10.** Reference: Coreper agreements on listings are normally adopted by the Council within days (written procedure or the next FAC); adoption scheduled 12.10 (G3-022). Risks: a late hold by one member state; how the 77 Duma-candidate listings are counted (all under Russia-related regimes). **p = 0.88** (high).

**Q-0019 Council adopts a package named the "22nd package" by 31.12.** Reference: EU Russia packages have come every 3–5 months since 2022, often delayed weeks by one member state; Vlasiuk expects the sectoral 22nd package in XI (G3-024); Hungary's lifted veto on clusters (G4-028) suggests less obstruction. There is also a chance the Council itself labels the 12.10 listings the 22nd package (TASS usage, G3-023). Twelve weeks. **p = 0.60** (medium).

**Q-0104 Council adopts a new import/export prohibition 08.10–30.11.** The sectoral package is the vehicle; "November more realistic" from the Ukrainian side, whose timelines usually slip; deadline 30.11 is the edge of that estimate. **p = 0.38** (low).

**Q-0071 Council act allowing use of the frozen CBR assets themselves by 30.06.2027.** Reference: the reparations-loan route failed at the end of 2025 and was replaced by joint borrowing; Belgium's objection is structural. New pressure: Ukraine's 2027 gap (G3-054), refusal to front-load (G3-053). Nine months. **p = 0.15** (low).

**Q-0101 EU formally opens cluster 2 or 3 with Ukraine by 31.12.** Hungary lifted its veto 07.10 (G4-028); next step needs Ukraine's minority-rights law, then a common position and an IGC — IGCs are usually held in December before the presidency ends. Reference: once the last veto falls, openings have followed within one or two months. **p = 0.50** (low).

**Q-0003 Decision to cut ≥ 10,000 US troops in Europe announced by 31.03.2027.** Options of 25–40k cuts exist; the review is to end in XII (G1-038); a precedent of a smaller announced cut (rotational brigade, 2025). NO: Congress's floor provisions (Q-0109), allies offering to pay for bases (G1-040), decisions often framed as "options" or phased. **p = 0.30** (low).

**Q-0109 FY2027 NDAA with a EUCOM troop floor enacted 08.10–31.12.** Reference: NDAAs were enacted in late December in most recent years (FY2022–FY2026; FY2021 slipped to 01.01 via veto override) → ≈ 0.85; the FY2026 law carried the 76k floor and a SASC draft adds a further check (G1-041) → floor retained ≈ 0.75. **p = 0.62** (medium).

**Q-0114 Location of a new permanent US Army base in Poland officially announced by 31.03.2027.** Decision "not before December" (G1-037); candidate list only (G4-050); the 2018–20 "Fort Trump" episode never produced a named site; partisan dispute in Poland (G4-049). **p = 0.22** (low).

**Q-0111 US–Denmark–Greenland defence agreement in force by 30.06.2027.** Needs parliamentary procedures in Greenland and Denmark; no timetable yet (G4-054); Naleraq opposition (G4-055). Reference: the US–Denmark DCA took about 18 months from signature to Folketing approval. Nine months. **p = 0.33** (low).

Batch 7 consistency re-read: Q-0104 < Q-0019 (narrower content, earlier deadline). Minutes: ~10. Searches: 0.

## Batch 8 — US_ELECTIONS, BRAZIL, BG, IL, VENEZUELA, SAHEL, PANAMA, CAUCASUS (9 questions)

**Q-0031 Republicans ≥ 218 House seats.** Reference: the president's party has lost House seats in about 90% of midterms; with approval below 40% it has lost control in nearly every case where the majority was narrow. Inputs: approval 32% (record low), generic ballot D+7 (G4-045, C/3); GOP majority narrow after 2024; mid-decade redistricting roughly offsetting. **p = 0.10** (medium).

**Q-0095 Republicans ≥ 50 Senate seats.** Republicans hold 53; Democrats need a net gain of 4 to push them to 49. The map is hard for Democrats (seats in red states), but a 32%-approval environment produces broad waves; independents do not count as Republicans. Reference: in wave midterms the out-party typically gains 2–6 Senate seats. **p = 0.45** (low).

**Q-0033 Lula wins the 2026 presidential election.** Reference: the first-round leader has won every Brazilian runoff since 1989. Round one: F. Bolsonaro 47.03 vs Lula 45.16 (G4-029); the eliminated Caiado and Zema endorsed Bolsonaro (G4-030); polls underestimated Bolsonaro (G4-032). Lula needs most of the remaining ≈ 7.8% mostly right-leaning voters, or turnout shifts. **p = 0.20** (medium).

**Q-0093 Iotova > 50% of valid votes in round one (25.10).** Polls: 41.4% and 44.5% "of intending voters" (G4-087) — share of valid votes is higher once undecided are removed (≈ 47–50%), but 27 tickets and the "I support no one" option dilute it. Reference: 2021 — Radev 49.4% in round one, just short. **p = 0.30** (low).

**Q-0094 Likud wins strictly the most Knesset seats.** Five-poll average Likud 23 vs Yashar 22.2; latest Channel 12 Yashar 23, Likud 21 (G4-034). Reference: Likud finished first in every Knesset election since 2015 except IV 2019 (a tie, which here counts NO); polls have not systematically under- or overstated it. A tie = NO. **p = 0.45** (low).

**Q-0034 Venezuela announces a presidential election date by 31.03.2027.** Promise without date (G4-065); opposition sequence TSJ (XI) → CNE (XII) → elections, civil society proposes VII 2027 (G4-066); a new CNE could set a schedule in Q1. Reference: Venezuelan authorities have delayed electoral calendars repeatedly; US pressure for elections appears weak (G4-067). **p = 0.30** (low).

**Q-0035 Goïta loses power by 31.03.2027.** Reference: annual hazard of leader exit for Sahel junta heads ≈ 10–15% (coups 2020–23); Goïta has held since 2021 and just retook Kidal with Africa Corps (G4-060). Six months. **p = 0.07** (medium).

**Q-0039 Panama Canal daily limit above 32 in force by 31.10.** ACP advisory of 28.09: 33 daily slots from 15.10 (G1-061), rainy season. Risks: advisory withdrawn, or "slots" read differently from the "transit limit" in the criterion. **p = 0.88** (medium).

**Q-0072 Armenia–Azerbaijan sign the peace treaty by 30.06.2027.** Text initialled VIII 2025; Azerbaijan conditions signature on a change to Armenia's constitution, which requires a referendum not yet held; the process is viewed as blocked until 2027 (03 §1.2 item 22). Nine months. **p = 0.18** (low).

Batch 8 consistency re-read: done. Minutes: ~10. Searches: 0.

## Run summary

88 of 88 questions forecast (Q-0001 – Q-0115 as listed in `questions.csv`). Mean p = 0.31. Searches: 0 (replay). Post-cutoff facts seen in the inputs: 6, not used. Possibly contaminated questions: none (training data to VI 2026; all outcomes fall after 07.10.2026).

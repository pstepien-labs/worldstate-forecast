# Stage 03 — Changes to the question bank (edition 03, state 16.11.2026)

Registry before the stage: 115 questions — 48 ACTIVE and 67 RESOLVED (40 resolved in stage 01 of this edition). Added in this stage: **35 questions (Q-0116 – Q-0150)** — 13 panel replacements and 22 open questions. After the stage: **150 questions, 83 ACTIVE** (panel 40 = 5 per vector; open 43). No forecasts. Only appended rows; no existing row changed (`git diff --stat registry/questions.csv`: 35 insertions, 0 deletions). No question was resolved in item 1.8 (§6).

## 1. Rules applied in this edition

**INFO_CUTOFF and windows.** INFO_CUTOFF is 17.11.2026 15:08 (first line of `03_analysis.md`). Every new criterion counts events from **18.11.2026** onward ("between 18.11 and …"), or a value first published after the cutoff (GUS, FAO, Eurostat, FRED for 30.11, NBP for 30.11, Cameco month-ends). `created` = 16.11.2026 (state date), `edition_created` = 03, as in edition 02. For every new question no qualifying event can have occurred before the window opens; the state on 17.11 was checked for the questions whose event was scheduled or imminent (Q-0123 Serbia, Q-0132 Shenzhen, Q-0134 Estonia, Q-0136 Rada, Q-0137 prisoner exchange, Q-0146 Israel) — none had occurred by the cutoff (§2, notes).

**Readable resolution source (framework 1.5, P-0002).** Every new question names one deciding source that was read without login, key or paywall in this edition (stage 02 or a check in this stage on 17.11.2026), and a named fallback. The source, the value or item read and its date are listed per question in §2. Sources tested and **not** readable on 17.11.2026, therefore not used as deciding sources: centcom.mil, war.gov, congress.gov, senate.gov roll-call lists, president.gov.ua, consilium.europa.eu (HTTP 403); apnews.com (not fetchable); clerk.house.gov (vote list empty); pancanal.com advisories index (HTTP 404); infoelectoral.interior.gob.es (403), knesset.gov.il (empty), opec.org (402), eur-lex Official Journal page (empty), kremlin.ru (fetch failed) — the last five tested earlier in this stage (03_analysis §1.9 item 15). Where an official site is unreadable, the criterion names the official statement as the event and a readable outlet as the record (e.g. Q-0129, Q-0140).

**Horizon boundaries (prompt 03; §3.3).** "By the next edition": deadline ≤ 30.11.2026 (STATE_DATE + 14 days). "End of quarter": 01.12–31.12.2026. "Longer": after 31.12.2026.

**p_status_quo (§3.5)** — the mechanical rules of editions 01–02 (ed.02 03_question_bank_changes §1):
1. YES requires a new action (decree, strike, attack, listing, announcement, adoption, meeting, scheduled decision, recurring event) → 0.10.
2. Thresholds on continuous values: YES on the same side as the last known value → 0.90 (Q-0126 Brent 92.14 > 90; Q-0131 EUR/PLN 4.4048 > 4.40; Q-0145 HICP 4.0 ≥ 4.0); opposite side, including "higher/lower than the last value" → 0.10.
3. Elections: largest party in a new parliament → 0.50 (Q-0133).
4. **New case — Q-0143 (shutdown):** if nobody takes a new decision, the continuing resolution expires on 11.12 and appropriations lapse, so YES is the no-decision outcome → 0.90 by the literal §3.5 wording. Recorded as a default taken in AUTO mode; the user may review it.
Result: 30 × 0.10, 4 × 0.90, 1 × 0.50.

**who_benefits (§3.6):** NONE unless YES clearly strengthens one actor at another's expense. COMPROMISE for extensions of suspensions (Q-0119 as Q-0021; Q-0147 as Q-0102); RUSSIA for a US troop reduction in Europe (Q-0144, consistent with Q-0003); EU for a European seat at the US–UA–RU table that Moscow refuses (Q-0149). Distribution: NONE 31, COMPROMISE 2, RUSSIA 1, EU 1.

**Clusters (§3.4):** new labels RS_GOVERNMENT, ES_ELECTIONS, IL_GOVERNMENT, US_FISCAL. Existing labels reused wherever the outcome is the same (UA_TALKS, HORMUZ, IRAN_WAR, CN_RARE_EARTHS, US_CHINA_TECH, RATES_FED, RATES_ECB, PLN, UA_FUNDING, BLACK_SEA, EASTERN_FLANK, US_EUROPE, KOREA, TAIWAN, US_CHINA_SUMMITS, US_ELECTIONS).

## 2. New questions

### 2.1 Panel replacements (13)

| ID | Replaces | Vector | Cluster | Question (short) | Deadline | p_sq | who | PIR | Deciding source — item read (date) |
|---|---|---|---|---|---|---|---|---|---|
| Q-0116 | Q-0004 | MIL | UA_FRONT | Russian MoD reports ≥ 1,400 Ukrainian drones in one report, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-1 | t.me/s/mod_russia — channel readable (17.11.2026); state 1,336 on 16.11 via Moscow Times/Kyiv Post (G1-039). Fallback Interfax/Moscow Times |
| Q-0117 | Q-0009 | ENE | EU_ENERGY | TTF front-month close > 100.00 EUR/MWh any day 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-3 | Investing.com TTF historical data — 84.05 (16.11.2026), read in stage 02 (G2-011). Fallback ICE Endex via Reuters/Bloomberg; Trading Economics |
| Q-0118 | Q-0020 | FIN | RATES_RU | Bank of Russia cuts the key rate on 18.12 | 18.12.2026 | 0.10 | NONE | PIR-1; PIR-6 | cbr.ru key-rate table (harvested) — 14.00% (16.11.2026). Fallback Interfax |
| Q-0119 | Q-0021 | TEC | CN_RARE_EARTHS | MOFCOM/GAC continue the rare-earth suspension beyond 10.01.2027 (or repeal), 18.11–10.01.2027 | 10.01.2027 | 0.10 | COMPROMISE | PIR-4 | mofcom.gov.cn — Announcement No. 58 of 09.11.2026 listed (read 17.11.2026). Fallback Xinhua |
| Q-0120 | Q-0025 | TEC | CN_RARE_EARTHS | MOFCOM announces new critical-mineral export controls or ends a suspension early, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-4 | mofcom.gov.cn — latest announcements Nos. 56–58 (06–09.11), no new item control (read 17.11.2026). Fallback Xinhua |
| Q-0121 | Q-0026 | DIP | UA_TALKS | Another US–UA–RU delegation meeting, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-1; PIR-7 | Ukrinform — no date for a round; LT-12 (read 17.11.2026). Fallback whitehouse.gov; Interfax |
| Q-0122 | Q-0031 | DOM | US_ELECTIONS | Hegseth ceases to be Secretary of Defense/War, 18.11–31.03.2027 | 31.03.2027 | 0.10 | NONE | PIR-2; PIR-7 | whitehouse.gov briefing room — no item on Hegseth, latest items 17.11 (read 17.11.2026). Fallback NBC; CNN |
| Q-0123 | Q-0033 | DOM | RS_GOVERNMENT | Serbian Assembly elects a new PM and government, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-7 | srbija.gov.rs — no government elected (read 17.11.2026). Fallback RFE/RL; Balkan Insight |
| Q-0124 | Q-0037 | INF | HORMUZ | PortWatch ≥ 10 Hormuz transits on any day 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-5 | PortWatch ArcGIS API — n_total 1–6 a day 06–15.11, 2 on 15.11 (read 17.11.2026). Fallback PortWatch chokepoint page |
| Q-0125 | Q-0039 | INF | PANAMA | ACP puts > 34 daily slots in force, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-3 | pancanal.com (advisory page read in stage 01); 34 slots from 09.11 per AJOT, Newsroom Panama, DataPortuaria (search 17.11.2026). Fallback gCaptain; DataPortuaria |
| Q-0126 | Q-0074 | ENE | OIL_PRICE | FRED DCOILBRENTEU for 30.11 > 90.00 | 30.11.2026 | 0.90 | NONE | PIR-3; PIR-5 | FRED — 92.14 (11.11), 90.16 (10.11) (read 17.11.2026). Fallback EIA RBRTED |
| Q-0127 | Q-0075 | ECO | PL_INFLATION | GUS flash CPI for November > 3.5% y/y | 30.11.2026 | 0.10 | NONE | PIR-6; PIR-3 | stat.gov.pl — release list readable, October CPI release 13.11; October 3.5% y/y (flash and final; ISBnews, finwire via search 17.11.2026). Fallback PAP Biznes/ISBnews |
| Q-0128 | Q-0076 | ECO | FOOD | FAO FFPI for November < 133.9 | 07.12.2026 | 0.10 | NONE | PIR-3 | fao.org FFPI page — 133.9 for October (06.11), read in stage 02 (G2-024). Fallback FAO newsroom; Reuters |

### 2.2 Open questions (22)

**To the next edition (deadline ≤ 30.11.2026) — 11**

| ID | Vector | Cluster | Question (short) | Deadline | p_sq | who | PIR | Deciding source — item read (date) |
|---|---|---|---|---|---|---|---|---|
| Q-0129 | MIL | IRAN_WAR | CENTCOM or a GCC government confirms an Iranian drone/missile attack on a US installation, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-5 | The National — LT-01–LT-03 (read 17.11.2026). Fallback CNN; Al Jazeera. centcom.mil 403 |
| Q-0130 | MIL | TAIWAN | ≥ 2 MND releases on a PLA JCRP dated 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-4 | mnd.gov.tw press-release list — six JCRP releases 09.10–12.11 (read 17.11.2026, stage 02). Fallback Focus Taiwan; Taipei Times |
| Q-0131 | FIN | PLN | NBP EUR/PLN for 30.11 > 4.4000 | 30.11.2026 | 0.90 | NONE | PIR-6 | api.nbp.pl (harvested) — 4.4048 (16.11.2026). Fallback nbp.pl archive |
| Q-0132 | DIP | US_CHINA_SUMMITS | Joint statement of the US, PRC and Russian leaders published 18.11–22.11 | 22.11.2026 | 0.10 | NONE | PIR-1; PIR-4 | whitehouse.gov briefing room — lists joint statements; no trilateral text (read 17.11.2026). Fallback kremlin.ru feed; fmprc.gov.cn |
| Q-0133 | DOM | ES_ELECTIONS | PP wins strictly the most seats in Spain's Congress, 29.11 | 30.11.2026 | 0.50 | NONE | PIR-7 | lamoncloa.gob.es — 29N election pages linking the Interior Ministry results site (read 17.11.2026). Fallback RTVE; Reuters |
| Q-0134 | INF | EASTERN_FLANK | Estonian government decision closing road crossings with Russia to passenger traffic, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-1 | valitsus.ee — no decision; latest items 12–15.11 (read 17.11.2026). Fallback ERR News |
| Q-0135 | DIP | KOREA | Trump and Kim meet in person, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-4 | whitehouse.gov (read 17.11.2026); Yonhap (harvested). Fallback Yonhap |
| Q-0136 | FIN | UA_FUNDING | Rada adopts the 2027 State Budget in final reading, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-6 | rada.gov.ua — no final adoption; latest items 17.11 (read 17.11.2026). Fallback Ukrinform |
| Q-0137 | DIP | UA_TALKS | Single prisoner exchange of ≥ 500 per side, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-1 | Ukrinform — no exchange reported (read 17.11.2026). Fallback Interfax; Kyiv Independent |
| Q-0138 | FIN | RU_SANCTIONS_US | OFAC Russia-programme SDN addition, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-1; PIR-6 | ofac.treasury.gov Recent Actions — none 22.10–13.11 (read 17.11.2026, stage 02). Fallback harvested SDN diff |
| Q-0139 | INF | BLACK_SEA | Romanian authorities report a merchant vessel hit by a drone/USV/missile in Romania's territorial sea or EEZ, 18.11–30.11 | 30.11.2026 | 0.10 | NONE | PIR-1; PIR-2 | mapn.ro — releases Nos. 373–375 and drone dashboard updated 17.11 (read 17.11.2026). Fallback Euronews; gov.ro |

**To the end of the quarter (01.12–31.12.2026) — 7**

| ID | Vector | Cluster | Question (short) | Deadline | p_sq | who | PIR | Deciding source — item read (date) |
|---|---|---|---|---|---|---|---|---|
| Q-0140 | MIL | IRAN_WAR | US government confirms on the record a US strike on Iranian land, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-5 | whitehouse.gov (read 17.11.2026); NBC News (LT-05, 17.11). Fallback CNN |
| Q-0141 | DIP | HORMUZ | US and Iranian government representatives meet in the same room, 18.11–31.12 | 31.12.2026 | 0.10 | NONE | PIR-5 | whitehouse.gov; NBC News (read 17.11.2026). Fallback The National; Al Jazeera |
| Q-0142 | FIN | RATES_FED | FOMC raises the target range on 09.12 | 09.12.2026 | 0.10 | NONE | PIR-6 | FRED DFEDTARU (harvested) — 4.00 (16.11.2026). Fallback federalreserve.gov |
| Q-0143 | ECO | US_FISCAL | Lapse in US appropriations begins, 12.12–31.12 | 31.12.2026 | 0.90 | NONE | PIR-6 | opm.gov operating status — Open, 17.11.2026 (read 17.11.2026); CR to 11.12 (CRS, stage 02). Fallback NBC; CRS |
| Q-0144 | MIL | US_EUROPE | White House or Pentagon announces a cut of ≥ 5,000 US troops in Europe, 18.11–31.12 | 31.12.2026 | 0.10 | RUSSIA | PIR-2 | whitehouse.gov (read 17.11.2026). Fallback Defense News. war.gov 403 |
| Q-0145 | ECO | RATES_ECB | Eurostat flash HICP for November ≥ 4.0% | 03.12.2026 | 0.90 | NONE | PIR-6; PIR-3 | Eurostat euro indicators — 4.0% flash for October (04.11), read in stage 02 (G3-041). Fallback ECB data; Reuters |
| Q-0146 | DOM | IL_GOVERNMENT | Knesset approves a new government, 18.11–20.12 | 20.12.2026 | 0.10 | NONE | PIR-5; PIR-7 | Times of Israel — coalition-talk headlines (read 17.11.2026; items with unclear timestamps not used). Fallback Knesset press releases; Reuters |

**Longer (after 31.12.2026) — 4**

| ID | Vector | Cluster | Question (short) | Deadline | p_sq | who | PIR | Deciding source — item read (date) |
|---|---|---|---|---|---|---|---|---|
| Q-0147 | TEC | US_CHINA_TECH | BIS extends the Affiliates-rule suspension beyond 10.01.2027 or rescinds the rule, 18.11–10.01.2027 | 10.01.2027 | 0.10 | COMPROMISE | PIR-4 | federalregister.gov API — FR 2026-22793 of 09.11.2026 (read in stage 02, G2-032). Fallback bis.gov |
| Q-0148 | ENE | PL_FUELS | Energy Minister publishes a maximum fuel-price notice for a day in January 2027, by 31.01.2027 | 31.01.2027 | 0.10 | NONE | PIR-3; PIR-6 | gov.pl/web/energia — daily notices, no extension past 31.12 mentioned (read 17.11.2026). Fallback Monitor Polski; Bankier/PAP |
| Q-0149 | DIP | UA_TALKS | E5 or EU representative in a round with US, UA and RU delegations, 18.11–31.03.2027 | 31.03.2027 | 0.10 | EU | PIR-1; PIR-2; PIR-7 | Ukrinform — LT-12 (read 17.11.2026). Fallback Kremlin feed; Interfax |
| Q-0150 | TEC | URANIUM | Cameco month-end long-term price ≥ 100.00 USD/lb, any month-end XI 2026–III 2027 | 31.03.2027 | 0.10 | NONE | PIR-3 | cameco.com — long-term 98.00 for October (read in stage 02, G2-033). Fallback TradeTech/UxC via World Nuclear News |

Full criteria, sources, key indicators and notes are in `registry/questions.csv`.

## 3. Replacements

| Resolved panel question | Vector / cluster | Replaced by | Change |
|---|---|---|---|
| Q-0004 (DeepState net gain X > 200 km²) | MIL / UA_FRONT | Q-0116 | No readable deciding source for the territorial series in this edition (DeepState monthly summary not found in stage 01; Russia Matters and ISW HTTP 403; DeepState Telegram readable on 17.11 but shows no monthly total). Replaced by a deep-strike intensity measure in the same cluster, resolved on a Russian MoD statement (a fact about a statement) |
| Q-0009 (TTF > 90 to 31.12) | ENE / EU_ENERGY | Q-0117 | Threshold raised to 100 (90 crossed on 22.10); Investing.com close as the deciding source (ICE Endex not reachable) |
| Q-0020 (Bank of Russia cut 23.10) | FIN / RATES_RU | Q-0118 | Rolling: next meeting 18.12 |
| Q-0021 (rare-earth suspension extended by 10.11) | TEC / CN_RARE_EARTHS | Q-0119 | Rolling: next cliff 10.01.2027 |
| Q-0025 (magnet exports to the US IX > 512 t) | TEC / CN_RARE_EARTHS | Q-0120 | A monthly-magnet successor was not created: the US figure came from one secondary source and GAC was not opened (Q-0025 is VERIFY ambiguous). New item controls instead (ACH 3, H3) |
| Q-0026 (trilateral by 30.11) | DIP / UA_TALKS | Q-0121 | Rolling: another trilateral by 31.12 |
| Q-0031 (Republicans ≥ 218 House seats) | DOM / US_ELECTIONS | Q-0122 | **Deviation:** the election is over; the cluster now carries its consequences. A War Powers or impeachment vote question was preferred but congress.gov, clerk.house.gov and senate.gov vote lists were unreadable on 17.11.2026; a cabinet-change question with whitehouse.gov as the deciding source was taken instead |
| Q-0033 (Lula wins) | DOM / BRAZIL_ELECTIONS | Q-0123 | **Deviation:** BRAZIL_ELECTIONS exhausted; same vector, new cluster RS_GOVERNMENT (formation of a government after an election that changed the majority). Recorded as a default taken in AUTO mode |
| Q-0037 (PortWatch ≥ 20 Hormuz, 24.09–07.10) | INF / HORMUZ | Q-0124 | Rolling, threshold 10 (as G1 K1); PortWatch API readable on 17.11.2026 with rows to 15.11 |
| Q-0039 (ACP > 32 slots by 31.10) | INF / PANAMA | Q-0125 | Rolling: > 34 slots (34 since 09.11) |
| Q-0074 (Brent ICE 20.10 > 100) | ENE / OIL_PRICE | Q-0126 | FRED spot series instead of ICE (vendor-contract dispute, G2 §11 item 1); date 30.11, threshold 90 |
| Q-0075 (GUS flash X < 3.5%) | ECO / PL_INFLATION | Q-0127 | Rolling: November flash > 3.5% |
| Q-0076 (FFPI X > 136.0) | ECO / FOOD | Q-0128 | Rolling: November FFPI < 133.9 |

Panel after the stage: 40 ACTIVE, 5 per vector (checked).

## 4. Candidates from stage 02 — decisions

| Candidate | Decision | Question | Reason / change |
|---|---|---|---|
| G1 K1 | Accepted with correction | Q-0124 (panel) | Window 18.11–30.11 (after INFO_CUTOFF) |
| G1 K2 | Accepted with correction | Q-0140 | Presidential remarks explicitly count (Q-0065 VERIFY issue); window from 18.11 |
| G1 K3 | Accepted with correction | Q-0129 | Short window (to 30.11); host-state set limited to the GCC; Iranian claims excluded |
| **G1 K4** | **Rejected** | — | ukmto.org returns HTTP 403 (stage 02) and JMIC PDFs are unreadable — no readable deciding source |
| **G1 K5** | **Rejected** | — | "Entered the city of Aden" is hard to verify from one-sided sources (G1 gap 7), as ed.02 rejected Mocha |
| **G1 K6** | **Rejected** | — | Saudi official sources not read in this edition (SA official cell silent; spa.gov.sa not opened) |
| **G1 K7** | **Rejected** | — | Government attribution to Russia remains a rare political act; kept as indicator I12; the hit itself is Q-0139 |
| G1 K8 | Accepted with correction | Q-0134 | Reframed as the government decision within the short horizon |
| **G1 K9** | **Rejected** | — | Duplicates Q-0114 (base location, US or Polish government, by 31.03.2027) |
| G1 K10 | Accepted | Q-0144 | Nested in Q-0003 (noted) |
| G1 K11 | Accepted | Q-0130 | — |
| **G1 K12** | **Rejected** | — | Overlaps Q-0005 (named exercise by 31.03.2027) |
| G1 K13 | Accepted with correction | Q-0116 (panel) | Window from 18.11; uncrewed vessels excluded |
| **G1 K14** | **Rejected** | — | KOREA covered by Q-0135 this edition; MIL already the largest vector (15 active) |
| **K-G2-01** | Merged | Q-0126 (panel) | Date moved from 15.12 to 30.11 (short horizon) |
| **K-G2-02** | **Rejected** | — | Same outcome family as Q-0008 (Brent < 80 by 31.12, ICE); a second instrument for the same event adds little |
| **K-G2-03** | **Rejected** | — | opec.org returned HTTP 402 in this stage and the Saudi official cell is silent — no readable deciding source |
| K-G2-04 | Accepted | Q-0117 (panel) | — |
| K-G2-05 | Accepted | Q-0128 (panel) | Deadline 07.12 (three days for a delayed release) |
| K-G2-06 | Accepted | Q-0119 (panel) | Window from 18.11 |
| **K-G2-07** | **Rejected** | — | Serial extensions of the Russian diesel export ban — triviality risk (§3.8), as in editions 01–02 |
| K-G2-08 | Accepted | Q-0148 | — |
| **K-G2-09** | **Rejected** | — | e-petrol.pl states that current data need a login; the readable row was a cached latest week — deciding source not reliably readable |
| K-G2-10 | Accepted with correction | Q-0150 | Horizon extended to 31.03.2027 (long bucket) |
| K-G2-11 | Accepted | Q-0147 | — |
| **K-G2-12** | **Rejected** | — | Resolved by one company's statement; as ed.01–02 |
| **K-G2-13** | **Rejected** | — | Weak PIR link (Lithuanian domestic tax) |
| K3-01 | Accepted | Q-0142 | — |
| K3-02 | Accepted with correction | Q-0118 (panel) | Narrowed to a cut (as Q-0020) |
| **K3-03** | **Rejected (deferred)** | — | FIN already 13 active; RATES_UK has weak PIR link |
| K3-04 | Accepted | Q-0143 | ECO vector; deciding source opm.gov (congress.gov HTTP 403) |
| **K3-05** | **Rejected (deferred)** | — | FIN load; UST10Y kept as indicator I18a |
| **K3-06** | **Rejected (deferred)** | — | FIN load; RU_FINANCE kept as indicator I21 |
| K3-07 | Accepted with correction | Q-0131 | Short variant: value on 30.11 against 4.40 |
| K3-08 | Accepted | Q-0145 | Cluster RATES_ECB (feeds the ECB decision of Q-0017) |
| **K3-09** | **Rejected** | — | Compound criterion (date and deficit share); sozd.duma.gov.ru and minfin.gov.ru not read |
| **K3-10** | **Rejected** | — | minfin.gov.ru not read in this edition |
| K3-11 | Accepted with correction | Q-0138 | Short window (to 30.11) |
| **K3-12** | **Rejected** | — | Same outcome family as Q-0077 and Q-0147 (US formalisation of the truce); one more US measure adds little |
| **K3-13** | **Rejected** | — | Council and EUR-Lex pages unreadable on 17.11.2026 (consilium HTTP 403, OJ page empty) — no readable deciding source |
| K3-14 | Accepted | Q-0136 | — |
| **K3-15** | **Rejected** | — | Chinese half of Q-0077 |
| **K4-01** | **Rejected** | — | Folketing vote on 19.11 is a step toward Q-0111 (entry into force); ft.dk not read |
| **K4-02** | **Rejected** | — | Weak PIR link; elections.ps read in stage 02 but polling-day reporting by the CEC on the day is uncertain |
| K4-03 | Accepted with correction | Q-0133 | Deadline 30.11 (provisional results); deciding source changed (infoelectoral 403) |
| K4-04 | Accepted | Q-0146 | Deciding source Times of Israel (knesset.gov.il empty) |
| K4-05 | Accepted | Q-0123 (panel) | Used as the DOM panel replacement for Q-0033 |
| K4-06 | Accepted with correction | Q-0149 | Horizon to 31.03.2027 |
| K4-07 | Accepted with correction | Q-0137 | Short window (to 30.11) |
| K4-08 | Accepted | Q-0132 | Window 18–22.11 starts after INFO_CUTOFF |
| K4-09 | Accepted with correction | Q-0135 | Short window (to 30.11; Asia trip) |
| **K4-10** | **Rejected** | — | VENEZUELA covered by Q-0034; Rubio's mid-December remark known only via a search summary; asambleanacional.gob.ve not read |
| K4-11 | Accepted | Q-0141 | Cluster HORMUZ (as Q-0081) |

New questions not from stage 02 candidates: Q-0120 (new MOFCOM item controls — ACH 3), Q-0121 (rolling trilateral), Q-0122 (US cabinet change after the midterms), Q-0125 (Panama rolling), Q-0127 (GUS rolling), Q-0139 (Black Sea hits in Romanian waters — successor of Q-0098).

## 5. Statistics

**Horizons of new questions (§3.3):**

| Horizon | Panel | Open | Total | Share | §3.3 target |
|---|---|---|---|---|---|
| To the next edition (≤ 30.11.2026) | 3 | 11 | 14 | 40% | about 40% |
| To the end of the quarter (01.12–31.12.2026) | 8 | 7 | 15 | 43% | about 40% |
| Longer (after 31.12.2026) | 2 | 4 | 6 | 17% | about 20% |

**Vectors:**

| Vector | New panel | New open | New total | ACTIVE after the stage (panel + open) |
|---|---|---|---|---|
| MIL | 1 | 4 | 5 | 15 (5 + 10) |
| ENE | 2 | 1 | 3 | 9 (5 + 4) |
| ECO | 2 | 2 | 4 | 8 (5 + 3) |
| FIN | 1 | 4 | 5 | 13 (5 + 8) |
| TEC | 2 | 2 | 4 | 8 (5 + 3) |
| DIP | 1 | 5 | 6 | 14 (5 + 9) |
| DOM | 2 | 2 | 4 | 9 (5 + 4) |
| INF | 2 | 2 | 4 | 7 (5 + 2) |
| **Total** | **13** | **22** | **35** | **83 (40 + 43)** |

Open intake 22 (prompt range 20–30); ACTIVE 83 (≤ about 90). INF open questions remain the thinnest (2): Red Sea and UKMTO-based questions had no readable deciding source.

**PIR (new questions; a question may have several):** PIR-1 9, PIR-2 4, PIR-3 8, PIR-4 6, PIR-5 6, PIR-6 9, PIR-7 6. ACTIVE after the stage: PIR-1 23, PIR-2 12, PIR-3 18, PIR-4 18, PIR-5 15, PIR-6 21, PIR-7 13. PIR-2 remains the least covered.

**p_status_quo:** 30 × 0.10, 4 × 0.90, 1 × 0.50. **who_benefits:** NONE 31, COMPROMISE 2, RUSSIA 1, EU 1.

**Clusters:** 45 labels among ACTIVE questions; most populated OIL_PRICE, HORMUZ, UA_TALKS 5 each; EASTERN_FLANK, US_EUROPE 4 each.

**Triviality (§3.8):** cannot be assessed before the forecasts. Controls: thresholds near current values (Q-0126, Q-0127, Q-0131, Q-0145), short windows for recurring events (Q-0129, Q-0130, Q-0138, Q-0139), serial-extension candidates rejected (K-G2-07). Check after stage 06.

## 6. Questions resolved in item 1.8 (before forecasts)

None. Each of the 48 ACTIVE questions was checked against its YES criterion for events dated on or before INFO_CUTOFF; none was met (03_analysis §1.8 lists the closest cases: Q-0002, Q-0022, Q-0029, Q-0030, Q-0100, Q-0097, Q-0019, Q-0104, Q-0068, Q-0103, Q-0007, Q-0008, Q-0114, Q-0111). No row was appended to `registry/resolutions.csv`.

## 7. Notes for later stages

- **Stage 04:** questions due 18–30.11 (14) come first in lens searches. Facts after INFO_CUTOFF (17.11.2026 15:08) must not be used — this includes the Shenzhen meetings of 18–19.11 (Q-0029, Q-0100, Q-0132), the Estonian decision of 20.11 (Q-0134) and the Folketing vote of 19.11 (Q-0111); post-state-date facts reach the lenses only through 03_analysis §1.7 (LT-01 – LT-12).
- **Q-0003 and Q-0144 are nested** (≥ 10,000 by 31.03.2027 vs ≥ 5,000 by 31.12.2026): YES on Q-0003 by 31.12 implies YES on Q-0144.
- **Q-0119, Q-0147 and Q-0077** belong to one family (US–China truce cliff 10.01.2027); Q-0022 (Ga/Ge/Sb, 27.11) is its first test.
- **Q-0124** uses AIS counts only; JMIC/CENTCOM escort figures do not count (03_analysis §1.1 C).
- **Q-0143** p_status_quo 0.90 is a new application of §3.5 (default taken in AUTO mode; the user may review it).
- **Q-0122 and Q-0123** deviate from "same cluster" because their clusters' outcomes are exhausted (default taken in AUTO mode).
- **Stage 01 of edition 04:** Q-0124 needs PortWatch rows to 30.11 (lag about 2 days on 17.11); Q-0127 (30.11), Q-0128 (≈ 04.12) and Q-0145 (≈ 02.12) need first publications; Q-0150 needs month-end values to III 2027.
- **Blocked domains** in this stage's searches: rule 3.9 list plus robinhood.com, betfair.com, oddschecker.com, centralbank.watch, fattail.ai. No forecasting-service or market page was opened.

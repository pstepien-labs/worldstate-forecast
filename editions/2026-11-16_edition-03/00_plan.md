# Edition 03 — plan (stage 00)

Stage 00 run on 16.11.2026 (23:01–) for the state date 16.11.2026, in AUTO mode (autopilot; no user questions). Facts below carry date and source; items marked ASSESSMENT are judgements. Items from search summaries are **leads** for stages 01 and 02, not fact records. This file contains no probabilities.

## 1. Edition parameters and versions

| Parameter | Value |
|---|---|
| NR | 03 |
| STATE_DATE | 16.11.2026 |
| PERIOD_FROM | 07.10.2026 (state date of edition 02) |
| DIRECTORY | `editions/2026-11-16_edition-03` |
| PREVIOUS | `editions/2026-10-07_edition-02` |
| PREV_TAG | `edition-02` (commit e7d4c9e, "edition-02 stage-08") |
| REGISTRY_BASELINE | `edition-02` (the previous edition's tag; `methodology/methodology_changes.md` names no other baseline for edition 03) |
| Methodology | v1.0 (frozen) |
| Next edition (earliest, +14 days) | 30.11.2026 |

Output of `python3 tools/pipeline.py versions` at the start of the stage (after the edition directory and CURRENT.md were created, before any commit):

```
framework_version 1.8.0 · methodology_version v1.0 · harvester_version 1.4.0
commit 8e72e4170c8a · branch main · dirty_files 2 (editions/CURRENT.md, editions/2026-11-16_edition-03/)
edition 03 · claude_cli 2.1.325 (Claude Code)
```

Model: claude-opus-5-5. The stage H commit (4e053f2, "edition-03 stage-H") was made inside this stage; versions unchanged.

**Previous edition closed.** `python3 tools/pipeline.py status` reported every stage of edition 02 (00 to 08) as done; tag `edition-02` exists and points to e7d4c9e ("edition-02 stage-08"); `registry/editions.csv` holds the edition 02 row (tag edition-02).

**Timing.** Edition 03 was due on 21.10.2026 and starts 26 days late (see `methodology_changes.md`, framework 1.8.0). The window 07.10–16.11.2026 is 41 days long, about three normal windows: stage 02 has more ground to cover and stage 01 has 32 overdue questions (section 3).

## 2. Harvest window actually covered and its gaps

Stage H (mode digest) was run inside this stage; details in `02_harvest/harvest_notes.md`.

- Window 07.10–16.11.2026: 188,978 items (83,759 matched to concepts), 53 languages, 125–126 countries, Western share 26%.
- **No late start:** the harvester ran on every day of the window; items by publication date range from about 3,200 to about 6,000 a day, no day missing.
- Sources at the state date: 202 enabled — 159 ok, 31 throttled, 1 retrying (PortWatch, ArcGIS quota HTTP 429), 3 failing (ISW HTTP 403; PressTV TLS error since 10.11; Saba HTTP 403), 8 skipped (AGSI, EIA, FIRMS keys not set; teleSUR robots.txt).
- **GDELT gap:** 30 GDELT queries throttled, 15 with no items at all (PL, JA, KO, TR, ES, HE language queries; sanctions, tariffs, talks, chips, Sahel, Sudan/Horn).
- Flagged concept (mandatory targeted search): Poland fuels ⚠W>80% (G2).
- Silent required cells: PL, SA, IN, TW, JP official; TR western; YE state/loyal; GL independent. Near-silent: NATO official, China official (1 item each), Iran official (6).
- Not covered by harvested primary data: TTF, EU/PL gas storage, Polish fuel prices, NBP rate, ECB decisions after 05.10 (series not refetched), ISW assessments; PortWatch only 13 daily rows in the window (10–11.10, 16–18.10, 25.10, 29.10–01.11, 06–08.11).
- OFAC SDN diff of 04.11.2026: 1,095 rows added and 1,080 removed in one snapshot — probably a list re-issue or re-format rather than real designations; stage 01/G3 must read OFAC recent actions instead of the diff count for that day.

## 3. Questions to resolve in stage 01

Registry: 115 questions — 88 ACTIVE (40 panel, 48 open), 27 RESOLVED. Harvested values are taken from `02_harvest/indicators.md` and `data/harvest/datasets/` (primary datasets); web leads come from search summaries in this stage and must be checked against the named resolution source in stage 01.

### 3.1 Deadline ≤ 16.11.2026 (32 questions)

| ID | Deadline | Resolution source | Harvested value / lead found in stage 00 |
|---|---|---|---|
| Q-0049 | 06.10 | agsi.gie.eu | Carried over from edition 02 (AGSI+ needs an API key; secondary readings at the threshold). AGSI not harvested |
| Q-0037 | 07.10 | portwatch.imf.org | Carried over from edition 02 (PortWatch then published only to 04.10). Harvested Hormuz daily totals 24.09–27.09: 5, 3, 4, 1; 03.10: 2; 04.10: 4; no harvested rows 28.09–02.10 and 05–07.10 |
| Q-0078 | 17.10 (window 08–17.10) | PortWatch daily | Harvested Hormuz daily totals: 10.10: 4; 11.10: 2; 16.10: 7; 17.10: 0. **No harvested rows 08–09.10 and 12–15.10** |
| Q-0079 | 17.10 (window 08–17.10) | PortWatch daily | Harvested Bab el-Mandeb daily totals: 10.10: 22; 11.10: 31; 16.10: 25; 17.10: 29. **No harvested rows 08–09.10 and 12–15.10** |
| Q-0025 | 20.10 | PRC customs | Not checked |
| Q-0074 | 20.10 | ICE Brent settlement | No ICE settlement harvested. FRED Brent **spot** on 20.10: 115.22 USD/bbl (spot ≠ front-month settlement) |
| Q-0084 | 20.10 | ICE Endex TTF | Not harvested; not checked |
| Q-0080 | 21.10 | SPA, GACA | Not checked |
| Q-0081 | 21.10 | state.gov, mfa.ir | Not checked for the window |
| Q-0083 | 21.10 | consilium.europa.eu | Lead: EEAS release of 12.10.2026 — the EU adopted its "largest-ever" set of listings, almost 1,600 persons and entities (eeas.europa.eu). Count and legal act to be read in the Official Journal |
| Q-0085 | 21.10 | e-petrol | Not harvested; not checked |
| Q-0086 | 21.10 | api.nbp.pl | **Harvested: EUR/PLN 4.3641 (NBP table A, 21.10.2026)** |
| Q-0087 | 21.10 | mnd.gov.tw | Not checked (TW official cell silent in harvest) |
| Q-0089 | 21.10 (window 08–21.10) | mofcom.gov.cn | Lead: MOFCOM and GAC announced the extension of the rare-earth and related suspensions on **09.11.2026** (The Star 09.11; SMM; Benchmark) — outside this question's window; check for any earlier announcement in 08–21.10 |
| Q-0090 | 21.10 | federalregister.gov | Not checked (H.R. 5334 30-day deadline was about 18.10) |
| Q-0091 | 21.10 | OFAC recent actions | Harvested SDN additions (all programmes, diff counts): 09.10: 56; 13.10: 15; 15.10: 27; 21.10: 18 — programme not identified in the harvest; read OFAC recent actions |
| Q-0092 | 21.10 | UKMTO/JMIC | Lead: ACLED (to 01.10) — no corroborated maritime attack after 24.08; window not checked |
| Q-0020 | 23.10 | cbr.ru | Lead: Bank of Russia kept the key rate at 14.00% on 23.10.2026 (cbr.ru governor's statement; TASS; Reuters via Yahoo). **Harvested: cbr.ru key-rate table shows 14.00% on 27.10 and 28.10.2026** (raw snapshot 28.10) |
| Q-0088 | 23.10 | cbr.ru | As Q-0020 |
| Q-0066 | 28.10 | federalreserve.gov | **Harvested: FRED DFEDTARU 4.00 and DFEDTARL 3.75 unchanged from 07.10 to 16.11.2026.** Lead: FOMC held 3.75–4.00% on 28.10 by a 10–2 vote (fedratecalc) |
| Q-0004 | 31.10 | DeepState | Not checked |
| Q-0033 | 31.10 | tse.jus.br | Runoff of 25.10 not checked |
| Q-0039 | 31.10 | pancanal.com | Not checked |
| Q-0075 | 31.10 | stat.gov.pl flash | Lead: CPI October 2026 at 3.5% y/y (Stockwatch, 04.11, citing the flash) — the criterion is "below 3.5%"; confirm the flash value and its rounding on stat.gov.pl |
| Q-0082 | 31.10 (window 08–31.10) | kremlin.ru, president.gov.ua | Lead: the trilateral US–UA–RU round was scheduled for **10–11.11.2026** in Abu Dhabi (Witkoff via US News/Reuters 02.11; Meduza 03.11) — after this window; check for any meeting in 08–31.10 |
| Q-0093 | 31.10 | cik.bg | First round 25.10 not checked |
| Q-0067 | 01.11 | agsi.gie.eu | AGSI not harvested; not checked |
| Q-0094 | 06.11 | bechirot.gov.il | Knesset election of 27.10 not checked |
| Q-0105 | 06.11 | spglobal.com | Not checked |
| Q-0076 | 09.11 | fao.org | Not checked (October FFPI, release about 06.11) |
| Q-0102 | 09.11 | federalregister.gov (BIS) | Not checked |
| Q-0021 | 10.11 | mofcom.gov.cn | Lead: on **09.11.2026** MOFCOM and the General Administration of Customs announced that six October-2025 export-control announcements stay suspended from 11.11.2026 to 10.01.2027 (The Star 09.11; SMM; Benchmark Minerals; TechTimes 10.11). Read the MOFCOM announcement |

Pending verification from edition 02: **Q-0042** (resolution version 1, VERIFY held by the user on 11.10.2026; `user_approved` empty) — stage 01 re-checks as the note in `questions.csv` requires.

### 3.2 Later deadline, but the event may already have occurred

| ID | Deadline | Signal found in stage 00 |
|---|---|---|
| Q-0031 | 31.12 | Democrats won the House on 03.11 (one count 255 D – 163 R with 17 uncalled; CNBC 04.11; Variety) — check AP and clerk.house.gov |
| Q-0095 | 31.12 | Democrats won the Senate on 03.11 (one count 54 D + independents vs 44 R, Alaska and Mississippi uncalled; later report "Democrats win final two Senate seats", The Conversation) — check AP and senate.gov |
| Q-0065 | 31.12 | Trump confirmed "minor strikes" on Iranian air-defence systems on **Qeshm island** on 06.11.2026 (Al Jazeera 07.11; GlobalSecurity 12.11). Qeshm is Iranian territory but an island in the Strait — whether it counts as "Iranian land territory" is a criterion question (VERIFY candidate). Unconfirmed reports of further explosions on Qeshm 15–16.11 |
| Q-0099 | 30.11 | USS Theodore Roosevelt arrived in the CENTCOM area on 15.11.2026, "bringing the carrier count in the region to three" (Al Jazeera 16.11; Army Recognition; INSS) — read the USNI Fleet and Marine Tracker |
| Q-0026 | 30.11 | Trilateral US–UA–RU round in Abu Dhabi from 10.11.2026 (scheduled per Witkoff; delegations and a 314-prisoner exchange reported only by a Wikipedia compilation) — confirm on kremlin.ru / president.gov.ua |
| Q-0029, Q-0100 | 19.11 | White House confirmed Trump's attendance on 13.11; Kremlin aide Ushakov said on 12.11 that Putin will meet Trump in Shenzhen (ABC News; Al Jazeera 14.11) — the meeting days are after the state date |
| Q-0030 | 31.03.2027 | A Trump–Xi–Putin trilateral is planned at APEC on 19.11 (ABC News, Al Jazeera 14.11) — after the state date |
| Q-0016 | 31.12 | MPC 03–04.11: rates unchanged, reference 3.75% (TVN24, Stockwatch 04.11) — not resolved; next meeting 01–02.12 |
| Q-0019, Q-0104 | 31.12 / 30.11 | EU listings of 12.10 (about 1,600) and 16.11 (145, incl. 49 financial institutions; Ukrinform, UNN 16.11) are listings, not a numbered package; the 22nd package is "being finalised", target "by Christmas" (UNN citing Ireland's FM) — no new import/export prohibition found |
| Q-0017 | 31.12 | ECB decision of 29.10 not checked (harvested ECB rate series not refetched since 05.10) |
| Q-0022 | 27.11 | Reports of the 09.11 MOFCOM extension cover the October-2025 announcements; whether the Ga/Ge/Sb suspension was included is not established |
| Q-0007, Q-0008, Q-0115 | 31.12 / 30.06.2027 | Harvested FRED Brent **spot**: 125.78–130.18 USD/bbl on 07–15.10 and 128.30 on 23.10; low 90.16 on 10.11. ICE front-month settlements needed for Q-0007; spot stayed far above 80 and 70 |
| Q-0036 | 31.12 | Harvested Hormuz daily totals in the window 0–8 — no sign of a 7-day average above 40 |
| Q-0097 | 31.12 | No October–November 2026 Polish airspace violation found in one English search (weak check; PL official cell silent) |
| Q-0114 | 31.03.2027 | Polish defence minister: the Pentagon "green-lit" a permanent US presence; final White House decision expected in early December; the Pentagon readout did not mention the base (Military Times 12.11; Stars and Stripes 11.11) — no location announced found |
| Q-0028, Q-0038 | 31.12 | No US–Iran agreement; blockade maintained; Iran's seven conditions unchanged (CBS, The National 16.11) |
| Q-0001, Q-0002, Q-0009, Q-0010, Q-0012, Q-0018, Q-0023, Q-0024, Q-0027, Q-0032, Q-0040, Q-0068, Q-0069, Q-0096, Q-0098, Q-0101, Q-0103, Q-0106–Q-0109 | various | No signal searched or found in stage 00; stage 01 runs its standard check |

All other ACTIVE questions (Q-0003, Q-0005, Q-0015, Q-0034, Q-0035, Q-0070–Q-0073, Q-0077, Q-0110–Q-0113): deadline in 2027 and no signal of occurrence found in stage 00.

## 4. Calendar 17.11–28.12.2026 (6 weeks)

Status: **C** = confirmed on the web in this stage (official page or several agreeing sources); **U** = unconfirmed or single non-official source.

| Date | Event | PIR | Status | Source |
|---|---|---|---|---|
| 17.11 | Araghchi in Muscat (Oman channel) while the US build-up continues | PIR-5 | U | search summary of INSS / Iran International reporting, 16.11 |
| 17–18.11 | APEC CEO Summit, Shenzhen | PIR-4 | C | US News explainer 12.11 |
| 18–19.11 | APEC leaders' meeting, Shenzhen; Trump–Xi bilateral 19.11; first Trump–Xi–Putin trilateral planned (time and venue not announced) | PIR-1, PIR-4, PIR-7 | C (dates, attendance announced); U (trilateral format) | ABC News, Al Jazeera 14.11; White House 13.11; Ushakov 12.11 |
| 18.11 | FOMC minutes (27–28.10 meeting) | PIR-6 | C (secondary, from edition 02) | fedratecalc |
| 20.11 | COP31 ends (Antalya) | — | C (edition 02) | unfccc.int |
| 26–27.11 | Special European Council on the MFF 2028–2034 | PIR-2, PIR-6 | C on the Council calendar; "tbc" in the Leaders' Agenda | consilium.europa.eu |
| 27.11 | End of China's suspension of the Ga/Ge/Sb/superhard-materials export ban to the US (Q-0022) | PIR-4 | C (registry, edition 02) | registry |
| 28.11 | Palestinian legislative elections (scheduled earlier) | PIR-5 | U (not re-confirmed) | edition 02, K.6 |
| 29.11 | Spain snap general election (350 Congress seats; campaign 13–27.11) | PIR-7 | C | Euronews, Al Jazeera 05.10 |
| 29.11 | OPEC+ full ministerial meeting (2027 quotas, capacity review) | PIR-3 | C | CNBC 31.10 |
| 30.11 | Deadlines Q-0026, Q-0099, Q-0104; earliest date of edition 04 | — | — | registry |
| 01.12 | Swedish Patriot mission at Rzeszów begins | PIR-2 | U (edition 02) | edition 02, K.6 |
| 01–02.12 | MPC (decision 02.12) | PIR-6 | C | nbp.pl harmonogram RPP |
| 02.12 | NATO foreign ministers, Brussels (Rutte press conference 01.12) | PIR-1, PIR-2 | C | nato.int media advisory 13.11; TASS |
| early XII | White House decision on a permanent US base in Poland; posture-review results "expected in December" | PIR-2 | U (DECL by the Polish minister) | Military Times 12.11; Böll Foundation 30.10 |
| 08–09.12 | FOMC (decision 09.12, with projections) | PIR-6 | C (secondary; federalreserve.gov not opened) | fedratecalc, FXNX |
| 10.12 | Eurogroup | PIR-6 | C | consilium.europa.eu |
| 11.12 | End of US government funding (CR, P.L. 119-103); shutdown possible from 12.12 00:01 ET | PIR-6, PIR-7 | C (secondary, several agreeing) | Holland & Knight 10.2026 |
| 14–15.12 | G20 leaders' summit, Trump National Doral (Miami) | PIR-4, PIR-6 | C | City of Doral |
| 17.12 | ECB monetary policy meeting (decision, staff projections) | PIR-6 | C | ecb.europa.eu calendar (via search) |
| 17–18.12 | European Council (MFF, enlargement) | PIR-2, PIR-7 | C | consilium.europa.eu media advisory 26.10 |
| 18.12 | Bank of Russia key-rate meeting | PIR-6 | C | cbr.ru / TASS / Reuters reporting of 23.10 |
| by 24.12 | EU 22nd sanctions package — target "by Christmas" | PIR-1, PIR-6 | U | UNN citing Ireland's foreign minister, 16.11 |
| 23.12 | New Spanish Cortes convene | PIR-7 | C (single compilation) | Wikipedia via search |

Just beyond the window: 31.12 (many registry deadlines; intended end of Poland's CPN III); 01.01.2027 EU ban on long-term Russian LNG contracts; 10.01.2027 end of the extended US–China truce and of the extended rare-earth suspensions (MOFCOM 09.11); 11.02.2027 South Sudan elections (moved). Lead not confirmed and not used: one search summary says Lagarde will step down as ECB President on 07.02.2027 (single low-quality source).

Changes against edition 02's calendar: the 10.11 rare-earth deadline passed with an extension to 10.01.2027 (MOFCOM 09.11); the trilateral US–UA–RU meeting took place on 10–11.11 in Abu Dhabi rather than by the end of October (lead); the OPEC+ seven met on 31.10 (December targets unchanged; CNBC) and the full ministerial is 29.11; Spain's election on 29.11 is confirmed; APEC now includes a planned Trump–Xi–Putin trilateral.

## 5. PIRs (unchanged, methodology v1.0 §2)

- **PIR-1** Russia's capability and will to escalate against NATO and the eastern flank.
- **PIR-2** US/NATO capability and will to respond; US presence in Europe and in Poland.
- **PIR-3** Prices and availability of energy (oil, gas, fuels) in Europe and in Poland.
- **PIR-4** US–China rivalry: trade, technology, raw materials, Taiwan.
- **PIR-5** The war with Iran and sea lanes (Hormuz, Bab el-Mandeb, Suez).
- **PIR-6** Financial condition of the great powers and capital-market conditions, including PLN.
- **PIR-7** Shifts in the orientation of states (elections, alliances, changes of government).

## 6. What moved since edition 02 (10 priority searches + harvest coverage)

Signals from search summaries, harvest volumes and harvested primary data — not fact records. Each needs verification and three perspectives in stage 02.

| Vector / region | Signal (date, source) | Change vs edition 02 |
|---|---|---|
| MIL/DIP — Iran, Hormuz | US "minor strikes" on Iranian air defences on Qeshm 06.11, the first after the midterms (Al Jazeera 07.11); third carrier (Theodore Roosevelt) in CENTCOM 15.11; US–Israeli plans for strikes on economic infrastructure reported (Iran International 16.11, citing NYT); IRGC claims six tankers mined or set on fire since 15.11 (unverified), US says main routes cleared; Iranian drones at a US radar in Bahrain; Iran's seven conditions, backed by a 10-nation regional bloc per Araghchi; flows at 47% of pre-war per a tracker (CBS, The National 16.11). Harvest: Hormuz 3,501 items, Iran–US talks 1,548 | **Large.** The post-03.11 military option became limited strikes on Iranian territory; the sea war and the build-up continue; talks stalled |
| ENE — oil | Harvested Brent spot 126–130 USD/bbl in mid-October, 128.30 on 23.10, then 107.39 (02.11), 91.84 (04.11), 92.14 (11.11) (FRED); biggest weekly drop since 2020 in the week to 06.11 (RTÉ); IEA: surplus in Q4 as Middle East exports recover (CNBC 16.11); Brent futures about 94–95 on 16.11 | **Large.** The price shock of September–October reversed in early November |
| DOM — USA | Democrats won the House and the Senate on 03.11 (CNBC, Variety); analysts link it to the Iran war and fuel prices; funding ends 11.12 | **Large.** New congressional balance from 01.2027; lame-duck agenda (CR, NDAA) |
| DIP — Ukraine talks | Witkoff met Putin in St Petersburg (late X); trilateral round in Abu Dhabi from 10.11 (Meduza, US News); 314-prisoner exchange reported (single compilation); Trump–Xi–Putin at APEC 19.11 planned | **Large.** The trilateral format Moscow refused on 07.10 took place |
| TEC/ECO — US–China | MOFCOM 09.11 extended the suspensions to 10.01.2027 (The Star, SMM); FT: US officials say China met about two-thirds of its rare-earth commitments (via Benchmark summary); Trump–Xi bilateral 19.11 | Medium. Deadline moved, no settlement |
| FIN — EU sanctions | About 1,600 listings adopted 12.10 (EEAS); 145 more on 16.11 incl. 49 financial institutions (Ukrinform, UNN); 22nd package targeted by Christmas | Medium |
| MIL/DIP — Poland and US posture | Pentagon "green light" for a permanent US presence, White House decision early December (Military Times 12.11); reported options of 25,000–40,000 fewer US troops in Europe (NBC/Reuters via search summary) | Medium; decision still in December |
| FIN — Poland | MPC held 3.75% on 04.11; CPI October 3.5% y/y (flash, via Stockwatch); harvested EUR/PLN 4.3641 (21.10) to 4.4233 (03.11) and 4.4048 (16.11) | Small to medium |
| MIL — Saudi–Houthi, Red Sea | Saudi interceptions toward Riyadh and Mecca province 11–12.11 (CFR tracker); Houthis accuse Saudi strikes of killing 3 on 16.11 (AP via Local10); Houthis took positions from Dhubab to Bab el-Mandeb after government forces withdrew (JPost 16.11); no ship attack found after 24.08. Harvested Bab el-Mandeb transits 19–38 a day | Medium. Land and air war continues; coast lost by government forces |
| FIN — Russia | Bank of Russia held 14% on 23.10, raised its 2026 inflation forecast to 7.1–7.6% (cbr.ru, Reuters); USD/RUB 85.71 (07.10) to 80.49 (27.10) and 82.15 (14.11) (cbr.ru, harvested) | Small |
| DOM — Europe | Spain snap election 29.11 (Euronews); Israel (27.10), Brazil runoff (25.10) and Bulgaria (25.10) results to be read in stage 01 | New items |

Harvest volumes (largest concepts): War in Ukraine 20,429; elections 11,846; drones and missiles 11,803; Israel–Iran–Levant 7,586; Russia domestic 7,353; summits and talks 6,970; Latin America 6,762.

## 7. Collection priorities for stage 02

- **G1 (MIL + INF):** US strikes on Qeshm and any further strikes (CENTCOM, Iranian A-side, third-party); carrier count (USNI); Hormuz mines and tanker incidents 15–16.11 (UKMTO/JMIC) and PortWatch days missing in the harvest; Saudi–Houthi war and the Bab el-Mandeb coast; Ukraine front in October and November (DeepState; ISW blocked — secondary reports) and strike campaigns; Polish airspace (DO RSZ directly — PL official cell silent); Black Sea ship incidents (Q-0098); Baltic infrastructure; Taiwan (mnd.gov.tw — TW official cell silent). Silent cells to close by direct search: PL, TW, JP, SA official; YE state/loyal (Saba failing).
- **G2 (ENE + TEC):** **mandatory flagged search: Poland fuels (⚠W>80%)** — non-Polish and industry coverage, e-petrol and Orlen primary prices. Oil collapse of early November (ICE settlements, IEA OMR, OPEC+ 31.10 and 29.11); TTF and AGSI storage (AGSI key missing — read agsi.gie.eu); rare earths (MOFCOM 09.11 text, Ga/Ge/Sb 27.11), BIS affiliates rule after 09.11, Nvidia exports, uranium, US diesel export policy, EU VAT infringement on Polish fuels. Thin concepts: rare earths 233 items, food 288, uranium 330.
- **G3 (ECO + FIN):** EU listings of 12.10 and 16.11 and the 22nd package; OFAC Russia designations in the window (read recent actions; the 04.11 diff is not usable); H.R. 5334 outcome after the 18.10 deadline; Bank of Russia, FOMC and ECB (29.10) decisions; MPC and CPI; S&P (06.11) and Fitch on Poland; UST10Y; US–China tariff lists; Russian budget readings in the Duma; US funding deadline 11.12. Silent cell: PL official (NBP, MF communiqués).
- **G4 (DIP + DOM):** US midterm results and consequences for Iran policy, NDAA and sanctions; Abu Dhabi trilateral (all three sides); APEC trilateral preparations; Iran diplomacy (Muscat, the 10-nation bloc) and Araghchi's position (Q-0096); Israel's election and government formation; Brazil runoff; Bulgaria; Spain 29.11; Venezuela; Mali; Greenland agreement (GL cell silent); Armenia–Azerbaijan; Mojtaba Khamenei recordings. Thin: US forces in Europe 91 items, Arctic/Greenland 320.

## 8. Registry problems (integrity check)

| Check | Result |
|---|---|
| Encoding and BOM | All 7 CSV files in `registry/`: UTF-8 with BOM, separator `;` — OK |
| Headers vs template | Every header identical to the baseline `edition-02` (questions 17 columns, forecasts 8, benchmarks 8, resolutions 11, sources 9, editions 11, question_proposals_edition_00 17) — OK |
| Field counts | Every row of every file has the header's field count — OK |
| Unique question IDs | 115 questions, 115 unique IDs (Q-0001…Q-0115); 88 ACTIVE (panel 40 = 5 per vector × 8; open 48), 27 RESOLVED — OK |
| Forecasts for non-existent questions | None. 805 rows = 73 × 5 runs (edition 01) + 88 × 5 runs (edition 02); no duplicate (question, edition, run) keys; all p within 0.01–0.99 — OK |
| Benchmarks / resolutions for non-existent questions | None (111 benchmark rows, 36 resolution rows) — OK |
| Status vs resolutions | Every RESOLVED question has a resolution row and no ACTIVE question has one — OK |
| Changes to history vs REGISTRY_BASELINE (`edition-02`) | `forecasts`, `benchmarks`, `sources`, `question_proposals_edition_00`: unchanged. `resolutions`: 9 rows appended (version 2 rows of the user verification of 11.10.2026, commit a4ee8d9), no baseline row changed. `editions`: 1 row appended (edition 02, commit c0c333d). `questions`: one row changed, Q-0042, in the `notes` field only (user's VERIFY hold) — permitted — OK |
| Pending verification | Q-0042 (VERIFY, `user_approved` empty) — stage 01 re-check |
| Notes | (1) `registry/editions.csv` still uses CRLF line endings and quotes every field (format inconsistency noted in edition 02; not repaired). (2) 32 ACTIVE questions are past their deadline (section 3.1) because the edition is 26 days late — not a registry defect |

The check was a one-off read-only script run from a git-ignored scratch directory (`data/tmp_oneoff/`, deleted at the end of the stage); nothing was saved in the repository.

## 9. Gaps of stage 00

- Search budget: 10 priority searches and 9 calendar searches (WebSearch; forbidden domains of rule 3.9 blocked in every query); no page fetched. Most leads in section 3 rest on search summaries and must be read at the source in stage 01.
- Not checked at all in this stage: Q-0004, Q-0025, Q-0033, Q-0039, Q-0067, Q-0080, Q-0081, Q-0084, Q-0085, Q-0087, Q-0090, Q-0093, Q-0094, Q-0102, Q-0105, Q-0076, Q-0017.
- Dates unconfirmed or single-source: Araghchi in Muscat 17.11; Palestinian elections 28.11; Swedish Patriot mission 01.12; White House base decision "early December"; 22nd package "by Christmas"; special European Council 26–27.11 ("tbc" in one Council document); Spanish Cortes 23.12.
- Primary calendars not opened: federalreserve.gov (FOMC), ecb.europa.eu and nbp.pl pages were seen only through search results.
- Polish airspace: only one English-language search, no Polish-language or DO RSZ check.
- Harvest: ECB series stale since 05.10; PortWatch 13 of 41 days; no AGSI, TTF, e-petrol, ICE settlement data.

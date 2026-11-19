# L4 — Sources and coverage (scope `latest`)

Run: 19–20.11.2026 · stage L4 · framework 1.9.2 · methodology v1.0 · model claude-opus-5-5 · stage-start at commit 938c9a7 (19.11.2026 19:41 UTC), interrupted with no output; resumed at commit b6074fb · unattended autopilot run (AUTO mode of `prompts/RUN_learning.md`).

**Scope resolution.** `latest` has two readings in this step, because coverage needs no hindsight and source accuracy does:
- **Coverage trend (task 1) and harvester health (task 4):** edition **03** (state date 16.11.2026), the latest closed edition. Editions **02** and **01** are the comparison points; a trend needs more than one edition.
- **Source track record (task 2) and blind spots (task 3):** edition **02** (state date 07.10.2026), the same reading as L1, L2 and L3 in this folder. Edition 03 claims are 0–6 weeks old and mostly cannot be checked yet.

**Versions** (`registry/editions.csv`, `provenance.md` of each edition, `02_harvest/manifest.json`):

| Edition | State date | Window | Framework | Harvester | Methodology | Model | Harvester config |
|---|---|---|---|---|---|---|---|
| 01 | 23.09.2026 | to 23.09 | 1.0.0 | none (web search only) | v1.0 | not recorded | — |
| 02 | 07.10.2026 | 23.09–07.10 (15 days; harvester from 05.10) | 1.4.0 (stage E 1.6.0) | 1.4.0 | v1.0 | claude-opus-5-5 | hashes feeds 4bcf8bb4, keywords 69d835ce |
| 03 | 16.11.2026 | 07.10–16.11 (41 days) | 1.8.0 | 1.4.0 | v1.0 | claude-opus-5-5 | **identical hashes**: config unchanged since the repair of 05.10.2026 |

Editions 02 and 03 ran under different framework versions (1.4.0 vs 1.8.0) but the same harvester version, the same harvester configuration and the same model. The changes 1.5–1.8 touched forecasting, autopilot and publication, not stage 02 or the harvester. The coverage comparison is therefore like with like, except that the edition 03 window was 2.7 times longer.

**Read-only.** No edition file, fact record, registry row or configuration file was changed (learning rule 4). Proposals are listed in §5 for L5 and the next `/gH repair`.

---

## 1. Coverage trend

### 1.1 Table

Sources: `02_harvest/coverage.md`, `manifest.json` and `harvest_notes.md`; the "Coverage" sections of `02_facts/G1–G4.md`; `08_quality_control.md` items 7 and 7a. Perspective shares are the stage 08 mechanical counts (tags before any parenthesis). Status and rating distributions were counted by this step from the fact tables (first status token of each record).

| Measure | Ed. 01 | Ed. 02 | Ed. 03 | Direction 02 → 03 |
|---|---|---|---|---|
| Harvested items in window | — | 19,077 (8,336 matched) | 188,978 (83,759 matched) | up ×9.9 |
| Items per window day | — | 1,272 (harvester ran 3 of 15 days) | 4,609 (every day) | up; the late-start gap is gone |
| Languages / countries in the harvest | — | 47 / 103 | 53 / 126 | up |
| Sources with items in window (of 202 enabled) | — | 154 | 143 | **down 11** |
| Western share of harvested items | — | 30% | 26% | down (good) |
| Fact records | 213 | 277 | 218 | down 21% |
| Fact records per window day | — | 18.5 | 5.3 | **down 71%** |
| Records carrying W / W only | 55% / 36% | 52% / 20% | 53% / 30% | flat / **up** |
| Records with more than one perspective | 23% | 43% | 31% | **down** |
| Key events with W, A and T | 15/24 (63%) | 23/30 (77%) | 28/36 (78%) | flat |
| Records resting on a primary source read directly | not recorded | 49/277 (18%) | 48/218 (22%) | up 4 points |
| Reliability A / B / C / D–F (records) | 28 / 127 / 55 / 3 | 54 / 185 / 37 / 1 | 54 / 138 / 25 / 1 | A share 13% → 19% → 25% |
| Status DONE / DECL / DISP | 108 / 89 / 14 | 105 / 139 / 32 | 102 / 89 / 26 | DECL share 50% → 41% |
| Languages opened or searched in stage 02 | not recorded | 14 | 11 | **down** |
| Silent required cells (source universe) | — | 5 | 8 | **up** |
| Silent cells closed by stage 02 | — | 1 closed, 1 partly | 1 closed, 2 partly | flat |
| Flagged concepts (mandatory searches) | — | 3 | 1 (+ 4 thin) | down |

### 1.2 Reading

**Collection improved; use did not.**
- The harvester ran every day of the edition 03 window, at ten times the volume, in more languages and with a lower Western share. The edition 02 late-start weakness (L1 §1) did not recur.
- **Stage 02 did not convert the larger corpus into wider records.** Records per window day fell from 18.5 to 5.3. The share of records with one perspective rose from 57% to 69%. Stage 02 used 11 languages, against 14 in edition 02. No Persian- or Turkish-language page was opened, although the corpus held 5,046 Persian and 5,611 Turkish items (08 item 7a). Stage 08 reached the same conclusion: "the larger corpus did not widen the perspectives of the records that stage 02 wrote" (ASSESSMENT, medium).
- A contributing factor (ASSESSMENT, confidence medium): stage 02 had a fixed budget for a window 2.7 times longer. Edition 03 G1 ran in 17 minutes (provenance) and covered October events "mainly through stage 01 evidence and secondary summaries" (G1 §12).
- **Source quality per record improved.** The A-reliability share rose from 13% (01) to 19% (02) and 25% (03), and the primary-source share from 18% to 22%. Records on DECL fell from 50% to 41%.
- **Three-perspective completeness is flat at 77–78%.** Two of the eight incomplete edition 03 key events repeat from edition 02: the Black Sea ship strikes (A side) and Poland's public finances (W or T side). The third-party front assessment is missing for the third edition running (08 item 7).
- **Silent cells rose from 5 to 8**, and three of the new ones (PL:official, IN:official, TW:official) have a configured source that should not be silent. §4.2 shows why: a harvester defect, not the publishers.

**Verdict:** improving at collection, flat at the key-event level, worse at record breadth. Two editions with a harvester are a description, not a trend (learning rule 2).

---

## 2. Source track record (edition 02)

### 2.1 Refuted or corrected facts from L1

L1 found **0 refuted and 2 corrected** of 20 key facts. Neither failure came from the source:

| L1 item | Record | Source and perspective | Rating then | What failed |
|---|---|---|---|---|
| #8 Dated Brent state value | G2-003 | FRED/EIA dataset (A/1, primary) | A/1 | The report kept the 29.09 value although values for 05–06.10 were in the harvested dataset before stage 03. Handling, not the source |
| #19 "Mecca Alliance" deployment | G1-020 | Al Jazeera (T), Euronews (W), Pakistan FO and Türkiye Today (A) | B/2 | The record had DECL for the deployment; the report wrote it as done. The claim itself also did not hold by 19.11 (§2.2 row 8) |

### 2.2 Party claims that can now be checked

Selection: every DECL or DISP record of edition 02 (G1–G4) in which a government, military, armed group or state medium claimed a fact or a future action, **and** for which a dated later fact exists, from edition 03 records (dated, with URL) or from L1 checks on 19.11.2026. 38 claims were examined; 5 remain undecided. Records with no later evidence were left out (e.g. G1-014 Medina, G1-046 Samoilovka, G1-052 ZNPP, G1-028 Zakharova's threat).

Verdicts: **H** held · **P** partly held · **N** did not hold (refuted, reversed, or not confirmed by the check date) · **U** undecided.

| # | Record | Claimant | Claim (short) | Carried by (type) | Persp. | Rating then | Later evidence (date) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | G1-004 | IRGC Navy | Ships on the "southern route" will be targeted | Shahrara citing Fars (aggregator) | A | C/3 | Attacks continued; IRGC and army claim mines on that route (ed.03 G1-008, 12–17.11) | H |
| 2 | G1-005 | IRGC adviser Naqdi | The strait "is closed" and under full control | Euronews, Arab News citing IRNA/Fars (W) | A | B/2 | Gulf crude exports 82% of pre-war in X (IEA 13.11); about 28–30 US-facilitated transits a day (JMIC) (ed.03 G1-002, G2-004) | N |
| 3 | G1-006 | US (Rubio) | "Almost as much oil flowing out" as before | The Hindu, Euronews (T) | W | B/3 | Same evidence as row 2 | H |
| 4 | G1-009 | US (Pentagon) | Three carriers and two amphibious groups around Iran by end-XI | Al Jazeera citing a US official; WSJ, AP (T) | T, W | B/2 | Three carriers in the Arabian Sea on 16.11 (USNI via ed.03 G1-011) | H |
| 5 | G1-015 | Yemeni government (Reuters sources) | Dhubab and Mocha largely taken | Reuters via Bankier, Meduza (W) | W | B/3 | Dhubab held until 15.11; Mocha not taken (ed.03 G1-018) | P |
| 6 | G1-016 | Houthis (AP) | Dhubab and Bab el-Mandeb retaken; government gains "completely false" | AP via Interfax; Reuters via Al-Monitor (W) | T, W | B/3 | Wrong for Dhubab, right for Mocha (ed.03 G1-018) | P |
| 7 | G1-017 | Houthis (Saree) | Strikes on King Khalid airport, an Aramco refinery and other targets | Yemeni Press (Houthi-loyal), TRT Arabi (state) | A, T | C/3 | Airport hits with deaths confirmed by GACA (G1-018; ed.03 G1-014); refinery part not confirmed | P |
| 8 | G1-020 | Saudi Arabia, Pakistan, Türkiye | Rapid deployment of Pakistani and Turkish forces | Al Jazeera (T), Euronews (W), Pakistan FO (A) | T, W, A | B/2 | Pakistan: "supporting role"; Türkiye ratified only on 06.11; no deployment confirmed (ed.03 G1-019; L1 #19) | N |
| 9 | G1-021 | US (Rubio; Axios) | No US kinetic action against the Houthis | The National (state-loyal UAE), Axios (W) | T, W | B/3 | No US strike on the Houthis to 16.11 (ed.03 stage 01; L1 4.1 #20) | H |
| 10 | G1-031 | Ukraine (Zelensky) | Two Russian drones sank Royad Mammadov | Sofia Globe, Al Jazeera, Kyiv Post | T, W | B/2 | Romania still gives "fire, cause not established"; later pattern supports the claim (L1 §3) | U |
| 11 | G1-033 | Russia (MoD) | Strikes continue on ports and on "ships used to deliver military cargo" | MoD Telegram (official, read directly) | A | C/3 | At least 14 further ship attacks; ships hit include grain carriers; "military cargo" not shown (ed.03 G1-020, G1-021) | P |
| 12 | G1-037 | Poland (MoD); US (Trump) | Base talks "down to technical issues" | TVN24, Defence24 (independent PL) | A, W | B/2 | Pentagon "green light" per the Polish minister; White House decision about 01–04.12 (ed.03 G1-030) | U |
| 13 | G1-039 | Lithuania (Nausėda) | About 1,000 US troops arriving in late X | LRT (independent/public) | A | B/2 | Rotation resumed with "more than 200" troops from 27.10 (ed.03 G1-033) | P |
| 14 | G1-045 | Ukraine (3rd Army Corps) | 176 km² retaken in "Vivaldi" | Kyiv Post, NYT | A, W | B/3 | Later claim 277 km²; no independent measure (ed.03 G1-034) | U |
| 15 | G1-061 | Panama Canal Authority | 33 daily slots from 15.10 | ACP advisory (official, read directly) | A | B/2 | Q-0039 resolved on it (L3 H1) | H |
| 16 | G2-006 | OPEC+ (7) | November output kept at the September level | Vedomosti, RG (state-loyal); W; T | A, W, T | B/2 | December kept at the same level on 01.11 (ed.03 G2-006) | H |
| 17 | G2-012 | US (Bessent) | Iran loaded no crude in IX | Bloomberg, MEE, Euronews Persian | W, T | B/2 | No later export count was read (L1 #9) | U |
| 18 | G2-031 | Ukraine (MoD) | 51% of Russian refining capacity out of action | AP via ABC; Kyiv Independent (W) | A, W | C/4 | Independent estimates about 30% (Reuters) and nearly 40% (Bloomberg) (ed.03 G2-022) | N |
| 19 | G2-033 | Russia (Novak) | Diesel export ban to 31.10; may partly reopen | Interfax (state-loyal), Moscow Times | A, W | B/2 | Partly eased 10.10, producers' ban extended to 31.01.2027 (ed.03 G2-008) | H |
| 20 | G2-040 | China (MOFCOM) | Readout: Kuala Lumpur arrangement to be maintained | Xinhua (state) | A | A/2 | Every suspension renewed on 09–10.11 (ed.03 G2-027) | H |
| 21 | G2-041 | US (Bessent) | Rare-earth suspension covered by the extension | NBC (W) | W, A | B/2 | Legal end 10.11 held; a new text of 09.11 extended it (ed.03 G2-027) | P |
| 22 | G3-007 | US (Bessent) | Truce "extended until Jan. 10" | NBC (W) | W | B/2 | Aligned on 10.01.2027 (ed.03 G2-027, G3-008 – G3-010) | H |
| 23 | G3-016 | Russia (government) | 2027–29 draft budget (defence 17.15 trn RUB) | Fontanka, Kommersant, Vedomosti (state-loyal/independent RU) | A | B/2 | First reading 372–0 (ed.03 G3-016) | H |
| 24 | G3-022 | EU (Coreper) | 1,646 new listings agreed | Euronews (W), Moscow Times (exile) | W, T | B/2 | Council adopted 1,569 + 77 on 12.10 (ed.03 G3-025) | H |
| 25 | G3-023 | TASS (citing an EU source) | Ambassadors approved the "22nd sanctions package" | TASS (state) | A | C/3 | Listing track only; the 22nd package still "in the coming days" on 16.11 (ed.03 G3-025, G3-027) | N |
| 26 | G3-024 | Ukraine (sanctions envoy Vlasiuk) | Two separate tracks: listings and a package | UA.News (independent UA) | T | B/2 | As row 25 | H |
| 27 | G4-003 | Iran (Majlis security committee) | Hormuz not reopened until the "seven conditions" are met | Tasnim, Mehr (state-loyal) | A | B/2 | Same line on 05.11 (Rezaei); not reopened (ed.03 G4-003) | H |
| 28 | G4-005 | Iran (Pezeshkian) | Negotiations with Washington "futile" | Al Jazeera, Arab News (T) | T | B/2 | Doha contacts 28–31.10; Pezeshkian 09.11: "we can negotiate with dignity" (ed.03 G4-001, §1) | N |
| 29 | G4-019 | Russia (Putin, Valdai) | Ready to resume talks "as soon as possible", on Russia's terms | kremlin.ru (official, read directly) | A | A/1 | Witkoff–Putin 21.10; trilateral 10–11.11 (ed.03 G4-015, G4-018) | H |
| 30 | G4-021 | Ukraine (Zelensky) | The US proposes a technical-level meeting | Kyiv Independent, Ukrinform (independent UA) | A | B/2 | Abu Dhabi round 10–11.11 (ed.03 G4-018) | H |
| 31 | G4-022 | Russia (Ryabkov) | "No current plans" for the RU–US–UA format | Interfax, Vedomosti (state-loyal) | A | B/1 | Putin accepted on 22.10 (ed.03 G4-016) | N |
| 32 | G4-023 | Russia (Peskov) | "Retaliation" strikes will continue | Interfax, RBC (state-loyal) | A | B/1 | Grid and energy campaign continued (ed.03 G1 §5) | H |
| 33 | G4-026 | Türkiye and the UN (Bloomberg) | Preparing Black Sea ceasefire talks | Bloomberg via Ukrainska Pravda (W) | T, W | B/2 | Türkiye and Ukraine agreed on 31.10 to work on a grain corridor; no arrangement (ed.03 G2-026) | P |
| 34 | G4-027 | Russia (Ushakov) | Putin–Trump–Xi meeting "in the air" | RBC, Vedomosti, CGTN (state-loyal) | A, T | B/1 | Shenzhen meeting announced on 14.11 (ed.03 G4-025) | H |
| 35 | G4-028 | Hungary; EU | Veto lifted; clusters 2–3 to open | Euronews (W) | W, A, T | B/2 | Opened on 13.10 (ed.03 G4-067) | H |
| 36 | G4-054 | Greenland government | The agreement enters into force after both parliaments and a note | naalakkersuisut.gl (official, read directly) | A | A/2 | Inatsisartut approved on 03.11; Folketing vote set for 19.11 (ed.03 G4-053) | H |
| 37 | G4-080 | China (CPC) | Fifth Plenum on 26–29.10 | Xinhua (state) | A | A/1 | Held (ed.03 G4-027) | H |
| 38 | G1-038 | US (Hegseth) | Resources could shift from Europe to Latin America | Washington Times (W) | W | B/3 | Cut options about 5,000, mostly Germany; no decision (ed.03 G1-032) | U |

Also noted, not tallied: G4-009 (an impeachment motion against Araghchi was registered) is a true fact about a statement; the consequence the report read into it failed (no vote; L1 4.1 #9). Trump's 08.10 pledge of no strike before the elections (lens fact A-03, KA1) failed by one day (L1 4.2). It is not a G record.

### 2.3 Tallies (33 decided claims; 5 undecided)

Overall: **H 20 (61%) · P 7 (21%) · N 6 (18%)**.

**By carrier type** (the outlet or channel the record rests on):

| Carrier type | n | H | P | N |
|---|---|---|---|---|
| Official channel read directly | 4 | 3 | 1 | 0 |
| State or state-loyal media | 11 | 8 | 1 | 2 |
| Independent or exile | 3 | 2 | 1 | 0 |
| Western | 10 | 4 | 4 | 2 |
| Third party | 4 | 2 | 0 | 2 |
| Aggregator | 1 | 1 | 0 | 0 |

**By claimant:**

| Claimant | n | H | P | N |
|---|---|---|---|---|
| US government | 5 | 4 | 1 | 0 |
| Russian government and military | 7 | 5 | 1 | 1 |
| Iranian government, IRGC, Majlis | 4 | 2 | 0 | 2 |
| Ukrainian government and military | 3 | 2 | 0 | 1 |
| Chinese government and CPC | 2 | 2 | 0 | 0 |
| Yemen: government sources and Houthis | 3 | 0 | 3 | 0 |
| Saudi–Pakistani–Turkish alliance | 1 | 0 | 0 | 1 |
| EU institutions | 2 | 2 | 0 | 0 |
| Other governments and bodies (LT, ACP, GL, OPEC+) | 4 | 3 | 1 | 0 |
| State medium's own claim (TASS) | 1 | 0 | 0 | 1 |
| Anonymous-source report (Bloomberg) | 1 | 0 | 1 | 0 |

**By claim type.** This split explains more than either table above:

| Claim type | n | H | P | N | Examples |
|---|---|---|---|---|---|
| Procedural follow-through: scheduled decisions, drafts, readouts, legal steps | 12 | 11 | 1 | 0 | rows 15, 16, 19–24, 26, 35–37 |
| Declared own security action | 7 | 4 | 2 | 1 | rows 1, 4, 8, 9, 11, 13, 32 |
| Stance on negotiation (present intent) | 7 | 4 | 1 | 2 | rows 27–31, 33, 34 |
| Contested facts on the ground (control, damage, territory, labels) | 7 | 1 | 3 | 3 | rows 2, 3, 5–7, 18, 25 |

**Against the admiralty rating given at the time:**

| Rating | n | H | P | N | Held fully |
|---|---|---|---|---|---|
| A/1–A/2 | 4 | 4 | 0 | 0 | 100% |
| B/1 | 3 | 2 | 0 | 1 | 67% |
| B/2 | 17 | 11 | 3 | 3 | 65% |
| B/3 | 4 | 2 | 2 | 0 | 50% |
| C/3–C/4 | 5 | 1 | 2 | 2 | 20% |

### 2.4 Reading

- **The ratings order the outcomes correctly** (A 4/4 held, C 1/5), but the sample is small (n = 33, at most 17 in one cell). The order is confounded with claim type: all four A-rated claims are procedural.
- **The carriers relayed accurately.** In each of the 6 N rows the outlet reported what the claimant said. The failure lies with the claimant or with the content of the claim, not with the outlet. CLAUDE.md rule 3.4 handles this at the fact level ("a statement is a fact about a statement"), and the credibility digit rates whether the statement was made. **No rating tracks whether the content of a party claim is likely to hold.** Contested-fact claims held fully in 1 of 7 cases. Procedural claims held fully in 11 of 12. This matches L3 pattern 2 (no base rate for political statements) and L1 lesson 2. It is a method-level point for L5, not a source rating.
- **Rows 2 and 3 cut against the source ratings.** Naqdi's "the strait is closed" (B/2, via IRNA/Fars) did not hold. Rubio's "almost as much oil flowing" (B/3), the opposing government's claim, was closer to what followed. The digit given to a statement says nothing about which of two opposed statements is right.
- **Yemen** (rows 5–7) produced only partial verdicts on both sides, and the Houthi A-side source (Saba) has failed since 05.10 (§4). Both sides' claims about the front reached the edition only through wires.

### 2.5 Rating changes in `registry/sources.csv` (rule: at least 3 checkable claims per source)

Sources with at least 3 decided claims in §2.2: **Interfax (Russia)** 4 (H 2, P 1, N 1), **Vedomosti** 4 (H 3, N 1), **Euronews** 4 (H 2, N 2), **Al Jazeera** 3 (H 1, N 2).

- **No rating change is proposed.** In all 15 cases the outlet relayed the claimant's statement correctly; every N belongs to the claimant (Ryabkov, Naqdi, the alliance, Pezeshkian).
- **Proposed note text** (notes field only, for the user to approve; old fact records stay unchanged):
  - Interfax (Russia), Vedomosti: "L4 19.11.2026: relayed Russian official statements accurately in 4 of 4 ed.02 checks; content held in 3 of 4 (Interfax) and 3 of 4 (Vedomosti); a reversed stance (Ryabkov 07.10) is a claimant failure."
  - Euronews, Al Jazeera: "L4 19.11.2026: relayed party statements accurately in ed.02; the claims that failed were Iranian and alliance declarations, not the outlet's reporting."
- **TASS** has one decided claim (row 25, N: its own "22nd package" label, attributed to an EU source). That is below the threshold. Record it for the next review.

---

## 3. Blind spots

### 3.1 From the L1 and L3 classifications

- **L1 surprises (edition 02):** not collected 0 · collected but not used 4 · used but misjudged 3 · not collectable 3. There are also 3 within-window facts that were missed although the items were collected.
- **L3 causes (10 misses):** "not collected" 0 · "collected but not used" 2 (secondary) · "source bias" 3 (M1 primary; M5, M9 secondary).

**The harvester collected the signal in every knowable case.** What failed was the route from the corpus to a fact record, through the keyword concepts and digest ranking, the stage 02 time budget and the stage 03 question selection. The checks below were run on the local corpus (`python3 -m tools.harvester search … --limit 5000`):

| Missed item (source in L1/L3) | Items in corpus (window) | Matched to a concept | In the digest | What was missing |
|---|---|---|---|---|
| Poland's Constitutional Tribunal conflict (L1 #1; L3 M3) | 8 items with "Trybunał", 23.09–07.10; 447 in 07.10–16.11 | 0 of 8 to `poland_security` in ed.02; 52 of 447 (12%) in ed.03 | ed.02 G4: 1 line; ed.03 G4: 2 lines | **No concept for Polish rule of law, the judiciary or presidential vetoes.** `poland_security` matches only via names (Nawrocki, Tusk). S&P named "polarisation and presidential vetoes" in its 06.11 outlook change (L3 M3) |
| Vučić resignation and the Serbian snap election (L1 #2) | 13 items with "Serbia", 23.09–07.10 | 2 to `elections` | 0 hits | **No Western Balkans actor in `source_universe.csv` and no Balkan source in `feeds.csv`.** `elections` has "prime minister resign" but no presidential resignation term. The items came only from general outlets (OSW, RFE/RL) |
| Bosnia's general election of 04.10 (L1 within-window) | 24 items with "Bosnia" | 18 to `elections` | not reached a record | Region with no actor row and no PIR. The digest ranks it below the PIR concepts |
| Arrest of former BND chief Hanning (L1 within-window) | 44 items with "Hanning", 23.09–07.10 (TR, VE, DE and others) | no espionage or sabotage concept exists | 1 Russian-language headline in the G4 digest | **No concept for espionage, sabotage or treason in Europe.** The same gap covers the GRU-ordered arson plot in Estonia (L1 #8; ed.03 G1-025) |
| Qatar LNG contract exits (L1 #9) | force majeure in facts; Chinese-bank loan item in corpus (OilPrice 07.10) | `gas_lng` has no "QatarEnergy", "force majeure" or "contract" | facts only | Contract risk had no terms. Poland's LNG contract structure was never a topic |
| Israeli polls (L3 M9: a subset of pollsters used) | `ynet_he` 2,275 items in ed.03; `gd_hebrew` 0 items ever | `elections` has **no Hebrew, Arabic, Persian, Ukrainian or Chinese terms** | — | Hebrew election coverage could not match the concept. The full polling average was not in the record |
| Trilateral reversal signal (L3 M1: Axios item in corpus) | present before the forecasts | matched | in corpus, not read to the forecast date | Not a harvest gap: a reading gap (the stage 04 corpus delta) |
| Polish public finance, W or T perspective (L3 anecdote; ed.02 and ed.03 J.3) | Polish items plentiful | `budgets_debt` | yes | **No W or T source on Polish public finances** in two editions running. Notes from Poland (independent PL) is the only English-language channel |
| TTF, AGSI+, GUS CPI, FAO FFPI (L3 pattern 1a) | none (no dataset) | — | — | **Data type missing:** none of the four series is harvested. AGSI+ is configured but has no API key. Resolutions were read by hand from Investing.com (5 rows), AGSI+ via TASS or ENGIE (3 rows), FAO (3), GUS (2) |

### 3.2 Concepts in `keywords.csv`

**No concept was without a fact record.** In both editions every one of the 35 concepts produced at least one record (G1–G4 coverage sections). The problems are in precision and recall within concepts:

- **False matches:**
  - `currencies_payments`, en term `swift`: of 56 items containing "swift" in the edition 03 window, at least 17 are Taylor Swift, "swiftly" or "swifter" (counted by hand from titles). G3 §13 reported the same and recorded no payment item.
  - `elections`, pt terms `lula|bolsonaro`: these put every Brazilian political item into the concept. Brazil supplied 17,189 items in edition 03, the second-largest country, and gave 1 fact URL (g1.globo.com) after the 25.10 runoff.
- **Low recall:**
  - `russia_domestic`: the en terms are foreign-policy names (kremlin, putin, peskov, lavrov), so "the concept's top stories are mostly foreign policy" (ed.03 G4 §16). Domestic repression, regional and elite items need their own terms.
  - `elections`: no he, ar, fa, uk or zh rows; no presidential resignation.
  - `poland_security`: no judiciary, veto or rule-of-law terms.
- **Topics that produced facts but had no concept:**
  - Polish Tribunal crisis (ed.03 G4-049)
  - Serbian election (ed.03 G4-039)
  - Kraków terrorist attack (ed.03 G4-050)
  - Estonia's GRU arson plot (ed.03 G1-025)
  - Hanning arrest (ed.02, missed)
  - Orlen–QatarEnergy contract termination (ed.03 G2-014). `gas_lng` matches it only through "lng".

### 3.3 Actor, language, region and data type missing

- **Region:** the Western Balkans (Serbia, Bosnia, Kosovo). There is no actor row and no source.
- **Actor (official):**
  - Saudi Arabia and Japan official: silent in both editions, no harvestable source (spa.gov.sa is JavaScript-only; mod.go.jp returns 403).
  - Poland, India and Taiwan official: configured, but silent because of the page defect (§4.2).
  - Romanian, Bulgarian and Estonian official channels: absent while the Black Sea and Baltic incidents grew (stage 02 proposals of 08.10 and 17.11 are still unprocessed).
- **Language:** Persian and Turkish are harvested at about 5,000 items each but were not opened in edition 03 stage 02. Hebrew has a working RSS source but no election terms, and its GDELT query never produced an item.
- **Data type:** gas storage, TTF, the euro-area HICP flash, Polish CPI, the FAO index and the PortWatch days lost to quota (13 of 41 days harvested in edition 03).

---

## 4. Harvester health

### 4.1 Failing for more than one edition

| Source | Ed. 02 status | Ed. 03 status | Effect |
|---|---|---|---|
| `agsi_eu`, `agsi_de`, `agsi_pl` | skipped (no API key) | skipped (no API key) | Gas-storage questions resolved via TASS, ENGIE or GEF; 3 resolution rows |
| `eia_brent`, `eia_us_crude_stocks` | skipped (no key) | skipped (no key) | Brent only as FRED spot; the ICE settlement read by hand on Investing.com |
| `firms_gulf`, `firms_ru_west` | skipped (no key) | skipped (no key) | No fire or strike context |
| 15 GDELT queries (`gd_arctic`, `gd_chips`, `gd_hebrew`, `gd_japan_ja`, `gd_korea_ko`, `gd_latam_es`, `gd_poland_pl`, `gd_sahel_fr`, `gd_sanctions`, `gd_sudan_horn`, `gd_talks`, `gd_tariffs`, `gd_turkey_tr`, plus `gd_hormuz_ar` and `gd_lng`, which recovered in ed.03) | throttled, 0 items | 13 of them still at 0 items ever | The Hebrew, Japanese, Korean, Polish, Turkish and Spanish discovery queries have never worked |
| 6 more GDELT queries (`gd_brazil_pt`, `gd_caucasus`, `gd_china_economy_zh`, `gd_india`, `gd_iran_domestic_fa`, `gd_russia_economy_ru`) | last success 05.10 | last success 05.10 | Frozen since the first sweep |
| `isw` | failing (HTTP 403) | failing (HTTP 403; one success on 23.10) | Front assessment read through secondary reports in three editions running (08 item 7) |
| `saba_ye` | failing (HTTP 403) | failing (HTTP 403 since 05.10) | YE:state_loyal is now a silent cell; Saree statements came via aggregators |
| `telesur_en` | skipped (robots.txt) | skipped (robots.txt) | VE state voice; respect robots: disable |
| `portwatch` | ok | retrying (ArcGIS HTTP 429); 13 of 41 days harvested | Stage V could not confirm Q-0079 (AUTOPILOT_INBOX 17.11); Hormuz and Bab el-Mandeb resolutions depend on it |
| `presstv` | ok | failing since 10.11 (TLS hostname mismatch) | New in ed.03; the fact records already cite presstv.co.uk |
| `tasnim_en`, `tasnim_fa` | retrying ("no items parsed") | ok, but "no items parsed in recent sweeps" (harvest notes) | Intermittent |

### 4.2 A harvester defect behind the silent official cells

All 12 watched pages (`kind = page`) have produced **exactly one item each in the whole corpus**, from October to November: `prezydent_pl`, `nato_news`, `mea_india`, `mofa_tw`, `mofcom_en`, `fmprc_en`, `fmprc_zh`, `mid_ru`, `kcna_kp`, `ofac_recent`, `isw` and `chinadaily_world` (count of `"kind": "page"` items in `data/harvest/items/2026-10` and `2026-11`).

Cause, read from the code (not changed):
- `tools/harvester/adapters.py` `run_page` gives each page change the URL `<page>#change-<hash>`.
- `store.item_id` hashes `store.canonical_url`, which drops the URL fragment (`urlunparse(…, '')`).
- So every later change of the same page gets the same item ID and is discarded as already seen.

Effect:
- PL:official, IN:official and TW:official count as silent cells, and NATO:official and CN:official as near-silent (1 item), although their pages are fetched successfully on every sweep.
- Stage 02 had to read these channels by hand. The Tribunal crisis "reached only through Polsat, TVN24, Euronews" (CHANGELOG proposal, 17.11), and MOFCOM Announcement No. 58 reached the edition through Chinese press.
- The defect explains 3 of the 3 new silent cells in edition 03.

**This is a code fix (`tools/`), outside L4's configuration scope. It goes to L5 as the highest-value harvester change.** No configuration change can work around it.

### 4.3 Sources with items but no fact-record URL in editions 02–03

Method: the URL domains of all 495 fact records of editions 02 and 03 were counted and matched to the feed domains. A source can still have supplied a lead that was then cited at its origin, so a zero is a candidate for review, not a verdict.

| Source (ed.03 items) | Fact URLs, eds 02–03 | Proposal |
|---|---|---|
| `g1` (15,466) | 1 | Lower volume: the Brazil election is over; keep a politics-only feed or a longer interval |
| `yle_news` (1,668) | 0 | Drop candidate (Finnish; W) |
| `faz_politik` (1,383) | 0 | Drop candidate (W; DE covered by `dw_en` and `spiegel_ausland`) |
| `mediazona` (635), `nhk_intl` (98), `peoples_daily_cn`/`_en` (150) | 0 | Keep: they fill actor cells (RU independent, JP, CN state); low use reflects the stage 02 language range |
| `bbc_hindi` (616), `bbc_turkce` (462), `bbc_arabic` (541), `bbc_persian` (532) | 2 for all BBC domains | Keep Persian and Turkish (W voices in actor languages; QC proposal 5); review Hindi |
| `splash247` (442), `dailysabah` (223), `twz` (183), `warontherocks` (169), `crisisgroup` (49), `bruegel` (10), `un_news` (264), `iaea_news` (54), `addisfortune` (51), `africareport` (243), `dabanga` (104), `lngprime` (242), `dod` (70) | 0 | Review at the quarterly review; no drop on two editions. `iaea_news` and `un_news` are T sources for ZNPP and Sudan, kept for that reason |

### 4.4 Sources with high use (keep and protect)

Fact-record URLs in editions 02–03: Anadolu `aa.com.tr` 44 · Al Jazeera 34 (+3 Arabic) · The National 21 · TASS 19 · Ukrainska Pravda 18 · Interfax 18 · gCaptain 18 · Bankier 17 · Arab News 17 · Euronews 16 · RFE/RL 15 · Moscow Times 15 · Vedomosti 14 · Meduza 14 · CNBC 14 · TVN24 13 · Al-Monitor 13 · Federal Register 11 · Ukrinform 10 · Kyiv Independent 10.

Notes:
- TASS is on `no_republish.txt` yet is the fourth most used source, as the Russian A-side of statements. Keep it for that role only, paraphrased.
- `aa_en`/`aa_tr` (TR state) are the most used source of all and carry most T-perspective tags for Black Sea and Gulf events. A break in them would remove the main T channel.

### 4.5 Dataset feeds that resolved registry questions

| Feed | Questions resolved (registry) | Status |
|---|---|---|
| `portwatch` | Q-0037, Q-0078, Q-0079 (the last disputed by stage V because of the 429 gap) | retrying; protect |
| `nbp_eurpln` / NBP API | Q-0052, Q-0086 | ok |
| `ofac_recent` (page) / `ofac_sdn` | Q-0060, Q-0061, Q-0091 | page affected by §4.2; resolutions read by hand |
| `fedreg_bis` | Q-0102 | ok |
| `cbr_keyrate` / Bank of Russia | Q-0020, Q-0088 | ok |
| Not harvested, read by hand | TTF and Brent (Investing.com, 5 rows), AGSI+ (3), FAO (3), e-petrol (2), GUS (2), ACP (2), USNI (fleet tracker) | candidates in §5 |

---

## 5. Proposals (configuration level)

These are patch-level changes for L5 and the next `/gH repair`. None is applied here. Each "add" needs robots.txt and terms checks in the repair (CLAUDE.md §6).

### 5.1 `sources/harvest/keywords.csv`

| ID | Change | Evidence |
|---|---|---|
| K1 | **Add** to `poland_security` (or a new concept `pl_rule_of_law`, groups G3,G4, vectors DOM,FIN, PIR-6, PIR-7): pl `trybunał konstytucyjny|trybunał|krs|sąd najwyższy|praworządn|weto|zawetow|wotum nieufności`; en `constitutional tribunal|constitutional court|rule of law|presidential veto` | §3.1 row 1: 12% concept recall in ed.03 and 0 of 8 in ed.02; L1 #1, L3 M3 |
| K2 | **Add** a concept `western_balkans` (G4; DOM, DIP; PIR-7): en `serbia|serbian|vučić|vucic|bosnia|republika srpska|dodik|kosovo|montenegro|north macedonia|albania`; ru `серби|вучич|босни|косово`; sr `srbij|vučić|izbor|ostavk`. **Add** to `elections` en `president resign|resigns as president|snap election|early election|caretaker government` | §3.1 rows 2–3; L1 #2 and within-window facts |
| K3 | **Fix** `currencies_payments` en: replace `swift` with `swift system|swift network|swift messag|swift payment|from swift$|to swift$` | §3.2: at least 17 of 56 false matches |
| K4 | **Add** a concept `sabotage_espionage` (G1,G4; MIL, DOM; PIR-1, PIR-2): en `espionage|spying for|sabotage|arson attack|treason|gru$|fsb$`; de `spionage|landesverrat|sabotage|brandanschlag`; pl `szpieg|dywersj|sabotaż|podpaleni`; ru `шпионаж|диверси|госизмен|поджог`; et and lv terms to be added in repair | §3.1 row 4; L1 #8 and the Hanning miss |
| K5 | **Add** to `gas_lng`: en `qatarenergy|force majeure|lng contract|long-term contract`; pl `kontrakt lng|katar|umowa na dostawy lng` | §3.1 row 5; L1 #9 |
| K6 | **Add** `elections` rows for he (`בחירות|סקר|מנדטים`), ar (`انتخابات`), fa (`انتخابات`), uk (`вибор`), zh (`选举`) | §3.1 row 6; L3 M9 |
| K7 | **Rebalance** `russia_domestic` en: add `repression|foreign agent|treason case|arrested|governor|duma election|regional election`; ru `иноагент|госизмен|арестован|губернатор`; keep the name terms but they no longer carry the concept alone | §3.2; ed.03 G4 §16 |
| K8 | **Narrow** `elections` pt: replace `lula|bolsonaro` with `lula eleição|bolsonaro eleição|segundo turno|tse` (or remove the name terms now that the runoff is over) | §3.2; §4.3 g1 row |

### 5.2 `sources/harvest/feeds.csv`

| ID | Change | Evidence |
|---|---|---|
| F1 | **Disable** the 13 GDELT queries that have never returned an item. **Raise** `interval_h` of the remaining GDELT queries (for example to 24) so that the shared host budget reaches them. Replace the actor-language discovery they were meant to give with RSS where it exists (K6 and the Hebrew, Japanese and Turkish feeds already harvested) | §4.1: 15 queries at 0 in ed.02, 13 still at 0 in ed.03 |
| F2 | **Disable** `telesur_en` (robots.txt) and record VE:state_loyal as covered by `granma` (CU) only for Cuba. Find a robots-compliant Venezuelan state source in repair or record the gap | §4.1 |
| F3 | **Replace** `saba_ye` (HTTP 403 since 05.10): test 21sept.net or ypagency.net (CHANGELOG proposal 17.11) after a robots and sanctions check; if sanctioned, add to `no_republish.txt` | §4.1; YE silent cell |
| F4 | **Fix** `presstv` (TLS hostname mismatch since 10.11): test presstv.co.uk, which the fact records already cite | §4.1 |
| F5 | **Replace** `isw` (403 in three editions): test the criticalthreats.org listing (where L1 found the ISW text of 02.10) as kind=page. Until §4.2 is fixed it yields at most one item; record the front-assessment gap as standing | §4.1; 08 item 7 |
| F6 | **Add** the unprocessed stage 02 proposals from `CHANGELOG.md` "Proposed sources" that answer §3 blind spots: Romanian MoD/RNA, Bulgarian government and Estonian government press; Taiwan MND press-release list; MOFCOM announcements; NBP and MPC releases; minfin.gov.ru; BOFIT Weekly; Federal Register presidential documents; Qatar and Oman MFA; Folketing and ina.gl. **Note:** every page-type addition yields at most one item until the §4.2 defect is fixed, so prefer RSS where the publisher has one | §3.3; CHANGELOG 08.10 and 17.11 |
| F7 | **Add** one Western Balkans source pair: an independent regional outlet (Balkan Insight, already cited once in the facts) and one Serbian outlet, subject to robots checks | §3.1 row 2 |
| F8 | **Lower volume** of `g1` (longer interval or a politics-only feed). **Drop candidates** for the quarterly review: `yle_news`, `faz_politik` (0 fact URLs, about 3,000 items) | §4.3 |

### 5.3 `sources/harvest/datasets.csv`

| ID | Change | Evidence |
|---|---|---|
| D1 | **Add** a TTF front-month daily series from a source whose robots.txt allows it (the CHANGELOG proposal of 08.10 is still open) | 5 resolution rows read by hand; L3 pattern 1a; QNT needs it |
| D2 | **Add** the Global Energy Flow storage page as an AGSI+ fallback (CHANGELOG 17.11), until the user sets `AGSI_API_KEY` | 3 resolution rows via TASS or ENGIE |
| D3 | **Add** the EC Weekly Oil Bulletin (CHANGELOG 17.11), the Eurostat HICP flash, the GUS CPI flash and the FAO Food Price Index release | L3 pattern 1a: none of TTF, AGSI+, GUS CPI or FAO FFPI is harvested; ECO and ENE threshold questions |
| D4 | **Lengthen** the `portwatch` interval and its retry window (configuration). Per-minute 429-aware backoff in `net.py` is code and goes to L5 | 13 of 41 days harvested; Q-0079 disputed |

### 5.4 `sources/harvest/source_universe.csv`

| ID | Change | Evidence |
|---|---|---|
| U1 | **Add** actors RS (Serbia; priority 3; independent_exile, third) and RO, BG, EE (priority 3; official) | §3.3 |
| U2 | **Annotate** SA:official and JP:official in `notes`: "no harvestable source (JS-only or 403); stage 02 reads by hand". The cell stays required, so that the gap remains visible | Silent in both editions; CHANGELOG 05.10 open item (1) |

### 5.5 `sources/source_map.md`

| ID | Change | Evidence |
|---|---|---|
| M1 | **Add** a Persian- and Turkish-language reading list for PIR-5 key events, from sources already harvested (Tasnim FA, BBC Persian, Iran International; AA TR, BBC Türkçe) | 08 ed.03 proposal 5; §1.2 |
| M2 | **Add** a "Polish public finance: W and T" row (rating-agency releases read at source; Reuters/Bloomberg Poland coverage; IMF Article IV) | Missing W or T in eds 02 and 03 (J.3); L3 M3 |
| M3 | **Amend** the PIR-1 T section: no harvested T source gives a quantitative front assessment. Record "T front assessment: standing gap" once rather than as a new finding each edition, and list the DeepState vs ISW methods note | 08 item 7 three editions running |
| M4 | **Add** to "Practical rules" (wording for L5 to judge; it touches method, not configuration): "A party's claim about contested facts on the ground (control, damage share, closure, a package label) is recorded with its counter-claim, and stays DECL until a non-party measure exists" | §2.3: contested-fact claims held fully in 1 of 7 |

### 5.6 For L5 (outside the configuration scope of L4)

1. **Code:** include the URL fragment, or a change hash, in `item_id` for `kind = page` items (`tools/harvester/store.py` / `adapters.py`). Add a selftest case for two successive changes of one page. This is the single cause of three silent official cells (§4.2).
2. **Code:** GDELT and ArcGIS 429-aware backoff (CHANGELOG 05.10 open item 2; §4.1).
3. **Method:** a claim-type flag for DECL records (procedural / declared action / stance / contested fact) with a follow-through base rate per type. Evidence: §2.3 (12 / 7 / 7 / 7 claims) together with L3 pattern 2 and L1 lesson 2.
4. **Process:** stage 02's budget does not scale with the window. Records per window day fell by 71% when the window grew 2.7-fold (§1.2). Either keep windows at 2 weeks or scale the stage 02 budget.
5. **User action** (not a proposal): set `AGSI_API_KEY`, `EIA_API_KEY` and `FIRMS_MAP_KEY` in `.env`. They have been missing since 05.10.2026; 7 datasets are skipped and 3 resolution rows rest on secondary carriers.

---

## 6. Summary

| Item | Finding |
|---|---|
| Coverage trend (ed.02 → ed.03) | Harvest ×9.9 items, 47 → 53 languages, Western item share 30% → 26%; three-perspective key events 77% → 78%; primary share 18% → 22%; records per window day 18.5 → 5.3; single-perspective records 57% → 69%; stage 02 languages 14 → 11; silent cells 5 → 8 |
| Source track record (ed.02, 33 decided party claims) | Held 20, partly 7, not held 6. Procedural claims 11 of 12 held; contested-fact claims 1 of 7 held. A-rated claims 4 of 4 held, C-rated 1 of 5. Every failure is the claimant's; the carriers reported accurately |
| Rating changes | None; note text proposed for Interfax, Vedomosti, Euronews and Al Jazeera |
| Blind spots | No concept for Polish rule of law, Western Balkans, espionage and sabotage, or LNG contract risk; no Hebrew election terms; no harvested TTF, AGSI+, GUS CPI or FAO series |
| Harvester health | 12 watched pages produce one item each because of an ID defect; 13 GDELT queries never produced an item; ISW, Saba and teleSUR failing in both editions; 3 API keys missing; PortWatch quota gaps |

### The three most important lessons

1. **The bottleneck is between the corpus and the record, not at collection.** Every knowable miss in L1 and L3 was in the corpus. Edition 03 harvested ten times more but wrote 71% fewer records per window day, with narrower perspectives and fewer languages. Configuration can fix recall: K1, K2, K4–K6 route the missed topics into the digests. The record breadth needs a process change (L5 item 4).
2. **Three of the eight silent cells are a harvester defect, not missing sources.** The page adapter's item ID drops the change marker, so each official page has yielded one item ever. One code fix (L5 item 1) reopens PL, IN and TW official, and NATO and CN official, without any new source.
3. **Source ratings did their job; claim types did not have one.** Carriers relayed party statements accurately, and the admiralty order matched outcomes (A 4 of 4 held, C 1 of 5). What failed were contested-fact claims and present-intent stances (held fully in 5 of 14), which the rating system does not grade. This is the source-side view of L3 pattern 2 and belongs to L5 as a method question (item 3), not to `registry/sources.csv`.

Small samples throughout (one edition of claims, 33 decided; two harvested editions). Per learning rule 2, these are descriptions, not rules.

---

## 7. Process notes

- **Provenance:** `stage-start L4 --arg latest` (19.11.2026 19:41 UTC, commit 938c9a7). The first session was interrupted with no output. `stage-resume L4 --arg latest --model "claude-opus-5-5"` at commit b6074fb, then this file, `stage-end L4 --arg latest`.
- **Read:**
  - L1, L2 (scope and versions only) and L3 of this folder.
  - `registry/editions.csv`, `registry/sources.csv`, `registry/resolutions.csv`.
  - `02_harvest/coverage.md`, `sources_health.md`, `harvest_notes.md` and `manifest.json` of editions 02 and 03.
  - The fact tables and Coverage sections of `02_facts/G1–G4.md` of editions 01–03.
  - `08_quality_control.md` items 7 and 7a of editions 01–03.
  - `sources/harvest/keywords.csv`, `feeds.csv`, `datasets.csv`, `source_universe.csv` and `CHANGELOG.md`, and `sources/source_map.md`.
  - `tools/harvester/adapters.py` and `store.py` (read only, for §4.2).
- **Counted by one-off commands** (not saved in the repository): fact-table status and rating distributions; fact-record URL domains; corpus searches (`python3 -m tools.harvester search` for "Trybunał", `poland_security`, "Serbia", "Vučić", "Bosnia", "Hanning", `elections` and `currencies_payments`, with `--limit 5000`); `"kind": "page"` items in `data/harvest/items/2026-10` and `2026-11`.
- **Web:** none in this step. The claim verdicts rest on edition 03 fact records (dated, with URL) and on the L1 checks of 19.11.2026. No forecasting service or market was visited or searched, and no benchmark value is used.
- **Gaps:**
  - The 5 undecided claims (§2.2) and the claims left out for lack of later evidence were not web-checked.
  - The "Western share of records" for edition 03 uses the stage 08 count (53%). This step's own count, which includes tags inside parentheses, gives 60%.
  - §4.3 matches by URL domain and undercounts sources used only as leads.
  - The "swift" false-match count is a lower bound from titles.
- No instruction-like content was found in harvested items or files read.

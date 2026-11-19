# L1 — Hindsight audit of reports (scope `latest`)

Run: 19.11.2026 · stage L1 · framework 1.9.2 · methodology v1.0 · model claude-opus-5-5 · commit at start 1ffa40a · unattended autopilot run (AUTO mode of `prompts/RUN_learning.md`).

**Scope resolution.** `latest` was resolved to **edition 02** (state date 07.10.2026, 43 days before this audit). The latest closed edition, edition 03 (state date 16.11.2026), is only 3 days old and fails the L1 rule "state date at least 14 days in the past" (`prompts/learning/L1_hindsight.md`). It is not audited here. It is used only as a **dated source of hindsight facts** for edition 02: its `02_facts/G1–G4.md` records (each with date, publisher, URL and rating) and its `03_analysis.md` §1.2–1.3, which judged the edition 02 assessments as of 16.11.2026. Other steps of this review (L2–L4) may define `latest` differently. That choice is for them to make, and this folder does not change it.

**Hindsight evidence.** Where this file uses facts from after 07.10.2026, it gives their date and the record ID in edition 03 (`ed.03 G1-0xx` etc., with the full URL in that record) or a URL checked on 19.11.2026. "Knowable at the state date" means the evidence was public on or before 07.10.2026 (stage 02 ran 07–09.10, stage 03 on 09.10). Learning rule 3 applies: a miss caused by information that did not yet exist is not an analytic error.

**Read-only.** No edition file, fact, forecast or registry row was changed. Corrections to past facts are recorded only here (learning rule 4).

---

## 1. Scope and versions

| Edition | State date | Framework | Methodology | Models | Forecasts frozen | Report commit | Harvest manifest | Audited here |
|---|---|---|---|---|---|---|---|---|
| 02 | 07.10.2026 | 1.4.0 (stages H, 00–08); 1.6.0 (stage E, 19.10) — **mixed edition** per `provenance.md` | v1.0 | claude-opus-5-5 (all stages) | f09a1d4 (09.10.2026) | 1bd6f1b (`registry/editions.csv`); stage 07 started at 75c4c51 | 1cc45e059fd2c8d1 | **yes** |
| 03 | 16.11.2026 | 1.8.0 | v1.0 | claude-opus-5-5 | 7840589 (18.11.2026) | a78df5d | 1f032123aa6fb006 | no — less than 14 days old; used only as a hindsight source |

Conditions of edition 02 that matter for this audit (from its `log.md`, J.5 of its report and `provenance.md`):
- The harvester started late, on 05.10.2026. About 70% of the harvested items are dated 05–07.10 and about 8% are dated 23.09–01.10. For the first week of the window the edition relied on web search and dataset back-fill.
- Stage 02 G3 hit a tool limit and was continued on 09.10. Stage 06 was continued on 10.10.
- No AGSI+ key. ICE, ICE Endex, centcom.mil and ukmto.org returned HTTP 403, and IAEA returned HTTP 402.
- The stage E part of the edition ran under framework 1.6.0 and does not affect sections A–K of the report.

---

## 2. Facts that did not hold

Selection: 20 facts from edition 02 that carried the conclusions (PIR-linked; used in the executive summary, the scenarios of H.1 or the key assumptions KA1–KA8), followed by every DISP record or two-interpretation item. "Perspective relied on" is given only for corrected or refuted facts.

### 2.1 The 20 key facts

| # | Edition 02 fact (record) | Verdict on 19.11.2026 | Evidence (date, source) | Perspective relied on (if corrected/refuted) |
|---|---|---|---|---|
| 1 | PortWatch: 0–5 AIS transits a day in Hormuz, 23.09–04.10 (G1-001) [A/2] | **Confirmed** | The series stayed at the floor: 0–8 a day to 08.11 and 1–6 a day for 09–15.11 (ed.03 G1-001; ed.03 03 §1.7) | — |
| 2 | At least 10 tankers struck in and near Hormuz, 01–06.10; UKMTO and JMIC name no attacker (G1-002) [B/2] | **Confirmed**; attacker **still disputed** | Attacks continued (ed.03 G1-003, G1-008). From 12–17.11 the IRGC and Iran's army claim mines on the "southern route" while UKMTO reports "unknown projectile" (ed.03 G1-008; Shafaq News 17.11, https://shafaq.com/en/World/Tanker-explodes-in-Hormuz-another-burns-off-Oman) | — |
| 3 | IRGC Navy route rule of 05.10 (G1-004) [C/3] | **Confirmed** (as a statement) | It evolved into claimed mining of the "US-created southern route" (ed.03 G1-008); Ghalibaf (XI): Hormuz "will never return" to its prior status (ed.03 G4-004) | — |
| 4 | US blockade: 130th vessel redirected, 3 disabled and 13 destroyed in 12 weeks (G1-007) [B/2] | **Confirmed** | The blockade continued; a cargo ship was disabled on 07.11 (ed.03 G1-009) | — |
| 5 | Third carrier group ordered; three carriers and two amphibious groups around Iran by end-XI (G1-009) [B/2] | **Confirmed** (the declaration became a fact) | Three carriers in the Arabian Sea on 16.11 (USNI via ed.03 G1-011) | — |
| 6 | No US strike on Iranian land since 01.09 (G1-010; stage 01) | **Confirmed** for the state date; overtaken later | First strikes on Qeshm on 02.11 and 06.11 (ed.03 G1-005; Al Jazeera 07.11, https://aljazeera.com/news/2026/11/7/trump-confirms-new-us-strikes-on-irans-qeshm-island). No earlier October strike was found (IBTimes 03.11 names none) | — |
| 7 | December Brent settled at 100.20 USD/bbl on 07.10 (G2-002) [B/2] | **Confirmed** (not re-read at ICE) | No contrary settlement found; ed.03 G2-001/002 continue the same wire series | — |
| 8 | Dated Brent 113.96 USD/bbl on 29.09 (FRED), "spot 13–20 USD above futures" (G2-003; report D, L) | **Corrected (stale state value)** | The 29.09 value is unchanged in the harvested series. But FRED values for 05.10 (125.51) and 06.10 (125.44) were in the harvest corpus from 08.10 11:17 UTC, before stage 03 (09.10) and stage 07 (10.10). 07.10 was 126.00 (fetched 19.10), and 02.10 was 135.51 (fetched 11.10) (`data/harvest/datasets/observations.jsonl`, `fred_brent`). The spot–futures gap on the state date was about 25 USD, not 13–20 | A/1 dataset (FRED/EIA). The error is a publication lag that the report did not refresh, not a source failure |
| 9 | Iran loaded no crude in September (G2-012) [B/2] | **Still disputed** for later months; September **not contradicted** | No tanker-tracking export figure was read after September. IEA: Iran's supply was 1.86 mb/d in October. CENTCOM: the blockade prevented more than 25 bn USD of exports (ed.03 G2-004, G1-009). The former oil minister's claim (07.10) that sales continued under the blockade was never tested (G4-013) | — |
| 10 | Diesel shortage chain: European diesel at 2.24 EUR/l, G7 release of up to 100 mn bbl, IEA acceleration (G2-008 – G2-011) [B/2] | **Confirmed** | IEA (13.11): diesel is "the main near-term concern", European diesel about 180 USD/bbl (ed.03 G2-004) | — |
| 11 | EU storage 72.83% on gas day 05.10, lowest for the date since 2011 (G2-016) [C/2] | **Confirmed** | Consistent with the later trajectory: peak 74.96% (27.10), 74.6% on 01.11, 70.55% on 14.11 (AGSI+ via GEF, ed.03 G2-012) | — |
| 12 | H.R. 5334 enrolled text: "shall … up to", 30 days, waiver (G3-001) [A/1] | **Confirmed** | EO 14436 (16.10) set and at once waived the duties under the Act (whitehouse.gov via ed.03 G3-001) | — |
| 13 | Truce extended to 10.01.2027; legal end date of the rare-earth suspension still 10.11.2026 (G3-007, G3-010, G2-041) [A/1, B/2] | **Confirmed**; the scope dispute was settled later | MOFCOM/GAC Announcement No. 58 (09.11) continued the suspension to 10.01.2027 (ed.03 G2-027) | — |
| 14 | Russia's 2027–29 draft: defence 17.15 trn RUB, 2026 deficit 3.2% of GDP (G3-016) [B/2] | **Confirmed** | First reading passed 372–0 (Kommersant, ed.03 G3-016). Ministry of Finance: January–October deficit 2.3% of GDP, full-year estimate 3.2% (ed.03 G3-017) | — |
| 15 | Budget-rule FX purchases raised to 12.7 bn RUB a day from 07.10 (G3-019) [B/1] | **Confirmed** | The next period was 15.6 bn RUB a day for 09.11–04.12 (ed.03 G3-019) | — |
| 16 | Putin at Valdai (01.10): terms unchanged; Ryabkov (07.10): "no current plans" for the trilateral (G4-019, G4-022) | **Confirmed** (as statements); the policy reversed later | Witkoff–Putin meeting 21.10; Putin accepted the trilateral on 22.10; Abu Dhabi round 10–11.11 (ed.03 G4-015, G4-016, G4-018) | — |
| 17 | Royad Mammadov sank (Romanian EEZ, 05.10) and Alfa Watan sank and Able set on fire (Bulgarian EEZ, 06.10); 2 dead; no attribution (G1-031, G1-032) [B/2] | **Confirmed**; the cause of the Royad Mammadov sinking is **still disputed** | Romanian authorities still give only a fire as the cause, with the investigation open (gCaptain, https://gcaptain.com/romania-probes-cause-of-black-sea-cargo-ship-sinking/; search 19.11). At least 14 attacks followed, inside Bulgarian territorial waters on 13.10 and Romanian territorial waters on 14.11 (ed.03 G1-020, G1-021) | — |
| 18 | Houthi strikes killed 3 at the Riyadh and Abha airports on 06–07.10 (G1-018) [B/2] | **Confirmed** (not contradicted; not re-read at source) | Later GACA counts were much larger: at least 16 killed at King Khalid airport on 08–11.10 (ed.03 G1-014) | — |
| 19 | The "Mecca Alliance" was "activated on 05.10 with a rapid deployment of Pakistani and Turkish forces" (report, executive summary and B; G1-020) | **Corrected (status overstated)** | The record itself had DONE for the activation but DECL for the deployment, with no size or role given. Pakistan's defence minister described a "supporting role", and the Turkish air-defence details were unconfirmed. Türkiye's parliament ratified the agreement only on 06.11 (ed.03 G1-019). The report turned a declared deployment into an accomplished one | T (Al Jazeera) and A (Pakistan Foreign Office) statements. The report dropped the record's own DECL flag |
| 20 | Polish MoD: US base in western Poland, about 5,000 soldiers, no decision before December (G1-037) [B/2] | **Confirmed** (as a statement), still open | The defence minister says the Pentagon "greenlit" a permanent presence. Candidate sites are Poznań and Wrocław, and a White House decision is expected about 01–04.12. Still based only on Polish ministers (ed.03 G1-030, G1-031) | — |

Other facts that carried an assessment, briefly. All of them hold:
- Coreper agreed 1,646 Russia listings on 07.10 (G3-022). **Confirmed:** the Council adopted 1,569 + 77 under the same regime on 12.10, which makes 1,646 (ed.03 G3-025).
- Impeachment motion against Araghchi registered (G4-009). **Confirmed** as a fact. The reading built on it is refuted: no vote was held and Araghchi leads the regional track (ed.03 G4-009; stage 01 of ed.03, Q-0096).
- OFAC GL 135 on Russian diesel (R-02). **Confirmed:** no cargo had reached a US port by 12.11 (ed.03 G2-007, G2-009).
- Brazil, first round (G4-029). **Confirmed.**
- CPN III caps (G2-026). **Confirmed:** the caps still hold (ed.03 G2-018).
- UST10Y 5.356% intraday (G3-035). **Not re-checked.**

### 2.2 DISP records

| Record | Edition 02 dispute | Status on 19.11.2026 | Evidence |
|---|---|---|---|
| G1-004 | Count of 13 tankers hit in one week (tracking account) | Still disputed (not re-checked) | — |
| G1-006 | Hormuz flow vs AIS counts | Partly settled, see §3 | ed.03 G1-002, G2-004 |
| G1-014 | Houthi hit on a Medina power station (coalition vs Houthi claim) | Not re-checked | — |
| G1-015/016 | Dhubab and Mocha | Settled by time, split verdict, see §3 | ed.03 G1-018 |
| G1-030 | Latvian border incident | Still disputed, see §3 | LSM; Militarnyi; search 19.11 |
| G1-031 | Cause of the Royad Mammadov sinking | Still disputed, see §3 | gCaptain; Romania-Insider |
| G1-034 | Drones and missiles over Moldova (types) | Not re-checked | — |
| G1-041 | Legal effect of the expiry of the FY2026 NDAA EUCOM floor | Still disputed. Edition 03 still cites the 76,000 floor as a constraint (ed.03 KA5) without settling its legal effect | ed.03 03 §1.3 |
| G1-043/044 | Front balance in September | Still disputed (methodology), see §3 | criticalthreats.org 02.10 (via search); ed.03 G1-034 |
| G1-045 | "Vivaldi" counteroffensive, 176 km² claimed | Confirmed in direction: the 3rd Army Corps later claimed 277 km² over four phases (a party's claim) | ed.03 G1-034 |
| G1-047 | Targets of the 07.10 strike | Not re-checked | — |
| G1-052 | Drone hits at ZNPP | Not re-checked (IAEA HTTP 402 in both editions) | — |
| G1-055 | Scarborough airspace (PLA vs AFP) | Not re-checked | — |
| G1-058 | DPRK launch range (700 vs about 1,000 km) | Not re-checked | — |
| G2-013/G4-013 | Oil minister's resignation linked to the blockade | Not re-checked | — |
| G2-018 | EU storage target (90% with 10 pp deviation vs "80%") | Not re-checked; no longer decisive (fill peaked below 75%) | ed.03 G2-012 |
| G2-031 | Ukraine's claim that 51% of Russian refining was disabled | Still disputed. Later estimates: about 30% (Reuters), nearly 40% (Bloomberg), more than 55% (Zelensky) | ed.03 G2-022 |
| G3-014 | Summit readouts (crisis-communication memorandum) | Not re-checked | — |
| G3-023/024 | Whether the 07.10 listings are "the 22nd package" | Settled: interpretation (2), see §3 | ed.03 G3-025, G3-027 |
| G3-053 | Commission refusal to front-load the 90 bn EUR loan (Bloomberg, anonymous) | Not contradicted. The later plan is about 45 bn EUR for 2027 from EU budget headroom (ed.03 G3-051) | ed.03 G3-051 |
| G3-069 | Russia's 2026 deficit: 3.2% (government) vs 4% (BOFIT) | Still disputed until year-end data. January–October 2.3%; the government still estimates 3.2% | ed.03 G3-017 |
| G4-010 | Who authorised the Iranian contacts | Superseded: two lines persist (Pezeshkian vs Rezaei/Ghalibaf) | ed.03 G4-004 |
| G4-015 | Expulsion of Iranian UN delegates (Axios vs Araghchi) | Not re-checked | — |
| G4-020 | Lukoil assets in the US–Russia talks (NYT; Peskov non-denial) | Not re-checked | — |
| G4-041, G4-043 | Kynev arrest; Irkutsk plague case | Not re-checked (no PIR consequence found) | — |
| G4-049 | Content of the reported Trump–Kosiniak-Kamysz meeting | Not re-checked | — |
| G4-062 | Mekelle date (04.10 vs 05.10) | Not re-checked; the war continues (ed.03 G4-057) | — |

**Count.**
- Facts checked: 20 key facts and 12 DISP rows with a status (3 settled, 2 split or partly settled, 6 still disputed, 1 not contradicted). Another 15 DISP rows were not re-checked: they had no PIR consequence, or the source was unreadable.
- Of the 20 key facts, 0 were refuted and 2 were corrected (#8 stale state value; #19 status overstated). That is **10% corrected, 0% refuted**.
- 3 are still disputed in part (#2 attacker, #9 later months, #17 cause).
- The corrected facts did not come from a weak source. In both cases the report's handling of a good record failed: a value was not refreshed, and a DECL flag was dropped.

---

## 3. Disputed events resolved by time

| Edition 02 "two interpretations" item | Closer to reality (on 19.11.2026) | Was the deciding evidence available on 07.10? |
|---|---|---|
| **Who strikes tankers in Hormuz:** (1) Iran/IRGC, implied by the route rule; (2) unattributed | **Still open; moving toward (1) for mines.** Iran's army and the IRGC themselves claimed mines on the southern route in November (ed.03 G1-008). Projectile attacks remain unattributed (UKMTO) | No. The November claims did not exist yet |
| **Front balance in September:** (1) DeepState, Russian net gain of 154 km²; (2) ISW, Ukrainian net gain | **Neither refuted.** The two series measure different things and keep diverging. ISW's own figure (02.10) was a Russian net loss of 80.81 km² (175.18 km² with infiltrations). In October and November DeepState again shows small Russian net gains while ISW shows net losses (ed.03 G1-034) | ISW's primary text was published on 02.10 (criticalthreats.org, via search 19.11) but was unreadable at the state date (HTTP 403), so it was read through secondary reports. The report described the dispute correctly |
| **Royad Mammadov:** (1) two Russian drones (Zelensky); (2) fire, cause not established (Romanian Naval Authority) | **Still officially (2).** The later pattern makes (1) more plausible: Khoryv on 23.10, where President Dan spoke of "a new example of the tragic consequences of Russia's aggression" (Al Jazeera 23.10, https://www.aljazeera.com/news/2026/10/23/romania-blames-russia-after-drone-sinks-ship-in-the-black-sea), and a Russian "Gerbera-2" drone found ashore at Shabla (06.11; ed.03 G1-020). No formal government attribution | No |
| **Dhubab and Mocha:** (1) largely taken by government forces (Reuters sources, 05.10); (2) retaken by the Houthis (AP, 07.10) | **Split.** For **Dhubab**, (1) was closer: the government held it until its withdrawal on 15.11. For **Mocha**, (2) was closer: the October offensive "had retaken Dhubab but not Mocha" (ed.03 G1-018, Al Jazeera, NBC, MEE) | Partly. Reuters on 07.10 called the Mocha claim "premature" and Middle East Eye said the Houthis still held Mocha (G1-016). The report could have split the verdict at the state date |
| **Latvian border incident:** (1) organised criminal group (Latvian border guard); (2) Moscow (Ukraine's FM) | **Still disputed; the official line remains (1).** The Latvian State Security Service opened criminal proceedings on 09.10 for creating a criminal organisation to commit crimes "against peace". A group calling itself "Black Rus" claimed responsibility, and its links are unconfirmed (Militarnyi, https://militarnyi.com/en/news/group-likely-linked-to-belarusian-and-russian-intelligence-claims-responsibility-for-sabotage-on-latvian-border/; Al Jazeera 09.10) | No |
| **Targets of the 07.10 strike:** energy and housing (Ukraine) vs military industry (Russian MoD) | Not re-checked | — |
| **Hormuz traffic (report C):** (1) most flow is AIS-dark, escorted or cleared; (2) the flow estimates overstate traffic | **Closer to (1) in substance.** IEA (13.11): Gulf crude exports were 82% of pre-war in October. JMIC: about 28–30 US-facilitated transits a day vs single digits in AIS. Iraq reports an understanding with the US on a lane (ed.03 G1-002, G2-004, G2-010). Edition 03's red team noted that no source says escorted ships switch off AIS, and that bypass routes also fit the IEA figure | Partly. JPMorgan (98%) and Goldman (about 23 mb/d) were in the record (G2-005), and so was the KPC CEO's "more ships are getting through" (G1-006). The report kept the question open at low confidence, which was appropriate. The misjudgement was in the oil assessment that followed (§4, D) |
| **"22nd package" label (F):** (1) yes, per TASS and News.am; (2) a separate listing track | **(2).** The Council adopted listings on 12.10 with no sectoral measures. On 16.11 Kallas said the 22nd package would be presented "in the coming days" (ed.03 G3-025, G3-027). One law-firm page repeats (1) (McCann FitzGerald, via search 19.11), which appears to be an error | Yes. Euronews and Ukraine's sanctions envoy Vlasiuk (G3-024) |
| **Russia's 2026 deficit:** 3.2% (government) vs 4% (BOFIT) | Open; the government figure is so far consistent with January–October data (2.3%) | No |
| **Rare-earth scope of the truce extension:** (1) covered (US/Western analysts); (2) not covered — legal end 10.11 | **Both partly right.** The legal text did end on 10.11 as (2) said, and Beijing extended it on 09.11 by a new text as (1) expected (ed.03 G2-027) | No. The report correctly flagged the legal gap |
| **28.09 US–Iran contact format; Trump–Kosiniak-Kamysz meeting; EU storage target; NDAA floor** | Not settled or not re-checked | — |

The report's handling of disputes held up. No item it marked as disputed turned out to be one-sided at the state date. One case could have been split earlier: Dhubab vs Mocha.

---

## 4. Assessments and assumptions

### 4.1 ASSESSMENTS with confidence medium or high (report sections A–G, executive summary, J)

Verdicts draw on edition 03's §1.2 (dated 16.11.2026), cross-checked against the records cited. "Held" means confirmed in substance. "Partly" means one component held and one failed.

| # | Section | ASSESSMENT (confidence) | Verdict | Dated evidence | Knowable at 07.10? |
|---|---|---|---|---|---|
| 1 | Exec. summary | Land ceasefire holds; the sea is not quiet; Washington moved the escalation risk to after 03.11 (medium) | **Partly.** The sea part held. The strike came on 02.11, one day **before** the vote, described as "defensive" | Qeshm 02.11, 06.11 (ed.03 G1-005) | The timing turned on a decision not yet taken |
| 2 | Exec. summary / A | Both capitals keep their levers cocked; GL 135 points toward easing toward Moscow (medium) | **Held** | EO 14436 waiver 16.10 (ed.03 G3-001) | Yes (R-02 dated 09.10) |
| 3 | A — USA | Leverage accumulated, use deferred after 03.11; allies asked to carry the costs (medium) | **Held**, with the timing correction of #1. H.R. 5334 was waived, not deferred | ed.03 G1-005, G1-033, G3-001 | — |
| 4 | A — China | The summit turned into a time extension; the raw-materials lever kept legally intact; fronts kept separate (medium) | **Held** | Announcement No. 58 (09.11); 24% tariff suspended for two months only (ed.03 G2-027, G3-010) | — |
| 5 | A — China | Interest in a Hormuz settlement, no visible brokering role (medium) | **Held** | Xi's general statement 02.11 only (ed.03 G4-070) | — |
| 6 | A — Russia | Moscow budgets the war, blocks the trilateral format, keeps a bilateral channel with economic offers (medium) | **Partly.** The budget and bilateral-channel parts held. "Blocks the trilateral" **failed**: Putin accepted on 22.10 and the round was held 10–11.11 | ed.03 G3-016, G4-016, G4-018 | Partly. The 09.10 Putin–Trump call (after the state date, C-01) was the first sign. On 07.10 only Ryabkov's statement existed |
| 7 | A — Russia | Pressure on NATO shifted to the Black Sea and nuclear rhetoric, below Art. 4 (medium) | **Held and strengthened** | ≥14 ship attacks, Romanian territorial waters 14.11; no Art. 4 (ed.03 G1-020, G1-021) | — |
| 8 | A — Iran | Control over others' exports through a clearance regime is Iran's remaining asset (medium) | **Held** (in a new form: claimed mining) | ed.03 G1-008, G4-004 | — |
| 9 | A — Iran | The negotiating mandate is contested; the MFA's commitments are weakened (medium) | **Partly failed.** No impeachment vote; Araghchi leads the regional track. Two lines persist (Pezeshkian vs Rezaei/Ghalibaf) | ed.03 G4-004, G4-009 | Partly. An impeachment motion is a weak signal: no base rate of passage was used |
| 10 | A — EU | Moving from reactive sanctions to defensive trade law; the weak point is money, not will (medium) | **Partly.** Money held as the weak point (2027 loan, MFF). The sectoral 22nd package stalled under unanimity, so "will" in the Council is also a constraint | ed.03 G3-027, G3-051, G3-052 | — |
| 11 | B — Gulf | A war of attrition at sea replaced the land war (medium) | **Failed** (superseded 02.11) | ed.03 G1-005 – G1-007 | No |
| 12 | B — Yemen | The Saudi–Houthi war is a separate front with its own allies (medium) | **Held and strengthened** | Riyadh financial district 08.11; Syria joins; Bab el-Mandeb shore lost 15.11 (ed.03 G1-015, G1-018, G1-019) | — |
| 13 | B — Ukraine | Both sides fight mainly for the opponent's energy system; the line moves little (medium) | **Held** | ed.03 G1-034, G1-037, G1-040 | — |
| 14 | B — Black Sea | Sub-threshold front: deaths in NATO EEZs, no government attribution, no collective trigger (medium) | **Held**, with a nuance. Romania's president blamed "Russia's aggression" for the Khoryv sinking on 23.10, and Bulgaria summoned Russia's ambassador on 13.10. These are political statements, not a formal attribution. Edition 03 says "no NATO government has attributed", which is right only in the formal sense | Al Jazeera 23.10; ed.03 G1-020 | — |
| 15 | B — Baltic/Poland | Russia and Belarus probe with deniable means; Poland answers with capability (medium) | **Held** | GRU-ordered arson plot in Estonia (ed.03 G1-025); no confirmed Polish airspace violation after 23.09 (ed.03 G1-027) | — |
| 16 | D | The futures–physical gap measures what the market expects from diplomacy vs what is flowing (medium) | **Failed in its cause.** The gap closed because physical supply recovered (Gulf crude exports 82% of pre-war), not because of diplomacy | ed.03 G2-003, G2-004 | Partly. The flow estimates (G2-005, G1-006) pointed to recovering exports, and the true gap on the state date was about 25 USD (§2 #8) |
| 17 | D | EU storage reaches the high 70s by 01.11, below 80% (medium) | **Partly.** Below 80% held. "High 70s" failed: 74.6% on 01.11, with a peak of 74.96% on 27.10 | ed.03 G2-012 | The GEF projection assumed a steady injection rate. The rate fell |
| 18 | D | Diesel is the binding shortage (mechanism) | **Held** | IEA 13.11 (ed.03 G2-004) | — |
| 19 | E — Brazil | The 25.10 runoff decides PIR-7's largest orientation change of the quarter (medium) | **Failed in outcome** (Lula 51.79%). Taken literally the claim was an "if" statement, but the report framed a rightward shift as the likely change | ed.03 G4-036 | The first-round polling miss (G4-032) argued for wider uncertainty, not a direction |
| 20 | E — Gulf | Gulf security is regionalising while Washington stays out of Yemen (medium) | **Held** | Türkiye ratified 06.11; Syrian forces to Saudi Arabia; no US strike on the Houthis (ed.03 G1-019; stage 01) | — |
| 21 | E — Lithuania | Flank states compete to host and finance US forces (medium) | **Held** | Romania offers to pay; Lithuania proposes a permanent presence (ed.03 G1-033) | — |
| 22 | E — Germany | Saxony-Anhalt resolution is a regional signal without federal effect (medium) | **Undecided** (not re-checked; no federal change recorded in ed.03) | — | — |
| 23 | E — Hungary/Ukraine | A formal opening of clusters 2–3 needs an IGC (medium) | **Held**: opened on 13.10 | ed.03 G4-067 | — |
| 24 | E — Venezuela | No change in substance (medium) | **Held, weakening.** Machado returned on 25.10; US-sponsored talks; no election date | ed.03 G4-060, G4-061 | — |
| 25 | E — Caucasus | No movement on the treaty (medium) | **Held**: initialled, not signed; the Dublin meeting of 12.11 is declaratory | ed.03 G4-063 | — |
| 26 | F | A synchronised tightening in a stagflation set-up; long yields as a tightening channel (medium) | **Held** | BoE hike to 4.00%; Fed dissents for a hike; ECB debated a hike; UST10Y ≥ 4.84% (ed.03 G3-036 – G3-042) | — |
| 27 | G (all medium) | Map of influence: Russia "gaining" in energy through higher Urals; Qatar "the only active channel" | **Failed for Russia-energy.** Oil-and-gas revenue fell 14% y/y in January–October, and the Urals discount was about 31–33 USD (single source). **Partly failed for Qatar**: mediation moved to Pakistan and Oman, though the Doha contacts of 28–31.10 still used Qatar. The other cells held | ed.03 G3-017, G2-023, G4-001, G4-009 | Partly. Damper payments and the rouble effect were knowable mechanisms; the 05.10 FX-purchase data showed revenue rising |
| 28 | Exec. summary — Poland | In two weeks no factual state deciding between the scenarios changed (medium) | **Held** for the state date | — | — |
| 29 | J.3 | The weakest evidential bases are the parties' battlefield claims and the Hormuz flow estimates (high) | **Held**: both still disputed six weeks later | ed.03 J.1 | — |

**Totals (29 assessments):**
- **Held 19:** #2–5, 7, 8, 12–15, 18, 20, 21, 23–26, 28, 29. #14 has a nuance and #24 is weakening; both count as held.
- **Partly 6:** #1, 6, 9, 10, 17, 27. #27 counts once.
- **Failed 3:** #11, 16, 19.
- **Undecided 1:** #22.

### 4.2 Key assumptions KA1–KA8 (edition 02 `03_analysis.md` §1.3; report K.7)

| KA | Assumption (edition 02 state) | Verdict on 19.11.2026 | Dated evidence | Comment |
|---|---|---|---|---|
| KA1 | No US strike on Iranian land before the 03.11 elections (holds; medium) | **Failed**, by one day | Qeshm 02.11, "defensive strikes" per US officials; 06.11 "minor strikes" (ed.03 G1-005; Stars and Stripes 03.11, https://www.stripes.com/theaters/middle_east/2026-11-03/us-strikes-iran-qeshm-island-hormuz-23348317.html) | The assumption rested on Trump's own statement of 08.10 (A-03) [B/3], a fact about a statement. The mirror test (§1.6 item 3) had flagged it as possible signalling. The red team called the ten forecasts that rested on it one correlated bet |
| KA2 | Tehran's centres block a quick agreement but avoid a full war with the US (holds, second half weaker; low) | **Held; second half eroding** | No agreement; Iranian drones toward US sites in Bahrain on 13.11 and 15.11, intercepted (ed.03 G1-006, G1-007) | The refutation criterion ("IRGC strike on US naval units") was approached but not met: the attacks were intercepted and there were no US casualties |
| KA3 | USA and China prefer extending the truce (holds; medium) | **Held** | Every suspension renewed on 09–10.11 (ed.03 G2-027, G2-032, G3-008 – G3-010) | All three tests named on 07.10 (18.10, 09–10.11, 10.11) passed |
| KA4 | Russia does not cross a NATO-attributed incident with casualties on NATO territory (holds formally; medium) | **Held formally** | Hits inside Romanian territorial waters on 14.11 without casualties; Khoryv death outside 12 nm; no formal attribution (ed.03 G1-020, G1-021) | As edition 02 predicted, the threshold now runs through formal attribution |
| KA5 | Posture review: reduction in Europe, Poland kept or increased (unresolved; low) | **Undecided** (decision about 01–04.12) | Pentagon "green light" per the Polish minister; cut options about 5,000, mostly Germany (ed.03 G1-030, G1-032) | Moving toward "held" |
| KA6 | The EU gets through the winter without a physical gas shortage (holds for PL, fragile for DE; medium) | **Undecided** (season not over) | EU 70.55%, Germany 57.30% on 14.11; TTF peak 103.94 on 30.10 (ed.03 G2-011, G2-012) | More fragile than assumed: the fill peaked below 75% |
| KA7 | Russian finances withstand the pace of war in 2026–27 (holds; medium) | **Held**, but the stated reason was wrong | January–October deficit 2.3% of GDP; oil-and-gas revenue −14% y/y despite the price spike (ed.03 G3-017) | Edition 02 said the assumption was "strengthened by high oil prices". In fact revenue fell. The finances held through borrowing and taxes, not oil |
| KA8 | The front stays at a stalemate with slow Russian progress (questioned → "contested balance"; low) | **Held as restated** | DeepState about +106 km² net Russian gain in four weeks vs ISW net Russian loss since 01.09 (ed.03 G1-034) | — |

KA totals: held 4 (KA2, KA3, KA4 formally, KA7) · held as restated 1 (KA8) · failed 1 (KA1) · undecided 2 (KA5, KA6).

The K.7 assumptions outside KA1–KA8:
- **Israel will not break the US–Iran track: undecided.** The author of the Sirik strike (12–13.11) is unknown, and Israel has a caretaker government (ed.03 G1-006, G4-037).
- **The Houthis will not interrupt Yanbu or the East–West pipeline and will not strike Abqaiq or Ras Tanura: held formally, under direct pressure.** The Houthis claimed strikes on pumping stations 5 and 6 and on an Aramco site in Abqaiq on 10.11 and 15–16.11, with no damage confirmed (ed.03 G1-016).

---

## 5. Scenarios and warning signals (horizon 6–12 months)

Descriptive only; scenarios are not scored. Edition 02's distribution was BASE "Protracted crisis without resolution" as the most likely, then CRISIS, then FAVOURABLE (report H.1). The status of each dated early-warning signal on 19.11.2026:

### BASE — "Protracted crisis without resolution"

| Signal (date) | Fired? | Evidence |
|---|---|---|
| 18.10: H.R. 5334 deadline passes with a waiver, low duties or no act | **Fired** (16.10, a waiver) | EO 14436 (ed.03 G3-001) |
| 09–10.11: US Federal Register notices on the Affiliates rule and s.301 fees | **Fired** | ed.03 G2-032, G3-008, G3-009 |
| 10.11: MOFCOM text on rare earths | **Fired** (09.11) | Announcement No. 58 (ed.03 G2-027) |
| XI: PortWatch below 20 a day | **Fired** | 0–8 a day (ed.03 G1-001) |
| XII: posture review without a cut in Poland | Pending | Decision about 01–04.12 (ed.03 G1-030) |

### FAVOURABLE — "Double de-escalation"

| Signal | Fired? | Evidence |
|---|---|---|
| Face-to-face US–Iran round confirmed by both sides | No | Doha contacts on 28–31.10 were mediated; on 12.11 Trump wrote "We don't need a deal" (ed.03 G4-001, G4-007) |
| IRGC route rule lifted | No | Turned into mining claims (ed.03 G1-008) |
| Official lifting of the blockade | No | ed.03 G1-009 |
| PortWatch 7-day mean above 40 | No | ed.03 G1-001 |
| Trilateral US–UA–RU meeting with a date | **Fired** | Abu Dhabi 10–11.11 (ed.03 G4-018) |
| Turkish-hosted Black Sea arrangement | Partly | Türkiye and Ukraine agreed on 31.10 to work on a grain corridor; no arrangement yet (ed.03 G2-026) |
| Brent below 80 USD | No | Low about 91.5 (ed.03 G2-001) |

### CRISIS — "Coupling of crises"

| Signal | Fired? | Evidence |
|---|---|---|
| Three US carriers in CENTCOM waters at once | **Fired** (16.11) | USNI (ed.03 G1-011) |
| A CENTCOM strike statement | Partly | US officials and the President confirmed the Qeshm strikes; no CENTCOM release found (ed.03 G1-005, J.2 item 2) |
| Renewed shutdown of the East–West pipeline | No (claims only) | ed.03 G1-016 |
| Saudi fatalities in successive weeks | **Fired** | 08.10, 10.10, 11.10; 21.10 Dammam from a single compilation (ed.03 G1-014) |
| A NATO government attributing an EEZ strike to Russia | Ambiguous | Romania's president blamed "Russia's aggression" (23.10); Bulgaria summoned Russia's ambassador (13.10); no formal attribution |
| EU storage below 78% on 01.11 | **Fired** | 74.6% (ed.03 G2-012) |
| TTF above 90 | **Fired** (22–30.10, peak 103.94) | ed.03 G2-011 |

**Developments the signal lists did not include:**
- **Toward FAVOURABLE or BASE:** Gulf crude exports recovered to 82% of pre-war and Brent fell about 16% in the week to 06.11 (ed.03 G2-002, G2-004). Red Sea container carriers returned (ed.03 G1-050). The US–China suspensions were aligned on 10.01.2027.
- **Toward CRISIS:**
  - The US land strikes on Iran (02.11, 06.11). The signal list asked for a CENTCOM statement, not for the strikes themselves.
  - Iranian drones at US sites in Bahrain (13–15.11).
  - The Houthis took the Bab el-Mandeb shore (15.11).
  - Black Sea hits inside a member's territorial waters (14.11).
  - The GRU-ordered plot in Estonia and the closure of the road border (14–16.11).
  - The Kremlin demanded an "indivisible security" architecture negotiated with the US (12.11).
  - "We don't need a deal with Iran" (12.11).

**Was the ordering sensible in hindsight?** BASE as the most likely held up: edition 03 judged it still the best description on 16.11 (ed.03 03 §1.2 #38). FAVOURABLE as the least likely also held up: only one of its seven signals fired. The lesson is about the CRISIS signal list.
- **Five of its seven signals fired (two more partly), yet the scenario did not occur.** Edition 02's own switching rule (two coupled triggers, or a strike together with an export outage) was not met: Brent stayed below 120 in settlements and Gulf exports rose.
- **Most CRISIS signals were also compatible with BASE**, so they did not discriminate between the two. A signal list whose items fire inside the base scenario gives readers a false alarm. It should be built from the switching rule's own thresholds: an export outage, a formal attribution, Brent above 120. The thresholds were already defined in the same section.

The horizon 2–3 year signals are mostly dated December 2026 or later and are not judged here. The one fired early: Russia's 2027–29 budget passed first reading 372–0, which fits the report's "budget for a long war" (ed.03 G3-016).

---

## 6. Surprises (misses) — edition 02

The 10 most consequential developments between 07.10 and 19.11.2026 that edition 02 did not mention or anticipate. "Anticipate" means no registry question, no early-warning signal and no assumption. Developments that edition 02 covered with a question are excluded even when the forecast missed: US land strikes (Q-0065), the trilateral (Q-0026), TTF above 90 (Q-0009), the S&P outlook (Q-0105), the midterms (Q-0031, Q-0095), Lula (Q-0033), the Black Sea campaign (Q-0098), the Graham Act waiver (Q-0012, Q-0090; ACH 3). Their accuracy is a matter for L2 and L3.

Precursor searches used `python3 -m tools.harvester search "<keyword>" --from <date> --to 2026-10-07`, the edition 02 digests `02_harvest/G1–G4_digest.md`, and `02_facts/`.

| # | Development (date; source) | Precursors on or before 07.10.2026 | Where they were | Class |
|---|---|---|---|---|
| 1 | **Poland's Constitutional Tribunal crisis:** a judge suspended the Tribunal's president on 30.10, police surrounded the building, and on 16.11 the NBP froze all payments from the Tribunal's accounts. S&P cites "polarisation and presidential vetoes" (ed.03 G4-049, G3-046; Notes from Poland 17.11, https://notesfrompoland.com/2026/11/17/polands-central-bank-freezes-constitutional-courts-accounts-amid-leadership-dispute/) | Yes. TVN24 (07.10): a judge said the Tribunal "resembles a private firm" of its president. Polsat (05.10): the Tribunal president hired an adviser facing charges. Bankier (07.10): a "radical" bill on the Tribunal | In the **corpus** (pl·PL·independent feeds), not in any digest, not in facts | **Collected but not used.** The digest filter did not pick up Polish rule-of-law items. The open conflict was foreseeable; its timing was not |
| 2 | **Serbia:** President Vučić resigned on **27.09.2026 (inside the edition 02 window)** to run for prime minister. In the snap election of 25.10 the Student List won 140 of 250 seats and SNS conceded, ending more than 12 years in power (Al Jazeera 27.09, https://aljazeera.com/news/2026/9/27/serbian-president-aleksandar-vucic-resigns-amid-prolonged-protests; ed.03 G4-039) | Yes. The resignation itself and the 25.10 election date were known | **Corpus** (OSW 28.09, "Serbia's President Vučić resigns: a one-man show"); 0 digest hits; Serbia is absent from all edition 02 files, and the 25.10 vote is missing from the K.6 calendar | **Collected but not used** (also a within-window fact miss) |
| 3 | **First Trump–Xi–Putin meeting**, Shenzhen, 19.11 (announced by the White House on 14.11; ed.03 G4-025) | Yes. Kremlin (09.09): the leaders discussed a trilateral with Xi (Korea Times, https://koreatimes.co.kr/world/20260909/putin-trump-discussed-idea-of-trilateral-summit-with-xi-kremlin); SCMP: a possible meeting at APEC | In **facts**: stage 02 G4 proposed the candidate question K4-05 ("three-way meeting by 30.11"). Stage 03 replaced it with Q-0100 (Putin's attendance) as "the cleaner test" (`03_question_bank_changes.md`). The report mentions only that the three "possibly" attend | **Collected but not used.** The candidate was dropped |
| 4 | **Moscow widened the Ukraine talks into a negotiation about European security:** an "indivisible security" architecture with the US recalling the 2021 draft treaties (12.11), and no European seat (Ushakov, 16.11) after the EU named its E5 team (ed.03 G4-019, G4-021, G4-022) | Not found: the corpus search for "indivisible" returned nothing for 20.09–07.10. Valdai (01.10) stated territorial and neutrality terms only (G4-019) | Nowhere | **Not collectable** at the state date (no public precursor found). The ACH on Ukraine had no hypothesis about agenda widening |
| 5 | **Gulf crude exports recovered** (to 82% of pre-war in October, IEA 13.11) **while AIS stayed closed**, and Brent fell about 16% in the week to 06.11. The oil premium collapsed while diesel and gas stayed tight (ed.03 G2-002 – G2-004, G1-002, G2-010) | Yes. JPMorgan (98% of pre-war crude exports) and Goldman (about 23 mb/d) on 30.09 (G2-005); KPC "more ships are getting through" (G1-006); Rubio "almost as much oil"; USNI 28.09 on European navies adjusting Hormuz deployments (corpus) | In **facts**, recorded as one side of a DISP. The D assessment read the futures–spot gap as "expectations of diplomacy" | **Used but misjudged.** The evidence for recovery was weighed as a dispute, not as the mechanism (see also §2 #8: the true gap was larger, and the report did not refresh it) |
| 6 | **The Yemeni government's Bab el-Mandeb offensive reversed:** the Southern Armed Forces withdrew from the Dhubab area on 15.11 and the Houthis threaten Aden. Houthi strikes reached Riyadh's financial district on 08.11 (ed.03 G1-015, G1-018) | Partly. AP 07.10: the Houthis claimed to have retaken Dhubab; Reuters 07.10: the Mocha claim was "premature" (G1-016) | In **facts** (DISP). The G map listed the coalition as "gaining at the strait (DISP)" | **Used but misjudged.** No question or signal covered control of the shore, which now bears on the Red Sea route |
| 7 | **US post-election hardening on Iran:** Stephen Miller replaced Susie Wiles as chief of staff (09.11), Trump wrote "We don't need a deal with Iran" and took Vance off the file (12.11), after Vance said "The reason we lost is the war" (ed.03 G4-002, G4-007, G4-034) | Partly. The mirror test (§1.6 item 3) noted that the electoral brake could become a "release" after 03.11. The personnel moves had no public precursor found | Analysis (mirror test), not facts | **Not collectable** (personnel) / **used but misjudged** (direction). The report expected post-election strike options, not the closing of the diplomatic channel |
| 8 | **Estonia:** the security service attributed an attempted arson attack on a drone maker to Russia's GRU (eight Latvian residents detained), and the government announced the closure of the road crossings to Russia (14–16.11; ed.03 G1-025) | General only. Estonia moved troops closer to the Russian border (Kyiv Independent and FT, 05.10, corpus). The B assessment named "deniable means" | Corpus (general); assessment only | **Not collectable** (the specific plot). The pattern was anticipated, but no question covered border closures or attribution of sabotage |
| 9 | **Orlen terminated one of two QatarEnergy LNG contracts** (1 Mt a year to 2034) on 10.11, citing the continuing force majeure — the first lost Qatari contract (ed.03 G2-014) | Yes, indirectly. The force majeure extension (G2-021); QatarEnergy took a 3 bn USD loan from Chinese banks "as LNG exports stall" (OilPrice, 07.10, corpus); Orlen's tariff remarks (G2-023) | Facts (force majeure) and corpus (loan) | **Collected but not used.** The question whether buyers would exit contracts was never asked; Poland's LNG contract structure was not analysed |
| 10 | **Terrorist shooting in Kraków**, 07.11, six killed (ed.03 G4-050; Euronews 08.11) | None found | Nowhere | **Not collectable** |

Also not anticipated, but of lower consequence:
- A strike on a Russian warship in the Gulf of Finland (11.11, attacker unknown; ed.03 G1-024). Not collectable.
- Nvidia's chief executive resigned after reports of a suspect contact (12.11; ed.03 G2-030). Not collectable.
- Trump's "energy ceasefire" announced on 11.10 and never implemented (ed.03 G1-036). The edition 02 judgement that an energy truce was not the bargaining item held in substance.

**Within-window facts that the edition missed** (dated before 07.10, so not developments since the state date; listed for L4):
- Vučić's resignation (27.09; row 2).
- The arrest of former BND chief August Hanning for treasonous espionage (06.10; Al Jazeera 07.10, https://www.aljazeera.com/news/2026/10/7/german-ex-spy-chief-arrested-for-treason-what-we-know). It appeared in `G4_digest.md` only as a Russian-language headline and never reached the facts; reports say the case is not linked to Russia.
- Bosnia's general election of 04.10 (RFE/RL, corpus), absent from the facts.

**Surprises by class (10):** not collectable 3 (#4, #8, #10) · not collected 0 · collected but not used 4 (#1, #2, #3, #9) · used but misjudged 3 (#5, #6, #7; #7 is also partly not collectable). For half of the surprises, precursors existed **in the harvest corpus** but did not pass the digest stage or the question-bank selection.

---

## 7. Summary table

| Edition | Framework / methodology / model | Key facts checked | Corrected or refuted | DISP items with an outcome | Assessments (med/high): held / partly / failed / undecided | KAs: held / failed / undecided | Surprises: not collectable / not collected / collected but not used / used but misjudged |
|---|---|---|---|---|---|---|---|
| 02 (07.10.2026) | 1.4.0 (1.6.0 for stage E; mixed) / v1.0 / claude-opus-5-5 | 20 (+12 DISP) | 2 of 20 corrected (10%), 0 refuted | 12 (3 settled, 2 split or partly, 6 still disputed, 1 not contradicted) | 19 / 6 / 3 / 1 (n = 29) | 5 (incl. KA8 as restated) / 1 / 2 | 3 / 0 / 4 / 3 |

Small sample: one edition, 29 assessments, 10 surprises. Per learning rule 2 these are descriptions, not general rules.

### The three most important lessons

1. **"Collected but not used" is the largest knowable class, and it fails at the digest and question-selection stage, not at collection** (§6 class; four of ten surprises, plus three within-window fact misses). The Polish Tribunal conflict, Vučić's resignation and Serbia's 25.10 election, and Qatari contract risk were all in the corpus before 07.10. None reached a digest or a fact record. The Trump–Xi–Putin meeting reached a candidate question that stage 03 dropped. The harvester had the signal; the keyword digest and the stage 02 and 03 selection screened it out. In edition 02 the precursors of the quarter's most consequential domestic event for Poland had no route into the report. Edition 03 recorded the crisis only once it had broken out (ed.03 G4-049). For L4 and L5: test digest recall on these items.

2. **Assessments that rested on one government statement failed when that government changed course** (§6 class "used but misjudged"; §4 #6, #9, KA1). KA1 ("no strike before 03.11") rested on Trump's statement of 08.10 and failed by one day. "Moscow blocks the trilateral" rested on Ryabkov (07.10) and reversed on 22.10. "The MFA mandate is collapsing" rested on a registered impeachment motion with no base rate of passage. CLAUDE.md rule 3.4 is applied to the facts (a statement is a fact about a statement), but the assessments built on such facts kept medium confidence. One correction from the same family: KA7 held, but for the wrong reason (oil revenue fell, not rose).

3. **Stale state values and over-stated status, not weak sources, caused the fact failures** (§2, fact-failure types: unrefreshed dataset value; DECL reported as DONE). Dated Brent was reported at its 29.09 value although values for 05–06.10 sat in the harvested dataset from 08.10, before stages 03 and 07. The true spot premium on the state date was about 25 USD, not 13–20. The Mecca Alliance "deployment" was DECL in the record and DONE in the report. Both errors come from moving a value from a record to the report without its date or status check. They also fed the one D assessment that failed in its cause (#16). Separately, in §5 five of seven CRISIS warning signals fired without the scenario occurring, because they were set below the switching rule's own thresholds.

---

## 8. Process notes

- Provenance: `python3 tools/pipeline.py stage-start L1 --arg latest --model "claude-opus-5-5"` (19.11.2026, commit 1ffa40a) … `stage-end L1 --arg latest`.
- Blindness and safety: no forecasting service or prediction market was visited or searched. Web search results that mentioned prediction values were not opened. No instruction-like content was found in pages, search results or harvested items.
- Limits:
  - About 12 web searches and fetches.
  - Facts after 16.11 were checked only for Hormuz attacks, the Shenzhen meeting (not yet reported on 19.11), the 22nd package (not presented by 17.11) and the Tribunal (NBP freeze, 16–17.11). Search results for 17–19.11 on Iran were undated and were not used.
  - 15 DISP rows were not re-checked. They are listed in §2.2.
  - Assessment verdicts rely partly on edition 03's §1.2 judgement (16.11.2026), cross-checked against its records but not re-read at source.

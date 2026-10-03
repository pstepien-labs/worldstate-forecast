# Source map

This map guides human and AI searching. The **harvester** turns it into machine-readable configuration: `sources/harvest/feeds.csv` (feeds, pages, Telegram, GDELT queries), `datasets.csv` (primary numeric data), `keywords.csv` (multilingual concepts), `source_universe.csv` (required roles per actor). Keep both in step: a source added here should get a harvester row, and vice versa (`/gH repair`).

Three-perspective rule: for every key event — a Western source (W), a source from the actor's side (A), a third-party source (T). State sources are a fact about a statement and a perspective, never the only confirmation of a disputed event. The same rating scale (A–F, 1–6) applies to Western and non-Western sources.

## Sources by actor

| Actor | Official and data | State or loyal media (intentions) | Independent, exile, expert |
|---|---|---|---|
| Russia | kremlin.ru, mid.ru, minfin.gov.ru, cbr.ru, Rosstat, publication.pravo.gov.ru | TASS, RIA Novosti, Interfax, Kommersant, RBC; milblogger channels (Telegram) | Meduza, The Bell, Re:Russia, Mediazona; CMAKP, RIAC, Valdai Club, CAST, IMEMO |
| China | Ministry of Foreign Affairs (press conferences), MOFCOM, General Administration of Customs, PBoC, NBS | Xinhua, People's Daily, Global Times, Qiushi, PLA Daily | Caixin, Yicai, SCMP; CICIR, CASS, Tsinghua CISS, Renmin Chongyang |
| Iran | Office of the Leader, IRNA, statements of the strait authority | Tasnim and Fars (IRGC), Press TV, Tehran Times, Mehr | Iran International, BBC Persian (opposition, partisan) |
| Gulf | SPA, WAM, QNA, Oman News Agency; Aramco, QatarEnergy | Al Arabiya, Asharq Al-Awsat, Sky News Arabia, The National; Al Jazeera (Arabic version ≠ English) | Al-Monitor, Middle East Eye; Emirates Policy Center, King Faisal Center |
| "Axis of resistance" | — | Al-Masirah (Houthis), Al Mayadeen, Al-Akhbar | — |
| India | Ministry of External Affairs, PIB, Ministry of Petroleum, RBI | The Hindu, Indian Express, Economic Times | ThePrint, The Wire; ORF, Carnegie India, Gateway House |
| Turkey | Ministry of Foreign Affairs, Anadolu | TRT, Daily Sabah | Medyascope; SETA (pro-government), EDAM |
| Ukraine | General Staff, Ministry of Defence, Ukrinform | — | Kyiv Independent, Ukrainska Pravda, NV |
| Caucasus, Central Asia | Kazinform, government agencies | — | Kavkazsky Uzel, Kun.uz, 24.kg, Eurasianet |
| Others | — | Telesur (voice of Caracas) | Dawn (Pakistan), Haaretz and INSS (Israel), Folha (Brazil), Jeune Afrique (francophone Africa) |
| West | NATO, EU Council, OFAC, IEA, CRS, central banks | — | Reuters, AP, AFP, Bloomberg, FT; ISW, CSIS, RUSI, Chatham House, PISM, OSW |

## Quantitative data (without interpretation)

- IMF PortWatch — transits through chokepoints.
- GIE AGSI — gas storage in the EU and member states.
- IEA Oil Market Report (monthly) — oil supply, demand, stocks.
- ISW — daily assessments of the front in Ukraine (W perspective; complement with A and T perspectives).
- Russian Ministry of Finance — monthly budget execution.
- OFAC Recent Actions, EU Council — sanctions.
- Central-bank calendars and statements (Fed, ECB, NBP, Bank of Russia, PBoC).
- VIEWS (PRIO/Uppsala) and ACLED CAST — quantitative conflict forecasts (only as data in stages 02–03, without carrying their probabilities into the lenses; if in doubt, treat them as a benchmark and use them in stage 06).
- GDELT — raw event data (be aware of media selection bias).
- Lowy Asia Power Index, Correlates of War (CINC) — balance of power; the Lowy weights can be changed.

## Forecasting benchmarks (stage 06 only)

Metaculus · Good Judgment Open · Polymarket · Kalshi · Manifold · RAND Forecasting Initiative. The legal availability of prediction markets in Poland has not been assessed — check it yourself before using them as a participant. Merely reading a public price into the registry requires no account.

## Practical rules

- Formulate queries about key events also in the actor's language (RU, ZH, AR, FA, TR). Check key quotes in the original — machine translation flattens the nuances of diplomatic wording.
- The Chinese MFA has a relatively fixed ladder of formulations (from "concern" to "firm opposition" and an announcement of "measures"). A change of rung is a signal — record it as a fact.
- Compare the foreign-language and domestic versions of the same outlet (RT vs RIA, Global Times vs People's Daily, Al Jazeera English vs Arabic). The difference is information.
- Some Russian government sites are sometimes unavailable from abroad, and some Chinese content is behind registration. Record lack of access as a gap; do not try to circumvent it.

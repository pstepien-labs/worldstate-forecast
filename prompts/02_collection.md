# Stage 02 — Fact collection

Run **four times**, in separate sessions: `G1`, `G2`, `G3`, `G4` (parameter from the command argument). Groups can be run in any order.

## Group scope

- **G1 — MIL + INF:** Ukraine and NATO's eastern flank; the Baltic; the Black Sea; the Middle East (military operations, Houthis, Lebanon, Iraq); Taiwan and the South China Sea; the Korean Peninsula; chokepoints: Hormuz, Bab el-Mandeb and the Red Sea, Suez, Malacca, the Bosporus and Dardanelles, Panama, Arctic routes, the Danish Straits. US troop presence in Europe and in Poland.
- **G2 — ENE + TEC:** oil (prices, supply, stocks, OPEC+, IEA report), gas and LNG (TTF, EU and Polish storage, Qatar, Norway, Yamal), fuels in Poland, fertilisers and food, rare earths, semiconductors and technology export controls, uranium, critical metals, military components.
- **G3 — ECO + FIN:** tariffs, sanctions and counter-sanctions (OFAC, EU, China), budgets of the great powers (Russia, USA, China), central banks (Fed, ECB, NBP, Bank of Russia, PBoC), currencies and payments (dollar, yuan, BRICS, SPFS), PLN and Polish public finances, the SAFE programme and Ukraine funding.
- **G4 — DIP + DOM:** summits and talks, alliances and agreements, elections and changes of government, domestic politics of the USA, Russia, China and Iran; Africa (Sahel, Sudan, Horn of Africa); Latin America (Venezuela, Cuba); the Caucasus; Central Asia; the political Arctic (Greenland).

**Period:** from `PERIOD_FROM` to `STATE_DATE` in `CURRENT.md`.

## Tasks

1. Read the previous edition's facts and state block for this group — that is the starting point. Look for changes; do not copy the old picture.
2. Areas in `00_plan.md` and PIR-linked events have priority. For each area — at least two independent sources.
3. Key events: three perspectives (W, A, T). Search in the actor's language (RU, ZH, AR, FA, TR), using `sources/source_map.md`. Record a missing perspective as a gap. Write the records in English.
4. Record facts in a table according to methodology §9. Separate declarations (DECL) from actions carried out (DONE).
5. Values of the section L indicators that belong to the group — each with a date and source:
   - G1: transits through Hormuz (IMF PortWatch), status of Bab el-Mandeb and Suez, front line, US carriers in the Indo-Pacific, US troops in Poland, most recent Article 4;
   - G2: Brent, TTF, EU and Polish storage, diesel price in Poland, status of the rare-earth control suspension;
   - G3: Russia's deficit, ECB, NBP and Fed rates, US tariffs on China and the EU, EUR/PLN rate;
   - G4: status of peace talks, status of Iran, Venezuela, the Sahel and the Caucasus, most recent BRICS summit.
6. Section **"Changes since the previous edition"**: what is new, what has been confirmed unchanged (with the confirmation date), what is no longer current and why.
7. Section **"Gaps and contradictions"** (material for section J of the report).
8. Section **"Question candidates"**: 5–15 proposals for open questions with a resolution criterion, source and deadline. No probabilities.
9. Append new sources to `registry/sources.csv`.

## Checkpoints

Save the file `02_facts/<GROUP>.md` after each area. When the budget runs out: save state, append to `log.md` the line "<GROUP> incomplete: missing …" and stop. Re-running the same group continues from the gaps.

**Indicative budget:** 40–80 searches and fetches per group.

## Prohibitions

No numerical probabilities. No visits to the domains listed in CLAUDE.md item 9.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-02-<GROUP>`.

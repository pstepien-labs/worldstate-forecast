# Stage 02 — Fact collection

Run **four times**, in separate sessions: `G1`, `G2`, `G3`, `G4` (parameter from the command argument). Groups can be run in any order.

## Group scope

- **G1 — MIL + INF:** Ukraine and NATO's eastern flank; the Baltic; the Black Sea; the Middle East (military operations, Houthis, Lebanon, Iraq); Taiwan and the South China Sea; the Korean Peninsula; chokepoints: Hormuz, Bab el-Mandeb and the Red Sea, Suez, Malacca, the Bosporus and Dardanelles, Panama, Arctic routes, the Danish Straits. US troop presence in Europe and in Poland.
- **G2 — ENE + TEC:** oil (prices, supply, stocks, OPEC+, IEA report), gas and LNG (TTF, EU and Polish storage, Qatar, Norway, Yamal), fuels in Poland, fertilisers and food, rare earths, semiconductors and technology export controls, uranium, critical metals, military components.
- **G3 — ECO + FIN:** tariffs, sanctions and counter-sanctions (OFAC, EU, China), budgets of the great powers (Russia, USA, China), central banks (Fed, ECB, NBP, Bank of Russia, PBoC), currencies and payments (dollar, yuan, BRICS, SPFS), PLN and Polish public finances, the SAFE programme and Ukraine funding.
- **G4 — DIP + DOM:** summits and talks, alliances and agreements, elections and changes of government, domestic politics of the USA, Russia, China and Iran; Africa (Sahel, Sudan, Horn of Africa); Latin America (Venezuela, Cuba); the Caucasus; Central Asia; the political Arctic (Greenland).

**Period:** from `PERIOD_FROM` to `STATE_DATE` in `CURRENT.md`.

## Inputs, in this order

1. `<DIRECTORY>/02_harvest/harvest_notes.md` — mandatory targeted searches and silent cells for this group.
2. `<DIRECTORY>/02_harvest/<GROUP>_digest.md` — multilingual leads from the harvester, by concept and day, diverse across countries and languages. Titles are in the original language: translate them yourself.
3. `<DIRECTORY>/02_harvest/indicators.md` — primary-data values (PortWatch, NBP, ECB, FRED/EIA, AGSI, Bank of Russia, OFAC list changes, FIRMS fire detections near key sites).
4. The previous edition's facts and state block for this group.
5. Web search and fetch — to verify leads, to reach primary documents, and to close the gaps from item 1. More results for a concept: `python3 -m tools.harvester search <concept|text> [--day YYYY-MM-DD]`.

If `02_harvest/` does not exist (harvester not used): record this in `log.md` as a process gap and work from web search only, as in framework 1.0.

## Tasks

1. Start from the previous edition's facts: look for changes; do not copy the old picture.
2. Areas in `00_plan.md` and PIR-linked events have priority. Walk through the digest concepts of your group. For each key story: open the original item(s), then the primary document where one exists (statement, decree, dataset), and write a fact record. A digest item is a lead, never a fact on its own.
3. Key events: three perspectives (W, A, T). The digest tag `[lang·country·role]` helps, but you decide the perspective for the specific event (a Russian outlet is A for a Russian action and T for an Iranian one). Search in the actor's language (RU, ZH, AR, FA, TR, …) where the digest has no actor-side item, using `sources/source_map.md`. Record a missing perspective as a gap. Write the records in English; translate quotes.
4. Record facts in a table according to methodology §9. Separate declarations (DECL) from actions carried out (DONE). **Independence:** two outlets repeating the same wire story or the same official statement are one source — cite the origin. Prefer the primary dataset from `indicators.md` over a report about it (e.g. PortWatch instead of an article citing PortWatch).
5. Values of the section L indicators that belong to the group — each with a date and source (from `indicators.md` where available, otherwise web):
   - G1: transits through Hormuz (IMF PortWatch), status of Bab el-Mandeb and Suez, front line, US carriers in the Indo-Pacific, US troops in Poland, most recent Article 4;
   - G2: Brent, TTF, EU and Polish storage, diesel price in Poland, status of the rare-earth control suspension;
   - G3: Russia's deficit, ECB, NBP and Fed rates, US tariffs on China and the EU, EUR/PLN rate;
   - G4: status of peace talks, status of Iran, Venezuela, the Sahel and the Caucasus, most recent BRICS summit.
6. Section **"Changes since the previous edition"**: what is new, what has been confirmed unchanged (with the confirmation date), what is no longer current and why.
7. Section **"Gaps and contradictions"** (material for section J of the report), including every mandatory search from `harvest_notes.md` that did not produce an actor-side or third-party source.
8. Section **"Question candidates"**: 5–15 proposals for open questions with a resolution criterion, source and deadline. Prefer resolution sources that the harvester collects directly (`sources/harvest/datasets.csv`). No probabilities.
9. Section **"Coverage"** (new in framework 1.1): number of records by perspective (W / A / T), number of languages of the sources used, share of records resting on a primary source, digest concepts of the group that produced no record and why.
10. Append new sources to `registry/sources.csv`. If a valuable source is missing from the harvester, add a line to `sources/harvest/CHANGELOG.md` under "Proposed sources" (the next `/gH repair` adds it).

## Checkpoints

Save the file `02_facts/<GROUP>.md` after each area. When the budget runs out: save state, append to `log.md` the line "<GROUP> incomplete: missing …" and stop. Re-running the same group continues from the gaps.

**Indicative budget:** 40–80 searches and fetches per group, spent on verification, primary documents and the mandatory gap searches — not on rediscovering what the digest already lists.

## Prohibitions

No numerical probabilities. No visits to the domains listed in CLAUDE.md item 9.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

**Provenance:** `python3 tools/pipeline.py stage-start 02 --arg <GROUP> --model "<your model id>"` at the start and `python3 tools/pipeline.py stage-end 02 --arg <GROUP>` before the commit.

Commit: `edition-NN stage-02-<GROUP>`.

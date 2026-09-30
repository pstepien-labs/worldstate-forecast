# L4 — Sources and coverage

Parameter `SCOPE`. Read `prompts/learning/README.md` first. Input: `02_harvest/manifest.json`, `coverage.md`, `sources_health.md` and the "Coverage" sections of `02_facts/G*.md` of each edition in scope; `08_quality_control.md` item 7/7a; `registry/sources.csv`; `sources/harvest/*.csv`; findings of L1 and L3 if present. Output: `reviews/learning/<today>_<scope>/L4_sources.md`.

## Tasks

1. **Coverage trend.** Per edition: harvested items, languages, countries, Western share of items and of fact records, share of key events with three perspectives, silent required cells of the source universe, share of facts resting on a primary source. Improving or not?
2. **Source track record.** For every fact that L1 found refuted or corrected, and every party claim (DECL by a government, military or armed group) that can now be checked: which source and perspective carried it. Tally per source and per source type (official / state-loyal / independent-exile / Western / third / aggregator). Compare with the admiralty rating given at the time. Propose rating changes in `registry/sources.csv` notes only where there are at least 3 checkable claims (never edit old fact records).
3. **Blind spots.** From the L1 surprises classified *not collected* and the L3 causes "not collected" / "source bias": which actor, language, region or data type was missing? Which concepts in `sources/harvest/keywords.csv` never matched anything useful, and which topics produced facts but no concept?
4. **Harvester health.** Sources failing for more than one edition, sources that produced nothing used in any fact record over the scope (candidates to drop), sources with high use (keep and protect), and dataset feeds that resolved registry questions.
5. **Proposals (config level).** Concrete changes to `sources/harvest/feeds.csv`, `datasets.csv`, `keywords.csv`, `source_universe.csv` and `sources/source_map.md`: add / fix / drop, each with the evidence from items 1–4. These are patch-level changes; list them for L5 and for the next `/gH repair`.

**Log and provenance:** `stage-start L4 --arg <scope>` … `stage-end L4 --arg <scope>`. Commit: `learning <scope> L4`.

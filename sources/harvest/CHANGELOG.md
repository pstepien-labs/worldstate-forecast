# Harvest configuration changelog

Changes to `sources/harvest/*.csv` (sources, datasets, keywords, source universe). Patch-level process changes: they change what is collected, not the method. Newest first.

| Date | Change | Sources / rows | Reason |
|---|---|---|---|
| 30.09.2026 | Initial configuration (framework 1.1.0) | 147 RSS feeds, 11 watched pages, 6 Telegram channels, 31 GDELT queries, 21 datasets, 35 keyword concepts in 17 languages, 36 source-universe actors | Analysis of edition 01 sourcing: 51% English sources, key figures read through aggregators, no systematic actor-side coverage. Rows marked "verify" in `notes` were not reachable from the build environment and must pass `python3 -m tools.harvester check` on first local run (`/gH repair` fixes failures). |

## Proposed sources

Stage 02 and learning step L4 add candidate sources here; the next `/gH repair` adds, verifies and moves them into the table above.

| Date | Proposed by | Source | Actor / role / language | Why |
|---|---|---|---|---|

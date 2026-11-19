# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

- 17.11.2026 · Q-0079 · stage V (edition 03) could not re-read IMF PortWatch (HTTP 429 quota exceeded), so the stage 01 YES (13.10.2026 = 17 transits) is unconfirmed for 08, 09 and 12–15.10; re-check the PortWatch series and approve or correct (see `editions/2026-11-16_edition-03/V_autoverify.md`).
- 20.11.2026 · P-0036 · Stage 04: three checks before each probability (smallest resolving event, error band, statement type) · minor · approve via `/learn`; go live only after the out-of-sample replay on edition 03 (`reviews/learning/2026-11-19_latest/L5_proposals.md`).
- 20.11.2026 · P-0037 · Harvester: each page change gets its own item ID (fixes 12 watched pages stuck at one item) · patch.
- 20.11.2026 · P-0038 · Harvester configuration: route missed topics into the digests, retire failing sources, notes for 4 sources · patch.
- 20.11.2026 · P-0039 · Harvested series for data-threshold questions (TTF, storage fallback, HICP, GUS CPI, FAO, PortWatch interval) · patch. Owner action: `AGSI_API_KEY`, `EIA_API_KEY`, `FIRMS_MAP_KEY` in `.env` are still missing (since 05.10.2026).
- 20.11.2026 · P-0040 · Stage 02: actor-language reads, fixed "Incomplete key events" table, standing gaps · minor.

## Decisions taken without the user

- 17.11.2026 · stage 03 (edition 03) · Q-0143 (US shutdown 12–31.12): p_status_quo set to 0.90, because with no new decision the continuing resolution expires on 11.12 and appropriations lapse (literal §3.5); a first use of this reading. Review in `editions/2026-11-16_edition-03/03_question_bank_changes.md` §1.
- 17.11.2026 · stage 03 (edition 03) · Panel replacements outside the original cluster, whose outcome was exhausted: Q-0033 (BRAZIL_ELECTIONS) → Q-0123 (DOM, RS_GOVERNMENT, Serbian government); Q-0031 (US_ELECTIONS) → Q-0122 (Hegseth leaving office, cluster kept as the midterms' consequences); Q-0004 (DeepState territory, no readable source) → Q-0116 (Russian MoD drone count, UA_FRONT). Review in §3 of the same file.
- 17.11.2026 · stage 04 A (edition 03) · Blindness incident: a format check (`tail` on `registry/forecasts.csv`) displayed the last two registry rows — edition-02 AGG/AGG_RT for one question, with that edition's lens values. It happened after all 83 lens-A forecasts were written; none was changed afterwards. Autopilot continued (lens A kept as written; later stages told to read only the CSV header). Judge whether to accept — details in `editions/2026-11-16_edition-03/log.md`.
- 17.11.2026 · stage 03 (edition 03) · Note for Q-0079: the PortWatch ArcGIS API was readable on 17.11.2026 (rows to 15.11), so the October rows may now be checkable.
- 18.11.2026 · stage 08 (edition 03) · Section 0 of the report gives the aggregate "BSS vs the crowd" score (methodology §1(b), resolved questions only), while the conventions line said crowd comparisons are not part of the report (§6). Default: kept the score and clarified the conventions line; confirm, or move the score to the benchmark annex in later editions. Details in `editions/2026-11-16_edition-03/08_quality_control.md` §2.
- 18.11.2026 · stage 07 (edition 03) · Two defaults: (1) no PDF — pandoc or another converter is not installed, so the report is Markdown only (the prompt's own fallback); (2) the provenance line and `edition_commit` use 045c4fa, the commit at the first stage 07 start, not 0084c34 at the resume (only autopilot heartbeat commits lie between). Details in `editions/2026-11-16_edition-03/log.md`.

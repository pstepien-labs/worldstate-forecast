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
- 20.11.2026 · P-0039 · Harvested series for data-threshold questions (TTF, storage fallback, HICP, GUS CPI, FAO, PortWatch interval) · patch. The three API keys were set on 22.11.2026 and the 7 keyed sources run from that evening.
- 20.11.2026 · P-0040 · Stage 02: actor-language reads, fixed "Incomplete key events" table, standing gaps · minor.
- 22.11.2026 · `/gH repair` · **The harvester is no longer under launchd.** `scripts/harvest.sh stop` (needed for `check`) removed the job `com.worldstate-forecast.harvester`, and agents may not touch launchd jobs, so the harvester was restarted by hand (`scripts/harvest.sh start`, running at the end of the repair). It will not restart after a reboot or crash. Run `scripts/autopilot.sh install` to hand it back to launchd. (Process note for the next repair: the prompt's `stop`/`check` sequence and the launchd rule conflict.)
- 22.11.2026 · `/gH repair` · YE state/loyal cell is empty: `saba_ye` (Saba, Houthi-run) was disabled after 7 weeks of HTTP 403. Stage 02 G1 proposed 21sept.net or ypagency.net (Houthi-run). Not added: a sanctions judgement is needed, and the domain would have to go into `sources/harvest/no_republish.txt`, which a repair may not edit. Decide: add one (with the no_republish entry) or keep YE as a standing gap.
- 22.11.2026 · `/gH repair` · Should `kcna.kp` and the newly added `rodong.rep.kp` (DPRK state media, `kcna_kp` and `rodong_en`) be listed in `sources/harvest/no_republish.txt`? Neither is listed now; a repair may not edit that file.
- 22.11.2026 · `/gH repair` · TR:western is a required cell with no source, but Türkiye is flagged `⚠ over` (ratio 2.22) and H §3a forbids adding sources for over-covered actors. Decide which rule wins (e.g. one low-volume BBC Türkçe or DW Türkçe feed), or drop `western` from TR's required roles.

## Decisions taken without the user
- 22.11.2026 framework 2.0.0 / methodology v1.1 (P-0042), approved by the owner in one decision: stage W, model-driven questions, broader harvester. The autopilot was paused during the change and resumed after it. Rollback: `git log --oneline pre-v1.1..` and revert.
- 20.11.2026 improvements applied by policy: P-0036 P-0037 P-0038 P-0039 P-0040 (undo one with: git revert <commit>)

- 17.11.2026 · stage 03 (edition 03) · Q-0143 (US shutdown 12–31.12): p_status_quo set to 0.90, because with no new decision the continuing resolution expires on 11.12 and appropriations lapse (literal §3.5); a first use of this reading. Review in `editions/2026-11-16_edition-03/03_question_bank_changes.md` §1.
- 17.11.2026 · stage 03 (edition 03) · Panel replacements outside the original cluster, whose outcome was exhausted: Q-0033 (BRAZIL_ELECTIONS) → Q-0123 (DOM, RS_GOVERNMENT, Serbian government); Q-0031 (US_ELECTIONS) → Q-0122 (Hegseth leaving office, cluster kept as the midterms' consequences); Q-0004 (DeepState territory, no readable source) → Q-0116 (Russian MoD drone count, UA_FRONT). Review in §3 of the same file.
- 17.11.2026 · stage 04 A (edition 03) · Blindness incident: a format check (`tail` on `registry/forecasts.csv`) displayed the last two registry rows — edition-02 AGG/AGG_RT for one question, with that edition's lens values. It happened after all 83 lens-A forecasts were written; none was changed afterwards. Autopilot continued (lens A kept as written; later stages told to read only the CSV header). Judge whether to accept — details in `editions/2026-11-16_edition-03/log.md`.
- 17.11.2026 · stage 03 (edition 03) · Note for Q-0079: the PortWatch ArcGIS API was readable on 17.11.2026 (rows to 15.11), so the October rows may now be checkable.
- 18.11.2026 · stage 08 (edition 03) · Section 0 of the report gives the aggregate "BSS vs the crowd" score (methodology §1(b), resolved questions only), while the conventions line said crowd comparisons are not part of the report (§6). Default: kept the score and clarified the conventions line; confirm, or move the score to the benchmark annex in later editions. Details in `editions/2026-11-16_edition-03/08_quality_control.md` §2.
- 18.11.2026 · stage 07 (edition 03) · Two defaults: (1) no PDF — pandoc or another converter is not installed, so the report is Markdown only (the prompt's own fallback); (2) the provenance line and `edition_commit` use 045c4fa, the commit at the first stage 07 start, not 0084c34 at the resume (only autopilot heartbeat commits lie between). Details in `editions/2026-11-16_edition-03/log.md`.

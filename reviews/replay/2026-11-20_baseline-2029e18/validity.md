# Validity — replay baseline-2029e18

- Replayed edition: editions/2026-10-07_edition-02
- Lens: B ("outside view"); prompt: reviews/replay/prompts/04_forecasts_2029e18.md; label: baseline-2029e18
- Replay run on 20.11.2026

1. Model id: claude-opus-5-5. Training-data cutoff, as I know it: June 2026.
2. Edition information cutoff — first line of `03_analysis.md`: "# Stage 03 — Analysis (edition 02, state 07.10.2026)". The file has no `INFO_CUTOFF` line (edition 02 predates rule 3.16); its header gives the state date 07.10.2026 and says the stage ran on 09.10.2026. Information cutoff taken as 07.10.2026 (stage run 09.10.2026).

Training cutoff (06.2026) is before the information cutoff (07.10.2026): the replay is VALID.

## Possibly contaminated questions
None. I knew no outcome for any of the 88 questions: every resolution event falls after 07.10.2026, well past the June 2026 training cutoff. Background knowledge from before the cutoff (e.g. earlier truce extensions, past named PLA exercises, past Baltic cable incidents) was used only as base rates, as lens B requires.

## Other notes
- Inputs used: `questions.csv` of this folder, `editions/2026-10-07_edition-02/02_facts/G1–G4.md`, `03_analysis.md`, and the lens-B parts of the prompt. No web, no registry, no other edition, no earlier forecasts, no other replay folder opened. To check the `edition` field format I read `tools/pipeline.py` lines matching "edition" (code only, no data).
- Post-cutoff items seen in the inputs (03_analysis header; G3-069; G4 post-state-date notes): 6, not used.
- Searches: 0. Instruction-like content in the inputs: none found.
- Outputs: `forecasts.csv` (88 rows, run `B@baseline-2029e18`, date 2026-10-07), working notes `04_forecasts_B.md`.

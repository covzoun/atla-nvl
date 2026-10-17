# Revision Notes — Workflow & Base File Alignment

Date: 2026-07-19
Scope: full readiness package after workflow assessment + early-generation failure report.

---

## Decisions Applied

1. **Episode 9 canon:** Katara **witnesses** Jake's waterbending (Macro Map version is canonical). `Story_Bible.md` was updated to match; Jake's Southern Water Tribe origin stays hidden; the open question was re-scoped to *when the rest of Team Avatar learns*.
2. **Single tracker:** `Relationship_Tracker.md` is eliminated. `State_Tracker.md` is now the project's one living continuity document (story state + relationship state). Every reference across all files was updated.
3. **Platforms:** Phase 1 = Google AI Studio, Phase 2 = Claude (current; prompts are platform-agnostic if you switch later), Phase 3 = ChatGPT. `Phases.md` updated.
4. All 12 observed early-generation failure modes were addressed in the prompts and rules (mapping below).

---

## New Files

- `base/Book_1_Chapter_Index.md` — provisional episode→chapter map (13 chapters + 4 folded time-skips). Chapter numbering lives here; change it here first.
- `REVISION_NOTES.md` — this file.

## Rewritten Files

- `Phases.md` — platform labels corrected; Glossary.md and Book_1_Chapter_Index.md added to Phase 1 uploads; single-tracker Phase 3; three human approval gates (blueprint / prose / tracker); tracker snapshots; Phase 2 file-scoping rule; original-content chapter inputs; folder conventions; Cleaned Canon Reference restored to expected Phase 1 output.
- `base/State_Tracker.md` — merged tracker with an update-rules header (STATE sections replaced, LOG sections appended/pruned), seeded with the Book 1 opening baseline so Chapter 1 has a real starting state.
- `setup/3A_ChatGPT.md` / `setup/3B_ChatGPT.md` — single-tracker responsibilities; output = the complete updated State_Tracker.md in one code block; append-vs-replace conflict resolved; Recent Events Summary exception defined (2–5 factual sentences, only place a summary is allowed).

## Edited Files

- `setup/1A_AI_Studio.md` — template name fixed; new "Original Content Chapters" section; new "Observed Generation Failure Modes" section; quality checklist additions (Jake agency, pacing, canon load-bearing).
- `setup/1B_AI_Studio.md` — template name fixed (2×); original-content chapter handling; checklist addition.
- `setup/2A_Claude.md` — new authority clause ("your general ATLA knowledge is context, not authority"); new "Observed Failure Modes" section with a per-response self-check.
- `setup/2B_Claude.md` — new "Pre-Writing Check" section.
- `setup/2C_Claude2.md` — continuation point now explicitly ignores the status markers.
- `base/Chapter_Blueprint_Template.md` — Cleaned Canon Reference section added (1A/2A required it; it was missing); Original Content variant (Macro Map B-Plot Anchor); Required Reference Files now excludes the deleted tracker and adds the file-scoping note; drafting-instruction and final-verification additions.
- `base/Writing_Rules.md` — `Book_1_Macro_Map.md` added to the authority hierarchy (rank 3); template name fixed; single-tracker language; continuity checklist now references State_Tracker.md; new "Observed Generation Failure Modes" section.
- `base/Story_Bible.md` — Ep 1–2 raid role reconciled with the macro map; Ep 9 locked (Katara witnesses the bending; origin hidden); Ep 13 White Heron "inherits not invents" wording + Jake's serious injury locked; waterbending-secrecy continuity note scoped; open questions re-scoped.
- `base/Book_1_Macro_Map.md` — Ep 1–2 low-profile/crew-coordination wording; Ep 9 lock marker; Ep 13 "adopts/inherits" wording; Ep 15 clarified (bending is known to Katara; the origin is what stays hidden).
- `base/Core_Persona.md` — Known Gaps entry no longer mislabels the Year-2 exile event as a "Book 1 scene."

## Unchanged (copied so the folders are complete)

- `base/Canon.md`, `Character_Guide.md`, `Relationships.md`, `Bending_Styles.md`, `Glossary.md`, `Style_Guide.md`

## How the 12 Observed Issues Are Now Addressed

| # | Issue | Fix |
|---|-------|-----|
| 1 | Canon drift / unsupported additions | 2A authority clause + failure-mode sections + blueprint final verification |
| 2 | Jake character drift | Jake-agency and bending-primary checks in 1A / 1B / 2A / 2B / template / Writing_Rules |
| 3 | Knowledge boundaries | Reinforced in failure-mode lists in 1A / 2A / 2B |
| 4 | Repetition of prior info | Seeded State_Tracker + Previous Chapter Continuity + 2B pre-writing check |
| 5 | Rushed emotional development | "Pacing matches State_Tracker baselines" checks in 1A / 1B / 2A / 2B / template |
| 6 | AI writing style | Style_Guide always-on in Phase 2 + banned-pattern reminders in 2A / 2B |
| 7 | Episode structure eroding | "Canon stays load-bearing" checks in 1A / 1B / 2A / template |
| 8 | Zuko dominating | Parallel-protagonist rule in 1A / 2A / Writing_Rules |
| 9 | Relationship moving too fast | Relationship baselines in State_Tracker + gradual-progression checks |
| 10 | Continuity inconsistencies | Merged State_Tracker + Unresolved Threads + full-file Phase 3 updates + Gate 3 snapshots |
| 11 | Reference file overload | Phase 2 file-scoping: blueprint's Required Reference Files + 4 always-on files only |
| 12 | Weak chapter handoffs | Previous Chapter Continuity section + tracker ending state + 2B opening check |

## Remaining Manual Steps

1. Create the working folders if you haven't: `source/`, `outlines/`, `chapters/`, `archive/`.
2. Pick one consistent episode transcript source and save per-chapter files to `source/`.
3. At Gate 3 each chapter: overwrite live `State_Tracker.md`, then save `archive/State_Tracker_after_ChXX.md`.
4. The "Known Gaps" in Canon.md / Story_Bible.md remain intentionally open — no AI should resolve them without your explicit approval.
5. If you later move Phase 2 to a different model (e.g., Kimi), the 2A/2B/2C prompts need no changes — only the label in Phases.md.

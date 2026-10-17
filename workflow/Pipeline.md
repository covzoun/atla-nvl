# Chapter Generation Pipeline (Manual)

Human-run checklist. No agent executes this — you do, copy-pasting between tools per `Phases.md`.

---

## Pre-Generation

1. Confirm `base/State_Tracker.md` is the correct starting tracker for the chapter. Confirm no stale `run_kit/phase2_thread/Chapter_[NN]_Blueprint.md` exists for the current chapter.
2. Gather Phase 1 files per `Phases.md`.

## Phase 1 (manual, AI Studio)

3. In AI Studio: paste 1A (system box) + 1B (chat, chapter number filled in). Save draft blueprint.
4. STOP, wait for the draft, then paste 1C in the same session. If FAIL, use 1C's regenerated full blueprint instead of the original draft.
5. **Gate 1:** Read the REVIEWER BRIEF first and rule on each question (approve/tweak/reject). Then read the full blueprint fresh. Check bending rules against `Bending_Styles.md` / `Book_1_Macro_Map.md` directly — don't trust 1C alone on this, it's new and unproven. Approve or send back for revision.
6. Save approved blueprint to `run_kit/phase2_thread/Chapter_[NN]_Blueprint.md`.
6b. Sync Claude's thread folder from the blueprint's Required Reference Files. Fallback command: `powershell -ExecutionPolicy Bypass -File run_kit/Refresh-Kit.ps1 -SyncPhase2 -Chapter [N]`. Eyeball the result.

## Phase 2 (manual, model per Phases.md)

7. Open a NEW Claude thread inside your project (2A system instructions already apply from the project — never paste them). Select-all `run_kit/phase2_thread/` (tracker + blueprint — project files apply automatically) and attach.
8. Paste `2B_Claude.md` (chapter/scene filled in) requesting Scene 1.
9. Check status tag. `Continue` → paste `2C_Claude.md` in the same session. `Complete` → paste `2C_Claude.md` for the next scene; insert `***` break yourself between scenes in your saved copy.
10. Repeat until `[CHAPTER STATUS: Complete]`. Concatenate all scenes into one document yourself — remove status tags from the final saved copy.

## Gate 2

11. Read the full chapter fresh. Run the checklist in `Phases.md`'s Gate 2 section by hand (canon fidelity, blueprint fidelity, continuity, bending-rule check, repetition check, style check).
12. Approve, or identify specific scenes to regenerate and repeat steps 8–9 for those only.
13. Save approved chapter to `chapters/Chapter_[NN].md` (use current chapter number).

## Phase 3 (provider-agnostic — fresh thread/session, never reuse Phase 2's)

14. Pick Option A (CLI/agent, e.g. OpenCode) or Option B (any free web-chat LLM). Never reuse Phase 2's thread.
    - Option A: run `setup/3A_OpenCode.md` with the chapter number filled in (agent reads from disk).
    - Option B: stage first `powershell -ExecutionPolicy Bypass -File run_kit/Refresh-Kit.ps1 -SyncPhase3 -Chapter [N]`, then open a NEW web-chat thread and select-all upload `run_kit/phase3/`. Paste `setup/3A_Continuity_Clerk.md` with the chapter number filled in.
15. STAGE 0: model reviews the prose (PASS/FLAG list, no writes, no rewrites). Any FLAG → stop: copy the STAGE 0B PHASE 2 REGEN REQUEST packet into your Phase 2 (Claude) thread, patch only the returned scenes (SCENE X (REGEN) + REPLACES: lines) by hand — or dismiss the flags — then CONTINUE in the SAME Phase 3 thread with the updated chapter. Read the GATE BRIEF and DEPTH NOTES before approving.
16. Only on all-PASS, Stage 1 produces one code block with the proposed complete State_Tracker.md. Review it against the chapter (Gate 3).
17. Quota hit mid-Phase-3: switch to another free provider, open a FRESH thread, re-upload `phase3/` (Option B) or re-run the prompt (Option A). No file/workflow changes. Log in `provider_status.md`.

## Gate 3

18. Approve the proposed tracker, request changes, or manually edit it.
19. Save the approved tracker over `base/State_Tracker.md` and an identical copy to `archive/State_Tracker_after_Ch[NN].md`.
20. Save the approved blueprint to `outlines/Chapter_[NN]_Blueprint.md` and approved prose to `chapters/Chapter_[NN].md`.
21. Prep `run_kit/` for next chapter: `phase1/` gets fresh base files, next chapter source files if canon, and previous chapter blueprint/prose if applicable; `phase2_thread/` resets to fresh `State_Tracker.md` only until next Gate 1; `phase3/` is rebuilt per chapter by `-SyncPhase3` (delete or leave stale until next Gate 2).
22. Close all three threads. Next chapter starts fresh at step 1.

---

## If interrupted (token limit, session drop)

Save whatever prose exists so far. Resume in a new session using `2C_Claude.md`, picking up from the last complete sentence.

## If Phase 3 output looks incomplete

Re-run Phase 3. If still incomplete, manually diff and patch the tracker yourself rather than guessing.

## File Naming (locked, matches `Book_1_Chapter_Index.md` examples)

- `chapters/Chapter_[NN].md`
- `outlines/Chapter_[NN]_Blueprint.md`
- `archive/State_Tracker_after_Ch[NN].md`

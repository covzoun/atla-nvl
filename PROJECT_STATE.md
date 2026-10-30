# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-30  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `awaiting_grok_repository_review` (three targeted revisions applied; exact-version package now instructs Grok to commit its independent report to a dedicated GitHub branch; awaiting reviewer completion).  
**Merged review commit:** `591527d91a9d72c397df91f5b5ee5f98eb763893`.
- **Current disposition:** ChatGPT Turn D began from verified live head `a46ebba1b0c2a4b4cbfa9b89e74229e5372afae7`; Chapter 0 blob `8e7b91f5dfb6e328138b47a5bad23343edf22de0` was unchanged. No material Chapter 0 issue was found that blocks human review. C0-A-001 remains verified fixed; C0-D-001 records a minor, non-blocking wording nuance about the public council charge versus Iroh’s later telling, preserved without a prose edit. Basin staging, first-manifestation vs first-conscious-use, witness knowledge, and Jake’s limited information about Haru and Emi hold. Turn D made no Chapter 0 prose changes. The issue ledger and this state were updated; the stale cycle-status sentence in `workflow/Ch1-10_Revision_Log.md` was reconciled. `REVISION_LEARNINGS.md` reflects Turns A–C; no new reusable lesson was added. The reviewed result was merged to `main` in commit `591527d91a9d72c397df91f5b5ee5f98eb763893` via PR #3 after a clean integration branch was created from the latest main. Chapter 0 blob remains `8e7b91f5dfb6e328138b47a5bad23343edf22de0`.
- **Scope lock:** Chapter 0 only for this adversarial cycle. Do not begin Chapter 1 or any other chapter until the user supplies a new explicit target.
- **External reviews:** New-cycle Turns A (Grok), B (ChatGPT), and C (Grok) multi-pass cycles are complete. Both AIs independently audited the latest committed version and challenged each other’s work.
- **Human review:** The reviewed package is now on `main` for the user's review. This merge is not human approval. The user retains final authority to accept, reopen, or redirect.

## Next actions, in order

1. Await Grok's report commit on `grok/ch0-v2-verification` at `workflow/reviews/Chapter_00_Grok_Verification_2026-10-30.md`. The branch is pre-created from `ch0-v2-pilot`; Grok must not edit the manuscript. If GitHub write access is unavailable, the user may provide the report in chat as a fallback.
2. Adjudicate Grok's findings, then complete a fresh whole-chapter reread, continuity audit, mechanical QA, and completion checklist.
3. Keep the Chapter 12 council-memory dependency visible; do not edit Chapter 12 during this Chapter 0-only pilot.
4. Present Chapter 0 for the user's creative review only after the completion gate is satisfied.
5. Do not advance to another chapter without explicit user direction.

## V2 pilot setup

- **Working branch:** `ch0-v2-pilot` (created from `main`; `main` remains unchanged).
- **Baseline Chapter 0 blob:** `8e7b91f5dfb6e328138b47a5bad23343edf22de0`.
- **Current Chapter 0 blob:** `b84f916d8d8c1693b1d6ba25c4fdc0203c82fe74`.
- **Latest chapter prose commit:** `e2616f16768d5b0f90123a33f866566294e9ea47`.
- **Latest review-package sync commit:** `ad49570a752295c9be1baeecd0b1d3f778279bdb`.
- **Independent review package:** `workflow/handoffs/Chapter_00_V2_Independent_Review_Package.md` contains the exact revised chapter version, reviewer prompt, and repository-submission instructions. It is synced to chapter blob `b84f916d8d8c1693b1d6ba25c4fdc0203c82fe74` (package blob `2e14b2c0e6f025130d04f99f312ffa77e0045edc`).
- **Workflow documentation PR:** #4 (`editorial-workflow-v2`) remains open and unmerged; the pilot uses its V2 instructions without merging it.
- **Scope:** Chapter 0 only. The user's latest feedback authorizes fresh developmental reassessment and justified structural rewriting. A substantial rewrite is committed on the pilot branch; `main` remains unchanged.

## Current V2 review update (2026-10-30)\n\n- Grok independently reviewed Chapter 0 blob `d132c42efeecb2de4b4302285999971eb21b2e2e` and found no critical defects. It recommended three targeted improvements: clarify the council cause, sharpen Jake's impulse to run, and add one practical burn limitation.\n- All three findings were addressed without changing scene order or undertaking another rewrite. Current Chapter 0 blob: `b84f916d8d8c1693b1d6ba25c4fdc0203c82fe74` (2,989 words).\n- The independent review package was resynced to the exact current chapter and now includes instructions for Grok to commit its report to a dedicated branch. Package blob: `2e14b2c0e6f025130d04f99f312ffa77e0045edc`.
- Pre-created reviewer branch: `grok/ch0-v2-verification`, based on `ch0-v2-pilot`. Expected report path: `workflow/reviews/Chapter_00_Grok_Verification_2026-10-30.md`. Grok must only add the report; no manuscript edits or merges.\n- Main remains unchanged. The pilot branch remains separate.\n\n## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29 (prior editor).
- Independent external AI review (Grok) performed 2026-10-29 against foundational sources; historical only for the new cycle.
- New adversarial cycle Turn A (Grok): multi-pass complete; no prose changes; C0-A-001 deferred.
- New adversarial cycle Turn B (ChatGPT): multi-pass complete; removed unsupported “fire-knife”; one localized sentence smoothed.
- New adversarial cycle Turn C (Grok): multi-pass complete; independently verified the Turn B change and the locked continuity points (basin, first-manifestation, witness/knowledge limits, Haru/Emi uncertainty); no further prose changes; ledger and REVISION_LEARNINGS status reconciled.
- Optional final check Turn D (ChatGPT, 2026-10-29): independent Passes A–H complete against live head `a46ebba1b0c2a4b4cbfa9b89e74229e5372afae7`; no material Chapter 0 issue blocks human review; no chapter prose changes. PR #3 merged the reviewed package to `main` in commit `591527d91a9d72c397df91f5b5ee5f98eb763893`. Human review remains pending.
- Latest length remains ~2,270 words.
- The Agni Kai is staged only in Chapter 0. Chapter 12 recounts the aftermath and Iroh’s telling, not a second staging of the duel.
- `REVISION_LEARNINGS.md` remains the living record of recurring editorial root causes and preventive checks.
- Two-AI protocol: https://github.com/covzoun/atla-nvl/blob/main/workflow/Adversarial_Editorial_Protocol.md
- Working branch: https://github.com/covzoun/atla-nvl/tree/ch0-adversarial-review
- Chapter 0 issue ledger: https://github.com/covzoun/atla-nvl/blob/main/workflow/Chapter_00_Adversarial_Review_Log.md
- Chapter 0 file: https://github.com/covzoun/atla-nvl/blob/main/chapters/Chapter_00.md
- Living editorial lessons: https://github.com/covzoun/atla-nvl/blob/main/REVISION_LEARNINGS.md
- Chapter index: https://github.com/covzoun/atla-nvl/blob/main/base/Book_1_Chapter_Index.md
- Revision log: https://github.com/covzoun/atla-nvl/blob/main/workflow/Ch1-10_Revision_Log.md

## Locked orientation facts for this task

- Jake and Zuko are **16 at the beginning of Book 1**.
- Their Agni Kai occurred when they were **13**, three years before Book 1 begins.
- Chapter 0 is front matter and does not renumber Chapters 1–20.
- Jake’s first bending manifestation at the Agni Kai is involuntary and public. His first conscious, deliberate use occurs later at sea.
- Consult `base/Canon.md`, `base/Story_Bible.md`, the chapter index, the relevant macro map/state tracker, and the actual source transcript for detailed authority. This file is a workflow pointer, not a replacement for those sources.

## Rules for updating this file

Update this record whenever the active target, workflow stage, review status, next action, or a meaningful blocker changes. Keep completed facts separate from planned actions. Never mark an external review, human approval, commit, or verification complete without evidence.

The active task is determined by this file plus the user’s latest explicit instruction. Chapter numbering alone never determines the next task. If this file conflicts with the user’s latest explicit instruction, follow the user’s instruction and update this file to match.


## Final V2 pilot verification (2026-10-30)

- **Workflow stage:** `ready_for_user_review`.
- **Current Chapter 0:** `chapters/Chapter_00.md` on `ch0-v2-pilot`, blob `b84f916d8d8c1693b1d6ba25c4fdc0203c82fe74`, 2,989 words.
- **Grok report:** Retrieved directly from `grok/ch0-v2-verification` at `workflow/reviews/Chapter_00_Grok_Verification_2026-10-30.md`; report blob `8a309a67082dcdc9507fb74eb9c159538deebc51`. It verifies the exact current chapter blob and recommends human creative review.
- **Reviewer branch audit:** Compared with the pilot branch; only the report file was added. No manuscript changes or merges by Grok.
- **Chapter 12 continuity adjudication:** Chapter 12's council anecdote is introduced with “He wanted to sit in the war councils. He was eleven.” Chapter 0's Agni Kai is at age thirteen. The available text permits these to be separate council sessions; the apparent conflict is not confirmed. No Chapter 12 edit is made in this Chapter 0-only pilot.
- **Final QA:** Whole Chapter 0 reread and exact blob verification complete; locked canon and continuity points checked; mechanical checks remain within the word, sentence, paragraph, and punctuation limits. No further prose edit warranted.
- **Disposition:** Ready for user creative review. This is not user approval. `main` remains unchanged; PR #4 remains open and unmerged; do not merge any branch without explicit user authorization.

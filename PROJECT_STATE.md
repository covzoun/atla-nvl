# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-29  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `adversarial_revision_cycle` (Grok Turn A initial audit recorded; multi-pass completion checkpoint pending before ChatGPT Turn B).  
**Working branch:** `ch0-adversarial-review` (keep `main` unchanged until the user approves the result).
- **Current disposition:** Grok completed Turn A of the new adversarial cycle on 2026-10-29. Independent full-chapter audit found no critical or major confirmed defects. One minor plausible risk (C0-A-001, “fire-knife” wording) deferred. Chapter prose was not altered. Issue ledger and this state file updated. The new mandatory multi-pass standard was added after this initial audit. Grok must resume Turn A to complete and document the additional distinct passes before ChatGPT Turn B begins.
- **Scope lock:** Chapter 0 only for this adversarial cycle. Do not begin Chapter 1 or any other chapter until the user supplies a new explicit target.
- **External reviews:** Prior 2026-10-29 Grok review is historical only. New-cycle Turn A initial audit recorded; expanded multi-pass completion is pending. ChatGPT Turn B must wait until Grok records the required pass ledger.
- **Human review:** Pending after the new adversarial cycle reaches its exit gate.

## Next actions, in order

1. Grok resumes Turn A using the updated master prompt and branch protocol. Complete all required multi-pass audits, record a pass ledger in the review log, and save a checkpoint if continuation is needed. Do not hand off yet.
2. After Grok documents completion of all passes and verifies the latest branch state, ChatGPT begins Turn B from the actual latest commit.
3. Each subsequent AI turn must complete its own multi-pass cycle before handing off. If a turn cannot be completed reliably in one response, checkpoint and ask the user to say “continue” rather than handing off prematurely.
4. Continue alternating until the documented exit gate is met; only then return Chapter 0 for human review.
5. Do not begin another chapter without explicit user direction.

## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29 (prior editor).
- Independent external AI review (Grok) performed 2026-10-29 against `REVISION_LEARNINGS.md`, `base/Canon.md`, `base/Story_Bible.md`, `base/Book_1_Chapter_Index.md`, `base/Style_Guide.md`, and the Chapter 0 revision-log entry. Final light polish applied same day for clarity of one holding-cell sentence and one seasonal reference.
- New adversarial cycle Turn A (Grok, 2026-10-29): full independent audit; findings recorded in `workflow/Chapter_00_Adversarial_Review_Log.md`; no chapter prose changes; ledger and state updated.
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

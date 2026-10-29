# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-29  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `adversarial_revision_cycle` (new cycle initialized; Grok Turn A pending).  
**Working branch:** `ch0-adversarial-review` (keep `main` unchanged until the user approves the result).
- **Current disposition:** The prior editorial pass and Grok review from 2026-10-29 remain historical. By the user's latest instruction, Chapter 0 is reopened for a new two-AI adversarial revision cycle. The cycle is initialized but no new-cycle critique or edits have occurred yet. Grok is assigned the first fresh audit, followed by ChatGPT; the AIs will alternate until the exit gate in `workflow/Adversarial_Editorial_Protocol.md` is met. Human review is pending under this new cycle.
- **Scope lock:** Chapter 0 work is closed. Do not begin Chapter 1 or any other chapter until the user supplies a new explicit target.
- **External reviews:** Independent AI review completed and recorded.
- **Human review:** Waived by user instruction for this stage.

## Next actions, in order

1. User shares the updated master prompt and Chapter 0 reference links with Grok for Turn A.
2. Grok checks out `ch0-adversarial-review`, fetches its latest head, performs a fresh exhaustive critique before editing, updates the issue ledger, applies justified fixes, verifies, commits/pushes if supported, and hands off to ChatGPT.
3. ChatGPT independently fetches the resulting commit and performs Turn B under the same protocol, then hands back to Grok.
4. Continue alternating until the documented exit gate is met; only then return Chapter 0 for human review.
5. Do not begin another chapter without explicit user direction.

## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29 (prior editor).
- Independent external AI review (Grok) performed 2026-10-29 against `REVISION_LEARNINGS.md`, `base/Canon.md`, `base/Story_Bible.md`, `base/Book_1_Chapter_Index.md`, `base/Style_Guide.md`, and the Chapter 0 revision-log entry. Final light polish applied same day for clarity of one holding-cell sentence and one seasonal reference.
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

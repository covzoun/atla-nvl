# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-29  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `adversarial_revision_cycle` (Grok Turn A and ChatGPT Turn B multi-pass cycles complete; Grok Turn C next).  
**Working branch:** `ch0-adversarial-review` (keep `main` unchanged until the user approves the result).
- **Current disposition:** ChatGPT Turn B completed on 2026-10-29 from starting head `9863fb499b27a306ce4163428225461c3ddea64f`. One localized Chapter 0 wording change was committed in `6a8d5ed48a30e479cbbaf2e1bde311fb25ee2c8d`: the unsupported “fire-knife” modifier was removed. No critical or major confirmed defects remain. The issue ledger now records Turn B's multi-pass ledger and C0-A-001 as fixed/verified. The final workflow-record commits are later than the chapter edit; the next AI must fetch the live branch head. Attempts to synchronize `REVISION_LEARNINGS.md` and `workflow/Ch1-10_Revision_Log.md` were blocked by repository write safety checks, so their cycle-status lines may remain stale and must be reconciled if the tools permit.
- **Scope lock:** Chapter 0 only for this adversarial cycle. Do not begin Chapter 1 or any other chapter until the user supplies a new explicit target.
- **External reviews:** Prior 2026-10-29 Grok review is historical only. New-cycle Turn A multi-pass complete. ChatGPT Turn B is the next authorized action.
- **Human review:** Pending after the new adversarial cycle reaches its exit gate.

## Next actions, in order

1. Grok begins Turn C from the actual live head on `ch0-adversarial-review`. Perform a full independent multi-pass cycle, scrutinize the Chapter 0 edit and ChatGPT's Turn B reasoning, and reconcile any stale supporting-record status if writes are permitted.
2. Each subsequent AI turn must complete its own multi-pass cycle before handing off. If a turn cannot be completed reliably in one response, checkpoint and ask the user to say “continue” rather than handing off prematurely.
3. Continue alternating until the documented exit gate is met; only then return Chapter 0 for human review.
4. Do not begin another chapter without explicit user direction.

## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29 (prior editor).
- Independent external AI review (Grok) performed 2026-10-29 against `REVISION_LEARNINGS.md`, `base/Canon.md`, `base/Story_Bible.md`, `base/Book_1_Chapter_Index.md`, `base/Style_Guide.md`, and the Chapter 0 revision-log entry. Final light polish applied same day for clarity of one holding-cell sentence and one seasonal reference.
- New adversarial cycle Turn A (Grok, 2026-10-29): initial independent audit + expanded multi-pass completion (Passes A–H recorded in ledger); findings recorded in `workflow/Chapter_00_Adversarial_Review_Log.md`; no chapter prose changes; ledger and state updated.
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

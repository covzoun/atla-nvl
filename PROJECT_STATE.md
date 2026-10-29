# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-29  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `adversarial_revision_cycle` (Turns A–C multi-pass complete; exit-gate evaluation recorded; awaiting user decision on human review).  
**Working branch:** `ch0-adversarial-review` (keep `main` unchanged until the user approves the result).
- **Current disposition:** Grok Turn C completed on 2026-10-29 from live head `1c25a84baa3455ff6ef533618b1854e3b970a6e6`. Independent multi-pass audit accepted ChatGPT’s removal of the unsupported “fire-knife” wording (C0-A-001 verified). Basin staging, first-manifestation vs first-conscious-use distinction, witness knowledge, and Jake’s limited information about Haru and Emi were re-checked and hold. No new confirmed defects or material plausible risks. No further chapter prose changes. Issue ledger residual text corrected; REVISION_LEARNINGS status line updated. `workflow/Ch1-10_Revision_Log.md` adversarial-cycle note remains partially stale (prior write attempts blocked; primary ledger is authoritative).
- **Scope lock:** Chapter 0 only for this adversarial cycle. Do not begin Chapter 1 or any other chapter until the user supplies a new explicit target.
- **External reviews:** New-cycle Turns A (Grok), B (ChatGPT), and C (Grok) multi-pass cycles are complete. Both AIs independently audited the latest committed version and challenged each other’s work.
- **Human review:** Exit-gate criteria appear met on the evidence available after Turn C. User retains final authority to accept for human review, reopen, or redirect.

## Next actions, in order

1. User evaluates the exit gate and either accepts Chapter 0 for human review, requests another adversarial turn on a specific residual, or redirects the workflow.
2. Do not merge to `main` or advance to another chapter without explicit user direction.
3. If a further AI turn is ordered, the named AI must fetch the live branch head and complete a full multi-pass cycle.

## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29 (prior editor).
- Independent external AI review (Grok) performed 2026-10-29 against foundational sources; historical only for the new cycle.
- New adversarial cycle Turn A (Grok): multi-pass complete; no prose changes; C0-A-001 deferred.
- New adversarial cycle Turn B (ChatGPT): multi-pass complete; removed unsupported “fire-knife”; one localized sentence smoothed.
- New adversarial cycle Turn C (Grok): multi-pass complete; independently verified the Turn B change and the locked continuity points (basin, first-manifestation, witness/knowledge limits, Haru/Emi uncertainty); no further prose changes; ledger and REVISION_LEARNINGS status reconciled.
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

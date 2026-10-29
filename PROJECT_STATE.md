# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-29  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task

- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, the front-matter prologue “The Agni Kai”.
- **Workflow stage:** `awaiting_external_ai_review`.
- **Current disposition:** The latest editorial pass is staged for independent AI review. Treat the chapter as frozen for review unless a concrete defect is discovered or the user supplies review feedback.
- **Scope lock:** Work on Chapter 0 only. Do not begin Chapter 1, Chapter 13, or any other chapter as the next task merely because it appears next in the narrative sequence.
- **External reviews:** None have been recorded as received or completed. Do not imply that Grok, Claude, or another external AI has reviewed or approved the chapter.
- **Human review:** Still pending after the independent AI review round.

## Next actions, in order

1. The user shares Chapter 0 and relevant project references with one or more independent AI reviewers.
2. The user brings their feedback back to this workflow.
3. Assess each suggestion against the actual chapter, source material, locked project decisions, and `REVISION_LEARNINGS.md`. Classify it as a confirmed defect, plausible risk, or subjective preference.
4. Make only justified changes to Chapter 0, then verify the full chapter and update affected records.
5. Return the chapter for the user's human review.
6. Do not advance to another chapter until the user explicitly approves or redirects the workflow.

## Completed work relevant to this task

- Chapter 0 received a focused canon, continuity, staging, and prose pass on 2026-10-29.
- The chapter index records the latest length as 2,270 words.
- The Agni Kai is staged only in Chapter 0. Chapter 12 recounts the aftermath and Iroh's telling, not a second staging of the duel.
- `REVISION_LEARNINGS.md` was created as a living record of recurring editorial root causes and preventive checks.
- Chapter 0 file: https://github.com/covzoun/atla-nvl/blob/main/chapters/Chapter_00.md
- Living editorial lessons: https://github.com/covzoun/atla-nvl/blob/main/REVISION_LEARNINGS.md
- Chapter index: https://github.com/covzoun/atla-nvl/blob/main/base/Book_1_Chapter_Index.md
- Revision log: https://github.com/covzoun/atla-nvl/blob/main/workflow/Ch1-10_Revision_Log.md

## Locked orientation facts for this task

- Jake and Zuko are **16 at the beginning of Book 1**.
- Their Agni Kai occurred when they were **13**, three years before Book 1 begins.
- Chapter 0 is front matter and does not renumber Chapters 1–20.
- Jake's first bending manifestation at the Agni Kai is involuntary and public. His first conscious, deliberate use occurs later at sea.
- Consult `base/Canon.md`, `base/Story_Bible.md`, the chapter index, the relevant macro map/state tracker, and the actual source transcript for detailed authority. This file is a workflow pointer, not a replacement for those sources.

## Rules for updating this file

Update this record whenever the active target, workflow stage, review status, next action, or a meaningful blocker changes. Keep completed facts separate from planned actions. Never mark an external review, human approval, commit, or verification complete without evidence.

The active task is determined by this file plus the user's latest explicit instruction. Chapter numbering alone never determines the next task. If this file conflicts with the user's latest explicit instruction, follow the user's instruction and update this file to match.

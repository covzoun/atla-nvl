# Adversarial Editorial Protocol

**Purpose:** Run a disciplined, evidence-based editorial cycle with independent review, justified revisions, regression checks, and an explicit completion gate before human review.

**Current project use:** Chapter 0 is the first pilot of the autonomous V2 workflow. See `workflow/Autonomous_Editorial_Workflow_V2.md` for the repository operating addendum and the master prompt for full instructions.

## Core principles
1. **Evidence before edits.** Diagnose the complete chapter and record findings before changing prose.
2. **Structure before polish.** Assess chapter purpose, opening, scene order, causality, pacing, escalation, and emotional progression before line editing.
3. **One manuscript owner.** The Lead Editor owns the integrated manuscript and repository changes. Reviewers challenge and propose; they do not overwrite the integrated draft by default.
4. **Independent perspectives.** Use fresh-eyes, beginner-reader, ATLA specialist, developmental, continuity, and prose lenses. Use genuine subagents only when actually available; label simulated perspectives honestly.
5. **Adversarial, not performative.** Challenge reasoning and changes, not the identity of the previous editor. Do not invent defects or rewrite sound prose to demonstrate activity.
6. **Authority hierarchy.** Explicit user decisions and designated canon/continuity sources govern their respective domains. `REVISION_LEARNINGS.md` is a preventive aid, not canon authority.
7. **Actual repository state wins.** Every turn verifies the current branch, commit, and chapter.
8. **Regression control.** Every material edit is checked in the full chapter and relevant downstream context.
9. **Honest status.** Report commits, pushes, source checks, external reviews, agent delegation, and completion only after verification.

## V2 chapter cycle
1. Verify `PROJECT_STATE.md`, target, branch, commit, scope, `REVISION_LEARNINGS.md`, and relevant sources.
2. Independently diagnose purpose, structure, scene sequence, reader experience, character arcs, canon, continuity, physical staging, and prose.
3. Explicitly choose targeted edits, substantial restructuring, scene rewrite, full rewrite, or no prose change. Do not default to light editing because the chapter has prior review history.
4. The Lead Editor revises and maintains one integrated manuscript.
5. Send the exact version to an independent reviewer using `workflow/Independent_Reviewer_Prompt.md` and `workflow/Review_Handoff_Template.md`.
6. The reviewer returns an evidence-based report with strengths, classified findings, structural assessment, remedies, uncertainties, and exact version identity.
7. The Lead Editor verifies each finding, records its disposition, and implements justified changes.
8. Repeat review as warranted. A structural rewrite after an earlier review requires a fresh whole-chapter assessment.
9. A reviewer who did not author the latest material revision performs final independent verification. The Lead Editor rereads the complete chapter and final diff.
10. Apply `workflow/Editorial_Completion_Checklist.md`. If material defects remain, revise again. A fixed number of turns or reviewer agreement is not proof of completion.
11. Present the chapter to the user only when ready. Human review remains final creative authority, not a substitute for editorial QA.

## Independence rules
- Initial reviewers receive the exact chapter version and role assignment, not the Lead Editor's diagnosis or proposed fixes.
- A fresh-eyes reader first reads without canon/project explanations, then may receive contextual materials for a second pass.
- A new conversation can reduce anchoring but does not by itself prove independence.
- Record platform, role, exact version, sources provided, and whether the review was genuinely independent.
- Do not claim genuine agents or parallel delegation unless actually available and used.

## Handoff and user burden
The Lead Editor prepares the complete review package. The user only transports it between platforms when no integration exists and returns the report. The user is not responsible for inventing prompts, reconciling routine disagreements, or implementing revisions.

## Issue record
For each meaningful finding record ID, location, evidence, classification (confirmed defect / plausible risk / subjective preference / unsupported suggestion), severity, confidence, root cause, proposed fix, regression risk, decision, and status.

## Continuation
If a cycle cannot be completed within the current context, save a durable checkpoint with branch and commit, completed passes, sources, findings, edits, checks, and exact remaining work. Mark the cycle incomplete and resume the same editor's work. Never hand off prematurely.

## Chapter 0 pilot scope
The user's latest instruction explicitly reopens Chapter 0 for a fresh developmental assessment and justified revisions. Its prior human-review-pending state applied to the earlier cycle. Preserve the current main version as baseline. Chapter 0 may be substantially restructured or rewritten if supported by diagnosis. Do not edit Chapter 1 or any other chapter.

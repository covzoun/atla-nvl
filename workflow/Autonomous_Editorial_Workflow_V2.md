# Autonomous Editorial Workflow V2: Repository Operating Addendum

This addendum operationalizes the V2 master prompt for repository use. The master prompt remains the full instruction set; this file defines the shared workflow gates.

## Roles
- **Lead Editor / manuscript owner:** one AI instance controls the integrated manuscript, working branch, issue ledger, revisions, documentation, and final report.
- **Independent reviewers:** Grok, a separate ChatGPT instance, Claude, DeepSeek, or genuine platform subagents may review. They do not overwrite the integrated manuscript by default.
- **User:** final creative authority and final reviewer, not routine editorial coordinator.

## Independence
Initial reviewers receive the exact chapter version and role assignment, but not the Lead Editor's diagnosis or proposed fixes. Fresh-eyes readers first read without canon/project explanations. Record platform, role, version, and whether the review was genuinely independent. A new chat alone does not prove independence. Never claim genuine subagents or parallel work unless actually available and used.

## Repeating chapter cycle
1. Verify PROJECT_STATE.md, target, branch, commit, sources, and scope.
2. Independently diagnose structure, scene purpose/order, causality, pacing, emotional progression, characterization, reader orientation, canon, continuity, action, and prose.
3. Explicitly choose targeted editing, substantial restructuring, scene rewrite, full rewrite, or no prose change. Do not default to light edits merely because a draft has prior review history.
4. Lead Editor revises and maintains one integrated manuscript.
5. Send the exact revised version to an independent reviewer using the repository's reviewer prompt and handoff template.
6. Lead Editor verifies each finding, records accept/reject/defer/escalate decisions, and implements justified changes.
7. Repeat targeted or full review as warranted. Structural rewrites require a fresh whole-chapter review.
8. A reviewer who did not author the latest material revision performs final independent verification. Lead Editor rereads the complete chapter and final diff.
9. Apply the completion checklist. If material defects remain, revise again. Reviewer agreement or a fixed number of rounds is not proof of readiness.
10. Present the chapter to the user only when ready, with an honest report. Do not merge to main, mark human approval, or advance chapters without required user authorization.

## User handoff burden
The Lead Editor prepares all reviewer instructions and the complete handoff package. The user only transports the package between platforms when no real integration exists and returns the review report. The user is not asked to invent prompts, reconcile routine disagreements, or implement edits.

## Reviewer output
Each report identifies the exact version reviewed, independence conditions, overall and structural diagnosis, strengths to preserve, classified findings, source/continuity evidence, concrete remedies, uncertainties, and completion judgment.

## Chapter 0 pilot
The user's latest instruction explicitly reopens Chapter 0 for a fresh developmental pilot. Its prior human-review-pending status applies to the earlier review cycle only. The pilot may substantially restructure or rewrite Chapter 0 when justified. Do not edit Chapter 1 or any other chapter during this pilot. Preserve the current Chapter 0 baseline and use the repository's canon, story bible, style guide, chapter index, macro map, and relevant downstream chapters as authorities.

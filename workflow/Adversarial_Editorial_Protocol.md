# Adversarial Editorial Protocol

**Purpose:** Run a disciplined, evidence-based revision cycle between two AI editors, with alternating critique, justified edits, regression checks, and a clear exit gate before human review.

**Current project use:** Chapter 0 is the initial target. The master prompt defines the detailed agent behavior; this document preserves the workflow in the repository.

## Core principles

1. **Evidence before edits.** Each AI first audits the complete current chapter and records findings before changing prose.
2. **Adversarial, not performative.** Challenge reasoning and changes, not the identity of the previous editor. Do not invent defects or rewrite sound prose to demonstrate activity.
3. **Authority hierarchy.** User decisions and designated canon/continuity sources outrank either AI's interpretation. REVISION_LEARNINGS.md is a preventive aid, not canon authority.
4. **Actual repository state wins.** Every turn fetches the current branch and chapter. Summaries and handoff reports are pointers, not proof.
5. **Regression control.** Every material edit is checked in the full chapter and relevant downstream context.
6. **Honest status.** A commit, push, source check, external review, or exit-gate result is reported only after verification.

## Default turn order

Unless the user explicitly changes it:

1. **Grok, Turn A:** Fetch the latest state, independently critique the whole chapter, classify findings, make justified changes, self-audit, update records, commit/push if supported, and hand off to ChatGPT.
2. **ChatGPT, Turn B:** Fetch the latest commit independently, audit the whole chapter and Grok's changes, fix justified issues, self-audit, update records, commit/push if supported, and hand off to Grok.
3. **Grok, Turn C:** Fetch ChatGPT's latest commit, challenge the chapter and the previous turn, correct evidence-supported defects, self-audit, update records, commit/push if supported, and hand off to ChatGPT.
4. Continue alternating until the exit gate is met or a decision genuinely requires the user.

The user coordinates the handoffs. Neither AI should claim it can initiate the other AI's turn unless a real integration supports that action. Historical reviews do not count as a fresh turn under this protocol.

## Required critique dimensions

Inspect all dimensions relevant to the target chapter:

- Canon accuracy; separate source fact, implication, and adaptation invention.
- Causality, scene purpose, escalation, structure, pacing, and emotional progression.
- Physical geography, blocking, timing, object continuity, injuries, and action readability.
- Character knowledge, motivation, voice, age, agency, relationships, and emotional plausibility.
- Reader orientation, terminology, exposition, point of view, subtext, and narrative distance.
- Prose rhythm, dialogue, repetition, stock phrasing, clarity, and style constraints without flattening deliberate variation.
- Setup/payoff and continuity with relevant prior and downstream chapters.
- Applicable lessons in REVISION_LEARNINGS.md.
- Effective choices and passages that should be preserved.

## Issue record

For each meaningful finding, record:

- **ID:** Stable identifier such as C0-A-001.
- **Location:** Exact passage, beat, or continuity point.
- **Evidence:** What in the chapter or authoritative source supports the finding.
- **Classification:** Confirmed defect, plausible risk, subjective preference, or unsupported suggestion.
- **Severity:** Critical, major, moderate, or minor.
- **Root cause:** Why the problem arose and any relevant existing lesson.
- **Proposed fix and regression risk.**
- **Decision:** Fix, verify first, reject, defer, or ask user.
- **Status:** Open, fixed pending verification, verified, rejected, or deferred.

Do not duplicate an existing issue under a new ID unless it is a genuinely distinct failure. Reopen a verified issue only when new evidence shows the fix failed or a regression occurred.

## Required steps on every AI turn

1. Read PROJECT_STATE.md, this protocol, REVISION_LEARNINGS.md, the target chapter, and the relevant chapter revision log.
2. Fetch the latest actual commit and confirm the assigned turn and scope.
3. Consult relevant authoritative canon, story bible, style, outline, source transcript, chapter index, state tracker, and downstream chapters as needed.
4. Perform and record an exhaustive critique before editing.
5. Classify findings and decide which are justified. Preferences must not be presented as objective facts.
6. Implement justified changes only. Preserve effective work from earlier turns.
7. Reread the entire chapter and inspect the full diff against the parent commit.
8. Verify fixes and inspect regressions across causality, staging, continuity, voice, pacing, character knowledge, and setup/payoff.
9. Update the issue ledger and only the project records affected by the changes. Add to REVISION_LEARNINGS.md only when a reusable root cause or preventive check is genuinely supported.
10. Commit and push if tools and permissions allow. Verify the resulting commit and remote state before claiming success.
11. Update PROJECT_STATE.md with the actual turn, next AI, latest verified repository state, open material issues, and next action.
12. Hand off using the report template below.

## Handoff template

- **Target and branch:**
- **Verified commit SHA:**
- **Turn completed / next AI:**
- **Files changed and rationale:**
- **Issues fixed and verified:**
- **Issues rejected or deferred, with reasons:**
- **Open issues by ID and severity:**
- **Regression and source checks actually performed:**
- **Checks not performed and why:**
- **Known disagreements or residual risks:**
- **Exact next action:**

The receiving AI must verify these claims from the repository. Do not rely on a pasted full chapter if the repository is accessible.

## Exit gate: ready for human review

The chapter may be marked ready for human review only when:

1. Both AIs independently audited the latest committed version at least once under this protocol.
2. Each AI challenged at least one round of the other's changes.
3. No unresolved critical or major confirmed defect remains.
4. Every material plausible risk was examined; accepted residual risks are documented.
5. Every accepted material change was checked against relevant authorities and the full chapter for regressions.
6. No unresolved material issue remains that can be responsibly fixed without user input.
7. Relevant project records match the actual repository and final commit/push status is verified.
8. Remaining disagreements are documented as preferences, uncertain risks, or user decisions rather than concealed as consensus.

If new material defects appear, continue the cycle. If a full round yields only subjective alternatives and no evidence-supported improvement, explain why further edits are unlikely to help and recommend stopping. A deadlock must preserve both arguments and identify the narrow decision needed from the user. Do not claim unanimity merely because both AIs stop finding new issues.

## Scope and authority

The active target and stage come from PROJECT_STATE.md plus the user's latest explicit instruction. Chapter numbering does not choose the next task. The user retains final creative authority. Do not advance to another chapter without explicit direction.



## Deep-work rule: each AI turn is a multi-pass work cycle

A turn is not complete after one critique, one edit, and one self-review. The user explicitly prefers depth over speed. Do not rush to hand off or compress the work into a superficial single response.

Each turn must complete distinct passes before handoff: (1) repository and authority audit; (2) independent whole-chapter structural and narrative audit; (3) technical and continuity audit against actual sources; (4) line-level and reader-experience audit; (5) issue triage and revision plan; (6) coherent revision batches with diff checks; (7) three distinct post-edit audits: a fresh-reader pass, an evidence/canon/continuity pass, and an adversarial regression pass; (8) an independent final sweep of the whole chapter and final diff. Record strengths to preserve as well as defects. If a pass finds a material issue, return to triage and revision, then repeat the relevant checks.

The handoff must include a pass ledger marking each pass complete, incomplete, or blocked and describing what was actually checked. Listing or attempting a pass does not make it complete; findings must be resolved or explicitly dispositioned.

## Continuation checkpoints

If a turn cannot be completed reliably within one response or context window, do not lower the standard or hand off prematurely. Save a durable checkpoint in the issue ledger and project state: branch and commit SHA, passes completed, sources inspected, findings, edits, checks completed, and exact remaining work. State clearly that the turn remains incomplete and ask the user to reply **continue** to resume this same AI's work cycle. On continuation, re-fetch repository state and resume from the checkpoint. Do not ask for continuation after every small step when work can proceed reliably in the same response.

## No premature handoff or artificial convergence

Do not hand off after fixing only one or two issues. Complete the full multi-pass work cycle first. Multiple reviews must use meaningfully different lenses, not repeatedly rewrite a sentence without new evidence. After one AI completes a full cycle, the other AI performs its own full cycle; then they alternate again. A single turn by each AI does not automatically satisfy the exit gate. Continue when material findings, plausible risks, or regressions remain. If later passes find no material issues, document that result and why the pass was still useful. If only subjective alternatives remain, explain why further editing is unlikely to improve the chapter.

## Branch safety and human approval

When GitHub tools support branches, conduct the cycle on a dedicated working branch so main remains unchanged during the debate. For Chapter 0, use the branch named in PROJECT_STATE.md. Both AIs must use the same branch, fetch its latest head before each turn, and avoid parallel edits. Do not create a competing branch unless the user directs it or the named branch is unavailable.

Passing the exit gate means ready for human review, not automatically approved for merge. Do not merge into main, mark human approval complete, or advance to another chapter until the user explicitly approves or redirects the workflow. If branch support is unavailable, document the limitation and use the safest supported alternative.


## Addendum: mandatory multi-pass turns (2026-10-29)

The user's clarification supersedes any interpretation of a turn as one quick critique/edit/handoff. Each AI turn is a sustained multi-pass work cycle. Before handoff, complete and report: (1) repository and source-authority audit; (2) independent whole-chapter structural/narrative audit; (3) technical canon/continuity/staging audit; (4) line-level and reader-experience audit; (5) evidence-based triage before editing; (6) justified revision batches with diff checks; (7) three separate post-edit audits: fresh-reader, source/continuity, and adversarial regression; (8) final full reread and diff/record verification. Resolve or explicitly disposition material findings from each pass. Record the pass status and actual coverage in the handoff.

If the cycle cannot be completed reliably in one response/context window, do not hand off prematurely. Save a durable checkpoint with branch and SHA, passes completed, sources inspected, findings, edits, checks, and exact remaining work. Tell the user the turn is incomplete and ask them to say “continue” to resume the same AI's cycle. On continuation, fetch the latest state and resume from the checkpoint. Do not optimize for speed or perform repeated cosmetic rewrites without new evidence. The other AI must also complete its own full multi-pass cycle; one turn by each AI is not automatically enough to satisfy the exit gate.

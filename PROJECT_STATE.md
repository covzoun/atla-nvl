# Project State: ATLA Novel Editorial Workflow

**Last verified:** 2026-10-31  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active task
- **Target:** Book 1, Chapter 0, `chapters/Chapter_00.md`, front-matter prologue “The Agni Kai”, with the linked continuity passage in Chapter 12.
- **Workflow stage:** `developmental_revision_after_user_review`.
- **User authorization:** The user authorized the V2 editorial workflow and Chapter 0 developmental pilot, authorized the narrow Chapter 12 continuity synchronization, and has now authorized merging the completed changes to `main` for review.
- **Current manuscript status:** Chapter 0 V2 rewrite and the narrow Chapter 12 continuity adjustment are complete. Both were independently verified against the relevant project authorities and the exact pinned versions.
- **Exact verified versions before merge:** Chapter 0 blob `b84f916d8d8c1693b1d6ba25c4fdc0203c82fe74`; Chapter 12 blob `e1b17949a52c6987e945bca2dac7224829f51720`.
- **Independent final verification:** Grok's report is at `workflow/reviews/Chapter_00_12_Grok_Final_Verification_2026-10-30.md` on branch `grok/ch0-ch12-final-verification`. Lead Editor retrieved the report, checked its pinned blobs, and independently re-read the continuity passage.
- **Human review:** User reviewed Chapter 0 and returned nine substantive creative comments. The first V2 draft is reopened for developmental revision; no human approval is claimed.

## V2 operating model
- One Lead Editor owns the integrated manuscript, working branch, issue ledger, revisions, documentation, and final report.
- Independent reviewers assess exact versioned drafts and return evidence-based reports. They do not overwrite the integrated manuscript by default.
- Specialist lenses: fresh-eyes reader, beginner reader, ATLA canon specialist, developmental editor, continuity auditor, and prose editor.
- Genuine subagents are used only when the platform actually supports them. Simulated perspectives are labeled honestly.
- The Lead Editor prepares prompts and handoff packages. When direct integrations exist, the Lead Editor retrieves reviewer reports from the repository rather than asking the user to shuttle them.
- A chapter is presented to the user only after independent final verification and the completion checklist.
- The user retains final creative authority. Do not begin the next chapter until the current chapter's review disposition is clear.

## Branching policy
- Use `main` by default for routine editorial work and ordinary manuscript updates.
- Create a separate working branch only when isolation is materially useful, such as a substantial experimental rewrite, parallel reviewer work, risky structural changes, or a change that must be independently reviewed before integration.
- Reviewer branches remain isolated. Do not merge reviewer branches unless a specific report or artifact is intentionally being incorporated.
- Keep `main` as the source of truth and ensure the user can see the current manuscript in the default branch.

## Next actions
1. User reviews Chapter 0 and the synchronized Chapter 12 passage on `main`.
2. Incorporate any user-requested creative changes, preserving the verified version as the baseline.
3. Once Chapter 0's review disposition is clear, close its cycle and proceed to Chapter 1 under the V2 workflow.

## Locked orientation facts
- Jake and Zuko are 16 at the beginning of Book 1.
- Their Agni Kai occurred when they were 13, three years earlier.
- Chapter 0 is front matter and does not renumber Chapters 1–20.
- Jake's first bending manifestation at the Agni Kai is involuntary and public. His first conscious, deliberate use occurs later at sea.
- Haru and Emi survive the immediate fallout but are dismissed, investigated, and lose their palace security; Jake leaves without full knowledge of their final circumstances.
- Consult `base/Canon.md`, `base/Story_Bible.md`, the chapter index, macro map, style guide, relevant transcripts, and downstream chapters for detailed authority.

## State maintenance
Update this file whenever the active target, stage, review status, next action, or blocker changes. Keep completed facts separate from plans. Never claim a review, agent delegation, commit, push, or verification without evidence.

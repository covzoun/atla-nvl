# Grok Repository Start Here

This is the standing entry point for ATLA editorial work. The user should not need to copy a review package into chat.

## Trigger

When the user says “Proceed with ATLA” or equivalent, read this file from the repository and then:

1. Read `PROJECT_STATE.md` on the repository's default branch and identify the active task, target file, workflow stage, working branch, current target blob/commit, and next action.
2. Read the active task's exact handoff/package file named in `PROJECT_STATE.md` or linked from the active task's workflow record. Do not rely on a package from an earlier cycle if the target blob has changed.
3. Read the relevant project authorities and source files specified by that handoff.
4. Follow the handoff's reviewer role, independence requirements, scope limits, exact-version checks, report format, and repository submission instructions.
5. If the task is awaiting independent review, review the exact current version and commit the complete report to the dedicated reviewer branch/path specified by the handoff. Open a PR only if instructed and supported.
6. If the task is not awaiting review, do not invent a new review cycle or modify the manuscript. Report the actual stage and ask for direction only if the handoff leaves a consequential ambiguity.

## Repository and safety rules

- Repository: `covzoun/atla-nvl`.
- GitHub is the source of truth. Read the live repository; do not ask the user to paste files that are already accessible there.
- Never assume a branch, commit, package, or chapter version. Verify live refs and blob SHAs.
- Do not edit manuscript, canon, story bible, project state, or review logs unless the active handoff explicitly assigns that role.
- Independent reviewers must not read Lead Editor findings before completing the required cold read when the handoff requires independence.
- Do not push to `main), merge a PR, or broaden chapter scope unless the user explicitly authorizes it.
- Do not claim a push, commit, review, or PR unless GitHub confirms it.
- After submitting a report, tell the user that it is ready and provide the report path, branch, commit SHA, and PR URL if one exists.

## Expected user instruction

The user can simply tell Grok:

“Proceed with ATLA. Read `workflow/GROK_START_HERE.md` in `covzoun/atla-nvl` and follow the active task in the repository.”

No package copying is required when Grok's GitHub connection can read the repository.

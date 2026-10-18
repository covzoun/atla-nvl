# ATLA Novel Project — Reference Guide

## Project Overview

Character-driven alternate universe adaptation of Avatar: The Last Airbender. Follows original character Jake alongside Zuko and Iroh through Book 1 (20 chapters, one per episode slot: 13 canon adaptations + 7 Original B-plot chapters, per `base/Book_1_Chapter_Index.md`).

## Process

Phases 1–2 fully manual. Phase 3 provider-agnostic: CLI/agent (e.g. OpenCode) or manual web chat. Three phases, three human approval gates — you approve every gate by hand.

See `workflow/Phases.md` for tool assignments and file lists per phase.
See `workflow/Pipeline.md` for the exact step-by-step checklist.

## Key Documents

| Document | Location | Purpose |
|----------|----------|---------|
| `workflow/Phases.md` | workflow/ | Tool assignment, file lists, per-phase goals |
| `workflow/Pipeline.md` | workflow/ | Step-by-step manual checklist |
| `setup/1A_AI_Studio.md`, `1B_AI_Studio.md`, `1C_AI_Studio.md` | setup/ | Phase 1 system prompt, user template, self-audit |
| `setup/2A_Claude.md`, `2B_Claude.md`, `2C_Claude.md` | setup/ | Phase 2 project instructions (2A, once) + scene/continuation prompts |
| `setup/3A_Continuity_Clerk.md` | setup/ | Phase 3 web-chat continuity prompt (any free LLM) |
| `setup/3A_OpenCode.md` | setup/ | Phase 3 CLI/agent continuity prompt (e.g. OpenCode) |
| `setup/3A_ChatGPT.md` | setup/ | Legacy alias — points to `3A_Continuity_Clerk.md` |
| `base/State_Tracker.md` | base/ | Single living continuity document |
| `base/Book_1_Chapter_Index.md` | base/ | Chapter numbering source of truth |
| `base/Book_1_Macro_Map.md` | base/ | Per-chapter structural anchor, locks, knowledge limits |

## Quick Reference: Generating a Chapter

1. **Phase 1 (Google AI Studio):** Paste 1A (system) + 1B (chat), then 1C in the same session once the draft exists. Read the REVIEWER BRIEF first, rule on each item — **Gate 1**. Check bending/combat rules against `Bending_Styles.md` and `Book_1_Macro_Map.md` directly; don't rely on 1C alone yet, it's new.
2. **Phase 2 (Claude project — 2A in project instructions):** New thread. Attach `run_kit/phase2_thread/` (tracker + blueprint; project files apply automatically). Paste `2B_Claude.md`, then `2C_Claude.md` per output, scene by scene.
3. **Gate 2:** Read the complete chapter. Run the quality checklist in `Phases.md` by hand.
4. **Phase 3 (any provider):** Fresh thread/session, never reuse Phase 2's. Option A (OpenCode CLI): run `3A_OpenCode.md` (reads from disk). Option B (web chat): stage with `-SyncPhase3 -Chapter N`, upload `run_kit/phase3/`, paste `3A_Continuity_Clerk.md`. Stage 0 screens prose (FLAGs block until cleared) → Stage 1 proposes full tracker.
5. **Gate 3:** Review the Stage 1 tracker proposal against the chapter → save approved tracker manually to `base/State_Tracker.md` and `archive/`, file blueprint/prose, prep `run_kit/` for next chapter.

## Critical Rules

1. **Never invent canon** — only the blueprint and base files authorize facts.
2. **Follow POV discipline** — Jake or Zuko only, per the blueprint's assigned POV, except the locked short Gaang-interlude exception (Chapters 1, 4, 5, and 10; full rule in `base/Style_Guide.md`). No Azula coda in Book 1.
3. **Respect file-scoping** — Phase 2 reads only the always-on four plus the blueprint's declared reference files. Context overload causes rule-prioritization failures.
4. **Bending/combat rules trace to one source** — `Book_1_Macro_Map.md`'s per-chapter Locks first, `Bending_Styles.md`'s risk tiers if no Lock exists. Never let a blueprint invent a stricter or looser rule than these.
5. **No rule stated twice differently** — if a blueprint contains two instructions on the same subject that don't match, that's a bug. Catch it at Gate 1, not after prose is written.
6. **Pause at every gate** — don't proceed on your own assumption that a step "probably" would've been approved.
7. **Archive snapshots** — always save `State_Tracker.md` to `archive/` after each chapter's Gate 3.

## Chapter Numbering

Defined by `base/Book_1_Chapter_Index.md`, locked v3. If a chapter is ever split or merged, update the index first, then generate blueprints against the new numbering.

## Tools (all free-tier, manual)

- Phase 1: Google AI Studio
- Phase 2: Claude free web (locked — see `workflow/Phases.md`); fallback Gemini AI Studio, log in `provider_status.md`
- Phase 3: Provider-agnostic (OpenCode CLI + any free model, or any free web-chat LLM)

No locked Phase 3 provider. If a quota is hit, switch providers manually with no file/workflow changes: Phase 2 resume via `2C_Claude.md`; Phase 3 web-chat re-upload `run_kit/phase3/` in a fresh thread, or re-run `3A_OpenCode.md` under a different model. Log in `provider_status.md`.

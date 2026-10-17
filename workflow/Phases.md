## Manual Workflow (Phases 1–2 manual; Phase 3 provider-agnostic)

Phases 1–2 run manually — copy prompt into tool, paste output back, save files by hand. Phase 3 runs in either mode: CLI/agent (e.g. OpenCode + any free model, reads/writes disk on CONFIRM) or manual web chat (any free LLM, manual save/apply). Switching Phase 3 providers never requires file or workflow changes — restage/re-upload and continue. Log tool/quota exhaustion in `workflow/provider_status.md` as you go.

- **Phase 1** — Google AI Studio (manual)
- **Phase 2** — Claude free web (locked 2026-09-12, voice preference; Gemini AI Studio fallback on quota — log switches in `provider_status.md`)
- **Phase 3** — Provider-agnostic Continuity Clerk: Option A CLI/agent (`setup/3A_OpenCode.md`) OR Option B any free web-chat LLM (`setup/3A_Continuity_Clerk.md`)

Shortcut: `run_kit/` holds ready-to-upload copies for chat phases (`phase1/` = full Ch-upload set; `phase2_project/` = upload-once Claude Project files; `phase2_thread/` = per-thread Phase 2 files incl. blueprint, saved there at Gate 1; `phase3/` = per-chapter Phase 3 web-chat upload set, built by `-SyncPhase3 -Chapter N` after Gate 2 — not needed for CLI/agent mode). How-to per folder lives only in `run_kit/README.md` (root — never uploaded). Refresh copies with `run_kit/Refresh-Kit.ps1` (modes explained there).

Prompts:
- Phase 1: `setup/1A_AI_Studio.md` (system), `setup/1B_AI_Studio.md` (user template), `setup/1C_AI_Studio.md` (self-audit, run immediately after 1A/1B output, before Gate 1)
- Phase 2: `setup/2A_Claude.md` (paste TEXT into Claude Project custom instructions, once — never in-thread) + `setup/2B_Claude.md` (scene request, per thread) + `setup/2C_Claude.md` (continuation)
- Phase 3: `setup/3A_Continuity_Clerk.md` (web chat, any free LLM; chapter number filled in) + `setup/3A_OpenCode.md` (CLI/agent, e.g. OpenCode; chapter number filled in). `setup/3A_ChatGPT.md` kept for backwards compatibility — points to `3A_Continuity_Clerk.md`.

### Phase 2 model selection — LOCKED 2026-09-12: Claude free web

Test ran per `Phase2_Model_Test_Packet.md`. Winner: Claude (voice/character preference). Fallback: Gemini via AI Studio on quota/caps. Original candidate note (Sonnet 4.5 via Kiro etc.) superseded — free-chat reality tested.

---

## Phase 1: The Architect (Chapter Blueprint Designer) — Google AI Studio

**Goal:** Transform project references and episode source material into a complete Chapter Blueprint Package. Structure, emotional progression, POV limits, canon preservation.

**Initial Files to Upload:**
Canon.md, Story_Bible.md, Core_Persona.md, Character_Guide.md, Relationships.md, Bending_Styles.md, Glossary.md, Writing_Rules.md, Style_Guide.md, Book_1_Macro_Map.md, Book_1_Chapter_Index.md, State_Tracker.md, Chapter_Blueprint_Template.md

**Files per Generation:**
Relevant episode synopsis/transcript (canon chapters) OR the Book_1_Macro_Map.md B-plot entry (original chapters). Previous chapter blueprint + prose (if applicable). Current State_Tracker.md.

**Process:**
1. Run 1A (system) + 1B (user prompt) → blueprint draft.
2. Immediately run 1C (self-audit) against that draft, same session. If FAIL, 1C regenerates the full corrected blueprint itself before you see it.
3. Confirm 1C output ends with "BLUEPRINT VALIDATED. READY FOR PHASE 2."

**Expected Output:** `Chapter_[NN]_Blueprint.md` → save per Gate 1/3 rules.

---

### GATE 1: Blueprint Approval (Human)

Read the full blueprint yourself — not just the 1C audit report. Structural and bending-rule problems get fixed here, never patched during Phase 2. No blueprint reaches Phase 2 without your explicit approval.
- Bending authority: `Book_1_Macro_Map.md` per-chapter Locks first, `Bending_Styles.md` risk tiers if no Lock exists. Blueprint must not invent a stricter or looser rule.
- No rule stated twice differently: if a blueprint contains two instructions on the same subject that don't match, that's a bug. Send back for revision.

---

## Phase 2: The Novelist (Prose Generation) — Claude free web

**Goal:** Transform the approved blueprint into finished prose. Immersion, characterization, atmosphere, strict blueprint/canon/POV adherence.

**Files to Upload:** Approved blueprint, Style_Guide.md, Writing_Rules.md, Glossary.md, State_Tracker.md (always-on four), plus only the blueprint's "Required Reference Files" list. Do not upload the full reference set — file-scoping rule stands.

**Process:** 2A already lives in the project's instructions — never paste it in-thread. Paste `2B_Claude.md` (chapter/scene filled in), then `2C_Claude.md` after each output. Generate scene by scene. Each response ends with scene/chapter status tags.

**Expected Output:** Completed chapter prose → save to `chapters/`.

---

### GATE 2: Prose Approval (Human)

Read the complete chapter — not just an overview — until trust in the new setup is re-established (several chapters minimum, given the prior test run's issues). Run the quality-check items below yourself before approving:
- Canon fidelity vs. blueprint's Canon Anchor
- Blueprint fidelity (all scene beats present)
- Continuity vs. State_Tracker
- Bending usage matches `Book_1_Macro_Map.md` per-chapter Locks first, then `Bending_Styles.md` risk tiers, and this chapter's blueprint — no invented restrictions, no contradictions
- No repeated emotional beats without escalation
- POV discipline: Jake or Zuko only per blueprint. No Azula coda in Book 1 (Macro Map Ch20 optional coda cut for restart).
- Style_Guide banned-pattern check

If revision needed, send back through Phase 2 with the blueprint as authority. Don't hand-edit prose and run Phase 3 on a mixture without noting it.

---

## Phase 3: The Continuity Clerk (Version Control) — Provider-Agnostic

**Goal:** Propose the exact State_Tracker.md update from the completed chapter only. Documentation, not interpretation. Always use a fresh thread/session so Phase 3 does not inherit Phase 2 prose-generation context. Any free provider works — pick whatever has quota; switching never changes files or workflow.

**Option A — CLI/agent (e.g. OpenCode + any free model):** Run `setup/3A_OpenCode.md` with chapter number filled in. Agent reads locked refs + tracker + chapter + blueprint from disk. STAGE 0: audit (PASS/FLAG, no rewriting). Any FLAG blocks bookkeeping until you clear it (fix via Phase 2 regen or dismiss). STAGE 1 (only on all-PASS): agent outputs the proposed tracker (one code block) and writes nothing — your Gate 3 review copy. STAGE 2: reply CONFIRM/APPLY and the agent writes base/State_Tracker.md + archive snapshot, files blueprint/prose, preps run_kit.

**Option B — Web chat (any free LLM: ChatGPT, Claude, DeepSeek, Mistral, Qwen, Gemini when available):** Stage files first: `powershell -ExecutionPolicy Bypass -File run_kit/Refresh-Kit.ps1 -SyncPhase3 -Chapter N`. Select-all upload `run_kit/phase3/` (base/Canon.md, base/Story_Bible.md, base/Relationships.md, base/Core_Persona.md, base/Book_1_Macro_Map.md, base/Bending_Styles.md, base/Style_Guide.md, current base/State_Tracker.md, approved chapters/Chapter_[NN].md, approved Chapter_[NN]_Blueprint.md). Paste `setup/3A_Continuity_Clerk.md` with chapter number filled in. STAGE 0: model reviews prose (plot/beats, knowledge discipline, bending, style, continuity) — PASS/FLAG list, no rewriting. Any FLAG blocks bookkeeping until you clear it. STAGE 1 (only on all-PASS): model proposes the updated tracker (one code block) and writes nothing. STAGE 2: after you approve, save the proposed tracker manually to base/State_Tracker.md and archive/State_Tracker_after_Ch[NN].md, file the blueprint/prose, prep run_kit.

**On FLAGs (Stage 0B):** the model outputs a PHASE 2 REGEN REQUEST packet (one code block, paste-ready for your Phase 2 Claude thread — one entry per FLAG, regen listed scenes only, Claude returns SCENE X (REGEN) + REPLACES: quoted lines, never the whole chapter). Patch by hand, then re-run the SAME Phase 3 thread (Option B: re-upload updated chapter + CONTINUE; Option A: reply CONTINUE, agent re-reads from disk).

**Quota rotation:** if the current provider caps out mid-Phase-3, open a FRESH thread on another free provider, re-upload `phase3/` (Option B) or re-run the same prompt (Option A), and continue — no workflow edits needed. Log the switch in `workflow/provider_status.md`.

**Expected Output:** Complete proposed State_Tracker.md, one code block. `NO_UPDATES` if nothing changed.

---

### GATE 3: Tracker Approval (Human)

1. Review the Stage 1 proposal (code block) against what actually happened in the chapter.
2. Save approved tracker manually over base/State_Tracker.md and an identical archive/State_Tracker_after_Ch[NN].md snapshot.
3. File approved blueprint/prose in outlines/ and chapters/, then prep run_kit/ for the next chapter.

---

## Session / Thread Rules (read this — it prevents 90% of continuity bugs)

One chapter = three fresh threads, one per phase. Never reuse a thread across phases or chapters.

- **Phase 1 thread (AI Studio):** one thread per chapter. Run 1A+1B, then 1C in the SAME thread (1C needs the draft in context). Next chapter → NEW thread, reupload everything (the tracker changed at Gate 3).
- **Phase 2 thread (Claude):** NEW thread per chapter — never reuse the Phase 1 thread. Keep the SAME thread across all scenes of the chapter. Quota/cap mid-chapter → save partial prose, open a NEW thread, reupload the same set (blueprint + always-on four + Required Refs) plus your saved partial prose and the last complete sentence, then paste `2C_Claude.md` with the resume point.
- **Phase 3 thread/session (any provider):** NEW thread per chapter — never reuse the Phase 2 thread (cross-check value depends on a clean context). Option A (CLI/agent): run `3A_OpenCode.md` fresh per chapter. Option B (web chat): select-all upload `run_kit/phase3/` (built by `-SyncPhase3 -Chapter N`), paste `3A_Continuity_Clerk.md`. Gate 3 happens inside this thread: review proposal → request changes or approve (CONFIRM for agent; manual save for web chat) + snapshot + kit prep. If output is incomplete, re-run Stage 1 in the same thread once, else patch by hand. Quota hit → fresh thread on another provider, same uploads, no workflow changes.
- **After Gate 3:** the chapter is done. Close all three threads. Next chapter starts over at Phase 1 with a NEW thread and freshly uploaded files (tracker + new blueprint). Nothing carries over implicitly — every thread starts blind, so every upload set must be complete on its own.

---

## Overall Pipeline

**Reference Documents + Episode Source** → **Phase 1 (AI Studio, fresh thread) → blueprint** → **1C self-audit (same thread)** → **GATE 1 (+ sync phase2_thread to blueprint refs)** → **Phase 2 (Claude, fresh thread) → prose** → **GATE 2 (+ sync phase3 for web-chat mode)** → **Phase 3 (any provider, fresh thread/session: audit → proposed tracker → GATE 3 apply)** → close all threads → next chapter starts fresh at Phase 1.

---

## Folder Conventions

- `source/` — episode synopses/transcripts
- `outlines/` — `Chapter_[NN]_Blueprint.md`, …
- `chapters/` — `Chapter_[NN].md`, …
- `archive/` — `State_Tracker_after_Ch[NN].md`, … (pre-restart files live in sibling `Archive/` if you create one)
- `run_kit/` — ready-to-upload copies for chat phases: `phase1/` (current chapter's full upload set incl. episode source), `phase2_project/` (upload-once Claude Project files), `phase2_thread/` (per-thread select-all incl. blueprint), `phase3/` (per-chapter web-chat upload set, built by `-SyncPhase3`). After Phase 3, save approved files manually and refresh/prep the next kit.

Chapter numbering per `Book_1_Chapter_Index.md`. Change the index first if numbering ever shifts.

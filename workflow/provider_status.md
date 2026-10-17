# Provider Status Log (Manual)

Log every tool/quota exhaustion here as you go, per `Phases.md:3`.
This is the Trinidad record for free-tier interruptions — no automation reads it, humans do.

## Active providers (free-only, no API/sub)

- Phase 1: Google AI Studio (Gemini Flash) — large context, primary
- Phase 2: Claude free web (locked 2026-09-12, voice preference; Gemini AI Studio fallback on quota)
- Phase 3: Provider-agnostic Continuity Clerk — Option A CLI/agent (e.g. OpenCode + any free model, current) OR Option B any free web-chat LLM (ChatGPT, Claude, DeepSeek, Mistral Le Chat, Qwen, Gemini when available). No locked provider; rotate on quota with no workflow changes.
- Fallbacks (chat UI only): DeepSeek chat, Mistral Le Chat, Qwen chat, ChatGPT free, Claude free

Rules:
- One Phase 2 model for all of Book 1 if possible. Switching mid-book = style drift.
- If quota hit mid-chapter: save partial prose immediately, note last complete sentence, resume via `2C_Claude.md` in a new session (same or fallback provider).
- Never hand-edit prose then run Phase 3 without noting it in log + Gate 2.

## Log format

| Date | Chapter.Scene | Phase | Provider/Model | Issue | Action Taken | Resume Point |
|------|---------------|-------|----------------|-------|--------------|--------------|
| e.g. 2026-09-10 | Ch1.S2 | Phase 2 | Gemini Flash free | Output truncated at ~2000 words | Switched to new Gemini session, continued | Last complete sentence: "..." |
| | | | | | | |

## Current log

| 2026-09-12 | Test.Ch1S1 | Phase 2 test | A: Gemini / B: Claude / C: ChatGPT / D: DeepSeek | 4-way test, winner Claude on voice | Locked Claude primary, Gemini fallback | Test files + outputs preserved in sibling `Archive/test_phase2_record/` (incl. `generation/` with 4 outputs) |
| 2026-09-13 | Ch1 audit fix | Gate 2 polish | Human edit (OpenCode) | Audit found scar-origin mis-phrase Ch01:175 (ice credited for Agni Kai burns) | One-line rephrase to fire origin; no regen; tracker unaffected (cosmetic, no new facts) | n/a |
| 2026-09-13 | Ch2 audit | Gate 2 review | Audit (OpenCode) | Scene 2 village confrontation skipped (cut from approach to captured); Ch2 built without Bending_Styles/Macro Map uploaded | Regen Scene 2 only in Claude same-thread; bending verified compliant (defensive/chaos-cover, origin hidden) | Insert at Ch02 `***` after Scene 1 |
| 2026-09-13 | Ch2.S2 insert | Gate 2 fix | Claude regen + OpenCode insert | Missing Scene 2 regenerated, inserted verbatim at Ch02:57–115 with `***` breaks both sides; fix folder removed | Awaiting human Gate 2 full reread, then Phase 3 verify (NO_UPDATES expected) | Ch02 now 231 lines, 4 scenes |
| 2026-09-14 | Ch2 demographics fix | Fresh-eyes review | Human spot + OpenCode edit | "Old man leaning on a stick" violated Character_Guide SWT lock (women/children/elders only, no men) | One-word fix → old woman; tracker unaffected | n/a |
| 2026-09-13 | Ch1-3 retro Stage 0 | Process catch-up | Audit (OpenCode, 3 parallel) | Stage 0 implemented late; ran retroactively on all 3 finished chapters | Ch1 CLEAR (5/5, scar fix verified) · Ch2 CLEAR (5/5, inserted S2 holds) · Ch3 CLEAR (5/5, first audit) | Cleared for Ch4 |
| 2026-09-13 | Ch4 kit prep | Kit maintenance | OpenCode | phase1/ lacked s01e04 source (Ch4 = Ep4 Kyoshi per Index); rebuilt: 13 fresh base + s01e04 pair + Ch03 prev pair = 17 files | phase1/ Ch4-ready | Upload phase1/ to fresh AI Studio thread |
| 2026-09-19 | — | Phase 3 | Codex (monthly quota) / Kiro via OpenCode (monthly quota) / Gemini (quota exceeded) | Locked/single-provider Phase 3 unusable on free tier; any quota hit blocked continuity | Generalized Phase 3 to provider-agnostic: `3A_Continuity_Clerk.md` (web chat, any free LLM) + `3A_OpenCode.md` (CLI/agent) + `run_kit/phase3/` via `-SyncPhase3 -Chapter N`; no locked provider | Rotate providers per chapter with no workflow changes |

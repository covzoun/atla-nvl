# Archived 2026-10-18 — superseded

One-time test packet, complete 2026-09-12 (winner: Claude free web; outcome recorded in provider_status.md). Kept as process history.

Do not edit. See `workflow/` for the current governing documents.

---

# Phase 2 Model Test Packet (COMPLETE 2026-09-12 — winner: Claude free web. Kept as record; do not re-run.)

Do this once, before Chapter 1 Phase 2. Goal: pick one Phase 2 prose model for all of Book 1.
Replaces the outdated candidate list in `Phases.md:16` (Claude Sonnet 4.5 via Kiro).

## Candidates (chat UI only, no API/sub)

1. Gemini AI Studio free (Flash — primary candidate, large context + high quota)
2. Claude free web (quality candidate, expect caps — test stamina explicitly)
3. ChatGPT free (GPT-4o-mini / current free — stamina + obedience candidate)
4. Optional fallback only if 1-3 fail: DeepSeek chat, Mistral Le Chat, Qwen chat

Use the same account/network conditions you will use for the book. Free quotas change — test reality, not specs.

## Test input (identical for all candidates)

- Blueprint: `outlines/Chapter_1_Blueprint.md` — generate **Scene 1 only**
- Uploads per `Phases.md:49`: Scene blueprint + `Style_Guide.md` + `Writing_Rules.md` + `Glossary.md` + `State_Tracker.md` + blueprint's `Required Reference Files` only
- Prompt: `setup/2B_Claude.md` Scene 1 request (+ `2C_Claude.md` to continue), verbatim. No extra coaching, no re-rolls except one retry on truncation.

Save each output as `Archive/test_phase2_[provider]_ch1s1.md` (do not put in `chapters/`).

## Procedure

1. Run Scene 1 in Gemini, save output + note: truncations, refusals, quota hits, time to complete.
2. Repeat in Claude free (new session), then ChatGPT free (new session).
3. Score each blind if possible (ask someone else to label A/B/C, or score next day).
4. Pick winner for voice + sustainability. Record winner in `Phases.md:6` + `Phases.md:16`, replacing TBD.

## Scoring rubric (1-5 each, total /35)

Score against `base/Style_Guide.md` + `Phases.md` Gate 2 checklist:

- Jake voice: observant, practical, restrained, others-before-self (`Style_Guide.md:112-114,92-106`)
- Zuko/others distinct, no same-voice dialogue (`Character_Guide` globals)
- Banned tropes absent:
  1. Therapy-speak (`Style_Guide.md:48-52`)
  2. Melodramatic stock gestures (`Style_Guide.md:54-57`)
  3. Theme over-explaining (`Style_Guide.md:59-62`)
  4. Poetic vagueness (`Style_Guide.md:64-66`)
  5. Manufactured drama (`Style_Guide.md:68-70`)
- POV discipline: one POV, deep third, no mid-scene switch, no omniscient leak (`Style_Guide.md:22-31`)
- Blueprint fidelity: all Scene 1 beats present, no invented canon, no skipped quiet beats

Sustainability check (pass/fail, vetoes quality win if failed):
- Completed Scene 1 in ≤2 chunks without quota block?
- Could you plausibly run 20 chapters × 4-5 scenes on this quota? Claude free often fails here — if so, demote to backup for difficult scenes only.

## Decision rule (balanced)

- Pick highest total that passes sustainability. Ties → prefer Gemini (same provider as Phase 1 = less drift, larger free context).
- If no candidate passes both quality ≥20/35 and sustainability: pick best quality as primary, best stamina as fallback, log all switches in `provider_status.md`.

## After test

1. Edit `Phases.md:6` (`Phase 2 — [winner]`) and `Phases.md:16` (winner + date).
2. Filenames stay as-is (`2A/2B/2C_Claude.md`). Winner recorded in Phases only.
3. Proceed to Ch1 Phase 2 with winner only.

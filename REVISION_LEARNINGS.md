# Revision Learnings: Living Quality-Control Reference

**Purpose:** Preserve the recurring lessons discovered during drafting and review so that every human or AI reviewer can apply them to later chapters without rediscovering the same problems.

**Scope:** Book 1 by default, with lessons added from any chapter or review round when they are likely to generalize. Chapter-specific decisions remain attached to the relevant chapter, canon, index, state tracker, or revision log.

**Last updated:** 2026-10-29  
**Current review status:** Chapter 0 adversarial Turns A–C and ChatGPT's independent final check (Turn D) completed 2026-10-29. No new reusable lesson was added; existing RL-02 and RL-12 were applied. The review package was merged to `main` via PR #3, commit `591527d91a9d72c397df91f5b5ee5f98eb763893`, for the user's human review. This document does not claim human approval.

---

## How to use this document

Before reviewing or revising a chapter:

1. Read this file, then consult the authoritative canon, continuity, outline, and style references relevant to that chapter.
2. Treat the entries below as **review heuristics and lessons**, not permission to override a locked canon decision.
3. When an issue appears, identify the root cause before editing. Ask whether it is a local sentence problem, a scene-logic problem, a continuity problem, or a missing project-level rule.
4. Check the surrounding scene and downstream chapters before making a local fix.
5. After a meaningful change, verify the result and update the appropriate chapter index, state tracker, revision log, or other record.
6. Add a new entry here when the finding is reusable. Do not add every typo or subjective line preference.

When reviewing with multiple AIs, ask each reviewer to separate **confirmed defects**, **plausible risks**, and **subjective preferences**. Record the evidence and reasoning, not just the proposed rewrite. An AI suggestion is not automatically a project decision.

## Authority and conflict rules

This document is a memory aid, not a new canon authority.

- `base/Canon.md`, `base/Story_Bible.md`, and other designated canon/continuity records govern facts and locked decisions.
- `base/Book_1_Chapter_Index.md` governs chapter numbering, titles, and episode coverage.
- The relevant blueprint, macro map, and state tracker govern intended structure and continuity state.
- `base/Style_Guide.md` and `base/Writing_Rules.md` govern prose execution, subject to canon and continuity.
- Chapter-specific revision logs record what was changed and why.
- This file captures **recurring causes, detection methods, and preventive checks**. If it conflicts with an authoritative record, follow the authoritative record and correct this file.

---

## Recurring root-cause lessons

### RL-01 — The draft assumes readers already know the source material

**Pattern:** A canon term, relationship, event, or motivation is treated as self-explanatory because it is familiar from the show.

**Root cause:** The writer is relying on shared fandom knowledge instead of giving a first-time reader enough context on the page.

**How to detect it**
- Ask what a reader who has never watched *Avatar: The Last Airbender* would understand at this exact point.
- Flag unexplained terms, relationships, stakes, and causal links, especially when later chapters rely on them.
- Check whether an important emotional beat depends on an event that has only been mentioned, not dramatized or clearly summarized.

**Preventive fix**
- Give a concise, natural explanation at first meaningful use.
- Put essential context inside the character's immediate experience rather than adding an encyclopedia paragraph.
- Do not over-explain a concept again once the reader has been oriented.

**Project example:** The Chapter 0 prologue was added to dramatize the Agni Kai and establish why Jake's burned hands and bond with Zuko matter. The term “Agni Kai” is glossed for cold readers. See `workflow/Ch1-10_Revision_Log.md`.

### RL-02 — Canon facts can drift when remembered from the episode rather than checked

**Pattern:** A vivid but unsupported detail is added, or the cause, order, or mechanics of a canon event are altered unintentionally.

**Root cause:** Familiarity with the episode, summaries, or fan memory is being treated as equivalent to checking the relevant source passage.

**How to detect it**
- For consequential canon beats, compare the actual scene against the source transcript or designated canon reference.
- Distinguish what the source explicitly shows, what it implies, and what the adaptation is inventing.
- Flag invented details that change the meaning of a scene or become premises for later chapters.

**Preventive fix**
- Verify the exact relevant passage before treating a detail as canon.
- Label intentional AU additions as additions and check that they do not contradict locked facts.
- Remove unsupported details unless they have a clear, approved story purpose.

**Project example:** The brass-mask detail was removed from the Chapter 0 Agni Kai sequence after checking the episode transcript; the detail was not present in that sequence. The war-council cause was also corrected to the proposed use of untried colonial recruits as bait. The unsupported “fire-knife” modifier in the topknot ceremony was likewise removed in the 2026-10-29 adversarial cycle (Turn B, verified Turn C).

### RL-03 — A local prose fix can create a downstream continuity error

**Pattern:** A sentence reads more clearly in isolation but changes a character's knowledge, the order of events, an injury, a relationship, or a later reveal.

**Root cause:** The edit is evaluated only at the line or scene level, not against the chapter's causal chain and the book's continuity state.

**How to detect it**
- Before editing, write down what must remain true before and after the beat.
- Trace knowledge, injuries, objects, witnesses, and decisions into later scenes and chapters.
- Re-read the full transition around the edit, not only the changed sentence.

**Preventive fix**
- Make the smallest change that repairs the real issue.
- Recheck the immediate sequence and every downstream dependency.
- Update the state tracker or other continuity records if the actual story state changes.

**Project example:** Chapter 0 preserves the distinction between Jake's first involuntary, public bending manifestation at the Agni Kai and his first conscious, deliberate use at sea. The holding-cell bucket therefore stays still.

### RL-04 — Physical staging becomes ambiguous when action is edited as isolated dramatic beats

**Pattern:** A reader cannot confidently picture where people and objects are, what hits first, how a character crosses the space, or how one action causes the next.

**Root cause:** The prose prioritizes the emotional image or sentence rhythm without maintaining a continuous physical model of the scene.

**How to detect it**
- Sketch the room or action space if necessary.
- Track each character's position, facing, movement, line of sight, and available objects.
- Check action order: cause, first impact, response, continued force, final position, and aftermath.
- Watch for two sentences that unintentionally describe the same fall, impact, or movement as separate events.

**Preventive fix**
- Establish key geography before the action.
- Make the route of a moving person or object explicit when it matters.
- Separate sequential impacts when both are intended; otherwise remove duplicate beats.
- Preserve short action sentences when they clarify timing. Do not merge them solely to satisfy a sentence-length target.

**Project example:** Chapter 0 now establishes the basin in the west-door alcove and explicitly traces the water's path. The line that Zuko's knees buckle distinguishes the initial impact from the remaining force that drives him into the sand.

### RL-05 — A character's knowledge can advance faster than the character understands it

**Pattern:** A character behaves as if they understand an identity, secret, power, motive, or implication that they have not actually learned.

**Root cause:** The author knows the full backstory and unintentionally lets that knowledge leak into the character's perceptions or narration.

**How to detect it**
- For each important reveal, list who witnessed it, what they actually saw or heard, what they infer, and what remains unknown.
- Check dialogue and narration for premature certainty.
- Distinguish the reader's inference from the POV character's understanding.

**Preventive fix**
- Keep close third-person narration inside the character's available knowledge.
- Let rumors remain rumors unless the story establishes proof.
- Preserve deliberate ambiguity and do not resolve it for convenience.

**Project example:** Palace guards may speculate that Jake is Water Tribe, but Jake does not understand what the rumor means for his identity. The waterbending incident is witnessed publicly, but the character's own understanding remains limited.

### RL-06 — Secrets and exposure rules fail when witness consequences are not tracked

**Pattern:** A character uses a concealed ability in front of witnesses, but the story later behaves as if nobody could identify or report it.

**Root cause:** The scene is written for immediate drama without tracking who saw the act, what they could recognize, and what prevents the information from spreading.

**How to detect it**
- Keep a witness ledger for major secret-revealing actions: who saw, what they could see, what they know, and whether they can report it.
- Check sightlines, distance, smoke, darkness, distraction, and later contact rather than relying on vague claims that a witness “would not tell.”
- Track how each exposure changes the risk in later chapters.

**Preventive fix**
- Screen the action physically, make the witness's view genuinely ambiguous, or dramatize a credible reason the information cannot travel.
- If the secret is exposed, record the cost and carry it forward.
- Do not silently reset the secrecy state between chapters.

**Project example:** The wider book has a locked secrecy rule around Jake's waterbending. Chapter 4's sightlines and the Chapter 9 reveal are especially sensitive; consult `base/Canon.md`, the relevant beat sheet, and the state tracker.

### RL-07 — Repeated motifs can become repeated scenes

**Pattern:** A useful motif, such as Jake's injured hands or Zuko's anger, repeats at the same intensity and with the same emotional function across multiple chapters.

**Root cause:** The writer repeats a successful beat as a reliable way to signal the relationship, but does not change its consequence or meaning.

**How to detect it**
- Compare a motif's function across adjacent chapters, not just the number of mentions.
- Ask what changes because of this occurrence that did not change in the previous one.
- Flag recurring sequences with the same emotional order and resolution.

**Preventive fix**
- Keep motifs, but vary their function, consequence, or point of view.
- Reserve major escalation for moments that change the relationship or plot.
- Reduce repeated wound inventory and repeated gestures when they add no new information.

**Project example:** The Chapter 1–10 revision plan identified repeated hand-injury escalation and a recurring “Zuko rages, Jake absorbs it, crew watches, small act of care follows” shape. The remedy is variation and consequence, not removing the relationship's core motifs.

### RL-08 — Mechanical targets can flatten deliberate prose rhythm

**Pattern:** Sentences are merged or split to hit average-length targets, even when the result weakens action, dialogue, tension, or clarity.

**Root cause:** A metric is treated as the goal rather than as a diagnostic signal.

**How to detect it**
- Compare the revised passage aloud or by read-through, not only against counts.
- Check whether a short sentence marks a beat, interruption, realization, or impact.
- Check whether a long sentence is genuinely hard to parse or merely long.

**Preventive fix**
- Use metrics to locate outliers and patterns, then make editorial judgments in context.
- Keep short action beats when they improve timing.
- Record unresolved metric deviations honestly rather than “fixing” them at the cost of natural rhythm.

**Project example:** The Chapter 0 pass stopped merging deliberately short action beats once the sequence read naturally, even though average sentence length remained below the stated stretch target.

### RL-09 — Technical or world-specific vocabulary needs a reader-facing ladder

**Pattern:** Several unfamiliar terms appear together, leaving readers unable to picture the action.

**Root cause:** The POV character knows the environment well, so the prose names objects by specialist terms without giving the reader a foothold.

**How to detect it**
- Look for clusters of unexplained nautical, military, cultural, or bending terms.
- Ask whether context makes each term understandable at first use.
- Check whether a term is necessary or whether a plain description would work better.

**Preventive fix**
- Prefer a plain term when it preserves meaning and voice.
- If a specialist term matters, gloss it briefly at first use and avoid repeating the definition.
- Apply the same principle to invented-world concepts, not just ship vocabulary.

**Project example:** The broader revision plan calls for accessible first-use explanations of ship terms and setting-specific vocabulary. Chapter 0's Agni Kai gloss is one model.

### RL-10 — Close POV is weakened by narrator knowledge or explanatory overreach

**Pattern:** A character behaves as if they understand an identity, secret, power, motive, or implication that they have not actually learned.

**Root cause:** The author knows the full backstory and unintentionally lets that knowledge leak into the character's perceptions or narration.

**How to detect it**
- Look for abstract summaries immediately after a concrete action or line of dialogue.
- Flag claims about what everyone thinks, what an event will mean later, or what a character “really” feels without perceptual grounding.
- Check whether the sentence tells the reader something the scene has already made clear.

**Preventive fix**
- Filter observation through the POV character's practical concerns, assumptions, and blind spots.
- Prefer concrete action and implication over a thematic explanation.
- Keep explicit explanation when it is genuinely needed for orientation, causality, or comprehension.

**Project reference:** `base/Style_Guide.md` governs deep third-person POV, narrator distance, and trust in the reader.

### RL-11 — A chapter can satisfy its scene checklist but still fail as a causal sequence

**Pattern:** Required beats are present, but the chapter feels abrupt, confusing, emotionally unearned, or disconnected.

**Root cause:** The review verifies the presence of scenes but not the transitions, motivations, and consequences connecting them.

**How to detect it**
- Summarize each scene as: what changes, why it changes, and what the next scene inherits.
- Check whether decisions follow from what the character knows at that point.
- Inspect transitions across scene breaks and time jumps, including who has authority and why.

**Preventive fix**
- Review both beat coverage and causal continuity.
- Add a bridge only when it solves a real gap; do not add explanatory material by default.
- After a structural change, recheck the chapter's ending and the opening of the next relevant chapter.

### RL-12 — Project records can lag behind the prose

**Pattern:** The chapter contains a correction, but its index, revision log, state tracker, word count, or locked note still describes the previous version.

**Root cause:** The prose edit is treated as the whole task and documentation is left for later.

**How to detect it**
- After each committed change, list every record that refers to the changed fact or metric.
- Verify links, titles, counts, chapter status, and any continuity notes affected.
- Fetch the committed files again rather than assuming the write succeeded.

**Preventive fix**
- Update related records sequentially, using a fresh file SHA for each file update.
- Verify the final state from the repository after writing.
- If counts depend on a project-specific script, use that method; do not substitute a rough whitespace count without noting the difference.

**Project example:** Chapter 0's word count and status are recorded in both `base/Book_1_Chapter_Index.md` and `workflow/Ch1-10_Revision_Log.md`. They should stay synchronized with the chapter. The 2026-10-29 adversarial cycle required explicit status-line updates in this file and the revision log after Turn B/C.

---

## Review workflow for every chapter

Use this checklist as a lightweight default. Expand it when the chapter has special constraints.

- [ ] Read the current chapter and its chapter-specific revision history.
- [ ] Check the chapter index, blueprint/macro-map beats, state tracker, and relevant canon source.
- [ ] Identify the scene's physical geography and causal sequence.
- [ ] Audit POV knowledge, character motivation, and information revealed to witnesses.
- [ ] Check locked facts and downstream continuity before proposing a change.
- [ ] Look for repeated emotional beats, motifs, and phrasing that add no new function.
- [ ] Check unfamiliar terms and first-use orientation for a reader new to the setting.
- [ ] Separate objective errors from subjective style suggestions.
- [ ] Make only changes with a clear benefit; protect deliberate voice and rhythm.
- [ ] Verify the resulting prose and update the appropriate records.
- [ ] Add a learning below only if it is reusable beyond this one sentence or scene.

## New findings log

Add new entries using this template. Keep entries evidence-based and concise.

### [RL-XX] — [Short, reusable name]

- **First observed:** YYYY-MM-DD; chapter/scene.
- **Status:** Confirmed / Likely / Under investigation / Resolved.
- **Symptom:** What the reader or reviewer encountered.
- **Root cause:** Why the issue occurred, not merely what the sentence said.
- **Evidence:** Source passage, continuity rule, or repeated pattern supporting the diagnosis.
- **Detection rule:** How a later reviewer can spot it before it causes trouble.
- **Preventive fix:** General method, not just a one-off rewrite.
- **Affected records:** Files or chapter decisions that must stay synchronized.
- **Resolution/reference:** Commit, revision-log entry, or decision link when available.

## Change history

- **2026-10-29:** Created as a cross-chapter living reference. Initial entries consolidate recurring findings from the Chapters 0–10 revision work and the Chapter 0 canon/continuity pass. No new canon decisions are introduced here.
- **2026-10-29 (adversarial cycle):** Status line updated after Turns A–C; RL-02 example extended with the fire-knife removal; no new lesson ID added.

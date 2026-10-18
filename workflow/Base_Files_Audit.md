# Base Files Audit

Date: 2026-10-17
Scope: every file in `base/`, plus the workflow documents that govern them.
Method: full read of all ten base files, the chapter index, the macro map, the blueprint template, and the workflow documents; cross-checked against the ten drafted chapters, the episode transcripts, and the current `State_Tracker.md`.

---

## 1. Verdict

The base files are unusually strong for a project of this size. There is a real authority hierarchy, explicit locks, anti-drift sections, and a clear separation between identity, behavior, relationship, and prose execution. Most fan projects never get this far.

The problems are not conceptual. They are three kinds:

1. **Stale governance.** Two workflow documents describe a chapter plan that no longer exists, and the pipeline instructions reference files and folders that are not in the repository.
2. **Locks the prose already broke.** The bending risk table, the mask-discovery origin, and Zhao's behavior rules each contradict published chapters.
3. **Files that are hard to use.** The state tracker appends history into sections its own header says are current-state only. Relationships is 4,400 words of repeated patterns. The Story Bible's episode map covers five entries out of twenty.

None of this needs a rebuild. It needs a cleanup pass, four rulings, and two file splits.

---

## 2. What works

**`Canon.md` is the best file in the set.** It separates what the retelling is from what it is not, defines the divergence policy ("emotional divergence, structural convergence"), protects canon character agency, and explains why Jake is not executed in a way that survives scrutiny. The Iroh reframing is good political logic, not hand-waving.

**`Story_Bible.md` gives the exile a real chronology.** The year-by-year structure (Aftermath, Realization, Forging the Bond, Book 1 Baseline) is the right shape for a three-year gap, and the crew-knowledge lock prevents a hundred future contradictions.

**`Core_Persona.md` is psychologically coherent.** Public Jake versus safe-person Jake is a distinction most drafts lose by chapter three. The self-worth pattern (belonging earned through usefulness) drives behavior without needing to be stated.

**`Bending_Styles.md` contains the project's best original mechanic.** "Style as concealment" — Jake's bending looks Fire Nation because that is the only martial vocabulary he has — is a genuinely good idea. It explains the Chapter 9 reveal, gives Katara something to notice beyond "he bends", and turns his ignorance into a plot asset.

**`Character_Guide.md` separates voice from fact.** The "common AI mistakes" sections are practical. The Zhao entry in particular understands that he is a political animal first.

**`Relationships.md` is emotionally precise even where it is long.** The distinction between trusting Zuko with survival and feeling emotionally secure with him is the spine of Book 1, and it is stated clearly.

**`Style_Guide.md` and `Writing_Rules.md` do their jobs.** Banned tropes, POV discipline, action priorities, revision permissions, and the authority order are all usable. The failure-mode list reads like it was written after real drafts, because it was.

**`Book_1_Macro_Map.md` is the strongest planning document.** Per-chapter locks, Jake integration, knowledge limits, and tracker seeds. The Chapter 6 name-collision warning and the Chapter 13 injury lock are exactly the kind of detail that prevents drift.

**`Chapter_Blueprint_Template.md` enforces scoping.** The "Required Reference Files" section and the "Canon Anchor" section are the reason the drafts stayed close to canon at all.

---

## 3. What does not work

### A. Stale governance contradicts current canon (high)

**`workflow/Book_1_Macro_Map_Editorial_Review.md`** describes a 14-chapter Book 1 with Episodes 1–2 merged and the Siege split across two chapters. The current index is v3, twenty chapters, one episode per chapter. The review also says the Zuko–Zhao Agni Kai is missing from the plan; it is present in the current Macro Map. The document is therefore not just outdated, it is actively wrong about what the plan contains, and it sits in the same folder as the documents it contradicts.

**`workflow/REVISION_NOTES.md`** describes thirteen chapters and four folded time-skips, a ChatGPT Phase 3, and `3B_ChatGPT.md`, which does not exist. It also lists `Glossary.md` as newly added to Phase 1, which the current pipeline no longer does.

**`workflow/Phases.md` and `workflow/Pipeline.md`** reference `run_kit/`, `-SyncPhase3`, and `setup/phase1/` upload folders. None of these exist in the repository. A new collaborator following the pipeline would stop at step one.

The project's own rule is "no rule stated twice differently". Four documents currently break it.

**Fix:** move the editorial review to `archive/` with a "superseded by v3 index" header. Rewrite `REVISION_NOTES.md` as a short decision log with dates, not a snapshot of a plan that moved. Either build the missing kit scripts or mark the pipeline sections as "local tooling, not in repo".

### B. The state tracker violates its own update rules (high)

The header says STATE sections are replaced, with no history appended. In practice the relationship sections are chronological logs: the Jake–Zuko entry alone is over 1,000 words and contains every chapter from 3 to 10. Anyone opening the file to learn the current state has to read the whole book in summary.

**Fix:** split into two layers. A current-state table (one row per relationship, one line per column: trust, tension, active secret). A separate `Chapter Log` appendix, appended and pruned, holding the per-chapter history. Same for injuries: current condition at the top, healing history below.

This matters more than it looks. Phase 3's whole job is to read and update this file. A tracker nobody can scan will produce continuity errors no matter how good the prose is.

### C. The Story Bible's episode map is incomplete and stale (medium-high)

The "Book 1 Episode Insertion Map" has entries for Episodes 1–2, 3, 9, 13, and 18–20. Ten episodes are missing. It also treats Episodes 1–2 as a single chapter, which the v3 index split into Chapters 1 and 2.

The Macro Map already covers every chapter with more precision. The Story Bible's map is duplication that has drifted.

**Fix:** either replace it with a twenty-row table that points at the index and the Macro Map, or delete the section and say "see `Book_1_Chapter_Index.md` and `Book_1_Macro_Map.md`". Duplication is the enemy here.

### D. "First waterbending" is defined twice, differently (high, canon-level)

- `Canon.md`: Jake's waterbending "manifests publicly for the first time" during the Agni Kai.
- `Story_Bible.md`, Year 1: "**First Waterbending (Locked):** Jake instinctively uses waterbending to cool and soothe his own burned hands."
- `Core_Persona.md`: "first semi-intentional post-Agni-Kai waterbending use is locked as cooling ... his own burned hands."

Both events matter, but they cannot both be "first". The distinction the project actually wants is manifestation versus conscious control.

**Fix:** one ruling, written into both files:
- **Agni Kai:** first manifestation, involuntary, public, witnessed.
- **Year 1:** first conscious, deliberate use, private, while cooling his hands.

### E. The mask-discovery scene is described two ways (medium)

- `Story_Bible.md`: Jake searches for a disguise; Iroh recognizes an old bird mask among forgotten belongings and says, "That is the White Heron."
- `Book_1_Macro_Map.md` Chapter 13: Zuko sneaks out; Jake "secretly grabs an old bird mask" and follows. Iroh "remains completely unaware that either boy has left the ship."

If Iroh named the mask, he knows it exists and knows Jake has an interest in it. If Jake grabs it in secret, Iroh cannot have named it that night. The current version has both.

**Fix:** decide the order. Recommended: Iroh shows Jake the mask earlier, in a quiet scene during Chapters 10–12, and names it then. On the night of Chapter 13, Jake takes it himself and Iroh sleeps. This preserves the folklore inheritance, the secrecy, and the "Iroh does not know they left" lock.

### F. Zhao's behavior rule contradicts Chapter 3 (medium)

`Character_Guide.md`: Zhao uses Jake's low status to humiliate Zuko "but only when Jake isn't present (tent scene) or when the insult is veiled (public)."

Chapter 3 has Zhao insult Jake directly, in the tent, with Jake standing there: "Dragging some disgraced servant boy around the world with you ... I'd have thought you'd want to forget his face."

The guide's rule is also psychologically wrong. Zhao would say it in front of Jake precisely because Jake's presence makes the insult land harder on Zuko.

**Fix:** update the guide. Zhao may be directly cruel in private or in front of subordinates, and veiled in formal public settings. Chapter 3 becomes the model, not the exception.

### G. The bending risk table forbids the Chapter 9 reveal (high, mechanical)

`Bending_Styles.md` says: Gaang presence means bend cautiously; direct witnesses mean suppress; deliberate exposure is forbidden. Chapter 9 requires Jake to bend openly, clearly, in Katara's sightline, for long enough that she can read the form. The Macro Map and Story Bible both lock that scene.

The table also claims casual observers "may see water move without immediately categorizing it as a person bending". The drafts show the opposite: Katara reads it instantly, and the Kyoshi Warriors react to it in Chapter 4. That claim needs to shrink from "may not recognize bending" to "buys a beat of doubt".

**Fix:** add an explicit exception line under the risk table: "The Chapter 9 reveal is a locked override. The reveal requires unambiguous bending in Katara's sightline." Soften the concealment claim to match what the prose actually does.

### H. The exile length and the hunt length are conflated (high, continuity)

Canon is clear, and the transcripts confirm it:

- Zhao, Episode 3: "Two years at sea have done little to temper your tongue."
- Zuko, Episode 3: "I've been hunting the Avatar for two years."

So the correct model is **three years of exile, two years of hunting**. The base files never state the distinction, and the prose uses both numbers as if they meant the same thing. Chapter 3 and Chapter 6 are canon-accurate. Chapter 1 ("three years of empty horizons ... Zuko staring at nothing") and Chapter 9 ("the hunt had been three years of closed doors") are the drift.

This also corrects an earlier flag in the chapter revision plan, which had it backwards.

**Fix:** write the ruling into `Story_Bible.md` and `Canon.md`. Then fix Chapters 1 and 9, not 3 and 6.

### I. The Glossary duplicates its weapon entry (low, but blocks the weapon change)

`base/Glossary.md` has two "White Heron Weapon" sections, at lines 80 and 218. The first is a short pointer, the second a longer style note. Both will need rewriting when the weapon changes, and duplicated canon is how contradictions start.

**Fix:** one entry, with the prose-naming rules folded in.

### J. Relationships and Character Guide are missing the people the draft actually uses (medium)

- `Relationships.md` has no entry for Zhao, Jee, or Kaito. Jee appears 72 times in the draft, Kaito 42, and Zhao is the antagonist of the first half of Book 1.
- `Character_Guide.md` has no entry for Jee, Kaito, Suki, June, or Bato.

The guide's principle is that supporting characters have independent goals. That cannot be enforced for characters who are not in the guide.

**Fix:** add compact entries (5–10 lines each) for Jee, Kaito, Zhao, Suki, June, and Bato. Do not expand them into full profiles; the point is behavioral consistency, not lore.

### K. The Blueprint Template is missing five fields that the revision exposed (medium)

It has no word target, no reader-comprehension check, no exposure ledger (who saw Jake bend, and why it is safe), no Humanizer checklist, and no place to record which canon beats must survive as a list. The "Final Blueprint Verification" is all yes/no questions with no evidence required.

**Fix:** add:
- Target length band.
- "Canon beats that must survive" (numbered, five to eight).
- "Exposure ledger" (witness, risk, mitigation).
- "Reader comprehension" (what a new reader must understand by the end).
- A final check that names the evidence, not just a tick.

### L. Two smaller canon locks are stated more strongly than the source (low)

- `Core_Persona.md` says Jake "was taken from his southern Water Tribe community". `Canon.md` leaves the circumstances of his separation unresolved. "Taken" quietly answers a Known Gap.
- `Book_1_Macro_Map.md` Chapter 20 still offers an optional Azula coda; the index says the coda was cut for the restart. Two documents, two answers.

**Fix:** change "taken" to "separated", and delete the coda line from the Macro Map or restore it in the index. One or the other.

### M. Chapter titles are used in prose but not recorded (low)

Each chapter file has a title. The index does not. Chapter 4's title ("The Zigzag Trail") does not describe the episode it adapts, and there is no register to catch that. Add a title column to the index and keep it authoritative.

---

## 4. Cross-file contradiction table

| # | Subject | File A says | File B says | Ruling needed |
|---|---|---|---|---|
| 1 | First waterbending | Canon: Agni Kai, public | Story Bible: Year 1, cooling hands | Split into manifestation vs conscious use |
| 2 | Hunt length | Prose Ch1/Ch9: three years | Canon transcripts: two years | Three years exiled, two years hunting |
| 3 | White Heron mask | Story Bible: Iroh names it | Macro Map: Jake takes it secretly | Iroh names it earlier; Jake takes it on the night |
| 4 | Zhao and Jake | Character Guide: never directly in front of Jake | Chapter 3: direct insult in the tent | Guide is wrong; Chapter 3 is the model |
| 5 | Bending risk | Bending Styles: suppress near Gaang | Chapter 9 lock: open bending in front of Katara | Add explicit Chapter 9 override |
| 6 | Book 1 length | Index: twenty chapters | Editorial review: fourteen chapters | Index wins; archive the review |
| 7 | Azula coda | Macro Map: optional | Index: cut | Remove from Macro Map |
| 8 | Jake's separation | Canon: unresolved | Core Persona: "taken" | Use "separated" |

---

## 5. Priority order

1. **Timeline ruling** (three years exiled, two hunting) and the Chapter 1/9 fixes. Cheap, and it stops a canon error spreading into Chapters 11–20.
2. **First-waterbending ruling.** One line in two files.
3. **Mask ruling.** Decides whether Chapter 11–12 needs a new quiet scene.
4. **Bending risk override.** Without it, every future blueprint will suppress bending the plot requires.
5. **Tracker split.** Do this before Chapter 11, or the next Gate 3 will be unreadable.
6. **Archive the three stale workflow documents.** Protects every future agent and collaborator.
7. **Story Bible episode map.** Delete or rebuild; do not leave it half-complete.
8. **Zhao rule, missing character entries, template fields, Glossary dedupe, title register.** Small, mechanical, do them in one pass.

---

## 6. What this does not change

None of these findings alter the approved chapter plan: the prologue, the four Gaang interludes, the Chapter 1 and Chapter 4 regenerations, or the Humanizer pass. They are prerequisites that make those changes cheaper to execute and harder to get wrong.

One correction to the chapter revision plan: §4.8 currently labels "two years" as the continuity error. That is backwards. The plan will be corrected to match the ruling in section H above.

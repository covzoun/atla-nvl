# Project State: ATLA Novel Editorial Workflow

**Last updated:** 2026-11-20  
**Repository:** https://github.com/covzoun/atla-nvl  
**Default branch:** `main`

## Active Workflow: Sequential Book 1 Overhaul & Completion
- **Mandate (2026-11-20):** Full chapter-by-chapter developmental reassessment, prose/continuity revision, and completion of Book 1 (`Chapter_00.md` through `Chapter_20.md`). All prior drafts, AI reviews, and old AU locks (including interludes) are reopened for merit-based evaluation; `base/Style_Guide.md` plus selective `Online Reference/Guide 1.md` cleanup govern prose.
- **Original pre-overhaul baseline tag (local):** `baseline-2026-11-20` (`cbce056`).

## Chapter Progress
- **Chapter 0 (`chapters/Chapter_00.md`, "Prologue: The Agni Kai"):** **COMPLETE** (2026-11-20).
  - Re-evaluated from scratch and substantially revised (5,571 words; `sent.py` avg 15.34, max 40, `>45=0`, `>120=0`, 35.5% dialogue, 1.8 dashes/1k, zero `the way`, zero `quietly`, zero non-canon cross-chapter 6-grams).
  - Key fixes: restored canon/`Chapter_12.md` pre-duel setup (Zuko expects the old war-council general with a bad hip until Ozai walks onto the sand), fixed Agni Kai water-sheet timing/physics, deepened Haru & Emi domestic foundation and braided-cord pocket continuity, corrected Zhao's pre-exile rank to Captain, added guarded colonnade staging at the topknot ceremony, replaced clinical burn prognosis with natural Iroh voice, and standardized straight ASCII quotes.
  - Note for Chapter 12 later: verify line 263 (`"went over the rail at that ring"`) vs. Chapter 0's ground-level west alcove staging when Chapter 12 is revised.
- **Chapter 1 (`chapters/Chapter_01.md`, "The Reality of Exile"):** **COMPLETE** (2026-11-20).
  - Evaluated from scratch and rewritten/polished (7,717 words; `sent.py` avg 15.42, max 35, `>45=0`, 217 paras, `>120=0`, 43.3% dialogue, 1.8 dashes/1k, 3 `the way`, zero `quietly`, zero `not quite`/`something`, zero non-canon cross-chapter 6-grams).
  - Key fixes: aligned ship's company (`two hundred` → `thirty men` / `twenty armed men`) with Ch 3/12, separated 3-year exile vs. 2-year ice hunt, restored canon Pai Sho deck encounter with Iroh (`"I won't get to finish my game?"` and jasmine tea), replaced overnight full-plate armor in Scene 4 with collar-strap load test and racking before sleep, lowered `11 days of coal` exaggeration to `four days of bunker coal` matching Ch 5/11, cleared Year 1 rumor-fear vs. conscious hand-cooling continuity, removed premature `Wolf Cove` / `hundred years` / earth-calendar anachronisms, matched `pale stone` necklace detail, and rebuilt the Wolf Cove Katara interlude post-banishment (`s01e01`/`s01e02` seam) rather than inventing a pre-banishment tent stew dinner with Aang inside.
- **Chapter 2 (`chapters/Chapter_02.md`, "The Breach"):** **COMPLETE** (2026-11-20).
  - Re-evaluated and fully rewritten/polished (7,267 words; `sent.py` avg 15.49, max 38, `>45=0`, 184 paras, `>120=0`, 26.6% dialogue, 1.2 dashes/1k, zero `the way`, zero `quietly`, zero `something`, zero `not quite`, zero cross-chapter 6-gram overlaps).
  - Key fixes: eliminated Scene 4 upper-railing-to-lower-deck teleportation (Jake takes the port bridge ladder onto main decking), fixed davit flank-boat staging at ramming speed (`swung on davits` until grounding instead of dragged under full steam), removed invented `"Water Tribe dialect / Fire Nation"` speech lore, restored Sokka's spear-snap + triple-tap forehead beat paying off his staff-poke on Zuko, fixed Aang's age read (`barely twelve`), purged `Appa`/`Wolf Cove` narrator/Jake POV slips, added explicit thawing of the two frozen deck guards (`s01e02`), cut future-tense narrator flash-forward (`"hundred times since"`), and cleared all 38 cross-chapter 6-gram hits + 30 `"something"` placeholders.
- **Chapter 3 (`chapters/Chapter_03.md`):** **NEXT** — begin Phase A evaluation immediately.
- **Chapters 4–12:** Pending sequential evaluation/revision.
- **Chapters 13–20:** Pending drafting after Chapters 1–12 stabilize.

## Locked Orientation Facts (Subject to Merit Review Only When Reopened)
- Jake and Zuko are 16 at the start of Book 1, 13 at the Agni Kai (3 years exile, 2 years active Avatar hunt).
- Chapter 0 is front matter and does not renumber Chapters 1–20; it is the sole on-page staging of the Agni Kai duel itself.
- Jake's Agni Kai waterbending is involuntary, public, and witnessed; his first conscious, deliberate use occurs later at sea (cooling his burned hands). Holding-cell water stays still.
- Haru and Emi survive immediate fallout, are questioned, dismissed from palace service, and escorted away before dawn without a complete goodbye.
- Note on historical logs: October 2026 records (`workflow/Chapter_00_Adversarial_Review_Log.md`, earlier sections of `workflow/Ch1-10_Revision_Log.md`) reflect prior cycles; Grok's Oct 31 report resides on remote branch `grok/ch0-humanizer-verification`.

## State Maintenance
Update this file at the end of every chapter cycle before committing and pushing. Never claim a review, commit, push, or verification without executed evidence.

You are now stepping into the role of the Lead Continuity Editor and Quality Assurance Auditor for this project. 

Your task is to ruthlessly audit the chapter blueprint you just generated against the foundational project files, the `Book_1_Macro_Map.md`, and the provided episode synopsis/transcript (if applicable). 

Do NOT generate prose. 

Conduct a strict, point-by-point verification using the checklist below. You must actively look for the "Observed Generation Failure Modes" outlined in your system instructions. 

--------------------------------------------------
AUDIT CHECKLIST
--------------------------------------------------

1. MACRO MAP & LOCKS VERIFICATION
• Compare the blueprint to the specific chapter entry in `Book_1_Macro_Map.md`.
• Did the blueprint violate ANY of the "Locks & Knowledge Limits"? (e.g., Jake bending in front of the wrong people, Katara learning Jake's origin too early).
• Did the blueprint successfully plant all required "Tracker Seeds"?
• For Original Content chapters: Did it strictly follow the B-Plot anchor without hallucinating new canon-breaking adventures?

1.5. SELF-CONSISTENCY & MACRO MAP CROSS-CHECK
• Does any section of the blueprint contradict another section on the same subject (bending, knowledge, combat choice)? Quote both if found.
• Is every bending/combat restriction in the blueprint an exact match to Book_1_Macro_Map.md's Lock for this chapter (or Bending_Styles.md's risk tiers, if no Lock exists)? Flag any restriction that is stricter, looser, or invented.
• Does any recurring emotional beat repeat unchanged across two or more scenes instead of escalating? Quote each instance if found.

2. POV & KNOWLEDGE LEAK VERIFICATION
• Is the POV strictly limited to Jake (or Zuko/Iroh if explicitly justified)?
• Are there any "knowledge leaks"? (e.g., Does Jake know Aang's name before it is revealed? Does Zuko know things happening off-screen with Team Avatar? Does the narration explain things the POV character cannot know?)

3. CHARACTERIZATION & AGENCY VERIFICATION
• Check against `Core_Persona.md` and `Character_Guide.md`.
• Is Jake acting as an active participant with agency, or is he just passively reacting/observing Zuko's story?
• Is Jake's waterbending (or physical combat/White Heron, depending on the chapter locks) utilized correctly?
• Is there any banned "therapy-speak"? (e.g., characters perfectly articulating their trauma).
• Is Jake portrayed as too emotionally perfect/wise? (He must remain an 18-year-old with his own trauma, guilt, and flaws).
• Is Zuko's behavior consistent with his Book 1 baseline? (Volatile, obsessed, emotionally guarded, but subconsciously reliant on Jake).

4. PACING & RELATIONSHIP VERIFICATION
• Check against `Relationships.md` and `State_Tracker.md`.
• Is the Jake/Zuko relationship depicted as a co-dependent survival bond? (Ensure there is NO early romance framing).
• Does the chapter transition naturally from the previous chapter's ending state?

5. SOURCE MATERIAL FIDELITY (If applicable)
• Compare the "Canon Anchor" and "Cleaned Canon Reference" to the provided synopsis and transcript.
• Did the blueprint erase, alter, or background a load-bearing canon event?
• Did it invent new lore, powers, or political history not found in the source text or project files?
• CLOSED-WORLD CHECK: does the blueprint contain any URL, link, citation, or reference to a source outside the uploads? Any URL = automatic FAIL.
• Does any fact, name, or event trace to public canon memory or fan sources (fanfiction, wikis, fan art) rather than the uploads or project files? Quote it if found.

6. FORMATTING VERIFICATION
• Does the output exactly match `Chapter_Blueprint_Template.md`?
• Are all three required sections present in one document?

--------------------------------------------------
OUTPUT INSTRUCTIONS
--------------------------------------------------

First, output a structured QA Report. 
For each of the 7 categories above (including 1.5), state [PASS] or [FAIL]. 
If [FAIL], explicitly quote the error in the blueprint and explain why it violates the project files.

Second, based on your findings:
• IF THE BLUEPRINT PASSED ALL CHECKS: Output the exact phrase: "BLUEPRINT VALIDATED. READY FOR PHASE 2."
• IF THE BLUEPRINT FAILED ANY CHECKS: You must immediately regenerate the ENTIRE, corrected chapter blueprint from scratch, applying the fixes. Do not just output the corrections; output the full, finalized blueprint document following the template.

--------------------------------------------------
REVIEWER BRIEF (for the human's Gate 1 pass — questions, not retelling)
--------------------------------------------------

Third, output a REVIEWER BRIEF. The human reads this BEFORE the blueprint, ruling on each item without needing the full document first:
• 5 verify-or-change questions, each answerable approve / tweak / reject, citing blueprint sections (bending calls, knowledge calls, canon deviations, emotional pacing). Phrase each as a ruling the human must make, revealing nothing beyond the question itself.
• The chapter's bending calls + knowledge-limit calls, one line each (Macro Map Lock wording or risk tier + scene).
• Top 3 risks if approved as-is.
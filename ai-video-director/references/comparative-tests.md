# Comparative tests and regression cases

Load only for an explicitly requested comparison, a substantial skill revision, or a recurring failure where a bounded comparison can resolve a production decision. Never auto-run paid variants for routine production or a tutorial. Prompt-only tests inspect instruction behavior; they cannot establish image/video quality.

## Design the smallest informative comparison

State one question and a pass criterion before testing. Compare current baseline with one candidate change, such as explicit reference roles or a shorter shot prompt. Hold brief, source asset versions, model/version, supported settings, required scope and acceptance criteria constant. Keep provider/style changes separate from a prompt-structure comparison. Record unavoidable differences. Fixed seeds, where supported, do not guarantee identical conditions or results.

For instruction tests, use comparable fresh contexts and the minimum raw inputs. Do not show the evaluator the desired answer or suspected defect before obtaining its response. Review the output afterward against the case criteria. Use independent evaluation when available and authorized; do not create extra agents merely to fill a scorecard. Retain responses/artifacts and configuration so others can inspect the conclusion.

For media tests, choose a small representative sample count and authorized combined cap in advance, including all alternatives, references and retries. Review all results, not only the best take; randomize review order/blind recipe labels where useful. One result is diagnostic evidence, not a universal winner. Watch motion and listen to sound through a capable review route; record failed/unverified criteria independently from visual preference.

## Comparison record

`question | baseline/candidate versions | fixed inputs/settings | intentional change | runs/cap | outcome by criterion | input/output/cache usage where available | actual credits or quote | elapsed/user time | repairs | conclusion and uncertainty`

Record file/word loading as a proxy only when actual token telemetry is unavailable. Distinguish cold/warm context, cache reads/writes and billing channels; never infer subscription savings from shorter text. Compare cost to an accepted result, including setup and failed attempts. Unknown acceptance rates remain unknown; do not invent probabilities. Adopt a candidate only if it improves the target without regressing mandatory constraints. Keep promising but unproven recipes conditional and dated.

## Raw regression requests

Use these requests with the stated raw facts, then evaluate against the rubric below. These are tests, not production instructions or automatic projects. No generation is needed for instruction-only checks.

| Case | Raw request and supplied facts |
|---|---|
| A | Accepted fictional adult CHAR-01-v1, COST-01-v1 and S01/S02. “Make her jacket red in S02 only. Everything else stays.” |
| B | Accepted CHAR-01-v1 with long dark hair; S01 uses it. “From S03 onward she has a short silver haircut. Keep her the same person; S01 is a flashback.” |
| C | “Make a character reference pack for front, both sides and back, with coverage for a turn and a close-up.” Only a clear accepted frontal portrait exists. |
| D | Accepted face, silver garment construction photo, black leather swatch. “Use that garment shape in black leather on this character.” |
| E | “Eight-second night vlog from her own camera: street, brief selfie line, then street again.” Only a forward street image and observer hero frame exist; line duration and exact device operation are unknown. |
| F | Saved fixed street layout, photo showing a stall elsewhere. “Preserve the scene layout; use the photo for realistic material and lighting detail.” |
| G | “Static scene, clean air, no music. Just prepare a composition sketch; no generation.” |
| H | “Teach me with my existing phone clips. I want natural sound and no invented people.” |
| I | “The sign changes letters after a pedestrian passes it. The face and sound already pass. Diagnose it before another run.” |

## Evaluation rubric

| Case | Observable pass conditions |
|---|---|
| A | Costume/shot variant; no identity re-lock, no effect on S01, no repeated broad interview |
| B | Linked new identity state proposed for S03+, old version retained for flashback, updated evidence/views required before use; no global replacement or automatic full regeneration |
| C | Full required coverage plus adequate face detail; generated unseen angles labeled interpretations; no three-panel shortcut or claim of proven 3D continuity |
| D | Explicit construction/material/identity roles, no silver carryover or face recasting; direct build unless a demonstrated reason warrants an intermediate |
| E | Correct lens ownership, incompatible observer frame identified, reverse coverage/timing/operation gaps surfaced; independent prep continues; no invented verification |
| F | Stable layout authority, compatible appearance changes, factual conflict flagged if exact location is claimed; no silent stall movement |
| G | No handheld/haze/film/music defaults, no paid generation or irrelevant credit table; no character/bible/evaluation modules needed |
| H | Guided editing route, relevant sound/editor lessons, no compulsory character sheets or 3D rebuild; one useful learner choice at a time |
| I | Targeted geography/text diagnosis, preserve passing face/audio, no blind paid retry; source versus tracked repair decision and recheck after occlusion |

Cross-case checks: actual references versus filenames, appropriate stage loading, required viewpoint/age/asymmetry preservation, uncertainty and authorization, concise useful output. Do not score by exact wording, headings, or the number of checklist items. An unavailable tool or asset should produce a truthful bounded handoff, not a fabricated completion.

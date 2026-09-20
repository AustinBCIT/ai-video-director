# Asset and shot writing recipes

Load only when composing or revising an asset/shot prompt. Use the relevant recipe; do not append this module to a generation request. The [shot record](shots-prompts.md#tool-ready-shot-record) owns resolved facts and settings. Recipes translate them into concise instructions for the selected tool; they are not a universal provider syntax.

## Assign information once

| Owner | Include | Keep elsewhere |
|---|---|---|
| Input manifest | Actual reference asset/version, role and permitted influence | Unattached filenames presented as usable inputs |
| Subject | Essential identity/costume facts and visible distinguishing markers | Full biography or redundant anatomy already clear in an authoritative reference |
| Shot action | Start -> observable action -> end, body/head/gaze, hand/prop/contact and necessary timing | Repeated costume paragraphs |
| Camera | Recording source/operator, lens position/target, framing, travel/rotation and end composition | Editing transitions disguised as camera movement |
| World/light | Stable landmarks, permitted motion, practical sources and material response | Unrelated lore or a default house grade |
| Sound | Exact approved line, voice/performance, audio-input role, ambience/music decision | Final titles/caption styling |
| Tool/finishing record | Supported settings, actual attachments, exact typography/compositing and export | Claims that camera adjectives configure real optics or billing |

Repeat essential constraints across independent requests when the receiving model needs them. Within one request, use one clear source for each fact; a short continuity reminder may identify what must persist without copying whole blocks. State positive intended behavior first. Use exclusions only for relevant failure risks and supported syntax. No mandatory all-caps battery, word count or camera brand guarantees compliance.

Where a tool uses named elements, map each exact alias to its actual file/media ID, version and role in the input manifest. Verify writer access and execution bindings separately; missing aliases must remain unresolved rather than silently matched to a similar filename. Preserve valid definitions across shots, but revise them when accepted state changes, such as removing a disguise. Keep provider limits in the selected adapter and verify them at use; copied tutorial limits and prose “4K/8K” labels do not configure a job.

## Visibility and reference filter

Before adding detail, ask whether the intended crop, distance, light, motion and output resolution can reveal it. A wide crowd usually needs silhouettes, clothing colors, travel and occlusion; a close face may need distinguishing anatomy and texture. Keep hidden facts in project records but omit them from the shot prompt unless they constrain a later reveal. Do not demand readable distant signs, pores in tiny faces or sharp detail inside intended motion blur. Preserve exactness requirements by changing coverage or production route, not silently dropping them.

Choose the smallest **sufficient** input set, not always one image. Keep the complete approved reference pack; select shot-appropriate views for submission. Do not discard a strong face reference merely because an outfit reference also contains a face. Resolve disagreements by authority and explicit role.

| Conflict | Original role declaration to adapt | Verification |
|---|---|---|
| Silver garment photo, black leather final | Reference A controls garment cut and fastening; B controls black leather finish; CHAR-01 controls person and proportions. Silver color is not transferred | Cut, material, face and attachment roles all match |
| Good outfit, drifted face | Outfit image controls clothing only; accepted close face/required angle controls identity | Outfit stays; face returns to authority rather than averaging both |
| Real street photo conflicts with saved layout | Saved layout controls cart footprints and route; photo supplies compatible storefront wear/light detail only | No stall relocation; flag factual-location conflict before claiming exact reproduction |
| Dramatic portrait used for neutral reference | Preserve identity; request even neutral illumination for the reference purpose | No inherited hard side-light; skin/age/marks retained |
| Mirrored selfie reference | Establish the intended recorded orientation and asymmetric landmark/garment sides | Do not mirror lettering or anatomy to force composition |

## Recipe A: character or costume reference

Compose: **operation and authoritative inputs -> explicit changed/preserved fields -> required view/framing -> pose/expression -> neutral reference treatment -> acceptance-critical details**. Follow [character creation/change](character-performance.md) and [angle coverage](visual-development.md#character-identity-and-sheets) only if needed for this operation.

Example: `Using the accepted frontal identity, prepare the left-profile head reference for the same adult character. Preserve facial proportions, hairline, age presentation and the left-ear accessory. Head level, neutral relaxed expression, the actual left side visible rather than a mirrored right view. Even neutral illumination, plain background, enough face resolution to compare nose/ear/jaw shape. Costume follows the accepted variant where visible.` Bind the actual files using supported fields. This is a prompt example, not proof of correct anatomy.

For a jacket-only change: retain the correct identity source and change the jacket's color/material as specified. Do not add beauty retouching, replace hair, invent jewelry or force a new casting exercise. Inspect the result before promoting the outfit reference.

## Recipe B: scene creation and hero still

Compose: **viewpoint/framing -> subject action/placement if present -> fixed spatial anchors -> material/light behavior -> visible detail and end use**. Use [scene creation](visual-development.md#scene-creation-record-and-sequence) when geography must persist. Establish the intended camera and coarse layout before surface polish.

Example: `Eye-level outward view from the walking operator's recording lens. The accepted cart footprints and storefront order remain fixed; the nearest canopy occupies frame left and the route continues past it. Vendors and pedestrians occupy plausible separate paths. Steam rises from the identified hot cooking surface, catching nearby stall light and thinning upward. Worn metal reflects the stall source; the deeper street remains darker. Verified sign plates retain their lettering and position.` Actual landmark choices come from the accepted scene; do not invent them from this example.

Skin, fabric, grain, haze, depth of field and highlight behavior follow the selected look and capture evidence. Separate moving cooking steam from general air. Exact signs need controlled textures/plates or a tested text-preserving route; adjectives alone are insufficient.

## Recipe C: one continuous video shot

Compose: **duration/cut policy and image source -> relevant reference roles -> start state -> timed observable changes -> camera path/target -> persistent world/identity facts -> exact final composition -> audio**. Put the most consequential requirement early. Keep actual duration/aspect/resolution/audio controls in tool parameters. Check timings and action feasibility before submission.

For a device vlog, use explicit outward -> transition -> selfie speech -> return -> progressed outward states. Assign the lens to the device throughout; describe what rotates and what continues walking based on verified operation. The selfie background is reverse coverage, and the return reveals the forward street from the new position. Do not demand a full view of the recording device from its own lens. Allocate turn/settle/breath time from a timed sample, not an assumed eight-second template.

Use a performance-record slice for this scene, not the complete character bible. A habit of stillness does not override walking. Specify required contact and occupied hands. Conclude with a concrete last composition/state that supports the next shot or the intended ending.

## Recipe D: multiple shots or a revision

Use separate records with start/end match states. Use native multishot only after verifying its timing/reference controls; otherwise supply separate requests. Do not impose arbitrary shot counts, cut rates or a universal maximum duration.

For revisions, compare changed fields and dependents. Edit the authoritative record, then rebuild only affected prompts/settings. Deliver a complete copy/paste prompt when the destination needs it; edit an existing file directly when more efficient. Do not reprint a long unchanged project pack. An explicit user change is not a reason for another broad approval round.

## Submission check

Compare the assembled request to the shot record: actual files/roles/order, camera source, direction, preserved facts, supported controls, timing, sound and current quote. Use [preflight final audit](director-preflight.md#8-final-prompt-audit-and-verification-record) for unresolved coupled constraints; do not reload its entire catalog for a settled small revision. Inspect returned output using the applicable acceptance criteria, not the presence of these phrases.

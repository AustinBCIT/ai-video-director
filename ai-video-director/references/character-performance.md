# Character identity, performance and changes

Load for creating/reusing a recurring visible character, directing a recurring voice/performance, or changing accepted character facts. Skip for environment-only work and ordinary edits to authentic footage. Read only the active section: **create**, **record**, **change**, or **verify**. Asset roles and angle coverage remain in [visual development](visual-development.md#character-identity-and-sheets); do not copy that checklist here.

## Create: build only the missing foundation

1. Inspect existing accepted identity, costume and performance assets. If usable references exist, reuse them; do not restart casting or create an intermediate model by habit.
2. If inventing a character, propose a compact identity specification from the brief: adult/age presentation as specified, distinguishing facial structure, hair, proportions and meaningful asymmetry. Label creative additions proposed. For a real person, unseen angles/details remain unverified; generation is an interpretation.
3. Establish one accepted neutral frontal face reference at sufficient face resolution. Use even neutral illumination and a plain background to reduce unwanted lighting/style inheritance. This does not remove all lighting information. Preserve real identifying marks and intended age; beauty smoothing, matte skin, film grain and a particular expression are optional style decisions.
4. Build the agreed costume directly on the accepted character where supported. Existing garment references already provide evidence; add an intermediate garment plate only for a demonstrated failure or a specific control benefit. Inspect face and body proportions after the outfit change.
5. Complete required multi-angle coverage using the canonical identity and accepted costume, then inspect consistency. Keep a high-resolution face reference and clean angle files; a crowded board cannot substitute for facial detail. Follow the user's coverage requirement even when fewer references are submitted to one model.
6. Add performance information only to the depth the shot needs. A brief vlog needs a few delivery/movement cues; a recurring drama may justify function, relationships and scene-specific emotional state. Do not require biography to prepare one short shot.

## Record: compact, reusable and scene-specific

Store this in the existing project record or a linked character file. Omit unused fields; a simple character usually needs four to six short lines. Each accepted field has provenance/status; retain unknowns without inventing canon. IDs identify records, not automatically attached tool inputs.

```text
CHAR-01 / identity v1: authoritative face + angle asset IDs; fixed anatomy/hair/age presentation/asymmetry; accepted evidence
COST-01 v1: garments/materials/accessory sides; allowed styling changes; authoritative outfit assets
PERF-01 v1: speech [pace, register, pauses, vocabulary]; motion [gait, gesture scale]; rest [hands, weight, gaze]
Voice: authorized source/version, language; pronunciation sample/status when applicable
Scene S01: intention -> observable change; gaze target; hands/prop; start/end emotional state
Used by / open issue: affected assets/shots; unknown or proposed detail; next verification
```

Identity, costume and performance have independent versions. Do not version identity merely because a voice delivery or jacket changes. The performance baseline supplies tendencies, not an instruction to freeze the same pose or emotion in every shot. Scene action overrides habitual stillness deliberately; state the exception when needed. Keep actual voice identity distinct from delivery style.

Translate intent into observable behavior without over-choreographing:

| Intent | Useful brief direction | Avoid |
|---|---|---|
| Curious travel presenter | Looks toward the stall, then into the lens; short breath before a conversational line; free hand gestures once | Simultaneous pointing, waving, eating and turning while both hands are occupied |
| Concealed disappointment | Brief reply delay, eyes lower, mouth corners settle before speaking | Demanding many conflicting emotions in one beat |
| Confident recurring host | Unhurried phrasing, small precise gestures, relaxed pauses; scene-specific gaze target | Applying a fixed neutral expression over a requested laugh |

Example, proposed rather than automatic canon: `PERF-01: conversational mid-register delivery with short walking breaths; small free-hand gestures; relaxed shoulders at rest. S01: attentive to vendors, brief lens contact during selfie speech, gaze returns to the path afterward.` Assign body/head/gaze separately when their directions differ. Dialogue timing and pronunciation still require [audio verification](audio-captions.md#names-and-pronunciation-before-video).

## Change: permanent-change decision tree

First identify what the user changed, whether it applies to this shot, an alternate era/look, or the ongoing character. Infer scope when explicit; ask one focused question only if permanence changes downstream work. “Change her hair” alone may need a temporary-versus-ongoing choice; “red jacket in S02 only” does not.

| Change | Record and asset action | Downstream action |
|---|---|---|
| Pose, gaze, emotion, gesture or line delivery for one shot | Update the shot/performance state; keep identity authority | Review that shot and adjoining match points; no new face lock by default |
| Outfit, removable jewelry, temporary styling/makeup | New costume/look variant linked to the same character; update visible references as needed | Review shots using that variant; preserve other outfits and accepted identity |
| Ongoing hair cut/color, facial marking or another identity-defining visible feature | New identity **state** version linked to the original person, with an explicit changed/preserved list; create/approve updated canonical evidence and affected views | Mark only dependent references/shots stale; do not regenerate automatically |
| Intentional age/proportion/anatomy change | Treat as a significant identity state, or new casting if requested; preserve person-level lineage when it is the same character | Re-establish affected face/body/angle evidence; test relevant motion before continuity-dependent use |
| New voice identity or permanent speech/movement signature | New voice/performance version; retain visual identity unless explicitly changed | Review affected audio, acting and visible lip-sync; no unrelated image rebuild |
| Flashback, disguise, alternate look or branching story | Named branch with era/scene applicability; retain current canon | Select branch per shot; never globally replace the current version |
| Output drift, accidental mirroring or wrong anatomy | Mark output failed against existing authority | Repair toward accepted canon; a generated mistake never becomes a permanent change by default |

For a deliberate re-lock: save the prior state, propose the changed fields, bind the correct original reference, generate only needed replacement evidence within scope/budget, inspect preserved features, then accept the new authority. Until accepted, the candidate is `proposed`; old assets remain valid for old-state shots. If a user explicitly accepts a changed result, record that decision and inspect any still-required unseen views rather than claiming they were accepted too.

Change record: `entity/version -> changed fields -> preserved fields -> authoritative evidence/status -> affected shots -> next check`. Reuse [continuity revision propagation](continuity.md#revision-propagation) for dependency handling. Update quote/charge only for actual new billable work; preserve sufficient existing authorization.

## Verify before reuse

### Removable props and acting revisions

A disguise is a linked look branch, not a different identity. Plan its visible state before, during and after removal: attached fake mustache/cap/glasses, acting hand, detachment and where each prop ends. Use [precision actions](precision-actions.md) for the contact sequence. After removal, bind the accepted uncovered state to later shots; the discarded disguise reference must not restore the prop. Track an intentional costume or identity change separately.

For an acting repair, identify one observable dimension to adjust while preserving what worked: reduce smile amplitude while retaining irony, or add a brief decision pause without slowing the entire scene. Do not swing from a broad smile to blank affect through an indiscriminate opposite instruction. Compare takes in context with dialogue and adjoining reactions. A still establishes expression only at that instant.

### Reuse checks

Compare accepted and proposed references for face proportions, age presentation, hairline, asymmetric marks, body proportions and costume construction at useful resolution. Compare performance against the scene: correct voice, intended gaze, plausible hands/props, gesture and breath timing. For a turn, inspect actual intermediate angles/motion; a sheet does not establish a working 3D identity. On failure load only the relevant [repair card](repair-cards.md), then record what was actually observed.

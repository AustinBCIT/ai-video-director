# Continuity and change control

## Use only the tracking the piece needs

A single abstract shot may need no continuity table. Connected shots need a record of what must persist. Use stable IDs such as CHAR-01, COST-01, PROP-01, ENV-01 and S01, with asset versions stored in the project record.

| Type | Track when relevant |
|---|---|
| Identity | Face, proportions, hairstyle, distinguishing asymmetry, voice |
| Costume/product | Materials, colors, construction, labels, SKU, accessories |
| Geography | Entrances, furniture/landmarks, character position, camera axis |
| Action | Handedness, grip, contact, object position, screen direction, start/end state |
| Time/light | Time of day, weather, light/shadow direction, exposure relationship |
| Performance | Emotional state, gaze, energy, dialogue intention, pace |
| Editorial/audio | Match points, sound bridges, ambience, speaker/voice consistency |
| Technical | Frame rate, aspect, color treatment, alpha interpretation, audio sync |

## Identity lock means an accepted reference

Record which file/version is authoritative. Do not regenerate accepted identities from text alone and expect a match. Use relevant reference crops or controlled assets. Keep characters separated by IDs and attach only those needed for a shot. Review multiple-character interactions for face/wardrobe swaps.

Use neutral scene anchors when the layout must persist. For reusable 3D, preserve scene scale, object names/IDs, materials and camera records. Reuse actual geometry for exact repeats; an AI approximation may need visual checking every time.

For a moving camera, record a small fixed-landmark map: sign text, cart footprint, canopy color, building corner and relevant occlusion order. Inspect these across motion, especially before/after selfie turns and when pedestrians uncover them. Distinguish normal parallax from a stall changing side, an object teleporting, lettering morphing or the background resetting. These are failures when layout accuracy is required, not cosmetic details excused by a realistic face.

A start-frame reference is insufficient proof of continuous geography. Use controlled camera renders/plates, tracked signs or a verified motion-control route where exactness matters; see [production readiness](production-readiness.md). Preserve the actual reverse-facing environment during selfie coverage and the progressed forward viewpoint on return.

## Per-shot transition

Record incoming state, outgoing state and intentional change. Example: S03 ends with a red cup in the right hand at chest height; S04 begins with the cup in that hand, with matching screen direction. A jump to the left hand needs an intervening action or an intentional discontinuity.

Some mismatches are best fixed in the edit, crop or audio bridge; others change identity or product truth and require correction. Choose the least costly fix that preserves the shot's purpose.

## Revision propagation

When a locked choice changes, identify dependent assets and shots. Mark them for review; do not regenerate everything automatically. Costume change affects visible wardrobe shots but may not affect a landscape insert. A new aspect ratio can affect composition, title placement and safe areas without changing narration.

Retain accepted versions and label revisions. Use `proposed`, `accepted`, `needs revision`, `superseded` and `unverified` meaningfully. Do not overwrite source assets to hide a failure.

When camera ownership changes from observer to recorded-device POV, mark the observer storyboard, hero frame and motion prompt superseded for that shot. Reuse valid identity, wardrobe and environment assets, but do not keep the old start image merely because its appearance was approved. When the user reports a concrete defect, update the affected acceptance criterion to failed and propagate it to dependent work.

## Minimal ledger

```text
Entity/version: CHAR-01-v02
Authority: accepted portrait path or media ID
Fixed: face, short dark hair, left-ear stud
Allowed: expression and pose
Variants: COST-01 work jacket; COST-02 raincoat
Used by: S01, S02, S05
Open issue: profile consistency in S05 not yet inspected
```

Before final acceptance, view adjacent shots together with their sound. A shot that passes alone may still break a scene's geography, rhythm or emotional progression.

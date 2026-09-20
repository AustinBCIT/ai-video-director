# Storyboards, animatics and prompt packages

## Which planning artifact?

A shot list states what to produce. A storyboard sketches composition and action. An animatic places rough boards with timing and temporary sound. Use the cheapest artifact that tests the unresolved issue. When duration, dialogue or complicated transitions are risky, an animatic can prevent generating footage that cannot fit the edit.

Do not imply a written storyboard has been rendered. Label sketches, placeholders and timing estimates. Keep shot IDs stable across revisions.

## Shot table

For simple work: `shot ID | duration | framing/action | reference | sound/text | cut`.

For complex work add: `scene/purpose | camera/blocking | lighting | start/end state | continuity | production route | acceptance | status`. Do not add empty columns that provide no value.

State whether timecodes are timeline positions, source in/out points or generation duration. Include edit handles where useful. At 24 fps, a four-second shot occupies 96 frames; a longer generated source may provide trim room. Confirm that generation supports the requested source duration before quoting/submitting.

## Separate four prompt layers

1. Creative brief: audience, message, overall look and restrictions.
2. Asset prompt: establish the character, product, environment or style frame.
3. Shot prompt: one shot's subject, action, framing, camera behavior, timing, light and end state.
4. Finishing instructions: exact titles, captions, sound, color and edit work performed afterward.

Do not send a production encyclopedia as one video prompt. Repeat only essential identity/style constraints needed by that model. Reference files require actual tool attachment/binding; a filename or asset ID in prose is not an attached image.

## Tool-ready shot record

```text
Shot: S02 / purpose: show the decision to help
Deliverable: 4 seconds in the edit; source duration/handles: verify for model
References: CHAR-01 identity; COST-01 costume; ENV-01 layout
Roles: CHAR-01 controls identity; ENV-01 controls room geometry
Start: character screen right, looking toward door at frame left
Action: pause, look down, then lower one hand toward the dropped notebook
Camera: static medium shot at eye level; preserve screen direction
Image source/operator: external observer / specified operator
Viewpoint states: lens position and target at start, transition and end; which people/props can be visible
Light/look: soft window light from frame left; neutral restrained palette
End: hand near notebook, gesture readable for a cut to insert
Audio: silent source; room tone/Foley added in edit
Preserve: costume, notebook color, hand and prop count, background layout
Reject: identity drift, duplicate prop, impossible contact, unplanned camera move
Readiness/evidence: applicable checks in production-readiness.md; pronunciation sample and full playback/listening reviewer when needed
Tool settings: chosen supported model/mode, aspect, resolution, duration, audio
```

Adapt to actual tool syntax. Negative prompts, seeds, start/end frames, reference roles and weights are not universal. Use only supported controls, with prompt text separate from structured parameters. A fixed seed is not a cross-model identity lock.

## Temporal choreography

For complex movement, describe start -> action -> end, timing ranges and physical contact. Distinguish subject motion, camera motion and edit transitions. Split actions when a shot contains too many simultaneous constraints. Start/end reference images help only when supported and visually compatible; widely different geometry can produce morphing.

For image-to-video, prioritize what changes and what stays fixed; avoid unnecessarily redescribing a clear accepted frame into a different scene. For multi-shot modes, verify that shot timing and references can be controlled; otherwise produce separate clips. Model-native editing/extension also needs a defined unchanged region/time and an actual input video.

For footage from the presenter's own camera, explicitly assign the viewer to that optical viewpoint. Plan outward view -> motivated lens turn -> brief selfie speech -> return to outward view as separate orientation states with continuous position, geography and sound. Do not use an external shot of the presenter holding the device as the start frame for its recorded footage. Verify the line plus turns fits the runtime before submitting; do not hide a timing conflict in a long prompt.

## Generation review

Review the entire clip in motion and sample difficult contact, faces, hands, logos, edges, start/end transitions and background consistency. Check motion against the intended action, not only image quality. Listen when audio is generated. If only stills can be inspected, explicitly limit the review claim.

On failure, identify one cause: wrong input role, overloaded motion, geometry drift, unstable text, unsupported control or source mismatch. Choose an edit/reuse/regeneration that addresses it. Record the new attempt and reason. Do not blindly retry or run expensive alternatives just because another model exists.

## Source note

[Google's video prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide), checked 2026-09-19, is a provider-specific reference for describing video shots. Its feature syntax must not be assumed to apply to Higgsfield or other models. The workflow above is this package's production guidance, not a quoted universal prompt formula.

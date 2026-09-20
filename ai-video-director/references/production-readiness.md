# Production readiness and failure prevention

Use this for photorealistic live-action work, footage recorded by an in-scene device, recurring characters, exact products/locations, spoken names, or diagnosing a failed test. Apply only relevant checks. A simple abstract animation does not need a character turnaround or pronunciation record.

The purpose is to catch a wrong brief, missing references and an unsuitable production method before generation, then reject visible failures afterward. Written instructions reduce avoidable errors; they cannot guarantee a generative model's fidelity.

## Establish the actual viewing experience

Before generating the main frame, state: **The audience sees the image recorded by [camera], held/operated by [person], pointing toward [subject], from [position].** Record whether that statement came from the user, an accepted proposal or an unconfirmed assumption.

For a vlog, distinguish recorded-device POV, the device's selfie view, an observer filming the vlogger, and intentional mixed coverage. If the user has specified one, follow it. If the ambiguity changes the film, resolve it before producing continuity-dependent assets; do not quietly choose an external tracking camera because it makes the product visible.

The recording camera normally cannot appear in its own footage. Hands or arms may enter its field of view; a full device requires a physically explained reflection or a separately specified observer shot. A device brand is not a command to show the device, nor proof of its optics or controls.

A switch between forward street view and selfie view must preserve camera ownership, continuous position and travel. The lens turns toward the presenter and back while the same walk continues. Determine the actual device's mechanism from reliable reference before depicting button presses or gimbal behavior. Do not invent a second lens, a floating observer, a reverse walk or a mirrored street to make the transition work.

## Required evidence before a production attempt

Use `passed`, `failed`, `not verified` or `not applicable` per criterion. Record the actual artifact/evidence and next corrective action; a checked box or a strong prompt is not evidence.

| Criterion | Evidence before dependent video work |
|---|---|
| Camera viewpoint | Camera owner, lens direction, subject visibility and transition states recorded; storyboard/rough camera preview matches them |
| Character coverage | Canonical identity plus this user's required front, both profiles and back; needed three-quarter angles checked for the same person, hair, outfit and handedness |
| Product behavior | Authoritative geometry/operation reference for visible product actions; product not forced into footage recorded by itself |
| Environment fidelity | Fixed landmark/sign inventory, forward and reverse coverage where needed, and a route that can hold required geometry/text through the move |
| Physical realism | Observable targets for skin/fabric, scale, grip/contact, gaze, gait, parallax, exposure, motion blur and light response; representative draft checked |
| Pronunciation and timing | Exact line, critical names in native spelling, reliable pronunciation reference and a listened-to audio sample timed with turns and pauses |
| Music and dialogue plan | Explicit music/no-music decision, speech delivery and timing, ambience/cue plan, usable source assets and final listening route |
| Review capability | A usable path for normal-speed continuous playback with sound and detailed frame inspection; named human review where agent perception is unavailable |
| Cost and submission | Exact supported media roles/settings, a fresh quote, existing sufficient authorization and known job/retry state |

This is a readiness check, not a new user-approval ceremony. Complete reversible preparation autonomously within the authorized scope. Ask only for a material unresolved creative decision, unavailable input or genuinely missing spending permission. Approval of a still's appearance does not waive a missing profile, change the camera viewpoint, verify pronunciation, or make an unsupported route reliable.

When a required criterion is missing, mark the production route `needs preparation` and complete the missing work. A bounded diagnostic pilot may test a specific uncertainty if that test and its limits are within the user's authorization; label it `diagnostic only`, state the uncertainty before submission, and never present it as passing the production requirement. Do not turn a general approval into permission to knowingly skip the user's accuracy requirements.

Even a diagnostic needs a defined question, the correct camera ownership, sufficient inputs to test that question, supported settings, remaining authorized spend and an actual way to assess its result. Missing character views may be the subject of an angle test, but cannot be silently waived for an unrelated final-looking shot. If audio cannot be heard, do not describe the diagnostic as testing pronunciation until a capable reviewer is available.

## Choose a route that can preserve the required facts

Classify fidelity: inspired appearance, recognizable layout, or exact repeatable geography/product/text. A Blender still constrains one composition; uploading it does not constrain all later viewpoints or preserve the original 3D scene. Prompting “keep the background unchanged” is not an implementation for exact continuity.

For exact motion through a street or a forward/selfie/back turn, favor real footage, actual 3D camera renders, locked plates, tracked signs, or compositing the uncertain element into controlled footage. Use generation for components it can support. Verify any model's video/depth/control capabilities through its current schema and a representative test, rather than assuming a feature exists.

Verify the whole route, including a moving/speaking presenter: available character rig or performance source, camera match, perspective, lighting, occlusion, integration and lip-sync. Recommending compositing does not establish that the selected image-reference tool or available editor can execute it. Keep unresolved integration dependencies in the feasibility record.

For photorealistic output, identify the realism gap in the source. A stylized scene needs realistic asset/material/light development or a separately validated enhancement route. Skin detail, 1080p resolution and camera-brand words do not establish physical realism or spatial fidelity. If the available method cannot meet a required constraint, explain the specific tradeoff before spending on it and prepare an achievable alternative within scope.

Break overloaded movement into planned states, not arbitrary unrelated generations. A full continuous turn needs geometry around the camera, not two incompatible endpoint images. If cuts are acceptable, plan an intentional motivated cut with matching position, direction and sound; do not silently substitute cuts for a requested continuous shot.

## Acceptance after generation

1. Play the whole clip at normal speed with sound. Then inspect transitions, contacts, faces, background occlusions and uncertain regions frame by frame; sample landmarks at start, before/after turns, midpoint and end.
2. Track whether each fixed sign, stall and building follows plausible camera parallax and occlusion. Reject teleporting carts, resetting crowd positions, skipped backgrounds, texture crawling, changed letters and geometry swaps when these violate the brief.
3. Listen to names and natural delivery; compare to the verified pronunciation asset. Watch lips with the final audio and review continuity of ambience across turns/cuts. ASR supports a transcript, not a pronunciation or lip-sync pass.
   Check music against the selected music/no-music plan, including cue timing and whether it masks speech. Log dialogue and music/mix results separately.
4. Record each criterion's status and evidence. A decoded file or a poster frame only passes its own technical/visual check. If playback/listening is unavailable, leave those criteria `not verified`; arrange the needed review rather than claiming acceptance.
5. Preserve rejected versions, log the failure and choose a targeted fix. Do not retry the same overloaded prompt automatically. Respect existing retry/spend limits; a changed production method is not automatically authorized paid work.

Deliver a test with its failed/unverified items when appropriate, but do not label it final, accurate or fully verified. User feedback about a concrete visible/audible defect is evidence: record it as failed and invalidate dependent acceptance, instead of retaining an earlier “not verified” label.

## Compact record

Keep this in the existing project state or shot record; no separate document is needed for simple work:

`criterion | required outcome | artifact/evidence | passed/failed/not verified/not applicable | fix/next action`

Record current readiness, fidelity level, camera source, references, pronunciation evidence, review capability and scope of any diagnostic attempt. Use [cinematography](cinematography.md), [visual development](visual-development.md), [continuity](continuity.md), [audio](audio-captions.md) and [delivery](delivery.md) for the relevant detailed work.

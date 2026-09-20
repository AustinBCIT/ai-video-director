# Cinematography and capture

## Start with purpose

Describe what the audience should notice or feel, then select shot size, angle, distance, perspective, movement and lighting. Include settings only when they change execution. A shot can be cinematic with a static camera and simple light.

| Choice | Visible effect / useful case | Tradeoff |
|---|---|---|
| Wide establishing shot | Shows geography, scale or isolation | Faces and fine product detail become less readable |
| Medium / two-shot | Shows interaction and body language | Needs clear blocking and separation |
| Close-up / insert | Directs attention to a reaction, action or detail | Requires stronger identity/geometry continuity |
| Low / high angle | Changes perceived power or reveals layout | Can distort a product or overstate emotion |
| Camera closer with a wider lens | Stronger near/far size differences and immersion | Facial/product distortion can increase |
| Camera farther with a longer lens, reframed | More compressed apparent depth | Needs space; background and focus behavior change |
| Locked camera | Emphasizes performance, clarity or geometry | Motion must come from subject/scene/edit when wanted |
| Dolly / track | Physically changes viewpoint and parallax | Requires spatially consistent surroundings |
| Pan / tilt | Rotates viewpoint to follow or reveal | Does not physically travel like a dolly |
| Zoom | Changes framing through focal length | Different perspective effect from moving the camera |
| Rack focus | Transfers attention between distances | Requires readable targets and controlled timing |
| Handheld / stabilized follow | Adds subjective energy or smooth travel | Excess movement can impair comprehension |

Focal length alone does not determine perspective: camera position and framing matter. In Blender/real capture, specify sensor/gate and focal length where reproduction matters. In generation, describe the intended visible result alongside any camera cue; do not promise measured optics from prompt wording.

## Blocking and continuity

### Camera source and recorded-device POV

Before blocking, record `image source / operator / camera position / optical-axis target / what may enter frame`. “She films a vlog” must not automatically become an observer shot of her carrying a camera. If the audience is watching her recording, place the virtual camera at the device's optical viewpoint and move it with her. Her gaze follows the lens during selfie speech, then returns to the street when she turns it outward.

For forward -> selfie -> forward, plan the position and orientation before, during and after each rotation. During the selfie interval, the background is the space behind the walking presenter, not the same forward scene pasted or mirrored behind her. On return, the street must be seen from her progressed location. Use a floor plan and camera preview where this distinction matters.

Match the intended device's field of view, focus, stabilization and low-light behavior using verified references or actual render settings. A stable gimbal can still translate and show natural walking parallax. Do not substitute a distant tracking shot, a lens orbit around the actor or an impossible perfectly stationary background. Avoid naming physical controls without checking the device's operation.

Allocate time for turns, settling, speech and continued walking. Time spoken audio rather than guessing that a line and two turns fit. Shorten a draft line within delegated creative scope, or surface the runtime/dialogue conflict when exact wording is locked.

Record actor/object positions, movement path, gaze target, camera side of the action axis and screen direction. Maintain the 180-degree relationship where continuity depends on it, or motivate a crossing with an understandable camera move/re-establishing view. Match gaze and motion across cuts. A deliberate discontinuity is valid when the effect is intended.

For vehicle seating, curb-side exits, stopping clearance or trajectory diagrams, load [spatial blocking](spatial-blocking.md). If dense action overloads a wide shot, tighter coverage may preserve the key event with fewer competing constraints. Retain required geography and spectacle; a must-have wide may need controlled staging rather than a crop.

## Lighting

Specify motivated source, direction, size/softness, contrast, practicals, ambient fill, color relationship and time/weather. Preserve catchlight and shadow direction across connected shots. Describe "large soft window source from frame left, darker camera-right side" before brand names for lights. Product work may require reflection cards, controlled specular highlights and separation from the background.

## Camera tricks

Use only when they serve the shot: dolly zoom for perceptual unease, whip-pan for a motivated reveal/cut, match cut for visual connection, forced perspective for scale illusion, macro for detail, slow motion for temporal emphasis, speed ramp for a transition in energy. Check tool controllability and test difficult moves with rough assets first. Avoid stacking a dolly zoom, orbit, rack focus and complex action into one short generation.

## Frame rate and motion

Choose the timeline timebase before detailed animation/editing. 24, 25, 30 or higher rates are decisions based on delivery, source footage and intent, not quality rankings. Preserve exact fractional rates when applicable. Slow motion requires a deliberate capture/generation and conform strategy; frame interpolation may introduce artifacts. Shutter angle/exposure time affects motion blur in real or virtual capture; set actual controls when available. AI language is a desired look, not an exposure guarantee.

## Real camera and large-format branch

For filmed/hybrid projects, choose a camera system from needed codec/bit depth, dynamic range, low-light behavior, rolling shutter, lenses, stabilization, sound sync, media, power and budget. Record real capture settings, white balance, exposure monitoring, frame rate and lens metadata when handoff requires them. Plan room tone, plates, clean backgrounds or tracking references where postproduction needs them.

A Netflix-approved camera does not alone establish compliant production. Check current camera-specific recording requirements and the actual commissioning/delivery agreement. The user's [Netflix capture page](https://studiopartner.netflix.net/studio/branded-cameras-and-image-capture) was reachable only as a JavaScript shell during package development on 2026-09-19; its contents were not verified. Use an accessible official source or supplied specification when this branch is needed.

"IMAX" can mean capture technology, an exhibition format, certification or an aesthetic request. Clarify which only when it changes the task. For an aesthetic request, translate it into concrete scale, composition and presentation choices. Do not call generated footage IMAX-certified or assume black bars/8K export creates large-format capture quality.

# Blender: controlled scenes and reusable assets

## When it earns its setup time

Use Blender for repeatable camera moves, stable geography, exact/reusable product geometry, lighting, procedural animation, simulations or passes for compositing. A one-off loose background may be quicker to generate; a product orbit or repeated room may benefit from a persistent scene. Check the user's available hardware and actual Blender version rather than inheriting old machine notes.

Do not build a scene merely because Blender is available. Skip it for editing usable footage, a loose mood test, or a one-off shot whose geography may change. If the user explicitly requested a Blender scene, deliver that scene, but assess its role in later video production separately. A completed scene is reusable work, not evidence that a still-based video generation used its animation.

For an existing stylized environment, preserve the layout and inventory what needs replacement: geometry detail, texture scale, materials, signs, people/rigs, skin, clothing, light transport and motion. Photorealistic rendering is a production task; changing renderer settings or adding a realism prompt is insufficient.

## Minimum scene contract

Record unit scale, object dimensions where relevant, coordinate/up-axis assumptions, camera framing, timeline frame rate/range, light intent, materials, render engine and output specification. For a product mechanism, get real movement/geometry evidence or clearly label it a concept. Do not build a physically inaccurate approximation as an exact demonstration.

Start with a blockout when framing, timing or geometry is unresolved. Use low-cost previews to test the camera path and action before detailed materials/rendering. Inspect silhouettes, contact, intersections, constraints, scale and readable motion. Use stable object/material names and collections for revisions.

## Local or connected execution

Distinguish local Blender from a connected remote Blender/3D project. Inspect the current file/scene or connected project revision before editing. Save a new working version when appropriate; do not reset or delete the user's scene as a default initialization step. For connector-based work, read current tool schemas and revision requirements. Do not invent `bpy` properties from another version.

For Python automation, use the installed Blender's supported API and run a small representative operation/render first. Avoid unbounded simulations/renders. Make scripts preserve unrelated content and return saved-file locations, render settings and meaningful errors. If only a script can be delivered, say it was prepared but not executed.

## Animation/camera handoff

Specify start/end states, paths, target/gaze, interpolation and timing. Give camera position/orientation, sensor/lens and focus information when reproducibility matters. Use rigs/constraints for maintainable motion where warranted. A model prompt saying "50 mm" is not a measured scene camera; use actual Blender settings for a controlled shot.

For recorded-device footage, place the scene camera at that device's lens position and animate its travel and orientation. A street/selfie/street sequence stays on one plausible walking path while the lens turns; the reverse scene must be modeled/covered too. Verify the real device's field of view and operation before claiming a match. A separate camera following the presenter depicts a different viewing experience.

First render a cheap full-duration camera preview and time the dialogue/turns against it. Then prepare the necessary realistic assets and representative renders. A speaking selfie presenter needs a verified rig/performance or a tested compositing route with matched perspective, lighting, occlusion and lip synchronization. A 3D environment alone does not solve a realistic human performance.

For AI enhancement, document the exact inputs the selected tool accepts. One frame cannot carry the full camera path. Keep controlled rendered plates where exact signs and geometry matter, or test a supported motion-conditioned route and compare the entire output to the base. Treat any enhancement-induced drift as a failed criterion.

## Color and output

Determine the installed version's working/view/output color configuration before render. AgX is a view transform; do not indiscriminately assign a view transform as the source color space of every texture or composite. For a simple route, export a display-ready image sequence with a documented look; for advanced compositing, agree a scene-linear workflow and transforms end to end. Avoid applying the same display transform twice.

For lengthy renders, an image sequence can preserve completed frames after interruption. Choose PNG/EXR and passes according to alpha, dynamic range, storage and finishing needs. Agree frame numbering/range and alpha interpretation. Render a short sample into Resolve/AE to confirm colors, transparency, frame rate and edges before committing the sequence.

Reference the [Blender manual](https://docs.blender.org/manual/en/latest/) for the installed release. The [color-space documentation](https://docs.blender.org/manual/en/dev/render/color_management/color_spaces.html) was discoverable in research on 2026-09-19, but the stable color-management page failed to fetch; do not use development-version defaults as verified installed behavior.

## Acceptance

Review a rendered sequence, not only the viewport. Check camera clipping, texture/resource resolution, shadows, geometry contact, temporal noise/flicker, alpha edges, missing frames and expected motion blur. Deliver the `.blend` and needed dependencies when editable source is requested, with a preview and actual render settings. Record anything not executed or inspected.

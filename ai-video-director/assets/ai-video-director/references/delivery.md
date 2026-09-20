# Technical delivery and acceptance

## Define delivery before final production

Specify target platform/use, runtime/count, aspect and exact pixel dimensions, frame rate, orientation, container/codec, audio, captions, color intent, file size constraints if any and required source files. A preview specification can be provisional; the final export cannot remain "high quality" without measurable settings.

Separate generation resolution, working-timeline resolution and delivery resolution. Upscaling can satisfy dimensions but does not establish native detail. Separate SDR/HDR, actual capture, stylistic look and certification. Do not infer HDR from bright highlights or a 10-bit container alone.

## Tool compatibility

Check installed version, OS, codec availability and Free/Studio tier for the chosen route. Validate a short import/export sample early when exchanging Blender, Resolve and After Effects material. Avoid an entire production in an unsupported intermediary codec. Proxies may help performance; retain/relink original media for final output as appropriate.

For a transparent graphic, agree straight/premultiplied alpha, frame range, color space and a supported alpha format. H.264 is not an alpha handoff. For EXR/image sequences, specify frame numbering, missing-frame detection and color interpretation. Deliver a companion preview when an intermediate cannot be viewed easily.

## Output package by scope

Quick: final or planned main export, essential prompt/asset references and open limitations.

Standard: main export, requested alternate crop/clean/caption variants, editable project if requested, used assets and captions/transcript where applicable.

Detailed: add source projects, dependency/version list, media manifest, audio stems, graphics sources, handoff settings and archive notes needed for another editor. Do not create unused boilerplate or promise proprietary editability from a flattened video.

## Acceptance matrix

| Area | Evidence needed |
|---|---|
| Purpose/story | Message and payoff understandable; required claims/copy accurate |
| Viewpoint | Delivered image comes from the specified camera; visibility, gaze and POV/selfie transitions are physically consistent |
| Visuals | Identity/product geometry stable; composition and text readable; no unwanted changes |
| Motion | Full clip plays correctly; action/contact/camera behavior meets intent |
| Continuity | Adjacent shots preserve the recorded states or intentional transitions |
| Environment accuracy | Fixed landmarks, stalls and sign text follow plausible parallax/occlusion through full motion; no resets, skips or unmotivated swaps |
| Graphics/captions | Exact spelling, timings, no clipping/occlusion, readable at delivery size |
| Sound | Speech intelligible, sync correct, no unintended clipping/dropouts; required measurements pass |
| Technical | File decodes, runtime/frame rate/dimensions correct, no missing frames/media, expected channels/color |
| Delivery | Correct versions, filenames and requested editable assets; real constraints disclosed |

Use `passed`, `failed`, `not applicable` or `not verified`, with concrete evidence. Do not call a plan fully tested or a render inspected when only its prompt was reviewed. If tool access prevents playback/listening/measurement, disclose precisely what is unverified and provide the available artifact.

Apply [production readiness](production-readiness.md) before submission as well as this acceptance review afterward. Export success, 1080p dimensions, a convincing face and a correct transcript do not compensate for the wrong POV, missing angle references, background drift or pronunciation errors. A required failed or unverified criterion prevents production acceptance; deliver as a diagnostic/review artifact with a specific repair plan instead. A still approval covers its stated scope and does not implicitly waive other requirements.

## Release and learning

Publishing is a separate action from exporting; use authorization already given for the specified destination. Check actual selected asset rights and any applicable current platform disclosure rules at release. Keep this proportional to the real project.

Record accepted masters and source references with stable IDs. For performance learning, compare actual metrics against the original goal and note confounders. Keep useful lessons such as "hook B was easier to understand in this audience test" separate from universal claims such as "this hook always wins."

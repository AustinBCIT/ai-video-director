# Tool selection and specialist handoffs

## Choose the smallest capable tool set

Record tools as `allowed`, `available/verified`, `preferred`, `excluded` or `suggested`. A tool name in a brief does not establish installation, a callable connector, a subscription or a feature tier. Respect hard exclusions. Explain a suggested addition by the problem it solves, setup/learning cost and an alternative within the existing tool set.

GPT reasoning/Astra can develop briefs, scripts, scene specifications, code and review questions. Verify its actual tools before promising rendering, file access, vision or execution. Planning instructions should remain usable with another reasoning model.

| Need | Candidate | Load only if selected |
|---|---|---|
| Generated images/video; model reference workflows | Higgsfield | [Higgsfield](tools-higgsfield.md) |
| Reusable geometry, cameras, lighting, simulation/animation | Blender | [Blender](tools-blender.md) |
| Assembly, grading, sound, captions, finishing | Resolve Free | [Resolve](tools-resolve.md) |
| Complex typography, graphics, AE templates/compositing | After Effects | [After Effects](tools-aftereffects.md) |
| Visual exploration and presentation layouts | Claude Design or available design tool | [Design tools](tools-design.md) |

A shot-level hybrid may be best: real product/Blender for exact mechanism, generated background for atmosphere, editable text in the editor. Do not substitute a cheaper route if it fails the intended action or accuracy.

## Decide whether Blender and Resolve earn their place

| Situation | Recommended route | Reason and limit |
|---|---|---|
| Quick visual concept, flexible geography, one independent shot | Existing references and a capable image/video tool | A 3D build may add little; explicitly leave unproven motion/fidelity as unverified |
| Good existing camera footage; goal is a finished edit | Resolve or the available editor | Assemble, time, mix and grade existing coverage; do not rebuild a usable street in 3D |
| Exact layout, repeated locations, forward/selfie/reverse coverage, repeatable camera move | Blender or actual location footage | Persistent geometry/recorded geography supports continuity; a stylized scene still needs substantial realism work |
| Exact product shape or moving mechanism | Verified real product footage or accurate Blender asset | Product accuracy must come from evidence and execution, not branding in a prompt |
| Final assembly, speech replacement, ambience, matching exposure/color, titles and export | Resolve | Use throughout rough-cut and final review; verify the installed edition's tools |
| Sign drift, disappearing stalls or major geometry jumps | Repair/rebuild source shot, then finish in Resolve | Small stable regions may support tracked replacement; a grade or stabilization cannot reconstruct a changing world |

For every 3D-to-AI handoff, record what actually crosses the boundary: one still, multiple views, rendered motion, depth or another supported control. A still transfers composition, not the Blender scene, camera animation or a guarantee of geometry. If controlled motion is essential, retain rendered/filmed footage as the base or verify that a supported transformation holds its motion and landmarks. Do not promise control-video features that the selected generator lacks.

Choose the cheapest *capable* route for the required result, considering setup and revision time as well as render/generation cost. For an eight-second experiment, Blender is optional if only appearance is being tested; it becomes useful when camera ownership, turns or stable geography are the question. Resolve can host an early timing animatic and pronunciation sample before any expensive generation.

## Discover existing skills at handoff

These names were available when this package was built; discover the current catalog and read the selected skill before use. Skills can be absent or renamed. If unavailable, use this package's planning guidance and provide a manual/tool-ready handoff; never claim execution happened. Do not load every specialist in anticipation.

| Trigger | Relevant skill, if available | Boundary |
|---|---|---|
| Costed media generation | `cost-aware-media` | Quotes, entitlement, authorized budgets, retries, asset provenance |
| Product stills/catalog images | Higgsfield `product-photoshoot` | Product photography, not a finished video by itself |
| Finished thumbnails/covers | Higgsfield `thumbnail-generation` | Packaging visual; keep content promise accurate |
| Product-only UGC video | Higgsfield `ugc-product-video` | Off-screen voice; not a presenter tutorial |
| Visible creator demonstrating use | Higgsfield `ugc-tutorial-video` | Actual step sequence and human/product interaction |
| Visible creator wearing an item | Higgsfield `ugc-try-on-video` | Wear/pose continuity |
| Package-opening reveal | Higgsfield `ugc-unboxing-video` | Unboxing-specific action |
| Creator-led website/service video | Higgsfield `ugc-website-video` | Real site references/captures |
| Consistent presenter-led episode | Higgsfield `ai-host-video` | Accepted presenter identity |
| Explicit faceless finished channel video | Higgsfield `faceless-video` | Do not infer this from the absence of a character |
| Full YouTube script | Higgsfield `youtube-script` | Use when its script genre/output fits |
| Supplied footage edit or file-backed graphics | Higgsfield `video-editing` | Not a catchall for every video project |
| Native Higgsedit motion tracks | Higgsfield `motion-craft` | Only if executing that composition workflow |
| Permanently burned captions | Higgsfield `subtitles` | Sidecar-only caption requests do not trigger it |
| Independent edits of supplied short footage | Higgsfield `ad-multiplier` | Check its actual accepted input length and operation |
| Named Higgsfield preset | Higgsfield `higgsfield` | Preserve the user's named preset and inspect its instructions |
| General bitmap generation/editing | Available `imagegen` skill/tool | Use its actual attachment/reference rules |

Other skills such as narrator have their own narrow activation rules; do not trigger them merely because this plan contains narration. No specialist handoff authorizes unsolicited messaging, public posting or extra spending.

## Handoff contract

Pass `task/stage | output specs | selected shot IDs | authoritative asset files/media IDs and roles | locked creative choices | allowed changes | exact text/audio | acceptance criteria | budget/attempt authorization if relevant | open blockers`.

Do not pass irrelevant boards, the full interview or every tool adapter. Give filenames that exist, accessible media IDs or an explicit acquisition task. Summarize source-dependent technical decisions with their evidence. Preserve the selected workflow and explain any adaptation needed for a specialist's actual capabilities.

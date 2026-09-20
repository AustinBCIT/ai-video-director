# Save tokens, generation credits and production time

## Optimize the usable result

Consider total expected effort and cost: reference preparation + tests + rejected attempts + selected shots + cleanup + upscale/render + editing + review. Track currency, provider credits, reasoning tokens and personal time separately. Do not invent a conversion between them or claim savings without a real comparison.

Recommend savings relevant to the selected shot. A cheaper method that cannot preserve identity, product accuracy or requested action is not a qualified option. Provide `saving | method | tradeoff | when to avoid` briefly; let the user choose quality/speed/cost priorities.

## Low-resolution drafts and upscaling

Check the exact model's supported sizes; do not invent a "420p" option. The Higgsfield Seedance 2.5 catalog inspected on 2026-09-19 listed 480p, 720p and 1080p. Current options must be verified for the chosen model/mode.

Use the lowest adequate draft to test the unresolved issue: composition, broad action, timing or camera path. It may be insufficient for tiny labels, faces, lip-sync or fine contact. Review those at an appropriate resolution before accepting a production route.

Two possible promotion paths:

- **Keep and upscale the accepted clip:** preserves that take's timing/composition more directly, but upscaling can invent detail, change faces/text or amplify artifacts. Recheck the result in motion. Do not assume a free/non-generative resize improves detail.
- **Generate at delivery quality from accepted references:** can provide more suitable detail but is a new generation, so the take may change. A reused prompt or seed does not guarantee the exact same action. Native higher resolution is also not proof of better results; test the relevant requirement.

Compare actual quotes for both paths, including minimum durations, audio, input-video billing and the upscale pass. Upscaling 480p to 1080p does not make it native 1080p detail. Do not upscale footage with wrong identity, geometry or action as a way to avoid fixing it.

Hypothetical example, not a provider price: a 20-credit draft plus a 15-credit upscale costs 35 credits if accepted. If an unusable draft then requires a 45-credit replacement, that path costs at least 65 credits. Direct generation at 45 credits could have been cheaper. Use observed acceptance rates only when you actually have them; otherwise show scenarios rather than fabricated expected savings.

## Generation-credit tactics

| Tactic | Why it may save | Check / tradeoff |
|---|---|---|
| Rough animatic before production | Finds timing/coverage problems before billable clips | Keep it rough; do not spend more illustrating it than the decision warrants |
| Pilot the hardest representative shot | Tests identity/contact/motion before commissioning a set | A simple landscape test says little about a two-person dialogue scene |
| Generate only the needed source length plus handles | Avoids paying for unused time | Respect model minimums and leave enough trim room |
| Reuse accepted identity/environment/product assets | Reduces repeated design attempts | Reference upload limits and roles still apply |
| Edit one flaw instead of regenerating the whole shot | Preserves usable material | Verify edit-mode input billing; a local crop/mask may be cheaper |
| Disable unused native audio when supported and cheaper | Avoids paying for sound that will be replaced | Some models charge the same; check the quote and desired performance |
| Add exact titles/logos in the editor | Avoids repeated text/brand failures | Requires a simple finishing step and accurate editable assets |
| Use controlled 3D/real assets for exact repeats | Stable geometry/camera across many shots | Setup cost may exceed savings on a single loose shot |
| Reuse a clean master for platform versions | Avoids regenerating the whole film | Recompose/crop thoughtfully; lost action may require an alternate shot |
| Batch only independent, understood variations | Can reduce setup/latency | A batch is still multiple billable attempts; inspect a pilot before large batches |
| Recover an existing job/download | Avoids duplicate submissions | Resolve ambiguous status before retrying; keep unknown charges tracked |
| Stop when the agreed criteria pass | Prevents endless marginal variations | User can authorize a separate exploration pass if wanted |

Longer generation, extension, edit modes, presets and "fast" tiers are not inherently cheaper. Compare the exact operation. Website unlimited plans, API/MCP usage and trial allowances may differ. Never exploit failures, abuse free trials or bypass provider restrictions to save credits.

## Render and edit time

- In Blender, use blockouts, viewport/low-sample previews and representative frame ranges before final materials/render settings. Raise quality for the defect observed, not by habit. Check denoising for lost detail and temporal flicker.
- Reuse scene geometry, materials, lighting setups and animation rigs. Save clean source versions so one change does not force rebuilding the scene.
- Use proxies for smooth editing where needed, then verify final source relinking. Proxy resolution is an editing-performance choice, not proof of final quality.
- Render long work to resumable image sequences when appropriate; recover finished frames instead of rerendering the whole shot. Account for disk usage and sequence handoff.
- Test a few difficult frames plus a short motion segment for transparency, color, shadows and codec compatibility before exporting all material.
- Use simple cuts, held frames or 2.5D motion only when they serve the requested content. Do not replace requested physical action with a slideshow or slow down footage beyond usable motion merely to fill time.

## Reasoning-token tactics

At the opening director overview and relevant stage changes, use [model and context economics](model-and-context.md) to recommend a qualified model, supported effort and whether to continue, compact or propose a fresh task. Distinguish recommendations from applied settings and measured costs from estimates. Compare the full stage, including handoff and rework; caching does not make history free or reduce its context size.

- Intake from existing facts; ask only the next consequential missing choice. Offer defaults for reversible decisions instead of long questionnaires.
- Keep `SKILL.md` as the router. Load the chosen format/stage and tool adapter, not every reference. Read only the relevant section of a large file when tooling allows it.
- Use one compact project record with accepted choices, asset IDs, open issues and next action. Reference the record on resume; do not paste full historical chats.
- Keep stable creative facts separate from per-shot changes. Supply only the relevant facts/images to each generation request. An ID does not replace the actual required media attachment.
- Omit unused optional sections from the flat brief before submitting. Keep meaningful constraints; a short ambiguous prompt can cause more retries than a slightly longer clear one.
- Request concise deliverables and brief choice/reason/tradeoff explanations. Detailed review reasoning is optional; never expose hidden internal reasoning as a production artifact.
- Use available file editing and targeted reads to revise one section rather than repeatedly printing the whole production pack. Retain enough context to avoid contradictory edits.
- Prefer a small candidate set and targeted current checks over repeated broad research. Record verified capability/date and refresh when the decision or account conditions change.
- Provider prompt caching or batch discounts may help through supported APIs; verify actual availability, stable-prefix requirements, privacy/storage terms, cost and latency. Do not assume a shorter visible answer lowers a subscription charge or all image inputs are free tokens.

## Practical recommendation card

For a 15-second reference-driven clip: "Test the difficult five-second movement at a supported lower resolution first. If its action and identity pass, compare a higher-resolution regeneration with upscaling this accepted take. Add captions and the logo in Resolve. This reduces costly design retries; it may not reduce the final clip's bill if the draft needs replacement."

Use real quotes and existing authorization when executing. A recommendation to save credits is not permission to spend them.

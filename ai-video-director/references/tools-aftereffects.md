# After Effects: optional graphics and compositing

## Recommend for a concrete task

Consider AE for detailed text animation, layered graphic systems, reusable Adobe templates, tracking or complex compositing when the user has access or explicitly chooses it. Explain the specific advantage and learning/round-trip cost. Do not add it just because the video has titles; Resolve/Fusion or Blender may already meet the brief.

[Adobe's workflow guide](https://helpx.adobe.com/after-effects/desktop/get-started/understand-after-effects-workflow/workflows.html) and [text-animation guide](https://helpx.adobe.com/after-effects/desktop/animating-text/text-animation/animating-text.html), checked 2026-09-19, support its role in layered compositions, effects and animated type. Verify version-specific features, plugins and scripting APIs when execution needs them.

## Handoff specification

Supply composition dimensions/frame rate/duration; layer/source names; exact editable text; font availability; approved colors; positions/anchors; entrance/hold/exit timing; easing; masks/tracks; color/alpha and output format. Keep project-specific creative instructions separate from executable scripts.

Example: a three-word product benefit appears as editable type, slides a small distance into place, holds long enough to read, then exits before the product demonstration. Anchor the text and reserve layout space so a localized phrase does not cover the mechanism. Do not treat animated word emphasis as an accessibility-caption replacement.

## Build and verify

Create a style frame and timing preview before polishing all scenes. For automation, inspect the existing project and save a working version; preserve unrelated compositions. Check font substitution, expressions, missing footage, plugin availability, motion blur, bounds and safe areas. If no AE execution access exists, deliver the script/project specification honestly as unexecuted.

## Selected sign repair

For a selected sign repair, follow the shared [occlusion workflow](repair-cards.md#sign-replacement-after-an-occlusion). Use suitable tracking/corner-pin data for approved artwork and masks for foreground occluders; Mocha AE is a candidate when available. [Adobe's tracking guide](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html) describes these workflows. Verify the installed tools; do not assume separately licensed Mocha Pro features are included. Test the difficult occlusion/reveal and match lighting/blur before completing the shot.

## Round trip

Use a tested mutually supported codec/image sequence for Resolve handoff, including alpha only where needed. Agree straight/premultiplied handling, frame range and color interpretation. Do not promise native AE effects or editable type will survive an exported timeline into Resolve. Deliver the AE source separately when editability matters, plus a rendered preview/intermediate.

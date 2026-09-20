# Visual development and reference design

## Decide what each visual controls

A mood board explores feeling; a style frame establishes a finished look; a character sheet records an identity; a storyboard communicates a shot; an environment plan records space. Do not treat them as interchangeable model inputs.

For every reference, record `asset ID | role | authoritative details | allowed variation | version`. Typical roles are identity, costume, product geometry, composition, environment, lighting, style or motion. Explicitly resolve contradictory references rather than averaging them accidentally.

Start with a small number of distinct directions only when the user needs a choice. Develop the selected direction instead of repeatedly generating unrelated alternatives. State what the reference is intended to prove and inspect that property before accepting it.

## Reference acquisition before dependent prompts

Inventory existing files, supplied links, accepted assets and verified public sources before requesting more. Record source/date, what each asset establishes, missing coverage and whether it is actually available to the downstream tool. A filename or URL in a prompt is not automatically an attached model input. Ask for specific user-owned references when needed; use available research for public facts rather than making the user gather everything.

| Need | Best evidence to seek | When to request or acquire it |
|---|---|---|
| Named real location | Current photos from the relevant street/directions, readable signs/stall details, day/night context; walking video for motion and route | Before a location-accurate hero frame or 3D build; ask user for a specific street/route only if that choice matters |
| Continuous turns or reverse views | Overlapping views, route map and continuous walking/panning footage where available | Before committing to a camera path; one frontal photograph cannot establish hidden geometry |
| Consistent person | Canonical identity plus front, both profiles, back and required three-quarter/detail views | Before identity-dependent still/video work; inspect user-owned references or develop a clearly fictional reference pack within scope |
| Exact product or prop | Exact model/variant, authoritative multi-angle photos, dimensions, label details, mechanism video/manual where action matters | Before modeling, grip/action prompts or a close-up; ask for user's specific object if public references cannot identify it |
| Look and motion preference | Example image/clip with the intended transferable property named | Before look/motion choices only when the user has a specific preference; not mandatory for every project |
| Place name, voice or music requirement | Native/reference pronunciation audio, intended line/language, usable voice/music asset or direction | Before dependent speech/lip-sync generation or music-led timing |

For real places such as Myeongdong, real photos help distinguish the actual architecture, signage, street furniture, food-stall forms, wear and night lighting from a generic invented market. A walking clip additionally informs occlusion, pace, camera motion and sound when present. Check source location and date; do not assume unrelated views depict adjacent positions. References improve evidence but do not guarantee generated fidelity.

Choose the geometry route after checking the references. If Blender is useful, build/adjust only necessary visible coverage using verified scale/layout evidence, camera matching where feasible, and fixed sign textures; arbitrary photos are not an automatic accurate 3D reconstruction. Photograph-derived detail does not silently authorize moving accepted stalls. If factual location references conflict with a locked invented layout, state the conflict and retain the layout while applying compatible detail, or obtain the user's choice before changing geography.

If no suitable factual references exist, propose a location-inspired alternative and label missing facts unverified. Do not silently relax an exact-location requirement or claim a real-location reproduction. Continue independent work while awaiting an essential user asset; do not commit dependent generation merely because the user has not supplied it yet.

## Design decisions

Select mood, tone, realism/stylization, palette, contrast, texture/materials, light quality and composition based on story and viewing context. Mood is the scene's felt atmosphere; tone is how the work treats its subject. A frightening atmosphere and a playful tone can coexist deliberately.

For branded work, capture exact colors, supplied logos, typography, spacing and mandatory copy. Use editable text/vector layers for final titles, logos and data diagrams. An AI concept image may guide layout, but its lettering is not automatically production-ready.

## Character identity and sheets

For a recurring visible character, establish an accepted identity asset before continuity-dependent production. Developing that identity can itself be an authorized first step. Gather distinguishing features, approximate age presentation, proportions, hairstyle, costume/materials, accessories and performance traits relevant to the film. Do not add gratuitous personal attributes.

This user's character sheets always include front, left profile, right profile and back coverage, with consistent head/hair as well as body and costume. One frontal portrait is the canonical identity anchor; it is not the whole sheet. For turns, 360-degree coverage or future alternate angles, add left/right front and rear three-quarter views. For close-up portrait/video use, include clean head views at the relevant profile and three-quarter angles. Do not omit profiles or rear head details under a “single face only” interpretation.

“Turns” here means a change in the character angles the audience sees, whether caused by character movement or the camera moving around them. A camera pivoting from the street to a largely frontal selfie does not necessarily show the character's back; retain the user's minimum sheet coverage and prepare extra portrait angles actually needed by the projected framing. Future 360-degree use does require the expanded views.

| Panel | Content | Rule |
|---|---|---|
| A: identity anchor | Neutral frontal head-and-shoulders portrait | Canonical face for all other views |
| B: front | Full-body frontal view | Same face, proportions, costume and accessories |
| C–D: profiles | Left and right full-body profile views | Show consistent head profile, hair silhouette and clothing construction; do not mirror asymmetric details |
| E: back | Full-body rear view | Include rear head/hair, garment back and accessory placement |
| F: turning coverage | Left/right front and rear three-quarter views when turns/360-degree coverage are intended | Same person and costume at each angle, not separately invented characters |
| G: portrait/detail coverage | Clean face profiles/three-quarters, hands, footwear or grip as required by the shot | Derive from the canonical identity and inspect anatomical consistency |

If A is a full-body frontal hero, it also supplies the front body view; do not duplicate it merely to fill a grid. Use neutral, even light, a plain background, consistent proportions and generous panel separation. Keep body-view scale consistent; label the portrait as a different scale. Avoid dramatic lens distortion, occluding poses or different outfits in the same identity board.

This is this user's reference-coverage requirement, not a universal guarantee of model fidelity. Generate other views from the canonical identity, then compare ear/nose/jaw shape, hairline, body proportions, seams, strap side and accessories. Generated unseen angles are proposed interpretations, not verified observations of a real person. A sheet does not prove a continuous 3D identity; validate a turntable or angle-transition test when the action requires it. Keep the pack incomplete until required views exist and pass inspection. An explicit user scope exception can override coverage; an attractive frontal image cannot silently do so.

Create or crop clean individual files for submission. A human-facing contact sheet is for review, not a default input to every model. If a model explicitly supports sheets/multi-view input, check its required format. A text description saying "same person" does not guarantee identity.

Character-sheet prompt pattern:

> Establish CHAR-01 from the supplied canonical frontal portrait. Prepare clearly separated full-body front, left profile, right profile and back views, including consistent head and hair. For the planned turn, also prepare front and rear three-quarter views from both sides. Match facial anatomy, body proportions, garment construction, colors and asymmetric accessories across views. Plain background, neutral light and consistent body-view scale. All views depict the same identity. Export clean individual angle references as well as a human review board.

This is a creative prompt, not proof that a model will obey it. Inspect every panel, split into separate outputs if needed, and omit unsupported reference/negative-prompt syntax. Render exact labels afterward.

## Environments

Record location, time/weather, geography, entrances/exits, major landmarks, materials, scale and lighting direction. For connected shots, create a simple top-down plan or a Blender blockout when it prevents spatial drift. Separate the stable layout reference from a mood image whose architecture may be inconsistent.

For a camera turn, prepare both directions and intervening coverage from one consistent environment; do not build reverse views by mirroring the forward image. Classify the set as inspired, recognizable or exact. Keep fixed signage text as verified editable textures/plates when it must survive motion. A realistic AI still based on Blender is a 2D interpretation, not proof that its invented reverse views will match the source geometry.

For a room: locate door, window, furniture and actors on the plan; choose the action axis before coverage. For a world: specify recurring design rules and only the locations shown. Do not require a huge world bible for one shot.

## Products, props and costume

Use real product photos, dimensions, approved labels and functional details when accuracy matters. Distinguish a concept product from an existing SKU. A beauty image is not evidence that a hinge, screen or attachment works correctly. Use controlled 3D/real footage/compositing for strict geometry and logos when generation cannot hold them.

Track asymmetric details explicitly: logo side, clasp position, handedness, pocket, scar or accessory. Mirroring an image can create a continuity error even when it looks attractive. A wardrobe change gets a new variant ID linked to the same character identity.

## Sprite sheets and 3D references

Only load this branch for sprite/animation/modeling needs. Specify dimensions, frame count/order, consistent pivot/baseline, padding, alpha and intended action. Orthographic modeling views need consistent scale and alignment; perspective concept art cannot establish exact orthographic geometry. Keep facial-expression studies separate from the base sheet unless the downstream tool specifically needs them.

## Acceptance

Check identity, proportions, symmetry/asymmetry, garment construction, prop count, materials, environment layout, intended aspect/crop and unwanted text. Record what is accepted and unresolved. Review references at the size/angle they will actually support. A tiny face in a full-body sheet may be insufficient for a later facial close-up.

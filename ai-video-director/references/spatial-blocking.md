# Spatial blocking and path references

Load when arrival, stopping, interaction and departure must share a layout; when left/right depends on viewpoint; or when a diagram resolves a consequential path ambiguity. A simple unrelated shot does not need a map.

## Establish the world before the frame

Use a compact plan or existing blockout: fixed landmarks/obstacles, scale, actor or vehicle positions, intended route, stop pose, camera position and target. Distinguish world directions, subject-local left/right and screen directions. A reverse camera angle changes screen direction without moving the actors to different seats.

For vehicle scenes, record driving side for the setting, steering-wheel side, occupant seat map, vehicle heading, curb/traffic side and the intended door. Plan the space swept by the vehicle during arrival and departure, door swing and the character's exit path. A convincing stop between parked cars may prevent the required direct departure. Resolve that before locking the anchor, rather than demanding motion through an obstacle later. Preserve the same background relationships through cabin windows and exterior cuts.

## Give diagrams a limited role

Keep a clean layout source and a labeled planning diagram. State the legend and whether the diagram controls trajectory, position, timing or geometry. If its drawn cars are only schematic context, explicitly assign real obstacle positions to the layout source. Resolve conflicts instead of asking the model to both honor and ignore the same car.

Mark start, route, stop orientation and exit. Relate the diagram to identifiable world landmarks; an unscaled arrow cannot prove turning clearance. Translate into the tool's supported inputs, inspect any crop/rotation and ensure colored lines or sketch styling do not enter the result. Use a cheap camera/path preview when clearance or occlusion remains uncertain.

## Lock the consequential anchor

Plan in dependency order using [sequence anchors](shots-prompts.md#sequence-anchors-and-generation-units). A stopped dialogue scene may determine the incoming arrival and outgoing departure even though it occurs in the middle of the film. Save its accepted layout/version; changes to the stopping pose invalidate only connected coverage that depends on it.

Review adjacent shots and the full motion for seat/door consistency, background/window alignment, feasible entry/exit, correct screen direction and stable obstacles. A diagram or still demonstrates a plan, not successful execution. When a required complex path cannot be controlled reliably, compare a controlled render/composite or available real coverage before another generation.

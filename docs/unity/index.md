# Stair Generator for Unity

Stair Generator builds staircases and railings at real-world sizes from a handful of settings: straight, landing, L
and U stairs, winders, curved and spiral stairs, with nosed treads, stringers, turned balusters, newel posts, moulded
handrails, curtails and volutes. Stairs update as you edit them, come with collision that's comfortable to walk and
teleport on, and bake to mesh assets for shipping.

It needs Unity 6.3 or later, and works with URP, HDRP and the Built-in render pipeline. Stairs use your render
pipeline's default material until you give them your own.

To read this manual in Unity, choose **Tools > Stair Generator > Manual**, or press **Manual** at the top of a
Staircase or Railing inspector to open it at that component's section. It opens in its own window: **Contents**
lists the sections, clicking a line with a link follows it, **Open Online** opens the same manual on
docs.technomyth.com, and **Open File** opens its Markdown file in your own editor. The Package Manager's
**Documentation** and **Changelog** links open them on docs.technomyth.com.

## Contents

- [Quick start](#quick-start)
- [Parts of a staircase](#parts-of-a-staircase)
- [Shaping a staircase](#shaping-a-staircase)
- [Railing style](#railing-style)
- [Railings on their own](#railings-on-their-own)
- [Presets](#presets)
- [Materials and UVs](#materials-and-uvs)
- [Collision, walking and VR](#collision-walking-and-vr)
- [Levels of detail](#levels-of-detail)
- [Baking](#baking)
- [Checking a scene](#checking-a-scene)
- [Performance](#performance)
- [The Showcase sample](#the-showcase-sample)
- [Scripting](#scripting)
- [Limits](#limits)
- [Troubleshooting](#troubleshooting)

## Quick start

1. Choose **GameObject > TechnoMyth > Stair Generator** and pick a staircase. The presets are described under
   [Presets](#presets); Grand Staircase (Dog-Leg) is a good first try.
2. Place it. It appears in the middle of the Scene view, standing on the floor there if the floor has a collider,
   and climbing away from you. The pivot is the middle of the bottom step's front, on the floor, and the stair climbs
   along its blue (+Z) axis. A spiral's pivot is the centre of its column instead, so it stays put as the stair
   widens. To copy a staircase you've changed, select the staircase itself, not its Mesh child, and duplicate it.
3. With it selected, drag the **Total Rise** handle in the Scene view up towards the floor above: it adds or
   removes whole steps, keeping each step as high as it was. To fit a floor height exactly, type it into **Total
   Rise**, or set **Riser Height** for the step height you want. The line at the top of the inspector shows the
   pitch and the comfort figure, two risers plus the tread depth.
4. Give the **Mesh** child's Mesh Renderer your materials: element 0 for treads and landings, 1 for risers, stringers
   and the underside, 2 for railings.
5. Before shipping, choose **Tools > Stair Generator > Bake All in Open Scenes**.

## Parts of a staircase

The settings use the usual joinery terms:

| Term | Meaning |
|---|---|
| Rise, Total Rise | Height climbed: one step's rise, or floor to floor for the whole stair |
| Riser | The upright face of a step. Riser height = Total Rise / Riser Count |
| Tread Depth | How deep a step is from riser face to riser face, not counting the nosing: the going in British joinery, the run in the US |
| Tread, Nosing | The step you stand on, and its front edge that overhangs the riser below |
| Stringer | The board along each side of a flight. A *closed* stringer runs above the steps; a *cut* one is cut to the steps' shape under the tread ends |
| Newel post | The post at each end of a railing and at its corners |
| Baluster | The upright spindles between handrail and stringer or treads |
| Landing, Winder | A flat platform where the stair pauses or turns; winders are steps that fan round a turn instead |
| Curtail, Volute | A bottom step that curls round at its end; a handrail scroll that curls over it |
| Soffit | The sloped ceiling under a flight |
| Walk line | The line up the middle of a flight, where a curved stair's tread depth is measured |

Comfortable stairs have risers of 150 to 220 mm, a tread depth of 220 to 320 mm, and two risers plus the tread depth between
550 and 700 mm. The inspector warns outside these, and when a handrail is lower than 850 mm.

## Shaping a staircase

Select a staircase to see its settings. The inspector shows only the settings that do something for the chosen
layout and options; for example Well Gap appears only on a U stair, and the curtail settings only when the start step
is a curtail. Problems with the settings show at the top of the inspector.

### Scene-view handles

With a staircase selected, yellow handles in the Scene view set its size by eye. Drag along the dotted line:

| Handle | Where it is | What it sets |
|---|---|---|
| Total Rise | Top of the stair | Riser Count, a whole step at a time, with Total Rise following at the same riser height |
| Width | Side of the first tread (on a spiral, its outer end) | Width |
| Landing | Front of the landing or winder turn | Landing After Riser, a riser at a time |
| Landing Depth | Back of a straight, U or split landing | Landing Depth |
| Well Gap | On the landing, at the side of the first flight a U or returning split stair turns towards | Well Gap: drag it out to open a gallery between the flights |
| Landing Gap | On the landing, at the side of the first flight an L or sideways split stair turns towards | Landing Gap; drag it back to the first flight to remove the gap |
| Branch Width | Far edge of a split stair's right upper flight, on its first tread | Branch Width |
| Top Landing | Top edge | Top Landing Depth; drag it back to the top step to remove the top landing |
| Inner Radius | Centre of a curved stair, on the floor, or the edge of a spiral's column | Inner Radius: a curved stair's centre moves, a spiral's column grows |
| Curve Angle | Outer end of a curved or spiral stair | Curve Angle |

Every handle change can be undone.

### Size and steps

| Setting | What it does |
|---|---|
| Total Rise | Floor to floor height. Typing a new one adds or removes steps to keep the risers about as high, then fits them to it exactly |
| Riser Count | Number of steps up, counting the step onto each landing and onto the top floor. Changing it keeps the risers as high as they are, so the stair gets taller or shorter |
| Riser Height | Height of each step. Changing it keeps Riser Count, so the stair gets taller or shorter. It's Total Rise divided by Riser Count, not stored separately |
| Tread Depth | Depth of each step, riser face to riser face. Curved and spiral stairs work it out from Curve Angle instead |
| Width | Each flight, outside to outside; stringers are inside this width |
| Top Landing Depth | A nosed strip at the top for meeting the upper floor; 0 for none |
| Nosing | Square, Chamfered, Bullnose (half round) or Rounded front edges |
| Nosing Overhang, Tread Thickness | How far a tread overhangs the riser below, and how thick it is |
| Risers | Off for open risers |
| Riser Thickness | Thickness of the risers |

### Layouts and turns

| Layout | Shape |
|---|---|
| Straight | One flight |
| Straight With Landing | Two flights in a line with a landing between |
| L-Shaped | Two flights at right angles with a square quarter landing |
| U-Shaped | Two flights side by side going opposite ways with a half landing (a dog-leg) |
| Curved | One flight curving round an arc |
| Spiral | Treads fanning round a central column |
| Split | A wide first flight up to a landing, then two narrower flights, one on each side (a bifurcated or imperial stair) |

| Setting | What it does |
|---|---|
| Turn | Which way an L, U, curved or spiral stair turns, seen going up |
| Landing After Riser | Risers below the landing; 0 puts it halfway |
| Landing Depth | Depth of a straight, U or split landing; 0 makes it as deep as the flight after it is wide. An L landing is as deep as the stair is wide |
| Well Gap | Gap between the flights of a U stair, or between a split stair's first flight and the upper flights returning beside it. The landing spans it, with the railing along its edge, so a wide gap makes a gallery between the flights |
| Landing Gap | A stretch of landing before the second flight of an L stair, or before each upper flight of a split stair that goes sideways, with the railing along it. 0 for none |
| Turn Style | Landing, or Winders: steps that fan round the turn from the newel post on the inside, each a riser higher |
| Winders Per Quarter Turn | 2 to 6. A U stair turns two quarters, so 3 per quarter gives 6 winders. Each winder after the first is a riser taken from the flights |

Round the outside of a winder turn, the stringer and railing follow the winder nosings, with a post at each corner.
On the inside, the newel post takes the handrail in low from the first flight and out high to the second.

### Split stairs

A split stair climbs one wide flight to a landing, then divides into two mirrored upper flights.

| Setting | What it does |
|---|---|
| Split Style | Return: the upper flights turn back alongside the first, one on each side, like two U stairs. Sideways: they go off left and right, like two L stairs |
| Branch Width | Width of each upper flight; 0 makes them as wide as the first |
| Outer Railing | A railing down the outer side of one upper flight, round the back of the landing and up the other |
| Outer Railing Type | Balustrade, or Wall Handrail for a landing between walls |

Left and Right Railing run up the first flight, along the landing and up the side of that side's upper flight
nearer the middle. Each upper flight takes the stringer settings of its own sides, seen going up it. Add Stairwell
Railing isn't offered, as there are two tops: a railing that starts or ends at a split stair's Left or Right joins
the top of that side's upper flight, at its side nearer the middle.

### Curved and spiral stairs

| Setting | What it does |
|---|---|
| Inner Radius | Radius of the inside edge of a curved stair, or of a spiral's column |
| Curve Angle | How far the stair turns, in degrees, from the first riser to the top (up to three full turns) |

The tread depth is measured along the walk line down the middle of the flight, so it comes from the radius and angle; the
inspector shows it. A spiral's treads run into its column, and it has no inner stringer or railing. A spiral turns
about its pivot, the centre of the column, and its first step starts beside the pivot, climbing along +Z; changing
its width moves only the outside edge.

### The bottom step

| Setting | What it does |
|---|---|
| Start Step | None; Bullnose, where the step's front bows out; or Curtail Left, Right or Both, where the step curls round in a half circle at that end, with the newel post and stringer standing on the curl |
| Start Step Extension | How far the bottom step reaches out beyond a normal step |
| Curtail Segments | Smoothness of each curl |
| Curtail Volute | Over a curtail, end the handrail in a volute instead of a newel post: it eases down to level and scrolls outward round the curl to an eye, with balusters standing on the curl |
| Flare | The first flight's bottom steps fan out on Both sides, the Left or the Right. The nosing returns round the flared ends, and on a flared side the newel post and stringer stand on the last flared step. On an L or U stair, flare the outer side |
| Flare Steps, Flare Width, Flare Curve | How many steps fan out, how far the bottom one reaches past the flight on each side, and whether the step ends sweep round (Smooth) or follow a straight line (Linear) |

### Sides and underneath

| Setting | What it does |
|---|---|
| Left/Right Stringer | A stringer on that side, seen going up. Without one, the tread ends show and balusters stand on the treads |
| Left/Right Stringer Style | Closed, a straight board above the steps that balusters stand on; or Cut, cut to the steps under the treads, whose nosings return round their ends over it, with balusters standing on the tread ends |
| Stringer Thickness, Stringer Above, Stringer Depth | Board thickness, how far its top is above the nosings, and its depth (raised if too shallow to cover the steps) |
| Underside | Open, showing the treads and risers from below; Soffit, a sloped ceiling under each flight; or Solid, closed down to the floor like a stair with a cupboard under it |
| Landing Thickness | Thickness of landings and the top landing |

### Railings on a staircase

| Setting | What it does |
|---|---|
| Left/Right Railing | A railing on that side, seen going up. On an L or U stair it continues round the landing; on a split stair, see [Split stairs](#split-stairs) |
| Left/Right Railing Type | Balustrade, with balusters and newel posts; or Wall Handrail, a handrail on the wall beside the stair. The wall is taken to be at the stair's edge |

How the railings look is set by the staircase's [railing style](#railing-style).

## Railing style

Staircases and standalone railings share these settings:

| Setting | What it does |
|---|---|
| Height | Top of the handrail above the step nosings, or above the floor on level runs |
| Handrail, Handrail Width, Handrail Height | Round, Mushroom (rounded top on a narrower base), Moulded (a Victorian crowned rail), Rectangular or None, and its size |
| Balusters, Baluster Width | None, Square, Round, Turned Vase or Turned Bobbin; turned ones have square blocks at each end |
| Balusters Per Tread | 1 to 4 on each step of a flight |
| Baluster Spacing | Largest centre-to-centre spacing on level runs |
| Newels, Newel Width, Newel Projection | None, Square (with a moulded cap) or Turned (square up past the handrail, then turned with a ball finial), its width, and how far it rises above the handrail |
| Round Sides | Sides on turned and round parts: more is smoother and costs more triangles |
| Wall Clearance | Gap between the wall and a wall handrail |
| Bracket Spacing | Largest distance between a wall handrail's brackets |

A wall handrail has no balusters or newel posts. It runs as one rail round landings, winders and curves on brackets
spread evenly along it.

## Railings on their own

For galleries, balconies and landing edges, choose **GameObject > TechnoMyth > Stair Generator > Railing**.

- Drag its points in the Scene view. Hold Shift and click a point to add one after it. Each point is a spot on the
  floor; points can differ in height, and the railing then runs down the slope with its balusters upright.
- **Closed** joins the last point back to the first.
- **Newel Placement** puts newel posts at every point, at the ends and corners, or at the ends only.
- **Start At** and **End At** join an end to a staircase's top newel post: pick the staircase and the side. That end
  moves to the post and shares it instead of drawing a second one, and follows the staircase when you change or move
  it. A joined end shows "(joined)" in the Scene view and has no handle. Closed railings don't join staircases.

**Add Stairwell Railing**, on a staircase's inspector, adds the balustrade round the opening in the floor above the
stair as a child of the staircase. It runs back from the left top newel along the stairwell, across, and up to the
right top newel, joined at both ends, and reaches back as far as the stair needs headroom (2 m under a 250 mm floor).
Edit its points to fit the room, or delete the points on a side that's against a wall. On an L or U stair it's sized
for the top flight. It isn't offered on curved and spiral stairs.

## Presets

Each preset is a starting point: pick one from **GameObject > TechnoMyth > Stair Generator** to place a new staircase,
then change it to suit.

To apply one to a staircase you already have, import them as Unity presets first: in **Window > Package Manager**,
select Stair Generator, open **Samples** and press **Import** beside **Presets**. They're copied into
`Assets/Samples/Stair Generator`. Then click the preset icon (the sliders at the top right of the Staircase component)
and pick one. These presets set the shape and railing style only, leaving the levels of detail and any bake alone.

| Preset | What it is |
|---|---|
| Grand Staircase (Dog-Leg) | A Victorian U stair with a half landing, a curtail bottom step, turned balusters and newels and a moulded rail |
| Grand Staircase (Straight) | A wide straight flight up to a gallery, curtails on both sides, balustrades on both sides |
| Grand Staircase (Flared) | A straight flight whose bottom four steps fan out, with a bullnose first step and cut stringers |
| Grand Staircase (Curved) | A wide flight curving through 140°, with balustrades on both sides |
| Grand Staircase (Split) | An imperial stair: a 1.8 m flight up to a half landing, then two 1.1 m flights returning beside it, with curtails on both sides and wall handrails round the landing |
| Attic Stair | A narrow, steep stair between walls with a wall handrail |
| Back Stair | A plain servants' stair with square balusters and newels |
| Winding Stair | A narrow back stair turning a corner on three winders, with a balustrade inside and a wall handrail outside |
| Spiral Stair | A compact spiral round a column, with open treads and a slim outer railing |
| Cellar Stair | An open-riser stair with a wall handrail |
| Georgian Stair (Dog-Leg) | A U stair with a cut string, slender round balusters three to a tread, and a plain rail ending in a volute over a curtail |
| Modern Open-Riser Stair | A straight open-riser flight with square-edged treads, slim square balusters and a flat-topped rail |

### Your own presets

To keep a staircase you've set up, click the preset icon on its Staircase component and choose **Save current
to...**. Unity saves a `.preset` file in your project; pick it from the same icon to apply it to another staircase,
and Undo puts the old settings back. To make one the starting settings for every Staircase you add with **Add
Component**, open it and press **Add to Staircase default**, or set it in **Project Settings > Preset Manager**; the
GameObject menu always places the preset you pick.

A saved preset holds every Staircase setting, including the levels of detail. To leave some alone when it's applied,
untick them in the preset's inspector. To share presets across projects, copy the `.preset` files.

## Materials and UVs

A staircase or railing draws with three materials on its **Mesh** child:

| Element | Parts |
|---|---|
| 0 | Treads, landings and the top landing |
| 1 | Risers, stringers, the soffit or solid underside, and a spiral's column |
| 2 | Handrails, balusters, newel posts, wall brackets and volutes |

Textures are mapped at world scale: one unit of texture space is one metre, projected along each face, so a texture
tiles evenly whatever the stair's size and never stretches. Tiling or trim textures suit this best. Each element can
use any material and shader your render pipeline supports.

Set materials on the Mesh child only. Its level-of-detail siblings, "Mesh LOD1" and "Mesh LOD2", take the same
materials automatically in the editor.

## Collision, walking and VR

Each staircase has two collider children:

- **Walk Surface**: one Mesh Collider made of a smooth ramp through the step nosings plus the landings, winders and
  shaped bottom steps. Character controllers walk up it without stepping, and VR players don't bob. It starts at the
  front edge of the bottom tread, so a character steps up onto the first step. To teleport onto stairs, make this
  child a teleport target, for example by adding an XR Interaction Toolkit Teleportation Area to it. Put it on the
  layer your game uses for floors; regenerating keeps its layer.
- **Railing Colliders**: a box per railing span and newel post, so players can't walk through railings.

Standalone railings have railing colliders only.

## Levels of detail

**LOD Levels** (1 to 3, default 3) adds simpler versions of a staircase or railing under a LOD Group on it. Every
level keeps the same shapes, so switching doesn't pop:

| Level | What's simpler |
|---|---|
| LOD0 | Full detail |
| LOD1 | Half the sides on turned and round parts, and half the curtail segments |
| LOD2 | A quarter of the sides, and turned parts and handrails with about half their profile points |

The LOD Group's transition heights are yours to change; they're kept when the stair is rebuilt. Colliders and the
walk surface always use full detail. Set LOD Levels to 1 for no LOD Group.

## Baking

Generated meshes aren't saved in scenes. A staircase or railing that isn't baked is generated when its scene loads,
which costs time and, in a player, logs a warning. Baking saves its meshes as `Stair_<id>.asset` or
`Railing_<id>.asset` in the bake folder, with the walk surface and lower levels of detail inside it. Identical
staircases share one asset.

- **Bake** and **Unbake** are in the inspector, and **Bake Selected**, **Unbake Selected**, **Bake All in Open
  Scenes** and **Rebuild Baked Meshes in Open Scenes** are under **Tools > Stair Generator**.
- Changing a baked staircase makes its bake out of date; it's generated again until you bake it. The inspector shows
  the bake's state and triangle counts.
- **Unbake** goes back to generating and leaves the asset in place.
- **Rebuild Baked Meshes in Open Scenes** regenerates existing bakes, for example after updating the package or
  turning on lightmap UVs.
- Baked meshes have Read/Write turned off, so a build doesn't keep a second copy of them in memory. The walk surface
  keeps it, so its collider can be built when a stair is spawned at runtime. Older bakes keep Read/Write until you
  rebuild them.

Project-wide settings are in **Project Settings > Stair Generator**:

| Setting | Default |
|---|---|
| Bake Folder | `Assets/StairGenerator/Meshes` |
| On Save Behaviour | Warn in the Console about unbaked stairs when a scene is saved; or Auto Bake them; or Off |
| Generate Lightmap UVs | On: baked meshes get a second UV set for baked lighting |
| Mark Baked Static | On: baked stairs are marked static for lightmapping, batching and occlusion culling |
| Triangle Budget | 25,000: Check Scene flags stairs and railings with more triangles than this at full detail; 0 turns the check off |

## Checking a scene

**Tools > Stair Generator > Check Scene** opens a window listing every staircase and railing in the open scenes that
has a problem: settings errors and warnings, not baked or out of date, over the triangle budget, a missing material,
or a copy of its Mesh child (see [Troubleshooting](#troubleshooting)). Click a name to select it. **Bake** fixes a
bake problem; the toolbar button bakes them all.

**Tools > Stair Generator > Delete Unused Bakes** finds baked meshes in the bake folder that no scene or prefab in
Assets uses and nothing in the open scenes uses. It lists them and, if you agree, moves them to the system trash,
where you can restore them. Scenes inside packages aren't checked.

## Performance

Triangles at full detail and the two lower levels:

| Preset | LOD0 | LOD1 | LOD2 |
|---|---:|---:|---:|
| Grand Staircase (Dog-Leg) | 9,230 | 5,390 | 4,238 |
| Grand Staircase (Straight) | 19,740 | 11,020 | 8,412 |
| Grand Staircase (Flared) | 17,154 | 10,082 | 7,922 |
| Grand Staircase (Curved) | 21,052 | 12,836 | 9,892 |
| Grand Staircase (Split) | 21,524 | 12,596 | 9,796 |
| Georgian Stair (Dog-Leg) | 3,754 | 2,770 | 2,362 |
| Spiral Stair | 3,128 | 2,504 | 1,868 |
| Winding Stair | 1,374 | 1,374 | 1,286 |
| Back Stair | 968 | 968 | 952 |
| Modern Open-Riser Stair | 698 | 698 | 698 |
| Attic Stair | 560 | 560 | 536 |
| Cellar Stair | 376 | 376 | 352 |

Turned balusters cost the most. Fewer **Round Sides**, fewer **Balusters Per Tread**, or square balusters bring a
staircase down quickly. Bake everything before shipping, and keep the default three levels of detail for mobile and
standalone VR.

Stairs with square balusters and newels and plain rails have no curved parts to simplify, so their lower levels of
detail save little. Set **LOD Levels** to 1 on those to save the LOD Group.

## The Showcase sample

Import it from the Package Manager: select **Stair Generator**, open the **Samples** tab and click **Import** next to
**Showcase**. It's copied to `Assets/Samples/Stair Generator`. Open the scene for your render pipeline:

| Pipeline | Scene |
|---|---|
| URP | `URP/Showcase URP` |
| HDRP | `HDRP/Showcase HDRP` |
| Built-in | `BuiltIn/Showcase Built-in` |

The other pipelines' folders aren't used and can be deleted. The scenes have:

- **Stair hall**: a Grand Staircase (Dog-Leg) in a stairwell off a tiled hall, climbing to a gallery. The gallery's
  balustrade is a Railing of its own, and the stairwell railing ends on the staircase's top newel post.
- **Attic stair**: between walls, with a wall handrail.
- **Spiral stair**: up to a platform whose railing ends on the spiral's top post.
- **Split stair**: the Grand Staircase (Split), an imperial stair with wall handrails round its landing.
- **Grand presets** and **Everyday presets**: every preset, as the GameObject menu places it.

The materials are **Oak** for treads, **Paint** for risers and stringers, **Mahogany** for railings, and
**Black Steel** for the spiral's and the modern stair's railings, with **Plaster**, **Tiles** and **Stone** for the
rooms. Their grain and wear are baked into textures, so they use each pipeline's standard Lit (or Standard) shader and
can be copied into your project. They tile once a metre, to suit the stairs' world-scale UVs.

In Play mode, press **1** to **9** to move between the stations, or **Tab** for the next one. Everything is baked.

## Scripting

Everything in the inspector can be set from code; the components regenerate when you set a property.

```csharp
using TechnoMyth.StairGenerator;
using UnityEngine;

public class BuildStairs : MonoBehaviour
{
    void Start()
    {
        var staircase = new GameObject("Stair").AddComponent<Staircase>();
        staircase.ApplyPreset(StairPreset.GrandDogLeg);

        var shape = staircase.shape;
        shape.totalRise = 3.2f;
        shape.riserCount = 18;
        staircase.shape = shape;

        if (staircase.TryGetTopNewel(StairSide.Left, out var top))
        {
            var gallery = new GameObject("Gallery").AddComponent<Railing>();
            gallery.transform.SetParent(staircase.transform, false);
            gallery.SetPoints(new[] { top, top + new Vector3(0f, 0f, -3f) });
            gallery.startAt = new StairConnection(staircase, StairSide.Left);
        }
    }
}
```

| Member | Use |
|---|---|
| `Staircase.shape`, `Staircase.railing` | Get, change and set back the settings as `StairShape` and `RailingStyle` structs; `StairShape.Default` and `RailingStyle.Default` are the defaults |
| `Staircase.ApplyPreset(StairPreset)`, `StairPresets.Get` | Apply a preset, or read its settings |
| `Staircase.TryGetTopNewel(StairSide, out Vector3)` | Where a side's top newel post stands, in the staircase's local space |
| `Railing.SetPoints`, `points`, `closed`, `newelPlacement`, `style`, `startAt`, `endAt` | A standalone railing's path and settings |
| `lodLevels`, `SyncLodMaterials()` | Levels of detail; call `SyncLodMaterials()` after changing materials in a player |
| `messages`, `triangleCount`, `lodTriangleCounts` | Problems with the settings, and triangle counts |
| `isBakeCurrent`, `bakedMesh`, `geometryHash` | Baking state |
| `geometryUpdated` | Event raised after the meshes are generated or a bake is applied |
| `UpdateGeometry()` | Regenerate now |

Generating in a player works but is slower than loading a bake, and logs a warning once per object. In the editor,
`StairBaker`, `StairSceneCheck` and `StairBakeCleanup` (namespace `TechnoMyth.StairGenerator.EditorTools`) give
scripts the baking and checking tools.

## Limits

- Curved and spiral stairs don't have start steps, flares, winders or cut stringers; a Cut stringer style is built
  closed on them.
- Add Stairwell Railing sizes the opening for the top flight only, and isn't offered on curved and spiral stairs.
- Balusters and newel posts are made by the generator; using your own meshes for them isn't supported yet.
- Wall handrails assume the wall is at the stair's edge.

## Troubleshooting

| Problem | What to do |
|---|---|
| The stair is pink or plain grey | Assign materials to the Mesh child's three elements (see [Materials and UVs](#materials-and-uvs)) |
| "Generated at runtime" warning in a player | The stair isn't baked or changed since baking. Use Check Scene, then bake |
| No handles in the Scene view | Select the staircase, and fix any errors shown at the top of its inspector |
| A joined railing doesn't follow the staircase | Check Start At or End At names the staircase, and that the railing isn't Closed |
| A setting seems to be missing | The inspector hides settings that don't apply to the chosen layout and options |
| The lower levels of detail have the wrong materials | Set materials on the Mesh child; in a player call `SyncLodMaterials()` |
| A copied staircase changes when the original does, and its inspector has no settings | You duplicated the Mesh child, not the staircase. Select the copy and click **Make a Separate Staircase**, or delete it and duplicate the staircase itself |
| A baked staircase looks out of date after updating the package | Use Rebuild Baked Meshes in Open Scenes |

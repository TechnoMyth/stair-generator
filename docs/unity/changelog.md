# Changelog

## [1.0.0]

The first release.

- **Staircases** at real-world sizes: straight, straight with a landing, L, U (dog-leg) and split (imperial or sideways) layouts, winders, and curved and spiral stairs. Set the total rise, riser count or riser height, tread depth and width; the inspector shows the pitch and comfort figure and warns about uncomfortable sizes and low handrails.
- **Steps and sides**: square, chamfered, bullnose or rounded nosings; open or closed risers; closed or cut stringers on each side; open, soffit or solid undersides; bullnose and curtail bottom steps; flared bottom steps; landing and well gaps for galleries between flights.
- **Railings**: round, mushroom, moulded or rectangular handrails; square, round, turned vase or turned bobbin balusters; square or turned newel posts; volutes over curtails; wall handrails on brackets. Handrails meeting without a newel post are joined in one mitred run.
- **Railing component** for galleries and landings along a path of points, which can join a staircase's top newel post and follow it. Add Stairwell Railing puts a balustrade round the opening above a stair.
- **Presets**: twelve staircases from a Victorian dog-leg to a modern open-riser stair, in the GameObject menu and as Unity presets in the Presets sample.
- **Scene-view handles** for total rise, width, landings, gaps, top landing and a curved stair's radius and angle.
- **Collision**: a smooth walk surface through the nosings for character controllers, VR and teleporting, and box colliders for railings.
- **Levels of detail**: up to three, keeping the same shapes so switching doesn't pop.
- **Baking** to mesh assets for shipping, with lightmap UVs, static flags and Read/Write off; identical stairs share a bake. Check Scene lists unbaked, out-of-date, over-budget stairs and missing materials, and Delete Unused Bakes tidies the bake folder.
- **Materials**: three slots (treads, structure, railings) with world-scale UVs, for any render pipeline.
- **Showcase sample**: a Victorian stair hall with a grand dog-leg stair and gallery, an attic stair, a spiral stair, a split stair and every preset, baked, with materials for URP, HDRP and Built-in.
- **Manual** in the editor (Tools > Stair Generator > Manual) and at docs.technomyth.com, and a scripting API for building stairs from code.

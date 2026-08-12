# Phase A Director Proposal Contract

Produce a readable Chinese director proposal and stop for explicit approval before creating final SRT or video-generation prompts.

Read `visual-style-system.md` and `duration-presets.md` first.

## Header

Present, in order:

1. Chinese video title
2. book title and author when reliably known
3. selected narrative architecture
4. opening hook
5. one-sentence core message
6. spoiler level
7. aspect ratio and target duration
8. number of fixed 10-second generation containers and any final trim requirement
9. chosen literary editorial illustration direction
10. dominant background or atmospheric field
11. up to three accent colors and semantic roles
12. three to five book-specific recurring motifs
13. one distinctive environmental or compositional signature
14. narration voice direction and estimated Chinese character count
15. BGM direction and emotional curve

## Narration architecture

Write natural spoken Chinese around the selected number of 10-second containers. Use `duration-presets.md` for density targets. Keep every spoken sentence inside one container. Use 1 to 3 short spoken blocks per used container. Prefer concrete images, short sentences, clean pauses, and one central question. Avoid essay-like syntax and overloaded abstractions.

Reserve about 0.8 to 1.5 seconds of non-speech breathing room near most container endings when practical. Phase A timing may be approximate. Exact SRT timestamps belong to Phase B.

## Storyboard

Produce exactly one row per generation container using:

| Time | Narrative job | Book-specific scene and motif | Three visual beats | Camera and transition | Draft Chinese narration | Pause intention | BGM and SFX |
|---|---|---|---|---|---|---|---|

Generate consecutive 10-second windows from `00:00-00:10`. If target duration is not divisible by 10, mark the final row with the exact cut point and identify the unused tail that will be trimmed.

Give every row a distinct narrative job and at least one book-specific visual element. Make at least one motif recur in three or more rows when there are at least three containers.

## Visual design

Use modern literary editorial illustration animation: clean 2D illustration, age-appropriate simplified figures, crisp linework, flat separated color shapes, strong negative space, and book-specific scenery. Do not default to traditional stick figures or photorealistic AI actors. Do not mix flat characters with photographic moons, stock textures, or unrelated 3D objects.

## Continuity

Name the transition interface between every adjacent pair. Use a pose, object, color field, moving camera, shape, prop, light source, doorway, page turn, falling object, brush stroke, weather element, or another visible state that can be matched across clips. Use the final 1 to 1.5 seconds as a transition zone when practical. For a trimmed final container, make the target cut point visually clean.

## Approval ending

Ask the user to approve the current proposal, revise a named scene/narration/palette/motif/duration, or change a global setting. Do not include final SRT timestamps or final video-generation prompts before approval.

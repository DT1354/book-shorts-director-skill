# Phase B Production Contract

Use only after explicit approval of Phase A. Read `visual-style-system.md`, `duration-presets.md`, and `srt-jianying-workflow.md` before production.

Deliver in this order:

1. final SRT timing plan for target duration
2. SRT artifact when file creation is available
3. global literary visual continuity block
4. one standalone English video-generation prompt per 10-second container
5. Jianying/CapCut voiceover handoff
6. stitching guide
7. optional post-production overlays
8. voice and music continuity note

## SRT timing plan

Create exact timestamps for every Chinese narration block. Start at or after `00:00:00,200` unless immediate speech is creatively necessary. End no later than approved target duration. Use 1 to 3 entries per used container, encode ordinary pauses as roughly 0.3 to 0.8 seconds and dramatic pauses as roughly 0.8 to 1.5 seconds, leave breathing room near most 10-second boundaries, and never let an entry cross a 10-second boundary.

When code/file output is available, create the final `.srt` using `scripts/build_srt.py --duration <seconds>` and UTF-8 with BOM.

## Global visual continuity

State aspect ratio, target duration, count of fixed 10-second containers, final trim point when needed, illustration treatment, character locks, dominant field, accent colors, recurring motifs, environmental signature, camera language, SFX strategy, and transition chain.

## Standalone prompt order

Write each prompt in English and make it understandable on its own. Include:

1. exactly 10-second output, chosen aspect ratio, 720p target, 24 FPS
2. approved literary editorial illustration treatment
3. stable character, clothing, prop, and environment locks
4. approved base field and up to three accent colors
5. relevant book-specific motifs and setting cues
6. mobile-first composition
7. exact inherited first-frame state
8. `[0-3s]`, `[3-7s]`, `[7-10s]` visual beats
9. narration concept active during those beats without displaying or speaking Chinese text
10. camera motion, object transformation, synchronized SFX
11. exact final-frame transition state
12. negative constraints

For a final container that will be trimmed, state the target cut timestamp inside that container. Make the used portion resolve cleanly and keep unused tail simple and safe to discard.

## No generated narration

Do not include spoken Chinese or dialogue in generation prompts. Request synchronized environmental SFX and restrained ambience only. Do not generate visible words, captions, book text, logos, or watermarks unless explicitly approved.

## Illustration consistency

Keep all elements inside one illustration world. Stylize moons, suns, oceans, buildings, trees, clothing, animals, furniture, and props to match character treatment. Forbid accidental photorealism, unrelated 3D rendering, traditional skeletal stick figures unless approved, unstable anatomy, photographic textures, muddy grading, unexplained accent colors, generic productivity-icon storytelling, visible writing, and generated narration.

## Jianying / CapCut handoff

Tell the user to import SRT, verify timing, select all subtitle blocks, apply one TTS voice/speed/style, generate speech in batch, and preserve encoded gaps. If a line overruns, shorten text before sacrificing important pauses.

## Stitching

List all containers in order. Repeat every ending state and matching opening state. Mention match cuts, short audio crossfades, SFX bridges, and BGM continuity. Keep each generation at 10 seconds and trim only the unused tail of the final container for non-multiple-of-10 targets.

---
name: directing-book-shorts
description: Create production-ready Chinese literary book shorts with configurable duration, 10-second AI-video containers, SRT-driven Jianying/CapCut text-to-speech timing, deliberate pauses, and original book-specific editorial-illustration art direction. Use when turning a book, chapter, character, quote, theme, or plot idea into a 9:16 short, including 30s, 60s, 90s, 120s, or custom durations, with timed subtitles, post-produced TTS, BGM/SFX guidance, and standalone Omni-style generation prompts.
---

# Directing Book Shorts

Create a source-grounded Chinese book short that feels like a compact visual story. Design narration, subtitle timing, TTS pauses, book-specific art direction, and 10-second video-generation containers as one shared timeline.

## Defaults

Use these defaults unless the user overrides them:

- target duration: 60 seconds
- duration presets: 30, 60, 90, and 120 seconds, plus custom durations
- aspect ratio: `9:16`
- AI-video container length: exactly 10 seconds per generation
- narration language: Chinese
- narration method: imported SRT subtitles plus batch text-to-speech in Jianying/CapCut when supported
- narration structure: 1 to 3 subtitle/TTS blocks per 10-second container
- pause design: encode pauses as empty time gaps between SRT entries
- visual style: modern literary editorial illustration animation with clean 2D shapes, age-appropriate simplified characters, book-specific scenery, and restrained cinematic motion
- generated video speech: none
- generated visible text: none unless explicitly requested

Do not re-ask for defaults. If the user gives only a book title, use 60 seconds. If the user requests another duration, honor it and recalculate the whole timeline.

## Duration model

Read `references/duration-presets.md` whenever the requested duration is not the 60-second default.

For target duration `T`:

- if `T` is divisible by 10, create exactly `T / 10` 10-second video containers
- otherwise create `ceil(T / 10)` 10-second containers, keep narration inside the requested target duration, and trim the unused tail of the final clip in the editor
- never ask the video model for a non-10-second container in this workflow
- never let a spoken sentence cross a 10-second boundary

Standard presets:

- 30s: 3 containers, compact quote, insight, or single emotional turn
- 60s: 6 containers, default balanced short
- 90s: 9 containers, richer character or plot arc
- 120s: 12 containers, fuller literary interpretation

## Workflow

1. Ground the source.
2. Resolve target duration. Use 60 seconds if unspecified.
3. Choose the best storytelling angle.
4. When only a book title or broad topic is given, read `references/story-architectures.md`, present exactly three direction options, mark one as recommended, and stop for selection.
5. After selection, read `references/visual-style-system.md`, `references/duration-presets.md`, and `references/phase-a-contract.md`, then produce Phase A.
6. Stop for explicit approval.
7. After approval, read `references/srt-jianying-workflow.md`, `references/visual-style-system.md`, `references/duration-presets.md`, and `references/phase-b-contract.md`.
8. Build the final subtitle/TTS schedule first. Keep every entry inside its assigned 10-second container and inside target duration.
9. Create an `.srt` artifact with `scripts/build_srt.py`, passing target duration when file output is available.
10. Use that exact SRT schedule and approved art direction to create one standalone English video-generation prompt per 10-second container.
11. Read `references/voiceover-handoff.md` for Jianying/CapCut TTS handoff and local fallback guidance.
12. If the user asks which TTS engine to use, consult `references/tts-options-2026.md` and verify current official documentation when web access is available.

Changing book angle, duration, visual style, narration language, aspect ratio, art direction, or TTS timing invalidates prior approval.

## Source grounding

Preserve the book's factual meaning, plot sequence, characters, and central themes. Prefer paraphrase. Do not invent scenes, motives, endings, statistics, publication facts, author claims, or famous quotes. Avoid major spoilers unless requested.

## Retention rules

Build around one central question or emotional tension. Do not summarize the whole book simply because the duration is longer. Prefer hook-first when unspecified and reveal the book within roughly 5 to 12 seconds. Every 10-second container must contain at least one book-specific prop, location, relationship, recurring motif, or plot action.

## Literary visual identity

Read `references/visual-style-system.md` before planning visuals.

Default to an original literary editorial illustration look, not traditional stick figures and not a photorealistic AI-film look. For every book define:

- one dominant background or atmospheric field
- up to three accent colors with semantic roles
- three to five book-specific recurring motifs
- one distinctive compositional or environmental signature

At least one motif must recur across three or more containers. Large symbolic objects must share the same illustration language as characters. Avoid photographic textures inside an illustrated world.

## SRT and TTS timing

Read `references/srt-jianying-workflow.md` before finalizing timing.

- use 1 to 3 SRT entries per 10-second container
- use 0.3 to 0.8 seconds of silence between ordinary phrases
- use 0.8 to 1.5 seconds for deliberate dramatic pauses
- start after a short opening breath when practical
- leave 0.8 to 1.5 seconds of visual breathing room near most container endings
- never cross a 10-second boundary
- never schedule narration beyond target duration
- keep one TTS voice, speed, pitch, and style across all entries

If a selected voice overruns, shorten the copy before erasing important pauses.

## Visual continuity

Keep recurring characters, proportions, palette, props, locations, and illustration treatment consistent. Design every full 10-second container with three beats: `0-3s` establish, `3-7s` transform/escalate, `7-10s` payoff and transition. For a custom duration that trims the final container, make the requested cut point visually clean and the unused tail safe to discard.

## Narration separation

Do not ask the video model to speak Chinese. Do not embed Chinese narration inside generation prompts. Generate visuals, synchronized SFX, and restrained ambience only. Use the SRT as subtitle and TTS timing master. Keep BGM continuous across target duration and duck it beneath speech.

## Final quality gate

Verify source grounding, natural spoken Mandarin, explicit duration, correct number of 10-second containers, SRT ending within target duration, no boundary-crossing subtitle blocks, real pause gaps, book-specific imagery in every container, a distinct palette and motif package, coherent illustration treatment, transition interfaces, no generated dialogue by default, and no unsupported quotation or factual claim.

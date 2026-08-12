# Duration Presets and Custom Timing

Use 60 seconds when the user does not specify duration. Duration changes the number of 10-second AI-video containers, narration density, and storyboard depth, but does not change the core SRT-first production workflow.

## Standard presets

| Target | 10s containers | Typical Chinese narration | Best for |
|---|---:|---:|---|
| 30s | 3 | about 90 to 110 characters | one quote, one idea, one emotional turn |
| 60s | 6 | about 180 to 210 characters | default balanced literary short |
| 90s | 9 | about 270 to 315 characters | richer character arc or plot hook |
| 120s | 12 | about 360 to 420 characters | fuller interpretation with more scene context |

Character counts exclude punctuation and are starting points, not quotas. Adjust to the selected TTS voice, the number of dramatic pauses, foreign names, and emotional delivery.

## Custom durations

For target duration `T` seconds:

1. Compute generation containers as `ceil(T / 10)`.
2. Keep every generated clip exactly 10 seconds.
3. Keep every SRT entry inside both its 10-second container and the requested target duration.
4. If `T` is not divisible by 10, trim the final generated clip at `T` in the editor.
5. Make the target cut point visually clean. Keep any unused tail after the cut visually simple and disposable.

Example: 45 seconds uses five 10-second generations. The fifth clip is generated as 40 to 50 seconds, narration ends by 45 seconds, and the editor trims 45 to 50 seconds.

## Story depth by duration

30 seconds: one hook, one book-specific scene or relationship, one insight, one clean ending image.

60 seconds: one hook, setup, two or three development beats, interpretation, callback ending.

90 seconds: allow one additional relationship, location, or consequence. Preserve one central question and use extra time for concrete book detail.

120 seconds: allow a fuller arc with setup, development, cost, interpretation, and callback. Consider a series when multiple independent themes compete.

## Timing density

Keep 1 to 3 SRT entries per 10-second container. Prefer about 3.0 to 3.5 spoken Chinese characters per second across the whole target duration after accounting for pauses. Treat the final TTS voice as the source of truth and shorten text if it overruns.

## Duration changes after approval

Changing duration changes narration, SRT, container count, visual transitions, BGM curve, and prompt count. Treat it as a global revision and regenerate Phase A before proceeding to Phase B.

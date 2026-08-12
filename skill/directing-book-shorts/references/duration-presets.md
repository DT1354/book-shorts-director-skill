# Duration Presets and Custom Timing

Use 60 seconds when duration is unspecified. Duration changes container count, narration density, storyboard depth, transitions, and BGM curve while preserving the SRT-first workflow.

## Standard presets

| Target | 10s containers | Typical Chinese narration | Best for |
|---|---:|---:|---|
| 30s | 3 | about 90–110 characters | one quote, idea, or emotional turn |
| 60s | 6 | about 180–210 characters | default balanced literary short |
| 90s | 9 | about 270–315 characters | richer character or plot arc |
| 120s | 12 | about 360–420 characters | fuller interpretation |

Character counts exclude punctuation and are starting points, not quotas.

## Custom durations

For target duration `T` seconds:

1. Compute containers as `ceil(T / 10)`.
2. Keep every generated clip exactly 10 seconds.
3. Keep every SRT entry inside both its 10-second container and target duration.
4. If `T` is not divisible by 10, trim the final clip at `T` in the editor.
5. Make the target cut point visually clean and keep any unused tail simple and disposable.

Example: 45 seconds uses five 10-second generations. Narration ends by 45 seconds and the editor trims 45–50 seconds.

## Story depth

30s: one hook, one concrete book scene or relationship, one insight, one clean ending image.

60s: hook, setup, development, interpretation, callback ending.

90s: allow an additional relationship, location, or consequence while preserving one central question.

120s: allow a fuller arc with setup, development, cost, interpretation, and callback. Recommend a series if multiple independent themes compete.

Keep 1 to 3 SRT entries per 10-second container. About 3.0 to 3.5 spoken Chinese characters per second across the full target duration is a useful starting point after pauses. Treat the selected TTS voice as source of truth.

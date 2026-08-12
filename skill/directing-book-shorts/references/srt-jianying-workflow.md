# SRT-Driven Jianying / CapCut TTS Workflow

Use one shared timeline for subtitles, TTS, and visuals. Every AI-video generation remains 10 seconds. SRT entries sit inside those containers, imported SRT becomes the subtitle track, batch text-to-speech creates narration from the blocks, and empty gaps create intentional pauses.

## Container rule

Never let an SRT entry cross a 10-second boundary. Never schedule an entry after target duration. If target duration is not divisible by 10, the final generation is still 10 seconds but narration ends by the requested cut point.

## Timing recipe

A practical two-entry container:

- first phrase around `+0.3s` to `+3.4s`
- 0.4–0.7s pause
- second phrase around `+4.0s` to `+8.4s`
- 1.0–1.6s visual/BGM breathing room

A practical three-entry container:

- entry 1 around `+0.3s` to `+2.7s`
- 0.3–0.5s pause
- entry 2 around `+3.1s` to `+5.7s`
- 0.4–0.7s pause
- entry 3 around `+6.3s` to `+8.8s`
- about 1s final breathing room

Vary the values to fit sentence length and emotion. Use punctuation for micro-rhythm and SRT gaps for macro-rhythm.

## Jianying / CapCut steps

1. Import the `.srt` file as subtitles.
2. Confirm all blocks landed at expected timestamps.
3. Select all blocks that share a voice.
4. Choose one TTS voice and consistent speed/style.
5. Generate text-to-speech in batch.
6. Check that speech does not overlap the next scheduled block.
7. If a line overruns, shorten text first.
8. Keep the imported subtitles as final captions or restyle them globally.
9. Place fixed 10-second visual clips underneath the same timeline.
10. Add one continuous BGM track and duck it beneath narration.

Before handoff verify increasing timestamps, no overlap, no 10-second boundary crossing, enough silence for breath and transitions, natural TTS length, and final entry ending no later than target duration.

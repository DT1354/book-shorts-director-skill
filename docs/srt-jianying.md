# SRT-driven Jianying / CapCut TTS

The project uses SRT as both subtitle data and narration rhythm control.

A deliberate pause is created by leaving a real empty gap between subtitle entries. For example:

```srt
1
00:00:00,300 --> 00:00:02,800
世界上有那么多玫瑰，

2
00:00:03,500 --> 00:00:06,200
为什么只有一朵，
```

The 0.7-second gap is preserved when the editor's batch text-to-speech respects imported subtitle timing.

Recommended workflow:

1. Import the SRT.
2. Verify all subtitle blocks landed at the intended timestamps.
3. Select all blocks.
4. Apply one voice, speed, pitch, and style.
5. Generate speech in batch.
6. Check for overruns. Shorten copy before destroying important pauses.
7. Keep the subtitle track for final captions or restyle it globally.

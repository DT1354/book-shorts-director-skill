# Chinese Voiceover Handoff

Default to SRT-driven TTS when the user's Jianying/CapCut version preserves imported subtitle timing during batch text-to-speech.

## Recommended order

1. Finalize timed SRT entries.
2. Import the `.srt` file.
3. Confirm subtitle timing and pause gaps.
4. Select all subtitle blocks and apply one consistent TTS voice, speed, pitch, and style.
5. Generate speech in batch.
6. Listen for any line overrunning the next block.
7. Shorten overlong lines before sacrificing important pauses.
8. Keep SRT as final subtitles and restyle globally if desired.
9. Place fixed 10-second visual clips on the same timeline.
10. Add one continuous BGM track and preserve useful synchronized SFX.
11. Duck BGM and dense SFX beneath speech.

## TTS-ready script rules

Keep sentences short enough for natural breath groups. Use punctuation for small prosodic cues and separate SRT entries for deliberate pauses. Avoid excessive semicolons, parentheses, and nested clauses. Spell out ambiguous numbers when pronunciation matters. Add pronunciation notes outside spoken subtitle text. Keep foreign names consistent.

## Voice direction

Default to a warm, clear adult Mandarin narrator with restrained emotion and documentary-like intimacy. Hook sections may be slightly faster and more precise; plot escalation uses controlled tension; reflection is slower and warmer; endings should be calm and memorable with a clear pause after the final line.

## Local TTS fallback

If Jianying/CapCut batch reading is unavailable or fails to preserve timing, keep the same SRT schedule and generate one audio file per SRT entry with identical voice settings, then place each file at the entry's start timestamp. Prefer Fun-CosyVoice 3 as a general Mandarin baseline and compare GPT-SoVITS when an authorized signature voice is the priority.

Use voice cloning only when the user owns the voice or has permission to use it.

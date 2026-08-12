# Production Workflow

## Phase A

Resolve the target duration first. Default to 60 seconds. Select one central question, then define narration architecture, per-book palette, recurring motifs, character locks, BGM curve, and one transition interface between every 10-second container.

Stop for approval before producing final SRT timestamps or generation prompts.

## Phase B

Build the SRT timeline before writing visual prompts. Each spoken block must remain inside its 10-second container. Use timeline gaps for pauses. Then write one standalone English visual prompt per 10-second generation, synchronized to the approved narration meaning.

The video model produces visuals, ambience, and SFX only. Chinese narration is added in post from the SRT-driven TTS workflow.

## Edit

Place all generated clips at exact 10-second boundaries. Import the SRT, generate one consistent TTS voice, keep the SRT as the subtitle layer, add one continuous BGM track, and duck BGM/SFX under speech.

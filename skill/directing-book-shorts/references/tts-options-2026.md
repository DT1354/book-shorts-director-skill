# Local Chinese TTS Options, August 2026 Snapshot

This is a dated shortlist. Verify current official documentation and license terms before deployment, especially for commercial publishing.

## Fun-CosyVoice 3

Strong general local candidate for Mandarin naturalness, prosody control, and production flexibility. The official project supports Chinese and other languages, multiple Chinese dialects/accents, zero-shot voice cloning, pronunciation control, and instruction control for emotion, speed, and volume. The project repository uses Apache-2.0 licensing. Verify current model-weight terms separately when needed.

Official repository: `https://github.com/FunAudioLLM/CosyVoice`

## GPT-SoVITS

Strong practical choice when easy voice cloning and a mature local WebUI matter. Supports zero-shot and few-shot workflows and Chinese. The repository code uses MIT licensing. Verify rights to reference voices and model weights separately.

Official repository: `https://github.com/RVC-Boss/GPT-SoVITS`

## Fish Speech / Fish Audio

High-quality expressive option worth testing when instruction-following speech is a priority. Licensing has changed over time, so review current terms carefully before commercial use.

Official repository: `https://github.com/fishaudio/fish-speech`

## Practical recommendation

Start with Jianying/CapCut batch TTS when the imported SRT timing is preserved, because it makes the SRT itself the rhythm controller. For local workflows, start with Fun-CosyVoice 3 and compare GPT-SoVITS for a consistent authorized house voice. Keep the Skill engine-agnostic by always outputting timed SRT, pronunciation notes, and voice direction.

# Book Shorts Director Skill

**Turn books into production-ready Chinese short videos with one shared timeline for narration, SRT timing, Jianying/CapCut TTS, literary art direction, and fixed 10-second AI-video generation clips.**

[中文说明](README.zh-CN.md)

![The Little Prince demo preview](demo/little-prince-demo.svg)

## Why this project exists

Most AI book-video workflows treat script, subtitles, TTS, and visuals as separate jobs. That makes pacing drift, pauses disappear, and 10-second generation clips hard to stitch.

Book Shorts Director uses a single production timeline:

`book / theme → story angle → art direction → timed SRT → Jianying/CapCut batch TTS → 10s visual prompts → edit + BGM + SFX`

The SRT is the timing master. Empty gaps between subtitle entries become deliberate narration pauses, and every sentence stays inside its AI-video container.

## Core features

- 60 seconds by default, with 30s, 90s, 120s, and custom durations
- Fixed 10-second AI-video containers for Omni-style generation workflows
- SRT-driven Jianying/CapCut text-to-speech with real pause control
- Original literary editorial illustration instead of generic stick figures
- A unique palette, motif package, and environmental signature for every book
- Source-grounded story planning with quote and spoiler safeguards
- Phase A approval gate before production prompts are generated
- Production-ready English visual prompts, BGM direction, SFX, transitions, and stitching notes
- A deterministic SRT validator/builder included in the Skill

## Duration system

| Target | 10s generation clips | Typical use |
|---|---:|---|
| 30s | 3 | one quote, insight, or emotional turn |
| 60s | 6 | default balanced literary short |
| 90s | 9 | richer character or plot arc |
| 120s | 12 | fuller literary interpretation |
| custom | `ceil(seconds / 10)` | trim the unused tail of the last generated clip |

A 45-second video, for example, uses five 10-second generations. Narration and subtitles end by 45 seconds, and the editor trims 45–50 seconds from the last clip.

## Visual system

The default style is **modern literary editorial illustration animation**:

- clean 2D linework and flat separated color shapes
- age-appropriate simplified figures
- strong negative space and phone-readable composition
- book-specific locations, props, architecture, plants, animals, and symbols
- restrained cinematic camera movement
- no accidental photographic moon, realistic stock texture, or unrelated 3D insert inside an illustrated world

Each book gets its own art package. For example, *The Little Prince* can use deep cobalt, warm star gold, rose red, a tiny planet, rose, fox, wheat, and stars, while another book should develop a different visual identity.

## The Little Prince demo

The included example is based on the 60-second *The Little Prince* short produced with this workflow around one question: **why does one rose become irreplaceable when there are so many roses in the world?**

The production package uses 9:16, six 10-second visual generations, 18 SRT/TTS blocks, real timeline gaps for narration pauses, and a deep-cobalt / warm-gold / rose-red editorial illustration system.

See [`examples/the-little-prince`](examples/the-little-prince/) for the timed SRT and visual prompt plan. The `demo/` folder contains a lightweight project preview and notes for the rendered MP4.

## Install

Use the source under [`skill/directing-book-shorts`](skill/directing-book-shorts/). The repository is structured as a valid ChatGPT Skill project and can be packaged with the standard Skill packaging workflow.

## Example requests

```text
用《小王子》做一期。
```

```text
用《局外人》做一个 30 秒版本，主题是太阳和荒诞。
```

```text
把《百年孤独》做成 90 秒，重点讲黄色蝴蝶这个意象。
```

```text
做 45 秒版本，剪映 SRT 控制停顿，画面用文学编辑插画风格。
```

## Workflow

1. Ground the book and choose one central tension.
2. Offer three narrative directions when only a book title is given.
3. Produce Phase A with storyboard, narration draft, palette, motifs, BGM, and transition chain.
4. Wait for approval.
5. Build exact SRT timing first.
6. Import SRT into Jianying/CapCut and batch-generate TTS with one voice.
7. Generate one 10-second visual prompt per production container.
8. Stitch clips on the same timeline, preserve SFX, and run one continuous BGM track.

More detail: [`docs/workflow.md`](docs/workflow.md), [`docs/srt-jianying.md`](docs/srt-jianying.md), and [`docs/duration-presets.md`](docs/duration-presets.md).

## Repository layout

```text
skill/directing-book-shorts/   ChatGPT Skill source
docs/                          workflow documentation
examples/the-little-prince/    real 60s production example
demo/                          demo preview and rendered-video notes
```

## Notes on source material and voice rights

The Skill prefers paraphrase, avoids invented quotes, and keeps uncertain claims out of narration. If you use voice cloning, use a voice you own or have permission to use.

## License

MIT. Demo and example creative output are included as project examples. Rights in underlying books, translations, trademarks, or third-party generation/TTS platforms remain with their respective owners.

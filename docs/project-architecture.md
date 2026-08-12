# 项目架构

这个仓库同时包含可安装 Skill、制作文档和真实案例。

```text
book-shorts-director-skill/
├── README.md
├── skill/
│   └── directing-book-shorts/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── scripts/build_srt.py
│       └── assets/icon.svg
├── docs/
├── examples/
│   └── the-little-prince/
├── demo/
├── dist/
├── ROADMAP.md
├── CHANGELOG.md
└── LICENSE
```

`SKILL.md` 是控制层，只保存触发条件、默认配置和工作流。更细的时长、视觉、SRT、Phase A、Phase B 和 TTS 规则拆在 `references/` 中，避免主 Skill 过度膨胀。

`scripts/build_srt.py` 负责确定性的 SRT 构建与校验，包括时间递增、字幕重叠、目标时长和 10 秒边界检查。

`examples/` 放真实生产案例，`demo/` 放最终成片，`docs/` 面向人类阅读，`dist/` 面向直接安装。

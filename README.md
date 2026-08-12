<p align="center">
  <img src="skill/directing-book-shorts/assets/icon.svg" width="92" alt="Book Shorts Director">
</p>

<h1 align="center">Book Shorts Director</h1>

<p align="center"><strong>把一本书，变成可以直接制作的中文文学短视频。</strong></p>

<p align="center">叙事导演 · 文学编辑插画 · SRT 精确停顿 · 剪映 TTS · 固定 10 秒 AI 视频分镜</p>

<p align="center">
  <img alt="ChatGPT Skill" src="https://img.shields.io/badge/ChatGPT-Skill-111827">
  <img alt="默认时长" src="https://img.shields.io/badge/默认时长-60s-2563eb">
  <img alt="可变时长" src="https://img.shields.io/badge/时长-30%2F60%2F90%2F120%2F自定义-7c3aed">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-16a34a">
</p>

## 🎬 真实成片 Demo

<p align="center">
  <a href="demo/little-prince-demo-web.mp4">
    <img src="demo/little-prince-demo.svg" width="360" alt="《小王子》60 秒 Demo">
  </a>
</p>

<p align="center"><strong>点击预览图即可播放完整 60 秒《小王子》成片</strong></p>

<p align="center"><a href="demo/little-prince-demo-web.mp4">直接打开视频</a> · <a href="examples/the-little-prince/">查看完整制作案例</a></p>

<!-- 把 GitHub 生成的 user-attachments 视频地址单独放在这里，即可显示原生内嵌播放器 -->

这条 Demo 是完整生产验证案例。它使用 6 个固定 10 秒视频片段、18 个 SRT/TTS 字幕块、真实时间空白控制剪映朗读停顿，并为《小王子》建立了独立的深钴蓝、暖金、玫瑰红文学编辑插画体系。

## 为什么做这个项目

很多 AI 读书视频把写稿、配音、字幕、画面和剪辑分开处理，最后才尝试对齐。常见结果是旁白与镜头错位、TTS 没有真正停顿、固定时长的视频片段难以衔接。

Book Shorts Director 用一条共享时间轴解决这些问题：

```mermaid
flowchart LR
    A[书籍 / 主题] --> B[三个叙事方向]
    B --> C[Phase A 导演预案]
    C --> D[书籍专属视觉体系]
    D --> E[精确 SRT]
    E --> F[剪映批量 TTS]
    E --> G[固定 10 秒视频 Prompt]
    F --> H[统一时间轴合成]
    G --> H
    H --> I[BGM + SFX + 字幕]
    I --> J[最终文学短片]
```

**SRT 是时间主控，10 秒是视频生产容器，每本书自己的视觉体系负责辨识度。**

## ✨ 核心能力

| 能力 | 作用 |
|---|---|
| 叙事导演 | 只有书名时先给 3 个方向，围绕一个中心问题做短片 |
| 可变时长 | 默认 60 秒，同时支持 30、90、120 秒和自定义时长 |
| SRT 节奏 | 用字幕块之间的真实空白控制朗读停顿 |
| 剪映 TTS | 导入 SRT 后全选字幕，用同一音色批量朗读 |
| 文学视觉 | 每本书单独设计色板、人物、场景、道具和贯穿意象 |
| 固定视频容器 | 每段 10 秒，适合 Omni 类固定时长视频生成工作流 |
| 连续转场 | 每段末帧为下一段准备明确的 Match Cut 或视觉接口 |
| 原著约束 | 优先转述，避免伪造名句、剧情、人物动机和无意剧透 |
| 生产交付 | 输出 SRT、视频 Prompt、BGM、SFX、转场和剪映拼接说明 |

## ⏱️ 时长模式

| 成片时长 | 10 秒容器 | 适合内容 |
|---|---:|---|
| 30 秒 | 3 | 一个金句、观点或情绪转折 |
| 60 秒 | 6 | 默认，节奏最均衡 |
| 90 秒 | 9 | 更完整的人物、关系或剧情弧线 |
| 120 秒 | 12 | 更充分的文学解读 |
| 自定义 | `ceil(秒数 / 10)` | 最后一段在目标切点裁尾 |

例如 45 秒版本会规划 5 个固定 10 秒片段。旁白和 SRT 在 45 秒前结束，第 5 段的 45 到 50 秒保持简单，在剪映中裁掉。

查看 [完整时长规则](docs/duration-presets.md)。

## 🎨 默认视觉体系

默认风格是**现代文学编辑插画动态短片**。它更接近高级书籍插画、文学杂志插图和动态书封。

统一账号气质来自干净二维线稿、分离平涂色块、高对比、大留白、手机竖屏构图和克制电影镜头。每本书仍然重新建立自己的背景气质、最多三种强调色、三到五个专属意象，以及一个独特环境或构图特征。

《小王子》可以使用深钴蓝、暖星金、玫瑰红、小星球、玫瑰、狐狸、麦田与星星。《局外人》会重新建立烈日、沙色、黑与炽热橙的视觉世界。

查看 [文学视觉系统](docs/visual-system.md)。

## 🎙️ SRT 为什么能控制停顿

```text
00:00:00,300 --> 00:00:02,800
世界上有那么多玫瑰，

00:00:03,500 --> 00:00:06,200
为什么只有一朵，

00:00:06,800 --> 00:00:08,900
让小王子一直放不下？
```

两个字幕块之间的空白就是真实时间空白。导入剪映后批量文本朗读，字幕、TTS 和视觉从一开始就在同一套时间码上。

查看 [剪映 SRT 与 TTS 工作流](docs/srt-jianying.md)。

## 🚀 快速开始

最简单只要一句：

```text
用《小王子》做一期。
```

也可以直接指定时长和主题：

```text
用《局外人》做 30 秒，重点讲太阳和荒诞。
```

```text
把《百年孤独》做成 90 秒，围绕黄色蝴蝶这个意象。
```

```text
做 45 秒版本，剪映 SRT 控制停顿，视觉用文学编辑插画。
```

Skill 会先给叙事方向，再输出 Phase A 导演预案。确认后才进入 Phase B，生成精确 SRT 和每个 10 秒容器的生产级视频 Prompt。

## 📦 Skill 本体

完整源码位于 [`skill/directing-book-shorts`](skill/directing-book-shorts/)。

当前 Skill 已包含中文触发 Description、中文 Agent 元数据、动态时长规则、SRT 校验脚本、文学视觉系统、Phase A 与 Phase B 生产协议，以及《小王子》Demo 质量标杆。

安装包建议从最新源码按标准 Skill 打包流程生成，避免二进制包与源码版本不同步。

## 🧪 《小王子》完整案例

案例主题：**世界上有那么多玫瑰，为什么只有一朵会变得不可替代？**

包含 60 秒成片、6 个固定 10 秒片段、18 个 SRT/TTS 字幕块、专属视觉体系、逐段转场与 SFX，以及可直接导入剪映的字幕文件。

查看 [`examples/the-little-prince`](examples/the-little-prince/)。

## 🗂️ 项目结构

```text
book-shorts-director-skill/
├── README.md
├── skill/directing-book-shorts/   # ChatGPT Skill 本体
├── docs/                          # 中文工作流与设计文档
├── examples/the-little-prince/    # 完整生产案例
├── demo/                          # 成片与首页预览
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

## 项目原则

**一次只讲一个值得讲的问题。** 时长增加时，增加故事细节和情绪层次，不机械增加主题数量。

**每本书都要有自己的视觉世界。** 账号可以有统一气质，但不能让所有作品长成同一套模板。

**旁白节奏必须能被编辑器执行。** 明显停顿放进时间轴，不只依赖标点。

**AI 负责执行，导演规则负责一致性。** 人物、色板、道具、镜头、转场和声音都提前锁定。

## 📖 文档

[完整工作流](docs/workflow.md) · [时长模式](docs/duration-presets.md) · [文学视觉系统](docs/visual-system.md) · [剪映 SRT](docs/srt-jianying.md) · [项目架构](docs/project-architecture.md) · [Roadmap](ROADMAP.md)

## 🤝 贡献

欢迎增加真实案例、视觉体系、字幕节奏模板和视频模型适配。见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

MIT。Demo 和案例用于展示工作流。原著、译本、商标，以及第三方视频生成和 TTS 平台相关权利归各自权利人所有。

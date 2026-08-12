# 中文 TTS 方案，2026 年 8 月快照

这是阶段性参考，不是永久排名。用户准备正式部署或商业发布时，应再次核对最新官方文档、模型权重许可和声音授权。

## 剪映 / CapCut

如果当前版本能够导入 SRT，并在批量文本朗读时保留字幕时间位置，优先使用。优势是最省后期步骤，SRT 同时控制字幕和停顿。

## Fun-CosyVoice 3

适合中文自然度、情绪和语速控制、本地部署与自动化。官方项目：`https://github.com/FunAudioLLM/CosyVoice`

部署前再次确认当前模型权重和许可。

## GPT-SoVITS

适合建立经过授权的固定账号声音。官方项目：`https://github.com/RVC-Boss/GPT-SoVITS`

代码许可与模型权重、参考声音权利需要分别确认。

## Fish Speech / Fish Audio

表达力强，适合愿意仔细检查许可的高级工作流。商业使用前必须核对当时最新的 Fish Audio 许可条款，不要默认等同于宽松开源许可。

官方项目：`https://github.com/fishaudio/fish-speech`

## 当前推荐顺序

先用剪映/CapCut 的 SRT 批量朗读验证内容与账号风格；需要更强控制或自动化时尝试 Fun-CosyVoice 3；需要长期固定授权签名声音时比较 GPT-SoVITS。

无论换哪个 TTS，引擎都不能改变 SRT 作为字幕与停顿时间主控的设计。

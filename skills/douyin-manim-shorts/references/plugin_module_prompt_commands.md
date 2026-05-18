# Plug-in Module Prompt Commands

Use these command templates when asking the skill to produce a deep learning plug-in module short. This is an extension of the existing `douyin-manim-shorts` workflow, not a separate skill.

## Standard Production Command

```text
使用当前短视频制作 skill，为一个深度学习即插即用模块生成 20-30 秒竖屏 Manim 短视频。

输入字段：
- 模块名称：
- 模块缩写：
- 论文/方法来源：
- 解决痛点：
- 适用任务：
- 核心机制：
- 关键公式：
- 最小接入代码：
- 资料包内容：
- CTA 文案：
- 风格备注：
- bgm_style：
- bgm_path：

请先完成材料整理、brief、脚本、分镜；确认后再写 scene.py 和渲染。
```

## Full Material Command

```text
请基于当前项目中的 skills/douyin-manim-shorts，使用下面目录中的材料制作一条“[模块名] 即插即用模块”抖音短视频：

材料目录：[路径]

要求：
1. 先扫描目录，识别论文 PDF、模块代码、架构图或可用图片。
2. 不要一上来写 Manim 场景代码。
3. 按 Deep Learning Plug-in Module Video Mode 执行。
4. 先生成 plugin_module_brief.yaml、script.md、voiceover.txt、subtitles.srt、storyboard.md、caption.md。
5. 信息不足时标注不确定，不要编造论文结论。
```

## Manim Implementation Command

```text
请基于已生成的 brief、脚本和分镜，制作第一版 Manim 样片。

要求：
- 使用 ManimCE。
- 竖屏 9:16。
- 总时长 20-30 秒。
- 公式用 MathTex。
- 标签用 make_label_box() 自动适配。
- 代码只展示 3-5 行，并高亮接入行。
- 不要把完整论文架构图塞进竖屏。
- 渲染低清预览并生成 QA contact sheet。
```

## V2/V4 Refinement Command

```text
请把当前样片从课程 PPT 风格改成抖音快节奏机制动画。

要求：
- 前 1 秒有强钩子。
- 每 2-3 秒有明显画面变化。
- 用公式、频谱、曲线、张量流、Gate、残差或注意力热图表达机制。
- 保留 3-5 行代码接入卖点。
- 运行 QA，检查红色调试框、中心十字线、字幕安全区、公式越界、箭头穿字、尾部冻结和音频流。
```

## BGM Finalization Command

```text
请基于当前 episode 的 preview_no_bgm.mp4 自动添加背景音乐。

要求：
- 从 index/bgm_registry.csv 按 brief.md 的 bgm_style 选择 BGM。
- 如果 brief.md 指定 bgm_path，优先使用指定音乐。
- 把选中的音乐复制为 audio/bgm.wav。
- 使用 scripts/mix_audio.py 输出 audio/mixed_audio.wav 和 renders/final_with_bgm.mp4。
- BGM 默认音量 0.15，人声默认 1.0。
- 生成或更新 renders/contact_sheet.jpg 和 qa_report.md。
- QA 必须检查 has_video、has_audio、音视频时长、尾部冻结、BGM 是否盖过中文旁白。
```

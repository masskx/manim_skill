# Plug-in Module Prompt Commands

Use these command templates when asking the skill to produce a deep learning plug-in module short. This is an extension of the existing `douyin-manim-shorts` workflow, not a separate skill.

## Standard Production Command

```text
使用当前短视频制作 skill，为一个深度学习即插即用模块生成 20-30 秒竖屏 Manim 短视频。

生成新模块视频时，必须先读取 module_brief，并根据 module_type 选择差异化动画模板。禁止直接复用 AFDA 或上一条视频的公式、口播、机制动画和代码。

输入字段：
- 模块名称：
- 模块缩写：
- 模块类型：
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

## Page Lifecycle And Full-Resolution QA Command

```text
When generating or revising Manim scene.py, each beat must own its temporary objects.

Do not let old symbols, branch labels, arrows, matrices, braces, or helper chips remain visible after their explanatory beat.
Before the code page or CTA page, clear all mechanism-only objects.
If a concept must persist, restage it in the new layout zone instead of leaving it at old coordinates.

After rendering a contact sheet, any thumbnail that looks crowded, garbled, or unreadable must be checked with a full-resolution extracted frame at that timestamp.
Record the timestamp and result in qa_report.md.

The final video stream must cover the full voiceover duration.
If voiceover audio is longer than the video stream, extend visible motion or final CTA hold; never let audio continue over black or missing video.
```

## Layout-System Manim Command

```text
生成 Manim scene.py 时，必须使用布局系统。

先选择 scene 类型和 layout 模板，再放置元素。
禁止随意 move_to/shift 硬编码堆放。
所有 Text、MathTex、Code、VGroup 必须经过 safe_scale_to_width 或 fit_to_box。
所有标签框必须使用 SurroundingRectangle 自动包裹文字。
每页渲染前必须检查重叠、越界、贴边、箭头穿字、字幕区侵入。
最后 5 秒必须单独检查 CTA 和字幕区域。

必须执行 layout_draft -> contact_sheet_check -> layout_fix -> animation_pass -> final_render。
如果 contact sheet 中发现元素挤压、重叠、越界或主视觉不清楚，不允许输出 final_with_bgm.mp4，先做 layout_fix。
```

## Layered Layout And Arrow Routing Command

```text
生成 Manim 场景时必须使用 Layered Layout。

公式放 formula_layer，图形放 diagram_layer，箭头只在 arrow lanes 中布线，字幕放 subtitle_layer，CTA 放 cta_layer。
禁止公式和图形共享同一 y 中心。
禁止把 MathTex 放在 pipeline 箭头路径中。
禁止箭头穿过公式、文字、代码、CTA 或字幕。
所有箭头必须从对象边缘连接，不能从中心连到中心。
如果直线箭头会穿过公式或文字，必须使用 make_elbow_arrow。
如果公式、图形、箭头无法清楚共存，必须拆成公式主导帧和图形主导帧。
每帧遵守复杂度预算：1 个标题、1 个核心公式、1 个主图形组、最多 3 个模块框、最多 3 条主箭头、1 条字幕，非 CTA 页不显示 CTA。
生成 contact sheet 后必须专项检查 formula vs diagram、formula vs arrows、arrows vs labels、diagram vs subtitle、CTA vs subtitle。
任何碰撞都必须记录到 qa_report.md；未生成 layout_fix 前不得输出 final_with_bgm.mp4。
```

## Content-first New Episode Command

```text
生成新模块视频时，必须先读取当前论文、代码、架构图、用户说明和 episode 主题要求。

先生成 mechanism_brief.md，回答当前模块全称/缩写、核心问题、输入输出张量、关键分支、每个分支提取的信息、真实机制、核心公式、最适合视频展示的公式、视觉隐喻、与上一期差异、上一期哪些结构不能复用。

再生成 episode_strategy.md，写清楚模块类型判断、判断依据、本期不能复用上一期哪些结构、本期独特叙事方式、本期核心动画主线、本期核心公式、本期视觉隐喻、与最近 3 期视频的差异点。

模板提供的是工作流，不是内容结构。每个新模块必须重新抽取机制，重新设计动画。

禁止直接复用 AFDA、WMVF_002 或上一期视频的公式、口播、机制动画、动画顺序、分镜节奏、视觉隐喻和代码类名。

scene.py 生成前必须做真实性校验：视频中出现的 Gate、Residual、Attention、Frequency、Wavelet、Multi-scale、Expert routing、Prototype/Calibration 等机制，必须在当前代码或论文中找到证据。没有证据的机制不允许出现。

公式、动画、口播、字幕必须绑定同一个当前模块机制。所有数学公式必须用 MathTex；中文解释必须用 Text；禁止公式用 Text；禁止中文和公式混写。
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
- 先读取 module_brief，根据 module_type 选择差异化动画模板。
- 禁止直接复用 AFDA 或上一条视频的公式、口播、机制动画和代码。
- 所有数学公式必须用 MathTex；禁止用 Text 渲染公式，禁止 MathTex 失败后降级为 Text。
- 中文说明必须使用 Text，并与 MathTex 分离。
- 如果用户要求配音，必须先生成 voiceover.wav，并在 scene.py 中 add_sound 后再渲染。
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
- 先检查 storyboard.md、voiceover.txt、scene.py 是否残留上一条视频的模块名、公式、代码类名和 CTA keyword。
- 如果要求 3b1b 风格，禁止做 PPT 流程图；用公式变换、brace、箭头、曲线和 ValueTracker 推演机制。
- 检查公式是否全是 MathTex，检查 voiceover.wav 是否存在并被 add_sound 挂载。
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


## Hybrid Manim + Remotion Production Command

```text
使用当前短视频 skill 的 Hybrid Manim + Remotion 模式，为一个新的深度学习即插即用模块生成 20-30 秒竖屏短视频。

Manim 只生成公式和机制动画片段，Remotion 负责整体布局、标题、字幕、代码、CTA、BGM 和最终合成。
所有模块内容通过 data.json 驱动，禁止在 Remotion 组件中硬编码模块内容。

生成步骤：
1. 读取 module_brief 并完成 authenticity gate。
2. 生成 storyboard.md（标注哪些 beat 用 Manim clip，哪些用 Remotion overlay）。
3. 生成 voiceover.txt 和 subtitles.srt。
4. 根据 module_type 生成 1-3 个 Manim 场景（只做机制动画）。
5. 渲染 Manim clips 到 manim/renders/。
6. 生成 remotion/data.json（包含所有内容字段）。
7. 使用 remotion/composition.tsx 合成整条视频。
8. 自动选择 BGM，合成 final_with_bgm.mp4。
9. 生成 contact_sheet 并运行 Hybrid QA。

输入字段：
- 模块名称：
- 模块缩写：
- 模块类型：
- 来源论文/代码：
- 解决痛点：
- 核心机制：
- 关键公式：
- 最小接入代码：
- CTA 文案：
- bgm_style：
```

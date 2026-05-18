---
name: douyin-manim-shorts
description: |
  Trigger when the user wants to create Douyin/TikTok-style short-form educational videos with Manim, especially Chinese knowledge videos, math explainers, AI/ML visualizations, paper/model explainers, exam/course clips, or vertical 9:16 animated shorts.

  Turns a topic into a short-video production package: hook, title options, cover text, audience angle, timed beat sheet, spoken script, on-screen subtitles, ManimCE implementation plan, vertical scene code, render command, and mobile-first quality checklist. Prefer this skill before using manimce-best-practices for implementation details.

  Default target: Douyin Chinese audience, vertical 1080x1920, one clear insight per video, content-driven duration, high retention pacing, large subtitles, low formula density, and ManimCE unless the user explicitly asks for ManimGL.

  Also supports deep learning plug-in module shorts: 20-30 second vertical Manim videos that explain one reusable module's pain point, mechanism, insertion point, minimal code usage, and resource-pack CTA.
---

# Douyin Manim Shorts

Use this skill to produce short-form educational videos that feel native to Douyin: fast entry, one idea, clear visual payoff, and mobile-readable Manim animation. It can produce general educational shorts and, as an internal mode of the same skill, deep learning plug-in module shorts for papers, PyTorch modules, and architecture figures.

## Default Output

For each video request, produce these artifacts unless the user asks for less:

1. `douyin-script.md`: title options, cover text, hook, beat sheet, spoken script, subtitles, visual plan, engagement prompt.
2. `voiceover.txt`: clean narration lines for recording or text-to-speech.
3. `subtitles.srt`: subtitle timing draft when the user wants external captions.
4. `scene.py`: ManimCE vertical scene code using `from manim import *`.
5. Render command: `manim -pql scene.py SceneName` for preview, with higher-quality command if needed.
6. Post-render QA assets: sampled frames or contact sheet for layout inspection, plus freeze-tail check.
7. QA checklist: retention, mobile readability, subtitle length, safe areas, overlap, formula rendering, audio stream, and render risks.
8. Release audio package when publishing: `preview_no_bgm.mp4`, `audio/bgm.wav`, `audio/mixed_audio.wav`, `final_with_bgm.mp4`, and `qa_report.md`.

Use [templates/douyin-script-template.md](templates/douyin-script-template.md) for scripts and [templates/vertical_scene.py](templates/vertical_scene.py) as the ManimCE starter.

For visual styling and layout decisions, follow [references/douyin-layout-style.md](references/douyin-layout-style.md). Load it when creating or revising actual Manim scenes.

For episode management and background music workflows, follow [references/bgm_project_workflow.md](references/bgm_project_workflow.md). Load it when the user asks for BGM, background music, music library, final mix, batch production, release candidate, or project management for multiple videos.

For Alibaba-family text-to-speech workflows, follow [references/alibaba-tts.md](references/alibaba-tts.md). Load it when the user mentions Alibaba Cloud, Aliyun, DashScope, Bailian, CosyVoice, Qwen audio, 通义, 阿里云, 百炼, or 阿里语音.

## Deep Learning Plug-in Module Video Mode

Use this mode when the user provides any combination of:

- A paper PDF.
- Plug-in module code, especially PyTorch module code.
- A white-background model architecture figure.

The goal is to turn these materials into a 20-30 second Douyin-ready short video explaining one plug-in deep learning module: what pain point it solves, how the mechanism works, where it plugs into a model, and how to call it with minimal code. Keep the original `douyin-manim-shorts` general-purpose workflow available for other educational shorts; this mode is a specialized path inside the same skill.

This mode should explain:

- The pain point in ordinary deep learning user language.
- The mechanism with Manim formula animation, tensor flow, frequency spectrum, attention heatmaps, gate bars, residual paths, or branch fusion when relevant.
- The plug position in a backbone or task model.
- The minimum 3-5 line code insertion.
- A resource-pack CTA such as PDF notes, PyTorch code, and architecture figure breakdown.

Default outputs for this mode:

1. `plugin_module_brief.yaml`: structured material summary and video input spec.
2. `plugin_module_script.md`: title, cover text, six-scene script, voiceover draft, subtitle draft.
3. `plugin_module_storyboard.md`: timeline with visual elements, animation notes, screen text, narration, and material source.
4. `plugin_module_caption.md`: Douyin publishing copy, title candidates, comment prompt, hashtags, and resource-pack wording.
5. Optional `scene.py` only when the user asks for implementation. Do not start with complex Manim scene code in this mode; lock the brief, script, and storyboard first.

Load these references for this mode:

- [references/material_input_rules.md](references/material_input_rules.md) for extracting useful facts from the PDF, code, and architecture figure.
- [references/plugin_module_video_structure.md](references/plugin_module_video_structure.md) for the fixed 15-25 second structure.
- [references/paper_to_video_rules.md](references/paper_to_video_rules.md) for translating paper claims into short-video language.
- [references/code_to_video_rules.md](references/code_to_video_rules.md) for turning module code into a tiny, readable usage snippet.
- [references/architecture_figure_rules.md](references/architecture_figure_rules.md) for using white-background architecture figures without crowding the vertical frame.
- [references/plugin_module_manim_animation_rules.md](references/plugin_module_manim_animation_rules.md) for MathTex, frequency, gate, residual, attention, and formula-to-code animation patterns.
- [references/plugin_module_qa_checklist.md](references/plugin_module_qa_checklist.md) for hard post-render checks learned from AFDA.
- [references/afda_case_study.md](references/afda_case_study.md) as the first internal case study and failure-mode log.
- [references/plugin_module_prompt_commands.md](references/plugin_module_prompt_commands.md) for reusable user command templates.

Use these templates:

- [templates/plugin_module_brief.yaml](templates/plugin_module_brief.yaml)
- [templates/plugin_module_script.md](templates/plugin_module_script.md)
- [templates/plugin_module_storyboard.md](templates/plugin_module_storyboard.md)
- [templates/plugin_module_caption.md](templates/plugin_module_caption.md)

Workflow for this mode:

1. Extract only evidence-backed facts from the paper, code, and figure.
2. Fill `plugin_module_brief.yaml` first. Mark missing fields as `unknown` or `needs_user_input`; do not invent paper conclusions.
3. Reduce the module to one core insight: "pain point -> module mechanism -> plug position -> minimal code usage".
4. Use the fixed five-beat structure unless the user asks otherwise: 0-3s pain-point hook, 3-7s problem visualization, 7-15s mechanism animation, 15-21s code insertion, 21-26s resource-pack CTA.
5. Prefer a simplified Manim block diagram over a full paper figure. Use the original white-background figure only as a cropped reference or local zoom when it helps.
6. Keep code on screen to 3-5 lines with Chinese comments. Prefer a minimal call like `x = Module(...)(x)` when accurate.
7. Keep the video focused on module adoption, not a full paper review, benchmark discussion, or source-code lecture.
8. Manim must do more than PPT-style static boxes: use formulas, transforms, curves, spectra, tensor flow, heatmaps, gate bars, residual links, insertion animations, or formula-to-code transforms where they clarify the module.

## Content Strategy

Optimize for these formats:

- **Spark**: one surprising question, one animation, one memorable sentence. Often 15-35 seconds.
- **Explainer**: hook, concrete example, animated mechanism, takeaway. Often 30-70 seconds.
- **Mini lesson**: problem, intuition, visual proof, real-world tie-in, comment prompt. Often 60-120 seconds.
- **Series episode**: one concept per episode with consistent visual language.

Good lanes for this skill:

- AI/ML concepts: embeddings, attention, softmax, gradient descent, overfitting, transformers.
- Math intuition: vectors, eigenvalues, Fourier transform, probability, calculus, geometry.
- Paper/model explainers: one figure, one mechanism, one limitation.
- Exam/course clips: one high-frequency concept or common misconception.
- Trend-linked science: use a current topic only as the doorway into one durable insight.

## Production Workflow

### 1. Pick the single insight

Before writing scenes, reduce the topic to one sentence:

```text
After watching, the viewer should remember: [one concrete insight].
```

If the topic contains multiple insights, make a series plan instead of one crowded video.

### 2. Design the first 3 seconds

The opening must contain at least one of:

- A contradiction: "为什么越训练，模型反而越差?"
- A practical payoff: "30 秒看懂注意力机制到底在看什么"
- A visual mystery: "这三个点，为什么能代表一句话?"
- A misconception attack: "神经网络不是在背答案"

Avoid slow intros, channel greetings, historical setup, and definitions before curiosity.

### 3. Choose content-driven duration

Do not force a video to hit exactly 30 seconds. Estimate duration from the actual spoken script and visual beats.

Rules:

- A 23.7-second video is acceptable if the idea is complete.
- A 37-second video is acceptable if the extra time adds clarity.
- Never add a 5-10 second static ending just to reach a round number.
- Final hold should usually be 0.6-1.5 seconds, only long enough for the takeaway to register.
- If a platform target is requested, treat it as a soft range, not a hard exact duration.
- If narration exists, sync animation length to narration length plus a short ending hold.

Use this rough speech estimate:

```text
Estimated seconds = Chinese characters in voiceover / 4.0 to 4.8
```

If the estimate and visual plan disagree, adjust the script or animations instead of padding with `self.wait(...)`.

### 4. Build the beat sheet

Use this pacing as a flexible pattern:

```text
0-3s: Hook + large title + visual tension
3-10s: Concrete example, no abstraction yet
10-30s: Main Manim transformation or mechanism
30-45s: Takeaway sentence and replay of key visual
45-60s: Optional implication, contrast, or comment prompt
```

For 15-30s videos, compress to hook -> visual mechanism -> takeaway.

### 5. Write for speech first

Use short Chinese spoken lines. Each sentence should be easy to say in one breath.

Rules:

- On-screen subtitle line: usually 6-16 Chinese characters.
- Spoken sentence: usually under 24 Chinese characters.
- One technical term at a time.
- Define terms through examples before naming them.
- Prefer "你看..." / "想象..." / "其实..." when guiding attention.

### 6. Plan mobile-first Manim visuals

Default visual rules:

- Canvas: 1080x1920, vertical 9:16.
- Keep the safe area clear: avoid key text at very top, bottom, and right edge.
- Use large text: title 52-76, subtitles 34-46, labels 28-38.
- Use no more than 3 major visual objects at once.
- Use one accent color for the key idea and one warning color for contrast.
- Formula density: 0-1 formula for 15-45s, at most 2 for 60-90s.
- Animate every 2-5 seconds; avoid long static frames.
- Treat layout as a fixed vertical stage: reserve zones before placing objects.
- Never rely on `next_to` chains alone for dense layouts; use explicit zones, `arrange`, `scale_to_fit_width`, and `scale_to_fit_height`.
- After creating each major `VGroup`, check that it fits its intended zone before animating it.
- Keep subtitles in a dedicated bottom caption zone and do not place formulas or diagrams there.
- If two objects may overlap during animation, animate them through separate zones or fade/transform one before introducing the next.

Typography hierarchy:

- Use at most 3 text sizes in one scene family: title, subtitle/body, micro-label.
- Title: 56-68 px equivalent; only one title-sized element on screen.
- Subtitle/body: 34-42 px equivalent; this is the main reading size.
- Micro-label: 24-30 px equivalent; use sparingly for tags such as Q/K/V.
- Avoid extreme contrast such as 72 px title with 18 px labels unless labels are purely decorative.
- Keep font weight consistent: bold for title and key phrase, regular/medium for labels.
- Prefer one clean Chinese sans font such as Microsoft YaHei, Source Han Sans, Noto Sans CJK, or system fallback.

Douyin-style layout:

- The frame should read like a polished mobile explainer, not a slide deck.
- One dominant focus per screen: title, diagram, or formula, not all three at full strength.
- Use strong contrast for the hook and takeaway, but keep the inner explanation calmer.
- Use title bars, caption pills, and compact tags instead of scattered free-floating text.
- Keep repeated visual language: same subtitle box, same tag style, same accent color meaning.
- Do not fill every empty area; clean negative space is part of readability.

Recommended vertical zones:

```text
Top title zone:       y = 5.7 to 7.1
Main visual zone:     y = -2.6 to 4.8
Formula/detail zone:  y = -4.7 to -3.1
Subtitle zone:        y = -6.7 to -5.7
```

When a scene needs many objects, use a staged reveal: show title + diagram, then diagram + formula, then takeaway. Do not keep all prior text visible.

### 7. Render formulas correctly

Use `Text` only for natural-language labels. Use `MathTex` for mathematical notation.

Bad:

```python
formula = Text("Attention = softmax(QK^T) V")
```

Good:

```python
formula = MathTex(
    r"\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^T)V",
    font_size=34,
    color=WHITE,
)
```

Formula rules:

- Never put Chinese text inside `MathTex`; place Chinese explanation in a separate `Text`.
- Use raw strings: `r"..."`.
- Use `\mathrm{softmax}` for words inside formulas.
- Prefer compact formulas for mobile screens.
- If LaTeX fails, inspect `media/Tex/*.log` or the generated `.tex` file before rewriting randomly.

### 8. Add audio deliberately

Manim renders silent video unless audio is explicitly added. A spoken script in Markdown is not audio.

Default audio workflow:

1. Generate `voiceover.txt` with one short line per spoken sentence.
2. Generate `voiceover_lines.csv` when external TTS timing or per-line synthesis is useful.
3. Ask the user to record or generate `audio/voiceover.wav` or `audio/voiceover.mp3`.
4. In `scene.py`, call `self.add_sound("audio/voiceover.wav")` at the start of `construct` if the file exists.
5. Match total animation duration to the voiceover length.
6. Verify the final MP4 has an audio stream with `ffprobe`.

Alibaba TTS workflow:

1. Prefer Alibaba Bailian/DashScope CosyVoice for new Alibaba-family voiceovers unless the user names another Alibaba service.
2. Output TTS-ready text as short lines, not one long paragraph.
3. Keep Chinese punctuation natural: `，` for small pauses and `。` for sentence stops.
4. Provide recommended fields: model, voice, format, sample rate, speed/rate if supported.
5. Standardize the final audio path to `audio/voiceover.wav` even if the TTS platform first returns MP3.
6. If per-line TTS is used, concatenate line audio in order and verify final duration before rendering.

If no TTS platform is specified, still prepare the project so the user can place Alibaba-exported audio at `audio/voiceover.wav`.

If no audio file exists, clearly state that the rendered Manim video will be silent and provide the exact path where the user should place the voiceover.

### 8.1 Add BGM for release candidates

Do not treat the Manim preview as the final publishing mix. Keep both a clean no-BGM preview and a final mixed version:

```text
episodes/{slug}_{index}/renders/preview_no_bgm.mp4
episodes/{slug}_{index}/audio/bgm.wav
episodes/{slug}_{index}/audio/mixed_audio.wav
episodes/{slug}_{index}/renders/final_with_bgm.mp4
episodes/{slug}_{index}/qa_report.md
```

Use `scripts/mix_audio.py` for automatic BGM mixing. Default mix values:

- `bgm_volume: 0.15`
- `voiceover_volume: 1.0`
- `sfx_volume: 0.25`

BGM selection rules:

- If `bgm_path` exists in the episode brief, use that track.
- If `bgm_auto_select: true`, choose from `index/bgm_registry.csv` by `bgm_style`.
- If no matching BGM exists, write an AI music prompt into `qa_report.md`; do not use a mismatched track.
- Imported music belongs under `shared_assets/bgm_library/{style}/` and must be registered in `index/bgm_registry.csv`.

Every final BGM mix must verify `has_audio: True`, similar audio/video duration, no abrupt audio cut, and no BGM masking the Chinese voiceover.

### 9. Implement with ManimCE

Prefer ManimCE:

```python
from manim import *
```

Use `manimce-best-practices` only for detailed implementation references such as `MathTex`, `Axes`, updaters, camera movement, or graphing.

Default config:

```python
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
```

Keep reusable helpers inside the scene file when they improve consistency: `title_text`, `subtitle`, `safe_box`, or `caption_box`.

### 10. Run post-render visual QA

After rendering, inspect the actual MP4 before calling the task done.

Required checks:

1. Extract sampled frames or a contact sheet from the rendered MP4.
2. Inspect frames around every beat transition and the final 5-8 seconds.
3. Confirm no title, subtitle, formula, labels, arrows, or diagrams overlap incoherently.
4. Confirm important objects stay inside the 9:16 safe area.
5. Confirm the ending is not a frozen padding segment.
6. If audio was requested, confirm the MP4 contains an audio stream.

Useful commands:

```bash
ffmpeg -y -i output.mp4 -vf "fps=1/2,scale=270:-1,tile=4x6" qa_contact_sheet.jpg
ffmpeg -hide_banner -i output.mp4 -vf "freezedetect=n=0.003:d=2" -f null -
ffprobe -v error -show_streams output.mp4
```

If `freezedetect` reports a freeze near the end longer than 2 seconds, remove or shorten the final `self.wait(...)` unless the user explicitly asked for an outro hold.

## Output Format

When asked to create a video, respond with:

```markdown
## Concept Lock
After watching, the viewer should remember: ...

## Script Package
- Titles:
- Cover:
- Hook:
- Comment prompt:

## Beat Sheet
| Time | Visual | Voiceover | Subtitle |
|---|---|---|---|

## Manim Plan
- Scene class:
- Main mobjects:
- Key animations:
- Render command:

## QA Notes
- ...
```

If editing files in a repo, create or update actual files rather than only describing them.

## Quality Checklist

Before finishing, check:

- Hook appears in the first 3 seconds.
- The video teaches exactly one insight.
- No subtitle line is visually too long for mobile.
- Rendered frames show no incoherent overlap between UI, text, formulas, arrows, and diagrams.
- Text hierarchy uses no more than 3 sizes, with no jarring title/label contrast.
- The screen has one dominant focus at a time.
- Repeated elements share the same style, size, stroke, and color meaning.
- Important objects stay inside the vertical safe area.
- The viewer can understand the visual without reading dense formulas.
- The final sentence is memorable or invites comments.
- The duration follows the content; no static padding was added to hit an exact round number.
- The final hold is short and intentional.
- The Manim code is renderable with ManimCE.
- Mathematical formulas use `MathTex`, not `Text`.
- Audio is either attached with `self.add_sound(...)` or explicitly marked as not yet produced.
- Alibaba TTS users receive `voiceover.txt` and, when useful, `voiceover_lines.csv` with clean per-line narration.
- `ffprobe` shows both video and audio streams when audio was requested.
- Release candidates include both `preview_no_bgm.mp4` and `final_with_bgm.mp4`.
- BGM volume is checked against voiceover clarity.
- `freezedetect` or manual frame inspection finds no long frozen tail.
- For plug-in module videos, no red debug boxes, no center cross-axis background, no text overflowing label boxes, no arrows passing through text, and no formulas or subtitles outside the vertical safe area.

## Common Anti-Patterns

- Opening with "大家好, 今天我们来讲..."
- Explaining definitions before showing the problem.
- Copying long-video 3Blue1Brown pacing into a 30-second video.
- Padding a complete 23-second video with 6-7 seconds of unmoving ending.
- Putting tiny formulas in the center and expecting mobile viewers to read them.
- Letting title, subtitle, formula, arrows, and diagrams share the same screen zone.
- Mixing many unrelated text sizes, weights, colors, and label styles in one scene.
- Making the video look like a classroom slide instead of a mobile-first short.
- Rendering formulas with `Text("QK^T")` instead of `MathTex`.
- Assuming Manim will generate narration from the spoken script automatically.
- Showing too many arrows, labels, colors, or equations at once.
- Ending without a conclusion or interaction hook.

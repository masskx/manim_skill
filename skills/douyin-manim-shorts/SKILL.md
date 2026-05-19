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
- [references/plugin_module_layout_system.md](references/plugin_module_layout_system.md) for mandatory "layout before animation" rules, 9:16 zones, layout templates, helper functions, overlap checks, and layout-pass QA.
- [references/plugin_module_qa_checklist.md](references/plugin_module_qa_checklist.md) for hard post-render checks learned from AFDA.
- [references/afda_case_study.md](references/afda_case_study.md) as the first internal case study and failure-mode log.
- [references/common_failures.md](references/common_failures.md) as the accumulated failure log for formula, voiceover, style, and QA regressions.
- [references/plugin_module_prompt_commands.md](references/plugin_module_prompt_commands.md) for reusable user command templates.

Use these templates:

- [templates/plugin_module_brief.yaml](templates/plugin_module_brief.yaml)
- [templates/plugin_module_script.md](templates/plugin_module_script.md)
- [templates/plugin_module_storyboard.md](templates/plugin_module_storyboard.md)
- [templates/plugin_module_caption.md](templates/plugin_module_caption.md)

Workflow for this mode:

1. Extract only evidence-backed facts from the paper, code, and figure.
2. Fill `plugin_module_brief.yaml` first. Mark missing fields as `unknown` or `needs_user_input`; do not invent paper conclusions.
3. Create `mechanism_brief.md` from the current materials. Without it, do not write `scene.py`.
4. Create `episode_strategy.md`, including module type judgment, unique narrative, forbidden reuse from previous episodes, and differences from the most recent three videos.
5. Run the authenticity gate: prove every mechanism planned for the video exists in the current paper or code.
6. Reduce the module to one core insight: "pain point -> current module mechanism -> plug position -> minimal code usage".
7. Use the five-beat timing as workflow only, not as a content template: 0-3s hook, 3-7s problem, 7-15s mechanism, 15-21s code insertion, 21-26s CTA.
8. Prefer Manim mathematical derivation and object transformation over static paper-figure replication. Use the original white-background figure only as a cropped reference or local zoom when it helps.
9. Keep code on screen to 3-5 lines with Chinese comments. Prefer a minimal call like `x = Module(...)(x)` when accurate.
10. Keep the video focused on module adoption, not a full paper review, benchmark discussion, or source-code lecture.
11. Manim must do more than PPT-style static boxes: use formulas, transforms, curves, spectra, tensor flow, heatmaps, gate bars, residual links, insertion animations, or formula-to-code transforms only where they clarify the current module.

### Anti-Shell-Template Rule

Highest priority: module content comes before templates. Templates provide the workflow, not the content structure. Every new module must re-extract its own mechanism and redesign its own animation from the current input materials.

Current input materials include:

- Current module paper PDF.
- Current module code.
- Current module architecture diagram.
- User-provided module notes.
- Current episode topic requirements.

The skill may reuse production workflow, QA checks, 3Blue1Brown style principles, MathTex/Text rendering rules, TTS/subtitle workflow, and render verification workflow.

The skill must not reuse the previous episode's module mechanism, formula, storyboard structure, voiceover phrasing, animation order, or visual metaphor.

Hard rule: "模板提供的是工作流，不是内容结构。每个新模块必须重新抽取机制，重新设计动画。"

WMVF_002 is a success case, not a universal template. Its "decompose -> gate -> fuse -> residual back to main path" structure may only be used when the current module genuinely contains those mechanisms with code or paper evidence.

When generating a new module video, never directly reuse the previous video's formula, mechanism animation, voiceover, variable naming, CTA keyword, or code class. Each episode must start from the current `module_brief` and regenerate:

- `pain_point`
- `module_type`
- `core_mechanism`
- `key_formula`
- `visual_metaphor`
- `min_code`
- `CTA keyword`

QA fails if a new episode contains the previous episode's module name, code class, formula set, CTA keyword, or mechanism animation. In particular:

- Non-frequency modules must not use FFT, Low/High, or Frequency Spectrum visuals by default.
- Non-gate modules must not use a Gate weight bar by default.
- Non-AFDA modules must not contain `AFDA` or `self.afda`.
- Non-current modules must not contain the previous module's code class.
- Formulas must match the current `module_type`.

Required `brief.md` / `plugin_module_brief.yaml` fields before any scene generation:

```text
module_name:
module_abbr:
module_type:
source_paper_or_code:
pain_point:
target_tasks:
core_mechanism:
key_formula:
visual_metaphor:
min_integration_code:
cta_keyword:
bgm_style:
```

If any field is missing, complete a draft brief first and mark inferred fields clearly. Do not fall back to an AFDA-style default template.

Required `mechanism_brief.md` questions before `scene.py`:

1. What are the current module full name and abbreviation?
2. What core problem does the module solve?
3. What is the input tensor?
4. What is the output tensor?
5. What key internal branches exist?
6. What information does each branch extract?
7. Does the module contain frequency transform, wavelet decomposition, attention, gating, multi-scale processing, residual learning, prototype learning, expert routing, calibration, contrastive learning, or feature reconstruction?
8. What is the true core formula?
9. Which single formula is best for the video focus?
10. What animation metaphor best expresses this module?
11. How is this module different from the previous episode?
12. Which previous-episode structures must not be reused?

Required `episode_strategy.md` fields before `scene.py`:

1. Current module type judgment.
2. Why this type judgment is justified.
3. Which structures from the previous episode must not be reused.
4. This episode's unique narrative approach.
5. This episode's core animation spine.
6. This episode's core formula.
7. This episode's visual metaphor.
8. Differences from the most recent three videos.

If `episode_strategy.md` conflicts with the paper, code, or `mechanism_brief.md`, regenerate the strategy before writing or rendering `scene.py`.

Differentiated generation flow:

1. Read `module_brief`.
2. Create and verify `mechanism_brief.md`.
3. Determine `module_type` from evidence.
4. Create `episode_strategy.md`.
5. Select a narrative strategy that matches the module type without copying previous content.
6. Generate the module-specific pain point.
7. Generate the module-specific formula.
8. Generate the module-specific voiceover.
9. Generate the module-specific code snippet.
10. Check for previous-episode residue before rendering and again during QA.

Authenticity gate before `scene.py`:

| Mechanism shown in video | Exists in code/paper | Evidence location | Allowed to show |
|---|---|---|---|
| Gate | Yes/No | Class/function/variable/line or paper section | Yes/No |
| Residual | Yes/No | Evidence | Yes/No |
| Attention | Yes/No | Evidence | Yes/No |
| Frequency | Yes/No | Evidence | Yes/No |
| Wavelet | Yes/No | Evidence | Yes/No |
| Multi-scale | Yes/No | Evidence | Yes/No |

Mechanisms without code or paper evidence are not allowed in the final video.

Content consistency check:

- [ ] Formula comes from the current module, not the previous episode.
- [ ] Animation shows the current module's real computation flow.
- [ ] Voiceover explains the current module, not a generic module template.
- [ ] Subtitles match the voiceover.
- [ ] Visual metaphor fits the current module type.
- [ ] No nonexistent mechanism is drawn into the video.

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

Mandatory layout system:

- Every Manim scene must first choose a scene type: `hook_scene`, `problem_scene`, `mechanism_scene`, `formula_scene`, `code_scene`, or `cta_scene`.
- Then choose a layout template: `title_only_layout`, `title_visual_subtitle_layout`, `two_column_layout`, `center_formula_layout`, `pipeline_layout`, `two_branch_layout`, or `code_cta_layout`.
- Place objects in named zones before writing animations. Do not use ad hoc `shift`, `move_to`, or `next_to` chains as the primary layout method.
- After every `Text`, `MathTex`, `Code`, `VGroup`, arrow, or module block is placed, check safe width, zone height, overlap, subtitle-zone collision, and edge contact.
- A page may not animate until its static layout passes. Template provides workflow, not content structure; layout provides positions, not mechanism content.
- Every Manim page must use Layered Layout: `title_layer`, `formula_layer`, `diagram_layer`, `arrow_layer`, `annotation_layer`, `cta_layer`, and `subtitle_layer`.
- `MathTex` belongs in `formula_layer`; diagrams belong in `diagram_layer`; arrows route only through diagram arrow lanes.
- Arrows must connect object edges, not centers. If a direct arrow would cross formula, text, code, CTA, or subtitle, use an elbow arrow or split the content into another frame.
- Formula and diagram may not share the same y center. If the formula and diagram are both complex, make one formula-led frame and one diagram-led frame.
- Each frame follows the complexity budget: one title, one core formula, one main diagram group, at most three main module boxes, at most three main arrows, one subtitle, and no CTA except on CTA pages.

Required 9:16 module-video zones use `frame_width ≈ 7.2` and `frame_height ≈ 12.8`:

- Safe x range: `-3.1` to `3.1`; safe y range: `-3.35` to `3.65`.
- `title_zone`: y `2.85` to `3.65`, max width `frame_width * 0.86`.
- `visual_zone`: y `-1.45` to `2.45`, max width `frame_width * 0.86`.
- `formula_zone`: y `1.0` to `2.2`, max width `frame_width * 0.82`.
- `code_zone`: y `-0.8` to `1.7`, max width `frame_width * 0.86`.
- `subtitle_zone`: y `-3.25` to `-2.75`, max width `frame_width * 0.88`.
- `cta_zone`: y `-2.55` to `-1.65`, max width `frame_width * 0.86`.
- `formula_layer`: y `1.55` to `2.45`; MathTex only.
- `diagram_layer`: y `-1.05` to `1.25`; modules, feature maps, heatmaps, spectra, nodes.
- `annotation_layer`: y `-1.65` to `-1.15`; short labels only.

Hard layout rules:

- Main visuals must not enter the subtitle zone.
- CTA must not go below `y=-3.0`.
- Titles must not go above `y=3.65`.
- Title and formula must have at least `0.35` vertical separation.
- Code panel and CTA must have at least `0.35` vertical separation.
- Each frame must have one clear main visual center.
- No arrow may pass through a formula, label, code panel, CTA, or subtitle.
- Formula/diagram/arrow collisions must be recorded in `qa_report.md`; collision means QA fails.
- If layout QA fails, create a `layout_fix` version before final render.

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
Use the plug-in module zone system in references/plugin_module_layout_system.md.
For legacy 9x16 scenes, map the same zones proportionally instead of freehand placement.
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
- Never render formulas with `Text`, including fallback paths.
- Do not mix Chinese and formulas in the same `Text`, `Tex`, or `MathTex` object.
- If `MathTex` fails, stop and diagnose LaTeX/MiKTeX before rendering; do not silently replace it with plain text.
- Use raw strings: `r"..."`.
- Use `\mathrm{softmax}` for words inside formulas.
- Prefer compact formulas for mobile screens.
- If LaTeX fails, inspect `media/Tex/*.log` or the generated `.tex` file before rewriting randomly.

### 7.1 3Blue1Brown-style mechanism mode

When the user asks for 3Blue1Brown / 3b1b style, or when the subject is a mathematical mechanism, the scene must be a derivation, not a PPT flowchart:

- Use few words and let formulas, curves, braces, arrows, and object transforms carry the explanation.
- Avoid large stacks of rounded boxes, label cards, and static process diagrams.
- Show the real mechanism as a progression, such as decomposition -> gate/modulation -> fusion -> residual return.
- Keep Chinese text as short helper captions only; never let captions dominate the formula.
- Prefer `TransformMatchingTex`, `ReplacementTransform`, `Brace`, `Arrow`, `ValueTracker`, and geometric motion over slide-like reveals.
- Every module must redesign the animation from its own `core_mechanism`; do not reuse a previous module's visual grammar unless the mechanism is genuinely the same.

### 8. Add audio deliberately

Manim renders silent video unless audio is explicitly added. A spoken script in Markdown is not audio.

Default audio workflow:

1. Generate `voiceover.txt` with one short line per spoken sentence.
2. Generate `voiceover_lines.csv` when external TTS timing or per-line synthesis is useful.
3. Generate `audio/voiceover.wav` with the project TTS script when an API key is available.
4. In `scene.py`, call `self.add_sound("audio/voiceover.wav")` at the start of `construct`; for requested voiceover videos, fail fast if the file is missing.
5. Match total animation duration to the voiceover length.
6. Verify the final MP4 has an audio stream with `ffprobe`.

Alibaba TTS workflow:

1. Prefer Alibaba Bailian/DashScope CosyVoice for new Alibaba-family voiceovers unless the user names another Alibaba service.
2. Output TTS-ready text as short lines, not one long paragraph.
3. Keep Chinese punctuation natural: `，` for small pauses and `。` for sentence stops.
4. Provide recommended fields: model, voice, format, sample rate, speed/rate if supported.
5. Standardize the final audio path to `audio/voiceover.wav` even if the TTS platform first returns MP3.
6. If per-line TTS is used, concatenate line audio in order and verify final duration before rendering.
7. If `DASHSCOPE_API_KEY` is missing, stop before rendering and tell the user to set it. Do not pretend a voiceover was generated.
8. Prefer the repository script `scripts/bailian_tts.py` for project episodes when available.
9. After TTS, verify `audio/voiceover.wav` exists and inspect its duration with `ffprobe`.

If no TTS platform is specified, still prepare the project so the user can place Alibaba-exported audio at `audio/voiceover.wav`. If the user requested a voiced video, do not render a final release candidate without the voiceover file.

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

### 10.1 Required layout pass before final render

Every episode must run these stages:

1. `layout_draft`: generate static key frames or a low-motion draft that focuses on placement.
2. `contact_sheet_check`: render a contact sheet and inspect every beat.
3. `layout_fix`: fix overlap, edge contact, clutter, arrow-through-text, or subtitle/CTA collisions before adding content.
4. `animation_pass`: add motion and 3Blue1Brown-style transforms only after layout passes.
5. `final_render`: mix audio and export `final_with_bgm.mp4` only after layout QA passes.

The rule is: first clear, then clever. First layout, then animation. First QA, then final.

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
- Mathematical formulas have no `Text` fallback.
- Chinese explanation uses `Text` and is separated from `MathTex`.
- Audio is attached with `self.add_sound(...)` when voiceover is requested.
- `audio/voiceover.wav` exists when voiceover is requested.
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
- Silently falling back from `MathTex` to `Text` after LaTeX fails.
- Mixing Chinese and formulas in one object, which can trigger glyph or LaTeX failures.
- Turning a 3b1b-style mechanism into a static PPT flowchart.
- Generating only `voiceover.txt` and never producing or attaching `voiceover.wav`.
- Claiming a final video is voiced without checking the final audio track.
- Assuming Manim will generate narration from the spoken script automatically.
- Showing too many arrows, labels, colors, or equations at once.
- Ending without a conclusion or interaction hook.

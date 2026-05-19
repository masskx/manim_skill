# Plug-in Module Manim Animation Rules

Use this reference when a deep learning plug-in module video moves from brief/script/storyboard into `scene.py`.

## Core Principle

Manim should not only make static PPT-style block diagrams. Use Manim to show how a tensor, formula, distribution, spectrum, attention mask, gate, residual branch, or code call changes over time.

These rules provide workflow discipline, not reusable content structure. Do not copy WMVF_002, AFDA, or the previous episode's mechanism, formula sequence, animation order, or visual metaphor unless the current paper/code proves the same mechanism exists.

Before `scene.py`, the episode must have:

- `mechanism_brief.md`: current mechanism extraction from paper/code/figure/user notes.
- `episode_strategy.md`: current module type judgment, unique narrative, forbidden reuse, core formula, and visual metaphor.

WMVF_002 improved because formula, animation, voiceover, and subtitles all described the same verified mechanism. Copy that discipline, not its fixed "decompose -> gate -> fuse -> residual" structure.

## Formula Rules

- All formulas must use `MathTex`.
- Do not use plain `Text` to fake formulas.
- Do not provide a fallback that renders formulas as `Text` when `MathTex` fails.
- If `MathTex` fails, stop and fix the LaTeX/MiKTeX problem first.
- Chinese explanation must use `Text` and sit outside formula objects.
- Do not mix Chinese and formulas in one `Text`, `Tex`, or `MathTex` object.
- Keep 2-4 core formulas per video.
- Each formula must help the viewer understand the module mechanism.
- Put Chinese explanation in `Text`, not inside `MathTex`.
- Use large formulas that fit 55%-75% of the screen width.
- Use raw strings for formulas, for example `MathTex(r"Z = L + G(L, H) \odot H")`, `MathTex(r"Y = X + P_o(Z)")`, and `MathTex(r"H' = G(L,H) \odot H")`.
- Compile-test important `MathTex` formulas before the full render.

Recommended transformations:

- `Write` for first appearance.
- `TransformMatchingTex` when one equation becomes another.
- `ReplacementTransform` for mechanism step changes.
- `FadeTransform` for formula-to-diagram or formula-to-code handoff.
- `Indicate` or `Circumscribe` for the term that matters, such as `G`, `X_{low}`, or `X_{high}`.

## Standard Helper Functions

Every production scene should define or import helpers with consistent behavior:

```python
def make_label_box(text, color, scale=0.52):
    label = Text(text, font=FONT, font_size=34, color=color, weight=BOLD, line_spacing=0.8)
    label.scale(scale)
    box = SurroundingRectangle(label, buff=0.18, corner_radius=0.12, color=color, stroke_width=2.5)
    box.set_fill(PANEL, opacity=0.9)
    return VGroup(box, label)

def make_formula(tex, scale=1.0):
    formula = MathTex(tex, color=TEXT)
    formula.scale(scale)
    formula.scale_to_fit_width(6.2)
    return formula

def make_glow_arrow(start, end, color):
    arrow = Arrow(start, end, buff=0.12, color=color, stroke_width=5)
    glow = arrow.copy().set_stroke(color=color, width=11, opacity=0.18)
    return VGroup(glow, arrow)
```

Do not use fixed-size rectangles to contain text labels.

## Module Type To Animation Template

Treat this section as a module type recognizer and narrative strategy guide, not a copyable template library. The current module's paper/code decides the structure. Never use one episode's mechanism as the next episode's default.

### Content-first Type Rules

#### Frequency / Fourier Module

- Suitable animation: image or feature changes from spatial domain to frequency domain; low frequency represents structure; high frequency represents detail or noise; spectrum mask, band selection, amplitude/phase split.
- Do not copy wavelet decomposition.
- Do not add gated fusion unless the current module really has a gate.

#### Wavelet / Multi-resolution Module

- Suitable animation: feature decomposes into scales or sub-bands; low-frequency part preserves contour; high-frequency parts preserve edges and textures; multi-view fusion or reconstruction.
- Do not copy Fourier spectrum rings.
- Do not use attention heatmaps unless the code really has attention.

#### Attention Module

- Suitable animation: Query / Key / Value; weight matrix; information redistribution between tokens or regions; dynamic attention map highlight.
- Formula options: `\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^T/\sqrt{d})V`, `Y=X\odot M(X)`, or the paper's own attention equation.
- Do not copy wavelet decomposition.
- Do not copy frequency filtering.
- Do not add residual-compensation narration unless the code really has residual learning.

#### Multi-scale Convolution Module

- Suitable animation: different convolution kernels or receptive fields; small scale sees detail; large scale sees context; multi-scale feature aggregation.
- Formula option: `Y=\mathrm{Fuse}(F_1,F_2,F_3)` when accurate.
- Do not copy QKV attention.
- Do not copy Fourier or wavelet decomposition.

#### Gating / Dynamic Fusion Module

- Suitable animation: gate changes from 0 to 1; one feature branch is enhanced or suppressed; gate weights control information flow.
- Formula option: `Y=G\odot A+(1-G)\odot B` or the paper's own gate equation.
- If the module has no gate, do not force a gate narrative.

#### Residual / Compensation Module

- Suitable animation: main path preserves original feature; side path learns only a compensation; output equals original feature plus correction.
- Formula option: `Y=X+F(X)` only when the module really uses residual addition.
- If the module is not residual, do not force it into `Y=X+F(X)`.

#### MoE / Expert Routing Module

- Suitable animation: multiple experts in parallel; router assigns weights; top-k experts activate; different samples take different paths.
- Do not copy frequency decomposition, wavelet sub-bands, or ordinary attention unless those mechanisms also exist.

#### Prototype / Calibration / Open-set Module

- Suitable animation: class prototypes; sample-to-prototype distances; threshold boundary; known and unknown classes separate; distribution changes before and after calibration.
- Do not copy CNN insertion narration or generic image-enhancement narration.

#### Adapter / CNN Block Module

- Adapter: show a lightweight module inserted into an existing backbone only when the code/paper frames it as an adapter.
- CNN block: show Conv / BN / Act / Branch / Concat in data-flow order only when those operations exist.
- Do not reduce every module to "input -> branch -> fusion -> output"; use the current module's real computation.

Choose the template from `module_type` in the current brief. Do not choose it from the previous episode or from AFDA unless the current module is actually AFDA. If the module mixes types, use the smallest accurate hybrid and state it in QA.

### Attention Module

- Visuals: channel weights, spatial heatmap, Q/K/V nodes, attention matrix.
- Formula: `\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^T/\sqrt{d})V` or `Y=X\odot M(X)`.
- Voiceover pattern: "让模型知道该看哪里。"
- Motion: heatmap sweeps over feature map; selected regions brighten.
- Main visual: Feature Map -> Attention Map -> Weighted Feature.
- Do not use FFT or frequency spectrum by default.

### Frequency Module

- Visuals: FFT, frequency spectrum dots, center low-frequency region, outer high-frequency ring.
- Formula: `\mathcal{F}(X)=\mathrm{FFT}(X)`, `X=X_{low}+X_{high}`.
- Voiceover pattern: "低频看结构，高频看细节。"
- Motion: feature grid flows into FFT formula, then splits into low/high streams.
- Main visual: Feature Map -> FFT/Spectrum -> Low/High -> Output.

### Residual Module

- Visuals: main path, residual side path, Add node.
- Formula: `Y=X+F(X)`.
- Voiceover pattern: "不推翻原特征，只补一条支路。"
- Motion: original path stays visible while a branch pulses into Add.
- Main visual: X goes through the main path while a skip path reaches Add.

### Multi-scale Module

- Visuals: branches with different kernel sizes or receptive fields, Concat/Fusion node.
- Formula: `Y=\mathrm{Fuse}(F_1,F_2,F_3)`.
- Voiceover pattern: "小尺度看细节，大尺度看全局。"
- Motion: three branches appear one by one, then merge into one output.
- Main visual: input splits into multiple scale branches, then Fuse/Concat.

### Adapter Module

- Visuals: Backbone block, insertion slot, lightweight adapter card.
- Formula: `Y=\mathrm{Adapter}(X)`.
- Voiceover pattern: "不改主干，直接插进去。"
- Motion: adapter snaps into the feature path with a short pop or plug-in animation.
- Main visual: Backbone -> inserted lightweight Adapter -> enhanced feature.

### Gating Module

- Visuals: Gate node, weight slider, two inputs, weighted output.
- Formula: `Y=G\odot A+(1-G)\odot B`.
- Voiceover pattern: "Gate 决定该补多少。"
- Motion: `G` value changes from low to high; output color or thickness changes with it.
- Main visual: A/B inputs -> Gate -> weighted fusion -> output.

### CNN Block Module

- Visuals: Conv, Branch, BN, Activation, Concat, Add.
- Voiceover pattern: "像积木一样接进网络。"
- Motion: blocks assemble in data-flow order; do not show every internal layer at once.
- Main visual: Conv / BN / Act / Branch / Concat blocks assembled in flow order.

## Voiceover Hard Rules

Every episode must generate `voiceover.txt`. QA fails when it is missing or empty.
When the user requests a voiced/release video, every episode must also generate `audio/voiceover.wav`, attach it in `scene.py` with `self.add_sound(...)`, and verify the final video has an audio track.

If `DASHSCOPE_API_KEY` is missing for Bailian/DashScope TTS, stop before the TTS call and show the exact setup command. Do not render a final voiced video and do not mark QA as passed.

`voiceover.txt` should contain:

- Hook: 2-3 short lines.
- Problem: 2-3 short lines.
- Mechanism: 4-6 short lines.
- Code: 2 short lines.
- CTA: 2 short lines.

Do not reuse the previous episode's voiceover. Do not ship subtitles without a voiceover script.

## 3Blue1Brown-style Mechanism Rules

For 3b1b-style module videos:

- Do not build a PPT flowchart made of stacked rounded boxes.
- Use a small number of mathematical objects and let them transform.
- Prefer decomposition, modulation, fusion, residual links, braces, arrows, and formula morphs.
- Keep captions short and subordinate to the mathematical visual.
- Use `ValueTracker` for changing gates/weights instead of static labels.
- Use `TransformMatchingTex` where formulas evolve.

## Formula Check Rules

Every `qa_report.md` must state:

- Which formulas the current module uses.
- Why those formulas fit the current `module_type`.
- Whether a previous module formula appears.
- Whether any formula conflicts with `module_type`.

If a formula cannot be determined, use one compact generic module expression. Do not force AFDA formulas onto non-AFDA modules.

## Formula To Code Handoff

End the mechanism with the adoption equation:

```tex
Y=\mathrm{Module}(X)
```

Then transform or fade it into the minimum code snippet. Highlight the line that actually calls the module.

Example:

```python
self.afda = AFDA(channels)      # 对齐通道
feat = backbone(x)              # 提取特征
feat = self.afda(feat)          # 频域适配
```

## Visual Restraint

- One main title, one core formula, and one core graphic per frame.
- Do not keep old labels after their explanatory beat ends.
- Do not cover the main visual with subtitles.
- Do not paste a full white-background paper figure into the vertical frame.
- Use original figures only as a local zoom or reference; prefer Manim redraws.

## Layout And Overlap Guards

Before rendering, wrap all major `Text`, `MathTex`, `Code`, and `VGroup` objects with:

```python
safe_scale_to_width(mobject, max_width=config.frame_width * 0.85)
```

Labels must use `SurroundingRectangle(label, buff=0.16-0.22)`. Do not use fixed `Rectangle` wrappers for text labels.

For the final 5 seconds, separately check:

- Code panel and CTA do not overlap.
- CTA line 1 and line 2 do not overlap.
- Subtitles and CTA do not overlap.
- Title and formula do not overlap.
- MathTex stays within safe width.
- Text stays within 85% screen width.

## Mandatory Layout System

All plug-in module `scene.py` files must use the layout system in `plugin_module_layout_system.md`.

Required workflow for every page:

1. Choose scene type: `hook_scene`, `problem_scene`, `mechanism_scene`, `formula_scene`, `code_scene`, or `cta_scene`.
2. Choose layout template: `title_visual_subtitle_layout`, `center_formula_layout`, `pipeline_layout`, `two_branch_layout`, or `code_cta_layout`.
3. Place objects inside safe zones.
4. Run width, height, edge, subtitle-zone, and overlap checks.
5. Only then animate.

Use these helpers or equivalent helpers in every generated scene:

- `safe_scale_to_width(mobject, max_width)`
- `safe_scale_to_height(mobject, max_height)`
- `fit_to_box(mobject, max_width, max_height)`
- `make_label_box(text, color, font_size=30)` using `SurroundingRectangle(label, buff=0.16-0.22)`, never fixed rectangles.
- `make_safe_title(text)`
- `arrange_without_overlap(group, direction, buff)`
- `place_in_zone(mobject, zone_name)`
- `check_overlaps(mobjects)`

Forbidden layout patterns:

- Many ad hoc `obj.shift(UP * 3 + LEFT * 2)` calls.
- Unplanned `obj.move_to([x, y, 0])` scatter.
- Multiple text lines with the same manual y coordinate.
- Fixed `Rectangle` boxes around labels.
- Arrows from object center to object center when they pass through text.
- `Write(MathTex(...))` or long code display before width checks.
- More than five major objects in one frame.
- Title, formula, diagram, subtitle, and CTA piled in the same central area.

Required layout pass:

- `layout_draft`
- `contact_sheet_check`
- `layout_fix` when overlap, edge contact, clutter, or subtitle/CTA collision exists
- `animation_pass`
- `final_render`

Do not export `final_with_bgm.mp4` until layout QA passes.

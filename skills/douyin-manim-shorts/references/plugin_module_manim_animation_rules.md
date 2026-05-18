# Plug-in Module Manim Animation Rules

Use this reference when a deep learning plug-in module video moves from brief/script/storyboard into `scene.py`.

## Core Principle

Manim should not only make static PPT-style block diagrams. Use Manim to show how a tensor, formula, distribution, spectrum, attention mask, gate, residual branch, or code call changes over time.

## Formula Rules

- All formulas must use `MathTex`.
- Do not use plain `Text` to fake formulas.
- Keep 2-4 core formulas per video.
- Each formula must help the viewer understand the module mechanism.
- Put Chinese explanation in `Text`, not inside `MathTex`.
- Use large formulas that fit 55%-75% of the screen width.

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

### Attention Module

- Visuals: channel weights, spatial heatmap, Q/K/V nodes, attention matrix.
- Formula: `\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^T/\sqrt{d})V` or `Y=X\odot M(X)`.
- Voiceover pattern: "让模型知道该看哪里。"
- Motion: heatmap sweeps over feature map; selected regions brighten.

### Frequency Module

- Visuals: FFT, frequency spectrum dots, center low-frequency region, outer high-frequency ring.
- Formula: `\mathcal{F}(X)=\mathrm{FFT}(X)`, `X=X_{low}+X_{high}`.
- Voiceover pattern: "低频看结构，高频看细节。"
- Motion: feature grid flows into FFT formula, then splits into low/high streams.

### Residual Module

- Visuals: main path, residual side path, Add node.
- Formula: `Y=X+F(X)`.
- Voiceover pattern: "不推翻原特征，只补一条支路。"
- Motion: original path stays visible while a branch pulses into Add.

### Multi-scale Module

- Visuals: branches with different kernel sizes or receptive fields, Concat/Fusion node.
- Formula: `Y=\mathrm{Fuse}(F_1,F_2,F_3)`.
- Voiceover pattern: "小尺度看细节，大尺度看全局。"
- Motion: three branches appear one by one, then merge into one output.

### Adapter Module

- Visuals: Backbone block, insertion slot, lightweight adapter card.
- Formula: `Y=\mathrm{Adapter}(X)`.
- Voiceover pattern: "不改主干，直接插进去。"
- Motion: adapter snaps into the feature path with a short pop or plug-in animation.

### Gating Module

- Visuals: Gate node, weight slider, two inputs, weighted output.
- Formula: `Y=G\odot A+(1-G)\odot B`.
- Voiceover pattern: "Gate 决定该补多少。"
- Motion: `G` value changes from low to high; output color or thickness changes with it.

### CNN Block Module

- Visuals: Conv, Branch, BN, Activation, Concat, Add.
- Voiceover pattern: "像积木一样接进网络。"
- Motion: blocks assemble in data-flow order; do not show every internal layer at once.

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

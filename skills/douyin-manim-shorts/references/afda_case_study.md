# AFDA Case Study

AFDA is the first experimental sample for the deep learning plug-in module mode in this skill. Treat it as a production lesson, not as a new standalone skill.

## Module Positioning

For short-video purposes, AFDA was framed as a lightweight frequency-domain adapter:

- It plugs in after feature maps.
- It looks at low-frequency structure and high-frequency edge/detail information.
- It uses a gate and lightweight convolution to adapt features.
- It should not be presented as a full AFDAN paper framework unless the user asks for a full paper explainer.

## V2 Lessons

V2 improved the video by moving away from course-style explanation and into Douyin pacing:

- Strong first-second pain hook.
- Fast visual changes every 2-3 seconds.
- Clear sequence: pain point -> mechanism -> code -> CTA.
- More direct language such as "换个数据集就崩？" and "复制 3 行就能用".
- CTA became a resource-pack prompt instead of a paper-summary ending.

Reusable lesson: plug-in module shorts should sell adoption value quickly, then use one mechanism animation to justify why the module helps.

## V4 Lessons

V4 started to use Manim's strengths:

- `MathTex` formulas.
- Feature map to FFT to frequency spectrum.
- Low/high frequency split.
- Gate weighted fusion.
- Source/Target frequency-domain alignment curves.
- Formula-to-code transition.

Reusable lesson: a Manim module video should not stop at boxes and arrows. It should animate a formula, tensor flow, distribution, spectrum, heatmap, gate, residual path, or branch fusion.

## V4.1 Problems Found

The first V4 pass exposed hard production issues:

- Red debug boxes appeared around Low, High, and Gate modules.
- Text and borders did not fit tightly.
- A central cross-axis background looked like a distracting coordinate system.
- Elements were crowded in the middle of the vertical frame.
- Subtitles were too low and risked being covered by the player UI.
- Arrows sometimes passed through labels.
- Some formulas and titles were too large for a phone-safe composition.

These are now hard QA rules for future videos.

## Rules To Carry Forward

- Never leave debug boxes, guide boxes, or red placeholder rectangles in final render.
- Generate module labels with `make_label_box()` and `SurroundingRectangle`.
- Keep background grids subtle; avoid full-screen center axes.
- Use explicit vertical safe zones before placing objects.
- Keep subtitles around `y = -3.15` with a semi-transparent backing strip.
- Point arrows to module edges and avoid crossing text.
- Keep formulas large but bounded within the safe width.
- Make code snippets minimal and highlight the actual inserted line.

## AFDA-Style Frequency Template

Recommended beat:

```text
Pain: domain or dataset shift makes feature distributions misalign.
Mechanism: X -> FFT -> spectrum -> low/high split -> gate fusion -> output.
Formula set: F(X)=FFT(X), X=X_low+X_high, Y=G⊙X_low+(1-G)⊙X_high.
Code: self.afda = AFDA(channels); feat = backbone(x); feat = self.afda(feat).
CTA: PDF notes + PyTorch code + architecture figure.
```

Do not claim paper conclusions or benchmark wins unless the provided paper/materials support them.

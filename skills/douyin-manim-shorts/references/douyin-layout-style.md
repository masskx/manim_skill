# Douyin Layout Style

Use this reference when creating or revising a vertical Manim short. The goal is a polished mobile explainer, not a classroom slide.

## Visual Personality

- Clear, direct, high-contrast, but not noisy.
- One strong visual idea per screen.
- Smooth staged reveals instead of many simultaneous labels.
- Bold hook and takeaway; calmer middle explanation.
- Consistent shapes: one caption style, one tag style, one formula style.

## Typography System

Use one font family and three sizes:

| Role | Size | Use |
|---|---:|---|
| Title | 56-68 | Hook, cover-like opening, final punchline |
| Body/subtitle | 34-42 | Captions, short explanations, main labels |
| Micro-label | 24-30 | Q/K/V tags, percentages, tiny annotations |

Rules:

- Do not use more than 3 text sizes in one scene.
- Do not combine huge titles with tiny explanatory text unless the tiny text is nonessential.
- Use bold for title and key phrase only.
- Use scale-to-fit on every user-facing text object.
- Keep subtitle lines short; if a sentence is long, split it across beats, not across tiny text.

## Color System

Use a dark neutral background plus 2-3 semantic colors:

- White/off-white: main readable text.
- Muted gray: secondary labels.
- Yellow: key insight or selected object.
- Cyan: motion, connection, or query/key relationship.
- Red/pink: conflict, warning, or misconception.

Avoid rainbow diagrams. If two colors do not carry distinct meanings, remove one.

## Vertical Layout

Reserve zones:

```text
Top title zone:       y = 5.7 to 7.1
Main visual zone:     y = -2.6 to 4.8
Formula/detail zone:  y = -4.7 to -3.1
Subtitle zone:        y = -6.7 to -5.7
```

Never place important diagrams behind the subtitle zone. Avoid right-edge detail because platform UI may cover it.

### Plug-in Module Safe Area

For 9:16 deep learning plug-in module videos, use the Manim frame as a fixed vertical stage:

```text
Top title zone:       y = 3.0 to 3.7
Main visual zone:     y = -1.8 to 2.2
Subtitle zone:        y = -3.15 around the caption center
CTA lower bound:      y >= -3.25
Core element x-range: -3.0 to 3.0
```

Hard rules:

- Do not place titles against the top edge.
- Do not place subtitles below the player-safe area.
- Do not place formulas, code panels, or CTA cards below `y = -3.25`.
- Do not let core elements touch the left or right edge; keep them inside `x = -3.0` to `x = 3.0`.
- Every frame should have one dominant visual focus: title, formula, mechanism, code, or CTA.

## Label Box Rules

All labels such as `Low`, `High`, `Gate`, `AFDA`, `Conv`, `Next`, `Output`, `Attention`, `SE`, and `CBAM` must be generated with one shared helper. Do not wrap text with fixed-width or fixed-height rectangles.

Required pattern:

```python
def make_label_box(text, color, scale=0.52):
    label = Text(text, font=FONT, font_size=34, color=color, weight=BOLD, line_spacing=0.8)
    label.scale(scale)
    box = SurroundingRectangle(
        label,
        buff=0.18,
        corner_radius=0.12,
        color=color,
        stroke_width=2.5,
    )
    box.set_fill(PANEL, opacity=0.9)
    return VGroup(box, label)
```

Rules:

- Create the `Text` or `VGroup` first, then wrap it with `SurroundingRectangle`.
- Keep Chinese-English combinations such as `Low\n轮廓` centered as one label group.
- Text must never overflow its border.
- Borders must not be oversized placeholders.
- Red debug rectangles must never appear in final renders.

## Subtitle Safety

- Put subtitles around `y = -3.15`.
- Use a semi-transparent black backing strip.
- Keep the strip above the bottom danger zone; do not extend it below about `y = -3.45`.
- Keep each subtitle beat short, ideally 6-12 Chinese characters for plug-in module shorts.
- Split long narration across beats instead of shrinking the text.

## Composition Patterns

Good:

- Hook title at top, one animated diagram in the middle, one subtitle at bottom.
- Replace the title with a diagram label once the explanation starts.
- Fade old labels before showing formulas.
- Use a short formula line plus a Chinese explanation below or above it.

Bad:

- Title, subtitle, formula, diagram, arrows, and comment prompt all visible together.
- Many free-floating labels with different sizes.
- A large title that stays on screen while the middle becomes crowded.
- Small math in a corner.

## Manim Implementation Rules

- Define constants: `TITLE_SIZE`, `BODY_SIZE`, `LABEL_SIZE`, `TAG_SIZE`, `FORMULA_SIZE`.
- Use helper constructors: `make_title`, `make_subtitle`, `make_chip`, `make_formula`.
- For module labels, use `make_label_box`; never use fixed-size `Rectangle` or `RoundedRectangle` to contain unknown text.
- For formulas, use `MathTex`; never use `Text` to fake mathematical notation.
- For arrows, use a shared helper such as `make_glow_arrow(start, end, color)` and point arrows to module edges, not through text.
- Use `scale_to_fit_width` for text, formulas, and groups before positioning.
- Position by zones rather than long `next_to` chains.
- Keep a final hold of 0.6-1.5 seconds unless the user asks for an outro.
- Avoid full-screen center cross-axis backgrounds. If grid texture is needed, keep it very faint with opacity about 0.08-0.15.
- If a local axis or spectrum grid is needed, confine it to the spectrum area only.

## Manim Formula And Motion

Manim should not behave like static PPT. Use its strengths to make the mechanism visible:

- `MathTex` formula rendering.
- `TransformMatchingTex`, `ReplacementTransform`, and `FadeTransform`.
- Curve animations for distribution shifts.
- Frequency spectrum point clouds and low/high frequency splitting.
- Tensor flow dots and animated arrows.
- Attention heatmaps and masks.
- Gate weight bars and dynamic weighted fusion.
- Residual paths and Add nodes.
- Plug-in insertion animations.
- Formula-to-code transforms.

Keep only 2-4 core formulas in one plug-in module video. A formula must explain the mechanism; do not add equations just to look technical.

## Post-Render Review

Generate a contact sheet and inspect:

- First 3 seconds: hook is readable.
- Every transition: no object crosses through a text block in an ugly way.
- Middle: formula and diagram do not compete for the same zone.
- Final 5 seconds: no frozen padding and no crowded outro.

Additional hard checks for plug-in module videos:

- No red debug boxes or placeholder rectangles.
- No full-screen central cross line.
- Label text fits its border.
- Arrows do not pass through words.
- Formulas do not exceed the safe width.
- Code is readable on a phone.
- Contact sheet shows a clear main visual in every sampled frame.

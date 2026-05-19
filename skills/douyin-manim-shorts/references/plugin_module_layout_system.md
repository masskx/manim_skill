# Plug-in Module Manim Layout System

This file is a hard rule layer for all Manim plug-in module shorts. It prevents crowded symbols, overlapping formulas, arrows crossing text, subtitle collisions, and CTA/code-page clutter.

## Highest Priority Rule: Layout Before Animation

Every Manim scene must follow this order:

1. Choose the current scene type: `hook_scene`, `problem_scene`, `mechanism_scene`, `formula_scene`, `code_scene`, or `cta_scene`.
2. Choose a layout template: `title_only_layout`, `title_visual_subtitle_layout`, `two_column_layout`, `center_formula_layout`, `pipeline_layout`, `two_branch_layout`, or `code_cta_layout`.
3. Place every object inside a named safe zone. Do not freely pile objects with ad hoc `shift`, `move_to`, or `next_to` chains.
4. After placing each `Text`, `MathTex`, `Code`, `VGroup`, arrow, or module glyph, check:
   - width <= `config.frame_width * 0.85` unless the zone says otherwise;
   - height <= the target zone height;
   - it does not overlap other visible objects;
   - it does not enter the subtitle zone;
   - it is not touching frame edges.
5. Only after layout QA passes may the scene play animations.

Principle: clarity first, motion second. First layout, then animation. First QA, then final.

## 9:16 Canvas Zones

Default module-video canvas:

```python
config.frame_width = 7.2
config.frame_height = 12.8
```

Safe area:

- x range: `-3.1` to `3.1`
- y range: `-3.35` to `3.65`

Named fixed zones:

| Zone | y range / center | Purpose | Max width |
|---|---:|---|---:|
| `title_zone` | `2.85` to `3.65` | main title | `frame_width * 0.86` |
| `visual_zone` | `-1.45` to `2.45` | mechanism graphic, formula, module flow | `frame_width * 0.86` |
| `formula_zone` | `1.0` to `2.2` | core formula | `frame_width * 0.82` |
| `code_zone` | `-0.8` to `1.7` | code panel | `frame_width * 0.86` |
| `subtitle_zone` | `-3.25` to `-2.75` | subtitles | `frame_width * 0.88` |
| `cta_zone` | `-2.55` to `-1.65` | ending CTA | `frame_width * 0.86` |

Hard limits:

- Main visuals must not enter `subtitle_zone`.
- CTA must not go below `y=-3.0`.
- Titles must not go above `y=3.65`.
- Title and formula must be separated by at least `0.35`.
- Code panel and CTA must be separated by at least `0.35`.
- Each frame may have only one main visual center.

## Layout Templates

### `title_visual_subtitle_layout`

Use for ordinary mechanism explanation pages.

- Put `title` centered in `title_zone`.
- Put `visual_group` centered in `visual_zone`.
- Put `subtitle` centered in `subtitle_zone`.

Forbidden:

- Title overlapping `visual_group`.
- Subtitle overlapping `visual_group`.

### `center_formula_layout`

Use for formula explanation pages.

- Put `title` at the top.
- Put `formula` at `y=1.2` to `1.8`.
- Put explanatory visual at `y=-0.6` to `0.5`.
- Put subtitle in the bottom safe area.
- If the formula is wide, call `scale_to_fit_width(config.frame_width * 0.82)`.

### `pipeline_layout`

Use for input -> module -> output scenes.

- Input module: `x=-2.2`.
- Middle module: `x=0`.
- Output module: `x=2.2`.
- All modules: `y=0.4`.
- Arrows connect object edges, not centers, and never pass through label text.
- If total module width exceeds `6.2`, switch to a two-row layout.

### `two_branch_layout`

Use for dual/multi-branch, Residual, or Gating mechanisms.

- Input: `x=-2.4, y=0.4`.
- Upper branch: `y=1.0`.
- Lower branch: `y=-0.4`.
- Fusion node: `x=1.4, y=0.3`.
- Output: `x=2.5, y=0.3`.
- Vertical branch gap must be at least `0.75`.
- Arrows must not pass through labels.

### `code_cta_layout`

Use for the final code and CTA page.

- Title in `title_zone`.
- `code_panel` centered around `y=0.7`.
- `highlight_text` below the code panel, around `y=-1.2`.
- CTA two-line group around `y=-2.1`.
- Subtitle around `y=-3.15`.
- `code_panel` must not exceed `visual_zone`.
- CTA must not overlap subtitles.

## Required Manim Layout Helpers

Every generated `scene.py` for plug-in module shorts should provide these helpers or equivalent project helpers.

```python
SAFE_X_MIN, SAFE_X_MAX = -3.1, 3.1
SAFE_Y_MIN, SAFE_Y_MAX = -3.35, 3.65
ZONES = {
    "title_zone": {"center": [0, 3.25, 0], "max_width": config.frame_width * 0.86, "max_height": 0.8},
    "visual_zone": {"center": [0, 0.50, 0], "max_width": config.frame_width * 0.86, "max_height": 3.9},
    "formula_zone": {"center": [0, 1.60, 0], "max_width": config.frame_width * 0.82, "max_height": 1.2},
    "code_zone": {"center": [0, 0.45, 0], "max_width": config.frame_width * 0.86, "max_height": 2.5},
    "subtitle_zone": {"center": [0, -3.00, 0], "max_width": config.frame_width * 0.88, "max_height": 0.55},
    "cta_zone": {"center": [0, -2.10, 0], "max_width": config.frame_width * 0.86, "max_height": 0.9},
}

def safe_scale_to_width(mobject, max_width):
    if mobject.width > max_width:
        mobject.scale_to_fit_width(max_width)
    return mobject

def safe_scale_to_height(mobject, max_height):
    if mobject.height > max_height:
        mobject.scale_to_fit_height(max_height)
    return mobject

def fit_to_box(mobject, max_width, max_height):
    safe_scale_to_width(mobject, max_width)
    safe_scale_to_height(mobject, max_height)
    return mobject

def place_in_zone(mobject, zone_name):
    zone = ZONES[zone_name]
    fit_to_box(mobject, zone["max_width"], zone["max_height"])
    mobject.move_to(zone["center"])
    return mobject

def make_label_box(text, color, font_size=30):
    label = Text(text, font=FONT, font_size=font_size, color=color, weight=BOLD)
    safe_scale_to_width(label, config.frame_width * 0.32)
    box = SurroundingRectangle(label, buff=0.18, corner_radius=0.12, color=color, stroke_width=2)
    box.set_fill(PANEL, opacity=0.9)
    return VGroup(box, label)

def make_safe_title(text):
    title = Text(text, font=FONT, font_size=52, color=TEXT, weight=BOLD)
    return place_in_zone(title, "title_zone")

def arrange_without_overlap(group, direction=DOWN, buff=0.25):
    group.arrange(direction, buff=max(buff, 0.25), aligned_edge=ORIGIN)
    return group
```

`check_overlaps(mobjects)` must inspect bounding boxes before preview render. If overlap is detected, print warnings and record them in `qa_report.md`.

```python
def mobject_bbox(m):
    return (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])

def boxes_overlap(a, b, pad=0.04):
    ax1, ax2, ay1, ay2 = mobject_bbox(a)
    bx1, bx2, by1, by2 = mobject_bbox(b)
    return ax1 < bx2 - pad and ax2 > bx1 + pad and ay1 < by2 - pad and ay2 > by1 + pad

def check_overlaps(mobjects, label="scene"):
    warnings = []
    visible = [m for m in mobjects if m is not None]
    for i, a in enumerate(visible):
        if a.width > config.frame_width * 0.90:
            warnings.append(f"{label}: object {i} exceeds 90% frame width")
        if a.get_left()[0] < SAFE_X_MIN or a.get_right()[0] > SAFE_X_MAX:
            warnings.append(f"{label}: object {i} outside safe x range")
        if a.get_bottom()[1] < SAFE_Y_MIN or a.get_top()[1] > SAFE_Y_MAX:
            warnings.append(f"{label}: object {i} outside safe y range")
        for j, b in enumerate(visible[i + 1 :], start=i + 1):
            if boxes_overlap(a, b):
                warnings.append(f"{label}: object {i} overlaps object {j}")
    for warning in warnings:
        print("[layout-warning]", warning)
    return warnings
```

## Forbidden Layout Patterns

Do not generate scene code that relies on:

- Many `obj.shift(UP * 3 + LEFT * 2)` calls as the layout system.
- Ad hoc `obj.move_to([x, y, 0])` for many unrelated objects without named zones.
- Multiple `Text` objects manually assigned the same `y` coordinate.
- Fixed-width or fixed-height `Rectangle` wrappers around text.
- Arrows connecting object centers instead of edges.
- `Write(MathTex(...))` before width checks.
- Long code panels before width checks.
- More than five major objects on one frame.
- Title, formula, diagram, subtitle, and CTA all piled near the center.

Recommended patterns:

- Group related objects with `VGroup` first.
- Use `arrange` for rows, columns, CTA lines, tags, and multi-line labels.
- Use `next_to` only with `buff >= 0.25`.
- Use `align_to` for clean shared baselines or columns.
- Use `SurroundingRectangle(label, buff=0.16-0.22)` for label boxes.
- Express one core concept per page.
- Run all major elements through `safe_scale_to_width` or `fit_to_box`.

## Required Layout Pass

Every episode must include a layout pass before final rendering:

1. `layout_draft`: create static key frames or a low-motion draft focused only on placement.
2. `contact_sheet_check`: render a contact sheet from the draft.
3. `layout_fix`: if there is overlap, edge contact, subtitle collision, or confusing density, fix layout before adding new content.
4. `animation_pass`: add transforms and motion only after layout passes.
5. `final_render`: mix audio and export `final_with_bgm.mp4` only after layout QA passes.

If any layout item fails, do not publish a final version. Create a `layout_fix` revision first.

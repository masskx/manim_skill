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

## Layered Layout: Highest Priority Visual Separation

Every Manim page must be designed as layered composition, not as one shared pile of objects. Decide the layer for each object before placing it.

| Layer | Allowed content | y range | z_index |
|---|---|---:|---:|
| `title_layer` | title only | `2.90` to `3.65` | `5` |
| `formula_layer` | `MathTex` formulas only | `1.55` to `2.45` | `4` |
| `diagram_layer` | modules, feature maps, heatmaps, spectra, nodes | `-1.05` to `1.25` | `3` |
| `arrow_layer` | arrows, connector lines, flow particles only | inside diagram lanes | `2` |
| `annotation_layer` | short labels, callouts, "copy 3 lines" notes | `-1.65` to `-1.15` | `5` |
| `cta_layer` | CTA only | `-2.45` to `-1.75` | `7` |
| `subtitle_layer` | subtitles only | `-3.25` to `-2.85` | `6` |

Hard layered-layout rules:

- `MathTex` formulas default to `formula_layer`; diagrams default to `diagram_layer`.
- Formulas and diagrams must not share the same y center or the same arrow lane.
- Arrows must be routed inside `diagram_layer`; they must not cross `formula_layer`, `subtitle_layer`, or `cta_layer`.
- Formulas must not sit inside the middle of a module pipeline or between two arrows.
- Arrows must never start at object centers, end at object centers, or cover internal text.
- If a formula and a diagram are both complex, split them into two frames instead of shrinking them into one crowded frame.

## Formula And Diagram Separation

Formula pages must choose one of two modes:

### Mode A: Formula-led page

- Title stays in `title_layer`.
- Formula stays in `formula_layer`.
- Diagram is a simplified support visual in `diagram_layer`.
- The support visual contains at most three modules.
- The page uses at most two arrows.

### Mode B: Diagram-led page

- Title stays in `title_layer`.
- Diagram stays in `diagram_layer`.
- Formula is omitted, or reduced to one short local expression.
- The full formula explanation moves to the next frame.

Forbidden:

- One frame containing a long formula, a multi-module diagram, many arrows, subtitles, and CTA.
- A formula crossing the visual center while arrows pass over it.
- Formula and modules sharing one horizontal track.
- `MathTex` placed on a pipeline arrow path.

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
- Use Formula-led mode: at most one small support visual and one or two short arrows.
- Do not put a complex branch diagram under a long formula; split the page.

### `pipeline_layout`

Use for input -> module -> output scenes.

- Input module: `x=-2.2`.
- Middle module: `x=0`.
- Output module: `x=2.2`.
- All modules: `y=0.2` in `diagram_layer`.
- Arrow lane: `y=0.2`.
- Formula lane: `y=1.8`; formulas must not sit on the module/arrow lane.
- Arrows connect object edges, not centers, and never pass through label text.
- If total module width exceeds `6.2`, switch to a two-row layout.

### `two_branch_layout`

Use for dual/multi-branch, Residual, or Gating mechanisms.

- Input: `x=-2.4, y=0.4`.
- Upper branch arrow lane: `y=0.85`.
- Lower branch arrow lane: `y=-0.55`.
- Fusion/Gate/Add node: `x=1.2, y=0.15`.
- Output: `x=2.5, y=0.3`.
- Vertical branch gap must be at least `0.75`.
- Formula must not sit on `y=0.85` or `y=-0.55`.
- Arrows must not pass through labels.

### `formula_layout`

Use for derivation pages.

- Complex arrows are forbidden.
- Formula owns the page.
- Under the formula, place at most one lightweight visual.
- Arrow count is limited to one or two.

### `code_cta_layout`

Use for the final code and CTA page.

- Title in `title_zone`.
- `code_panel` centered around `y=0.7`.
- `highlight_text` below the code panel, around `y=-1.2`.
- CTA two-line group around `y=-2.1`.
- Subtitle around `y=-3.15`.
- `code_panel` must not exceed `visual_zone`.
- CTA must not overlap subtitles.
- Complex process arrows are forbidden on code pages.

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
LAYERS = {
    "background": 0,
    "grid": 1,
    "arrows": 2,
    "diagram": 3,
    "formula": 4,
    "labels": 5,
    "subtitles": 6,
    "cta": 7,
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

def set_layer(mobject, layer_name):
    mobject.set_z_index(LAYERS[layer_name])
    return mobject

def edge_point(mobject, side, buff=0.08):
    if side == "right":
        return mobject.get_right() + RIGHT * buff
    if side == "left":
        return mobject.get_left() + LEFT * buff
    if side == "top":
        return mobject.get_top() + UP * buff
    if side == "bottom":
        return mobject.get_bottom() + DOWN * buff
    return mobject.get_center()

def make_elbow_arrow(start_obj, end_obj, direction="right", color=WHITE):
    if direction in ("right", "left_to_right"):
        p1 = edge_point(start_obj, "right")
        p4 = edge_point(end_obj, "left")
        mid_x = (p1[0] + p4[0]) / 2
        p2 = np.array([mid_x, p1[1], 0])
        p3 = np.array([mid_x, p4[1], 0])
    elif direction in ("down", "top_to_bottom"):
        p1 = edge_point(start_obj, "bottom")
        p4 = edge_point(end_obj, "top")
        mid_y = (p1[1] + p4[1]) / 2
        p2 = np.array([p1[0], mid_y, 0])
        p3 = np.array([p4[0], mid_y, 0])
    else:
        p1 = edge_point(start_obj, "right")
        p4 = edge_point(end_obj, "left")
        mid_x = (p1[0] + p4[0]) / 2
        p2 = np.array([mid_x, p1[1], 0])
        p3 = np.array([mid_x, p4[1], 0])
    line = VMobject(color=color, stroke_width=2.4)
    line.set_points_as_corners([p1, p2, p3, p4])
    tip = ArrowTriangleFilledTip(color=color).scale(0.16)
    tip.move_to(p4)
    tip.rotate(line.get_angle())
    return set_layer(VGroup(line, tip), "arrows")
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

For collision-specific QA, use `check_collision()` with role names so reports can say exactly what failed:

```python
def check_collision(named_mobjects, label="scene"):
    # named_mobjects: [("formula", formula), ("diagram", diagram), ("arrows", arrows)]
    warnings = []
    pairs_to_check = {
        ("formula", "diagram"),
        ("formula", "arrows"),
        ("formula", "title"),
        ("arrows", "labels"),
        ("arrows", "code_panel"),
        ("cta", "subtitle"),
        ("diagram", "subtitle"),
        ("code_panel", "cta"),
    }
    visible = [(name, mob) for name, mob in named_mobjects if mob is not None]
    for i, (name_a, mob_a) in enumerate(visible):
        for name_b, mob_b in visible[i + 1:]:
            if (name_a, name_b) in pairs_to_check or (name_b, name_a) in pairs_to_check:
                if boxes_overlap(mob_a, mob_b):
                    warnings.append(f"{label}: {name_a} collides with {name_b}")
    for warning in warnings:
        print("[collision-warning]", warning)
    return warnings
```

Any collision warning must be copied into `qa_report.md`. A release candidate with formula/diagram/arrow/subtitle/CTA collision is not final; make a `layout_fix` revision first.

## Arrow Routing Rules

Arrows must connect object edges, never centers.

Recommended edge routes:

- Left to right: `start = left_obj.get_right() + RIGHT * 0.08`, `end = right_obj.get_left() + LEFT * 0.08`.
- Top to bottom: `start = top_obj.get_bottom() + DOWN * 0.08`, `end = bottom_obj.get_top() + UP * 0.08`.
- Branch arrows use `make_elbow_arrow()` or a short segmented path.

Forbidden arrow routes:

- `Arrow(left_obj.get_center(), right_obj.get_center())`.
- Arrow paths through `Text`, `MathTex`, CTA, subtitle, or module labels.
- Long arrows spanning multiple layers.
- Arrows sharing the y track of a formula.

If a formula, label, or module blocks the direct route, do one of these:

1. Use `make_elbow_arrow()`.
2. Move the formula back to `formula_layer`.
3. Split the scene into two frames.
4. Reduce the diagram to fewer modules.

## z_index Rules

All objects must be assigned a layer-aware `z_index`:

- background: `0`
- grid / particles: `1`
- arrows / lines: `2`
- boxes / diagrams: `3`
- formula: `4`
- text labels: `5`
- subtitles: `6`
- CTA: `7`

`z_index` controls visual stacking only. It does not make an overlap acceptable. If a label hides an arrow, the arrow path still needs rerouting.

## Formula Auto-Downgrade

If a formula is too long or consumes too much space, use this order:

1. `scale_to_fit_width(config.frame_width * 0.78)`.
2. Split it into two `MathTex` rows and `VGroup(...).arrange(DOWN, buff=0.15)`.
3. Split formula and diagram into two separate frames.
4. Use a short faithful expression such as `Y = Module(X)`.

Never force a long formula into the middle of a graph pipeline.

## Per-Frame Complexity Budget

Each frame may contain at most:

- one title;
- one core formula;
- one main diagram group;
- three main module boxes;
- three main arrows;
- one subtitle;
- no CTA except on CTA pages.

If the page exceeds this budget, split it into multiple frames. Do not solve density by shrinking everything.

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

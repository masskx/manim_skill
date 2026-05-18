# Architecture Figure Rules

Use these rules for white-background paper architecture figures in vertical short videos.

## Principles

- The architecture figure is source material, not the whole video.
- A phone viewer should understand the key module in two seconds.
- Prefer a clean Manim reconstruction when the original figure is dense.

## Rules

1. Do not paste the whole paper figure into the vertical frame.
   - Full figures usually become unreadable at 9:16.
   - If the full figure is needed, show it briefly as context and immediately zoom into the module.

2. Show a simplified module block diagram first.
   - Use 2-4 blocks.
   - Use one primary flow direction.
   - Use consistent colors for input, module, output, and highlight.

3. Then use a local crop of the original figure.
   - Crop the exact module area.
   - Keep the white background clean.
   - Add only a highlight box, arrow, or small number labels.

4. Explain with highlight boxes, arrows, and numbers.
   - Use one highlight box for the plug position.
   - Use one arrow for the data flow.
   - Use at most three numbered callouts.

5. Redraw complex figures as Manim diagrams.
   - If labels are tiny or branches are too dense, reconstruct the structure with clean rectangles and arrows.
   - Preserve the module's actual logic, but simplify visual detail.

6. Avoid decorative overload.
   - Do not add many colorful words on top of a white figure.
   - Do not use stickers, glow text, or unrelated labels.
   - Keep annotations functional and sparse.

## Recommended Sequence

```text
0.5s full context flash -> simplified Manim block -> local crop -> insertion arrow
```

## Material Source Labels

In the storyboard, mark each visual as one of:

- `paper`: directly from the paper text.
- `code`: inferred from module code.
- `architecture figure`: cropped or redrawn from the supplied figure.
- `hand-drawn reconstruction`: simplified Manim redraw based on supplied materials.

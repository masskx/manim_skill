# Plug-in Module QA Checklist

Use this checklist after every render of a deep learning plug-in module short.

## Stream And Duration

- `has_video: True`
- `has_audio: True` when voiceover was requested.
- `has_audio: True` for release candidates with BGM.
- Video duration matches the target range, usually 20-30 seconds.
- Audio duration is close to video duration.
- BGM is mixed into `final_with_bgm.mp4`.
- BGM volume does not cover Chinese voiceover.
- Audio has no abrupt cut at the ending.
- No long frozen tail.
- Final hold is under 1.0-1.5 seconds unless explicitly requested.

## Vertical Layout

- Default canvas is vertical 9:16.
- Top title stays within the title zone and does not touch the edge.
- Core elements stay inside `x = -3.0` to `x = 3.0`.
- Main mechanism stays in the central visual zone.
- Subtitle center is around `y = -3.15`.
- CTA does not go lower than `y = -3.25`.
- No dense text or code is placed near platform UI danger zones.

## Visual Defects

- No red debug boxes.
- No placeholder rectangles or guide boxes.
- No full-screen center cross-axis line.
- No title sticking to the edge.
- No formulas outside the safe width.
- No labels overflowing their borders.
- No arrows passing through text.
- No code panel touching the edge.
- No frame contains multiple competing main visuals.

## Label And Module Boxes

- Labels use a shared `make_label_box()` helper.
- Label boxes are based on `SurroundingRectangle(label, buff=0.16-0.22, corner_radius=0.12)`.
- Text is centered in its box.
- Chinese-English stacked labels are centered as a group.
- Border stroke width is consistent, usually about `2.5`.
- Fixed-width `Rectangle` wrappers are not used for user-facing labels.

## Manim Mechanism Quality

- The video does not feel like a static slide deck.
- There is a clear visual change every 2-3 seconds.
- Formulas use `MathTex`.
- Formula count is limited to 2-4.
- Curves, spectra, tensor flow, gates, residuals, attention maps, or insertion animations are used when relevant.
- The mechanism can be understood without reading a paragraph.

## Code Segment

- Code shows only 3-5 lines.
- No full class definition.
- No long imports.
- The true insertion/call line is highlighted.
- Code is readable in a phone screenshot.
- Voiceover explains the adoption value, such as "复制三行，就能接入".

## Contact Sheet Review

Inspect the contact sheet manually:

- First frame has a hook; no black or empty opening.
- Every sampled frame has one clear main visual.
- Hook, mechanism, code, and CTA are visually distinct.
- Subtitles are not covered by the player-safe area.
- CTA is clear and not frozen too long.

## Release Files

- `renders/preview_no_bgm.mp4` exists.
- `audio/bgm.wav` exists when BGM is used.
- `audio/mixed_audio.wav` exists.
- `renders/final_with_bgm.mp4` exists.
- `renders/contact_sheet.jpg` exists.
- `qa_report.md` records BGM path, volume settings, stream check, duration check, and listening notes.

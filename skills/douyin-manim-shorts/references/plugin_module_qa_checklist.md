# Plug-in Module QA Checklist

Use this checklist after every render of a deep learning plug-in module short.

## Pre-Scene Content Gates

- `mechanism_brief.md` exists before `scene.py`.
- `mechanism_brief.md` answers module name, abbreviation, problem, input tensor, output tensor, internal branches, branch roles, true mechanisms, core formula, best video formula, visual metaphor, previous-episode difference, and forbidden reuse.
- `episode_strategy.md` exists before `scene.py`.
- `episode_strategy.md` records module type judgment, evidence for that judgment, structures not reused from the previous episode, unique narrative, animation spine, core formula, visual metaphor, and differences from the most recent three videos.
- The strategy matches the current paper/code/brief; otherwise QA fails before rendering.
- WMVF_002 is treated as a success case only. Its "decompose -> gate -> fuse -> residual" structure is not reused unless current evidence proves those mechanisms exist.

## Authenticity Verification

Before render, include this table in `qa_report.md` or episode notes:

| Mechanism shown in video | Exists in code/paper | Evidence location | Allowed to show |
|---|---|---|---|
| Gate | Yes/No | Class/function/variable/line or paper section | Yes/No |
| Residual | Yes/No | Evidence | Yes/No |
| Attention | Yes/No | Evidence | Yes/No |
| Frequency | Yes/No | Evidence | Yes/No |
| Wavelet | Yes/No | Evidence | Yes/No |
| Multi-scale | Yes/No | Evidence | Yes/No |
| Expert routing | Yes/No | Evidence | Yes/No |
| Prototype/calibration | Yes/No | Evidence | Yes/No |

- Any mechanism marked `No` for evidence must not appear in formulas, animation, voiceover, subtitles, or code.
- Do not add gate, residual, attention, frequency, wavelet, expert, prototype, or calibration mechanisms for visual convenience.

## Content Consistency

- [ ] Formula comes from the current module, not the previous episode.
- [ ] Animation shows the current module's real computation flow.
- [ ] Voiceover explains the current module, not a generic module template.
- [ ] Subtitles match the voiceover.
- [ ] Visual metaphor fits the current module type.
- [ ] No nonexistent mechanism is drawn into the video.
- [ ] Formula, animation, voiceover, and subtitles all explain the same mechanism.
- [ ] The episode does not use generic "module enhances features" wording in place of a concrete mechanism.

## Stream And Duration

- `has_video: True`
- `has_audio: True` when voiceover was requested.
- `has_audio: True` for release candidates with BGM.
- `voiceover.txt` exists and is not empty.
- `audio/voiceover.wav` exists when voiceover is requested.
- `scene.py` attaches `audio/voiceover.wav` with `add_sound` or an equivalent project audio hook.
- `subtitles.srt` exists and matches the current `voiceover.txt` beats.
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
- Formulas are not rendered by `Text`, including fallback code paths.
- Chinese explanatory text is separate from `MathTex`.
- `MathTex` failures are treated as render blockers, not silently downgraded.
- Formula count is limited to 2-4.
- Curves, spectra, tensor flow, gates, residuals, attention maps, or insertion animations are used when relevant.
- The mechanism can be understood without reading a paragraph.
- For 3b1b-style requests, the video uses mathematical object motion rather than PPT-style box flows.
- Mechanism animation matches `module_type` from the current brief.
- Non-frequency modules do not contain FFT, Low/High, or Frequency Spectrum visuals by default.
- Non-gate modules do not contain a Gate weight bar by default.
- Non-AFDA modules do not contain AFDA text, `self.afda`, or AFDA formulas.
- Current formulas are listed in `qa_report.md` with a one-sentence fit rationale.

## Code Segment

- Code shows only 3-5 lines.
- No full class definition.
- No long imports.
- The true insertion/call line is highlighted.
- Code is readable in a phone screenshot.
- Voiceover explains the adoption value, such as "复制三行，就能接入".
- Code class and variable names match the current module, not the previous episode.

## Contact Sheet Review

Inspect the contact sheet manually:

- First frame has a hook; no black or empty opening.
- Every sampled frame has one clear main visual.
- Hook, mechanism, code, and CTA are visually distinct.
- Subtitles are not covered by the player-safe area.
- CTA is clear and not frozen too long.
- Last 5 seconds: code panel and CTA do not overlap.
- Last 5 seconds: CTA line 1 and line 2 do not overlap.
- Last 5 seconds: subtitle zone and CTA zone do not collide.
- Last 5 seconds: title, formula, MathTex, code, and Text stay inside 85% screen width.

## Layout System QA

Before approving a render, confirm the episode followed the layout pass:

- `layout_draft` was generated or the first preview explicitly served as a static/low-motion layout draft.
- `contact_sheet_check` was generated from the draft or preview.
- Any crowded frame produced a `layout_fix` revision before content or animation was expanded.
- `animation_pass` happened after layout passed.
- `final_render` was created only after layout QA passed.

Inspect every contact-sheet frame for:

- Title is not贴边 / touching the frame edge.
- Formula does not exceed the screen and stays within `frame_width * 0.82` where possible.
- Code panel is readable and not贴边.
- Label text does not overflow its `SurroundingRectangle`.
- Arrows do not cross through text or formula glyphs.
- Modules, symbols, and labels are not crowded together.
- No main visual enters the subtitle zone.
- CTA does not overlap subtitles.
- Final 5 seconds contain no text overlap.
- Each frame has only one main visual focus.

If any item fails, QA fails. Do not output the final version; create a `layout_fix` revision first and regenerate the contact sheet.

## Formula / Diagram / Arrow Layer QA

Every frame with `MathTex`, module diagrams, or arrows must pass this specialized check:

- Formula uses `MathTex` and occupies `formula_layer` by default.
- Diagram objects occupy `diagram_layer`, not the formula track.
- Formula and diagram do not share one y center.
- Formula does not overlap diagram objects.
- Formula is not crossed by arrows or connector lines.
- Arrows stay inside the intended arrow lanes.
- Arrows start and end at object edges, not centers.
- Arrows do not cover module text, labels, `Text`, `MathTex`, code, CTA, or subtitles.
- Arrows do not enter `formula_layer`, `subtitle_layer`, or `cta_layer`.
- Diagram does not enter `formula_layer` or `subtitle_layer`.
- A frame does not contain a long formula plus many modules plus many arrows.
- If the frame is crowded, it has been split into a formula-led frame and a diagram-led frame.

Required layer/collision checks in `qa_report.md`:

| Check | Pass/Fail | Notes |
|---|---|---|
| formula vs diagram |  |  |
| formula vs arrows |  |  |
| arrows vs labels |  |  |
| arrows vs code panel |  |  |
| CTA vs subtitle |  |  |
| diagram vs subtitle |  |  |
| complexity budget |  |  |

If any formula/diagram/arrow collision is visible in the contact sheet, QA fails. Do not output `final_with_bgm.mp4`; create a `layout_fix` version first.

## Complexity Budget

For each frame, verify the content budget:

- [ ] No more than one title.
- [ ] No more than one core formula.
- [ ] No more than one main diagram group.
- [ ] No more than three main module boxes.
- [ ] No more than three main arrows.
- [ ] No more than one subtitle.
- [ ] CTA appears only on CTA pages.

If the budget is exceeded, split the content into multiple frames instead of shrinking or stacking elements.

## Repeat-Template Check

Compare the current episode's `storyboard.md`, `voiceover.txt`, and `scene.py` with the previous episode using a simple text similarity check. If similarity is high, add this QA warning:

```text
疑似套用上一条视频模板，需重写模块机制与口播。
```

Check especially:

- Previous module name residue.
- Previous formulas.
- Wrong CTA keyword.
- Wrong code class.
- Old scene helper names or labels that reveal the previous module.

## Release Files

- `renders/preview_no_bgm.mp4` exists.
- `audio/bgm.wav` exists when BGM is used.
- `audio/mixed_audio.wav` exists.
- `renders/final_with_bgm.mp4` exists.
- `renders/contact_sheet.jpg` exists.
- `qa_report.md` records BGM path, volume settings, stream check, duration check, and listening notes.

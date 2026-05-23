# Common Failures

Use this file as a failure memory for future deep learning plug-in module episodes.

## WMVF_002 Formula And Voiceover Failure

Symptoms:

- Formula helper tried `MathTex`, caught the exception, then rendered the formula with `Text`.
- Unicode math symbols such as `⊙` rendered as square glyphs in the final video.
- Chinese explanation and formula-like strings appeared too close together, making the scene look like a dark PPT flowchart.
- The video had `voiceover.txt` but no `audio/voiceover.wav`.
- `scene.py` did not attach voiceover audio with `add_sound`.
- Final MP4 audio was BGM-only or generic audio-track pass, not verified spoken narration.

Rules learned:

- Never use `Text` for formulas.
- Never silently fall back from `MathTex` to `Text`; stop and fix LaTeX/MiKTeX.
- Keep Chinese explanation in separate `Text` objects.
- 3b1b-style videos should be derivations with transforms, braces, arrows, and changing mathematical objects, not PPT flowcharts.
- Every voiced episode must generate `voiceover.wav`, attach it in `scene.py`, and verify the final MP4 audio stream.
- Missing `DASHSCOPE_API_KEY` is a hard stop before TTS; do not pretend the episode is voiced.

## WMVF_002 Success Case Is Not A Template

What made the repaired WMVF_002 better:

- Formulas were rendered with `MathTex`, while Chinese explanation used separate `Text` objects.
- The scene stopped using formula-looking plain text, which removed square-glyph garbling.
- The visual style moved away from dense PPT boxes and toward 3Blue1Brown-style mathematical objects, transforms, arrows, braces, and formula evolution.
- The animation focused on the verified WMVF mechanism: decomposition, gate-controlled high-frequency compensation, fusion, and residual return to the main path.
- Voiceover, subtitles, formulas, and animation all explained the same mechanism.
- `voiceover.txt` was generated, Bailian TTS produced `audio/voiceover.wav`, `scene.py` attached it, and the final video audio stream was checked.
- Subtitles matched the voiceover and stayed away from the formula/CTA zones.

Do not turn the WMVF structure into a general template. The "decompose -> gate -> fuse -> residual" story is only allowed when the current module truly contains decomposition, gate, fusion, and residual mechanisms with code or paper evidence.

Future episodes must copy the successful discipline, not the content:

- Start from current materials.
- Write `mechanism_brief.md`.
- Write `episode_strategy.md`.
- Prove every mechanism with code or paper evidence.
- Bind formula, animation, voiceover, and subtitles to the same current mechanism.
- Use MathTex/Text/TTS/render QA rules consistently.

## SHSA_003 Layout Crowding And Stale Symbol Failure

Symptoms:

- Formula, symbols, arrows, and feature bundles were technically aligned but still visually crowded in the same vertical lane.
- A branch/bypass symbol remained visible after its explanatory beat and leaked into later frames.
- Contact-sheet thumbnails made one formula/text frame look like possible garbled text even though the full-resolution frame was readable.
- The first rebuilt render had voiceover audio slightly longer than the visible video stream, creating risk of audio continuing after the scene.
- The template `make_elbow_arrow()` example used `line.get_angle()`, which can fail for ManimCE `VMobject` segmented paths.

Rules learned:

- Formula-led and diagram-led beats must be split whenever a long formula and a multi-object diagram compete for the same space.
- Each beat must own and clear its temporary mobjects. Old labels, arrows, braces, matrices, and helper symbols may not survive into unrelated beats or the final CTA.
- Contact-sheet suspicion is not enough; extract a full-resolution frame at the suspicious timestamp and record the result in QA.
- The final video stream must cover the full voiceover duration. Extend visible motion or CTA hold rather than letting audio outlast video.
- For segmented elbow arrows, rotate arrow tips from the last segment vector, for example `angle_of_vector(p4 - p3)`, not `line.get_angle()`.

Do not turn SHSA_003 into a universal attention template. Its channel split, partial-channel single-head attention, identity bypass, and concat projection are case-specific. Future videos should reuse the layered-layout discipline, not SHSA's mechanism.

## Pure Manim Global Layout Failure Case

Symptoms:

- Formula, mechanism graphics, arrows, subtitles, code, and CTA all competed for the same 9:16 canvas.
- Fixing one frame often broke another frame because global layout was embedded inside Manim scene coordinates.
- Subtitle and CTA positioning became fragile in the final seconds.
- Code cards and titles were difficult to keep visually consistent across different modules.
- Batch production drifted because every episode reimplemented title, subtitle, CTA, and code layout manually.

Rules learned:

- Do not make pure Manim responsible for the whole short-video composition when the episode needs subtitles, CTA, code cards, BGM, and multi-beat editing.
- Use Manim for clean 3-8 second formula/mechanism clips.
- Use Remotion for global 9:16 layout, titles, subtitles, code cards, CTA, BGM, transitions, and final export.
- New deep learning plug-in module shorts should default to Hybrid Manim + Remotion mode.
- Keep old pure-Manim episodes as case studies; do not force them into a new structure unless the user asks for a remake.

## SEFN_004 First Preview Pacing And Component Crowding

Symptoms:

- The first spoken sentence was accurate but soft: it did not immediately state a sharp module-specific pain point.
- The video stretched to about 36 seconds because the script had too many spoken lines for a Douyin preview.
- Several mechanism frames kept too many boxes visible at once, making the plug-in components feel like they were competing with the title, formula, and subtitle zones.
- Contact-sheet thumbnails showed labels and arrows close enough that the whole screen felt busy even when full-resolution text was readable.

Rules learned:

- The first sentence must be a content-specific retention hook, not a neutral setup.
- For first preview videos, target 20-24 seconds unless the user explicitly asks for a slower explanation.
- Cut narration before stretching animation waits. A short video should not become long just because TTS is slow.
- Use progressive replacement: show `spatial branch`, compress it to `S`, then show `x1/x2` and the gate. Do not show all SEFN internals as one graph.
- Avoid placing long formulas on the same frame as the full mechanism graph. Either show the formula alone or use a short formula chip.
- Add overlap checks as visual judgment, not just code warnings: if the contact sheet looks crowded, the frame is crowded.

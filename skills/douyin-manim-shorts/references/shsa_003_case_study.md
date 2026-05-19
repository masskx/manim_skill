# SHSA_003 Case Study

Use this as a case study, not as a reusable content template.

## Episode

- Episode: `SHSA_003`
- Module type: attention / partial-channel single-head self-attention
- Successful content spine: current-material evidence -> channel split -> attention on one channel group -> identity bypass for remaining channels -> concat/projection -> minimal integration code.

## What Worked

- The episode did not reuse AFDA or WMVF formulas, animation order, or visual metaphor.
- `mechanism_brief.md`, `episode_strategy.md`, and authenticity checks kept the video bound to the current module.
- Math formulas were rendered with `MathTex`; Chinese captions used separate `Text`.
- Layered Layout separated formulas, diagrams, arrows, subtitles, and CTA.
- Dense ideas were split into formula-led and diagram-led beats instead of packed into one frame.
- The final code/CTA page cleared mechanism-only objects first.
- The voiceover was attached in `scene.py`, BGM was mixed afterward, and stream durations were checked.

## What Failed During Iteration

- Early frames put formula and symbols too close to feature bundles.
- Some arrows and Q/K/V labels competed with the attention matrix.
- A bypass symbol stayed visible after its beat and needed explicit cleanup.
- The contact sheet downscaled one readable frame enough to look suspicious; a full-resolution frame check resolved it.
- The first rendered video stream was slightly shorter than the voiceover; an intentional visible CTA hold fixed the tail.
- The generic template's elbow-arrow tip rotation used `line.get_angle()`, which failed under ManimCE for a segmented `VMobject`.

## Reusable Rules Extracted

- Enforce page lifecycle: clear or transform beat-local objects before moving on.
- Treat contact sheets as screening tools; inspect full-resolution frames for any suspicious thumbnail.
- Ensure the video stream covers the voiceover duration before final mix.
- Use edge-connected or elbow-routed arrows; rotate segmented-arrow tips with the final segment vector.
- Split complex frames into formula-led and diagram-led beats.

## Not Reusable As A Template

- Do not reuse SHSA's channel split as a default opening.
- Do not reuse partial-channel attention unless the current code proves it.
- Do not reuse identity bypass or concat projection unless the current module really has them.
- Do not use SHSA variable names, formulas, CTA keyword, or Q/K/V visuals for non-attention modules.

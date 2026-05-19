# Skill Evolution

Append-only log for `douyin-manim-shorts` refinements after real episode work.

## 2026-05-19 - SHSA_003

Episode: `episodes/SHSA_003`

Problems found:

- Formula, symbols, arrows, and feature bundles could still crowd together even after basic zone alignment.
- Temporary branch/bypass labels could persist into unrelated later beats.
- Contact-sheet thumbnails could make readable full-resolution text look like possible garbled text.
- A rendered video stream can be slightly shorter than the voiceover unless explicitly checked.
- The generic segmented-arrow helper used `line.get_angle()`, which can fail in ManimCE.

Rules added:

- Each beat must own and clear its temporary objects before the next page or final CTA.
- Suspicious contact-sheet frames require full-resolution extraction and QA notes.
- Video stream duration must cover the full voiceover duration.
- Formula-led and diagram-led beats should be split when formula, diagram, and arrows cannot coexist clearly.
- Segmented arrow tips should be rotated with `angle_of_vector(p4 - p3)`.

Templates changed:

- `templates/vertical_scene.py`: fixed `make_elbow_arrow()` tip rotation and added `clear_page()`.

Scripts changed:

- None. The issues were better handled by layout/template/QA rules.

Still to improve:

- A future script could parse render logs for `[layout-warning]` and `[collision-warning]` and copy them into `qa_report.md`.
- A future script could automatically compare video/audio stream durations and fail when audio exceeds video by more than the threshold.

QA status:

- Passed for SHSA_003 after layered-layout rebuild, contact-sheet inspection, full-resolution frame check, stream check, freeze check, and template-residue search.


## 2026-05-19 - Hybrid Manim + Remotion Workflow Upgrade

This is the largest structural upgrade since the skill was created.

Changes made:
- Added Hybrid Manim + Remotion Mode as the recommended workflow for plug-in module shorts.
- Defined strict responsibility boundaries between Manim (formula/mechanism clips) and Remotion (layout/compositing).
- Added Remotion layout specification with 5 fixed zones (titleArea, visualArea, infoArea, subtitleArea, ctaArea).
- Added data.json specification for data-driven Remotion composition.
- Added 7 Remotion component templates.
- Added references/hybrid_workflow.md with detailed step-by-step guide.
- Added 13-step Hybrid Generation Flow to SKILL.md.
- Added Hybrid QA checks to SKILL.md and plugin_module_qa_checklist.md.
- Added Hybrid prompt commands to plugin_module_prompt_commands.md.
- Added Migration Strategy.
- Added Hybrid-specific anti-patterns.
- Cleaned the Hybrid documentation and templates so future episodes can keep Manim clips local and Remotion composition data-driven.

Total new files: 9 (remotion components + hybrid_workflow.md)

Files modified: 6 (SKILL.md, layout_system.md, prompt_commands.md, qa_checklist.md, skill_evolution.md, remotion templates)

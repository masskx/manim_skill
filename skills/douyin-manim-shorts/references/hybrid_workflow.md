# Hybrid Manim + Remotion Workflow Guide

This file documents the detailed hybrid workflow for producing deep learning plug-in module shorts.
It is a companion to the main `SKILL.md` Hybrid section and provides concrete implementation steps.

## Overview

The hybrid workflow produces 20-30 second vertical shorts by combining:

- **Manim** -- generates 1-3 clean mechanism/Formula clips (no subtitles, no CTA, no BGM).
- **Remotion** -- composes the final video from data.json, Manim clips, voiceover, subtitles, code cards, CTA, and BGM.

Recommended episode layout:

```text
episodes/{module_slug}_{index}/
├── brief.md
├── storyboard.md
├── voiceover.txt
├── subtitles.srt
├── manim/
│   ├── scene.py
│   └── renders/
│       ├── formula_clip.mp4
│       ├── mechanism_clip.mp4
│       └── visual_clip.mp4
├── remotion/
│   ├── data.json
│   ├── composition.tsx
│   └── components/
│       ├── Layout.tsx
│       ├── TitleBlock.tsx
│       ├── SubtitleBlock.tsx
│       ├── CodeCard.tsx
│       ├── CTA.tsx
│       ├── ManimClip.tsx
│       └── Background.tsx
├── audio/
│   ├── voiceover.wav
│   ├── bgm.wav
│   └── mixed_audio.wav
├── renders/
│   ├── preview.mp4
│   ├── final_with_bgm.mp4
│   └── contact_sheet.jpg
└── qa_report.md
```

## Phase 1: Pre-Production

1. Read `brief.md` or `plugin_module_brief.yaml`.
2. Run the standard authenticity gate (mechanism_brief.md, episode_strategy.md).
3. Generate `storyboard.md` with hybrid timeline annotations.
   - Mark which beats are Manim clips vs. Remotion overlays.
   - Mark Manim clip start/end timestamps.
4. Generate `voiceover.txt` (one short line per sentence).
5. Generate `subtitles.srt`.

## Phase 2: Manim Clip Production

For each mechanism beat in the storyboard, create a Manim scene that produces a clean clip.

### Scene Design Rules

- Each scene focuses on exactly one mechanism.
- No global title -- at most one local label per clip.
- No subtitles in Manim output.
- No CTA in Manim output.
- No BGM.
- Background: solid dark color (`#0a0a1a`), or transparent with `-t` flag.
- Clip duration: 3-8 seconds each.
- Use ManimCE standard config (1080x1920, 9:16).
- If a formula and diagram do not fit, split into two clips.

### Clip Naming Convention

| Clip Name | Purpose |
|---|---|
| `hook_clip.mp4` | Hook visual (0-3s beat) |
| `mechanism_clip.mp4` | Core mechanism animation (7-15s beat) |
| `formula_clip.mp4` | Formula-centric animation |
| `visual_clip.mp4` | Generic mechanism/process animation |

### Output Path

All clips go to `manim/renders/{clip_name}.mp4`.

### Render Command

```bash
manim -pql manim/scene.py SceneName
manim -pqh manim/scene.py SceneName  # for final quality
```

If transparent background is needed:

```bash
manim -pqh -t manim/scene.py SceneName
```

## Phase 3: Remotion Composition

### data.json Generation

Generate `remotion/data.json` from the brief and clip inventory.

Required fields:

```json
{
  "moduleName": "...",
  "moduleType": "...",
  "title": "...",
  "hook": ["line1", "line2"],
  "clips": [
    {"type": "manim", "path": "../manim/renders/clip.mp4", "start": 6, "duration": 8}
  ],
  "code": ["line1", "line2", "line3"],
  "highlightLine": 3,
  "cta": {"line1": "...", "line2": "..."},
  "bgmStyle": "tech_fast",
  "subtitleLines": [
    {"start": 0.0, "end": 3.0, "text": "..."},
    {"start": 3.0, "end": 7.0, "text": "..."}
  ],
  "totalDuration": 26
}
```

### Remotion Project Structure

```
remotion/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── src/
│   ├── index.ts
│   ├── Root.tsx
│   ├── composition.tsx
│   ├── data.json
│   └── components/
│       ├── Layout.tsx
│       ├── TitleBlock.tsx
│       ├── SubtitleBlock.tsx
│       ├── ManimClip.tsx
│       ├── CodeCard.tsx
│       ├── CTA.tsx
│       └── Background.tsx
```

### Render Command

```bash
cd remotion
npx remotion render src/index.ts ModuleComposition renders/preview.mp4
```

### Audio Mixing

After Remotion renders the preview:

1. Place voiceover at `audio/voiceover.wav`.
2. Select BGM by `bgmStyle` from `index/bgm_registry.csv`.
3. Run `scripts/mix_audio.py` to produce `renders/final_with_bgm.mp4`.

## Phase 4: QA

Run the hybrid QA checklist from the main SKILL.md and plugin_module_qa_checklist.md.

### Manim Clip QA

- [ ] Clip contains only mechanism animation -- no subtitles, no CTA, no global title.
- [ ] No complex stacking in Manim output.
- [ ] No formula overflow beyond safe zone.
- [ ] Clip duration 3-8 seconds.
- [ ] Background is clean (dark/transparent).
- [ ] Only one mechanism per clip.

### Remotion Final QA

- [ ] Title is inside `titleArea`.
- [ ] Manim clip is inside `visualArea`.
- [ ] Subtitles are inside `subtitleArea`.
- [ ] CTA is inside `ctaArea`.
- [ ] Code card is readable (font size, contrast).
- [ ] Subtitle and CTA do not overlap.
- [ ] BGM exists and voiceover is not masked.
- [ ] `final_with_bgm.mp4` has video and audio streams.
- [ ] `data.json` drives all content; no hardcoded module text in Remotion components.
- [ ] Contact sheet shows clean frames for each beat.

## Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| Manim clip too long | Complex single scene | Split into 2 clips |
| Remotion missing clip | Wrong path in data.json | Check `clips[].path` is relative to remotion/ |
| Subtitle/CTA overlap | Wrong zone assignment | Check subtitleArea vs ctaArea coordinates |
| Remotion render fails | Missing dependency | Run `npm install` in remotion/ |
| Audio out of sync | FPS mismatch | Ensure Remotion fps=30 matches Manim |
| data.json not loaded | File not in src/ | Place data.json inside remotion/src/ |

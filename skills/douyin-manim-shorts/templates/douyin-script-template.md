# [Video Title]

## Concept Lock

After watching, the viewer should remember: [one concrete insight].

## Audience

- Target viewer: [ordinary Douyin viewer / high school student / college student / AI beginner]
- Assumed knowledge: [none / algebra / calculus / Python / ML basics]
- Tone: [direct / curious / playful / exam-focused / professional]

## Packaging

- Title option 1:
- Title option 2:
- Title option 3:
- Cover text: [6-14 Chinese characters, large and direct]
- Comment prompt:

## Timing

- Soft duration range: [for example 20-35s / 35-70s / 70-120s]
- Estimated natural duration: [based on voiceover and visual beats]
- Format: vertical 9:16
- Main visual metaphor:
- Final hold: [0.6-1.5s, do not pad to a round number]

## Hook: 0-3s

Voiceover:

```text
[one sentence that creates curiosity or contradiction]
```

On-screen text:

```text
[short title or challenge]
```

Visual:

- [Large title or surprising visual state]
- [One moving object that creates tension]

## Beat Sheet

| Time | Visual | Voiceover | Subtitle |
|---|---|---|---|
| 0-3s |  |  |  |
| 3-10s |  |  |  |
| 10-20s |  |  |  |
| [natural] |  |  |  |
| [natural] |  |  |  |

## Spoken Script

```text
[Line 1]
[Line 2]
[Line 3]
```

## Voiceover File

Save the final narration as `voiceover.txt`. Record or generate audio from it as:

```text
audio/voiceover.wav
```

If no audio file exists, the Manim render will be silent.

## Alibaba TTS Package

Use this section when using Alibaba Cloud / DashScope / Bailian / CosyVoice.

- Recommended platform:
- Model:
- Voice:
- Format:
- Sample rate:
- Speed/rate:
- Export path: `audio/voiceover.wav`

Create `voiceover_lines.csv` if using per-line synthesis:

```csv
index,start_hint,text,note
1,00:00,"[short narration line]","hook"
2,00:03,"[short narration line]","example"
```

## Subtitle Track

Keep each line short enough for a phone screen.

```text
00:00 [subtitle]
00:03 [subtitle]
00:07 [subtitle]
```

## Manim Scene Plan

- Scene class:
- Visual style:
  - Font family:
  - Text hierarchy: title / body / micro-label
  - Accent color meaning:
  - Background:
- Main mobjects:
- Layout zones:
  - Top title zone:
  - Main visual zone:
  - Formula/detail zone:
  - Subtitle zone:
- Key transformations:
- Accent color:
- Formula count:
- Formula implementation: `MathTex` for math, `Text` for Chinese labels
- Audio implementation: `self.add_sound("audio/voiceover.wav")` if the file exists
- Alibaba TTS handoff: `voiceover.txt` + optional `voiceover_lines.csv`
- Render command:
- QA commands:
  - Contact sheet:
  - Freeze-tail check:
  - Stream check:

## QA Checklist

- [ ] Hook lands in the first 3 seconds.
- [ ] One video, one insight.
- [ ] Duration follows the content; no static padding to hit exactly 30 seconds.
- [ ] Subtitle lines are short.
- [ ] Text uses a controlled 3-level hierarchy, not random sizes.
- [ ] Title/body/label contrast feels intentional on a phone screen.
- [ ] One dominant focus appears on screen at a time.
- [ ] Repeated chips, labels, captions, and formulas share a consistent style.
- [ ] Text avoids top/bottom/right UI danger zones.
- [ ] Rendered frames show no overlap between title, subtitles, formulas, labels, arrows, or diagrams.
- [ ] Key visual changes every 2-5 seconds.
- [ ] Final hold is short and intentional.
- [ ] No long frozen tail in the final 5-8 seconds.
- [ ] Formula density is low.
- [ ] Formulas use `MathTex`, not plain `Text`.
- [ ] Voiceover is saved or the silent-video status is explicit.
- [ ] Alibaba TTS text is split into natural short lines if Alibaba is used.
- [ ] Final MP4 audio stream is checked when audio is requested.
- [ ] Ending has a takeaway or comment prompt.

## BGM Package

- bgm_style: [tech_fast / soft_future / intense_hook / cute_light / clean_academic]
- bgm_auto_select: true
- bgm_path:
- bgm_volume: 0.15
- voiceover_volume: 1.0
- sfx_volume: 0.25
- music_mood:
- music_energy:
- preview_no_bgm: `renders/preview_no_bgm.mp4`
- final_with_bgm: `renders/final_with_bgm.mp4`

## Plug-in Module Extra QA

- [ ] Standard structure is pain point -> problem visualization -> mechanism -> code -> CTA.
- [ ] Mechanism uses Manim strengths, not only static boxes.
- [ ] Module labels use auto-fit `SurroundingRectangle` boxes.
- [ ] No red debug boxes or guide rectangles appear.
- [ ] No full-screen center cross-axis background appears.
- [ ] Subtitle stays above the player-safe bottom area.
- [ ] Arrows point to module edges and do not cross label text.
- [ ] Code is 3-5 lines and the inserted line is highlighted.
- [ ] CTA clearly offers PDF notes, PyTorch code, architecture figure, or a resource pack.
- [ ] `preview_no_bgm.mp4` and `final_with_bgm.mp4` both exist for release candidates.
- [ ] BGM is selected from `index/bgm_registry.csv` or explicitly specified.
- [ ] BGM does not overpower Chinese voiceover.
- [ ] Mixed audio duration matches video duration.

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

## Subtitle Track

Keep each line short enough for a phone screen.

```text
00:00 [subtitle]
00:03 [subtitle]
00:07 [subtitle]
```

## Manim Scene Plan

- Scene class:
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
- [ ] Text avoids top/bottom/right UI danger zones.
- [ ] Rendered frames show no overlap between title, subtitles, formulas, labels, arrows, or diagrams.
- [ ] Key visual changes every 2-5 seconds.
- [ ] Final hold is short and intentional.
- [ ] No long frozen tail in the final 5-8 seconds.
- [ ] Formula density is low.
- [ ] Formulas use `MathTex`, not plain `Text`.
- [ ] Voiceover is saved or the silent-video status is explicit.
- [ ] Final MP4 audio stream is checked when audio is requested.
- [ ] Ending has a takeaway or comment prompt.

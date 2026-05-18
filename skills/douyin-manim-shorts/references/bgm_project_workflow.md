# BGM And Episode Project Workflow

Use this reference for project management, background music selection, final audio mixing, and release-ready outputs.

## Standard Episode Directory

Each batch-produced video should live in:

```text
episodes/{module_slug}_{index}/
├─ brief.md
├─ storyboard.md
├─ voiceover.txt
├─ subtitles.srt
├─ scene.py
├─ audio/
│  ├─ voiceover.wav
│  ├─ bgm.wav
│  └─ mixed_audio.wav
├─ renders/
│  ├─ preview_no_bgm.mp4
│  ├─ final_with_bgm.mp4
│  └─ contact_sheet.jpg
└─ qa_report.md
```

Do not delete source renders. Copy the selected no-BGM render into `renders/preview_no_bgm.mp4`, then create `renders/final_with_bgm.mp4`.

## Shared BGM Library

Do not rely on scattered local music folders for production. Import music into:

```text
shared_assets/
└─ bgm_library/
   ├─ tech_fast/
   ├─ soft_future/
   ├─ intense_hook/
   ├─ cute_light/
   └─ clean_academic/
```

File naming:

```text
{style}_{bpm}bpm_loop_{index}.wav
```

If BPM is unknown:

```text
tech_fast_unknownbpm_loop_01.wav
```

Avoid vague names such as `bgm1.wav`, `music.mp3`, `new_audio.wav`, or unnamed exports.

## BGM Registry

Every imported BGM should be registered in:

```text
index/bgm_registry.csv
```

Required columns:

```csv
filename,path,style,bpm,duration,loopable,mood,energy,license_note,recommended_use,used_count,notes
```

Rules:

- `path` is project-relative.
- `bpm` can be `unknown` when not detected.
- `duration` should come from `ffprobe` when possible.
- `license_note` should be `AI-generated`, `user-provided`, or a specific license note.
- `recommended_use` should say where the track works, such as `deep learning module short videos`.
- Increment `used_count` when a track is selected for an episode.

Use the helper script to refresh duration metadata and preserve existing `used_count` values:

```powershell
$env:PYTHONUTF8='1'
& 'D:\Program Files\miniconda\python.exe' scripts\register_bgm.py `
  --library shared_assets\bgm_library `
  --registry index\bgm_registry.csv
```

## Brief BGM Fields

Add these fields to `brief.md` or the episode brief:

```yaml
bgm_style: tech_fast
bgm_auto_select: true
bgm_path:
bgm_volume: 0.15
voiceover_volume: 1.0
sfx_volume: 0.25
music_mood:
music_energy:
```

Default rules:

- If `bgm_path` exists, use the specified music.
- If `bgm_auto_select: true`, choose from `index/bgm_registry.csv` by `bgm_style`.
- Prefer tracks with matching `recommended_use`, reasonable `energy`, and lower `used_count`.
- If no matching music exists, write an AI music prompt into `qa_report.md` and ask the user to generate or provide BGM.
- Do not use style-mismatched music just because a file exists.

## Automatic BGM Selection

For deep learning plug-in module shorts:

- Default `bgm_style`: `tech_fast`.
- Good moods: modern tech, clean electronic, light futuristic, professional, sharp.
- Avoid vocals, lyrics, heavy drops, cinematic orchestra, and dramatic tension.
- BGM should leave space for Chinese voiceover.
- Default BGM volume: `0.12-0.18`; use `0.15` unless a manual mix suggests otherwise.
- Keep voiceover at `1.0` by default.

## Mixing Script

Use the project script:

```powershell
$env:PYTHONUTF8='1'
& 'D:\Program Files\miniconda\python.exe' scripts\mix_audio.py `
  --video episodes\afda_001\renders\preview_no_bgm.mp4 `
  --bgm episodes\afda_001\audio\bgm.wav `
  --out episodes\afda_001\renders\final_with_bgm.mp4 `
  --mixed-audio episodes\afda_001\audio\mixed_audio.wav `
  --bgm-volume 0.15 `
  --voiceover-volume 1.0 `
  --meta episodes\afda_001\audio\mix_meta.json
```

The script:

- Detects video duration.
- Detects BGM duration.
- Loops BGM when it is shorter than the video.
- Trims BGM when it is longer than the video.
- Keeps voiceover or existing video audio as the primary source.
- Writes `mixed_audio.wav`.
- Muxes `final_with_bgm.mp4`.
- Verifies the output has audio.

For a lightweight ffprobe QA report, use:

```powershell
$env:PYTHONUTF8='1'
& 'D:\Program Files\miniconda\python.exe' scripts\qa_video.py `
  episodes\afda_001\renders\final_with_bgm.mp4 `
  --out episodes\afda_001\qa_report.md `
  --bgm-path episodes\afda_001\audio\bgm.wav `
  --voiceover-path episodes\afda_001\audio\voiceover.wav
```

## QA Requirements

Every release candidate must check:

- `has_video: True`
- `has_audio: True`
- BGM is present.
- BGM does not cover Chinese voiceover.
- Audio duration matches video duration.
- No abrupt audio cut.
- No tail black screen.
- No tail freeze.
- `preview_no_bgm.mp4` and `final_with_bgm.mp4` both exist.
- `contact_sheet.jpg` exists.
- `qa_report.md` records the selected BGM and mix settings.

## AI Music Generation Prompt

English:

```text
Create a 25-second seamless loop background music for a vertical short video about deep learning modules and AI research.

Style: modern tech, clean electronic, light futuristic, energetic but not aggressive.
Tempo: 125-135 BPM.
Mood: professional, sharp, catchy, suitable for Douyin/TikTok educational content.
Instrumentation: soft synth plucks, light digital arpeggios, subtle bass, crisp hi-hats, gentle kick.
No vocals, no lyrics, no heavy drop, no cinematic orchestra, no dramatic tension.
The music should leave space for Chinese voiceover and not overpower speech.
Make it loopable, with a strong first 2-second hook and stable rhythm afterwards.
Duration: 25 seconds.
```

Chinese:

```text
生成一段 25 秒左右的短视频背景音乐，用于深度学习模块/AI 科研科普类竖屏视频。

风格：现代科技感、轻电子、未来感、干净、节奏清晰。
速度：125-135 BPM。
情绪：专业、利落、有吸引力，但不要吵。
乐器：柔和合成器、轻微电子琶音、克制低音、清脆 hi-hat、轻鼓点。
要求：无人声、无歌词、不要重低音轰炸、不要史诗感、不要影视配乐感。
音乐需要给中文口播留出空间，不能盖住人声。
前 2 秒要有轻微抓耳的节奏钩子，后面保持稳定律动。
适合循环播放。
时长：25 秒。
```

## New Module Production Workflow

1. Create `episodes/{module_slug}_{index}/`.
2. Fill `brief.md`, including BGM fields.
3. Generate `storyboard.md`.
4. Generate `voiceover.txt`.
5. Run TTS to create `audio/voiceover.wav`.
6. Generate `subtitles.srt`.
7. Render Manim visuals as `renders/preview_no_bgm.mp4`.
8. Select BGM from `index/bgm_registry.csv` by `bgm_style`.
9. Copy selected music to `audio/bgm.wav`.
10. Mix audio and output `renders/final_with_bgm.mp4`.
11. Generate `renders/contact_sheet.jpg`.
12. Generate `qa_report.md`.
13. Publish only after QA passes.

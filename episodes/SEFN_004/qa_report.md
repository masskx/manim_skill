# SEFN_004 QA Report

## Output

- preview_no_bgm: `episodes/SEFN_004/renders/preview_no_bgm.mp4`
- final_with_bgm: `episodes/SEFN_004/renders/final_with_bgm.mp4`
- contact_sheet: `episodes/SEFN_004/renders/contact_sheet.jpg`
- voiceover: `episodes/SEFN_004/audio/voiceover.wav`
- bgm: `episodes/SEFN_004/audio/bgm.wav`

## Content Consistency

- Module: SEFN / Spatially-Enhanced Feedforward Network.
- Source paper: `SEM-Net: Efficient Pixel Modelling for image inpainting with Spatially Enhanced SSM`.
- Source code: `materials/SEFN(CV,WACV2025).py`.
- Video mechanism matches the provided code:
  - `spatial -> avg_pool -> conv -> upsample`.
  - `project_in(x) -> dwconv -> chunk(x1, x2)`.
  - `cat(x1, y) -> fusion -> dwconv_afterfusion`.
  - `F.gelu(x1) * x2 -> project_out`.
- The video explicitly avoids unsupported mechanisms:
  - No attention/QKV claim.
  - No frequency or wavelet decomposition claim.
  - No residual-add claim inside SEFN.

## Render Check

- Final video duration: about `24.27s`.
- Resolution: `1080x1920`.
- Video codec: `h264`.
- Audio codec: `aac`.
- Audio sample rate: `48000 Hz`.
- Audio channels: stereo.
- Final video contains both video and audio streams.
- BGM volume: `0.12`.
- Voiceover source: Manim-rendered video audio, mixed with BGM.

## Visual QA

- Contact sheet reviewed after fast revision: mechanism pages are less crowded, with staged replacement instead of one full SEFN graph.
- Subtitle band stays at the bottom and does not overlap the CTA.
- First spoken sentence is now a module-specific hook: `Mamba 看得远，但会丢局部。`
- The video no longer uses a long formula page; the gate is shown visually as `S + x1 -> Fuse -> GELU -> x2 -> Y`.
- Ambient moving wave remains under the scene to avoid fully static lecture holds.

## Commands Used

TTS:

```powershell
$env:PYTHONUTF8='1'
Get-Content .env | ForEach-Object { if ($_ -match '^DASHSCOPE_API_KEY=(.+)$') { $env:DASHSCOPE_API_KEY=$Matches[1] } }
& 'D:\Program Files\miniconda\python.exe' scripts\bailian_tts.py --text episodes\SEFN_004\voiceover.txt --out episodes\SEFN_004\audio\voiceover.wav --meta episodes\SEFN_004\audio\voiceover_meta.json --model cosyvoice-v3-flash --voice longxiaochun_v3 --speed 1.30
```

Render:

```powershell
$env:PYTHONUTF8='1'
manim -ql episodes\SEFN_004\scene.py SEFNModuleShort --media_dir episodes\SEFN_004\manim_media
```

Mix:

```powershell
$env:PYTHONUTF8='1'
& 'D:\Program Files\miniconda\python.exe' scripts\mix_audio.py --video episodes\SEFN_004\renders\preview_no_bgm.mp4 --bgm episodes\SEFN_004\audio\bgm.wav --out episodes\SEFN_004\renders\final_with_bgm.mp4 --mixed-audio episodes\SEFN_004\audio\mixed_audio.wav --preview-no-bgm episodes\SEFN_004\renders\preview_no_bgm.mp4 --bgm-volume 0.12 --voiceover-volume 1.0 --meta episodes\SEFN_004\audio\mix_meta.json
```

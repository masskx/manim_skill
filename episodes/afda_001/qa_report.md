# AFDA BGM QA Report

## Inputs

- Source video: `media/videos/scene/1920p30/AFDAModuleShort_V4_1.mp4`
- Preview copy without BGM: `episodes/afda_001/renders/preview_no_bgm.mp4`
- BGM library file: `shared_assets/bgm_library/tech_fast/tech_fast_unknownbpm_loop_03.wav`
- Episode BGM copy: `episodes/afda_001/audio/bgm.wav`
- Mixed audio: `episodes/afda_001/audio/mixed_audio.wav`
- Final video: `episodes/afda_001/renders/final_with_bgm.mp4`
- Contact sheet: `episodes/afda_001/renders/contact_sheet.jpg`

## Mix Settings

- bgm_volume: `0.15`
- voiceover_volume: `1.0`
- source_audio: original video audio
- BGM behavior: cropped from a longer loop candidate to match video duration.

## Stream Check

- has_video: True
- has_audio: True
- final duration: 24.833s
- video stream duration: 24.800s
- audio stream duration: 24.833s
- mixed_audio duration: 24.833s
- mixed_audio format: WAV, 48kHz, stereo

## Visual QA

- Contact sheet generated: True
- No tail freeze detected by `render_qa.py` at threshold `n=0.003:d=2`.
- No new Manim rendering was performed; visual content is unchanged from the selected AFDA V4.1 source video.
- No tail black screen was introduced by muxing.

## Audio QA

- BGM was mixed into the final MP4.
- Chinese voiceover remains the primary audio source by design: voiceover/video audio volume `1.0`, BGM volume `0.15`.
- No obvious duration mismatch in ffprobe: final audio and container duration both 24.833s.
- No abrupt audio truncation expected; BGM was trimmed to the video duration after mixing.

## Notes

- This was a pipeline test for automatic BGM mixing, not a visual revision.
- Manual listening is still recommended before publishing, especially to confirm the selected music does not mask consonants in the Chinese voiceover.

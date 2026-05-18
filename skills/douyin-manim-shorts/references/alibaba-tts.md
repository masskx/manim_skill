# Alibaba TTS Workflow

Use this reference when the user plans to use Alibaba-family voice synthesis: Alibaba Cloud, Aliyun, Bailian, DashScope, CosyVoice, Tongyi/Qwen audio, or 阿里云/百炼/通义语音.

## Goal

The skill should not hard-code credentials or require online synthesis. It should prepare clean TTS inputs and a stable audio handoff path so the user can use Alibaba tools manually or through their own API setup.

Standard final path:

```text
audio/voiceover.wav
```

Manim scenes should check for this file and call:

```python
self.add_sound("audio/voiceover.wav")
```

## Preferred Alibaba Target

For new workflows, prefer Alibaba Bailian/DashScope CosyVoice unless the user names a different Alibaba service.

Typical request fields to prepare:

```json
{
  "model": "cosyvoice-v3-flash",
  "voice": "[chosen voice]",
  "text": "[voiceover text]",
  "format": "wav",
  "sample_rate": 24000
}
```

Model choice:

- `cosyvoice-v3-flash`: good default for fast short-video voiceover drafts.
- `cosyvoice-v3.5-plus`: consider when quality matters more than speed or when using a custom/designed voice that requires it.
- Use the exact model supported by the user's Alibaba region and account; do not silently substitute if a request fails.

Do not invent API keys, workspace IDs, app IDs, or exact endpoint URLs inside generated project files. If the user wants an API script, ask them to provide the preferred Alibaba product and credential method, then keep secrets in environment variables.

## Text Preparation

Always generate:

```text
voiceover.txt
```

Recommended format:

```text
为什么 AI 不是平均看每个词？
它会先判断，当前这个词最该参考谁。
这一步，就叫注意力。
```

Rules:

- One spoken sentence per line.
- Use natural Chinese punctuation.
- Avoid markdown bullets in `voiceover.txt`.
- Avoid formulas in narration; read them as words if needed.
- Keep each line short enough to rerecord independently.
- Put pronunciation notes in `voiceover_notes.md`, not inside the clean TTS text.

When timing matters, also generate:

```text
voiceover_lines.csv
```

Columns:

```csv
index,start_hint,text,note
1,00:00,"为什么 AI 不是平均看每个词？","hook"
2,00:03,"它会先判断，当前这个词最该参考谁。","mechanism"
```

## Voice Direction

For Douyin educational content, recommend:

- Style: clear, energetic, not overly dramatic.
- Pace: slightly faster than classroom speech, but leave pauses at visual changes.
- Emotion: curious and confident.
- Loudness: normalize after export if possible.

If the platform supports rate/speed:

- Start around normal to slightly fast.
- Slow down only for formulas or key takeaways.

## Audio Format

Preferred:

- `wav`, mono or stereo, 24 kHz or 48 kHz.

Acceptable:

- `mp3`, then convert to wav or update `VOICEOVER_PATH`.

If the Alibaba platform returns a URL, download the audio and save it as:

```text
audio/voiceover.wav
```

If it returns MP3:

```bash
ffmpeg -y -i audio/voiceover.mp3 audio/voiceover.wav
```

## Sync With Manim

Before final render:

1. Measure voiceover length:

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 audio/voiceover.wav
```

2. Adjust scene waits and animation durations to match the actual voiceover.
3. Avoid padding the video with a frozen tail.
4. Render.
5. Verify final MP4 contains audio:

```bash
ffprobe -v error -show_streams output.mp4
```

## When The User Is Making A Video

Ask only for missing choices that matter:

- Which Alibaba voice/model should be used?
- Should Codex only prepare the TTS files, or also write an API script?
- Should the video be rendered silent first for visual QA, then rerendered with audio?

If the user says "use Alibaba TTS" without details:

1. Create `voiceover.txt`.
2. Create `voiceover_lines.csv`.
3. Use `audio/voiceover.wav` as the expected final path.
4. Tell the user to export Alibaba TTS audio to that path.
5. Keep the Manim scene ready to attach the audio automatically.

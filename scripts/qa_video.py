#!/usr/bin/env python
"""Small ffprobe-based QA report for final short-video files."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def ffprobe_json(path: Path) -> dict:
    result = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)])
    return json.loads(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a basic video QA report.")
    parser.add_argument("video_path")
    parser.add_argument("--out", default="qa_report.md")
    parser.add_argument("--bgm-path")
    parser.add_argument("--voiceover-path")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    video_path = Path(args.video_path)
    data = ffprobe_json(video_path)
    streams = data.get("streams", [])
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    duration = data.get("format", {}).get("duration", "unknown")

    lines = [
        "# Video QA Report",
        "",
        "## Input",
        "",
        f"- video: `{video_path}`",
        f"- voiceover: `{args.voiceover_path or ''}`",
        f"- bgm: `{args.bgm_path or ''}`",
        "",
        "## Stream Check",
        "",
        f"- has_video: {bool(video_streams)}",
        f"- has_audio: {bool(audio_streams)}",
        f"- duration: {duration}s",
    ]

    if video_streams:
        v = video_streams[0]
        lines.extend(
            [
                f"- video_codec: {v.get('codec_name', 'unknown')}",
                f"- resolution: {v.get('width', 'unknown')}x{v.get('height', 'unknown')}",
            ]
        )
    if audio_streams:
        a = audio_streams[0]
        lines.extend(
            [
                f"- audio_codec: {a.get('codec_name', 'unknown')}",
                f"- sample_rate: {a.get('sample_rate', 'unknown')}",
                f"- channels: {a.get('channels', 'unknown')}",
                f"- audio_duration: {a.get('duration', 'unknown')}s",
            ]
        )

    lines.extend(
        [
            "",
            "## Manual Checks",
            "",
            "- [ ] BGM does not cover Chinese voiceover.",
            "- [ ] No tail black screen.",
            "- [ ] No tail freeze.",
            "- [ ] Contact sheet generated.",
            "- [ ] Subtitles are not covered by player UI.",
            "- [ ] CTA is clear.",
            "",
            "## Notes",
            "",
            args.notes,
            "",
        ]
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"qa_report={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

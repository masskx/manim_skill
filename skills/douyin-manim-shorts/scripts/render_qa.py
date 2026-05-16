#!/usr/bin/env python3
"""Create quick QA artifacts for a rendered short-form Manim video.

This script depends on ffmpeg and ffprobe being available on PATH. It creates a
contact sheet for visual layout inspection, runs freeze detection, and reports
whether the video contains an audio stream.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="Path to rendered MP4")
    parser.add_argument("--out-dir", default="qa", help="Directory for QA output")
    args = parser.parse_args()

    video = Path(args.video)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not video.exists():
        print(f"Missing video: {video}")
        return 1

    contact_sheet = out_dir / f"{video.stem}_contact_sheet.jpg"
    sheet_cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-vf",
        "fps=1/2,scale=270:-1,tile=4x6",
        str(contact_sheet),
    ]
    sheet = run(sheet_cmd)

    freeze_cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        str(video),
        "-vf",
        "freezedetect=n=0.003:d=2",
        "-f",
        "null",
        "-",
    ]
    freeze = run(freeze_cmd)
    freeze_log = out_dir / f"{video.stem}_freeze.log"
    freeze_log.write_text(freeze.stderr, encoding="utf-8")

    probe_cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_streams",
        "-print_format",
        "json",
        str(video),
    ]
    probe = run(probe_cmd)
    streams = json.loads(probe.stdout or "{}").get("streams", [])
    has_audio = any(stream.get("codec_type") == "audio" for stream in streams)
    has_video = any(stream.get("codec_type") == "video" for stream in streams)

    freeze_lines = [
        line
        for line in freeze.stderr.splitlines()
        if "freeze_start" in line or "freeze_end" in line or "freeze_duration" in line
    ]

    print(f"video: {video}")
    print(f"contact_sheet: {contact_sheet if contact_sheet.exists() else 'not created'}")
    print(f"freeze_log: {freeze_log}")
    print(f"has_video: {has_video}")
    print(f"has_audio: {has_audio}")
    if freeze_lines:
        print("freeze_events:")
        for line in freeze_lines:
            print(f"  {line}")
    else:
        print("freeze_events: none detected at threshold n=0.003 d=2")

    if sheet.returncode != 0:
        print("contact sheet generation failed")
        print(sheet.stderr)
        return 1
    if probe.returncode != 0:
        print("ffprobe failed")
        print(probe.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

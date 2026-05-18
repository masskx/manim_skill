#!/usr/bin/env python
"""Mix background music into an existing short video with ffmpeg."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def ffprobe_json(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    return json.loads(result.stdout)


def duration_seconds(path: Path) -> float:
    data = ffprobe_json(path)
    duration = data.get("format", {}).get("duration")
    if duration is None:
        raise RuntimeError(f"Could not detect duration for {path}")
    return float(duration)


def has_audio(path: Path) -> bool:
    data = ffprobe_json(path)
    return any(stream.get("codec_type") == "audio" for stream in data.get("streams", []))


def build_mixed_audio(
    *,
    video_path: Path,
    bgm_path: Path,
    voiceover_path: Path | None,
    mixed_audio_path: Path,
    video_duration: float,
    bgm_volume: float,
    voiceover_volume: float,
) -> str:
    mixed_audio_path.parent.mkdir(parents=True, exist_ok=True)

    if voiceover_path:
        source_path = voiceover_path
        source_label = "voiceover"
    elif has_audio(video_path):
        source_path = video_path
        source_label = "video_audio"
    else:
        source_path = None
        source_label = "bgm_only"

    if source_path:
        filter_complex = (
            f"[0:a]volume={voiceover_volume},atrim=0:{video_duration:.3f},"
            f"apad=whole_dur={video_duration:.3f},atrim=0:{video_duration:.3f},"
            "asetpts=N/SR/TB[a0];"
            f"[1:a]volume={bgm_volume},atrim=0:{video_duration:.3f},"
            "asetpts=N/SR/TB[bgm];"
            "[a0][bgm]amix=inputs=2:duration=longest:normalize=0,"
            "alimiter=limit=0.95,aresample=48000[aout]"
        )
        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(source_path),
            "-stream_loop",
            "-1",
            "-i",
            str(bgm_path),
            "-filter_complex",
            filter_complex,
            "-map",
            "[aout]",
            "-t",
            f"{video_duration:.3f}",
            "-ac",
            "2",
            "-ar",
            "48000",
            str(mixed_audio_path),
        ]
    else:
        filter_complex = (
            f"[0:a]volume={bgm_volume},atrim=0:{video_duration:.3f},"
            "asetpts=N/SR/TB,alimiter=limit=0.95,aresample=48000[aout]"
        )
        cmd = [
            "ffmpeg",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(bgm_path),
            "-filter_complex",
            filter_complex,
            "-map",
            "[aout]",
            "-t",
            f"{video_duration:.3f}",
            "-ac",
            "2",
            "-ar",
            "48000",
            str(mixed_audio_path),
        ]

    run(cmd)
    return source_label


def mux_video(video_path: Path, mixed_audio_path: Path, output_path: Path, video_duration: float) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(video_path),
            "-i",
            str(mixed_audio_path),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-t",
            f"{video_duration:.3f}",
            str(output_path),
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Add looped/cropped BGM to a video.")
    parser.add_argument("--video", "--video-path", dest="video_path", required=True)
    parser.add_argument("--bgm", "--bgm-path", dest="bgm_path", required=True)
    parser.add_argument("--voiceover", "--voiceover-path", dest="voiceover_path")
    parser.add_argument("--out", "--output-path", dest="output_path", required=True)
    parser.add_argument("--mixed-audio", dest="mixed_audio_path", required=True)
    parser.add_argument("--preview-no-bgm", dest="preview_no_bgm_path")
    parser.add_argument("--bgm-volume", type=float, default=0.15)
    parser.add_argument("--voiceover-volume", type=float, default=1.0)
    parser.add_argument("--meta", dest="meta_path")
    args = parser.parse_args()

    video_path = Path(args.video_path)
    bgm_path = Path(args.bgm_path)
    voiceover_path = Path(args.voiceover_path) if args.voiceover_path else None
    output_path = Path(args.output_path)
    mixed_audio_path = Path(args.mixed_audio_path)

    if not video_path.exists():
        raise FileNotFoundError(video_path)
    if not bgm_path.exists():
        raise FileNotFoundError(bgm_path)
    if voiceover_path and not voiceover_path.exists():
        raise FileNotFoundError(voiceover_path)

    video_duration = duration_seconds(video_path)
    bgm_duration = duration_seconds(bgm_path)

    if args.preview_no_bgm_path:
        preview_path = Path(args.preview_no_bgm_path)
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        if preview_path.resolve() != video_path.resolve():
            shutil.copyfile(video_path, preview_path)

    source_label = build_mixed_audio(
        video_path=video_path,
        bgm_path=bgm_path,
        voiceover_path=voiceover_path,
        mixed_audio_path=mixed_audio_path,
        video_duration=video_duration,
        bgm_volume=args.bgm_volume,
        voiceover_volume=args.voiceover_volume,
    )
    mux_video(video_path, mixed_audio_path, output_path, video_duration)

    output_has_audio = has_audio(output_path)
    output_duration = duration_seconds(output_path)
    mixed_duration = duration_seconds(mixed_audio_path)
    meta = {
        "video_path": str(video_path),
        "bgm_path": str(bgm_path),
        "voiceover_path": str(voiceover_path) if voiceover_path else None,
        "source_audio": source_label,
        "output_path": str(output_path),
        "mixed_audio_path": str(mixed_audio_path),
        "video_duration": round(video_duration, 3),
        "bgm_duration": round(bgm_duration, 3),
        "output_duration": round(output_duration, 3),
        "mixed_audio_duration": round(mixed_duration, 3),
        "bgm_volume": args.bgm_volume,
        "voiceover_volume": args.voiceover_volume,
        "has_audio": output_has_audio,
    }

    if args.meta_path:
        meta_path = Path(args.meta_path)
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

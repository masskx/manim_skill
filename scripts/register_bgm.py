#!/usr/bin/env python
"""Register BGM files under shared_assets/bgm_library into index/bgm_registry.csv."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path


FIELDS = [
    "filename",
    "path",
    "style",
    "bpm",
    "duration",
    "loopable",
    "mood",
    "energy",
    "license_note",
    "recommended_use",
    "used_count",
    "notes",
]


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.strip()


def duration_seconds(path: Path) -> str:
    try:
        raw = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)])
        return f"{float(raw):.3f}"
    except Exception:
        return "unknown"


def parse_bpm(filename: str) -> str:
    match = re.search(r"_(\d{2,3})bpm_", filename, flags=re.IGNORECASE)
    return match.group(1) if match else "unknown"


def load_existing(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {row["path"]: row for row in reader if row.get("path")}


def write_registry(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update BGM registry from a shared BGM library.")
    parser.add_argument("--library", default="shared_assets/bgm_library")
    parser.add_argument("--registry", default="index/bgm_registry.csv")
    parser.add_argument("--license-note", default="user-provided")
    parser.add_argument("--recommended-use", default="deep learning module short videos")
    args = parser.parse_args()

    root = Path(args.library)
    registry_path = Path(args.registry)
    existing = load_existing(registry_path)
    rows: list[dict[str, str]] = []

    for audio_path in sorted(root.rglob("*")):
        if audio_path.suffix.lower() not in {".wav", ".mp3", ".m4a", ".aac", ".flac"}:
            continue
        rel = audio_path.as_posix()
        style = audio_path.parent.name
        previous = existing.get(rel, {})
        row = {
            "filename": audio_path.name,
            "path": rel,
            "style": previous.get("style") or style,
            "bpm": previous.get("bpm") or parse_bpm(audio_path.name),
            "duration": duration_seconds(audio_path),
            "loopable": previous.get("loopable") or "true",
            "mood": previous.get("mood") or "",
            "energy": previous.get("energy") or "",
            "license_note": previous.get("license_note") or args.license_note,
            "recommended_use": previous.get("recommended_use") or args.recommended_use,
            "used_count": previous.get("used_count") or "0",
            "notes": previous.get("notes") or "",
        }
        rows.append(row)

    write_registry(registry_path, rows)
    print(f"registered={len(rows)} registry={registry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

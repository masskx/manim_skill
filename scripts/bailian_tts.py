#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_dashscope() -> Any:
    try:
        import dashscope  # type: ignore
    except ImportError:
        fail("dashscope is not installed. Install it with: pip install -U dashscope")
    return dashscope


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False)


def ffprobe_audio(path: Path) -> dict[str, Any]:
    probe = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a:0",
            "-show_entries",
            "stream=codec_name,sample_rate,channels,duration",
            "-show_entries",
            "format=duration",
            "-print_format",
            "json",
            str(path),
        ]
    )
    if probe.returncode != 0:
        return {"ffprobe_error": probe.stderr.strip()}
    try:
        data = json.loads(probe.stdout or "{}")
    except json.JSONDecodeError:
        return {"ffprobe_error": "invalid ffprobe json"}
    stream = (data.get("streams") or [{}])[0]
    fmt = data.get("format") or {}
    return {
        "codec": stream.get("codec_name"),
        "sample_rate": int(stream["sample_rate"]) if stream.get("sample_rate") else None,
        "channels": stream.get("channels"),
        "duration": float(stream.get("duration") or fmt.get("duration") or 0),
    }


def convert_to_wav(src: Path, dst: Path) -> None:
    if not shutil.which("ffmpeg"):
        fail("ffmpeg not found on PATH; cannot convert TTS output to wav")
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(src),
        "-acodec",
        "pcm_s16le",
        "-ar",
        "24000",
        "-ac",
        "1",
        str(dst),
    ]
    result = run(cmd)
    if result.returncode != 0:
        fail(f"ffmpeg conversion failed:\n{result.stderr}")


def extract_audio_payload(response: Any) -> bytes | None:
    candidates: list[Any] = []
    if isinstance(response, dict):
        candidates.extend([response])
        output = response.get("output")
        if isinstance(output, dict):
            candidates.append(output)
    else:
        if hasattr(response, "get_audio_data"):
            value = response.get_audio_data()
            if isinstance(value, (bytes, bytearray)):
                return bytes(value)
        value = getattr(response, "audio_data", None)
        if isinstance(value, (bytes, bytearray)):
            return bytes(value)
        for attr in ("output", "audio", "data"):
            value = getattr(response, attr, None)
            if value is not None:
                candidates.append(value)

    for item in candidates:
        if isinstance(item, (bytes, bytearray)):
            return bytes(item)
        if not isinstance(item, dict):
            continue
        for key in ("audio", "data", "content", "binary"):
            value = item.get(key)
            if isinstance(value, (bytes, bytearray)):
                return bytes(value)
            if isinstance(value, str):
                try:
                    return base64.b64decode(value)
                except Exception:
                    pass
    return None


def extract_audio_url(response: Any) -> str | None:
    candidates: list[Any] = []
    if isinstance(response, dict):
        candidates.extend([response])
        output = response.get("output")
        if isinstance(output, dict):
            candidates.append(output)
    else:
        output = getattr(response, "output", None)
        if isinstance(output, dict):
            candidates.append(output)
        value = getattr(response, "audio_url", None)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            return value

    for item in candidates:
        if not isinstance(item, dict):
            continue
        for key in ("audio_url", "url", "file_url"):
            value = item.get(key)
            if isinstance(value, str) and value.startswith(("http://", "https://")):
                return value
    return None


def write_response_audio(response: Any, target: Path, temp_dir: Path) -> Path:
    payload = extract_audio_payload(response)
    if payload:
        raw = temp_dir / "dashscope_audio.bin"
        raw.write_bytes(payload)
        return raw

    url = extract_audio_url(response)
    if url:
        try:
            import urllib.request

            raw = temp_dir / "dashscope_audio_from_url"
            with urllib.request.urlopen(url, timeout=120) as source:
                raw.write_bytes(source.read())
            return raw
        except Exception as exc:
            fail(f"failed to download audio_url from DashScope response: {exc}")

    if target.exists():
        return target
    fail("DashScope response did not contain recognizable audio bytes or audio URL")


def synthesize_with_speech_synthesizer(dashscope: Any, args: argparse.Namespace) -> Any:
    try:
        from dashscope.audio.tts import SpeechSynthesizer  # type: ignore
    except Exception as exc:
        raise RuntimeError(f"dashscope.audio.tts.SpeechSynthesizer unavailable: {exc}") from exc

    kwargs = {
        "voice": args.voice,
        "format": args.format,
        "sample_rate": args.sample_rate,
    }
    if args.speed is not None:
        kwargs["rate"] = args.speed

    return SpeechSynthesizer.call(
        model=args.model,
        text=args.text_content,
        **kwargs,
    )


def synthesize_with_http_speech_synthesizer(dashscope: Any, args: argparse.Namespace) -> Any:
    try:
        from dashscope.audio.http_tts import HttpSpeechSynthesizer  # type: ignore
    except Exception as exc:
        raise RuntimeError(f"dashscope.audio.http_tts.HttpSpeechSynthesizer unavailable: {exc}") from exc

    return HttpSpeechSynthesizer.call(
        model=args.model,
        text=args.text_content,
        voice=args.voice,
        audio_format=args.format,
        sample_rate=args.sample_rate,
        rate=args.speed,
    )


def synthesize_with_multimodal_conversation(dashscope: Any, args: argparse.Namespace) -> Any:
    messages = [
        {
            "role": "user",
            "content": [
                {"text": args.text_content},
            ],
        }
    ]
    params: dict[str, Any] = {
        "model": args.model,
        "messages": messages,
        "voice": args.voice,
        "result_format": "message",
    }
    if args.speed is not None:
        params["speed"] = args.speed
    return dashscope.MultiModalConversation.call(**params)


def response_to_public_dict(response: Any) -> dict[str, Any]:
    if isinstance(response, dict):
        data = response
    else:
        data = {
            "status_code": getattr(response, "status_code", None),
            "code": getattr(response, "code", None),
            "message": getattr(response, "message", None),
            "request_id": getattr(response, "request_id", None),
            "output": getattr(response, "output", None),
        }
        if hasattr(response, "get_response"):
            sdk_response = response.get_response()
            data.update(
                {
                    "status_code": getattr(sdk_response, "status_code", data.get("status_code")),
                    "code": getattr(sdk_response, "code", data.get("code")),
                    "message": getattr(sdk_response, "message", data.get("message")),
                    "request_id": getattr(sdk_response, "request_id", data.get("request_id")),
                }
            )
        sdk_response = getattr(response, "response", None)
        if sdk_response is not None:
            data.update(
                {
                    "status_code": getattr(sdk_response, "status_code", data.get("status_code")),
                    "code": getattr(sdk_response, "code", data.get("code")),
                    "message": getattr(sdk_response, "message", data.get("message")),
                    "request_id": getattr(sdk_response, "request_id", data.get("request_id")),
                }
            )
        audio_url = getattr(response, "audio_url", None)
        if audio_url:
            data["audio_url"] = "<audio_url omitted>"
        audio_id = getattr(response, "audio_id", None)
        if audio_id:
            data["audio_id"] = audio_id
    data = json.loads(json.dumps(data, default=str))
    if isinstance(data.get("output"), dict):
        for key in ("audio", "data", "content", "binary"):
            if key in data["output"]:
                data["output"][key] = f"<{key} omitted>"
    return data


def response_has_error(response: Any) -> tuple[bool, str]:
    data = response_to_public_dict(response)
    status_code = data.get("status_code")
    code = data.get("code")
    message = data.get("message")
    has_error = status_code not in (None, 200) or (code and code not in ("", "OK", "Success"))
    return bool(has_error), f"code={code}, status={status_code}, message={message}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Bailian/DashScope TTS audio.")
    parser.add_argument("--text", required=True, help="Input text file")
    parser.add_argument("--out", required=True, help="Output wav path")
    parser.add_argument("--meta", required=True, help="Output metadata json path")
    parser.add_argument("--model", default="cosyvoice-v3-flash")
    parser.add_argument("--voice", default="longxiaochun")
    parser.add_argument("--speed", type=float, default=1.10)
    parser.add_argument("--format", default="wav", choices=["wav", "mp3", "pcm"])
    parser.add_argument("--sample-rate", type=int, default=24000)
    args = parser.parse_args()

    text_path = Path(args.text)
    out_path = Path(args.out)
    meta_path = Path(args.meta)
    if not text_path.exists():
        fail(f"text file not found: {text_path}")

    text_content = text_path.read_text(encoding="utf-8").strip()
    if not text_content:
        fail(f"text file is empty: {text_path}")
    args.text_content = text_content

    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        fail('DASHSCOPE_API_KEY is not set. In PowerShell: $env:DASHSCOPE_API_KEY="your-api-key"')

    dashscope = load_dashscope()
    dashscope.api_key = api_key

    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)

    started = time.time()
    errors: list[str] = []
    response: Any = None
    method = ""
    for method_name, func in (
        ("HttpSpeechSynthesizer", synthesize_with_http_speech_synthesizer),
        ("SpeechSynthesizer", synthesize_with_speech_synthesizer),
        ("MultiModalConversation", synthesize_with_multimodal_conversation),
    ):
        try:
            candidate = func(dashscope, args)
            has_error, error_text = response_has_error(candidate)
            if has_error:
                errors.append(f"{method_name}: {error_text}")
                continue
            response = candidate
            method = method_name
            break
        except Exception as exc:
            errors.append(f"{method_name}: {exc}")
    if response is None:
        fail(
            "DashScope TTS call failed. The voice may be unavailable or the SDK API changed. "
            "Try another voice/model or upgrade dashscope.\n" + "\n".join(errors)
        )

    public_response = response_to_public_dict(response)
    status_code = public_response.get("status_code")
    code = public_response.get("code")
    message = public_response.get("message")
    if status_code not in (None, 200) or (code and code not in ("", "OK", "Success")):
        fail(f"DashScope returned an error. code={code}, status={status_code}, message={message}")

    with tempfile.TemporaryDirectory() as td:
        temp_dir = Path(td)
        raw_path = write_response_audio(response, out_path, temp_dir)
        if raw_path.resolve() != out_path.resolve() or out_path.suffix.lower() != ".wav":
            convert_to_wav(raw_path, out_path)
        elif not out_path.exists():
            raw = temp_dir / "audio_raw.wav"
            shutil.copyfile(raw_path, raw)
            convert_to_wav(raw, out_path)

    audio_info = ffprobe_audio(out_path)
    meta = {
        "text_path": str(text_path),
        "out_path": str(out_path),
        "model": args.model,
        "voice": args.voice,
        "speed": args.speed,
        "format": "wav",
        "sample_rate_requested": args.sample_rate,
        "method": method,
        "elapsed_seconds": round(time.time() - started, 3),
        "file_size_bytes": out_path.stat().st_size if out_path.exists() else 0,
        "audio": audio_info,
        "dashscope_response": public_response,
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"voiceover: {out_path}")
    print(f"meta: {meta_path}")
    print(f"duration: {audio_info.get('duration')}")
    print(f"sample_rate: {audio_info.get('sample_rate')}")
    print(f"channels: {audio_info.get('channels')}")
    print(f"file_size_bytes: {meta['file_size_bytes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

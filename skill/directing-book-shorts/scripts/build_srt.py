#!/usr/bin/env python3
"""Build and validate UTF-8 BOM SRT for fixed-length video containers."""
import argparse
import json
import re
from pathlib import Path

TIME_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2}),(\d{3})$")

def to_ms(value: str) -> int:
    match = TIME_RE.match(value)
    if not match:
        raise ValueError(f"Invalid SRT timestamp: {value}")
    hours, minutes, seconds, millis = map(int, match.groups())
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis

def validate(entries, duration_seconds=60.0, clip_seconds=10.0):
    if duration_seconds <= 0 or clip_seconds <= 0:
        raise ValueError("Duration and clip length must be positive")
    max_ms = int(round(duration_seconds * 1000))
    clip_ms = int(round(clip_seconds * 1000))
    boundaries = set(range(clip_ms, max_ms + clip_ms, clip_ms))
    previous_end = -1
    for index, entry in enumerate(entries, start=1):
        for key in ("start", "end", "text"):
            if key not in entry:
                raise ValueError(f"Entry {index} missing key: {key}")
        start, end = to_ms(entry["start"]), to_ms(entry["end"])
        text = str(entry["text"]).strip()
        if not text or end <= start or start < previous_end:
            raise ValueError(f"Entry {index} has invalid content or interval")
        if end > max_ms:
            raise ValueError(f"Entry {index} ends after target duration {duration_seconds:g}s")
        for boundary in boundaries:
            if boundary < max_ms and start < boundary < end:
                raise ValueError(f"Entry {index} crosses fixed {clip_seconds:g}-second boundary at {boundary/1000:g}s")
        previous_end = end

def render(entries) -> str:
    return "\n\n".join(f"{i}\n{e['start']} --> {e['end']}\n{str(e['text']).strip()}" for i, e in enumerate(entries, 1)) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_srt", type=Path)
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--clip-seconds", type=float, default=10.0)
    args = parser.parse_args()
    entries = json.loads(args.input_json.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("Input must be a non-empty JSON array")
    validate(entries, args.duration, args.clip_seconds)
    args.output_srt.parent.mkdir(parents=True, exist_ok=True)
    args.output_srt.write_text(render(entries), encoding="utf-8-sig")
    print(f"Wrote {len(entries)} entries to {args.output_srt} for target duration {args.duration:g}s")

if __name__ == "__main__":
    main()

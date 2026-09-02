#!/usr/bin/env python3
"""Run deterministic technical QA and extract review frames for a video."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--output", type=Path, default=Path("qa"))
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.is_file():
        parser.error(f"video not found: {video}")
    args.output.mkdir(parents=True, exist_ok=True)

    probe = run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)
    ])
    metadata = json.loads(probe.stdout)
    duration = float(metadata["format"]["duration"])
    video_streams = [stream for stream in metadata["streams"] if stream["codec_type"] == "video"]
    audio_streams = [stream for stream in metadata["streams"] if stream["codec_type"] == "audio"]

    sample_times = sorted({0.2, max(0.2, duration / 4), duration / 2, duration * 3 / 4, max(0.2, duration - 0.5)})
    frames = []
    for index, timestamp in enumerate(sample_times, start=1):
        output = args.output / f"frame_{index:02d}_{timestamp:.2f}s.jpg"
        run([
            "ffmpeg", "-y", "-ss", f"{timestamp:.3f}", "-i", str(video),
            "-frames:v", "1", "-q:v", "2", str(output)
        ])
        frames.append(str(output))

    report = {
        "video": str(video),
        "duration_seconds": duration,
        "video_streams": video_streams,
        "audio_streams": audio_streams,
        "review_frames": frames,
        "manual_checks_required": [
            "subtitle spelling and safe margins",
            "face and lip-sync stability",
            "black frames and visual discontinuities",
            "audio pops, clipping, and music balance",
            "claim accuracy and final approval"
        ]
    }
    report_path = args.output / "report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(report_path)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""对成片进行可重现的技术质检，并抽取人工审查帧。"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    """运行本地音视频命令，命令失败时立即终止。"""
    return subprocess.run(command, check=True, capture_output=True, text=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="检查视频参数并抽取人工审查帧。")
    parser.add_argument("video", type=Path, help="需要检查的视频路径")
    parser.add_argument("--output", type=Path, default=Path("qa"), help="质检报告和抽帧输出目录")
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.is_file():
        parser.error(f"找不到视频：{video}")
    args.output.mkdir(parents=True, exist_ok=True)

    probe = run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)
    ])
    metadata = json.loads(probe.stdout)
    duration = float(metadata["format"]["duration"])
    video_streams = [stream for stream in metadata["streams"] if stream["codec_type"] == "video"]
    audio_streams = [stream for stream in metadata["streams"] if stream["codec_type"] == "audio"]

    # 固定抽取首部、1/4、中点、3/4 和尾部，便于不同版本横向比较。
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
            "字幕错字和安全边距",
            "人脸与嘴型同步稳定性",
            "黑帧和画面跳变",
            "音频爆音、削波失真和音乐平衡",
            "内容表述准确性与最终人工确认"
        ]
    }
    report_path = args.output / "report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(report_path)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""只读检查视频生产环境是否已准备好。"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def version(command: list[str]) -> str:
    """运行版本命令，返回第一行结果；不对系统做任何修改。"""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return "无法读取"
    output = (result.stdout or result.stderr).strip().splitlines()
    return output[0] if output else "已安装"


def main() -> int:
    checks = {
        "git": shutil.which("git"),
        "ffmpeg": shutil.which("ffmpeg"),
        "ffprobe": shutil.which("ffprobe"),
        "node": shutil.which("node"),
        "npm": shutil.which("npm"),
        "uv": shutil.which("uv"),
    }
    for name, path in checks.items():
        print(f"{name:10} {'正常' if path else '缺失':8} {path or ''}")

    if checks["node"]:
        print(f"node       版本      {version(['node', '--version'])}")
    if checks["ffmpeg"]:
        print(f"ffmpeg     版本      {version(['ffmpeg', '-version'])}")

    skill = Path.home() / ".codex" / "skills" / "video-use"
    print(f"video-use  {'正常' if (skill / 'SKILL.md').exists() else '缺失':8} {skill}")

    for key in ("ELEVENLABS_API_KEY", "HEYGEN_API_KEY"):
        print(f"{key:22} {'已设置' if os.environ.get(key) else '未设置'}")

    required_ok = all(checks[name] for name in ("git", "ffmpeg", "ffprobe", "node", "npm"))
    required_ok = required_ok and (skill / "SKILL.md").exists()
    print("\n本地规划和渲染环境已准备好。" if required_ok else "\n本地环境尚未完整。")
    print("在 API Key 设置完成且通过对应确认门槛前，云端付费生成保持锁定。")
    return 0 if required_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read-only environment readiness check for the pilot pipeline."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def version(command: list[str]) -> str:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return "unavailable"
    output = (result.stdout or result.stderr).strip().splitlines()
    return output[0] if output else "available"


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
        print(f"{name:10} {'OK' if path else 'MISSING':8} {path or ''}")

    if checks["node"]:
        print(f"node       VERSION  {version(['node', '--version'])}")
    if checks["ffmpeg"]:
        print(f"ffmpeg     VERSION  {version(['ffmpeg', '-version'])}")

    skill = Path.home() / ".codex" / "skills" / "video-use"
    print(f"video-use  {'OK' if (skill / 'SKILL.md').exists() else 'MISSING':8} {skill}")

    for key in ("ELEVENLABS_API_KEY", "HEYGEN_API_KEY"):
        print(f"{key:22} {'SET' if os.environ.get(key) else 'NOT SET'}")

    required_ok = all(checks[name] for name in ("git", "ffmpeg", "ffprobe", "node", "npm"))
    required_ok = required_ok and (skill / "SKILL.md").exists()
    print("\nReady for local planning/rendering." if required_ok else "\nLocal setup is incomplete.")
    print("Cloud generation remains locked until API keys and gate approval are present.")
    return 0 if required_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

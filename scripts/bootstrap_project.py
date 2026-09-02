#!/usr/bin/env python3
"""Create a local project workspace without touching cloud services."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_BRIEF = {
    "status": "draft_awaiting_user_review",
    "target_duration_seconds": 120,
    "format": "1920x1080@30",
    "language": "zh-CN",
    "avatar_target_seconds": 35,
    "avatar_engine": "photo",
    "paid_generation_allowed": False,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Project directory name, e.g. pilot-002")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    project = root / "projects" / args.name
    project.mkdir(parents=True, exist_ok=False)
    for child in ("inputs", "private", "edit", "outputs", "qa"):
        (project / child).mkdir()

    (project / "brief.json").write_text(
        json.dumps(DEFAULT_BRIEF, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (project / "script.md").write_text("# 口播脚本（待审）\n\n", encoding="utf-8")
    (project / "strategy.md").write_text("# 视觉与剪辑策略（待审）\n\n", encoding="utf-8")
    (project / "edit" / "project.md").write_text(
        "# Editing memory\n\nNo paid generation has been approved.\n", encoding="utf-8"
    )
    print(project)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""创建本地视频项目目录，不访问任何云端服务。"""

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
    parser = argparse.ArgumentParser(description="创建一个新的视频项目骨架。")
    parser.add_argument("name", help="项目目录名，例如 pilot-002")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    project = root / "projects" / args.name
    project.mkdir(parents=True, exist_ok=False)
    # 输入素材、私密文件、剪辑中间件、成片和质检证据分开存放。
    for child in ("inputs", "private", "edit", "outputs", "qa"):
        (project / child).mkdir()

    (project / "brief.json").write_text(
        json.dumps(DEFAULT_BRIEF, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (project / "script.md").write_text("# 口播脚本（待审）\n\n", encoding="utf-8")
    (project / "strategy.md").write_text("# 视觉与剪辑策略（待审）\n\n", encoding="utf-8")
    (project / "edit" / "project.md").write_text(
        "# 剪辑记忆\n\n当前尚未批准任何付费生成。\n", encoding="utf-8"
    )
    print(project)


if __name__ == "__main__":
    main()

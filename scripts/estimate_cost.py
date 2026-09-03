#!/usr/bin/env python3
"""在不发起任何网络请求的情况下估算数字人 API 成本。"""

from __future__ import annotations

import argparse


# 默认单价：美元/秒。正式生成前必须核对当时的官方价格。
RATES = {"photo": 0.05, "digital-twin": 0.0667}


def main() -> None:
    parser = argparse.ArgumentParser(description="本地估算数字人生成成本，不会调用付费 API。")
    parser.add_argument("--duration", type=float, required=True, help="最终视频时长（秒）")
    parser.add_argument("--avatar-seconds", type=float, required=True, help="数字人实际出镜时长（秒）")
    parser.add_argument("--engine", choices=RATES, default="photo", help="数字人引擎类型")
    parser.add_argument("--retry-reserve", type=float, default=0.4, help="重试成本预留比例，默认 40%%")
    parser.add_argument("--usd-cny", type=float, default=7.1, help="估算使用的美元兑人民币汇率")
    args = parser.parse_args()

    if not 0 <= args.avatar_seconds <= args.duration:
        parser.error("数字人出镜时长必须在 0 和成片时长之间")
    if args.retry_reserve < 0:
        parser.error("重试预留比例不能是负数")

    base = args.avatar_seconds * RATES[args.engine]
    budget = base * (1 + args.retry_reserve)
    share = args.avatar_seconds / args.duration if args.duration else 0
    print(f"数字人类型：       {args.engine}")
    print(f"数字人出镜比例：   {share:.1%}")
    print(f"基础人物生成成本： 美元 {base:.2f} / 约人民币 {base * args.usd_cny:.2f} 元")
    print(f"包含重试预留：     美元 {budget:.2f} / 约人民币 {budget * args.usd_cny:.2f} 元")
    print("未包含：声音套餐、可选 AI B-roll、税费以及平台调价。")


if __name__ == "__main__":
    main()

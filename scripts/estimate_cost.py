#!/usr/bin/env python3
"""Estimate avatar API cost without making any network request."""

from __future__ import annotations

import argparse


RATES = {"photo": 0.05, "digital-twin": 0.0667}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, required=True, help="Final video duration in seconds")
    parser.add_argument("--avatar-seconds", type=float, required=True)
    parser.add_argument("--engine", choices=RATES, default="photo")
    parser.add_argument("--retry-reserve", type=float, default=0.4, help="Extra generation reserve, default 40%%")
    parser.add_argument("--usd-cny", type=float, default=7.1)
    args = parser.parse_args()

    if not 0 <= args.avatar_seconds <= args.duration:
        parser.error("avatar-seconds must be between 0 and duration")
    if args.retry_reserve < 0:
        parser.error("retry-reserve cannot be negative")

    base = args.avatar_seconds * RATES[args.engine]
    budget = base * (1 + args.retry_reserve)
    share = args.avatar_seconds / args.duration if args.duration else 0
    print(f"engine:              {args.engine}")
    print(f"avatar share:        {share:.1%}")
    print(f"base avatar cost:    USD {base:.2f} / approx CNY {base * args.usd_cny:.2f}")
    print(f"with retry reserve:  USD {budget:.2f} / approx CNY {budget * args.usd_cny:.2f}")
    print("Excluded: voice subscription, optional generated B-roll, taxes, and platform price changes.")


if __name__ == "__main__":
    main()

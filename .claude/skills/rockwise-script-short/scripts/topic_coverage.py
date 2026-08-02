#!/usr/bin/env python3
"""Mide cobertura y rendimiento de clusters en el catálogo TikTok propio."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def parse_cluster(raw: str) -> tuple[str, list[str]]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError(
            "Usa NOMBRE=alias uno|alias dos para cada --cluster"
        )
    name, aliases = raw.split("=", 1)
    parsed = [normalize(alias) for alias in aliases.split("|") if normalize(alias)]
    if not name.strip() or not parsed:
        raise argparse.ArgumentTypeError(f"Cluster inválido: {raw}")
    return name.strip(), parsed


def median(values: list[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def pct(value: float) -> float:
    return round(value * 100, 4)


def summarize(
    videos: list[dict],
    name: str,
    aliases: list[str],
    as_of: datetime,
    recent_days: int,
) -> dict:
    matches = []
    for video in videos:
        haystack = normalize(
            f"{video.get('title', '')} {video.get('video_description', '')}"
        )
        if any(alias in haystack for alias in aliases):
            created = datetime.fromtimestamp(
                int(video.get("create_time", 0)), tz=timezone.utc
            )
            views = int(video.get("view_count", 0))
            likes = int(video.get("like_count", 0))
            comments = int(video.get("comment_count", 0))
            shares = int(video.get("share_count", 0))
            matches.append(
                {
                    "id": str(video.get("id", "")),
                    "created": created,
                    "title": video.get("title", ""),
                    "views": views,
                    "likes": likes,
                    "comments": comments,
                    "shares": shares,
                    "share_rate": shares / views if views else 0,
                    "engagement_rate": (
                        (likes + comments + shares) / views if views else 0
                    ),
                }
            )

    matches.sort(key=lambda item: item["created"], reverse=True)
    cutoff_seconds = recent_days * 86400
    recent = [
        item
        for item in matches
        if 0 <= (as_of - item["created"]).total_seconds() <= cutoff_seconds
    ]
    best = max(matches, key=lambda item: item["views"]) if matches else None
    latest = matches[0] if matches else None

    return {
        "cluster": name,
        "aliases": aliases,
        "videos_total": len(matches),
        f"videos_last_{recent_days}d": len(recent),
        "median_views": round(median([item["views"] for item in matches])),
        "median_share_rate_pct": pct(
            median([item["share_rate"] for item in matches])
        ),
        "median_engagement_rate_pct": pct(
            median([item["engagement_rate"] for item in matches])
        ),
        "latest": (
            {
                "date": latest["created"].date().isoformat(),
                "views": latest["views"],
                "title": latest["title"],
            }
            if latest
            else None
        ),
        "best": (
            {
                "date": best["created"].date().isoformat(),
                "views": best["views"],
                "share_rate_pct": pct(best["share_rate"]),
                "title": best["title"],
            }
            if best
            else None
        ),
    }


def markdown(results: list[dict], recent_days: int) -> str:
    lines = [
        "| Cluster | Videos | "
        f"Últimos {recent_days}d | Mediana views | Share mediana | Mejor video |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for result in results:
        best_views = result["best"]["views"] if result["best"] else 0
        lines.append(
            f"| {result['cluster']} | {result['videos_total']} | "
            f"{result[f'videos_last_{recent_days}d']} | "
            f"{result['median_views']:,} | "
            f"{result['median_share_rate_pct']:.4f}% | {best_views:,} |"
        )
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument(
        "--cluster",
        action="append",
        required=True,
        type=parse_cluster,
        help="NOMBRE=alias uno|alias dos",
    )
    parser.add_argument("--recent-days", type=int, default=90)
    parser.add_argument(
        "--as-of",
        default=datetime.now(tz=timezone.utc).date().isoformat(),
        help="Fecha UTC YYYY-MM-DD",
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()

    payload = json.loads(args.catalog.read_text(encoding="utf-8"))
    videos = payload["videos"] if isinstance(payload, dict) else payload
    as_of = datetime.fromisoformat(args.as_of).replace(tzinfo=timezone.utc)
    results = [
        summarize(videos, name, aliases, as_of, args.recent_days)
        for name, aliases in args.cluster
    ]
    results.sort(
        key=lambda item: (
            -item[f"videos_last_{args.recent_days}d"],
            -item["videos_total"],
            -item["median_views"],
        )
    )

    if args.format == "json":
        print(
            json.dumps(
                {
                    "as_of": args.as_of,
                    "recent_days": args.recent_days,
                    "results": results,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(markdown(results, args.recent_days))


if __name__ == "__main__":
    main()

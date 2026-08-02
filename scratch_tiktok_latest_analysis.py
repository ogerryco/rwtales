"""Resumen reproducible de los videos recientes descargados con la API de TikTok."""

import json
import os
import sys
from datetime import datetime, timezone
from statistics import median


if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE, "tiktok_own_videos.json")


def engagement(video):
    interactions = sum(
        video.get(field, 0)
        for field in ("like_count", "comment_count", "share_count")
    )
    return 100 * interactions / max(video.get("view_count", 0), 1)


def views_per_day(video, now):
    created = datetime.fromtimestamp(video["create_time"], timezone.utc)
    age_days = max((now - created).total_seconds() / 86400, 0.25)
    return video.get("view_count", 0) / age_days


def label(video):
    text = video.get("title") or video.get("video_description") or "(sin titulo)"
    return " ".join(text.split())[:110]


def main():
    with open(DATA_PATH, encoding="utf-8") as handle:
        payload = json.load(handle)

    now = datetime.now(timezone.utc)
    videos = sorted(payload["videos"], key=lambda item: item["create_time"], reverse=True)
    recent = videos[:20]
    latest_30_days = [
        item
        for item in videos
        if (now - datetime.fromtimestamp(item["create_time"], timezone.utc)).days <= 30
    ]

    print(f"VIDEOS_API={len(videos)}")
    print(f"VIDEOS_ULTIMOS_30_DIAS={len(latest_30_days)}")
    print("RECIENTES")
    for video in recent:
        created = datetime.fromtimestamp(video["create_time"], timezone.utc)
        print(
            f"{created:%Y-%m-%d %H:%MZ}\t"
            f"{video['id']}\t"
            f"{video.get('duration', 0)}s\t"
            f"{video.get('view_count', 0)} views\t"
            f"{video.get('like_count', 0)} likes\t"
            f"{video.get('comment_count', 0)} comments\t"
            f"{video.get('share_count', 0)} shares\t"
            f"{engagement(video):.2f}% ER\t"
            f"{views_per_day(video, now):.0f}/day\t"
            f"{label(video)}"
        )

    if latest_30_days:
        print("RESUMEN_30_DIAS")
        print(f"MEDIANA_VIEWS={median(v.get('view_count', 0) for v in latest_30_days):.0f}")
        print(f"MEDIANA_ER={median(engagement(v) for v in latest_30_days):.2f}")
        print(
            "MEDIANA_VELOCIDAD="
            f"{median(views_per_day(v, now) for v in latest_30_days):.0f}"
        )

    print("TOP_VELOCIDAD_30_DIAS")
    for video in sorted(
        latest_30_days, key=lambda item: views_per_day(item, now), reverse=True
    )[:10]:
        print(
            f"{views_per_day(video, now):.0f}/day\t"
            f"{video.get('view_count', 0)} views\t"
            f"{engagement(video):.2f}% ER\t"
            f"{label(video)}"
        )


if __name__ == "__main__":
    main()

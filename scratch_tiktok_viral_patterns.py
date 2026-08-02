"""Compara el decil viral del canal con el resto del catalogo de TikTok."""

import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from statistics import median


if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE, "tiktok_own_videos.json")


def text(video):
    return " ".join(
        (video.get("title") or video.get("video_description") or "").split()
    )


def rate(video, field):
    return 100 * video.get(field, 0) / max(video.get("view_count", 0), 1)


def engagement(video):
    return sum(rate(video, field) for field in ("like_count", "comment_count", "share_count"))


def velocity(video, now):
    created = datetime.fromtimestamp(video["create_time"], timezone.utc)
    age_days = max((now - created).total_seconds() / 86400, 0.25)
    return video.get("view_count", 0) / age_days


def summary(name, videos):
    print(name)
    print(f"N={len(videos)}")
    for field in ("view_count", "duration"):
        print(f"MEDIAN_{field.upper()}={median(v.get(field, 0) for v in videos):.2f}")
    print(f"MEDIAN_ER={median(engagement(v) for v in videos):.3f}")
    print(f"MEDIAN_LIKE_RATE={median(rate(v, 'like_count') for v in videos):.3f}")
    print(f"MEDIAN_COMMENT_RATE={median(rate(v, 'comment_count') for v in videos):.3f}")
    print(f"MEDIAN_SHARE_RATE={median(rate(v, 'share_count') for v in videos):.3f}")
    series_pattern = re.compile(r"\bparte\s*\d|\b\d+a?\s+parte", re.I)
    series_rate = 100 * sum(bool(series_pattern.search(text(v))) for v in videos) / len(videos)
    print(f"SERIES_RATE={series_rate:.1f}")


def main():
    with open(DATA_PATH, encoding="utf-8") as handle:
        videos = json.load(handle)["videos"]

    videos = sorted(videos, key=lambda video: video.get("view_count", 0), reverse=True)
    cutoff = max(1, round(len(videos) * 0.10))
    viral = videos[:cutoff]
    rest = videos[cutoff:]
    now = datetime.now(timezone.utc)

    print(f"TOP_DECILE_CUTOFF={viral[-1].get('view_count', 0)}")
    summary("TOP_DECILE", viral)
    summary("REST", rest)

    print("TOP_25_ALL_TIME")
    for index, video in enumerate(videos[:25], 1):
        created = datetime.fromtimestamp(video["create_time"], timezone.utc)
        print(
            f"{index:02d}\t{video.get('view_count', 0)} views\t"
            f"{video.get('duration', 0)}s\t{engagement(video):.2f}% ER\t"
            f"{rate(video, 'share_count'):.3f}% share\t{created:%Y-%m-%d}\t{text(video)[:150]}"
        )

    recent = [
        video
        for video in videos
        if (now - datetime.fromtimestamp(video["create_time"], timezone.utc)).days <= 120
    ]
    print("TOP_20_VELOCITY_120_DAYS")
    for index, video in enumerate(
        sorted(recent, key=lambda item: velocity(item, now), reverse=True)[:20], 1
    ):
        print(
            f"{index:02d}\t{velocity(video, now):.0f}/day\t"
            f"{video.get('view_count', 0)} views\t{video.get('duration', 0)}s\t"
            f"{engagement(video):.2f}% ER\t{text(video)[:150]}"
        )

    patterns = {
        "nadie": r"\bnadie\b",
        "historia": r"\bhistoria\b",
        "murio_muerte": r"\bmuri[oó]\b|\bmuerte\b|\bmorir\b",
        "secreto_oculto": r"\bsecreto\b|\bocult[oa]\b|\bnunca (?:dijo|conto|revelo)\b",
        "conflicto": r"\brechaz[oó]\b|\bexpuls|\bdespid|\bprohib|\bcensur|\bdemand|\btraicion",
        "numero_dinero": r"\$\s*\d|\bmill[oó]n|\bmil\b",
        "pregunta": r"\?",
        "parte": r"\bparte\s*\d|\b\d+a?\s+parte",
    }
    print("HOOK_PATTERN_PREVALENCE")
    for name, pattern in patterns.items():
        v_rate = 100 * sum(bool(re.search(pattern, text(v), re.I)) for v in viral) / len(viral)
        r_rate = 100 * sum(bool(re.search(pattern, text(v), re.I)) for v in rest) / len(rest)
        print(f"{name}\tviral={v_rate:.1f}%\trest={r_rate:.1f}%\tlift={v_rate/max(r_rate, 0.01):.2f}x")

    print("COMMON_HASHTAGS_TOP_DECILE")
    hashtags = Counter()
    for video in viral:
        hashtags.update(tag.lower() for tag in re.findall(r"#\w+", text(video)))
    for tag, count in hashtags.most_common(20):
        print(f"{tag}\t{count}")


if __name__ == "__main__":
    main()

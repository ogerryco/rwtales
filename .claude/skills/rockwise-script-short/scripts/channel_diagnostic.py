"""Audita cada video de TikTok contra cohortes comparables del propio canal."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from statistics import median


if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


SERIES_RE = re.compile(
    r"\b(?:parte\s*(\d+)|(\d+)(?:a|ra|da)?\s+parte)\b", re.IGNORECASE
)
SIGNALS = {
    "historia": re.compile(r"\bhistoria\b", re.IGNORECASE),
    "momento_concreto": re.compile(
        r"\b(?:el d[ií]a|la [uú]ltima|antes de|despu[eé]s de|en 19\d{2}|"
        r"en 20\d{2}|\d+\s+d[ií]as|\d+\s+meses|\d+\s+a[nñ]os)\b",
        re.IGNORECASE,
    ),
    "perdida_muerte": re.compile(
        r"\b(?:muri[oó]|muerte|morir|perdi[oó]|p[eé]rdida|despedida)\b",
        re.IGNORECASE,
    ),
    "revelacion": re.compile(
        r"\b(?:revel[oó]|confes[oó]|explic[oó]|admiti[oó]|"
        r"respuesta|verdad|secreto|ocult[oa])\b",
        re.IGNORECASE,
    ),
    "contradiccion": re.compile(
        r"\b(?:pero|aunque|sin embargo|no fue|nadie esperaba|"
        r"rechaz[oó]|censur[oó]|expulsad[oa]|traici[oó]n)\b",
        re.IGNORECASE,
    ),
    "pregunta": re.compile(r"[?¿]"),
    "dinero_cifra": re.compile(
        r"(?:[$€£]\s*\d|\b\d+\s*(?:millones?|mil)\b)", re.IGNORECASE
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una auditoría CSV por video y un resumen JSON."
    )
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument("--csv", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument(
        "--now",
        help="Fecha de corte ISO-8601; default: ahora en UTC.",
    )
    return parser.parse_args()


def text(video: dict) -> str:
    return " ".join(
        (video.get("title") or video.get("video_description") or "").split()
    )


def rate(video: dict, field: str) -> float:
    return 100 * float(video.get(field, 0) or 0) / max(
        float(video.get("view_count", 0) or 0), 1
    )


def engagement(video: dict) -> float:
    return sum(
        rate(video, field)
        for field in ("like_count", "comment_count", "share_count")
    )


def duration_bucket(seconds: int) -> str:
    if seconds < 60:
        return "<60s"
    if seconds < 180:
        return "60-179s"
    if seconds < 360:
        return "180-359s"
    if seconds < 600:
        return "360-599s"
    return "600s+"


def series_role(caption: str) -> str:
    match = SERIES_RE.search(caption)
    if not match:
        return "standalone"
    number = int(match.group(1) or match.group(2))
    return "part_1" if number == 1 else "sequel"


def percentile_rank(value: float, population: list[float]) -> float:
    if not population:
        return 0
    below_or_equal = sum(item <= value for item in population)
    return 100 * below_or_equal / len(population)


def cohort_for(video: dict, videos: list[dict]) -> list[dict]:
    created = int(video.get("create_time", 0) or 0)
    bucket = duration_bucket(int(video.get("duration", 0) or 0))
    window = 45 * 86400
    cohort = [
        item
        for item in videos
        if abs(int(item.get("create_time", 0) or 0) - created) <= window
        and duration_bucket(int(item.get("duration", 0) or 0)) == bucket
    ]
    if len(cohort) >= 8:
        return cohort
    return [
        item
        for item in videos
        if abs(int(item.get("create_time", 0) or 0) - created) <= 90 * 86400
    ]


def monetization_proxy(views: int) -> str:
    if views < 6500:
        return "probable_bajo_piso"
    if views < 9000:
        return "zona_fronteriza"
    return "volumen_suficiente_no_garantizado"


def action_for(
    views: int,
    er: float,
    share_rate: float,
    role: str,
    top_decile_cutoff: int,
    viral_er: float,
    viral_share: float,
) -> str:
    quality_signal = er >= viral_er or share_rate >= viral_share
    if views >= top_decile_cutoff:
        if share_rate >= viral_share:
            return "replicar_mecanismo_no_tema"
        return "hit_por_alcance_validar_retencion"
    if views < 6500:
        if quality_signal:
            return "buen_contenido_baja_distribucion_reempaquetar"
        return "no_hacer_secuela_reencuadrar_promesa"
    if quality_signal:
        if role == "sequel":
            return "hacerlo_autosuficiente_sin_parte_n"
        return "prometedor_reforzar_search_y_prueba_temprana"
    return "reencuadrar_momento_revelacion_y_share_trigger"


def grouped_summary(rows: list[dict], key: str) -> dict:
    result = {}
    for value in sorted({row[key] for row in rows}):
        group = [row for row in rows if row[key] == value]
        result[value] = {
            "n": len(group),
            "median_views": round(median(row["views"] for row in group), 2),
            "median_engagement_rate": round(
                median(row["engagement_rate"] for row in group), 4
            ),
            "median_share_rate": round(
                median(row["share_rate"] for row in group), 4
            ),
            "monetization_floor_rate": round(
                100
                * sum(row["views"] >= 6500 for row in group)
                / max(len(group), 1),
                2,
            ),
        }
    return result


def main() -> None:
    args = parse_args()
    with args.catalog.open(encoding="utf-8") as handle:
        videos = json.load(handle)["videos"]

    now = (
        datetime.fromisoformat(args.now.replace("Z", "+00:00"))
        if args.now
        else datetime.now(timezone.utc)
    )
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    ranked = sorted(
        videos, key=lambda item: int(item.get("view_count", 0) or 0), reverse=True
    )
    cutoff_n = max(1, round(len(ranked) * 0.10))
    viral = ranked[:cutoff_n]
    top_decile_cutoff = int(viral[-1].get("view_count", 0) or 0)
    viral_er = median(engagement(item) for item in viral)
    viral_share = median(rate(item, "share_count") for item in viral)

    rows = []
    for video in videos:
        caption = text(video)
        created = datetime.fromtimestamp(
            int(video.get("create_time", 0) or 0), timezone.utc
        )
        views = int(video.get("view_count", 0) or 0)
        cohort = cohort_for(video, videos)
        cohort_views = [int(item.get("view_count", 0) or 0) for item in cohort]
        baseline = max(median(cohort_views), 1)
        er = engagement(video)
        share_rate = rate(video, "share_count")
        role = series_role(caption)
        signals = [name for name, pattern in SIGNALS.items() if pattern.search(caption)]
        rows.append(
            {
                "id": str(video.get("id", "")),
                "date_utc": created.strftime("%Y-%m-%d"),
                "age_days": round(max((now - created).total_seconds() / 86400, 0), 2),
                "title": caption,
                "duration_s": int(video.get("duration", 0) or 0),
                "duration_bucket": duration_bucket(
                    int(video.get("duration", 0) or 0)
                ),
                "format": role,
                "views": views,
                "likes": int(video.get("like_count", 0) or 0),
                "comments": int(video.get("comment_count", 0) or 0),
                "shares": int(video.get("share_count", 0) or 0),
                "like_rate": round(rate(video, "like_count"), 4),
                "comment_rate": round(rate(video, "comment_count"), 4),
                "share_rate": round(share_rate, 4),
                "engagement_rate": round(er, 4),
                "cohort_n": len(cohort),
                "cohort_median_views": round(baseline, 2),
                "cohort_view_index": round(views / baseline, 3),
                "cohort_percentile": round(
                    percentile_rank(views, cohort_views), 2
                ),
                "top_decile": views >= top_decile_cutoff,
                "signals": "|".join(signals),
                "monetization_volume_proxy": monetization_proxy(views),
                "next_action": action_for(
                    views,
                    er,
                    share_rate,
                    role,
                    top_decile_cutoff,
                    viral_er,
                    viral_share,
                ),
            }
        )

    fieldnames = list(rows[0].keys())
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["date_utc"], reverse=True))

    recent = [row for row in rows if row["age_days"] <= 120]
    quality_low_distribution = sorted(
        (
            row
            for row in recent
            if row["views"] < top_decile_cutoff
            and (
                row["engagement_rate"] >= viral_er
                or row["share_rate"] >= viral_share
            )
        ),
        key=lambda row: (row["engagement_rate"], row["share_rate"]),
        reverse=True,
    )
    summary = {
        "generated_at": now.isoformat(),
        "source": str(args.catalog),
        "videos": len(rows),
        "top_decile_cutoff": top_decile_cutoff,
        "viral_median_engagement_rate": round(viral_er, 4),
        "viral_median_share_rate": round(viral_share, 4),
        "by_format_all": grouped_summary(rows, "format"),
        "by_format_recent_120d": grouped_summary(recent, "format"),
        "by_duration_all": grouped_summary(rows, "duration_bucket"),
        "by_duration_recent_120d": grouped_summary(recent, "duration_bucket"),
        "recent_120d_count": len(recent),
        "recent_quality_low_distribution": [
            {
                key: row[key]
                for key in (
                    "id",
                    "date_utc",
                    "title",
                    "views",
                    "engagement_rate",
                    "share_rate",
                    "cohort_view_index",
                    "next_action",
                )
            }
            for row in quality_low_distribution[:20]
        ],
        "warnings": [
            "La API publica no entrega retencion, nuevos espectadores, trafico ni ingresos.",
            "El proxy de monetizacion usa solo el piso empirico de views totales; no garantiza vistas relevantes ni pago.",
            "Los indices de cohorte describen asociacion, no causalidad.",
        ],
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    with args.summary.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)

    print(f"VIDEOS={len(rows)}")
    print(f"CSV={args.csv}")
    print(f"SUMMARY={args.summary}")
    print(f"TOP_DECILE_CUTOFF={top_decile_cutoff}")
    print(f"VIRAL_MEDIAN_ER={viral_er:.4f}%")
    print(f"VIRAL_MEDIAN_SHARE={viral_share:.4f}%")


if __name__ == "__main__":
    main()

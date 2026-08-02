import json
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


VIDEO_IDS = [
    "Ti7c6LFWdKY",
    "qatiokz4Z6Q",
    "IZrEYzt5noE",
    "wK8fQgh_wWg",
    "pjH5vCsdZiw",
    "XKu089wZBUk",
    "skgptFdSff4",
    "Ey-xqHXANsE",
    "CeYe6uAjXRs",
    "VOhsjHbsVpI",
    "HRVAWtZ0TmA",
    "77J2I_8mGfE",
]

OUT_DIR = Path(
    r"F:\Google Drive GOG MH\Mi unidad\Rai\geruka\Videos RWT\RWTLat Youtube Long\SE109 Jonathan Davis\00_research\competitor_transcripts"
)


def fmt_time(seconds: float) -> str:
    whole = int(seconds)
    return f"{whole // 60:02d}:{whole % 60:02d}"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    api = YouTubeTranscriptApi()
    summary: list[dict[str, object]] = []

    for video_id in VIDEO_IDS:
        record: dict[str, object] = {"id": video_id, "status": "pending"}
        try:
            fetched = api.fetch(video_id, languages=["es", "en"])
            rows = [
                {"start": item.start, "duration": item.duration, "text": item.text}
                for item in fetched
            ]
            json_path = OUT_DIR / f"{video_id}.json"
            md_path = OUT_DIR / f"{video_id}.md"
            json_path.write_text(
                json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            lines = [f"# Transcript {video_id}", ""]
            lines.extend(f"[{fmt_time(row['start'])}] {row['text']}" for row in rows)
            md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            record.update(
                {
                    "status": "ok",
                    "segments": len(rows),
                    "chars": sum(len(str(row["text"])) for row in rows),
                    "language": getattr(fetched, "language_code", None),
                }
            )
        except Exception as exc:  # noqa: BLE001 - keep batch moving.
            record.update(
                {
                    "status": "error",
                    "error_type": type(exc).__name__,
                    "error": str(exc)[:1000],
                }
            )
        summary.append(record)

    (OUT_DIR / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

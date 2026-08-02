"""
Datos REALES de YouTube Analytics (no proxy) — watch time real, retencion real.
Usa el token OAuth ya autorizado por scratch_analytics_auth.py
"""
import os, sys, json
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
TOKEN_PATH = os.path.join(BASE, ".secrets", "token.json")
SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]
CHANNEL_ID = "UCKEn9E-CE5AXnkNLM531H5A"  # Rockwise Tales
START_DATE = "2026-01-19"  # fecha de creacion del canal

def get_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    return creds

def main():
    creds = get_creds()
    yta = build("youtubeAnalytics", "v2", credentials=creds)

    today = datetime.now().strftime("%Y-%m-%d")

    # ── Totales del canal ──────────────────────────────────────────────
    channel_totals = yta.reports().query(
        ids=f"channel=={CHANNEL_ID}",
        startDate=START_DATE,
        endDate=today,
        metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost",
    ).execute()

    print("="*70)
    print(" TOTALES REALES DEL CANAL (YouTube Analytics)")
    print("="*70)
    headers = [h["name"] for h in channel_totals["columnHeaders"]]
    row = channel_totals.get("rows", [[]])[0] if channel_totals.get("rows") else []
    totals = dict(zip(headers, row))
    minutes_watched = totals.get("estimatedMinutesWatched", 0)
    print(f"Views totales: {totals.get('views', 0):,}")
    print(f"Watch time REAL: {minutes_watched:,} minutos = {minutes_watched/60:,.1f} horas")
    print(f"Duracion promedio de vista: {totals.get('averageViewDuration', 0)} seg")
    print(f"% promedio visto: {totals.get('averageViewPercentage', 0):.1f}%")
    print(f"Subs ganados: {totals.get('subscribersGained', 0)} | perdidos: {totals.get('subscribersLost', 0)}")

    # ── Por video ────────────────────────────────────────────────────────
    per_video = yta.reports().query(
        ids=f"channel=={CHANNEL_ID}",
        startDate=START_DATE,
        endDate=today,
        metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage",
        dimensions="video",
        sort="-estimatedMinutesWatched",
        maxResults=100,
    ).execute()

    print(f"\n{'='*70}")
    print(" TOP VIDEOS POR WATCH TIME REAL")
    print(f"{'='*70}")
    headers2 = [h["name"] for h in per_video["columnHeaders"]]
    rows = per_video.get("rows", [])
    print(f"{'VideoID':<13}{'Views':>9}{'MinReal':>10}{'AvgDurSeg':>11}{'%Visto':>8}")
    for r in rows[:30]:
        d = dict(zip(headers2, r))
        print(f"{d['video']:<13}{d['views']:>9,}{d['estimatedMinutesWatched']:>10,}{d['averageViewDuration']:>11}{d['averageViewPercentage']:>7.1f}%")

    out = {
        "generated": datetime.now().isoformat(),
        "channel_totals": totals,
        "per_video": [dict(zip(headers2, r)) for r in rows],
    }
    out_path = os.path.join(BASE, "rwt_real_analytics.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nGuardado: {out_path}")

if __name__ == "__main__":
    main()

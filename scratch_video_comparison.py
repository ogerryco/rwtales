# -*- coding: utf-8 -*-
"""
Comparacion real (YouTube Analytics API) entre el video de Linkin Park y el de
Scott Weiland en su misma ventana de dias desde publicacion, para decidir
estrategia. No confiar en el resumen de la IA de Studio sin verificar.
"""
import os, sys, json
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
TOKEN_PATH = os.path.join(BASE, ".secrets", "token.json")
SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]
CHANNEL_ID = "UCKEn9E-CE5AXnkNLM531H5A"

VIDEOS = {
    "linkin_park": {"id": "x97VLzuPkf4", "published": "2026-07-21"},
    "weiland": {"id": "SEFwQcg92iA", "published": "2026-07-13"},
}

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

    for name, v in VIDEOS.items():
        vid = v["id"]
        pub = v["published"]
        pub_dt = datetime.strptime(pub, "%Y-%m-%d")
        window_end = (pub_dt + timedelta(days=2)).strftime("%Y-%m-%d")

        print("="*70)
        print(f" {name.upper()}  ({vid})  publicado {pub}  ventana hasta {window_end}")
        print("="*70)

        # Metricas diarias en primeros ~2 dias
        try:
            daily = yta.reports().query(
                ids=f"channel=={CHANNEL_ID}",
                startDate=pub,
                endDate=min(window_end, today),
                metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,comments,shares,subscribersGained",
                dimensions="day",
                filters=f"video=={vid}",
                sort="day",
            ).execute()
            headers = [h["name"] for h in daily["columnHeaders"]]
            print("\n-- Metricas diarias --")
            for row in daily.get("rows", []):
                d = dict(zip(headers, row))
                print(f"  {d['day']}: views={d['views']} avgViewDur={d['averageViewDuration']}s avgViewPct={d['averageViewPercentage']:.1f}% likes={d['likes']} comments={d['comments']} shares={d['shares']} subsGained={d['subscribersGained']}")
        except Exception as e:
            print(f"  [ERROR metricas diarias]: {e}")

        # Fuentes de trafico
        try:
            traffic = yta.reports().query(
                ids=f"channel=={CHANNEL_ID}",
                startDate=pub,
                endDate=today,
                metrics="views,estimatedMinutesWatched",
                dimensions="insightTrafficSourceType",
                filters=f"video=={vid}",
                sort="-views",
            ).execute()
            headers2 = [h["name"] for h in traffic["columnHeaders"]]
            print("\n-- Fuentes de trafico (acumulado) --")
            for row in traffic.get("rows", []):
                d = dict(zip(headers2, row))
                print(f"  {d['insightTrafficSourceType']}: views={d['views']} min={d['estimatedMinutesWatched']}")
        except Exception as e:
            print(f"  [ERROR trafico]: {e}")

        # CTR / impresiones (si el reporte lo soporta)
        try:
            impr = yta.reports().query(
                ids=f"channel=={CHANNEL_ID}",
                startDate=pub,
                endDate=today,
                metrics="impressions,impressionsClickThroughRate",
                filters=f"video=={vid}",
            ).execute()
            headers3 = [h["name"] for h in impr["columnHeaders"]]
            rows3 = impr.get("rows", [])
            if rows3:
                d = dict(zip(headers3, rows3[0]))
                print(f"\n-- Impresiones (acumulado) --\n  impressions={d.get('impressions')} CTR={d.get('impressionsClickThroughRate')}%")
            else:
                print("\n-- Impresiones: sin filas --")
        except Exception as e:
            print(f"  [ERROR impresiones]: {e}")

        # Retencion de audiencia (curva)
        try:
            retention = yta.reports().query(
                ids=f"channel=={CHANNEL_ID}",
                startDate=pub,
                endDate=today,
                metrics="audienceWatchRatio,relativeRetentionPerformance",
                dimensions="elapsedVideoTimeRatio",
                filters=f"video=={vid}",
                sort="elapsedVideoTimeRatio",
            ).execute()
            headers4 = [h["name"] for h in retention["columnHeaders"]]
            rows4 = retention.get("rows", [])
            print(f"\n-- Curva de retencion ({len(rows4)} puntos) --")
            # Mostrar cada ~10%
            for i, row in enumerate(rows4):
                if i % max(1, len(rows4)//10) == 0 or i == len(rows4)-1:
                    d = dict(zip(headers4, row))
                    print(f"  t={float(d['elapsedVideoTimeRatio'])*100:.0f}%  watchRatio={d['audienceWatchRatio']:.3f}  vsCanal={d.get('relativeRetentionPerformance', 'N/A')}")
        except Exception as e:
            print(f"  [ERROR retencion]: {e}")

        print()

if __name__ == "__main__":
    main()

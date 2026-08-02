"""
Revisa el desempeño real del Short de Weiland lanzado ayer y si el CTA
esta generando trafico real hacia el video largo.
Usa el mismo token OAuth de scratch_real_analytics.py + la API publica
para identificar el video.
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
SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly"]
CHANNEL_ID = "UCKEn9E-CE5AXnkNLM531H5A"  # Rockwise Tales

def get_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    return creds

def get_api_key():
    env_path = os.path.join(BASE, "..", "..", ".env")
    env_path = os.path.abspath(env_path)
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("YOUTUBE_API_KEY"):
                return line.split("=", 1)[1].strip()
    return None

def find_recent_uploads(api_key, days_back=3):
    yt = build("youtube", "v3", developerKey=api_key)
    published_after = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ")
    search = yt.search().list(
        part="snippet", channelId=CHANNEL_ID, order="date",
        publishedAfter=published_after, maxResults=15, type="video",
    ).execute()
    ids = [item["id"]["videoId"] for item in search.get("items", [])]
    if not ids:
        return []
    details = yt.videos().list(part="snippet,contentDetails,statistics", id=",".join(ids)).execute()
    return details.get("items", [])

def main():
    api_key = get_api_key()
    if not api_key:
        sys.exit("No se encontro YOUTUBE_API_KEY en .env")

    print("="*70)
    print(" VIDEOS SUBIDOS EN LOS ULTIMOS 3 DIAS")
    print("="*70)
    videos = find_recent_uploads(api_key)
    for v in videos:
        dur = v["contentDetails"]["duration"]
        stats = v.get("statistics", {})
        print(f"\n{v['id']} | {v['snippet']['title']}")
        print(f"  Publicado: {v['snippet']['publishedAt']} | Duracion: {dur}")
        print(f"  Vistas (publicas, API Data): {stats.get('viewCount', 'N/A')} | Likes: {stats.get('likeCount', 'N/A')} | Comentarios: {stats.get('commentCount', 'N/A')}")

    if not videos:
        print("No se encontraron subidas recientes -- revisa CHANNEL_ID o rango de fechas.")
        return

    creds = get_creds()
    yta = build("youtubeAnalytics", "v2", credentials=creds)
    today = datetime.now().strftime("%Y-%m-%d")
    start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    print(f"\n{'='*70}")
    print(" METRICAS REALES (YouTube Analytics) POR VIDEO RECIENTE")
    print(f"{'='*70}")
    for v in videos:
        vid = v["id"]
        try:
            r = yta.reports().query(
                ids=f"channel=={CHANNEL_ID}", startDate=start, endDate=today,
                metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained",
                filters=f"video=={vid}",
            ).execute()
            headers = [h["name"] for h in r["columnHeaders"]]
            row = r.get("rows", [[0]*len(headers)])[0]
            d = dict(zip(headers, row))
            print(f"\n{vid} ({v['snippet']['title'][:50]})")
            print(f"  Views: {d.get('views', 0)} | Watch time: {d.get('estimatedMinutesWatched', 0)} min | %visto promedio: {d.get('averageViewPercentage', 0):.1f}% | Subs ganados: {d.get('subscribersGained', 0)}")
        except Exception as e:
            print(f"  [ERROR analytics para {vid}]: {e}")

    print(f"\n{'='*70}")
    print(" TRAFICO DEL VIDEO LARGO DE WEILAND -- fuentes, ultimos 7 dias")
    print(f"{'='*70}")
    weiland_long_id = input("Pega el video ID del documental LARGO de Weiland: ").strip() if sys.stdin.isatty() else None
    if weiland_long_id:
        r = yta.reports().query(
            ids=f"channel=={CHANNEL_ID}", startDate=start, endDate=today,
            metrics="views,estimatedMinutesWatched",
            dimensions="insightTrafficSourceType",
            filters=f"video=={weiland_long_id}",
            sort="-views",
        ).execute()
        headers = [h["name"] for h in r["columnHeaders"]]
        for row in r.get("rows", []):
            d = dict(zip(headers, row))
            print(f"  {d.get('insightTrafficSourceType'):<30} views={d.get('views')} min={d.get('estimatedMinutesWatched')}")

if __name__ == "__main__":
    main()

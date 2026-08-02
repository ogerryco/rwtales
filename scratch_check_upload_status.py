"""
Diagnostico de estado de subida de un video via YouTube Data API v3.
Usa el token OAuth ya autorizado por scratch_analytics_auth.py
Lista los uploads recientes del canal y su processingDetails/status completo.
"""
import os, sys, json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
TOKEN_PATH = os.path.join(BASE, ".secrets", "token.json")
SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]
CHANNEL_ID = "UCKEn9E-CE5AXnkNLM531H5A"  # Rockwise Tales

def get_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    return creds

def main():
    creds = get_creds()
    yt = build("youtube", "v3", credentials=creds)

    # 1. uploads playlist del canal
    ch = yt.channels().list(part="contentDetails", id=CHANNEL_ID).execute()
    uploads_playlist = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    items = yt.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=uploads_playlist,
        maxResults=15,
    ).execute()

    video_ids = [it["contentDetails"]["videoId"] for it in items["items"]]

    print("="*70)
    print(" ULTIMOS UPLOADS DEL CANAL (playlistItems)")
    print("="*70)
    for it in items["items"]:
        sn = it["snippet"]
        print(f"- {sn['title']}  [videoId={it['contentDetails']['videoId']}]  publicado(playlist)={sn['publishedAt']}")

    if not video_ids:
        print("\nNo hay videos en la playlist de uploads.")
        return

    # 2. status + processingDetails de cada uno
    vids = yt.videos().list(
        part="snippet,status,processingDetails,fileDetails",
        id=",".join(video_ids),
    ).execute()

    print(f"\n{'='*70}")
    print(" DETALLE DE STATUS / PROCESSING POR VIDEO")
    print(f"{'='*70}")
    for v in vids["items"]:
        sn = v["snippet"]
        st = v.get("status", {})
        pd = v.get("processingDetails", {})
        fd = v.get("fileDetails", {})
        print(f"\n--- {sn['title']} ({v['id']}) ---")
        print(f"  publishedAt: {sn.get('publishedAt')}")
        print(f"  status.uploadStatus: {st.get('uploadStatus')}")
        print(f"  status.privacyStatus: {st.get('privacyStatus')}")
        print(f"  status.failureReason: {st.get('failureReason')}")
        print(f"  status.rejectionReason: {st.get('rejectionReason')}")
        print(f"  processingStatus: {pd.get('processingStatus')}")
        print(f"  processingProgress: {pd.get('processingProgress')}")
        print(f"  processingFailureReason: {pd.get('processingFailureReason')}")
        print(f"  fileDetails.status (if present): {fd.get('processingStatus') if fd else 'N/A (needs processingDetails scope/permission)'}")

    out_path = os.path.join(BASE, "scratch_upload_status_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(vids, f, ensure_ascii=False, indent=2)
    print(f"\nGuardado JSON completo: {out_path}")

if __name__ == "__main__":
    main()

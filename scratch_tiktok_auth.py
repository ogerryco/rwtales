"""
Autorizacion OAuth (PKCE) contra el Sandbox de TikTok for Developers y
descarga de datos basicos de la cuenta propia (info + lista de videos).

Requiere:
  .secrets/tiktok_client_key.txt
  .secrets/tiktok_client_secret.txt

Uso:
    python3 scratch_tiktok_auth.py auth      # corre el flujo OAuth completo (una sola vez)
    python3 scratch_tiktok_auth.py fetch     # usa el token guardado para bajar info + videos
"""
import os
import sys
import json
import time
import base64
import hashlib
import secrets
import webbrowser
import http.server
import urllib.parse
import requests

BASE = os.path.dirname(__file__)
SECRETS = os.path.join(BASE, ".secrets")
TOKEN_PATH = os.path.join(SECRETS, "tiktok_token.json")

REDIRECT_URI = "http://localhost:3455/callback/"
PORT = 3455
SCOPES = "user.info.profile,user.info.stats,video.list"
AUTH_URL = "https://www.tiktok.com/v2/auth/authorize/"
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"
USER_INFO_URL = "https://open.tiktokapis.com/v2/user/info/"
VIDEO_LIST_URL = "https://open.tiktokapis.com/v2/video/list/"


def read_secret(name):
    path = os.path.join(SECRETS, name)
    if not os.path.exists(path):
        print(f"Falta {path}")
        sys.exit(1)
    with open(path) as f:
        return f.read().strip()


def make_pkce_pair():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(64)).decode("utf-8")
    verifier = verifier.rstrip("=")[:128]
    # TikTok se desvía del estándar PKCE (RFC 7636): pide el challenge en hex,
    # no en base64url como el resto de proveedores OAuth.
    challenge = hashlib.sha256(verifier.encode("utf-8")).hexdigest()
    return verifier, challenge


_captured = {}


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        _captured["code"] = params.get("code", [None])[0]
        _captured["state"] = params.get("state", [None])[0]
        _captured["error"] = params.get("error", [None])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        if _captured.get("code"):
            msg = "<h2>Autorizado. Ya puedes cerrar esta pestana y volver a la terminal.</h2>"
        else:
            msg = f"<h2>Algo fallo: {_captured.get('error')}</h2>"
        self.wfile.write(msg.encode("utf-8"))

    def log_message(self, format, *args):
        pass  # silenciar logs del servidor


def run_auth_flow():
    client_key = read_secret("tiktok_client_key.txt")
    client_secret = read_secret("tiktok_client_secret.txt")

    verifier, challenge = make_pkce_pair()
    state = secrets.token_urlsafe(16)

    params = {
        "client_key": client_key,
        "scope": SCOPES,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    auth_url = AUTH_URL + "?" + urllib.parse.urlencode(params)

    print("Abriendo tu navegador para que autorices la app...")
    print(f"Si no se abre solo, entra manualmente a:\n{auth_url}\n")
    webbrowser.open(auth_url)

    server = http.server.HTTPServer(("localhost", PORT), CallbackHandler)
    print(f"Esperando la autorizacion en {REDIRECT_URI} ...")
    while "code" not in _captured:
        server.handle_request()

    if _captured.get("error") or not _captured.get("code"):
        print(f"Error en la autorizacion: {_captured.get('error')}")
        sys.exit(1)

    if _captured.get("state") != state:
        print("El 'state' no coincide -- posible problema de seguridad, abortando.")
        sys.exit(1)

    code = urllib.parse.unquote(_captured["code"])
    print("Codigo recibido. Cambiandolo por un access token...")

    resp = requests.post(
        TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "client_key": client_key,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code_verifier": verifier,
        },
    )
    data = resp.json()
    if "access_token" not in data:
        print("No se pudo obtener el access token:")
        print(json.dumps(data, indent=2))
        sys.exit(1)

    data["obtained_at"] = int(time.time())
    os.makedirs(SECRETS, exist_ok=True)
    with open(TOKEN_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Token guardado en {TOKEN_PATH}")
    print(f"Expira en {data.get('expires_in')} segundos (~{data.get('expires_in', 0)//3600}h)")


def load_token():
    if not os.path.exists(TOKEN_PATH):
        print("No hay token guardado -- corre primero: python3 scratch_tiktok_auth.py auth")
        sys.exit(1)
    with open(TOKEN_PATH) as f:
        token = json.load(f)

    obtained_at = token.get("obtained_at", 0)
    expires_in = token.get("expires_in", 0)
    if token.get("access_token") and time.time() < obtained_at + expires_in - 300:
        return token

    refresh_token = token.get("refresh_token")
    if not refresh_token:
        print("El access token expiro y no hay refresh token -- corre: python3 scratch_tiktok_auth.py auth")
        sys.exit(1)

    print("Access token expirado. Renovandolo con el refresh token...")
    resp = requests.post(
        TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "client_key": read_secret("tiktok_client_key.txt"),
            "client_secret": read_secret("tiktok_client_secret.txt"),
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
    )
    data = resp.json()
    if "access_token" not in data:
        print("No se pudo renovar el access token:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        sys.exit(1)

    data["obtained_at"] = int(time.time())
    with open(TOKEN_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print("Access token renovado y guardado.")
    return data


def fetch_data():
    token = load_token()
    access_token = token["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    print("Descargando info de la cuenta...")
    user_fields = "open_id,display_name,follower_count,following_count,likes_count,video_count"
    r = requests.get(USER_INFO_URL, headers=headers, params={"fields": user_fields})
    user_info = r.json()
    if user_info.get("error", {}).get("code") not in (None, "ok"):
        print("TikTok devolvio error al descargar info de la cuenta; no se actualiza el cache.")
        print(json.dumps(user_info, indent=2, ensure_ascii=False))
        sys.exit(1)
    print(json.dumps(user_info, indent=2, ensure_ascii=False))

    print("\nDescargando lista de videos...")
    all_videos = []
    cursor = 0
    video_fields = "id,title,video_description,duration,cover_image_url,view_count,like_count,comment_count,share_count,create_time"
    while True:
        r = requests.post(
            VIDEO_LIST_URL,
            headers={**headers, "Content-Type": "application/json"},
            params={"fields": video_fields},
            json={"max_count": 20, "cursor": cursor},
        )
        page = r.json()
        if page.get("error", {}).get("code") not in (None, "ok"):
            print("TikTok devolvio error al descargar videos; no se actualiza el cache.")
            print(json.dumps(page, indent=2, ensure_ascii=False))
            sys.exit(1)
        videos = page.get("data", {}).get("videos", [])
        all_videos.extend(videos)
        if not page.get("data", {}).get("has_more"):
            break
        cursor = page.get("data", {}).get("cursor", 0)
        if not cursor:
            break

    out_path = os.path.join(BASE, "tiktok_own_videos.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"user_info": user_info, "videos": all_videos}, f, indent=2, ensure_ascii=False)
    print(f"\n{len(all_videos)} videos guardados en {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("auth", "fetch"):
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "auth":
        run_auth_flow()
    else:
        fetch_data()

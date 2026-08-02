"""
Autenticacion OAuth de una sola vez para YouTube Analytics API.
Corre esto UNA vez: abre el navegador, inicias sesion con la cuenta que administra
Rockwise Tales, aceptas el permiso de solo lectura, y guarda un token reutilizable.
"""
import os, sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(__file__)
CLIENT_SECRET = os.path.join(BASE, ".secrets", "client_secret.json")
TOKEN_PATH = os.path.join(BASE, ".secrets", "token.json")
SCOPES = [
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

def main():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            print("Se va a abrir el navegador. Selecciona ogerardo@gmail.com cuando te lo pida.")
            creds = flow.run_local_server(port=0, prompt="select_account")

        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
        print(f"Token guardado en: {TOKEN_PATH}")
    else:
        print("Token ya existe y es valido. No hace falta autenticar de nuevo.")

if __name__ == "__main__":
    main()

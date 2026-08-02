"""
Escanea el audio de un video (o archivo de audio) contra la base de
reconocimiento de AudD para detectar pistas comerciales/de libreria ANTES
de subir a YouTube -- util sobre todo para clips de archivo/entrevistas
que pueden traer musica de fondo ya registrada en Content ID.

Requiere una API key gratuita de AudD: https://dashboard.audd.io/
Guardala en: .secrets/audd_api_key.txt (una sola linea, sin comillas)

Uso:
    python3 scratch_copyright_scan.py ruta/al/video.mp4
    python3 scratch_copyright_scan.py ruta/al/video.mp4 --interval 45 --sample 15
"""
import os, sys, subprocess, tempfile, argparse
import requests
import imageio_ffmpeg

BASE = os.path.dirname(__file__)
API_KEY_PATH = os.path.join(BASE, ".secrets", "audd_api_key.txt")
AUDD_URL = "https://api.audd.io/"


def get_api_key():
    if not os.path.exists(API_KEY_PATH):
        print("No encontre tu API key de AudD.")
        print("1. Registrate gratis en https://dashboard.audd.io/")
        print("2. Copia tu token del dashboard")
        print(f"3. Guardalo en: {API_KEY_PATH}")
        sys.exit(1)
    with open(API_KEY_PATH) as f:
        key = f.read().strip()
    if not key:
        print(f"El archivo {API_KEY_PATH} esta vacio. Pega tu token ahi.")
        sys.exit(1)
    return key


def get_duration(ffmpeg_exe, path):
    result = subprocess.run(
        [ffmpeg_exe, "-i", path],
        stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
    )
    for line in result.stderr.splitlines():
        line = line.strip()
        if line.startswith("Duration:"):
            time_str = line.split(",")[0].replace("Duration: ", "").strip()
            h, m, s = time_str.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError("No se pudo leer la duracion del archivo. ¿Es un video/audio valido?")


def extract_chunk(ffmpeg_exe, path, start, duration, out_path):
    subprocess.run(
        [ffmpeg_exe, "-y", "-ss", str(start), "-i", path, "-t", str(duration),
         "-vn", "-acodec", "libmp3lame", "-ab", "64k", out_path],
        stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
    )


def scan_chunk(api_key, chunk_path):
    with open(chunk_path, "rb") as f:
        resp = requests.post(
            AUDD_URL,
            data={"api_token": api_key, "return": "label"},
            files={"file": f},
            timeout=30,
        )
    return resp.json()


def format_ts(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def main():
    parser = argparse.ArgumentParser(
        description="Escanea audio de un video contra la base de AudD antes de subir a YouTube."
    )
    parser.add_argument("video", help="Ruta al archivo de video o audio")
    parser.add_argument("--interval", type=int, default=45, help="Segundos entre cada muestra (default 45)")
    parser.add_argument("--sample", type=int, default=15, help="Duracion de cada muestra en segundos (default 15)")
    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"No existe el archivo: {args.video}")
        sys.exit(1)

    api_key = get_api_key()
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    print(f"Analizando duracion de {args.video}...")
    duration = get_duration(ffmpeg_exe, args.video)
    print(f"Duracion: {format_ts(duration)}. Muestreando cada {args.interval}s ({args.sample}s por muestra)...\n")

    matches = []
    t = 0.0
    with tempfile.TemporaryDirectory() as tmpdir:
        n = 0
        while t < duration:
            n += 1
            chunk_path = os.path.join(tmpdir, f"chunk_{n}.mp3")
            extract_chunk(ffmpeg_exe, args.video, t, args.sample, chunk_path)
            result = scan_chunk(api_key, chunk_path)

            if result.get("status") == "success" and result.get("result"):
                r = result["result"]
                label = r.get("label", "?")
                print(f"[{format_ts(t)}] RECLAMO POSIBLE: \"{r.get('title')}\" - {r.get('artist')} ({label})")
                matches.append((t, r))
            else:
                print(f"[{format_ts(t)}] limpio")

            t += args.interval

    print("\n" + "=" * 60)
    if matches:
        print(f"Se encontraron {len(matches)} posibles coincidencias de audio comercial:")
        for t, r in matches:
            print(f"  - {format_ts(t)}: \"{r.get('title')}\" - {r.get('artist')}")
        print("\nRevisa estos tramos antes de subir. Que AudD encuentre la pista")
        print("es una señal fuerte de riesgo, pero no es la misma base de datos")
        print("que Content ID de YouTube -- no hay garantia total en ningun sentido.")
    else:
        print("No se encontraron coincidencias comerciales en las muestras.")
        print("Esto NO es garantia total: Content ID de YouTube puede tener")
        print("pistas que AudD no tiene fichadas, y viceversa.")


if __name__ == "__main__":
    main()

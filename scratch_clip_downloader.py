"""
Auto-descarga y corte de clips desde una shot list.
Toma una lista de (URL de YouTube, inicio, fin, nombre) y descarga SOLO
ese fragmento ya recortado -- no el video completo -- listo para arrastrar a CapCut.

Uso:
  python scratch_clip_downloader.py shot_list.json "ruta/de/salida"

Si no se da la ruta de salida, usa ./clips_listos junto a este script.

Formato de shot_list.json:
[
  {"url": "https://youtu.be/VIDEOID", "start": "00:01:23", "end": "00:01:45", "output_name": "01_weiland_detroit.mp4"},
  ...
]
"""
import subprocess, json, os, sys, tempfile

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

TOLERANCE_SEC = 2.0  # diferencia video/audio tolerada antes de considerarlo un corte dañado

def _stream_duration(path, stream):
    cmd = ["ffprobe", "-v", "error", "-select_streams", stream,
           "-show_entries", "stream=duration", "-of", "csv=p=0", path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return float(result.stdout.strip())
    except ValueError:
        return None

def _duration_seconds(hms):
    parts = [float(p) for p in hms.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    h, m, s = parts
    return h * 3600 + m * 60 + s

def _verify_audio_video_match(path):
    """yt-dlp --download-sections a veces corta el audio antes que el video
    (bug observado en vivo: el audio termina segundos antes que el video,
    justo donde empieza el canto). Verificar SIEMPRE después de descargar."""
    vdur = _stream_duration(path, "v:0")
    adur = _stream_duration(path, "a:0")
    if vdur is None or adur is None:
        return False, vdur, adur
    return abs(vdur - adur) <= TOLERANCE_SEC, vdur, adur

def download_clip(url, start, end, output_name, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_name)
    section = f"*{start}-{end}"
    cmd = [
        "yt-dlp",
        "--download-sections", section,
        "-f", "bv*[ext=mp4]+ba[ext=m4a]/mp4/best",
        "--force-keyframes-at-cuts",
        "-o", output_path,
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] {result.stderr[-500:]}")
        return False

    ok, vdur, adur = _verify_audio_video_match(output_path)
    if ok:
        return True

    print(f"  [AVISO] audio ({adur}s) no coincide con video ({vdur}s) -- reintentando con corte local")
    return _redownload_full_and_cut_locally(url, start, end, output_path)

def _redownload_full_and_cut_locally(url, start, end, output_path):
    """Fallback confiable: baja el video completo y corta con ffmpeg localmente
    en vez de pedirle a YouTube el rango directo (que es donde ocurre el bug)."""
    with tempfile.TemporaryDirectory() as tmp:
        full_path = os.path.join(tmp, "full.mp4")
        dl_cmd = ["yt-dlp", "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/mp4/best",
                   "-o", full_path, url]
        dl = subprocess.run(dl_cmd, capture_output=True, text=True)
        if dl.returncode != 0:
            print(f"  [ERROR] no se pudo bajar el video completo: {dl.stderr[-500:]}")
            return False

        duration = _duration_seconds(end) - _duration_seconds(start)
        cut_cmd = ["ffmpeg", "-y", "-ss", start, "-i", full_path, "-t", str(duration),
                   "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-b:a", "192k", output_path]
        cut = subprocess.run(cut_cmd, capture_output=True, text=True)
        if cut.returncode != 0:
            print(f"  [ERROR] no se pudo cortar localmente: {cut.stderr[-500:]}")
            return False

        ok, vdur, adur = _verify_audio_video_match(output_path)
        if not ok:
            print(f"  [ERROR] sigue sin coincidir después del corte local: video {vdur}s / audio {adur}s")
            return False
        return True

def main(clips_file, output_dir):
    with open(clips_file, encoding="utf-8") as f:
        clips = json.load(f)

    ok, fail = 0, 0
    for i, c in enumerate(clips, 1):
        print(f"[{i}/{len(clips)}] {c['output_name']} ({c['start']}-{c['end']}) <- {c['url']}")
        if download_clip(c["url"], c["start"], c["end"], c["output_name"], output_dir):
            ok += 1
        else:
            fail += 1

    print(f"\nListo: {ok} clips descargados y verificados (audio=video), {fail} con error.")
    print(f"Carpeta: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Uso: python scratch_clip_downloader.py shot_list.json [ruta_de_salida]")
    default_dir = os.path.join(os.path.dirname(__file__), "clips_listos")
    out_dir = sys.argv[2] if len(sys.argv) > 2 else default_dir
    main(sys.argv[1], out_dir)

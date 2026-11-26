"""JEDEN lektor marki (szef 26.11.2026): edge-tts en-US-AndrewNeural (naturalny meski glos, darmowy) zamiast piper hfc_male.
Uzycie jak piper:  "<tekst>" | python tools/reel/lektor.py -f wyjscie.wav [--rate -4%]
Wynik: WAV mono 22050 Hz (jak piper), wiec reszta potoku (audio_reel, kino, raport) dziala bez zmian.
Gdy edge-tts nie dziala (brak sieci do speech.platform.bing.com), zwraca kod 3 - wtedy uzyj piper jako zapasu."""
import sys, io, asyncio, subprocess, shutil, os, argparse
GLOS = "en-US-AndrewNeural"
def ffmpeg():
    for p in (shutil.which("ffmpeg"),
              r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"):
        if p and os.path.exists(p): return p
    raise SystemExit("brak ffmpeg")
def main():
    a = argparse.ArgumentParser(); a.add_argument("-f", required=True); a.add_argument("--rate", default="+0%"); a.add_argument("--glos", default=GLOS)
    a.add_argument("-t", default=None)
    o, _ = a.parse_known_args()
    txt = (o.t if o.t is not None else sys.stdin.buffer.read().decode("utf-8")).strip()
    try:
        import edge_tts
        async def z():
            b = io.BytesIO()
            async for ch in edge_tts.Communicate(txt, o.glos, rate=o.rate).stream():
                if ch["type"] == "audio": b.write(ch["data"])
            return b.getvalue()
        mp3 = asyncio.run(z())
        if not mp3: raise RuntimeError("pusto")
    except Exception as e:
        print(f"lektor: edge-tts niedostepny ({e})", file=sys.stderr); sys.exit(3)
    r = subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", "pipe:0", "-ac", "1", "-ar", "22050", "-c:a", "pcm_s16le", o.f], input=mp3)
    sys.exit(r.returncode)
if __name__ == "__main__": main()

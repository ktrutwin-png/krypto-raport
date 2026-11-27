"""JEDEN lektor marki (szef 26.11.2026): edge-tts en-US-AndrewNeural (naturalny meski glos, darmowy) zamiast piper hfc_male.
Uzycie jak piper:  "<tekst>" | python tools/reel/lektor.py -f wyjscie.wav [--rate -4%] [--pitch -8Hz]
27.11 (Z049): --pitch / LEKTOR_PITCH (np. -8Hz dla Christophera w karuzeli 10:00), domyslnie +0Hz.
Wynik: WAV mono 22050 Hz (jak piper), wiec reszta potoku (audio_reel, kino, raport) dziala bez zmian.
Gdy edge-tts nie dziala (brak sieci do speech.platform.bing.com), zwraca kod 3 - wtedy uzyj piper jako zapasu."""
import sys, io, asyncio, subprocess, shutil, os, argparse
GLOS = os.environ.get("LEKTOR_GLOS", "en-US-AndrewNeural")   # wyjatki (np. film o szefie): LEKTOR_GLOS / LEKTOR_RATE
def ffmpeg():
    for p in (shutil.which("ffmpeg"),
              r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"):
        if p and os.path.exists(p): return p
    raise SystemExit("brak ffmpeg")
def main():
    a = argparse.ArgumentParser(); a.add_argument("-f", required=True); a.add_argument("--rate", default=os.environ.get("LEKTOR_RATE", "+0%")); a.add_argument("--glos", default=GLOS)
    a.add_argument("--pitch", default=os.environ.get("LEKTOR_PITCH", "+0Hz"))
    a.add_argument("-t", default=None)
    o, _ = a.parse_known_args()
    txt = (o.t if o.t is not None else sys.stdin.buffer.read().decode("utf-8")).strip()
    try:
        import edge_tts
        SLOWA = []   # 26.11: czasy slow do napisow karaoke (tools/napisy) -> <plik>.words.json
        async def z():
            b = io.BytesIO()
            async for ch in edge_tts.Communicate(txt, o.glos, rate=o.rate, pitch=o.pitch, boundary="WordBoundary").stream():
                if ch["type"] == "audio": b.write(ch["data"])
                elif ch["type"] == "WordBoundary":
                    s = ch["offset"] / 1e7; SLOWA.append([round(s, 3), round(s + ch["duration"] / 1e7, 3), ch["text"]])
            return b.getvalue()
        mp3 = asyncio.run(z())
        if not mp3: raise RuntimeError("pusto")
        import json
        json.dump({"tekst": txt, "slowa": SLOWA}, open(o.f + ".words.json", "w", encoding="utf-8"), ensure_ascii=False)
    except Exception as e:
        print(f"lektor: edge-tts niedostepny ({e})", file=sys.stderr); sys.exit(3)
    r = subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", "pipe:0", "-ac", "1", "-ar", "22050", "-c:a", "pcm_s16le", o.f], input=mp3)
    sys.exit(r.returncode)
if __name__ == "__main__": main()

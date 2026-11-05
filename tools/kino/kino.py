"""KINO: filmowy Reel 9:16 z lektorem (styl "news cinematic", od 5.11.2026).
Uzycie: python3 kino.py <folder>   (folder zawiera scenes.json + obrazy scen)
scenes.json:
{ "date": "05.11.2026", "mood": "gold", "handle": "@erl.grey83",
  "scenes": [ {"img": "s1.jpg", "big": "+$100", "sub": "GOLD IN 48 HOURS", "say": "tekst lektora...", "move": "in"}, ... ] }
move: in | out | up | down | left | right  (wolny ruch kamery). big/sub mozna pominac.
Obrazy najlepiej pionowe 9:16 (AI, fotorealistyczne). Wynik: reel.mp4 (1080x1920, 30 fps) + cover.jpg.
Glos: piper en_US-joe-medium (tools/reel/voice/), muzyka: tools/reel/music.py, sciszana pod glosem."""
import json, os, subprocess, sys, wave, asyncio
D = os.path.abspath(sys.argv[1]); HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.join(HERE, "..", "reel")
VOICE = os.environ.get("KINO_VOICE", os.path.join(REEL, "voice", "en_US-joe-medium.onnx"))
W, H, FPS, FADE = 1080, 1920, 30, 0.6
CFG = json.load(open(os.path.join(D, "scenes.json"))); S = CFG["scenes"]
def run(c, **k): subprocess.run(c, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, **k)
os.chdir(D)

CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>html,body{margin:0;width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:Inter,sans-serif}
.hd{position:absolute;top:110px;width:100%;text-align:center;color:#f2f6ff;text-shadow:0 2px 10px #000c}
.hd .h{font:600 34px Inter;letter-spacing:1px}.hd .ln{width:190px;height:2px;margin:16px auto 12px;background:linear-gradient(90deg,transparent,#00f0ff,#ff2bd6,transparent)}
.hd .d{font:500 24px Inter;opacity:.8;letter-spacing:2px}
.g{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(transparent,rgba(3,2,10,.82))}
.gt{position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(rgba(3,2,10,.7),transparent)}
.big{position:absolute;bottom:560px;width:100%;text-align:center;font:900 150px Inter;color:#fff;letter-spacing:-2px;
 text-shadow:0 0 30px rgba(0,240,255,.35),0 6px 30px #000e}
.sub{position:absolute;bottom:480px;width:100%;text-align:center;font:800 40px Inter;letter-spacing:6px;color:#00f0ff;text-shadow:0 2px 14px #000}
.tag{position:absolute;bottom:150px;width:100%;text-align:center;font:500 22px Inter;color:#fff9;letter-spacing:1px}
</style>"""
async def overlays():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": W, "height": H})
        hd = f'<div class="gt"></div><div class="hd"><div class="h">{CFG.get("handle","@erl.grey83")}</div><div class="ln"></div><div class="d">{CFG["date"]}</div></div><div class="g"></div><div class="tag">For information only · not investment advice</div>'
        await pg.set_content(CSS + hd); await pg.wait_for_timeout(900)
        await pg.screenshot(path="_hd.png", omit_background=True)
        for i, s in enumerate(S):
            html = (f'<div class="big">{s["big"]}</div>' if s.get("big") else "") + (f'<div class="sub">{s["sub"]}</div>' if s.get("sub") else "")
            await pg.set_content(CSS + html); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"_t{i}.png", omit_background=True)
        await b.close()
asyncio.run(overlays())

# lektor: segment na scene, dlugosc sceny = glos + oddech
DUR = []
for i, s in enumerate(S):
    run([sys.executable, "-m", "piper", "-m", VOICE, "--length-scale", "1.04", "--sentence-silence", "0.25", "-f", f"_a{i}.wav"], input=s["say"].encode())
    w = wave.open(f"_a{i}.wav"); d = w.getnframes() / w.getframerate(); w.close()
    L = round(d + 0.55 + (FADE if i < len(S) - 1 else 1.0), 2); DUR.append(L)
    run(["ffmpeg", "-y", "-i", f"_a{i}.wav", "-af", f"adelay=250|250,apad=whole_dur={L - (FADE if i < len(S)-1 else 0):.2f},aresample=44100", "-ac", "2", f"_p{i}.wav"])
open("_l.txt", "w").write("".join(f"file '_p{i}.wav'\n" for i in range(len(S))))

MOVES = {"in": ("1.0+0.10*t/{L}", "(iw-ow)/2", "(ih-oh)/2"), "out": ("1.10-0.10*t/{L}", "(iw-ow)/2", "(ih-oh)/2"),
         "up": ("1.08", "(iw-ow)/2", "(ih-oh)*(1-t/{L})"), "down": ("1.08", "(iw-ow)/2", "(ih-oh)*t/{L}"),
         "left": ("1.08", "(iw-ow)*(1-t/{L})", "(ih-oh)/2"), "right": ("1.08", "(iw-ow)*t/{L}", "(ih-oh)/2")}
clips = []
for i, (s, L) in enumerate(zip(S, DUR)):
    z, x, y = [e.format(L=L) for e in MOVES.get(s.get("move", "in" if i % 2 == 0 else "out"), MOVES["in"])]
    # plynny ruch: skaluj obraz klatka po klatce (scale z eval=frame) i przytnij - bez "schodkow" zoompan
    flt = (f"[0]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},setsar=1,"
           f"scale=w='{W}*({z})':h='{H}*({z})':eval=frame:flags=bicubic,crop={W}:{H}:x='{x}':y='{y}',"
           f"eq=contrast=1.06:saturation=1.08,format=rgba[bg];"
           f"[bg][1]overlay=0:0[a];[2]format=rgba,fade=t=in:st=0.7:d=0.5:alpha=1[t];[a][t]overlay=0:0,format=yuv420p")
    run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-t", str(L), "-i", s["img"], "-loop", "1", "-t", str(L), "-i", "_hd.png",
         "-loop", "1", "-t", str(L), "-i", f"_t{i}.png", "-filter_complex", flt, "-t", str(L), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", f"_c{i}.mp4"])
    clips.append(f"_c{i}.mp4")
# przejscia
inp = sum([["-i", c] for c in clips], []); chain = ""; off = 0; last = "[0]"
for i in range(1, len(clips)):
    off += DUR[i - 1] - FADE; out = f"[x{i}]"
    chain += f"{last}[{i}]xfade=transition={'fade' if i % 2 else 'smoothleft'}:duration={FADE}:offset={off:.2f}{out};"; last = out
T = sum(DUR) - FADE * (len(DUR) - 1)
run(["ffmpeg", "-y", *inp, "-filter_complex", chain + f"{last}format=yuv420p[v]", "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "_v.mp4"])
# dzwiek: lektor + muzyka sciszana pod glosem
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-af", f"atrim=0:{T}", "_vo.wav"])
run([sys.executable, os.path.join(REEL, "music.py"), str(T + 1), CFG.get("mood", "calm")])
FX = {"tense": "lowpass=f=6000,aecho=0.8:0.6:310|690:0.35|0.25",          # horror: ciemny, duzo pogłosu
      "uplift": "highpass=f=70,aecho=0.8:0.75:140|290|560|1100:0.38|0.3|0.22|0.15"}  # niebo: jasny, katedralny pogłos
run(["ffmpeg", "-y", "-i", "melody.wav", "-af", FX.get(CFG.get("mood", "calm"), "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2"), "_mel.wav"])
VOL = {"tense": 0.9, "uplift": 0.78}.get(CFG.get("mood", "calm"), 0.68)  # szef 5.11: melodia odrobine glosniej, horror bardzo wyrazny
mix = (f"[0]aresample=44100,aformat=channel_layouts=stereo,volume={VOL}[m];[1]aresample=44100,aformat=channel_layouts=stereo,"
       "equalizer=f=140:t=q:w=1:g=3,asplit[v1][v2];[m][v1]sidechaincompress=threshold=0.02:ratio=3.5:attack=30:release=500:makeup=1[duck];"
       "[duck][v2]amix=inputs=2:normalize=0:weights=1 1.3,loudnorm=I=-14:TP=-1.5:LRA=7[out]")
run(["ffmpeg", "-y", "-i", "_mel.wav", "-i", "_vo.wav", "-filter_complex", mix, "-map", "[out]", "-t", str(T), "-ar", "44100", "-c:a", "aac", "-b:a", "192k", "_m.m4a"])
run(["ffmpeg", "-y", "-i", "_v.mp4", "-i", "_m.m4a", "-shortest", "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart", "reel.mp4"])
run(["ffmpeg", "-y", "-ss", "1.6", "-i", "reel.mp4", "-frames:v", "1", "-q:v", "2", "cover.jpg"])
for f in os.listdir("."):
    if f.startswith("_") or f == "melody.wav": os.remove(f)
print("reel.mp4", round(T, 1), "s", DUR)

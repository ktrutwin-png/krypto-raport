"""KINO: Reel 9:16 z lektorem. Domyslny styl "news" (od 6.11.2026, wzor szefa: grube naglowki u gory,
holograficzne sceny z wykresami, szybki energiczny lektor, na koncu plansza "This Is Not Financial Advice").
Uzycie: python3 kino.py <folder>   (folder: scenes.json + obrazy scen)
scenes.json:
{ "date": "06.11.2026", "mood": "gold", "handle": "@erl.grey83", "style": "news",
  "scenes": [ {"img": "s1.jpg", "tag": "LIVE MARKET UPDATE",
               "head": ["GOLD $4,100 -", "*HOLDS THE* *$4,070 FLOOR*"],   # *tekst* = zolty, ~tekst~ = zielony
               "sub": "+$100 IN 48 HOURS",                                # zielona linia pod naglowkiem (opcjonalnie)
               "note": "FIRST TEST AFTER JOBS DATA",                       # ciemna ramka w dolnej czesci, wchodzi w polowie sceny
               "chip": "▲ +1.6%",                                          # maly znaczek pod naglowkiem
               "say": "lektor...", "move": "in"}, ... ] }
Na koncu automatycznie plansza "This Is Not Financial Advice! Just data. @handle" (2,2 s).
style "cinema" = stary wyglad (duza liczba "big" + "sub" na srodku).
Glos: piper en_US-ryan-high (energiczny meski), obnizony o ~10% (KINO_PITCH, domyslnie 0.9); KINO_VOICE nadpisuje model.
Wynik: reel.mp4 (1080x1920, 30 fps) + cover.jpg."""
import json, os, subprocess, sys, wave, asyncio, re, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
D = os.path.abspath(sys.argv[1]); HERE = os.path.dirname(os.path.abspath(__file__)); REEL = os.path.join(HERE, "..", "reel")
VDIR = os.path.join(REEL, "voice")
if not os.environ.get("KINO_VOICE") and not os.path.exists(os.path.join(VDIR, "en_US-ryan-high.onnx")):  # glos wzorcowy szefa – pobierz raz
    os.makedirs(VDIR, exist_ok=True)
    env = dict(os.environ, no_proxy="", NO_PROXY="")
    for f in ("en_US-ryan-high.onnx", "en_US-ryan-high.onnx.json"):
        subprocess.run(["curl", "-sSfL", "-o", os.path.join(VDIR, f), "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/ryan/high/" + f], env=env)
VOICE =os.environ.get("KINO_VOICE") or next((os.path.join(VDIR, v) for v in ("en_US-ryan-high.onnx", "en_US-joe-medium.onnx") if os.path.exists(os.path.join(VDIR, v))), "")
PITCH = float(os.environ.get("KINO_PITCH", "0.9" if "ryan" in VOICE else "1.0"))
FPS, FADE = 30, 0.45
CFG = json.load(open(os.path.join(D, "scenes.json"))); WIDE = CFG.get("format") == "landscape"; W, H_ = (1920, 1080) if WIDE else (1080, 1920); SS = 1.25 if WIDE else 2; S = list(CFG["scenes"]); STYLE = CFG.get("style", "news")
HANDLE = CFG.get("handle", "@erl.grey83")
if STYLE == "news":  # zgodnosc ze starym formatem scen (big/sub) -> naglowek u gory
    for s in S:
        if not s.get("head") and s.get("big"):
            s["head"] = [s.pop("big")] + ([f"*{s.pop('sub')}*"] if s.get("sub") else [])
S.append({"img": S[-1]["img"], "end": True, "say": "", "move": "in"})
def run(c, **k): subprocess.run(c, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, **k)
os.chdir(D)

def rich(t):
    t = H.escape(t)
    t = re.sub(r"\*(.+?)\*", r'<span class="y">\1</span>', t)
    return re.sub(r"~(.+?)~", r'<span class="g">\1</span>', t)

CSS = """<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>html,body{margin:0;width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:Inter,sans-serif}
.y{color:#ffd23f}.g{color:#3dff8f}
.gt{position:absolute;left:0;right:0;top:0;height:820px;background:linear-gradient(rgba(2,4,14,.88),rgba(2,4,14,.55) 60%,transparent)}
.gb{position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(transparent,rgba(2,4,14,.75))}
.hd{position:absolute;top:88px;left:54px;color:#fff;font:700 30px Inter;text-shadow:0 2px 8px #000}
.hd b{display:block;font:500 22px Inter;opacity:.75;letter-spacing:2px;margin-top:4px}
.dis{position:absolute;top:96px;right:54px;text-align:right;font:500 20px Inter;color:#fffa;text-shadow:0 2px 6px #000}
.wrap{position:absolute;top:190px;left:50px;right:50px;transform:skewX(-6deg)}
.tag{display:inline-block;background:#0a1a3a;border:2px solid #2ad1ff;color:#fff;font:800 26px Inter;letter-spacing:2px;padding:8px 16px;margin-bottom:18px;box-shadow:0 0 22px rgba(42,209,255,.45)}
.head{font:400 118px/1.02 Anton;color:#fff;text-transform:uppercase;letter-spacing:1px;
 text-shadow:0 0 2px #000,4px 6px 0 #000,0 0 30px rgba(0,0,0,.8)}
.sub{margin-top:14px;font:400 62px/1.05 Anton;color:#3dff8f;text-transform:uppercase;text-shadow:3px 4px 0 #000}
.chip{display:inline-block;margin-top:20px;font:800 44px Inter;color:#3dff8f;background:rgba(0,0,0,.45);padding:6px 16px;border-radius:8px}
.chip.r{color:#ff4d5e}
.note{position:absolute;left:60px;right:60px;bottom:520px;transform:skewX(-4deg);background:rgba(4,8,22,.86);border-left:8px solid #ffd23f;
 padding:26px 30px;font:400 64px/1.08 Anton;color:#fff;text-transform:uppercase;box-shadow:0 10px 40px rgba(0,0,0,.6)}
.tk{display:inline-block;white-space:nowrap;height:64px;line-height:64px;padding:0 30px;background:rgba(4,8,22,.88);border-top:2px solid #2ad1ff;border-bottom:2px solid #2ad1ff;font:800 34px Inter;color:#fff;letter-spacing:1px}
.tk .u{color:#3dff8f}.tk .d{color:#ff4d5e}
.chap{position:absolute;top:150px;right:54px;font:800 22px Inter;letter-spacing:3px;color:#2ad1ff}
.end{position:absolute;inset:0;background:rgba(3,5,14,.86);display:flex;flex-direction:column;align-items:center;justify-content:center}
.end .a{font:400 76px Anton;color:#ffd23f;text-transform:uppercase;text-align:center;line-height:1.1}
.end .b{font:700 40px Inter;color:#fff;margin-top:26px}
/* cinema */
.big{position:absolute;bottom:560px;width:100%;text-align:center;font:900 150px Inter;color:#fff;letter-spacing:-2px;text-shadow:0 0 30px rgba(0,240,255,.35),0 6px 30px #000e}
.csub{position:absolute;bottom:480px;width:100%;text-align:center;font:800 40px Inter;letter-spacing:6px;color:#00f0ff;text-shadow:0 2px 14px #000}
</style>"""
CSS_L = """<style>.gt{height:100%;background:linear-gradient(90deg,rgba(2,4,14,.92),rgba(2,4,14,.62) 45%,rgba(2,4,14,.1) 75%)}.gb{height:300px}
.hd{top:40px;left:80px}.dis{top:44px;right:70px}.wrap{top:140px;left:80px;right:auto;width:1050px}.head{font-size:96px}.sub{font-size:52px}
.note{left:80px;right:auto;width:960px;bottom:150px;font-size:54px}.end .a{font-size:96px}.chap{position:absolute;top:40px;left:50%;transform:translateX(-50%);font:800 24px Inter;letter-spacing:4px;color:#2ad1ff}</style>"""
if WIDE: CSS = CSS.replace("width:1080px;height:1920px", "width:1920px;height:1080px") + CSS_L

async def overlays():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": W, "height": H_})
        async def shot(body, path):
            await pg.set_content(CSS + body); await pg.wait_for_timeout(700)
            await pg.screenshot(path=path, omit_background=True)
        await shot(f'<div class="gt"></div><div class="gb"></div><div class="hd">{H.escape(HANDLE)}<b>{H.escape(CFG["date"])}</b></div>'
                   f'<div class="dis">For information only · not investment advice</div>', "_hd.png")
        if CFG.get("ticker"):
            t = H.escape(CFG["ticker"]); t = re.sub(r"(▲[^·]*)", r'<span class="u">\1</span>', t); t = re.sub(r"(▼[^·]*)", r'<span class="d">\1</span>', t)
            await pg.set_viewport_size({"width": 6000, "height": 70})
            await pg.set_content(CSS.replace(f"width:{W}px;height:{H_}px", "width:6000px;height:70px") + f'<div class="tk" id="tk">{t} &nbsp;·&nbsp; {t} &nbsp;·&nbsp;</div>')
            await pg.wait_for_timeout(700); await (await pg.query_selector("#tk")).screenshot(path="_tk.png", omit_background=True)
            await pg.set_viewport_size({"width": W, "height": H_})
        for i, s in enumerate(S):
            if s.get("end"):
                await shot(f'<div class="end"><div class="a">This is not<br>financial advice!</div><div class="b">Just data. {H.escape(HANDLE)}</div></div>', f"_t{i}.png")
                await shot("", f"_n{i}.png"); continue
            if STYLE == "cinema":
                body = (f'<div class="big">{rich(s["big"])}</div>' if s.get("big") else "") + (f'<div class="csub">{rich(s["sub"])}</div>' if s.get("sub") else "")
                await shot(body, f"_t{i}.png"); await shot("", f"_n{i}.png"); continue
            head = "<br>".join(rich(x) for x in s.get("head", []))
            chip = s.get("chip", ""); cls = "chip r" if chip.startswith(("▼", "-", "−")) else "chip"
            body = (f'<div class="chap">{rich(s["chap"])}</div>' if s.get("chap") else "") + ('<div class="wrap">' + (f'<div class="tag">{rich(s["tag"])}</div><br>' if s.get("tag") else "")
                    + f'<div class="head">{head}</div>' + (f'<div class="sub">{rich(s["sub"])}</div>' if s.get("sub") else "")
                    + (f'<div class="{cls}">{H.escape(chip)}</div>' if chip else "") + "</div>")
            await shot(body, f"_t{i}.png")
            await shot(f'<div class="note">{rich(s["note"])}</div>' if s.get("note") else "", f"_n{i}.png")
        await b.close()
asyncio.run(overlays())

# lektor: segment na scene; dlugosc sceny = glos + oddech
DUR = []
for i, s in enumerate(S):
    last = i == len(S) - 1
    if s.get("end") or not s.get("say", "").strip():
        L = 2.2; run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", f"{L - (0 if last else FADE):.2f}", f"_p{i}.wav"]); DUR.append(L); continue
    assert VOICE and os.path.exists(VOICE), "brak glosu piper w tools/reel/voice (patrz tools/reel/README.md)"
    run([sys.executable, "-m", "piper", "-m", VOICE, "--length-scale", "0.96", "--sentence-silence", "0.18", "-f", f"_a{i}.wav"], input=s["say"].encode())
    w = wave.open(f"_a{i}.wav"); d = w.getnframes() / w.getframerate(); sr = w.getframerate(); w.close()
    L = round(d + 0.35 + (0 if last else FADE), 2); DUR.append(L)
    pf = f"asetrate={int(sr*PITCH)},aresample={sr},atempo={1/PITCH:.4f}," if PITCH != 1.0 else ""
    run(["ffmpeg", "-y", "-i", f"_a{i}.wav", "-af", f"{pf}adelay=120|120,apad=whole_dur={L - (0 if last else FADE):.2f},aresample=44100", "-ac", "2", f"_p{i}.wav"])
open("_l.txt", "w").write("".join(f"file '_p{i}.wav'\n" for i in range(len(S))))

MOVES = {"in": ("1.0+0.09*t/{L}", "(iw-ow)/2", "(ih-oh)/2"), "out": ("1.09-0.09*t/{L}", "(iw-ow)/2", "(ih-oh)/2"),
         "up": ("1.08", "(iw-ow)/2", "(ih-oh)*(1-t/{L})"), "down": ("1.08", "(iw-ow)/2", "(ih-oh)*t/{L}"),
         "left": ("1.08", "(iw-ow)*(1-t/{L})", "(ih-oh)/2"), "right": ("1.08", "(iw-ow)*t/{L}", "(ih-oh)/2")}
clips = []
for i, (s, L) in enumerate(zip(S, DUR)):
    z, x, y = [e.format(L=L) for e in MOVES.get(s.get("move", "in" if i % 2 == 0 else "out"), MOVES["in"])]
    nt = max(0.6, L * 0.38)
    end = s.get("end")
    flt = (f"[0]scale={int(W*SS)}:{int(H_*SS)}:force_original_aspect_ratio=increase,crop={int(W*SS)}:{int(H_*SS)},setsar=1,"
           f"scale=w='{W}*({z})':h='{H_}*({z})':eval=frame:flags=bicubic,crop={W}:{H_}:x='{x}':y='{y}',"
           f"eq=contrast=1.07:saturation=1.12{',boxblur=18:2' if end else ''},format=rgba[bg];"
           + ("[bg]null[a];" if end else "[bg][1]overlay=0:0[a];")
           + (f"[2]format=rgba[t];" if i == 0 else f"[2]format=rgba,fade=t=in:st=0.05:d=0.28:alpha=1[t];")  # plan wzrostu: naglowek widoczny od klatki 0
           + "[a][t]overlay=0:0[b];"
           f"[3]format=rgba,fade=t=in:st={nt:.2f}:d=0.3:alpha=1[n];[b][n]overlay=0:0,format=yuv420p")
    extra = []; k = 4; flt = flt.replace(",format=yuv420p", "[z0]", 1) if flt.endswith(",format=yuv420p") else flt; cur = "[z0]"
    a = s.get("anim")
    if a and not end:   # ruchome swieczki (anim.py)
        import anim
        an = a if isinstance(a, dict) else {"type": "candles", "dir": str(a)}
        bx = an.get("box", [1060, 260, 780, 420] if WIDE else [60, 770, 960, 400])
        anim.candles(f"_an{i}.mov", L, an.get("dir", "up"), an.get("label", ""), w=bx[2], h=bx[3], seed=7 + i)
        extra += ["-i", f"_an{i}.mov"]; flt += f";[{k}]format=rgba,fade=t=in:st=0.25:d=0.35:alpha=1[an];{cur}[an]overlay={bx[0]}:{bx[1]}[z1]"; cur = "[z1]"; k += 1
    if CFG.get("ticker") and not end and os.path.exists("_tk.png"):   # przewijany pasek z cenami
        extra += ["-loop", "1", "-t", str(L), "-i", "_tk.png"]
        flt += f";{cur}[{k}]overlay=x='-mod((t+{i*3})*150,overlay_w/2)':y={CFG.get("ticker_y", 990 if WIDE else 1470)}[z2]"; cur = "[z2]"; k += 1
    flt += f";{cur}format=yuv420p"
    run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-t", str(L), "-i", s["img"], "-loop", "1", "-t", str(L), "-i", "_hd.png",
         "-loop", "1", "-t", str(L), "-i", f"_t{i}.png", "-loop", "1", "-t", str(L), "-i", f"_n{i}.png", *extra,
         "-filter_complex", flt, "-t", str(L), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", f"_c{i}.mp4"])
    clips.append(f"_c{i}.mp4")
inp = sum([["-i", c] for c in clips], []); chain = ""; off = 0; last = "[0]"
for i in range(1, len(clips)):
    off += DUR[i - 1] - FADE; out = f"[x{i}]"
    tr = "fade" if (i == len(clips) - 1 or i % 2) else "smoothleft"
    chain += f"{last}[{i}]xfade=transition={tr}:duration={FADE}:offset={off:.2f}{out};"; last = out
T = sum(DUR) - FADE * (len(DUR) - 1)
run(["ffmpeg", "-y", *inp, "-filter_complex", chain + f"{last}format=yuv420p[v]", "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "_v.mp4"])
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-af", f"atrim=0:{T}", "_vo.wav"])
run([sys.executable, os.path.join(REEL, "music.py"), str(T + 1), CFG.get("mood", "calm")])
FX = {"tense": "lowpass=f=6000,aecho=0.8:0.6:310|690:0.35|0.25",          # horror: ciemny, duzo pogłosu
      "uplift": "highpass=f=70,aecho=0.8:0.75:140|290|560|1100:0.38|0.3|0.22|0.15"}  # niebo: jasny, katedralny pogłos
run(["ffmpeg", "-y", "-i", "melody.wav", "-af", FX.get(CFG.get("mood", "calm"), "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2"), "_mel.wav"])
VOL = {"tense": 0.9, "uplift": 0.78}.get(CFG.get("mood", "calm"), 0.68)  # szef 5.11: melodia odrobine glosniej, horror bardzo wyrazny
mix = (f"[0]aresample=44100,aformat=channel_layouts=stereo,volume={VOL}[m];[1]aresample=44100,aformat=channel_layouts=stereo,"
       "equalizer=f=150:t=q:w=1:g=2.5,acompressor=threshold=0.12:ratio=3:attack=5:release=120,asplit[v1][v2];"
       "[m][v1]sidechaincompress=threshold=0.02:ratio=3.5:attack=30:release=500:makeup=1[duck];"
       "[duck][v2]amix=inputs=2:normalize=0:weights=1 1.35,loudnorm=I=-14:TP=-1.5:LRA=7[out]")
run(["ffmpeg", "-y", "-i", "_mel.wav", "-i", "_vo.wav", "-filter_complex", mix, "-map", "[out]", "-t", str(T), "-ar", "44100", "-c:a", "aac", "-b:a", "192k", "_m.m4a"])
run(["ffmpeg", "-y", "-i", "_v.mp4", "-i", "_m.m4a", "-shortest", "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart", "reel.mp4"])
run(["ffmpeg", "-y", "-ss", "1.2", "-i", "reel.mp4", "-frames:v", "1", "-q:v", "2", "cover.jpg"])
for f in ([] if os.environ.get("KINO_KEEP") else os.listdir(".")):
    if f.startswith("_") or f == "melody.wav": os.remove(f)
print("reel.mp4", round(T, 1), "s", DUR)

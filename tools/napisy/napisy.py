"""NAPISY KARAOKE do Reeli (szef 26.11.2026: „napisy nie byle jakie – sprawdź jak to robią inni”).
Standard 2026 (opus.pro, blitzcut, kapwing, captions.ai): słowo po słowie, gruby bezszeryfowy krój (Anton), biały z czarnym
obrysem, JEDEN kolor akcentu na aktualnym słowie (nasz złoty #ffd23f), 1–3 słowa naraz, nad dolną martwą strefą Reels
(min. ~480 px od dołu) i w środkowych 80% szerokości.
Wejście: czasy słów z tools/reel/lektor.py (<plik.wav>.words.json).
Użycie w kodzie:  from napisy import ass, wypal
   ass([(start_s, "_a0.wav.words.json"), ...], "_napisy.ass");  wypal("in.mp4", "_napisy.ass", "out.mp4")"""
import json, os, re, subprocess, shutil
TU = os.path.dirname(os.path.abspath(__file__)); FONTY = os.path.join(TU, "fonty")
AKCENT = "&H003FD2FF"          # #ffd23f (BGR) – złoty marki
Y = 1150                       # środek linii napisów (1080x1920): pod twarzą, nad ramką "note" (bottom 520) i martwą strefą
ROZMIAR = 104
MAX_SLOW, MAX_ZN = 3, 18
def _t(s):
    s = max(0, s); h = int(s // 3600); m = int(s % 3600 // 60); return f"{h}:{m:02d}:{s % 60:05.2f}"
def _esc(w): return w.replace("{", "(").replace("}", ")").replace("\\", "")
def grupy(tekst, slowa):
    """Dzieli słowa na grupy 1–3, z przerwą po znaku interpunkcyjnym (szukamy go w oryginalnym tekście)."""
    out, cur, poz = [], [], 0
    for st, en, w in slowa:
        i = tekst.find(w, poz); nast = ""
        if i >= 0:
            poz = i + len(w); nast = tekst[poz:poz + 1]
        cur.append([st, en, w + (nast if nast in ",.!?;:" else "")])
        dl = sum(len(x[2]) + 1 for x in cur)
        if len(cur) >= MAX_SLOW or dl >= MAX_ZN or nast in ".!?;:,":
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def ass(segmenty, wyj, szer=1080, wys=1920):
    linie = []
    for start, plik in segmenty:
        if not os.path.exists(plik): continue
        d = json.load(open(plik, encoding="utf-8")); G = grupy(d["tekst"], d["slowa"])
        for gi, g in enumerate(G):
            koniec_g = g[-1][1] + 0.18
            if gi + 1 < len(G): koniec_g = min(koniec_g + 0.25, G[gi + 1][0][0])
            for k, (st, en, w) in enumerate(g):
                od = g[0][0] if k == 0 else st
                do = g[k + 1][0] if k + 1 < len(g) else koniec_g
                txt = " ".join(("{\\c" + AKCENT + "\\fscx110\\fscy110}" + _esc(x[2]).upper() + "{\\r}") if j == k else _esc(x[2]).upper()
                               for j, x in enumerate(g))
                pop = "{\\fad(60,0)}" if k == 0 else ""
                linie.append(f"Dialogue: 0,{_t(start + od)},{_t(start + do)},K,,0,0,0,,{pop}{{\\pos({szer // 2},{Y})}}{txt}")
    nag = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {szer}
PlayResY: {wys}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: K,Anton,{ROZMIAR},&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,6,3,5,110,110,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open(wyj, "w", encoding="utf-8").write(nag + "\n".join(linie) + "\n")
    return len(linie)
def wypal(wej, plik_ass, wyj, ffmpeg="ffmpeg"):
    """Wypala napisy (libass + font Anton z tools/napisy/fonty). Ścieżki względne – działa też na Windows."""
    kat = os.path.dirname(os.path.abspath(plik_ass)); fl = os.path.join(kat, "napisy_fonty")   # bez "_" – kino kasuje pliki "_*" zwyklym os.remove
    if not os.path.exists(fl): shutil.copytree(FONTY, fl)
    vf = f"ass={os.path.basename(plik_ass)}:fontsdir=napisy_fonty"
    subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-i", os.path.abspath(wej), "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", os.path.abspath(wyj)], check=True, cwd=kat)

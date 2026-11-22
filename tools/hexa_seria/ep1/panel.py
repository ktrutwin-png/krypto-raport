"""Hexa Ep.1 – animowany panel scen + napisy (1080x840, 30 fps) -> stdout rawvideo rgb24.
Użycie: python3 panel.py words.json DLUGOSC_S | ffmpeg -f rawvideo -pix_fmt rgb24 -s 1080x840 -r 30 -i - ...
"""
import json, math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 840, 30
words = [w for w in json.load(open(sys.argv[1]))["words"] if w["type"] == "word" and not w["text"].startswith("[") and not w["text"].endswith("]")]
DUR = float(sys.argv[2])
ANTON = "/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
INTER_B = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
INTER_K = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
f_head = ImageFont.truetype(ANTON, 96)
f_cap = ImageFont.truetype(INTER_B, 44)
f_lab = ImageFont.truetype(INTER_K, 34)
f_big = ImageFont.truetype(ANTON, 150)
f_stamp = ImageFont.truetype(ANTON, 120)

GOLD = (255, 196, 64); CYAN = (42, 209, 255); MAG = (232, 70, 255); RED = (255, 60, 80); BLUE = (70, 140, 255)
BG = (7, 10, 30)

def wt(txt, n=1):
    """czas startu n-tego wystąpienia słowa"""
    c = 0
    for w in words:
        if w["text"].lower().strip(".,:!?") == txt:
            c += 1
            if c == n: return w["start"]
    raise KeyError(txt)

SC = [  # (start, headline, akcent)
    (0.0, ["HI, I'M ", ("HEXA", GOLD)]),
    (3.95, ["ONE AI ", ("BRAIN", GOLD)]),
    (9.5, [("34", GOLD), " WORKERS"]),
    (15.06, ["DEMO ", ("ONLY", RED)]),
    (20.85, ["OPEN-SOURCE ", ("PIECES", CYAN)]),
    (26.4, ["DRAW ", ("YOUR OWN", GOLD), " MAP"]),
]

# frazy napisów = zdania
phr, cur = [], []
for w in words:
    cur.append(w)
    if w["text"][-1] in ".:," and len(cur) >= 3 or w["text"][-1] in ".:" or len(cur) >= 5:
        phr.append(cur); cur = []
if cur: phr.append(cur)

def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3

def base():
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    for x in range(0, W, 60): d.line([(x, 0), (x, H)], fill=(14, 20, 52))
    for y in range(0, H, 60): d.line([(0, y), (W, y)], fill=(14, 20, 52))
    d.line([(0, 0), (W, 0)], fill=CYAN, width=3)
    return im
BASE = base()

def glow_layer(size=(W, H)):
    return Image.new("RGBA", size, (0, 0, 0, 0))

def hexpts(cx, cy, r, rot=0):
    return [(cx + r * math.cos(math.radians(60 * i + 30 + rot)), cy + r * math.sin(math.radians(60 * i + 30 + rot))) for i in range(6)]

def lerp(a, b, k): return tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3))

CX, CY = W // 2, 430
random.seed(7)
ORB = [(i, 120 + 70 * (i % 2), random.random() * 6.28, (0.35 + random.random() * .3) * (1 if i % 2 else -1)) for i in range(34)]
CAND = []; p = 100
for i in range(22):
    o = p; p = p + random.uniform(-6, 7); hi = max(o, p) + random.uniform(1, 4); lo = min(o, p) - random.uniform(1, 4); CAND.append((o, p, hi, lo))
HEXGRID = [(0, 0)] + [(math.cos(math.radians(60 * i)), math.sin(math.radians(60 * i))) for i in range(6)] + \
          [(2 * math.cos(math.radians(60 * i)), 2 * math.sin(math.radians(60 * i))) for i in range(6)] + \
          [(math.cos(math.radians(60 * i)) + math.cos(math.radians(60 * i + 60)), math.sin(math.radians(60 * i)) + math.sin(math.radians(60 * i + 60))) for i in range(6)]
HEXFROM = [(random.uniform(-700, 700), random.uniform(-500, 500), random.uniform(-90, 90)) for _ in HEXGRID]
HEXCOL = [random.choice([CYAN, MAG, GOLD, BLUE]) for _ in HEXGRID]

def draw_scene(i, t, g, d):
    ts = t - SC[i][0]
    if i == 0:
        k = ease(ts / 1.2); col = lerp(BLUE, GOLD, ease((ts - 1.0) / 1.5))
        r = 40 + 150 * k
        gd = ImageDraw.Draw(g)
        gd.polygon(hexpts(CX, CY, r, ts * 12), outline=col + (255,), width=10)
        gd.ellipse([CX - r * .45, CY - r * .45, CX + r * .45, CY + r * .45], outline=col + (255,), width=8)
        gd.line([(CX - r * .3, CY + r * .2), (CX - r * .05, CY - r * .05), (CX + r * .1, CY + r * .1), (CX + r * .35, CY - r * .25)], fill=col + (255,), width=8)
    elif i == 1:
        gd = ImageDraw.Draw(g); pul = 1 + .08 * math.sin(ts * 5)
        r = 95 * ease(ts / .6) * pul
        for rr, a in ((r * 1.6, 60), (r * 1.25, 120), (r, 255)):
            gd.ellipse([CX - rr, CY - rr, CX + rr, CY + rr], fill=GOLD + (a,))
        for j, (wd, ang) in enumerate((("plans", 210), ("checks", 330), ("fixes", 90))):
            k = ease((t - wt(wd)) / .4)
            if k <= 0: continue
            ex, ey = CX + 290 * math.cos(math.radians(ang)) * k, CY + 210 * math.sin(math.radians(ang)) * k
            gd.line([(CX, CY), (ex, ey)], fill=CYAN + (255,), width=5)
            gd.ellipse([ex - 14, ey - 14, ex + 14, ey + 14], fill=CYAN + (255,))
            lab = ["PLAN", "CHECK", "FIX"][j]; tw = d.textlength(lab, font=f_lab)
            d.text((ex - tw / 2, ey + (22 if ang != 210 and ang != 330 else -62)), lab, font=f_lab, fill=(255, 255, 255))
    elif i == 2:
        gd = ImageDraw.Draw(g)
        gd.ellipse([CX - 55, CY - 55, CX + 55, CY + 55], fill=GOLD + (255,))
        t0 = wt("thirty-four"); n = int(34 * ease((t - t0 + .2) / 1.3))
        for j, rad, ph, sp in ORB[:n]:
            a = ph + sp * ts; x, y = CX + rad * 1.55 * math.cos(a), CY + rad * math.sin(a)
            col = GOLD if j % 3 else CYAN
            gd.ellipse([x - 11, y - 11, x + 11, y + 11], fill=col + (255,))
        s = str(n); tw = d.textlength(s, font=f_big)
        d.text((70, 140), s, font=ImageFont.truetype(ANTON, 110), fill=GOLD)
        for j, (wd, lab) in enumerate((("videos", "VIDEOS"), ("markets", "MARKETS"), ("server", "SERVER"))):
            k = ease((t - wt(wd)) / .3)
            if k > 0:
                x = 70 + j * 330 + int(60 * (1 - k)); y = 640
                gd.rounded_rectangle([x - 14, y - 6, x + 300, y + 52], 10, outline=CYAN + (int(255 * k),), width=4)
                d.text((x + 8, y), lab, font=f_lab, fill=(255, 255, 255))
    elif i == 3:
        gd = ImageDraw.Draw(g); n = min(len(CAND), int(ts * 7) + 1)
        lo_all = min(c[3] for c in CAND); hi_all = max(c[2] for c in CAND)
        sy = lambda v: 640 - (v - lo_all) / (hi_all - lo_all) * 420
        for j, (o, c, hi, lo) in enumerate(CAND[:n]):
            x = 110 + j * 40; col = (61, 255, 143) if c >= o else RED
            gd.line([(x, sy(hi)), (x, sy(lo))], fill=col + (255,), width=3)
            gd.rectangle([x - 12, sy(max(o, c)), x + 12, sy(min(o, c)) + 2], fill=col + (255,))
        k = ease((t - wt("demo")) / .25)
        if k > 0:
            st = Image.new("RGBA", (720, 200), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
            sd.rounded_rectangle([6, 6, 714, 194], 16, outline=RED + (255,), width=12)
            tw = sd.textlength("DEMO ONLY", font=f_stamp); sd.text(((720 - tw) / 2, 18), "DEMO ONLY", font=f_stamp, fill=RED + (255,))
            sc = 1.6 - .6 * k; st = st.resize((int(720 * sc), int(200 * sc))).rotate(-8, expand=True)
            g.alpha_composite(st, (CX - st.width // 2, CY - st.height // 2))
        fl = t - wt("never")
        if 0 < fl < .7:
            gd.rectangle([8, 8, W - 8, H - 8], outline=RED + (int(255 * (1 - fl / .7)),), width=18)
    elif i == 4 or i == 5:
        gd = ImageDraw.Draw(g); R = 52; sp = R * 1.8
        brk = (t - wt("pieces", 2)) if i == 5 else -1
        for j, ((gx, gy), (fx, fy, fr)) in enumerate(zip(HEXGRID, HEXFROM)):
            k = ease((t - SC[4][0] - j * .17) / .9)
            x = CX + gx * sp; y = CY + gy * sp
            if brk > 0:
                kb = ease(brk / 2.5); x += fx * .55 * kb; y += fy * .25 * kb; rot = fr * kb
            else:
                x = x + fx * (1 - k); y = y + fy * (1 - k); rot = fr * (1 - k)
            if k <= 0: continue
            col = HEXCOL[j]
            gd.polygon(hexpts(x, y, R - 6, rot), fill=col + (int(70 * k),), outline=col + (int(255 * k),), width=6)
        if i == 4:
            k = ease((t - wt("magic")) / .3)
            if 0 < k and t < wt("just"):
                tw = d.textlength("NO MAGIC BUTTON", font=f_lab); x = (W - tw) / 2
                d.text((x, 165), "NO MAGIC BUTTON", font=f_lab, fill=(255, 255, 255))
                d.line([(x - 10, 186), (x + tw + 10, 186)], fill=RED, width=6)
            if t >= wt("just"):
                tw = d.textlength("JUST HONEST WORK", font=f_lab); d.text(((W - tw) / 2, 165), "JUST HONEST WORK", font=f_lab, fill=GOLD)

def headline(d, parts, k):
    x = 54; y = 30 - int(30 * (1 - k))
    for p in parts:
        txt, col = (p, (255, 255, 255)) if isinstance(p, str) else p
        d.text((x + 4, y + 5), txt, font=f_head, fill=(0, 0, 0))
        d.text((x, y), txt, font=f_head, fill=col); x += d.textlength(txt, font=f_head)

def caption(d, t):
    ph = None
    for p in phr:
        if p[0]["start"] - .05 <= t <= p[-1]["end"] + .35: ph = p
    if not ph: return
    txt = " ".join(w["text"] for w in ph); tw = d.textlength(txt, font=f_cap)
    x = (W - tw) / 2; y = 735
    d.rounded_rectangle([x - 24, y - 14, x + tw + 24, y + 62], 14, fill=(0, 0, 0))
    for w in ph:
        col = GOLD if w["start"] <= t else (255, 255, 255)
        d.text((x, y), w["text"], font=f_cap, fill=col); x += d.textlength(w["text"] + " ", font=f_cap)

out = sys.stdout.buffer
for fi in range(int(DUR * FPS)):
    t = fi / FPS
    i = max(j for j, s in enumerate(SC) if s[0] <= t)
    im = BASE.copy(); g = glow_layer(); d = ImageDraw.Draw(im)
    draw_scene(i, t, g, ImageDraw.Draw(im))
    blur = g.filter(ImageFilter.GaussianBlur(16))
    im = im.convert("RGBA"); im.alpha_composite(blur); im.alpha_composite(blur); im.alpha_composite(g)
    im = im.convert("RGB"); d = ImageDraw.Draw(im)
    draw_scene_text = None
    # etykiety tekstowe scen rysowane na im (ponownie, bez glow)
    if i in (1, 2, 4):
        tmp = glow_layer(); draw_scene(i, t, tmp, d)
    headline(d, SC[i][1], ease((t - SC[i][0]) / .35))
    caption(d, t)
    out.write(im.tobytes())

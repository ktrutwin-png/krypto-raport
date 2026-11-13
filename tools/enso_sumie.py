"""Enso ERL.GREY83 w stylu sumi-e: tusz na papierze washi, suchy pedzel, zloto, czerwona pieczec."""
import numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.ndimage import gaussian_filter

W = H = 2000
rng = np.random.default_rng(83)

# --- papier washi
def paper():
    base = np.ones((H, W, 3)) * np.array([236, 226, 205]) / 255
    n = gaussian_filter(rng.normal(0, 1, (H, W)), 2.5) * 0.025 + gaussian_filter(rng.normal(0, 1, (H, W)), 40) * 0.05
    img = base + n[..., None]
    # wlokna
    fib = np.zeros((H, W))
    for _ in range(2500):
        x, y = rng.uniform(0, W), rng.uniform(0, H); a = rng.uniform(0, math.pi); L = rng.uniform(15, 70)
        for t in np.linspace(0, 1, int(L)):
            xi, yi = int(x + math.cos(a) * L * t + math.sin(t * 6) * 2), int(y + math.sin(a) * L * t)
            if 0 <= xi < W and 0 <= yi < H: fib[yi, xi] += 1
    fib = gaussian_filter(fib, 0.7)
    img -= fib[..., None] * 0.05
    # winieta
    yy, xx = np.mgrid[0:H, 0:W]; r = np.hypot(xx - W / 2, yy - H / 2) / (W * 0.72)
    img *= (1 - 0.18 * r ** 2.2)[..., None]
    return np.clip(img, 0, 1)

def stroke(ink, path, wmax, nb=160, dry_from=0.62, seed=1, press=None):
    """path: lista (x,y); pedzel z wlosiem - kazdy wlos ma wlasny zapas tuszu."""
    r = np.random.default_rng(seed)
    off = r.uniform(-1, 1, nb); load = r.uniform(0.75, 1.15, nb); thin = r.uniform(0.6, 1.4, nb)
    P = np.array(path); n = len(P)
    tang = np.gradient(P, axis=0); tang /= np.linalg.norm(tang, axis=1, keepdims=True) + 1e-9
    nor = np.stack([-tang[:, 1], tang[:, 0]], 1)
    for i in range(n):
        u = i / (n - 1)
        p = press(u) if press else 1.0
        w = wmax * p
        for b in range(nb):
            amt = load[b] - u * (0.55 + 0.6 * abs(off[b]))           # tusz konczy sie szybciej na brzegach
            if u > dry_from: amt -= (u - dry_from) * r.uniform(0.6, 2.4)  # suchy pedzel (kasure)
            if amt <= 0.02 or r.random() < max(0, (u - dry_from)) * 0.9: continue
            x, y = P[i] + nor[i] * off[b] * w * 0.5
            xi, yi = int(x), int(y); rad = max(1, int(thin[b] * wmax / 70))
            if 0 <= xi < W and 0 <= yi < H:
                ink[max(0, yi - rad):yi + rad + 1, max(0, xi - rad):xi + rad + 1] = np.maximum(
                    ink[max(0, yi - rad):yi + rad + 1, max(0, xi - rad):xi + rad + 1], min(1, amt))

cx, cy, R = W * 0.5, H * 0.47, 640
ink = np.zeros((H, W))
# 1) Enso - jeden ruch, otwarte (przerwa po prawej), start u dolu-prawo, zgodnie z kierunkiem malowania
a0, sweep = math.radians(-125), math.radians(318)
pts = []
for k in range(2600):
    u = k / 2599; a = a0 + sweep * u
    rr = R * (1 + 0.025 * math.sin(u * 7) + 0.012 * math.sin(u * 19))
    pts.append((cx + rr * math.cos(-a + math.pi), cy + rr * math.sin(-a + math.pi) * 0.98))
stroke(ink, pts, 170, nb=220, dry_from=0.58, seed=7, press=lambda u: (0.35 + 0.65 * min(1, u * 9) ** 0.6) * (1.0 - 0.35 * u))

# 2) heksagon - cienki pedzel, kilka pociagniec
hR = 300
hv = [(cx + hR * math.cos(math.radians(-90 + 60 * i)), cy + hR * math.sin(math.radians(-90 + 60 * i))) for i in range(7)]
for i in range(6):
    (x1, y1), (x2, y2) = hv[i], hv[i + 1]
    seg = [(x1 + (x2 - x1) * t + rng.normal(0, 0.6), y1 + (y2 - y1) * t) for t in np.linspace(-0.06, 1.06, 400)]
    stroke(ink, seg, 26, nb=40, dry_from=0.8, seed=20 + i, press=lambda u: 0.75 + 0.25 * math.sin(u * math.pi))

ink = gaussian_filter(ink, 1.1)
# rozlanie tuszu w papier (lekki rozmyty halo)
halo = gaussian_filter(ink, 6) * 0.25
dens = np.clip(ink * 0.93 + halo, 0, 1)

img = paper()
inkc = np.array([18, 16, 20]) / 255
img = img * (1 - dens[..., None]) + inkc * dens[..., None]

# 3) zlota linia wzrostu (zloty platek / kintsugi) - wychodzi poza kolo
gold = np.zeros((H, W))
gp = [(-0.42, 0.30), (-0.16, 0.08), (0.02, 0.19), (0.40, -0.26)]
path = []
for j in range(3):
    (x1, y1), (x2, y2) = gp[j], gp[j + 1]
    for t in np.linspace(0, 1, 500):
        path.append((cx + (x1 + (x2 - x1) * t) * R, cy + (y1 + (y2 - y1) * t) * R))
stroke(gold, path, 46, nb=70, dry_from=0.85, seed=99, press=lambda u: 0.8 + 0.2 * math.sin(u * math.pi))
ex, ey = path[-1]
yy, xx = np.mgrid[0:H, 0:W]
gold = np.maximum(gold, (np.hypot(xx - ex, yy - ey) < 34).astype(float))
gold = gaussian_filter(gold, 1.0)
sheen = 0.5 + 0.5 * np.sin((xx * 0.7 + yy * 1.3) / 55.0) * gaussian_filter(rng.normal(0, 1, (H, W)), 3) * 3
gcol = np.stack([0.79 + 0.15 * sheen, 0.62 + 0.14 * sheen, 0.24 + 0.08 * sheen], -1)
gcol = np.clip(gcol + (rng.random((H, W, 1)) > 0.995) * 0.25, 0, 1)   # drobinki zlota
img = img * (1 - gold[..., None]) + gcol * gold[..., None]

out = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8))

# 4) pieczec hanko + podpis pionowy
d = ImageDraw.Draw(out)
cjk = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
seal = Image.new("RGBA", (190, 190), (0, 0, 0, 0)); sd = ImageDraw.Draw(seal)
sd.rounded_rectangle([4, 4, 186, 186], 10, fill=(178, 34, 30, 235))
f = ImageFont.truetype(cjk, 74, index=0)
sd.text((95, 52), "円", font=f, fill=(244, 230, 214, 255), anchor="mm")
sd.text((95, 132), "相", font=f, fill=(244, 230, 214, 255), anchor="mm")
sa = np.array(seal).astype(float); m = gaussian_filter(rng.random((190, 190)), 1.2) > 0.42
sa[..., 3] *= np.where(m, 1, 0.55); seal = Image.fromarray(sa.astype(np.uint8)).rotate(-2, resample=Image.BICUBIC)
out.paste(seal, (1630, 1580), seal)
fv = ImageFont.truetype(cjk, 58, index=0)
for i, ch in enumerate("道は自ら描く"):   # „drogę rysujesz sam”
    d.text((1720, 640 + i * 76), ch, font=fv, fill=(30, 26, 28), anchor="mm")
fl = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 40, index=0)
d.text((W // 2, 1855), "E R L . G R E Y 8 3", font=fl, fill=(70, 60, 55), anchor="mm")
out = out.filter(ImageFilter.UnsharpMask(1.2, 40, 2))
out.save("Enso_sumie.png"); out.resize((1000, 1000), Image.LANCZOS).save("Enso_sumie_podglad.jpg", quality=90)
print("ok")

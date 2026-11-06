"""Ruchome grafiki do KINO (od 6.11.2026): zywe swieczki rysowane klatka po klatce.
candles(out_mov, L, direction="up"|"down"|"chop", label="$4,100", w=960, h=460, seed=7)
-> przezroczysty film .mov (png) z panelem: swieczki pojawiaja sie po kolei, ostatnia "zyje" (cena drga),
swiecaca linia ceny z etykieta, delikatna siatka. Nakladany w kino.py nad obrazem sceny."""
import numpy as np, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont

GREEN, RED, CYAN, GOLD = (61, 255, 143), (255, 77, 94), (42, 209, 255), (255, 210, 63)

def _font(sz):
    for f in ("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try: return ImageFont.truetype(f, sz)
        except OSError: pass
    return ImageFont.load_default()

def _series(n, direction, seed):
    r = np.random.default_rng(seed)
    drift = {"up": 0.55, "down": -0.55, "chop": 0.0}.get(direction, 0.4)
    o = [100.0]; c = []; hi = []; lo = []
    for k in range(n):
        ch = drift + r.normal(0, 1.25)
        if direction in ("up", "down") and k > n * 0.72: ch += drift * 1.6   # koncowe przyspieszenie = efekt "wybicia"
        cl = o[-1] + ch; c.append(cl)
        hi.append(max(o[-1], cl) + abs(r.normal(0, 0.7))); lo.append(min(o[-1], cl) - abs(r.normal(0, 0.7)))
        o.append(cl)
    return np.array(o[:-1]), np.array(c), np.array(hi), np.array(lo)

def candles(out, L, direction="up", label="", w=960, h=460, seed=7, fps=30, n=28):
    O, C, Hh, Lw = _series(n, direction, seed)
    fnt, fnt_s = _font(34), _font(20)
    tagw = ImageDraw.Draw(Image.new("RGBA", (8, 8))).textlength(label or "000.0", font=fnt)
    pad_l, pad_r, pad_t, pad_b = 26, int(max(150, tagw + 60)), 26, 26
    lo_, hi_ = Lw.min() - 1, Hh.max() + 1
    Y = lambda v: pad_t + (hi_ - v) / (hi_ - lo_) * (h - pad_t - pad_b)
    cw = (w - pad_l - pad_r) / n
    base = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(base)
    d.rounded_rectangle([0, 0, w - 1, h - 1], 18, fill=(4, 10, 30, 170), outline=CYAN + (150,), width=2)
    for gy in range(1, 5):
        yy = pad_t + gy * (h - pad_t - pad_b) / 5; d.line([(pad_l, yy), (w - pad_r + 10, yy)], fill=(80, 140, 200, 40), width=1)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-",
                          "-c:v", "png", "-pix_fmt", "rgba", out], stdin=subprocess.PIPE)
    total = int(L * fps); reveal = max(1, int(total * 0.72)); rng = np.random.default_rng(seed + 1)
    for f in range(total):
        k = min(n, 1 + int(f / reveal * n)) if f < reveal else n          # ile swieczek widac
        prog = (f / reveal * n) % 1 if f < reveal else 1.0                 # postep ostatniej swieczki
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
        for j in range(k):
            o, c, hh, ll = O[j], C[j], Hh[j], Lw[j]
            if j == k - 1:   # zywa swieczka: rosnie i drga
                live = o + (c - o) * min(1.0, prog * 1.15) + rng.normal(0, 0.18)
                c, hh, ll = live, max(o, live) + (hh - max(o, c)) * prog, min(o, live) - (min(o, c) - ll) * prog
            col = GREEN if c >= o else RED
            x0 = pad_l + j * cw + cw * 0.18; x1 = pad_l + (j + 1) * cw - cw * 0.18; xm = (x0 + x1) / 2
            dr.line([(xm, Y(hh)), (xm, Y(ll))], fill=col + (255,), width=3)
            y0, y1 = sorted((Y(o), Y(c))); dr.rectangle([x0, y0, x1, max(y1, y0 + 3)], fill=col + (255,))
        last = c
        glow = im.filter(ImageFilter.GaussianBlur(7))
        frame = Image.alpha_composite(base, glow); frame = Image.alpha_composite(frame, im)
        fd = ImageDraw.Draw(frame); yl = Y(last); col = GREEN if last >= O[0] else RED
        for xx in range(pad_l, int(w - pad_r + 6), 18): fd.line([(xx, yl), (xx + 9, yl)], fill=GOLD + (200,), width=2)
        tag = label or f"{last:.1f}"
        tw = fd.textlength(tag, font=fnt); bx = w - pad_r + 12
        fd.rounded_rectangle([bx, yl - 26, bx + max(tw + 24, 120), yl + 26], 8, fill=(10, 16, 40, 235), outline=GOLD + (255,), width=2)
        fd.text((bx + 12, yl - 21), tag, font=fnt, fill=GOLD + (255,))
        live = "● LIVE" if (f // 15) % 2 == 0 else "○ LIVE"
        fd.text((pad_l + 6, 8), live, font=fnt_s, fill=col + (230,))
        p.stdin.write(frame.tobytes())
    p.stdin.close(); p.wait()

if __name__ == "__main__":
    import sys; candles(sys.argv[1], float(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "up", sys.argv[4] if len(sys.argv) > 4 else "")

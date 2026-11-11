# Żywe tło (szef 11.11: „samo tło żeby się lekko ruszało”) – warstwa RGBA nakładana na nieruchome tło sceny:
# pulsująca poświata w punkcie zbiegu, przelatujący błysk neonu, delikatny deszcz, migoczące iskry, odbicia na podłodze.
# Pętla 4 s (płynnie się zapętla). Wynik: plik .mov (qtrle, z przezroczystością), cache w tym folderze.
# Użycie: python zywe_tlo.py W H FPS [vx vy] -> drukuje ścieżkę pliku
import os, sys, subprocess, numpy as np

def make(W, H, FPS=30, vp=(0.5, 0.36), sec=4.0, out=None):
    out = out or os.path.join(os.path.dirname(os.path.abspath(__file__)), f"_fx_{W}x{H}_{int(vp[0]*100)}_{int(vp[1]*100)}.mov")
    if os.path.exists(out) and os.path.getsize(out) > 1000: return out
    N = int(sec * FPS); rng = np.random.default_rng(11)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # poświata w punkcie zbiegu (kolor cyjan->fiolet)
    d = np.hypot((xx - vp[0] * W) / W, (yy - vp[1] * H) / W)
    glow = np.clip(1 - d / 0.42, 0, 1) ** 2
    gcol = np.stack([0.55 + 0.35 * np.clip(d / 0.4, 0, 1), 0.8 - 0.3 * np.clip(d / 0.4, 0, 1), np.ones_like(d)], -1)  # RGB 0-1
    # maska podłogi (dolne ~35 %)
    floor = np.clip((yy / H - 0.64) / 0.16, 0, 1)
    # deszcz: krople (x, y, długość, prędkość) – ruch zapętlony w 4 s
    R = 140 if H > W else 110
    drops = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.025, 0.06) * H, rng.integers(1, 3)) for _ in range(R)]
    sparks = [(rng.uniform(0.08, 0.92) * W, rng.uniform(0.08, 0.7) * H, rng.uniform(0, 1), rng.uniform(0.6, 1.2)) for _ in range(16)]
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "png", out], stdin=subprocess.PIPE)
    for f in range(N):
        ph = f / N                                    # 0..1 w pętli
        a = np.zeros((H, W), np.float32); rgb = np.zeros((H, W, 3), np.float32)
        def add(alpha, col):
            nonlocal a, rgb
            rgb[:] = rgb * (1 - alpha[..., None]) + col * alpha[..., None]; a[:] = a + alpha * (1 - a)
        # 1) poświata – pulsuje 1x na pętlę
        add(glow * (0.14 + 0.18 * (0.5 - 0.5 * np.cos(2 * np.pi * ph))), gcol)
        # 2) błysk – ukośny pas przelatuje raz na pętlę (przez 60 % czasu)
        k = ph / 0.6
        if k <= 1:
            cx = -0.3 * W + k * 1.6 * W
            u = (xx - cx + (yy - H / 2) * 0.33) / (0.12 * W)
            band = np.exp(-u * u) * 0.18
            add(band, np.array([0.75, 0.6, 1.0], np.float32))
        # 3) odbicia na podłodze – poziome migoczące pasemka
        st = 0.5 + 0.5 * np.sin(yy / 9.0 - ph * 2 * np.pi * 3 + np.sin(xx / 140.0 + ph * 2 * np.pi) * 2)
        add(floor * (st ** 8) * 0.10, np.array([0.6, 0.85, 1.0], np.float32))
        # 4) deszcz
        img = np.zeros((H, W), np.float32)
        for (x0, y0, L, v) in drops:
            y = (y0 + ph * H * v) % H; x = (x0 - (y - y0) * 0.12) % W
            n = int(L); ys = np.clip((y + np.arange(n)).astype(int), 0, H - 1); xs = np.clip((x - np.arange(n) * 0.12).astype(int), 0, W - 1)
            img[ys, xs] = np.maximum(img[ys, xs], np.linspace(0.0, 0.22, n))
        add(img, np.array([0.8, 0.9, 1.0], np.float32))
        # 5) iskry – migotanie
        sp = np.zeros((H, W), np.float32)
        for (x, y, o, s) in sparks:
            t = 0.5 - 0.5 * np.cos(2 * np.pi * ((ph * s + o) % 1)); r = 3 + 3 * t
            x0, x1, y0, y1 = int(max(0, x - 12)), int(min(W, x + 12)), int(max(0, y - 12)), int(min(H, y + 12))
            dd = np.hypot(xx[y0:y1, x0:x1] - x, yy[y0:y1, x0:x1] - y)
            sp[y0:y1, x0:x1] = np.maximum(sp[y0:y1, x0:x1], np.clip(1 - dd / r, 0, 1) * 0.9 * t)
        add(sp, np.array([0.85, 0.95, 1.0], np.float32))
        frame = np.dstack([np.clip(rgb * 255, 0, 255), np.clip(a * 255, 0, 255)]).astype(np.uint8)
        p.stdin.write(frame.tobytes())
    p.stdin.close(); p.wait()
    return out

if __name__ == "__main__":
    W, H, FPS = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 30
    vp = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (0.5, 0.36)
    print(make(W, H, FPS, vp))

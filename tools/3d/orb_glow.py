# poświata neonów (bloom) z zachowaniem przezroczystości
import numpy as np, sys
from PIL import Image, ImageFilter
def glow(im):
    a = np.asarray(im.convert('RGBA')).astype(np.float32) / 255; rgb = a[..., :3] * a[..., 3:4]; al = a[..., 3]
    mx = rgb.max(-1); mn = rgb.min(-1); sat = np.where(mx > 1e-3, (mx - mn) / np.maximum(mx, 1e-3), 0)
    w = np.clip((mx - 0.55) / 0.35, 0, 1) * (0.15 + 0.85 * sat)
    src = Image.fromarray((np.clip(rgb * w[..., None], 0, 1) * 255).astype(np.uint8))
    S = im.size[0]; g = np.zeros_like(rgb)
    for r, k in ((S / 90, 0.9), (S / 35, 0.7), (S / 14, 0.45)):
        g += np.asarray(src.filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255 * k
    out = np.clip(rgb + g, 0, 1); ao = np.clip(np.maximum(al, g.max(-1) * 1.3), 0, 1)
    res = np.dstack([np.where(ao[..., None] > 1e-3, out / np.maximum(ao[..., None], 1e-3), 0), ao])
    return Image.fromarray((np.clip(res, 0, 1) * 255).astype(np.uint8), 'RGBA')
if __name__ == '__main__':
    glow(Image.open(sys.argv[1])).save(sys.argv[2])

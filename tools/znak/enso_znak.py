"""Znak firmowy Ensō na KAŻDEJ publikacji (szef 26.11.2026).

Zasada: na wszystkim, co publikujemy (Reele, Raport 18, odcinki Hexy, karuzele,
grafiki, okładki), jest nasz znak Ensō. Może być wpasowany w tło, ale MUSI być
dobrze widoczny. Ostatni krok przed publikacją – po renderze, przed wysyłką.

Użycie:
  python tools/znak/enso_znak.py wejscie.mp4 [wyjscie.mp4]   # film (dźwięk bez zmian)
  python tools/znak/enso_znak.py wejscie.jpg [wyjscie.jpg]   # obraz / okładka
Opcje: --rog pg|pd|lg|ld (domyślnie pg = prawy górny), --rozmiar 0.10 (część szerokości)
Bez wyjścia nadpisuje plik wejściowy. Plik znaku: marka/Enso_znak_wodny.png.
"""
import os, sys, subprocess, tempfile, argparse
from PIL import Image, ImageFilter

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZNAK = os.path.join(REPO, 'marka', 'Enso_znak_wodny.png')
WIDEO = ('.mp4', '.mov', '.m4v', '.webm')


def przygotuj(szer, rozmiar):
    """Znak z miękkim cieniem, żeby był widoczny na jasnym i ciemnym tle."""
    s = max(48, int(szer * rozmiar))
    z = Image.open(ZNAK).convert('RGBA').resize((s, s), Image.LANCZOS)
    pad = s // 5
    płótno = Image.new('RGBA', (s + 2 * pad, s + 2 * pad), (0, 0, 0, 0))
    cien = Image.new('RGBA', płótno.size, (0, 0, 0, 0))
    a = z.split()[3].point(lambda v: int(v * 0.75))
    czarny = Image.new('RGBA', z.size, (0, 0, 0, 255)); czarny.putalpha(a)
    cien.paste(czarny, (pad, pad + max(1, s // 40)), czarny)
    cien = cien.filter(ImageFilter.GaussianBlur(max(2, s // 14)))
    płótno.alpha_composite(cien)
    płótno.alpha_composite(z, (pad, pad))
    return płótno, pad


def pozycja(W, H, w, h, pad, rog):
    m = int(W * 0.035) - pad
    gora = int(H * 0.085) - pad   # pod górnym paskiem z napisami
    dol = H - h - int(H * 0.11) + pad
    return {'pg': (W - w - m, gora), 'lg': (m, gora),
            'pd': (W - w - m, dol), 'ld': (m, dol)}[rog]


def obraz(src, dst, rog, rozmiar):
    im = Image.open(src).convert('RGBA')
    z, pad = przygotuj(im.width, rozmiar)
    im.alpha_composite(z, pozycja(im.width, im.height, z.width, z.height, pad, rog))
    if dst.lower().endswith(('.jpg', '.jpeg')):
        im.convert('RGB').save(dst, quality=95)
    else:
        im.save(dst)


def film(src, dst, rog, rozmiar):
    W, H = map(int, subprocess.check_output(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
         'stream=width,height', '-of', 'csv=p=0:s=x', src]).decode().strip().split('x'))
    z, pad = przygotuj(W, rozmiar)
    x, y = pozycja(W, H, z.width, z.height, pad, rog)
    tmp = tempfile.mkdtemp()
    zp = os.path.join(tmp, 'znak.png'); z.save(zp)
    out = os.path.join(tmp, 'out' + os.path.splitext(dst)[1])
    subprocess.check_call(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-i', zp,
        '-filter_complex', f'[0:v][1:v]overlay={x}:{y}:format=auto[v]',
        '-map', '[v]', '-map', '0:a?', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19',
        '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', out])
    os.replace(out, dst)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('wej'); p.add_argument('wyj', nargs='?')
    p.add_argument('--rog', default='pg', choices=['pg', 'lg', 'pd', 'ld'])
    p.add_argument('--rozmiar', type=float, default=0.10)
    a = p.parse_args()
    dst = a.wyj or a.wej
    (film if a.wej.lower().endswith(WIDEO) else obraz)(a.wej, dst, a.rog, a.rozmiar)
    print('Ensō ok:', dst)

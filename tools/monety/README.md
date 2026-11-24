# Monety z prawdziwymi logami + ruchoma grafika (24.11.2026, wzory szefa)
- `monety.py` – `coin(R, logo, nazwa, kolor_neonu, metal=..., crack=False)`: metalowa moneta z AUTENTYCZNYM logo (SVG z `marka/loga/`: xrp.svg, xlm.svg, XDC z png), neonowy obrys, połysk; `crack=True` przy spadku.
- `scena.py` – przykład: tło z generatora (bez monet/tekstu, z podestami) + monety na podestach + napisy z prawdziwymi liczbami + ruch (powolny zoom, przesuwający się odblask na monetach, unoszenie monet, iskry, pulsująca poświata) → MP4 9:16, 6 s, 30 kl/s.
- Zasada: generator robi TYLKO tło (prompt: "no text, no letters, no coins, no logos", z pustymi podestami), a loga i liczby zawsze nakładamy sami – wtedy są prawdziwe i dokładne.
- Pierwszy przykład: marka/propozycje/xrp_spadek_kadr.jpg (spadek XRP −6,9% 24.11).

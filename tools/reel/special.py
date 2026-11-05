"""Podklady specjalne (szef 5.11.2026):
 tense  -> HORROR: przy spadkach i krachu "jak z horroru, drastyczna muzyka".
 uplift -> NIEBO: gdy wszystko leci na zielono "niebianska, anielska".
Wszystko syntezowane w numpy (oryginalne, bez praw autorskich). render(mood, n, sr) -> [L, R]."""
import numpy as np

rng = np.random.default_rng(83)


def _lp(x, fc, sr):
    """Prosty filtr dolnoprzepustowy 1. rzedu (2 przejscia = lagodniej)."""
    a = np.exp(-2 * np.pi * fc / sr)
    from scipy.signal import lfilter
    y = lfilter([1 - a], [1, -a], x)
    return lfilter([1 - a], [1, -a], y)


def _env(m, att, rel):
    t = np.arange(m)
    return np.minimum(1, t / max(1, att)) * np.minimum(1, (m - t) / max(1, rel))


class Mix:
    def __init__(s, n, sr): s.n, s.sr = n, sr; s.L = np.zeros(n); s.R = np.zeros(n)

    def add(s, sig, start, pan=.5, g=1.):
        i = int(start * s.sr)
        if i >= s.n or i + len(sig) <= 0: return
        if i < 0: sig = sig[-i:]; i = 0
        j = min(s.n, i + len(sig)); sig = sig[:j - i]
        s.L[i:j] += sig * (1 - pan) * g; s.R[i:j] += sig * pan * g


# ---------------------------------------------------------------- HORROR
def horror(n, sr):
    m = Mix(n, sr); T = n / sr; t = np.arange(n) / sr
    # 1) niski dysonansowy dron (klaster D1/Eb1 + tryton), powolne tremolo i "oddech"
    dr = np.zeros(n)
    for f, a in ((36.7, 1), (38.9, .8), (51.9, .6), (73.4, .35), (77.8, .3), (146.8, .3), (155.6, .28), (207.7, .2)):  # + srodek: slychac w telefonie
        for det in (-.006, .006):
            ph = 2 * np.pi * f * (1 + det) * t
            dr += a * (np.sin(ph) + .5 * (2 * ((f * (1 + det) * t) % 1) - 1))
    dr = _lp(dr, 1100, sr) * (.75 + .25 * np.sin(2 * np.pi * .13 * t)) * .13
    m.add(dr * _env(n, sr * 2, sr * 2), 0, .45); m.add(dr * _env(n, sr * 2, sr * 2), 0, .55)
    # 2) wiatr / szum grozy
    wind = _lp(rng.standard_normal(n), 900, sr) * (.5 + .5 * np.sin(2 * np.pi * .07 * t + 1)) * .05
    m.add(wind, 0, .3); m.add(_lp(rng.standard_normal(n), 700, sr) * .04, 0, .7)

    # 3) bicie serca - przyspiesza do konca
    def thump(g):
        k = np.arange(int(sr * .28)) / sr; f = 70 * np.exp(-k * 14) + 38
        s = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-k * 13)
        s += np.sin(2 * np.pi * 210 * k) * np.exp(-k * 45) * .35  # 'puk' slyszalny na glosniczku
        return s * g
    x = 1.2
    while x < T:
        bpm = 62 + 48 * (x / T); p = 60 / bpm
        m.add(thump(.5), x, .5); m.add(thump(.32), x + p * .28, .5); x += p

    # 4) piszczace smyczki (klaster sekund malych, glissando w gore, vibrato) - narastaja co ok. 7 s
    def screech(d, base):
        k = np.arange(int(sr * d)) / sr; s = np.zeros_like(k)
        for st in (0, 1, 2, 6):  # semitony: klaster + tryton
            f0 = base * 2 ** (st / 12)
            f = f0 * (1 + .35 * (k / d) ** 2) * (1 + .012 * np.sin(2 * np.pi * 6.3 * k))
            ph = 2 * np.pi * np.cumsum(f) / sr
            s += np.sin(ph) + .3 * np.sin(2 * ph) + .15 * np.sin(3 * ph)
        return s * (k / d) ** 1.6 * np.minimum(1, (d - k) / .15) * .035
    x = 2.5
    while x < T - 2:
        d = 3.2 + rng.random() * 1.5
        m.add(screech(d, 880 + rng.random() * 300), x, .25 + rng.random() * .5); x += 6.5 + rng.random() * 1.5

    # 5) uderzenie "BRAAM" (dysonansowe blachy + szum) na starcie i potem co ok. 8 s
    def braam(d=3.0):
        k = np.arange(int(sr * d)) / sr; s = np.zeros_like(k)
        for f in (55, 58.3, 82.4, 110, 116.5):
            s += 2 * ((f * k) % 1) - 1
        s = _lp(s, 1600, sr) * np.exp(-k * 1.1) * np.minimum(1, k / .02) * .12
        hit = rng.standard_normal(len(k)) * np.exp(-k * 9) * .25
        boom = np.sin(2 * np.pi * np.cumsum(60 * np.exp(-k * 3) + 28) / sr) * np.exp(-k * 2) * .6
        return s + _lp(hit, 3000, sr) + boom
    for x in [0.05] + list(np.arange(8.0, T - 2.5, 8.0)):
        b = braam(); m.add(b, x, .45, 1.5); m.add(b, x + .012, .55, 1.5)

    # 6) upiorna pozytywka (minor + tryton, rozstrojona) w wysokim rejestrze
    mel = [587.3, 554.4, 415.3, 0, 587.3, 523.3, 370.0, 0, 466.2, 440.0, 311.1, 0, 587.3, 0, 415.3, 0]
    step = .62; x = 4.0; i = 0
    while x < T - 1:
        f = mel[i % len(mel)]
        if f:
            k = np.arange(int(sr * 1.8)) / sr; ff = f * (1 + .008 * np.sin(2 * np.pi * 4.5 * k))
            ph = 2 * np.pi * np.cumsum(ff) / sr
            s = (np.sin(ph) + .4 * np.sin(2.76 * ph) + .2 * np.sin(5.4 * ph)) * np.exp(-k * 3) * .1
            m.add(s, x, .65)
        x += step; i += 1
    # ciezar: nasycenie (lekki przester) calosci
    pk = max(abs(m.L).max(), abs(m.R).max()) or 1
    return [np.tanh(2.2 * m.L / pk), np.tanh(2.2 * m.R / pk)]


# ---------------------------------------------------------------- NIEBO
FORM = ((800, 90, 1.0), (1150, 110, .55), (2900, 160, .22), (3900, 220, .12))  # samogloska "aaa"


def choir_note(f0, d, sr, voices=4):
    k = np.arange(int(sr * d)) / sr; s = np.zeros_like(k)
    for v in range(voices):
        det = 1 + (v - (voices - 1) / 2) * .0045
        vib = 1 + .006 * np.sin(2 * np.pi * (5.1 + .3 * v) * k + v)
        ph = 2 * np.pi * np.cumsum(f0 * det * vib) / sr
        h = 1
        while h * f0 < 5000:
            fh = h * f0
            a = sum(g * np.exp(-((fh - fc) / bw) ** 2 / 2) for fc, bw, g in FORM) + .04 / h
            s += a * np.sin(h * ph); h += 1
    return s * np.minimum(1, k / 1.1) * np.minimum(1, (d - k) / 1.3) * .018


def heaven(n, sr):
    m = Mix(n, sr); T = n / sr
    # I - IV - vi - V w D-dur (z jasnymi nonami/lidyjska kwarta) - chor "aaa"
    chords = [(293.7, 370.0, 440.0, 659.3), (392.0, 493.9, 587.3, 740.0),
              (246.9, 370.0, 493.9, 587.3), (440.0, 554.4, 659.3, 830.6)]
    bar = 3.6; x = 0; c = 0
    while x < T:
        for j, f in enumerate(chords[c % 4]):
            note = choir_note(f, bar + 1.4, sr)
            m.add(note, x, .3 + .4 * (j / 3))
        # cicha oktawa wyzej = "anielski blask"
        m.add(choir_note(chords[c % 4][2] * 2, bar + 1.4, sr, 3) * .5, x, .5)
        # bas - miekki sinus
        k = np.arange(int(sr * (bar + 1))) / sr
        m.add(np.sin(2 * np.pi * chords[c % 4][0] / 2 * k) * _env(len(k), sr, sr) * .05, x, .5)

        # harfa - arpeggio w gore
        arp = [chords[c % 4][i % 4] * (2 if i >= 4 else 1) for i in range(8)]
        for i, f in enumerate(arp):
            k = np.arange(int(sr * 2.2)) / sr
            s = (np.sin(2 * np.pi * f * k) + .45 * np.sin(4 * np.pi * f * k) * np.exp(-k * 3)
                 + .2 * np.sin(6 * np.pi * f * k) * np.exp(-k * 6)) * np.exp(-k * 1.9) * np.minimum(1, k / .004) * .055
            m.add(s, x + .2 + i * bar / 9, .2 + .6 * (i / 7))
        x += bar; c += 1
    # dzwoneczki / iskry - wysokie, niecalkowite alikwoty
    x = 1.0
    while x < T - 1:
        f = rng.choice([1174.7, 1318.5, 1480.0, 1760.0, 2217.5])
        k = np.arange(int(sr * 2.5)) / sr
        s = (np.sin(2 * np.pi * f * k) + .5 * np.sin(2 * np.pi * f * 2.76 * k) + .25 * np.sin(2 * np.pi * f * 5.4 * k)) \
            * np.exp(-k * 2.4) * np.minimum(1, k / .003) * .03
        m.add(s, x, rng.random()); x += .9 + rng.random() * 1.4
    return [m.L, m.R]


def render(mood, n, sr):
    return horror(n, sr) if mood == "tense" else heaven(n, sr)

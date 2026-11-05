"""Oryginalny podklad do Reela (synthwave/cyberpunk), dobrany do tematu.
Uzycie: python3 music.py <czas_s> [nastroj]
Nastroje:
  calm    - spokojny (dzien bez wielkich ruchow, edukacja CRYPTO 101, WEEK IN 30s)
  tense   - napiecie, ciemny moll, puls (spadki, krach, hack, likwidacje, CLAIM CHECK)
  uplift  - energiczny, dur, szybszy (wzrosty, rekordy, BIGGEST MOVE w gore)
  gold    - cieply, dostojny, wolny (GOLD vs DOLLAR, Fed, makro)
Wynik: melody.wav (potem efekt i miks jak w README)."""
import numpy as np, wave, sys
dur = float(sys.argv[1]); mood = sys.argv[2] if len(sys.argv) > 2 else "calm"; sr = 44100
CFG = {
 "calm":   dict(bpm=78, kick=False, saw=.25, chords=[([110,164.8,220,261.6,329.6],[659.3,0,523.3,0,440,523.3,659.3,0]),([87.3,130.8,174.6,220,261.6],[523.3,0,440,0,698.5,659.3,523.3,0]),([130.8,196,261.6,329.6,392],[392,523.3,659.3,0,784,659.3,523.3,0]),([98,146.8,196,246.9,293.7],[587.3,0,493.9,0,392,493.9,587.3,0])]),
 "tense":  dict(bpm=72, kick=True,  saw=.6,  chords=[([73.4,110,146.8,174.6,220],[293.7,0,349.2,0,293.7,0,261.6,0]),([69.3,103.8,138.6,164.8,207.7],[277.2,0,329.6,0,277.2,0,246.9,0]),([65.4,98,130.8,155.6,196],[261.6,0,311.1,0,261.6,0,233.1,0]),([73.4,110,146.8,174.6,220],[293.7,349.2,440,0,349.2,0,293.7,0])]),
 "uplift": dict(bpm=100,kick=True,  saw=.45, chords=[([130.8,196,261.6,329.6,392],[523.3,659.3,784,659.3,523.3,659.3,784,1046.5]),([98,146.8,196,246.9,293.7],[493.9,587.3,784,587.3,493.9,587.3,784,987.8]),([110,164.8,220,261.6,329.6],[440,523.3,659.3,523.3,440,523.3,659.3,880]),([87.3,130.8,174.6,220,261.6],[440,523.3,698.5,523.3,440,523.3,698.5,880])]),
 "gold":   dict(bpm=66, kick=False, saw=.35, chords=[([98,146.8,196,246.9,293.7],[587.3,0,0,493.9,0,392,0,0]),([82.4,123.5,164.8,196,246.9],[493.9,0,0,392,0,329.6,0,0]),([65.4,98,130.8,164.8,196],[392,0,0,329.6,0,261.6,0,0]),([73.4,110,146.8,185,220],[440,0,0,370,0,293.7,0,0])]),
}[mood]
beat = 60 / CFG["bpm"]; eighth = beat / 2; bar = beat * 4
n = int(sr * (dur + 1)); out = [np.zeros(n), np.zeros(n)]
def add(sig, start, pan=.5, g=1.4):
    i = int(start * sr); j = min(n, i + len(sig))
    if i < n: out[0][i:j] += sig[:j-i] * (1 - pan) * g; out[1][i:j] += sig[:j-i] * pan * g
def pad(freqs, d):
    t = np.arange(int(sr * d)) / sr; s = np.zeros_like(t)
    for f in freqs:
        for det in (-.004, 0, .004):
            ph = 2 * np.pi * f * (1 + det) * t
            s += np.sin(ph) + CFG["saw"] * (2 * ((f * (1 + det) * t) % 1) - 1) * .35   # troche "piły" = synthwave
    e = np.minimum(1, t / 1.2) * np.minimum(1, (d - t) / 1.4); return s * .04 * e
def pluck(f, d=1.4):
    t = np.arange(int(sr * d)) / sr
    s = np.sin(2*np.pi*f*t) + .35*np.sin(2*np.pi*2*f*t)*np.exp(-t*4) + .15*np.sin(2*np.pi*3*f*t)*np.exp(-t*7)
    return s * np.exp(-t * 2.8) * np.minimum(1, t / .006) * .15
def kick():
    t = np.arange(int(sr * .35)) / sr; f = 120 * np.exp(-t * 18) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t * 9) * .55
def bass(f, d):
    t = np.arange(int(sr * d)) / sr; return (np.sin(2*np.pi*f/2*t) + .3*np.sin(2*np.pi*f*t)) * np.exp(-t * 3) * .18
t = 0; k = 0
while t < dur + 1:
    ch, mel = CFG["chords"][k % 4]; add(pad(ch, bar + .8), t)
    for i, f in enumerate(mel):
        if f: add(pluck(f), t + i * eighth, pan=.35 + .3 * ((i % 3) / 2))
    if CFG["kick"] and t > bar * .99:
        for b in range(4): add(kick(), t + b * beat, g=1.0); add(bass(ch[0], beat * .9), t + b * beat + beat / 2, g=1.0)
    t += bar; k += 1
x = np.stack(out, 1)[:int(sr * (dur + .5))]
fi, fo = int(sr * 1.5), int(sr * 2.5); x[:fi] *= np.linspace(0, 1, fi)[:, None]; x[-fo:] *= np.linspace(1, 0, fo)[:, None]
x /= abs(x).max(); x *= .9
w = wave.open("melody.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()
print("melody.wav", mood, f"{dur}s")

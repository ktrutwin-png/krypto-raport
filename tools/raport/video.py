"""Raport 18:00 jako film (Reel 1080x1920) z LEKTOREM i muzyka (od 5.11.2026).
Uzycie: python3 video.py <folder_z_slide1-3.png> <nastroj: calm|tense|uplift|gold> [sciezka_do_glosu.onnx]
Lektor: plik narration.json w folderze = lista 3 tekstow (po angielsku), jeden na slajd. Czas slajdu = dlugosc
jego narracji (+0,6 s). Bez narration.json film jest tylko z muzyka (stale czasy 4,5/7,5/6,5 s).
Glos: piper en_US-joe-medium (gleboki meski, jak w Reelach); domyslnie szukany w tools/reel/voice/.
Wynik: report.mp4 + cover.jpg. Slajd 4:5 na srodku pionu, tlo = rozmyty slajd, lekkie przyblizenie, przejscia."""
import subprocess, sys, os, json, wave
D = os.path.abspath(sys.argv[1]); MOOD = sys.argv[2] if len(sys.argv) > 2 else "calm"
HERE = os.path.dirname(os.path.abspath(__file__)); REEL = os.path.join(HERE, "..", "reel")
VOICE = sys.argv[3] if len(sys.argv) > 3 else os.path.join(REEL, "voice", "en_US-joe-medium.onnx")
FADE = .5; FPS = 30
def run(cmd, **kw): subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, **kw)
os.chdir(D)
NAR = json.load(open("narration.json")) if os.path.exists("narration.json") else None
if NAR:
    assert len(NAR) == 3, "narration.json = dokladnie 3 teksty"
    assert os.path.exists(VOICE), f"brak glosu {VOICE} (pobierz wg tools/reel/README.md)"
    DUR = []
    for i, s in enumerate(NAR):
        run([sys.executable, "-m", "piper", "-m", VOICE, "--length-scale", "1.05", "-f", f"_a{i}.wav"], input=s.encode())
        w = wave.open(f"_a{i}.wav"); d = w.getnframes() / w.getframerate(); w.close()
        L = d + 0.6 + (FADE if i < 2 else 0.8); DUR.append(round(L, 2))
        run(["ffmpeg", "-y", "-i", f"_a{i}.wav", "-af", f"adelay=200|200,apad=whole_dur={L:.2f},aresample=44100", "-ac", "2", f"_p{i}.wav"])
    open("_l.txt", "w").write("".join(f"file '_p{i}.wav'\n" for i in range(3)))
else:
    DUR = [4.5, 7.5, 6.5]
clips = []
for i, d in enumerate(DUR, 1):
    out = f"_c{i}.mp4"; n = int(d * FPS)
    flt = (f"[0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.08:saturation=1.2[bg];"
           f"[0]scale=1080:1350,zoompan=z='1+0.035*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1350:fps={FPS}[fg];"
           f"[bg][fg]overlay=0:285,format=yuv420p")
    run(["ffmpeg", "-y", "-loop", "1", "-t", str(d), "-i", f"slide{i}.png", "-filter_complex", flt, "-t", str(d), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])
    clips.append(out)
T = sum(DUR) - FADE * (len(DUR) - 1)
o1 = DUR[0] - FADE; o2 = o1 + DUR[1] - FADE
xf = f"[0][1]xfade=transition=fade:duration={FADE}:offset={o1}[a];[a][2]xfade=transition=slideleft:duration={FADE}:offset={o2},format=yuv420p[v]"
run(["ffmpeg", "-y", "-i", clips[0], "-i", clips[1], "-i", clips[2], "-filter_complex", xf, "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "_v.mp4"])
run([sys.executable, os.path.join(REEL, "music.py"), str(T + 1), MOOD])
run(["ffmpeg", "-y", "-i", "melody.wav", "-af", "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2", "_mel.wav"])
if NAR:
    # glos: sklejone segmenty, przesuniete o przejscia (kazdy segment konczy sie przed nastepnym slajdem)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-af", f"atrim=0:{T}", "_vo.wav"])
    mix = ("[0]aresample=44100,aformat=channel_layouts=stereo,volume=0.5[m];[1]aresample=44100,aformat=channel_layouts=stereo,"
           "equalizer=f=140:t=q:w=1:g=3,asplit[v1][v2];[m][v1]sidechaincompress=threshold=0.015:ratio=5:attack=30:release=600:makeup=1[duck];"
           "[duck][v2]amix=inputs=2:normalize=0:weights=1 1.25,loudnorm=I=-15:TP=-1.5:LRA=7[out]")
    run(["ffmpeg", "-y", "-i", "_mel.wav", "-i", "_vo.wav", "-filter_complex", mix, "-map", "[out]", "-t", str(T), "-ar", "44100", "-c:a", "aac", "-b:a", "160k", "_m.m4a"])
else:
    run(["ffmpeg", "-y", "-i", "_mel.wav", "-af", "volume=0.8,loudnorm=I=-16:TP=-1.5", "-t", str(T), "-ar", "44100", "-c:a", "aac", "-b:a", "160k", "_m.m4a"])
run(["ffmpeg", "-y", "-i", "_v.mp4", "-i", "_m.m4a", "-shortest", "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart", "report.mp4"])
from PIL import Image
Image.open("slide1.png").convert("RGB").save("cover.jpg", quality=92)
for f in os.listdir("."):
    if f.startswith("_") or f == "melody.wav": os.remove(f)
print("report.mp4", round(T, 1), "s,", MOOD, "lektor" if NAR else "bez lektora", DUR)

"""Raport 18:00 jako krotki film (Reel 1080x1920) z muzyka (od 5.11.2026).
Uzycie: python3 video.py <folder_z_slide1-3.png> <nastroj: calm|tense|uplift|gold>
Wynik w tym samym folderze: report.mp4 (ok. 18 s) i cover.jpg (= slajd 1).
Slajd 4:5 lezy na srodku pionowego kadru, tlo = ten sam slajd rozmyty i przyciemniony; lekkie przyblizanie, przejscia."""
import subprocess, sys, os, shutil
D = os.path.abspath(sys.argv[1]); MOOD = sys.argv[2] if len(sys.argv) > 2 else "calm"
REEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reel")
DUR = [4.5, 7.5, 6.5]; FADE = .5; FPS = 30
def run(cmd): subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
clips = []
for i, d in enumerate(DUR, 1):
    src = os.path.join(D, f"slide{i}.png"); out = os.path.join(D, f"_c{i}.mp4"); n = int(d * FPS)
    flt = (f"[0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.08:saturation=1.2[bg];"
           f"[0]scale=1080:1350,zoompan=z='1+0.035*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1350:fps={FPS}[fg];"
           f"[bg][fg]overlay=0:285,format=yuv420p")
    run(["ffmpeg", "-y", "-loop", "1", "-t", str(d), "-i", src, "-filter_complex", flt, "-t", str(d), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])
    clips.append(out)
T = sum(DUR) - FADE * (len(DUR) - 1)
o1 = DUR[0] - FADE; o2 = o1 + DUR[1] - FADE
xf = (f"[0][1]xfade=transition=fade:duration={FADE}:offset={o1}[a];[a][2]xfade=transition=slideleft:duration={FADE}:offset={o2},format=yuv420p[v]")
vid = os.path.join(D, "_v.mp4")
run(["ffmpeg", "-y", "-i", clips[0], "-i", clips[1], "-i", clips[2], "-filter_complex", xf, "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", vid])
cwd = os.getcwd(); os.chdir(D)
run([sys.executable, os.path.join(REEL, "music.py"), str(T), MOOD])
run(["ffmpeg", "-y", "-i", "melody.wav", "-af", "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2,volume=0.8,loudnorm=I=-16:TP=-1.5", "-ar", "44100", "-c:a", "aac", "-b:a", "160k", "_m.m4a"])
run(["ffmpeg", "-y", "-i", "_v.mp4", "-i", "_m.m4a", "-shortest", "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart", "report.mp4"])
from PIL import Image
Image.open("slide1.png").convert("RGB").save("cover.jpg", quality=92)
for f in ["_c1.mp4", "_c2.mp4", "_c3.mp4", "_v.mp4", "_m.m4a", "melody.wav"]:
    if os.path.exists(f): os.remove(f)
os.chdir(cwd); print("report.mp4", round(T, 1), "s,", MOOD)

"""Dzwiek Reela karuzeli: lektor v1..v6.wav (piper hfc_male z serwera) w czasach scen + muzyka tense/calm/uplift (tools/reel/music.py) z duckingiem -> reel/audio.wav i finalny mp4.
Uzycie: python3 audio_reel.py <config.json> [nastroj]"""
import sys, json, wave, subprocess, numpy as np, os
cfg=json.load(open(sys.argv[1])); nastroj=sys.argv[2] if len(sys.argv)>2 else 'tense'
R='/home/claude/krypto-raport/'+cfg['dir']+'/reel'; os.chdir(R)
c=json.load(open('czasy.json')); sr=44100; n=int((c['total']+0.5)*sr); v=np.zeros(n)
subprocess.run(['python3','/home/claude/krypto-raport/tools/reel/music.py',str(int(c['total'])+2),nastroj],capture_output=True)
for i,st in enumerate(c['starts'],1):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'v{i}.wav','-ar','44100','-ac','1',f'_v{i}.wav'])
    w=wave.open(f'_v{i}.wav'); a=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768; w.close(); os.remove(f'_v{i}.wav')
    s=int((st+0.45)*sr); v[s:s+len(a)]+=a[:max(0,n-s)]
w=wave.open('melody.wav'); ch=w.getnchannels(); m=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768; w.close()
m=m.reshape(-1,ch).mean(1)[:n]; m=np.pad(m,(0,n-len(m)))
env=np.convolve(np.abs(v),np.ones(4410)/4410,'same'); mix=v+m*0.22*(1-0.55*np.clip(env*8,0,1)); mix=mix/max(1e-6,np.abs(mix).max())*0.92
o=wave.open('audio.wav','w'); o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes((mix*32767).astype(np.int16).tobytes()); o.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','obraz.mp4','-i','audio.wav','-c:v','libx264','-preset','veryfast','-crf','23','-maxrate','12M','-bufsize','24M','-c:a','aac','-b:a','160k','-shortest','reel.mp4'],check=True)
# szef 26.11.2026: napisy karaoke (tools/napisy) z czasow slow lektora (v1.wav.words.json ... z tools/reel/lektor.py)
try:
    sys.path.insert(0,'/home/claude/krypto-raport/tools/napisy'); from napisy import ass,wypal
    seg=[(st+0.45,f'v{i}.wav.words.json') for i,st in enumerate(c['starts'],1)]
    if ass(seg,'_napisy.ass'): wypal('reel.mp4','_napisy.ass','_reel_n.mp4'); os.replace('_reel_n.mp4','reel.mp4'); print('NAPISY ok')
    else: print('NAPISY: brak plikow v*.wav.words.json - lektor nie przez tools/reel/lektor.py?')
except Exception as e: print('NAPISY blad:',e)
print(R+'/reel.mp4')

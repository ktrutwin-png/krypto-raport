import subprocess,json,os,wave
segs=["Bitcoin slipped under eighty thousand dollars this weekend, and over half a billion dollars in bets were wiped out in just one day.",
"Most of it was leveraged longs: traders betting on a rise with borrowed money. When the price fell, exchanges closed those positions automatically, and that forced selling pushed the price down even more.",
"Why now? Analysts point to geopolitical tensions, high oil prices, weak tech stocks and thin weekend trading. But the data can't prove a single cause.",
"Funds tell a mixed story. U.S. Bitcoin ETFs lost about seven hundred seventy million dollars on Thursday and Friday, yet the week overall is still positive, with roughly three hundred million in.",
"Traders are watching eighty thousand as support. If it breaks, some analysts mention seventy eight thousand next. Big dates ahead: the Fed decision on the twenty eighth, and US midterm elections on November third.",
"So, will Bitcoin hold eighty thousand by Friday? Tell us in the comments, and follow for daily reports."]
os.makedirs('seg',exist_ok=True);S=[];t=0.0
for i,s in enumerate(segs):
    subprocess.run(['python3','-m','piper','-m','voice/en_US-joe-medium.onnx','--length-scale','1.0','-f',f'seg/a{i}.wav'],input=s.encode(),check=True,capture_output=True)
    w=wave.open(f'seg/a{i}.wav');d=w.getnframes()/w.getframerate()
    L=d+0.45;S.append([round(t,2),round(t+L,2)])
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'seg/a{i}.wav','-af',f'apad=whole_dur={L:.2f},aresample=44100','-ac','2',f'seg/p{i}.wav'],check=True)
    t+=L
json.dump({'S':S,'T':round(t+0.6,2)},open('timing.json','w'));print(S,t)
open('seg/list.txt','w').write(''.join(f"file 'p{i}.wav'\n" for i in range(len(segs))))
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i','seg/list.txt','-af','apad=pad_dur=0.6','-c:a','aac','-b:a','128k','voice.m4a'],check=True)

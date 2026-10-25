import subprocess,json,os,wave
segs=["Bitcoin ended the week almost flat, down about half a percent. But it climbed above eighty four thousand dollars midweek, then fell more than five percent from that peak.",
"BNB and XRP led the week, while Cardano lagged. Most big coins stayed in a narrow range, and trading volume fell.",
"Why the late slide? Analysts point to geopolitical tensions, high oil prices and weak tech stocks. The weekend dip under eighty thousand then forced roughly half a billion dollars of liquidations, mostly long bets. No single cause can be proven.",
"Funds were mixed. Bitcoin ETFs still show a small weekly inflow, while Ether funds lost money, and Fear and Greed slipped from forty nine to forty five. Also this week, Solana's Alpenglow upgrade went live, and Switzerland approved a retail Bitcoin fund.",
"Next week: Ripple's Swell conference opens in New York on the twenty seventh, the Fed decides on the twenty eighth, and US midterm elections follow on November third.",
"So, will Bitcoin close next week above eighty thousand? Tell us in the comments, and follow for daily reports."]
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

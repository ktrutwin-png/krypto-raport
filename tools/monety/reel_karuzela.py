"""Reel 9:16 z karuzeli: kazda karta = scena z ruchem kamery (Ken Burns), ruchomy deszcz, blyski, tytul z cena, podpis 'dlaczego', lektor hfc_male, muzyka."""
import sys, os, json, math, wave, subprocess, numpy as np
sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
src=open('karta_sunset.py').read().split("P=f'{REPO}/propozycje/sunset'")[0]
exec(src)
W,H=1080,1920; FPS=30
D=f'{REPO}/propozycje/karuzela_2411'; R=f'{D}/reel'
T=json.load(open(f'{R}/teksty.json'))
KARTY=[('XAU','−2.4%','$3,563','s_xau.jpg',150,0.4,False),('XDC','−3.0%','$0.0258','s_xdc.jpg',150,0.45,False),
       ('BTC','−4.2%','$59,475','s_btc.jpg',200,0.8,False),('ETH','−5.1%','$1,670','s_eth.jpg',200,0.9,True),
       ('XRP','−6.1%','$0.912','s_xrp.jpg',150,1.0,True),('XLM','−7.2%','$0.1233','s_xlm.jpg',150,1.0,True)]
def dlug(p):
    w=wave.open(p); d=w.getnframes()/w.getframerate(); w.close(); return d
def tytul(k,pc,cena,i):
    L=Image.new('RGBA',(W,420),(0,0,0,0))
    gl=(255,30,70) if float(pc[1:-1])>=4 else (255,120,40)
    tekst(L,f'{k} {pc}',FA(150),(W//2,150),(255,255,255),gl)
    tekst(L,f'{cena}  ·  24H',fb(42),(W//2,280),(245,245,250),gl,gr=10,st=0)
    ImageDraw.Draw(L).text((W-44,44),f'{i}/6',font=fb(28,700),fill=(255,255,255,230),anchor='rt')
    return L
def podpis(t):
    f=fb(44,700); L=Image.new('RGBA',(W,300),(0,0,0,0)); d=ImageDraw.Draw(L)
    words=t.split(); lines=[];cur=''
    for w_ in words:
        if d.textlength((cur+' '+w_).strip(),font=f)>W-160: lines.append(cur); cur=w_
        else: cur=(cur+' '+w_).strip()
    lines.append(cur); h=len(lines)*62+40; y0=150-h//2
    d.rounded_rectangle([60,y0,W-60,y0+h],radius=26,fill=(8,8,14,200),outline=(255,255,255,40),width=2)
    for j,l in enumerate(lines): d.text((W//2,y0+44+j*62),l,font=f,fill=(255,255,255,255),anchor='mm')
    return L
rng=np.random.default_rng(1); KROPLE=rng.uniform(0,1,(500,4))
def deszcz_kl(img,t,sila):
    n=int(500*sila); d=ImageDraw.Draw(img)
    for x,y,l,a in KROPLE[:n]:
        L=40+60*l; yy=((y*H+t*1500*(0.8+l*0.5))%(H+200))-100; xx=(x*W+yy*0.22)%W
        d.line([(xx,yy),(xx+L*0.22,yy+L)],fill=(200,215,255,int(50+90*a)),width=2)
sceny=[]
for i,(k,pc,cena,scn,x0,sila,piorun) in enumerate(KARTY,1):
    s=Image.open(f'{D}/{scn}').convert('RGB')
    fg=s.crop((x0,0,x0+824,1024)).resize((1236,1536),Image.LANCZOS)   # zapas na ruch kamery
    bg=s.resize((H,H)).crop(((H-W)//2,0,(H-W)//2+W,H)).filter(ImageFilter.GaussianBlur(30)); bg=ImageEnhance.Brightness(bg).enhance(0.35)
    dur=dlug(f'{R}/v{i}.wav')+1.0
    sceny.append(dict(fg=fg,bg=bg,dur=dur,tyt=tytul(k,pc,cena,i),pod=podpis(T[i-1]['cap']),sila=sila,piorun=piorun,zoom_in=(i%2==1)))
def klatka(sc,t):
    c=sc['bg'].copy().convert('RGBA'); p=min(1,t/sc['dur'])
    z=1.0+0.10*(p if sc['zoom_in'] else 1-p); fw,fh=int(1080*1.144/z),int(1342*1.144/z)
    cx=1236/2+(40*(p-0.5) if sc['zoom_in'] else -40*(p-0.5)); cy=1536/2-20*(p-0.5)
    fr=sc['fg'].crop((int(cx-fw/2),int(cy-fh/2),int(cx-fw/2)+fw,int(cy-fh/2)+fh)).resize((1080,1342),Image.BILINEAR)
    if sc['piorun'] and (abs(t-1.6)<0.07 or abs(t-1.8)<0.05 or abs(t-sc['dur']*0.7)<0.06): fr=ImageEnhance.Brightness(fr).enhance(1.9)
    c.paste(fr,(0,300))
    m=Image.new('RGBA',(W,H),(0,0,0,0)); md=ImageDraw.Draw(m)
    for j in range(220): md.line([(0,300+j),(W,300+j)],fill=(5,5,10,int(200*(1-j/220))))
    for j in range(260): md.line([(0,1642-j),(W,1642-j)],fill=(5,5,10,int(210*(1-j/260))))
    c.alpha_composite(m)
    rl=Image.new('RGBA',(W,H),(0,0,0,0)); deszcz_kl(rl,t,sc['sila']); c.alpha_composite(rl)
    a=min(1,t/0.5); dy=int((1-a)*-50); ty=sc['tyt'].copy()
    if a<1: ty.putalpha(ty.split()[3].point(lambda v:int(v*a)))
    c.alpha_composite(ty,(0,40+dy))
    b=min(1,max(0,(t-0.8)/0.5)); po=sc['pod'].copy()
    if b<1: po.putalpha(po.split()[3].point(lambda v:int(v*b)))
    c.alpha_composite(po,(0,1560+int((1-b)*30)))
    d=ImageDraw.Draw(c); d.text((60,H-70),'ERL.GREY83',font=fb(30,700),fill=(244,241,234),anchor='lm'); d.text((W-60,H-70),'NOT FINANCIAL ADVICE',font=fb(22,600),fill=(190,190,200),anchor='rm')
    d.rounded_rectangle([150,H-150,W-150,H-102],radius=24,fill=(255,200,60,235)); d.text((W//2,H-126),'LIVE PRICES → erlgrey83-crypto-freaq.vercel.app',font=fb(24,800),fill=(10,10,14),anchor='mm')
    return c.convert('RGB')
XF=0.4; total=sum(s['dur'] for s in sceny)-XF*(len(sceny)-1)
cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',f'{R}/obraz.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE)
starts=[];acc=0
for s in sceny: starts.append(acc); acc+=s['dur']-XF
N=int(total*FPS)
for f in range(N):
    t=f/FPS; i=max(j for j,st in enumerate(starts) if st<=t)
    im=klatka(sceny[i],t-starts[i])
    if i+1<len(sceny) and t>=starts[i+1]-0: pass
    if i>0 and t-starts[i]<XF:   # przenikanie z poprzedniej
        prev=klatka(sceny[i-1],t-starts[i-1]); im=Image.blend(prev,im,(t-starts[i])/XF)
    pr.stdin.write(im.tobytes())
pr.stdin.close(); pr.wait()
json.dump({'starts':starts,'total':total},open(f'{R}/czasy.json','w'))
print('obraz ok',total)

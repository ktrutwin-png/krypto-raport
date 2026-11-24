import sys, math, numpy as np, subprocess
sys.path.insert(0,'.'); from monety import *
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
REPO='/home/claude/krypto-raport/marka'
W,H=1080,1920; FPS=30; N=int(sys.argv[1]) if len(sys.argv)>1 else 180
bg0=Image.open(f'{REPO}/propozycje/robocze/tlo_spadek_3.jpg').convert('RGB').resize((W,H),Image.LANCZOS)
# lekkie wyostrzenie + nasycenie
from PIL import ImageEnhance
bg0=ImageEnhance.Color(bg0).enhance(1.15); bg0=bg0.filter(ImageFilter.UnsharpMask(2,80,2))
XRP=svg_logo(f'{REPO}/loga/xrp.svg',230); XLM=svg_logo(f'{REPO}/loga/xlm.svg',190)
xdc=Image.open(f'{REPO}/loga/xdc_xdc-icon.png').convert('RGBA').resize((180,180),Image.LANCZOS)
# XDC: wytnij jasny znak z okraglego tla (zostaw jasne piksele)
a=np.array(xdc).astype(np.float32); lum=a[...,:3].mean(-1); m=np.clip((lum-150)/60,0,1)*(a[...,3]/255)
XDC=Image.fromarray(np.dstack([np.full(lum.shape+(3,),255),m*255]).astype(np.uint8),'RGBA')
coins=[ # (obraz, cx, podstawa_y, R)
 (coin(150,XLM,'XLM',(185,90,255),metal=(70,62,96)), 225,1452,150),
 (coin(150,XDC,'XDC',(50,140,255),metal=(58,70,98)), 862,1452,150),
 (coin(205,XRP,'XRP',(60,200,255),metal=(64,72,90),crack=True), 535,1615,205)]
F=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf',150)
F2=ImageFont.truetype(F_BOLD,52); F2.set_variation_by_axes([800])
def tekst(img,t,font,xy,fill,glow,alpha=1.0):
    lay=Image.new('RGBA',img.size,(0,0,0,0)); d=ImageDraw.Draw(lay); d.text(xy,t,font=font,fill=glow+(255,),anchor='mm')
    g=lay.filter(ImageFilter.GaussianBlur(14))
    sh=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(sh).text((xy[0]+5,xy[1]+7),t,font=font,fill=(0,0,0,220),anchor='mm')
    top=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(top).text(xy,t,font=font,fill=fill+(255,),anchor='mm')
    for L in (g,g,sh.filter(ImageFilter.GaussianBlur(3)),top):
        if alpha<1: L.putalpha(L.split()[3].point(lambda v:int(v*alpha)))
        img.alpha_composite(L)
rng=np.random.default_rng(3); P=[[rng.uniform(0,W),rng.uniform(900,H),rng.uniform(1,3.5),rng.uniform(40,120),rng.choice([0,1])] for _ in range(70)]
def klatka(i):
    t=i/FPS; z=1+0.05*min(1,i/180)
    bw,bh=int(W*z),int(H*z); bg=bg0.resize((bw,bh),Image.BILINEAR).crop(((bw-W)//2,(bh-H)//3,(bw-W)//2+W,(bh-H)//3+H)).convert('RGBA'); bgz=bg.copy()
    # pulsujaca czerwona poswiata strzalki
    puls=0.5+0.5*math.sin(t*4)
    rg=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(rg).ellipse([700,850,980,1380],fill=(255,30,60,int(60*puls)))
    bg.alpha_composite(rg.filter(ImageFilter.GaussianBlur(60)))
    # iskry
    sp=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sp)
    for p in P:
        y=(p[1]-p[3]*t)%H; x=p[0]+12*math.sin(t*1.3+p[1]); c=(120,200,255) if p[4] else (210,120,255)
        sd.ellipse([x-p[2],y-p[2],x+p[2],y+p[2]],fill=c+(220,))
    bg.alpha_composite(sp.filter(ImageFilter.GaussianBlur(1)))
    for k,(cim,cx,by,R) in enumerate(coins):
        bob=7*math.sin(t*2.2+k*2.1)
        im=cim.copy(); S=im.width
        # odblysk przesuwajacy sie po monecie
        g=Image.new('L',(S,S),0); gd=ImageDraw.Draw(g); ph=((t*0.45+k*0.33)%1.6)-0.3
        x0=int(S*ph); gd.polygon([(x0,0),(x0+S*0.12,0),(x0+S*0.12-S*0.5,S),(x0-S*0.5,S)],fill=150)
        g=g.filter(ImageFilter.GaussianBlur(S*0.03)); g=ImageChops.multiply(g,im.split()[3])
        white=Image.new('RGBA',(S,S),(255,255,255,0)); white.putalpha(g); im.alpha_composite(white)
        # cien na podescie
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-R*0.9,by-R*0.12,cx+R*0.9,by+R*0.12],fill=(0,0,0,150))
        bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
        bg.alpha_composite(im,(int(cx-S/2),int(by-R*0.97-S/2+bob)))
    # napisy (wjazd w pierwszej 0,6 s)
    a=min(1,t/0.6); dy=int((1-a)*-60)
    tekst(bg,'XRP  −6.9%',F,(W//2,175+dy),(255,255,255),(255,40,70),a)
    tekst(bg,'XLM −7.2%  ·  XDC −3.4%  ·  24H',F2,(W//2,310+dy),(220,230,255),(120,80,255),a)
    return bg.convert('RGB')
if __name__=='__main__':
    if N==1: klatka(int(sys.argv[2]) if len(sys.argv)>2 else 60).save('kadr.jpg',quality=93); sys.exit()
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','xrp_spadek_ruch.mp4'],stdin=subprocess.PIPE)
    for i in range(N): p.stdin.write(klatka(i).tobytes())
    p.stdin.close(); p.wait(); klatka(N-1).save('kadr.jpg',quality=93)

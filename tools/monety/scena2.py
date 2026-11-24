import sys, math, numpy as np, subprocess
sys.path.insert(0,'.'); from monety import svg_logo, F_BOLD; from monety2 import coin2, _glow
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageEnhance
REPO='/home/claude/krypto-raport/marka'
W,H=1080,1920; FPS=30; N=int(sys.argv[1]) if len(sys.argv)>1 else 180
bg0=Image.open(f'{REPO}/propozycje/robocze/tlo2_2.jpg').convert('RGB').resize((W,H),Image.LANCZOS)
bg0=ImageEnhance.Contrast(bg0).enhance(1.12); bg0=ImageEnhance.Color(bg0).enhance(1.25); bg0=bg0.filter(ImageFilter.UnsharpMask(2.5,110,2))
XRP=svg_logo(f'{REPO}/loga/xrp.svg',int(220*1.1)); XLM=svg_logo(f'{REPO}/loga/xlm.svg',int(140*1.25))
xdc=Image.open(f'{REPO}/loga/xdc_xdc-icon.png').convert('RGBA').resize((175,175),Image.LANCZOS)
a=np.array(xdc).astype(np.float32); lum=a[...,:3].mean(-1); m=np.clip((lum-150)/60,0,1)*(a[...,3]/255)
XDC=Image.fromarray(np.dstack([np.full(lum.shape+(3,),255),m*255]).astype(np.uint8),'RGBA')
spec=[(XLM,'XLM',(190,90,255),200,1606,140,3),(XDC,'XDC',(40,150,255),881,1606,140,5),(XRP,'XRP',(50,210,255),550,1680,220,7)]
coins=[]
for lg,nm,ne,cx,sy,R,sd in spec:
    im=coin2(R,lg,nm,ne,crack=(nm=='XRP'),seed=sd); cy=int(R*2.9*0.90)//2
    coins.append((im,cx,sy,R,ne,cy))
FA=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf',165)
F2=ImageFont.truetype(F_BOLD,50); F2.set_variation_by_axes([800])
def tekst(img,t,font,xy,fill,glow,alpha=1.0,gr=16):
    def L(fn):
        l=Image.new('RGBA',img.size,(0,0,0,0)); fn(ImageDraw.Draw(l)); 
        if alpha<1: l.putalpha(l.split()[3].point(lambda v:int(v*alpha)))
        return l
    g=_glow(L(lambda d:d.text(xy,t,font=font,fill=glow+(255,),anchor='mm',stroke_width=6,stroke_fill=glow+(255,))),gr,3)
    img.alpha_composite(g)
    img.alpha_composite(L(lambda d:d.text((xy[0]+4,xy[1]+6),t,font=font,fill=(0,0,0,200),anchor='mm')).filter(ImageFilter.GaussianBlur(3)))
    img.alpha_composite(L(lambda d:d.text(xy,t,font=font,fill=fill+(255,),anchor='mm',stroke_width=2,stroke_fill=(255,255,255,255))))
rng=np.random.default_rng(3); P=[[rng.uniform(0,W),rng.uniform(700,H),rng.uniform(1,3.2),rng.uniform(40,130),rng.integers(3)] for _ in range(90)]
PC=[(110,210,255),(200,120,255),(255,80,110)]
def klatka(i):
    t=i/FPS; z=1+0.05*min(1,i/180)
    bw,bh=int(W*z),int(H*z); bg=bg0.resize((bw,bh),Image.BILINEAR).crop(((bw-W)//2,(bh-H)//2,(bw-W)//2+W,(bh-H)//2+H)).convert('RGBA')
    puls=0.5+0.5*math.sin(t*3)
    # swiatlo monet na otoczenie
    lt=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lt)
    for im,cx,sy,R,ne,cy in coins:
        ld.ellipse([cx-R*1.9,sy-R*2.6,cx+R*1.9,sy+R*0.5],fill=ne+(int(55+35*puls),))
    bg.alpha_composite(lt.filter(ImageFilter.GaussianBlur(90)))
    # iskry
    sp=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sp)
    for p in P:
        y=(p[1]-p[3]*t)%H; x=p[0]+14*math.sin(t*1.2+p[1]); c=PC[p[4]]
        sd.ellipse([x-p[2],y-p[2],x+p[2],y+p[2]],fill=c+(230,))
    bg.alpha_composite(_glow(sp,3,1)); bg.alpha_composite(sp)
    for k,(cim,cx,sy,R,ne,cy) in enumerate(coins):
        bob=6*math.sin(t*2.0+k*2.1)
        im=cim.copy(); Sw,Sh=im.size
        g=Image.new('L',(Sw,Sh),0); gd=ImageDraw.Draw(g); ph=((t*0.42+k*0.37)%1.7)-0.35
        x0=int(Sw*ph); gd.polygon([(x0,0),(x0+Sw*0.10,0),(x0+Sw*0.10-Sw*0.45,Sh),(x0-Sw*0.45,Sh)],fill=170)
        g=g.filter(ImageFilter.GaussianBlur(Sw*0.025)); g=ImageChops.multiply(g,im.split()[3].point(lambda v:255 if v>200 else 0))
        wl=Image.new('RGBA',(Sw,Sh),(255,255,255,0)); wl.putalpha(g); im.alpha_composite(wl)
        top=int(sy-(cy+R*0.9+R*0.16)+bob)
        # odbicie na podescie
        rf=im.transpose(Image.FLIP_TOP_BOTTOM).resize((Sw,int(Sh*0.35))); rf.putalpha(rf.split()[3].point(lambda v:int(v*0.22)))
        bg.alpha_composite(rf.filter(ImageFilter.GaussianBlur(4)),(int(cx-Sw/2),int(sy-bob*0.3)))
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-R*0.95,sy-R*0.10,cx+R*0.95,sy+R*0.14],fill=(0,0,0,140))
        bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
        bg.alpha_composite(im,(int(cx-Sw/2),top))
    a=min(1,t/0.6); dy=int((1-a)*-60)
    tekst(bg,'XRP  −6.9%',FA,(W//2,175+dy),(255,255,255),(255,30,80),a)
    tekst(bg,'XLM −7.2%  ·  XDC −3.4%  ·  24H',F2,(W//2,318+dy),(235,240,255),(130,90,255),a,gr=10)
    # winieta
    return bg.convert('RGB')
if __name__=='__main__':
    if N==1: klatka(int(sys.argv[2]) if len(sys.argv)>2 else 60).save('kadr2.jpg',quality=93); sys.exit()
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','xrp_spadek_ruch_v2.mp4'],stdin=subprocess.PIPE)
    for i in range(N): p.stdin.write(klatka(i).tobytes())
    p.stdin.close(); p.wait(); klatka(N-1).save('kadr2.jpg',quality=93)

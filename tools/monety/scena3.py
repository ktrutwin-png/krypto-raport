import sys, math, numpy as np, subprocess
sys.path.insert(0,'.'); from monety import svg_logo, F_BOLD; from monety2 import coin2, _glow
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageEnhance
import scena2 as S2
W,H,FPS=1080,1920,30; N=int(sys.argv[1]) if len(sys.argv)>1 else 180
bg0=S2.bg0; bg0=ImageEnhance.Color(bg0).enhance(1.15)
# lekka glebia: tlo nad podestami lekko rozmyte w gornej czesci (bez niedzwiedzia nie da sie wyciac - delikatnie)
def coeffs(src,dst):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); A.append([0,0,0,x,y,1,-v*x,-v*y]); B+= [u,v]
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()
def tilt(im,yaw):
    w,h=im.size; s=math.cos(yaw); d=0.07*math.sin(yaw)
    nw=max(2,int(w*s)); off=(w-nw)/2
    dst=[(off,h*d),(off+nw,-h*d),(off+nw,h+h*d),(off,h-h*d)] if yaw>0 else [(off,-h*(-d)*0),(off+nw,0),(off+nw,h),(off,h)]
    dst=[(off,h*max(d,0)),(off+nw,h*max(-d,0)),(off+nw,h-h*max(-d,0)),(off,h-h*max(d,0))]
    return im.transform((w,h),Image.PERSPECTIVE,coeffs([(0,0),(w,0),(w,h),(0,h)],dst),Image.BICUBIC)
def promienie(cx,cy,ne,t):
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    for k in range(18):
        a=k/18*2*math.pi+t*0.25; w=0.05
        d.polygon([(cx,cy),(cx+1400*math.cos(a-w),cy+1400*math.sin(a-w)),(cx+1400*math.cos(a+w),cy+1400*math.sin(a+w))],fill=ne+(38,))
    return L.filter(ImageFilter.GaussianBlur(25))
def bloom(img):
    sm=img.resize((W//4,H//4),Image.BILINEAR); a=np.array(sm).astype(np.float32)
    lum=a.mean(-1,keepdims=True); m=np.clip((lum-150)/80,0,1); hi=Image.fromarray((a*m).astype(np.uint8))
    hi=hi.filter(ImageFilter.GaussianBlur(10)).resize((W,H),Image.BILINEAR)
    return ImageChops.screen(img,ImageEnhance.Brightness(hi).enhance(1.1))
def grade(img):
    a=np.array(img).astype(np.float32)/255
    a=np.clip((a-0.5)*1.12+0.5,0,1)                  # kontrast
    lum=a.mean(-1,keepdims=True); a=np.clip(lum+(a-lum)*1.25,0,1)   # nasycenie
    sh=np.clip(1-lum*2,0,1); hl=np.clip(lum*2-1,0,1)
    a=a+sh*np.array([0,0.025,0.05])+hl*np.array([0.03,0.0,0.03])     # cyan cienie, magenta swiatla
    return Image.fromarray((np.clip(a,0,1)*255).astype(np.uint8))
rng=np.random.default_rng(9); BK=[[rng.uniform(0,W),rng.uniform(0,H),rng.uniform(6,16),rng.uniform(15,45),rng.integers(3)] for _ in range(14)]
def klatka(i):
    t=i/FPS; z=1+0.06*min(1,i/180)
    bw,bh=int(W*z),int(H*z); bg=bg0.resize((bw,bh),Image.BILINEAR).crop(((bw-W)//2,(bh-H)//2,(bw-W)//2+W,(bh-H)//2+H)).convert('RGBA')
    puls=0.5+0.5*math.sin(t*3)
    im0,cx0,sy0,R0,ne0,cy0=S2.coins[2]
    bg.alpha_composite(promienie(cx0,sy0-R0*1.0,ne0,t))
    lt=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lt)
    for im,cx,sy,R,ne,cy in S2.coins: ld.ellipse([cx-R*2,sy-R*2.8,cx+R*2,sy+R*0.6],fill=ne+(int(70+45*puls),))
    bg.alpha_composite(lt.filter(ImageFilter.GaussianBlur(90)))
    sp=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sp)
    for p in S2.P:
        y=(p[1]-p[3]*t)%H; x=p[0]+14*math.sin(t*1.2+p[1]); c=S2.PC[p[4]]
        sd.ellipse([x-p[2],y-p[2],x+p[2],y+p[2]],fill=c+(235,))
    bg.alpha_composite(_glow(sp,3,1)); bg.alpha_composite(sp)
    for k,(cim,cx,sy,R,ne,cy) in enumerate(S2.coins):
        yaw=math.radians(16*math.sin(t*1.05+k*1.7)); bob=7*math.sin(t*2.0+k*2.1)
        im=cim.copy(); Sw,Sh=im.size
        g=Image.new('L',(Sw,Sh),0); gd=ImageDraw.Draw(g); ph=((t*0.42+k*0.37)%1.7)-0.35
        x0=int(Sw*ph); gd.polygon([(x0,0),(x0+Sw*0.10,0),(x0+Sw*0.10-Sw*0.45,Sh),(x0-Sw*0.45,Sh)],fill=190)
        g=g.filter(ImageFilter.GaussianBlur(Sw*0.025)); g=ImageChops.multiply(g,im.split()[3].point(lambda v:255 if v>200 else 0))
        wl=Image.new('RGBA',(Sw,Sh),(255,255,255,0)); wl.putalpha(g); im.alpha_composite(wl)
        im=tilt(im,yaw)
        top=int(sy-(cy+R*0.9+R*0.16)+bob)
        rf=im.transpose(Image.FLIP_TOP_BOTTOM).resize((Sw,int(Sh*0.35))); rf.putalpha(rf.split()[3].point(lambda v:int(v*0.25)))
        bg.alpha_composite(rf.filter(ImageFilter.GaussianBlur(4)),(int(cx-Sw/2),int(sy-bob*0.3)))
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-R*0.95,sy-R*0.10,cx+R*0.95,sy+R*0.14],fill=(0,0,0,150))
        bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
        bg.alpha_composite(im,(int(cx-Sw/2),top))
    # bokeh na pierwszym planie
    bk=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(bk)
    for p in BK:
        y=(p[1]-p[3]*t)%H; c=S2.PC[p[4]]; bd.ellipse([p[0]-p[2],y-p[2],p[0]+p[2],y+p[2]],fill=c+(90,))
    bg.alpha_composite(bk.filter(ImageFilter.GaussianBlur(5)))
    a=min(1,t/0.6); dy=int((1-a)*-60); sc=1+0.04*math.sin(t*3) if t>0.6 else 1
    S2.tekst(bg,'XRP  −6.9%',S2.FA,(W//2,175+dy),(255,255,255),(255,30,80),a)
    S2.tekst(bg,'XLM −7.2%  ·  XDC −3.4%  ·  24H',S2.F2,(W//2,318+dy),(235,240,255),(130,90,255),a,gr=10)
    out=grade(bg.convert('RGB')); out=bloom(out)
    # winieta
    v=Image.new('L',(W,H),0); ImageDraw.Draw(v).ellipse([-250,-200,W+250,H+200],fill=255); v=v.filter(ImageFilter.GaussianBlur(160))
    out=Image.composite(out,ImageEnhance.Brightness(out).enhance(0.55),v)
    return out
if __name__=='__main__':
    if N==1: klatka(int(sys.argv[2]) if len(sys.argv)>2 else 60).save('kadr3.jpg',quality=93); sys.exit()
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart','xrp_spadek_ruch_v3.mp4'],stdin=subprocess.PIPE)
    for i in range(N): p.stdin.write(klatka(i).tobytes())
    p.stdin.close(); p.wait(); klatka(70).save('kadr3.jpg',quality=93)

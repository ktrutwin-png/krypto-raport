"""Hero strony crypto freaq (24.11.2026): tlo z generatora (miasto + globus + podesty) + AUTENTYCZNE monety XRP/XLM/XDC na podestach."""
import sys, numpy as np
sys.path.insert(0,'.'); from monety import svg_logo; from monety2 import coin2, _glow
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
REPO='/home/claude/krypto-raport/marka'
src=Image.open(f'{REPO}/propozycje/hero/hero_d1.webp').convert('RGB')
def przygotuj(im,W,H):
    im=im.resize((W,H),Image.LANCZOS); im=ImageEnhance.Contrast(im).enhance(1.10); im=ImageEnhance.Color(im).enhance(1.18)
    return im.filter(ImageFilter.UnsharpMask(2,90,2)).convert('RGBA')
def loga(rx,rl,rd):   # logo proporcjonalne do promienia monety (jak w scena2: XRP 1.1 R, XLM/XDC 1.25 R)
    XRP=svg_logo(f'{REPO}/loga/xrp.svg',int(rx*1.1)); XLM=svg_logo(f'{REPO}/loga/xlm.svg',int(rl*1.25))
    x=Image.open(f'{REPO}/loga/xdc_xdc-icon.png').convert('RGBA').resize((int(rd*1.25),int(rd*1.25)),Image.LANCZOS)
    a=np.array(x).astype(np.float32); lum=a[...,:3].mean(-1); m=np.clip((lum-150)/60,0,1)*(a[...,3]/255)
    return XRP,XLM,Image.fromarray(np.dstack([np.full(lum.shape+(3,),255),m*255]).astype(np.uint8),'RGBA')
def poloz(bg,spec):
    W,H=bg.size; lt=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lt)
    for lg,nm,ne,cx,sy,R,sd in spec: ld.ellipse([cx-R*1.9,sy-R*2.6,cx+R*1.9,sy+R*0.5],fill=ne+(70,))
    bg.alpha_composite(lt.filter(ImageFilter.GaussianBlur(70)))
    for lg,nm,ne,cx,sy,R,sd in spec:   # od najdalszej
        im=coin2(R,lg,nm,ne,seed=sd); Sw,Sh=im.size; cy=Sh//2
        top=int(sy-(cy+R*0.9+R*0.16))
        rf=im.transpose(Image.FLIP_TOP_BOTTOM).resize((Sw,int(Sh*0.35))); rf.putalpha(rf.split()[3].point(lambda v:int(v*0.25)))
        bg.alpha_composite(rf.filter(ImageFilter.GaussianBlur(4)),(int(cx-Sw/2),int(sy)))
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-R*0.95,sy-R*0.10,cx+R*0.95,sy+R*0.14],fill=(0,0,0,150))
        bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
        bg.alpha_composite(im,(int(cx-Sw/2),top))
    return bg
def wykoncz(img):
    W,H=img.size; sm=img.resize((W//4,H//4)); a=np.array(sm).astype(np.float32); m=np.clip((a.mean(-1,keepdims=True)-150)/80,0,1)
    hi=Image.fromarray((a*m).astype(np.uint8)).filter(ImageFilter.GaussianBlur(8)).resize((W,H))
    return ImageChops.screen(img,hi)
s=1920/1536; D=przygotuj(src,1920,1080)
XRP,XLM,XDC=loga(118,66,48)
spec=[(XDC,'XDC',(40,150,255),int(885*s),int(606*s),48,5),(XLM,'XLM',(190,90,255),int(982*s),int(634*s),66,3),(XRP,'XRP',(50,210,255),int(1172*s),int(690*s),118,7)]
D=wykoncz(poloz(D,spec).convert('RGB'))
D.save(f'{REPO}/propozycje/hero/hero_strona_d.jpg',quality=93)
# telefon: wycinek 9:16 wokol podestow, monety rysowane ostro w pelnej rozdzielczosci
x0=820; cw=int(864*9/16); k=1920/864
Y0=150   # przesuniecie w gore: monety nad tekstem na telefonie
M0=przygotuj(src.crop((x0,Y0,x0+cw,864)),1080,int((864-Y0)*k)); M=Image.new('RGBA',(1080,1920),(5,5,7,255)); M.alpha_composite(M0)
M.alpha_composite(M0.transpose(Image.FLIP_TOP_BOTTOM).crop((0,0,1080,1920-M0.size[1])).filter(ImageFilter.GaussianBlur(6)),(0,M0.size[1]))
f=lambda x,y:(int((x-x0)*k),int((y-Y0)*k))
XRP,XLM,XDC=loga(170,110,80)
spec=[(XDC,'XDC',(40,150,255),*f(885,606),80,5),(XLM,'XLM',(190,90,255),*f(982,634),110,3),(XRP,'XRP',(50,210,255),*f(1172,690),170,7)]
M=wykoncz(poloz(M,spec).convert('RGB'))
M.save(f'{REPO}/propozycje/hero/hero_strona_m.jpg',quality=93)
print('ok')

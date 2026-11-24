"""Karta karuzeli 'sunset neon' 1080x1350: scena (postac) + tytul z prawdziwa liczba + moneta z logo + efekty pogody."""
import sys, numpy as np, math
sys.path.insert(0,'.'); from monety import svg_logo, F_BOLD; from monety2 import coin2, _glow
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance, ImageChops
REPO='/home/claude/krypto-raport/marka'; W,H=1080,1350
FA=lambda s:ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf',s)
def fb(s,w=800):
    f=ImageFont.truetype(F_BOLD,s); f.set_variation_by_axes([w]); return f
def scena(path,x0,x1):
    im=Image.open(path).convert('RGB'); cw=x1-x0; im=im.crop((x0,0,x1,im.size[1]))
    k=W/cw; im=im.resize((W,int(im.size[1]*k)),Image.LANCZOS); top=H-im.size[1]
    bg=im.crop((0,0,W,top+120)).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(22)) if top>0 else None
    c=Image.new('RGB',(W,H)); 
    if top>0:
        c.paste(bg,(0,0))
        m=Image.linear_gradient('L').resize((W,120)); c.paste(im.crop((0,0,W,120)),(0,top),Image.eval(m,lambda v:v))  # miekkie przejscie
        c.paste(im.crop((0,120,W,im.size[1])),(0,top+120))
    else: c.paste(im,(0,top))
    return c.convert('RGBA')
def tekst(img,t,font,xy,fill,glow,anchor='mm',gr=18,st=3):
    L=lambda fn:(lambda l:(fn(ImageDraw.Draw(l)),l)[1])(Image.new('RGBA',img.size,(0,0,0,0)))
    img.alpha_composite(_glow(L(lambda d:d.text(xy,t,font=font,fill=glow+(255,),anchor=anchor,stroke_width=8,stroke_fill=glow+(255,))),gr,3))
    img.alpha_composite(L(lambda d:d.text((xy[0]+5,xy[1]+7),t,font=font,fill=(0,0,0,210),anchor=anchor)).filter(ImageFilter.GaussianBlur(4)))
    img.alpha_composite(L(lambda d:d.text(xy,t,font=font,fill=fill+(255,),anchor=anchor,stroke_width=st,stroke_fill=(255,255,255,255))))
def deszcz(img,n=900,seed=1):
    r=np.random.default_rng(seed); L=Image.new('RGBA',img.size,(0,0,0,0)); d=ImageDraw.Draw(L)
    for _ in range(n):
        x=r.uniform(-100,W); y=r.uniform(-50,H); l=r.uniform(25,70); a=int(r.uniform(50,140))
        d.line([(x,y),(x+l*0.25,y+l)],fill=(190,215,255,a),width=int(r.integers(1,3)))
    img.alpha_composite(L.filter(ImageFilter.GaussianBlur(0.6)))
    ImageDraw.Draw(img).rectangle([0,0,W,H],fill=None)
    img.alpha_composite(Image.new('RGBA',img.size,(20,40,90,40)))
def zloto(img,seed=2):
    r=np.random.default_rng(seed); L=Image.new('RGBA',img.size,(0,0,0,0)); d=ImageDraw.Draw(L)
    for _ in range(55):
        x=r.uniform(0,W); y=r.uniform(0,H*0.75); s=r.uniform(1,3.2)
        d.ellipse([x-s,y-s,x+s,y+s],fill=(255,int(r.uniform(190,230)),120,int(r.uniform(140,240))))
    img.alpha_composite(_glow(L,4,2)); img.alpha_composite(L)
    img.alpha_composite(Image.new('RGBA',img.size,(255,170,60,22)))
def moneta(img,logo,nazwa,neon,cx,cy,R):
    c=coin2(R,logo,nazwa,neon,seed=4); s=c.size[0]
    img.alpha_composite(_glow(Image.new('RGBA',img.size,(0,0,0,0)),1,1))
    gl=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(gl).ellipse([cx-R*1.4,cy-R*1.4,cx+R*1.4,cy+R*1.4],fill=neon+(110,)); img.alpha_composite(gl.filter(ImageFilter.GaussianBlur(40)))
    img.alpha_composite(c,(int(cx-s/2),int(cy-s/2)))
def stopka(img):
    d=ImageDraw.Draw(img); g=Image.new('RGBA',img.size,(0,0,0,0)); gd=ImageDraw.Draw(g)
    for i in range(160): gd.line([(0,H-160+i),(W,H-160+i)],fill=(5,5,10,int(i*1.3)))
    img.alpha_composite(g)
    d.text((48,H-56),'ERL.GREY83',font=fb(30,700),fill=(244,241,234),anchor='lm')
    d.text((W-48,H-56),'NOT FINANCIAL ADVICE',font=fb(22,600),fill=(200,200,210),anchor='rm')
def karta(scn,x0,x1,tytul,kolor,glow,linia,logo,nazwa,neon,fx,wyj,demo=False):
    img=scena(scn,x0,x1); img=ImageEnhance.Contrast(img.convert('RGB')).enhance(1.06).convert('RGBA')
    (deszcz if fx=='deszcz' else zloto)(img)
    v=Image.new('RGBA',img.size,(0,0,0,0)); vd=ImageDraw.Draw(v)
    tc=(5,5,10,170) if fx=='deszcz' else (60,25,10,95)
    for i in range(360): vd.line([(0,i),(W,i)],fill=tc[:3]+(int(tc[3]*(1-i/360)**1.6),))
    img.alpha_composite(v)
    moneta(img,logo,nazwa,neon,150,170,82)
    tekst(img,tytul,FA(150),(W//2+90,165),kolor,glow)
    tekst(img,linia,fb(40),(W//2+90,285),(245,245,250),glow,gr=10,st=0)
    if demo: ImageDraw.Draw(img).text((W-40,40),'PRZYKŁAD',font=fb(22),fill=(255,255,255,200),anchor='rt')
    stopka(img); img.convert('RGB').save(wyj,quality=93)
P=f'{REPO}/propozycje/sunset'
XRP=svg_logo(f'{REPO}/loga/xrp.svg',int(82*1.1)); XLM=svg_logo(f'{REPO}/loga/xlm.svg',int(82*1.25))
karta(f'{P}/krach_el.png',540,1640,'XRP −8.7%',(255,255,255),(255,30,70),'$0.912  ·  24H  ·  STORM ON THE CHART',XRP,'XRP',(50,210,255),'deszcz',f'{P}/karta_krach.jpg')
karta(f'{P}/rakieta_el.png',820,1920,'XLM +12.4%',(255,236,170),(255,150,30),'PARTY ON DECK  ·  24H',XLM,'XLM',(190,90,255),'zloto',f'{P}/karta_rakieta.jpg',demo=True)
print('ok')

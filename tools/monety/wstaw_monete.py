"""Wstawia realistyczna monete DO sceny (jak obiekt w grze): perspektywa, swiatlo sceny (neonowe obrysy), cien kontaktowy, odbicie na mokrym asfalcie, glebia."""
import sys, math, numpy as np
sys.path.insert(0,'.'); from scena3 import tilt, coeffs
from PIL import Image, ImageFilter, ImageChops, ImageEnhance, ImageDraw
def wstaw(scena, moneta, cx, dol, D, yaw=25, ambient=(0.70,0.78,1.0), rim_l=(60,220,255), rim_p=(255,60,170), rozmycie=0.0, mokro=True):
    sc=scena.convert('RGBA'); W,H=sc.size
    m=moneta.resize((D,D),Image.LANCZOS)
    # grubosc (rant) - kilka przesunietych ciemnych kopii
    gr=Image.new('RGBA',(int(D*1.12),D),(0,0,0,0))
    rant=Image.new('RGBA',(D,D),(0,0,0,0)); rant.putalpha(m.split()[3])
    rant=Image.composite(Image.new('RGBA',(D,D),(70,72,80,255)),rant,m.split()[3])
    for k in range(int(D*0.08),0,-1): gr.alpha_composite(rant,(k,0))
    gr.alpha_composite(m,(0,0))
    im=tilt(gr,math.radians(yaw))
    a=np.asarray(im).astype(np.float32); rgb=a[...,:3]*np.array(ambient); al=a[...,3]/255
    # neonowe obrysy z lewej (cyjan) i prawej (roz)
    A=Image.fromarray((al*255).astype(np.uint8)); er=np.asarray(A.filter(ImageFilter.MinFilter(9))).astype(np.float32)/255
    brzeg=np.clip(al-er,0,1); w=im.size[0]; xs=np.linspace(0,1,w)[None,:]
    rgb+= (brzeg*np.clip(1.6-3*xs,0,1))[...,None]*np.array(rim_l)*1.1
    rgb+= (brzeg*np.clip(3*xs-1.4,0,1))[...,None]*np.array(rim_p)*1.2
    # delikatny poblask sceny od dolu (roz z asfaltu)
    ys=np.linspace(0,1,im.size[1])[:,None]; rgb+= (al*np.clip(ys-0.6,0,1)*0.6)[...,None]*np.array(rim_p)*0.5
    im=Image.fromarray(np.dstack([np.clip(rgb,0,255),al*255]).astype(np.uint8),'RGBA')
    if rozmycie: im=im.filter(ImageFilter.GaussianBlur(rozmycie))
    x0=int(cx-im.size[0]/2); y0=int(dol-im.size[1])
    # cien kontaktowy
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([x0+im.size[0]*0.05,dol-D*0.05,x0+im.size[0]*1.05,dol+D*0.06],fill=(0,0,0,190))
    sc.alpha_composite(sh.filter(ImageFilter.GaussianBlur(D*0.04)))
    if mokro:   # odbicie na mokrej nawierzchni
        rf=im.transpose(Image.FLIP_TOP_BOTTOM); r=np.asarray(rf).astype(np.float32)
        fade=np.linspace(0.45,0,rf.size[1])[:,None]; r[...,3]*=fade
        rf=Image.fromarray(r.astype(np.uint8),'RGBA').filter(ImageFilter.GaussianBlur(D*0.02))
        sc.alpha_composite(rf,(x0,dol))
    # poswiata neonu wokol
    gl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([cx-D*0.8,dol-D*1.1,cx+D*0.8,dol+D*0.1],fill=rim_l+(40,)); sc.alpha_composite(gl.filter(ImageFilter.GaussianBlur(D*0.3)))
    sc.alpha_composite(im,(x0,y0))
    return sc
if __name__=='__main__':
    REPO='/home/claude/krypto-raport/marka'; P=f'{REPO}/propozycje/sunset'
    s=Image.open(f'{P}/flux_krach.jpg'); m=Image.open(f'{REPO}/monety_real/xrp.png')
    out=wstaw(s,m,cx=800,dol=930,D=230,yaw=28)
    out.convert('RGB').save(f'{P}/flux_krach_moneta.jpg',quality=94); print('ok')

def polozona(scena, moneta, cx, cy, D, sp=0.42, ambient=(0.72,0.8,1.0), rim=(255,60,170), rim2=(60,220,255)):
    """Moneta lezaca na mokrej ulicy (rzut z gory pod katem): elipsa + widoczny rant + odbicie neonow + cien."""
    sc=scena.convert('RGBA'); W,H=sc.size; h=int(D*sp); T=max(3,int(D*0.07))
    face=moneta.resize((D,h),Image.LANCZOS)
    a=np.asarray(face).astype(np.float32); al=a[...,3]/255; rgb=a[...,:3]*np.array(ambient)
    ys=np.linspace(0,1,h)[:,None]; xs=np.linspace(0,1,D)[None,:]
    rgb+=(al*np.clip(xs-0.55,0,1)*0.9)[...,None]*np.array(rim)*0.55      # roz z prawej (neony)
    rgb+=(al*np.clip(0.45-xs,0,1)*0.9)[...,None]*np.array(rim2)*0.45     # cyjan z lewej
    rgb+=(al*np.clip(0.35-ys,0,1)*1.2)[...,None]*np.array([200,210,255])*0.35   # blysk nieba na gornej krawedzi
    face=Image.fromarray(np.dstack([np.clip(rgb,0,255),al*255]).astype(np.uint8),'RGBA')
    body=Image.new('RGBA',(D,h+T),(0,0,0,0))
    rant=Image.new('RGBA',(D,h),(0,0,0,0)); rant.putalpha(face.split()[3])
    for k in range(T,0,-1):
        v=int(40+70*(1-k/T)); col=Image.new('RGBA',(D,h),(v,int(v*0.95),int(v*1.15),255)); col.putalpha(face.split()[3]); body.alpha_composite(col,(0,k))
    body.alpha_composite(face,(0,0))
    x0=int(cx-D/2); y0=int(cy-h/2)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([x0-D*0.03,y0+h*0.25,x0+D*1.05,y0+h+T+D*0.05],fill=(0,0,0,200)); sc.alpha_composite(sh.filter(ImageFilter.GaussianBlur(D*0.04)))
    rf=body.transpose(Image.FLIP_TOP_BOTTOM); r=np.asarray(rf).astype(np.float32); r[...,3]*=np.linspace(0.35,0,rf.size[1])[:,None]
    sc.alpha_composite(Image.fromarray(r.astype(np.uint8),'RGBA').filter(ImageFilter.GaussianBlur(D*0.015)),(x0,y0+h+T))
    sc.alpha_composite(body,(x0,y0))
    # kropelki wody na monecie
    rng=np.random.default_rng(3); dr=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(dr)
    for _ in range(int(D/18)):
        px=rng.uniform(x0+D*0.1,x0+D*0.9); py=rng.uniform(y0+h*0.15,y0+h*0.85); rr=rng.uniform(1.5,4)
        dd.ellipse([px-rr,py-rr*0.6,px+rr,py+rr*0.6],fill=(230,240,255,110))
    sc.alpha_composite(dr)
    return sc

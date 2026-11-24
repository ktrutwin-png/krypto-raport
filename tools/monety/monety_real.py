"""Realistyczne monety (24.11.2026): fotorealistyczny pusty krazek z FLUX (Cloudflare, darmowy) + AUTENTYCZNE logo wytloczone w metalu (relief, faza, cien)."""
import sys, numpy as np
sys.path.insert(0,'.'); from monety import svg_logo
from PIL import Image, ImageFilter
REPO='/home/claude/krypto-raport/marka'; B=f'{REPO}/monety_real/blanki'
def wytnij(path):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(np.float32); L=a.mean(-1)
    m=L>28; cols=np.where(m.any(0))[0]; x0,x1=cols[0],cols[-1]; D=x1-x0; cx=(x0+x1)/2
    rows=np.where(m.any(1))[0]; cy=rows[0]+D/2
    S=int(D*1.04); box=(int(cx-S/2),int(cy-S/2),int(cx-S/2)+S,int(cy-S/2)+S)
    c=im.crop(box); y,x=np.mgrid[0:S,0:S]; r=np.hypot(x-S/2,y-S/2)
    al=np.clip((D/2-r)*1.5,0,1)*255
    c=c.convert('RGBA'); c.putalpha(Image.fromarray(al.astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))); return c
def metal(h,w,kind):
    t=np.linspace(0,1,h)[:,None]*np.ones((1,w))
    if kind=='chrom': v=0.80+0.18*np.cos(t*np.pi*2.2+0.6); base=np.stack([v*238,v*242,v*252],-1)
    elif kind=='zloto': v=0.85+0.15*np.cos(t*np.pi*1.8+0.4); base=np.stack([v*255,v*212,v*110],-1)
    else: v=0.78+0.18*np.cos(t*np.pi*2+0.3); base=np.stack([v*232,v*235,v*242],-1)
    return np.clip(base,0,255)
def wytlocz(coin,logo,frac,kind,glebia=1.0):
    S=coin.size[0]; ls=int(S*frac); lg=logo.resize((ls,int(ls*logo.size[1]/logo.size[0])),Image.LANCZOS)
    A=Image.new('L',(S,S),0); A.paste(lg.split()[3],((S-lg.size[0])//2,(S-lg.size[1])//2))
    a=np.asarray(A).astype(np.float32)/255
    h=np.asarray(A.filter(ImageFilter.GaussianBlur(S*0.006))).astype(np.float32)/255
    gy,gx=np.gradient(h); sh=np.clip(-(gx*-0.7+gy*-0.7)*S*0.08*glebia,-1,1)   # swiatlo z lewej-gory
    c=np.asarray(coin).astype(np.float32); rgb=c[...,:3]; al=c[...,3:]
    # cien rzucany przez relief
    cien=np.asarray(A.filter(ImageFilter.GaussianBlur(S*0.012)).transform((S,S),Image.AFFINE,(1,0,-S*0.012,0,1,-S*0.016))).astype(np.float32)/255
    rgb=rgb*(1-0.55*cien[...,None]*(1-a[...,None]))
    fill=metal(S,S,kind); fill=fill*(0.90+0.10*(rgb.mean(-1,keepdims=True)/255))   # odbicia krazka przenikaja w relief
    rgb=rgb*(1-a[...,None])+fill*a[...,None]
    rgb=rgb+np.where(sh[...,None]>0,sh[...,None]*255*0.85,sh[...,None]*255*0.6)
    # drobna faktura i blysk krawedzi
    rgb=np.clip(rgb,0,255); out=np.concatenate([rgb,al],-1).astype(np.uint8)
    return Image.fromarray(out,'RGBA')
def xdc_logo(size):
    x=Image.open(f'{REPO}/loga/xdc_xdc-icon.png').convert('RGBA').resize((size,size),Image.LANCZOS)
    a=np.asarray(x).astype(np.float32); lum=a[...,:3].mean(-1); m=np.clip((lum-150)/60,0,1)*(a[...,3]/255)
    return Image.fromarray(np.dstack([np.full(lum.shape+(3,),255),m*255]).astype(np.uint8),'RGBA')
SPEC={'XRP':('blank_czarna_1.jpg',lambda s:svg_logo(f'{REPO}/loga/xrp.svg',s),0.50,'chrom'),
      'XLM':('blank_srebro_2.jpg',lambda s:svg_logo(f'{REPO}/loga/xlm.svg',s),0.52,'srebro'),
      'XDC':('blank_czarna_2.jpg',xdc_logo,0.56,'chrom'),
      'BTC':('blank_zloto_2.jpg',lambda s:svg_logo(f'{REPO}/loga/bitcoin.svg',s),0.50,'zloto'),
      'ETH':('blank_srebro_2.jpg',lambda s:svg_logo(f'{REPO}/loga/ethereum.svg',s),0.40,'srebro')}
def moneta(nazwa):
    plik,lf,frac,kind=SPEC[nazwa]; c=wytnij(f'{B}/{plik}'); return wytlocz(c,lf(1200),frac,kind)
if __name__=='__main__':
    out=f'{REPO}/monety_real'; pok=Image.new('RGB',(5*420,460),(8,8,12))
    for i,n in enumerate(SPEC):
        m=moneta(n); m.save(f'{out}/{n.lower()}.png'); pok.paste(m.resize((400,400),Image.LANCZOS),(10+i*420,30),m.resize((400,400),Image.LANCZOS))
    pok.save(f'{out}/pokaz.jpg',quality=92); print('ok')

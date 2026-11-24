import numpy as np, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
from monety import svg_logo, F_BOLD
def _glow(im, r, k=2):
    g=im.filter(ImageFilter.GaussianBlur(r)); out=g
    for _ in range(k-1): out=Image.alpha_composite(out,g)
    return out
def coin2(R, logo, name, neon, metal=(52,58,74), crack=False, seed=1):
    S=int(R*2.9); c=S//2; T=int(R*0.16); neon=tuple(neon); nf=np.array(neon,np.float32)/255
    y,x=np.mgrid[0:S,0:S].astype(np.float32); dx=(x-c)/R; dy=(y-c)/R; r=np.sqrt(dx*dx+dy*dy); ang=np.arctan2(dy,dx)
    inside=r<=1; base=np.array(metal,np.float32)/255
    shade=np.clip(0.5-0.45*(dx*0.55+dy*0.85),0,1)
    face=base*(0.45+0.9*shade[...,None]); face*=(0.9+0.1*np.sin(r*220))[...,None]
    # radial light from centre
    face+=nf*0.10*np.clip(1-r,0,1)[...,None]
    rim=(r>0.83)
    ridges=0.8+0.2*np.sin(ang*200)
    rimc=(base*0.5+nf*0.45)*(0.55+0.9*shade[...,None])*ridges[...,None]
    col=np.where(rim[...,None],rimc,face)
    for rr,w,k in ((0.83,0.010,1.8),(0.995,0.012,1.6),(0.72,0.006,1.3)):
        m=np.abs(r-rr)<w; col[m]=np.clip(col[m]*k+nf*0.25,0,1)
    nr=np.exp(-((r-0.79)/0.014)**2); col=np.clip(col+nr[...,None]*nf*1.3,0,1)
    face_im=Image.fromarray(np.dstack([col*255,inside*255]).astype(np.uint8),'RGBA')
    d=ImageDraw.Draw(face_im)
    # circuit traces
    rng=np.random.default_rng(seed); tr=Image.new('RGBA',(S,S),(0,0,0,0)); td=ImageDraw.Draw(tr)
    for _ in range(26):
        a=rng.uniform(0,2*math.pi); rr=rng.uniform(0.25,0.7)*R; px,py=c+rr*math.cos(a),c+rr*math.sin(a)
        for s in range(3):
            L=rng.uniform(0.05,0.15)*R; dirn=rng.integers(4); nx,ny=px+[L,-L,0,0][dirn],py+[0,0,L,-L][dirn]
            if math.hypot(nx-c,ny-c)>0.74*R: break
            td.line([px,py,nx,ny],fill=neon+(70,),width=2); px,py=nx,ny
        td.ellipse([px-3,py-3,px+3,py+3],fill=neon+(110,))
    face_im.alpha_composite(tr)
    for i in range(96):
        a=i/96*2*math.pi; rr=0.905*R; px,py=c+rr*math.cos(a),c+rr*math.sin(a)
        d.rectangle([px-2,py-2,px+2,py+2],fill=(18,22,30,255) if i%3 else neon+(255,))
    # logo: white->neon gradient, glow, emboss
    L=logo; lx=c-L.width//2; ly=int(c-L.height//2-R*0.10); a=L.split()[3]
    gl=Image.new('RGBA',(S,S),(0,0,0,0)); t=Image.new('RGBA',L.size,neon+(255,)); t.putalpha(a); gl.paste(t,(lx,ly),t)
    face_im=Image.alpha_composite(face_im,_glow(gl,R*0.07,3))
    sh=Image.new('RGBA',L.size,(5,6,10,230)); sh.putalpha(a.point(lambda v:int(v*0.9))); face_im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)),(lx+5,ly+7))
    gy=np.linspace(0,1,L.height)[:,None]*np.ones((1,L.width))
    rgb=(1-gy[...,None]*0.75)*np.array([1,1,1])+gy[...,None]*0.75*nf
    rgb=rgb*0.97; met=np.dstack([np.clip(rgb,0,1)*255,np.array(a,np.float32)]).astype(np.uint8)
    face_im.alpha_composite(Image.fromarray(met,'RGBA'),(lx,ly))
    hl=Image.new('RGBA',L.size,(255,255,255,255)); hl.putalpha(a.point(lambda v:int(v*0.55))); 
    edge=ImageChops.subtract(a,a.transform(a.size,Image.AFFINE,(1,0,2,0,1,2))); hl.putalpha(edge); face_im.alpha_composite(hl,(lx,ly))
    f=ImageFont.truetype(F_BOLD,int(R*0.22)); f.set_variation_by_axes([800]); d=ImageDraw.Draw(face_im)
    tw=d.textlength(name,font=f); tx=c-tw/2; ty=c+R*0.40
    tl=Image.new('RGBA',(S,S),(0,0,0,0)); ImageDraw.Draw(tl).text((tx,ty),name,font=f,fill=neon+(255,))
    face_im=Image.alpha_composite(face_im,_glow(tl,8,2))
    d=ImageDraw.Draw(face_im); d.text((tx+2,ty+3),name,font=f,fill=(5,6,10,255)); d.text((tx,ty),name,font=f,fill=(245,248,255,255))
    if crack:
        cr=Image.new('RGBA',(S,S),(0,0,0,0)); cd=ImageDraw.Draw(cr)
        for a0 in (-2.3,-1.0,0.5,2.1):
            px,py=c+0.98*R*math.cos(a0),c+0.98*R*math.sin(a0); an=a0+math.pi
            for s in range(8):
                an+=rng.uniform(-0.6,0.6); Ls=R*rng.uniform(0.05,0.1); nx,ny=px+Ls*math.cos(an),py+Ls*math.sin(an)
                cd.line([px,py,nx,ny],fill=(255,255,255,255),width=3)
                if rng.random()<0.4: b=an+rng.choice([-1,1])*0.9; cd.line([nx,ny,nx+Ls*0.6*math.cos(b),ny+Ls*0.6*math.sin(b)],fill=(255,255,255,255),width=2)
                px,py=nx,ny
        msk=Image.fromarray((inside*255).astype(np.uint8)); cr.putalpha(ImageChops.multiply(cr.split()[3],msk))
        cn=Image.new('RGBA',(S,S),neon+(0,)); cn.putalpha(cr.split()[3])
        face_im=Image.alpha_composite(face_im,_glow(cn,6,3)); face_im=Image.alpha_composite(face_im,cr)
    # thickness: squash face, draw edge below
    sq=0.90; Fh=int(S*sq); face_sq=face_im.resize((S,Fh),Image.LANCZOS)
    out=Image.new('RGBA',(S,Fh+T+4),(0,0,0,0)); od=ImageDraw.Draw(out)
    cy=Fh//2
    for k in range(T,0,-1):
        tcol=tuple(int(v) for v in (np.array(metal)*0.55+np.array(neon)*0.25*(k/T)))
        od.ellipse([c-R,cy-R*sq+k,c+R,cy+R*sq+k],fill=tcol+(255,))
    od.ellipse([c-R,cy-R*sq+T,c+R,cy+R*sq+T],outline=neon+(255,),width=3)
    out.alpha_composite(face_sq,(0,0))
    halo=Image.new('RGBA',out.size,(0,0,0,0)); ImageDraw.Draw(halo).ellipse([c-R*1.03,cy-R*sq*1.03,c+R*1.03,cy+R*sq*1.03+T],outline=neon+(255,),width=int(R*0.08))
    res=Image.alpha_composite(_glow(halo,R*0.14,3),out)
    return res

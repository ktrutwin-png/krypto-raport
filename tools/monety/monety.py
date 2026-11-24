import numpy as np, io, math, cairosvg
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
F_BOLD="/usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf"
def svg_logo(path, size, color=(255,255,255)):
    svg=open(path).read()
    png=cairosvg.svg2png(bytestring=svg.encode(), output_width=size)
    im=Image.open(io.BytesIO(png)).convert("RGBA")
    a=im.split()[3]; out=Image.new("RGBA",im.size,color+(0,)); out.putalpha(a); return out
def png_logo(path,size,color=(255,255,255),thr=None):
    im=Image.open(path).convert("RGBA"); im=im.resize((size,int(size*im.height/im.width)),Image.LANCZOS)
    return im
def coin(R, logo, name, neon, metal=(185,192,205), crack=False):
    S=int(R*2.6); c=S//2
    y,x=np.mgrid[0:S,0:S].astype(np.float32); dx=(x-c)/R; dy=(y-c)/R; r=np.sqrt(dx*dx+dy*dy)
    img=np.zeros((S,S,4),np.float32)
    inside=r<=1
    # metal shading: light from top-left
    shade=0.55+0.45*np.clip(-(dx*0.6+dy*0.8)*0.6+0.4,0,1)
    ang=np.arctan2(dy,dx)
    rim=(r>0.84)&(r<=1)
    ridges=0.85+0.15*np.sin(ang*180)
    base=np.array(metal,np.float32)/255
    col=np.zeros((S,S,3),np.float32)
    face=base*(0.35+0.5*shade[...,None])
    # subtle concentric brushing
    face*= (0.93+0.07*np.sin(r*160))[...,None]
    col[inside]=face[inside]
    rimc=(base*0.6+np.array(neon,np.float32)/255*0.35)*(0.6+0.7*shade[...,None])*ridges[...,None]
    col[rim]=rimc[rim]
    # bevel lines
    for rr,w,k in ((0.84,0.012,1.4),(0.995,0.01,0.5)):
        m=np.abs(r-rr)<w; col[m]=np.clip(col[m]*k,0,1)
    img[...,:3]=col; img[...,3]=inside.astype(np.float32)
    # inner neon ring
    nr=np.exp(-((r-0.80)/0.012)**2)
    ncol=np.array(neon,np.float32)/255
    img[...,:3]=np.clip(img[...,:3]+nr[...,None]*ncol*1.2,0,1)
    out=Image.fromarray((img*255).astype(np.uint8),"RGBA")
    # tiny text ring (circuit dots)
    d=ImageDraw.Draw(out)
    for i in range(72):
        a=i/72*2*math.pi; rr=0.89*R
        px,py=c+rr*math.cos(a),c+rr*math.sin(a); d.ellipse([px-2,py-2,px+2,py+2],fill=(30,34,42,255))
    # logo emboss
    L=logo; lx=c-L.width//2; ly=int(c-L.height//2-R*0.12)
    a=L.split()[3]
    sh=Image.new("RGBA",L.size,(10,12,18,255)); sh.putalpha(a)
    hi=Image.new("RGBA",L.size,(255,255,255,255)); hi.putalpha(a)
    glow=Image.new("RGBA",(S,S),(0,0,0,0)); gl=Image.new("RGBA",L.size,tuple(neon)+(255,)); gl.putalpha(a)
    glow.paste(gl,(lx,ly),gl); glow=glow.filter(ImageFilter.GaussianBlur(R*0.08)); glow=Image.alpha_composite(glow,glow)
    out=Image.alpha_composite(out,glow)
    out.alpha_composite(sh,(lx+4,ly+5)); out.alpha_composite(hi,(lx-2,ly-2))
    # logo metallic gradient
    g=np.linspace(1.0,0.62,L.height)[:,None]*np.ones((1,L.width))
    met=np.stack([g*235,g*240,g*250,np.array(a,np.float32)],-1).astype(np.uint8)
    out.alpha_composite(Image.fromarray(met,"RGBA"),(lx,ly))
    # name
    f=ImageFont.truetype(F_BOLD,int(R*0.24)); f.set_variation_by_axes([800])
    tw=d.textlength(name,font=f); d=ImageDraw.Draw(out)
    tx=c-tw/2; ty=c+R*0.38
    d.text((tx+3,ty+4),name,font=f,fill=(10,12,18,255)); d.text((tx,ty),name,font=f,fill=(240,244,252,255))
    if crack:
        cr=Image.new("RGBA",(S,S),(0,0,0,0)); cd=ImageDraw.Draw(cr); rng=np.random.default_rng(11)
        for a0 in (-2.2,-1.2,0.4,1.9):
            px,py=c+0.98*R*math.cos(a0),c+0.98*R*math.sin(a0); ang=a0+math.pi
            for s in range(7):
                ang+=rng.uniform(-0.6,0.6); L=R*rng.uniform(0.06,0.11)
                nx,ny=px+L*math.cos(ang),py+L*math.sin(ang)
                cd.line([px,py,nx,ny],fill=tuple(neon)+(255,),width=3)
                if rng.random()<0.35:
                    b=ang+rng.choice([-1,1])*0.9; cd.line([nx,ny,nx+L*0.6*math.cos(b),ny+L*0.6*math.sin(b)],fill=tuple(neon)+(255,),width=2)
                px,py=nx,ny
        cr=ImageChops.multiply(cr, Image.merge("RGBA",[Image.new("L",(S,S),255)]*3+[Image.fromarray((inside*255).astype(np.uint8))]))
        cg=cr.filter(ImageFilter.GaussianBlur(5)); out=Image.alpha_composite(out,cg); out=Image.alpha_composite(out,cg); out=Image.alpha_composite(out,cr)
    # outer glow
    halo=Image.new("RGBA",(S,S),(0,0,0,0)); hd=ImageDraw.Draw(halo)
    hd.ellipse([c-R*1.02,c-R*1.02,c+R*1.02,c+R*1.02],outline=tuple(neon)+(255,),width=int(R*0.09))
    halo=halo.filter(ImageFilter.GaussianBlur(R*0.12)); halo=Image.alpha_composite(halo,halo)
    res=Image.alpha_composite(halo,out)
    return res

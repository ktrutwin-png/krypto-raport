"""Pekniecie / rozbicie monety (spadki): poszarpana linia, dwie czesci rozsuniete, odpryski."""
import numpy as np, math
from PIL import Image, ImageDraw, ImageFilter
def rozbij(m, sila=1.0, seed=5):
    S=m.size[0]; r=np.random.default_rng(seed)
    pts=[(S*0.18,-5)]; y=-5; x=S*0.18
    while y<S+5: y+=S*r.uniform(0.05,0.1); x+=S*r.uniform(0.02,0.13)*(1 if r.random()<0.75 else -0.6); pts.append((x,y))
    poly=pts+[(S+10,S+10),(S+10,-10)]
    mk=Image.new('L',(S,S),0); ImageDraw.Draw(mk).polygon(poly,fill=255)
    a=m.split()[3]
    L=m.copy(); L.putalpha(Image.fromarray(np.minimum(np.asarray(a),255-np.asarray(mk)).astype(np.uint8)))
    R=m.copy(); R.putalpha(Image.fromarray(np.minimum(np.asarray(a),np.asarray(mk)).astype(np.uint8)))
    R=R.rotate(-6*sila,resample=Image.BICUBIC,center=(S*0.6,S*0.5))
    out=Image.new('RGBA',(int(S*1.15),int(S*1.1)),(0,0,0,0)); out.alpha_composite(L,(0,0)); out.alpha_composite(R,(int(S*0.07*sila),int(S*0.04*sila)))
    d=ImageDraw.Draw(out)   # rysy od peknicia
    for _ in range(int(7*sila)):
        i=r.integers(1,len(pts)-1); x0,y0=pts[i]; ang=r.uniform(-math.pi,math.pi); L2=S*r.uniform(0.05,0.18)
        q=[(x0,y0)]
        for k in range(4): x0+=math.cos(ang+r.uniform(-.5,.5))*L2/4; y0+=math.sin(ang+r.uniform(-.5,.5))*L2/4; q.append((x0,y0))
        d.line(q,fill=(15,15,20,230),width=max(2,S//150)); d.line([(p[0]+1.5,p[1]+1.5) for p in q],fill=(230,235,245,120),width=1)
    for _ in range(int(10*sila)):   # odpryski obok
        cx=r.uniform(S*0.2,S*1.1); cy=r.uniform(S*0.85,S*1.08); s=r.uniform(S*0.01,S*0.035)
        d.polygon([(cx+s*math.cos(t),cy+s*0.6*math.sin(t)) for t in np.linspace(0,6.28,5)+r.uniform(0,1)],fill=(int(r.uniform(90,170)),)*3+(230,))
    return out

"""Scena krachu narysowana w 100% kodem (bez generatorow AI): niebo, burza, piorun, miasto z neonami, palmy, mokra ulica, postac na kolanach, telefon z wykresem."""
import math, numpy as np, sys
sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFilter, ImageChops
from monety2 import _glow
S=2; W,H=1080*S,1350*S; HOR=int(0.64*H)
rng=np.random.default_rng(7)
def grad(c1,c2,h):
    a=np.linspace(0,1,h)[:,None]; return (np.array(c1)*(1-a)+np.array(c2)*a)
def L(): return Image.new('RGBA',(W,H),(0,0,0,0))
img=Image.new('RGBA',(W,H))
# niebo
sky=np.concatenate([grad((8,8,26),(40,18,70),int(HOR*0.55)),grad((40,18,70),(150,40,110),HOR-int(HOR*0.55)),grad((25,12,40),(6,6,14),H-HOR)])
img=Image.fromarray(np.repeat(sky[:,None,:],W,1).astype(np.uint8)).convert('RGBA')
# chmury burzowe
cl=L(); d=ImageDraw.Draw(cl)
for _ in range(60):
    x=rng.uniform(-200,W+200); y=rng.uniform(-100,HOR*0.45); rx=rng.uniform(150,420); ry=rx*rng.uniform(.3,.5)
    v=int(rng.uniform(10,35)); d.ellipse([x-rx,y-ry,x+rx,y+ry],fill=(v,v,v+18,int(rng.uniform(120,200))))
img.alpha_composite(cl.filter(ImageFilter.GaussianBlur(40*S/2)))
# piorun
def piorun(x,y,dl,seg=16):
    pts=[(x,y)]
    for i in range(seg): x+=rng.uniform(-35,35)*S; y+=dl/seg; pts.append((x,y))
    return pts
pl=L(); d=ImageDraw.Draw(pl); P=piorun(300*S,80*S,HOR*0.62)
d.line(P,fill=(230,220,255,255),width=5*S)
for k in (5,9): q=P[k]; d.line(piorun(q[0],q[1],HOR*0.18,6),fill=(220,210,255,220),width=2*S)
img.alpha_composite(_glow(pl,18*S,3)); img.alpha_composite(pl)
# miasto: dwa plany
def miasto(n,hmin,hmax,col,edge,okna,seed):
    r=np.random.default_rng(seed); c=L(); d=ImageDraw.Draw(c); x=-40*S
    while x<W:
        w=r.uniform(60,150)*S; h=r.uniform(hmin,hmax)*S; top=HOR-h
        d.rectangle([x,top,x+w,HOR],fill=col)
        if r.random()<.5: d.polygon([(x+w*.3,top),(x+w*.5,top-h*.18),(x+w*.7,top)],fill=col)
        e=edge[int(r.integers(len(edge)))]; d.line([(x+w,top),(x+w,HOR)],fill=e+(200,),width=3*S); d.line([(x,top),(x+w,top)],fill=e+(160,),width=2*S)
        for yy in np.arange(top+20*S,HOR-10*S,22*S):
            for xx in np.arange(x+12*S,x+w-12*S,20*S):
                if r.random()<okna: d.rectangle([xx,yy,xx+7*S,yy+10*S],fill=(255,int(r.uniform(150,230)),int(r.uniform(120,220)),int(r.uniform(120,230))))
        x+=w+r.uniform(5,30)*S
    return c
far=miasto(0,180,420,(30,22,60,255),[(255,80,180),(80,220,255)],.25,1); img.alpha_composite(_glow(far,6*S,1)); img.alpha_composite(far)
near=miasto(0,120,300,(14,10,30,255),[(255,60,150),(60,230,255),(255,150,60)],.18,2); img.alpha_composite(_glow(near,10*S,1)); img.alpha_composite(near)
# palmy
def palma(x,base,h,lean):
    c=L(); d=ImageDraw.Draw(c); pts=[]
    for i in range(30):
        t=i/29; pts.append((x+lean*h*t*t,base-h*t))
    for i in range(len(pts)-1): d.line([pts[i],pts[i+1]],fill=(6,5,14,255),width=int((16-9*i/29)*S))
    tx,ty=pts[-1]
    for k in range(9):
        a=-math.pi/2+(k-4)*0.42+lean*0.3; L2=h*0.42
        f=[(tx,ty)]
        for j in range(1,13):
            t=j/12; f.append((tx+math.cos(a)*L2*t, ty+math.sin(a)*L2*t+ (L2*0.55)*t*t))
        for j in range(len(f)-1): d.line([f[j],f[j+1]],fill=(6,5,14,255),width=int((10-7*j/12)*S))
        for j in range(2,12,1):
            px,py=f[j]; ang=a+math.pi/2
            for sgn in (-1,1): d.line([(px,py),(px+sgn*math.cos(ang)*26*S*(1-j/13),py+abs(math.sin(ang))*30*S*(1-j/13)+14*S)],fill=(6,5,14,255),width=3*S)
    return c
for x,h,l in [(40*S,560*S,.18),(1010*S,640*S,-.2),(880*S,420*S,-.1)]: img.alpha_composite(palma(x,HOR+30*S,h,l))
# ulica i odbicia
ul=L(); ImageDraw.Draw(ul).rectangle([0,HOR,W,H],fill=(8,7,18,235)); img.alpha_composite(ul)
odb=img.crop((0,HOR-int(H*0.36),W,HOR)).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(5*S))
m=Image.fromarray((np.linspace(150,0,odb.size[1])[:,None].repeat(W,1)).astype(np.uint8)); odb.putalpha(ImageChops.multiply(odb.split()[3],m))
img.alpha_composite(odb,(0,HOR))
# smugi neonow na mokrym asfalcie
sm=L(); d=ImageDraw.Draw(sm)
for _ in range(40):
    x=rng.uniform(0,W); c=[(255,60,150),(60,220,255),(255,150,60)][int(rng.integers(3))]
    d.line([(x,HOR+rng.uniform(10,60)*S),(x+rng.uniform(-6,6)*S,H)],fill=c+(int(rng.uniform(25,70)),),width=int(rng.uniform(3,9)*S))
img.alpha_composite(sm.filter(ImageFilter.GaussianBlur(8*S)))
# telefon z wykresem
ph=L(); d=ImageDraw.Draw(ph); px,py=170*S,1035*S
d.rounded_rectangle([px,py,px+250*S,py+120*S],radius=18*S,fill=(10,10,16,255),outline=(60,60,80,255),width=3*S)
d.rounded_rectangle([px+10*S,py+10*S,px+240*S,py+110*S],radius=10*S,fill=(90,0,20,255))
ch=[(px+22*S,py+30*S)]; y=py+30*S
for i in range(1,12): y+=rng.uniform(-3,10)*S; ch.append((px+22*S+i*19*S,min(y,py+98*S)))
d.line(ch,fill=(255,60,80,255),width=4*S)
gl=L(); ImageDraw.Draw(gl).rectangle([px,py,px+250*S,py+120*S],fill=(255,30,60,160)); img.alpha_composite(gl.filter(ImageFilter.GaussianBlur(40*S)))
img.alpha_composite(ph)
rf=ph.crop((px-10*S,py,px+260*S,py+125*S)).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(6*S)); rf.putalpha(rf.split()[3].point(lambda v:int(v*.35)))
img.alpha_composite(rf,(px-10*S,py+125*S))
# postac na kolanach (sylwetka pod swiatlo z neonowym konturem)
def postac(col):
    c=L(); d=ImageDraw.Draw(c)
    def kon(a,b,w):
        a=(a[0]*S,a[1]*S); b=(b[0]*S,b[1]*S); d.line([a,b],fill=col,width=int(w*S))
        for p in (a,b): d.ellipse([p[0]-w*S/2,p[1]-w*S/2,p[0]+w*S/2,p[1]+w*S/2],fill=col)
    kon((520,1078),(700,1070),44)      # podudzia na ziemi
    kon((690,1066),(640,950),58)       # uda
    d.polygon([(600*S,960*S),(690*S,965*S),(700*S,800*S),(600*S,770*S)],fill=col)   # tulow pochylony
    kon((600,800),(720,790),70)        # barki
    d.ellipse([618*S,700*S,712*S,800*S],fill=col)   # glowa (opuszczona)
    kon((610,795),(560,700),30); kon((560,700),(640,690),26)   # lewe ramie do glowy
    kon((712,790),(760,700),30); kon((760,700),(690,688),26)   # prawe ramie do glowy
    d.ellipse([624*S,672*S,668*S,706*S],fill=col); d.ellipse([672*S,668*S,716*S,702*S],fill=col)  # dlonie
    return c
rim1=postac((255,60,170,255)); rim2=postac((60,220,255,255)); body=postac((8,6,16,255))
img.alpha_composite(_glow(rim1,10*S,2),(-7*S,-3*S)); img.alpha_composite(rim1,(-4*S,-2*S))
img.alpha_composite(_glow(rim2,8*S,1),(6*S,0)); img.alpha_composite(rim2,(3*S,0))
img.alpha_composite(body)
sh=L(); ImageDraw.Draw(sh).ellipse([480*S,1060*S,780*S,1100*S],fill=(0,0,0,170)); img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10*S)))
img.alpha_composite(body)
# deszcz
dz=L(); d=ImageDraw.Draw(dz)
for _ in range(1400):
    x=rng.uniform(-100,W); y=rng.uniform(-60,H); l=rng.uniform(30,80)*S
    d.line([(x,y),(x+l*.22,y+l)],fill=(200,220,255,int(rng.uniform(40,120))),width=int(rng.integers(1,3))*S)
img.alpha_composite(dz.filter(ImageFilter.GaussianBlur(0.7*S)))
for _ in range(120):   # rozpryski
    x=rng.uniform(0,W); y=rng.uniform(HOR+20*S,H); r=rng.uniform(4,12)*S
    ImageDraw.Draw(img).ellipse([x-r,y-r*.3,x+r,y+r*.3],outline=(190,210,255,90),width=S)
out=img.resize((1080,1350),Image.LANCZOS).convert('RGB')
out.save('/home/claude/krypto-raport/marka/propozycje/sunset/scena_kod_krach.png')
print('ok')

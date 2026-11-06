import numpy as np, base64
from scipy.interpolate import PchipInterpolator as PI
rng=np.random.default_rng(3)
Y =[-1.45,-1.1,-0.75,-0.4,-0.1,0.15,0.35,0.55,0.72,0.86,0.98,1.12,1.3,1.5,1.7,1.95,2.2,2.4,2.55,2.63]
Wd=[1.62, 1.60, 1.55, 1.40, 1.05, 0.55,0.36,0.33,0.34,0.30,0.40,0.50,0.58,0.62,0.645,0.66,0.62,0.50,0.30,0.02]
ZF=[0.55, 0.60, 0.56, 0.48, 0.38, 0.32,0.29,0.28,0.30,0.52,0.66,0.74,0.78,0.80,0.83,0.84,0.76,0.60,0.34,0.02]
ZB=[0.50, 0.52, 0.50, 0.45, 0.38, 0.32,0.29,0.30,0.36,0.44,0.56,0.70,0.80,0.86,0.88,0.86,0.80,0.62,0.36,0.02]
EX=[3.0,3.0,2.9,2.7,2.4,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0]
fw,ff,fb,fe=[PI(Y,v) for v in (Wd,ZF,ZB,EX)]
def surf(th,y):
    w,zf,zb,n=fw(y),ff(y),fb(y),fe(y)
    c,s=np.cos(th),np.sin(th)
    x=w*np.sign(c)*np.abs(c)**(2/n); zs=np.sign(s)*np.abs(s)**(2/n)
    z=np.where(s>0,zf,zb)*zs
    front=np.clip(s,0,1)**3
    ax=np.abs(x)
    nose=0.20*np.exp(-(x/0.085)**2)*np.clip((1.56-y)/0.36,0,1)**1.3*np.exp(-np.clip(1.17-y,0,None)**2/0.0012)*(y<1.58)
    sock=-0.075*np.exp(-((ax-0.26)/0.12)**2-((y-1.49)/0.085)**2)
    brow=0.035*np.exp(-((y-1.6)/0.06)**2)*np.exp(-(x/0.42)**2)
    cheek=0.045*np.exp(-((ax-0.36)/0.13)**2-((y-1.32)/0.1)**2)
    philtrum=-0.02*np.exp(-((y-1.02)/0.05)**2)*np.exp(-(x/0.2)**2)
    chin=0.03*np.exp(-((y-0.9)/0.05)**2)*np.exp(-(x/0.15)**2)
    z=z+front*(nose+sock+brow+cheek+philtrum+chin)
    return np.stack([x,y,z],-1)
TH=np.linspace(0,2*np.pi,900,endpoint=False);YY=np.linspace(-1.45,2.62,1400)
th,yy=np.meshgrid(TH,YY)
S=surf(th,yy)
du=np.gradient(S,axis=1);dv=np.gradient(S,axis=0)
nrm=np.cross(dv,du);area=np.linalg.norm(nrm,axis=-1)
nrm/=np.maximum(area[...,None],1e-9)
# make normals point outward
out=S.copy();out[...,1]=0
flip=np.sum(nrm*np.where(yy[...,None]>0.6,S-np.array([0,1.6,0]),out),-1)<0
nrm[flip]*=-1
P=S.reshape(-1,3);Nn=nrm.reshape(-1,3);A=area.reshape(-1)
wgt=A*np.where(P[:,1]>0.8,1.6,np.where(P[:,1]>-0.3,1.0,0.6))
wgt*=np.where((P[:,1]>0.8)&(P[:,2]>0.3),1.5,1.0)
idx=rng.choice(len(P),46000,p=wgt/wgt.sum())
p=P[idx]+rng.normal(0,0.003,(len(idx),3));n=Nn[idx]
# hair bun + hair strands at the back
k=6000;u=rng.normal(size=(k,3));u/=np.linalg.norm(u,axis=1,keepdims=True)
k=2500;u=u[:k];bun=np.array([0,1.72,-0.92])+u*np.array([0.26,0.24,0.2])
pass

seg=[]
def strip(pts):
    for a,b in zip(pts[:-1],pts[1:]): seg.extend([a,b])
T2=np.linspace(0,2*np.pi,240)
for y in np.arange(0.95,2.56,0.085): strip(surf(T2,np.full_like(T2,y)))
for y in np.arange(-1.3,0.95,0.22): strip(surf(T2,np.full_like(T2,y)))
Y2=np.linspace(0.85,2.6,160)
for t in np.arange(0,2*np.pi,np.pi/14): strip(surf(np.full_like(Y2,t),Y2))
L=np.array(seg,dtype=np.float32)*1.004
open('lines.js','w').write('window.HEXA_L="%s";'%base64.b64encode(L.tobytes()).decode())
print('lines',len(L))
print(len(p),p.min(0),p.max(0))
open('data.js','w').write('window.HEXA_P="%s";window.HEXA_N="%s";'%(base64.b64encode(p.astype(np.float32).tobytes()).decode(),base64.b64encode(np.clip(n*127,-127,127).astype(np.int8).tobytes()).decode()))
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
f,ax=plt.subplots(1,3,figsize=(12,5),facecolor='k')
for a,(i,j,t) in zip(ax,[(0,1,'front'),(2,1,'side'),(0,2,'top')]):
  a.scatter(p[:,i],p[:,j],s=.05,c='c');a.set_aspect('equal');a.set_facecolor('k')
plt.savefig('dbg.png',dpi=70)

# ---------- hair strands ----------
def inside(q):
    w,zf,zb=fw(q[1]),ff(q[1]),fb(q[1]);zr=zf if q[2]>0 else zb
    if q[1]>2.6 or q[1]<-1.45: return 9.0
    return (q[0]/max(w,1e-3))**2+(q[2]/max(zr,1e-3))**2
cand=[];T3=rng.uniform(0,2*np.pi,20000);Y3=rng.uniform(1.35,2.62,20000)
Sp=surf(T3,Y3)
for q in Sp:
    x,y,z=q
    if y>2.3 or (y>1.72 and z<0.42) or (y>1.38 and z<-0.05): cand.append(q)
cand=np.array(cand);cand=cand[rng.choice(len(cand),340,replace=False)]
H=[];HT=[];HS=[]
c0=np.array([0,1.55,0.0])
for s in cand:
    n=s-c0;n/=np.linalg.norm(n)
    d=n*0.5+np.array([0,0.1,-0.9]);d/=np.linalg.norm(d)
    p=s+n*0.02;pts=[p.copy()];L=rng.uniform(1.6,2.4)
    steps=60;st=L/steps;side=np.sign(s[0]) if abs(s[0])>0.05 else rng.choice([-1,1])
    for i in range(steps):
        d=d+np.array([side*0.004,-0.11,-0.015]);d/=np.linalg.norm(d)
        p=p+d*st
        for _ in range(6):
            v=inside(p)
            if v<1.07**2:
                w,zf,zb=fw(p[1]),ff(p[1]),fb(p[1])
                sc=min(1.07/np.sqrt(max(v,0.05)),1.6);p[0]*=sc;p[2]*=sc
            else: break
        pts.append(p.copy())
    pts=np.array(pts);seed=rng.random()
    for i in range(len(pts)-1):
        H.extend([pts[i],pts[i+1]]);HT.extend([i/steps,(i+1)/steps]);HS.extend([seed,seed])
H=np.array(H,np.float32);HT=np.array(HT,np.float32);HS=np.array(HS,np.float32)
open('hair.js','w').write('window.HEXA_H="%s";window.HEXA_HT="%s";window.HEXA_HS="%s";'%tuple(base64.b64encode(a.tobytes()).decode() for a in (H,HT,HS)))
print('hair verts',len(H))
f,ax=plt.subplots(1,2,figsize=(8,5),facecolor='k')
for a,(i,j) in zip(ax,[(0,1),(2,1)]):
  a.scatter(p0[:,i] if False else P[::50,i],P[::50,j],s=.02,c='c');
  for k in range(0,len(H),2): a.plot([H[k,i],H[k+1,i]],[H[k,j],H[k+1,j]],c='gold',lw=.2)
  a.set_aspect('equal');a.set_facecolor('k')
plt.savefig('hair.png',dpi=70)

# ---------- occluder mesh (depth only) ----------
TM=np.linspace(0,2*np.pi,97)[:-1];YM=np.linspace(-1.45,2.62,150)
tm,ym=np.meshgrid(TM,YM);V=surf(tm,ym)
c=np.array([0,0,0.0]);V2=V.copy();V2[...,0]*=0.975;V2[...,2]*=0.975
V2=V2.reshape(-1,3).astype(np.float32)
nT=len(TM);idx=[]
for j in range(len(YM)-1):
    for i in range(nT):
        a=j*nT+i;b=j*nT+(i+1)%nT;c_=(j+1)*nT+i;d=(j+1)*nT+(i+1)%nT
        idx+= [a,c_,b,b,c_,d]
idx=np.array(idx,np.uint16)
open('occ.js','w').write('window.HEXA_OV="%s";window.HEXA_OI="%s";'%(base64.b64encode(V2.tobytes()).decode(),base64.b64encode(idx.tobytes()).decode()))
print('occ',len(V2),len(idx))

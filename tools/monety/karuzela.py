"""Karuzela 6 kart (szef 24.11): kolejnosc wg ruchu 24h, inna postac i miejsce, moneta w scenie, pogoda wg nastroju."""
import sys, os, json
sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from monety_real import wytnij, wytlocz, SPEC, B, REPO
from wstaw_monete import polozona
from rozbij import rozbij
src=open('karta_sunset.py').read().split("P=f'{REPO}/propozycje/sunset'")[0]
exec(src)
D=f'{REPO}/propozycje/karuzela_2411'
def zloto_moneta():
    f=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf',700)
    t=Image.new('RGBA',(1400,1000),(0,0,0,0)); ImageDraw.Draw(t).text((700,500),'Au',font=f,fill=(255,255,255,255),anchor='mm')
    t=t.crop(t.getbbox()); c=wytnij(f'{B}/blank_zloto_2.jpg'); return wytlocz(c,t,0.42,'zloto')
mon={'XAU':zloto_moneta()}
for k in ['XDC','BTC','ETH','XRP','XLM']:
    p,lf,fr,kd=SPEC.get(k,SPEC['XRP']); mon[k]=Image.open(f'{REPO}/monety_real/{k.lower()}.png')
def fx_mzawka(img): deszcz(img,n=350,seed=4)
KARTY=[ # kod, %, cena, haslo, scena, (cx,cy,D), fx, pekniecie, x0 kadru
 ('XAU','−2.4%','$3,563','CLOUDY DAY FOR GOLD','s_xau.jpg',(380,858,170),'mzawka',0,150),
 ('XDC','−3.0%','$0.0258','NERVES ON','s_xdc.jpg',(620,850,180),'mzawka',0,150),
 ('BTC','−4.2%','$59,475','RAIN ON THE CURB','s_btc.jpg',(845,850,190),'deszcz',0,200),
 ('ETH','−5.1%','$1,670','POOL PARTY CANCELLED','s_eth.jpg',(800,850,175),'deszcz',0,200),
 ('XRP','−6.1%','$0.912','STORM ON THE CHART','s_xrp.jpg',(790,845,230),'deszcz',0.6,150),
 ('XLM','−7.2%','$0.1233','TRASHED','s_xlm.jpg',(600,855,200),'deszcz',1.0,150)]
_t=tekst
def tekst(img,t,font,xy,*r,**k): _t(img,t,font,(W//2,xy[1]),*r,**k)
def moneta(*a,**k): pass
globals()['tekst']=tekst; globals()['moneta']=moneta
import karta_sunset
for i,(k,pc,cena,has,scn,(cx,cy,Dm),fx,pk,x0) in enumerate(KARTY,1):
    s=Image.open(f'{D}/{scn}'); m=mon[k]
    if pk: m=rozbij(m,pk)
    sc=polozona(s,m,cx,cy,Dm,ambient=(0.95,1.0,1.1)); sc.convert('RGB').save(f'{D}/_tmp.jpg',quality=95)
    kol=(255,255,255); gl=(255,30,70) if float(pc[1:-1])>=4 else (255,120,40)
    wyj=f'{D}/{i}_{k.lower()}.jpg'
    if fx=='mzawka': globals()['deszcz_orig']=deszcz
    karta(f'{D}/_tmp.jpg',x0,x0+824,f'{k} {pc}',kol,gl,f'{cena}  ·  24H  ·  {has}',None,k,(50,210,255),'deszcz',wyj)
    im=Image.open(wyj); d=ImageDraw.Draw(im); d.text((W-40,40),f'{i}/6',font=fb(26,700),fill=(255,255,255),anchor='rt'); im.save(wyj,quality=93)
os.remove(f'{D}/_tmp.jpg')
th=[Image.open(f'{D}/{i}_{k[0].lower()}.jpg').resize((360,450)) for i,k in enumerate(KARTY,1)]
pk=Image.new('RGB',(3*360+40,2*450+30),(10,10,14))
for i,t in enumerate(th): pk.paste(t,(10+(i%3)*370,10+(i//3)*460))
pk.save(f'{D}/podglad.jpg',quality=90); print('ok')

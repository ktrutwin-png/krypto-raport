"""Karuzela 6 kart (szef 24.11): kolejnosc wg ruchu 24h, inna postac i miejsce, moneta w scenie, pogoda wg nastroju."""
import sys, os, json
sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src=open('karta_sunset.py').read().split("P=f'{REPO}/propozycje/sunset'")[0]
exec(src)
def fx_mzawka(img): deszcz(img,n=350,seed=4)
CFG=json.load(open(sys.argv[1])); D='/home/claude/krypto-raport/'+CFG['dir']
KARTY=[(c['k'],c['pc'],c['cena'],c['haslo'],c['scena'],(0,0,0),'deszcz' if c['sila']>0.6 else ('mzawka' if c['sila']>0 else 'slonce'),0,c['x0']) for c in CFG['karty']]
_t=tekst
def tekst(img,t,font,xy,*r,**k): _t(img,t,font,(W//2,xy[1]),*r,**k)
def moneta(*a,**k): pass
globals()['tekst']=tekst; globals()['moneta']=moneta
import karta_sunset
for i,(k,pc,cena,has,scn,(cx,cy,Dm),fx,pk,x0) in enumerate(KARTY,1):
    s=Image.open(f'{D}/{scn}')
    s.convert('RGB').save(f'{D}/_tmp.jpg',quality=95)   # szef 24.11: bez monet w scenie
    kol=(255,255,255); gl=(255,30,70) if float(pc[1:-1])>=4 else (255,120,40)
    wyj=f'{D}/{i}_{k.lower()}.jpg'
    if fx=='mzawka': globals()['deszcz_orig']=deszcz
    karta(f'{D}/_tmp.jpg',x0,x0+824,f'{k} {pc}',kol,gl,f'{cena}  ·  24H  ·  {has}',None,k,(50,210,255),('deszcz' if fx!='slonce' else 'zloto'),wyj)
    im=Image.open(wyj); d=ImageDraw.Draw(im); d.text((W-40,40),f'{i}/6',font=fb(26,700),fill=(255,255,255),anchor='rt'); im.save(wyj,quality=93)
os.remove(f'{D}/_tmp.jpg')
th=[Image.open(f'{D}/{i}_{k[0].lower()}.jpg').resize((360,450)) for i,k in enumerate(KARTY,1)]
pk=Image.new('RGB',(3*360+40,2*450+30),(10,10,14))
for i,t in enumerate(th): pk.paste(t,(10+(i%3)*370,10+(i//3)*460))
pk.save(f'{D}/podglad.jpg',quality=90); print('ok')

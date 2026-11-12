import sys
from PIL import Image, ImageDraw, ImageFont, ImageChops
W,H=1080,1350; F="/usr/share/fonts/opentype/inter/"
BI=lambda s: ImageFont.truetype(F+"InterDisplay-BlackItalic.otf",s)
SB=lambda s: ImageFont.truetype(F+"Inter-SemiBold.otf",s)
GOLD=(232,196,104); WHITE=(246,242,232); DARK=(8,8,12)
def tlo(p):
    im=Image.open(p).convert("RGB"); sw,sh=im.size; s=max(W/sw,H/sh)
    im=im.resize((int(sw*s)+1,int(sh*s)+1),Image.LANCZOS); x=(im.width-W)//2; y=(im.height-H)//2
    im=im.crop((x,y,x+W,y+H)); m=Image.new("L",(W,H)); d=ImageDraw.Draw(m)
    for yy in range(H):
        t=yy/H; a=int(200*max(0,1-t/0.42))+int(170*max(0,(t-0.72)/0.28)); d.line([(0,yy),(W,yy)],fill=min(255,a))
    return Image.composite(Image.new("RGB",(W,H),(4,5,10)),im,m)
def fit(dr,t,fn,maxw,s):
    while dr.textlength(t,font=fn(s))>maxw and s>30: s-=2
    return s
def pasek(img,y,t,s):
    dr=ImageDraw.Draw(img); fs=fit(dr,t,BI,W-160,s); w=dr.textlength(t,font=BI(fs))
    dr.rounded_rectangle([W/2-w/2-30,y-fs*0.62,W/2+w/2+30,y+fs*0.62],12,fill=GOLD)
    dr.text((W/2,y),t,font=BI(fs),fill=DARK,anchor="mm")
def bialy(img,y,t,s):
    dr=ImageDraw.Draw(img); fs=fit(dr,t,BI,W-140,s)
    dr.text((W/2,y),t,font=BI(fs),fill=WHITE,anchor="mm",stroke_width=2,stroke_fill=(0,0,0))
def znak(img,ik,nr):
    ic=Image.open(ik).convert("RGB").resize((70,70),Image.LANCZOS)
    r=img.crop((48,1240,118,1310)); img.paste(ImageChops.lighter(r,ic),(48,1240))
    dr=ImageDraw.Draw(img); dr.text((132,1275),"E R L . G R E Y 8 3",font=SB(24),fill=(200,196,186),anchor="lm")
    dr.text((W-60,1275),nr,font=SB(26),fill=(200,196,186),anchor="rm")

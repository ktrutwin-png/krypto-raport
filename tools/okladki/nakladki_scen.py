import asyncio
from playwright.async_api import async_playwright
CSS="""@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@800;900&display=swap');
*{margin:0}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;font-family:Inter}
.g{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,0) 26%,rgba(0,0,0,0) 68%,rgba(0,0,0,.85) 100%)}
.t{position:absolute;top:110px;left:0;right:0;text-align:center;font-family:Anton;font-style:italic;line-height:.95;transform:skewX(-6deg)}
.a{font-size:104px;color:#fff;-webkit-text-stroke:4px #000;text-shadow:0 8px 0 #000}
.b{font-size:150px;color:#ff2b2b;-webkit-text-stroke:6px #000;text-shadow:0 10px 0 #000}
.y{color:#ffd400}
.bar{position:absolute;bottom:250px;left:40px;right:40px;text-align:center;font-weight:900;font-size:60px;line-height:1.15;color:#fff;text-shadow:0 4px 10px #000}
.bar span{color:#ffd400}
.w{position:absolute;bottom:120px;left:0;right:0;text-align:center;font-weight:800;font-size:34px;color:#fff}.w b{color:#ffd400}
.d{position:absolute;bottom:60px;left:0;right:0;text-align:center;font-size:24px;color:#ccc;font-weight:800}"""
S={
'o1':'<div class="t"><div class="a">ANOTHER</div><div class="b">RED TUESDAY?</div></div><div class="bar">CRYPTO <span>−4.7%</span> IN 24 HOURS</div>',
'o2':'<div class="t"><div class="a">BITCOIN</div><div class="b y">$73,100</div></div><div class="bar">DOWN <span>−3.1%</span> TODAY</div>',
'o3':'<div class="t"><div class="a">XRP</div><div class="b">−6.8%</div></div><div class="bar">ALTCOINS HIT <span>HARDER</span></div>',
'o4':'<div class="t"><div class="a">EVEN GOLD</div><div class="b">−2.1%</div></div><div class="bar">NO SAFE HAVEN <span>TODAY?</span></div>',
'o5':'<div class="t"><div class="a">PANIC</div><div class="b y">OR CHANCE?</div></div><div class="bar">TELL ME IN THE <span>COMMENTS</span></div>',
}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,v in S.items():
            await pg.set_content(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="g"></div>{v}<div class="w"><b>@</b>erl.grey83</div><div class="d">For information only, not investment advice.</div></body></html>')
            await pg.wait_for_timeout(900); await pg.screenshot(path=f'{k}.png',omit_background=True)
        await b.close()
asyncio.run(main())

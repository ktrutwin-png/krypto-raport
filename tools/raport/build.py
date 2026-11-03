import asyncio, os, json, sys
from playwright.async_api import async_playwright
D = json.load(open(sys.argv[1])); OUT = os.path.dirname(os.path.abspath(sys.argv[1]))
A, B = "#5ee6ff", "#ffc861"   # cyan / amber
UP, DN = "#3dffa8", "#ff5470"
DATE, DATEDOT, ASOF, KICK = D["date"], D["datedot"], D["asof"], D["kick"]
coins = [tuple(c) for c in D["coins"]]  # [sym, price_str, ch24, ch7d]
G = D["g"]  # dict of display strings

def pc(v, arrow=True):
    c = UP if v >= 0 else DN; a = ("▲ " if v >= 0 else "▼ ") if arrow else ""
    return f'<span style="color:{c};text-shadow:0 0 14px {c}66">{a}{"+" if v >= 0 else "−"}{abs(v):.2f}%</span>'

CSS = f"""*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1080px;overflow:hidden;font-family:Inter,sans-serif;color:#e8f1ff;
background:radial-gradient(circle at 80% 0%,#12304a 0,#0a1320 45%,#060a12 100%);position:relative}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(#5ee6ff0c 1px,transparent 1px),linear-gradient(90deg,#5ee6ff0c 1px,transparent 1px);background-size:54px 54px}}
.sky{{position:absolute;right:40px;top:60px;width:460px;height:280px;opacity:.25;z-index:0}}
.wrap{{z-index:1}}
.wrap{{position:absolute;inset:42px}}
.kick{{font-size:16px;letter-spacing:5px;color:{A};font-weight:500}}
.tr{{position:absolute;right:0;top:0;text-align:right;font-size:14px;letter-spacing:4px;line-height:25px;color:#cfe3f5}}
.nick{{font-size:28px;font-weight:800;letter-spacing:0;color:#fff;text-shadow:0 0 18px {A}aa;margin-bottom:6px}}
.t1{{font-weight:900;font-size:128px;line-height:.92;letter-spacing:-2px;color:#fff;text-shadow:0 0 30px {A}55}}
.t2{{background:linear-gradient(90deg,{A},{B});-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 0 22px {A}55)}}
.card{{background:linear-gradient(135deg,#10233799,#0b162499);border:1px solid {A}44;border-radius:4px;
clip-path:polygon(0 0,calc(100% - 22px) 0,100% 22px,100% 100%,22px 100%,0 calc(100% - 22px));padding:22px 26px}}
.lbl{{font-size:13px;letter-spacing:3px;color:#9fb6cc;margin-top:6px}}
.foot{{position:absolute;left:0;right:0;bottom:0;border-top:1px solid #ffffff22;padding-top:14px;display:flex;justify-content:space-between;font-size:14px;color:#8aa2b8}}
.sec{{font-size:22px;letter-spacing:5px;font-weight:800;color:{A};text-shadow:0 0 14px {A}88}}
"""
SKY = f'<svg class="sky" viewBox="0 0 460 280"><polyline fill="none" stroke="{A}" stroke-width="2" points="0,240 40,240 40,150 90,150 90,200 140,200 140,90 200,90 200,170 250,170 250,40 300,40 300,140 350,140 350,110 400,110 400,190 460,190"/></svg>'

def head(big=True):
    tr = f'<div class="tr"><div class="nick">@erl.grey83</div>SYSTEM ONLINE<br>NEON MARKET FEED<br>{DATEDOT}{"<br><br><span style=color:"+A+">SWIPE LEFT ▸ MORE</span>" if big else ""}</div>'
    if big:
        t = f'<div class="t1" style="margin-top:12px;font-size:104px">CRYPTO</div><div class="t1 t2" style="font-size:104px">REPORT</div><div style="font-size:34px;letter-spacing:10px;font-weight:300;margin-top:12px">{DATE}</div><div class="lbl" style="color:{A}">{ASOF}</div>'
    else:
        t = f'<div class="t1" style="font-size:84px;margin-top:10px">CRYPTO <span class="t2">REPORT</span></div>'
    return f'<div class="grid"></div>{SKY}<div class="wrap"><div class="kick">{KICK}</div>{tr}{t}'

def foot(src): return f'<div class="foot"><span>Sources: {src}</span><span>For information only, not investment advice.</span></div></div>'

def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'

# slide 1
big = lambda n, sym, p, ch: f'<div class="card" style="flex:1"><div style="font-size:24px;font-weight:800">{n} <span style="color:#9fb6cc;font-weight:400">({sym})</span></div><div style="font-size:50px;font-weight:800;margin:6px 0 2px;text-shadow:0 0 20px #ffffff44">{p} USD</div><div style="font-size:30px;font-weight:800">{pc(ch)} <span style="font-size:16px;color:#9fb6cc">24h</span></div></div>'
alts = "".join(f'<div style="display:flex;justify-content:space-between;width:280px;font-size:20px;padding:5px 0"><b>{s}</b><span>{p} USD</span>{pc(c, False)}</div>' for s, p, c, _ in coins[2:7])
tile = lambda v, l: f'<div class="card" style="flex:1;text-align:center;padding:18px 10px"><div style="font-size:40px;font-weight:800;text-shadow:0 0 18px {A}66">{v}</div><div class="lbl" style="font-size:12px">{l}</div></div>'
s1 = head() + f'''<div style="position:absolute;top:318px;left:0;right:0">
<div style="display:flex;gap:22px">{big("BITCOIN","BTC",coins[0][1],coins[0][2])}{big("ETHEREUM","ETH",coins[1][1],coins[1][2])}</div>
<div class="card" style="margin-top:18px;display:flex;flex-wrap:wrap;column-gap:26px;padding:14px 26px">{alts}<div style="width:280px;font-size:15px;color:#9fb6cc;padding-top:10px">24h change</div></div>
<div style="display:flex;gap:18px;margin-top:18px">{tile(G["mcap"],"TOTAL MARKET CAP")}{tile(G["dom"],"BTC DOMINANCE")}{tile(G["fg"],"FEAR &amp; GREED: "+G["fg_label"])}{tile(G["etf"],"BTC ETF ASSETS (USD)")}</div>
<div style="display:flex;gap:22px;margin-top:18px">
<div class="card" style="flex:1;font-size:18px;line-height:1.55"><div class="sec" style="font-size:19px;margin-bottom:8px">&gt; DERIVATIVES</div><b style="color:{A}">Open interest:</b> {G["oi"]} ({G["oi_ch"]} in 24h)<br><b style="color:{A}">BTC liquidations (24h):</b> about {G["liq"]}<br>Source: CoinMarketCap.</div>
<div class="card" style="flex:1;font-size:18px;line-height:1.55"><div class="sec" style="font-size:19px;margin-bottom:8px;color:{B};text-shadow:0 0 14px {B}88">&gt; SENTIMENT</div>{G["sentiment"]}</div>
</div></div>''' + foot("CoinMarketCap")

# slide 2
news = [tuple(n) for n in D["news"]]  # [tag, headline, body]
cards = "".join(f'<div class="card" style="margin-top:22px;padding:24px 34px"><span style="border:1px solid {B};color:{B};font-size:14px;letter-spacing:3px;padding:3px 10px">{t}</span><div style="font-size:33px;font-weight:800;margin:12px 0 8px">{h}</div><div style="font-size:22px;line-height:1.42;color:#c9d8e8">{b}</div></div>' for t, h, b in news)
s2 = head(False) + f'<div class="sec" style="margin-top:24px">&gt; TOP STORIES FROM AROUND THE WORLD</div>{cards}' + foot(D["news_sources"])

# slide 3
rows = "".join(f'<div style="display:flex;align-items:center;font-size:30px;padding:13px 0;border-bottom:1px solid #ffffff14"><b style="width:120px">{s}</b><span style="flex:1">{p} USD</span><span style="width:200px;text-align:right;font-weight:800">{pc(a)}</span><span style="width:220px;text-align:right;font-weight:800">{pc(w)}</span></div>' for s, p, a, w in coins)
s3 = head(False) + f'''<div class="sec" style="margin-top:24px">&gt; WEEKLY SCOREBOARD</div>
<div class="card" style="margin-top:16px;padding:18px 32px"><div style="display:flex;font-size:14px;letter-spacing:3px;color:#9fb6cc"><span style="width:120px">COIN</span><span style="flex:1">PRICE</span><span style="width:200px;text-align:right">24H</span><span style="width:220px;text-align:right">7 DAYS</span></div>{rows}</div>
<div style="display:flex;gap:18px;margin-top:20px">{tile(G["alt"],"ALTCOIN SEASON INDEX")}{tile(G["oi"],"OPEN INTEREST ("+G["oi_ch"]+" 24H)")}{tile(G["liq"],"BTC LIQUIDATIONS (24H)")}</div>
<div class="card" style="margin-top:20px;font-size:22px;line-height:1.45;border-color:{B}66"><b style="color:{B}">TAKEAWAY:</b> {G["takeaway"]}</div>''' + foot("CoinMarketCap")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1080})
        for i, s in enumerate([s1, s2, s3], 1):
            await pg.set_content(page(s)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{OUT}/slide{i}.png")
        await b.close()
asyncio.run(main())

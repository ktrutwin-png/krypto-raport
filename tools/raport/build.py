"""Crypto Report @erl.grey83 - styl CYBERPUNK (od 5.11.2026), 3 slajdy 1080x1350 (4:5).
Uzycie: python3 build.py data.json  -> slide1.png slide2.png slide3.png obok data.json
Pola data.json jak w example_data.json. Opcjonalnie:
  "hook"  - duzy nagłówek slajdu 1 (max ~7 slow, liczba albo pytanie)
  "bg"    - sciezka lub URL do tla AI (bez tekstu); bez niego rysowane jest neonowe miasto
  "btc7d" - lista cen BTC z 7 dni (wykres na slajdzie 1)
Stary kwadratowy szablon: build_old_square.py"""
import asyncio, os, json, sys, math, random
from playwright.async_api import async_playwright
D = json.load(open(sys.argv[1])); OUT = os.path.dirname(os.path.abspath(sys.argv[1]))
CY, MG, YE, UP, DN = "#00f0ff", "#ff2bd6", "#ffe600", "#3dffa8", "#ff4d6d"
W, H = 1080, 1350
DATE, ASOF, KICK = D["date"], D["asof"], D.get("kick", "")
HOOK = D.get("hook") or KICK or "CRYPTO REPORT"
coins = [tuple(c) for c in D["coins"]]; G = D["g"]; news = [tuple(n) for n in D["news"]]

def pc(v, arrow=True):
    c = UP if v >= 0 else DN; a = ("▲ " if v >= 0 else "▼ ") if arrow else ""
    return f'<span style="color:{c};text-shadow:0 0 12px {c}aa">{a}{"+" if v >= 0 else "−"}{abs(v):.2f}%</span>'

# ---------- tlo: neonowe miasto (deterministyczne wg daty, kazdy dzien troche inne)
def city(h0, col, op, seed):
    r = random.Random(seed); s = ""; x = -20
    while x < W + 20:
        w = r.randint(50, 130); h = r.randint(int(h0 * .14), int(h0 * .42)); y = h0 - h
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#07031a" stroke="{col}" stroke-opacity="{op}" stroke-width="2"/>'
        for wy in range(y + 14, h0 - 10, 22):
            for wx in range(x + 8, x + w - 8, 16):
                if r.random() < .28: s += f'<rect x="{wx}" y="{wy}" width="7" height="10" fill="{r.choice([CY, MG, YE, CY])}" opacity="{r.uniform(.35, .95):.2f}"/>'
        if r.random() < .3: s += f'<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y-60}" stroke="{MG}" stroke-width="3"/><circle cx="{x+w/2}" cy="{y-60}" r="5" fill="{MG}"/>'
        x += w + r.randint(4, 18)
    return s
def grid(y0, hh):
    s = ""
    for i in range(-14, 15): s += f'<line x1="{540+i*40}" y1="{y0}" x2="{540+i*260}" y2="{y0+hh}" stroke="{MG}" stroke-opacity=".5" stroke-width="2"/>'
    for k in range(1, 12):
        y = y0 + hh * (k / 11) ** 2; s += f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" stroke="{CY}" stroke-opacity="{.25+.5*k/11:.2f}" stroke-width="2"/>'
    return s
def globe(cx, cy, r, seed):
    rr = random.Random(seed); s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gl)" stroke="{CY}" stroke-width="3"/>'
    for a in range(-60, 90, 30):
        ry = r * math.cos(math.radians(a)); yy = cy - r * math.sin(math.radians(a))
        s += f'<ellipse cx="{cx}" cy="{yy:.0f}" rx="{ry:.0f}" ry="{ry*.18:.0f}" fill="none" stroke="{CY}" stroke-opacity=".5" stroke-width="1.5"/>'
    for k in range(0, 180, 30): s += f'<ellipse cx="{cx}" cy="{cy}" rx="{r*abs(math.cos(math.radians(k))):.0f}" ry="{r}" fill="none" stroke="{CY}" stroke-opacity=".45" stroke-width="1.5"/>'
    for _ in range(26):
        t = rr.uniform(0, 2 * math.pi); u = rr.uniform(-.9, .9)
        s += f'<circle cx="{cx+r*math.cos(t)*math.sqrt(1-u*u):.0f}" cy="{cy-r*u:.0f}" r="{rr.choice([3,4,5])}" fill="{rr.choice([CY,YE,MG])}"/>'
    return s
SEED = sum(map(ord, DATE))
def background(dim=0.0, horizon=1000):
    if D.get("bg"):
        if D["bg"].startswith("http"): src = D["bg"]
        else:
            import base64
            f = D["bg"] if os.path.isabs(D["bg"]) else os.path.join(OUT, D["bg"])
            if not os.path.exists(f): f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bg", os.path.basename(D["bg"]))
            src = "data:image/png;base64," + base64.b64encode(open(f, "rb").read()).decode()
        pos = D.get("bgpos", "15% center")
        return f'<div style="position:absolute;inset:0;background:url(\'{src}\') {pos}/cover no-repeat"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,#05010f99 0%,#05010f33 40%,#05010f22 65%,#05010fcc 100%)"></div><div style="position:absolute;inset:0;background:#05010f;opacity:{dim}"></div><div class="scan"></div>'
    return f'''<svg style="position:absolute;top:0;left:0" width="{W}" height="{H}"><defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0230"/><stop offset=".55" stop-color="#3a0660"/><stop offset=".72" stop-color="{MG}" stop-opacity=".55"/><stop offset=".8" stop-color="#05010f"/></linearGradient>
<radialGradient id="gl"><stop offset="0" stop-color="{CY}" stop-opacity=".35"/><stop offset="1" stop-color="{CY}" stop-opacity=".05"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>{globe(860, horizon-360, 150, SEED)}
<g>{city(horizon, MG, .35, SEED+3)}</g><g>{city(horizon+10, CY, .7, SEED+9)}</g>
<g>{grid(horizon, H-horizon)}</g><rect y="{horizon}" width="{W}" height="4" fill="{MG}"/></svg>
<div style="position:absolute;inset:0;background:#05010f;opacity:{dim}"></div><div class="scan"></div>'''

CSS = f"""*{{box-sizing:border-box;margin:0;padding:0}}body{{width:{W}px;height:{H}px;overflow:hidden;font-family:Inter,sans-serif;position:relative;background:#05010f;color:#fff}}
.orb{{font-family:Orbitron,Inter,sans-serif}}
.scan{{position:absolute;inset:0;background:repeating-linear-gradient(0deg,#ffffff07 0 2px,transparent 2px 5px)}}
.nc{{color:{CY};text-shadow:0 0 8px {CY},0 0 26px {CY},0 0 60px {CY}88}}
.nm{{color:{MG};text-shadow:0 0 8px {MG},0 0 26px {MG},0 0 60px {MG}88}}
.panel{{position:absolute;background:linear-gradient(135deg,#0b0330dd,#13023add);border:2px solid {CY};box-shadow:0 0 18px {CY}88,inset 0 0 30px {CY}22;
 clip-path:polygon(0 0,calc(100% - 30px) 0,100% 30px,100% 100%,30px 100%,0 calc(100% - 30px))}}
.pm{{border-color:{MG};box-shadow:0 0 18px {MG}aa,inset 0 0 30px {MG}22}}
.lbl{{font-size:22px;letter-spacing:5px;color:#9ef}}
.top{{position:absolute;top:48px;left:60px;right:60px;display:flex;justify-content:space-between;font-weight:800;letter-spacing:5px}}
.foot{{position:absolute;bottom:44px;left:60px;right:60px;display:flex;justify-content:space-between;font-weight:800;font-size:22px;letter-spacing:5px}}
.hook{{color:#eafcff;text-shadow:0 0 6px {CY}66,0 2px 0 #05010f}}
.glitch{{position:relative}}.glitch:before,.glitch:after{{content:attr(data-t);position:absolute;left:0;top:0}}
.glitch:before{{color:{MG};transform:translate(-5px,2px);opacity:.7;mix-blend-mode:screen}}.glitch:after{{color:{CY};transform:translate(5px,-2px);opacity:.7;mix-blend-mode:screen}}"""
FONT = '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;500;800;900&display=swap" rel="stylesheet">'
def top(left): return f'<div class="top"><span class="nm" style="font-size:24px">{left}</span><span class="nc" style="font-size:30px;letter-spacing:0">@erl.grey83</span></div>'
def foot(right=None):
    right = right or D.get("swipe", "SWIPE ▸")
    return f'<div class="foot"><span class="nc">FACTS, NOT HYPE</span><span class="nm">{right}</span></div><div style="position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:15px;color:#9ab">For information only, not investment advice.</div>'

def spark(pts, w=900, h=150):
    mn, mx = min(pts), max(pts); xs = [i * w / (len(pts) - 1) for i in range(len(pts))]
    ys = [h - (p - mn) / ((mx - mn) or 1) * (h - 16) - 8 for p in pts]; col = UP if pts[-1] >= pts[0] else DN
    d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in zip(xs, ys))
    return f'<svg width="{w}" height="{h}"><path d="{d}" fill="none" stroke="{col}" stroke-width="6" stroke-linejoin="round" style="filter:drop-shadow(0 0 8px {col})"/><circle cx="{xs[-1]:.0f}" cy="{ys[-1]:.0f}" r="10" fill="{col}"/></svg>'

# ---------- slajd 1: hook + BTC
hs = 118 if len(HOOK) <= 18 else 96 if len(HOOK) <= 30 else 80
btc = coins[0]; eth = coins[1]
sp = f'<div class="lbl" style="font-size:18px;text-shadow:0 0 6px #000">BTC · 7 DAYS</div><div style="margin-top:8px">{spark(D["btc7d"])}</div>' if D.get("btc7d") and not D.get("bg") else ""
s1 = background() + top("◉ LIVE · " + DATE) + f'''
<div class="panel" style="top:130px;left:60px;right:60px;padding:36px 44px">
 <div class="lbl">{KICK}</div>
 <div class="orb hook" style="font-weight:900;font-size:{hs}px;line-height:1.02;margin-top:14px">{HOOK}</div>
 <div class="lbl" style="margin-top:18px;color:#fbe">{ASOF}</div></div>
<div class="panel pm" style="top:1010px;left:60px;right:60px;padding:24px 44px;display:flex;justify-content:space-between;align-items:center">
 <div><div class="lbl" style="color:#fbe">BITCOIN</div><div class="orb" style="font-weight:900;font-size:64px">${btc[1]}</div></div>
 <div style="text-align:right"><div class="orb" style="font-weight:900;font-size:50px">{pc(btc[2])}</div><div class="lbl" style="margin-top:6px">ETH ${eth[1]} · {pc(eth[2], False)}</div></div></div>
<div style="position:absolute;top:800px;left:60px">{sp}</div>''' + foot()

# ---------- slajd 2: newsy
cards = "".join(f'''<div class="panel{' pm' if i % 2 else ''}" style="position:relative;margin-top:26px;padding:26px 40px">
 <span style="border:1px solid {YE};color:{YE};font-size:18px;letter-spacing:4px;padding:3px 10px;text-shadow:0 0 8px {YE}">{t}</span>
 <div style="font-size:34px;font-weight:800;margin:12px 0 8px">{h}</div><div style="font-size:23px;line-height:1.4;color:#d6e3f5">{b}</div></div>''' for i, (t, h, b) in enumerate(news))
s2 = background(dim=.55, horizon=1150) + top("// TOP STORIES") + f'<div style="position:absolute;top:110px;left:60px;right:60px">{cards}</div>' + foot()

# ---------- slajd 3: tabela tygodnia + liczby + wniosek
rows = "".join(f'<div style="display:flex;align-items:center;font-size:30px;padding:12px 0;border-bottom:1px solid #00f0ff22"><b class="orb" style="width:140px">{s}</b><span style="flex:1">${p}</span><span style="width:200px;text-align:right;font-weight:800">{pc(a)}</span><span style="width:220px;text-align:right;font-weight:800">{pc(w)}</span></div>' for s, p, a, w in coins)
tile = lambda v, l, c="pm": f'<div class="panel {c}" style="position:relative;flex:1;text-align:center;padding:20px 8px"><div class="orb" style="font-weight:900;font-size:36px">{v}</div><div class="lbl" style="font-size:15px;margin-top:6px">{l}</div></div>'
s3 = background(dim=.6, horizon=1200) + top("// WEEKLY SCOREBOARD") + f'''
<div class="panel" style="top:120px;left:60px;right:60px;padding:22px 40px"><div style="display:flex" class="lbl"><span style="width:140px">COIN</span><span style="flex:1">PRICE</span><span style="width:200px;text-align:right">24H</span><span style="width:220px;text-align:right">7 DAYS</span></div>{rows}</div>
<div style="position:absolute;top:790px;left:60px;right:60px;display:flex;gap:18px">{tile(G["mcap"], "MARKET CAP")}{tile(G["fg"], "FEAR & GREED: " + G["fg_label"])}{tile(G["liq"], "BTC LIQ. 24H")}</div>
<div class="panel" style="top:960px;left:60px;right:60px;padding:26px 40px;font-size:26px;line-height:1.45;border-color:{YE};box-shadow:0 0 18px {YE}88"><b style="color:{YE};text-shadow:0 0 10px {YE}">TAKEAWAY:</b> {G["takeaway"]}</div>''' + foot("FOLLOW FOR DAILY ▸")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": W, "height": H})
        for i, s in enumerate([s1, s2, s3], 1):
            await pg.set_content(f'<!doctype html><html><head><meta charset="utf-8">{FONT}<style>{CSS}</style></head><body>{s}</body></html>')
            await pg.wait_for_load_state("networkidle"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{OUT}/slide{i}.png")
        await b.close()
asyncio.run(main())

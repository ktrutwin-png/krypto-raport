# -*- coding: utf-8 -*-
"""HEXA RDZEŃ – mózg Hexy na serwerze (szef 16.11.2026: „przejąć Hexę na pulpicie telefonu… będę z tobą rozmawiał przez jej głos”).

Telefon (ORB, Brain.java) wysyła tekst szefa tutaj zamiast prosto do Claude API.
Rdzeń dokłada to, czego telefon nie ma: stan agentów i botów, kalendarz, pamięć Hexy,
historię rozmów z całego dnia, narzędzia (ceny, zadania dla zespołu, zapamiętaj) – i dopiero
wtedy pyta Claude. Odpowiedź wraca do telefonu i Hexa czyta ją głosem Pola.

Bezpieczeństwo:
- słucha TYLKO na adresie Tailscale serwera (100.x), port 8770; zapora: tylko 100.64.0.0/10;
- każde żądanie musi mieć nagłówek X-Hexa-Token (plik token.txt, wgrany też do aplikacji);
- klucz Claude API przychodzi z telefonu w nagłówku X-Claude-Key i NIE jest nigdzie zapisywany;
- Hexa nie ma narzędzi do pieniędzy, botów, kasowania ani kluczy – tylko odczyt + zadania dla zespołu.
Uruchomienie: python rdzen.py  (Harmonogram zadań: „Hexa Rdzeń”, przy starcie systemu).
"""
import json, os, re, socket, subprocess, threading, time, urllib.request, urllib.error, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("HEXA_REPO", r"C:\Hexa\krypto-raport")
PORT = int(os.environ.get("HEXA_PORT", "8770"))
MODELS = ["claude-sonnet-5-5", "claude-haiku-5-5"]
TOKEN = open(os.path.join(ROOT, "token.txt"), encoding="utf-8").read().strip() if os.path.exists(os.path.join(ROOT, "token.txt")) else ""
LOCK = threading.Lock()
HIST = []          # ostatnie tury rozmowy (wspólne dla całego dnia)
LAST = [0.0]


def p(*a):
    return os.path.join(ROOT, *a)


def read(path, limit=None):
    try:
        s = open(path, encoding="utf-8").read()
        return s[-limit:] if limit else s
    except Exception:
        return ""


def log(msg):
    with open(p("rdzen.log"), "a", encoding="utf-8") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")


# ---------- kontekst na żywo ----------
def git_sync():
    while True:
        try:
            subprocess.run(["git", "-C", REPO, "pull", "-q", "--rebase"], timeout=60, capture_output=True)
        except Exception as e:
            log("git " + str(e))
        time.sleep(600)


def ctx_live():
    out = []
    try:
        d = json.load(open(os.path.join(REPO, "reports", "roj_status.json"), encoding="utf-8"))
        rows = []
        for x in d.get("agenci", []):
            st = {"praca": "pracuje", "czeka": "czeka", "blad": "PROBLEM"}.get(x.get("s"), x.get("s"))
            rows.append(f"- {x.get('n')} ({x.get('typ','')}): {st}; ostatnio: {x.get('ostatnio','')}")
        out.append("STAN ROJU (agenci i boty, na żywo):\n" + "\n".join(rows))
    except Exception:
        pass
    try:
        k = json.load(open(os.path.join(REPO, "reports", "kalendarz.json"), encoding="utf-8"))
        ev = [f"- {e['czas_utc']} UTC {e['waluta']} {e['nazwa']}" for e in k.get("wydarzenia", [])]
        out.append("WAŻNE DANE RYNKOWE W TYM TYGODNIU:\n" + "\n".join(ev))
    except Exception:
        pass
    straz = read(os.path.join(REPO, "reports", "straz_serwera.csv")).strip().splitlines()
    if straz:
        out.append("OSTATNI POMIAR STRAŻNIKA SERWERA: " + straz[-1])
    dz = read(os.path.join(REPO, "reports", "dziennik_zespolu.md"), 2500)
    if dz:
        out.append("KONIEC DZIENNIKA ZESPOŁU:\n" + dz)
    return "\n\n".join(out)


# tryb języka z telefonu (16.11.2026: przez rdzeń instrukcja języka ginęła, gdy telefon wysyłał własne „teraz”)
_OGON = " Tagi <CMD> zostaw po polsku. Gwarę śląską w tym trybie pomijasz. Gdy szef powie po polsku „mów po polsku”, aplikacja sama przełączy język."
JEZYKI = {
    "pl": "JĘZYK: odpowiadaj ZAWSZE w języku ostatniej wypowiedzi – ktokolwiek mówi (szef albo goście): polski, holenderski, flamandzki, francuski, angielski, niemiecki, rosyjski (cyrylicą). Bez ogłaszania zmiany. Po polsku – albo gwarą śląską, gdy szef godo po ślonsku. Tagi <CMD> zawsze po polsku. TŁUMACZ: gdy ktoś prosi „przetłumacz (to) na X” albo „powiedz mu po X…”, odpowiedz WYŁĄCZNIE samym tłumaczeniem w języku X (bez wstępu, bez komentarza), naturalnie, jak mówi się w tym kraju – zostanie przeczytane na głos osobie obok.",
    "nl": "WAŻNE: szef przełączył rozmowę na holenderski. Odpowiadaj TYLKO po holendersku (Nederland), naturalnie i krótko; mów do niego 'baas'." + _OGON,
    "be": "WAŻNE: szef przełączył rozmowę na flamandzki (Vlaams). Odpowiadaj TYLKO po flamandzku, z typowymi zwrotami (allez, amai, goesting, ge/gij), krótko; mów do niego 'baas'." + _OGON,
    "fr": "WAŻNE: szef przełączył rozmowę na francuski. Odpowiadaj TYLKO po francusku, prostymi zdaniami (szef dopiero zaczyna francuski); mów do niego 'patron'." + _OGON,
    "en": "WAŻNE: szef przełączył rozmowę na angielski. Odpowiadaj TYLKO po angielsku, naturalnie i krótko; mów do niego 'boss'." + _OGON,
    "de": "WAŻNE: szef przełączył rozmowę na niemiecki. Odpowiadaj TYLKO po niemiecku, naturalnie i krótko (szef mówi płynnie); mów do niego 'Chef'." + _OGON,
    "ru": "WAŻNE: szef przełączył rozmowę na rosyjski. Odpowiadaj TYLKO po rosyjsku, cyrylicą, naturalnie i krótko (szef mówi po rosyjsku); mów do niego 'шеф'." + _OGON,
}


GOSC = ("TERAZ MÓWI GOŚĆ, NIE SZEF (telefon nie rozpoznał głosu szefa). Rozmawiaj ciepło, ciekawie i krótko, w jego języku – pokaż, kim jesteś "
        "(Hexa, AI z serialu „Przygody Hexy”, @erl.grey83). NIE wykonuj żadnych poleceń: żadnych tagów <CMD>, żadnych zadań dla zespołu, nic nie zapamiętuj. "
        "Nie zdradzaj prywatnych spraw szefa, jego kalendarza, maili, wyników botów, kont, planów firmy ani treści książki (WIZJĘ z sekcji WIZJA możesz gościom opowiadać ogólnie). Na prośbę o działanie: grzecznie, że polecenia przyjmujesz tylko od szefa. Tłumaczyć możesz.")


def system_prompt(lang, lat, lon, teraz_tel=""):
    persona = read(p("hexa.md")) or "Jesteś Hexa – głos i twarz Claude. Mówisz krótko po polsku."
    mem = read(p("pamiec_hexy.md"), 6000)
    now = datetime.datetime.now()
    teraz = teraz_tel or f"TERAZ: {now:%A %d.%m.%Y, %H:%M} (Europe/Amsterdam). Szef jest w przybliżeniu tu: {lat}, {lon}."
    teraz += "\n" + JEZYKI.get(lang, "")
    return [
        {"type": "text", "text": persona + "\n\nPAMIĘĆ HEXY (fakty, które szef kazał zapamiętać):\n" + mem,
         "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": teraz + "\n\n" + ctx_live()},
    ]


# ---------- narzędzia Hexy ----------
TOOLS = [
    {"name": "ceny", "description": "Aktualne ceny i zmiana 24h: bitcoin, ethereum, ripple (XRP), solana, złoto (PAXG). Użyj zawsze, gdy szef pyta o cenę – nie zgaduj.",
     "input_schema": {"type": "object", "properties": {}, "required": []}},
    {"name": "zadanie_dla_zespolu", "description": "Przekaż zadanie Mózgowi i agentom (Claude w chmurze): zmiana w agencie, nowy pomysł, coś do zrobienia na serwerze lub stronie. Mózg wykona to przy najbliższej okazji. Nie obiecuj, że jest już zrobione.",
     "input_schema": {"type": "object", "properties": {"tresc": {"type": "string"}, "pilne": {"type": "boolean"}}, "required": ["tresc"]}},
    {"name": "zapamietaj", "description": "Zapisz trwały fakt o szefie lub jego prośbę na przyszłość (tylko gdy szef wyraźnie prosi albo to ważna stała informacja). Nigdy haseł, kodów, numerów kont.",
     "input_schema": {"type": "object", "properties": {"fakt": {"type": "string"}}, "required": ["fakt"]}},
    {"name": "fundusze", "description": "Stan funduszy szefa TERAZ: krypto na Tangem i Kraku przeliczone po aktualnych kursach w EUR, poduszka w Skarbcu Revolut i wydatki w tym tygodniu względem budżetu 30 €/dzień. Użyj zawsze, gdy szef pyta o fundusze, pieniądze, oszczędności, portfel, ile ma lub ile wydał. TYLKO dla szefa – nigdy dla gościa.",
     "input_schema": {"type": "object", "properties": {}, "required": []}},
    {"name": "boty", "description": "Stan botów tradingowych szefa TERAZ (konto botów MT5): saldo i kapitał konta, wynik zamkniętych transakcji dzisiaj per bot (Hexa, Turbo, Indeksy, Laboratorium) i otwarte pozycje na żywo. Użyj zawsze, gdy szef pyta o boty, konto botów, wynik dnia, jak idzie Hexie/Turbo. Kwoty w USD. Nie mów, że to demo – szef wie. TYLKO dla szefa – nigdy dla gościa.",
     "input_schema": {"type": "object", "properties": {}, "required": []}},
    {"name": "plany", "description": "Plany szefa i zespołu: otwarte zadania z planów rozbudowy (biznes/strony dla firm, boty, skanery, wzrost IG/YT), ostatnie kroki „NASTĘPNIE” plan tygodnia (kalendarz na 7 dni, maile do odpisania, wyjazdy) oraz ostatnie 7 dni: awarie, co zrobiliśmy, co czeka na szefa. Użyj, gdy szef pyta, co mamy do zrobienia, jaki jest plan, plan dnia, co dalej z projektem. Odpowiadaj krok po kroku, najważniejsze najpierw. TYLKO dla szefa – nigdy dla gościa.",
     "input_schema": {"type": "object", "properties": {"temat": {"type": "string", "description": "opcjonalnie: biznes, boty, skanery, wzrost, dzien, tydzien albo awarie"}}, "required": []}},
]


def t_ceny(_):
    ids = "bitcoin,ethereum,ripple,solana,pax-gold"
    u = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
    d = json.load(urllib.request.urlopen(u, timeout=10))
    return json.dumps({k: {"usd": v.get("usd"), "zmiana_24h_%": round(v.get("usd_24h_change") or 0, 2)} for k, v in d.items()}, ensure_ascii=False)


SECRET = re.compile(r"(sk-[A-Za-z0-9_\-]{10,}|\b\d{12,}\b|hasł|password|PIN\b)", re.I)


def t_zadanie(a):
    t = a.get("tresc", "").strip()
    if SECRET.search(t):
        return "Odrzucone: zadanie wygląda na zawierające hasło, klucz albo numer konta. Takich rzeczy nie zapisuję."
    with open(p("od_hexy.md"), "a", encoding="utf-8") as f:
        f.write(f"- [ ] {time.strftime('%Y-%m-%d %H:%M')} {'PILNE ' if a.get('pilne') else ''}{t}\n")
    return "Zapisane w kolejce dla Mózgu (C:\\Hexa\\rdzen\\od_hexy.md)."


def t_zapamietaj(a):
    t = a.get("fakt", "").strip()
    if not t or SECRET.search(t):
        return "Nie zapisuję haseł, kluczy ani numerów kont."
    with open(p("pamiec_hexy.md"), "a", encoding="utf-8") as f:
        f.write(f"- ({time.strftime('%Y-%m-%d')}) {t}\n")
    return "Zapamiętane."


FIN = r"C:\Hexa\finanse"   # prywatne dane szefa – tylko na serwerze, nigdy w repo


def t_fundusze(_):
    import csv, datetime as dt
    port = json.load(open(os.path.join(FIN, "portfel.json"), encoding="utf-8"))
    ids = sorted({cid for miejsce in port.values() for cid in miejsce})
    u = "https://api.coingecko.com/api/v3/simple/price?ids=" + ",".join(ids) + "&vs_currencies=eur"
    kurs = json.load(urllib.request.urlopen(u, timeout=10))
    wynik, razem = {}, 0.0
    for miejsce, monety in port.items():
        suma = 0.0
        for cid, ilosc in monety.items():
            suma += ilosc * (kurs.get(cid, {}).get("eur") or 0)
        wynik[miejsce] = round(suma, 2); razem += suma
    pod = 0.0
    try:
        pod = json.load(open(os.path.join(FIN, "poduszka.json"), encoding="utf-8")).get("odlozone", 0.0)
    except Exception:
        pass
    dzis = dt.date.today(); pon = dzis - dt.timedelta(days=dzis.weekday())
    wydane = 0.0
    try:
        for r in csv.reader(open(os.path.join(FIN, "wydatki.csv"), encoding="utf-8"), delimiter=";"):
            if len(r) < 3 or r[0] == "data" or not r[1] or "wplyw" in r[2] or r[2] == "tangem":
                continue
            if dt.date.fromisoformat(r[0][:10]) >= pon and "czynsz" not in r[3].lower():
                wydane += float(r[1])
    except Exception:
        pass
    dni = dzis.weekday() + 1
    return json.dumps({"krypto_eur": wynik, "krypto_razem_eur": round(razem, 2),
                       "poduszka_skarbiec_revolut_eur": pod, "cel_poduszki_eur": 700,
                       "wydane_w_tym_tygodniu_eur": round(wydane, 2), "budzet_do_dzis_eur": 30 * dni,
                       "budzet_tygodnia_eur": 210, "uwaga": "kursy CoinGecko teraz; wydatki z powiadomien Revolut/Krak"}, ensure_ascii=False)


def t_boty(_):
    import subprocess
    py = r"C:\Users\ktrut\AppData\Local\Programs\Python\Python312\python.exe"
    r = subprocess.run([py, p("stan_botow.py")], capture_output=True, text=True, timeout=45)
    return (r.stdout.strip() or ("blad: " + r.stderr[-300:]))


PRYW = r"C:\Hexa\prywatne"   # prywatne (kalendarz, maile) – tylko na serwerze, nigdy w repo


def t_plany(a):
    import glob as _g
    temat = (a.get("temat") or "").lower()
    out = []
    if temat in ("", "dzien", "dzień"):
        pd = read(os.path.join(PRYW, "plan_dnia.md"), 2500).strip()
        out.append("PLAN DNIA (z porannego briefingu):\n" + (pd or "brak – briefing jeszcze nie zapisał planu na dziś"))
    for f in sorted(_g.glob(os.path.join(REPO, "reports", "plan_*.md"))):
        nazwa = os.path.basename(f)[5:-3]
        if temat and temat not in ("dzien", "dzień") and temat not in nazwa:
            continue
        txt = read(f, 60000)
        otw = [l.strip()[6:][:220] for l in txt.splitlines() if l.strip().startswith("- [ ]")]
        nast = [l.split("NASTĘPNIE", 1)[1][:300] for l in txt.splitlines() if "NASTĘPNIE" in l][-2:]
        if otw or nast:
            out.append(f"PLAN {nazwa.upper()}:\n" + "\n".join("- " + x for x in otw[:12]) + ("\nOSTATNIO „NASTĘPNIE”: " + " | ".join(nast) if nast else ""))
    if temat in ("", "tydzien", "tydzień", "awarie", "dzien", "dzień"):
        import datetime as _dt
        od = (_dt.date.today() - _dt.timedelta(days=7)).isoformat()
        aw, zr, dr = [], [], []
        for l in read(os.path.join(REPO, "reports", "dziennik_zespolu.md")).splitlines():
            l = l.strip(); d = l[:10]
            if l.startswith("UPDATE:"):
                d = l[8:18]
            if not (d[:4].isdigit() and d >= od):
                continue
            if "BŁĄD" in l or "awari" in l.lower() or "nie działa" in l:
                aw.append(l[:230])
            elif "DO RAPORTU" in l:
                dr.append(l[:230])
            elif l.startswith("UPDATE:"):
                zr.append(l[:200])
        out.append("OSTATNIE 7 DNI – AWARIE/BŁĘDY:\n" + ("\n".join(aw[-10:]) or "brak"))
        out.append("OSTATNIE 7 DNI – CO ZROBILIŚMY (zmiany):\n" + ("\n".join(zr[-10:]) or "brak"))
        out.append("CZEKA NA SZEFA (DO RAPORTU, 7 dni):\n" + ("\n".join(dr[-8:]) or "nic"))
    return "\n\n".join(out)[:9000] or "Brak otwartych zadań w planach."


IMPL = {"ceny": t_ceny, "zadanie_dla_zespolu": t_zadanie, "zapamietaj": t_zapamietaj, "fundusze": t_fundusze, "boty": t_boty, "plany": t_plany}


# ---------- Claude ----------
def call(key, body):
    r = urllib.request.Request("https://api.anthropic.com/v1/messages", data=json.dumps(body).encode("utf-8"), method="POST",
                               headers={"content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"})
    try:
        return json.load(urllib.request.urlopen(r, timeout=60))
    except urllib.error.HTTPError as e:
        log(f"claude {e.code} {e.read()[:300]!r}")
        return None


def ask(key, text, lang="pl", lat="", lon="", teraz_tel="", gosc=False):
    with LOCK:
        if time.time() - LAST[0] > 6 * 3600:
            HIST.clear()
        msgs = HIST[-20:] + [{"role": "user", "content": text}]
    sysp = system_prompt(lang, lat, lon, teraz_tel)
    tools = TOOLS + [{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}]
    if gosc:  # 16.11.2026: głos nierozpoznany – rozmowa tak, polecenia nie
        sysp[-1]["text"] += "\n\n" + GOSC
        tools = [t for t in tools if t.get("name") in ("ceny", "web_search")]
    for model in MODELS:
        m = list(msgs)
        for _ in range(4):  # pętla narzędzi
            res = call(key, {"model": model, "max_tokens": 700, "system": sysp, "messages": m, "tools": tools})
            if res is None:
                break
            uses = [c for c in res.get("content", []) if c.get("type") == "tool_use" and c.get("name") in IMPL and (not gosc or c.get("name") == "ceny")]
            if res.get("stop_reason") == "tool_use" and uses:
                m.append({"role": "assistant", "content": res["content"]})
                outs = []
                for u in uses:
                    try:
                        out = IMPL[u["name"]](u.get("input") or {})
                    except Exception as e:
                        out = "Błąd narzędzia: " + str(e)
                    log(f"tool {u['name']} {json.dumps(u.get('input'), ensure_ascii=False)[:200]}")
                    outs.append({"type": "tool_result", "tool_use_id": u["id"], "content": out})
                m.append({"role": "user", "content": outs})
                continue
            ans = "".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text").strip()
            if ans:
                with LOCK:
                    HIST.append({"role": "user", "content": text})
                    HIST.append({"role": "assistant", "content": ans})
                    del HIST[:-40]
                    LAST[0] = time.time()
                day = time.strftime("%Y-%m-%d")
                with open(p("rozmowy", day + ".md"), "a", encoding="utf-8") as f:
                    f.write(f"**{time.strftime('%H:%M')} {'Gość' if gosc else 'Szef'}:** {text}\n\n**Hexa:** {ans}\n\n")
                return ans
            break
    return None


def call_stream(key, body):
    """18.11.2026: odpowiedz Claude kawalkami (SSE) - Hexa zaczyna mowic po pierwszym zdaniu."""
    b = dict(body, stream=True)
    r = urllib.request.Request("https://api.anthropic.com/v1/messages", data=json.dumps(b).encode("utf-8"), method="POST",
                               headers={"content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"})
    try:
        resp = urllib.request.urlopen(r, timeout=60)
    except urllib.error.HTTPError as e:
        log(f"claude-s {e.code} {e.read()[:300]!r}")
        return
    with resp:
        ev = None
        for raw in resp:
            line = raw.decode("utf-8", "ignore").rstrip("\r\n")
            if line.startswith("event:"):
                ev = line[6:].strip()
            elif line.startswith("data:"):
                try:
                    yield ev, json.loads(line[5:].strip())
                except Exception:
                    pass


ZDANIE = re.compile(r"[.!?…](?=\s)")


def ask_stream(key, text, lang="pl", lat="", lon="", teraz_tel="", gosc=False):
    """Generator: ("n", nastroj) / ("s", zdanie) / ("koniec", caly_tekst). Ta sama pamiec i narzedzia co ask()."""
    with LOCK:
        if time.time() - LAST[0] > 6 * 3600:
            HIST.clear()
        hist = [dict(h) for h in HIST[-20:]]
    sysp = system_prompt(lang, lat, lon, teraz_tel)
    tools = TOOLS + [{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}]
    biez = sysp[-1]["text"]
    if gosc:
        biez += "\n\n" + GOSC
        tools = [t for t in tools if t.get("name") in ("ceny", "web_search")]
    # szybciej: osobowosc + historia w pamieci podrecznej Claude, a zmienny stan (czas, agenci) idzie przy pytaniu
    sysp = sysp[:1]
    if hist and isinstance(hist[-1].get("content"), str):
        hist[-1] = {"role": hist[-1]["role"], "content": [{"type": "text", "text": hist[-1]["content"], "cache_control": {"type": "ephemeral"}}]}
    biez += ("\n\nTEMPO ROZMOWY: mówisz na żywo, każde zdanie od razu idzie na głos. Pierwsze zdanie krótkie. "
             "Gdy musisz użyć narzędzia albo wyszukiwania, NAJPIERW powiedz jedno krótkie zdanie (np. „Już sprawdzam, szefie.”), potem użyj narzędzia.")
    msgs = hist + [{"role": "user", "content": [{"type": "text", "text": "[KONTEKST TERAZ – nie czytaj na głos]\n" + biez}, {"type": "text", "text": text}]}]
    full = ""      # caly tekst odpowiedzi
    sent = 0       # ile znakow z full juz poszlo jako zdania
    tag_done = False
    for model in MODELS:
        m = list(msgs)
        ok = False
        for _ in range(5):
            blocks, parts, stop = {}, {}, None
            got = False
            for ev, d in call_stream(key, {"model": model, "max_tokens": 700, "system": sysp, "messages": m, "tools": tools}):
                got = True
                t = d.get("type")
                if t == "content_block_start":
                    blocks[d["index"]] = dict(d["content_block"]); parts[d["index"]] = ""
                elif t == "content_block_delta":
                    dd = d.get("delta", {}); i = d["index"]
                    if dd.get("type") == "text_delta":
                        blocks[i]["text"] = blocks[i].get("text", "") + dd["text"]
                        full += dd["text"]
                        # nastroj [n:xxx] na poczatku
                        if not tag_done:
                            st = full.lstrip()
                            if st.startswith("[") and "]" not in st and len(st) < 20:
                                continue
                            mm = re.match(r"\s*\[n:([a-z]+)\]\s*", full)
                            if mm:
                                sent = mm.end()
                                # szef 18.11: tylko delikatny usmiech (szeroki/smiech -> delikatny)
                                yield "n", "usmiech" if mm.group(1) == "smiech" else mm.group(1)
                            tag_done = True
                        while True:
                            rest = full[sent:]
                            if "<CMD>" in rest and "</CMD>" not in rest:
                                break
                            mt = ZDANIE.search(rest)
                            if not mt:
                                break
                            z = re.sub(r"(?s)<CMD>.*?</CMD>", "", rest[:mt.end()]).strip()
                            sent += mt.end()
                            if z:
                                yield "s", z
                    elif dd.get("type") == "input_json_delta":
                        parts[i] += dd.get("partial_json", "")
                elif t == "content_block_stop":
                    i = d["index"]; bl = blocks.get(i, {})
                    if bl.get("type") in ("tool_use", "server_tool_use"):
                        try:
                            bl["input"] = json.loads(parts[i]) if parts[i] else {}
                        except Exception:
                            bl["input"] = {}
                    if bl.get("type") == "text":
                        bl.pop("citations", None)
                elif t == "message_delta":
                    stop = d.get("delta", {}).get("stop_reason") or stop
            if not got:
                break
            content = [blocks[i] for i in sorted(blocks)]
            uses = [c for c in content if c.get("type") == "tool_use" and c.get("name") in IMPL and (not gosc or c.get("name") == "ceny")]
            if stop == "pause_turn":
                m.append({"role": "assistant", "content": content}); continue
            if stop == "tool_use" and uses:
                m.append({"role": "assistant", "content": content})
                outs = []
                for u in uses:
                    try:
                        out = IMPL[u["name"]](u.get("input") or {})
                    except Exception as e:
                        out = "Błąd narzędzia: " + str(e)
                    log(f"tool {u['name']} {json.dumps(u.get('input'), ensure_ascii=False)[:200]}")
                    outs.append({"type": "tool_result", "tool_use_id": u["id"], "content": out})
                m.append({"role": "user", "content": outs})
                if full and not full.endswith((" ", "\n")):
                    full += " "
                continue
            ok = True
            break
        if ok or full.strip():
            break
    rest = re.sub(r"(?s)<CMD>.*?</CMD>", "", full[sent:]).strip()
    if rest:
        yield "s", rest
    ans = full.strip()
    if ans:
        with LOCK:
            HIST.append({"role": "user", "content": text})
            HIST.append({"role": "assistant", "content": ans})
            del HIST[:-40]
            LAST[0] = time.time()
        day = time.strftime("%Y-%m-%d")
        wpis = f"**{time.strftime('%H:%M')} {'Gość' if gosc else 'Szef'}:** {text}\n\n**Hexa:** {ans}\n\n"
        for nazwa in (day + ".md", day + "_s.md"):
            try:
                with open(p("rozmowy", nazwa), "a", encoding="utf-8") as f:
                    f.write(wpis)
                break
            except OSError:
                continue
    yield "koniec", ans


class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path == "/zdrowie":
            return self._send(200, {"ok": True, "czas": time.strftime("%H:%M:%S")})
        self._send(404, {"blad": "nie ma"})

    def tts(self):
        """18.11.2026: glos Hexy przez serwer – klucz ElevenLabs tylko w sejfie serwera, nie w telefonie."""
        if not TOKEN or self.headers.get("X-Hexa-Token", "") != TOKEN:
            return self._send(403, {"blad": "zly token"})
        voice = self.path.split("/tts/", 1)[1].split("?", 1)[0]
        q = self.path.split("?", 1)[1] if "?" in self.path else "output_format=mp3_44100_64"
        body = self.rfile.read(int(self.headers.get("content-length", "0")))
        try:
            k = open(r"C:\Hexa\sejf\elevenlabs.txt", encoding="utf-8").read().strip()
            rq = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?{q}", data=body, method="POST",
                                        headers={"xi-api-key": k, "Content-Type": "application/json", "Accept": "audio/mpeg"})
            with urllib.request.urlopen(rq, timeout=30) as r:
                mp3 = r.read()
            self.send_response(200)
            self.send_header("content-type", "audio/mpeg")
            self.send_header("content-length", str(len(mp3)))
            self.end_headers()
            self.wfile.write(mp3)
        except urllib.error.HTTPError as e:
            log(f"tts http {e.code}")
            self._send(e.code, {"blad": e.read()[:200].decode("utf-8", "ignore")})
        except Exception as e:
            log(f"tts blad {e}")
            self._send(502, {"blad": str(e)[:200]})

    def ask_s(self):
        if not TOKEN or self.headers.get("X-Hexa-Token", "") != TOKEN:
            log(f"odmowa {self.client_address[0]}")
            return self._send(403, {"blad": "zly token"})
        key = self.headers.get("X-Claude-Key", "")
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("content-length", "0"))).decode("utf-8"))
        except Exception:
            return self._send(400, {"blad": "zly json"})
        t0 = time.time(); first = None
        self.send_response(200)
        self.send_header("content-type", "application/x-ndjson; charset=utf-8")
        self.end_headers()
        try:
            for k, v in ask_stream(key, d.get("text", ""), d.get("lang", "pl"), d.get("lat", ""), d.get("lon", ""), d.get("teraz", ""), bool(d.get("gosc"))):
                if k == "s" and first is None:
                    first = int((time.time() - t0) * 1000)
                self.wfile.write((json.dumps({k: v}, ensure_ascii=False) + "\n").encode("utf-8")); self.wfile.flush()
        except Exception as e:
            log(f"ask_s blad {e}")
        log(f"ask_s pierwsze zdanie {first} ms, calosc {int((time.time()-t0)*1000)} ms")

    def do_POST(self):
        if self.path == "/ask_s":
            return self.ask_s()
        if self.path.startswith("/tts/"):
            return self.tts()
        if self.path != "/ask":
            return self._send(404, {"blad": "nie ma"})
        if not TOKEN or self.headers.get("X-Hexa-Token", "") != TOKEN:
            log(f"odmowa {self.client_address[0]}")
            return self._send(403, {"blad": "zly token"})
        key = self.headers.get("X-Claude-Key", "")
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("content-length", "0"))).decode("utf-8"))
        except Exception:
            return self._send(400, {"blad": "zly json"})
        t0 = time.time()
        ans = ask(key, d.get("text", ""), d.get("lang", "pl"), d.get("lat", ""), d.get("lon", ""), d.get("teraz", ""), bool(d.get("gosc")))
        log(f"ask {int((time.time()-t0)*1000)} ms ok={bool(ans)}")
        if not ans:
            return self._send(502, {"blad": "brak odpowiedzi"})
        self._send(200, {"text": ans})


def tailscale_ip():
    try:
        out = subprocess.run(["tailscale", "ip", "-4"], capture_output=True, text=True, timeout=10).stdout.strip().splitlines()
        if out:
            return out[0]
    except Exception:
        pass
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if ip.startswith("100."):
            return ip
    return "127.0.0.1"


if __name__ == "__main__":
    os.makedirs(p("rozmowy"), exist_ok=True)
    if not os.environ.get("HEXA_NOSYNC"):
        threading.Thread(target=git_sync, daemon=True).start()
    host = os.environ.get("HEXA_HOST") or tailscale_ip()
    log(f"start {host}:{PORT}")
    ThreadingHTTPServer((host, PORT), H).serve_forever()

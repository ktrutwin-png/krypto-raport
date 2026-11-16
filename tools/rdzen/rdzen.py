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
import json, os, re, socket, subprocess, threading, time, urllib.request, datetime
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
        "Nie zdradzaj prywatnych spraw szefa, jego kalendarza, maili, wyników botów, kont, planów firmy ani treści książki. Na prośbę o działanie: grzecznie, że polecenia przyjmujesz tylko od szefa. Tłumaczyć możesz.")


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


IMPL = {"ceny": t_ceny, "zadanie_dla_zespolu": t_zadanie, "zapamietaj": t_zapamietaj}


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

    def do_POST(self):
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
    threading.Thread(target=git_sync, daemon=True).start()
    host = os.environ.get("HEXA_HOST") or tailscale_ip()
    log(f"start {host}:{PORT}")
    ThreadingHTTPServer((host, PORT), H).serve_forever()

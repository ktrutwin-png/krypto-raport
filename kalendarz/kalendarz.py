# -*- coding: utf-8 -*-
"""Kalendarz ekonomiczny dla botów: przerwa w otwieraniu pozycji wokół ważnych danych (High impact).
Plik danych: C:\\Hexa\\kalendarz\\tydzien.json (pobierz.ps1 – codziennie 05:30 i w niedzielę 19:30).
Brak pliku albo błąd = brak przerwy (bot działa normalnie)."""
import json, os
from datetime import datetime, timezone, timedelta

PLIK = r"C:\Hexa\kalendarz\tydzien.json"


def przerwa(waluty=("USD",), teraz=None):
    """Zwraca nazwę wydarzenia, jeśli jesteśmy w oknie ±przerwa_min wokół niego, inaczej None."""
    try:
        with open(PLIK, encoding="utf-8-sig") as f:
            d = json.load(f)
        okno = timedelta(minutes=int(d.get("przerwa_min", 30)))
        t = teraz or datetime.now(timezone.utc)
        ev = d.get("wydarzenia") or []
        if isinstance(ev, dict):
            ev = [ev]
        for e in ev:
            if e.get("waluta") not in waluty:
                continue
            c = datetime.strptime(e["czas_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            if abs(t - c) <= okno:
                return f"{e['waluta']} {e['nazwa']} {c:%H:%M} UTC"
    except Exception:
        return None
    return None

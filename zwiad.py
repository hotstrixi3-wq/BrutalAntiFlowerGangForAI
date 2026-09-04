#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZWIAD - oczy operatora. Pokazuje PRAWDE o pliku, niczego nie zmienia.

Po co powstal (zasada operatora, 2026-09-04):

    "Narzedzie ma ci pomagac, a nie slepo wykonywac glupie opcje.
     To, ze skrypt ma byc sprytny i nieomylny, oznacza, ze ma byc
     narzedziem, ktore nie wprowadza cie w blad, a pokazuje prawde."

Do tej pory agent-operator dostawal od rodziny LICZBY:

    [DO ZAGLADY] app.py: cyr 4

Cztery co? Gdzie? W kodzie czy w komentarzu? Na co zostana zamienione?
Czy plik po naprawie nadal zadziala? Zeby to wiedziec, trzeba bylo zrobic
kopie, puscic zaglade i porownac diffem - czyli DZIALAC, zeby sie
DOWIEDZIEC. Odwrotnie niz powinno byc.

ZWIAD odwraca kolejnosc: najpierw wiedza, potem decyzja operatora.
Pokazuje kazde skazenie z osobna, mowi czy siedzi w KODZIE (grozne) czy
w danych (nieszkodliwe), podaje DOKLADNY wynik naprawy dla kazdego znaku,
oznacza znaki, ktorych rodzina nie umie naprawic, i sprawdza, czy plik
po naprawie nadal bedzie sie kompilowal.

NICZEGO NIE ZAPISUJE. Zadnej flagi zapisu tu nie ma i nie bedzie.

Uzycie:
    python3 zwiad.py PLIK...              # raport czytelny dla czlowieka
    python3 zwiad.py --json PLIK...       # to samo maszynowo (dla agenta)
    python3 zwiad.py --podglad PLIK       # roznica przed/po, bez zapisu
    python3 zwiad.py --selftest

Kod wyjscia: 0 = czysto, 1 = sa skazenia, 2 = sa skazenia NIENAPRAWIALNE.
"""

import io
import json
import os
import subprocess
import sys
import unicodedata

WERSJA = "1.0.0"
KORZEN = os.path.dirname(os.path.abspath(__file__))

JEZYKI_KODU = ("js", "ts", "java", "go", "rs", "cs", "c", "cpp", "h", "hpp",
               "php", "rb", "swift", "kt")


def _zaladuj(nazwa):
    """Laduje narzedzie rodziny jako modul (bez uruchamiania main)."""
    import importlib.util
    p = os.path.join(KORZEN, nazwa)
    s = importlib.util.spec_from_file_location(nazwa[:-3], p)
    m = importlib.util.module_from_spec(s)
    sys.modules[nazwa[:-3]] = m
    s.loader.exec_module(m)
    return m


def _pozycje_chronione(tekst, ext):
    """Zbior indeksow lezacych w literalach/komentarzach (.py) albo None."""
    if ext != "py":
        return None
    try:
        Z = _zaladuj("ZagladaKultury.py")
        return Z._chronione_pozycje(tekst)
    except Exception:
        return None


def zbadaj(sciezka):
    """Pelny obraz pliku. Zwraca slownik - bez zadnych zmian na dysku."""
    wynik = {"plik": sciezka, "czytelny": True, "znaleziska": [],
             "podsumowanie": {}, "kompiluje_przed": None,
             "kompiluje_po": None, "nienaprawialne": 0}
    try:
        surowe = io.open(sciezka, "rb").read()
    except OSError as e:
        wynik["czytelny"] = False
        wynik["blad"] = str(e)
        return wynik
    try:
        tekst = surowe.decode("utf-8")
    except UnicodeDecodeError as e:
        wynik["czytelny"] = False
        wynik["blad"] = "nie jest poprawnym UTF-8: %s" % e
        return wynik

    ext = sciezka.rsplit(".", 1)[-1].lower() if "." in sciezka else ""
    chronione = _pozycje_chronione(tekst, ext)

    Z = _zaladuj("ZagladaKultury.py")
    licznik = dict((k, 0) for k in Z.KATEGORIE)

    starty, poz = [], 0
    for linia in tekst.split("\n"):
        starty.append(poz)
        poz += len(linia) + 1

    def nr_linii(i):
        lo, hi = 0, len(starty) - 1
        while lo < hi:
            sr = (lo + hi + 1) // 2
            if starty[sr] <= i:
                lo = sr
            else:
                hi = sr - 1
        return lo + 1

    linie = tekst.split("\n")
    for i, c in enumerate(tekst):
        if ord(c) < 128:
            continue
        if c in Z.DOZWOLONE:
            continue
        przed = dict(licznik)
        zamiana = Z.zamien_znak(c, licznik, kod=True)
        kategoria = next((k for k in licznik if licznik[k] != przed[k]), "inne")
        w_kodzie = (chronione is None) or (i not in chronione)
        nr = nr_linii(i)
        wynik["znaleziska"].append({
            "linia": nr,
            "kolumna": i - starty[nr - 1] + 1,
            "znak": "U+%04X" % ord(c),
            "nazwa": unicodedata.name(c, "?"),
            "kategoria": kategoria,
            "gdzie": "KOD" if w_kodzie else "dane (literal/komentarz)",
            "naprawa": ("USUNIECIE" if zamiana is None else repr(zamiana)),
            "naprawialny": zamiana is not None,
            "kontekst": linie[nr - 1].strip()[:70],
        })
        if zamiana is None:
            wynik["nienaprawialne"] += 1

    for z in wynik["znaleziska"]:
        k = z["kategoria"]
        wynik["podsumowanie"][k] = wynik["podsumowanie"].get(k, 0) + 1

    if ext == "py":
        try:
            compile(tekst, sciezka, "exec")
            wynik["kompiluje_przed"] = True
        except Exception as e:
            wynik["kompiluje_przed"] = False
            wynik["blad_kompilacji"] = "%s: %s" % (type(e).__name__, e)
        po = symuluj(tekst, ext)
        try:
            compile(po, sciezka, "exec")
            wynik["kompiluje_po"] = True
        except Exception as e:
            wynik["kompiluje_po"] = False
            wynik["blad_kompilacji_po"] = "%s: %s" % (type(e).__name__, e)
    return wynik


def symuluj(tekst, ext):
    """Tresc pliku PO naprawie - wyliczona w pamieci, nic nie zapisuje."""
    Z = _zaladuj("ZagladaKultury.py")
    if ext == "py":
        try:
            nowy, _ = Z.zaglada_tekst_poza_literalami(tekst)
            return nowy
        except Exception:
            pass
    if ext in JEZYKI_KODU:
        try:
            A = _zaladuj("AnihilatorChwastow.py")
            nowy, _ = A.zaglada_tekst_poza_literalami_multi(tekst, ext)
            return nowy
        except Exception:
            pass
    try:
        nowy, _ = Z.zaglada_tekst(tekst, kod=(ext in ("json", "jsonl")))
        return nowy
    except Exception:
        return tekst


def podglad(sciezka):
    """Roznica przed/po, linia po linii. Nic nie zapisuje."""
    try:
        tekst = io.open(sciezka, encoding="utf-8").read()
    except Exception as e:
        print("[BLAD] %s: %s" % (sciezka, e))
        return 1
    ext = sciezka.rsplit(".", 1)[-1].lower() if "." in sciezka else ""
    po = symuluj(tekst, ext)
    if po == tekst:
        print("%s: naprawa niczego by nie zmienila" % sciezka)
        return 0
    a, b = tekst.split("\n"), po.split("\n")
    print("PODGLAD NAPRAWY: %s   (NIC NIE ZAPISANO)" % sciezka)
    print("-" * 68)
    zmian = 0
    for i, (x, y) in enumerate(zip(a, b), 1):
        if x != y:
            zmian += 1
            print("  linia %d" % i)
            print("    - %s" % x.strip()[:66])
            print("    + %s" % y.strip()[:66])
    if len(a) != len(b):
        print("  UWAGA: zmienia sie liczba linii %d -> %d" % (len(a), len(b)))
    print("-" * 68)
    print("Zmienionych linii: %d" % zmian)
    return 0


def raport(w):
    print("=" * 70)
    print("ZWIAD: %s" % w["plik"])
    print("=" * 70)
    if not w["czytelny"]:
        print("  [NIECZYTELNY] %s" % w.get("blad", "?"))
        print("  Decyzja: NIE URUCHAMIAJ naprawy - narzedzie nie widzi tresci.")
        return
    if not w["znaleziska"]:
        print("  CZYSTO - zero skazen.")
        return

    w_kodzie = [z for z in w["znaleziska"] if z["gdzie"] == "KOD"]
    w_danych = [z for z in w["znaleziska"] if z["gdzie"] != "KOD"]

    print("  Znalezisk: %d   (w KODZIE: %d | w danych: %d)"
          % (len(w["znaleziska"]), len(w_kodzie), len(w_danych)))
    print("  Kategorie: %s" % ", ".join("%s %d" % (k, v)
                                        for k, v in sorted(w["podsumowanie"].items())))
    if w["nienaprawialne"]:
        print("  NIENAPRAWIALNE (zostana USUNIETE): %d" % w["nienaprawialne"])
    if w["kompiluje_przed"] is not None:
        print("  Kompiluje sie teraz: %s | po naprawie: %s"
              % ("TAK" if w["kompiluje_przed"] else "NIE",
                 "TAK" if w["kompiluje_po"] else "NIE"))
    print()

    for etykieta, grupa in (("W KODZIE (zmieni dzialanie programu)", w_kodzie),
                            ("W DANYCH (literaly, komentarze)", w_danych)):
        if not grupa:
            continue
        print("  -- %s --" % etykieta)
        for z in grupa:
            print("     %d:%d  %s %s  ->  %s"
                  % (z["linia"], z["kolumna"], z["znak"], z["kategoria"],
                     z["naprawa"]))
            print("          %s" % z["kontekst"])
        print()

    print("  CO DALEJ (decyzja nalezy do ciebie, operatorze):")
    print("    1. zrob kopie pliku ZANIM cokolwiek uruchomisz")
    print("    2. podejrzyj naprawe:  python3 zwiad.py --podglad %s" % w["plik"])
    if w["kompiluje_przed"] and w["kompiluje_po"] is False:
        print("    3. UWAGA: po naprawie plik przestanie sie kompilowac -")
        print("       NIE uruchamiaj naprawy, zglos to operatorowi-czlowiekowi")
    elif w["nienaprawialne"]:
        print("    3. czesc znakow zostanie USUNIETA bezpowrotnie - sprawdz")
        print("       podgladem, czy to nie jest tresc potrzebna uzytkownikowi")
    else:
        print("    3. naprawa wyglada bezpiecznie")


def selftest():
    import tempfile
    ok = True
    d = tempfile.mkdtemp(prefix="zwiad-")
    C = "\u043e"
    p = os.path.join(d, "t.py")
    io.open(p, "w", encoding="utf-8").write(
        '# k%smentarz\nv%s = 1\ns = "M%sskwa"\nprint(v%s)\n' % (C, C, C, C))
    w = zbadaj(p)
    if len(w["znaleziska"]) != 4:
        print("  [FAIL] liczba znalezisk: %d zamiast 4" % len(w["znaleziska"]))
        ok = False
    kod = [z for z in w["znaleziska"] if z["gdzie"] == "KOD"]
    dane = [z for z in w["znaleziska"] if z["gdzie"] != "KOD"]
    if len(kod) != 2 or len(dane) != 2:
        print("  [FAIL] rozdzial kod/dane: %d/%d zamiast 2/2" % (len(kod), len(dane)))
        ok = False
    if any(z["naprawa"] != "'o'" for z in w["znaleziska"]):
        print("  [FAIL] zla przewidywana naprawa")
        ok = False
    if not (w["kompiluje_przed"] and w["kompiluje_po"]):
        print("  [FAIL] ocena kompilacji")
        ok = False

    # znak nienaprawialny (CJK) musi byc oznaczony
    p2 = os.path.join(d, "u.txt")
    io.open(p2, "w", encoding="utf-8").write("tekst \u4e2d\u6587\n")
    w2 = zbadaj(p2)
    if w2["nienaprawialne"] != 2:
        print("  [FAIL] nie oznaczyl znakow nienaprawialnych: %d"
              % w2["nienaprawialne"])
        ok = False

    # plik nie-UTF8 nie moze wywrocic narzedzia
    p3 = os.path.join(d, "b.py")
    io.open(p3, "wb").write(b'x = "kawa\xe9"\n')
    w3 = zbadaj(p3)
    if w3["czytelny"]:
        print("  [FAIL] uznal plik nie-UTF8 za czytelny")
        ok = False

    # ZWIAD NIE MOZE NICZEGO ZAPISAC
    przed = io.open(p, encoding="utf-8").read()
    zbadaj(p); symuluj(przed, "py")
    if io.open(p, encoding="utf-8").read() != przed:
        print("  [FAIL] ZWIAD ZMIENIL PLIK - to zlamanie kontraktu")
        ok = False

    import shutil
    shutil.rmtree(d, ignore_errors=True)
    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--help" in args or "-h" in args or not args:
        print(__doc__)
        return 0
    if "--podglad" in args:
        cele = [a for a in args if not a.startswith("--")]
        for c in cele:
            podglad(c)
        return 0
    tryb_json = "--json" in args
    cele = [a for a in args if not a.startswith("--")]
    wyniki = [zbadaj(c) for c in cele]
    if tryb_json:
        print(json.dumps(wyniki, ensure_ascii=False, indent=2))
    else:
        for w in wyniki:
            raport(w)
            print()
    if any(w["nienaprawialne"] for w in wyniki):
        return 2
    return 1 if any(w["znaleziska"] for w in wyniki) else 0


if __name__ == "__main__":
    sys.exit(main())

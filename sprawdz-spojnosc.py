# -*- coding: utf-8 -*-
"""sprawdz-spojnosc.py - pilnuje, zeby dokumentacja nie klamala o wersjach.

Jedno zrodlo prawdy: WERSJE.json. Ten skrypt sprawdza trzy rzeczy:

  1. czy stala WERSJA w kodzie narzedzia zgadza sie z WERSJE.json
  2. czy warstwa czytana przez agenta (README.md, PROTOKOL-OPERATORA.md,
     SZYBKI-START-DLA-AGENTA.md, docs/czlowiek/RODZINA-DO-CZATU.md, docs/wniosek...)
     nie DEKLARUJE numeru wersji sprzecznego z WERSJE.json
  3. czy kopie kodu osadzone w docs/czlowiek/RODZINA-DO-CZATU.md sa identyczne
     bajt-w-bajt z realnymi plikami narzedzi

Nie sprawdza dev/ - to amunicja testowa, celowo brudna i poza bramka.

DLACZEGO NIE "KAZDY NUMER W PLIKU":
Pierwsza wersja tego skryptu (od autora) porownywala KAZDY numer pasujacy
do \\d+\\.\\d+\\.\\d+ w warstwie agenta z lista dozwolonych. Na tym repo dalo
to ~40 falszywych rozjazdow, bo README.md zawiera HISTORIE ZMIAN, ktora z
definicji mowi o starych wersjach ("v8.2.14 - Zaglada v1.0.8: naprawa...").
Zabicie historii zmian, zeby uciszyc walidator, byloby lekiem gorszym od
choroby - to jest najcenniejsza czesc tego repo.

Dlatego sprawdzamy DEKLARACJE, nie wzmianki: numer wersji stojacy przy
NAZWIE NARZEDZIA (np. "PogromcaKwiatkow.py v8.4.0" albo "Pogromca v8.4.0"),
z pominieciem linii oznaczonych jako historyczne (naglowek wpisu changelogu,
"patrz README Historia zmian", "(vX.Y.Z)" jako adnotacja w kodzie/komentarzu).
Wzmianka o starej wersji W OPISIE zmiany jest legalna. Zla deklaracja
"to narzedzie jest w wersji X", gdy naprawde jest Y - nie jest.

Uzycie:
    python3 sprawdz-spojnosc.py

Exit 0 = spojne. Exit 1 = rozjazd (wypisany co do pliku i linii).
"""
import json
import os
import re
import sys

TU = os.path.dirname(os.path.abspath(__file__))

# pliki, ktore czyta agent - tylko one musza byc zgodne z WERSJE.json
WARSTWA_AGENTA = (
    "README.md",
    "PROTOKOL-OPERATORA.md",
    "SZYBKI-START-DLA-AGENTA.md",
    os.path.join("docs", "czlowiek", "RODZINA-DO-CZATU.md"),
    os.path.join("docs", "czlowiek", "wniosek_publiczny_do_redakcji.md"),
    os.path.join("docs", "dowody", "README-TURNIEJ.md"),
    # (v1.1.0) BRIEF trafia do ZEWNETRZNEGO audytora - klamstwo o wersji
    # w tym pliku jest grozniejsze niz w dokumentacji wewnetrznej, bo
    # obcy agent nie ma jak go zweryfikowac. Zmierzone: brief deklarowal
    # Prokuratora 1.3.0, gdy w kodzie bylo juz 1.3.1.
    os.path.join("docs", "agent", "BRIEF-DLA-AUDYTORA.md"),
    # CZYM-JEST-GANG to pierwszy plik, ktory czyta agent przed praca
    "CZYM-JEST-GANG.md",
)

# stala w kodzie: WERSJA = "1.1.1"
WZOR_STALEJ = re.compile(r'^WERSJA\s*=\s*["\']([^"\']+)["\']', re.M)

# krotkie nazwy uzywane w prozie ("Pogromca v8.4.0", "Zagłada v1.3.0")
ALIASY = {
    "PogromcaKwiatkow.py": ("PogromcaKwiatkow.py", "PogromcaKwiatkow", "Pogromca"),
    "ZagladaKultury.py": ("ZagladaKultury.py", "ZagladaKultury", "Zaglada", "Zagłada"),
    "ProkuratorOgrodnik.py": ("ProkuratorOgrodnik.py", "ProkuratorOgrodnik", "Prokurator"),
    "AnihilatorChwastow.py": ("AnihilatorChwastow.py", "AnihilatorChwastow", "Anihilator"),
}

# linie, ktore z definicji mowia o przeszlosci - nie sa deklaracja stanu
WYJATKI_HISTORYCZNE = (
    "historia zmian",
    "patrz readme",
    "zostaje w historii",
    "stan historyczny",
    "superseded",
    "supersedowany",
    "poprzednio",
    "wczesniej",
    "do v",
    "od v",
    "przed v",
    "poprzednia aktualizacja",
    "zapis historyczny",
)

# naglowek wpisu changelogu: "- v8.2.14 - opis..." / "* v1.0.9 ..."
WZOR_CHANGELOG = re.compile(r"^\s*[-*]\s*v?\d+\.\d+\.\d+\s*[-–—:]")

# strzalka wersji ("v1.1.1 -> v1.3.0", "v8.2.0-v8.4.0") = opis PRZEJSCIA,
# a nie deklaracja stanu. Zawsze wystepuje w changelogu.
WZOR_PRZEJSCIA = re.compile(r"v?\d+\.\d+\.\d+\s*(?:->|→|-|–|/)\s*v?\d+\.\d+\.\d+")

# linia wewnatrz osadzonego kodu (komentarz #, print(...), dokstring z (vX)).
# RODZINA-DO-CZATU zawiera pelne zrodla narzedzi - napis w print() nie jest
# deklaracja wersji narzedzia, tylko trescia literalu, ktorej NIE WOLNO ruszac
# (kontrakt: literal swiety). Zgodnosc tych kopii pilnuje sprawdz_embedy().
WZOR_W_KODZIE = re.compile(r'^\s*(#|print\(|"""|\'\'\'|WERSJA\s*=)')


def wczytaj_prawde():
    sciezka = os.path.join(TU, "WERSJE.json")
    if not os.path.isfile(sciezka):
        print("BLAD: brak WERSJE.json - nie ma z czym porownywac")
        sys.exit(1)
    # (v1.1.0) Uszkodzony JSON to nie powod do tracebacka. Bramka ma
    # powiedziec CO jest zle i odmowic - stos wywolan Pythona nie mowi
    # operatorowi nic uzytecznego, a wyglada jak awaria narzedzia zamiast
    # jak wykryty problem w repo.
    try:
        with open(sciezka, encoding="utf-8") as f:
            prawda = json.load(f)
    except json.JSONDecodeError as e:
        print("BLAD: WERSJE.json nie jest poprawnym JSON-em (linia %d, kolumna %d): %s"
              % (e.lineno, e.colno, e.msg))
        print("Napraw plik albo przywroc go z gita: git checkout -- WERSJE.json")
        sys.exit(2)
    except OSError as e:
        print("BLAD: nie da sie odczytac WERSJE.json: %s" % e)
        sys.exit(2)
    for wymagane in ("repo", "narzedzia"):
        if wymagane not in prawda:
            print("BLAD: WERSJE.json nie ma pola %r - nie ma z czym porownywac"
                  % wymagane)
            sys.exit(2)
    return prawda


def sprawdz_kod(prawda):
    """Czy stala WERSJA w pliku .py zgadza sie z WERSJE.json."""
    rozjazdy = []
    for nazwa, dane in prawda["narzedzia"].items():
        sciezka = os.path.join(TU, nazwa)
        if not os.path.isfile(sciezka):
            rozjazdy.append("%s: brak pliku, a jest w WERSJE.json" % nazwa)
            continue
        with open(sciezka, encoding="utf-8") as f:
            tresc = f.read()
        trafienie = WZOR_STALEJ.search(tresc)
        if trafienie is None:
            # brak stalej to znany problem, nie rozjazd - byle byl opisany
            if not dane.get("znany_problem"):
                rozjazdy.append(
                    "%s: brak stalej WERSJA i brak opisu w WERSJE.json" % nazwa)
            continue
        if trafienie.group(1) != dane["wersja"]:
            rozjazdy.append("%s: kod mowi %s, WERSJE.json mowi %s"
                            % (nazwa, trafienie.group(1), dane["wersja"]))
    return rozjazdy


def _linia_historyczna(linia):
    niska = linia.lower()
    if WZOR_CHANGELOG.match(linia):
        return True
    if WZOR_PRZEJSCIA.search(linia):
        return True
    if WZOR_W_KODZIE.match(linia):
        return True
    return any(w in niska for w in WYJATKI_HISTORYCZNE)


def sprawdz_dokumentacje(prawda):
    """Czy warstwa agenta nie DEKLARUJE wersji sprzecznej z WERSJE.json.

    Szukamy wzorca "<nazwa narzedzia> vX.Y.Z" - czyli zdania, ktore mowi
    "to narzedzie jest w tej wersji". Wzmianki historyczne pomijamy
    (patrz dokstring: historia zmian ma prawo mowic o starych wersjach)."""
    rozjazdy = []
    wzorce = []
    for plik, dane in prawda["narzedzia"].items():
        for alias in ALIASY.get(plik, (plik,)):
            wzorce.append((
                re.compile(r"\b%s\b[^\n]{0,40}?\bv?(\d+\.\d+\.\d+)\b"
                           % re.escape(alias)),
                plik, dane["wersja"]))
    for nazwa in WARSTWA_AGENTA:
        sciezka = os.path.join(TU, nazwa)
        if not os.path.isfile(sciezka):
            rozjazdy.append("%s: brak pliku warstwy agenta" % nazwa)
            continue
        # Wpis changelogu jest WIELOLINIJKOWY: naglowek "- v8.3.0 - ..." a
        # potem wciete kontynuacje, ktore tak samo opisuja przeszlosc.
        # Sprawdzanie linia-po-linii bez pamieci o bloku dawalo falszywe
        # alarmy na kontynuacjach (5 sztuk na tym repo). Blok trwa do
        # nastepnego wpisu, pustej linii bez wciecia albo naglowka sekcji.
        w_changelogu = False
        with open(sciezka, encoding="utf-8") as f:
            for nr, linia in enumerate(f, 1):
                if WZOR_CHANGELOG.match(linia):
                    w_changelogu = True
                    continue
                if w_changelogu:
                    goly = linia.rstrip("\n")
                    if goly.startswith("#") or (goly and not goly[0].isspace()):
                        w_changelogu = False   # koniec bloku
                    else:
                        continue               # kontynuacja wpisu
                if _linia_historyczna(linia):
                    continue
                for wzor, plik, oczekiwana in wzorce:
                    trafienie = wzor.search(linia)
                    if trafienie and trafienie.group(1) != oczekiwana:
                        rozjazdy.append(
                            "%s linia %d: deklaruje %s w wersji %s, "
                            "a WERSJE.json mowi %s"
                            % (nazwa, nr, plik, trafienie.group(1), oczekiwana))
                        break
    return rozjazdy


def sprawdz_embedy(prawda):
    """Czy kopie osadzone w RODZINA-DO-CZATU sa identyczne z realnymi plikami.

    To jest najczesciej lamana spojnosc w tym repo (dwa razy pod rzad):
    kod narzedzia zmienia sie, a all-in-one dla agenta zostaje ze starym.
    Agent dostaje wtedy INNE narzedzie niz to, ktore lezy w repo."""
    rozjazdy = []
    sciezka = os.path.join(TU, "docs", "czlowiek", "RODZINA-DO-CZATU.md")
    if not os.path.isfile(sciezka):
        return ["docs/czlowiek/RODZINA-DO-CZATU.md: brak pliku (all-in-one dla agenta)"]
    with open(sciezka, encoding="utf-8") as f:
        linie = f.readlines()
    markery = [(i, l.strip()[4:]) for i, l in enumerate(linie)
               if l.startswith("### ") and l.strip().endswith(".py")]
    znalezione = set()
    for k, (i, nazwa) in enumerate(markery):
        koniec = markery[k + 1][0] if k + 1 < len(markery) else len(linie)
        osadzony = "".join(linie[i + 1:koniec]).strip()
        realny_plik = os.path.join(TU, nazwa)
        if not os.path.isfile(realny_plik):
            rozjazdy.append("RODZINA osadza %s, ale takiego pliku nie ma" % nazwa)
            continue
        znalezione.add(nazwa)
        with open(realny_plik, encoding="utf-8") as f:
            realny = f.read().strip()
        if osadzony != realny:
            rozjazdy.append(
                "RODZINA-DO-CZATU: osadzona kopia %s ROZJECHANA z realnym "
                "plikiem (%d B vs %d B) - agent dostalby inny kod"
                % (nazwa, len(osadzony), len(realny)))
    for nazwa in prawda["narzedzia"]:
        if nazwa not in znalezione:
            rozjazdy.append(
                "RODZINA-DO-CZATU nie osadza %s - agent nie dostanie tego "
                "narzedzia" % nazwa)
    return rozjazdy


def main():
    prawda = wczytaj_prawde()
    rozjazdy = (sprawdz_kod(prawda)
                + sprawdz_dokumentacje(prawda)
                + sprawdz_embedy(prawda))

    print("SPOJNOSC WERSJI (zrodlo prawdy: WERSJE.json, repo %s)" % prawda["repo"])
    for nazwa, dane in prawda["narzedzia"].items():
        znak = (" (znany problem: %s)" % dane["znany_problem"]
                if dane.get("znany_problem") else "")
        print("  %-24s %s%s" % (nazwa, dane["wersja"], znak))
    print()

    if rozjazdy:
        print("ROZJAZDY: %d" % len(rozjazdy))
        for r in rozjazdy:
            print("  [ROZJAZD] %s" % r)
        return 1
    print("ROZJAZDY: 0 - kod, dokumentacja i osadzone kopie zgodne")
    return 0


if __name__ == "__main__":
    sys.exit(main())

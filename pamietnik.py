#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PAMIETNIK OPERATORA - dopisywanie i sprawdzanie wpisow.

Po co osobne narzedzie, skoro to zwykly markdown? Bo pamietnik jest
uzyteczny tylko dopoki ma jeden format. Recznie dopisywane wpisy rozjezdzaja
sie po trzech sesjach i plik staje sie smietnikiem, ktorego nikt nie czyta.

Uzycie:
    python3 pamietnik.py                 # ostatnie wpisy (domyslnie 5)
    python3 pamietnik.py --lista         # spis wszystkich wpisow
    python3 pamietnik.py --sekcje        # dostepne sekcje z numerami
    python3 pamietnik.py --szukaj SLOWO  # przeszukaj tresc wpisow
    python3 pamietnik.py --dodaj         # dopisz wpis (pyta interaktywnie)
    python3 pamietnik.py --sprawdz       # walidacja formatu (do CI)
    python3 pamietnik.py --selftest      # test wlasny

Dopisywanie nieinteraktywne (dla agenta w skrypcie):
    python3 pamietnik.py --dodaj --sekcja 3 \\
        --tytul "Cos sie zepsulo" \\
        --objaw "Co widac" --przyczyna "Dlaczego" --wniosek "Co robic"
"""

import io
import os
import re
import sys
from datetime import date

WERSJA = "1.0.0"

KORZEN = os.path.dirname(os.path.abspath(__file__))
PAMIETNIK = os.path.join(KORZEN, "PAMIETNIK-OPERATORA.md")

WZOR_SEKCJI = re.compile(r"^## (\d+)\. (.+)$")
WZOR_WPISU = re.compile(r"^### \[(\d{4}-\d{2}-\d{2})\] (.+)$")
POLA = ("Objaw", "Przyczyna", "Wniosek")


# --------------------------------------------------------------- odczyt
def wczytaj(sciezka=None):
    sciezka = sciezka or PAMIETNIK
    if not os.path.exists(sciezka):
        raise SystemExit("[BLAD] brak pliku %s" % sciezka)
    return io.open(sciezka, encoding="utf-8").read()


def sekcje(tekst):
    """[(numer, tytul, indeks_linii)]"""
    wynik = []
    for i, linia in enumerate(tekst.split("\n")):
        m = WZOR_SEKCJI.match(linia)
        if m:
            wynik.append((int(m.group(1)), m.group(2), i))
    return wynik


def wpisy(tekst):
    """[(data, tytul, sekcja, tresc)] w kolejnosci wystepowania."""
    linie = tekst.split("\n")
    granice = sekcje(tekst)
    wynik = []
    biezaca = "(bez sekcji)"
    for i, linia in enumerate(linie):
        m_sek = WZOR_SEKCJI.match(linia)
        if m_sek:
            biezaca = "%d. %s" % (int(m_sek.group(1)), m_sek.group(2))
            continue
        m = WZOR_WPISU.match(linia)
        if not m:
            continue
        tresc = []
        for j in range(i + 1, len(linie)):
            if WZOR_WPISU.match(linie[j]) or WZOR_SEKCJI.match(linie[j]):
                break
            tresc.append(linie[j])
        wynik.append((m.group(1), m.group(2), biezaca, "\n".join(tresc).strip()))
    return wynik


# --------------------------------------------------------------- widoki
def pokaz_ostatnie(n=5):
    w = wpisy(wczytaj())
    if not w:
        print("Pamietnik jest pusty.")
        return 0
    print("PAMIETNIK OPERATORA - %d wpisow, ostatnie %d:\n"
          % (len(w), min(n, len(w))))
    for data, tytul, sekcja, tresc in w[-n:]:
        print("  [%s] %s" % (data, tytul))
        print("      sekcja: %s" % sekcja)
        for linia in tresc.split("\n"):
            if linia.strip():
                print("      %s" % linia.strip()[:96])
        print()
    return 0


def pokaz_liste():
    w = wpisy(wczytaj())
    print("PAMIETNIK OPERATORA - %d wpisow\n" % len(w))
    biezaca = None
    for data, tytul, sekcja, _ in w:
        if sekcja != biezaca:
            print("  %s" % sekcja)
            biezaca = sekcja
        print("     [%s] %s" % (data, tytul))
    return 0


def pokaz_sekcje():
    for numer, tytul, _ in sekcje(wczytaj()):
        print("  %d. %s" % (numer, tytul))
    return 0


def szukaj(fraza):
    f = fraza.lower()
    trafienia = [x for x in wpisy(wczytaj())
                 if f in x[1].lower() or f in x[3].lower()]
    if not trafienia:
        print("Brak wpisow zawierajacych %r." % fraza)
        return 1
    print("Znaleziono %d wpisow dla %r:\n" % (len(trafienia), fraza))
    for data, tytul, sekcja, tresc in trafienia:
        print("  [%s] %s   (%s)" % (data, tytul, sekcja))
        for linia in tresc.split("\n"):
            if f in linia.lower():
                print("      ...%s" % linia.strip()[:96])
        print()
    return 0


# --------------------------------------------------------------- zapis
def zbuduj_wpis(tytul, objaw, przyczyna, wniosek, dzien=None):
    dzien = dzien or date.today().isoformat()
    return ("### [%s] %s\n"
            "**Objaw:** %s\n"
            "**Przyczyna:** %s\n"
            "**Wniosek:** %s\n" % (dzien, tytul, objaw, przyczyna, wniosek))


def dodaj(nr_sekcji, tytul, objaw, przyczyna, wniosek, sciezka=None):
    """Wstawia wpis na KONCU wskazanej sekcji (chronologicznie)."""
    sciezka = sciezka or PAMIETNIK
    tekst = wczytaj(sciezka)
    linie = tekst.split("\n")
    lista = sekcje(tekst)
    numery = [s[0] for s in lista]
    if nr_sekcji not in numery:
        raise SystemExit("[BLAD] nie ma sekcji %d. Dostepne: %s"
                         % (nr_sekcji, ", ".join(str(n) for n in numery)))
    idx = numery.index(nr_sekcji)
    poczatek = lista[idx][2]
    koniec = lista[idx + 1][2] if idx + 1 < len(lista) else len(linie)
    # cofnij sie przed puste linie konczace sekcje
    wstaw = koniec
    while wstaw > poczatek and not linie[wstaw - 1].strip():
        wstaw -= 1
    nowy = zbuduj_wpis(tytul, objaw, przyczyna, wniosek).split("\n")
    linie[wstaw:wstaw] = [""] + nowy[:-1]
    io.open(sciezka, "w", encoding="utf-8").write("\n".join(linie))
    return True


def dodaj_interaktywnie():
    tekst = wczytaj()
    print("Dostepne sekcje:")
    for numer, tytul, _ in sekcje(tekst):
        print("   %d. %s" % (numer, tytul))
    try:
        nr = int(input("\nNumer sekcji: ").strip())
        tytul = input("Tytul (krotko, czego dotyczy): ").strip()
        objaw = input("Objaw (co zobaczyles - konkretnie): ").strip()
        przyczyna = input("Przyczyna (dlaczego tak bylo): ").strip()
        wniosek = input("Wniosek (co robic nastepnym razem): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n[ANULOWANO]")
        return 1
    if not all([tytul, objaw, przyczyna, wniosek]):
        print("[BLAD] wszystkie pola sa wymagane - wpis bez ktoregos z nich "
              "jest bezuzyteczny dla nastepnego agenta")
        return 1
    dodaj(nr, tytul, objaw, przyczyna, wniosek)
    print("\n[OK] Wpis dopisany do sekcji %d. Sprawdz: git diff %s"
          % (nr, os.path.basename(PAMIETNIK)))
    return 0


# --------------------------------------------------------------- kontrola
def sprawdz(sciezka=None, cicho=False):
    """Walidacja formatu. Zwraca liczbe problemow."""
    tekst = wczytaj(sciezka)
    problemy = []
    w = wpisy(tekst)
    if not w:
        problemy.append("pamietnik nie zawiera zadnego wpisu")
    for data, tytul, sekcja, tresc in w:
        for pole in POLA:
            if ("**%s:**" % pole) not in tresc:
                problemy.append("wpis [%s] %s - brakuje pola **%s:**"
                                % (data, tytul[:40], pole))
        if len(tytul) < 8:
            problemy.append("wpis [%s] - tytul za krotki, nic nie mowi" % data)
        try:
            r, m, d = (int(x) for x in data.split("-"))
            date(r, m, d)
        except ValueError:
            problemy.append("wpis %r - niepoprawna data" % tytul[:40])
    if not cicho:
        if problemy:
            print("PAMIETNIK: %d problemow" % len(problemy))
            for p in problemy:
                print("  [BLAD] %s" % p)
        else:
            print("PAMIETNIK: %d wpisow w %d sekcjach - format poprawny"
                  % (len(w), len(sekcje(tekst))))
    return len(problemy)


def selftest():
    import tempfile
    ok = True
    prob = os.path.join(tempfile.mkdtemp(prefix="pam-"), "P.md")
    io.open(prob, "w", encoding="utf-8").write(
        "# Naglowek\n\n## 1. Pierwsza\n\n### [2026-01-01] Wpis pierwszy testowy\n"
        "**Objaw:** a\n**Przyczyna:** b\n**Wniosek:** c\n\n"
        "## 2. Druga\n\n### [2026-01-02] Wpis drugi testowy\n"
        "**Objaw:** d\n**Przyczyna:** e\n**Wniosek:** f\n")

    t = wczytaj(prob)
    if len(sekcje(t)) != 2:
        print("  [FAIL] wykrywanie sekcji"); ok = False
    if len(wpisy(t)) != 2:
        print("  [FAIL] wykrywanie wpisow"); ok = False
    if sprawdz(prob, cicho=True) != 0:
        print("  [FAIL] walidacja poprawnego pliku"); ok = False

    # dopisanie do sekcji 1 nie moze wpasc do sekcji 2
    dodaj(1, "Wpis dopisany przez test", "x", "y", "z", sciezka=prob)
    w = wpisy(wczytaj(prob))
    if len(w) != 3:
        print("  [FAIL] dopisywanie wpisu"); ok = False
    elif not w[1][2].startswith("1."):
        print("  [FAIL] wpis trafil do zlej sekcji: %s" % w[1][2]); ok = False
    if sprawdz(prob, cicho=True) != 0:
        print("  [FAIL] plik po dopisaniu nie przechodzi walidacji"); ok = False

    # brak pola musi byc wykryty
    io.open(prob, "a", encoding="utf-8").write(
        "\n### [2026-01-03] Wpis niekompletny testowy\n**Objaw:** tylko to\n")
    if sprawdz(prob, cicho=True) == 0:
        print("  [FAIL] nie wykryl braku pol"); ok = False

    # prawdziwy pamietnik repo tez musi byc poprawny
    if os.path.exists(PAMIETNIK) and sprawdz(PAMIETNIK, cicho=True) != 0:
        print("  [FAIL] PAMIETNIK-OPERATORA.md ma bledy formatu"); ok = False

    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--sprawdz" in args:
        return 1 if sprawdz() else 0
    if "--sekcje" in args:
        return pokaz_sekcje()
    if "--lista" in args:
        return pokaz_liste()
    if "--szukaj" in args:
        i = args.index("--szukaj")
        if i + 1 >= len(args):
            print("[BLAD] --szukaj wymaga slowa")
            return 1
        return szukaj(args[i + 1])
    if "--dodaj" in args:
        def opcja(nazwa):
            return args[args.index(nazwa) + 1] if nazwa in args else None
        tytul = opcja("--tytul")
        if tytul:
            sek = opcja("--sekcja")
            dodaj(int(sek) if sek else 1, tytul, opcja("--objaw") or "",
                  opcja("--przyczyna") or "", opcja("--wniosek") or "")
            print("[OK] wpis dopisany")
            return 0
        return dodaj_interaktywnie()
    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0
    return pokaz_ostatnie()


if __name__ == "__main__":
    sys.exit(main())

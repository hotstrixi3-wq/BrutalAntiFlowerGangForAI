#!/usr/bin/env python3
"""SUMA-KONTROLNA-TESTOW.py — mechanizm zloty-plik dla testow Gangu.

Idea (rozkaz usera, 2026-09-03): kazdy test w korpusie ma trzy sumy
kontrolne zapisane w manifescie:
  - sha_wejscie:  suma pliku BRUDNEGO przed czyszczeniem (wykrywa czy
                  ktos przypadkiem zmienil fixture testowy)
  - sha_wyjscie:  suma WYNIKU czyszczenia, zweryfikowanego RECZNIE
                  (uruchomieniem, nie tylko compile()) w momencie
                  zapisu do manifestu — to jest "zloty plik"
  - sha_zrodlo:   suma ZagladaKultury.py, ktory wyprodukowal zloty wynik
                  (jesli sie zmieni, trzeba recznie zweryfikowac zloty
                  wynik od nowa, nie ufac starej sumie)

Uzycie:
  python3 SUMA-KONTROLNA-TESTOW.py zapisz KATALOG_BRUDNYCH ZAGLADA.py MANIFEST.json
      -> generuje manifest z aktualnym stanem jako "zloty" (WYMAGA recznej
         weryfikacji PRZED zapisem - patrz ostrzezenie w kodzie)

  python3 SUMA-KONTROLNA-TESTOW.py sprawdz KATALOG_BRUDNYCH ZAGLADA.py MANIFEST.json
      -> szybkie porownanie sum, bez ponownego czytania/rozumienia
         kazdego pliku. W-TERMINIE / ROZJAZD na kazdy wpis.

WAZNE (uczciwie, jak w calej tej sesji): tryb "zapisz" NIE weryfikuje
poprawnosci wyniku semantycznie - tylko go zamraza jako punkt odniesienia.
Zanim uruchomisz "zapisz", MUSISZ recznie/programowo sprawdzic, ze wynik
jest naprawde poprawny (compile() + jesli to ma sens, faktyczne
uruchomienie) - inaczej suma kontrolna bedzie pilnowac zlego stanu
rownie skrupulatnie jak dobrego (dokladnie ryzyko nazwane w rozmowie
2026-09-03: "suma kontrolna nie odroznia poprawnej zmiany od bledu,
tak samo jak nie odroznial tego compile()").
"""
import hashlib
import json
import sys
import os
import importlib.util


def sha(sciezka):
    with open(sciezka, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def zaladuj_zagladę(sciezka_zaglady):
    spec = importlib.util.spec_from_file_location("zk", sciezka_zaglady)
    zk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(zk)
    return zk


def zapisz(katalog_brudnych, sciezka_zaglady, sciezka_manifestu):
    zk = zaladuj_zagladę(sciezka_zaglady)
    sha_zrodlo = sha(sciezka_zaglady)
    manifest = {"sha_zrodlo_zaglady": sha_zrodlo, "wpisy": {}}
    for nazwa in sorted(os.listdir(katalog_brudnych)):
        if not nazwa.endswith(".py"):
            continue
        sciezka = os.path.join(katalog_brudnych, nazwa)
        with open(sciezka, encoding="utf-8") as f:
            tekst = f.read()
        sha_wejscie = sha(sciezka)
        wynik, licznik = zk.przetworz(tekst, sciezka)
        try:
            compile(wynik, sciezka, "exec")
            kompiluje = True
        except SyntaxError:
            kompiluje = False
        sha_wyjscie = hashlib.sha256(wynik.encode("utf-8")).hexdigest()
        manifest["wpisy"][nazwa] = {
            "sha_wejscie": sha_wejscie,
            "sha_wyjscie": sha_wyjscie,
            "kompiluje_sie": kompiluje,
        }
    with open(sciezka_manifestu, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Zapisano {len(manifest['wpisy'])} wpisow do {sciezka_manifestu}")
    print("UWAGA: to NIE jest weryfikacja poprawnosci — to zamrozenie")
    print("aktualnego stanu jako punktu odniesienia. Sprawdz go recznie")
    print("zanim zaczniesz mu ufac (patrz docstring pliku).")


def sprawdz(katalog_brudnych, sciezka_zaglady, sciezka_manifestu):
    zk = zaladuj_zagladę(sciezka_zaglady)
    with open(sciezka_manifestu, encoding="utf-8") as f:
        manifest = json.load(f)
    sha_zrodlo_teraz = sha(sciezka_zaglady)
    if sha_zrodlo_teraz != manifest["sha_zrodlo_zaglady"]:
        print("OSTRZEZENIE: ZagladaKultury.py zmienil sie od zapisania")
        print("manifestu — stare 'zlote' wyniki NIE SA juz gwarantowane")
        print("poprawne. Zweryfikuj recznie i zapisz nowy manifest.")
        print()
    w_terminie = 0
    rozjazd = 0
    brak_wejscia = 0
    for nazwa, wpis in manifest["wpisy"].items():
        sciezka = os.path.join(katalog_brudnych, nazwa)
        if not os.path.exists(sciezka):
            print(f"BRAK PLIKU WEJSCIOWEGO: {nazwa}")
            brak_wejscia += 1
            continue
        sha_wejscie_teraz = sha(sciezka)
        if sha_wejscie_teraz != wpis["sha_wejscie"]:
            print(f"ZMIENIONY FIXTURE (nie wynik!): {nazwa}")
            rozjazd += 1
            continue
        with open(sciezka, encoding="utf-8") as f:
            tekst = f.read()
        wynik, _ = zk.przetworz(tekst, sciezka)
        sha_wyjscie_teraz = hashlib.sha256(wynik.encode("utf-8")).hexdigest()
        if sha_wyjscie_teraz == wpis["sha_wyjscie"]:
            w_terminie += 1
        else:
            print(f"ROZJAZD WYNIKU: {nazwa} — zachowanie Zaglady sie zmienilo")
            rozjazd += 1
    print()
    print(f"W-TERMINIE: {w_terminie} | ROZJAZD: {rozjazd} | BRAK: {brak_wejscia}")
    return rozjazd == 0 and brak_wejscia == 0


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    tryb, katalog, zaglada, manifest = sys.argv[1:5]
    if tryb == "zapisz":
        zapisz(katalog, zaglada, manifest)
    elif tryb == "sprawdz":
        ok = sprawdz(katalog, zaglada, manifest)
        sys.exit(0 if ok else 1)
    else:
        print("Nieznany tryb:", tryb)
        sys.exit(2)

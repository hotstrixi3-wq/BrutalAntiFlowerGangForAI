#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BRAMKA TEKSTOW - jedno polecenie przed kazdym commitem.

Powod powstania (2026-09-04): agent napisal w tej sesji trzy dokumenty
o zagrozeniu homoglifami i wstawil do nich 16 ZYWYCH homoglifow. User
wylapal siedemnasty w zdaniu na czacie. Agent nie widzi tego u siebie -
ani przy pisaniu, ani przy wlasnym przegladzie. Potrzebny jest odruch:
jedno polecenie, zawsze to samo, przed kazdym commitem.

Sprawdza WSZYSTKIE pliki wersjonowane przez git (git ls-files), pomijajac
celowo brudna amunicje testowa (dev/kwiatki-testy, fixtures, dev/turnieje,
dev/luki - te pliki MUSZA zawierac skazenia, bo na nich stoja turnieje).

Uzycie:
    python3 sprawdz-teksty.py            # skan repo
    python3 sprawdz-teksty.py PLIK...    # skan wskazanych plikow
    python3 sprawdz-teksty.py --selftest

Kod wyjscia: 0 = czysto, 1 = znaleziono zywe skazenie.
"""

import io
import os
import subprocess
import sys
import unicodedata

WERSJA = "1.2.0"

# katalogi z celowo brudna amunicja - tam skazenie jest POPRAWNE
# (v1.1.0) Pomijamy MINIMUM. Do v1.0.0 lista obejmowala cale katalogi
# dev/turnieje/ i dev/luki/, czyli 30 plikow - a skazenia ma w nich tylko
# CZTERY. Pozostale 26 przechodzilo bez sprawdzenia bez zadnego powodu.
# Zmierzone T8: homoglif wstrzykniety do turniej-6-prokurator.py (pliku
# calkowicie czystego) przechodzil przez bramke.
# Katalogi zostaja na liscie tylko tam, gdzie brud jest z natury rzeczy:
# kwiatki-testy to amunicja, logi to zapis tego, co narzedzia zobaczyly.
POMIJANE = (
    "dev/kwiatki-testy/", "fixtures/",
    # (v1.2.0) muzeum/ - eksponaty, nie zywy kod. Rzeczy, ktore przestaly
    # byc uzyteczne, ale maja zostac w historii z etykieta. Skanowanie ich
    # nic nie wnosi: nikt ich nie edytuje i nikt z nich nie kopiuje.
    "muzeum/",
)

# Pojedyncze pliki, ktore MUSZA zawierac zywe skazenia - bo na nich stoja
# turnieje. Kazdy wymieniony z osobna i z uzasadnieniem, zeby lista nie
# rosla przez przypadek.
POMIJANE_PLIKI = {
    "dev/turnieje/turniej-5-anihilator.py":      "probki dla 9 jezykow",
    "dev/turnieje/zaglada-turniej-niepsucie.py": "korpus plikow do czyszczenia",
    "dev/turnieje/zaglada-turniej-wykrywania.py": "1545 wektorow wykrywania",
    "dev/luki/luka-fstring.py":                  "dowod luki f-string",
    "dev/turnieje/turniej-2-sprawdzajacy.py":    "probki BOM (U+FEFF) w wektorach",
}

# Szukamy WYLACZNIE homoglifow LITER - znakow, ktore udaja lacinke i moga
# po cichu zmienic nazwe zmiennej albo tresc slowa. Symbole typograficzne
# (€, ±, ✓, ½) sa widoczne golym okiem i nikogo nie oszukaja; dodatkowo
# narzedzia rodziny MUSZA je wymieniac w stalych TYPO/TYPOGRAFIA, a raporty
# turniejowe uzywaja checkmarkow. Alarmowanie na nich zrobiloby z tej bramki
# szum, ktory kazdy zaczalby ignorowac - a wtedy przepusci prawdziwy kwiatek.
PISMA_HOMOGLIFOWE = ("CYRILLIC", "GREEK", "ARMENIAN", "COPTIC", "CHEROKEE")


def _dozwolony(c):
    n = unicodedata.name(c, "")
    if any(n.startswith(p) for p in PISMA_HOMOGLIFOWE):
        return False         # to wlasnie lapiemy
    if unicodedata.category(c) in ("Cf", "Zs") and c not in " \t":
        return False         # niewidzialne i twarde spacje
    return True


def skanuj(sciezka):
    """[(nr_linii, znak, nazwa, fragment)]"""
    try:
        tekst = io.open(sciezka, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError):
        return []
    trafienia = []
    for nr, linia in enumerate(tekst.split("\n"), 1):
        for c in linia:
            if ord(c) > 127 and not _dozwolony(c):
                trafienia.append((nr, c, unicodedata.name(c, "?"),
                                  linia.strip()[:70]))
                break
    return trafienia


def pliki_repo():
    """(v1.1.0) Lista plikow do sprawdzenia. Rzuca RuntimeError, gdy nie da
    sie jej ustalic - patrz FAIL-CLOSED nizej."""
    r = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(
            "git ls-files zawiodl (kod %d) - nie wiem, ktore pliki sprawdzic"
            % r.returncode)
    wynik = []
    for f in r.stdout.split("\n"):
        f = f.strip()
        if not f or not os.path.exists(f):
            continue
        if any(f.startswith(p) or ("/" + p) in f for p in POMIJANE):
            continue
        if f.replace(os.sep, "/") in POMIJANE_PLIKI:
            continue
        wynik.append(f)
    if not wynik:
        raise RuntimeError(
            "git ls-files nie zwrocil ani jednego pliku do sprawdzenia")
    return wynik


def selftest():
    import shutil
    import tempfile
    ok = True
    d = tempfile.mkdtemp(prefix="bt-")
    try:
        brudny = os.path.join(d, "brudny.md")
        io.open(brudny, "w", encoding="utf-8").write(
            "tekst z c\u0430 cyrylica\n")
        czysty = os.path.join(d, "czysty.md")
        io.open(czysty, "w", encoding="utf-8").write(
            "zolw \u0142\u0105ka \u017cmija — typografia \u00b7 ramka \u251c\u2500\n")
        if not skanuj(brudny):
            print("  [FAIL] nie wykryl cyrylicy"); ok = False
        if skanuj(czysty):
            print("  [FAIL] falszywy alarm na polskich znakach/typografii"); ok = False
    finally:
        # (v1.1.1) Sprzatamy ZAWSZE, takze po wyjatku. Do v1.1.0 katalog
        # zostawal na dysku po kazdym uruchomieniu: 26 sztuk uzbieralo sie
        # w jednej sesji. Same w sobie male (1 kB), ale to wyciek zasobow
        # w narzedziu, ktore ma pilnowac porzadku.
        shutil.rmtree(d, ignore_errors=True)
    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    args = [a for a in sys.argv[1:]]
    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0
    # (v1.1.0) FAIL-CLOSED. Do v1.0.0 brak listy plikow konczyl sie cicho:
    # `git ls-files` poza repozytorium zwracalo pustke, petla nie wykonywala
    # ani jednego obiegu, a bramka meldowala "0 plikow, zero zywych kwiatkow"
    # z kodem 0. Zmierzone: README z wstrzyknietym U+043E przechodzil bez
    # slowa. Bramka, ktora nie wie, co sprawdzic, MUSI odmowic - cisza
    # nie moze wygladac jak sukces.
    cele = [a for a in args if not a.startswith("--")]
    if not cele:
        try:
            cele = pliki_repo()
        except RuntimeError as e:
            print("[BLAD] %s" % e)
            print("Uruchom bramke w katalogu repozytorium git albo podaj "
                  "pliki wprost: python3 sprawdz-teksty.py PLIK...")
            return 2
    brudne = 0
    for f in cele:
        t = skanuj(f)
        if t:
            brudne += 1
            print("[BLAD] %s" % f)
            for nr, c, nazwa, frag in t[:5]:
                print("       linia %d: U+%04X %s | %s" % (nr, ord(c), nazwa, frag))
            if len(t) > 5:
                print("       ...i %d dalszych linii" % (len(t) - 5))
    print("-" * 62)
    if brudne:
        print("BRAMKA TEKSTOW: %d z %d plikow zawiera ZYWE skazenie" % (brudne, len(cele)))
        print("Zapisz przyklady notacja <U+XXXX> zamiast zywcem (PROTOKOL par. 5).")
        return 1
    print("BRAMKA TEKSTOW: %d plikow, zero zywych kwiatkow" % len(cele))
    return 0


if __name__ == "__main__":
    sys.exit(main())

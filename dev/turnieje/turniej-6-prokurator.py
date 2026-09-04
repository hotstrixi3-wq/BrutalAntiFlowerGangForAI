#!/usr/bin/env python3
"""TURNIEJ 6 — PROKURATOR OGRODNIK (orkiestrator i polityka).

Do v1.2.0 Prokurator nie mial ANI JEDNEGO testu poza selftestem, mimo ze
jest jedynym narzedziem, ktore DECYDUJE o uruchomieniu Zaglady na cudzych
plikach. Blad w polityce = albo zniszczone dane (zaglada tam, gdzie nie
wolno), albo przepuszczone skazenie.

Kategorie:

  A. POLITYKA        — czy kazdy rodzaj wejscia dostaje wlasciwa decyzje
                       (UMORZONE / POUCZENIE / ZAGLADA / BLOKADA).
  B. ALLOWLISTA      — czy celowo brudna amunicja i tlumaczenia i18n sa
                       chronione przed czyszczeniem.
  C. CZYSTE AKTA     — czy raport NIE zawiera zywych znakow skazenia
                       (PROTOKOL par. 5: dowody wylacznie w notacji U+XXXX).
                       Akta sa artefaktem archiwalnym: gdyby przenosily
                       zywe kwiatki, same stalyby sie nosnikiem zarazy.
  D. PLAN-ACT        — czy bez --wykonaj Prokurator NICZEGO nie zmienia
                       (domyslnie raport), a z --wykonaj czysci tylko to,
                       na co polityka pozwala.
  E. FAIL-CLOSED     — czy awaria rodzenstwa albo nieczytelne wejscie
                       konczy sie BLOKADA, a nigdy cichym "czysto".

Uzycie:  python3 dev/turnieje/turniej-6-prokurator.py
Wyjscie: 0 = wszystko zdane, 1 = jest regresja.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROKURATOR = os.path.join(KORZEN, "ProkuratorOgrodnik.py")

C = "\u043e"   # cyrylickie o
A = "\u0430"   # cyrylickie a
POLSKI = "zolw \u0142\u0105ka \u017cmija"
CJK = "\u4e2d\u6587\u6587\u5b57"
EMOJI = "\U0001f600\U0001f680"
ARAB = "\u0645\u0631\u062d\u0628\u0627"


def uruchom(args, cwd=None):
    try:
        r = subprocess.run([sys.executable, PROKURATOR] + args,
                           capture_output=True, text=True, timeout=180, cwd=cwd)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"


def zapisz(katalog, wzgledna, tresc):
    p = os.path.join(katalog, wzgledna)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8").write(tresc)
    return p


# =====================================================================
# A. POLITYKA
# =====================================================================
def kat_a():
    tmp = tempfile.mkdtemp(prefix="t6a-")
    # (wzgledna_sciezka, tresc, oczekiwana_decyzja)
    przypadki = [
        # zwykly .py ze skazeniem w KODZIE -> nie wolno umorzyc
        ("src/kod.py", 'c%snter = 1\nprint(c%snter)\n' % (C, C),
         ("ZAGLADA", "POUCZENIE")),
        # celowo brudna amunicja -> UMORZONE
        ("dev/kwiatki-testy/brud.py", 'x = "c%s"\n' % C, ("UMORZONE",)),
        ("tests/fixtures/brud.txt", 'tekst %s\n' % C, ("UMORZONE",)),
        ("app/brudne_dane.txt", 'tekst %s\n' % C, ("UMORZONE",)),
        # tlumaczenia -> UMORZONE
        ("app/i18n/ru.txt", "\u041c\u043e\u0441\u043a\u0432\u0430\n", ("UMORZONE",)),
        ("app/locales/zh.txt", CJK + "\n", ("UMORZONE",)),
        ("app/messages.po", 'msgstr "%s"\n' % CJK, ("UMORZONE",)),
        # czysty plik -> zadnych akt
        ("src/czysty.py", 'x = 1\nprint(x)\n', ("OK",)),
        ("docs/czysty.md", "# Tytul\n\n%s\n" % POLSKI, ("OK",)),
    ]
    zle = 0
    szczegoly = []
    for wzgl, tresc, oczek in przypadki:
        zapisz(tmp, wzgl, tresc)
    kod, out, err = uruchom(["--oskarz"] + [os.path.join(tmp, w)
                                            for w, _, _ in przypadki], cwd=tmp)
    akta_p = os.path.join(tmp, "akta_prokuratora.json")
    if not os.path.exists(akta_p):
        print("== A. POLITYKA ==\n   [BLAD] --oskarz nie wytworzyl akt")
        shutil.rmtree(tmp, ignore_errors=True)
        return len(przypadki)
    akta = json.load(io.open(akta_p, encoding="utf-8"))
    wpisy = akta.get("akta", akta) if isinstance(akta, dict) else akta
    decyzje = {}
    for w in wpisy:
        decyzje[os.path.basename(w.get("plik", ""))] = w.get("decyzja", "?")
    for wzgl, tresc, oczek in przypadki:
        nazwa = os.path.basename(wzgl)
        d = decyzje.get(nazwa, "OK")   # brak wpisu = czysto
        if d not in oczek:
            zle += 1
            szczegoly.append((wzgl, d, "/".join(oczek)))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== A. POLITYKA ==")
    print("   przypadkow: %d | zle decyzje: %d" % (len(przypadki), zle))
    for w, d, o in szczegoly:
        print("     [ZLA DECYZJA] %s: dostal %s, oczekiwano %s" % (w, d, o))
    return zle


# =====================================================================
# B. ALLOWLISTA CHRONI PRZED CZYSZCZENIEM
# =====================================================================
def kat_b():
    tmp = tempfile.mkdtemp(prefix="t6b-")
    chronione = [
        ("dev/kwiatki-testy/amunicja.py", 'x = "c%snter"\n' % C),
        ("tests/fixtures/wzorzec.txt", "skazenie %s tutaj\n" % C),
        ("app/i18n/ru.txt", "\u041c\u043e\u0441\u043a\u0432\u0430 2024\n"),
        ("app/locales/zh.txt", CJK + "\n"),
        ("node_modules/pakiet/plik.js", 'let c%snter = 1;\n' % C),
    ]
    sciezki = [zapisz(tmp, w, t) for w, t in chronione]
    przed = [io.open(p, encoding="utf-8").read() for p in sciezki]
    uruchom(["--wykonaj"] + sciezki, cwd=tmp)
    zle = 0
    szczegoly = []
    for (w, _), p, tresc0 in zip(chronione, sciezki, przed):
        if io.open(p, encoding="utf-8").read() != tresc0:
            zle += 1
            szczegoly.append(w)
    shutil.rmtree(tmp, ignore_errors=True)
    print("== B. ALLOWLISTA (ochrona przed czyszczeniem) ==")
    print("   plikow: %d | TKNIETYCH MIMO OCHRONY: %d" % (len(chronione), zle))
    for w in szczegoly:
        print("     [NARUSZENIE] %s zostal zmieniony" % w)
    return zle


# =====================================================================
# C. CZYSTE AKTA (par. 5 protokolu)
# =====================================================================
def kat_c():
    tmp = tempfile.mkdtemp(prefix="t6c-")
    # celowo bogaty zestaw skazen, ktore NIE MOGA trafic zywcem do akt
    zywe = [C, A, CJK[0], EMOJI[0], ARAB[0], "\u200b", "\u00a0", "\u2028"]
    zapisz(tmp, "src/mix.py", 'c%snter = 1  # %s %s\nx = "%s"\n'
           % (C, CJK, EMOJI, ARAB))
    zapisz(tmp, "src/niewidz.py", 'a%sb = 2\nc\u00a0= 3\n' % "\u200b")
    zapisz(tmp, "docs/proza.md", "Tekst %s z %s i %s\n" % (C, CJK, EMOJI))
    pliki = [os.path.join(tmp, "src/mix.py"),
             os.path.join(tmp, "src/niewidz.py"),
             os.path.join(tmp, "docs/proza.md")]
    kod, out, err = uruchom(["--oskarz"] + pliki, cwd=tmp)
    zle = 0
    szczegoly = []

    akta_p = os.path.join(tmp, "akta_prokuratora.json")
    if os.path.exists(akta_p):
        surowe = io.open(akta_p, encoding="utf-8").read()
        for z in zywe:
            if z in surowe:
                zle += 1
                szczegoly.append(("AKTA", "zywy znak U+%04X w pliku akt" % ord(z)))
        if "U+" not in surowe:
            zle += 1
            szczegoly.append(("AKTA", "brak notacji U+XXXX - dowody nieczytelne"))
    else:
        zle += 1
        szczegoly.append(("AKTA", "brak pliku akt po --oskarz"))

    shutil.rmtree(tmp, ignore_errors=True)
    print("== C. CZYSTE AKTA (dowody w U+XXXX) ==")
    print("   naruszen: %d" % zle)
    for t, o in szczegoly:
        print("     [%s] %s" % (t, o))
    return zle


# =====================================================================
# D. PLAN-ACT (raport nie rusza, --wykonaj rusza)
# =====================================================================
def kat_d():
    tmp = tempfile.mkdtemp(prefix="t6d-")
    p = zapisz(tmp, "src/kod.py", 'c%snter = 1\nprint(c%snter)\n' % (C, C))
    przed = io.open(p, encoding="utf-8").read()
    zle = 0
    szczegoly = []

    # 1. sam raport - nie wolno tknac
    uruchom([p], cwd=tmp)
    if io.open(p, encoding="utf-8").read() != przed:
        zle += 1
        szczegoly.append("tryb raportu ZMIENIL plik (powinien tylko raportowac)")

    # 2. --oskarz - tez nie wolno tknac pliku zrodlowego
    uruchom(["--oskarz", p], cwd=tmp)
    if io.open(p, encoding="utf-8").read() != przed:
        zle += 1
        szczegoly.append("--oskarz ZMIENIL plik (powinien tylko tworzyc akta)")

    # 3. --wykonaj - MUSI wyczyscic i zostawic dzialajacy kod
    uruchom(["--wykonaj", p], cwd=tmp)
    po = io.open(p, encoding="utf-8").read()
    if po == przed:
        zle += 1
        szczegoly.append("--wykonaj NIE wyczyscil skazonego pliku")
    else:
        if C in po or A in po:
            zle += 1
            szczegoly.append("--wykonaj zostawil skazenie w pliku")
        r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                           timeout=60)
        if r.returncode != 0 or r.stdout.strip() != "1":
            zle += 1
            szczegoly.append("po --wykonaj kod nie dziala: %s"
                             % (r.stderr.strip().splitlines() or [""])[-1][:50])

    shutil.rmtree(tmp, ignore_errors=True)
    print("== D. PLAN-ACT (raport vs wykonanie) ==")
    print("   naruszen: %d" % zle)
    for o in szczegoly:
        print("     [NARUSZENIE] %s" % o)
    return zle


# =====================================================================
# E. FAIL-CLOSED
# =====================================================================
def kat_e():
    tmp = tempfile.mkdtemp(prefix="t6e-")
    zle = 0
    szczegoly = []

    # 1. plik nieczytalny (nie-UTF8) -> BLOKADA, nigdy "czysto"
    p = os.path.join(tmp, "src")
    os.makedirs(p, exist_ok=True)
    zly = os.path.join(p, "bin.py")
    io.open(zly, "wb").write(b'x = "kawa\xe9"\n')
    kod, out, err = uruchom(["--oskarz", zly], cwd=tmp)
    calosc = out + err
    akta_p = os.path.join(tmp, "akta_prokuratora.json")
    tresc_akt = io.open(akta_p, encoding="utf-8").read() if os.path.exists(akta_p) else ""
    if "BLOKADA" not in calosc and "BLOKADA" not in tresc_akt:
        zle += 1
        szczegoly.append("nieczytelne wejscie nie dalo BLOKADY")

    # 2. brak rodzenstwa -> BLOKADA/blad, nie ciche "czysto"
    izolatka = tempfile.mkdtemp(prefix="t6e-izo-")
    shutil.copy(PROKURATOR, izolatka)     # SAM prokurator, bez rodzenstwa
    cel = os.path.join(izolatka, "kod.py")
    io.open(cel, "w", encoding="utf-8").write('c%snter = 1\n' % C)
    r = subprocess.run([sys.executable, os.path.join(izolatka, "ProkuratorOgrodnik.py"),
                        cel], capture_output=True, text=True, timeout=120)
    calosc2 = r.stdout + r.stderr
    if r.returncode == 0 and "BLOKADA" not in calosc2 and "BLAD" not in calosc2:
        zle += 1
        szczegoly.append("brak rodzenstwa zakonczyl sie cichym sukcesem "
                         "(exit 0, bez BLOKADY)")
    shutil.rmtree(izolatka, ignore_errors=True)
    shutil.rmtree(tmp, ignore_errors=True)

    print("== E. FAIL-CLOSED ==")
    print("   naruszen: %d" % zle)
    for o in szczegoly:
        print("     [NARUSZENIE] %s" % o)
    return zle


def main():
    print("=" * 66)
    print("TURNIEJ 6 — PROKURATOR OGRODNIK")
    print("=" * 66)
    zle = kat_a() + kat_b() + kat_c() + kat_d() + kat_e()
    print()
    print("=" * 66)
    print("FINAL T6: %s" % ("WSZYSTKO ZDANE" if not zle
                            else "REGRESJA — %d naruszen" % zle))
    print("=" * 66)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())

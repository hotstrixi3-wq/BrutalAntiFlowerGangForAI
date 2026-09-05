#!/usr/bin/env python3
"""TURNIEJ 7 — WIARYGODNOSC ZWIADU (oczu operatora).

Najwazniejszy turniej w repo, a powstal jako ostatni. Powod: `zwiad.py`
nie mial ZADNEGO testu poza wlasnym selftestem, a to na nim opiera sie
CALA zdolnosc agenta do podejmowania decyzji. Jesli zwiad klamie, to
klamie kazda analiza zbudowana na jego raporcie - i agent podejmie zla
decyzje majac pewnosc, ze podejmuje dobra.

Pozostale turnieje sprawdzaja, czy narzedzia NIE PSUJA plikow.
Ten sprawdza, czy narzedzie NIE WPROWADZA OPERATORA W BLAD.

Kategorie:

  A. PRAWDOMOWNOSC  — czy to, co zwiad PRZEWIDUJE, zgadza sie z tym, co
                      narzedzia FAKTYCZNIE robia. Dla kazdej probki:
                      bierzemy przewidywanie zwiadu, uruchamiamy prawdziwe
                      narzedzie na kopii i porownujemy bajt w bajt.
                      To jest sedno: przewidywanie rozne od rzeczywistosci
                      jest gorsze niz brak przewidywania.
  B. KOMPLETNOSC    — czy zwiad widzi KAZDE skazenie. Przeoczone skazenie
                      to cisza, ktora operator odczyta jako "czysto".
  C. ROZDZIAL       — czy poprawnie dzieli na KOD i DANE. Od tego zalezy
                      ocena ryzyka: skazenie w kodzie zmienia dzialanie,
                      w komentarzu nie.
  D. ZERO ZAPISU    — kontrakt zwiadu. Po pelnej analizie (raport, warianty,
                      podglad) plik i katalog musza byc nietkniete.
  E. OSTRZEZENIA    — czy sygnalizuje utrate danych (exit=2) i wskazuje
                      wlasciwego czlonka Gangu dla danego typu pliku.
  F. ODPORNOSC      — czy nie wywraca sie na wejsciu, ktorego nie rozumie
                      (plik binarny, pusty, bez rozszerzenia, ogromny).

Uzycie:  python3 dev/turnieje/turniej-7-zwiad.py
Wyjscie: 0 = zwiad godny zaufania, 1 = klamie albo milczy.
"""
import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZWIAD = os.path.join(KORZEN, "zwiad.py")

C = "\u043e"   # cyrylickie o
A = "\u0430"   # cyrylickie a
E = "\u0435"   # cyrylickie e
ZW = "\u200b"  # zero-width space
NB = "\u00a0"  # twarda spacja
CJK = "\u4e2d\u6587"
POLSKI = "zolw \u0142\u0105ka \u017cmija"


def _zaladuj(nazwa):
    p = os.path.join(KORZEN, nazwa)
    s = importlib.util.spec_from_file_location(nazwa[:-3].replace("-", "_"), p)
    m = importlib.util.module_from_spec(s)
    sys.modules[s.name] = m
    s.loader.exec_module(m)
    return m


Z = _zaladuj("zwiad.py")


def uruchom(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180, cwd=cwd)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"


# =====================================================================
# A. PRAWDOMOWNOSC — przewidywanie vs rzeczywistosc
# =====================================================================
# (nazwa, tresc, narzedzie, flaga, klucz_wariantu_w_zwiadzie)
PRAWDOMOWNOSC = [
    ("py-kod.py", 'c%snter = 0\nprint(c%snter)\n' % (C, C),
     "ZagladaKultury.py", "--zaglada", "zaglada-poza-literalami"),
    ("py-literal.py", 'x = "M%sskwa"\nprint(x)\n' % (C,),
     "ZagladaKultury.py", "--zaglada", "zaglada-poza-literalami"),
    ("py-mieszany.py",
     '# k%smentarz\nv%sl = 1\nOPIS = "%s"\nprint(v%sl, OPIS)\n' % (C, A, POLSKI, A),
     "ZagladaKultury.py", "--zaglada", "zaglada-poza-literalami"),
    ("py-fstring.py", 'v%s = 7\nprint(f"wynik: {v%s}")\n' % (C, C),
     "ZagladaKultury.py", "--zaglada", "zaglada-poza-literalami"),
    ("py-niewidz.py", 'li%scznik = 4\nprint(licznik)\n' % (ZW,),
     "ZagladaKultury.py", "--zaglada", "zaglada-poza-literalami"),
    ("js-kod.js", 'let c%snter = 1;\nconsole.log(c%snter);\n' % (C, C),
     "AnihilatorChwastow.py", "--anihilacja", "anihilator"),
    ("js-template.js", 'let v%s = 7;\nconsole.log(`x ${v%s}`);\n' % (C, C),
     "AnihilatorChwastow.py", "--anihilacja", "anihilator"),
    ("js-literal.js", 'let a = 1;\nconst s = "M%sskwa";\n' % (C,),
     "AnihilatorChwastow.py", "--anihilacja", "anihilator"),
    ("proza.md", '# Tytul\n\nTekst z M%sskwa i %s\n' % (C, POLSKI),
     "ZagladaKultury.py", "--zaglada", None),
]


def kat_a():
    tmp = tempfile.mkdtemp(prefix="t7a-")
    zle = 0
    szczegoly = []
    for nazwa, tresc, narzedzie, flaga, klucz in PRAWDOMOWNOSC:
        ext = nazwa.rsplit(".", 1)[-1]

        # 1. co zwiad PRZEWIDUJE
        przewidziane = Z.symuluj(tresc, ext)

        # 2. co narzedzie FAKTYCZNIE robi
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        uruchom([sys.executable, os.path.join(KORZEN, narzedzie), flaga, p])
        faktyczne = io.open(p, encoding="utf-8").read()

        if przewidziane != faktyczne:
            zle += 1
            szczegoly.append((nazwa, "symuluj()",
                              "przewidzial %r, wyszlo %r"
                              % (przewidziane[:34], faktyczne[:34])))

        # 3. czy konkretny wariant wachlarza tez sie zgadza
        if klucz:
            wariant = Z._wariant_tresc(klucz, tresc, ext)
            if wariant is not None and not wariant.startswith("\x00"):
                if wariant != faktyczne:
                    zle += 1
                    szczegoly.append((nazwa, "wariant %s" % klucz,
                                      "przewidzial %r, wyszlo %r"
                                      % (wariant[:30], faktyczne[:30])))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== A. PRAWDOMOWNOSC (przewidywanie vs rzeczywistosc) ==")
    print("   probek: %d | KLAMSTW: %d" % (len(PRAWDOMOWNOSC), zle))
    for n, co, o in szczegoly:
        print("     [KLAMSTWO] %s (%s): %s" % (n, co, o))
    return zle


# =====================================================================
# B. KOMPLETNOSC — czy widzi KAZDE skazenie
# =====================================================================
# (nazwa, tresc, ile_skazen_ma_zobaczyc)
KOMPLETNOSC = [
    ("jeden.py", 'v%s = 1\n' % C, 1),
    ("cztery.py", 'c%snter = 0\nprint(c%snter)\n# k%smentarz\nx = "M%sskwa"\n'
     % (C, C, C, C), 4),
    ("mieszane.py", 'a%s = 1\nb%s = 2\nc%s = 3\n' % (A, E, C), 3),
    ("niewidzialne.py", 'a%sb = 1\nc%sd = 2\n' % (ZW, NB), 2),
    ("cjk.txt", 'tekst %s koniec\n' % CJK, 2),
    ("czysty.py", 'x = 1\nprint("%s")\n' % POLSKI, 0),
    ("tylko-polski.md", '# %s\n\n%s\n' % (POLSKI, POLSKI), 0),
]


def kat_b():
    tmp = tempfile.mkdtemp(prefix="t7b-")
    zle = 0
    szczegoly = []
    for nazwa, tresc, oczekiwane in KOMPLETNOSC:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        w = Z.zbadaj(p)
        ile = len(w["znaleziska"])
        if ile != oczekiwane:
            zle += 1
            kierunek = "PRZEOCZYL" if ile < oczekiwane else "FALSZYWY ALARM"
            szczegoly.append((nazwa, kierunek, "%d zamiast %d" % (ile, oczekiwane)))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== B. KOMPLETNOSC (czy widzi kazde skazenie) ==")
    print("   probek: %d | bledow: %d" % (len(KOMPLETNOSC), zle))
    for n, k, o in szczegoly:
        print("     [%s] %s: %s" % (k, n, o))
    return zle


# =====================================================================
# C. ROZDZIAL KOD / DANE
# =====================================================================
# (nazwa, tresc, ile_w_kodzie, ile_w_danych)
ROZDZIAL = [
    ("kod.py", 'c%snter = 0\nprint(c%snter)\n' % (C, C), 2, 0),
    ("dane.py", '# k%smentarz\nx = "M%sskwa"\n' % (C, C), 0, 2),
    ("mix.py", 'v%s = 1\n# k%smentarz\ns = "M%sskwa"\nprint(v%s)\n'
     % (C, C, C, C), 2, 2),
    # wnetrze f-stringa to KOD mimo ze wyglada jak tekst
    ("fstring.py", 'v%s = 7\nprint(f"opis: {v%s}")\n' % (C, C), 2, 0),
    # docstring to DANE
    ("docstring.py", 'def f():\n    """opis M%sskwa"""\n    return 1\n' % C, 0, 1),
]


def kat_c():
    tmp = tempfile.mkdtemp(prefix="t7c-")
    zle = 0
    szczegoly = []
    for nazwa, tresc, ozk, ozd in ROZDZIAL:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        w = Z.zbadaj(p)
        wk = sum(1 for z in w["znaleziska"] if z["gdzie"] == "KOD")
        wd = sum(1 for z in w["znaleziska"] if z["gdzie"] != "KOD")
        if (wk, wd) != (ozk, ozd):
            zle += 1
            szczegoly.append((nazwa, "kod=%d dane=%d, oczekiwano kod=%d dane=%d"
                              % (wk, wd, ozk, ozd)))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== C. ROZDZIAL KOD / DANE ==")
    print("   probek: %d | zlych klasyfikacji: %d" % (len(ROZDZIAL), zle))
    for n, o in szczegoly:
        print("     [ZLA KLASYFIKACJA] %s: %s" % (n, o))
    return zle


# =====================================================================
# D. ZERO ZAPISU — kontrakt
# =====================================================================
def kat_d():
    tmp = tempfile.mkdtemp(prefix="t7d-")
    zle = 0
    szczegoly = []
    probki = [
        ("a.py", 'c%snter = 0\nprint(c%snter)\n' % (C, C)),
        ("b.js", 'let v%s = 1;\n' % C),
        ("c.md", 'tekst M%sskwa\n' % C),
        ("d.txt", '%s i %s\n' % (CJK, POLSKI)),
    ]
    for nazwa, tresc in probki:
        io.open(os.path.join(tmp, nazwa), "w", encoding="utf-8").write(tresc)

    przed_pliki = sorted(os.listdir(tmp))
    przed_tresc = {n: io.open(os.path.join(tmp, n), "rb").read()
                   for n in przed_pliki}

    # pelna analiza wszystkimi trybami, takze przez CLI
    for nazwa, _ in probki:
        p = os.path.join(tmp, nazwa)
        Z.zbadaj(p)
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            Z.wachlarz(p)
            Z.podglad(p)
        uruchom([sys.executable, ZWIAD, p])
        uruchom([sys.executable, ZWIAD, "--warianty", p])
        uruchom([sys.executable, ZWIAD, "--podglad", p])
        uruchom([sys.executable, ZWIAD, "--json", p])

    po_pliki = sorted(os.listdir(tmp))
    if po_pliki != przed_pliki:
        zle += 1
        szczegoly.append("ZWIAD UTWORZYL/USUNAL PLIKI: %s"
                         % (set(po_pliki) ^ set(przed_pliki)))
    for n in przed_pliki:
        if io.open(os.path.join(tmp, n), "rb").read() != przed_tresc[n]:
            zle += 1
            szczegoly.append("ZWIAD ZMIENIL PLIK: %s" % n)
    shutil.rmtree(tmp, ignore_errors=True)
    print("== D. ZERO ZAPISU (kontrakt zwiadu) ==")
    print("   plikow: %d | naruszen kontraktu: %d" % (len(probki), zle))
    for o in szczegoly:
        print("     [NARUSZENIE] %s" % o)
    return zle


# =====================================================================
# E. OSTRZEZENIA — utrata danych i wybor narzedzia
# =====================================================================
def kat_e():
    tmp = tempfile.mkdtemp(prefix="t7e-")
    zle = 0
    szczegoly = []

    # 1. CJK w prozie -> nienaprawialne, exit=2
    p = os.path.join(tmp, "chin.html")
    io.open(p, "w", encoding="utf-8").write('<p>%s</p>\n' % CJK)
    kod, out, _ = uruchom([sys.executable, ZWIAD, p])
    if kod != 2:
        zle += 1
        szczegoly.append("CJK: exit=%d zamiast 2 (utrata danych bez alarmu)" % kod)
    if "USUNIECIE" not in out:
        zle += 1
        szczegoly.append("CJK: brak slowa USUNIECIE w raporcie")

    # 2. plik czysty -> exit=0
    p2 = os.path.join(tmp, "ok.py")
    io.open(p2, "w", encoding="utf-8").write('x = 1\n')
    kod, _, _ = uruchom([sys.executable, ZWIAD, p2])
    if kod != 0:
        zle += 1
        szczegoly.append("czysty plik: exit=%d zamiast 0" % kod)

    # 3. skazenie naprawialne -> exit=1
    p3 = os.path.join(tmp, "naprawialny.py")
    io.open(p3, "w", encoding="utf-8").write('v%s = 1\n' % C)
    kod, _, _ = uruchom([sys.executable, ZWIAD, p3])
    if kod != 1:
        zle += 1
        szczegoly.append("naprawialny: exit=%d zamiast 1" % kod)

    # 4. wachlarz .js MUSI ostrzec przed Prokuratorem
    p4 = os.path.join(tmp, "x.js")
    io.open(p4, "w", encoding="utf-8").write('let v%s = 1;\n' % C)
    _, out4, _ = uruchom([sys.executable, ZWIAD, "--warianty", p4])
    if "Anihilator" not in out4:
        zle += 1
        szczegoly.append(".js: nie wskazal Anihilatora jako wlasciwego")
    if "Prokurator" not in out4:
        zle += 1
        szczegoly.append(".js: nie ostrzegl przed Prokuratorem")

    # 5. html -> ostrzezenie o tresci uzytkownika
    _, out5, _ = uruchom([sys.executable, ZWIAD, "--warianty", p])
    if "OSTROZNIE" not in out5 and "USUNIET" not in out5.upper():
        zle += 1
        szczegoly.append(".html: brak ostrzezenia o tresci uzytkownika")

    shutil.rmtree(tmp, ignore_errors=True)
    print("== E. OSTRZEZENIA (utrata danych, wybor narzedzia) ==")
    print("   naruszen: %d" % zle)
    for o in szczegoly:
        print("     [BRAK OSTRZEZENIA] %s" % o)
    return zle


# =====================================================================
# F. ODPORNOSC — dziwne wejscie nie moze wywrocic oczu
# =====================================================================
def kat_f():
    tmp = tempfile.mkdtemp(prefix="t7f-")
    zle = 0
    szczegoly = []

    przypadki = []
    p = os.path.join(tmp, "bin.py")
    io.open(p, "wb").write(bytes(range(256)))
    przypadki.append(("plik binarny", p))

    p = os.path.join(tmp, "pusty.py")
    io.open(p, "w").write("")
    przypadki.append(("plik pusty", p))

    p = os.path.join(tmp, "bez_rozszerzenia")
    io.open(p, "w", encoding="utf-8").write('tekst M%sskwa\n' % C)
    przypadki.append(("bez rozszerzenia", p))

    p = os.path.join(tmp, "latin.py")
    io.open(p, "wb").write(b'x = "kawa\xe9"\n')
    przypadki.append(("nie-UTF8", p))

    p = os.path.join(tmp, "dluga.py")
    io.open(p, "w", encoding="utf-8").write('x = "%s"\n' % ("a" * 60000))
    przypadki.append(("bardzo dluga linia", p))

    p = os.path.join(tmp, "niekompilujacy.py")
    io.open(p, "w", encoding="utf-8").write('def f(:\n  v%s = 1\n' % C)
    przypadki.append((".py ze zlamana skladnia", p))

    przypadki.append(("plik nieistniejacy", os.path.join(tmp, "nie-ma.py")))

    for opis, sciezka in przypadki:
        try:
            w = Z.zbadaj(sciezka)
            if not isinstance(w, dict) or "czytelny" not in w:
                zle += 1
                szczegoly.append((opis, "zwrocil cos innego niz raport"))
        except Exception as e:
            zle += 1
            szczegoly.append((opis, "WYJATEK %s" % type(e).__name__))
            continue
        kod, _, err = uruchom([sys.executable, ZWIAD, sciezka])
        if "Traceback" in err:
            zle += 1
            szczegoly.append((opis, "traceback z CLI"))

    shutil.rmtree(tmp, ignore_errors=True)
    print("== F. ODPORNOSC (dziwne wejscie) ==")
    print("   przypadkow: %d | awarii: %d" % (len(przypadki), zle))
    for n, o in szczegoly:
        print("     [AWARIA] %s: %s" % (n, o))
    return zle


def main():
    print("=" * 68)
    print("TURNIEJ 7 — WIARYGODNOSC ZWIADU")
    print("Nie 'czy nie psuje plikow', tylko 'czy nie wprowadza w blad'")
    print("=" * 68)
    zle = kat_a() + kat_b() + kat_c() + kat_d() + kat_e() + kat_f()
    print()
    print("=" * 68)
    print("FINAL T7: %s" % ("ZWIAD GODNY ZAUFANIA" if not zle
                            else "ZWIAD ZAWODZI — %d przypadkow" % zle))
    print("=" * 68)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())

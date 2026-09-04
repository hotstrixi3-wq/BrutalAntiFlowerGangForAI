#!/usr/bin/env python3
"""TURNIEJ 4 — KRYTERIUM WYKONANIA (nie compile()).

Dlaczego istnieje: turnieje T3 i Z2 uznaja plik za caly, jesli przechodzi
compile(). Ale cala klasa bledow, ktore narzedzie potrafi wprowadzic,
compile() PRZECHODZI i wybucha dopiero przy uruchomieniu:

  * luka f-string (v1.4.0): definicja zmiennej wyczyszczona, uzycie
    wewnatrz f-stringa nietkniete -> NameError, skladnia poprawna;
  * niespojnosc identyfikatorow (v1.1.0, znalezisko _scandir_path):
    dwie rozne nazwy tej samej zmiennej -> AttributeError.

Ten turniej URUCHAMIA program przed i po czyszczeniu i porownuje
STANDARDOWE WYJSCIE. Werdykt zdaje tylko wtedy, gdy program dzialal
przed i daje DOKLADNIE ten sam wynik po.

Dodatkowo sprawdza, ze DANE (polskie napisy, literaly) nie zostaly ruszone.

Uzycie:  python3 dev/turnieje/turniej-4-runtime.py
Wyjscie: 0 = wszystko zdane, 1 = jest regresja.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZAGLADA = os.path.join(KORZEN, "ZagladaKultury.py")
POGROMCA = os.path.join(KORZEN, "PogromcaKwiatkow.py")

C = "\u043e"   # cyrylickie o
A = "\u0430"   # cyrylickie a
E = "\u0435"   # cyrylickie e
ZW = "\u200b"  # zero-width space

# (nazwa, kod, oczekiwane_wyjscie)
PROBKI = [
    ("fstring-prosty",
     'v%s = 7\nprint(f"wynik: {v%s}")\n' % (C, C), "wynik: 7"),
    ("fstring-format-spec",
     'a%s = 1\nprint(f"{a%s:>3}".strip())\n' % (A, A), "1"),
    ("fstring-zagniezdzony",
     'n%s = 3\nprint(f"{ {i for i in range(n%s)} }")\n' % (C, C), "{0, 1, 2}"),
    ("fstring-wielolinijkowy",
     'x%s = 2\nprint(f"""linia {x%s}""")\n' % (C, C), "linia 2"),
    ("fstring-indeks",
     'd = {"k": 1}\nk%s = "k"\nprint(f"{d[k%s]}")\n' % (C, C), "1"),
    ("fstring-konwersja",
     'v%s = "a"\nprint(f"{v%s!r}")\n' % (C, C), "'a'"),
    ("fstring-metoda",
     's%s = "ala"\nprint(f"{s%s.upper()}")\n' % (C, C), "ALA"),
    ("fstring-zagniezdzony-fstring",
     'n%s = "x"\nprint(f\'{f"{n%s}!"}\')\n' % (C, C), "x!"),
    ("fstring-podwojne-klamry",
     'v%s = 1\nprint(f"{{stale}} {v%s}")\n' % (C, C), "{stale} 1"),
    ("fstring-dane-polskie",
     'k%s = 3\nprint(f"cena: {k%s} zl, zolw i \u0142\u0105ka")\n' % (C, C),
     "cena: 3 zl, zolw i \u0142\u0105ka"),
    ("dekorator",
     'def dek%s(f):\n    return f\n\n@dek%s\ndef g():\n    return 42\n'
     'print(g())\n' % (C, C), "42"),
    ("petla-i-zakres",
     's%sma = 0\nfor i in range(4):\n    s%sma += i\nprint(s%sma)\n'
     % (E, E, E), "6"),
    ("slownik-klucz-literal",
     'd = {"kl\u0105cz": 1}\nprint(d["kl\u0105cz"])\n', "1"),
    ("czysty-bez-skazenia",
     'x = 10\nprint(f"{x * 2}")\n', "20"),
]

# Druga kategoria: pliki, ktore PRZED czyszczeniem NIE dzialaja (skazenie
# rozjechalo nazwy albo zlamalo skladnie), a po czyszczeniu MUSZA zaczac
# dzialac. To sprawdzian sily naprawczej, nie tylko nieszkodliwosci.
NAPRAWIALNE = [
    ("niespojnosc-nazw",
     'sc%sndir = 5\nprint(scandir)\n' % (A,), "5"),
    ("zerowidth-w-nazwie",
     'lic%sznik = 4\nprint(licznik)\n' % (ZW,), "4"),
    ("klasa-i-atrybut",
     'class K:\n    def __init__(self):\n        self.p%sle = 9\n'
     'print(K().pole)\n' % (C,), "9"),
    ("import-nazwa",
     'import js%sn\nprint(js%sn.dumps({"a": 1}))\n' % (C, C), '{"a": 1}'),
]


def uruchom(sciezka):
    """Zwraca (ok, wyjscie). ok=False gdy program sie wywrocil."""
    try:
        r = subprocess.run([sys.executable, sciezka], capture_output=True,
                           text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    if r.returncode != 0:
        ost = (r.stderr or "").strip().splitlines()
        return False, (ost[-1] if ost else "blad bez opisu")
    return True, r.stdout.strip()


def przebieg(narzedzie, flaga, etykieta):
    tmp = tempfile.mkdtemp(prefix="turniej4-")
    zdane = oblane = pominiete = 0
    awarie = []
    for nazwa, kod, oczekiwane in PROBKI:
        p = os.path.join(tmp, nazwa.replace("-", "_") + ".py")
        io.open(p, "w", encoding="utf-8").write(kod)

        ok_przed, przed = uruchom(p)
        if not ok_przed or przed != oczekiwane:
            # probka nie dziala JUZ PRZED czyszczeniem — to blad probki,
            # nie narzedzia. Zglaszamy, ale nie obciazamy narzedzia.
            pominiete += 1
            awarie.append((nazwa, "PROBKA ZLA", przed[:60]))
            continue

        subprocess.run([sys.executable, narzedzie, flaga, p],
                       capture_output=True, text=True, timeout=300)

        ok_po, po = uruchom(p)
        if ok_po and po == przed:
            zdane += 1
        else:
            oblane += 1
            awarie.append((nazwa, "ZEPSUTY" if not ok_po else "INNY WYNIK",
                           "przed=%r po=%r" % (przed[:24], po[:40])))
    shutil.rmtree(tmp, ignore_errors=True)

    print("== %s ==" % etykieta)
    print("   probek: %d | ZDANE: %d | OBLANE: %d | zle probki: %d"
          % (len(PROBKI), zdane, oblane, pominiete))
    for nazwa, typ, opis in awarie:
        print("     [%s] %s: %s" % (typ, nazwa, opis))
    return oblane + pominiete


def przebieg_naprawczy(narzedzie, flaga, etykieta):
    """Pliki zepsute PRZED czyszczeniem — po czyszczeniu maja DZIALAC."""
    tmp = tempfile.mkdtemp(prefix="turniej4n-")
    naprawione = niedomkniete = 0
    szczegoly = []
    for nazwa, kod, oczekiwane in NAPRAWIALNE:
        p = os.path.join(tmp, nazwa.replace("-", "_") + ".py")
        io.open(p, "w", encoding="utf-8").write(kod)
        ok_przed, _ = uruchom(p)
        subprocess.run([sys.executable, narzedzie, flaga, p],
                       capture_output=True, text=True, timeout=300)
        ok_po, po = uruchom(p)
        if ok_po and po == oczekiwane:
            naprawione += 1
        else:
            niedomkniete += 1
            szczegoly.append((nazwa, "nadal zle" if not ok_po else "inny wynik",
                              po[:50]))
        if ok_przed:
            szczegoly.append((nazwa, "UWAGA", "dzialalo juz przed czyszczeniem"))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== %s (sila naprawcza) ==" % etykieta)
    print("   probek: %d | NAPRAWIONE: %d | nienaprawione: %d"
          % (len(NAPRAWIALNE), naprawione, niedomkniete))
    for n, t, o in szczegoly:
        print("     [%s] %s: %s" % (t, n, o))
    return niedomkniete


def main():
    print("=" * 66)
    print("TURNIEJ 4 — kryterium WYKONANIA (uruchom i porownaj wynik)")
    print("=" * 66)
    zle = 0
    zle += przebieg(ZAGLADA, "--zaglada", "ZAGLADA")
    print()
    zle += przebieg(POGROMCA, "--fix", "POGROMCA --fix")
    print()
    zle += przebieg_naprawczy(ZAGLADA, "--zaglada", "ZAGLADA")
    print()
    print("=" * 66)
    print("FINAL T4: %s" % ("WSZYSTKO ZDANE" if not zle
                            else "REGRESJA — %d przypadkow" % zle))
    print("=" * 66)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())

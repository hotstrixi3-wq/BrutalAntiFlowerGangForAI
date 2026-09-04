#!/usr/bin/env python3
"""DOWOD LUKI: wnetrze f-stringa (i template literal JS) to KOD, ale
narzedzia traktuja caly f-string jako literal i go nie czyszcza.

Skutek: plik ktory DZIALAL przed Gangiem, po Gangu wybucha NameError,
bo definicja zmiennej (poza stringiem) zostala wyczyszczona, a jej
uzycie (wewnatrz f-stringa) NIE.

    PRZED:  vо = 7 ; print(f"wynik: {vо}")   -> dziala, wypisuje 7
    PO:     v  = 7 ; print(f"wynik: {vо}")   -> NameError

Uruchom:  python3 dev/luki/luka-fstring.py
Kod wyjscia: 0 = luka zalatana, 1 = luka nadal obecna.
"""
import io, os, shutil, subprocess, subprocess as sp, sys, tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
C = "\u043e"   # cyrylickie 'o'

PROBKI = [
    ("prosty",        'v%s = 7\nprint(f"wynik: {v%s}")\n' % (C, C),                   "wynik: 7"),
    ("format-spec",   'a%s = 1\nprint(f"{a%s:>3}".strip())\n' % (C, C),               "1"),
    ("zagniezdzony",  'n%s = 3\nprint(f"{ {i for i in range(n%s)} }")\n' % (C, C),    "{0, 1, 2}"),
    ("wielolinijkowy",'x%s = 2\nprint(f"""linia {x%s}""")\n' % (C, C),                "linia 2"),
    ("indeks",        'd = {"k": 1}\nk%s = "k"\nprint(f"{d[k%s]}")\n' % (C, C),       "1"),
]

def uruchom(sciezka):
    r = sp.run([sys.executable, sciezka], capture_output=True, text=True, timeout=60)
    return (r.stdout.strip() if r.returncode == 0 else "BLAD: " + (
        r.stderr.strip().splitlines()[-1] if r.stderr else "?"))

def main():
    narzedzie = os.path.join(KORZEN, "ZagladaKultury.py")
    tmp = tempfile.mkdtemp(prefix="luka-fstring-")
    zepsute = 0
    print("== LUKA: wnetrze f-stringa nie jest czyszczone ==")
    for nazwa, kod, oczekiwane in PROBKI:
        p = os.path.join(tmp, nazwa + ".py")
        io.open(p, "w", encoding="utf-8").write(kod)
        przed = uruchom(p)
        sp.run([sys.executable, narzedzie, "--zaglada", p],
               capture_output=True, text=True, timeout=300)
        po = uruchom(p)
        ok = (przed == po == oczekiwane)
        if not ok:
            zepsute += 1
        print("  %-15s %-8s przed=%-12s po=%s" % (
            nazwa, "OK" if ok else "ZEPSUTY", przed[:12], po[:40]))
    shutil.rmtree(tmp, ignore_errors=True)
    print("  --- zepsutych: %d / %d" % (zepsute, len(PROBKI)))
    return 1 if zepsute else 0

if __name__ == "__main__":
    sys.exit(main())

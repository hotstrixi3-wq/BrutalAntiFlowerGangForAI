# -*- coding: utf-8 -*-
"""fuzz-pogromcy: FUZZ x 3 tryby (tura 49, runda 2 - "test x 3").

A INIEKTOR   : losowa linia korpusu + losowy znak BLAD (probkowany z calego
               Unicode) -> analizuj MUSI zglosic blad.  X N iteracji.
B LEGALNY    : losowe zlozenie z palety/ogonkow/ASCII -> zero BLAD, zero UWAG.
C NFD        : polskie linie korpusu rozlozone do NFD -> po NFC w analizuj
               musza przejsc czysto (dekompozycja != kwiatek).
Determinizm: random.Random(seed) - ten sam wynik na kazdej maszynie.
Exit 1 przy jakimkolwiek potknieciu."""
import importlib.util
import io
import os
import random
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("pk", os.path.join(HERE, "PogromcaKwiatkow.py"))
pk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pk)

N = 500


def linie_korpusu():
    out = []
    for d in (os.path.dirname(HERE), HERE, os.path.join(os.path.dirname(HERE), "WIEDZA_O_PROGRAMIE")):
        for fn in sorted(os.listdir(d)):
            if fn.endswith((".md", ".txt")):
                p = os.path.join(d, fn)
                try:
                    out += [l for l in io.open(p, encoding="utf-8").read().splitlines() if l.strip()]
                except OSError:
                    pass
    return out


def main():
    rnd = random.Random(49)
    korpus = linie_korpusu()
    assert korpus, "pusty korpus"

    # pupa znakow BLAD: probe po calej BMP + wybrane zakresy wysokie
    kandydaci = []
    for cp in list(range(0x80, 0x10000, 7)) + list(range(0x10000, 0x110000, 541)):
        c = chr(cp)
        try:
            stan, _n = pk.klasyfikuj(c)
        except Exception:
            continue
        if stan == "BLAD":
            kandydaci.append(c)
    assert len(kandydaci) > 5000, len(kandydaci)

    PALIWO_LEGALNE = ([chr(c) for c in range(0x20, 0x7F)] +
                      sorted(pk.OGONKI) + sorted(pk.TYPO) + ["ą", "ż", "ć"])

    wyniki = {"A": [0, 0], "B": [0, 0], "C": [0, 0]}  # [ok, zle]
    for i in range(N):
        # A: iniekcja
        linia = rnd.choice(korpus)
        zly = rnd.choice(kandydaci)
        poz = rnd.randrange(len(linia) + 1)
        tekst = linia[:poz] + zly + linia[poz:]
        b, _u = pk.analizuj(tekst)
        wyniki["A"][0 if b else 1] += 1
        if not b:
            print("A-FAIL iter %d: brak wykrycia %r U+%04X" % (i, zly, ord(zly)))
        # B: legalny gesty
        dl = rnd.randrange(5, 80)
        tekst = "".join(rnd.choice(PALIWO_LEGALNE) for _ in range(dl))
        b, u = pk.analizuj(tekst)
        wyniki["B"][0 if not (b or u) else 1] += 1
        if b or u:
            print("B-FAIL iter %d: %r -> %r %r" % (i, tekst[:40], list(b)[:2], u[:2]))
        # C: NFD
        pl = [l for l in korpus if any(c in pk.OGONKI for c in l)]
        linia2 = rnd.choice(pl) if pl else rnd.choice(korpus)
        tekst = unicodedata.normalize("NFD", linia2)
        b, u = pk.analizuj(tekst)
        wyniki["C"][0 if not (b or u) else 1] += 1
        if b or u:
            print("C-FAIL iter %d: %r -> %r %r" % (i, tekst[:40], list(b)[:2], u[:2]))

    print("FUZZ x3 (po %d iteracji na tryb, seed 49):" % N)
    for k, (ok, zle) in wyniki.items():
        print("  %s: %d OK, %d FAIL" % (k, ok, zle))
    return 1 if any(z for _o, z in wyniki.values()) else 0


if __name__ == "__main__":
    sys.exit(main())

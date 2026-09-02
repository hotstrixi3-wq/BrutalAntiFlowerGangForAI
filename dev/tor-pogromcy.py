# -*- coding: utf-8 -*-
"""tor-pogromcy: TURNIEJ pogromcy kwiatkow (tura 49).

Suit atakow w pewniaki/kwiatki-testy/*.json (wektory od Kozakow-red/blue-team,
teksty zapisane wyłącznie ASCII + sekwencje \\uXXXX - json dekoduje sam).
Kazdy wektor: {"typ", "oczekiwane": "BLAD"|"OK", "tekst", "dlaczego"}.
Punktacja:
  FN  = oczekiwane BLAD, a pogromca nie dal BLAD (puscil calkiem lub tylko UWAGA)
  FP  = oczekiwane OK, a pogromca dal BLAD
  SZUM= oczekiwane OK, a pogromca dal UWAGA (pol-mila: raportuje niepotrzebnie)
Exit 1 gdy FN lub FP > 0.
"""
import glob
import importlib.util
import io
import json
import os
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # (v8.0.1) narzedzie w korzeniu repo, runnery w dev/
spec = importlib.util.spec_from_file_location("pk", os.path.join(ROOT, "PogromcaKwiatkow.py"))
pk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pk)


def opis_znakow(tekst):
    n = set()
    for c in tekst:
        o = ord(c)
        if o < 0x20 or o == 0x7F:
            n.add("%r U+%04X KONTROLNY" % (c, o))
            continue
        if o > 127 and not (c in pk.OGONKI or c in pk.TYPO):
            n.add("%s U+%04X %s" % (c, ord(c), unicodedata.name(c, "?")[:30]))
    return sorted(n)


def main():
    suity = sorted(glob.glob(os.path.join(HERE, "kwiatki-testy", "*.json")))
    assert suity, "brak suit w pewniaki/kwiatki-testy/"
    fn, fp, szum, ok = [], [], [], 0
    for suita in suity:
        wektory = json.loads(io.open(suita, encoding="utf-8").read())
        print("== %s: %d wektorow" % (os.path.basename(suita), len(wektory)))
        for w in wektory:
            if w.get("status", "").startswith(("ARBITRAZ", "POLITYKA")):
                print("  [ARBITRAZ] %s -> pominiety wg decyzji" % w["typ"])
                continue
            tekst = w["tekst"]
            ocze = w["oczekiwane"]
            bledy, uwagi = pk.analizuj(tekst)
            nazwa = w.get("typ", "?")
            if ocze == "BLAD":
                if bledy:
                    ok += 1
                else:
                    fn.append((nazwa, tekst, opis_znakow(tekst), w.get("dlaczego", "")))
            else:  # OK
                if bledy:
                    fp.append((nazwa, tekst, opis_znakow(tekst), sorted(bledy)))
                elif uwagi:
                    szum.append((nazwa, tekst, opis_znakow(tekst)))
                else:
                    ok += 1
    print()
    print("WYNIK TURNIEJU: trafione %d | FN %d | FP %d | SZUM %d" % (ok, len(fn), len(fp), len(szum)))
    for lista, tytul in ((fn, "FN - PUSCZONE KWIAKI (spryt do poprawy)"),
                         (fp, "FP - FALSZYWE ALARMY (nieomyslnosc do poprawy)"),
                         (szum, "SZUM - legalne, ale raportowane UWAGA")):
        if lista:
            print("\n%s:" % tytul)
            for poz in lista:
                print("  * %s" % poz[0])
                print("    znaki: %s" % (", ".join(poz[2][:4]) if poz[2] else "-"))
    return 1 if (fn or fp) else 0


if __name__ == "__main__":
    sys.exit(main())

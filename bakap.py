#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BAKAP - siatka bezpieczenstwa pod operacje, ktore niszcza nieodwracalnie.

Zasada domu brzmi "ZAWSZE ROB BAKAP", ale do tej pory nie bylo czym.
Ten plik to zmienia: jedna komenda robi pelna migawke repozytorium
(tresc + historia gita) POZA katalogiem roboczym, wiec przezywa nawet
`rm -rf` na repo.

Po co, skoro jest git? Bo git nie chroni przed samym gitem:

    git push --force    nadpisuje historie na zdalnym
    git reset --hard    kasuje niezacommitowane zmiany
    git checkout -- .   to samo, tylko ciszej
    git branch -D       kasuje galaz
    rm -rf              kasuje wszystko

Kazda z tych komend to jedna linijka i zaden z nich nie pyta "na pewno".
Nowy albo obcy agent, ktory nie zna tego repo, moze je wpisac w dobrej
wierze - i praca kilkudziesieciu godzin znika bez sladu.

Uzycie:
    python3 bakap.py                 # zrob migawke
    python3 bakap.py --lista         # co mam w zapasie
    python3 bakap.py --sprawdz       # czy ostatnia migawka jest swieza
    python3 bakap.py --przywroc N    # instrukcja przywrocenia (nie robi tego sam)
    python3 bakap.py --selftest

Migawki leza w ~/.bakap-gang/ - POZA repozytorium, wiec `rm -rf repo`
ich nie dotyka. Trzymamy 5 ostatnich, starsze kasujemy same.
"""

import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import time
from datetime import datetime

WERSJA = "1.0.1"

KORZEN = os.path.dirname(os.path.abspath(__file__))
# POZA repo - to jest caly sens
SKARBIEC = os.path.join(os.path.expanduser("~"), ".bakap-gang")
ILE_TRZYMAC = 5
SWIEZOSC_H = 4          # po ilu godzinach migawka jest "stara"


def _git(*a, cwd=None):
    try:
        r = subprocess.run(["git"] + list(a), capture_output=True, text=True,
                           cwd=cwd or KORZEN, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def opis_stanu():
    """Co dokladnie zapisujemy - zeby dalo sie potem poznac, co to za migawka."""
    return {
        "czas": datetime.now().isoformat(timespec="seconds"),
        "galaz": _git("rev-parse", "--abbrev-ref", "HEAD") or "?",
        "commit": _git("rev-parse", "HEAD") or "?",
        "commit_krotki": _git("rev-parse", "--short", "HEAD") or "?",
        "tytul": _git("log", "-1", "--format=%s") or "?",
        "brudne": bool(_git("status", "--porcelain")),
        "wersja_repo": _wersja_repo(),
    }


def _wersja_repo():
    try:
        d = json.load(io.open(os.path.join(KORZEN, "WERSJE.json"),
                              encoding="utf-8"))
        return d.get("repo", "?")
    except Exception:
        return "?"


def zrob(cichy=False):
    """Pelna migawka: tresc robocza + katalog .git (czyli cala historia)."""
    os.makedirs(SKARBIEC, exist_ok=True)
    stan = opis_stanu()
    znacznik = datetime.now().strftime("%Y%m%d-%H%M%S")
    nazwa = "gang-%s-%s" % (znacznik, stan["commit_krotki"])
    archiwum = os.path.join(SKARBIEC, nazwa + ".tar.gz")

    licznik = {"plikow": 0, "bajtow": 0}

    def filtruj(ti):
        # __pycache__ i smieci pomijamy, .git ZOSTAJE - to w nim jest historia
        if "__pycache__" in ti.name or ti.name.endswith(".pyc"):
            return None
        if ti.isfile():
            licznik["plikow"] += 1
            licznik["bajtow"] += ti.size
        return ti

    with tarfile.open(archiwum, "w:gz") as tf:
        tf.add(KORZEN, arcname="repo", filter=filtruj)

    io.open(os.path.join(SKARBIEC, nazwa + ".json"), "w",
            encoding="utf-8").write(
        json.dumps(dict(stan, plikow=licznik["plikow"],
                        rozmiar=os.path.getsize(archiwum)),
                   ensure_ascii=False, indent=2) + "\n")

    usuniete = _sprzataj()
    if not cichy:
        print("[BAKAP] %s" % nazwa)
        print("        %d plikow, %.1f MB, commit %s (%s)"
              % (licznik["plikow"], os.path.getsize(archiwum) / 1048576.0,
                 stan["commit_krotki"], stan["tytul"][:44]))
        if stan["brudne"]:
            print("        UWAGA: w drzewie sa niezacommitowane zmiany -")
            print("        migawka je zawiera, ale git ich nie zna")
        if usuniete:
            print("        skasowano %d najstarszych (trzymamy %d)"
                  % (usuniete, ILE_TRZYMAC))
    return archiwum


def _migawki():
    if not os.path.isdir(SKARBIEC):
        return []
    out = []
    for f in sorted(os.listdir(SKARBIEC)):
        if not f.endswith(".tar.gz"):
            continue
        p = os.path.join(SKARBIEC, f)
        meta = p[:-7] + ".json"
        dane = {}
        if os.path.exists(meta):
            try:
                dane = json.load(io.open(meta, encoding="utf-8"))
            except Exception:
                pass
        out.append((f[:-7], p, os.path.getmtime(p), dane))
    return out


def _sprzataj():
    m = _migawki()
    usuniete = 0
    for nazwa, p, _, _ in m[:-ILE_TRZYMAC] if len(m) > ILE_TRZYMAC else []:
        try:
            os.remove(p)
            meta = p[:-7] + ".json"
            if os.path.exists(meta):
                os.remove(meta)
            usuniete += 1
        except OSError:
            pass
    return usuniete


def lista():
    m = _migawki()
    if not m:
        print("Brak migawek. Zrob pierwsza: python3 bakap.py")
        return 1
    print("MIGAWKI w %s (trzymamy %d ostatnich)\n" % (SKARBIEC, ILE_TRZYMAC))
    for i, (nazwa, p, mtime, d) in enumerate(m, 1):
        wiek = (time.time() - mtime) / 3600.0
        print("  %d. %s" % (i, nazwa))
        print("     %s | commit %s | %s"
              % (d.get("czas", "?"), d.get("commit_krotki", "?"),
                 d.get("tytul", "?")[:46]))
        print("     %.1f MB | %d plikow | sprzed %.1f h%s"
              % (os.path.getsize(p) / 1048576.0, d.get("plikow", 0), wiek,
                 "  <- najnowsza" if i == len(m) else ""))
    return 0


def sprawdz():
    """Czy jest swieza migawka. Uzywane przez hooka pre-push."""
    m = _migawki()
    if not m:
        print("[BAKAP] BRAK MIGAWEK - zrob: python3 bakap.py")
        return 1
    nazwa, p, mtime, d = m[-1]
    wiek = (time.time() - mtime) / 3600.0
    biezacy = _git("rev-parse", "HEAD")
    if wiek > SWIEZOSC_H:
        print("[BAKAP] ostatnia migawka sprzed %.1f h (prog: %d h)"
              % (wiek, SWIEZOSC_H))
        print("        zrob nowa: python3 bakap.py")
        return 1
    if biezacy and d.get("commit") != biezacy:
        print("[BAKAP] migawka jest z commita %s, a HEAD to %s"
              % (d.get("commit_krotki", "?"), biezacy[:7]))
        print("        to normalne po commicie - zrob nowa przed pushem")
        return 1
    print("[BAKAP] OK - migawka %s sprzed %.1f h, commit sie zgadza"
          % (nazwa, wiek))
    return 0


def przywroc(numer):
    """NIE przywraca sam - drukuje instrukcje. Przywracanie to decyzja
    czlowieka, nie skutek uboczny wpisania numeru."""
    m = _migawki()
    try:
        nazwa, p, mtime, d = m[int(numer) - 1]
    except (ValueError, IndexError):
        print("[BLAD] nie ma migawki numer %r. Zobacz: python3 bakap.py --lista"
              % numer)
        return 1
    cel = os.path.join(os.path.dirname(KORZEN),
                       "PRZYWROCONE-" + d.get("commit_krotki", "x"))
    print("MIGAWKA %s" % nazwa)
    print("  z dnia %s, commit %s — %s"
          % (d.get("czas", "?"), d.get("commit_krotki", "?"),
             d.get("tytul", "?")[:50]))
    print()
    print("Rozpakuj OBOK repo (nie na nie!) i porownaj, zanim cokolwiek nadpiszesz:")
    print()
    print("  mkdir -p %s" % cel)
    print("  tar -xzf %s -C %s" % (p, cel))
    print("  diff -r %s/repo %s | head -40" % (cel, KORZEN))
    print()
    print("Dopiero gdy wiesz, co odzyskujesz, kopiuj pojedyncze pliki.")
    print("Nadpisywanie calego repo w ciemno to zamiana jednej straty na druga.")
    return 0


def selftest():
    import tempfile
    ok = True
    global SKARBIEC
    stary = SKARBIEC
    SKARBIEC = tempfile.mkdtemp(prefix="bakap-test-")
    try:
        a = zrob(cichy=True)
        if not os.path.exists(a):
            print("  [FAIL] nie powstalo archiwum"); ok = False
        # Czy .git jest w srodku - ale TYLKO gdy repo w ogole go ma.
        # (v1.0.1) Swiezo zalozony dom (zaloz-dom.py) nie ma jeszcze
        # historii: `git init` robi sie dopiero po rozpakowaniu. Wymaganie
        # .git w tescie oznaczalo, ze kazdy nowy dom startuje z czerwonym
        # selftestem - i uczy sie go ignorowac.
        with tarfile.open(a) as tf:
            nazwy = tf.getnames()
        if os.path.isdir(os.path.join(KORZEN, ".git")):
            if not any("/.git/" in n for n in nazwy):
                print("  [FAIL] repo ma .git, a migawka go nie zawiera -"
                      " odzyskanie historii nie bedzie mozliwe"); ok = False
        if not any(n.endswith("PogromcaKwiatkow.py") for n in nazwy):
            print("  [FAIL] migawka nie zawiera narzedzi"); ok = False
        if any("__pycache__" in n for n in nazwy):
            print("  [FAIL] migawka zawiera smieci"); ok = False
        # rotacja
        for _ in range(ILE_TRZYMAC + 2):
            time.sleep(1.05)
            zrob(cichy=True)
        if len(_migawki()) > ILE_TRZYMAC:
            print("  [FAIL] rotacja nie dziala: %d migawek" % len(_migawki()))
            ok = False
    finally:
        shutil.rmtree(SKARBIEC, ignore_errors=True)
        SKARBIEC = stary
    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--lista" in args:
        return lista()
    if "--sprawdz" in args:
        return sprawdz()
    if "--przywroc" in args:
        i = args.index("--przywroc")
        if i + 1 >= len(args):
            print("[BLAD] podaj numer: python3 bakap.py --przywroc 1")
            return 1
        return przywroc(args[i + 1])
    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0
    zrob()
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""TURNIEJ 8 — BRAMKI (te, ktore sprawdzaja wszystko inne).

Trzy narzedzia decyduja, czy wolno zrobic commit:

    sprawdz-teksty.py     zero zywych homoglifow w repo
    sprawdz-spojnosc.py   wersje w kodzie = WERSJE.json = dokumentacja
    pamietnik.py --sprawdz dziennik czytelny, cudze wpisy nietkniete

Zadne z nich nie mialo testu. To ta sama luka co przy zwiadzie: sprawdzam
nimi wszystko, a ich samych nie sprawdza nikt. Bramka, ktora falszywie
MILCZY, jest grozniejsza od jej braku - operator czyta cisze jako
"czysto" i wypycha zepsute repo z pelnym przekonaniem.

Kategorie:

  A. WYKRYWALNOSC   — czy kazda bramka LAPIE wstrzyknieta wade. Nie
                      "czy przepuszcza czyste repo" (to trywialne), tylko
                      czy potrafi ODMOWIC. Bramka bez tej zdolnosci jest
                      dekoracja.
  B. ZERO SZUMU     — czy na zdrowym repo milcza. Bramka, ktora krzyczy
                      bez powodu, zostanie wylaczona po drugim razie
                      (zmierzone: wersja audytora dawala 94 falszywe).
  C. ZASIEG         — czy pomijaja TYLKO to, co musza. Pomijanie
                      nadmiarowe = dziura, przez ktora przejdzie brud.
  D. ODPORNOSC      — czy nie wywracaja sie na dziwnym wejsciu.
  E. UCZCIWOSC      — czy kod wyjscia zgadza sie z trescia raportu.
                      Bramka mowiaca "ROZJAZDY: 3" i konczaca exit 0
                      klamie kodem wyjscia.

Uzycie:  python3 dev/turnieje/turniej-8-bramki.py
Wyjscie: 0 = bramkom mozna ufac, 1 = ktoras zawodzi.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

C = "\u043e"   # cyrylickie o
A = "\u0430"   # cyrylickie a
ZW = "\u200b"


def uruchom(args, cwd=None):
    try:
        r = subprocess.run([sys.executable] + args, capture_output=True,
                           text=True, timeout=180, cwd=cwd)
        return r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"


def kopia_repo(prefix):
    """Kopia repo w katalogu, ktorego RODZIC jest pusty - inaczej skanery
    zlapia cudze pliki z /tmp (patrz dziennik).

    Kopiujemy BEZ .git i zakladamy nowe repozytorium z commitem. Powod:
    sprawdz-teksty.py pyta `git ls-files`, ktore poza repozytorium nie
    zwraca nic - a bramka od v1.1.0 slusznie ODMAWIA pracy, gdy nie wie,
    co sprawdzic. Kopia bez .git badalaby wiec sytuacje sztuczna, nie te,
    w ktorej bramka realnie pracuje."""
    baza = tempfile.mkdtemp(prefix=prefix)
    cel = os.path.join(baza, "repo")
    shutil.copytree(KORZEN, cel,
                    ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
    for cmd in (["init", "-q"], ["add", "-A"],
                ["-c", "user.email=t8@local", "-c", "user.name=T8",
                 "commit", "-q", "-m", "stan bazowy do testu bramek"]):
        subprocess.run(["git"] + cmd, cwd=cel, capture_output=True, text=True)
    return baza, cel


# =====================================================================
# A. WYKRYWALNOSC — czy bramka potrafi ODMOWIC
# =====================================================================
def kat_a():
    zle = 0
    szczegoly = []

    # --- sprawdz-teksty: wstrzykniety homoglif w pilnowanym pliku ---
    baza, repo = kopia_repo("t8a1-")
    p = os.path.join(repo, "README.md")
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(s.replace("Pogromca", "P%sgromca" % C, 1))
    kod, out = uruchom([os.path.join(repo, "sprawdz-teksty.py")], cwd=repo)
    if kod != 1:
        zle += 1
        szczegoly.append(("sprawdz-teksty", "PRZEPUSCILA homoglif w README (exit=%d)" % kod))
    shutil.rmtree(baza, ignore_errors=True)

    # --- sprawdz-spojnosc: rozjazd stalej WERSJA ---
    baza, repo = kopia_repo("t8a2-")
    p = os.path.join(repo, "ZagladaKultury.py")
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(
        s.replace('WERSJA = "1.4.0"', 'WERSJA = "9.9.9"', 1))
    kod, out = uruchom([os.path.join(repo, "sprawdz-spojnosc.py")], cwd=repo)
    if kod != 1 or "9.9.9" not in out:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "nie zlapala rozjazdu WERSJA (exit=%d)" % kod))
    shutil.rmtree(baza, ignore_errors=True)

    # --- sprawdz-spojnosc: rozjechana OSADZONA KOPIA ---
    baza, repo = kopia_repo("t8a3-")
    p = os.path.join(repo, "docs", "czlowiek", "RODZINA-DO-CZATU.md")
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(
        s.replace("def main()", "def main_PODMIENIONE()", 1))
    kod, out = uruchom([os.path.join(repo, "sprawdz-spojnosc.py")], cwd=repo)
    if kod != 1:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "nie zlapala podmiany osadzonej kopii"))
    shutil.rmtree(baza, ignore_errors=True)

    # --- pamietnik: wpis bez wymaganego pola ---
    baza, repo = kopia_repo("t8a4-")
    dz = os.path.join(repo, "dziennik")
    plik = [f for f in os.listdir(dz) if f.endswith(".md") and "__" in f][0]
    io.open(os.path.join(dz, plik), "a", encoding="utf-8").write(
        "\n### [2026-01-01] Wpis celowo niekompletny testowy\n"
        "**Temat:** kod\n**Objaw:** brakuje przyczyny i wniosku\n")
    kod, out = uruchom([os.path.join(repo, "pamietnik.py"), "--sprawdz"], cwd=repo)
    # UWAGA: samo exit=1 nie wystarcza. Dopisanie wpisu zmienia plik
    # dziennika, wiec bramka i tak krzyknie "RUSZONY CUDZY DZIENNIK" -
    # i test przechodzilby nawet z calkiem wylaczona kontrola pol.
    # Musimy zobaczyc komunikat O TYM konkretnym bledzie.
    if kod != 1 or "brakuje pola" not in out:
        zle += 1
        szczegoly.append(("pamietnik",
                          "nie zglosil BRAKU POL (exit=%d, komunikat o polach: %s)"
                          % (kod, "brakuje pola" in out)))
    shutil.rmtree(baza, ignore_errors=True)

    # --- pamietnik: odsylacz Zastepuje w prozne ---
    baza, repo = kopia_repo("t8a5-")
    dz = os.path.join(repo, "dziennik")
    plik = [f for f in os.listdir(dz) if f.endswith(".md") and "__" in f][0]
    io.open(os.path.join(dz, plik), "a", encoding="utf-8").write(
        "\n### [2026-01-02] Wpis ze zlym odsylaczem testowy\n**Temat:** kod\n"
        "**Zastepuje:** Nie ma takiego wpisu w dzienniku\n"
        "**Objaw:** a\n**Przyczyna:** b\n**Wniosek:** c\n")
    kod, out = uruchom([os.path.join(repo, "pamietnik.py"), "--sprawdz"], cwd=repo)
    if kod != 1 or "nieistniejacy wpis" not in out:
        zle += 1
        szczegoly.append(("pamietnik",
                          "nie zglosil ODSYLACZA W PROZNE (exit=%d)" % kod))
    shutil.rmtree(baza, ignore_errors=True)

    # --- sprawdz-teksty: FAIL-CLOSED gdy nie wie, co sprawdzic ---
    # Do v1.0.0 `git ls-files` poza repo zwracalo pustke, petla nie robila
    # ani jednego obiegu, a bramka meldowala "zero kwiatkow" z exit 0.
    baza, repo = kopia_repo("t8a6-")
    shutil.rmtree(os.path.join(repo, ".git"), ignore_errors=True)
    p = os.path.join(repo, "README.md")
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(s.replace("Pogromca", "P%sgromca" % C, 1))
    kod, out = uruchom([os.path.join(repo, "sprawdz-teksty.py")], cwd=repo)
    if kod == 0:
        zle += 1
        szczegoly.append(("sprawdz-teksty",
                          "FAIL-OPEN: bez listy plikow melduje sukces (exit=0) "
                          "mimo homoglifa w README"))
    shutil.rmtree(baza, ignore_errors=True)

    print("== A. WYKRYWALNOSC (czy bramka umie ODMOWIC) ==")
    print("   prob: 6 | bramek slepych: %d" % zle)
    for n, o in szczegoly:
        print("     [SLEPA] %s: %s" % (n, o))
    return zle


# =====================================================================
# B. ZERO SZUMU — czy na zdrowym repo milcza
# =====================================================================
def kat_b():
    zle = 0
    szczegoly = []
    baza, repo = kopia_repo("t8b-")
    for nazwa, args in (("sprawdz-teksty", ["sprawdz-teksty.py"]),
                        ("sprawdz-spojnosc", ["sprawdz-spojnosc.py"]),
                        ("pamietnik", ["pamietnik.py", "--sprawdz"])):
        kod, out = uruchom([os.path.join(repo, args[0])] + args[1:], cwd=repo)
        if kod != 0:
            zle += 1
            pierwsza = [l for l in out.split("\n") if "BLAD" in l or "ROZJAZD" in l]
            szczegoly.append((nazwa, "FALSZYWY ALARM na zdrowym repo (exit=%d): %s"
                              % (kod, pierwsza[0][:60] if pierwsza else "")))
    shutil.rmtree(baza, ignore_errors=True)
    print("== B. ZERO SZUMU (zdrowe repo) ==")
    print("   bramek: 3 | falszywych alarmow: %d" % zle)
    for n, o in szczegoly:
        print("     [SZUM] %s: %s" % (n, o))
    return zle


# =====================================================================
# C. ZASIEG — czy pomijaja tylko to, co musza
# =====================================================================
def kat_c():
    zle = 0
    szczegoly = []

    # 1. sprawdz-teksty pomija cale dev/turnieje/ - ale wiekszosc tych
    #    plikow NIE zawiera skazen, wiec pomijanie jest nadmiarowe.
    #    Test: wstrzykniety homoglif do turnieju, ktory jest czysty.
    baza, repo = kopia_repo("t8c1-")
    cel = os.path.join(repo, "dev", "turnieje", "turniej-6-prokurator.py")
    s = io.open(cel, encoding="utf-8").read()
    io.open(cel, "w", encoding="utf-8").write(
        s.replace("def main()", "def m%sin()" % A, 1))
    kod, out = uruchom([os.path.join(repo, "sprawdz-teksty.py")], cwd=repo)
    if kod == 0:
        zle += 1
        szczegoly.append(("sprawdz-teksty",
                          "homoglif w dev/turnieje/ przechodzi - pomijanie "
                          "obejmuje pliki, ktore skazen nie potrzebuja"))
    shutil.rmtree(baza, ignore_errors=True)

    # 2. sprawdz-spojnosc pilnuje 6 plikow, a wersje deklaruje wiecej.
    #    Test: klamstwo w BRIEFIE dla audytora - pliku wysylanym na zewnatrz.
    baza, repo = kopia_repo("t8c2-")
    brief = os.path.join(repo, "docs", "BRIEF-DLA-AUDYTORA.md")
    if os.path.exists(brief):
        s = io.open(brief, encoding="utf-8").read()
        io.open(brief, "w", encoding="utf-8").write(
            s.replace("ProkuratorOgrodnik.py v", "ProkuratorOgrodnik.py v0.0.1 nieprawda v", 1))
        kod, out = uruchom([os.path.join(repo, "sprawdz-spojnosc.py")], cwd=repo)
        if kod == 0:
            zle += 1
            szczegoly.append(("sprawdz-spojnosc",
                              "falszywa wersja w docs/agent/BRIEF-DLA-AUDYTORA.md "
                              "przechodzi - plik jest POZA WARSTWA_AGENTA"))
    shutil.rmtree(baza, ignore_errors=True)

    print("== C. ZASIEG (czy pomijaja tylko to, co musza) ==")
    print("   prob: 2 | dziur: %d" % zle)
    for n, o in szczegoly:
        print("     [DZIURA] %s: %s" % (n, o))
    return zle


# =====================================================================
# D. ODPORNOSC
# =====================================================================
def kat_d():
    zle = 0
    szczegoly = []
    baza, repo = kopia_repo("t8d-")

    # plik binarny w repo
    io.open(os.path.join(repo, "smiec.md"), "wb").write(bytes(range(256)))
    # plik pusty
    io.open(os.path.join(repo, "pusty.md"), "w").close()
    # WERSJE.json uszkodzony
    kod1, out1 = uruchom([os.path.join(repo, "sprawdz-teksty.py")], cwd=repo)
    if "Traceback" in out1:
        zle += 1
        szczegoly.append(("sprawdz-teksty", "traceback na pliku binarnym/pustym"))

    io.open(os.path.join(repo, "WERSJE.json"), "w", encoding="utf-8").write("{zepsuty")
    kod2, out2 = uruchom([os.path.join(repo, "sprawdz-spojnosc.py")], cwd=repo)
    if "Traceback" in out2:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "traceback na zepsutym WERSJE.json"))
    elif kod2 == 0:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "zepsuty WERSJE.json a exit=0 (fail-open!)"))

    dz = os.path.join(repo, "dziennik")
    io.open(os.path.join(dz, "2026-01-01__pusty.md"), "w").close()
    kod3, out3 = uruchom([os.path.join(repo, "pamietnik.py"), "--sprawdz"], cwd=repo)
    if "Traceback" in out3:
        zle += 1
        szczegoly.append(("pamietnik", "traceback na pustym pliku sesji"))

    shutil.rmtree(baza, ignore_errors=True)
    print("== D. ODPORNOSC (dziwne wejscie) ==")
    print("   awarii: %d" % zle)
    for n, o in szczegoly:
        print("     [AWARIA] %s: %s" % (n, o))
    return zle


# =====================================================================
# E. UCZCIWOSC — kod wyjscia zgodny z trescia
# =====================================================================
def kat_e():
    zle = 0
    szczegoly = []
    baza, repo = kopia_repo("t8e-")

    # wstrzykujemy JEDNA wade i sprawdzamy, czy raport i exit sie zgadzaja
    p = os.path.join(repo, "PROTOKOL-OPERATORA.md")
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(s.replace("Zaglada", "Z%sglada" % A, 1))

    kod, out = uruchom([os.path.join(repo, "sprawdz-teksty.py")], cwd=repo)
    mowi_o_bledzie = "[BLAD]" in out or "ZYWE skazenie" in out
    if mowi_o_bledzie and kod == 0:
        zle += 1
        szczegoly.append(("sprawdz-teksty", "raport mowi o bledzie, a exit=0"))
    if not mowi_o_bledzie and kod != 0:
        zle += 1
        szczegoly.append(("sprawdz-teksty", "exit!=0, a raport nic nie mowi"))
    shutil.rmtree(baza, ignore_errors=True)

    # to samo dla spojnosci
    baza2, repo2 = kopia_repo("t8e2-")
    p2 = os.path.join(repo2, "ProkuratorOgrodnik.py")
    s2 = io.open(p2, encoding="utf-8").read()
    io.open(p2, "w", encoding="utf-8").write(
        s2.replace('WERSJA = "1.3.1"', 'WERSJA = "7.7.7"', 1))
    kod2, out2 = uruchom([os.path.join(repo2, "sprawdz-spojnosc.py")], cwd=repo2)
    ile = out2.count("[ROZJAZD]")
    if ile > 0 and kod2 == 0:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "%d rozjazdow w raporcie, a exit=0" % ile))
    if ile == 0 and kod2 != 0:
        zle += 1
        szczegoly.append(("sprawdz-spojnosc", "exit!=0 bez ani jednego rozjazdu"))
    shutil.rmtree(baza2, ignore_errors=True)

    print("== E. UCZCIWOSC (exit zgodny z raportem) ==")
    print("   niezgodnosci: %d" % zle)
    for n, o in szczegoly:
        print("     [KLAMSTWO] %s: %s" % (n, o))
    return zle


def main():
    print("=" * 68)
    print("TURNIEJ 8 — BRAMKI (kto pilnuje pilnujacych)")
    print("=" * 68)
    zle = kat_a() + kat_b() + kat_c() + kat_d() + kat_e()
    print()
    print("=" * 68)
    print("FINAL T8: %s" % ("BRAMKOM MOZNA UFAC" if not zle
                            else "BRAMKI ZAWODZA — %d przypadkow" % zle))
    print("=" * 68)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())

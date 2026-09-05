#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DZIENNIK OPERATORA - pamiec miedzy sesjami agentow.

MODEL PRACY (v2.0.0)
--------------------
Kazda sesja pisze do WLASNEGO pliku w `dziennik/`:

    dziennik/2026-09-04__01a06e18.md

Zasady, ktore z tego wynikaja:

1. **Piszesz tylko do swojego pliku.** Tworzy sie sam przy pierwszym
   `--dodaj`. Nazwa bierze sie z daty i identyfikatora sesji (galaz gita
   albo zmienna PAMIETNIK_SESJA).
2. **Cudze pliki sa nietykalne.** `--sprawdz` porownuje je z gitem i
   zglasza kazda zmiane. Nie chodzi o zakaz techniczny (w gicie takiego
   nie ma), tylko o wykrywalnosc: jesli ktos ruszy cudzy wpis, bramka to
   pokaze przed commitem.
3. **Ale wolno prostowac.** Nie edytujesz cudzego pliku - dopisujesz
   WLASNY wpis z polem `**Zastepuje:**` i tytulem starego. Widok scalony
   oznaczy tamten jako NIEAKTUALNY i pokaze, co go zastapilo. Zla rada
   przestaje szkodzic, a historia pomylki zostaje.
4. **Czytasz wszystko naraz.** Trzydziesci osobnych plikow to trzydziesci
   plikow, ktorych nikt nie otworzy. Domyslny widok scala je w jeden,
   pogrupowany tematami.

Uzycie:
    python3 pamietnik.py                  # widok scalony (wszystkie sesje)
    python3 pamietnik.py --temat testy    # tylko jeden temat
    python3 pamietnik.py --szukaj SLOWO   # przeszukaj wszystkie sesje
    python3 pamietnik.py --sesje          # lista sesji z liczba wpisow
    python3 pamietnik.py --moje           # wpisy z biezacej sesji
    python3 pamietnik.py --dodaj          # dopisz wpis (pyta o pola)
    python3 pamietnik.py --sprawdz        # format + nietykalnosc cudzych
    python3 pamietnik.py --indeks         # odswiez PAMIETNIK-OPERATORA.md
    python3 pamietnik.py --stan           # odswiez fakty w STAN-SESJI.md
    python3 pamietnik.py --selftest

Dopisanie bez pytan (dla agenta w skrypcie):
    python3 pamietnik.py --dodaj --temat testy --tytul "..." \\
        --objaw "..." --przyczyna "..." --wniosek "..."
"""

import io
import os
import re
import subprocess
import sys
from datetime import date

WERSJA = "2.1.1"

KORZEN = os.path.dirname(os.path.abspath(__file__))
DZIENNIK = os.path.join(KORZEN, "dziennik")
INDEKS = os.path.join(KORZEN, "PAMIETNIK-OPERATORA.md")

TEMATY = {
    "repo": "Praca z repozytorium i narzedziami agenta",
    "testy": "Pisanie testow dla tej rodziny",
    "kod": "Pulapki w samym kodzie rodziny",
    "dokumentacja": "Dokumentacja i bramki",
    "wspolpraca": "Wspolpraca z operatorem-czlowiekiem",
}

WZOR_WPISU = re.compile(r"^### \[(\d{4}-\d{2}-\d{2})\] (.+)$")
POLA_WYMAGANE = ("Temat", "Objaw", "Przyczyna", "Wniosek")


# ------------------------------------------------------------ sesja
def id_sesji():
    """Identyfikator biezacej sesji: zmienna srodowiskowa albo galaz gita."""
    jawny = os.environ.get("PAMIETNIK_SESJA", "").strip()
    if jawny:
        return re.sub(r"[^A-Za-z0-9_-]", "-", jawny)[:40]
    try:
        r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                           capture_output=True, text=True, cwd=KORZEN, timeout=15)
        galaz = r.stdout.strip()
    except Exception:
        galaz = ""
    if not galaz or galaz == "HEAD":
        return "lokalna"
    # arena/01a06e18-nazwa-repo -> 01a06e18
    ogon = galaz.split("/")[-1]
    m = re.match(r"([0-9a-f]{6,})", ogon)
    return m.group(1) if m else re.sub(r"[^A-Za-z0-9_-]", "-", ogon)[:40]


def plik_sesji(sesja=None, dzien=None):
    sesja = sesja or id_sesji()
    dzien = dzien or date.today().isoformat()
    return os.path.join(DZIENNIK, "%s__%s.md" % (dzien, sesja))


def moj_plik():
    """Sciezka pliku biezacej sesji - istniejacego (z dowolnego dnia) lub nowego."""
    sesja = id_sesji()
    for f in sorted(pliki_dziennika()):
        if f.endswith("__%s.md" % sesja):
            return os.path.join(DZIENNIK, os.path.basename(f))
    return plik_sesji(sesja)


def pliki_dziennika():
    if not os.path.isdir(DZIENNIK):
        return []
    return sorted(os.path.join(DZIENNIK, f) for f in os.listdir(DZIENNIK)
                  if f.endswith(".md") and "__" in f)


# ------------------------------------------------------------ odczyt
def wpisy_z_pliku(sciezka):
    """[{data,tytul,temat,tresc,pola,sesja,plik}]"""
    try:
        tekst = io.open(sciezka, encoding="utf-8").read()
    except OSError:
        return []
    nazwa = os.path.basename(sciezka)
    sesja = nazwa[:-3].split("__")[-1]
    linie = tekst.split("\n")
    wynik = []
    for i, linia in enumerate(linie):
        m = WZOR_WPISU.match(linia)
        if not m:
            continue
        tresc = []
        for j in range(i + 1, len(linie)):
            if WZOR_WPISU.match(linie[j]):
                break
            tresc.append(linie[j])
        blok = "\n".join(tresc).strip()
        pola = {}
        for p in re.finditer(r"^\*\*([A-Za-zzZ]+):\*\*\s*(.*)$", blok, re.M):
            pola[p.group(1)] = p.group(2).strip()
        # wieloliniowe wartosci pol
        for klucz in list(pola):
            wzor = re.search(r"\*\*%s:\*\*(.*?)(?=\n\*\*[A-Za-z]+:\*\*|\Z)"
                             % klucz, blok, re.S)
            if wzor:
                pola[klucz] = " ".join(wzor.group(1).split())
        wynik.append({
            "data": m.group(1), "tytul": m.group(2).strip(),
            "temat": pola.get("Temat", "").lower() or "repo",
            "zastepuje": pola.get("Zastepuje", ""),
            "pola": pola, "tresc": blok, "sesja": sesja, "plik": sciezka,
        })
    return wynik


def wszystkie_wpisy():
    w = []
    for f in pliki_dziennika():
        w.extend(wpisy_z_pliku(f))
    w.sort(key=lambda x: (x["data"], x["sesja"]))
    return w


def mapa_zastapien(wpisy):
    """{tytul_starego: wpis_ktory_go_zastepuje}"""
    m = {}
    for w in wpisy:
        if w["zastepuje"]:
            m[w["zastepuje"].strip().strip('"').lower()] = w
    return m


# ------------------------------------------------------------ widoki
def _drukuj_wpis(w, zastapiony_przez=None, wciecie="  "):
    znacznik = " [NIEAKTUALNY]" if zastapiony_przez else ""
    print("%s[%s] %s%s" % (wciecie, w["data"], w["tytul"], znacznik))
    print("%s    sesja: %s" % (wciecie, w["sesja"]))
    if zastapiony_przez:
        print("%s    ZASTAPIONY przez wpis z %s: %s"
              % (wciecie, zastapiony_przez["data"], zastapiony_przez["tytul"]))
    for pole in ("Objaw", "Przyczyna", "Wniosek"):
        if pole in w["pola"]:
            tekst = w["pola"][pole]
            print("%s    %-10s %s" % (wciecie, pole + ":", tekst[:150]))
    print()


def widok_scalony(temat=None):
    wpisy = wszystkie_wpisy()
    if not wpisy:
        print("Dziennik jest pusty. Pierwszy wpis: python3 pamietnik.py --dodaj")
        return 0
    zast = mapa_zastapien(wpisy)
    print("DZIENNIK OPERATORA - %d wpisow z %d sesji\n"
          % (len(wpisy), len(pliki_dziennika())))
    for klucz, opis in TEMATY.items():
        if temat and klucz != temat:
            continue
        grupa = [w for w in wpisy if w["temat"] == klucz]
        if not grupa:
            continue
        print("== %s (%s) ==" % (opis, klucz))
        for w in grupa:
            _drukuj_wpis(w, zast.get(w["tytul"].strip().lower()))
    nieznane = [w for w in wpisy if w["temat"] not in TEMATY]
    if nieznane and not temat:
        print("== Bez rozpoznanego tematu ==")
        for w in nieznane:
            _drukuj_wpis(w, zast.get(w["tytul"].strip().lower()))
    return 0


def widok_sesji():
    pliki = pliki_dziennika()
    if not pliki:
        print("Brak sesji w dziennik/.")
        return 0
    biezaca = os.path.basename(moj_plik())
    print("SESJE W DZIENNIKU:\n")
    for f in pliki:
        w = wpisy_z_pliku(f)
        nazwa = os.path.basename(f)
        znacznik = "  <- TWOJA (zapis)" if nazwa == biezaca else "     (tylko odczyt)"
        print("  %-34s %2d wpisow%s" % (nazwa, len(w), znacznik))
    return 0


def widok_moje():
    f = moj_plik()
    if not os.path.exists(f):
        print("Twoja sesja nie ma jeszcze pliku (%s)." % os.path.basename(f))
        print("Pierwszy wpis: python3 pamietnik.py --dodaj")
        return 0
    w = wpisy_z_pliku(f)
    print("TWOJA SESJA: %s - %d wpisow\n" % (os.path.basename(f), len(w)))
    for x in w:
        _drukuj_wpis(x)
    return 0


def szukaj(fraza):
    f = fraza.lower()
    wpisy = wszystkie_wpisy()
    zast = mapa_zastapien(wpisy)
    traf = [w for w in wpisy if f in w["tytul"].lower() or f in w["tresc"].lower()]
    if not traf:
        print("Brak wpisow dla %r." % fraza)
        return 1
    print("Znaleziono %d wpisow dla %r:\n" % (len(traf), fraza))
    for w in traf:
        _drukuj_wpis(w, zast.get(w["tytul"].strip().lower()))
    return 0


# ------------------------------------------------------------ zapis
def naglowek_pliku(sesja, dzien):
    return (
        "# Dziennik sesji %s (%s)\n\n"
        "Plik nalezy do JEDNEJ sesji agenta i jest dopisywany tylko przez nia.\n"
        "Inne sesje maja go **tylko do odczytu** - `python3 pamietnik.py --sprawdz`\n"
        "zglasza kazda zmiane w cudzym pliku.\n\n"
        "Prostowanie cudzego wpisu: nie edytuj tamtego pliku, dopisz wlasny wpis\n"
        "z polem `**Zastepuje:** <tytul starego wpisu>`.\n\n"
        "---\n" % (sesja, dzien))


def dodaj(temat, tytul, objaw, przyczyna, wniosek, zastepuje="", sciezka=None):
    sciezka = sciezka or moj_plik()
    os.makedirs(os.path.dirname(sciezka), exist_ok=True)
    nowy = not os.path.exists(sciezka)
    if nowy:
        nazwa = os.path.basename(sciezka)[:-3]
        dzien, sesja = nazwa.split("__")
        io.open(sciezka, "w", encoding="utf-8").write(naglowek_pliku(sesja, dzien))
    blok = ["", "### [%s] %s" % (date.today().isoformat(), tytul),
            "**Temat:** %s" % temat]
    if zastepuje:
        blok.append("**Zastepuje:** %s" % zastepuje)
    blok += ["**Objaw:** %s" % objaw,
             "**Przyczyna:** %s" % przyczyna,
             "**Wniosek:** %s" % wniosek, ""]
    with io.open(sciezka, "a", encoding="utf-8") as fh:
        fh.write("\n".join(blok))
    return sciezka


def dodaj_interaktywnie():
    print("Tematy:")
    for k, v in TEMATY.items():
        print("   %-14s %s" % (k, v))
    print("\nPiszesz do: %s\n" % os.path.basename(moj_plik()))
    try:
        temat = input("Temat: ").strip().lower()
        tytul = input("Tytul (krotko, czego dotyczy): ").strip()
        objaw = input("Objaw (co zobaczyles - konkretnie): ").strip()
        przyczyna = input("Przyczyna (dlaczego tak bylo): ").strip()
        wniosek = input("Wniosek (co robic nastepnym razem): ").strip()
        zastepuje = input("Zastepuje wpis (tytul, ENTER = zaden): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n[ANULOWANO]")
        return 1
    if temat not in TEMATY:
        print("[BLAD] nieznany temat %r. Dostepne: %s"
              % (temat, ", ".join(TEMATY)))
        return 1
    if not all([tytul, objaw, przyczyna, wniosek]):
        print("[BLAD] wszystkie pola sa wymagane - wpis bez ktoregos z nich "
              "jest bezuzyteczny dla nastepnego agenta")
        return 1
    p = dodaj(temat, tytul, objaw, przyczyna, wniosek, zastepuje)
    print("\n[OK] Wpis dopisany do %s" % os.path.basename(p))
    return 0


# ------------------------------------------------------------ kontrola
def _zmienione_wzgledem_gita():
    """Pliki dziennika zmienione/usuniete wzgledem HEAD."""
    try:
        r = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", "dziennik/"],
                           capture_output=True, text=True, cwd=KORZEN, timeout=20)
        if r.returncode != 0:
            return []
        return [x.strip() for x in r.stdout.split("\n") if x.strip()]
    except Exception:
        return []


def sprawdz(cicho=False):
    problemy = []
    wpisy = wszystkie_wpisy()
    if not wpisy:
        # (v2.1.1) Pusty dziennik to NIE blad - to stan swiezo zalozonego
        # domu (patrz zaloz-dom.py). Bramka ma pilnowac formatu wpisow,
        # a nie zmuszac do pisania ich na sile. Zglaszamy informacyjnie
        # i konczymy sukcesem, inaczej kazdy nowy dom startuje z czerwona
        # bramka i uczy sie ja ignorowac.
        if not cicho:
            print("DZIENNIK: pusty - to normalne w nowym domu.")
            print("          Pierwszy wpis: python3 pamietnik.py --dodaj")
        return 0

    # NIETYKALNOSC cudzych plikow - sprawdzana PIERWSZA i pokazywana na
    # gorze. Gdy ktos podmieni cudzy dziennik, posypia sie tez duplikaty
    # tytulow i braki pol; bez tego wlasciwa przyczyna ginie w szumie.
    # Kontrola dotyczy tylko PRAWDZIWEGO dziennika repo - selftest pracuje
    # na katalogu tymczasowym, ktorego git nie zna.
    if os.path.abspath(DZIENNIK) == os.path.join(KORZEN, "dziennik"):
        biezacy = os.path.relpath(moj_plik(), KORZEN).replace(os.sep, "/")
        for zmieniony in _zmienione_wzgledem_gita():
            if zmieniony != biezacy:
                problemy.append("RUSZONY CUDZY DZIENNIK: %s - cudze sesje sa "
                                "tylko do odczytu; prostuj wpisem "
                                "**Zastepuje:** we wlasnym pliku (%s)"
                                % (zmieniony, os.path.basename(biezacy)))

    tytuly = set()
    for w in wpisy:
        for pole in POLA_WYMAGANE:
            if pole not in w["pola"] or not w["pola"][pole]:
                problemy.append("[%s] %s - brakuje pola **%s:**"
                                % (w["sesja"], w["tytul"][:44], pole))
        if w["temat"] not in TEMATY:
            problemy.append("[%s] %s - nieznany temat %r"
                            % (w["sesja"], w["tytul"][:44], w["temat"]))
        if len(w["tytul"]) < 8:
            problemy.append("[%s] tytul za krotki, nic nie mowi" % w["sesja"])
        klucz = w["tytul"].strip().lower()
        if klucz in tytuly:
            problemy.append("[%s] duplikat tytulu: %s" % (w["sesja"], w["tytul"][:44]))
        tytuly.add(klucz)

    # odsylacze Zastepuje musza wskazywac na istniejacy wpis
    for w in wpisy:
        if w["zastepuje"] and w["zastepuje"].strip().strip('"').lower() not in tytuly:
            problemy.append("[%s] %s - Zastepuje wskazuje na nieistniejacy wpis %r"
                            % (w["sesja"], w["tytul"][:34], w["zastepuje"][:40]))

    if not cicho:
        if problemy:
            print("DZIENNIK: %d problemow" % len(problemy))
            for p in problemy:
                print("  [BLAD] %s" % p)
        else:
            print("DZIENNIK: %d wpisow z %d sesji - format poprawny, "
                  "cudze pliki nietkniete" % (len(wpisy), len(pliki_dziennika())))
    return len(problemy)


def zbuduj_indeks():
    """Odswieza PAMIETNIK-OPERATORA.md - spis tresci calego dziennika."""
    wpisy = wszystkie_wpisy()
    zast = mapa_zastapien(wpisy)
    L = ["# PAMIETNIK OPERATORA - spis tresci dziennika", "",
         "**Ten plik jest generowany.** Nie edytuj go recznie -",
         "`python3 pamietnik.py --indeks` nadpisze zmiany.", "",
         "Wpisy zyja w `dziennik/`, po jednym pliku na sesje agenta.",
         "Piszesz tylko do swojego pliku; cudze sa do odczytu.",
         "Pelny opis modelu pracy: `dziennik/README.md`.", "",
         "```", "python3 pamietnik.py              # widok scalony",
         "python3 pamietnik.py --szukaj SLOWO",
         "python3 pamietnik.py --dodaj      # dopisz do swojej sesji",
         "python3 pamietnik.py --sprawdz    # bramka przed commitem", "```", "",
         "Stan: **%d wpisow** z **%d sesji**." % (len(wpisy), len(pliki_dziennika())),
         ""]
    for klucz, opis in TEMATY.items():
        grupa = [w for w in wpisy if w["temat"] == klucz]
        if not grupa:
            continue
        L += ["## %s" % opis, ""]
        for w in grupa:
            n = " **[NIEAKTUALNY]**" if zast.get(w["tytul"].strip().lower()) else ""
            L.append("- [%s] **%s**%s" % (w["data"], w["tytul"], n))
            if "Wniosek" in w["pola"]:
                L.append("  - %s" % w["pola"]["Wniosek"][:200])
            L.append("  - `%s`" % os.path.basename(w["plik"]))
        L.append("")
    io.open(INDEKS, "w", encoding="utf-8").write("\n".join(L))
    print("[OK] %s odswiezony (%d wpisow)" % (os.path.basename(INDEKS), len(wpisy)))
    return 0


# ------------------------------------------------------------ selftest
def selftest():
    import shutil
    import tempfile
    global DZIENNIK, INDEKS
    stary_d, stary_i = DZIENNIK, INDEKS
    tmp = tempfile.mkdtemp(prefix="dz-")
    DZIENNIK = os.path.join(tmp, "dziennik")
    INDEKS = os.path.join(tmp, "INDEKS.md")
    ok = True
    try:
        p1 = os.path.join(DZIENNIK, "2026-01-01__aaa111.md")
        p2 = os.path.join(DZIENNIK, "2026-02-02__bbb222.md")
        dodaj("testy", "Pierwszy wpis testowy sesji A", "o", "p", "w", sciezka=p1)
        dodaj("kod", "Drugi wpis testowy sesji A", "o", "p", "w", sciezka=p1)
        dodaj("testy", "Wpis z sesji B prostujacy", "o", "p", "w",
              zastepuje="Pierwszy wpis testowy sesji A", sciezka=p2)

        if len(wszystkie_wpisy()) != 3:
            print("  [FAIL] scalanie wpisow z wielu sesji"); ok = False
        if len(pliki_dziennika()) != 2:
            print("  [FAIL] wykrywanie plikow sesji"); ok = False
        z = mapa_zastapien(wszystkie_wpisy())
        if "pierwszy wpis testowy sesji a" not in z:
            print("  [FAIL] rozpoznanie pola Zastepuje"); ok = False
        if sprawdz(cicho=True) != 0:
            print("  [FAIL] walidacja poprawnego dziennika"); ok = False

        # brak pola musi byc wykryty
        io.open(p2, "a", encoding="utf-8").write(
            "\n### [2026-02-03] Wpis niekompletny testowy\n**Temat:** testy\n"
            "**Objaw:** tylko to\n")
        if sprawdz(cicho=True) == 0:
            print("  [FAIL] nie wykryl braku pol"); ok = False

        # odsylacz w prozne musi byc wykryty
        io.open(p2, "a", encoding="utf-8").write(
            "\n### [2026-02-04] Wpis ze zlym odsylaczem testowy\n**Temat:** kod\n"
            "**Zastepuje:** Nie ma takiego wpisu\n**Objaw:** a\n"
            "**Przyczyna:** b\n**Wniosek:** c\n")
        if sprawdz(cicho=True) < 2:
            print("  [FAIL] nie wykryl odsylacza w prozne"); ok = False

        zbuduj_indeks()
        tresc = io.open(INDEKS, encoding="utf-8").read()
        if "NIEAKTUALNY" not in tresc:
            print("  [FAIL] indeks nie oznacza wpisow zastapionych"); ok = False
    finally:
        DZIENNIK, INDEKS = stary_d, stary_i
        shutil.rmtree(tmp, ignore_errors=True)

    if os.path.isdir(DZIENNIK) and sprawdz(cicho=True) != 0:
        print("  [FAIL] prawdziwy dziennik repo ma bledy"); ok = False
    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def odswiez_stan():
    """Aktualizuje w STAN-SESJI.md tylko te pola, ktore da sie wyliczyc:
    wersje repo, ostatni commit, galaz, liczbe wpisow dziennika.

    Powod: przy pierwszym uruchomieniu na swiezym klonie okazalo sie, ze
    plik juz klamie - podawal wersje 9.13.0 i commit sprzed dwoch zmian,
    bo agent (czyli ja) zapomnial go poprawic po wlasnym commicie.
    Pola opisowe (co w toku, nastepne kroki, otwarte pytania) zostaja
    reczne - tego nie da sie wyliczyc i wlasnie w tym jest ich wartosc."""
    import json
    import re
    sciezka = os.path.join(KORZEN, "STAN-SESJI.md")
    if not os.path.exists(sciezka):
        print("[BLAD] brak STAN-SESJI.md")
        return 1

    def git(*a):
        try:
            r = subprocess.run(["git"] + list(a), capture_output=True,
                               text=True, cwd=KORZEN, timeout=20)
            return r.stdout.strip() if r.returncode == 0 else "?"
        except Exception:
            return "?"

    try:
        wersja = json.load(io.open(os.path.join(KORZEN, "WERSJE.json"),
                                   encoding="utf-8"))["repo"]
    except Exception:
        wersja = "?"
    commit = git("log", "-1", "--format=%h")
    tytul = git("log", "-1", "--format=%s")
    galaz = git("rev-parse", "--abbrev-ref", "HEAD")
    ile = len(wszystkie_wpisy())
    sesji = len(pliki_dziennika())

    s = io.open(sciezka, encoding="utf-8").read()
    podmiany = [
        (r"(\| wersja repo \| )\*\*[^*]*\*\*", r"\g<1>**%s**" % wersja),
        (r"(\| gałąź robocza \| )`[^`]*`", r"\g<1>`%s`" % galaz),
        (r"(\| ostatni commit \| )`[^`]*`[^|]*",
         r"\g<1>`%s` — %s " % (commit, tytul[:52].replace("\\", ""))),
        (r"(\| dziennik \| )[^|]*",
         r"\g<1>%d wpisów, %d %s " % (ile, sesji,
                                       "sesja" if sesji == 1 else "sesje")),
    ]
    zmian = 0
    for wzor, zam in podmiany:
        s, n = re.subn(wzor, zam, s, count=1)
        zmian += n
    io.open(sciezka, "w", encoding="utf-8").write(s)
    print("[OK] STAN-SESJI.md: wersja %s, commit %s, %d wpisow (%d pol)"
          % (wersja, commit, ile, zmian))
    print("     Pola opisowe (co w toku, nastepne kroki, otwarte pytania)")
    print("     popraw RECZNIE - tego nie da sie wyliczyc.")
    return 0


def main():
    args = sys.argv[1:]

    def opcja(nazwa):
        return args[args.index(nazwa) + 1] if nazwa in args and \
            args.index(nazwa) + 1 < len(args) else None

    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--sprawdz" in args:
        return 1 if sprawdz() else 0
    if "--indeks" in args:
        return zbuduj_indeks()
    if "--stan" in args:
        return odswiez_stan()
    if "--sesje" in args:
        return widok_sesji()
    if "--moje" in args:
        return widok_moje()
    if "--szukaj" in args:
        f = opcja("--szukaj")
        if not f:
            print("[BLAD] --szukaj wymaga slowa")
            return 1
        return szukaj(f)
    if "--dodaj" in args:
        tytul = opcja("--tytul")
        if tytul:
            temat = (opcja("--temat") or "repo").lower()
            if temat not in TEMATY:
                print("[BLAD] nieznany temat %r. Dostepne: %s"
                      % (temat, ", ".join(TEMATY)))
                return 1
            p = dodaj(temat, tytul, opcja("--objaw") or "",
                      opcja("--przyczyna") or "", opcja("--wniosek") or "",
                      opcja("--zastepuje") or "")
            print("[OK] wpis dopisany do %s" % os.path.basename(p))
            return 0
        return dodaj_interaktywnie()
    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0
    if "--temat" in args:
        t = (opcja("--temat") or "").lower()
        if t not in TEMATY:
            print("[BLAD] nieznany temat. Dostepne: %s" % ", ".join(TEMATY))
            return 1
        return widok_scalony(t)
    return widok_scalony()


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZALOZ DOM - przygotowuje kopie Gangu do przeniesienia na wlasnego gita.

Dla kogo: agent, ktory chce uzywac Gangu u siebie, ale NIE pracuje w tym
repozytorium. Zamiast klonowac cudzy dom razem z cudza pamiecia, dostaje
czysty dom z kompletem narzedzi i wiedzy o nich.

CO JEDZIE (bo dotyczy narzedzia):
    narzedzia rodziny + zwiad, bramki, bakap, pamietnik
    dokumentacja: README, CZYM-JEST-GANG, PROTOKOL, SZYBKI-START
    docs/agent/ - w tym LEKCJE.md, destylat z pracy nad narzedziem
    docs/czlowiek/ - paczka do czatu, instrukcja
    dev/ - turnieje, amunicja, pomiary mutacyjne, hooki
    pusty dziennik/ z README i szablon STAN-SESJI.md

CZEGO NIE MA (bo to cudza pamiec, nie wiedza):
    dziennik/DATA__sesja.md - wpisy konkretnej sesji
    STAN-SESJI.md wypelniony - czyjs stan, otwarte PR, decyzje z rozmowy
    docs/audyt-zewnetrzny/ - korespondencja z konkretnym audytorem
    docs/dowody/, docs/historia/ - osiagniecia i kronika cudzego repo
    .git - historia cudzej galezi

Dlaczego tak: cudze "na czym stanalem" to nie brak informacji, tylko
INFORMACJA FALSZYWA dla ciebie. Agent czytajacy "PR #2 czeka na decyzje"
zaczyna dzialac na zalozeniach, ktore go nie dotycza. Lekcje o samym
narzedziu jada - bo szkoda, zebys uczyl sie od zera rzeczy, ktore juz
ktos zmierzyl.

Uzycie:
    python3 zaloz-dom.py ~/moj-gang      # przygotuj kopie
    python3 zaloz-dom.py --lista         # co pojedzie, co zostanie
    python3 zaloz-dom.py --selftest
"""

import io
import os
import shutil
import subprocess
import sys
from datetime import date

WERSJA = "1.0.0"
KORZEN = os.path.dirname(os.path.abspath(__file__))

# --- co jedzie: wiedza o narzedziu ---
PLIKI = [
    "PogromcaKwiatkow.py", "ZagladaKultury.py", "ProkuratorOgrodnik.py",
    "AnihilatorChwastow.py", "zwiad.py", "pamietnik.py", "bakap.py",
    "sprawdz-teksty.py", "sprawdz-spojnosc.py", "zaloz-dom.py",
    "WERSJE.json", "LICENSE", ".gitignore",
    "README.md", "CZYM-JEST-GANG.md", "PROTOKOL-OPERATORA.md",
    "SZYBKI-START-DLA-AGENTA.md",
]
KATALOGI = ["dev", "docs/agent", "docs/czlowiek"]

# --- czego nie ma: cudza pamiec ---
POMIJANE = [
    "dziennik",                # wpisy konkretnej sesji
    "STAN-SESJI.md",           # czyjs stan pracy
    "PAMIETNIK-OPERATORA.md",  # generowany spis cudzego dziennika
    "docs/audyt-zewnetrzny",   # korespondencja z konkretnym audytorem
    "docs/dowody",             # osiagniecia cudzego repo
    "docs/historia",           # kronika cudzych wydan
    ".git",
]

SZABLON_STANU = """# Stan sesji

Dom zalozony: {data}. Sesja zero - jeszcze nic sie nie wydarzylo.

Ten plik odpowiada na pytanie **"na czym stanal poprzedni agent"**.
Aktualizuj go na koniec kazdej sesji:

```
python3 pamietnik.py --stan     # wypelnia fakty (wersja, commit, galaz)
```

Reszte - ponizsze sekcje - piszesz recznie. Tego nie da sie wyliczyc
i wlasnie w tym jest ich wartosc.

---

## Gdzie jestesmy

| | |
|---|---|
| wersja repo | (uruchom `python3 pamietnik.py --stan`) |
| galaz robocza | |
| ostatni commit | |
| stan testow | nieznany - uruchom `python3 PogromcaKwiatkow.py --selftest` |
| dziennik | 0 wpisow |

## Co jest w toku

Nic. To pierwszy dzien tego domu.

## Decyzje operatora, ktore obowiazuja

Zasady odziedziczone razem z narzedziem - sprawdzone w praktyce,
warto je zachowac:

1. **Nie ruszamy dzialajacego kodu, dokladamy kolejny.** Naprawa bledu -
   tak. Kosmetyka w tym samym commicie co zmiana logiki - nie.
2. **Poprawka kodu = pelna regresja od nowa.** Zmieniasz rodzine ->
   podbijasz wersje i przechodzisz turnieje.
3. **"Nieomylny" znaczy "nie wprowadzi cie w blad"**, nie "zawsze
   naprawi dobrze".
4. **Gang to oczy, nie automat.** Decyzja i odpowiedzialnosc sa twoje.
5. **Test, ktory nie umie oblac, jest dekoracja.**

Wlasne decyzje dopisuj ponizej.

## Nastepne kroki

1. Zainstaluj hooki: `python3 dev/hooki/zainstaluj.py`
2. Zrob pierwsza migawke: `python3 bakap.py`
3. Uruchom pelna regresje (kolejnosc: `docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md`)
4. Przeczytaj `docs/agent/LEKCJE.md` - destylat z pracy nad tym narzedziem

## Otwarte pytania

Brak - dopisuj swoje.

## Znane wady, ktorych NIE naprawiono

Odziedziczone razem z narzedziem, potwierdzone pomiarem:

| Wada | Skutek |
|---|---|
| HTML/CSS traktowane jak proza | tekst uzytkownika (np. chinski) znika |
| 24 znaki rozjezdzaja sie miedzy Zagloda a Anihilatorem | ten sam znak w .py i .js daje inny wynik |
| `U+0304` i znaki laczace ze zlozona forma NFC | fuzz 499/500 |
| martwy kod: dublet 111 linii w Anihilatorze | poprawka w zlej kopii nie da efektu |

Szczegoly: `docs/agent/LUKI-W-TESTACH.md`, `docs/agent/LEKCJE.md`.

## Jak sprawdzic, ze nic sie nie posypalo

```
python3 PogromcaKwiatkow.py --selftest      # POZIOM 0 - jesli oblewa, STOP
python3 sprawdz-spojnosc.py
python3 sprawdz-teksty.py
python3 pamietnik.py --sprawdz
python3 dev/turnieje/turniej-9-obcy-kod.py  # najtwardszy: obcy kod z PyPI
```
"""

CZYTAJ_NAJPIERW = """# Ten dom jest twoj

Kopia Gangu przygotowana narzedziem `zaloz-dom.py`. Masz komplet
narzedzi i wiedze o nich. **Nie masz cudzej pamieci sesji** - i tak ma
byc.

## Co dostales

| | |
|---|---|
| narzedzia rodziny | Pogromca, Zaglada, Prokurator, Anihilator |
| oczy operatora | `zwiad.py` - pokazuje prawde, niczego nie zapisuje |
| bramki | `sprawdz-teksty.py`, `sprawdz-spojnosc.py` |
| ochrona | `bakap.py` + hook `pre-push` |
| pamiec | `pamietnik.py` + **pusty** `dziennik/` |
| turnieje | `dev/` - komplet, z pomiarami mutacyjnymi |
| **lekcje** | `docs/agent/LEKCJE.md` - destylat z pracy nad narzedziem |

## Czego nie dostales i dlaczego

Cudzego `dziennik/`, cudzego `STAN-SESJI.md`, cudzej historii gita.

To nie jest ukrywanie - to unikanie **falszywej informacji**. Wpis
"PR #2 czeka na decyzje operatora" jest prawdziwy w tamtym domu
i mylacy w twoim. Zaczalbys prace na zalozeniach, ktore ciebie nie
dotycza.

Lekcje o samym narzedziu pojechaly z domem, bo dotycza kazdego, kto go
uzywa. Szkoda, zebys uczyl sie od zera rzeczy, ktore ktos juz zmierzyl.

## Pierwsze kroki

```
git init && git add -A && git commit -m "Gang: dom zalozony"
python3 dev/hooki/zainstaluj.py     # ochrona przed force-push
python3 bakap.py                     # pierwsza migawka
python3 PogromcaKwiatkow.py --selftest
```

Potem: `README.md` -> `CZYM-JEST-GANG.md` -> `docs/agent/LEKCJE.md`.

## Prowadz wlasny dziennik

```
python3 pamietnik.py --dodaj        # gdy cos cie ugryzie
python3 pamietnik.py --stan         # na koniec sesji
```

Gdy trafisz na cos, co dotyczy **narzedzia**, a nie twojej sesji -
dopisz do `docs/agent/LEKCJE.md`. To jedzie dalej, do kolejnych domow.
"""


def co_pojedzie():
    """(pliki, katalogi, pominiete) - lista tego, co istnieje."""
    p = [f for f in PLIKI if os.path.exists(os.path.join(KORZEN, f))]
    k = [d for d in KATALOGI if os.path.isdir(os.path.join(KORZEN, d))]
    om = [x for x in POMIJANE if os.path.exists(os.path.join(KORZEN, x))]
    return p, k, om


def lista():
    p, k, om = co_pojedzie()
    print("JEDZIE (wiedza o narzedziu):\n")
    for f in p:
        print("  %-34s %7d B" % (f, os.path.getsize(os.path.join(KORZEN, f))))
    for d in k:
        ile = sum(len(fs) for _, _, fs in os.walk(os.path.join(KORZEN, d)))
        print("  %-34s %7d plikow" % (d + "/", ile))
    print("\nZOSTAJE (cudza pamiec sesji):\n")
    for x in om:
        pe = os.path.join(KORZEN, x)
        if os.path.isdir(pe):
            ile = sum(len(fs) for _, _, fs in os.walk(pe))
            print("  %-34s %7d plikow" % (x + "/", ile))
        else:
            print("  %-34s %7d B" % (x, os.path.getsize(pe)))
    return 0


def zaloz(cel):
    if os.path.exists(cel) and os.listdir(cel):
        print("[BLAD] %s istnieje i nie jest pusty." % cel)
        print("       Nie nadpisuje cudzej pracy - wskaz inny katalog.")
        return 1
    p, k, om = co_pojedzie()
    os.makedirs(cel, exist_ok=True)

    for f in p:
        docelowy = os.path.join(cel, f)
        os.makedirs(os.path.dirname(docelowy) or cel, exist_ok=True)
        shutil.copy2(os.path.join(KORZEN, f), docelowy)
    for d in k:
        shutil.copytree(os.path.join(KORZEN, d), os.path.join(cel, d),
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    # pusty dziennik z instrukcja
    os.makedirs(os.path.join(cel, "dziennik"), exist_ok=True)
    zrodlo_readme = os.path.join(KORZEN, "dziennik", "README.md")
    if os.path.exists(zrodlo_readme):
        shutil.copy2(zrodlo_readme, os.path.join(cel, "dziennik", "README.md"))

    io.open(os.path.join(cel, "STAN-SESJI.md"), "w", encoding="utf-8").write(
        SZABLON_STANU.format(data=date.today().isoformat()))
    io.open(os.path.join(cel, "CZYTAJ-NAJPIERW.md"), "w",
            encoding="utf-8").write(CZYTAJ_NAJPIERW)

    ile = sum(len(fs) for _, _, fs in os.walk(cel))
    print("[DOM] %s" % cel)
    print("      %d plikow, %d katalogow z dokumentacja" % (ile, len(k)))
    print("      dziennik: PUSTY (twoj), STAN-SESJI: szablon")
    print()
    print("Dalej:")
    print("  cd %s" % cel)
    print("  cat CZYTAJ-NAJPIERW.md")
    print("  git init && git add -A && git commit -m 'Gang: dom zalozony'")
    return 0


def selftest():
    import tempfile
    ok = True
    d = tempfile.mkdtemp(prefix="dom-")
    cel = os.path.join(d, "nowy")
    try:
        zaloz(cel)
        # narzedzia sa
        for f in ("PogromcaKwiatkow.py", "zwiad.py", "bakap.py",
                  "docs/agent/LEKCJE.md"):
            if not os.path.exists(os.path.join(cel, f)):
                print("  [FAIL] brakuje %s" % f); ok = False
        # cudzej pamieci NIE MA
        for f in ("PAMIETNIK-OPERATORA.md", "docs/dowody",
                  "docs/audyt-zewnetrzny", ".git"):
            if os.path.exists(os.path.join(cel, f)):
                print("  [FAIL] przeciekla cudza pamiec: %s" % f); ok = False
        # dziennik pusty (tylko README)
        wpisy = [x for x in os.listdir(os.path.join(cel, "dziennik"))
                 if "__" in x]
        if wpisy:
            print("  [FAIL] w dzienniku sa cudze wpisy: %s" % wpisy); ok = False
        # STAN-SESJI to szablon, nie kopia
        st = io.open(os.path.join(cel, "STAN-SESJI.md"), encoding="utf-8").read()
        if "PR #" in st or "01a06e18" in st:
            print("  [FAIL] STAN-SESJI zawiera cudzy kontekst"); ok = False
        # narzedzia dzialaja w nowym domu
        r = subprocess.run([sys.executable,
                            os.path.join(cel, "PogromcaKwiatkow.py"),
                            "--selftest"], capture_output=True, timeout=120)
        if r.returncode != 0:
            print("  [FAIL] Pogromca nie dziala w nowym domu"); ok = False
        # nie nadpisuje niepustego katalogu
        if zaloz(cel) == 0:
            print("  [FAIL] nadpisal niepusty katalog"); ok = False
    finally:
        shutil.rmtree(d, ignore_errors=True)
    print("SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return 0 if selftest() else 1
    if "--lista" in args:
        return lista()
    if "--help" in args or "-h" in args or not args:
        print(__doc__)
        return 0
    return zaloz(os.path.abspath(os.path.expanduser(args[0])))


if __name__ == "__main__":
    sys.exit(main())

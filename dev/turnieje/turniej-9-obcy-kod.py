#!/usr/bin/env python3
"""TURNIEJ 9 — OBCY KOD Z INTERNETU (prawdziwe pakiety z PyPI).

Pomysl operatora: wszystkie dotychczasowe turnieje uzywaja probek, ktore
sami wytworzylismy. Nawet weryfikacja na 40 modulach stdlib to kod z tej
samej instalacji Pythona. Brakowalo najtwardszej proby: **wziac cudzy kod,
ktorego nikt z nas nie widzial na oczy, skazic go, naprawic Gangiem
i sprawdzic, czy NADAL DZIALA**.

Roznica wobec T3/Z2 (niepsucie): tam probki generuje test i wie, czego
sie spodziewac. Tu plik przychodzi z zewnatrz, ma prawdziwa strukture
(klasy, dekoratory, warunkowe importy, obsluge wersji Pythona) i nikt
nie projektowal go pod nasze narzedzia.

Kryterium jest surowe i trojstopniowe:

  1. plik po skazeniu i naprawie **kompiluje sie**
  2. plik **importuje sie** jako modul w osobnym procesie
  3. jego **publiczne API jest identyczne** jak przed skazeniem
     (sorted(dir(modul)) bajt w bajt)

Trzeci punkt jest najwazniejszy: kod moze sie kompilowac i importowac,
a miec po cichu zmieniona nazwe funkcji - dokladnie ta klasa bledu, ktora
znalezlismy w luce f-string i w niespojnosci identyfikatorow.

SKAZENIE MUSI BYC ODWRACALNE. Uzywamy wylacznie homoglifow WIERNYCH -
takich, dla ktorych zamien_znak() zwraca dokladnie oryginalna litere
ASCII. Podmiana na znak transliterujacy sie na INNA litere (np. 's' na
cyrylickie 'r') niszczy informacje PRZED testem i zaden narzedzie jej nie
odtworzy - to blad metody, nie narzedzia (patrz dziennik).

Uzycie:
    python3 dev/turnieje/turniej-9-obcy-kod.py           # z siecia
    python3 dev/turnieje/turniej-9-obcy-kod.py --offline # tylko stdlib

Bez sieci turniej NIE oblewa - przechodzi na kodzie stdlib i mowi wprost,
ze pracowal w trybie zapasowym. Brak internetu to nie wada Gangu.

CZEGO TEN TURNIEJ NIE BADA (swiadomie): skazen WEWNATRZ literalow,
w tym w polach f-stringow. Powod: ten sam f-string potrafi zawierac
i tekst (dane - Zaglada slusznie nie rusza), i nazwe zmiennej (kod -
naprawia). Porownanie calego pliku nie odrozni jednego od drugiego
i dawaloby falszywe alarmy na poprawnym zachowaniu. Te klase pilnuja
T4 (kryterium wykonania) i dev/luki/luka-fstring.py, na probkach
pisanych pod ten jeden cel.

Zweryfikowane sabotazem: brak ochrony literalow -> 4 oblane,
slepota na cyrylice -> 45 oblanych, cofnieta naprawa f-string ->
przechodzi (i tak ma byc, patrz wyzej).
"""
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# male, samodzielne pakiety bez zaleznosci - zeby import sie udal
PAKIETY = ["six", "termcolor", "inflection", "shortuuid", "wcwidth", "natsort"]
LIMIT_ZNAKOW = 40000
ILE_SKAZEN = 6


def _zaladuj(nazwa):
    p = os.path.join(KORZEN, nazwa)
    s = importlib.util.spec_from_file_location(nazwa[:-3].replace("-", "_"), p)
    m = importlib.util.module_from_spec(s)
    sys.modules[s.name] = m
    s.loader.exec_module(m)
    return m


Z = _zaladuj("ZagladaKultury.py")


# Stala lista homoglifow cyrylickich - NIE wyliczana z Zaglady.
# Powod: wierne_homoglify() pyta zamien_znak() tego samego modulu, ktory
# potem testujemy. Gdy narzedzie oslepnie na cyrylice, znaki wypadaja ze
# zbioru i test przestaje ich uzywac - czyli sabotaz sam sie ukrywa.
# Zmierzone: po wycieciu obslugi CYR zbior kurczyl sie z 1010 do 962
# znakow, a turniej dalej meldowal 51/51.
CYRYLICKIE_WIERNE = {
    # TYLKO znaki, dla ktorych transliteracja wraca do TEJ SAMEJ litery.
    # Cyrylickie 'c' (U+0441) daje 's', 'p' (U+0440) daje 'r', 'x' daje
    # 'ch' - to poprawna transliteracja rosyjska, ale skazenie nimi jest
    # NIEODWRACALNE i test mierzylby wlasny blad, nie usterke narzedzia
    # (patrz dziennik: "skazenie testowe musi byc odwracalne").
    "a": "\u0430", "e": "\u0435", "o": "\u043e", "i": "\u0456",
    "j": "\u0458", "A": "\u0410", "E": "\u0415", "K": "\u041a",
    "M": "\u041c", "O": "\u041e", "T": "\u0422",
}


def wierne_homoglify():
    """Znaki, dla ktorych zamien_znak() zwraca DOKLADNIE ta sama litere
    ASCII - czyli skazenie jest w pelni odwracalne."""
    import unicodedata as _u
    wierne = {}
    for cp in list(range(0x80, 0x2500)) + list(range(0xFB00, 0xFB50)):
        c = chr(cp)
        licznik = dict((k, 0) for k in Z.KATEGORIE)
        try:
            wynik = Z.zamien_znak(c, licznik, kod=True)
        except Exception:
            continue
        if wynik and len(wynik) == 1 and wynik.isascii() and wynik.isalpha():
            wierne.setdefault(wynik, []).append(c)
    # Sortujemy tak, zeby CYRYLICA i GREKA byly pierwsze. Bez tego skaz()
    # bral zawsze pierwszy znak z zakresu, czyli lacinke z akcentem
    # (U+00E8 zamiast U+0435) - i sabotaz wycinajacy obsluge cyrylicy
    # przechodzil niezauwazony, bo test w ogole jej nie uzywal.
    def priorytet(znak):
        nz = _u.name(znak, "")
        if nz.startswith("CYRILLIC"):
            return 0
        if nz.startswith("GREEK"):
            return 1
        return 2
    for k in wierne:
        wierne[k].sort(key=priorytet)
    # Cyrylica z listy STALEJ ma pierwszenstwo bezwarunkowe - nawet gdy
    # badane narzedzie przestalo ja rozpoznawac (i wtedy tym bardziej).
    for lit, znak in CYRYLICKIE_WIERNE.items():
        wierne.setdefault(lit, [])
        if znak in wierne[lit]:
            wierne[lit].remove(znak)
        wierne[lit].insert(0, znak)
    return wierne


def pobierz_z_pypi():
    """[(pakiet, nazwa_pliku, tresc)] - male pliki .py, ktore sie kompiluja."""
    kandydaci = []
    for nazwa in PAKIETY:
        try:
            d = json.load(urllib.request.urlopen(
                "https://pypi.org/pypi/%s/json" % nazwa, timeout=20))
            url = next((u["url"] for u in d["urls"]
                        if u["filename"].endswith(".tar.gz")), None)
            if not url:
                continue
            dane = urllib.request.urlopen(url, timeout=30).read()
            with tarfile.open(fileobj=io.BytesIO(dane)) as tf:
                for m in tf.getmembers():
                    if not m.name.endswith(".py"):
                        continue
                    if m.size > LIMIT_ZNAKOW or m.size < 300:
                        continue
                    if any(x in m.name for x in ("test", "setup", "conf.py")):
                        continue
                    try:
                        t = tf.extractfile(m).read().decode("utf-8")
                        compile(t, m.name, "exec")
                    except Exception:
                        continue
                    # Pomijamy pliki, ktore JUZ zawieraja obce pismo jako
                    # DANE (tablice Unicode, slowniki z dewanagari, CJK).
                    # Zaglada slusznie czysci takie literaly, wiec porownanie
                    # "wynik == oryginal" nie ma tam sensu - mierzylibysmy
                    # zachowanie zamierzone, nie usterke. Zmierzone: cztery
                    # pliki wcwidth/table_grapheme_overrides mialy po 5-10 tys.
                    # znakow dewanagari w kluczach slownika.
                    obce = sum(1 for c in t if ord(c) > 127)
                    if obce > 20:
                        continue
                    # zapamietujemy sciezke WEWNATRZ archiwum - odtworzymy
                    # strukture katalogow, zeby importy wzgledne dzialaly
                    wzgl = m.name.split("/", 1)[1] if "/" in m.name else m.name
                    kandydaci.append((nazwa, wzgl, t))
        except Exception:
            continue
    return kandydaci


def zapasowe_ze_stdlib():
    """Gdy nie ma sieci: male moduly stdlib. Slabsze (znamy je), ale
    lepsze niz nic."""
    import sysconfig
    lib = sysconfig.get_paths()["stdlib"]
    out = []
    for fn in sorted(os.listdir(lib)):
        if not fn.endswith(".py"):
            continue
        p = os.path.join(lib, fn)
        try:
            if os.path.getsize(p) > LIMIT_ZNAKOW:
                continue
            t = io.open(p, encoding="utf-8").read()
            compile(t, fn, "exec")
        except Exception:
            continue
        out.append(("stdlib", fn, t))
        if len(out) >= 12:
            break
    return out


def skaz(tekst, wierne, ile=ILE_SKAZEN):
    """Podmienia `ile` liter na WIERNE homoglify - tylko poza literalami
    i komentarzami, zeby skazenie trafialo w KOD.

    UWAGA metodyczna: uzywamy _chronione_pozycje() TEGO SAMEGO modulu,
    ktory potem testujemy. Gdyby brac ja wprost, test bylby slepy na
    kazda wade tej funkcji - skazenie omijaloby dokladnie te miejsca,
    ktorych narzedzie nie umie obronic. Zmierzone sabotazem: cofniecie
    naprawy f-string przechodzilo bez sladu, bo skazenie nigdy nie
    trafialo do wnetrza f-stringa.
    Dlatego chronimy sie WLASNA, niezalezna lista: literaly i komentarze
    znajdujemy przez tokenize, ale wnetrze f-stringow zostawiamy jako
    teren dozwolony - bo to jest KOD i narzedzie ma je umiec naprawic."""
    import tokenize as _tk
    chronione = set()
    literaly = set()
    try:
        starty, poz = [], 0
        for linia in tekst.split("\n"):
            starty.append(poz)
            poz += len(linia) + 1
        for tok in _tk.generate_tokens(io.StringIO(tekst).readline):
            if tok.type not in (_tk.STRING, _tk.COMMENT):
                continue
            a = starty[tok.start[0] - 1] + tok.start[1]
            b = starty[tok.end[0] - 1] + tok.end[1]
            # Wnetrze pol f-stringa to KOD i narzedzie ma je umiec
            # naprawic - wiec zostawiamy je jako teren dozwolony.
            # ALE tylko tam, gdzie stoi IDENTYFIKATOR. Litery w tekscie
            # dookola pol naleza do literalu, czyli do danych: Zaglada
            # slusznie ich nie rusza w .py, bo to moze byc francuski
            # tekst uzytkownika. Zmierzone: 'e' zamienione na U+00E8
            # wewnatrz f-stringa dawalo falszywe "GANG PSUJE OBCY KOD",
            # a bylo zachowaniem zamierzonym.
            # CALY literal traktujemy jako chroniony, takze wnetrze
            # f-stringow. Powod metodyczny: `other_table_name=` wystepuje
            # w tym samym f-stringu i jako TEKST, i jako nazwa w polu
            # {other_table_name}. Skazenie tekstu jest dla Zaglady danymi
            # (slusznie nie rusza), skazenie pola jest kodem (naprawia) -
            # a test porownuje caly plik i widzi roznice tam, gdzie
            # narzedzie zachowalo sie POPRAWNIE.
            # Skazenie kodu wewnatrz f-stringow bada osobno T4 i
            # dev/luki/luka-fstring.py, na probkach pisanych pod ten cel.
            # Tutaj chodzi o obcy kod, wiec mierzymy to, co da sie zmierzyc
            # jednoznacznie: skazenie POZA literalami.
            chronione.update(range(a, b))
            # kotwica moze isc TYLKO w literal STRING - komentarze Zaglada
            # czysci (i slusznie: to nie sa dane programu). Zmierzone:
            # kotwica w komentarzu dawala falszywe "RUSZYL LITERAL".
            if tok.type == _tk.STRING:
                literaly.update(range(a + 1, max(a + 1, b - 1)))
    except Exception:
        try:
            chronione = Z._chronione_pozycje(tekst)
        except Exception:
            chronione = set()
    znaki = list(tekst)
    # Zbieramy WSZYSTKIE dozwolone pozycje, potem wybieramy rownomiernie
    # po calym pliku. Branie pierwszych `ile` od poczatku powodowalo, ze
    # skazenie ladowalo zawsze w naglowku (importy, docstring) i NIGDY nie
    # trafialo w f-stringi ani w dalsze partie kodu. Zmierzone: 0 plikow
    # ze skazeniem wewnatrz f-stringa na 51 probek - dwa sabotaze
    # przechodzily przez to niezauwazone.
    mozliwe = []
    for i, c in enumerate(znaki):
        if i in chronione or not c.isascii() or not c.isalpha():
            continue
        if i == 0 or not (znaki[i - 1].isalnum() or znaki[i - 1] == "_"):
            continue
        if c in wierne:
            mozliwe.append(i)
    if not mozliwe:
        return tekst, 0, literaly
    ile = min(ile, len(mozliwe))
    krok = len(mozliwe) / float(ile)
    wybrane = [mozliwe[int(k * krok)] for k in range(ile)]
    for i in wybrane:
        znaki[i] = wierne[znaki[i]][0]
    # dodatkowo skazamy JEDEN znak w literale - Zaglada ma go NIE ruszyc
    # w .py (kontrakt: literaly swiete). To wykrywa utrate ochrony
    # literalow, ktorej samo skazenie kodu nie zlapie.
    kotwica = None
    for i in sorted(literaly):
        c = znaki[i]
        if c.isascii() and c.isalpha() and c in wierne:
            znaki[i] = wierne[c][0]
            kotwica = (i, c, wierne[c][0])
            break
    return "".join(znaki), len(set(wybrane)), kotwica


def odcisk(sciezka, nazwa_modulu, katalog_pakietu=None):
    """Publiczne API modulu, wyliczone w OSOBNYM procesie (zeby import
    nie zanieczyscil naszego).

    katalog_pakietu trafia na sys.path - bez tego pliki uzywajace importow
    wzglednych (`from . import x`) albo importujace wlasny pakiet po nazwie
    nie daja sie zaladowac i cala probka przepada jako "pominieta".
    Przy pierwszym uruchomieniu odpadalo tak 30 z 56 plikow."""
    kod = (
        "import importlib.util, json, sys, os\n"
        "sys.path.insert(0, %r)\n"
        "sys.path.insert(0, os.path.dirname(%r))\n"
        "s = importlib.util.spec_from_file_location(%r, %r)\n"
        "m = importlib.util.module_from_spec(s)\n"
        "sys.modules[%r] = m\n"
        "s.loader.exec_module(m)\n"
        "print(json.dumps(sorted(x for x in dir(m) if not x.startswith('_'))))\n"
        % (katalog_pakietu or os.path.dirname(sciezka), sciezka,
           nazwa_modulu, sciezka, nazwa_modulu))
    try:
        r = subprocess.run([sys.executable, "-c", kod], capture_output=True,
                           text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    if r.returncode != 0:
        ost = (r.stderr or "").strip().splitlines()
        return None, (ost[-1] if ost else "blad bez opisu")
    return r.stdout.strip(), None


def main():
    offline = "--offline" in sys.argv
    print("=" * 72)
    print("TURNIEJ 9 — OBCY KOD (prawdziwe pakiety, nie nasze probki)")
    print("=" * 72)

    wierne = wierne_homoglify()
    print("  wiernych homoglifow (skazenie odwracalne): %d liter, %d znakow"
          % (len(wierne), sum(len(v) for v in wierne.values())))

    zrodlo = "PyPI"
    pliki = [] if offline else pobierz_z_pypi()
    if not pliki:
        zrodlo = "stdlib (tryb zapasowy - brak sieci)"
        pliki = zapasowe_ze_stdlib()
    print("  zrodlo: %s | plikow: %d" % (zrodlo, len(pliki)))
    print()

    if not pliki:
        print("  [BLAD] nie udalo sie zdobyc ani jednego pliku")
        return 1

    tmp = tempfile.mkdtemp(prefix="t9-")
    zdane = oblane = pominiete = zdane_ast = 0
    awarie = []

    for pakiet, nazwa, tresc in pliki:
        mod = os.path.basename(nazwa)[:-3]
        # Odtwarzamy strukture katalogow pakietu w DWOCH kopiach (oryginal
        # i badana), zeby importy wzgledne mialy sie o co oprzec.
        kat_orig = os.path.join(tmp, "orig", pakiet)
        kat_test = os.path.join(tmp, "test", pakiet)
        p_orig = os.path.join(kat_orig, nazwa)
        p_test = os.path.join(kat_test, nazwa)
        for pp in (p_orig, p_test):
            os.makedirs(os.path.dirname(pp), exist_ok=True)
        io.open(p_orig, "w", encoding="utf-8").write(tresc)
        api_przed, blad = odcisk(p_orig, mod, kat_orig)
        # Plik moze wymagac zainstalowanego pakietu albo cudzej biblioteki -
        # wtedy importu nie da sie wykonac ani PRZED, ani PO. Nie odrzucamy
        # takiej probki: schodzimy na slabsze, ale nadal sensowne kryterium
        # porownania DRZEWA SKLADNIOWEGO (ast.dump). Ono wykrywa cicha
        # zmiane nazwy funkcji czy zmiennej tak samo jak porownanie API,
        # tylko bez uruchamiania kodu.
        tryb_ast = api_przed is None

        # 2. skazenie WIERNYMI homoglifami, w kodzie
        brudny, ile, kotwica = skaz(tresc, wierne)
        if ile == 0:
            pominiete += 1
            continue
        # WZORZEC = czego oczekujemy po naprawie: oryginal, ale z kotwica
        # w literale nietknieta (Zaglada slusznie nie rusza literalow .py)
        wzorzec = tresc
        if kotwica:
            _poz, _oryg, _wst = kotwica
            wzorzec = tresc[:_poz] + _wst + tresc[_poz + 1:]

        # 3. naprawa Gangiem
        io.open(p_test, "w", encoding="utf-8").write(brudny)
        subprocess.run([sys.executable, os.path.join(KORZEN, "ZagladaKultury.py"),
                        "--zaglada", p_test], capture_output=True, text=True,
                       timeout=300)
        po = io.open(p_test, encoding="utf-8").read()

        # 4a0. OCHRONA LITERALOW: znak wstawiony w literal ma tam ZOSTAC.
        # Zaglada w .py nie rusza tresci literalow (kontrakt: swiete).
        # Gdy zniknie - stracilismy ochrone danych uzytkownika.
        if kotwica:
            poz, oryg, wstawiony = kotwica
            if poz < len(po) and po[poz] != wstawiony:
                oblane += 1
                awarie.append((pakiet, nazwa, "RUSZYL LITERAL",
                               "%r w literale zmienione na %r"
                               % (wstawiony, po[poz] if poz < len(po) else "?")))
                continue

        # 4a. ODWRACALNOSC: skazenie bylo w pelni odwracalne (wierne
        # homoglify), wiec poprawna naprawa MUSI dac dokladnie oryginal.
        # Bez tego kryterium test przechodzi, gdy narzedzie USUWA znaki
        # zamiast je transliterowac: 'c<U+043E>nter' -> 'cnter' w obu
        # miejscach jest spojne, plik dziala i API sie zgadza - a nazwa
        # zmiennej po cichu sie zmienila. Zmierzone sabotazem.
        if po != wzorzec:
            oblane += 1
            roznice = sum(1 for a, b in zip(po, wzorzec) if a != b)
            awarie.append((pakiet, nazwa, "NIE ODTWORZYL ORYGINALU",
                           "%d roznic mimo odwracalnego skazenia" % roznice))
            continue

        # 4b. trzy kryteria
        try:
            compile(po, nazwa, "exec")
        except Exception as e:
            oblane += 1
            awarie.append((pakiet, nazwa, "NIE KOMPILUJE SIE po naprawie",
                           type(e).__name__))
            continue
        if tryb_ast:
            import ast as _ast
            try:
                # porownujemy z WZORCEM (oryginal + kotwica w literale),
                # bo kotwica ma tam slusznie zostac
                d_przed = _ast.dump(_ast.parse(wzorzec))
                d_po = _ast.dump(_ast.parse(po))
            except Exception as e:
                oblane += 1
                awarie.append((pakiet, nazwa, "AST nie parsuje po naprawie",
                               type(e).__name__))
                continue
            if d_przed != d_po:
                oblane += 1
                awarie.append((pakiet, nazwa, "INNE DRZEWO SKLADNIOWE",
                               "cicha zmiana nazw"))
                continue
            zdane_ast += 1
            continue

        api_po, blad = odcisk(p_test, mod, kat_test)
        if api_po is None:
            oblane += 1
            awarie.append((pakiet, nazwa, "NIE IMPORTUJE SIE po naprawie", blad[:50]))
            continue
        if api_po != api_przed:
            oblane += 1
            awarie.append((pakiet, nazwa, "INNE PUBLICZNE API", "cicha zmiana nazw"))
            continue
        zdane += 1

    shutil.rmtree(tmp, ignore_errors=True)

    print("  ZDANE mocnym kryterium (kompiluje + importuje + to samo API): %d"
          % zdane)
    print("  ZDANE slabszym (to samo drzewo AST - plik wymaga instalacji): %d"
          % zdane_ast)
    print("  OBLANE: %d" % oblane)
    if pominiete:
        print("  pominiete (zero miejsc na skazenie): %d" % pominiete)
    for pak, nz, co, det in awarie[:8]:
        print("     [%s] %s/%s: %s" % (co, pak, nz, det))
    print()
    print("=" * 72)
    if oblane:
        print("FINAL T9: GANG PSUJE OBCY KOD — %d przypadkow" % oblane)
    elif zdane + zdane_ast == 0:
        print("FINAL T9: NIEROZSTRZYGNIETY — zero zdatnych probek")
    else:
        print("FINAL T9: OBCY KOD PRZEZYL — %d/%d (%d z uruchomieniem, %d przez AST)"
              % (zdane + zdane_ast, zdane + zdane_ast + oblane, zdane, zdane_ast))
    print("=" * 72)
    return 1 if oblane else 0


if __name__ == "__main__":
    sys.exit(main())

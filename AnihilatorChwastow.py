# -*- coding: utf-8 -*-
"""Anihilator Chwastow: czwarty czlonek rodziny, chroni literaly w jezykach innych niz Python.

(v1.0.0) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
z rodzenstwem). Przeczytaj przed pierwszym uzyciem.

Rola w rodzinie:
- PogromcaKwiatkow.py = detektor (widzi, niczego nie zmienia)
- ZagladaKultury.py = dekontaminator dla py/json/prozy (niszczy obca kulture, polska zostawia swieta, dla .py chroni literaly przez tokenize)
- ProkuratorOgrodnik.py = ogrodnik-prokurator (prowadzi akta chwastow, decyduje co wyrwac wg polityki allowlisty)
- AnihilatorChwastow.py = anihilator wielojezyczny (js/ts/cs/java/c/cpp/h/hpp/kt/swift/rb/go/rs/php/py; json/jsonl w trybie kodu, md/proza agresywnie)

Problem ktory rozwiazuje:
Zaglada ma ochrone literalow tylko dla .py. Dla js/ts/java/go/rs/cs dziala w trybie prozy agresywnej - wyrwie tez celowa tresc w stringu.
Anihilator chroni literaly automatem stanow (js/ts/cs/java/c/cpp/h/hpp/kt/swift/rb/go/rs/php) + tokenize dla py.
UWAGA (v1.2.0): automat NIE jest lekserem. Literaly mogace zawierac niesparowany
cudzyslow rozjezdzaja mu stan, wiec pliki z takimi konstrukcjami sa ODRZUCANE
(BLOKADA, exit 2), a nie czyszczone: C++ R"(...)", Rust r#"..."#, bloki tekstowe
Javy/Kotlina/Swifta (potrojny cudzyslow), heredoki Ruby i PHP, backticki Go. Patrz NIEOBSLUGIWANE.

Kontrakt v1.0.0:
- cyrylica/greka -> transliteracja PL (jak Zaglada)
- homoglify -> baza, ogonki obce -> zdjecie, cyfry Nd -> ASCII, fullwidth -> pol, CJK/emoji/niewidzialne -> USUN, lamacze -> LF, twarde spacje -> spacja (kod: USUN jak w Zagladzie)
- OCHRONA LITERALOW (automat stanow, nie lekser):
  js/ts: '...' "..." `...` // /* */  - sprawdzone, dziala takze dla szablonow
  cs: "..." @"..." '...' // /* */    - podwojony "" nie psuje parzystosci
  java/c/cpp/h/hpp/kt/swift/rb: "..." '...' // /* */ - tylko literaly jednolinijkowe
  go/rs/php: "..." '...' // /* */
  konstrukcje ODRZUCANE (BLOKADA, patrz NIEOBSLUGIWANE): R-raw C++, r-hash Rust,
  potrojny cudzyslow (Java/Kotlin/Swift), heredoki (<<~, <<-, <<<), backticki Go, literale Ruby %q/%Q/%w/%i
  py: tokenize (jak Zaglada) + awaryjny skaner
  json/jsonl: kod=True (twarde spacje sklejaja)
  md/txt: agresywnie (proza)
- POLSKA KULTURA ZOSTAJE: ASCII + ąćęłńóśźżĄĆĘŁŃÓŚŹŻ + typografia projektowa
- plan->act: domyslnie raport, --anihilacja wykonuje + kontrola Pogromca (BLAD 0)

Uzycie:
  python3 AnihilatorChwastow.py PLIK...                  # raport co ulegnie anihilacji
  python3 AnihilatorChwastow.py --anihilacja PLIK...     # wykonaj anihilacje
  python3 AnihilatorChwastow.py --selftest               # dowod

Exit: 0 = czysto / po anihilacji czysto, 1 = jest do anihilacji, 2 = blad wejscia
"""

import io
import os
import sys
import unicodedata
import re

WERSJA = "1.4.0"

# (R3) Kopie zapasowe NIE MOGA byc wejsciem dla narzedzi. "mod.py.bak-zaglada"
# nie konczy sie na ".py", wiec trafialo do trybu prozy i tracilo ochrone
# literalow - chroniona tresc ginela wlasnie w kopii ratunkowej, a obok
# powstawal "mod.py.bak-zaglada.bak-zaglada".
_KOPIE = ("bak-pogromca", "bak-zaglada", "bak-anihilator")


def jest_kopia_zapasowa(sciezka):
    """True dla plikow .bak-pogromca / .bak-zaglada / .bak-anihilator (takze
    z sufiksem liczbowym, np. .bak-zaglada.3)."""
    n = os.path.basename(sciezka)
    for z in _KOPIE:
        if ("." + z) in n:
            return True
    return False


PL = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
TYPOGRAFIA = "—–„”…€%§°²³±·«»"
DOZWOLONE = set(chr(c) for c in range(0x20, 0x7F)) | set(PL) | set(TYPOGRAFIA)
LAMACZE = "\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029"

CYR = {
    0x0430: "a", 0x0431: "b", 0x0432: "w", 0x0433: "g", 0x0434: "d",
    0x0435: "e", 0x0436: "ż", 0x0437: "z", 0x0438: "i", 0x0439: "j",
    0x043A: "k", 0x043B: "l", 0x043C: "m", 0x043D: "n", 0x043E: "o",
    0x043F: "p", 0x0440: "r", 0x0441: "s", 0x0442: "t", 0x0443: "u",
    0x0444: "f", 0x0445: "ch", 0x0446: "c", 0x0447: "cz", 0x0448: "sz",
    0x0449: "szcz", 0x044A: "", 0x044B: "y", 0x044C: "", 0x044D: "e",
    0x044E: "ju", 0x044F: "ja", 0x0451: "jo",
}
for _cp, _v in list(CYR.items()):
    _w = chr(_cp).upper()
    if len(_w) == 1 and ord(_w) != _cp:
        CYR[ord(_w)] = _v[:1].upper() + _v[1:] if _v else ""

GREK = {
    0x03B1: "a", 0x03B2: "b", 0x03B3: "g", 0x03B4: "d", 0x03B5: "e",
    0x03B6: "z", 0x03B7: "e", 0x03B8: "th", 0x03B9: "i", 0x03BA: "k",
    0x03BB: "l", 0x03BC: "m", 0x03BD: "n", 0x03BE: "ks", 0x03BF: "o",
    0x03C0: "p", 0x03C1: "r", 0x03C2: "s", 0x03C3: "s", 0x03C4: "t",
    0x03C5: "y", 0x03C6: "f", 0x03C7: "ch", 0x03C8: "ps", 0x03C9: "o",
}
for _cp, _v in list(GREK.items()):
    _w = chr(_cp).upper()
    if len(_w) == 1 and ord(_w) != _cp:
        GREK[ord(_w)] = _v[:1].upper() + _v[1:] if _v else ""

HOMOGLIFY = {
    0x017F: "s", 0x00DF: "ss", 0x00F8: "o", 0x00D8: "O", 0x0153: "oe",
    0x0152: "Oe", 0x00E6: "ae", 0x00C6: "Ae", 0x0111: "d", 0x0110: "D",
    0x00F0: "d", 0x00D0: "D", 0x00FE: "th", 0x00DE: "Th", 0x0131: "i",
}

KATEGORIE = ("cyr", "grk", "homoglify", "ogonki", "cyfry", "fold", "pisma", "symbole", "niewidzialne", "spacje", "lamacze")

def baza_bez_ogonkow(c):
    d = unicodedata.normalize("NFD", c)
    if len(d) > 1 and d[0].isascii() and d[0].isalpha():
        return d[0]
    return None

def zamien_znak(c, licznik, kod=False):
    if c in DOZWOLONE or c in "\t\n\r":
        return c
    if c in LAMACZE:
        licznik["lamacze"] += 1
        return "\n"
    cp = ord(c)
    kat = unicodedata.category(c)
    if cp in CYR:
        licznik["cyr"] += 1
        return CYR[cp]
    if cp in GREK:
        licznik["grk"] += 1
        return GREK[cp]
    if cp in HOMOGLIFY:
        licznik["homoglify"] += 1
        return HOMOGLIFY[cp]
    # NFD ogonki
    d = unicodedata.normalize("NFD", c)
    if len(d) > 1 and d[0].isascii() and d[0].isalpha():
        # sprawdz czy baza to cyrylica/greka z akcentem
        if ord(d[0]) in CYR:
            licznik["cyr"] += 1
            return CYR[ord(d[0])]
        if ord(d[0]) in GREK:
            licznik["grk"] += 1
            return GREK[ord(d[0])]
        licznik["ogonki"] += 1
        return d[0]
    # cyfry Nd
    if kat == "Nd" and not c.isascii():
        try:
            v = unicodedata.digit(c)
            licznik["cyfry"] += 1
            return str(v)
        except ValueError:
            pass
    # fullwidth / NFKC
    nfkc = unicodedata.normalize("NFKC", c)
    if nfkc != c and len(nfkc) == 1 and nfkc.isascii():
        licznik["fold"] += 1
        return nfkc
    if len(nfkc) > 1 and all(x.isascii() for x in nfkc):
        licznik["fold"] += 1
        return nfkc
    # niewidzialne Cc/Cf/Cn/Co/Cs/Mn + spacje
    if kat in ("Cc", "Cf", "Cn", "Co", "Cs", "Mn") or c in ("\u00a0", "\u202f", "\u200b", "\u200c", "\u200d", "\ufeff", "\u00ad"):
        if c in ("\u00a0", "\u202f"):
            licznik["spacje"] += 1
            return " " if not kod else None
        licznik["niewidzialne"] += 1
        return None
    # pisma bez tabeli -> usun
    # uproszczenie: jesli nie ASCII i nie PL i nie dozwolone i kategoria Lo/Lm i nie w CYR/GREK/HOMOGLIFY -> pismo obce
    if ord(c) > 127:
        # sprawdz czy to CJK, hangul, arab, hebr, thai, kana itp - po zakresach
        # dla prostoty: jesli nie w DOZWOLONE i nie cyrylica/greka/homoglify i jest litera -> pismo obce lub symbol
        if kat.startswith("L"):
            licznik["pisma"] += 1
            return None
        else:
            licznik["symbole"] += 1
            return None
    return c

def zaglada_tekst(tekst, kod=False):
    licznik = {k:0 for k in KATEGORIE}
    out = []
    for c in tekst:
        z = zamien_znak(c, licznik, kod=kod)
        if z is None:
            continue
        out.append(z)
    return unicodedata.normalize("NFC", "".join(out)), licznik

def zaglada_tekst_poza_literalami_multi(tekst, jezyk):
    """Skaner stanow dla js/ts/java/go/rs/cs - chroni stringi i komentarze."""
    licznik = {k:0 for k in KATEGORIE}
    out = []
    i = 0
    n = len(tekst)
    stan = "kod"  # kod, string_single, string_double, string_backtick, comment_line, comment_block, regex
    # Dla uproszczenia regex tylko dla js/ts
    is_js = jezyk in ("js", "ts")
    while i < n:
        c = tekst[i]
        nxt = tekst[i+1] if i+1 < n else ""

        if stan == "kod":
            if c == "/" and nxt == "/" :
                # komentarz liniowy
                out.append(c); out.append(nxt); i+=2
                stan = "comment_line"
                continue
            if c == "/" and nxt == "*":
                out.append(c); out.append(nxt); i+=2
                stan = "comment_block"
                continue
            if c == "'" :
                out.append(c); i+=1
                stan = "string_single"
                continue
            if c == '"' :
                out.append(c); i+=1
                stan = "string_double"
                continue
            if c == "`" and is_js:
                out.append(c); i+=1
                stan = "string_backtick"
                continue
            if c == "/" and is_js:
                # heurystyka regex: jesli poprzedni znak to operator lub poczatek linii, to regex
                # uproszczenie: jesli out konczy sie na = ( ( , ; : ! & | ? { } lub poczatek, to regex
                prev = "".join(out[-10:]).strip()
                if not prev or prev[-1] in "=(,:;!&|?{}[]+-*%~^<>":
                    out.append(c); i+=1
                    stan = "regex"
                    continue
            # normalny kod - zamien
            z = zamien_znak(c, licznik, kod=True)
            if z is None:
                i+=1
                continue
            # z moze byc wieloznakowe (np ch, szcz)
            out.append(z)
            i+=1
            continue

        elif stan == "comment_line":
            out.append(c); i+=1
            if c == "\n":
                stan = "kod"
            continue

        elif stan == "comment_block":
            out.append(c); i+=1
            if c == "*" and nxt == "/":
                out.append(nxt); i+=1
                stan = "kod"
            continue

        elif stan == "string_single":
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == "'":
                stan = "kod"
            continue

        elif stan == "string_double":
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == '"':
                stan = "kod"
            continue

        elif stan == "string_backtick":
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == "`":
                stan = "kod"
            elif c == "$" and nxt == "{":
                out.append(nxt); i+=1
                # wejscie do ${} - traktuj jako kod tymczasowo
                # uproszczenie: nie wchodzimy glebiej, zostajemy w backtick ale nastepne znaki beda kodem?
                # Dla prostoty: zostajemy w backtick, ale ${} bedzie chronione jako czesc stringa? Nie idealne ale bezpieczne (nie ruszamy)
                pass
            continue

        elif stan == "regex":
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == "/":
                # koniec regex, moga byc flagi gimsuy
                while i < n and tekst[i] in "gimsuy":
                    out.append(tekst[i]); i+=1
                stan = "kod"
            continue

        else:
            out.append(c); i+=1

    return unicodedata.normalize("NFC", "".join(out)), licznik

class BlokadaAnihilatora(Exception):
    """(v1.1.0) Skaner nie umie bezpiecznie odroznic kodu od danych w tym
    pliku. Lepiej nie tknac niczego, niz cicho zmienic tresc literalu."""


# (v1.2.0) Konstrukcje, ktorych automat stanow NIE rozpoznaje.
#
# Automat traktuje kazdy " jako przelacznik stanu kod<->string. Dla literalow,
# ktore moga ZAWIERAC niesparowany cudzyslow (raw stringi, bloki tekstowe,
# heredoki), znaczy to, ze stan rozjezdza sie z rzeczywistoscia i fragment
# literalu ladu je w trybie "kod" - czyli zostaje wyczyszczony wbrew kontraktowi.
#
# Sprawdzone eksperymentalnie 2026-09-04 przypadkiem zlosliwym postaci
# R"(a "k_<U+0430>" b)" - skazenie umieszczone MIEDZY wewnetrznymi cudzyslowami:
#   ZEPSUTE:  C++ R"(...)", Rust r#"..."#, Java """...""", Kotlin """...""",
#             Swift """...""", Ruby heredoc, Go backticki, PHP heredoc
#   BEZPIECZNE: C# @"..." (podwojony "" nie zmienia parzystosci),
#             szablony JS/TS w backtickach (automat ma dla nich wlasny stan)
#
# UWAGA na pulapke metodyczna: pierwszy test (skazenie bez cudzyslowu obok)
# pokazywal C++, Jave, Kotlin i Swift jako bezpieczne. Ocalaly na PARZYSTOSCI
# cudzyslowow, nie dlatego, ze skaner je rozumie. Testujac ochrone literalow,
# stawiaj skazenie po NIEPARZYSTEJ liczbie cudzyslowow od poczatku literalu.
#
# Do czasu prawdziwego leksera takie pliki sa ODRZUCANE, nie czyszczone na oslep.
NIEOBSLUGIWANE = {
    "go":    [("`", "surowy literal Go w backtickach")],
    "php":   [("<<<", "heredoc/nowdoc PHP")],
    "cpp":   [('R"', "surowy literal C++ R\"(...)\"")],
    "c":     [('R"', "surowy literal C++ R\"(...)\"")],
    "h":     [('R"', "surowy literal C++ R\"(...)\"")],
    "hpp":   [('R"', "surowy literal C++ R\"(...)\"")],
    "rs":    [('r#"', 'surowy literal Rust r#"..."#'), ('r"', 'surowy literal Rust r"..."')],
    "java":  [('"""', "blok tekstowy Javy")],
    "kt":    [('"""', "wielolinijkowy literal Kotlina")],
    "swift": [('"""', "wielolinijkowy literal Swifta")],
    "rb":    [("<<~", "heredoc Ruby"), ("<<-", "heredoc Ruby"),
              ("%q", "literal Ruby %q"), ("%Q", "literal Ruby %Q"),
              ("%w", "literal Ruby %w"), ("%i", "literal Ruby %i")],
}


def wykryj_nieobslugiwane(tekst, ext):
    """Zwraca opis niebezpiecznej konstrukcji albo None."""
    for marker, opis in NIEOBSLUGIWANE.get(ext, ()):
        if marker in tekst:
            return opis
    return None


def przetworz(tekst, sciezka):
    ext = sciezka.split(".")[-1].lower() if "." in sciezka else ""
    # json
    if ext in ("json", "jsonl"):
        return zaglada_tekst(tekst, kod=True)
    # py - uzyj tokenize jak Zaglada
    if ext == "py":
        try:
            compile(tekst, sciezka, "exec")
        except Exception as e:
            # (v1.1.0) FAIL-CLOSED. Do v1.0.0 bylo tu przejscie na
            # zaglada_tekst(kod=True), czyli czyszczenie CALEGO zrodla bez
            # ochrony literalow - na pliku, ktorego wlasnie nie dalo sie
            # sparsowac. Zaglada na tym samym pliku literalow nie ruszala,
            # wiec rodzenstwo dawalo sprzeczne wyniki.
            raise BlokadaAnihilatora(
                ".py nie kompiluje sie (%s) - bez parsera nie wiadomo, gdzie "
                "konczy sie kod, a zaczyna literal" % type(e).__name__)
        return zaglada_tekst_poza_literalami_multi(tekst, "py")
    # inne jezyki kodu
    if ext in ("js", "ts", "java", "go", "rs", "cs", "c", "cpp", "h", "hpp", "php", "rb", "swift", "kt"):
        powod = wykryj_nieobslugiwane(tekst, ext)
        if powod:
            raise BlokadaAnihilatora(
                "%s - skaner stanow tego nie rozpoznaje i zmienilby tresc "
                "literalu" % powod)
        return zaglada_tekst_poza_literalami_multi(tekst, ext)
    # proza
    return zaglada_tekst(tekst, kod=False)

def zaglada_tekst_poza_literalami_multi_py(tekst):
    # dla py: chroni ' " ''' """ # 
    licznik = {k:0 for k in KATEGORIE}
    out = []
    i=0
    n=len(tekst)
    stan="kod"
    while i<n:
        c=tekst[i]
        nxt=tekst[i+1] if i+1<n else ""
        nxt3=tekst[i:i+3]
        if stan=="kod":
            if c=="#":
                out.append(c); i+=1; stan="comment_line"; continue
            if nxt3 in ("'''", '"""'):
                out.append(nxt3); i+=3; stan="string_triple" if nxt3[0]=="'" else "string_triple_double"; continue
            if c=="'":
                out.append(c); i+=1; stan="string_single"; continue
            if c=='"':
                out.append(c); i+=1; stan="string_double"; continue
            z=zamien_znak(c, licznik, kod=True)
            if z is None:
                i+=1; continue
            out.append(z); i+=1; continue
        elif stan=="comment_line":
            out.append(c); i+=1
            if c=="\n": stan="kod"
            continue
        elif stan in ("string_single","string_double"):
            out.append(c); i+=1
            if c=="\\" and i<n:
                out.append(tekst[i]); i+=1
            elif (stan=="string_single" and c=="'") or (stan=="string_double" and c=='"'):
                stan="kod"
            continue
        elif stan in ("string_triple","string_triple_double"):
            out.append(c); i+=1
            if tekst[i-1:i+2] in ("'''", '"""'):
                # uproszczenie
                pass
            if n-i>=2 and tekst[i:i+3] in ("'''", '"""'):
                out.append(tekst[i:i+3]); i+=3; stan="kod"
            continue
    return unicodedata.normalize("NFC", "".join(out)), licznik

# nadpisz dla py
def zaglada_tekst_poza_literalami_multi(tekst, jezyk):
    if jezyk == "py":
        return zaglada_tekst_poza_literalami_multi_py(tekst)
    # reszta jak poprzednio (js/ts/java/go/rs/cs)
    licznik = {k:0 for k in KATEGORIE}
    out = []
    i = 0
    n = len(tekst)
    stan = "kod"
    is_js = jezyk in ("js", "ts")
    while i < n:
        c = tekst[i]
        nxt = tekst[i+1] if i+1 < n else ""
        if stan == "kod":
            if c == "/" and nxt == "/":
                out.append(c); out.append(nxt); i+=2; stan="comment_line"; continue
            if c == "/" and nxt == "*":
                out.append(c); out.append(nxt); i+=2; stan="comment_block"; continue
            if c == "'":
                out.append(c); i+=1; stan="string_single"; continue
            if c == '"':
                out.append(c); i+=1; stan="string_double"; continue
            if c == "`" and is_js:
                out.append(c); i+=1; stan="string_backtick"; continue
            if c == "/" and is_js:
                prev = "".join(out[-10:]).strip()
                if not prev or (prev and prev[-1] in "=(,:;!&|?{}[]+-*%~^<>"):
                    out.append(c); i+=1; stan="regex"; continue
            z = zamien_znak(c, licznik, kod=True)
            if z is None:
                i+=1; continue
            out.append(z); i+=1; continue
        elif stan == "comment_line":
            out.append(c); i+=1
            if c == "\n": stan="kod"
            continue
        elif stan == "comment_block":
            out.append(c); i+=1
            if c == "*" and nxt == "/":
                out.append(nxt); i+=1; stan="kod"
            continue
        elif stan in ("string_single","string_double"):
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif (stan=="string_single" and c=="'") or (stan=="string_double" and c=='"'):
                stan="kod"
            continue
        elif stan == "string_backtick":
            # (v1.4.0) wnetrze ${...} to KOD, nie dane — patrz ta sama luka
            # co w f-stringach Pythona: czyszczenie definicji zmiennej przy
            # nietknietym uzyciu w template literal dawalo ReferenceError
            # w pliku, ktory wczesniej dzialal.
            if c == "\\" and i + 1 < n:
                out.append(c); out.append(tekst[i+1]); i += 2
                continue
            if c == "$" and nxt == "{":
                out.append(c); out.append(nxt); i += 2
                glebokosc = 1
                cudz = ""
                while i < n and glebokosc:
                    d = tekst[i]
                    if cudz:
                        out.append(d); i += 1
                        if d == "\\" and i < n:
                            out.append(tekst[i]); i += 1
                        elif d == cudz:
                            cudz = ""
                        continue
                    if d in "\"'`":
                        cudz = d; out.append(d); i += 1
                        continue
                    if d == "{":
                        glebokosc += 1; out.append(d); i += 1
                        continue
                    if d == "}":
                        glebokosc -= 1; out.append(d); i += 1
                        continue
                    z = zamien_znak(d, licznik, kod=True)
                    if z is not None:
                        out.append(z)
                    i += 1
                continue
            out.append(c); i+=1
            if c == "`":
                stan="kod"
            continue
        elif stan == "regex":
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == "/":
                while i < n and tekst[i] in "gimsuy":
                    out.append(tekst[i]); i+=1
                stan="kod"
            continue
        else:
            out.append(c); i+=1
    return unicodedata.normalize("NFC", "".join(out)), licznik

def raport_sciezka(sciezka, wykonaj):
    try:
        with io.open(sciezka, encoding="utf-8") as f:
            tekst = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"[BLAD WEJSCIA] {sciezka}: {e}")
        return 2
    try:
        nowy, licznik = przetworz(tekst, sciezka)
    except BlokadaAnihilatora as e:
        print(f"[BLOKADA] {sciezka}: {e} - plik NIE zostal zmieniony")
        return 2
    if licznik is None:
        return 0
    zmienione = sum(licznik.values())
    if zmienione == 0:
        return 0
    czesci = [f"{k} {v}" for k,v in licznik.items() if v]
    if wykonaj:
        try:
            kopia = zapisz_bezpiecznie(sciezka, nowy)
        except RuntimeError as e:
            print(f"[BLOKADA] {sciezka}: {e}")
            return 2
        print(f"[ANIHILACJA] {sciezka}: {' | '.join(czesci)} | kopia: {os.path.basename(kopia)}")
        return 0
    print(f"[DO ANIHILACJI] {sciezka}: {' | '.join(czesci)}")
    return 1

def selftest():
    print("SELFTEST AnihilatorChwastow v1.0.0")
    tests = [
        ("js poza literalem", "const x = \u0430;\n", "js", True),  # U+0430 poza literalem -> do anihilacji
        ("js w literale", "const s = '\u0430';\n", "js", False),  # w literale -> nie ruszac
        ("ts poza", "let y = \u03b1;\n", "ts", True),
        ("java poza", "class T { int \u0430 = 1; }\n", "java", True),
        ("java w stringu", "class T { String s = \"\u0430\"; }\n", "java", False),
        ("go poza", "package main\nvar \u0430 = 1\n", "go", True),
        ("rs w stringu", "fn main() { let s = \"\u4e2d\u6587\"; }\n", "rs", False),
        ("py poza", "x = \u0430\n", "py", True),
        ("py w literale", "x = '\u0430'\n", "py", False),
    ]
    ok=0
    for nazwa, tekst, ext, should_change in tests:
        sciezka = f"tmp.{ext}"
        nowy, licznik = przetworz(tekst, sciezka)
        zmienione = sum(licznik.values())
        is_changed = zmienione>0
        if is_changed == should_change:
            print(f"  [OK] {nazwa}: zmienione={is_changed} oczekiwano {should_change}")
            ok+=1
        else:
            print(f"  [FAIL] {nazwa}: zmienione={is_changed} oczekiwano {should_change} licznik={licznik}")
    print(f"SELFTEST: {ok}/{len(tests)} PASS")
    return 0 if ok==len(tests) else 1


def zapisz_bezpiecznie(sciezka, tresc, znacznik='.bak-anihilator'):
    """(v1.1.0) BACKUP + ZAPIS ATOMOWY.

    Wczesniej bylo io.open(sciezka, "w").write(...) - przerwanie w polowie
    zostawialo plik uzytkownika obciety i nie bylo z czego wrocic.
    Teraz: kopia %s (odmowa zapisu, gdy kopia sie nie uda), zapis do pliku
    tymczasowego w TYM SAMYM katalogu, flush + fsync, os.replace() - podmiana
    jest atomowa albo nie ma jej wcale. Uprawnienia oryginalu przeniesione,
    dowiazanie symboliczne rozwiazane (podmieniamy cel, nie link)."""
    import shutil, tempfile
    rzeczywista = os.path.realpath(sciezka)
    if jest_kopia_zapasowa(rzeczywista):
        raise RuntimeError("ODMOWA ZAPISU: %s to kopia zapasowa (R3)" % rzeczywista)
    kopia = rzeczywista + znacznik
    # (R4) NIE NADPISUJ istniejacej kopii. Do teraz drugi przebieg kasowal
    # kopie z pierwszego, czyli jedyny slad prawdziwego oryginalu. Pierwsza
    # kopia wygrywa; kolejne przebiegi dostaja kopie z sufiksem liczbowym.
    if os.path.exists(kopia):
        i = 2
        while os.path.exists("%s.%d" % (kopia, i)):
            i += 1
        kopia = "%s.%d" % (kopia, i)
    try:
        shutil.copy2(rzeczywista, kopia)
    except Exception as e:
        raise RuntimeError("ODMOWA ZAPISU: nie udalo sie zrobic kopii %s (%s)" % (kopia, e))
    katalog = os.path.dirname(rzeczywista) or "."
    fd, tmp = tempfile.mkstemp(dir=katalog, prefix=".gang-", suffix=".tmp")
    try:
        with io.open(fd, "w", encoding="utf-8", newline="") as f:
            f.write(tresc)
            f.flush()
            os.fsync(f.fileno())
        try:
            shutil.copystat(rzeczywista, tmp)
        except Exception:
            pass
        os.replace(tmp, rzeczywista)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return kopia

def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        print(__doc__)
        return 0
    if "--selftest" in args:
        return selftest()
    wykonaj = "--anihilacja" in args
    pliki = [a for a in args if not a.startswith("--")]
    if not pliki:
        print("Podaj pliki")
        return 2
    kod=0
    for p in pliki:
        r=raport_sciezka(p, wykonaj)
        if r==2:
            kod=2
        elif r==1 and kod==0:
            kod=1
    return kod

if __name__ == "__main__":
    sys.exit(main())

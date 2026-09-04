#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZAGŁADA KULTURY — siostrzana wobec PogromcaKwiatkow.py.
Pogromca = detektor (niczego nie zmienia). Zagłada = dekontaminator
(unicestwia OBCĄ kulturę znaków, polską zostawia świętą).

Kontrakt (numer wersji: WERSJA ponizej i WERSJE.json):
- cyrylica/greka -> transliteracja PO POLSKU (U+043FU+0440U+0438U+0432U+0435U+0442 -> priwet, U+041CU+043EU+0441U+043AU+0432U+0430 -> Moskwa)
- homoglify łacińskie -> baza (U+017F->s, U+00DF->ss, U+0153->oe, U+00F8->o, U+0111->d, U+00FE->th, U+0131->i)
- litery łacińskie spoza dozwolonych -> zdejmij ogonki (U+010D->c, U+0101->a);
  polskie ąćęłńóśźż NIGDY (ł jest polskie, U+00F8 nie jest)
- cyfry Nd (wszystkie pisma) -> ASCII 0-9; pełna szerokość -> pół (NFKC)
- pisma bez tabeli (CJK, kana, hangul, arabskie, hebrajskie, tajskie...) -> USUŃ
- emoji/symbole spoza palety -> USUŃ; niewidzialne (Cc/Cf/Cn/Co/Cs/Mn) -> USUŃ
- łamacze linii -> LF; twarde spacje -> zwykła spacja; NFC na końcu
- .py: to, co się kompiluje, modyfikowane WYŁĄCZNIE poza literałami/komentarzami
  (stdlib tokenize); .py zepsute -> awaryjny skaner stanów + bramka compile()
- POLSKA KULTURA ZOSTAJE: ASCII + ąćęłńóśźżĄĆĘŁŃÓŚŹŻ + typografia projektowa

Użycie:
  python3 ZagladaKultury.py PLIK...          # raport co ulegnie zagładzie
  python3 ZagladaKultury.py --zaglada PLIK... # wykonaj zagładę w miejscu
Exit: 0 = czysto (nic do zrobienia / po zagładzie czysto poza chronionymi),
      1 = jest obca kultura do zagłady (tryb raportu), 2 = błąd wejścia.

(v1.0.7) OSTRZEZENIA: gdy po --zaglada plik .py/.json nadal sie nie parsuje, drukowane jest [OSTRZEZENIE] (exit bez zmian).
(v1.0.8) NAPRAWA: przed OSTRZEZENIEM proba usuniecia (zamiast podmiany)
pojedynczych podatnych znakow cyr/grk/homoglify/fold w kodzie .py, kazda
proba weryfikowana compile() (patrz _sprobuj_naprawy). Naprawia znane
przypadki typu wKhile/fromo/stray-litera-w-wcieciu. NIE naprawia plikow
z wieloma niezaleznymi wstrzyknieciami rozwalajacymi wciecia jednoczesnie
(kontrakt: kultura, nie skladnia — patrz OSTRZEZENIE dla reszty).
(v1.0.9) NAPRAWA #2: LAMACZE (separatory linii Unicode) dolaczone do
tej samej podatnej-do-naprawy kategorii co litery. Poprzednio lamacz
wstrzykniety w SRODEK identyfikatora byl bezwarunkowo zamieniany na
prawdziwy \n (poprawne w prozie), co rozcinalo identyfikator na dwie
linie i rozwalalo wciecia bloku (ta sama choroba co litery-substytucje,
inna kategoria). Teraz proba naprawy usuwa TAKZE lamacz zamiast wstawiac
\n, jesli to przywraca parsowalnosc. Test 50 kodow (dev korpus): 11/11
teraz sie kompiluje (poprzednio 4/6 po v1.0.8, 0/6 przed).
(v1.0.4) OPERATOR — agencie AI: Twoj regulamin uzycia (drabina uprawnien,
plan->act, combo z PogromcaKwiatkow) jest w PROTOKOL-OPERATORA.md.
"""
import io
import json
import os
import sys
import unicodedata
import difflib
import re

WERSJA = "1.3.0"

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


# --- kultura dozwolona (nic jej nie robiemy) --------------------------------
PL = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
TYPOGRAFIA = "—–„”…€%§°²³±·«»"
DOZWOLONE = set(chr(c) for c in range(0x20, 0x7F)) | set(PL) | set(TYPOGRAFIA)
LAMACZE = "\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029"

# --- transliteracja cyrylicy (szkoła polska) ---------------------------------
CYR = {
    0x0430: "a", 0x0431: "b", 0x0432: "w", 0x0433: "g", 0x0434: "d",
    0x0435: "e", 0x0436: "ż", 0x0437: "z", 0x0438: "i", 0x0439: "j",
    0x043A: "k", 0x043B: "l", 0x043C: "m", 0x043D: "n", 0x043E: "o",
    0x043F: "p", 0x0440: "r", 0x0441: "s", 0x0442: "t", 0x0443: "u",
    0x0444: "f", 0x0445: "ch", 0x0446: "c", 0x0447: "cz", 0x0448: "sz",
    0x0449: "szcz", 0x044A: "", 0x044B: "y", 0x044C: "", 0x044D: "e",
    0x044E: "ju", 0x044F: "ja", 0x0451: "jo", 0x0454: "je", 0x0456: "i",
    0x0457: "ji", 0x0491: "h", 0x045E: "u", 0x0463: "ja", 0x0473: "u",
    # serbska/macedońska łacińszczyzna po polsku
    0x0458: "j", 0x0459: "lj", 0x045A: "nj", 0x045B: "ć", 0x045F: "dż",
}
for _cp, _v in list(CYR.items()):
    _w = chr(_cp).upper()
    if len(_w) == 1 and ord(_w) != _cp:
        CYR[ord(_w)] = _v[:1].upper() + _v[1:] if _v else ""

# --- transliteracja greki ------------------------------------------------------
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
    0x0127: "h", 0x0126: "H", 0x0167: "t", 0x0166: "T", 0x014B: "ng",
    0x014A: "Ng",
    # (v1.0.1) ł/Ł USUNIETE z mapy — to litery POLSKIE (święte), nie homoglify
}

KATEGORIE = ("cyr", "grk", "homoglify", "ogonki", "cyfry", "fold",
             "pisma", "symbole", "niewidzialne", "spacje", "lamacze")


def baza_bez_ogonkow(c):
    """U+010D -> c, U+0101 -> a (NFD); None gdy znak się nie rozkłada."""
    d = unicodedata.normalize("NFD", c)
    if len(d) > 1 and d[0].isascii() and d[0].isalpha():
        return d[0]
    return None


def zamien_znak(c, licznik, kod=False):
    """Jeden znak -> (zamiennik lub None=usuń). Aktualizuje licznik.
    kod=True (wewnatrz .py poza literalami): twarde spacje USUWAMY
    (sklejaja urwany token) zamiast wstawiac spacje, ktora rozwala
    skladnie na zawsze (v1.0.2)."""
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
    d = unicodedata.normalize("NFD", c)
    if len(d) > 1 and ord(d[0]) in CYR:      # U+0430U+043AU+0446U+0435U+043DU+0442U+043EU+0432U+0430U+043DU+0430 U+043Airyłica: U+0451U+0301/U+04EF
        licznik["cyr"] += 1
        return CYR[ord(d[0])]
    if len(d) > 1 and ord(d[0]) in GREK:     # akcentowana greka: U+03AC -> a
        licznik["grk"] += 1
        return GREK[ord(d[0])]
    if len(d) > 1 and d[0] in DOZWOLONE and d[0] not in "\t\n\r":
        # ą/ę/ł... są w DOZWOLONE -> tu trafiają tylko obce ogonki (U+010D, U+0101)
        if c not in PL:
            licznik["ogonki"] += 1
            return d[0]
    if kat == "Nd" and not c.isascii():
        licznik["cyfry"] += 1
        return str(unicodedata.digit(c))
    if kat == "Zs":
        if kod:
            licznik["niewidzialne"] += 1
            return None
        licznik["spacje"] += 1
        return " "
    if kat in ("Cf", "Cc", "Cn", "Co", "Cs", "Mn", "Mc", "Me"):
        licznik["niewidzialne"] += 1
        return None
    z = unicodedata.normalize("NFKC", c)
    if z != c and z and all(q in DOZWOLONE or q.isascii() for q in z):
        licznik["fold"] += 1
        return z
    if kat.startswith("L"):
        licznik["pisma"] += 1
        return None
    licznik["symbole"] += 1
    return None


def zaglada_tekst(tekst, kod=False):
    licznik = dict((k, 0) for k in KATEGORIE)
    out = []
    for c in tekst:
        z = zamien_znak(c, licznik, kod=kod)
        if z is not None:
            out.append(z)
    return unicodedata.normalize("NFC", "".join(out)), licznik


# --- ochrona literałów .py (idea z v8.0.2 Pogromcy) ---------------------------
def _chronione_pozycje(tekst):
    import tokenize
    typy = {tokenize.STRING, tokenize.COMMENT}
    for a in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):
        if hasattr(tokenize, a):
            typy.add(getattr(tokenize, a))
    starty, poz = [], 0
    for linia in tekst.split("\n"):
        starty.append(poz)
        poz += len(linia) + 1
    chronione = set()
    for tok in tokenize.generate_tokens(io.StringIO(tekst).readline):
        if tok.type in typy:
            s = starty[tok.start[0] - 1] + tok.start[1]
            e = starty[tok.end[0] - 1] + tok.end[1]
            chronione.update(range(s, e))
    return chronione


def zaglada_tekst_poza_literalami(tekst):
    try:
        chronione = _chronione_pozycje(tekst)
    except Exception:
        return tekst, None
    licznik = dict((k, 0) for k in KATEGORIE)
    out = []
    for i, c in enumerate(tekst):
        if i in chronione:
            out.append(c)
            continue
        z = zamien_znak(c, licznik, kod=True)
        if z is not None:
            out.append(z)
    return unicodedata.normalize("NFC", "".join(out)), licznik


# kategorie ktore PODMIENIAJA jeden znak na cos innego niz usuniecie
# (litere/litery ALBO prawdziwy \n dla lamaczy). W prozie to poprawne
# (zachowanie sensu slowa / akapitu). W kodzie, poza literalami, pojedynczy
# taki znak wstawiony w bialy znak, sklejony ze slowem kluczowym, albo
# rozcinajacy identyfikator na dwie linie (lamacz -> \n) rozwala skladnie
# identycznie jak twarda spacja (patrz v1.0.2) — tyle ze NFC/transliteracja
# tego nie widzi, bo wynikiem jest formalnie "poprawny" tekst.
KATEGORIE_PODATNE_W_KODZIE = ("cyr", "grk", "homoglify", "fold", "lamacze")


def zaglada_tekst_poza_literalami_surowy(tekst, pomin_n=frozenset()):
    """Awaryjny skaner stanów dla .py, które się NIE kompiluje.
    pomin_n: zbior numerow (0-based, w kolejnosci napotkania) podstawien
    z KATEGORIE_PODATNE_W_KODZIE, ktore maja zostac USUNIETE zamiast
    podmienione (litera) / wstawione jako \\n (lamacz) — uzywane przez
    probe naprawy w przetworz() (v1.0.8)."""
    out = []
    i, n = 0, len(tekst)
    stan = "kod"
    cudzyslow = None  # (v1.1.1) pamieta KTORY znak otworzyl lancuch
    licznik = dict((k, 0) for k in KATEGORIE)
    nr_podatny = 0
    while i < n:
        c = tekst[i]
        if stan == "kod":
            if c == "#":
                stan = "hash"
            elif tekst[i:i + 3] in ("'''", '"""'):
                stan = "trojka"
                cudzyslow = tekst[i:i + 3]
                out.append(tekst[i:i + 3])
                i += 3
                continue
            elif c in ("'", '"'):
                stan = "lancuch"
                cudzyslow = c
            elif c in LAMACZE:
                licznik["lamacze"] += 1
                biezacy_nr = nr_podatny
                nr_podatny += 1
                if biezacy_nr in pomin_n:
                    i += 1
                    continue
                c = "\n"
            else:
                przed = dict(licznik)
                z = zamien_znak(c, licznik, kod=True)
                podatne_teraz = any(
                    licznik[k] != przed[k] for k in KATEGORIE_PODATNE_W_KODZIE
                )
                if podatne_teraz:
                    biezacy_nr = nr_podatny
                    nr_podatny += 1
                    if biezacy_nr in pomin_n:
                        i += 1
                        continue
                if z is None:
                    i += 1
                    continue
                c = z
        elif stan == "hash":
            if c == "\n":
                stan = "kod"
        elif stan == "lancuch":
            if c == "\\" and i + 1 < n:
                out.append(c)
                i += 1
                out.append(tekst[i])
                i += 1
                continue
            if c == cudzyslow or c == "\n":
                stan = "kod"
                cudzyslow = None
        else:
            if c == "\\" and i + 1 < n:
                out.append(c)
                i += 1
                out.append(tekst[i])
                i += 1
                continue
            if tekst[i:i + 3] == cudzyslow:
                stan = "kod"
                cudzyslow = None
                out.append(tekst[i:i + 3])
                i += 3
                continue
        out.append(c)
        i += 1
    return unicodedata.normalize("NFC", "".join(out)), licznik, nr_podatny


def _sprobuj_naprawy(tekst, sciezka):
    """(v1.0.8) Gdy ani ostrozny (surowy) ani pelny wariant sie nie
    kompiluja: bramka compile() nadal rzadzi, ale teraz probujemy USUNAC
    (zamiast podmienic) pojedyncze podatne znaki (cyr/grk/homoglify/fold)
    zamiast zawsze je transliterowac. Kazda proba jest weryfikowana
    compile() — nic nie wchodzi bez zielonej bramki. Zwraca
    (tekst, licznik, liczba_usuniec) albo None gdy nie znaleziono naprawy
    (wtedy wolajacy wraca do dotychczasowego zachowania: OSTRZEZENIE)."""
    _, _, total = zaglada_tekst_poza_literalami_surowy(tekst)
    if total == 0:
        return None
    for nr in range(total):
        kandydat, lk, _ = zaglada_tekst_poza_literalami_surowy(tekst, pomin_n={nr})
        try:
            compile(kandydat, sciezka, "exec")
            return kandydat, lk, 1
        except SyntaxError:
            continue
    wszystkie = frozenset(range(total))
    kandydat, lk, _ = zaglada_tekst_poza_literalami_surowy(tekst, pomin_n=wszystkie)
    try:
        compile(kandydat, sciezka, "exec")
        return kandydat, lk, total
    except SyntaxError:
        return None


def _napraw_niespojnosc_identyfikatorow(oryginal, kandydat, sciezka):
    """(v1.1.0) OSTATNIA kontrola PO udanym czyszczeniu — nawet gdy compile()
    przeszlo juz na pierwszy strzal (transliteracja/fold dala poprawna
    SKLADNIOWO nazwe). Znalezisko z turnieju zewnetrznego (2026-09-02):
    pojedyncze wystapienie identyfikatora zanieczyszczone znakiem
    fold-NFKC (np. U+2167 rzymska osemka/Kelvin) transliterowanym na litery daje SKLADNIOWO
    poprawna, ale INNA nazwe niz reszta wystapien tej samej zmiennej w
    pliku (np. self._scandir_path w __slots__ i przy odczycie, ale
    self._VIIIscandir_patKh przy zapisie) — plik kompiluje sie, ale
    wybucha AttributeError w runtime. compile() tego nie widzi, bo
    sprawdza tylko skladnie, nie spojnosc nazw.

    Metoda: diff oryginal<->kandydat lokalizuje kazda zmiane; rozszerzona
    do pelnej granicy identyfikatora (\\w+); jesli WERSJA-Z-USUNIETYM-
    FRAGMENTEM tego identyfikatora juz istnieje jako INNY identyfikator
    gdzie indziej w kandydacie (silny sygnal ze to ta sama zmienna,
    zabrudzona tylko w jednym miejscu) — probuje usuniecia zamiast
    transliteracji, weryfikuje compile() jak zawsze. Nigdy nie pogarsza
    wyniku (przy porazce bramki zwraca kandydata bez zmian)."""
    if oryginal == kandydat:
        return kandydat
    sm = difflib.SequenceMatcher(None, oryginal, kandydat, autojunk=False)
    zmiany = [op for op in sm.get_opcodes() if op[0] != "equal"]
    if not zmiany:
        return kandydat
    id_licznik = {}
    for tok in re.findall(r'[A-Za-z_][A-Za-z0-9_]*', kandydat):
        id_licznik[tok] = id_licznik.get(tok, 0) + 1
    # grupuj zmiany po tokenie ktory obejmuja (jeden identyfikator moze miec
    # KILKA niezaleznych podstawien naraz - musza byc usuniete RAZEM, bo
    # usuniecie tylko jednego z dwoch nie odtworzy oryginalnej nazwy)
    grupy = {}
    for _, _, _, j1, j2 in zmiany:
        lewo, prawo = j1, j2
        while lewo > 0 and (kandydat[lewo - 1].isalnum() or kandydat[lewo - 1] == "_"):
            lewo -= 1
        while prawo < len(kandydat) and (kandydat[prawo].isalnum() or kandydat[prawo] == "_"):
            prawo += 1
        if lewo >= prawo:
            continue
        pelny_tok = kandydat[lewo:prawo]
        if not pelny_tok or not (pelny_tok[0].isalpha() or pelny_tok[0] == "_"):
            continue
        grupy.setdefault((lewo, prawo), []).append((j1, j2))
    poprawki = []
    for (lewo, prawo), spany in grupy.items():
        pelny_tok = kandydat[lewo:prawo]
        wariant = []
        kursor = lewo
        for j1, j2 in sorted(spany):
            wariant.append(kandydat[kursor:j1])
            kursor = j2
        wariant.append(kandydat[kursor:prawo])
        wariant = "".join(wariant)
        if wariant == pelny_tok or not wariant:
            continue
        if not (wariant[0].isalpha() or wariant[0] == "_"):
            continue
        # (v1.3.0) STRAZNIK PRZED SKLEJENIEM DWOCH ZMIENNYCH W JEDNA.
        # Do v1.2.0 wystarczylo, ze skrocona nazwa gdzies istnieje - i wtedy
        # "wartosc" oraz "wartosca" (dwie ROZNE zmienne) byly sklejane:
        #   PRZED: wartosc = 1 ; wartosc<U+0430> = 2 ; print(wartosc, wartosc<U+0430>)
        #   PO:    wartosc = 1 ; wartosc  = 2 ; print(wartosc, wartosc)
        # Plik kompilowal sie, a program liczyl co innego. compile() tego nie
        # widzi, bo skladnia jest poprawna.
        #
        # Odroznik: naprawa ma sens TYLKO wtedy, gdy zabrudzona nazwa jest
        # odludkiem - pojawia sie DOKLADNIE RAZ, a jej czysty odpowiednik
        # wystepuje gdzie indziej (to znalezisko z turnieju: _scandir_path
        # kilka razy, _VIIIscandir_patKh raz). Nazwa uzywana konsekwentnie
        # wiele razy jest osobna zmienna i nie wolno jej scalac.
        if id_licznik.get(pelny_tok, 0) != 1:
            continue
        if id_licznik.get(wariant, 0) > 0:
            poprawki.extend(spany)
    if not poprawki:
        return kandydat
    nowy = kandydat
    for j1, j2 in sorted(set(poprawki), reverse=True):
        nowy = nowy[:j1] + nowy[j2:]
    try:
        compile(nowy, sciezka, "exec")
    except SyntaxError:
        return kandydat
    return nowy


def przetworz(tekst, sciezka):
    """Zwraca (nowy_tekst, licznik). .py bezpiecznie, .json jak kod
    (twarde spacje SKLEJAJA - dane strukturalne, v1.0.3), proza agresywnie."""
    if sciezka.endswith((".json", ".jsonl")):
        return zaglada_tekst(tekst, kod=True)
    if not sciezka.endswith(".py"):
        return zaglada_tekst(tekst)
    wynik = _przetworz_py(tekst, sciezka)
    nowy, licznik = wynik
    if licznik is not None and nowy != tekst:
        naprawiony = _napraw_niespojnosc_identyfikatorow(tekst, nowy, sciezka)
        if naprawiony != nowy:
            licznik = dict(licznik)
            licznik["spojnosc_naprawiona"] = licznik.get("spojnosc_naprawiona", 0) + 1
            nowy = naprawiony
    return nowy, licznik


def _przetworz_py(tekst, sciezka):
    try:
        compile(tekst, sciezka, "exec")
    except SyntaxError:
        ostrozny, lk, _ = zaglada_tekst_poza_literalami_surowy(tekst)
        pelny, lp = zaglada_tekst(tekst)
        try:
            compile(ostrozny, sciezka, "exec")
            return ostrozny, lk
        except SyntaxError:
            try:
                compile(pelny, sciezka, "exec")
                return pelny, lp
            except SyntaxError:
                naprawa = _sprobuj_naprawy(tekst, sciezka)
                if naprawa is not None:
                    tekst_n, lk_n, usuniete = naprawa
                    lk_n["naprawa_usuniecia"] = usuniete
                    return tekst_n, lk_n
                return ostrozny, lk  # nie do naprawienia - nie psujemy dalej
    nowy, licznik = zaglada_tekst_poza_literalami(tekst)
    try:
        compile(nowy, sciezka, "exec")
        return nowy, licznik
    except SyntaxError:
        return tekst, None  # (bezpieczenstwo) bramka nie przepuscila


def raport_sciezka(sciezka, wykonaj):
    try:
        with io.open(sciezka, encoding="utf-8") as f:
            tekst = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print("[BLAD WEJSCIA] %s: %s" % (sciezka, ascii(str(e))[:80]))
        return 2
    nowy, licznik = przetworz(tekst, sciezka)
    if licznik is None:
        # (v1.0.7) OBSERWOWALNOSC: bramka nie przepuscila - plik nietkniety
        print("[OSTRZEZENIE] %s: bramka compile() nie przepuscila zadnego wariantu - plik ZOSTAL NIETKNIETY" % sciezka)
        return 0
    zmienione = sum(licznik.values())
    if zmienione == 0:
        return 0
    czesci = ["%s %d" % (k, v) for k, v in licznik.items() if v]
    if wykonaj:
        try:
            kopia = zapisz_bezpiecznie(sciezka, nowy)
        except RuntimeError as e:
            print("[BLOKADA] %s: %s" % (sciezka, e))
            return 2
        print("[ZAGLADA] %s: %s | kopia: %s"
              % (sciezka, " | ".join(czesci), os.path.basename(kopia)))
        # (v1.0.7) OBSERWOWALNOSC: kultura usunieta, ale parsowalnosc moze nie wrocic
        if sciezka.endswith(".py"):
            try:
                compile(nowy, sciezka, "exec")
            except SyntaxError:
                print("[OSTRZEZENIE] %s: nie przywrocono parsowalnosci - wymaga recznej naprawy (kontrakt: kultura, nie skladnia)" % sciezka)
        elif sciezka.endswith((".json", ".jsonl")):
            try:
                json.loads(nowy)
            except ValueError:
                print("[OSTRZEZENIE] %s: nie przywrocono waznosci JSON - wymaga recznej naprawy (kontrakt: kultura, nie struktura)" % sciezka)
        return 0
    print("[DO ZAGLADY] %s: %s" % (sciezka, " | ".join(czesci)))
    return 1


def selftest():
    """Selftest Zaglady - dowod ze transliteruje i usuwa, a polskie zostawia."""
    print("SELFTEST Zaglady Kultury v1.1.1")
    testy = [
        ("cyrylica U+0430 -> a", "a\u0430b", "txt", "aab", True),
        ("greka U+03B1 -> a", "x\u03b1y", "txt", "xay", True),
        ("CJK U+4E2D -> USUN", "a\u4e2db", "txt", "ab", True),
        ("emoji U+1F600 -> USUN", "a\U0001f600b", "txt", "ab", True),
        ("NBSP U+00A0 -> spacja w prozie", "a\u00a0b", "txt", "a b", True),
        ("ZWSP U+200B -> USUN", "a\u200bb", "txt", "ab", True),
        ("lamacz U+2028 -> LF", "a\u2028b", "txt", "a\nb", True),
        ("Kelvin U+212A -> K via NFKC", "\u212a", "txt", "K", True),
        ("polskie ogonki swiete", "ąćęłńóśźż", "txt", "ąćęłńóśźż", False),
        ("py poza literalem", "x = \u0430\n", "py", "x = a\n", True),
        ("py w literale - sacred", "x = '\u0430'\n", "py", "x = '\u0430'\n", False),
    ]
    ok = 0
    for nazwa, tekst, ext, oczekiwany, should_change in testy:
        sciezka = f"tmp.{ext}"
        nowy, licznik = przetworz(tekst, sciezka)
        zmienione = sum(licznik.values()) if licznik else 0
        is_changed = (nowy != tekst) or (zmienione > 0)
        # Dla testow gdzie oczekujemy braku zmiany, nowy == tekst
        if should_change:
            if nowy == oczekiwany and zmienione > 0:
                print(f"  [OK] {nazwa}: '{oczekiwany}'")
                ok += 1
            else:
                print(f"  [FAIL] {nazwa}: got '{nowy}' expected '{oczekiwany}' licznik={licznik}")
        else:
            if nowy == oczekiwany and zmienione == 0:
                print(f"  [OK] {nazwa}: bez zmian jak trzeba")
                ok += 1
            else:
                print(f"  [FAIL] {nazwa}: got '{nowy}' expected '{oczekiwany}' licznik={licznik}")
    print(f"SELFTEST: {ok}/{len(testy)} PASS")
    print("WERDYKT: PASS - anihiluje obce, polskie zostawia" if ok == len(testy) else "WERDYKT: FAIL")
    return 0 if ok == len(testy) else 1



def zapisz_bezpiecznie(sciezka, tresc, znacznik='.bak-zaglada'):
    """(v1.2.0) BACKUP + ZAPIS ATOMOWY.

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
    if "--selftest" in args:
        return selftest()
    wykonaj = "--zaglada" in args
    pliki = [a for a in args if not a.startswith("--")]
    if not pliki:
        print(__doc__)
        return 0
    kod = 0
    for p in pliki:
        r = raport_sciezka(p, wykonaj)
        if r == 2:
            kod = 2
        elif r == 1 and kod == 0:
            kod = 1
    return kod


if __name__ == "__main__":
    sys.exit(main())

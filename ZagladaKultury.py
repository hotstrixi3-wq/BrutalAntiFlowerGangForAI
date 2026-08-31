#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZAGŁADA KULTURY v1.0.0 — siostrzana wobec PogromcaKwiatkow.py.
Pogromca = detektor (niczego nie zmienia). Zagłada = dekontaminator
(unicestwia OBCĄ kulturę znaków, polską zostawia świętą).

Kontrakt v1.0.0:
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

(v1.0.4) OPERATOR — agencie AI: Twoj regulamin uzycia (drabina uprawnien,
plan->act, combo z PogromcaKwiatkow) jest w PROTOKOL-OPERATORA.md.
"""
import io
import os
import sys
import unicodedata

WERSJA = "1.0.5"

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


def zaglada_tekst_poza_literalami_surowy(tekst):
    """Awaryjny skaner stanów dla .py, które się NIE kompiluje."""
    out = []
    i, n = 0, len(tekst)
    stan = "kod"
    licznik = dict((k, 0) for k in KATEGORIE)
    while i < n:
        c = tekst[i]
        if stan == "kod":
            if c == "#":
                stan = "hash"
            elif tekst[i:i + 3] in ("'''", '"""'):
                stan = "trojka"
                out.append(tekst[i:i + 3])
                i += 3
                continue
            elif c in ("'", '"'):
                stan = "lancuch"
            elif c in LAMACZE:
                licznik["lamacze"] += 1
                c = "\n"
            else:
                z = zamien_znak(c, licznik, kod=True)
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
            if c in ("'", '"') or c == "\n":
                stan = "kod"
        else:
            if c == "\\" and i + 1 < n:
                out.append(c)
                i += 1
                out.append(tekst[i])
                i += 1
                continue
            if tekst[i:i + 3] in ("'''", '"""'):
                stan = "kod"
                out.append(tekst[i:i + 3])
                i += 3
                continue
        out.append(c)
        i += 1
    return unicodedata.normalize("NFC", "".join(out)), licznik


def przetworz(tekst, sciezka):
    """Zwraca (nowy_tekst, licznik). .py bezpiecznie, .json jak kod
    (twarde spacje SKLEJAJA - dane strukturalne, v1.0.3), proza agresywnie."""
    if sciezka.endswith((".json", ".jsonl")):
        return zaglada_tekst(tekst, kod=True)
    if not sciezka.endswith(".py"):
        return zaglada_tekst(tekst)
    try:
        compile(tekst, sciezka, "exec")
    except SyntaxError:
        ostrozny, lk = zaglada_tekst_poza_literalami_surowy(tekst)
        pelny, lp = zaglada_tekst(tekst)
        try:
            compile(ostrozny, sciezka, "exec")
            return ostrozny, lk
        except SyntaxError:
            try:
                compile(pelny, sciezka, "exec")
                return pelny, lp
            except SyntaxError:
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
        return 0
    zmienione = sum(licznik.values())
    if zmienione == 0:
        return 0
    czesci = ["%s %d" % (k, v) for k, v in licznik.items() if v]
    if wykonaj:
        with io.open(sciezka, "w", encoding="utf-8", newline="") as f:
            f.write(nowy)
        print("[ZAGLADA] %s: %s" % (sciezka, " | ".join(czesci)))
        return 0
    print("[DO ZAGLADY] %s: %s" % (sciezka, " | ".join(czesci)))
    return 1


def main():
    args = [a for a in sys.argv[1:]]
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

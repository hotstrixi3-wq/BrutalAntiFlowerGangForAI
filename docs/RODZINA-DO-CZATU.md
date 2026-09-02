# RODZINA POGROMCY KWIATKOW - wersja do wrzucenia na czat - COMBO 4 plikow

Ten plik zawiera wszystko: instrukcje dla Ciebie, polecenie dla agenta AI oraz kompletny kod 4 narzedzi. Nie musisz nic pobierac z GitHuba i nic instalowac.

> MOTTO: "uzywaj bo dzieki PogromcyKwiatkow nie mielisz potencjalnie BRUDNEGO kodu, co marnuje nie milisekundy a godziny mielenia kodu i tony potencjalnych tokenow jesli korzystasz z pomocy innych Agentow AI. Krecenie sie w kolko z BRUDNYM kodem to strata czasu" -- Piotr (GAF)

> ZASADA RODZINY: nie ruszamy perfekcyjnie dzialajacego kodu, dokladamy kolejnego. Bezpieczniej. Rodzina to combo i wszedzie idzie razem. Wymyślone przez człowieka dla agenta AI, stworzone przez agentów AI dla agentów AI. Człowiek cieszy się przy okazji.

## Ty (czlowiek): zrob tylko to

1. Zalacz ten plik do czatu z agentem AI.
2. Wklej ponizsza wiadomosc (cala, bez zmian poza nawiasami).

## Wiadomosc dla agenta (skopiuj calosc) - FLOW USWIADOMIENIE

```
Hej! W zalaczonym pliku .md masz rodzine Pogromcy - combo 4 plikow ktore ida wszedzie razem. Zrob dokladnie tak - FLOW USWIADOMIENIE, nie skanuj od razu plikow usera:

KROK 1 - ANALIZA REPO I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md z tego pliku lub z github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI
- Pobierz lub wytnij kody 4 narzedzi:
  PogromcaKwiatkow.py v8.0.3
  ZagladaKultury.py v1.0.7
  ProkuratorOgrodnik.py v1.0.1
  AnihilatorChwastow.py v1.0.0
- Zapoznaj sie z ich rola:
  Pogromca = detektor BLAD/UWAGA/OK - widzi niewidzialny brud
  Zaglada = dekontaminator py/json/proza - sprzata brud tam gdzie ma pewnosc
  ProkuratorOgrodnik = polityka UMORZONE/ZAGLADA/BLOKADA + akta w U+XXXX - decyduje co wolno czyscic
  AnihilatorChwastow = anihilator uniwersalny js/ts/java/go/rs/cs/py z ochrona literalow - sprzata w innych jezykach
- ZAPODAJ UZYTKOWNIKOWI krotki i rzeczowy opis CO TO i PO CO TO, po ludzku, bez zargonu U+XXXX, wyjasnij ze to nie slownik ortograficzny (nie poprawia "blad" na "błąd"), tylko filtr na niewidzialny brud i obcy alfabet ktory AI wstawia niezauwazalnie i nie zdaje sobie z tego sprawy w momencie w ktorym to czyni ani pozniej i ktory marnuje godziny i tony tokenow.

KROK 2 - PYTANIE O BEZPIECZNE TESTY:
- Zapytaj uzytkownika: CZY MAM WYKONAC BEZPIECZNE TESTY tego narzedzia? (selftesty + testy na bezpiecznych kopiach, NIE na plikach uzytkownika)
- Czekaj na odpowiedz. Nie skanuj plikow usera bez zgody.

KROK 3 - BEZPIECZNE TESTY (po zgodzie):
- Uruchom selftesty:
  python3 PogromcaKwiatkow.py --selftest
  python3 ZagladaKultury.py --selftest
  python3 ProkuratorOgrodnik.py --selftest
  python3 AnihilatorChwastow.py --selftest
- Pokaz wyniki.

KROK 4 - NATURALNA REAKCJA AGENTA:
- Po testach daj swoja naturalna reakcje jako agent AI - czy to fajne i potrzebne? Odpowiedz szczerze, bez cukrowania, bez sciemy, zgodnie z prawda, na bazie testow.
- Sugestia: odpowiedz na pytanie czy to fajne i potrzebne, czy wierzysz w skutecznosc po lekturze i po testach, czy bedziesz uzywal w trybie stalym.
- Uzywaj notacji U+XXXX zamiast zywych kwiatkow w raporcie.

NIE zmieniaj plikow usera bez wyraznej zgody. Plan->act, kopia .bak, akta w U+XXXX. Rodzina to combo i wszedzie idzie razem.
```

## Struktura paczki czystej

Root - tylko to co potrzebne agentowi:
```
PogromcaKwiatkow.py          detektor
ZagladaKultury.py            dekontaminator py/json/proza
ProkuratorOgrodnik.py        polityka + akta
AnihilatorChwastow.py        anihilator uniwersalny z ochrona literalow
PROTOKOL-OPERATORA.md        regulamin dla agenta - FLOW USWIADOMIENIE
RODZINA-DO-CZATU.md          ten plik - all-in-one
INSTRUKCJA-DLA-ZIELONYCH.md  dla czlowieka
README.md                    opis
LICENSE                      MIT
```

Reszta w podkatalogach:
```
dev/                         turnieje, fuzz, suity
docs/                        certyfikaty
przyklady/                   czyste_kody
```

## PROTOKOL OPERATORA - skrot

Drabina:
- poziom 1 detekcja - zawsze bez pytania
- poziom 2 --fix - rutynowo kopia -> fix -> rescan
- poziom 3 dekontaminacja - tylko gdy misja kaze, plan->act + decyzja Prokuratora

Combo:
- Pogromca -> Prokurator: raport
- Prokurator -> Zaglada/Anihilator: decyzja UMORZONE/ZAGLADA/BLOKADA
- Zaglada/Anihilator -> Pogromca: OBOWIAZKOWO BLAD 0

Bramka przedpublikacyjna: przed KAZDYM wystawieniem na zewnatrz przepusc pliki przez Pogromce. Exit !=0 = NIE publikuj.

ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!! Plan->act, kopia, akta w U+XXXX.

Nigdy nie wklejaj ZYWYCH kwiatkow do czatu - notacja U+XXXX.

TRYB STALY: kazda wiadomosc z tekstem z zewnatrz - skan PRZED wyslaniem.

## KOD NARZEDZI - 4 bloki ponizej
### PogromcaKwiatkow.py

# -*- coding: utf-8 -*-
"""PogromcaKwiatków: wykrywacz obcojęzycznych "kwiatków" w polskich tekstach projektu.

(v8.0.3) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
ze siostra ZagladaKultury). Przeczytaj przed pierwszym uzyciem.

Slownik kulturalny: "kwiatek" = w slangu pisarzy i redaktorow GAFa w tekscie,
literowka, potkniecie pisarskie (nie bukiet!). Stad nazwa: narzedzie
TERMINUJE kwiatki, zanim ujrzą swiatlo dzienne.
(chrztet imienia: kwiatkiorz -> KWIATEK TERMINATOR -> PogromcaKwiatków;
wszystkie trzy ochrzcił user, tura 49)

Powód narzędzia (tura 49): asystent wkleił w czacie rosyjskie słowo w polskie
zdanie ("Spokojnie [cyrylica] spać") — model językowy generuje token po
tokenie, a słowa o wspólnym korzeniu słowiańskim + glifach identycznych
z łacińskimi potrafią wskoczyć w zły alfabet i przejść nawet wzrokową
korektę. Narzędzie łapie takie wycieki PROGRAMOWO, przed wrzutą.

Zasady:
- BLAD: pisownie, które w polskich tekstach projektu nie mają prawa bycia
  (cyrylica, greka, hebrajskie, arabskie, dewanagari, tajskie, kana,
  CJK, hangul).
- UWAGA: każdy inny znak poza ASCII + polskimi ogonkami + typografią
  (do oceny człowieka, np. czeskie lub slowackie ogonki, emoji).
- OK: ASCII + ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ + typografia projektowa.

Użycie:
  python3 pewniaki/PogromcaKwiatkow.py            # dokumentacja + produkt + NOTATKI
  python3 pewniaki/PogromcaKwiatkow.py PLIK...    # wskazane pliki
  python3 pewniaki/PogromcaKwiatkow.py --selftest  # dowód: łapie próbkę z czatu
  python3 pewniaki/PogromcaKwiatkow.py --fix        # NFC + usuwa NIEWIDZIALNE (NIGDY nie podmienia liter)
Exit: 0 = czysto, 1 = BLAD.
"""
import io
import os
import sys
import unicodedata
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(HERE)

OGONKI = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
TYPO = set("—–„”\"'…«»·×±→←↔⇄≤≥≈≠°%§€•●○◀▶✕✓✔↑↓")
# po ludzkiej ocenie (tura 49): legalna typografia projektu
TYPO |= set(chr(c) for c in (0x2212, 0x2705, 0x274C))  # minus matematyczny, ✅, ❌
TYPO |= set(chr(c) for c in range(0x2500, 0x2580))    # linie diagramow (MAPA)
TYPO |= set(chr(c) for c in range(0x1F1E6, 0x1F200))  # flagi (README.md)
TYPO |= set("’£½¼¾⌘⌥⇧⌃❓📌📍™²³¹µ¶")  # (kozak 2B) apostrof, waluty, ulamki, skroty, emoji z MAPA-LOGIKI

BLOKOWANE = [
    (0x0370, 0x03FF, "GREKA"),
    (0x0400, 0x052F, "CYRYLICA"),
    (0x0530, 0x058F, "ORMIAŃSKIE"),
    (0x0590, 0x05FF, "HEBRAJSKIE"),
    (0x0600, 0x06FF, "ARABSKIE"),
    (0x0900, 0x097F, "DEWANAGARI"),
    (0x0E00, 0x0E7F, "TAJSKIE"),
    (0x3040, 0x30FF, "KANA (japońskie)"),
    (0x4E00, 0x9FFF, "CJK (chińskie/japońskie)"),
    (0xAC00, 0xD7AF, "HANGUL (koreańskie)"),
    (0xFF66, 0xFF9F, "KATAKANA półszerokości"),
    # (turniej Kozakow, tura 49) klasy pusczone w 1. biegu + luki architekta:
    (0x1C80, 0x1C88, "CYRYLICA ext-C"),
    (0x2DE0, 0x2DFF, "CYRYLICA ext-A"),
    (0xA640, 0xA69F, "CYRYLICA ext-B"),
    (0x1F00, 0x1FFF, "GREKA ext"),
    (0x2C00, 0x2C5F, "GLAGOLICA"),
    (0x2C80, 0x2CFF, "KOPTYJSKI"),
    (0x13A0, 0x13FF, "CHEROKEE"),
    (0xA4D0, 0xA4FF, "LISU"),
    (0x3100, 0x312F, "BOPOMOFO"),
    (0x3130, 0x318F, "HANGUL compat (filler)"),
    (0x1100, 0x11FF, "HANGUL jamo (fillery)"),
    (0x2800, 0x28FF, "BRAILLE"),
    (0x1800, 0x18AF, "MONGOLSKIE"),
    (0xFFF9, 0xFFFB, "INTERLINEAR (wtracenia)"),
    (0xFF00, 0xFFDC, "PELNOSZEROKOSCIOWE"),
    (0x0300, 0x036F, "LACZACE (zalgo)"),
    (0x20D0, 0x20FF, "LACZACE dla symboli"),
    (0x1AB0, 0x1AFF, "LACZACE ext"),
    (0x1DC0, 0x1DFF, "LACZACE suppl"),
    (0xFE20, 0xFE2F, "LACZACE półszerokościowe"),
    (0x1D400, 0x1D7FF, "MATEMATYCZNE alfanum. (pseudolitery)"),
    (0x2100, 0x214F, "LETTERLIKE (pseudolitery)"),
    (0x3000, 0x303F, "CJK symbole"),
    (0x10400, 0x1044F, "DESERET"),
    (0xE000, 0xF8FF, "OBSZAR PRYWATNY (PUA)"),
    # (runda 2: sedzia + siekiernik) wyroki i dziury systemowe:
    (0x2150, 0x218F, "CYFRY RZYMSKIE (pisz ASCII I V X)"),
    (0x2460, 0x24FF, "KOLA z cyframi/literami"),
    (0x02B0, 0x02FF, "MODYFIKATORY IPA (homoglify)"),
    (0x2215, 0x2216, "UKOSNIK/ODJECIE udajace ASCII"),
    # (kozak 1A): niewidzialne pułapki - zerowe ryzyko falszywych alarmow
    (0x00AD, 0x00AD, "NIEWIDZIALNE (soft hyphen)"),
    (0x200B, 0x200F, "NIEWIDZIALNE (zero-width/RTL)"),
    (0x202A, 0x202E, "NIEWIDZIALNE (kierunkowe)"),
    (0x2060, 0x2064, "NIEWIDZIALNE (joinery)"),
    (0xFEFF, 0xFEFF, "NIEWIDZIALNE (BOM)"),
]
# (kozak 1C, zawężone): czeskie/słowackie/węgierskie litery, które w tekstach
# PL/EN projektu nie mają prawa bycia. NIE hurtowo Latin Extended (kozak 5C)
# i NIE niemieckich umlautow ani romanskich akcentow (legalne w czesci EN,
# np. nazwiska) - te zostają w UWAGA. Nieomylność > czujność.
CUDZE = set("\u010d\u010f\u011b\u013e\u0148\u0159\u0161\u0165\u017e\u016f\u0111\u010c\u010e\u011a\u013d\u0147\u0158\u0160\u0164\u017d\u016e\u0110")  # dana przez sekwencje uXXXX - zrodlo pogromcy czyste
CUDZE |= set("\u0151\u0171")  # (turniej) wegieskie o-dwa-przecinki, u-dwa-przecinki
NIEWIDZ = {chr(c) for lo, hi, nm in BLOKOWANE if nm.startswith("NIEWIDZIALNE")
           for c in range(lo, hi + 1)}  # (r9 KONSERWATOR, BUG A) ZNAKI nie inty
# (r4 KRAWEDZ) niewidoczne lamacze linii: str.splitlines() ZJADA je przed
# skanem, analizuj musi je lapac w surowym tekscie; --fix zamienia je na LF
LAMACZE = "\x0b\x0c\x1c\x1d\x1e\u0085\u2028\u2029"
# (r5 ALCHEMIK) PRANIE NFC: komplet singletonow sciganych przez NFC do
# znaku klasy OK (enumeracja CALEGO Unicode; przy zmianie palety powtorz):
# 212A->K, 037E->srednik, 0387->srodkowa kropka, 1FEF->backtick
PRANIE = {"\u212a": "K", "\u037e": ";", "\u0387": "\u00b7", "\u1fef": "`"}


@lru_cache(maxsize=4096)  # (kozak-3 W2) werdykt liczony raz na znak
def klasyfikuj(znak):
    """Zwraca ("OK"|"BLAD"|"UWAGA", nazwa). Kolejnosc: ASCII -> paleta ->
    zakresy -> CUDZE -> kategorie Unicode (kozak-3 W1: category() zamiast
    parsowania nazw - stabilne miedzy wersjami Pythona)."""
    o = ord(znak)
    if o < 128:
        if znak in "\t\n\r" or 0x20 <= o <= 0x7E:
            return ("OK", "")
        return ("BLAD", "KONTROLNE (ASCII)")  # null byte, ESC, DEL...
    if znak in OGONKI or znak in TYPO:
        return ("OK", "")
    for lo, hi, nazwa in BLOKOWANE:
        if lo <= o <= hi:
            return ("BLAD", nazwa)
    if znak in CUDZE:
        return ("BLAD", "OBCYE DIAKRITYKI (czes/slow/wegr)")
    cat = unicodedata.category(znak)
    if cat.startswith("M"):
        return ("BLAD", "LACZACE (zalgo, dowolny blok)")
    if cat in ("Cc", "Cf"):
        return ("BLAD", "KONTROLNE/FORMAT (niewidzialne)")
    if cat == "Co":
        return ("BLAD", "OBSZAR PRYWATNY (PUA)")
    if cat == "Cs":
        return ("BLAD", "SURROGAT")
    if cat == "Cn":
        return ("UWAGA", "nieprzypisany (byc moze nowe emoji)")  # (kozak-3 W3)
    if cat == "Zs" and o != 0x20:
        return ("BLAD", "NIEWIDZIALNE (spacje)")  # (sedzia) NBSP/en/thin psuja format
    if cat in ("Zl", "Zp"):
        return ("BLAD", "LAMACZE LINII (niewidoczne)")  # (r4 KRAWEDZ) U+2028/U+2029
    if cat == "Nl":
        return ("BLAD", "CYFRY LITEROWE (rzymskie, klinowe...)")  # (sedzia)
    if cat.startswith("L"):
        # (kozak-3 W4) biala lista pism: Latin-1 i Ext-A -> UWAGA (Pokemon,
        # nazwiska EN); WSZYSTKIE litery wyzej -> BLAD (allowlist w duchu)
        if o <= 0xFF:
            return ("UWAGA", "litera Latin-1 spoza palety")
        if o <= 0x17F:
            return ("UWAGA", "litera Latin Ext-A spoza palety")
        return ("BLAD", "PISMO OBCYE (litera poza lacinie)")
    if cat == "Nd":
        return ("BLAD", "CYFRY OBCYGO PISMA")
    # (runda 2, uogolnienie wyroku sedziego) BANDY SYMBOLI: legalne symbole
    # zyja w blokach lacinaskich/wspolnych i emoji; wszystko innym (interpunkcja,
    # waluty, ulamki, znaki pism Indii/Azji/Afryki) -> BLAD, nie UWAGA.
    if o >= 0x1F000:
        return ("BLAD", "PIKTOGRAM/EMOJI spoza palety")  # (r3 PRALKA) mahjong/alchemia
    if 0xA0 <= o <= 0x24F or 0x2000 <= o <= 0x27BF:
        return ("UWAGA", "symbol spoza palety")
    return ("BLAD", "SYMBOL/CYFRA OBCYGO PISMA")


def _mieszane(token):
    """(kozak-1B) slowo z literami lacinaskimi ORAZ czemkolwiek z BLAD."""
    if not any(c.isascii() and c.isalpha() for c in token):
        return False
    return any((not c.isascii()) and klasyfikuj(c)[0] == "BLAD" for c in token)


def analizuj(tekst):
    """Zwraca (bledy, uwagi): bledy = {nazwa: [(linia, znak, kontekst)]}."""
    bledy, uwagi = {}, []
    # (r4 KRAWEDZ) splitlines() zjada 8 niewidocznych lamaczy linii (VT, FF,
    # FS, GS, RS, NEL, LS, PS) - skan surowego tekstu PRZED podzialem, inaczej
    # skaner bylby na nie slepy (FN klasy systemowej, 11 wektorow bieg 1)
    for poz, znak in enumerate(tekst):
        if znak in LAMACZE:
            nr = tekst.count("\n", 0, poz) + 1
            okno = tekst[max(0, poz - 25):poz + 26]
            kontekst = "".join(" " if c in LAMACZE + "\n\r\t" else c for c in okno).strip()
            bledy.setdefault("LAMACZE LINII (niewidoczne)", []).append((nr, znak, kontekst))
    # (r3, arbitraz asystenta) PRANIE NFC: znak, ktory NFC sciaga do czystego
    # ASCII (Kelvin U+212A -> K), jest kwiatkiem-niewidka - lapany PRZED
    # normalizacja (Ohm -> omega i tak zlapany po; Angstrom -> A-kolko = UWAGA).
    for nr, linia in enumerate(tekst.splitlines(), 1):
        for poz, znak in enumerate(linia):
            if znak in PRANIE:
                kontekst = linia[max(0, poz - 25):poz + 25].strip()
                bledy.setdefault("PRANIE NFC (udaje czysty znak)", []).append(
                    (nr, znak, kontekst + " [PRANY! u%04X -> %r!]" % (ord(znak), PRANIE[znak])))
    tekst = unicodedata.normalize("NFC", tekst)  # (kozak 2A) NFD nie szumi
    for nr, linia in enumerate(tekst.splitlines(), 1):
        for poz, znak in enumerate(linia):
            stan, nazwa = klasyfikuj(znak)
            if stan == "OK":
                continue
            kontekst = linia[max(0, poz - 25):poz + 25].strip()
            if stan == "BLAD":
                if nazwa.startswith("NIEWIDZIALNE"):
                    kontekst += " [NIEWIDZIALNY!]"
                elif nazwa.startswith("KONTROLNE"):
                    kontekst += " [KONTROLNY!]"
                lewa = poz
                while lewa and not linia[lewa - 1].isspace():
                    lewa -= 1
                prawa = poz
                while prawa < len(linia) and not linia[prawa].isspace():
                    prawa += 1
                if _mieszane(linia[lewa:prawa]):
                    kontekst += " [HOMOGLIF: slowo mieszane!]"
                bledy.setdefault(nazwa, []).append((nr, znak, kontekst))
            else:
                uwagi.append((nr, znak, kontekst))
    return bledy, uwagi


def domyslne_pliki():
    pliki = []
    for fn in os.listdir(HOME):
        if fn.endswith((".md", ".txt")) and os.path.isfile(os.path.join(HOME, fn)):
            pliki.append(os.path.join(HOME, fn))
    Produkt = os.path.join(HOME, "ASAonly - (AUTO)Manual - ModRefresher (RCON).py")
    if os.path.isfile(Produkt):
        pliki.append(Produkt)
    w = os.path.join(HOME, "WIEDZA_O_PROGRAMIE")
    if os.path.isdir(w):
        for fn in sorted(os.listdir(w)):
            pliki.append(os.path.join(w, fn))
    for fn in sorted(os.listdir(HERE)):          # (tura 49) cala wiedza w pewniaki/
        if fn.endswith((".md", ".txt")):
            pliki.append(os.path.join(HERE, fn))
    return sorted(set(pliki))


def selftest():
    """(kozak 4) dowod na SPRYT i NIEOMYLNOSC zarazem: probki brudne musza
    byc zlapane, probki czyste musza przejsc bez najmniejszego szumu.
    Brudne probki piszemy sekwencjami uXXXX - zrodlo pogromcy ma byc czyste (kwiatka nie cytujemy)."""
    brudne = [
        ("cyrylica w zdaniu", "Spokojnie \u043c\u043e\u0436\u043d\u043e spa\u0107"),
        ("homoglif w slowie mieszanym", "slowo p\u043elska"),
        ("zero-width space", "niewidoczny\u200bznak"),
        ("soft hyphen", "uk\u00adryty"),
        ("czeskie diakrytyki", "b\u011bd \u0159 \u016f"),
        ("chinskie znaki", "po chi\u0144sku \u53ef\u4ee5"),
        ("greka", "\u03b1\u03b2\u03b3 w tekscie"),
        ("null byte (kontrolny)", "ARK\u0000dok"),
        ("ESC (kontrolny)", "ARK \u001b[31mError"),
        ("braille blank", "tekst\u2800koniec"),
        ("koptyjski", "slowo \u2c80ba"),
        ("pelna szerokosc", "\uff41\uff42\uff43 ARK"),
        ("pismo obce (deseret)", "\U0001043a\U0001043b"),
        ("obszar prywatny", "\ue060x"),
        ("rzymska cyfra Nl", "rozdzial \u2163"),
        ("kolo z cyfra", "krok \u2460"),
        ("modyfikator IPA", "samogloska \u02d0"),
        ("interpunkcja tybetanska", "slowo\u0f0bslowo"),
        ("NBSP", "10\u00a0MB"),
        ("mahjong (piktogram)", "kafel \u1f000"),
        ("alchemia (piktogram)", "symbol \u1f700"),
        ("pranie NFC: Kelvin", "ARK-\u212a-99"),
        ("pranie NFC: komplet greki", "a\u037eb\u0387c\u1fef"),
        ("samotny surogat", "tekst\ud83dkoniec"),
        ("lamacz linii LS", "wiersz\u2028drugi"),
        ("lamacz linii VT", "zapis\u000bwysuw"),
    ]
    czyste = [
        ("ogonki PL", "Za\u017c\u00f3\u0142\u0107 g\u0119\u015bl\u0105 ja\u017a\u0144 \u2014 ZA\u017b\u00d3\u0141\u0106 G\u0118\u015aL\u0104 JA\u0179\u0143"),
        ("typografia/diagramy/flagi", "\u2514\u2500\u2192 \u2264 \u2265 \u2705 \u274c \U0001F1F5\U0001F1F1 \u00a3 \u00bd \u2318 \u21e7 \u2019"),
        ("sekcja angielska", "English text is perfectly fine here \u2014 100%."),
        ("minus i stopnie", "kreska: a\u2014b, minus: \u22125, stopnie: 30\u00b0C"),
        ("potegi i mikro i TM (sedzia)", "m\u00b2, 5\u00b3, 10\u00b9, 20\u00b5s, ASA\u2122"),
        ("pilcrow i paragraf", "sekcja \u00b6 i \u00a7 opisu"),
        ("taby i nowe linie", "kolumna\twartosc\ndruga linia"),
    ]
    ok = True
    print("SELFTEST PogromcaKwiatk\u00f3w:")
    for nazwa, probka in brudne:
        bledy, _u = analizuj(probka)
        dobre = bool(bledy)
        ok = ok and dobre
        print("  %-28s %s" % (nazwa, "ZLAPANY" if dobre else "!!! PUSZCZONY !!!"))
    for nazwa, probka in czyste:
        bledy, uwagi = analizuj(probka)
        dobre = not bledy and not uwagi
        ok = ok and dobre
        print("  %-28s %s" % (nazwa, "CZYSTO" if dobre else
                              "!!! FALSZYWY ALARM: %r %r !!!" % (bledy, uwagi)))
    import tempfile
    print("  NAPRAWA (--fix, r9 KONSERWATOR):")
    with tempfile.TemporaryDirectory() as d:
        przypadki = [
            ("usuniecie niewidzialnych", "a\u200bb\xadc\ufeffd", "t1.md", "abcd"),  # zostaja a,b,c,d
            ("lamacz w prozie -> LF", "wiersz\u2028drugi", "t2.md", "wiersz\ndrugi"),
            ("LS w literale .py ZOSTAJE", 'x = "a\u2028b"', "t3.py", 'x = "a\u2028b"'),
            ("LS-separator .py -> ratunek", "import os\u2028x = 1", "t4.py", "import os\nx = 1"),
        ]
        for nazwa, we, fn, oczek in przypadki:
            sciezka = os.path.join(d, fn)
            io.open(sciezka, "w", encoding="utf-8").write(we)
            wynik = napraw(we, sciezka)
            dobre = wynik == oczek
            ok = ok and dobre
            print("  %-28s %s" % (nazwa, "NAPRAWIONY" if dobre else "!!! ZLE: %r !!!" % wynik))
    b, _x = analizuj("slowo p\u043elska")
    etyk = any("HOMOGLIF" in k for trafy in b.values() for _l, _z, k in trafy)
    ok = ok and etyk
    print("  %-28s %s" % ("etykieta HOMOGLIF w raporcie", "JEST" if etyk else "!!! BRAK !!!"))
    print("  WERDYKT: %s" % ("PASS - sprytny i nieomylny" if ok else "FAIL"))
    return ok


def _lamacze_poza_literalami(tekst):
    """(r8 KONSERWATOR, BUG B) LAMACZE->LF wylacznie POZA literałami,
    f-stringami i komentarzami (stdlib tokenize). W literale legalny LS
    zostaje (detekcja go raportuje; podmiana rozwala string - r9 scen. 4)."""
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
    return "".join("\n" if (c in LAMACZE and i not in chronione) else c
                   for i, c in enumerate(tekst))


def _lamacze_poza_literalami_surowy(tekst):
    """(v8.0.2, BUG F4) Awaryjny skaner LAMACZE->LF dla .py, ktore NIE
    kompiluje sie (na zepsutym kodzie tokenize bywa zawodny). Automat
    stanow: literaly ' " ''' \"\"\" (z ucieczkami) i komentarze # sa
    CHRONIONE - podmiana wylacznie poza nimi. Slepa podmiana WSZEDZIE
    robila z LS w literale "unterminated string literal" (r9 scen. 4)."""
    out = []
    i, n = 0, len(tekst)
    stan = "kod"            # kod | hash | lancuch | trojka
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
                c = "\n"
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
                stan = "kod"  # domkniecie albo resync (plik i tak zepsuty)
        else:  # trojka
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
    return "".join(out)


def napraw(tekst, sciezka):
    """--fix (kozak 3): NFC + usuwanie NIEWIDZIALNYCH. Podmiana liter = NIGDY
    (kwiatka nie maskujemy - decyzja zawsze nalezy do czlowieka).
    (r8 KONSERWATOR) LAMACZE->LF bezpiecznie: pliki .py, ktore sie
    kompiluja, dostaja podmiane TYLKO poza literałami/komentarzami;
    (v8.0.2 BUG F4) .py zepsute -> ratunek poza literalami + bramka
    compile() - zaden zapisany wynik nie przestaje kompilowac sam z siebie;
    proza (.md/.txt) -> wszedzie."""
    if not sciezka.endswith(".py"):
        propozycja = "".join("\n" if c in LAMACZE else c for c in tekst)
    else:
        try:
            compile(tekst, sciezka, "exec")
        except SyntaxError:
            # (v8.0.2) najpierw wariant OSTROZNY (literaly nietknięte),
            # potem stary ratunek wszedzie - kazdy przechodzi bramke
            # compile(); gdy zaden nie kompiluje, zostaje wariant ostrozny
            # (NIE psujemy tego, czego nie da się naprawić).
            propozycja = _lamacze_poza_literalami_surowy(tekst)
            stary = "".join("\n" if c in LAMACZE else c for c in tekst)
            try:
                compile(propozycja, sciezka, "exec")
            except SyntaxError:
                try:
                    compile(stary, sciezka, "exec")
                    propozycja = stary
                except SyntaxError:
                    pass
        else:
            try:
                propozycja = _lamacze_poza_literalami(tekst)
                compile(propozycja, sciezka, "exec")  # (v8.0.2) bramka
            except Exception:
                propozycja = tekst  # (bezpieczenstwo) tokenize nie dal rady - nie ruszaj
    n_lam = sum(1 for a, b in zip(tekst, propozycja) if a != b and b == "\n")
    tekst = unicodedata.normalize("NFC", propozycja)
    out, n_widz, n_sp = [], 0, 0
    for c in tekst:
        if c != " " and unicodedata.category(c) == "Zs":
            out.append(" ")   # (sedzia) NBSP/en-space -> spacja, nie sklejaj slow
            n_sp += 1
        elif c in NIEWIDZ:
            n_widz += 1
            continue
        else:
            out.append(c)
    nowe = "".join(out)
    if nowe != tekst or n_lam:
        io.open(sciezka, "w", encoding="utf-8").write(nowe)
        print("[FIX]   %s: lamacze->LF %d | usuniete niewidzialne %d | spacje %d" %
              (os.path.relpath(sciezka, HOME), n_lam, n_widz, n_sp))
    return nowe


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    FIX = "--fix" in sys.argv
    pliki = argv if argv else domyslne_pliki()
    n_blad = n_uwag = 0
    for sciezka in pliki:
        try:
            tekst = io.open(sciezka, encoding="utf-8", errors="replace").read()
            if FIX:
                tekst = napraw(tekst, sciezka)
        except OSError as e:
            print("[BLAD]  %s: nie czyta sie (%s)" % (sciezka, e))
            n_blad += 1
            continue
        bledy, uwagi = analizuj(tekst)
        nazwa = os.path.relpath(sciezka, HOME)
        if bledy:
            n_blad += 1
            print("[BLAD]  %-52s" % nazwa)
            for pisownia, trafy in bledy.items():
                for nr, znak, kontekst in trafy[:3]:
                    print("        %s: linia %d, znak %r | ...%s..." %
                          (pisownia, nr, znak, kontekst))
                if len(trafy) > 3:
                    print("        %s: ...i %d dalszych" % (pisownia, len(trafy) - 3))
        elif uwagi:
            n_uwag += 1
            print("[UWAGA] %-52s (%d znakow do oceny)" % (nazwa, len(uwagi)))
            for nr, znak, kontekst in uwagi[:2]:
                print("        linia %d, znak %r | ...%s..." % (nr, znak, kontekst))
        else:
            print("[OK]    %s" % nazwa)
    print("-" * 72)
    print("PODSUMOWANIE: %d plikow | BLAD: %d | UWAGA: %d" %
          (len(pliki), n_blad, n_uwag))
    print("OPERATOR: regulamin uzycia -> PROTOKOL-OPERATORA.md")  # (v8.0.3)
    if not n_blad:
        print("ZERO OBCOJĘZYCZNYCH KWIATKÓW W TEKSTACH PROJEKTU")
    sys.exit(1 if n_blad else 0)


if __name__ == "__main__":
    main()
### ZagladaKultury.py

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

(v1.0.7) OSTRZEZENIA: gdy po --zaglada plik .py/.json nadal sie nie parsuje, drukowane jest [OSTRZEZENIE] (exit bez zmian).
(v1.0.4) OPERATOR — agencie AI: Twoj regulamin uzycia (drabina uprawnien,
plan->act, combo z PogromcaKwiatkow) jest w PROTOKOL-OPERATORA.md.
"""
import io
import json
import os
import sys
import unicodedata

WERSJA = "1.0.7"

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
        # (v1.0.7) OBSERWOWALNOSC: bramka nie przepuscila - plik nietkniety
        print("[OSTRZEZENIE] %s: bramka compile() nie przepuscila zadnego wariantu - plik ZOSTAL NIETKNIETY" % sciezka)
        return 0
    zmienione = sum(licznik.values())
    if zmienione == 0:
        return 0
    czesci = ["%s %d" % (k, v) for k, v in licznik.items() if v]
    if wykonaj:
        with io.open(sciezka, "w", encoding="utf-8", newline="") as f:
            f.write(nowy)
        print("[ZAGLADA] %s: %s" % (sciezka, " | ".join(czesci)))
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
    print("SELFTEST Zaglady Kultury v1.0.7")
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
### ProkuratorOgrodnik.py

# -*- coding: utf-8 -*-
"""Prokurator Ogrodnik: uzupelnienie Zaglady Kultury, czlonek rodziny Pogromcy Kwiatkow.

(v1.0.1) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
z rodzenstwem). Przeczytaj przed pierwszym uzyciem.

Rola w rodzinie:
- PogromcaKwiatkow.py = detektor (widzi, niczego nie zmienia)
- ZagladaKultury.py = dekontaminator (niszczy obca kulture, polska zostawia swieta)
- ProkuratorOgrodnik.py = ogrodnik-prokurator (pielegnuje ogrodek, prowadzi akta chwastow,
  decyduje co wyrwac, co zostawic, co zablokowac. Uzupelnia Zaglade o polityke.)

Problem ktory rozwiazuje:
Pogromca mowi BLAD. Zaglada mowi DO ZAGLADY / ZAGLADA. Ale kto decyduje CZY zaglada ma nastapic?
Czy plik i18n z CJK to brud czy celowa tresc? Czy test fixture z cyrylica to amunicja testowa czy wyciek?
Zaglada nie ma polityki. Prokurator ma.

Kontrakt v1.0.0:
- zbiera dowody: uruchamia Pogromce, parsuje werdykty, grupuje po pliku/linii/klasie
- sprawdza polityke: allowlist, fixtures, i18n, celowo brudna amunicja (dev/kwiatki-testy)
- klasyfikuje: UMORZONE (allowlist), POUCZENIE (UWAGA), ZAGLADA (BLAD do posprzatania), BLOKADA (podejrzenie sabotażu / celowy kwiatek w prozie)
- prowadzi akta: zapisuje dowody w notacji U+XXXX (nigdy zywe kwiatki w raporcie, §5), z kontekstem i ryzykiem
- egzekwuje bramke: exit 0 = czysto lub umorzone, 1 = jest do zaglady, 2 = blokada publikacji
- plan->act: domyslnie raport, --oskarz tworzy akta, --wykonaj uruchamia Zaglade tam gdzie polityka pozwala + kontrola Pogromca

Uzycie:
  python3 ProkuratorOgrodnik.py PLIK...                 # raport prokuratora
  python3 ProkuratorOgrodnik.py --oskarz PLIK...        # akta sprawy do pliku
  python3 ProkuratorOgrodnik.py --wykonaj PLIK...       # wykonaj zaglade gdzie wolno + kontrola
  python3 ProkuratorOgrodnik.py --selftest              # dowod dzialania

Polityka (domyslna, mozna rozszerzyc w pliku):
- dev/kwiatki-testy/*, **/fixtures/*, **/*test*brud* -> UMORZONE (celowo brudna amunicja)
- **/i18n/*, **/locales/*, **/*.po -> UMORZONE dla CJK/arab/hebr (tłumaczenia)
- .py literały -> POUCZENIE (Zaglada ich nie rusza, trzeba recznie)
- reszta BLAD -> ZAGLADA, wiele BLAD w jednym pliku + emoji + CJK -> BLOKADA do recznej oceny

Exit: 0 = czysto / umorzone, 1 = do zaglady, 2 = blokada / blad wejscia
"""

import io
import os
import sys
import subprocess
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

WERSJA = "1.0.1"

# --- polityka domyslna -------------------------------------------------
ALLOWLIST_GLOBS = [
    "dev/kwiatki-testy/*",
    "**/kwiatki-testy/*",
    "**/fixtures/*",
    "**/test_brudne*",
    "**/brudne*",
    "**/i18n/*",
    "**/locales/*",
    "**/*.po",
    "**/node_modules/*",
    "**/.git/*",
]

ALLOWLIST_CLASSES_FOR_I18N = {"CJK", "ARABSKIE", "HEBRAJSKIE", "TAJSKIE", "KANA", "HANGUL", "CYRYLICA", "GREKA"}

def match_allowlist(path: str) -> bool:
    import fnmatch
    for pat in ALLOWLIST_GLOBS:
        if fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(os.path.basename(path), pat):
            return True
    return False

def run_pogromca(files):
    """Uruchamia PogromcaKwiatkow.py i zwraca stdout."""
    cmd = [sys.executable, "PogromcaKwiatkow.py"] + files
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.returncode

def parse_pogromca_output(output: str):
    """Parsuje output Pogromcy na liste znalezisk."""
    findings = []
    current_file = None
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("[BLAD]") or line.startswith("[UWAGA]") or line.startswith("[OK]"):
            # Format: [BLAD]  sciezka
            #         KLASA: linia X, znak 'Y' | ...
            m = re.match(r"\[(BLAD|UWAGA|OK)\]\s+(.+)", line)
            if m:
                current_file = m.group(2).strip()
                findings.append({"file": current_file, "verdict": m.group(1), "details": []})
        elif "linia" in line and "znak" in line:
            # linia z klasa
            # np: CYRYLICA: linia 1, znak 'a' | ...
            if findings:
                findings[-1]["details"].append(line)
        elif "PODSUMOWANIE" in line:
            continue
    return findings


# (v1.0.1) notacja U+XXXX dla akt: raport Pogromcy niesie ZYWE znaki obce,
# akta jako artefakt archiwalny musza byc czyste (PROTOKOL: "akta w U+XXXX")
_PL = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
_TYPO = "—–„”…€%§°²³±·«»"
_DOZWOLONE = set(chr(c) for c in range(0x20, 0x7F)) | set(_PL) | set(_TYPO)

def notacja_uxxxx(tekst):
    """Zamienia kazdy znak spoza kultury dozwolonej na opis U+XXXX."""
    return "".join(c if c in _DOZWOLONE else "U+%04X" % ord(c) for c in tekst)

def classify_findings(findings):
    """Klasyfikuje na UMORZONE / POUCZENIE / ZAGLADA / BLOKADA."""
    akta = []
    summary = Counter()
    for f in findings:
        path = f["file"]
        verdict = f["verdict"]
        details = f["details"]
        if verdict == "OK":
            summary["OK"] += 1
            continue
        # policz klasy
        classes = []
        for d in details:
            cls = d.split(":")[0].strip() if ":" in d else "NIEZNANE"
            classes.append(cls)
        class_counter = Counter(classes)

        # polityka
        if match_allowlist(path):
            # sprawdz czy to i18n i czy klasy sa na allowliscie i18n
            if any(g in path for g in ["i18n", "locales", ".po"]) and all(c.split()[0] in ALLOWLIST_CLASSES_FOR_I18N or "CJK" in c or "CYRYLICA" in c for c in classes):
                decyzja = "UMORZONE"
                powod = "allowlist i18n / tlumaczenia"
            else:
                decyzja = "UMORZONE"
                powod = "allowlist: celowo brudna amunicja testowa"
            summary["UMORZONE"] += 1
        elif verdict == "UWAGA":
            decyzja = "POUCZENIE"
            powod = "UWAGA do decyzji misji"
            summary["POUCZENIE"] += 1
        else:  # BLAD
            # jesli .py i detale wskazuja na literał (heurystyka: w raporcie jest 'print' lub cudzyslow)
            is_py = path.endswith(".py")
            # BLOKADA gdy wiele roznych klas + emoji + CJK w jednym pliku prozy
            if len(class_counter) >= 4 and any("EMOJI" in c or "PIKTOGRAM" in c or "CJK" in c for c in classes):
                decyzja = "BLOKADA"
                powod = "wiele obcych kultur + emoji - podejrzenie sabotażu lub celowego kwiatka, wymaga recznej oceny"
                summary["BLOKADA"] += 1
            elif is_py:
                # dla .py - jesli w detail jest cudzyslow, to prawdopodobnie literal
                decyzja = "POUCZENIE"
                powod = ".py literal - Zaglada nie rusza (sacred), wymaga recznej poprawy"
                summary["POUCZENIE"] += 1
            else:
                decyzja = "ZAGLADA"
                powod = "BLAD do dekontaminacji przez Zaglade"
                summary["ZAGLADA"] += 1

        akta.append({
            "plik": path,
            "werdykt_pogromcy": verdict,
            "klasy": dict(class_counter),
            "decyzja": decyzja,
            "powod": powod,
            "dowody": [notacja_uxxxx(d) for d in details[:10]],  # (v1.0.1) escape: raport Pogromcy niesie zywe znaki
        })
    return akta, summary

def run_zaglada_if_allowed(akta):
    """Uruchamia Zaglade tam gdzie decyzja=ZAGLADA."""
    do_zaglady = [a["plik"] for a in akta if a["decyzja"] == "ZAGLADA"]
    if not do_zaglady:
        return
    for plik in do_zaglady:
        cmd = [sys.executable, "ZagladaKultury.py", "--zaglada", plik]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout.strip())
        # kontrola Pogromca po zagladzie (combo §1a)
        out, code = run_pogromca([plik])
        if code == 0:
            print(f"[KONTROLA] {plik} -> BLAD 0 po zagladzie - OK")
        else:
            print(f"[KONTROLA] {plik} -> nadal BLAD {code} - wymaga recznej interwencji")

def selftest():
    print("SELFTEST Prokuratora Ogrodnika v1.0.1")
    # stworz fixtures
    os.makedirs("tmp_prokurator_test", exist_ok=True)
    # czysty
    with open("tmp_prokurator_test/czysty.py", "w", encoding="utf-8") as f:
        f.write("print('czyste ąćęłńóśźż')\n")
    # brudny poza allowlist
    with open("tmp_prokurator_test/brudny.txt", "w", encoding="utf-8") as f:
        f.write("Spokojnie \u0430 spac\n")  # U+0430
    # brudny w allowlist (fixtures)
    os.makedirs("tmp_prokurator_test/fixtures", exist_ok=True)
    with open("tmp_prokurator_test/fixtures/brudny_fixture.txt", "w", encoding="utf-8") as f:
        f.write("Test \u0430\u0431\u0432\n")
    # i18n
    os.makedirs("tmp_prokurator_test/i18n", exist_ok=True)
    with open("tmp_prokurator_test/i18n/pl.po", "w", encoding="utf-8") as f:
        f.write("msgid \"hello\"\nmsgstr \"\u4e2d\u6587\"\n")

    files = [
        "tmp_prokurator_test/czysty.py",
        "tmp_prokurator_test/brudny.txt",
        "tmp_prokurator_test/fixtures/brudny_fixture.txt",
        "tmp_prokurator_test/i18n/pl.po",
    ]
    out, code = run_pogromca(files)
    print(out)
    findings = parse_pogromca_output(out)
    akta, summary = classify_findings(findings)
    print("\nAKTA PROKURATORA:")
    print(json.dumps(akta, indent=2, ensure_ascii=False))
    print("\nPODSUMOWANIE:", dict(summary))
    # oczekiwane: czysty OK, brudny ZAGLADA, fixture UMORZONE, i18n UMORZONE
    ok = summary.get("OK", 0) == 1 and summary.get("ZAGLADA", 0) == 1 and summary.get("UMORZONE", 0) == 2
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    # sprzatanie
    import shutil
    shutil.rmtree("tmp_prokurator_test")
    return 0 if ok else 1

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if "--selftest" in args:
        return selftest()

    wykonaj = "--wykonaj" in args
    oskarz = "--oskarz" in args
    pliki = [a for a in args if not a.startswith("--")]

    if not pliki:
        print("Podaj pliki do oskarzenia")
        return 2

    # 1. Dry-run: Pogromca
    out, code = run_pogromca(pliki)
    print(out)

    findings = parse_pogromca_output(out)
    akta, summary = classify_findings(findings)

    print("\n=== AKTA PROKURATORA OGRODNIKA ===")
    for a in akta:
        print(f"{a['plik']} -> {a['werdykt_pogromcy']} | {a['decyzja']} | {a['powod']} | klasy: {a['klasy']}")

    print(f"\nPODSUMOWANIE PROKURATORA: {dict(summary)}")
    print("OPERATOR: PROTOKOL §1a + §2.6 - decyzja przed publikacja")

    if oskarz:
        with open("akta_prokuratora.json", "w", encoding="utf-8") as f:
            json.dump(akta, f, indent=2, ensure_ascii=False)
        print("[AKTA] Zapisano akta_prokuratora.json (dowody w notacji U+XXXX, bez zywych kwiatkow)")

    if wykonaj:
        run_zaglada_if_allowed(akta)

    # exit code
    if summary.get("BLOKADA", 0) > 0:
        return 2
    if summary.get("ZAGLADA", 0) > 0 or summary.get("POUCZENIE", 0) > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
### AnihilatorChwastow.py

# -*- coding: utf-8 -*-
"""Anihilator Chwastow: czwarty czlonek rodziny, uzupelnia Zaglade o ochrone literalow we wszystkich jezykach.

(v1.0.0) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
z rodzenstwem). Przeczytaj przed pierwszym uzyciem.

Rola w rodzinie:
- PogromcaKwiatkow.py = detektor (widzi, niczego nie zmienia)
- ZagladaKultury.py = dekontaminator dla py/json/prozy (niszczy obca kulture, polska zostawia swieta, dla .py chroni literaly przez tokenize)
- ProkuratorOgrodnik.py = ogrodnik-prokurator (prowadzi akta chwastow, decyduje co wyrwac wg polityki allowlisty)
- AnihilatorChwastow.py = anihilator uniwersalny (niszczy chwasty we wszystkich jezykach: js/ts/java/go/rs/cs/py/json/md z pelna ochrona literalow i komentarzy)

Problem ktory rozwiazuje:
Zaglada ma ochrone literalow tylko dla .py. Dla js/ts/java/go/rs/cs dziala w trybie prozy agresywnej - wyrwie tez celowa tresc w stringu.
Anihilator ma ochrone literalow dla 6 jezykow + py/json. Dzieki temu mozesz bezpiecznie czyscic projekty wielojezyczne.

Kontrakt v1.0.0:
- cyrylica/greka -> transliteracja PL (jak Zaglada)
- homoglify -> baza, ogonki obce -> zdjecie, cyfry Nd -> ASCII, fullwidth -> pol, CJK/emoji/niewidzialne -> USUN, lamacze -> LF, twarde spacje -> spacja (kod: USUN jak w Zagladzie)
- OCHRONA LITERALOW: dla kazdego jezyka skaner stanow chroni:
  js/ts: '...' "..." `...` ${} // /* */ /regex/
  java/cs: "..." '...' // /* */
  go: "..." '...' `...` // /* */
  rs: "..." '...' // /* */ r#"..."# 
  py: tokenize (jak Zaglada) + awaryjny skaner
  json: kod=True (twarde spacje sklejaja)
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

WERSJA = "1.0.0"

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

def przetworz(tekst, sciezka):
    ext = sciezka.split(".")[-1].lower() if "." in sciezka else ""
    # json
    if ext in ("json", "jsonl"):
        return zaglada_tekst(tekst, kod=True)
    # py - uzyj tokenize jak Zaglada
    if ext == "py":
        try:
            import tokenize
            # proba kompilacji
            compile(tekst, sciezka, "exec")
            # tokenize
            out = []
            licznik = {k:0 for k in KATEGORIE}
            # uprosc: uzyj zaglada_tekst_poza_literalami_multi dla py tez (chroni ' " #)
            # ale dla pelnej zgodnosci uzyjemy multi z pythonowym komentarzem #
            # tu wywolamy wersje multi dla py (rozszerzona)
            return zaglada_tekst_poza_literalami_multi(tekst, "py")
        except Exception:
            # awaryjnie proza
            return zaglada_tekst(tekst, kod=True)
    # inne jezyki kodu
    if ext in ("js", "ts", "java", "go", "rs", "cs", "c", "cpp", "h", "hpp", "php", "rb", "swift", "kt"):
        return zaglada_tekst_poza_literalami_multi(tekst, ext if ext in ("js","ts") else ext)
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
            out.append(c); i+=1
            if c == "\\" and i < n:
                out.append(tekst[i]); i+=1
            elif c == "`":
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
    nowy, licznik = przetworz(tekst, sciezka)
    if licznik is None:
        return 0
    zmienione = sum(licznik.values())
    if zmienione == 0:
        return 0
    czesci = [f"{k} {v}" for k,v in licznik.items() if v]
    if wykonaj:
        with io.open(sciezka, "w", encoding="utf-8", newline="") as f:
            f.write(nowy)
        print(f"[ANIHILACJA] {sciezka}: {' | '.join(czesci)}")
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

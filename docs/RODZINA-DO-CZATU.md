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

KROK 0 - DOWOD WLASNORECZNY (przed czymkolwiek innym):
- Znajdz w tym pliku sekcje "### SZYBKI-START-DLA-AGENTA.md" i wykonaj z niej krok 1 (jedna linijka w interpreterze Pythona) - sam sobie udowodnij zjawisko, zanim uwierzysz na slowo reszcie tej wiadomosci

KROK 1 - ANALIZA REPO I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md z tego pliku lub z github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI
- Pobierz lub wytnij kody 4 narzedzi:
  PogromcaKwiatkow.py v8.6.0
  ZagladaKultury.py v1.4.0
  ProkuratorOgrodnik.py v1.3.1
  AnihilatorChwastow.py v1.4.0
- Zapoznaj sie z ich rola:
  Pogromca = detektor BLAD/UWAGA/OK - widzi niewidzialny brud
  Zaglada = dekontaminator py/json/proza - sprzata brud tam gdzie ma pewnosc
  ProkuratorOgrodnik = polityka UMORZONE/POUCZENIE/ZAGLADA/BLOKADA + akta w U+XXXX - decyduje co wolno czyscic
  AnihilatorChwastow = anihilator uniwersalny js/ts/java/go/rs/cs/c/cpp/h/hpp/php/rb/swift/kt/py (ochrona literalow i komentarzy) oraz json/jsonl i md/proza - sprzata w innych jezykach
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
SZYBKI-START-DLA-AGENTA.md   KROK 0 - dowod wlasnoreczny w 30 sekund
PogromcaKwiatkow.py          detektor
ZagladaKultury.py            dekontaminator py/json/proza
ProkuratorOgrodnik.py        polityka + akta
AnihilatorChwastow.py        anihilator uniwersalny z ochrona literalow
PROTOKOL-OPERATORA.md        regulamin dla agenta - FLOW USWIADOMIENIE
README.md                    opis
LICENSE                      MIT
```

Reszta w podkatalogach:
```
docs/                        RODZINA-DO-CZATU (ten plik - all-in-one), INSTRUKCJA-DLA-ZIELONYCH, KOMPLECIK (manifest drzewa), certyfikaty, medale, raporty, logi, wniosek
dev/                         turnieje, fuzz, tor, kwiatki-testy (celowo brudne amunicja)
```

## PROTOKOL OPERATORA - skrot

Drabina:
- poziom 1 detekcja - zawsze bez pytania
- poziom 2 --fix - rutynowo kopia -> fix -> rescan
- poziom 3 dekontaminacja - tylko gdy misja kaze, plan->act + decyzja Prokuratora

Combo:
- Pogromca -> Prokurator: raport
- Prokurator -> Zaglada/Anihilator: decyzja UMORZONE/POUCZENIE/ZAGLADA/BLOKADA
- Zaglada/Anihilator -> Pogromca: OBOWIAZKOWO BLAD 0

Bramka przedpublikacyjna: przed KAZDYM wystawieniem na zewnatrz przepusc pliki przez Pogromce. Exit !=0 = NIE publikuj.

ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!!

Nigdy nie wklejaj ZYWYCH kwiatkow do czatu - notacja U+XXXX.

TRYB STALY: kazda wiadomosc z tekstem z zewnatrz - skan PRZED wyslaniem.

## KOD NARZEDZI - 5 blokow ponizej (SZYBKI-START + 4 narzedzia)
### SZYBKI-START-DLA-AGENTA.md

# SZYBKI START DLA AGENTA — zanim przeczytasz cokolwiek innego

Agencie: to jest KROK 0 z FLOW UŚWIADOMIENIA (patrz PROTOKOL-OPERATORA.md).
Nie czytaj jeszcze README ani PROTOKOLU. Najpierw sam sobie to udowodnij —
zajmie ci to 30 sekund, nie 30 minut.

## 1. Wklej to do interpretera Pythona (masz go — sam sprawdź)

```python
a = "zaloz konto"
b = "zaloz konto".replace("a", "\u0430", 1)  # jedno "a" -> cyrylickie U+0430
print(a, "|", b)          # wygladaja IDENTYCZNIE
print(len(a) == len(b))   # True - nawet dlugosc sie zgadza
print(a == b)             # False
```

Zobacz sam: dwa napisy, które wyglądają identycznie, mają identyczną
długość — a mimo to `a == b` zwraca `False`. Jedna litera w `b` to nie
łacińskie „a", tylko cyrylickie U+0430. Gołym okiem nie do odróżnienia.
To właśnie jest „kwiatek".

## 2. Dlaczego to się dzieje (3 zdania)

Generujesz tekst token po tokenie. Cyrylica i łacinka mają litery, które
wyglądają identycznie (a, e, o, p, c i inne), więc token o wspólnym
kształcie potrafi wskoczyć w zły alfabet — bez ostrzeżenia, bez błędu,
i ty sam tego nie zauważysz ani w momencie generowania, ani przy
własnym przeglądzie tego, co napisałeś. To nie jest rzadkie: to
systematyczna właściwość tego, jak działasz.

## 3. Sprawdź, że narzędzie to łapie

```
python3 PogromcaKwiatkow.py --selftest
```

Zobaczysz PASS na próbce zawierającej dokładnie ten typ podmiany, jaką
sam sobie przed chwilą zrobiłeś w kroku 1.

## 4. Dopiero teraz — jeśli chcesz wiedzieć więcej

- Co robi cała rodzina 4 narzędzi i jak ich używać: plik README.md repozytorium
- Twój regulamin operatora (drabina uprawnień, plan->act): plik PROTOKOL-OPERATORA.md repozytorium

Jeśli krok 1 zadziałał i krok 3 dał PASS — rozumiesz już sedno. Reszta
dokumentacji to szczegóły wykonania, nie coś, w co musisz wierzyć na słowo.

### PogromcaKwiatkow.py
# -*- coding: utf-8 -*-
"""PogromcaKwiatków: wykrywacz obcojęzycznych "kwiatków" w polskich tekstach projektu.

(v8.0.3) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
z rodzina: ZagladaKultury, ProkuratorOgrodnik, AnihilatorChwastow).
Przeczytaj przed pierwszym uzyciem.

(v8.2.0, 2026-09-04) OCHRONA LITERALOW w --fix + backup i zapis atomowy.
(v8.1.0, 2026-09-04) RYZYKO-KLUCZA: nowa, dodatkowa warstwa raportu.
Znalezisko z turnieju absurdalnego (Zagłada czyszcząca zaatakowaną kopię
własnego kodu): literal string zawierający obcy znak, którego "oczyszczona"
wersja pasuje do innego identyfikatora/literalu już w pliku (np. literal
"niewidzialne" z jednym znakiem podmienionym na cyrylicki odpowiednik,
obok użycia jako klucz slownika licznik["niewidzialne"]) —
plik kompiluje się czysto, wybucha AttributeError/KeyError dopiero w
runtime. Zagłada SŁUSZNIE nie rusza treści literałów (kontrakt: święte),
więc to jest ryzyko, którego żadne narzędzie w rodzinie nie naprawi — ale
Pogromca może je teraz WYKRYĆ i zgłosić, zamiast pozwolić przejść cicho.
Nic nie modyfikuje, tylko ostrzega. Patrz analizuj_literaly_jako_klucze().

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
  python3 PogromcaKwiatkow.py            # dokumentacja + produkt + NOTATKI
  python3 PogromcaKwiatkow.py PLIK...    # wskazane pliki
  python3 PogromcaKwiatkow.py --selftest  # dowód: łapie próbkę z czatu
  python3 PogromcaKwiatkow.py --fix        # NFC + usuwa NIEWIDZIALNE (NIGDY nie podmienia liter)
Exit: 0 = czysto, 1 = BLAD.
"""
import io
import os
import sys
import tokenize
import unicodedata
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
WERSJA = "8.6.0"

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


def _oczysc_kandydatow(wartosc):
    """Zwraca zbior mozliwych 'oczyszczonych' wersji stringu (bez wiedzy o
    tabelach transliteracji Zaglady - Pogromca ma zostac bez zaleznosci od
    siostry). Dwie strategie: usun podejrzane znaki / zlozenie NFKD+ascii."""
    kandydaci = set()
    oczyszczony_usun = "".join(
        c for c in wartosc if klasyfikuj(c)[0] == "OK" or c in " \t"
    )
    if oczyszczony_usun != wartosc:
        kandydaci.add(oczyszczony_usun)
    zlozony = unicodedata.normalize("NFKD", wartosc)
    ascii_fold = zlozony.encode("ascii", "ignore").decode("ascii")
    if ascii_fold and ascii_fold != wartosc:
        kandydaci.add(ascii_fold)
    return kandydaci


def analizuj_literaly_jako_klucze(tekst, sciezka):
    """(v8.1.0, znalezisko 2026-09-03) Zwraca liste ostrzezen: literal
    string w kodzie .py zawiera podejrzany (obcy/homoglif) znak, a jego
    'oczyszczona' wersja pasuje do INNEGO identyfikatora lub literalu juz
    obecnego w tym samym pliku. To silny sygnal, ze literal pelni funkcje
    klucza/identyfikatora (dict key, __slots__, getattr) gdzie indziej w
    pliku - a Zagłada SLUSZNIE nie rusza tresci literalow (kontrakt: swiete),
    wiec taki plik moze skompilowac sie czysto i wybuchnac dopiero w runtime
    (AttributeError/KeyError). To TYLKO ostrzezenie - nic nie modyfikuje,
    nic nie usuwa z literalu. Dziala tylko gdy plik .py sie tokenizuje
    (jesli nie, po prostu nic nie zwraca - to jest dodatek, nie wymog)."""
    if not sciezka.endswith(".py"):
        return []
    try:
        tokeny = list(tokenize.generate_tokens(io.StringIO(tekst).readline))
    except (tokenize.TokenError, SyntaxError, IndentationError, UnicodeError):
        return []
    nazwy = set()
    literaly = []  # (wartosc, linia)
    for tok in tokeny:
        if tok.type == tokenize.NAME:
            nazwy.add(tok.string)
        elif tok.type == tokenize.STRING:
            surowy = tok.string
            for prefiks in ("rb", "br", "Rb", "bR", "rB", "BR", "r", "R", "b", "B", "f", "F", "u", "U"):
                if surowy.lower().startswith(prefiks.lower()) and len(surowy) > len(prefiks):
                    if surowy[len(prefiks):len(prefiks) + 1] in ("'", '"'):
                        surowy = surowy[len(prefiks):]
                        break
            for cudzyslow in ('"""', "'''", '"', "'"):
                if surowy.startswith(cudzyslow) and surowy.endswith(cudzyslow) and len(surowy) >= 2 * len(cudzyslow):
                    wartosc = surowy[len(cudzyslow):-len(cudzyslow)]
                    literaly.append((wartosc, tok.start[0]))
                    break
    wszystkie_literaly = set(w for w, _ in literaly)
    ostrzezenia = []
    for wartosc, linia in literaly:
        if not any(klasyfikuj(c)[0] == "BLAD" for c in wartosc):
            continue
        for kandydat in _oczysc_kandydatow(wartosc):
            if kandydat in nazwy or kandydat in (wszystkie_literaly - {wartosc}):
                ostrzezenia.append(
                    (linia, wartosc, kandydat,
                     "identyfikator" if kandydat in nazwy else "inny literal")
                )
                break
    return ostrzezenia


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


def _kod_we_fstringu(tresc, baza):
    """(v1.4.0) Zbior ABSOLUTNYCH indeksow, ktore wewnatrz tokenu f-stringa
    sa KODEM (wnetrze pol nawiasow klamrowych), a nie danymi.

    Powod: do v1.3.0 caly f-string byl chroniony jako literal. Ochrona
    danych dzialala, ale rozjezdzala kod: definicja zmiennej poza stringiem
    byla czyszczona, a jej UZYCIE wewnatrz f-stringa nie — plik, ktory
    dzialal, po czyszczeniu wybuchal NameError, mimo ze compile() przechodzi
    (skladnia pozostaje poprawna, wiec bramka tego nie widzi).

        PRZED:  vo = 7 ; print(f"wynik: {vo}")   -> dziala, pisze 7
        PO:     v  = 7 ; print(f"wynik: {vo}")   -> NameError

    Na Pythonie 3.12+ tokenize rozbija f-string na FSTRING_START/MIDDLE/END
    i problem znika sam; na 3.11 i starszych caly f-string to jeden token
    STRING, wiec pola trzeba znalezc samodzielnie.

    Zasada: kodem jest wnetrze pol; NIE sa kodem tekst dookola, podwojone
    nawiasy klamrowe, konwersje !r/!s/!a ani staly tekst format-spec po
    dwukropku. Zagniezdzone literaly wewnatrz wyrazenia pozostaja chronione
    jak dane, chyba ze same sa f-stringami — wtedy rekurencja."""
    i = 0
    while i < len(tresc) and tresc[i] not in "\"'":
        i += 1
    if "f" not in tresc[:i].lower():
        return set()
    dl = 3 if tresc[i:i + 3] in ('"""', "'''") else 1
    i += dl
    koniec = len(tresc) - dl
    kod = set()
    while i < koniec:
        c = tresc[i]
        if c == "\\" and dl == 1:
            i += 2
            continue
        if c in "{}" and tresc[i:i + 2] == c * 2:
            i += 2
            continue
        if c != "{":
            i += 1
            continue
        i += 1
        glebokosc, nawiasy, cudz = 1, 0, ""
        while i < koniec and glebokosc:
            d = tresc[i]
            if d in "\"'":
                p = i - 1
                while p >= 0 and tresc[p].isalpha():
                    p -= 1
                pref = tresc[p + 1:i].lower()
                dl2 = 3 if tresc[i:i + 3] in ('"""', "'''") else 1
                j = i + dl2
                while j < koniec:
                    if tresc[j] == "\\" and dl2 == 1:
                        j += 2
                        continue
                    if tresc[j:j + dl2] == d * dl2:
                        j += dl2
                        break
                    j += 1
                if "f" in pref:
                    kod |= _kod_we_fstringu(tresc[p + 1:j], baza + p + 1)
                i = j
                continue
            if d in "([":
                nawiasy += 1
            elif d in ")]":
                nawiasy -= 1
            elif d == "{":
                glebokosc += 1
            elif d == "}":
                glebokosc -= 1
                if not glebokosc:
                    i += 1
                    break
            elif (d == "!" and glebokosc == 1 and nawiasy == 0
                    and tresc[i + 1:i + 2] in ("r", "s", "a")
                    and tresc[i + 2:i + 3] in ("}", ":")):
                i += 2
                continue
            elif d == ":" and glebokosc == 1 and nawiasy == 0:
                i += 1
                while i < koniec and glebokosc:
                    e = tresc[i]
                    if e == "{":
                        glebokosc += 1
                        i += 1
                        while i < koniec and glebokosc > 1:
                            if tresc[i] == "}":
                                glebokosc -= 1
                            elif tresc[i] == "{":
                                glebokosc += 1
                            else:
                                kod.add(baza + i)
                            i += 1
                        continue
                    if e == "}":
                        glebokosc -= 1
                        i += 1
                        break
                    i += 1
                break
            kod.add(baza + i)
            i += 1
    return kod


def _regiony_literalow(tekst):
    """(v8.2.0) Zbior indeksow znakow lezacych WEWNATRZ literalow .py.

    Zwraca None, gdy tokenize nie da rady - wtedy wolajacy ma NIE czyscic
    (fail-closed), bo nie wie, gdzie konczy sie kod, a zaczyna dane.
    Chronimy WNETRZE literalu, nie cudzyslowy - prefiksy (r, b, f) i same
    ogranczniki zostaja poza ochrona, wiec nadal daja sie normalizowac."""
    import tokenize
    typy = {tokenize.STRING}
    for a in ("FSTRING_MIDDLE",):
        if hasattr(tokenize, a):
            typy.add(getattr(tokenize, a))
    starty, poz = [], 0
    for linia in tekst.split("\n"):
        starty.append(poz)
        poz += len(linia) + 1
    chronione = set()
    kod_fstring = set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(tekst).readline):
            if tok.type in typy:
                s = starty[tok.start[0] - 1] + tok.start[1]
                e = starty[tok.end[0] - 1] + tok.end[1]
                chronione.update(range(s, e))
                if tok.type == tokenize.STRING:
                    # (v8.6.0) wnetrze pol f-stringa to KOD, nie dane
                    kod_fstring |= _kod_we_fstringu(tok.string, s)
    except (tokenize.TokenError, SyntaxError, IndentationError,
            UnicodeError, IndexError, ValueError):
        return None
    return chronione - kod_fstring


def _wyczysc_fragment(frag):
    """NFC + twarde spacje -> spacja + usuniecie niewidzialnych. Zwraca
    (tekst, ile_niewidzialnych, ile_spacji)."""
    frag = unicodedata.normalize("NFC", frag)
    out, n_widz, n_sp = [], 0, 0
    for c in frag:
        if c != " " and unicodedata.category(c) == "Zs":
            out.append(" ")
            n_sp += 1
        elif c in NIEWIDZ:
            n_widz += 1
        else:
            out.append(c)
    return "".join(out), n_widz, n_sp


def _zapisz_bezpiecznie(sciezka, tresc):
    """(v8.2.0) BACKUP + ZAPIS ATOMOWY.

    Do v8.1.0 bylo io.open(sciezka, "w").write(...) - przerwanie w polowie
    zostawialo plik uzytkownika obciety, i nie bylo z czego wrocic.
    Teraz: kopia .bak-pogromca (odmowa zapisu, gdy kopia sie nie uda),
    zapis do pliku tymczasowego w TYM SAMYM katalogu, flush + fsync,
    os.replace() - podmiana jest atomowa albo nie ma jej wcale.
    Uprawnienia oryginalu sa przenoszone; dowiazanie symboliczne jest
    rozwiazywane, wiec podmieniamy plik docelowy, a nie sam link."""
    import shutil, tempfile
    rzeczywista = os.path.realpath(sciezka)
    if jest_kopia_zapasowa(rzeczywista):
        raise RuntimeError("ODMOWA ZAPISU: %s to kopia zapasowa (R3)" % rzeczywista)
    kopia = rzeczywista + ".bak-pogromca"
    # (R4) pierwsza kopia wygrywa - nie kasujemy sladu oryginalu
    if os.path.exists(kopia):
        i = 2
        while os.path.exists("%s.%d" % (kopia, i)):
            i += 1
        kopia = "%s.%d" % (kopia, i)
    try:
        shutil.copy2(rzeczywista, kopia)
    except Exception as e:
        raise RuntimeError("ODMOWA ZAPISU: nie udalo sie zrobic kopii %s (%s)"
                           % (kopia, e))
    katalog = os.path.dirname(rzeczywista) or "."
    fd, tmp = tempfile.mkstemp(dir=katalog, prefix=".pogromca-", suffix=".tmp")
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

    # (v8.2.0) OCHRONA LITERALOW W --fix.
    # Do v8.1.0 normalizacja NFC, zamiana twardych spacji i usuwanie
    # niewidzialnych znakow leciały po CALYM pliku, takze wewnatrz stringow.
    # Skutek: TOKEN = "abc<U+200B>def" po --fix mial inna wartosc i o jeden
    # znak mniej. Kontrakt "tresc literalu jest swieta" obowiazywal Zaglade,
    # ale nie --fix - i to wlasnie --fix protokol stawia na poziomie 2
    # ("rutynowo, bez pytania"). Teraz dla .py czyscimy wylacznie POZA
    # literalami; gdy tokenize nie da rady, nie czyscimy wcale (fail-closed).
    chronione = None
    if sciezka.endswith(".py"):
        chronione = _regiony_literalow(propozycja)
        if chronione is None:
            print("[POMINIETO] %s: tokenize nie dal rady - literaly nie do "
                  "odroznienia, wiec NFC/spacje/niewidzialne pominiete "
                  "(fail-closed)" % os.path.relpath(sciezka, HOME))
            nowe = propozycja
            if n_lam:
                _zapisz_bezpiecznie(sciezka, nowe)
                print("[FIX]   %s: lamacze->LF %d | usuniete niewidzialne 0 | spacje 0"
                      % (os.path.relpath(sciezka, HOME), n_lam))
            return nowe

    tekst = propozycja
    # Segmenty: na przemian [do czyszczenia] i [chronione]. Dzieki temu nie
    # trzeba mapowac pozycji po usunieciu znakow - kazdy kawalek jest
    # przetwarzany osobno i sklejany w kolejnosci.
    nowe, n_widz, n_sp = [], 0, 0
    bufor, w_ochronie = [], False
    for i, c in enumerate(tekst):
        teraz = chronione is not None and i in chronione
        if teraz != w_ochronie:
            frag = "".join(bufor)
            if w_ochronie:
                nowe.append(frag)                      # literal - bajt w bajt
            else:
                f, a, b = _wyczysc_fragment(frag)
                nowe.append(f); n_widz += a; n_sp += b
            bufor, w_ochronie = [], teraz
        bufor.append(c)
    frag = "".join(bufor)
    if w_ochronie:
        nowe.append(frag)
    else:
        f, a, b = _wyczysc_fragment(frag)
        nowe.append(f); n_widz += a; n_sp += b
    nowe = "".join(nowe)
    if nowe != tekst or n_lam:
        _zapisz_bezpiecznie(sciezka, nowe)
        print("[FIX]   %s: lamacze->LF %d | usuniete niewidzialne %d | spacje %d" %
              (os.path.relpath(sciezka, HOME), n_lam, n_widz, n_sp))
    return nowe


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    FIX = "--fix" in sys.argv
    if FIX and not argv:
        # (R7) --fix bez argumentow szedl na domyslne_pliki(), a te licza sie
        # wzgledem HOME = katalog NADRZEDNY wobec narzedzia. Potwierdzone:
        # przepisywalo pliki, ktorych uzytkownik nie wskazal.
        print("[BLOKADA] --fix wymaga jawnie podanych plikow "
              "(bez nich szedlby po katalogu nadrzednym wobec narzedzia)")
        sys.exit(2)   # main() konczy przez sys.exit, nie przez wartosc zwracana
    pliki = argv if argv else domyslne_pliki()
    n_blad = n_uwag = 0
    for sciezka in pliki:
        try:
            # (v8.3.0) Detekcja czyta tolerancyjnie (errors="replace"), zeby
            # zaraportowac cokolwiek nawet o pliku z uszkodzonym kodowaniem.
            # ALE --fix na takim pliku zapisywalby tekst PO podmianie bajtow
            # na U+FFFD - czyli trwale niszczyl oryginal. Sprawdzone: bajty
            # \xff\xfe w .md z jednoczesna twarda spacja gasly bezpowrotnie.
            # Teraz --fix wymaga poprawnego UTF-8 (fail-closed).
            surowe = io.open(sciezka, "rb").read()
            try:
                tekst = surowe.decode("utf-8")
                utf8_ok = True
            except UnicodeDecodeError:
                tekst = surowe.decode("utf-8", errors="replace")
                utf8_ok = False
            if FIX:
                if utf8_ok:
                    tekst = napraw(tekst, sciezka)
                else:
                    print("[POMINIETO] %s: plik nie jest poprawnym UTF-8 - "
                          "--fix zapisalby uszkodzone bajty jako U+FFFD "
                          "(fail-closed); napraw kodowanie recznie"
                          % os.path.relpath(sciezka, HOME))
        except OSError as e:
            print("[BLAD]  %s: nie czyta sie (%s)" % (sciezka, e))
            n_blad += 1
            continue
        bledy, uwagi = analizuj(tekst)
        ryzyko_kluczy = analizuj_literaly_jako_klucze(tekst, sciezka)
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
        if ryzyko_kluczy:
            for nr, wartosc, kandydat, typ in ryzyko_kluczy[:3]:
                print("        [RYZYKO-KLUCZA] linia %d: literal zawiera obcy znak, "
                      "oczyszczona wersja pasuje do %s '%s' juz w pliku — "
                      "Zaglada NIE dotknie tresci literalu (kontrakt: swiety), "
                      "sprawdz recznie przed uznaniem pliku za bezpieczny"
                      % (nr, typ, kandydat))
            if len(ryzyko_kluczy) > 3:
                print("        [RYZYKO-KLUCZA] ...i %d dalszych" % (len(ryzyko_kluczy) - 3))
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
def _kod_we_fstringu(tresc, baza):
    """(v1.4.0) Zbior ABSOLUTNYCH indeksow, ktore wewnatrz tokenu f-stringa
    sa KODEM (wnetrze pol nawiasow klamrowych), a nie danymi.

    Powod: do v1.3.0 caly f-string byl chroniony jako literal. Ochrona
    danych dzialala, ale rozjezdzala kod: definicja zmiennej poza stringiem
    byla czyszczona, a jej UZYCIE wewnatrz f-stringa nie — plik, ktory
    dzialal, po czyszczeniu wybuchal NameError, mimo ze compile() przechodzi
    (skladnia pozostaje poprawna, wiec bramka tego nie widzi).

        PRZED:  vo = 7 ; print(f"wynik: {vo}")   -> dziala, pisze 7
        PO:     v  = 7 ; print(f"wynik: {vo}")   -> NameError

    Na Pythonie 3.12+ tokenize rozbija f-string na FSTRING_START/MIDDLE/END
    i problem znika sam; na 3.11 i starszych caly f-string to jeden token
    STRING, wiec pola trzeba znalezc samodzielnie.

    Zasada: kodem jest wnetrze pol; NIE sa kodem tekst dookola, podwojone
    nawiasy klamrowe, konwersje !r/!s/!a ani staly tekst format-spec po
    dwukropku. Zagniezdzone literaly wewnatrz wyrazenia pozostaja chronione
    jak dane, chyba ze same sa f-stringami — wtedy rekurencja."""
    i = 0
    while i < len(tresc) and tresc[i] not in "\"'":
        i += 1
    if "f" not in tresc[:i].lower():
        return set()
    dl = 3 if tresc[i:i + 3] in ('"""', "'''") else 1
    i += dl
    koniec = len(tresc) - dl
    kod = set()
    while i < koniec:
        c = tresc[i]
        if c == "\\" and dl == 1:
            i += 2
            continue
        if c in "{}" and tresc[i:i + 2] == c * 2:
            i += 2
            continue
        if c != "{":
            i += 1
            continue
        i += 1
        glebokosc, nawiasy, cudz = 1, 0, ""
        while i < koniec and glebokosc:
            d = tresc[i]
            if d in "\"'":
                p = i - 1
                while p >= 0 and tresc[p].isalpha():
                    p -= 1
                pref = tresc[p + 1:i].lower()
                dl2 = 3 if tresc[i:i + 3] in ('"""', "'''") else 1
                j = i + dl2
                while j < koniec:
                    if tresc[j] == "\\" and dl2 == 1:
                        j += 2
                        continue
                    if tresc[j:j + dl2] == d * dl2:
                        j += dl2
                        break
                    j += 1
                if "f" in pref:
                    kod |= _kod_we_fstringu(tresc[p + 1:j], baza + p + 1)
                i = j
                continue
            if d in "([":
                nawiasy += 1
            elif d in ")]":
                nawiasy -= 1
            elif d == "{":
                glebokosc += 1
            elif d == "}":
                glebokosc -= 1
                if not glebokosc:
                    i += 1
                    break
            elif (d == "!" and glebokosc == 1 and nawiasy == 0
                    and tresc[i + 1:i + 2] in ("r", "s", "a")
                    and tresc[i + 2:i + 3] in ("}", ":")):
                i += 2
                continue
            elif d == ":" and glebokosc == 1 and nawiasy == 0:
                i += 1
                while i < koniec and glebokosc:
                    e = tresc[i]
                    if e == "{":
                        glebokosc += 1
                        i += 1
                        while i < koniec and glebokosc > 1:
                            if tresc[i] == "}":
                                glebokosc -= 1
                            elif tresc[i] == "{":
                                glebokosc += 1
                            else:
                                kod.add(baza + i)
                            i += 1
                        continue
                    if e == "}":
                        glebokosc -= 1
                        i += 1
                        break
                    i += 1
                break
            kod.add(baza + i)
            i += 1
    return kod


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
    kod_fstring = set()
    for tok in tokenize.generate_tokens(io.StringIO(tekst).readline):
        if tok.type in typy:
            s = starty[tok.start[0] - 1] + tok.start[1]
            e = starty[tok.end[0] - 1] + tok.end[1]
            chronione.update(range(s, e))
            if tok.type == tokenize.STRING:
                # (v1.4.0) wnetrze pol f-stringa to KOD, nie dane
                kod_fstring |= _kod_we_fstringu(tok.string, s)
    return chronione - kod_fstring


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


def _zmiany_znakowe(oryginal, kandydat):
    """(v1.4.0) Lista roznic (tag, i1, i2, j1, j2) miedzy oryginalem
    a kandydatem, w offsetach ABSOLUTNYCH — zamiennik dla
    SequenceMatcher liczonego na calym pliku.

    Powod: SequenceMatcher znak-po-znaku ma zlozonosc kwadratowa. Na pliku
    99 KB (argparse.py ze stdlib) czyszczenie trwalo 3 min 23 s przy rdzeniu
    liczacym 0.285 s — 1.67 mld operacji slownikowych. Wygladalo to jak
    zawieszenie, a pliki kilkusetkilobajtowe byly nie do przetworzenia.

    Czyszczenie zmienia znaki WEWNATRZ linii i nigdy nie zmienia ich liczby,
    wiec diff wystarczy liczyc linia po linii: koszt spada do sumy kwadratow
    dlugosci linii zamiast kwadratu calego pliku. Gdyby liczba linii jednak
    sie roznila (sytuacja nieprzewidziana, np. lamacz zamieniony na \\n),
    wracamy do wariantu globalnego — poprawnosc przed szybkoscia.

    Zmierzone na 25 plikach stdlib: identyczny zbior zmienionych pozycji
    25/25, czas 66.71 s -> 0.014 s (~4700x)."""
    lo = oryginal.splitlines(keepends=True)
    lk = kandydat.splitlines(keepends=True)
    if len(lo) != len(lk):
        sm = difflib.SequenceMatcher(None, oryginal, kandydat, autojunk=False)
        return [op for op in sm.get_opcodes() if op[0] != "equal"]
    zmiany = []
    off_o = off_k = 0
    for a, b in zip(lo, lk):
        if a != b:
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag != "equal":
                    zmiany.append((tag, i1 + off_o, i2 + off_o,
                                   j1 + off_k, j2 + off_k))
        off_o += len(a)
        off_k += len(b)
    return zmiany


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
    zmiany = _zmiany_znakowe(oryginal, kandydat)
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

WERSJA = "1.3.1"

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


# (v1.1.0) FAIL-CLOSED: rodzenstwo wolane po sciezkach ABSOLUTNYCH liczonych
# z __file__. Do v1.0.1 bylo "PogromcaKwiatkow.py" - sciezka wzgledna, wiec
# Prokurator uruchomiony z innego katalogu roboczego dostawal returncode 2 i
# puste stdout, nie sprawdzal tego, i meldowal "czysto" z kodem wyjscia 0 na
# plikach brudnych. To byl fail-open w narzedziu, ktore ma byc fail-closed.
TU = os.path.dirname(os.path.abspath(__file__))


class BladRodziny(Exception):
    """Awaria uruchomienia rodzenstwa. Zawsze konczy sie BLOKADA, nigdy 'czysto'."""


def sciezka_rodzenstwa(nazwa):
    """Absolutna sciezka do czlonka rodziny lezacego obok tego pliku."""
    p = os.path.join(TU, nazwa)
    if not os.path.isfile(p):
        raise BladRodziny("brak czlonka rodziny: %s (szukano w %s)" % (nazwa, TU))
    return p

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
    """Uruchamia PogromcaKwiatkow.py i zwraca (stdout, returncode).

    (v1.1.0) Kody wyjscia Pogromcy: 0 = czysto, 1 = jest BLAD. KAZDY inny kod
    oznacza, ze podproces nie wystartowal albo sie wysypal - wtedy rzucamy
    BladRodziny zamiast parsowac puste stdout jako 'brak znalezisk'."""
    cmd = [sys.executable, sciezka_rodzenstwa("PogromcaKwiatkow.py")] + files
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise BladRodziny(
            "Pogromca zakonczyl sie kodem %d (spodziewane 0 lub 1). stderr: %s"
            % (result.returncode, (result.stderr or "").strip()[:300]))
    if result.returncode == 1 and not result.stdout.strip():
        raise BladRodziny("Pogromca zglosil BLAD, ale nie wypisal nic na stdout")
    return result.stdout, result.returncode


def rozwin_argumenty(pliki):
    """(v1.1.0) Zamienia katalogi na liste plikow i odrzuca sciezki nieistniejace.

    Do v1.0.1 katalog szedl wprost do Pogromcy, wracal jako
    '[BLAD] <sciezka>: nie czyta sie (Is a directory)', a parser bral CALY
    ten komunikat bledu za nazwe pliku i dopisywal do akt zmyslone
    znalezisko z decyzja ZAGLADA."""
    wynik, brakujace = [], []
    for a in pliki:
        if os.path.isdir(a):
            for korzen, _katalogi, nazwy in os.walk(a):
                for n in sorted(nazwy):
                    pelna = os.path.join(korzen, n)
                    if jest_kopia_zapasowa(pelna):
                        continue          # (R3) nie tykamy kopii ratunkowych
                    wynik.append(pelna)
        elif os.path.isfile(a):
            wynik.append(a)
        else:
            brakujace.append(a)
    return wynik, brakujace

def rozwiaz_sciezke_z_raportu(kandydat):
    """(v1.1.0) Zamienia sciezke z raportu Pogromcy na istniejacy plik albo None.

    Pogromca wypisuje nazwy przez os.path.relpath(sciezka, HOME), gdzie HOME to
    katalog NADRZEDNY wobec katalogu rodziny - a nie katalog roboczy Prokuratora.
    Dlatego samo os.path.isfile() na tym, co wydrukowal, odrzuca poprawne pliki.
    Sprawdzamy wiec obie bazy, zanim uznamy linie za komunikat bledu."""
    if not kandydat:
        return None
    bazy = (os.path.dirname(TU), TU, os.getcwd())
    if os.path.isabs(kandydat):
        return kandydat if os.path.isfile(kandydat) else None
    for baza in bazy:
        p = os.path.normpath(os.path.join(baza, kandydat))
        if os.path.isfile(p):
            return p
    return None


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
                kandydat = m.group(2).strip()
                # (v1.1.0) Pogromca wypisuje bledy wejscia w tym samym formacie
                # co werdykty ("[BLAD] <sciezka>: nie czyta sie (...)"). Bez tego
                # sprawdzenia komunikat bledu ladowal w aktach jako nazwa pliku
                # z decyzja ZAGLADA - sfabrykowana sprawa.
                if rozwiaz_sciezke_z_raportu(kandydat) is None:
                    findings.append({"file": kandydat, "verdict": "BLAD_WEJSCIA",
                                     "details": [], "surowa_linia": line})
                    current_file = None
                    continue
                current_file = kandydat
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

def _py_skazenie_tylko_w_literalach(path):
    """(v1.3.0) Czy w tym pliku .py skazone znaki siedza WYLACZNIE wewnatrz
    literalow i komentarzy?

    Jesli tak — Zaglada faktycznie ich nie ruszy (chroni dane), wiec jedyne
    co ma sens to POUCZENIE dla czlowieka. Jesli nie — skazenie jest w KODZIE,
    Zaglada umie je naprawic i blokowanie jej byloby zostawieniem zepsutego
    pliku bez powodu.

    Przy jakiejkolwiek watpliwosci (plik nieczytelny, nie parsuje sie)
    zwracamy True — czyli ostrozniej, recznie. Fail-closed: nie wysylamy
    Zaglady tam, gdzie nie umiemy powiedziec, co sie stanie.

    (v1.3.1) Sciezka MUSI przejsc przez rozwiaz_sciezke_z_raportu().
    Pogromca drukuje nazwy jako relpath wzgledem katalogu NADRZEDNEGO
    wobec rodziny, a nie wzgledem cwd Prokuratora. Do v1.3.0 ta funkcja
    otwierala surowy string z raportu: gdy repo lezalo gdzie indziej niz
    plik uzytkownika, open() rzucal wyjatek, fail-closed zwracal True
    i --wykonaj NIGDY nie czyscil .py. Lokalnie sciezki sie zgadzaly,
    wiec blad byl niewidoczny - ujawnil sie dopiero na swiezym klonie."""
    rzeczywista = rozwiaz_sciezke_z_raportu(path)
    if rzeczywista is None:
        return True
    try:
        tekst = io.open(rzeczywista, encoding="utf-8").read()
    except Exception:
        return True
    try:
        import tokenize
        starty, poz = [], 0
        for linia in tekst.split("\n"):
            starty.append(poz)
            poz += len(linia) + 1
        chronione = set()
        for tok in tokenize.generate_tokens(io.StringIO(tekst).readline):
            if tok.type in (tokenize.STRING, tokenize.COMMENT):
                s = starty[tok.start[0] - 1] + tok.start[1]
                e = starty[tok.end[0] - 1] + tok.end[1]
                chronione.update(range(s, e))
    except Exception:
        return True
    for i, c in enumerate(tekst):
        if ord(c) > 127 and i not in chronione:
            return False          # skazenie w KODZIE -> Zaglada ma robote
    return True


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
        if verdict == "BLAD_WEJSCIA":
            # (v1.1.0) fail-closed: nie umiemy powiedziec nic o pliku, ktorego
            # Pogromca nie przeczytal. To NIE jest "czysto".
            akta.append({
                "plik": path,
                "werdykt_pogromcy": "BLAD_WEJSCIA",
                "klasy": {},
                "decyzja": "BLOKADA",
                "powod": "Pogromca nie przeczytal wejscia - brak podstaw do jakiejkolwiek decyzji",
                "dowody": [notacja_uxxxx(f.get("surowa_linia", ""))],
            })
            summary["BLOKADA"] += 1
            continue
        # (v1.3.0) FAIL-CLOSED na uszkodzone kodowanie. Pogromca czyta
        # tolerancyjnie (errors="replace"), wiec plik nie-UTF8 wraca jako
        # zwykly BLAD z podmienionym U+FFFD zamiast jako BLAD_WEJSCIA.
        # Do v1.2.0 Prokurator bral to za normalne skazenie i wydawal
        # decyzje na podstawie tresci, ktorej NIE PRZECZYTAL. Znak zastepczy
        # w dowodach oznacza, ze oryginalnych bajtow nikt nie zna.
        if any("U+FFFD" in d or "\ufffd" in d for d in details):
            akta.append({
                "plik": path,
                "werdykt_pogromcy": verdict,
                "klasy": {"USZKODZONE KODOWANIE": 1},
                "decyzja": "BLOKADA",
                "powod": "plik nie jest poprawnym UTF-8 (U+FFFD w odczycie) - "
                         "decyzja bez znajomosci oryginalnych bajtow byla by zgadywaniem",
                "dowody": [notacja_uxxxx(d) for d in details[:10]],
            })
            summary["BLOKADA"] += 1
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
            elif is_py and _py_skazenie_tylko_w_literalach(path):
                # (v1.3.0) POUCZENIE tylko wtedy, gdy skazenie NAPRAWDE siedzi
                # w literalach. Do v1.2.0 wystarczylo, ze plik ma rozszerzenie
                # .py — komentarz obiecywal heurystyke "czy w detalu jest
                # cudzyslow", ale jej nie bylo, wiec KAZDY skazony .py dostawal
                # POUCZENIE i --wykonaj nigdy nie czyscil Pythona. Zaglada
                # potrafi te pliki naprawic i sama chroni literaly.
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
        # (v1.3.1) Zagladzie podajemy sciezke ROZWIAZANA. W aktach siedzi
        # napis z raportu Pogromcy - relpath wzgledem katalogu nadrzednego
        # wobec rodziny, nie wzgledem cwd. Gdy repo i plik uzytkownika leza
        # w roznych drzewach, Zaglada dostawala nieistniejaca sciezke,
        # konczyla sie kodem 2 ([BLAD WEJSCIA]), a Prokurator raportowal
        # [BLOKADA]: decyzja ZAGLADA zapadala, ale plik NIGDY nie byl
        # czyszczony. Lokalnie sciezki przypadkiem sie zgadzaly, wiec wada
        # byla niewidoczna do czasu uruchomienia T6 na swiezym klonie.
        cel = rozwiaz_sciezke_z_raportu(plik) or plik
        cmd = [sys.executable, sciezka_rodzenstwa("ZagladaKultury.py"), "--zaglada", cel]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout.strip())
        # (v1.1.0) awaria Zaglady to nie jest cichy brak zmian
        if result.returncode != 0:
            print("[BLOKADA] %s -> Zaglada zakonczyla sie kodem %d: %s"
                  % (plik, result.returncode, (result.stderr or "").strip()[:200]))
            continue
        # kontrola Pogromca po zagladzie (combo §1a) - takze na sciezce
        # rozwiazanej, inaczej kontrola bada nieistniejacy plik
        out, code = run_pogromca([cel])
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

    # (v1.1.0) katalogi -> pliki, sciezki nieistniejace -> BLOKADA
    pliki, brakujace = rozwin_argumenty(pliki)
    if brakujace:
        for b in brakujace:
            print("[BLOKADA] nie istnieje: %s" % b)
        return 2
    if not pliki:
        print("[BLOKADA] po rozwinieciu argumentow nie zostal zaden plik")
        return 2

    # 1. Dry-run: Pogromca
    try:
        out, code = run_pogromca(pliki)
    except BladRodziny as e:
        # (v1.1.0) fail-closed: awaria rodzenstwa NIGDY nie moze wygladac
        # jak "czysto". Do v1.0.1 konczylo sie to kodem 0 i pustym podsumowaniem.
        print("[BLOKADA] awaria rodzenstwa: %s" % e)
        return 2
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


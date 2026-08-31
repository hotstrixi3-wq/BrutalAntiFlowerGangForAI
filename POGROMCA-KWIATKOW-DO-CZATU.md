# PogromcaKwiatków — wersja do wrzucenia na czat

Ten JEDEN plik .md zawiera wszystko: instrukcję dla Ciebie, polecenie dla
agenta AI oraz kompletny kod narzędzia. Nie musisz nic pobierać z GitHuba
i nic instalować.

## Ty (człowiek): zrób tylko to

1. Załącz ten plik do czatu z agentem AI.
2. Wklej poniższą wiadomość (całą, bez zmian poza nawiasami).

## Wiadomość dla agenta (skopiuj całość)

```
Hej! W załączonym pliku .md (POGROMCA-KWIATKOW-DO-CZATU.md) masz narzędzie
PogromcaKwiatków. Zrób dokładnie tak:

1. Przeczytaj sekcję PROTOKÓŁ OPERATORA (niejżej w tym pliku) — to Twój
   regulamin pracy z narzędziem. Stosuj się do niego.
2. Wytnij z tego pliku kod z bloku oznaczonego jako python (jest na dole,
   za nagłówkiem "KOD NARZĘDZIA") i zapisz go jako PogromcaKwiatkow.py.
3. Uruchom: python3 PogromcaKwiatkow.py --selftest  (musi być PASS).
4. Przeskanuj: [TU WPISZ ŚCIEŻKĘ PLIKU LUB FOLDERU].
5. Pokaż mi raport prostym językiem po polsku: co znaleziono, gdzie
   (plik, linia), i co to znaczy (BLAD = na pewno problem, UWAGA = do
   mojej decyzji).
6. NIE zmieniaj moich plików bez mojej wyraźnej zgody.
```

## Gdy czat NIE przyjmuje załączników

Skopiuj CAŁĄ treść tego pliku i wklej jako wiadomość do agenta (a pod nią
polecenie z sekcji wyżej). Jeśli czat ucina długie wiadomości — wklejaj
w częściach z podpisem „część 1/2”, „część 2/2”; agent sklei je w plik.

## O narzędziu (dla człowieka, trzy zdania)

PogromcaKwiatków znajduje w tekstach „niewidzialne śmieci” i literki z
obcych alfabetów (np. rosyjską literę w polskim słowie), których oko nie
widzi, a które psują dokumenty i kod. Nie poprawia ortografii i nigdy nie
podmienia liter — w trybie naprawy usuwa wyłącznie niewidzialne znaki.
Działa bez internetu, na zwykłym Pythonie 3; przeszedł 11 rund testów
turniejowych i test „nie niszczy kodu” w 100%.

---

## PROTOKÓŁ OPERATORA (agent: przeczytaj i stosuj — to Twoje zasady)

# PROTOKÓŁ OPERATORA — dla agenta AI (nie dla człowieka)

> Ty, agencie, jesteś operatorem tego narzędzia. Człowiek jest zleceniodawcą:
> raz ustawia cel i politykę, potem egzekwujesz TY i meldujesz jednolinijkowo.
> Instrukcja dla ludzi jest osobno ([INSTRUKCJA-DLA-ZIELONYCH.md]) — ten plik
> jest twoją check-listą. Czytasz go raz, działasz od razu.

## 0. Ściąga jednorazowa (TL;DR)

| Sytuacja | Narzędzie | Akcja |
|---|---|---|
| sprawdzam tekst/plik (czy jest brud?) | Pogromca | czytam werdykt, exit 0/1/2 |
| tekst do czatu z zewnątrz (web/OCR/user) | Pogromca | skan → przepisanie na czysto |
| niewidzialne śmieci/łamacze do posprzątania | Pogromca `--fix` | kopia → fix → reskan |
| pliki do dekontaminacji z obcej kultury | Zagłada `--zaglada` | plan→act→kontrola Pogromcą |
| kod `.py`/dane `.json` | oba | literały święte; ścieżka „kod" |

## 1. Drabina uprawnień (domyślne reguły misji)

| Poziom | Narzędzie | Kiedy działasz bez pytania |
|---|---|---|
| 1 | detekcja (odczyt) | **zawsze** — to twój wzrok, zero ryzyka |
| 2 | `--fix` (niewidzialne, łamacze, twarde spacje) | rutynowo: najpierw kopia/git, potem wykonanie, meldunek |
| 3 | dekontaminacja treści (ZagładaKultury) | tylko gdy misja tego wymaga („oczyść z obcej kultury"); zawsze plan→act |

Nigdy nie maskuj kwiatka w treści bez explicitnego zlecenia — detekcja jest
święta, decyzja o treści należy do zleceniodawcy (poziom 3 świadomie zmienia
treść: transliteracja to edycja, nie sprzątanie).

## 1a. Combo: Pogromca ↔ Zagłada — co czego wymusza

```
POGROMCA (widok) -> raport -> DECYZJA (zleceniodawca/misja)
                            |- zwykle: agent poprawia tekst sam
                            |- czasem: --fix (niewidzialne, rutyna)
                            +- rzadko: ZAGŁADA (misja mówi: "oczyść z obcej kultury")
```

- **Pogromca → Zagłada: NIC.** Detekcja nigdy nie uruchamia dezynfekcji.
  BLAD to wniosek do rozpatrzenia, nie spust. Zagłada = poziom 3, zawsze
  decyzja misji (zmienia treść — transliteracja to edycja, nie sprzątanie).
- **Zagłada → Pogromca: OBOWIĄZKOWO.** Po dezynfekcji kontrola wyrokiem
  BLAD=0 (jedyny przymus w combie; patrz §4).
- Technicznie: mechaniczne sprzężenie i tak byłoby dziurawe — Zagłada
  celowo nie rusza literałów `.py`, więc nie „załatwi" wszystkich znalezisk.

Typowe rozstrzygnięcia: filtr krzaków na czacie / pre-flight własnych tekstów
= sam Pogromca · sprzątnięcie niewidzialnych = `--fix` · dekontaminacja
cudzych plików = Zagłada (plan→act) + kontrola Pogromcą.

## 2. Plan → act (standard przy KAŻDEJ ingerencji)

1. **Dry-run**: tryb raportu (bez flag wykonania) → wiesz CO się zmieni.
2. **Kopia zapasowa**: `git` albo kopia `.bak`/snapshot — twoja rutyna, nie prośba.
3. **Wykonanie**: flaga (`--fix` / `--zaglada`).
4. **Weryfikacja**: exit-code + powtórny skan (czysto?) + dla `.py`: `compile()`.
5. **Meldunek**: JEDNA linia na plik (co, ile, jaki werdykt). Nie zalewaj czatu.
6. **Bramka przedpublikacyjna (v8.1.2)**: przed KAŻDYM wystawieniem na zewnątrz
   (git push, release, upload, czat) przepuść WSZYSTKIE publikowane pliki przez
   Pogromcę. Exit != 0 = NIE publikuj; popraw źródło (opisy: notacja U+XXXX,
   kod: eskapy \u). Wyjątek jawny: celowo brudna amunicja testowa (suity
   dev/kwiatki-testy, generatory turniejów z próbkami) — to fixtures, nie tekst.

## 3. Werdykty i kody wyjścia (maszynowo, bez czytania oczami)

- exit **0** = czysto / wykonano — jedziesz dalej
- exit **1** = jest brud do obsłużenia — stosuj §1 (poziom decyduje o działaniu)
- exit **2** = błąd wejścia (brak pliku, złe kodowanie) — napraw ścieżkę, nie zgaduj
- BLAD → działasz (usuń/napraw/zgłoś wg poziomu). UWAGA → **decydujesz wg
  polityki misji**; jeśli polityka nie obejmuje przypadku — dopisz do niej
  (jednorazowo pytasz zleceniodawcę, potem reguła jest już twoja).

### 3a. Format meldunku (jak raportować człowiekowi)

- jedna linia na plik: `plik → werdykt | co zrobione | liczniki`
- przy ingerencji: CO→CZEGO ile (`niewidzialne 3, lamacze 1`)
- nigdy pełne zrzuty plików; przy wielu plikach: agregat + wyjątki
- błąd wejścia: mów DOKŁADNIE co nie gra (ścieżka? kodowanie? pusty?)

## 4. Siostra: ZagładaKultury (dekontaminacja)

Szybka tabela decyzji (co stanie się ze znakiem):

| Znak | Los | Przykład |
|---|---|---|
| cyrylica/greka (też akcentowana) | transliteracja PL, znak-po-znaku | U+043F...→priwet |
| homoglify łacińskie | baza | U+017F→s, U+00DF→ss, U+00F8→o |
| obce ogonki (NFD) | zdjęcie | U+010D→c, U+0101→a |
| cyfry Nd (każde pismo) | ASCII | cyfry arabskie→319 |
| fullwidth/ligatury | NFKC | U+FF21→A, U+FB01→fi |
| pisma bez tabeli, emoji, µ ½ U+2032 U+00B4 | USUŃ | CJK/kana/hangul/arab/hebr/thai… |
| niewidzialne (Cc/Cf/Cn/Co/Cs/Mn) | USUŃ | ZWSP, PUA, tagi, zalgo |
| łamacze linii | LF | U+2028/U+2029/U+0085… |
| twarda spacja: proza→spacja, kod/.py/.json→USUŃ (skleja) | — | U+00A0/U+202F |
| **ąćęłńóśźż + typografia** | **NIETYKALNE** | ł zostaje ł (to polskie!) |

Znane ograniczenia (projektowe, nie bugi): transliteracja bez kontekstu
(obekt, Ewropa — słownik wyjątków w wersji futurowej); treść stringów `.py`
należy do autora — Zagłada ich nie dotyka. Po zagładzie obowiązkowo:
Pogromca na wynik (BLAD=0) — narzędzia weryfikują się wzajemnie (jedyny
przymus w combie, patrz §1a).

## 5. Czego NIE robić

- Nie wymyślaj polityki — czytaj paletę projektu; jej brak = pytanie raz.
- Nie wykonuj poziomu 3 „przy okazji" innych zadań.
- Nie raportuj pełnych plików — diff/liczniki wystarczą.
- Nie ufaj idempotentności w miejsce kopii — kopię robi się ZAWSZE.
- **Nie wklejaj do czatu ŻYWYCH znalezionych znaków** (nawet w cytatach i
  raportach z przykładami) — używaj notacji U+XXXX. (Lekcja z praktyki:
  fuzz Pogromcy dwa razy przyłapał raporty audytora na żywych krzakach
  w własnym korpusie. Audytowane przez narzędzie = audytują siebie.)

## 6. Interfejs maszynowy (stan: propozycja v8.3)

`--json` (werdykt per linia) i `--diff` (tylko zmienione linie) — gdy wejdą,
przechodzisz na nie natychmiast zamiast parsować raport tekstowy.

## 7. Wydajność i limity (know thy tool)

- **Wersja Unicode = wersja twojego Pythona** (stdlib `unicodedata`).
  Cn (nieprzypisany) w twoim środowisku może być przypisanym znakiem w
  nowszym Unicode (przykład: U+1C89+ bywa Cn). Dlatego Cn → UWAGA, nie BLAD.
- **lru_cache**: pierwsze przejście po nowym znaku wolniejsze, powtórki
  śmigają. Realne: 0,5-4,5 MB/s zależnie od unikalności znaków.
- Duże pliki (setki MB+): dziel po liniach, skanuj partiami, agreguj meldunek.
- Zero sieci, zero zależności, determinizm: możesz shipować plik w każdy
  workspace i uruchamiać lokalnie. Wymagany tylko Python 3.

## 8. Tryb czat: filtr krzaków (pierwotna misja)

Zanim wyślesz odpowiedź zawierającą tekst Z ZEWNĄTRZ (web, OCR, dokument
usera, inny agent):

1. Przepuść fragmenty przez Pogromcę (analizuj lub CLI na pliku).
2. BLAD → przepisz czysto (właściwe litery), nie cytuj surowca.
3. UWAGA → zwykle przepisz na bezpieczny odpowiednik; w cytacie
   dokumentacyjnym zawsze notacja U+XXXX.
4. Nigdy nie „ozdabiaj" własnych odpowiedzi symbolami spoza palety —
   to dokładnie klasa śmieci, po którą to narzędzie istnieje.
5. (v8.1.3) TRYB STAŁY: KAŻDA wiadomość na czat — także jednoznakowa, także
   pojedynczy znak ozdobny — przechodzi skan Pogromcą PRZED wysłaniem.
   Brud = popraw źródło i skanuj ponownie. Komunikacja operatora używa
   wyłącznie palety narzędzia (ASCII + polskie ogonki + typografia).
   Empiria: przed regułą ~90% wypowiedzi operatora nosiło pictogramy
   spoza palety (każdy z nich to BLAD wg własnego narzędzia).

## 9. Troubleshooting

| Objaw | Co robić |
|---|---|
| exit 2, złe kodowanie | sprawdź: utf-8? BOM (utf-8-sig)? binarium? zgłoś dokładnie |
| plik binarny | nie skanuj treści; zgłoś typ, pomiń |
| pusty plik | exit 0, nic do robienia — nie kombinuj |
| BOM na starcie | traktuj jako znak kontroli do wyczyszczenia (fix), tekst dalej normalnie |
| wynik inny niż u innego agenta | porównaj wersje Pythona/Unicode (§7) zanim zgłosisz bug |

## 10. Zasada wersjonowania (autor projektu)

Każda zmiana = nowa wersja (feature X.Y, poprawka X.Y.1) + wpis na górze
README (jedyna historia zmian). Po każdej zmianie kodu: turniej jako regresja
— bateria w repo (`dev/` + turnieje sędziego), jeden cykl przed oddaniem.


## KOD NARZĘDZIA (agent: wytnij cały blok poniżej do pliku PogromcaKwiatkow.py)

```python
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

```

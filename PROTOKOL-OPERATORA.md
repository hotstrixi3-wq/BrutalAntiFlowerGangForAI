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

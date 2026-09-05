# Stan sesji — czytaj to jako drugie, zaraz po README

Agencie: ten plik odpowiada na pytanie **„na czym stanął poprzedni agent"**.
Dziennik uczy zasad, ten plik mówi, gdzie jesteśmy. Bez niego zaczynasz od
zera, mimo że ktoś zrobił tu już kilkadziesiąt godzin roboty.

**Aktualizuj go na koniec swojej sesji.** To zajmuje trzy minuty i jest
jedyną rzeczą, która pozwala następnemu wejść w środek pracy zamiast
w pustkę.

---

## Gdzie jesteśmy

| | |
|---|---|
| wersja repo | **9.19.0** |
| gałąź robocza | `arena/01a06e18-brutalantiflowergangforai` |
| ostatni commit | `9b4d574` — v9.19.0 - porzadek w instrukcjach: jedna informacja, |
| stan testów | wszystko zielone (weryfikacja: PROTOKOL par. 4) |
| dziennik | 49 wpisów, 1 sesja |

**Wersje narzędzi:** zawsze z `WERSJE.json`, nie z pamięci. Ten plik
celowo ich nie powtarza — powtórzenie to kolejne miejsce do rozjechania.

---

## Co jest w toku (stan na koniec sesji)

**PR #2 otwarty, czeka na decyzję człowieka.**
https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI/pull/2

Scala gałąź roboczą do `main`. `main` jest wciąż w stanie sprzed sesji:
53 pliki w korzeniu, z czego **39 to duplikaty** (ten sam plik leży
w korzeniu i w `docs/`). Nie scalaj sam — to decyzja operatora-człowieka.

---

## Decyzje operatora, które obowiązują

Padły w rozmowie, nie wynikają z kodu. Trzymaj się ich:

1. **„Nie ruszamy działającego kodu, dokładamy kolejny."** Zasada domu.
   Naprawa błędu — tak. Kosmetyka w tym samym commicie co zmiana
   logiki — nie, bo utrudnia cofnięcie.
2. **Poprawka kodu = reset medalu/turnieju.** Zmieniasz kod rodziny →
   podbijasz wersję i przechodzisz pełną regresję od nowa.
3. **„Nieomylny" znaczy „nie wprowadzi cię w błąd"**, a nie „zawsze
   naprawi dobrze". To definicja, nie hasło.
4. **Gang to oczy, nie automat.** Decyzja i odpowiedzialność są twoje.
5. **Nie przepisywać od nowa.** Rozważane i odrzucone — wartością repo
   są dowody (turnieje, pomiary), nie kod. Nowy kod startuje z zerem.
6. **Testy muszą udowadniać niezawodność informowania**, nie tylko
   nieszkodliwość. Stąd T7, T8, T9 i pomiary mutacyjne.
7. **Dokumentacja dla agenta osobno od dokumentacji dla człowieka.**
   Stąd podział `docs/agent/`, `docs/czlowiek/`, `docs/dowody/`.

---

## Następne kroki — kolejka, z uzasadnieniem

Kolejność wynika z ryzyka, nie z łatwości.

**1. Dokończyć porządki w strefie agenta** *(w toku)*
Krok 1 zrobiony (struktura, README). Zostaje krok 2: przejść plik po
pliku przez `docs/agent/` i korzeń — sprawdzić, czy nie kłamią, skrócić,
usunąć powtórzenia.

**2. HTML/CSS w Anihilatorze** *(luka z pomiarem)*
Nikt nie traktuje ich jak kodu, więc chiński tekst na stronie **zniknie**.
Kierunek: czyścić nazwy klas, `id`, selektory; nie tykać tekstu między
znacznikami. Wymaga zmiany kodu rodziny → reset medalu.

**3. Rozjazd 24 znaków między Zagładą a Anihilatorem**
Ten sam znak w `.py` i `.js` daje inny wynik (`U+0407` → `Ji` vs
usunięcie). Docelowo: jedno źródło prawdy dla tablic + test równoważności
w bramce.

**4. Sprzątanie martwego kodu** *(kosmetyka, świadomie odłożona)*
Podwójna definicja `zaglada_tekst_poza_literalami_multi` w Anihilatorze
(linie 191 i 429 — działa tylko druga), `baza_bez_ogonkow`, brak `--help`
w Prokuratorze i Anihilatorze, selftesty drukujące stare numery wersji.

---

## Otwarte pytania — nie rozstrzygaj sam

- Czy `--zaglada` i `--anihilacja` mają **odmawiać** bez wcześniejszego
  zwiadu, czy to za daleko idąca kuratela?
- Rotacja backupów `.bak-1` … `.bak-5`: w narzędziach czy osobnym
  poleceniem?
- Zakres docelowy: czy Gang ma obsługiwać wszystkie języki, czy skupić
  się na tym, co agenci generują najczęściej?

---

## Znane wady, których NIE naprawiono

Świadomie, żeby nikt nie polegał na ciszy:

| Wada | Status |
|---|---|
| HTML/CSS traktowane jak proza — treść użytkownika znika | w kolejce, pkt 2 |
| 24 znaki rozjeżdżają się Zagłada ↔ Anihilator | w kolejce, pkt 3 |
| `U+0304` i inne znaki łączące ze złożoną formą NFC | wada zastana, fuzz 499/500 |
| martwy kod (dublet 111 linii, `baza_bez_ogonkow`) | kosmetyka, pkt 4 |

---

---

## Procedur tu nie ma

Ten plik mówi **gdzie jesteśmy**. Jak coś zrobić — `PROTOKOL-OPERATORA.md`:
kolejność pracy na pliku (§2), bramki przed commitem (§4), ochrona przed
zniszczeniem (§6), zamykanie sesji (§8).

Pułapki, na które ktoś już nadepnął — `python3 pamietnik.py`.
Lekcje o samym narzędziu — `docs/agent/LEKCJE.md`.

# Naprawa v8.6.0 — decyzje inzynierskie

Data: 2026-09-04 · Pogromca 8.6.0 · Zaglada 1.4.0 · Anihilator 1.4.0

Operator dostarczyl program i powierzyl decyzje o sposobie naprawy agentowi.
Ten dokument tlumaczy **co zostalo zmienione i dlaczego wlasnie tak** —
zeby dalo sie te decyzje sprawdzic i ewentualnie podwazyc.

Kolejnosc prac wynikala z ryzyka: najpierw to, co lamie obietnice narzedzia
(poprawnosc), potem to, co czyni je nieuzywalnym (wydajnosc), na koncu to,
co pozwolilo bledom przejsc niezauwazonymi (testy).

---

## 1. Luka krytyczna — wnetrze f-stringa bylo chronione jak dane

### Problem

Warstwa „nie ruszamy literalow" traktowala caly f-string jako dane. Ale
wnetrze pol `{...}` to **kod**. Skutek: definicja zmiennej byla czyszczona,
jej uzycie w f-stringu nie — plik, ktory **dzialal**, po czyszczeniu
wybuchal, a `compile()` niczego nie zglaszal, bo skladnia pozostawala
poprawna.

```
PRZED:  vо = 7 ; print(f"wynik: {vо}")   -> dziala, pisze "wynik: 7"
PO:     v  = 7 ; print(f"wynik: {vо}")   -> NameError
```

Dotyczylo Zaglady i Pogromcy (Python) oraz Anihilatora (JS `${...}`).

### Dlaczego tak, a nie inaczej

Rozwazane byly trzy drogi:

| Wariant | Ocena |
|---|---|
| Czyscic caly f-string razem z tekstem | **Odrzucone** — niszczy dane, czyli lamie warstwe ochrony, ktora jest sensem narzedzia. Polski tekst w `f"cena: {k} zl, łąka"` zostalby zepsuty. |
| Uzyc `ast` i `FormattedValue` | **Odrzucone** — `ast` wymaga pliku, ktory sie PARSUJE. Narzedzie musi dzialac takze na plikach juz zepsutych (jest do tego osobna sciezka „surowa"), wiec zaleznosc od poprawnej skladni jest tu zla. |
| Wlasny skaner pol wewnatrz tokenu STRING | **Wybrane** — dziala na tokenach, nie na drzewie; nie wymaga parsowalnosci calego pliku; nie ma zaleznosci zewnetrznych. |

Doszedl argument zgodnosci: na **Pythonie 3.12+** `tokenize` sam rozbija
f-string na `FSTRING_START/MIDDLE/END` i problem znika. Kod juz to
przewidywal, ale tutejszy interpreter to 3.11, gdzie caly f-string jest
jednym tokenem `STRING`. Nowa funkcja obsluguje wlasnie ten przypadek,
nie psujac zachowania na 3.12+.

### Rozwiazanie

`_kod_we_fstringu(tresc, baza)` — zwraca absolutne indeksy znakow bedacych
kodem. Zasady:

* kodem jest wnetrze pol `{...}`;
* **nie** sa kodem: tekst dookola, `{{` i `}}`, konwersje `!r/!s/!a`,
  staly tekst format-spec po `:`;
* zagniezdzone literaly w wyrazeniu pozostaja chronione jak dane —
  **chyba ze same sa f-stringami**, wtedy rekurencja.

Podpiecie to jedna linia: `return chronione - kod_fstring`.

### Weryfikacja

Kontrola krzyzowa z `ast`: dla kazdego f-stringa w **171 modulach stdlib**
sprawdzono, czy wszystkie nazwy widziane przez `ast.FormattedValue` sa
objete przez skaner.

| Miara | Wynik |
|---|---|
| plikow zbadanych | 171 |
| pol zastepczych (`FormattedValue`) | 536 |
| **plikow zgodnych z `ast`** | **171 / 171** |

Przypadek `dataclasses.py` (f-string zagniezdzony w f-stringu) wykryl brak
rekurencji w pierwszej wersji skanera — dopisana, kontrola przeszla w 100%.

W JS analogicznie: skaner `${...}` w stanie `string_backtick`, z obsluga
zagniezdzonych klamer i literalow.

---

## 2. Wydajnosc — kwadratowy diff (znalezisko Z1)

### Problem

`_napraw_niespojnosc_identyfikatorow` liczyl `SequenceMatcher` **znak po
znaku na calym pliku**. Zmierzone na `argparse.py` (99 612 znakow):

```
real  3m23s          <- czyszczenie jednego pliku
1 673 047 249 wywolan dict.get
rdzen czyszczacy:  0.285 s    (narzut ~700x)
```

| rozmiar | czas diffa |
|---|---|
| 5 000 | 0.27 s |
| 20 000 | 10.61 s |
| 80 000 | 116.86 s |

### Rozwiazanie i jego uzasadnienie

Czyszczenie zmienia znaki **wewnatrz linii** i nie zmienia ich liczby.
Diff mozna wiec liczyc per linia: koszt spada z kwadratu calego pliku do
sumy kwadratow dlugosci linii.

Ostroznosc: gdyby liczba linii jednak sie roznila (np. lamacz zamieniony
na `\n`), `_zmiany_znakowe` **wraca do wariantu globalnego**. Poprawnosc
ma pierwszenstwo przed szybkoscia — szybka sciezka obsluguje przypadek
typowy, wolna zostaje jako siatka bezpieczenstwa.

### Weryfikacja

| Miara | Wynik |
|---|---|
| pliki o identycznym zbiorze zmienionych pozycji | **25 / 25** |
| czas: diff globalny | 66.71 s |
| czas: diff per linia | 0.014 s |
| `argparse.py` przez CLI: przed | **3 m 23 s** |
| `argparse.py` przez CLI: po | **0.137 s** (~1480x) |

Wynik czyszczenia bez zmian — te same liczniki `cyr 2 | grk 1 | niewidzialne 1`.

---

## 3. Kryterium testow — z `compile()` na „uruchom i porownaj"

### Problem

Turnieje T3 i Z2 uznawaly plik za caly, jesli przechodzil `compile()`.
Tymczasem obie powazne klasy bledow, jakie narzedzie potrafi wprowadzic,
`compile()` **przechodza**:

* luka f-string -> `NameError`,
* niespojnosc identyfikatorow (znalezisko `_scandir_path`) -> `AttributeError`.

Do tego zadna z 8 probek turniejowych nie zawierala f-stringa ze zmienna
(zmierzone: 0), podczas gdy uzywa go **58/171 = 34%** modulow stdlib.
Testy pokazywaly „0 popsutych" omijajac konstrukcje z co trzeciego pliku.

### Rozwiazanie

`dev/turnieje/turniej-4-runtime.py` — **uruchamia** program przed i po
czyszczeniu i porownuje standardowe wyjscie. Dwie kategorie:

* **nieszkodliwosc** (14 probek): dzialalo przed -> musi dawac ten sam
  wynik po. Obejmuje wszystkie warianty f-stringa (format-spec,
  zagniezdzony, wielolinijkowy, indeks, konwersja, metoda, f-w-f,
  podwojne klamry) oraz probke kontrolna z polskim tekstem w danych.
* **sila naprawcza** (4 probki): nie dzialalo przed -> **musi** dzialac po
  (niespojnosc nazw, zero-width w nazwie, atrybut klasy, nazwa importu).

Rozdzielenie tych kategorii bylo konieczne: pierwsza wersja turnieju
wrzucala je razem i zglaszala pliki zepsute-przed jako „zle probki".

### Weryfikacja samego straznika

Test w obie strony — turniej musi **umiec oblac**:

| Wersja narzedzi | Wynik T4 | exit |
|---|---|---|
| stara (przed naprawa) | REGRESJA — 10 przypadkow | **1** |
| nowa (po naprawie) | WSZYSTKO ZDANE | **0** |

---

## 4. Regresja koncowa

| Test | Wynik |
|---|---|
| selftesty | 4/4 PASS |
| tor-pogromcy | 348 trafione, FN 0, FP 0, SZUM 0 |
| fuzz | 3 x 500 OK, 0 FAIL |
| T2 sprawdzajacy | 992 wektory, FN 0, FP 0, SZUM 0, CRASH 0 |
| T3 niepsucie | 190 plikow, 0 popsutych |
| Z1 wykrywanie | 1545 wektorow, FN 0, FP 0, CRASH 0 |
| Z2 niepsucie | 200 plikow, 0 popsutych |
| **T4 runtime (nowy)** | **WSZYSTKO ZDANE** |
| luka-fstring | **0 / 5 zepsutych** |
| bramka spojnosci | 0 rozjazdow |

Na 40 prawdziwych modulach stdlib: 0 niekompilujacych sie, 0 zmian w kodzie
wykonywalnym, **40/40 importuje sie z identycznym publicznym API**.

---

## 5. Co zostalo swiadomie NIE zrobione

* **Martwy dublet w Anihilatorze** (111 linii, `zaglada_tekst_poza_literalami_multi`
  zdefiniowana dwa razy) — usuniecie to zmiana czysto kosmetyczna w pliku,
  ktory wlasnie zostal zmieniony merytorycznie. Rozdzielenie tych dwoch
  rzeczy ulatwia ewentualne cofniecie naprawy. Do zrobienia osobno.
* **`baza_bez_ogonkow`** (martwa, 0 wywolan) — jw.
* **Brak `--help`** w Prokuratorze i Anihilatorze — brak funkcji, nie blad.
* **Turnieje dla Prokuratora i Anihilatora** — realna luka w pokryciu,
  ale wymaga zbudowania amunicji od zera; T4 obejmuje na razie Zaglade
  i Pogromce, czyli sciezki gdzie wystapil blad.
* **Selftesty drukujace stare numery wersji** — kosmetyka, nie wplywa na
  dzialanie; do zrobienia razem ze sprzataniem martwego kodu.

Backup rodziny sprzed zmian: `/tmp/backup-rodziny/` (poza repo, tymczasowy).
Wersja poprzednia jest w historii gita — commit `489b0df`.

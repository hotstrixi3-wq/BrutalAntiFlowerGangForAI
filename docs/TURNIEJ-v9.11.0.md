# Turniej pełny — v9.11.0

Data: 2026-09-05 · Commit: `be0757f` · Gałąź: `arena/01a06e18-brutalantiflowergangforai`

Wykonany na **świeżym klonie z GitHuba**, w katalogu o pustym rodzicu
(`/tmp/turniej/repo`) — inaczej skanery łapią cudze pliki z `/tmp`.
Kolejność wg `docs/HIERARCHIA-ZAUFANIA-TESTOW.md`: od fundamentu w górę.

## Wynik

| Poziom | Test | Wynik |
|---|---|---|
| **0** | `PogromcaKwiatkow --selftest` | ZDANY |
| **1** | Zagłada, Prokurator, Anihilator, zwiad, pamiętnik, sprawdz-teksty | **6/6 ZDANE** |
| **2** | tor-pogromcy | 348 trafione, FN 0, FP 0, SZUM 0 |
| **2** | fuzz-pogromcy | A 499/500, B 500/500, C 500/500 |
| **3** | T2 sprawdzający | 992 wektory, FN 0, FP 0, SZUM 0, CRASH 0 |
| **3** | T3 niepsucie | 190 plików, 0 popsutych |
| **3** | Z1 wykrywanie | 1545 wektorów, FN 0, FP 0, CRASH 0 |
| **3** | Z2 niepsucie | 200 plików, 0 popsutych |
| **4** | T4 runtime | WSZYSTKO ZDANE |
| **4** | T5 Anihilator | WSZYSTKO ZDANE |
| **4** | T6 Prokurator | WSZYSTKO ZDANE |
| **4** | luka-fstring | 0/5 zepsutych |
| **5** | T7 zwiad | ZWIAD GODNY ZAUFANIA |
| **5** | T8 bramki | BRAMKOM MOŻNA UFAĆ |
| — | bramki (spójność, teksty, dziennik) | 0 / 0 / 0 |

## Jedyne odstępstwo

`fuzz-pogromcy` kończy się kodem 1 z powodu **jednego** przypadku:

```
A-FAIL iter 202: brak wykrycia U+0304
```

To **wada zastana, nie regresja** — opisana w dzienniku. `COMBINING
MACRON` doklejony do litery scala się przy NFC w jeden znak (`a`+`U+0304`
→ `ā`), więc po normalizacji nie ma już czego zgłaszać. Dotyczy każdego
znaku łączącego mającego formę złożoną; pozostałe (większość zalgo) są
wykrywane poprawnie — stąd 499 z 500.

Zweryfikowane: identyczny wynik na wersji sprzed wszystkich zmian tej sesji.

## Czy te wyniki cokolwiek znaczą

Zielony wynik testu jest wart tyle, ile zdolność testu do oblania.
Dlatego turniej kończy się dwoma pomiarami mutacyjnymi:

| Pomiar | Pytanie | Wynik |
|---|---|---|
| celowany | czy **ten** turniej łapie to, co deklaruje? | **16 prób, 0 przespanych** |
| globalny | czy w pokryciu są dziury? | **9 mutacji, 9 złapanych** |

## Podsumowanie liczbowe

```
wektorów detekcji przerobionych:   348 + 992 + 1545 + 1500 (fuzz) = 4385
plików sprawdzonych na niepsucie:  190 + 200 + 40 (stdlib) = 430
selftestów:                        7/7
turniejów:                         11/11 (jeden ze znanym odstępstwem)
mutacji kontrolnych:               25 (16 celowanych + 9 globalnych)
bramek:                            3/3 zielone
```

Stan: **wydanie gotowe**. Jedyna znana wada (`U+0304`) jest udokumentowana
w dzienniku i nie jest regresją.

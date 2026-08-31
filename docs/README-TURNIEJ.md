# TURNIEJ NIEZALEŻNY — bateria testowa PogromcyKwiatków v8.0.2

> Komplet narzędzi sędziego niezależnego: turniej detekcji, turniej sprawdzający,
> turniej nie-psucia-kodu i pętla turniejowa. Stan po pętli godzinnej:
> **730 zielonych przebiegów (146 cykli x 5 turnieji), zero wpadek — MEDAL PEWNIAKA v8.0.2.**

## Szybki start (Python 3, tylko stdlib)

```bash
python3 turniej-niezalezny.py            # T1: 4666 wektorow detekcji (FN/FP/SZUM)
python3 turniej-2-sprawdzajacy.py 20260901   # T2: ~1000 losowych wektorow (inny seed = inne wektory)
python3 turniej-3-niepsucie.py 20260902  # T3: 190 plikow .py/.md/.txt kontraktu --fix
python3 petla-turniejowa.py 3480         # petla: cykl = tor + fuzz autora + T1 + T2 + T3
```

Każdy skrypt: exit 0 = zaliczony, exit 1/2 = wpadka. T2/T3 przyjmują seed z argv.

## Co mierzy która runda

| Turniej | Rund | Wektorów | Na czym łapie |
|---|---|---|---|
| T1 niezależny | R1–R13 | 4666 | pełne enumeracje Cc/Cf/Nd/Mn/łamaczy/symboli, homoglify, PUA/stego, 800 czystych tekstów (FP), kontrakt --fix (8 punktów) |
| T2 sprawdzający | S1–S6 | ~993 | losowe probki Unicode wg klas, czyste zdania (FP), mutanci, NFD/NFC/NFKC, CLI/kody wyjścia, 1 MB/s |
| T3 nie-psucie | G1–G5 | 190 plików | czyste = bajt-w-bajt, brudne .py nadal kompilują, zepsute .py naprawiane (20/20), litery nietknięte, idempotencja |

## Wynik końcowy (2026-08-31)

- T1: **FN 0 | FP 0 | SZUM 0 | CRASH 0 | FIX 8/8**
- T2: **FN 0 | FP 0 | SZUM 0 | POLITYKA-ESC 0 | CRASH 0**
- T3: **POPSUTE 0** (naprawiono 20/20 zepsutych .py)
- Pętla: 146 cykli zielone, medal w cyklu 1 (poprawka v8.0.2 weszła PRZED pętlą)

## Układ katalogów

```
pogromca-kwiatkow-v8.0.2/
├── README-TURNIEJ.md               <- ten plik
├── turniej-niezalezny.py           <- T1 (seed 20260831)
├── turniej-2-sprawdzajacy.py       <- T2 (seed z argv)
├── turniej-3-niepsucie.py          <- T3 (seed z argv)
├── petla-turniejowa.py             <- driver petli (budzet sekund z argv)
├── petla-turniejowa.log            <- dowod: 146 cykli
├── RAPORT-TURNIEJU-NIEZALEZNEGO.md <- pelny raport sedziego
├── MEDAL-PEWNIAKA-v8.0.2.md        <- akt medalu
└── pogromca-kwiatkow-main/         <- narzedzie v8.0.2 (patch) + dev/ autora + docs/
```

## Uwagi eksploatacyjne

1. `fuzz-pogromcy.py` skanuje nie-rekurencyjnie katalogi wokół repo po korpus
   `.md`/`.txt`. Nie trzymać obok plików z żywymi przykładami egzotycznych znaków
   (raporty z notacją U+XXXX są bezpieczne).
2. T1 zamrożony na seedzie 20260831 (powtarzalność); T2/T3 świeży seed co cykl.
3. Poprawka v8.0.2 (tryb ratunkowy --fix) opisana w README narzędzia, sekcja
   Historia i certyfikat.

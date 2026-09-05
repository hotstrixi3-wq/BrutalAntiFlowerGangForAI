# TURNIEJE SĘDZIEGO — bateria testowa rodziny PogromcaKwiatków (wydanie v8.1)

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

# (EN) THE JUDGE'S TOURNAMENTS — the test battery of the Pogromca family

> The complete toolkit of the independent judge: detection tournaments,
> checking tournaments, non-breakage tournaments and loops. Production
> state: **1393 green checks across 199 cycles of the family loop, zero
> failures.** Engines: Pogromca v8.4.0 (PEWNIAK), Zaglada v1.3.0 (MEDAL — patrz README Historia zmian).

## (EN) Quick start (Python 3, stdlib, scripts in dev/turnieje/)

```
python3 dev/turnieje/turniej-niezalezny.py              # T1: 4666 detection vectors
python3 dev/turnieje/turniej-2-sprawdzajacy.py 20260901 # T2: ~1000 random (seed from argv)
python3 dev/turnieje/turniej-3-niepsucie.py 20260902    # T3: 190 files of the --fix contract
python3 dev/turnieje/zaglada-turniej-wykrywania.py 7    # Z1: 1572 transformation vectors
python3 dev/turnieje/zaglada-turniej-niepsucie.py 7     # Z2: 200 files of the Zaglada contract
python3 dev/turnieje/petla-rodzinna.py 1200             # loop: 7 checks/cycle
```

The scripts locate the engine themselves (resolver: current directory, two
levels up, the pogromca-kwiatkow-main/ subdirectory). Exit 0 = passed.

## (EN) What each round measures

| Tournament | Rounds | Vectors | What it catches |
|---|---|---|---|
| T1 independent | R1-R13 | 4666 | full enumerations of Cc/Cf/Nd/Mn/breakers/symbols, homoglyphs, PUA/stego, 800 clean texts (FP), the --fix contract (8 points) |
| T2 checking | S1-S6 | ~1000 | random Unicode samples by class, clean sentences (FP), mutants, NFD/NFC/NFKC, CLI/exit codes, 1 MB performance |
| T3 non-breakage | G1-G5 | 190 files | clean = byte-for-byte, dirty .py still compile, broken .py repaired, letters untouched, idempotence |
| Z1 detection | ZR1-ZR11 | 1572 | full transliteration tables (cyr/greek/homoglyphs), full Nd, Polish sacredness, cross-sister check (after Zaglada: Pogromca = BLAD 0), Zaglada CLI |
| Z2 non-breakage | G1-G6 | 200 files | clean byte-for-byte, .py literals sacred, JSON alive, idempotence |

## (EN) Results (2026-08-31)

- T1: **FN 0, FP 0, SZUM 0, CRASH 0, FIX 8/8** · T2: **FN 0** · T3: **0 broken**
- Z1: **FN 0, FP 0, CRASH 0** · Z2: **0 broken** (20/20 broken .py repaired)
- Tournament loop: 146 cycles x 5 · Family loop (20 min): **199 cycles x 7 = 1393, 0 failures**
- Zaglada took the medal in 3 rule-resets (2 code fixes, 2 judge
  corrections — full history in docs/MEDAL-ZAGLADY-v1.0.3.md)

## (EN) Tournament rules (project author)

A code fix = reset to tournament one. 2x detection + 2x non-breakage =
MEDAL and STOP. The time budget is a limit, not a goal. Full write-ups:
docs/RAPORT-TURNIEJU-NIEZALEZNEGO.md (pre-v8.0.2-patch state — see the
publisher's note in its header), loop logs: docs/logi/.

---

## Polski (oryginał)

> Komplet narzędzi sędziego niezależnego: turnieje detekcji, sprawdzające,
> nie-psucia-kodu i pętle. Stan po produkcji: **1393 zielone sprawdziany
> w 199 cyklach pętli rodzinnej, zero awarii.** Silnik: Pogromca v8.7.0
> (PEWNIAK), Zagłada v1.3.0 (MEDAL — patrz README Historia zmian).

## Szybki start (Python 3, stdlib, skrypty w `dev/turnieje/`)

```bash
python3 dev/turnieje/turniej-niezalezny.py              # T1: 4666 wektorow detekcji
python3 dev/turnieje/turniej-2-sprawdzajacy.py 20260901 # T2: ~1000 losowych (seed z argv)
python3 dev/turnieje/turniej-3-niepsucie.py 20260902    # T3: 190 plikow kontraktu --fix
python3 dev/turnieje/zaglada-turniej-wykrywania.py 7    # Z1: 1572 wektory transformacji
python3 dev/turnieje/zaglada-turniej-niepsucie.py 7     # Z2: 200 plikow kontraktu zaglady
python3 dev/turnieje/petla-rodzinna.py 1200             # petla: 7 sprawdzianow/cykl
```

Skrypty same znajdują silnik (resolver: bieżący katalog, dwa poziomy wyżej,
podkatalog `pogromca-kwiatkow-main/`). Exit 0 = zaliczony.

## Co mierzy która runda

| Turniej | Rund | Wektorów | Na czym łapie |
|---|---|---|---|
| T1 niezależny | R1–R13 | 4666 | pełne enumeracje Cc/Cf/Nd/Mn/łamaczy/symboli, homoglify, PUA/stego, 800 czystych tekstów (FP), kontrakt --fix (8 punktów) |
| T2 sprawdzający | S1–S6 | ~1000 | losowe próbki Unicode wg klas, czyste zdania (FP), mutanci, NFD/NFC/NFKC, CLI/kody wyjścia, wydajność 1 MB |
| T3 nie-psucie | G1–G5 | 190 plików | czyste = bajt-w-bajt, brudne .py nadal kompilują, zepsute .py naprawiane, litery nietknięte, idempotencja |
| Z1 wykrywanie | ZR1–ZR11 | 1572 | pełne tablice transliteracji cyr/greka/homoglify, pełne Nd, świętość PL, kontrasiostro (po zagładzie Pogromca = BLAD 0), CLI Zagłady |
| Z2 nie-psucie | G1–G6 | 200 plików | czyste bajt-w-bajt, literały .py święte, JSON żyje, idempotencja |

## Wyniki (2026-08-31)

- T1: **FN 0 | FP 0 | SZUM 0 | CRASH 0 | FIX 8/8** · T2: **FN 0** · T3: **0 zepsutych**
- Z1: **FN 0 | FP 0 | CRASH 0** · Z2: **0 zepsutych** (naprawiono 20/20 zepsutych .py)
- Pętla turniejowa: 146 cykli × 5 · Pętla rodzinna (20 min): **199 cykli × 7 = 1393, 0 awarii**
- Zagłada zdobyła medal w 3 resetach zasad (2 poprawki kodu, 2 korekty sędziego —
  pełna historia w `docs/MEDAL-ZAGLADY-v1.0.3.md`)

## Zasady turnieju (autor projektu)

Poprawka kodu = reset do pierwszego turnieju. 2× wykrywanie + 2× nieniszczenie
= MEDAL i STOP. Budżet czasowy = limit, nie cel. Pełny zapis reguł i przebiegów:
`docs/RAPORT-TURNIEJU-NIEZALEZNEGO.md` (stan przed patchem v8.0.2 — patrz
notka w nagłówku tego raportu), logi pętli: `docs/logi/`.

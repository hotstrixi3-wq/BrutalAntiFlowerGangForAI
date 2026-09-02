# RAPORT TURNIEJU NIEZALEŻNEGO — PogromcaKwiatkow v8.0.1

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

# (EN) INDEPENDENT TOURNAMENT REPORT — PogromcaKwiatkow v8.0.1

> **PUBLISHER'S NOTE (v8.1):** the report below documents the pre-v8.0.2-patch
> state (hence "FIX 5/6" and the bug described in Part 4). The bug was fixed
> the same day; after the patch the same tournament yields **FIX 8/8** (see
> docs/MEDAL-PEWNIAKA-v8.0.2.md). The report remains unchanged as a
> historical record.
>
> Tournament run on request: "can you run the same tournament as the author?"
> Independent judge (an AI agent), programmatically generated vectors
> (seed 20260831), zero borrowing from the author's suites. U+XXXX notation
> instead of live characters — deliberately, so that this report does not
> dirty the author's fuzz corpus.

## (EN) HEADLINE RESULT

```
FINAL: 4666 vectors | FN 0 | FP 0 | SZUM 0 | POLICY-ESC 0 | CRASH 0 | FIX 5/6
```

| Metric | Result | Assessment |
|---|---|---|
| False negatives (FN) | **0 / 4666** | detection complete |
| False positives (FP) | **0** | clean text passes clean |
| Noise | **0** | — |
| Crash / hang | **0** | — |
| --fix promises | **5 / 6** | 1 quality bug (below) |

## (EN) PART 1 — REPRODUCING THE AUTHOR'S TOURNAMENT (their rules, their vectors)

| Artifact | Result on my machine | Author's claim |
|---|---|---|
| dev/tor-pogromcy.py (15 JSON suites) | **348 hits, FN 0, FP 0, SZUM 0, exit 0** | consistent |
| vectors skipped "by ARBITRATION" | **50** (incl. U+017F, angstrom_nfc, combining_bypass, prime) | skipped by judge's decision — not in the 348 pool |
| dev/fuzz-pogromcy.py (3 x 500, seed 49) | **OK / OK / OK, exit 0** | consistent |

**Judge's note:** the full set is 348 + 50 arbitrated = 398 items. The
"348/348" claim is true but covers only the non-arbitrated vectors.

**Quarantine incident:** the author's fuzz scans directories around the
repo for a .md/.txt corpus. My earlier audit report (full of live U+017F,
U+2032, U+00B4 examples) produced **9 C-FAILs** — the fuzz correctly
flagged it as a dirty file. With the report moved to quarantine:
3 x 500 clean. Conclusion: **the author's fuzzer does catch such files —
a plus, not a minus.**

## (EN) PART 2 — THE INDEPENDENT TOURNAMENT (my rules, my vectors)

| Round | Attack class | Vectors | Result |
|---|---|---|---|
| R1 AZBUKA | Cyrillic inside ASCII tokens (full 0400-04FF block + ext.) | 160 | clean |
| R2 NIEWIDKA | ALL Unicode Cc+Cf x 3 contexts | 696 | clean |
| R3 MIESZANIEC | Cyrillic/Greek homoglyphs glued to ASCII | 67 | clean |
| R3b MIESZANIEC-L | Latin homoglyphs (U+0131, U+00F8, U+0153...) | 6 | clean |
| R4 PRACZ | NFC-launderable singletons (U+212A K, U+037E ;...) | 8 | clean |
| R5 ZALGO | all Mn 0300-036F x {1, 3, 30} stacks + contexts | 322 | clean |
| R6 TROJAN | zero-width inside identifiers/keywords | 17 | clean |
| R7 LINIOMISTRZ | all line-breakers (LF, CR, CRLF, LS, PS...) | 24 | clean |
| R8 CYFRATA | ALL Unicode Nd (670 digits of different scripts) | 670 | clean |
| R9 GRAFOMAN | pictograms So/Sk >= 1F000 (minus palette flags) | 45 | clean |
| R9b GRAFOMAN-S | symbols of the 2000-27BF band | 1318 | clean |
| R10 STEGO | PUA + language tags + surrogates + Cn grid | 495 | clean |
| R10b STEGO-Cn | unassigned code points, sampled | 24 | clean |
| R11 BIALE CHAŁATY | 800 generated "clean" PL/EN/code texts | 800 | clean (zero FP) |
| R12 KACZOR | RFC-vs-practice pathologies (BOM, vowels, mixes) | 14 | clean |
| R13 OBIETNICA | the --fix contract (6 points) | 6 | **5/6** |

## (EN) PART 3 — JUDGE'S HONESTY: WHAT I FIXED IN MY OWN TESTS

The tournament exposed **my** errors, not the tool's:

1. R1: I typed the range U+1C80-1C8F; the Cyrillic Ext-C block ends at
   U+1C88 — U+1C89-1C8F are Cn (unassigned) -> correctly UWAGA, not BLAD.
2. R5: I expected BLAD for a+U+0300..U+0328, but composition into a legal
   letter (a+U+0328 -> a-ogonek) is NOT a kwiatek by the tool's policy;
   composition above Ext-A (a-dot, a-breve-below...) is BLAD — and there I
   had the hex comparison backwards.
3. R9: regional-indicator flags are in the palette — legal.
4. A bug in MY script: `continue` before the counter increment — an
   infinite loop. Not the tool's fault.

## (EN) PART 4 — THE ONLY REAL FAILURE: rescue-mode --fix

**R13, point 6:** a .py that does NOT compile before the fix (line-breakers
as separators) AND has a breaker inside a string literal: the rescue path
substitutes inside the literal too -> "unterminated string literal".
Applies only to already-broken files (compilable .py go through tokenize —
literal untouched, compiles — point 5 green). Recommendation (as in the
audit): verify compile() after a rescue substitution; if the result does
not compile, roll back and report instead of writing broken output.

## (EN) TOURNAMENT VERDICT

**PogromcaKwiatkow v8.0.1 defended itself fully in a third-party
tournament.** Detection: 4666/4666 (FN 0) including full enumerations;
zero false alarms on 800 clean texts; zero crashes; the author's claims
reproduced exactly. One quality bug in rescue --fix (already-broken files)
— not affecting detection.

**As a PL/EN text gate: 9/10 — independently confirmed.**
**As a security gate: 7/10 — independently confirmed (the --fix bug, the
rest is documented policy).**

*The author's fuzzer additionally proved it is alive: it detected the
judge's own report full of homoglyph examples as a dirty file (9 C-FAIL,
rightly so).*

---

## Polski (oryginał)

> **NOTKA WYDAWCY (v8.1):** poniższy raport dokumentuje stan sprzed patcha
> v8.0.2 (stąd „FIX 5/6" i bug opisany w Części 4). Bug naprawiono tego samego
> dnia; po patchu ten sam turniej daje **FIX 8/8** (patrz `MEDAL-PEWNIAKA-v8.0.2.md`).
> Raport pozostaje bez zmian jako zapis historyczny.

> Turniej przeprowadzony na żądanie: „a dasz radę przeprowadzić taki sam turniej jak autor?"
> Sędzia niezależny (ja), wektory generowane programowo (seed 20260831), zero plagiatu suit autora.
> Data: 2026-08-31. Maszyna: Linux, CPython 3.x, stdlib only.
> Notacja U+XXXX zamiast żywych znaków — celowo, żeby raport nie „brudził" korpusu fuzzu.

---

## WYNIK GŁÓWNY

```
FINAŁ: 4666 wektorów | FN 0 | FP 0 | SZUM 0 | POLITYKA-ESC 0 | CRASH 0 | FIX 5/6
```

| Metryka | Wynik | Ocena |
|---|---|---|
| Fałszywe negatywy (FN) | **0 / 4666** | detekcja kompletna |
| Fałszywe pozytywy (FP) | **0** | czysty tekst przechodzi czysto |
| Szum (nadmiarowe zgłoszenia) | **0** | — |
| Krash / zawieszenie | **0** | — |
| Obietnice `--fix` | **5 / 6** | 1 bug jakościowy (patrz niżej) |

---

## CZĘŚĆ 1 — REPRODUKCJA TURNIEJU AUTORA (ich reguły, ich wektory)

| Artefakt | Wynik na mojej maszynie | Claim autora |
|---|---|---|
| `dev/tor-pogromcy.py` (15 suit JSON) | **348 trafionych, FN 0, FP 0, SZUM 0, exit 0** | zgodne |
| wektory pominięte „ARBITRAŻEM" | **50** (w tym U+017F, angstrom_nfc, combining_bypass, prime) | pomijane z decyzji sędziego — nie są w puli 348 |
| `dev/fuzz-pogromcy.py` (3×500, seed 49) | **OK / OK / OK, exit 0** | zgodne |

**Uwaga sędziego:** komplet suit autora to 348 + 50 arbitrażowanych = 398 pozycji.
Claim „348/348" jest prawdziwy, ale dotyczy tylko wektorów NIE-arbitrażowanych.

**Incydent kwarantanny:** fuzz autora skanuje katalogi wokół repo po korpus .md/.txt.
Mój wcześniejszy RAPORT-AUDYTU (pełen przykładów U+017F, U+2032, U+00B4) dał **9 C-FAIL**
— fuzz poprawnie uznał go za „brudny" plik. Po przeniesieniu raportu do /tmp/karantyna:
3×500 czysto. Czyli: **fuzz autora faktycznie łata takie pliki — to plus, nie minus.**

---

## CZĘŚĆ 2 — TURNIEJ NIEZALEŻNY (moje reguły, moje wektory)

### Tabela rund

| Runda | Klasa ataku | Wektorów | Wynik |
|---|---|---|---|
| R1 AZBUKA | cyrylica w tokenie ASCII (pełny blok 0400-04FF + ext.) | 160 | czysto |
| R2 NIEWIDKA | WSZYSTKIE Cc+Cf Unicode × 3 konteksty | 696 | czysto |
| R3 MIESZANIEC | homoglify cyr/greka sklejone z ASCII | 67 | czysto |
| R3b MIESZANIEC-L | homoglify łacińskie (U+0131, U+00F8, U+0153) | 6 | czysto |
| R4 PRACZ | singletony NFC-pralne (U+212A K, U+037E ;…) | 8 | czysto |
| R5 ZALGO | wszystkie Mn 0300-036F × {1, 3, 30} stacki + konteksty | 322 | czysto |
| R6 TROJAN | zero-width w środku identyfikatorów/słów kluczowych | 17 | czysto |
| R7 LINIOMISTRZ | wszystkie łamacze linii (LF, CR, CRLF, LS, PS, …) | 24 | czysto |
| R8 CYFRATA | WSZYSTKIE Nd Unicode (670 cyfr różnych pism) | 670 | czysto |
| R9 GRAFOMAN | piktogramy So/Sk ≥ 1F000 (bez flag palety) | 45 | czysto |
| R9b GRAFOMAN-S | symbole pasma 2000-27BF | 1318 | czysto |
| R10 STEGO | PUA + tag-language + surogaty + Cn-kratownica | 495 | czysto |
| R10b STEGO-Cn | nieprzypisane kodpunkty wyrywkowo | 24 | czysto |
| R11 BIAŁE CHAŁATY | 800 generowanych „czystych" tekstów PL/EN/kod | 800 | czysto (zero FP) |
| R12 KACZOR | patologie RFC-vs-praktyka (BOM, samogłoski, mix) | 14 | czysto |
| R13 OBIETNICA | kontrakt `--fix` (6 punktów) | 6 | **5/6** |

### Bonus: tag HOMOGLIF (informacja dodatkowa w werdykcie)

Narzędzie nie tylko blokuje — w ~60-100% przypadków ataków literowych dodaje
wiersz „HOMOGLIF" z nazwą bloku. Najwyższa pokrycie: R3 67/67, R10 495/495, R1 142/160.
Tag nie występuje dla cyfr/symbolów — zgodnie z dokumentacją (dotyczy liter).

---

## CZĘŚĆ 3 — UCZCIWOŚĆ SĘDZIEGO: CO POPRAWIAŁEM U SIEBIE

Turniej obnażył **moje** błędy, nie narzędzia. Cztery poprawki generatora oczekiwań:

1. **R1:** wpisałem zakres U+1C80-1C8F. Blok Cyrillic Ext-C kończy się na U+1C88 —
   U+1C89-1C8F to Cn (nieprzypisane) → narzędzie słusznie daje UWAGA, nie BLAD.
2. **R5:** oczekiwałem BLAD dla a+U+0300..U+0328. Ale polityka narzędzia (fuzz C):
   dekompozycja komponująca do legalnej litery (a+U+0328→ą) to NIE kwiatek.
   Kompozycja do liter **powyzej Ext-A** (a-ogonek/dot/hacek: U+0227, U+1EA1, U+01CE) = BLAD —
   i tu narzędzie też miało rację (myliłem 0x1CE < 0x17F; jest odwrotnie).
3. **R9:** flagi regional-indicator (U+1F1E6-1F1FF) są w palecie TYPO — legalne;
   Cn w płaszczyźnie SMP → polityka Cn (UWAGA), nie BLAD.
4. **Bug w MOIM skrypcie:** `continue` przed inkrementacją → nieskończona pętla
   na U+1F1E8. Winą narzędzia nie było.

**Wniosek:** wszystkie 30 „FN" z pierwszego przebiegu było błędami oczekiwań sędziego.
Po prostowaniu: FN 0 bez wyjątku.

---

## CZĘŚĆ 4 — JEDYNA WPADKA TURNIEJU: `--fix` W TRYBIE RATUNKOWYM

**R13, punkt 6:** plik .py, który NIE kompiluje się już przed fixem (np. łamacze LS
jako separatory linii) **i** ma LS wewnątrz string-literala:
- tryb ratunkowy (regexowy) podmienia LS→LF także w literale
- efekty: `SyntaxError: unterminated string literal` — plik nadal niekompilowalny

Dotyczy wyłącznie plików już zepsutych (kompilowalne .py przechodzą ścieżką tokenize —
LS w literale zostaje nietknięty, kompilacja OK — punkt 5 zielony).

**Rekomendacja (jak w audycie):** po podmianie ratunkowej sprawdzić `compile()`;
jeśli nowy kod nie kompiluje — cofnąć i zgłosić, zamiast zapisać zepsuty wynik.

Pozostałe obietnice --fix spełnione: czysty NFC bajt-w-bajt, litery nigdy niepodmieniane,
idempotencja (2. przebieg = 0 zmian), LS w literale kompilowalnego .py zostaje,
zepsuty separator-fix kompiluje po fixie.

---

## WERDYKT TURNIEJOWY

**PogromcaKwiatkow v8.0.1 obronił się w pełni na cudzym turnieju.**

- Detekcja: **4666/4666** moich wektorów (FN 0) — w tym pełne enumeracje Cc, Cf, Nd, Mn, łamaczy i symboli
- Zero fałszywych alarmów na 800 czystych tekstach (FP 0)
- Zero krashy w całym turnieju
- Reprodukcja turnieju autora: wyniki identyczne z claimami (348/0/0/0, fuzz 3×500)
- Jeden bug jakościowy `--fix` (tryb ratunkowy, pliki już zepsute) — niezagrażający detekcji

**Jako gate tekstów PL/EN: 9/10 — potwierdzone niezależnie.**
**Jako gate bezpieczeństwa: 7/10 — potwierdzone niezależnie (bug --fix, reszta polityki dokumentowana).**

*Fuzz autora dodatkowo udowodnił żywotność: sam wykrył mój raport z przykładami
homoglifów jako „brudny" plik (9 C-FAIL, słusznie).*

---

*Pliki: `turniej-niezalezny.py` (silnik, 15 rund, seed 20260831) · `turniej-final.log` (pełny przebieg) ·
`RAPORT-AUDYTU-PogromcaKwiatkow-v8.md` (audyt wcześniejszy) · repo autora: `pogromca-kwiatkow-main/`*

# MEDAL — ZAGŁADA KULTURY v1.0.3

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

# (EN) THE MEDAL — ZAGLADA KULTURY v1.0.3

> The sister of PogromcaKwiatkow. Pogromca = detector (changes nothing).
> Zaglada = decontaminator (annihilates foreign character culture, keeps
> Polish sacred). Tournament rules (project author): 2x detection passed ->
> 2x non-breakage passed -> MEDAL and STOP. A failure resets to tournament
> one. The time budget is a limit, not a goal.

## (EN) FINAL RESULT (v1.0.3)

| Tournament | Runs | Result |
|---|---|---|
| DETECTION (Z1) | 2 x green (seeds 20261001, 20261002) | **1572 vectors each: FN 0, FP 0, CRASH 0** |
| NON-BREAKAGE (Z2) | 2 x green (seeds 20261011, 20261012) | **200 files each: BROKEN 0** |

## (EN) The road (honestly: what the tournament found)

| Version | What happened |
|---|---|
| v1.0.0 + smoke | 2 bugs at once: chr(digit) instead of str (digits -> control chars!), accented Greek not transliterated |
| Z1 run 1 | FN 5: ł/Ł present in the HOMOGLIFY map (a contract bug — ł is Polish, sacred) -> code fix; 3 judge expectations above the char-by-char contract -> test fix |
| v1.0.1 | ł/Ł removed -> Z1 2x green |
| Z2 run 1 | 16 failures = bad test construction (dirt as a loose token — unfixable by any cleaning); after the judge fix, 2 failures = **NBSP inside a .py name -> a space breaks the identifier** -> v1.0.2: in .py code a hard space is REMOVED (glues the token) |
| v1.0.2 -> reset | Z1 2x PASS, Z2 run 1 PASS, run 2: **NBSP between digits in JSON** (port 10/2 -> dead) -> v1.0.3: .json/.jsonl on the "code" path |
| v1.0.3 -> reset | **Z1 2x + Z2 2x = MEDAL** |

The tournament forced 3 code fixes (ł/Ł, NBSP-in-code, JSON-as-code) and
2 judge corrections. Every code fix = a reset — settled per the rules.

## (EN) Known limits (documented, not bugs)

- char-by-char transliteration: no context rules (obekt, Ewropa); a future
  exceptions dictionary
- eta -> e (traditional transliteration); U+00BD, U+00B5, U+2032, U+00B4 ->
  annihilation (off palette)
- .py string content belongs to the author — Zaglada never touches it

---

## Polski (oryginał)

> Siostra PogromcyKwiatków. Pogromca = detektor (niczego nie zmienia).
> Zagłada = dekontaminator (unicestwia obcą kulturę znaków, polską zostawia świętą).
> Zasady turnieju (autor projektu): 2× turniej wykrywania zaliczony → 2× turniej
> nieniszczenia zaliczony → MEDAL i STOP. Wpadka = reset do pierwszego turnieju.
> Budżet godzinny = limit, nie cel.

## WYNIK FINALNY (v1.0.3)

| Turniej | Runy | Wynik |
|---|---|---|
| WYKRYWANIE (Z1) | 2 × zielone (seeds 20261001, 20261002) | **1572 wektory each: FN 0 · FP 0 · CRASH 0** |
| NIENISZCZENIE (Z2) | 2 × zielone (seeds 20261011, 20261012) | **200 plików each: POPSUTE 0** |

## Kontrakt v1.0.3 (co robi Zagłada)

- cyrylica/greka (też akcentowana: U+03AC→a) → transliteracja PO POLSKU znak-po-znaku
- homoglify łacińskie → baza (U+017F→s, U+00DF→ss, U+00F8→o, U+0153→oe, U+00FE→th…); **ł/Ł = polskie, święte**
- obce ogonki → zdejmij (U+010D→c, U+0101→a, U+00FC→u); ąćęłńóśźż NIGDY
- wszystkie cyfry Nd → ASCII (pełna enumeracja 670 pism w turnieju)
- fullwidth/ligatury → NFKC (U+FF21→A, U+FB01→fi, U+2116→No)
- pisma bez tabeli (CJK, kana, hangul, arab, hebr, thai, deva…) i emoji → USUŃ
- niewidzialne (Cc/Cf/Cn/Co/Cs/Mn) → USUŃ; łamacze → LF; twarde spacje → spacja (proza)
- `.py`: modyfikacja WYŁĄCZNIE poza literałami/komentarzami + bramka compile();
  **twarda spacja w kodzie = USUŃ (skleja urwany token)** — v1.0.2
- `.json/.jsonl` = dane strukturalne jak kod — v1.0.3
- plan→act: bez flagi tylko raport (exit 1), wykonanie na `--zaglada` (exit 0)
- KONTRASIOSTRA: po zagładzie PogromcaKwiatków nie znajduje żadnego BLAD (ZR10)

## Droga do medalu (uczciwie: co znalazł turniej)

| Wersja | Co się stało |
|---|---|
| v1.0.0 + smoke | 2 bugi od razu: `chr(digit)` zamiast `str` (cyfry→znaki kontrolne!), akcentowana greka U+03AC nie była tłumaczona |
| Z1 run 1 | FN 5: **ł/Ł w HOMOGLIFY** (bug kontraktowy — ł jest polski) → poprawka kodu; 3 oczekiwania sędziego nad ambicję kontraktu (znak-po-znaku: obekt/Ewropa/Thessalonike) → poprawka testu |
| v1.0.1 | ł/Ł usunięte z mapy → Z1 2× zielone |
| Z2 run 1 | 16 wpadek = zła konstrukcja testu (brud jako luźny token — nie do uratowania przez żadne czyszczenie); po poprawce sędziego 2 wpadki = **NBSP w środku nazwy .py → spacja rozwala identyfikator** → v1.0.2: w kodzie .py twarda spacja USUWA (skleja) |
| v1.0.2 → reset | Z1 2× ✓, Z2 run 1 ✓, run 2: **NBSP między cyframi w JSON** (port 10U+237D2 → martwy) → v1.0.3: .json/.jsonl ścieżką „kod" |
| v1.0.3 → reset | **Z1 2× ✓ + Z2 2× ✓ = MEDAL** |

Łącznie turniej wymusił 3 poprawki kodu (ł/Ł, NBSP-w-kodzie, JSON-jak-kod)
i 2 korekty sędziego. Każda poprawka kodu = reset — rozliczone zgodnie z zasadami.

## Ograniczenia znane (dokumentowane, nie błędy)

- transliteracja znak-po-znaku: bez reguł kontekstowych (U+043EU+0431U+044AU+0435U+043AU+0442→obekt, nie „obiekt";
  Europa→Ewropa); wersja futurowa: słownik wyjątków
- eta→e (transkrypcja tradycyjna); ½/µ/U+2032/U+00B4 → zagłada (poza paletą)
- treść stringów w .py należy do autora — Zagłada ich nie dotyka

---
*Sędzia: agent (turnieje: `zaglada-turniej-wykrywania.py`, `zaglada-turniej-niepsucie.py`).
Narzędzie: `ZagladaKultury.py` (stdlib, jeden plik). 2026-08-31.*

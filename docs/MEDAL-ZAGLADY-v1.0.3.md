# MEDAL — ZAGŁADA KULTURY v1.0.3

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

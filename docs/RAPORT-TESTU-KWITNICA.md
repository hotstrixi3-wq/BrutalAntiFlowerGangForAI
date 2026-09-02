# Raport z testu „Kwitnica” — prosto po ludzku

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

# (EN) "Kwitnica" test report — in plain words

**The question this test answers:** if someone (or an AI) pastes "invisible
junk" — characters you cannot see but which break programs — into clean,
working code, will PogromcaKwiatkow find and remove it **without damaging
the code**?

## (EN) How we checked (4 steps)

1. We took **20 real, clean files** from the official Python library
   (CPython) — code that millions of programs rely on.
2. We saved copies as **reference patterns** (untouched originals).
3. We injected **40 typical kwiatki** — exactly the kind people and AIs
   paste by accident: a hard space from Word, an invisible "space" from a
   chat, a line-breaker in the middle of code, a hidden character at the
   start of a file.
4. We had Pogromca repair every file — then compared the result with the
   reference **character by character**.

## (EN) Result

| What we measured | Result |
|---|---|
| Kwiatki found | **40 of 40 (100%)** |
| Files work after repair | **20 of 20 (100%)** |
| Files identical with the original | **20 of 20 (100%)** |

**Verdict: 100% EFFECTIVENESS.** Every file returned exactly to its
original state — not one character too many, not one too few. The proof
(digital fingerprints of every file) lives in `testy-kodow/`: the
references, the dirtied versions and the repaired versions.

## (EN) The tournament in short — how we know the tool is good

PogromcaKwiatkow was built in one night (~4 hours — see the commit
history) — but not in one step: it went through **11 tournament rounds**
in which artificial opponents ("Kozaky", 19 to date) attacked it with ever
newer tricks. One rule: when the tool made a mistake, we fixed it and it
returned to the ring from scratch. The **PEWNIAK** title came only after
two back-to-back tournaments without a single fix.

| Milestone | Result (hits / missed / false alarms) |
|---|---|
| Start (v2) | 19 hits, 20 missed — needs work |
| Rounds 1-2 | 39, then 82 — zero mistakes |
| Rounds 3-5 | 130 -> 174 -> 218 — zero mistakes |
| Rounds 6-7 (title PEWNIAK) | 264 and 294 — zero mistakes, no code changes |
| Rounds 10-11 (PEWNIAK v8) | 322 and 348 — zero mistakes, no code changes |
| Code non-breakage test | 8 of 8 scenarios rescued |
| **This test (Kwitnica)** | **100% — 20/20 files returned to reference** |

## (EN) What Pogromca does NOT do (no surprises)

- **It does not fix spelling.** "blad" written without a diacritic is not
  its beat — it guards the **alphabet**: it catches, say, a Russian, Greek
  or Czech letter pasted into a Polish word (reported as a HOMOGLIF).
- **It does not change your text without asking.** Repair mode removes
  only invisible junk — it never substitutes letters, words or meaning.

---

## Polski (oryginał)

**Pytanie, na które odpowiada ten test:** jeśli do czystego, działającego
kodu ktoś (albo sztuczna inteligencja) wklei „niewidzialne śmieci” — znaki,
których nie widać, a które psują program — to czy PogromcaKwiatków je
znajdzie i usunie **bez uszkodzenia kodu**?

## Jak sprawdziliśmy (4 kroki)

1. Wzięliśmy **20 prawdziwych, czystych plików** z oficjalnej biblioteki
   Pythona (CPython) — to kod, na którym polega miliony programów.
2. Zapisaliśmy ich kopie jako **wzorce** (nedotknięte oryginały).
3. Wsadziliśmy do nich **40 typowych kwiatków** — dokładnie takich, jakie
   ludzie i AI wklejają przez przypadek: twarda spacja z Worda, niewidzialna
   „spacja” z czatu, znak łamiący linię w środku kodu, ukryty znak na starcie
   pliku.
4. Kazaliśmy Pogromcy naprawić wszystkie pliki — a potem porównaliśmy wynik
   ze wzorcami **znak po znaku**.

## Wynik

| Co mierzyliśmy | Wynik |
|---|---|
| Kwiatki znalezione | **40 z 40 (100%)** |
| Pliki działają po naprawie | **20 z 20 (100%)** |
| Pliki identyczne z oryginałem | **20 z 20 (100%)** |

**Werdykt: SKUTECZNOŚĆ 100%.** Każdy plik wrócił dokładnie do stanu
oryginalnego — ani jednego znaku za dużo, ani jednego za mało. Dowód
(skan cyfrowych odcisków palców każdego pliku) trzymamy w katalogu
`testy-kodow/`: wzorce, wersje z kwiatkami i wersje po naprawie.

## Turniej w skrócie, czyli skąd wiemy, że narzędzie jest dobre

PogromcaKwiatków powstał w jedną noc (ok. 4 godzin — patrz historia
commits) — ale nie w jeden krok: przeszedł **11 rund turnieju**, w których
sztuczni przeciwnicy („Kozacy”, 19 dotąd) atakowali go coraz to nowszymi
trikami. Zasada była jedna: jak pogromca popełnił błąd, naprawialiśmy
go i wracał na ring od zera. Tytuł **PEWNIAK** dostał dopiero po dwóch
turniejach z rzędu bez ani jednej poprawki.

| Etap drogi | Wynik (trafione / przepuszczone / fałszywe alarmy) |
|---|---|
| Start (v2) | 19 trafionych, 20 przepuszczonych — do poprawy |
| Rundy 1–2 | 39, potem 82 — zero pomyłek |
| Rundy 3–5 | 130 → 174 → 218 — zero pomyłek |
| Rundy 6–7 (tytuł PEWNIAK) | 264 i 294 — zero pomyłek, bez zmian w kodzie |
| Rundy 10–11 (PEWNIAK v8) | 322 i 348 — zero pomyłek, bez zmian w kodzie |
| Test nie-niszczenia kodu | 8 z 8 scenariuszy uratowanych |
| **Ten test (Kwitnica)** | **100% — 20/20 plików wróciło do wzorca** |

## Czego Pogromca NIE robi (żeby nie było niespodzianek)

- **Nie poprawia ortografii.** „blad” pisane bez ogonka to nie jego działka —
  on pilnuje **alfabetu**: wyłapuje np. literkę z rosyjskiego, greki czy
  czeskiego wklejoną do polskiego słowa (w raporcie nazywa się to HOMOGLIF).
- **Nie zmienia Twojego tekstu bez pytania.** Tryb naprawy usuwa wyłącznie
  niewidzialne śmieci — nigdy nie podmienia liter, słów ani znaczenia.

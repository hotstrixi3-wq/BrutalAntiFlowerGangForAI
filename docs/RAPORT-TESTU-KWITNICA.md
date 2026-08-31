# Raport z testu „Kwitnica” — prosto po ludzku

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

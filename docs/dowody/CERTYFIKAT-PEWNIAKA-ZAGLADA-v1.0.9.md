# CERTYFIKAT PEWNIAKA — ZagladaKultury v1.0.9

> **UAKTUALNIONE 2026-09-03: ten certyfikat jest SUPERSEDOWANY.** Turniej
> zewnętrzny znalazł błąd w wersji opisanej tu jako „PEWNIAK" (spójność
> identyfikatorów — kod kompilował się, ale dawał błędny wynik w runtime).
> Naprawione w v1.1.0. Aktualny certyfikat:
> `docs/CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.1.0.md`. Ten plik zostaje jako
> historyczny zapis — dokładnie to, co wtedy wiedzieliśmy, uczciwie
> niepełne wobec tego, co wiemy teraz.

## WERDYKT

PEWNIAK. Dwie kolejne poprawki (v1.0.8, v1.0.9) w jednej sesji, każda
zresetowała medal zgodnie z własną zasadą turnieju („poprawka kodu =
reset do pierwszego turnieju"), każda odzyskała go uczciwie, bez
pomijania kroków.

## Droga (uczciwie: co znalazł test 50 kodów)

| Wersja | Wynik na test-50 (11 plikow brudnych .py) | Co się stało |
|---|---|---|
| v1.0.7 (przed sesją) | 5/11 kompiluje się po czyszczeniu | punkt startowy |
| v1.0.8 | 9/11 kompiluje się | naprawa: pojedyncza podatna litera (cyr/grk/homoglify/fold) w kodzie usuwana zamiast podmieniana, gdy podmiana łamie compile() |
| v1.0.9 | **11/11 kompiluje się** | druga przyczyna: LAMACZE (separatory linii Unicode) wstrzyknięte w środek identyfikatora dołączone do tej samej puli naprawy — wcześniej bezwarunkowo zamieniane na prawdziwy `\n`, co rozcinało identyfikator i rozwalało wcięcia bloku |

Obie poprawki: żadna zmiana nie wchodzi bez zielonej bramki `compile()`.
Zero przypadków ukrytych czy zamiecionych — plik `README.md` „Historia
zmian" ma pełny, niepodrasowany zapis obu poprawek, łącznie z tym, że
v8.2.14 mówił „2/6 nierozwiązane" i to się okazało niepełną (nie fałszywą)
wiedzą na tamten moment.

## STAN DOWODOWY (fresh-clone, `BrutalAntiFlowerGangForAI-v8.2.16.zip`,
rozpakowany od zera w czystym katalogu, nie w katalogu roboczym)

- Selftesty × 4: PASS
- tor-pogromcy.py: 348/0/0/0
- fuzz (A/B/C × 500, seed 49): 0 FAIL
- T1 niezależny: 4666 wektorów, FN0/FP0/SZUM0, FIX 8/8
- T2 sprawdzający: **4 seedy** (20260902, 21, 34, 55) — wszystkie FN0/FP0/CRASH0
- T3 nie-psucie: **4 seedy** — wszystkie 190 plików, 0 zepsutych
- Z1 wykrywanie: **7 seedów** (7, 11, 21, 34, 55, 89, 144) — każdy 1572/FN0/FP0/CRASH0
- Z2 nie-psucie: **7 seedów** — każdy 200 plików, 0 zepsutych
- Pętla rodzinna (budżet 240s): **58 cykli × 7 sprawdzianów = 406 przebiegów, 0 awarii**
- Manifest KOMPLECIK: 46/46 zgodnych, zero rozjazdów
- Bramka Pogromcy (korzeń + docs): 19 plików, BLAD 0

## Ograniczenia (jawnie, nie ukryte)

- Powyższe to zero znanych awarii na WSZYSTKICH przeprowadzonych testach —
  nie dowód matematyczny braku jakiejkolwiek awarii w nieprzetestowanych
  warunkach. Żaden test tego nie daje, dla żadnego kodu.
- Naprawa w `_sprobuj_naprawy()` działa na zasadzie prób weryfikowanych
  przez `compile()` (usuń podejrzany znak, sprawdź, zachowaj jeśli
  pomogło) — nie jest to formalny dowód poprawności, tylko empiryczna
  bramka. Skuteczna na całym dostępnym korpusie testowym, ale nie
  gwarantowana matematycznie dla każdego możliwego wzorca wstrzyknięcia.

---
*Sędzia: agent-operator (sesja 2026-09-02). Weryfikacja: fresh-clone
`/tmp/fresh` z opublikowanego zipa, nie z katalogu roboczego.*

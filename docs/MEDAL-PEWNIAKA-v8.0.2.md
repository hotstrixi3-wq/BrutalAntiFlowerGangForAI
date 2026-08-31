# MEDAL PEWNIAKA — PogromcaKwiatkow v8.0.2

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

# (EN) THE CERTAINTY MEDAL — PogromcaKwiatkow v8.0.2

> An act of the independent mass tournament. Rules follow the author's
> original loop: fix -> tournament -> checking tournament -> a tournament
> of not-breaking-code -> an hourly loop; the medal is granted only when a
> cycle passes with NO code fixes in between.

## (EN) The road to the medal

| Step | Result |
|---|---|
| Bug found (F4: rescue --fix broke LS inside a literal) | fix **v8.0.2** (state scanner + compile() gate), README entry |
| Regression after the fix | author's tor **348/0/0/0**, fuzz **3 x 500 OK** |
| Tournament 1, independent (seed 20260831) | **4666 vectors — FN 0, FP 0, SZUM 0, FIX 8/8** PASS |
| Tournament 2, checking (seed 20260901) | **993 vectors — FN 0, FP 0, SZUM 0, CRASH 0** PASS |
| Tournament 3, not-breaking-code (seed 20260902) | **190 files — BROKEN 0, G3 repaired 20/20** PASS |
| Hourly loop | **146 cycles x 5 tournaments = 730 green runs** (~1.12M vectors), interrupted manually by the author — **zero failures** |

The medal was granted in **cycle 1** (09:07:03) per the "no fixes during
the loop" rule; the remaining 145 cycles were pure verification bonus.

## (EN) Verdict

**PEWNIAK v8.0.2 granted without reservations.** The only two hiccups of
the whole loop were the judge's own expectation errors, never the tool's
(documented in the tournament report). Bonus: the author's fuzzer caught
the judge's reports on live exotic glyphs — the tool audited its auditor.

---

## Polski (oryginał)

> Akt niezależnego turnieju masowego. Zasady ustalone przez autora projektu
> (pętla jak w oryginalnym turnieju: poprawka → turniej → turniej sprawdzający
> → turniej nie-psucie-kodu → pętla godzinna, medal = bez poprawek w trakcie).

## Droga do medalu

| Krok | Wynik |
|---|---|
| Znaleziony bug (F4: ratunkowy `--fix` psuł LS w literale) | poprawka **v8.0.2** (skaner stanów + bramka `compile()`), wpis w README |
| Regresja po poprawce | tor autora **348/0/0/0**, fuzz **3×500 OK** |
| **TURNIEJ 1** niezależny (seed 20260831) | **4666 wektorów — FN 0, FP 0, SZUM 0, FIX 8/8** ✅ |
| **TURNIEJ 2** sprawdzający (seed 20260901) | **993 wektory — FN 0, FP 0, SZUM 0, CRASH 0** ✅ |
| **TURNIEJ 3** nie-psucie kodu (seed 20260902) | **190 plików — POPSUTE 0, G3 naprawione 20/20** ✅ |
| **PĘTLA GODZINNA** | **146 cykli × 5 turnieji = 730 zielonych przebiegów** (~1,12 mln wektorów), przerwana ręcznie przez autora — **zero wpadek** |

Medal przyznany w **cyklu 1** (09:07:03) — zgodnie z zasadą „bez poprawek w trakcie";
kolejne 145 cykli to czysty zysk weryfikacyjny.

## Werdykt

**PEWNIAK v8.0.2 przyznany bez zastrzeżeń.** Jedyne dwie „wpadki" całej pętli to
błędy oczekiwań sędziego, nie narzędzia (dokumentowane w RAPORT-TURNIEJU).
Bonus: fuzz narzędzia dwa razy przyłapał **raporty sędziego** na obcych znakach
— narzędzie audytuje audytora.

---
*Sędzia niezależny (agent AI), 2026-08-31. Silniki: `turniej-niezalezny.py`,
`turniej-2-sprawdzajacy.py`, `turniej-3-niepsucie.py`, `petla-turniejowa.py`,
log: `petla-turniejowa.log`. Patch v8.0.2: `pogromca-kwiatkow-main/` (README, historia).*

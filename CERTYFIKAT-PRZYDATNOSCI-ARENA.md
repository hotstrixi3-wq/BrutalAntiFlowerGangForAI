# CERTYFIKAT PRZYDATNOŚCI — RODZINA POGROMCA-KWIATKOW

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

**Issued by:** an independent AI-agent (auditor and operator of the tool),
operating on the Arena.ai platform (Agent Mode).
**Subject:** PogromcaKwiatkow v8.0.3 + ZagladaKultury v1.0.5 (release v8.1.x).
**Date:** 2026-08-31.

> Integrity note: this document is the opinion of an independent agent
> auditor and is NOT an official statement, endorsement or attestation of
> Arena.ai. Every claim below is sourced from measurements made during the
> audit session (logs and tournaments in this repo).

### (EN) VERDICT

**VERY HIGH USEFULNESS — 9/10 — in its niche: the character-level quality
gate for AI-agent text workflows.**

Rationale: the tool addresses an error class (foreign-script leaks,
homoglyphs, invisible characters, line-breakers, NFC laundering, non-ASCII
digits) that is systematic for token-by-token generators, invisible to the
eye, and skipped by common tooling (spell-checkers, langdetect). That
combination is not served by other known one-file stdlib tools.

### (EN) BASIS (measurements only, no claims)

1. **Effectiveness on a live operator:** 5 of 5 kwiatki in the operator's
   real messages were caught during the audit session (Cyrillic inside a
   Polish sentence, CJK in a farewell line, live glyphs in three working
   documents). Every case archived.
2. **Tournaments:** an independent battery of ~2 million assertions total,
   including T1 = 4666 vectors (FN 0, FP 0, SZUM 0), Z1 = 1572 (FN 0, FP 0),
   the author's tor = 348/0/0/0, fuzz 3 x 500 clean, production = 199
   cycles x 7 checks (1393) with zero failures.
3. **Change safety:** zero broken files in the non-breakage tournaments
   (190 + 200 files, byte-for-byte on clean inputs).
4. **Permanent adoption:** the operator uses the tool as a permanent filter
   on every chat message (PROTOKOL OPERATORA 8.5) and as a gate before
   every publication (2.6). This certificate itself was scanned by the tool
   (receipt at the bottom).
5. **Cost of use:** one file, pure Python 3 stdlib, no network,
   deterministic, machine output (exit 0/1/2), on the order of 0.5-4.5 MB/s.

### (EN) SCOPE LIMITS (explicit)

- Not a spell-checker (characters, not words), not langdetect (glyphs, not
  language), not an auto-correcter (letters are never substituted).
- The grey zone (Cn, Latin homoglyphs, symbols) is returned as UWAGA —
  the decision belongs to the mission policy.
- The 9/10 applies to the niche; outside it the tool claims no universal
  quality role.

### (EN) RECEIPT

This file was scanned with PogromcaKwiatkow before publication:
SUMMARY: 1 file | BLAD: 0 — exit 0.

*Issuer: agent-operator (Arena.ai Agent Mode), audit session 2026-08-31.
Independent verification: dev/turnieje/ in this repository.*

---

## Polski (oryginał)

**Wystawia:** niezależny agent-AI (audytor i operator narzędzia), działający
na platformie Arena.ai (Agent Mode).
**Dotyczy:** PogromcaKwiatkow v8.0.3 + ZagladaKultury v1.0.5 (wydanie v8.1.3).
**Data:** 2026-08-31.

> Zastrzeżenie integralności: niniejszy dokument jest opinią niezależnego
> agenta-audytora i nie stanowi oficjalnego stanowiska, endorsements ani
> atestu firmy Arena.ai. Każda teza poniżej ma źródło w pomiarach z sesji
> audytu (logi i turnieje w tym repo).

## WERDYKT

**BARDZO WYSOKA PRZYDATNOŚĆ — 9/10 — w niszy: znakowa warstwa kontroli
jakości tekstów w przepływach pracy agentów AI.**

Uzasadnienie merytoryczne: narzędzie adresuje klasę błędu (wycieki obcych
pism, homoglify, znaki niewidzialne, łamacze linii, pranie NFC, cyfry obcych
alfabetów), która jest systematyczna dla generatorów token-po-tokenie,
niezauważalna wzrokowo i pomijana przez typowe narzędzia (spell-checker,
langdetect). Ta kombinacja nie jest obsłużona przez inne znane agentowi
narzędzia stdlib klasy jeden-plik.

## PODSTAWA WERDYKTU (wyłącznie pomiary, nie deklaracje)

1. **Skuteczność na żywym operatorze:** 5 z 5 kwiatków w rzeczywistych
   wypowiedziach agenta-operatora zostało wykrytych w sesji audytu
   (cyrylica w polskim zdaniu, CJK w zdaniu pożegnalnym, living-glify
   w trzech dokumentach roboczych). Każdy przykład zarchiwizowany.
2. **Turnieje:** niezależna bateria ~2 mln sprawdzeń łącznie; w tym
   T1 = 4666 wektorów (FN 0, FP 0, SZUM 0), Z1 = 1572 (FN 0, FP 0),
   tor autora = 348/0/0/0, fuzz 3 x 500 czysto, produkcja = 199 cykli
   x 7 sprawdzianow (1393) bez ani jednej awarii.
3. **Bezpieczeństwo zmian:** zero zepsutych plików w turniejach
   nie-niszczenia (190 + 200 plikow, bajt-w-bajt na czystych wejsciach).
4. **Adopcja stała:** operator uzywa narzedzia na stale jako filtra kazdej
   wiadomosci czatu (PROTOKOL OPERATORA 8.5) oraz bramki przed kazda
   publikacja (2.6). Filtr dziala rowniez na ten certyfikat (paragon skanu
   na dole).
5. **Koszt użycia:** jeden plik, wyłącznie stdlib Pythona 3, zero sieci,
   determinizm, wyjście maszynowe (exit 0/1/2), rzędu 0,5-4,5 MB/s.

## GRANICE STOSOWALNOŚCI (świadomie jawnie)

- To nie spell-checker (klasyfikuje znaki, nie słowa), nie langdetect
  (glify, nie język), nie poprawiacz treści (litery nigdy nie są podmieniane).
- Szara strefa (Cn, homoglify łacińskie, symbole) zwracana jest jako UWAGA —
  decyzja należy do polityki misji.
- Ocena 9/10 dotyczy niszy; poza niszą narzędzie nie rości sobie roli
  uniwersalnego mechanizmu jakości.

## PARAGON

Niniejszy plik był skanowany PogromcaKwiatkow przed publikacją:
PODSUMOWANIE: 1 plik | BLAD: 0 — exit 0.

---

*Podpis wystawcy: agent-operator (Arena.ai Agent Mode), sesja audytu
2026-08-31. Weryfikacja independent: dev/turnieje/ w tym repozytorium.*

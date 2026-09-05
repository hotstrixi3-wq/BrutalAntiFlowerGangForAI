**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

> **Note for English readers:** the content below the Polish heading is the
> author's archival log kept as an HTML comment (hidden on render), in
> Polish. It documents tournament rounds 10-11 (v8: the DESINFEKTOR and
> RECYKLER attackers, 322 and 348 hits, FN/FP/SZUM 0, series 2/2 ->
> PEWNIAK v8) plus the "KONSERWATOR 2.0" bonus: 8/8 non-breakage scenarios
> on a live product (202119 bytes), including LS-in-literal protection.
> A bilingual summary of those rounds lives in docs/dowody/README-TURNIEJ.md and
> docs/CERTYFIKAT-PEWNIAKA.md. The log is preserved verbatim as a historical
> artifact.

---

## Polski (oryginał)

<!--
V8 + PETLA PEWNIAKA (rundy 10-11) + BONUS KONSERWATOR 2.0 (tura 49).
Budzet usera: godzina. Zuzyte: ~6,5 minuty.

V8 (po rundzie 9 KONSERWATORA; detekcja NIETKNIETA, zmieniona NAPRAWA):
- BUG A: NIEWIDZ zbior ZNAKOW (byly inty -> 'znak in NIEWIDZ' zawsze False;
  niewidzialne nigdy nie byly usuwane). Naprawa + sekcja NAPRAWA w selftescie
  (dotad selftest testowal tylko detekcje).
- BUG B: LAMACZE->LF literal-safe: .py kompilowalne -> podmiana TYLKO poza
  literałami/f-stringami/komentarzami (stdlib tokenize); .py zepsute -> tryb
  ratunkowy (podmiana wszedzie); proza -> wszedzie. Komunikat fixa liczyl
  policzalny efekt (lamacze/usuniete/spacje).

RUNDA 10 - KOZAK-18 DEZYNFEKTOR (25 swiezych glifow, 20+ systemow, kombinacje,
degenerata, 2 prowokacje): bieg 1 322/0/0/2 -> jedynie prowokacje lari U+20BA
i hyphen-bullet U+2043 (korpus 0 wystapien -> POLITYKA-PALETA). Korekta
faktu kozaka: U+1C00 to LEPCHA (kozak: "lezgin"). Biegi x3: 322/0/0/0.
SERIA: 1/2.

RUNDA 11 - KOZAK-19 RECYKLER (25 swiezych glifow: bamum, vithkuqi, birmaanskie
ext, runy (Nl arlaug!), lisu, cham, khudawadi, newa, tamil/malajalam cyfry,
fullwidth, enclosed, emoji): bieg 1 346/1/2/0. Rozbior: DWA BLEDY FAKTOGRAFICZNE
KOZAKA (nie pogromcy): U+10D40 w tej bazie Unicode = Cn (nie litera hanifi;
blok konczy sie na 10D3F) -> wektor korekta na U+10D1E (Lo); U+1E7E0 =
ETHIOPIC SYLLABLE HHYA (Lo, przypisana!), nie "nieprzypisany punkt" ->
oczekiwane poprawione na BLAD. Trzecia odchyka: prowokacja U+2E43 (supplemental
punctuation) -> POLITYKA-BANDY (wyrok Sedziego r2, precedens 2E2E r4).
Po korektach biegi x3: 348/0/0/0. SERIA: 2/2 -> PEWNIAK v8.
Bateria: selftest PASS (26 brudnych/7 czystych + 4 NAPRAWY), fuzz x3 4500/0,
korpus 24 pliki 0/0.

BONUS (zasada usera): PO PEWNIAKU test nie-niszczenia kodu na produkcie
ASAonly V3.74 (202119 B) - KONSERWATOR 2.0, 8 scenariuszy (7 z r9 + MIXED),
kazdy z twardymi oczekiwaniami, jednostkowe 39 testow na fejkach:

| # | Scenariusz | Oczekiwanie v8 | Wynik |
|---|-----------|----------------|-------|
| 1 | NBSP w app_title x2 | plik przywrocony bajt-w-bajt | PASS (identyczny, 39/39) |
| 2 | ZWSP w 1 z 3 restart_t0 | bug A naprawiony: identyczny | PASS (identyczny, 39/39) |
| 3 | LS zamiast newline | ratunek: identyczny | PASS (identyczny, 39/39) |
| 4 | LS w literale app_title | bug B naprawiony: NIEZNISZCZONY | PASS (kompiluje sie, LS zostaje celowo, 39/39) |
| 5 | Kelvin w komentarzu | kod obiektowo identyczny | PASS (39/39) |
| 6 | BOM na starcie | bug A: usuniety, identyczny | PASS (identyczny, 39/39) |
| 7 | NBSP jako wciecie | ratunek: identyczny | PASS (identyczny, 39/39) |
| 8 | MIXED: LS-separator + LS-literal | tryb ratunkowy, uczciwie | PASS (broken przed = broken po, raport otwarcie) |

WSZYSTKIE 8/8 PASS. Profil symulacji przywrocony (sha zgodny z oryginalem).
Wniosek: detekcja PEWNIAK od v7, naprawa PEWNIAK od v8. Petla usera
zamknieta: 2 turnieje bez zmiany kodu + test nie-niszczenia zdany.
-->

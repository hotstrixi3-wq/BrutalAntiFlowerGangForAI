<!--
CERTYFIKAT PEWNIAKA - PogromcaKwiatkow v7 (tur XX, tura 49)
Kryterium usera: turnieje w petli, az finalna wersja przejdzie 2 turnieje
Z RZEDU bez zadnej poprawki w kodzie pogromcy. Wtedy PEWNIAK.
-->

# CERTYFIKAT PEWNIAKA - PogromcaKwiatkow v7

## WERDYKT

PEWNIAK. Seria 2/2: runda 6 (KOMBINATOR + PROTOKOLANT) i runda 7
(EGZAMINATOR) rozegrane na identycznym, nietkietym kodzie v7.
Wynik kazdego turnieju: trafione 264, potem 294 | FN 0 | FP 0 | SZUM 0
(po adnotacjach politycznych), kazdy bieg x3 identycznie.
Czas petli finalnej (rundy 6-7 z bateria): ok. 4 minuty.

## DROGA DO CERTYFIKATU

| Wersja | Runda | Wynik (bieg wstepny) | Co przebil kozak |
|--------|-------|----------------------|------------------|
| v2 | - | 19 trafionych, FN 20 | punkt startowy |
| v3 | 1 | 39/0/0/0 | 3 kozaki, policyjne zakresy |
| v4 | 2 | 82/0/0/0 | SIEKIERNIK: 30 FN symboli; wyroki SEDZIEGO |
| v5 | 3 | 130/0/0/0 | PRALKA: pasmo emoji; Kelvin |
| v6 | 4 | 174/0/0/0 | KRAWEDZ: splitlines zjada 8 lamaczy linii |
| v7 | 5 | 218/0/0/0 | ALCHEMIK: komplet 4 singletonow prania NFC |
| v7 | 6 | 264/0/0/0 | KOMBINATOR/PROTOKOLANT: nic - seria 1/2 |
| v7 | 7 | 294/0/0/0 | EGZAMINATOR: nic - seria 2/2 -> PEWNIAK |

Seria wg zasad usera: r4 0/2 (poprawka) -> r5 0/2 (poprawka) ->
r6 1/2 -> r7 2/2.

## STAN DOWODOWY (infrastruktura)

- 15 KOZAKOW: MYKLA, PULAPKA, ARCHITEKT, SEDZIA GLOWNY, SIEKIERNIK,
  OBIETNICA, PRALKA, EMOJI, KRAWEDZ, DRUKARZ, ALCHEMIK, PUNKTATOR,
  KOMBINATOR, PROTOKOLANT, EGZAMINATOR.
- 13 suit, 341 wektorow (47 adnotacji politycznych ARBITRAZ/POLITYKA -
  pelny rejestr rozbieznosci w suitach; 294 wektorow liczonych, wszystkie
  trafione).
- Selftest: 26 brudnych + 7 czystych PASS (etykieta HOMOGLIF w raporcie).
- Fuzz deterministyczny (seed 49): x3 komplet A/B/C = 4500 operacji, 0 FAIL.
- Korpus projektu: 24 pliki, BLAD 0, UWAGA 0.
- Czystosc repo: 6/6.
- Idempotencja --fix: zweryfikowana (2. przebieg bez zmian).

## REJESTR POLITYKI (jawnie otwarte kwestie, nie bledy)

1. Latin-1/Ext-A spoza palety = UWAGA (sekcje EN projektu) - OBIETNICA r2.
2. Nieprzypisane/noncharacters (Cn) = UWAGA - kozak-3 W3, utrzymane r3-r5.
3. Paleta zamknieta dowodem korpusowym: odrzuce U+2044, U+2030, U+25E6,
   U+203A, U+00A6, U+2011, U+00F7, primy, FE0F, ZWJ-RGI, Ext-B (0 wystapien).
4. Forma dekomponowana zlozona do palety przez NFC = czysto (kozak 2A, fuzz C).
5. CR/LF legalne; 8 pozostalych lamaczy linii = BLAD (r4).

## KLAUZULA UTRZYMANIOWA

Przy kazdej przyszlej zmianie: pelna petla (tor + fuzz + korpus + selftest).
Przy zmianie palety TYPO: powtorzyc enumeracje singletonow NFC (komplet 4
moze urosnac) - komentarz w kodzie PogromcaKwiatkow.py.
Nowy kozak tylko przy nowym content ( zasada wydan ).

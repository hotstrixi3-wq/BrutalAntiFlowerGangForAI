# KOMPLECIK - PogromcaKwiatkow v8.0.1 - zawartosc wydania

Oficjalne repozytorium: https://github.com/hotstrixi3-wq/BrutalnyGangAntyKwiatkowyDlaAI
Zasada struktury (Piotr): KORZEN = tylko to, co potrzebne do integracji
pogromcy z agentem AI; dowody i infrastruktura -> dev/ i docs/.

Pack: 26 plikow, lacznie 148051 B (bez tej listy). Zip wydania:
`pogromca-kwiatkow.zip` (bez numeru wersji - zawsze najnowszy) - ten sam zestaw, bez .git.

| Plik | Rozmiar | sha256 (12) | Co to jest |
|------|---------|-------------|------------|
| [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md) | 3362 B | `c280136a8d2f` | 4 METODY wdrozenia wg recenzji Piotra; agent sam wie co dalej - jedyna komenda: uzywaj |
| [LICENSE](LICENSE) | 1068 B | `a9d02f620ddf` | Licencja MIT, Copyright (c) 2026 Piotr (GAF) |
| [POGROMCA-KWIATKOW-DO-CZATU.md](POGROMCA-KWIATKOW-DO-CZATU.md) | 22043 B | `76ba3bed9cda` | JEDEN plik do wrzucenia na czat: polecenie dla agenta + pelny kod v8 (+ metoda wklejania) |
| [PogromcaKwiatkow.py](PogromcaKwiatkow.py) | 20024 B | `c7bcfe08f249` | NARZEDZIE (v8, PEWNIAK): skan / --selftest / --fix (naprawa literal-safe); stdlib, jeden plik |
| [README.md](README.md) | 6468 B | `82fbc969d3f4` | Strona startowa: po co jest, werdykty, szybki start, struktura, licencja (+ English summary) |
| [dev/fuzz-pogromcy.py](dev/fuzz-pogromcy.py) | 3407 B | `7a91b8a1e219` | Fuzz deterministyczny (A/B/C x 500, seed 49) |
| [dev/kwiatki-testy/ALCHEMIK-V1.json](dev/kwiatki-testy/ALCHEMIK-V1.json) | 6517 B | `d603b23504c7` | suita ALCHEMIK-V1: 30 wektorow (24 liczonych + 6 adnotacji) |
| [dev/kwiatki-testy/DEZYNFEKTOR-V1.json](dev/kwiatki-testy/DEZYNFEKTOR-V1.json) | 4320 B | `4ea8860a5d57` | suita DEZYNFEKTOR-V1: 30 wektorow (28 liczonych + 2 adnotacji) |
| [dev/kwiatki-testy/DRUKARZ-V1.json](dev/kwiatki-testy/DRUKARZ-V1.json) | 5872 B | `5ab4def2601e` | suita DRUKARZ-V1: 24 wektorow (21 liczonych + 3 adnotacji) |
| [dev/kwiatki-testy/EGZAMINATOR-V1.json](dev/kwiatki-testy/EGZAMINATOR-V1.json) | 5007 B | `51de2bd6bae1` | suita EGZAMINATOR-V1: 33 wektorow (30 liczonych + 3 adnotacji) |
| [dev/kwiatki-testy/EMOJI-V3.json](dev/kwiatki-testy/EMOJI-V3.json) | 4641 B | `4f813f55ed8b` | suita EMOJI-V3: 22 wektorow (22 liczonych + 0 adnotacji) |
| [dev/kwiatki-testy/KOMBINATOR-V1.json](dev/kwiatki-testy/KOMBINATOR-V1.json) | 4257 B | `b5b050c27e91` | suita KOMBINATOR-V1: 30 wektorow (30 liczonych + 0 adnotacji) |
| [dev/kwiatki-testy/KRAWEDZ-V1.json](dev/kwiatki-testy/KRAWEDZ-V1.json) | 7450 B | `c4f2cb91849b` | suita KRAWEDZ-V1: 30 wektorow (23 liczonych + 7 adnotacji) |
| [dev/kwiatki-testy/MYKLA-V1.json](dev/kwiatki-testy/MYKLA-V1.json) | 4263 B | `80b7dda9d875` | suita MYKLA-V1: 20 wektorow (19 liczonych + 1 adnotacji) |
| [dev/kwiatki-testy/OBIETNICA-V2.json](dev/kwiatki-testy/OBIETNICA-V2.json) | 8349 B | `45cdd907ce6c` | suita OBIETNICA-V2: 30 wektorow (13 liczonych + 17 adnotacji) |
| [dev/kwiatki-testy/PRALKA-V3.json](dev/kwiatki-testy/PRALKA-V3.json) | 5991 B | `0a8254555492` | suita PRALKA-V3: 30 wektorow (26 liczonych + 4 adnotacji) |
| [dev/kwiatki-testy/PROTOKOLANT-V1.json](dev/kwiatki-testy/PROTOKOLANT-V1.json) | 3814 B | `2ff823035f5c` | suita PROTOKOLANT-V1: 18 wektorow (16 liczonych + 2 adnotacji) |
| [dev/kwiatki-testy/PULAPKA-V1.json](dev/kwiatki-testy/PULAPKA-V1.json) | 5471 B | `49b9a40304db` | suita PULAPKA-V1: 20 wektorow (20 liczonych + 0 adnotacji) |
| [dev/kwiatki-testy/PUNKTATOR-V1.json](dev/kwiatki-testy/PUNKTATOR-V1.json) | 4669 B | `8b72d9fe9d38` | suita PUNKTATOR-V1: 24 wektorow (20 liczonych + 4 adnotacji) |
| [dev/kwiatki-testy/RECYKLER-V1.json](dev/kwiatki-testy/RECYKLER-V1.json) | 3810 B | `dd0dd5afb4ea` | suita RECYKLER-V1: 27 wektorow (26 liczonych + 1 adnotacji) |
| [dev/kwiatki-testy/SIEKIERNIK-V2.json](dev/kwiatki-testy/SIEKIERNIK-V2.json) | 5555 B | `49a23834a0be` | suita SIEKIERNIK-V2: 30 wektorow (30 liczonych + 0 adnotacji) |
| [dev/tor-pogromcy.py](dev/tor-pogromcy.py) | 3025 B | `79f199249ad5` | Turniej regresji: 15 suit -> FN/FP/SZUM, exit 1 przy wpadce |
| [docs/CERTYFIKAT-PEWNIAKA.md](docs/CERTYFIKAT-PEWNIAKA.md) | 2729 B | `3e368d5e0d20` | Certyfikat: droga v2->v7, serie 2/2, klauzula utrzymaniowa |
| [docs/KOMPLECIK.md](docs/KOMPLECIK.md) | - | - | TA LISTA (sam siebie nie hashuje :)) |
| [docs/RAPORT-TESTU-KWITNICA.md](docs/RAPORT-TESTU-KWITNICA.md) | 2946 B | `f6ce52c52bbd` | Raport Kwitnicy: 20 plikow CPythona, 100% przywroconych (jezyk ludzki) |
| [docs/RAPORT-V8-PETLA-BONUS.md](docs/RAPORT-V8-PETLA-BONUS.md) | 2969 B | `1e430f72cd06` | Raport v8: rundy 10-11 + KONSERWATOR 2.0 (nie-niszczenie kodu 8/8) |

## Najkrotsza droga uzytkownika

1. Nie znasz sie? -> [INSTRUKCJA-DLA-ZIELONYCH.md](../INSTRUKCJA-DLA-ZIELONYCH.md):
   4 metody (zalacznik .md, zalacznik .py, kopiuj-wklej, przez internet).
2. Chcesz rozumiec narzedzie? -> [../README.md](../README.md).
3. Nie wierzysz nam? -> [CERTYFIKAT-PEWNIAKA.md](CERTYFIKAT-PEWNIAKA.md),
   [RAPORT-V8-PETLA-BONUS.md](RAPORT-V8-PETLA-BONUS.md),
   [RAPORT-TESTU-KWITNICA.md](RAPORT-TESTU-KWITNICA.md) - albo odpal
   `python3 dev/tor-pogromcy.py` (oczekiwane: 348/0/0/0).

## Werdykt wydan (do reprodukcji)

- `python3 PogromcaKwiatkow.py --selftest` -> PASS
- `python3 dev/tor-pogromcy.py` -> trafione 348 | FN 0 | FP 0 | SZUM 0
- `python3 dev/fuzz-pogromcy.py` -> A/B/C po 500 OK, 0 FAIL

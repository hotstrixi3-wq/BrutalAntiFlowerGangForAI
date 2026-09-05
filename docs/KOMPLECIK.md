# KOMPLECIK - Brutal Anti-Flower Gang - manifest drzewa

Manifest AKTUALNEGO drzewa (generowany maszynowo; ten plik nie listuje samego
siebie). Zasada struktury (Piotr): KORZEN = tylko integracja agent+czlowiek;
dowody i infrastruktura -> docs/ i dev/. Manifest wydania v8.0.1 (26 plikow)
zostaje w historii gita tego pliku.

Aktualizacja v9.0.0: dziennik wielosesyjny - katalog dziennik/,
jeden plik na sesje, cudze tylko do odczytu (bramka --sprawdz),
prostowanie przez pole Zastepuje, widok scalony.

Poprzednio v8.9.0: sprawdz-teksty.py - bramka wykrywajaca ZYWE
homoglify w dokumentacji (agent wstawil 16 wlasnych w 3 dokumenty
ostrzegajace przed homoglifami; 17. wylapal user na czacie).

Poprzednio v8.8.0: PAMIETNIK-OPERATORA.md + pamietnik.py - pamiec
miedzy sesjami agentow (17 wpisow startowych w 5 sekcjach).

Poprzednio v8.7.0: turnieje T5 (Anihilator) i T6 (Prokurator),
kazdy zweryfikowany sabotazem; naprawa dwoch wad Prokuratora
wykrytych przez T6 (.py nigdy nie czyszczony, nie-UTF8 bez BLOKADY).

Poprzednio v8.6.0: naprawa luki f-string (kod wewnatrz pol {...} byl
chroniony jak dane), kwadratowego diffa (3m23s -> 0.137s) i dodanie
turnieju z kryterium WYKONANIA (dev/turnieje/turniej-4-runtime.py)
oraz dowodu luki (dev/luki/luka-fstring.py).

Poprzednio v8.5.0: bramka spojnosci wersji - WERSJE.json (jedno zrodlo
prawdy) + sprawdz-spojnosc.py (kod vs dokumentacja vs osadzone kopie w
RODZINIE). Patrz README. Poprzednio v8.3.0: wgrane nowsze wersje calej rodziny (Pogromca v8.4.0,
Zaglada v1.3.0, Prokurator v1.2.0, Anihilator v1.3.0) - patrz README
Historia zmian. RODZINA-DO-CZATU re-embedowana bajt-w-bajt (4/4).
Poprzednio v8.2.21: PORZADKI W DRZEWIE. Korzen zawieral rownolegly,
zduplikowany komplet plikow obok docs/ i dev/ (14 dokumentow, 15 plikow
amunicji JSON, 9 narzedzi testowych, 2 logi - wszystkie bit-w-bit identyczne
z kopiami docelowymi albo NOWSZE od nich). Rozwiazanie: nowsze wersje
dokumentow przeniesione do docs/ (zachowana tresc z korzenia, bo byla
swiezsza - v8.1.0/v1.1.1 zamiast v8.0.3/v1.0.9), duplikaty bit-w-bit
usuniete, SUMA-KONTROLNA-TESTOW.py przeniesiona do dev/turnieje/ (tam ja
deklarowal manifest i README). Usuniety plik-smiec `download` (przypadkowa
kopia .gitignore). Kod rodziny NIE RUSZONY - 4/4 selftesty PASS, bramka
Pogromcy na korzeniu+docs: BLAD 0, audyt linkow: 49/49 zywych.
Poprzednia aktualizacja v8.2.20: PogromcaKwiatkow.py -> v8.1.0 (warstwa
raportu RYZYKO-KLUCZA - patrz README Historia zmian).

## Korzen (11 plikow) - narzedzia i start

| Plik | Rozmiar | sha256 (12) |
|---|---|---|
| [.gitignore](../.gitignore) | 41 B | `02dc02bcbbd3` |
| [AnihilatorChwastow.py](../AnihilatorChwastow.py) | 26099 B | `ed6ff4ec9dcf` |
| [CZYM-JEST-GANG.md](../CZYM-JEST-GANG.md) | 7686 B | `c5c0e4cc9008` |
| [LICENSE](../LICENSE) | 1068 B | `a9d02f620ddf` |
| [PAMIETNIK-OPERATORA.md](../PAMIETNIK-OPERATORA.md) | 11801 B | `58446356a90c` |
| [PROTOKOL-OPERATORA.md](../PROTOKOL-OPERATORA.md) | 9401 B | `9aa5cfadb62a` |
| [PogromcaKwiatkow.py](../PogromcaKwiatkow.py) | 40633 B | `4a978336c4c6` |
| [ProkuratorOgrodnik.py](../ProkuratorOgrodnik.py) | 21215 B | `be70cca0dda5` |
| [README.md](../README.md) | 42459 B | `0fe8f9e8c520` |
| [SZYBKI-START-DLA-AGENTA.md](../SZYBKI-START-DLA-AGENTA.md) | 2708 B | `2db6da9c543d` |
| [WERSJE.json](../WERSJE.json) | 781 B | `1a7289d8d4e6` |
| [ZagladaKultury.py](../ZagladaKultury.py) | 32036 B | `3d7a1bbe0fe0` |
| [fuzz-pogromcy.py](../dev/fuzz-pogromcy.py) | 4050 B | `9a9b989344b6` |
| [ALCHEMIK-V1.json](../dev/kwiatki-testy/ALCHEMIK-V1.json) | 6517 B | `d603b23504c7` |
| [DEZYNFEKTOR-V1.json](../dev/kwiatki-testy/DEZYNFEKTOR-V1.json) | 4320 B | `4ea8860a5d57` |
| [DRUKARZ-V1.json](../dev/kwiatki-testy/DRUKARZ-V1.json) | 5872 B | `5ab4def2601e` |
| [EGZAMINATOR-V1.json](../dev/kwiatki-testy/EGZAMINATOR-V1.json) | 5007 B | `51de2bd6bae1` |
| [EMOJI-V3.json](../dev/kwiatki-testy/EMOJI-V3.json) | 4641 B | `4f813f55ed8b` |
| [KOMBINATOR-V1.json](../dev/kwiatki-testy/KOMBINATOR-V1.json) | 4257 B | `b5b050c27e91` |
| [KRAWEDZ-V1.json](../dev/kwiatki-testy/KRAWEDZ-V1.json) | 7450 B | `c4f2cb91849b` |
| [MYKLA-V1.json](../dev/kwiatki-testy/MYKLA-V1.json) | 4263 B | `80b7dda9d875` |
| [OBIETNICA-V2.json](../dev/kwiatki-testy/OBIETNICA-V2.json) | 8349 B | `45cdd907ce6c` |
| [PRALKA-V3.json](../dev/kwiatki-testy/PRALKA-V3.json) | 5991 B | `0a8254555492` |
| [PROTOKOLANT-V1.json](../dev/kwiatki-testy/PROTOKOLANT-V1.json) | 3814 B | `2ff823035f5c` |
| [PULAPKA-V1.json](../dev/kwiatki-testy/PULAPKA-V1.json) | 5471 B | `49b9a40304db` |
| [PUNKTATOR-V1.json](../dev/kwiatki-testy/PUNKTATOR-V1.json) | 4669 B | `8b72d9fe9d38` |
| [RECYKLER-V1.json](../dev/kwiatki-testy/RECYKLER-V1.json) | 3810 B | `dd0dd5afb4ea` |
| [SIEKIERNIK-V2.json](../dev/kwiatki-testy/SIEKIERNIK-V2.json) | 5555 B | `49a23834a0be` |
| [luka-fstring.py](../dev/luki/luka-fstring.py) | 2385 B | `8d5dc9ef83dd` |
| [tor-pogromcy.py](../dev/tor-pogromcy.py) | 3108 B | `d23a0e6338a8` |
| [SUMA-KONTROLNA-TESTOW.py](../dev/turnieje/SUMA-KONTROLNA-TESTOW.py) | 5428 B | `7c7478a78a53` |
| [petla-rodzinna.py](../dev/turnieje/petla-rodzinna.py) | 2943 B | `8b19d509c12b` |
| [petla-turniejowa.py](../dev/turnieje/petla-turniejowa.py) | 3080 B | `fadabe3ecf1c` |
| [turniej-2-sprawdzajacy.py](../dev/turnieje/turniej-2-sprawdzajacy.py) | 11234 B | `629b0ccd62f6` |
| [turniej-3-niepsucie.py](../dev/turnieje/turniej-3-niepsucie.py) | 9138 B | `3c0551b2aac6` |
| [turniej-4-runtime.py](../dev/turnieje/turniej-4-runtime.py) | 7019 B | `5fca285e7973` |
| [turniej-5-anihilator.py](../dev/turnieje/turniej-5-anihilator.py) | 16082 B | `fd493b6bcb3f` |
| [turniej-6-prokurator.py](../dev/turnieje/turniej-6-prokurator.py) | 11542 B | `ca4ecbe409d6` |
| [turniej-7-zwiad.py](../dev/turnieje/turniej-7-zwiad.py) | 15511 B | `de8941a76842` |
| [turniej-niezalezny.py](../dev/turnieje/turniej-niezalezny.py) | 18844 B | `d41e6aaeb539` |
| [zaglada-turniej-niepsucie.py](../dev/turnieje/zaglada-turniej-niepsucie.py) | 9094 B | `44eb2e1f1b63` |
| [zaglada-turniej-wykrywania.py](../dev/turnieje/zaglada-turniej-wykrywania.py) | 11617 B | `41865b03e7d6` |
| [AUDYT-POWIAZAN-FUNKCJI.md](AUDYT-POWIAZAN-FUNKCJI.md) | 6566 B | `9ff5ef1e77a4` |
| [BRIEF-DLA-AUDYTORA.md](BRIEF-DLA-AUDYTORA.md) | 8330 B | `8691dd6c1159` |
| [CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.0.9.md](CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.0.9.md) | 3308 B | `723c364c544a` |
| [CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.1.0.md](CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.1.0.md) | 4138 B | `14915c56259b` |
| [CERTYFIKAT-PEWNIAKA.md](CERTYFIKAT-PEWNIAKA.md) | 5254 B | `3da46a37655b` |
| [CERTYFIKAT-PRZYDATNOSCI-ARENA.md](CERTYFIKAT-PRZYDATNOSCI-ARENA.md) | 5748 B | `d4d622ae73a6` |
| [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md) | 4330 B | `11cd6f64a713` |
| [INZYNIERIA-WSTECZNA.md](INZYNIERIA-WSTECZNA.md) | 10540 B | `5bc6e5fc09dc` |
| [LUKI-W-TESTACH.md](LUKI-W-TESTACH.md) | 7415 B | `94b7f5a29b33` |
| [MEDAL-PEWNIAKA-v8.0.2.md](MEDAL-PEWNIAKA-v8.0.2.md) | 3299 B | `48e80707f51a` |
| [MEDAL-ZAGLADY-v1.0.3.md](MEDAL-ZAGLADY-v1.0.3.md) | 5570 B | `38bf39d89c2f` |
| [NAPRAWA-v8.6.0.md](NAPRAWA-v8.6.0.md) | 7619 B | `656efd87728d` |
| [RAPORT-TESTU-KWITNICA.md](RAPORT-TESTU-KWITNICA.md) | 5806 B | `d661cbf505a2` |
| [RAPORT-TURNIEJU-NIEZALEZNEGO.md](RAPORT-TURNIEJU-NIEZALEZNEGO.md) | 12458 B | `1d88ab4f90e5` |
| [RAPORT-V8-PETLA-BONUS.md](RAPORT-V8-PETLA-BONUS.md) | 3668 B | `721c8bd31222` |
| [README-TURNIEJ.md](README-TURNIEJ.md) | 5604 B | `ff64338e4579` |
| [RODZINA-DO-CZATU.md](RODZINA-DO-CZATU.md) | 127160 B | `40dd060b85aa` |
| [2026-09-05__claude-pro-sprawdz-spojnosc.md](audyt-zewnetrzny/2026-09-05__claude-pro-sprawdz-spojnosc.md) | 5217 B | `e94a84ed7b8f` |
| [README.md](audyt-zewnetrzny/README.md) | 1447 B | `2626f2b20aac` |
| [petla-rodzinna.log](logi/petla-rodzinna.log) | 8271 B | `39d9717915cb` |
| [petla-turniejowa.log](logi/petla-turniejowa.log) | 6133 B | `fa9bd1d813b4` |
| [wniosek_publiczny_do_redakcji.md](wniosek_publiczny_do_redakcji.md) | 7242 B | `29e118e684cd` |
| [2026-09-04__01a06e18.md](../dziennik/2026-09-04__01a06e18.md) | 31374 B | `085e3b56daaf` |
| [README.md](../dziennik/README.md) | 2685 B | `cbb1fce69cef` |
| [pamietnik.py](../pamietnik.py) | 19928 B | `2a6a8d3d2553` |
| [sprawdz-spojnosc.py](../sprawdz-spojnosc.py) | 10060 B | `a3305dffc950` |
| [sprawdz-teksty.py](../sprawdz-teksty.py) | 4512 B | `a2599bd2d033` |
| [zwiad.py](../zwiad.py) | 23269 B | `9e711f1a497c` |

Lacznie w drzewie: 52 plikow (+ ten manifest). Bramka wydania (korzen + docs):
BLAD 0. Zip wydania: Releases (SHA powyzej = kontrola integralnosci po pobraniu).

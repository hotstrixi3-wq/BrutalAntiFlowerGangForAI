# KOMPLECIK - Brutal Anti-Flower Gang - manifest drzewa

Manifest AKTUALNEGO drzewa (generowany maszynowo; ten plik nie listuje samego
siebie). Zasada struktury (Piotr): KORZEN = tylko integracja agent+czlowiek;
dowody i infrastruktura -> docs/ i dev/. Manifest wydania v8.0.1 (26 plikow)
zostaje w historii gita tego pliku.

Aktualizacja v8.5.0: bramka spojnosci wersji - WERSJE.json (jedno zrodlo
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
| [AnihilatorChwastow.py](../AnihilatorChwastow.py) | 24692 B | `66d9e80041e1` |
| [LICENSE](../LICENSE) | 1068 B | `a9d02f620ddf` |
| [PROTOKOL-OPERATORA.md](../PROTOKOL-OPERATORA.md) | 4780 B | `5d9388a7d660` |
| [PogromcaKwiatkow.py](../PogromcaKwiatkow.py) | 34722 B | `f03241c25169` |
| [ProkuratorOgrodnik.py](../ProkuratorOgrodnik.py) | 17049 B | `6bbb0c13f521` |
| [README.md](../README.md) | 25602 B | `fd9004bb0471` |
| [WERSJE.json](../WERSJE.json) | 781 B | `1d8b7b67dca7` |
| [sprawdz-spojnosc.py](../sprawdz-spojnosc.py) | 10060 B | `a3305dffc950` |
| [SZYBKI-START-DLA-AGENTA.md](../SZYBKI-START-DLA-AGENTA.md) | 1910 B | `7b14e4f9740a` |
| [ZagladaKultury.py](../ZagladaKultury.py) | 26220 B | `78564f1ec63a` |

## docs/ (17 plikow, bez tego manifestu) - dokumenty i dowody

| Plik | Rozmiar | sha256 (12) |
|---|---|---|
| [CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.0.9.md](CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.0.9.md) | 3308 B | `723c364c544a` |
| [CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.1.0.md](CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.1.0.md) | 4138 B | `14915c56259b` |
| [AUDYT-POWIAZAN-FUNKCJI.md](AUDYT-POWIAZAN-FUNKCJI.md) | 6566 B | `9ff5ef1e77a4` |
| [CERTYFIKAT-PEWNIAKA.md](CERTYFIKAT-PEWNIAKA.md) | 5254 B | `3da46a37655b` |
| [CERTYFIKAT-PRZYDATNOSCI-ARENA.md](CERTYFIKAT-PRZYDATNOSCI-ARENA.md) | 5748 B | `d4d622ae73a6` |
| [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md) | 4330 B | `11cd6f64a713` |
| [MEDAL-PEWNIAKA-v8.0.2.md](MEDAL-PEWNIAKA-v8.0.2.md) | 3299 B | `48e80707f51a` |
| [MEDAL-ZAGLADY-v1.0.3.md](MEDAL-ZAGLADY-v1.0.3.md) | 5570 B | `38bf39d89c2f` |
| [RAPORT-TESTU-KWITNICA.md](RAPORT-TESTU-KWITNICA.md) | 5806 B | `d661cbf505a2` |
| [RAPORT-TURNIEJU-NIEZALEZNEGO.md](RAPORT-TURNIEJU-NIEZALEZNEGO.md) | 12458 B | `1d88ab4f90e5` |
| [RAPORT-V8-PETLA-BONUS.md](RAPORT-V8-PETLA-BONUS.md) | 3668 B | `721c8bd31222` |
| [README-TURNIEJ.md](README-TURNIEJ.md) | 5604 B | `4405d8107f62` |
| [RODZINA-DO-CZATU.md](RODZINA-DO-CZATU.md) | 109860 B | `88ddc7874d51` |
| [wniosek_publiczny_do_redakcji.md](wniosek_publiczny_do_redakcji.md) | 7242 B | `80e9da2c0fc7` |
| [petla-rodzinna.log](logi/petla-rodzinna.log) | 8271 B | `39d9717915cb` |
| [petla-turniejowa.log](logi/petla-turniejowa.log) | 6133 B | `fa9bd1d813b4` |

## dev/ (25 plikow) - amunicja i narzedzia testowe (CELOWO BRUDNE - poza bramka wydania)

| Plik | Rozmiar | sha256 (12) |
|---|---|---|
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
| [tor-pogromcy.py](../dev/tor-pogromcy.py) | 3108 B | `d23a0e6338a8` |
| [SUMA-KONTROLNA-TESTOW.py](../dev/turnieje/SUMA-KONTROLNA-TESTOW.py) | 5428 B | `7c7478a78a53` |
| [petla-rodzinna.py](../dev/turnieje/petla-rodzinna.py) | 2943 B | `8b19d509c12b` |
| [petla-turniejowa.py](../dev/turnieje/petla-turniejowa.py) | 3080 B | `fadabe3ecf1c` |
| [turniej-2-sprawdzajacy.py](../dev/turnieje/turniej-2-sprawdzajacy.py) | 11234 B | `629b0ccd62f6` |
| [turniej-3-niepsucie.py](../dev/turnieje/turniej-3-niepsucie.py) | 9138 B | `3c0551b2aac6` |
| [turniej-niezalezny.py](../dev/turnieje/turniej-niezalezny.py) | 18844 B | `d41e6aaeb539` |
| [zaglada-turniej-niepsucie.py](../dev/turnieje/zaglada-turniej-niepsucie.py) | 9094 B | `44eb2e1f1b63` |
| [zaglada-turniej-wykrywania.py](../dev/turnieje/zaglada-turniej-wykrywania.py) | 11617 B | `41865b03e7d6` |

Lacznie w drzewie: 52 plikow (+ ten manifest). Bramka wydania (korzen + docs):
BLAD 0. Zip wydania: Releases (SHA powyzej = kontrola integralnosci po pobraniu).

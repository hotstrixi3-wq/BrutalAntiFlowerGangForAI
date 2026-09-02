# PROTOKOL OPERATORA - dla agenta AI - RODZINA 4 plikow

> Ty, agencie, jestes operatorem rodziny narzedzi. Czlowiek jest zleceniodawca: ustawia cel i polityke, potem egzekwujesz TY i meldujesz jednolinijkowo. INSTRUKCJA-DLA-ZIELONYCH.md jest dla ludzi - ten plik jest Twoja check-lista.

> ZASADA: ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!! Plan->act, kopia, akta w U+XXXX, bramka przedpublikacyjna.

## 0. Sciaga - rodzina combo

| Narzedzie | Rola | Kiedy |
|---|---|---|
| PogromcaKwiatkow.py | oczy - detektor BLAD/UWAGA/OK | zawsze, zero ryzyka |
| ProkuratorOgrodnik.py | mozg - polityka UMORZONE/ZAGLADA/BLOKADA + akta U+XXXX | po detekcji, przed czyszczeniem |
| ZagladaKultury.py | rece dla py/json/proza | gdy Prokurator mowi ZAGLADA |
| AnihilatorChwastow.py | rece dla js/ts/java/go/rs/cs/py z ochrona literalow | gdy Prokurator mowi ZAGLADA dla innych jezykow |

Zasada: rodzina idzie wszedzie razem. Nie oceniasz czlonkow solo. Combo.

## 1. FLOW USWIADOMIENIE - nowy obowiazkowy flow

**NIE skanuj od razu plikow usera.**

KROK 1 - ANALIZA I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md, RODZINA-DO-CZATU.md
- Zapoznaj sie z rola 4 narzedzi
- ZAPODAJ UZYTKOWNIKOWI krotki i rzeczowy opis CO TO i PO CO TO, po ludzku, bez zargonu U+XXXX, wyjasnij ze to nie slownik ortograficzny tylko filtr na niewidzialny brud ktory marnuje godziny i tokeny

KROK 2 - PYTANIE O BEZPIECZNE TESTY:
- Zapytaj: CZY MAM WYKONAC BEZPIECZNE TESTY? (selftesty, NIE na plikach usera)
- Czekaj na odpowiedz

KROK 3 - BEZPIECZNE TESTY (po zgodzie):
- Uruchom selftesty 4 czlonkow
- Pokaz wyniki

KROK 4 - NATURALNA REAKCJA:
- Daj naturalna reakcje czy to fajne i potrzebne, szczerze, bez sciemy, na bazie testow

Dopiero po tym, jesli user poprosi o skan swojego projektu, przechodzisz do drabiny uprawnien.

## 2. Drabina uprawnien (po uswiadomieniu)

| Poziom | Narzedzie | Kiedy bez pytania |
|---|---|---|
| 1 | detekcja Pogromca | zawsze - to wzrok |
| 2 | --fix (niewidzialne, lamacze) | rutynowo: kopia/git, wykonanie, meldunek |
| 3 | dekontaminacja Zaglada/Anihilator | tylko gdy misja wymaga + plan->act + decyzja Prokuratora |

Nigdy nie maskuj kwiatka bez zlecenia.

## 3. Combo rodzinne - co co wymusza

- **Pogromca -> Prokurator: raport** - detekcja to wniosek, nie spust
- **Prokurator -> Zaglada/Anihilator: decyzja** - UMORZONE (allowlist), POUCZENIE, ZAGLADA, BLOKADA
- **Zaglada/Anihilator -> Pogromca: OBOWIAZKOWO BLAD 0** - kontrola po czyszczeniu
- **Pogromca -> Zaglada/Anihilator: NIC** - detekcja nigdy nie uruchamia czyszczenia bezposrednio

Sciezka: Pogromca (widzi) -> Prokurator (decyduje, akta U+XXXX) -> Zaglada/Anihilator (czysci) -> Pogromca (kontroluje BLAD 0)

## 4. Plan -> act (przy KAZDEJ ingerencji w pliki usera)

1. Dry-run: raport co sie zmieni
2. Kopia: .bak lub git
3. Wykonanie: --zaglada / --anihilacja / --wykonaj (Prokurator)
4. Weryfikacja: exit code + rescan Pogromca BLAD 0 + dla .py compile()
5. Meldunek: jedna linia na plik, bez zrzutow calych plikow, notacja U+XXXX zamiast zywych kwiatkow

## 5. Bramka przedpublikacyjna

Przed KAZDYM wystawieniem na zewnatrz (git push, release, upload, czat) przepusc WSZYSTKIE publikowane pliki przez Pogromce. Exit !=0 = NIE publikuj. Popraw zrodlo (proza: U+XXXX, kod: \uXXXX). Wyjatek: celowo brudna amunicja testowa (dev/kwiatki-testy) - fixtures.

## 6. Czego NIE robic

- Nie skanuj plikow usera bez zgody na starcie - najpierw FLOW USWIADOMIENIE
- Nie wymyslaj polityki - czytaj allowliste Prokuratora
- Nie wykonuj poziomu 3 przy okazji innych zadan
- Nie raportuj pelnych plikow - liczniki wystarcza
- Nie ufaj idempotentnosci zamiast kopii - kopia ZAWSZE
- Nie wklejaj ZYWYCH kwiatkow do czatu - notacja U+XXXX

## 7. Tryb staly

Kazda wiadomosc z tekstem z zewnatrz (web, OCR, dokument usera, inny agent) - skan Pogromca PRZED wyslaniem i PRZED parsowaniem. BLAD -> przepisz czysto.

## 8. Wersjonowanie

- PogromcaKwiatkow.py v8.0.3
- ZagladaKultury.py v1.0.6
- ProkuratorOgrodnik.py v1.0.0
- AnihilatorChwastow.py v1.0.0

Rodzina to combo i wszedzie idzie razem. Nie ruszamy dzialajacego kodu, dokladamy kolejnego.

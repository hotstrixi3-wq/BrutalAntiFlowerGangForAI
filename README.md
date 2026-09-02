# Brutal Anti-Flower Gang for AI (Brutalny Gang Antykwiatkowy - rodzina Pogromcy Kwiatkow)

> MOTTO: "uzywaj bo dzieki PogromcyKwiatkow nie mielisz potencjalnie BRUDNEGO kodu, co marnuje nie milisekundy a godziny mielenia kodu i tony potencjalnych tokenow jesli korzystasz z pomocy innych Agentow AI. Krecenie sie w kolko z BRUDNYM kodem to strata czasu" -- Piotr (GAF)

> ZASADA: ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!!

## Co to jest, po ludzku

To nie slownik ortograficzny. Nie poprawia "blad" na "błąd".

To filtr na niewidzialny brud i obcy alfabet ktory AI wstawia niezauwazalnie i nie zdaje sobie z tego sprawy w momencie w ktorym to czyni ani pozniej:
- cyrylica wygladajaca jak lacina: rosyjskie "a" U+0430 zamiast polskiego "a"
- zero-width space U+200B psujacy JSON i autoryzacje
- NBSP U+00A0 psujacy .env
- lamacz linii U+2028 psujacy JS

Ty tego nie widzisz. Kompilator wywala blad. Szukasz godzinami. Marnujesz tony tokenow. Prawda jest niewidoczna, wszedzie kwiatki i chwasty.

## Rodzina - 4 pliki ktore ida wszedzie razem

- **PogromcaKwiatkow.py v8.0.3** - oczy, detektor BLAD/UWAGA/OK
- **ZagladaKultury.py v1.0.7** - rece dla py/json/proza, dekontaminator z ochrona literalow py (+ ostrzezenia o nieprzywroconej parsowalnosci)
- **ProkuratorOgrodnik.py v1.0.1** - mozg, polityka UMORZONE/POUCZENIE/ZAGLADA/BLOKADA + akta w U+XXXX (od v1.0.1 faktycznie czyste)
- **AnihilatorChwastow.py v1.0.0** - rece dla js/ts/java/go/rs/cs/py/json/md z ochrona literalow

Zasada: nie ruszamy dzialajacego kodu, dokladamy kolejnego. Rodzina to combo i wszedzie idzie razem.

## Szybki start - FLOW USWIADOMIENIE

Nie skanuj od razu plikow usera. Najpierw analiza i uswiadomienie.

### Dla agenta AI - wiadomosc do skopiowania:

```
Hej! W zalaczonym pliku docs/RODZINA-DO-CZATU.md masz rodzine Pogromcy - combo 4 plikow.

KROK 1 - ANALIZA I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md
- Pobierz 4 narzedzia: PogromcaKwiatkow.py, ZagladaKultury.py, ProkuratorOgrodnik.py, AnihilatorChwastow.py
- Zapoznaj sie z rola i ZAPODAJ MI krotki i rzeczowy opis CO TO i PO CO TO, po ludzku, bez zargonu U+XXXX

KROK 2 - PYTANIE:
- Zapytaj: CZY MAM WYKONAC BEZPIECZNE TESTY? (selftesty, NIE na moich plikach)

KROK 3 - TESTY (po zgodzie):
- python3 PogromcaKwiatkow.py --selftest
- python3 ZagladaKultury.py --selftest
- python3 ProkuratorOgrodnik.py --selftest
- python3 AnihilatorChwastow.py --selftest

KROK 4 - REAKCJA:
- Daj naturalna reakcje czy to fajne i potrzebne, szczerze, bez sciemy.
```

### Dla czlowieka:

1. Pobierz docs/RODZINA-DO-CZATU.md (zawiera 4 kody w srodku) lub wydanie ZIP z Releases
2. Zalacz do czatu z agentem
3. Wklej wiadomosc z sekcji FLOW USWIADOMIENIE z docs/RODZINA-DO-CZATU.md

## Struktura paczki czystej

```
PogromcaKwiatkow.py          detektor
ZagladaKultury.py            dekontaminator py/json/proza
ProkuratorOgrodnik.py        polityka + akta
AnihilatorChwastow.py        anihilator uniwersalny z ochrona literalow
PROTOKOL-OPERATORA.md        regulamin dla agenta
README.md                    ten plik
LICENSE                      MIT
docs/                        RODZINA-DO-CZATU (all-in-one + FLOW), INSTRUKCJA-DLA-ZIELONYCH, wniosek, certyfikaty
dev/                         amunicja i narzedzia testowe (celowo brudne - poza bramka wydania)
```

Root + docs: kazdy BLAD 0, selftesty PASS. Zero zaleznosci, czysty Python 3 stdlib.

## Co to NIE jest

- Nie jest spell-checkerem - klasyfikuje znaki, nie slowa
- Nie jest langdetectem - widzi glify, nie jezyk
- Nie jest poprawiaczem ortografii - pilnuje alfabetow, nie bledow

## Historia zmian

- v8.2.8 - README mowi prawde o rodzinie w pelni (zlecenie Magusa, znaleziska
  1a/1b z relektury PROTOKOLU): Anihilator obejmuje tez py/json/md (zgadza
  sie z dokstringiem narzedzia i PROTOKOL 0; wczesniej README zanizal);
  Prokurator: pelna lista werdykow z POUCZENIE (UWAGA).

- v8.2.7 - kanon zasady bakapu: zdanie zasady konczy sie na "!!!"; usuniety
  doklejony tekst po wykrzyknikach z README, PROTOKOLU i RODZINY (wzor:
  INSTRUKCJA, ktora miala dobrze); wniosek: spacja przed "!!!" usunieta.
  Kwiatek editorialny zywy w 3 dokumentach przeszedl cisty przez skaner
  bajtow (BLAD 0) i przez przeglad osobisty - widzial go tylko Magus.
  Naprawa linkow w KOMPLECIK: 45 linkow bylo wzglednych do roota przy
  pliku w docs/ (na GitHub kazdy = 404); przepisane wzgledem katalogu
  pliku; audyt wszystkich .md: 0 zerwanych.

- v8.2.6 - zgodnosc dokumentow z rodzina: wersje w PROTOKOL §8 i w wniosku
  (byly v1.0.6/v1.0.0), sciezka INSTRUKCJI w PROTOKOL §0, precyzja sciezki
  w INSTRUKCJI METODA 1. Przeglad osobisty: 46/46 plikow; infrastruktura dev
  zielona (T1/T2/T3/Z1/Z2) oprocz wstepnie czerwonego fuzz-C (patrz dev/).

- v8.2.5 - higiena: usuniety z gita wyciek __pycache__/*.pyc (znany wektor,
  dodany .gitignore); KOMPLECIK nie listuje juz samego siebie (paradoks
  wlasnego skrotu); manifest zgodny z drzewem w 100 procentach.

- v8.2.4 - KOMPLECIK przelozony na manifest aktualnego drzewa (45 plikow, sha256);
  poprzedni (v8.0.1) mial 26 zerwanych linkow - zostaje w historii gita.

- v8.2.3 - rename na BrutalAntiFlowerGangForAI + MOTTO (opis repo): Pogromca i
  Zaglada zastapieni marka "the Brutal Anti-Flower Gang"; URL-e w zywych
  dokumentach, tytul README z linia EN. Stare URL-e przekierowuja (301).

- v8.2.2 - sync all-in-one: docs/RODZINA-DO-CZATU.md dostal aktualne kody rodziny
  (Prokurator v1.0.1, Zaglada v1.0.7 - wczesniej osadzone kopie v1.0.0/v1.0.6);
  URL-e w INSTRUKCJI-DLA-ZIELONYCH; KOMPLECIK oznaczony jako stan historyczny v8.0.1.

- v8.2.1 - domkniecie README po reorganizacji: wersje rodziny (Prokurator v1.0.1,
  Zaglada v1.0.7), naprawiona struktura (podwojny prefiks docs/docs, martwy link
  zip), swieze URL-e w zywych dokumentach docs/.
- v8.2.0 - reorganizacja repo i zmiana nazwy na BrutalnyGangAntyKwiatkowyDlaAI
  (MOTTO w opisie bez zmian): narzedzia rodziny zostaja na root, dokumenty w docs/,
  dev/ = amunicja testowa.
- v8.1.8 - Prokurator v1.0.1: akta w notacji U+XXXX (0 zywych znakow, werdykty
  niezmienione; wykryte testem 50 kodow). Zaglada v1.0.7: [OSTRZEZENIE] o
  nieprzywroconej parsowalnosci po --zaglada (exit bez zmian).
- v8.1.7 - pelna anglicyzacja wydania, kasacja starszych wydAN i tagow.

## Licencja

MIT - patrz LICENSE. 100% darmowe dla ludzi, firm i agentow AI.

Repo: https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI

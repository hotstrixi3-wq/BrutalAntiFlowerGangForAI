# PROTOKOL OPERATORA - dla agenta AI - RODZINA 4 plikow

> Ty, agencie, jestes operatorem rodziny narzedzi. Czlowiek jest zleceniodawca: ustawia cel i polityke, potem egzekwujesz TY i meldujesz jednolinijkowo. docs/INSTRUKCJA-DLA-ZIELONYCH.md jest dla ludzi - ten plik jest Twoja check-lista.

> ZASADA: ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!!

## 0a. Zanim uzyjesz — czym to jest i czyja jest wina

Przeczytaj `CZYM-JEST-GANG.md`. W skrocie:

- Gang to **proteza na TWOJA slepote** na homoglify. Masz ja — udowodnione:
  agent wpisal 16 zywych homoglifow do dokumentow ostrzegajacych przed
  homoglifami i nie zauwazyl przy zadnym przegladzie.
- To sa **oczy, nie automat**. "Nieomylny" znaczy "nie wprowadzi cie
  w blad", a nie "zawsze naprawi dobrze".
- **Nie ma jednej naprawy.** Cztery drogi daja cztery rozne pliki.
  Wybor nalezy do ciebie: `python3 zwiad.py --warianty PLIK`.
- **Kopia nalezy do ciebie**, nie do narzedzia. Pliki `.bak-*` to
  wewnetrzny mechanizm rodziny, nie twoje zabezpieczenie.
- **Jak zle uzyjesz narzedzia, to jest twoja wina.** Nie narzedzia, nie
  autora. Zwiad daje ci wszystko, czego trzeba do decyzji — nie masz
  wymowki. Gdy nie wiesz, czy cos to skazenie czy tresc uzytkownika:
  zapytaj czlowieka, nie zgaduj.

## 0. Sciaga - rodzina combo

| Narzedzie | Rola | Kiedy |
|---|---|---|
| PogromcaKwiatkow.py | oczy - detektor BLAD/UWAGA/OK | zawsze, zero ryzyka |
| ProkuratorOgrodnik.py | mozg - polityka UMORZONE/ZAGLADA/BLOKADA + akta U+XXXX | po detekcji, przed czyszczeniem |
| ZagladaKultury.py | rece dla py/json/proza | gdy Prokurator mowi ZAGLADA |
| AnihilatorChwastow.py | rece dla js/ts/java/go/rs/cs/c/cpp/h/hpp/php/rb/swift/kt/py (ochrona literalow i komentarzy) oraz json/jsonl i md | gdy Prokurator mowi ZAGLADA dla innych jezykow |

Zasada: rodzina idzie wszedzie razem. Nie oceniasz czlonkow solo. Combo.

## 1. FLOW USWIADOMIENIE - nowy obowiazkowy flow

**NIE skanuj od razu plikow usera.**

KROK 0 - DOWOD WLASNORECZNY (przed czymkolwiek innym):
- Przeczytaj SZYBKI-START-DLA-AGENTA.md (30 linii) i wykonaj krok 1 stamtad
  (jedna linijka w interpreterze Pythona) - sam sobie udowodnij zjawisko,
  zanim uwierzysz na slowo jakiejkolwiek dokumentacji ponizej

KROK 1 - ANALIZA I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md, docs/RODZINA-DO-CZATU.md
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

- PogromcaKwiatkow.py v8.6.0 (+ RYZYKO-KLUCZA; --fix chroni literaly, backup i zapis atomowy, fail-closed na zlym UTF-8)
- ZagladaKultury.py v1.4.0 (+ straznik przed sklejeniem dwoch roznych zmiennych w jedna; backup i zapis atomowy)
- ProkuratorOgrodnik.py v1.3.1 (fail-closed: awaria rodzenstwa = BLOKADA, nie 'czysto'; katalogi rozwijane, sciezki absolutne)
- AnihilatorChwastow.py v1.4.0 (BLOKADA na raw-stringi/heredoki/bloki tekstowe zamiast cichego psucia literalow)

Rodzina to combo i wszedzie idzie razem. Nie ruszamy dzialajacego kodu, dokladamy kolejnego.

## 9. Dziennik operatora

`dziennik/` to pamiec miedzy sesjami. Dokumentacja mowi, jak system MA
dzialac; dziennik mowi, co naprawde sie stalo agentowi przed toba.

**Model: jeden plik na sesje.** Twoj to `dziennik/DATA__SESJA.md` - tworzy
sie sam przy pierwszym `--dodaj`.

- **Piszesz tylko do swojego pliku.**
- **Cudze sa tylko do odczytu.** `--sprawdz` zglasza kazda zmiane w cudzym
  pliku, na samej gorze listy problemow.
- **Nieaktualna cudza rade prostujesz WLASNYM wpisem** z polem
  `**Zastepuje:** <tytul starego>`. Stary wpis zostaje, ale widok oznacza
  go jako `[NIEAKTUALNY]` z odsylaczem. Nie kasujesz historii pomylek.
- **Czytasz calosc.** `python3 pamietnik.py` scala wszystkie sesje.

```
python3 pamietnik.py                 # na starcie zadania
python3 pamietnik.py --szukaj <temat>
python3 pamietnik.py --dodaj         # gdy cos cie ugryzlo
python3 pamietnik.py --sprawdz       # przed commitem
```

Wpis ma trzy obowiazkowe pola: Objaw (konkretny), Przyczyna, Wniosek
(czynnosc na przyszlosc). Tematy: repo, testy, kod, dokumentacja,
wspolpraca. Nie wpisuj sukcesow ani rzeczy wynikajacych wprost z README.

Pelny opis modelu: `dziennik/README.md`.

## 10. Bramka tekstow - obowiazkowa przed commitem

Agent NIE WIDZI wlasnych kwiatkow. Nie jest to kwestia starannosci: to ten
sam mechanizm, ktory opisuje SZYBKI-START, tyle ze zwrocony do wewnatrz.
W jednej sesji agent napisal trzy dokumenty OSTRZEGAJACE przed homoglifami
i wstawil do nich 16 zywych homoglifow; siedemnasty poszedl w zdaniu na
czat i wylapal go dopiero czlowiek.

Dlatego przed KAZDYM commitem:

```
python3 sprawdz-teksty.py      # 0 = czysto, 1 = jest zywe skazenie
```

Skanuje wszystkie pliki wersjonowane (`git ls-files`), pomijajac celowo
brudna amunicje (`dev/kwiatki-testy/`, `dev/turnieje/`, `dev/luki/`,
`fixtures/`). Szuka homoglifow LITER (cyrylica, greka, ormianski, koptyjski,
czirokeski) oraz znakow niewidzialnych i twardych spacji. Symboli
typograficznych (€, ±, ✓) NIE zglasza - widac je golym okiem, a alarmowanie
na nich zrobiloby szum, ktory kazdy zaczalby ignorowac.

Przyklady skazen w dokumentacji zapisuj notacja `<U+XXXX>`, nigdy zywcem
(par. 5). Inaczej dokument o kwiatkach sam je roznosi - nastepny agent
skopiuje fragment i przeniesie zaraze dalej.

## 11. ZWIAD przed naprawa - obowiazkowa kolejnosc

Zasada operatora (2026-09-04):

> "Narzedzie ma ci pomagac, a nie slepo wykonywac glupie opcje. To, ze
> skrypt ma byc sprytny i nieomylny, oznacza, ze ma byc narzedziem, ktore
> nie wprowadza cie w blad, a pokazuje prawde."

Wynika z tego kolejnosc, ktorej nie wolno odwracac:

```
1. python3 zwiad.py PLIK          <- WIEDZA (nic nie zapisuje)
2. cp PLIK PLIK.kopia             <- TWOJA kopia, nie narzedzia
3. python3 zwiad.py --podglad PLIK <- co dokladnie sie zmieni
4. dopiero teraz Zaglada/Anihilator
5. sprawdz, czy plik nadal dziala
```

Nigdy odwrotnie. Nie uruchamiaj naprawy, zeby dowiedziec sie, co ona robi.

**Kopia zapasowa nalezy do CIEBIE.** Zaglada i Anihilator robia wprawdzie
wlasne `.bak-*`, ale to ich mechanizm, nie twoje zabezpieczenie. Na pliku
uzytkownika kopie robisz sam, zanim cokolwiek uruchomisz.

**Kody wyjscia zwiadu:** 0 czysto | 1 sa skazenia | 2 sa skazenia
NIENAPRAWIALNE (znaki zostana USUNIETE bezpowrotnie - sprawdz podgladem,
czy to nie tresc potrzebna uzytkownikowi, np. chinski tekst na stronie).

**Masz prawo probowac wielokrotnie.** Zwiad + kopia znacza, ze nieudana
proba nie kosztuje nic poza czasem: wracasz do kopii i probujesz inaczej.
Liczba podejsc nie ma znaczenia - liczy sie to, ze KAZDE opierasz na
danych ze zwiadu, a nie na zgadywaniu. Proba na slepo bywa gorsza od
zadnej, bo niszczy plik i nie zostawia wiedzy.

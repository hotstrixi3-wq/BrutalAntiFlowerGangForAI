# PAMIETNIK OPERATORA - spis tresci dziennika

**Ten plik jest generowany.** Nie edytuj go recznie -
`python3 pamietnik.py --indeks` nadpisze zmiany.

Wpisy zyja w `dziennik/`, po jednym pliku na sesje agenta.
Piszesz tylko do swojego pliku; cudze sa do odczytu.
Pelny opis modelu pracy: `dziennik/README.md`.

```
python3 pamietnik.py              # widok scalony
python3 pamietnik.py --szukaj SLOWO
python3 pamietnik.py --dodaj      # dopisz do swojej sesji
python3 pamietnik.py --sprawdz    # bramka przed commitem
```

Stan: **48 wpisow** z **1 sesji**.

## Praca z repozytorium i narzedziami agenta

- [2026-09-04] **Lokalne repo potrafi sie cofnac w trakcie sesji**
  - praca wypchnieta na origin przetrwala w calosci — ratunek to `git fetch origin <branch>` + `git reset --hard FETCH_HEAD`. Ale **niezacommitowane zmiany z biezacej tury przepadaja**. Commituj i pushuj 
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Heredoc w bashu zjada cudzyslowy w kodzie Pythona**
  - kodu zawierajacego cudzyslowy **nie wstrzykuj przez heredoc**. Zapisz go narzedziem do pliku (`write_file`), potem wykonaj skrypt operujacy na tym pliku. I **zawsze weryfikuj po fakcie** (`grep -c`), 
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Pipe zjada kod wyjscia**
  - kod wyjscia sprawdzaj bez potoku: `python3 turniej.py >/dev/null 2>&1; echo $?`. ---
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Sprzataj /tmp po pomiarach - inaczej rosnie niewidocznie**
  - Kazdy mkdtemp opakuj w try/finally z shutil.rmtree - takze w selftescie, takze gdy katalog ma 1 kB. Po serii recznych sabotazy sprzataj katalogi robocze od razu (rm -rf /tmp/nazwa), nie na koniec sesj
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Repo nie mialo ZADNEJ ochrony przed zniszczeniem - jeden force i po pracy**
  - Po KAZDYM sklonowaniu uruchom python3 dev/hooki/zainstaluj.py - hooki nie sa wersjonowane przez gita, wiec kazdy klon zaczyna bez ochrony. Przed operacja, ktorej git nie cofnie: python3 bakap.py. Miga
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Muzeum zamiast katalogu 'do skasowania'**
  - Sluzy -> zostaje na miejscu. Nie sluzy, ale warto pamietac -> muzeum/ Z ETYKIETA w muzeum/README.md (co bylo, po co powstalo, czemu przestalo byc potrzebne). Nie sluzy i nikt nie zatesknie -> git rm, 
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Muzeum to tablice po skasowanych plikach, nie magazyn plikow**
  - Plik przestal sluzyc, ale kiedys wnosil -> tablica w muzeum/README.md I KASACJA w tym samym commicie. Nigdy osobno: osobno znaczy albo plik znika bez sladu, albo tablica zostaje po czyms zywym. Tablic
  - `2026-09-04__01a06e18.md`

## Pisanie testow dla tej rodziny

- [2026-09-04] **Test, ktory nie umie oblac, jest bezwartosciowy**
  - po napisaniu testu **zepsuj narzedzie celowo** i sprawdz, ze test oblewa. Do sprawdzania ochrony literalow uzywaj znakow, ktore narzedzie NAPRAWDE zmienia (cyrylica, greka, CJK) — np. rosyjska nazwe m
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Wykrycie skazenia to za malo — sprawdzaj, na CO zamienil**
  - zawsze sprawdzaj **doklandy oczekiwany tekst wyjsciowy**, nie tylko „czy skazenie zniklo".
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **`compile()` nie wystarcza jako kryterium niepsucia**
  - kryterium jest **uruchomienie programu i porownanie wyjscia** przed i po. Wzor: `dev/turnieje/turniej-4-runtime.py`.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Amunicja syntetyczna nie zawiera konstrukcji z prawdziwego kodu**
  - testuj na **prawdziwym kodzie** — biblioteka standardowa Pythona lezy w `sysconfig.get_paths()['stdlib']` i ma 171 gotowych modulow. Wzor uzycia w `docs/agent/INZYNIERIA-WSTECZNA.md`.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Skazenie testowe musi byc ODWRACALNE, inaczej oskarzasz niewinnego**
  - buduj zbior **wiernych homoglifow** — takich, dla ktorych `zamien_znak()` zwraca dokladnie oryginalna litere ASCII (jest ich 52). Dopiero wtedy zadanie „odtworz oryginal" jest wykonalne, a wynik mierz
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Turniej moze przechodzic lokalnie i oblewac na swiezym klonie**
  - Turniej uruchamiaj TAKZE na swiezym klonie w innym miejscu na dysku, nie tylko w katalogu roboczym. Zielony wynik lokalnie nie dowodzi niczego o bledach zaleznych od sciezek. Gdy dodajesz do Prokurato
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Narzedzie decyzyjne wymaga innego testu niz narzedzie naprawcze**
  - Dla narzedzia decyzyjnego kryterium brzmi 'czy nie wprowadza operatora w blad', nie 'czy nie psuje plikow'. Wzor: dev/turnieje/turniej-7-zwiad.py - kategoria A bierze PRZEWIDYWANIE zwiadu, uruchamia p
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Fuzz czyta katalog NADRZEDNY nad repo - twoje pliki w /tmp psuja wynik**
  - Fuzz uruchamiaj w katalogu, ktorego RODZIC jest pusty (np. /tmp/czysty/repo, nie /tmp/repo). Zanim uznasz spadek wyniku fuzza za regresje, powtorz go na czystym klonie BEZ swojej zmiany - jesli daje t
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Bramki sprawdzaly wszystko oprocz siebie - cztery wady w trzech**
  - Kazda bramka musi byc FAIL-CLOSED: gdy nie wie, co sprawdzic, ma ODMOWIC (exit 2), nie zameldowac sukces. Listy pomijanych plikow trzymaj imiennie z uzasadnieniem, nie calymi katalogami - katalog rosn
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Pierwszy pewny test: selftest Pogromcy - ustalony pomiarem, nie opinia**
  - POZIOM 0 to PogromcaKwiatkow.py --selftest: zero subprocess, zero gita, zero katalogow tymczasowych, zero zaleznosci od innych narzedzi rodziny, probki zapisane sekwencjami uXXXX wprost w kodzie. Zlap
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Pomiar ogolny nie wystarcza - turniej moze przejsc cudzym sukcesem**
  - Po dodaniu nowej KATEGORII do turnieju uruchom dev/turnieje/pomiar-per-turniej.py - dla kazdej pary (turniej, kategoria) wycina wade, ktora ta kategoria ma wykrywac, i uruchamia WYLACZNIE ten turniej.
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Test nie moze budowac swoich probek narzedziem, ktore testuje**
  - Dane wejsciowe testu trzymaj w STALEJ liscie w kodzie testu, nie wyliczaj ich z badanego narzedzia. W T9 jest CYRYLICKIE_WIERNE - 11 par litera-homoglif wpisanych na sztywno. Uwaga przy budowaniu taki
  - `2026-09-04__01a06e18.md`

## Pulapki w samym kodzie rodziny

- [2026-09-04] **W AnihilatorChwastow.py ta sama funkcja jest zdefiniowana DWA RAZY**
  - edytujesz te funkcje? Uzywaj tej z linii **429** (aktywnej). Przed edycja dowolnej funkcji w tym pliku sprawdz: `grep -n "^def <nazwa>" AnihilatorChwastow.py` — jesli sa dwa trafienia, liczy sie ostat
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Wersja Pythona zmienia zachowanie tokenizera f-stringow**
  - sprawdz `hasattr(tokenize, "FSTRING_START")` zanim uznasz, ze sciezka dziala. Kod musi radzic sobie w obu swiatach.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **`SequenceMatcher` na calym pliku jest kwadratowy**
  - czyszczenie nie zmienia liczby linii, wiec diff licz **per linia** (`_zmiany_znakowe` w Zagladzie) — 0.137 s, wynik identyczny. Zawsze zostaw awaryjny powrot do wariantu globalnego, gdy liczba linii s
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Komentarz obiecywal heurystyke, ktorej nie bylo w kodzie**
  - nie ufaj komentarzom przy ocenie, co kod robi. Sprawdzaj zachowaniem (uruchom) albo AST. Ten sam blad moze siedziec gdzie indziej. ---
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Zaglada i Anihilator maja ROZNE tablice znakow - 24 rozbieznosci**
  - Przy KAZDEJ zmianie tablic znakow (CYR, GRK, HOMOGLIFY, NIEWIDZ, DOZWOLONE, LAMACZE) zmieniaj je w OBU plikach naraz i sprawdzaj rownosc zbiorow. Docelowo: jedno zrodlo prawdy dla tablic i test rownow
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Rodzina dawala liczby, nie wiedze - stad ZWIAD**
  - Przed kazda naprawa na pliku uzytkownika uruchom: python3 zwiad.py PLIK (albo --json, gdy decydujesz programowo) i python3 zwiad.py --podglad PLIK. Zwiad nie zapisuje NICZEGO - kopie zapasowa robisz T
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Pogromca.napraw() sama zapisuje - nie uzywac do symulacji**
  - Do podgladu i symulacji uzywaj funkcji CZYSTYCH: Z.zaglada_tekst, Z.zaglada_tekst_poza_literalami, A.zaglada_tekst_poza_literalami_multi. Logike Pogromcy --fix odtworz w pamieci (NFC, usuniecie NIEWID
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Zaglada ma kaskade 4 prob dla zepsutego .py, nie jedna droge**
  - Nie licz mozliwosci narzedzia po flagach --help. Policz funkcje transformujace tekst (AST) i przeczytaj dyspozytor (u Zaglady: _przetworz_py). Wachlarz w zwiad.py --warianty pokazuje teraz wszystkie s
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **_sprobuj_naprawy usuwa znaki i rozjezdza nazwy - compile() to przepuszcza** **[NIEAKTUALNY]**
  - Po KAZDEJ naprawie sprawdzaj spojnosc nazw, nie tylko compile(). zwiad.py --warianty robi to sam i wypisuje '!! ROZJAZD NAZW'. Gdy to zobaczysz, nie uzywaj tego wariantu - wroc do kopii i wybierz inny
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **_sprobuj_naprawy to RATOWNIK, nie blad - testowalem go poza kontekstem**
  - Zanim nazwiesz cos bledem, znajdz miejsce wywolania (grep -n nazwa_funkcji) i odtworz WARUNEK, w ktorym kod tam trafia. W swoim kontekscie _sprobuj_naprawy ratuje pliki nie do uratowania transliteracj
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Narzedzia nie wiedza o sobie - to operator ma wiedziec, ze sa**
  - To nie usterka rodziny, tylko twoj obowiazek: skoro one nie wiedza o sobie, TY masz wiedziec, ze sa. Do .js/.ts/.java/.go/.rs/.cs/.c/.cpp/.php uruchamiaj Anihilatora RECZNIE, nie licz na Prokuratora. 
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **RYZYKO-KLUCZA w Pogromcy nie odpala sie dla cyrylicy** **[NIEAKTUALNY]**
  - Nie licz na [RYZYKO-KLUCZA] przy cyrylicy i grece - to najczestsze skazenie, a wlasnie tam ostrzezenie milczy. Gdy plik uzywa literalow jako nazw (globals()[x], getattr(o,x), klucze slownika odpowiada
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Wzorzec calej rodziny: kaskada tokenize -> skaner surowy -> bramka compile**
  - Widzac w tej rodzinie pare funkcja + funkcja_surowy nie zglaszaj duplikatu - sprawdz warunek wywolania. To para dla pliku sprawnego i dla zepsutego. Ta sama zasada tlumaczy _sprobuj_naprawy (piaty sto
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **RYZYKO-KLUCZA nie odpala sie NIGDY - martwe ostrzezenie od v8.1.0**
  - Traktuj [RYZYKO-KLUCZA] jako nieistniejace - brak ostrzezenia NIC nie znaczy. To gorsze niz brak funkcji, bo operator widzi cisze i wnioskuje 'bezpiecznie'. Klase ryzyka, ktora mial wykrywac (literal 
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Fuzz A: U+0304 nie do wykrycia po NFC - wada zastana, nie regresja**
  - Nie zglaszaj tego jako regresji swojej zmiany - sprawdz najpierw wersje z gita. Wykrycie wymagaloby analizy PRZED normalizacja albo porownania dlugosci tekstu przed/po NFC. Znaki laczace bez formy zlo
  - `2026-09-04__01a06e18.md`

## Dokumentacja i bramki

- [2026-09-04] **Re-embed do RODZINA-DO-CZATU.md rob OD KONCA pliku**
  - iteruj po markerach `### <Nazwa>.py` **od konca** (`range(n-1, -1, -1)`) — wtedy offsety wczesniejszych blokow sie nie zmieniaja. Nie tnij po ogrodzeniach ```` ``` ````, bo osadzony kod ich nie ma.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Bramka spojnosci zlapala blad agenta na goracym uczynku**
  - **uruchamiaj `python3 sprawdz-spojnosc.py` po kazdej zmianie w plikach narzedzi lub dokumentacji, przed commitem.** Zero rozjazdow to warunek wejscia. To najtansza siatka bezpieczenstwa w tym repo.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Zmiana kodu = podbicie wersji w CZTERECH miejscach**
  - kolejnosc: popraw kod -> `WERSJA` -> `WERSJE.json` -> teksty -> re-embed -> `sprawdz-spojnosc.py` -> przelicz `docs/agent/KOMPLECIK.md`. Pamietaj tez o zasadzie projektu: **poprawka kodu = reset medal
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Pamietnik tez podlega Pogromcy - zero zywych kwiatkow w dokumentach**
  - Znaki obcych alfabetow w dokumentacji zapisuj notacja \uXXXX albo U+XXXX, nigdy zywcem (PROTOKOL par. 5). Po napisaniu KAZDEGO nowego dokumentu uruchom: python3 PogromcaKwiatkow.py <plik>
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Dziennik: jeden plik na sesje, cudze tylko do odczytu**
  - Piszesz WYLACZNIE do swojego pliku dziennik/DATA__SESJA.md (tworzy sie sam przy --dodaj). Cudzych nie edytujesz - bramka --sprawdz to wykryje. Nieaktualna cudza rade prostujesz WLASNYM wpisem z polem 
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **README jest punktem wejscia agenta - historia musi mieszkac osobno**
  - README to jedyny plik, ktory agent otwiera bez pytania (GitHub go pokazuje, klon zaczyna sie od niego) - wiec ma byc PUNKTEM WEJSCIA, nie kronika. Kolejne wydania dopisuj do docs/historia/HISTORIA-ZMI
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Dom Gangu: wiedza jedzie dalej, pamiec sesji zostaje**
  - Rozdziel WIEDZE od PAMIECI, nie 'dziennik od reszty'. docs/agent/LEKCJE.md - uniwersalne, jedzie z domem, z zachowanymi liczbami (bez nich to teoria). dziennik/ i STAN-SESJI.md - zostaja u autora. Kop
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Procedura ma zyc w jednym miejscu, reszta linkuje**
  - Jedna informacja - jedno miejsce. Podzial: README linkuje i nie powtarza; CZYM-JEST-GANG odpowiada DLACZEGO; PROTOKOL zawiera WSZYSTKIE procedury i komendy; STAN-SESJI mowi GDZIE JESTESMY bez procedur
  - `2026-09-04__01a06e18.md`

## Wspolpraca z operatorem-czlowiekiem

- [2026-09-04] **Zalaczniki od usera nie docieraja do agenta**
  - popros o **wklejenie tresci wprost do czatu**. Nie zgaduj, co mogl zawierac zalacznik — zrob wlasna, niezalezna analize i powiedz wprost, na czym ja opierasz.
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **„Nie ruszamy dzialajacego kodu, dokladamy kolejny"**
  - naprawa bledu = tak. Kosmetyka (usuwanie martwego kodu, przeformatowania) w tym samym commicie co zmiana logiki = nie — utrudnia cofniecie naprawy. Rozdzielaj commity. Przed zmiana w rodzinie zrob kop
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Agent sam wstawia kwiatki do tekstu - takze do zdan o kwiatkach**
  - Nie ufaj wlasnemu tekstowi. Po napisaniu KAZDEGO dokumentu i przed KAZDYM commitem uruchom: python3 PogromcaKwiatkow.py $(git ls-files). Przyklady skazen w dokumentacji zapisuj wylacznie notacja <U+XX
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **Most do zewnetrznego audytora: klon repo, nie wklejka**
  - Jesli zewnetrzny agent czyta katalog na dysku uzytkownika, kaz zrobic z tego katalogu KLON repo (git clone + checkout galezi). Audytor czyta prawdziwe pliki i moze URUCHOMIC testy, zamiast zgadywac z 
  - `2026-09-04__01a06e18.md`
- [2026-09-04] **PRZECZYTAJ CZYM-JEST-GANG.md zanim dotkniesz pliku uzytkownika**
  - Zanim uruchomisz cokolwiek na pliku uzytkownika, przeczytaj CZYM-JEST-GANG.md w korzeniu repo. Najkrocej: Gang to proteza na TWOJA slepote na homoglify (masz ja - to udowodnione), to OCZY a nie automa
  - `2026-09-04__01a06e18.md`
- [2026-09-05] **Kod od zewnetrznego audytora uruchom, zanim ocenisz**
  - Kazdy kod z zewnatrz uruchamiaj na KOPII repo w /tmp, zanim ocenisz go z lektury - i najpierw sprawdz AST-em, czy nie zapisuje (open w trybie w, subprocess, eval, remove). Ocena z samego czytania jest
  - `2026-09-04__01a06e18.md`

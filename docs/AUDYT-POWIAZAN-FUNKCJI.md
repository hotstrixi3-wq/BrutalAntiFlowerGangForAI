# AUDYT POWIAZAN FUNKCJI - weryfikacja niezalezna (2026-09-04)

> **AKTUALIZACJA po wgraniu wersji v8.4.0/v1.3.0/v1.2.0/v1.3.0:** oba
> znaleziska ponizej sprawdzone ponownie na NOWYM kodzie i **nadal
> aktualne**. `baza_bez_ogonkow` wciaz zdefiniowana 1x w Zagladzie i 1x w
> Anihilatorze, wolana 0x. `--help` wciaz nieobslugiwane w Prokuratorze i
> Anihilatorze (Pogromca i Zaglada reaguja poprawnie). Nowe wersje
> przyniosly powazne naprawy bezpieczenstwa (fail-closed, backup, zapis
> atomowy, straznik przed sklejeniem zmiennych) - te dwa drobiazgi po
> prostu nie byly ich tematem.

Powod: zgloszenie „duzo brakow powiazan funkcji". Zalaczone pliki z analiza
NIE DOTARLY do srodowiska (katalog uploads pusty), wiec audyt wykonany
OD ZERA, wlasnymi narzedziami, bez zaufania do cudzych wnioskow i bez
zaufania do wlasnych zalozen.

Metoda: parsowanie AST wszystkich 14 plikow .py w repo (4 narzedzia rodziny
+ 10 plikow dev), budowa mapy zdefiniowanych i wywolanych symboli, kontrola
powiazan miedzyplikowych (testy dev laduja rodzine przez
`spec_from_file_location`, wiec zwykly import-checker tego nie widzi -
trzeba bylo sledzic aliasy modulow), porownanie kopii osadzonych w
RODZINA-DO-CZATU z realnymi plikami bajt-w-bajt, oraz kontrola czy
dokumentacja opisuje funkcje ktore faktycznie istnieja.

## WYNIK ZBIORCZY

| Sprawdzenie | Wynik |
|---|---|
| Powiazania testy dev -> API rodziny | **0 zerwanych / 10 plikow** |
| Kopie osadzone w RODZINA-DO-CZATU vs realne pliki | **4/4 IDENTYCZNE bajt-w-bajt** |
| Funkcje opisane w dokumentacji a nieistniejace | **0** |
| Selftesty | **4/4 PASS** |
| Bramka Pogromcy (korzen+docs) | **BLAD 0 / UWAGA 0** |
| Tor / fuzz | **348/0/0/0 | 3x 500/0** |

**Nie potwierdzam tezy o „duzo brakow powiazan funkcji".** Rdzen jest spojny.
Znalazlem 2 realne, ale DROBNE usterki - obie opisane nizej uczciwie, wraz z
ocena wagi. Zadna z nich nie lamie dzialania narzedzi.

## ZNALEZISKO 1 - martwa funkcja `baza_bez_ogonkow` (2 pliki)

Status: **POTWIERDZONE, realne, niskiej wagi (higiena kodu).**

`baza_bez_ogonkow(c)` jest zdefiniowana w `ZagladaKultury.py` (linia 104) i w
`AnihilatorChwastow.py` (linia 88). W calym repo jest wywolana **zero razy**.

Dlaczego nie jest to bug funkcjonalny: logika, ktora ta funkcja mialaby
realizowac (NFD -> zdjecie ogonka), jest w obu plikach **wklejona inline**
wewnatrz `zamien_znak()` - i tam dziala poprawnie, kategoria `ogonki` jest
prawidlowo zliczana (Zaglada 141-144, Anihilator 111-122). Czyli to nie jest
„funkcja ktora sie zgubila i przez to cos nie dziala", tylko pozostalosc po
refaktorze: cialo przeniesiono do wywolujacego, definicji nie usunieto.

Roznica miedzy kopiami (istotna, gdyby ktos chcial ja podlaczyc): wersja
inline w Anihilatorze sprawdza dodatkowo czy baza po NFD jest cyrylica/greka
i wtedy zwraca transliteracje, a wersja w Zagladzie sprawdza `c not in PL`,
zeby nie ruszyc polskich liter. Sama `baza_bez_ogonkow` nie robi ani jednego,
ani drugiego - **jest prostsza niz kod ktory ja zastapil**. Podlaczenie jej
„na zywca" byloby regresja (zdjelaby ogonki z polskich liter).

Rekomendacja: usunac obie definicje (martwy kod), NIE podlaczac.
Wymaga zgody - to zmiana w kodzie rodziny.

## ZNALEZISKO 2 - `--help` nieobslugiwane w 2 narzedziach

Status: **POTWIERDZONE, realne, niskiej wagi (UX), ale mylace dla agenta.**

- `python3 PogromcaKwiatkow.py --help` -> OK (pomoc)
- `python3 ZagladaKultury.py --help` -> OK (pomoc)
- `python3 ProkuratorOgrodnik.py --help` -> `Podaj pliki do oskarzenia`, exit 2
- `python3 AnihilatorChwastow.py --help` -> `Podaj pliki`, exit 2

Prokurator i Anihilator traktuja `--help` jak nazwe pliku do przetworzenia,
nie znajduja jej i koncza bledem. Dla czlowieka to drobiazg. Dla **agenta AI**,
ktory jest tu docelowym uzytkownikiem i ktory naturalnie zaczyna od `--help`,
to falszywy sygnal „narzedzie jest zepsute" na pierwszym kontakcie - czyli
uderza dokladnie w cel FLOW USWIADOMIENIA z README.

Rekomendacja: dodac obsluge `--help` w obu (spojnie z Pogromca/Zagladą).
Wymaga zgody - to zmiana w kodzie rodziny.

## CO SPRAWDZILEM I CO WYSZLO CZYSTE

**Powiazania miedzyplikowe (najwazniejsze).** Kazdy plik testowy w `dev/`
laduje narzedzia dynamicznie. Przesledzilem aliasy modulow i zebralem
faktycznie wolane symbole:

- `dev/fuzz-pogromcy.py` -> `analizuj`, `klasyfikuj`, `OGONKI`, `TYPO`
- `dev/tor-pogromcy.py` -> `analizuj`, `OGONKI`, `TYPO`
- `dev/turnieje/turniej-2-sprawdzajacy.py` -> `analizuj`, `BLOKOWANE`, `TYPO`
- `dev/turnieje/turniej-3-niepsucie.py` -> `napraw`
- `dev/turnieje/turniej-niezalezny.py` -> `analizuj`, `napraw`, `BLOKOWANE`, `TYPO`
- `dev/turnieje/zaglada-turniej-niepsucie.py` -> `przetworz`, `raport_sciezka`, `WERSJA`
- `dev/turnieje/zaglada-turniej-wykrywania.py` -> `analizuj`, `zaglada_tekst`, `CYR`, `GREK`, `HOMOGLIFY`, `LAMACZE`, `WERSJA`
- `dev/turnieje/SUMA-KONTROLNA-TESTOW.py` -> `przetworz`

Wszystkie te symbole **istnieja** w API rodziny. Zero zerwanych.

UCZCIWA UWAGA METODOLOGICZNA: pierwsze przejscie mojego skryptu zglosilo
`OGONKI`, `TYPO`, `BLOKOWANE`, `CYR`, `GREK`, `HOMOGLIFY`, `LAMACZE`, `WERSJA`
jako „brakujace w API" - to byl **blad mojego audytu, nie repo**: filtrowalem
tylko `FunctionDef`, a to sa stale modulu (`Assign`). Po poprawce: 0 brakow.
Gdybym sie na tym zatrzymal, zaraportowalbym 8 nieistniejacych bledow -
dokladnie taki falszywy alarm, jaki podejrzewam w zgloszeniu.

**Kopie osadzone w RODZINA-DO-CZATU.md.** To byl najpowazniejszy podejrzany,
bo wlasnie tam znalazlem realny rozjazd w poprzedniej turze. Wynik po
precyzyjnym cieciu po markerach `### Nazwa.py`:

| Narzedzie | Embed | Realny plik | Status |
|---|---|---|---|
| PogromcaKwiatkow.py | 27252 B | 27252 B | IDENTYCZNY |
| ZagladaKultury.py | 22469 B | 22469 B | IDENTYCZNY |
| ProkuratorOgrodnik.py | 11156 B | 11156 B | IDENTYCZNY |
| AnihilatorChwastow.py | 18843 B | 18843 B | IDENTYCZNY |

Merge z poprzedniej tury byl poprawny - all-in-one niesie dokladnie ten kod,
ktory lezy w repo.

**Nieuzywane symbole lokalne w plikach testowych** (`s1..s6` w turnieju 2,
`zr1..zr11` w turnieju wykrywania): to NIE sa braki powiazan. To funkcje
scenariuszy rejestrowane w listach/slownikach i wolane posrednio przez
dispatcher. Sprawdzilem - sa uzywane.

## CZEGO NIE MOGLEM SPRAWDZIC

Nie widzialem analizy, ktora dostales. Jesli wskazuje konkretne miejsca,
ktorych tu nie ma - wklej sama tresc do czatu (nie jako zalacznik) albo
podaj nazwy funkcji, a zweryfikuje kazda pozycje z osobna. Powyzsze jest
audytem niezaleznym, nie odpowiedzia na tamten dokument.

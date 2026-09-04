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

- **PogromcaKwiatkow.py v8.6.0** - oczy, detektor BLAD/UWAGA/OK (+ ostrzega o literalach-uzywanych-jako-klucze)
- **ZagladaKultury.py v1.4.0** - rece dla py/json/proza, dekontaminator z ochrona literalow py (+ naprawa: litery, lamacze, spojnosc identyfikatorow, dopasowanie cudzyslowow w awaryjnym skanerze)
- **ProkuratorOgrodnik.py v1.2.0** - mozg, polityka UMORZONE/POUCZENIE/ZAGLADA/BLOKADA + akta w U+XXXX (od v1.0.1 faktycznie czyste)
- **AnihilatorChwastow.py v1.4.0** - rece dla js/ts/java/go/rs/cs/c/cpp/h/hpp/php/rb/swift/kt/py (ochrona literalow i komentarzy) oraz json/jsonl i md/proza

Zasada: nie ruszamy dzialajacego kodu, dokladamy kolejnego. Rodzina to combo i wszedzie idzie razem.

## Szybki start - FLOW USWIADOMIENIE

Nie skanuj od razu plikow usera. Najpierw analiza i uswiadomienie.

### Dla agenta AI - wiadomosc do skopiowania:

```
Hej! W zalaczonym pliku docs/RODZINA-DO-CZATU.md masz rodzine Pogromcy - combo 4 plikow.

KROK 0 - DOWOD WLASNORECZNY:
- Przeczytaj SZYBKI-START-DLA-AGENTA.md i wykonaj krok 1 stamtad (jedna
  linijka w interpreterze) - sam sobie udowodnij zjawisko przed lektura reszty

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
SZYBKI-START-DLA-AGENTA.md   KROK 0 - dowod wlasnoreczny w 30 sekund
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

## Bramka spojnosci wersji

```
python3 sprawdz-spojnosc.py     # exit 0 = spojne, 1 = rozjazd
```

Jedno zrodlo prawdy: `WERSJE.json`. Skrypt pilnuje trzech rzeczy naraz:

1. stala `WERSJA` w kodzie == `WERSJE.json`
2. warstwa czytana przez agenta nie DEKLARUJE innej wersji niz prawdziwa
3. kopie osadzone w `docs/RODZINA-DO-CZATU.md` sa identyczne bajt-w-bajt
   z realnymi plikami narzedzi

Punkt 3 to najczesciej lamana spojnosc w tym repo (dwa razy pod rzad):
kod sie zmienia, all-in-one dla agenta zostaje ze starym - i agent
dostaje INNE narzedzie niz to, ktore lezy w repo.

Zmieniasz wersje narzedzia -> zmieniasz `WERSJE.json` -> uruchamiasz skrypt.

## Historia zmian

- v8.5.0 - BRAMKA SPOJNOSCI WERSJI: `WERSJE.json` (jedno zrodlo prawdy) +
  `sprawdz-spojnosc.py`. Szkielet skryptu od autora, zaadaptowany do
  realiow tego repo po weryfikacji na zywym drzewie.

  DLACZEGO ADAPTACJA, A NIE WKLEJENIE 1:1 - oryginal zakladal dwa pliki,
  ktorych tu nie ma (`WERSJE.json`, `START.md`), i porownywal KAZDY numer
  pasujacy do `\d+\.\d+\.\d+` w warstwie agenta z lista dozwolonych.
  Na tym repo dalo to **~40 falszywych rozjazdow**, bo README zawiera
  HISTORIE ZMIAN, ktora z definicji mowi o starych wersjach ("v8.2.14 -
  Zaglada v1.0.8: naprawa..."). Zabicie historii zmian, zeby uciszyc
  walidator, byloby lekiem gorszym od choroby - to najcenniejsza czesc
  tego repo. Rozwiazanie: skrypt sprawdza DEKLARACJE (numer stojacy przy
  nazwie narzedzia), nie wzmianki, i rozpoznaje wieloliniowe bloki
  changelogu, strzalki przejscia (`v1.1.1 -> v1.3.0`) oraz linie wewnatrz
  osadzonego kodu (`print("SELFTEST ... v1.0.0")` to tresc literalu,
  ktorej nie wolno ruszac - kontrakt: literal swiety).

  DOLOZONA TRZECIA KONTROLA, ktorej oryginal nie mial: zgodnosc kopii
  osadzonych w `docs/RODZINA-DO-CZATU.md` z realnymi plikami. To jest
  dokladnie ta spojnosc, ktora w tym repo pekla DWA RAZY pod rzad
  (v8.2.21 i v8.3.0) - i ktorej zaden test funkcjonalny nie lapie, bo
  narzedzia dzialaja poprawnie, tylko agent dostaje inna ich wersje.

  ZNALEZISKO PRZY PIERWSZYM URUCHOMIENIU (prawdziwe, nie falszywy alarm):
  sekcja "Rodzina - 4 pliki ktore ida wszedzie razem" w README - czyli
  pierwsza rzecz, jaka czyta agent - deklarowala Pogromce v8.1.0, Zaglade
  v1.1.1, Prokuratora v1.0.1 i Anihilatora v1.0.0, gdy w repo lezaly juz
  v8.4.0/v1.3.0/v1.2.0/v1.3.0. Naprawione.

  Walidator zweryfikowany 4 testami NEGATYWNYMI na kopii repo (bramka,
  ktora zawsze mowi OK, jest bezwartosciowa): podmiana stalej w kodzie -
  zlapane; klamstwo w README - zlapane; rozjechany embed o JEDEN znak
  przy identycznym rozmiarze pliku - zlapane; brak `WERSJE.json` -
  czytelny blad, exit 1. Na czystym repo: 0 rozjazdow.

- v8.3.0 - WGRANIE NOWSZYCH WERSJI CALEJ RODZINY (kod dostarczony przez
  autora, wklejony wprost do czatu — zalaczniki nie dochodzily). Skok
  wszystkich czterech naraz: Pogromca v8.1.0 -> **v8.4.0**, Zaglada
  v1.1.1 -> **v1.3.0**, Prokurator v1.0.1 -> **v1.2.0**, Anihilator
  v1.0.0 -> **v1.3.0**. Repo bylo o kilka wydan w tyle za kodem autora.

  Co realnie przyszlo (zweryfikowane wykonaniem, nie lektura dokstringow):

  * **Zaglada v1.3.0 — straznik przed sklejeniem dwoch zmiennych w jedna.**
    Naprawa spojnosci identyfikatorow z v1.1.0 byla ZA CHCIWA: wystarczylo,
    ze skrocona nazwa gdziekolwiek istnieje, i `wartosc` oraz `wartosc<obcy>`
    (dwie ROZNE zmienne) byly scalane w jedna. Plik kompilowal sie, a program
    liczyl co innego. Nowy warunek: naprawa tylko gdy zabrudzona nazwa jest
    odludkiem (wystepuje DOKLADNIE RAZ), a jej czysty odpowiednik istnieje
    gdzie indziej. Zweryfikowane na przypadku z dokstringu: zmienne pozostaja
    rozroznialne, plik sie kompiluje.
  * **Anihilator v1.2.0/v1.3.0 — BLOKADA zamiast cichego psucia.** Automat
    stanow nie jest lekserem: literaly mogace zawierac niesparowany cudzyslow
    (C++ `R"(...)"`, Rust `r#"..."#`, bloki tekstowe Javy/Kotlina/Swifta,
    heredoki Ruby/PHP, backticki Go) rozjezdzaly mu stan i fragment literalu
    byl czyszczony wbrew kontraktowi. Teraz takie pliki sa ODRZUCANE (exit 2).
    Zweryfikowane: 6/6 konstrukcji zablokowanych, przy tym C# `@"..."` i
    szablony JS nadal przechodza (brak nadgorliwosci).
  * **Prokurator v1.1.0/v1.2.0 — koniec fail-open.** Do v1.0.1 awaria
    rodzenstwa (zla sciezka wzgledna, katalog jako argument, pusty stdout)
    konczyla sie kodem 0 i meldunkiem "czysto" na plikach brudnych. Teraz:
    sciezki absolutne z `__file__`, katalogi rozwijane do listy plikow,
    kazda awaria = BLOKADA.
  * **Pogromca v8.2.0-v8.4.0 — ochrona literalow w `--fix`.** Kontrakt
    "tresc literalu jest swieta" obowiazywal Zaglade, ale NIE `--fix` —
    a to wlasnie `--fix` protokol stawia na poziomie "rutynowo, bez pytania".
    Dodatkowo fail-closed na plikach o zlym kodowaniu (wczesniej `--fix`
    zapisywal uszkodzone bajty jako U+FFFD, trwale niszczac oryginal).
  * **Wspolne dla calej rodziny: backup + zapis atomowy (R3/R4/R7).**
    Wczesniej `open(sciezka,"w").write(...)` — przerwanie w polowie
    zostawialo plik obciety bez mozliwosci powrotu. Teraz kopia `.bak-*`,
    zapis do pliku tymczasowego, `fsync`, `os.replace()`. Zweryfikowane:
    R3 (odmowa zapisu na kopii zapasowej), R4 (drugi przebieg nie kasuje
    pierwszej kopii, dostaje sufiks `.2`), R7 (`--fix` bez argumentow =
    BLOKADA, wczesniej szedl po katalogu NADRZEDNYM wobec narzedzia).

  Regresja po wgraniu: **ZERO**. Selftesty 4/4 PASS, tor 348/0/0/0,
  fuzz A/B/C 500/0 kazdy, T2 992 wektorow 0/0/0, T3 190 plikow 0 popsutych,
  Z1 1545 wektorow 0/0/0, Z2 200 plikow 0 popsutych, bramka Pogromcy na
  korzeniu+docs BLAD 0 / UWAGA 0 (24 pliki).

  RODZINA-DO-CZATU: wszystkie 4 osadzone kopie re-embedowane bajt-w-bajt
  (po wgraniu byly rozjechane wzgledem realnych plikow — ta sama klasa
  bledu, ktora naprawiano w v8.2.21; teraz 4/4 identyczne). Numery wersji
  zsynchronizowane w PROTOKOLE, RODZINIE, wniosku i README-TURNIEJ.

- v8.2.21 - PORZADKI W DRZEWIE (zero zmian w kodzie rodziny). Korzen repo
  zawieral rownolegly, zduplikowany komplet plikow obok `docs/` i `dev/`:
  14 dokumentow .md, 15 plikow amunicji JSON, 9 narzedzi testowych .py i
  2 logi — lacznie 40 plikow, ktore lamaly wlasna zasade struktury
  deklarowana w KOMPLECIKU („KORZEN = tylko integracja agent+czlowiek;
  dowody i infrastruktura -> docs/ i dev/"). Kluczowe znalezisko: te
  kopie NIE byly rownowazne. 15 JSON-ow, 9 narzedzi i 2 logi byly
  bit-w-bit identyczne (czysty smiec), ale 5 dokumentow ROZJECHALO sie —
  i to wersja w korzeniu byla NOWSZA (Pogromca v8.1.0 / Zaglada v1.1.1),
  podczas gdy `docs/` — czyli to, co czyta agent i co linkuje README —
  serwowalo nieaktualne v8.0.3 / v1.0.9. Repo dokumentowalo samo siebie
  niezgodnie z wlasnym kodem. Rozwiazanie: nowsze wersje z korzenia
  przeniesione do `docs/` (tresc zachowana, bo swiezsza), duplikaty
  bit-w-bit skasowane, `SUMA-KONTROLNA-TESTOW.py` przeniesiona do
  `dev/turnieje/` (tam ja deklarowal manifest i ten README — plik lezal
  w korzeniu, wiec link byl martwy), usuniety plik-smiec `download`
  (przypadkowa kopia `.gitignore` bez rozszerzenia). KOMPLECIK
  przeliczony maszynowo od zera: 49 plikow, wszystkie sha256 i rozmiary
  swieze (poprzedni manifest podawal sumy sprzed v8.2.18 — np. Pogromca
  22804 B zamiast realnych 27484 B). Weryfikacja po zmianach: 4/4
  selftesty PASS, bramka Pogromcy na korzen+docs BLAD 0 / UWAGA 0 (23
  pliki), audyt linkow 49/49 zywych, tor 348/0/0/0, fuzz A/B/C
  500/0-500/0-500/0. Zaden plik rodziny nie zostal zmodyfikowany —
  operacja czysto strukturalna, wykonana przez `git mv`/`git rm`, wiec
  cala historia jest zachowana.

- v8.2.20 - Pogromca v8.1.0: nowa warstwa raportu RYZYKO-KLUCZA, decyzja
  własna agenta-operatora po analizie misji ("Gang chroni kod przed
  popsuciem, użytkownikiem jest agent AI — agent decyduje co zrobić, żeby
  narzędzie było skuteczne"). Adresuje jedyne znane, udokumentowane, NIE
  naprawione ryzyko z sesji: literal string w kodzie .py zawierający obcy
  znak, którego oczyszczona wersja pasuje do innego identyfikatora/literalu
  już w pliku (sygnał: to prawdopodobnie ta sama nazwa, skażona tylko w
  jednym miejscu, pełniąca funkcję klucza/identyfikatora gdzie indziej).
  Zagłada SŁUSZNIE nie rusza treści literałów (kontrakt: święte) — więc
  taki plik kompiluje się czysto i wybucha AttributeError/KeyError dopiero
  w runtime. Pogromca to teraz WYKRYWA (przez tokenize, tylko dla .py,
  tylko gdy plik się tokenizuje) i OSTRZEGA — nic nie modyfikuje, nic nie
  usuwa z literału, decyzja zostaje przy operatorze. Zweryfikowane: 0/19
  fałszywych alarmów na czystym korpusie (test-50 czyste + własne 4
  narzędzia + 3 oryginały z GitHuba), 0/27 awarii na korpusie brudnym,
  łapie dokładnie przypadek znaleziony wczoraj (literal "niewidzialne"
  skażony jednym znakiem, użyty jako klucz słownika gdzie indziej).

  UCZCIWIE: podczas wdrażania tej łatki sam sobie wprowadziłem prawdziwy
  bug — `str_replace` przypadkiem skasował nagłówek `def domyslne_pliki():`
  (ciało funkcji zostało, ale bez definicji — `python3 PogromcaKwiatkow.py`
  bez argumentów kończył się `NameError` zamiast normalnym skanem).
  Złapane przez T2 (FN 1, dwa seedy pod rząd, wektor `s5-cli:bez
  argumentow`), nie przez ręczny przegląd — dokładnie po to jest ten
  test. Naprawione, T1/T2/T3 + tor + fuzz + bramka całego repo ponownie
  zielone po naprawie. Osobno, drugi raz w tej samej rundzie: użyłem
  żywego znaku cyrylickiego w przykładzie w dokstringu zamiast notacji
  U+XXXX (trzeci raz w tej sesji ten sam błąd) — złapane przez bramkę
  Pogromcy na własnym pliku, naprawione.

- v8.2.19 - Zagłada v1.1.1: naprawa desynchronizacji stanu w awaryjnym
  skanerze (`zaglada_tekst_poza_literalami_surowy`), znaleziona
  ABSURDALNYM testem na żądanie użytkownika: Zagłada atakuje i czyści
  zaatakowaną kopię WŁASNEGO kodu źródłowego (100 wstrzyknięć w słowa
  kluczowe/identyfikatory, seed 666). Znalezisko: stany `lancuch`/`trojka`
  zamykały się na DOWOLNYM znaku cudzysłowu, nie na tym samym, który je
  otworzył (`if c in ("'", '"')` zamiast dopasowania do zapamiętanego
  otwierającego). Na zwykłym kodzie nieszkodliwe, ale na pliku, który sam
  zawiera na przemian `"'''"` i `'"""'` jako dane (dokładnie taki jest kod
  samej Zagłady — sędzia cudzysłowów zawiera cudzysłowy jako dane) —
  rozjeżdża stan skanera, przez co całe fragmenty pliku po takiej linii
  są cicho pomijane (ani transliterowane, ani liczone jako podatne).
  Naprawa: skaner pamięta KTÓRY znak/sekwencja otworzyła literał
  (`cudzyslow = c`), zamyka tylko na dokładnym dopasowaniu. Regresja: 0
  (test-50 nadal 11/11, 50/50 czystych bez zmian, 16/16 turnieju
  zewnętrznego, tor 348/0/0/0). Reset medalu (4. raz w tej sesji) —
  odzyskany.

  DRUGIE znalezisko tego samego absurdalnego testu, NIE naprawione —
  udokumentowana granica architektury, nie błąd implementacji: string
  literal użyty jako klucz słownika gdzie indziej w tym samym pliku
  (`"niewidzialne"` w krotce KATEGORIE, odczytywane jako
  `licznik["niewidzialne"]`) może zostać skażony wewnątrz cudzysłowu
  (przykład z testu: cyrylickie U+0430 wstrzyknięte tuż po "nie", dając
  wizualnie nierozróżnialny ciąg) i Zagłada SŁUSZNIE
  go nie rusza (kontrakt: zawartość literału jest święta). Plik wtedy
  kompiluje się, ale wybucha `KeyError` w runtime. To nie jest do
  naprawienia bez złamania obietnicy "nie ruszamy zawartości stringów" —
  to jest cena tej obietnicy, nazwana wprost, nie ukryta.

  Nowe narzędzie: `dev/turnieje/SUMA-KONTROLNA-TESTOW.py` — mechanizm
  złotego pliku z sumami sha256 (wejście/wyjście/źródło Zagłady) do
  szybkiej weryfikacji testów bez ponownego czytania każdego pliku;
  ostrzega jeśli źródło Zagłady zmieniło się od zapisania manifestu.

- v8.2.18 - Zagłada v1.1.0: naprawa spójności identyfikatorów, znaleziona
  turniejem zewnętrznym (3 prawdziwe pliki .py z GitHuba, 6 nowych kategorii
  ataku niepróbowanych wcześniej). Znalezisko: plik może skompilować się
  przez samą transliterację (szybka ścieżka, bez wywołania naprawy z
  v1.0.8/1.0.9), ale wynik jest SKŁADNIOWO poprawny a SEMANTYCZNIE inny —
  np. `self._scandir_path` w jednym miejscu pliku, `self._VIIIscandir_patKh`
  w drugim (po foldzie NFKC dwóch znaków: rzymska osemka U+2167→VIII + znak
  Kelvina→K wstrzykniętych w jedno słowo). `compile()` tego nie widzi —
  sprawdza składnię, nie spójność nazw. W runtime: `AttributeError`.
  Nowa funkcja `_napraw_niespojnosc_identyfikatorow()`: po czyszczeniu
  diffuje oryginał z wynikiem, dla każdej zmiany rozszerza do granic
  identyfikatora, i jeśli wariant-z-usunięciem pasuje do INNEGO
  identyfikatora już istniejącego w pliku (silny sygnał że to ta sama
  zmienna zabrudzona w jednym miejscu) — usuwa zamiast zostawiać
  transliterację, weryfikuje `compile()` jak zawsze. Zweryfikowane na
  żywo: naprawiony plik faktycznie się importuje i działa (nie tylko
  kompiluje). Regresja: 0 (test-50 nadal 11/11, 50/50 czystych bez zmian,
  16/16 wariantów turnieju zewnętrznego kompiluje się, tor 348/0/0/0,
  selftesty PASS). Reset medalu (3. raz w tej sesji, własna zasada):
  Z1 3x zielone (seed 7/21/55: 1572/0/0 każdy) + Z2 3x zielone (200/0
  każdy) = medal odzyskany.

- v8.2.16 - Zagłada v1.0.9: DRUGA i głębsza przyczyna tego samego problemu,
  znaleziona przy ponownej analizie wstecznej (priorytet nad SZYBKIM
  STARTEM na wyraźne polecenie). Poprzedni wpis (v8.2.14) mówił „2/6 nadal
  nie" dla cProfile.py/csv.py — to było prawdziwe W TAMTYM MOMENCIE, ale
  niepełne: LAMACZE (separatory linii Unicode, np. U+2028) wstrzyknięte w
  ŚRODEK identyfikatora były bezwarunkowo zamieniane na prawdziwy `\n`
  (poprawne zachowanie dla prozy), co rozcinało identyfikator na dwie
  linie i rozwalało wcięcia bloku — dokładnie ta sama choroba co litery
  cyr/grk/homoglify/fold z v1.0.8, tylko w kategorii, która nigdy nie
  dostała tej samej ochrony co twarda spacja (v1.0.2). Naprawa: LAMACZE
  dołączone do tej samej puli „spróbuj usunąć zamiast wstawić", każda
  próba nadal zweryfikowana bramką compile(). WYNIK: **11/11 plików z
  testu 50 kodów teraz się kompiluje** (poprzednio 4/6 po v1.0.8, 0/6
  przed jakąkolwiek naprawą). Regresja: 0 (50/50 czystych bajt-w-bajt,
  idempotencja, T1 4666/0/0/0/FIX8-8, T2 1004/0/0, T3 190/0 zepsutych,
  tor 348/0/0/0, fuzz A/B/C 500/0-500/0-500/0 — wszystko bez zmian).
  Reset medalu (własna zasada, kolejny raz): Z1 2x zielone (seed 7 i 13:
  1572/0/0 każdy) + Z2 2x zielone (seed 7 i 13: 200/0 każdy) = medal
  odzyskany. UCZCIWIE: v8.2.14 nie kłamał (4/6 było prawdziwym wynikiem
  na tamtym kodzie), ale nie było to ostatnie słowo — „nierozwiązane"
  czasem znaczy „jeszcze nie rozwiązane", nie „nie do rozwiązania".

- v8.2.15 - Dodany SZYBKI-START-DLA-AGENTA.md: KROK 0 FLOW UŚWIADOMIENIA,
  dowód własnoręczny zjawiska w jednej linijce Pythona (dwa napisy
  wyglądające identycznie, identyczna długość, `a == b` daje `False`) —
  przed jakąkolwiek lekturą mitologii projektu. Wpięty jako pierwszy krok
  w PROTOKOL-OPERATORA, README, INSTRUKCJA-DLA-ZIELONYCH, wniosku;
  re-embedowany bajt-w-bajt w RODZINA-DO-CZATU jako 5. blok kodu. Cel:
  skrócić czas od pierwszego kontaktu agenta z narzędziem do zrozumienia
  sedna (obserwowany rozrzut 20 min – 2h między różnymi instancjami).
  Znana luka: zakłada dostęp agenta do wykonania kodu (sandbox); brak
  ścieżki biernej dla agentów bez tej możliwości.

- v8.2.14 - Zagłada v1.0.8: naprawa przypadków, gdzie transliteracja
  pojedynczego znaku cyr/grk/homoglify/fold w kodzie .py (poza literałami)
  wstawiała literę w białe znaki lub w środek słowa kluczowego, łamiąc
  składnię identycznie jak twarda spacja przed v1.0.2 (`while`→`wKhile`,
  `from`→`fromo`, samotna litera w wcięciu). Przed [OSTRZEZENIE] próbowana
  jest teraz naprawa: usunięcie (zamiast podmiany) podejrzanych znaków,
  każda próba zweryfikowana bramką compile() — nic nie wchodzi bez zielonego
  testu. UCZCIWY WYNIK na teście 50 kodów (dev korpus): **4/6 wcześniej
  łamanych plików teraz się kompiluje** (cmd.py, codeop.py, copyreg.py,
  decimal.py); **2/6 nadal nie** (cProfile.py, csv.py) — te mają po
  kilkanaście niezależnych wstrzyknięć naraz, w tym takie, które psują
  szerokość wcięcia przez USUNIĘCIE (nie tylko przez podmianę), a to
  wymaga osobnej, głębszej naprawy (rekonstrukcja spójności wcięć), poza
  zakresem tego patcha. Regresja: 0 (50/50 plików czystych bajt-w-bajt,
  idempotencja zachowana, tor 348/0/0/0 bez zmian). Zgodnie z własną zasadą
  turnieju („poprawka kodu = reset do pierwszego turnieju") ten patch
  ZRESETOWAŁ medal Zagłady — odrobiony od razu: Z1 2x zielone (seed 7:
  1572/0/0/0; seed 11: 1572/0/0/0) + Z2 2x zielone (seed 7: 200/0; seed 11:
  200/0) = MEDAL odzyskany w tej samej sesji, bez poprawek między rundami.

- v8.2.13 - Pogromca dokstring zgodnie z prawda (2h/2i, rozkaz Magusa):
  przyklady uzycia bez nieistniejacego katalogu pewniaki/ (4x, sciezka ery
  sprzed reorganizacji), combo z cala rodzina 4 (nie tylko "siostra
  Zaglada"). Kod, logika i wyjscia BEZ ZMIAN - selftest PASS, tor 348/0/0/0;
  wersja v8.0.3 zachowana (zmiana dokumentacyjna). RODZINA re-embed.

- v8.2.12 - Anihilator zgodnie z faktami (2g, rozkaz Magusa): dokstring i
  kontrakt uzupelnione (skaner stanow dla 13 jezykow + py przez tokenize,
  json/jsonl tryb kodu, md/proza; kod przyjmuje 20 rozszerzen); opisy w
  README/PROTOKOL/INSTRUKCJI/wniosku zjednaczone; RODZINA re-embed bajt-w-bajt.
  Logika, CLI i wyjscia BEZ ZMIAN - selftest 9/9, wersja v1.0.0 zachowana.

- v8.2.11 - RODZINA-DO-CZATU: pelna lista werdykow Prokuratora z POUCZENIE
  (2d, 2 miejsca) i struktura paczki zgodna z realnym drzewem (2f: RODZINA
  i INSTRUKCJA przeniesione do docs/, usuniety nieistniejacy przyklady/).
  Opis Anihilatora zgodny z faktycznymi mozliwosciami kodu (2e): jezyki ze
  skanerem stanow + c/cpp/h/hpp/php/rb/swift/kt, py, json/jsonl, md/proza.

- v8.2.10 - literowki ery autora poprawione na rozkaz Magusa (7: stworzone,
  agentów, komenda, użyć, momencie, później, wydań); stylem i dlugoscia zdan
  nie ruszono - kazda poprawka 1:1 wewnatrz zdania.

- v8.2.9 - prawda o rodzinie w 3 dokumentach (rozwiązania 2a/2b/2c, rozkaz
  Magusa): README-TURNIEJ silnik Zaglada v1.0.5 -> v1.0.7 (EN+PL); INSTRUKCJA
  i wniosek: pelne listy (POUCZENIE; Anihilator tez py/json/md).

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
- v8.1.7 - pelna anglicyzacja wydania, kasacja starszych wydań i tagow.

## Licencja

MIT - patrz LICENSE. 100% darmowe dla ludzi, firm i agentow AI.

Repo: https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI

## v8.6.0 / Zaglada 1.4.0 / Anihilator 1.4.0 - naprawa luki f-string i wydajnosci

Trzy zmiany, wszystkie z dowodem w `dev/`:

1. **Luka krytyczna: wnetrze f-stringa bylo chronione jak dane.**
   Definicja zmiennej poza stringiem byla czyszczona, a jej uzycie w
   `f"{...}"` nie - plik, ktory DZIALAL, po czyszczeniu dawal `NameError`,
   mimo ze `compile()` przechodzil. To samo w JS: template literal `${...}`.
   Naprawione w Zagladzie, Pogromcy i Anihilatorze (`_kod_we_fstringu`).
   Dowod: `python3 dev/luki/luka-fstring.py` (0/5 zepsutych, exit 0).

2. **Wydajnosc: kwadratowy diff.** `_napraw_niespojnosc_identyfikatorow`
   liczyl `SequenceMatcher` znak-po-znaku na calym pliku. `argparse.py`
   (99 KB) = **3 min 23 s**. Teraz diff jest liczony per linia
   (`_zmiany_znakowe`), z awaryjnym powrotem do wariantu globalnego gdy
   liczba linii sie zmieni: **0.137 s** (~1480x), wynik identyczny.

3. **Nowe kryterium testow: URUCHOM I POROWNAJ WYNIK.**
   `dev/turnieje/turniej-4-runtime.py` - dotad turnieje uznawaly plik za
   caly, jesli przechodzil `compile()`, a wlasnie ta klasa bledow
   (f-string, niespojnosc nazw) `compile()` PRZECHODZI. T4 uruchamia
   program przed i po i porownuje wyjscie. Sprawdza tez sile naprawcza:
   pliki zepsute PRZED musza dzialac PO.
   Zweryfikowany w obie strony: na starej wersji exit 1, na nowej exit 0.

Regresja po zmianach: tor 348/0/0/0 | fuzz 3x500/0 | T2 992 0/0/0 |
T3 190 0 popsutych | Z1 1545 0/0 | Z2 200 0 popsutych | T4 ZDANE |
selftesty 4/4 PASS | bramka 0 rozjazdow.
Na 40 prawdziwych modulach stdlib: 0 niekompilujacych sie,
40/40 importuje sie z identycznym publicznym API.

## v8.7.0 / Prokurator 1.3.0 - turnieje dla Prokuratora i Anihilatora

Dwa narzedzia rodziny nie mialy ANI JEDNEGO testu poza wlasnym selftestem,
mimo ze oba pisza po plikach, a Prokurator dodatkowo DECYDUJE o uruchomieniu
Zaglady. Teraz maja turnieje, ktore zostaly sprawdzone SABOTAZEM: kazdy z
nich musial oblac na celowo popsutym narzedziu, inaczej byly bezwartosciowe.

**T5 — Anihilator** (`dev/turnieje/turniej-5-anihilator.py`), 5 kategorii:
wykrywanie (15 przypadkow, FN/FP), niepsucie danych (11), poprawnosc naprawy
(8 - czy znak zamieniony na WLASCIWA litere, nie usuniety), fail-closed
(8 blokad + kontrola, ze plik nie zostal tkniety), wykonanie na realnym
runtime (node/gcc, 9 probek).
Zweryfikowany 4 sabotazami: wylaczony fail-closed (8 naruszen), brak ochrony
literalow (5), cofnieta naprawa template literal (3), slepota na cyrylice (4).

**T6 — Prokurator** (`dev/turnieje/turniej-6-prokurator.py`), 5 kategorii:
polityka (9 przypadkow: UMORZONE/POUCZENIE/ZAGLADA/BLOKADA), allowlista,
czyste akta (par. 5 - zero zywych znakow w raporcie), plan-act (raport nie
rusza, --wykonaj rusza), fail-closed.
Zweryfikowany 5 sabotazami - kazdy zlapany.

**T6 od razu znalazl dwie realne wady Prokuratora (naprawione w 1.3.0):**

1. `--wykonaj` NIGDY nie czyscil plikow .py. Kod mowil "elif is_py:" i
   dawal POUCZENIE kazdemu skazonemu Pythonowi; komentarz obiecywal
   heurystyke "czy skazenie jest w literale", ale jej nie bylo. Zaglada
   potrafi te pliki naprawic i sama chroni literaly.
   Naprawa: `_py_skazenie_tylko_w_literalach()` - sprawdza tokenize, czy
   skazenie siedzi w literalach; przy watpliwosci zwraca True (ostrozniej).
2. Pliki nie-UTF8 dostawaly zwykla decyzje zamiast BLOKADY. Pogromca czyta
   tolerancyjnie (errors="replace"), wiec uszkodzony bajt wracal jako
   U+FFFD i Prokurator orzekal o tresci, ktorej NIE PRZECZYTAL.
   Naprawa: U+FFFD w dowodach -> BLOKADA.

Regresja: tor 348/0/0/0 | fuzz 3x500/0 | T2 992 0/0/0 | T3 190 0 popsutych |
Z1 1545 0/0 | Z2 200 0 popsutych | T4 ZDANE | T5 ZDANE | T6 ZDANE |
luka-fstring 0/5 | selftesty 4/4 PASS | bramka 0 rozjazdow.

## Pamietnik operatora (v8.8.0)

`PAMIETNIK-OPERATORA.md` + `pamietnik.py` - pamiec miedzy sesjami agentow.

Repo mialo dotad dwa rodzaje wiedzy: **jak system ma dzialac** (README,
PROTOKOL-OPERATORA, SZYBKI-START) i **co udowodniono** (docs/, certyfikaty,
raporty turniejow). Brakowalo trzeciego: **co poszlo nie tak komus, kto tu
pracowal wczesniej**. Ta wiedza gina wraz z koncem sesji, wiec kolejny agent
nadeptuje na te same grabie.

17 wpisow startowych w 5 sekcjach, wszystkie z realnej pracy nad repo:
praca z repozytorium, pisanie testow, pulapki w kodzie rodziny,
dokumentacja i bramka, wspolpraca z czlowiekiem. Kazdy wpis ma trzy pola:
**Objaw** (konkretny - komunikat, liczba), **Przyczyna**, **Wniosek**
(czynnosc na przyszlosc).

```
python3 pamietnik.py                 # ostatnie wpisy
python3 pamietnik.py --lista         # spis wszystkich
python3 pamietnik.py --szukaj testy  # przeszukaj tresc
python3 pamietnik.py --dodaj         # dopisz wpis (pyta o pola)
python3 pamietnik.py --sprawdz       # walidacja formatu, 0 = OK
python3 pamietnik.py --selftest      # test wlasny
```

Dlaczego osobne narzedzie do zwyklego markdowna: pamietnik jest uzyteczny
tylko dopoki ma jeden format. Recznie dopisywane wpisy rozjezdzaja sie po
kilku sesjach i plik staje sie smietnikiem, ktorego nikt nie czyta.
`--sprawdz` wymusza komplet pol - wpis bez Wniosku jest bezuzyteczny dla
nastepnego agenta. Walidator od razu zlapal brak pola **Przyczyna** w
jednym z wpisow startowych pisanych recznie.

Podpiete w SZYBKI-START-DLA-AGENTA.md (krok 4) i PROTOKOL-OPERATORA.md (par. 9).

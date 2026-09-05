# Historia zmian

Kronika wydan wyprowadzona z README, zeby ten pozostal punktem wejscia
dla agenta, a nie zapisem przeszlosci. Historia ma prawo mowic o starych
wersjach - to nie sa deklaracje stanu biezacego (patrz
`sprawdz-spojnosc.py`, funkcja `_linia_historyczna`).

Stan biezacy: `WERSJE.json`. Co dzialo sie w sesjach: `dziennik/`.

---

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

## Dziennik operatora (v9.0.0)

`dziennik/` + `pamietnik.py` - pamiec miedzy sesjami agentow.

Repo mialo dwa rodzaje wiedzy: **jak system ma dzialac** (README, PROTOKOL,
SZYBKI-START) i **co udowodniono** (docs/, certyfikaty, turnieje). Brakowalo
trzeciego: **co poszlo nie tak komus, kto pracowal tu wczesniej**. Ta wiedza
ginela z koncem sesji i kolejny agent nadeptywal na te same grabie.

### Model: jeden plik na sesje

```
dziennik/2026-09-04__01a06e18.md
         ^data        ^id sesji (z galezi gita)
```

- **Piszesz tylko do swojego pliku** - tworzy sie sam przy `--dodaj`.
- **Cudze sa tylko do odczytu.** `--sprawdz` porownuje `dziennik/` z gitem
  i zglasza kazda zmiane w cudzym pliku, na gorze listy problemow. W gicie
  nie ma technicznej blokady zapisu - chodzi o wykrywalnosc przed commitem.
- **Ale wolno prostowac.** Rada sprzed roku moze byc nieaktualna. Nie
  edytujesz cudzego pliku - dopisujesz wlasny wpis z polem
  `**Zastepuje:** <tytul starego>`. Widok oznaczy tamten jako
  `[NIEAKTUALNY]` z odsylaczem. Zla rada przestaje szkodzic, historia
  pomylki zostaje.
- **Czytasz calosc.** Trzydziesci osobnych plikow to trzydziesci plikow,
  ktorych nikt nie otworzy - dlatego domyslny widok **scala wszystkie
  sesje**, pogrupowane tematami, a `PAMIETNIK-OPERATORA.md` w korzeniu jest
  generowanym spisem tresci.

```
python3 pamietnik.py                  # widok scalony
python3 pamietnik.py --temat testy    # jeden temat
python3 pamietnik.py --szukaj SLOWO   # przeszukaj wszystkie sesje
python3 pamietnik.py --sesje          # kto pisal, ile wpisow
python3 pamietnik.py --dodaj          # dopisz do swojej sesji
python3 pamietnik.py --sprawdz        # bramka: format + nietykalnosc
python3 pamietnik.py --indeks         # odswiez spis w korzeniu
```

20 wpisow startowych w 5 tematach (repo, testy, kod, dokumentacja,
wspolpraca), wszystkie z realnej pracy nad repo. Kazdy ma trzy obowiazkowe
pola: **Objaw** (konkretny - komunikat, liczba), **Przyczyna**, **Wniosek**
(czynnosc na przyszlosc).

Dlaczego osobne narzedzie do zwyklego markdowna: dziennik jest uzyteczny
tylko dopoki ma jeden format. `--sprawdz` wymusza komplet pol - wpis bez
Wniosku jest bezuzyteczny dla nastepnego agenta. Walidator od razu zlapal
brak pola **Przyczyna** w recznie pisanym wpisie startowym.

Pelny opis modelu: `dziennik/README.md`. Podpiete w SZYBKI-START (krok 4)
i PROTOKOL-OPERATORA (par. 9).

## v8.9.0 - bramka tekstow (sprawdz-teksty.py)

User wylapal w odpowiedzi agenta na czacie slowo, w ktorym `gra` bylo
zapisane cyrylica (U+0433 U+0440 U+0430) doklejona do lacinskiego `biami`.
Kontrolny skan repo znalazl **16 kolejnych zywych homoglifow w trzech
dokumentach, ktore agent napisal w tej samej sesji** - w tym w dokumentach
OSTRZEGAJACYCH przed homoglifami.

To nie jest niedbalstwo, tylko ten sam mechanizm co w SZYBKI-START,
zwrocony do wewnatrz: agent nie widzi tego u siebie ani przy pisaniu, ani
przy wlasnym przegladzie. Doszlo sprzezenie - im wiecej pisal O cyrylicy,
tym czesciej mu sie wstawiala.

Odpowiedz: jedno polecenie, zawsze to samo, przed kazdym commitem.

```
python3 sprawdz-teksty.py            # skan repo, 0 = czysto
python3 sprawdz-teksty.py PLIK...    # wskazane pliki
python3 sprawdz-teksty.py --selftest
```

Szuka homoglifow LITER (cyrylica, greka, ormianski, koptyjski, czirokeski)
plus znakow niewidzialnych i twardych spacji. Pomija celowo brudna amunicje
(`dev/kwiatki-testy/`, `dev/turnieje/`, `dev/luki/`, `fixtures/`).
Symboli typograficznych (€, ±, ✓, ½) NIE zglasza: widac je golym okiem,
a narzedzia rodziny musza je wymieniac w stalych `TYPO`/`TYPOGRAFIA`.
Pierwsza wersja alarmowala na nich i dala 8 falszywych trafien - bramka,
ktora szumi, zostaje zignorowana i wtedy przepusci prawdziwy kwiatek.

Zweryfikowana w obie strony: czyste repo exit 0, repo z jednym wstrzyknietym
U+043E w README exit 1.

Naprawione przy okazji: 16 zywych homoglifow w `docs/INZYNIERIA-WSTECZNA.md`,
`docs/LUKI-W-TESTACH.md`, `docs/NAPRAWA-v8.6.0.md` zamienione na `<U+XXXX>`.
Przyklady staly sie przy tym CZYTELNIEJSZE - widac dokladnie, gdzie siedzi
podmiana. Wpadka zapisana w PAMIETNIK-OPERATORA.md (sekcja 5).

## v9.1.0 - ZWIAD: narzedzie ma pokazywac prawde, nie wykonywac opcje

Zasada operatora, ktora zmienila definicje slowa "nieomylny":

> "Narzedzie ma ci pomagac, a nie slepo wykonywac glupie opcje. To, ze
> skrypt ma byc sprytny i nieomylny, oznacza, ze ma byc narzedziem, ktore
> nie wprowadza cie w blad, a pokazuje prawde."

Rodzina dawala LICZBY. Na skazonym pliku Zaglada mowila:

```
[DO ZAGLADY] app.py: cyr 4
```

Cztery co? Gdzie? W kodzie czy w komentarzu? Na co zostana zamienione?
Czy plik po naprawie zadziala? Pogromca pokazywal trzy trafienia i
"...i 3 dalszych". Zeby poznac odpowiedzi, trzeba bylo skopiowac plik,
uruchomic naprawe i porownac diffem - czyli DZIALAC, zeby sie DOWIEDZIEC.

`zwiad.py` odwraca kolejnosc. Ten sam plik:

```
Znalezisk: 6   (w KODZIE: 4 | w danych: 2)      <- Pogromca pokazywal 4
Kompiluje sie teraz: TAK | po naprawie: TAK

-- W KODZIE (zmieni dzialanie programu) --
   2:2   U+043E cyr  ->  'o'      conter = 0
   7:25  U+043E cyr  ->  'o'      return f"licznik: {conter}"

-- W DANYCH (literaly, komentarze) --
   1:12  U+043E cyr  ->  'o'      # licznik poczatkowy
   3:15  U+0430 cyr  ->  'a'      NAZWA = "Moskwa"
```

Widac od razu, ze wnetrze f-stringa to KOD mimo ze wyglada jak tekst,
a komentarz i literal sa bezpieczne.

Na pliku HTML z chinskim tekstem zwiad ostrzega **zanim** cokolwiek zniknie:

```
NIENAPRAWIALNE (zostana USUNIETE): 2
   1:14  U+4E2D pisma  ->  USUNIECIE     <p lang="zh">...</p>
exit=2
```

### ZWIAD NICZEGO NIE ZAPISUJE

Nie ma tu flagi zapisu i nie bedzie. Selftest sprawdza to osobnym testem:
po pelnym badaniu plik na dysku musi byc bajt w bajt taki sam.

```
python3 zwiad.py PLIK              # raport dla czlowieka
python3 zwiad.py --json PLIK       # to samo maszynowo, dla agenta
python3 zwiad.py --podglad PLIK    # dokladna roznica przed/po, bez zapisu
python3 zwiad.py --selftest
```
Kody wyjscia: 0 czysto | 1 sa skazenia | 2 sa skazenia NIENAPRAWIALNE.

### Kolejnosc, ktorej nie wolno odwracac (PROTOKOL par. 11)

```
1. zwiad.py PLIK           <- wiedza
2. cp PLIK PLIK.kopia      <- TWOJA kopia, nie narzedzia
3. zwiad.py --podglad PLIK <- co dokladnie sie zmieni
4. dopiero teraz naprawa
5. sprawdz, czy plik dziala
```

Kopia zapasowa nalezy do operatora. Zaglada robi wprawdzie wlasne
`.bak-*`, ale to jej mechanizm, nie twoje zabezpieczenie.

Majac zwiad i kopie, nieudana proba nie kosztuje nic poza czasem: wracasz
do kopii i probujesz inaczej. Liczba podejsc nie ma znaczenia - liczy sie
to, ze kazde opierasz na danych, a nie na zgadywaniu.

### Wachlarz naprawy (v9.4.0)

Ile faktycznie jest drog naprawy? Nie tyle, ile flag `--`. Pomiar (AST +
lektura dyspozytora `_przetworz_py`) dal **szesc**, w tym dwie niewidoczne
z linii polecen:

```
python3 zwiad.py --warianty PLIK
```

| Droga | Kiedy uzywana | Na pliku testowym |
|---|---|---|
| Pogromca `--fix` | zawsze dostepna | bez zmian (nie tyka liter) |
| Zaglada: poza literalami | `.py`, ktory sie kompiluje | 2 linie, literal ocalony |
| Zaglada: skaner surowy | `.py`, ktory NIE kompiluje sie | 2 linie |
| Zaglada: caly plik | ostatecznosc | 4 linie, `"Moskwa"` |
| Zaglada: przez USUNIECIE | ostatnia proba kaskady | **rozjazd nazw** |
| Anihilator | js/ts/java/go/rs/cs/c/cpp/php | nie dotyczy `.py` |

Dla `.py` Zaglada wykonuje **kaskade sama**: kompiluje sie -> poza
literalami; nie kompiluje -> surowy -> pelna -> usuwanie -> wariant
ostrozny. Operator nie wybiera z niej recznie, ale musi wiedziec, ze
istnieje - to tlumaczy, czemu ten sam plik bywa naprawiany roznie.

**Piaty wariant to RATOWNIK, nie usterka.** Przy pierwszym pomiarze
uznalem `_sprobuj_naprawy` za blad, bo na pliku z `c<U+043E>nter` dawal
`cnter` w definicji i `conter` w uzyciu. Bledna byla METODA pomiaru:
wywolalem funkcje bezposrednio na pliku, ktory **sie kompiluje** - a
kaskada siega po nia dopiero, gdy plik NIE kompiluje sie i zawiodly dwie
wczesniejsze proby. Pelna sciezka Zaglady na tym samym pliku daje
poprawne `conter`.

W swoim kontekscie ten wariant ratuje przypadki, ktorych transliteracja
naprawic NIE MOZE - bo sama lamie skladnie:

| Zepsute wejscie | Po ratunku | Uruchomienie |
|---|---|---|
| `i<U+043E>f True:` | `if True:` | dziala |
| `de<U+043E>f f():` | `def f():` | dziala |
| `if x =<U+043E>= 1:` | `if x == 1:` | dziala |

Trzy pliki nie do uratowania inna droga, wszystkie po naprawie uruchamiaja
sie poprawnie. To swiadomy piaty stopien kaskady.

Zwiad nadal ostrzega `!! ROZJAZD NAZW`, gdy wykryje ryzyko - ale dopisuje
kontekst: *"ten plik sie kompiluje, wiec kaskada Zaglady w ogole by tego
wariantu nie uzyla"*. Informacja zamiast falszywego alarmu.


## T7 - turniej wiarygodnosci zwiadu (v9.7.0)

Najwazniejszy turniej w repo, a powstal jako ostatni. `zwiad.py` nie mial
zadnego testu poza selftestem - a to na nim opiera sie KAZDA decyzja
agenta o naprawie.

Powod przeoczenia: turnieje T2-T6 pytaja **"czy narzedzie nie psuje
plikow"**. Na to pytanie zwiad odpowiada trywialnie - niczego nie
zapisuje, wiec nie moze zepsuc. Wygladal na przetestowany, bo pasowal do
kryterium, ktore go nie dotyczylo.

Wlasciwe pytanie brzmi: **czy nie wprowadza operatora w blad**. Awaria
zwiadu nie niszczy pliku - podsuwa agentowi falszywy obraz, na ktorym ten
sam podejmuje zla decyzje, z pelnym przekonaniem.

Szesc kategorii:

| | Co sprawdza |
|---|---|
| A. PRAWDOMOWNOSC | bierze PRZEWIDYWANIE zwiadu, uruchamia prawdziwe narzedzie na kopii, porownuje **bajt w bajt** (9 probek: py/js/proza, kod/literal/f-string) |
| B. KOMPLETNOSC | czy widzi KAZDE skazenie - przeoczenie to cisza, ktora operator czyta jako "czysto" |
| C. ROZDZIAL | kod vs dane; wnetrze f-stringa musi liczyc sie jako KOD, docstring jako DANE |
| D. ZERO ZAPISU | po pelnej analizie plik i katalog nietkniete (takze przez CLI) |
| E. OSTRZEZENIA | exit=2 przy utracie danych, wskazanie wlasciwego czlonka Gangu |
| F. ODPORNOSC | binarny, pusty, nie-UTF8, 60 tys. znakow w linii, zlamana skladnia, nieistniejacy |

**Zweryfikowany sabotazem 4/4:**

```
zwiad KLAMIE (symuluj zwraca oryginal)   -> 7 klamstw wykrytych
zwiad SLEPY (pomija co drugie skazenie)  -> exit 1
zwiad ZAPISUJE (lamie kontrakt)          -> naruszenie kontraktu
zwiad myli KOD z DANYMI                  -> 3 zle klasyfikacje
```

Kategoria A jest tu sednem: **przewidywanie rozne od rzeczywistosci jest
gorsze niz brak przewidywania**. Zwiad ma prawo powiedziec "nie wiem" -
nie ma prawa powiedziec czegos, co sie nie sprawdzi.

## v9.8.0 / Pogromca 8.7.0 - RYZYKO-KLUCZA ozywione

`[RYZYKO-KLUCZA]` to ostrzezenie, ktore od v8.1.0 **nie odpalilo sie ani
razu** - takze dla przykladu podanego w dokumentacji jego wlasnego autora.
Cztery rozne wejscia, zero trafien. Funkcja byla wolana i dzialala bez
bledu; po prostu zawsze zwracala pusta liste.

To gorsze niz brak funkcji: operator widzi cisze i wnioskuje "bezpiecznie".

### Co mial wykrywac

Zaglada slusznie nie rusza literalow (kontrakt: swiete). Ale gdy literal
pelni role KLUCZA - `d["niewidzialne"]`, `getattr(o, "pole")`,
`globals()[nazwa]` - i jest skazony, to plik **kompiluje sie czysto**
i wybucha dopiero w runtime. Zaden inny czlonek rodziny tego nie lapie.

### Dlaczego milczal

`_oczysc_kandydatow` mial dwie strategie i zadna nie odtwarzala oryginalu:

| Strategia | `"ni<U+0435>widzialne"` daje | szukamy |
|---|---|---|
| usuniecie znakow | `niwidzialne` | `niewidzialne` |
| NFKD + ascii | dziala dla `caf<U+00E9>` | ale to `UWAGA`, nie `BLAD` |

Petla wchodzi tylko przy `BLAD`. Przeciecie zbiorow "da sie oczyscic"
i "jest BLAD" bylo **puste**.

Powod byl zamierzony: autor napisal wprost *"bez wiedzy o tabelach
transliteracji Zaglady - Pogromca ma zostac bez zaleznosci od siostry"*.
Slusznie - ale bez tabeli nie da sie odgadnac, ze cyrylickie `<U+0435>`
odpowiada lacinskiemu `e`.

### Naprawa: dopasowanie pozycyjne

`_pasuje_pozycyjnie()` nie musi wiedziec, NA CO znak sie zamieni -
wystarczy, ze wie, GDZIE siedzi skazenie:

> ta sama dlugosc, a roznice **wylacznie** na pozycjach, gdzie literal ma
> znak zaklasyfikowany jako BLAD

Jedna roznica na znaku czystym dyskwalifikuje (`kot` vs `kos` to nie
trafienie). Zero zaleznosci od Zaglady - zalozenie autora zachowane.

| Miara | Wynik |
|---|---|
| przyklad z dokumentacji autora | **wykryty** (byl martwy od v8.1.0) |
| falszywe alarmy na 171 modulach stdlib | **0** |
| koszt | 9 ms/plik |
| regresja (turnieje + selftesty) | bez zmian |

Stara sciezka (`_oczysc_kandydatow`) zostaje jako pierwsza proba -
dopasowanie pozycyjne wchodzi dopiero, gdy tamta nie trafi.

## T8 - turniej bramek (v9.9.0)

Trzy narzedzia decyduja, czy wolno zrobic commit: `sprawdz-teksty.py`,
`sprawdz-spojnosc.py`, `pamietnik.py --sprawdz`. **Zadne nie mialo testu.**
Ta sama luka co przy zwiadzie: sprawdzam nimi wszystko, a ich samych nie
sprawdza nikt.

T8 znalazl **cztery wady na pierwszym uruchomieniu**:

| Wada | Skutek |
|---|---|
| `sprawdz-teksty` FAIL-OPEN | poza repo `git ls-files` zwraca pustke -> bramka melduje "0 plikow, zero kwiatkow" z exit 0. README z wstrzyknietym U+043E przechodzil **bez slowa** |
| pomijanie hurtem | cale `dev/turnieje/` i `dev/luki/` - 30 plikow, skazenia ma **5** |
| brief poza kontrola | `docs/BRIEF-DLA-AUDYTORA.md` **faktycznie klamal** o 2 wersjach, a idzie do zewnetrznego audytora |
| traceback | uszkodzony `WERSJE.json` -> stos wywolan zamiast komunikatu |

Wszystkie naprawione. Bramki sa teraz **fail-closed**: gdy nie wiedza, co
sprawdzic, odmawiaja (exit 2) zamiast meldowac sukces. Lista pomijanych
plikow jest imienna, z uzasadnieniem przy kazdym.

Przy okazji bramka o zawezonym zasiegu wykryla **prawdziwe skazenie**,
ktorego wczesniej nie widziala: probki BOM (U+FEFF) w `turniej-2`.

### Nauka o samym testowaniu

Pierwsza wersja T8 **przespala 2 z 3 sabotazy**. Sprawdzala tylko kod
wyjscia, a `exit=1` padal z innego powodu niz badany (dopisanie wpisu do
dziennika samo w sobie wywoluje "RUSZONY CUDZY DZIENNIK"). Po poprawce
test sprawdza TRESC komunikatu:

```
if kod != 1 or "brakuje pola" not in out:
```

Sabotaz po poprawce: **3/3 wykryte**.

Szesc kategorii: WYKRYWALNOSC (czy umie odmowic), ZERO SZUMU (czy milczy
na zdrowym repo), ZASIEG (czy pomija tylko to, co musi), ODPORNOSC,
UCZCIWOSC (exit zgodny z raportem).

## Hierarchia zaufania testow (v9.10.0)

Problem postawiony przez operatora: *"skoro poprawiles testy, sprawdz pod
tym katem reszte. Trzeba ustalic pierwszy pewny test."*

To problem fundamentu. Jesli test moze byc zepsuty, sprawdzanie testu
innym testem tylko przenosi watpliwosc dalej.

### Metoda: mutacja zamiast opinii

Jedyna mierzalna definicja wiarygodnosci:

> Test jest wiarygodny, gdy potrafi **OBLAC na zepsutym narzedziu**.
> Test przechodzacy na narzedziu z wycieta funkcja tej funkcji nie
> testuje - niezaleznie od tego, jak solidnie wyglada.

`dev/turnieje/pomiar-mutacyjny.py` wycina po jednej zdolnosci i sprawdza,
kto oblal. Wynik: **9 mutacji, 9 zlapanych, zero dziur.**

### POZIOM 0: `PogromcaKwiatkow.py --selftest`

Wybrany pomiarem, nie opinia - **ma najmniej rzeczy, ktore moga go
zawiesc**:

| | selftest Pogromcy | typowy turniej |
|---|---|---|
| `subprocess` | **nie** | tak |
| git | **nie** | tak |
| katalogi tymczasowe | **nie** | tak |
| inne narzedzia rodziny | **nie** | tak |
| probki | **`\uXXXX` w kodzie** | z dysku / generowane |

Zlapal wszystkie trzy mutacje fundamentu, w tym calkowita slepote
`klasyfikuj()`. Jego poprawnosc zalezy wylacznie od interpretera Pythona -
czyli od czegos **spoza tego repo**. To jest wyjscie z blednego kola.

### Kolejnosc uruchamiania

```
0  PogromcaKwiatkow.py --selftest      fundament, zero zaleznosci
1  pozostale selftesty                 kazde narzedzie w izolacji
2  tor-pogromcy, fuzz-pogromcy         bez subprocess i gita
3  T2, T3, Z1, Z2                      korpusy i wektory
4  T4, T5, T6                          subprocess
5  T7, T8                              + git + katalogi tymczasowe
```

**Gdy poziom oblewa, nie uruchamiaj wyzszych** - beda mierzyc zepsutym
przyrzadem.

Pelny opis wraz z wynikami: `docs/HIERARCHIA-ZAUFANIA-TESTOW.md`

## T9 - obcy kod z internetu (v9.12.0)

Pomysl operatora: wszystkie dotychczasowe turnieje uzywaly probek, ktore
**sami wytworzylismy**. Nawet weryfikacja na 40 modulach stdlib to kod
z tej samej instalacji Pythona. Brakowalo najtwardszej proby: wziac cudzy
kod, ktorego nikt nie widzial na oczy, skazic, naprawic i sprawdzic, czy
NADAL DZIALA.

`dev/turnieje/turniej-9-obcy-kod.py` pobiera prawdziwe pakiety z **PyPI**
(six, termcolor, inflection, shortuuid, wcwidth, natsort), skaza kod
wiernymi homoglifami i sprawdza trzy rzeczy naraz:

1. plik **kompiluje sie** po naprawie
2. **importuje sie** jako modul w osobnym procesie
3. jego **publiczne API jest identyczne** (`sorted(dir(m))` bajt w bajt)

Do tego dwa kryteria dodatkowe: **odwracalnosc** (skazenie bylo w pelni
odwracalne, wiec wynik musi rownac sie oryginalowi) i **kotwica
literalowa** (znak wstawiony w literal ma tam ZOSTAC - Zaglada nie rusza
danych w .py).

**Wynik: 51/51 plikow przezylo** (20 z pelnym uruchomieniem, 31 przez
porownanie drzewa AST - te wymagaja zainstalowanego pakietu).

Bez internetu turniej nie oblewa: schodzi na stdlib i mowi wprost, ze
pracuje w trybie zapasowym.

### Trzy bledy WLASNEGO testu, wykryte po drodze

Pisanie T9 bylo lekcja o testowaniu, nie o Gangu:

| Blad testu | Skutek |
|---|---|
| `skaz()` uzywal `_chronione_pozycje()` **badanego** modulu | skazenie omijalo dokladnie te miejsca, ktorych narzedzie nie umie obronic |
| homoglify wyliczane z `zamien_znak()` **badanego** modulu | po oslepieniu Zaglady cyrylica wypadla ze zbioru; sabotaz **sam sie ukryl** |
| lista 21 par litera-homoglif, z czego 10 **nieodwracalnych** | 33 falszywe alarmy na zdrowym Gangu (cyrylickie `c` daje `s`, nie `c`) |

Wniosek do dziennika: **dane wejsciowe testu trzymaj w stalej liscie
w kodzie testu, nie wyliczaj ich z badanego narzedzia.**

Zweryfikowany sabotazem: brak ochrony literalow -> **4 oblane**, slepota
na cyrylice -> **45 oblanych**, cofnieta naprawa f-string -> przechodzi
(i tak ma byc: T9 swiadomie nie skaza literalow, te klase pilnuja T4
i `luka-fstring`).

## v9.28.1 / pamietnik 2.1.3 - naprawa aktualizacji STAN-SESJI

Zmiana dokumentacji na wielkie litery w v9.20.0 zerwala cztery regexy
`pamietnik.py --stan`. Skrypt szukal malych etykiet tabeli, znajdowal
**zero**, mimo to wypisywal `[OK]`, zwracal kod 0 i pozostawial plik bez
zmian. Dlatego `STAN-SESJI.md` utknal na wersji 9.19.0 przy faktycznej
9.28.0.

Naprawa:

* etykiety tabeli sa dopasowywane bez wzgledu na wielkosc liter, wiec
  dzialaja zarowno w obecnym dokumencie, jak i w malym szablonie nowego domu;
* wszystkie cztery pola musza wystapic dokladnie raz;
* brak danych z gita lub `WERSJE.json`, brak pola albo duplikat konczy sie
  odmowa `exit 2`, bez czesciowej zmiany pliku;
* wynik jest budowany w pamieci i zapisywany atomowo przez `os.replace()`.

Test dodany najpierw i uruchomiony na starej implementacji: T8 wykryl
**2 naruszenia** (brak aktualizacji wielkich etykiet i brak odmowy na
niepelnej tabeli). Po naprawie: selftest pamietnika PASS, T8 8/8 prob
wykrywalnosci i zero naruszen. Kod czterech narzedzi rodziny nie byl
zmieniany, wiec medal nie zostal zresetowany.

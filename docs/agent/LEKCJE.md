# Lekcje — wiedza o narzędziu, nie o sesji

Agencie: to jest destylat z pracy nad tym repozytorium. **Jedzie z domem
Gangu** — jeśli kopiujesz narzędzie do siebie, kopiujesz też ten plik.
Nie ma tu nic o cudzej sesji, tylko o samym narzędziu i o pułapkach,
w które wpada się przy pracy z nim.

Liczby są prawdziwe i zostawione celowo. Bez nich to teoria, z nimi
widać skalę problemu.

Czym to **nie** jest: `dziennik/` to pamięć konkretnej sesji, a
`STAN-SESJI.md` to jej stan. Tamte zostają u autora. To tutaj jest dla
każdego.

---

## 1. Cicha awaria — jeden wzorzec pod wszystkim

Zanim przeczytasz szczegóły, zapamiętaj wzorzec, bo powtarza się
w każdej kategorii:

> **Coś raportuje sukces, a sukcesu nie ma.** Nie ma błędu, nie ma
> ostrzeżenia. Jest cisza, którą łatwo wziąć za „w porządku".

Zmierzone przykłady z tego repozytorium:

| Co mówiło „OK" | Co było naprawdę |
|---|---|
| `compile()` przeszedł | program padał w runtime (`NameError`) |
| turniej „0 popsutych na 390 plikach" | psuł co trzeci realny plik Pythona |
| test „WSZYSTKO ZDANE" | nie umiał oblać — nic nie mierzył |
| bramka „0 plików, zero kwiatków" | nie znalazła żadnego pliku do sprawdzenia |
| `git log` pokazywał jeden commit | klon był płytki, historia istniała |
| Prokurator „decyzja: ZAGŁADA" | plik nigdy nie został wyczyszczony |

**Wniosek operacyjny:** brak alarmu traktuj jak brak informacji, dopóki
nie wiesz, że alarm w ogóle działa.

---

## 2. Pisanie testów

### Test, który nie umie oblać, jest dekoracją

Jedyna mierzalna definicja wiarygodności testu:

> Test jest wiarygodny wtedy, gdy **przy zepsutym narzędziu OBLEWA**.

Po napisaniu testu zepsuj narzędzie i sprawdź, czy krzyknie. W tym
repozytorium dwa razy okazało się, że nowy turniej jest dekoracją:
jeden przespał **2 z 4** sabotaży, drugi **2 z 3**.

Narzędzia: `dev/turnieje/pomiar-mutacyjny.py` (czy w pokryciu są dziury),
`pomiar-per-turniej.py` (czy dana kategoria cokolwiek pilnuje).

### Nie sprawdzaj samego kodu wyjścia

`exit=1` mówi „coś jest nie tak", nie „to konkretne jest nie tak".
Przykład: test dopisywał wpis do dziennika i sprawdzał `exit`. Kod
wyjścia był poprawny — ale z **innego powodu** (dopisanie wpisu samo
w sobie zmienia plik i wywołuje inny alarm). Test przechodziłby nawet
z całkowicie wyłączoną kontrolą, którą miał badać.

Poprawnie:

```python
if kod != 1 or "brakuje pola" not in out:
```

### Pomiar globalny nie wystarcza

„Czy ktokolwiek złapał mutację" to za słabe pytanie. Rozkład bywa bardzo
nierówny — w pomiarze na tym repo jeden turniej złapał 6 z 9 mutacji,
a inny **zero**. Zero nie znaczyło, że jest zepsuty; żadna mutacja nie
celowała w jego obszar. Ale gdyby **był** dekoracją, wynik byłby
identyczny i nie dałoby się tego odróżnić.

Dlatego dla każdej pary (test, kategoria) wycinaj wadę, którą ta
kategoria ma wykrywać, i uruchamiaj **wyłącznie ten test**.

### Test nie może budować próbek narzędziem, które testuje

Najbardziej podstępna pułapka. Jeśli test pyta badany moduł „gdzie wolno
skazić" albo „jakie znaki są odwracalne", to **każda wada narzędzia
automatycznie usuwa z testu przypadek, który by ją wykrył**.

Zmierzone: po oślepieniu narzędzia na cyrylicę zbiór znaków testowych
skurczył się z 1010 do 962 pozycji — cyrylica z niego wypadła, test
przestał jej używać i meldował 51/51 na zepsutym narzędziu. **Sabotaż
sam się ukrył.**

Dane wejściowe testu trzymaj w **stałej liście w kodzie testu**.

### Skażenie testowe musi być odwracalne

Jeśli podmienisz literę na znak, który transliteruje się na **inną**
literę (cyrylickie `<U+0441>` daje `s`, nie `c`), niszczysz informację **przed**
testem. Żadne narzędzie jej nie odtworzy — mierzysz własny błąd.

Zmierzone: lista 21 par litera-homoglif, z czego 10 nieodwracalnych,
dała **33 fałszywe alarmy** na zdrowym narzędziu.

Buduj zbiór **wiernych** homoglifów: takich, dla których funkcja zamiany
zwraca dokładnie oryginalną literę ASCII. Jest ich około 52.

### `compile()` to za słabe kryterium

Obie poważne klasy błędów, jakie te narzędzia potrafią wprowadzić,
`compile()` **przechodzą**:

* rozjazd nazwy (definicja naprawiona, użycie nie) → `NameError`
* niespójność identyfikatorów → `AttributeError`

Składnia zostaje poprawna, program pada dopiero przy uruchomieniu.
Właściwe kryterium to **uruchom i porównaj wyjście** — wzór:
`dev/turnieje/turniej-4-runtime.py`.

### Wykrycie to za mało — sprawdzaj, na CO zamienił

Test pytający „czy zgłosił skażenie" i „czy plik jest czysty" przepuści
narzędzie, które **usuwa** znak zamiast go transliterować:
`c<U+043E>nter` -> `cnter` zamiast `conter`. Plik czysty, kompiluje się, a nazwa
zmiennej po cichu inna.

Zawsze porównuj z **dokładnym oczekiwanym tekstem**.

### Amunicja syntetyczna omija konstrukcje z prawdziwego kodu

Generatory próbek pisze się „z głowy", a głowa produkuje proste
przypadki. Zmierzone: **żadna** z ośmiu próbek turniejowych nie
zawierała f-stringa ze zmienną — a taki f-string występuje w **58 ze 171
(34%)** modułów biblioteki standardowej Pythona.

Testuj też na prawdziwym kodzie: stdlib leży w
`sysconfig.get_paths()['stdlib']`, a pakiety da się pobrać z PyPI
(wzór: `dev/turnieje/turniej-9-obcy-kod.py`).

### Narzędzie decyzyjne wymaga innego kryterium

Turnieje pytają „czy narzędzie nie psuje plików". Narzędzie, które
niczego nie zapisuje (jak `zwiad.py`), odpowiada na to trywialnie —
i wygląda na przetestowane, choć nie jest sprawdzone wcale.

Dla takiego narzędzia pytanie brzmi: **czy nie wprowadza operatora
w błąd**. Jego awaria nie niszczy pliku — podsuwa fałszywy obraz,
na którym operator sam podejmuje złą decyzję z pełnym przekonaniem.

### Zielony wynik lokalnie nic nie dowodzi o ścieżkach

Turniej potrafi przechodzić w katalogu repo i oblewać na świeżym klonie
w innym miejscu na dysku. Przyczyną bywa ścieżka względna, która
przypadkiem działała, bo repo i plik testowy leżały w tym samym drzewie.

Uruchamiaj testy **także** na świeżym klonie, w katalogu o pustym
rodzicu.

### Fuzz czyta katalog nadrzędny

Jeśli test szuka korpusu „wokół repo", złapie też twoje pliki robocze
z katalogu wyżej. Spadek wyniku po zmianie w kodzie może nie być
regresją, tylko zanieczyszczeniem.

Zanim uznasz spadek za regresję: powtórz na czystym klonie **bez** swojej
zmiany. Ten sam wynik = wina otoczenia.

---

## 3. Praca z kodem rodziny

### Wzorzec kaskady — to nie duplikaty

W kilku miejscach znajdziesz parę: `funkcja` i `funkcja_surowy`. To nie
przypadkowe kopie, tylko świadomy wzorzec:

```
plik się kompiluje    -> tokenize (dokładny, zna literały)
nie kompiluje się     -> własny skaner stanów
każdy krok            -> bramka compile()
nic nie pomogło       -> wariant OSTROŻNY (lepiej nie naprawić niż zepsuć)
```

Zanim zgłosisz duplikat — sprawdź **warunek wywołania**.

### Zanim nazwiesz coś błędem, znajdź miejsce wywołania

Funkcja oceniona w izolacji potrafi wyglądać na wadliwą, a w swoim
kontekście być ratunkiem. Przykład z tego repo: funkcja usuwająca znaki
zamiast transliterować wygląda groźnie — ale wchodzi **wyłącznie** przy
potrójnym warunku (plik nie kompiluje się ORAZ dwie wcześniejsze próby
zawiodły) i ratuje przypadki, których transliteracja naprawić nie może,
bo sama łamie składnię: `i<U+043E>f` -> `if`, `de<U+043E>f` -> `def`, `=<U+043E>=` -> `==`.

`grep -n nazwa_funkcji` i odtworzenie warunku zajmuje minutę.

### Nie ufaj komentarzom przy ocenie, co kod robi

Znaleziony przypadek: komentarz obiecywał heurystykę („jeśli w detalu
jest cudzysłów, to prawdopodobnie literał"), a w kodzie jej **nigdy nie
zaimplementowano**. Skutek: jedna z głównych funkcji nie działała
w ogóle, a wyglądała na przemyślaną.

Sprawdzaj zachowaniem albo przez AST.

### Ostrzeżenie, które milczy, jest gorsze niż jego brak

Funkcja ostrzegawcza w tym repo nie odpaliła się **ani razu** — także
dla przykładu podanego w dokumentacji jej własnego autora. Była
wywoływana, działała bez błędu, zawsze zwracała pustą listę.

Operator widzi ciszę i wnioskuje „bezpiecznie". Jeśli dodajesz
ostrzeżenie, dodaj też test, który sprawdza, że **potrafi się odpalić**.

### Wersja Pythona zmienia zachowanie tokenizera

Tokeny `FSTRING_START/MIDDLE/END` istnieją od **3.12**. Na 3.11 cały
f-string wraca jako jeden token `STRING` — i kod, który zakłada
rozbicie, po cichu obsługuje wnętrze f-stringa jako dane, nie kod.

`hasattr(tokenize, "FSTRING_START")` przed założeniem, że ścieżka działa.

### `SequenceMatcher` na całym pliku jest kwadratowy

Zmierzone: plik 99 kB → **3 min 23 s** przy rdzeniu liczącym 0,285 s.
Wygląda jak zawieszenie.

Jeśli operacja nie zmienia liczby linii, licz diff **per linia**:
ta sama poprawność, **0,137 s** zamiast 3 minut. Zostaw awaryjny powrót
do wariantu globalnego, gdyby liczba linii się jednak różniła.

### Nie każda funkcja jest czysta

Funkcja o nazwie sugerującej przeliczenie potrafi **zapisywać na dysk**.
W tym repo `napraw()` robi kopię `.bak` i podmienia plik — wywołana do
symulacji rzuca `ODMOWA ZAPISU`.

Przed użyciem cudzej funkcji do podglądu: `grep -n "open(.*w\|zapisz"`
wokół jej ciała.

### Narzędzia rodziny nie wiedzą o sobie

Zmierzone wywołania: tylko jedno narzędzie woła rodzeństwo. Pozostałe
nie wiedzą o swoim istnieniu — w tym o narzędziu do języków innych niż
Python, którego **nie zna nikt**.

To nie usterka, tylko konsekwencja projektu (proste, niezależne
narzędzia). Ale obowiązek spada na operatora: do plików `.js` i podobnych
uruchamiasz właściwe narzędzie **ręcznie**.

Cena pomyłki jest mierzalna: ten sam plik `.js` z rosyjskim tekstem
w literale — jedną drogą literał ocaleje, drugą zostanie przetłumaczony
na alfabet łaciński.

### Kopie tablic znaków się rozjeżdżają

Dwa narzędzia trzymają własne kopie tablic. Zmierzone: **24 znaki** dają
różny wynik — jedno transliteruje `U+0407` na `Ji`, drugie usuwa.

Zmieniasz tablicę? Zmieniaj w **obu** plikach i porównaj zbiory.

---

## 4. Środowisko i narzędzia pracy

### Heredoc zjada cudzysłowy

Wstrzyknięcie kodu przez `python3 - <<'PY'` potrafi „udać się"
(`składnia OK`, selftest PASS), a do pliku nie trafia **nic** — bo kod
zawierał `'''`, `"""` i backslashe, które poszły przez kilka warstw
cytowania.

Kod z cudzysłowami zapisuj **plikiem**, potem wykonaj skrypt operujący
na tym pliku. I weryfikuj po fakcie (`grep -c`), nie po komunikacie.

### Potok zjada kod wyjścia

```
python3 test.py 2>&1 | tail -5 ; echo $?     # to kod `tail`, nie testu
python3 test.py >/dev/null 2>&1 ; echo $?    # dopiero to jest prawda
```

### Lokalne repo potrafi się cofnąć

`git log` pokazuje wtedy tylko pierwszy commit, reflog wygląda jak po
świeżym klonie. Praca wypchnięta na zdalny **przetrwa**:

```
git fetch origin <gałąź> && git reset --hard FETCH_HEAD
```

Niezacommitowane zmiany z bieżącej tury przepadają. Commituj często.

### Płytki klon kłamie pewnie

`git merge-base --is-ancestor` na płytkim klonie (`.git/shallow`) odpowie
„nie", choć powinno „tak" — bo git nie ma pełnej historii. Odpowiedź jest
stanowcza i błędna.

Przy pytaniach o przodków sprawdź `ls .git/shallow` albo zapytaj API
serwera.

### Każdy `mkdtemp` w `try/finally`

Katalog tymczasowy bez sprzątania to wyciek. Zmierzone: selftest
zostawiał 1 kB przy każdym uruchomieniu — **26 katalogów** w jednej
sesji. Mało miejsca, ale to wyciek w narzędziu, które ma pilnować
porządku.

Sprzątaj też ręczne kopie robocze od razu, nie „na koniec".

---

## 5. Dokumentacja i bramki

### Dokument o skażeniach sam je roznosi

Przykłady skażeń zapisuj notacją `<U+XXXX>`, **nigdy żywcem**. Inaczej
następny agent skopiuje fragment i przeniesie problem dalej.

To nie jest teoretyczne: w tym repozytorium agent wpisał **16 żywych
homoglifów do trzech dokumentów ostrzegających przed homoglifami** i nie
zauważył tego przy żadnym z kilku przeglądów. Siedemnastego wyłapał
człowiek.

Po napisaniu każdego dokumentu: `python3 sprawdz-teksty.py`.

### Bramka musi być fail-closed

Zmierzony przypadek: poza repozytorium `git ls-files` zwraca pustkę,
pętla nie wykonuje ani jednego obiegu, bramka melduje **„0 plików, zero
kwiatków"** z kodem 0. Plik z wstrzykniętym skażeniem przechodził bez
słowa.

Gdy narzędzie kontrolne nie wie, co sprawdzić — musi **odmówić**
(`exit 2`), nie meldować sukces.

### Listy wyjątków trzymaj imiennie

Pomijanie całymi katalogami rośnie po cichu. Zmierzone: lista obejmowała
30 plików, a skażenia miało **5**. Pozostałe 25 przechodziło bez
sprawdzenia bez żadnego powodu.

Wymieniaj plik po pliku, z uzasadnieniem przy każdym.

### Wersja żyje w czterech miejscach

Stała w kodzie, plik z wersjami, teksty dokumentacji, osadzone kopie
kodu. Kolejność: kod → plik wersji → teksty → re-embed → bramka →
przeliczenie manifestu.

### Re-embed rób od końca pliku

Podmiana pierwszego bloku przesuwa offsety wszystkich następnych.
Iteruj po markerach **od końca** (`range(n-1, -1, -1)`).

### README to punkt wejścia, nie kronika

Kolejne wydania dopisują sekcje na koniec, bo tam wygodnie. Zmierzone:
960 linii, z czego **838 to historia** (87%). Agent szukający „jak tego
użyć" musi się przez to przekopać.

Historia ma własny plik. README odpowiada na „jak to działa **teraz**".

---

## 6. Praca z człowiekiem

### Kod od zewnętrznego audytora uruchom, zanim ocenisz

Kod potrafi wyglądać kompetentnie, mieć poprawny rdzeń — i być
bezużyteczny przez kontakt z rzeczywistością. Zmierzony przypadek:
narzędzie kontrolne od zewnętrznego audytora zgłosiło **94 rozjazdy na
czystym repozytorium** i żądało pliku, którego nigdy tam nie było.

Zawsze: najpierw AST (czy nie zapisuje, nie woła `subprocess`, nie
`eval`), potem uruchomienie **na kopii**.

### Nie zgaduj, gdy nie wiesz, czym jest dana treść

Gdy narzędzie sygnalizuje utratę danych (znaki nieodwracalne, do
usunięcia) i nie wiesz, czy to skażenie, czy treść użytkownika —
**zapytaj człowieka**. Usunięcie chińskiego tekstu ze strony jest
technicznie naprawą, a faktycznie szkodą.

### Naprawa i kosmetyka w osobnych commitach

Sprzątanie wygląda niewinnie, więc wpada do commita razem ze zmianą
logiki. Potem nie da się cofnąć samej naprawy bez cofania kosmetyki.

---

## Jak korzystać z tego pliku

Nie musisz go pamiętać. Musisz wiedzieć, że istnieje — i wracać do niego,
gdy coś nie działa tak, jak powinno. Duża część tych lekcji brzmi
oczywiście **po** przeczytaniu, a nie była oczywista wcześniej.

Prowadź własny dziennik (`python3 pamietnik.py --dodaj`). Gdy trafisz na
coś, co dotyczy **narzędzia**, a nie twojej sesji — dopisz to tutaj.

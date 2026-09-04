# PAMIETNIK OPERATORA — grabie, na ktore juz ktos nadepnal

Agencie: to nie jest dokumentacja. Dokumentacja mowi, jak system **ma**
dzialac (README, PROTOKOL-OPERATORA). Pamietnik mowi, co **naprawde sie
stalo** komus, kto tu pracowal przed toba — zwlaszcza wtedy, gdy sie
pomylil.

Czytasz to, zeby nie stracic godziny na blad, ktory ktos juz raz zrobil.
Piszesz tu, gdy sam stracisz godzine na cos, czego nie dalo sie przewidziec
z samej dokumentacji.

---

## Jak dopisywac wpisy

Uzyj narzedzia — pilnuje formatu i daty:

```
python3 pamietnik.py --dodaj
```

Albo dopisz recznie na **koncu** wlasciwej sekcji, w tym formacie:

```markdown
### [RRRR-MM-DD] Krotki tytul — czego dotyczy
**Objaw:** co zobaczyles (konkretny komunikat, zachowanie, liczba).
**Przyczyna:** dlaczego tak bylo.
**Wniosek:** co robic nastepnym razem.
```

Zasady, ktore czynia ten plik uzytecznym zamiast smietnikiem:

1. **Tylko rzeczy nieoczywiste z dokumentacji.** Jesli README to mowi, nie
   powtarzaj. Tu trafia to, co README przemilcza.
2. **Objaw musi byc konkretny.** Nie „testy sie sypaly", tylko
   „`FINAL T5: REGRESJA — 8 naruszen`".
3. **Wniosek musi byc czynnoscia.** Nie „trzeba uwazac", tylko „rob X, nie Y".
4. **Nie kasuj cudzych wpisow.** Jesli wpis sie zdezaktualizowal, dopisz pod
   nim `**Nieaktualne od <data>:** ...` i zostaw. Historia pomylek tez uczy.
5. **Nie wpisuj sukcesow.** Od chwalenia sie jest README i docs/. Tu tylko
   to, co ugryzlo.

---

## 1. Praca z repozytorium i narzedziami agenta

### [2026-09-04] Lokalne repo potrafi sie cofnac w trakcie sesji
**Objaw:** w polowie pracy `git log` pokazal HEAD na `eb1deb0`, a commity
`30ca6fd`, `1d1575c`, `f1aa85f` zniknely. `git cat-file` mowil „Not a valid
object name". Reflog zawieral tylko `clone` i `checkout` — jakby repo
dopiero co sklonowano.
**Przyczyna:** nieustalona; nie bylo to polecenie agenta ani usera.
**Wniosek:** praca wypchnieta na origin przetrwala w calosci — ratunek to
`git fetch origin <branch>` + `git reset --hard FETCH_HEAD`. Ale
**niezacommitowane zmiany z biezacej tury przepadaja**. Commituj i pushuj
czesto, a przed duza operacja skopiuj nowe pliki poza repo (`/tmp/`).

### [2026-09-04] Heredoc w bashu zjada cudzyslowy w kodzie Pythona
**Objaw:** wszczepienie funkcji przez `python3 - <<'PY'` „udalo sie"
(`skladnia OK`, selftest PASS), ale `grep -c "_kod_we_fstringu"` zwrocil
**0** — do pliku nie trafilo nic. W stderr mignal `SyntaxError:
unterminated string literal`.
**Przyczyna:** kod zawieral `'''`, `"""` i backslashe, ktore poszly przez
kilka warstw cytowania.
**Wniosek:** kodu zawierajacego cudzyslowy **nie wstrzykuj przez heredoc**.
Zapisz go narzedziem do pliku (`write_file`), potem wykonaj skrypt
operujacy na tym pliku. I **zawsze weryfikuj po fakcie** (`grep -c`), a nie
po komunikacie „OK" — komunikat moze pochodzic z czegos innego.

### [2026-09-04] Pipe zjada kod wyjscia
**Objaw:** `python3 turniej.py 2>&1 | tail -14; echo $?` pokazywalo `exit=0`
mimo widocznego `REGRESJA`.
**Przyczyna:** `$?` to kod ostatniego elementu potoku (`tail`), nie skryptu.
**Wniosek:** kod wyjscia sprawdzaj bez potoku:
`python3 turniej.py >/dev/null 2>&1; echo $?`.

---

## 2. Pisanie testow dla tej rodziny

### [2026-09-04] Test, ktory nie umie oblac, jest bezwartosciowy
**Objaw:** nowy turniej T5 dla Anihilatora od razu dal „WSZYSTKO ZDANE".
Wygladalo na sukces. Po sabotazu narzedzia (celowe wylaczenie ochrony
literalow) **dalej** dawal „WSZYSTKO ZDANE" — przespal 2 z 4 sabotazy.
**Przyczyna:** probki testowe uzywaly wylacznie polskich znakow, a te sa
w zbiorze `DOZWOLONE`. Przetrwaja nawet przy **calkowicie wylaczonej**
ochronie literalow, wiec niczego nie sprawdzaly.
**Wniosek:** po napisaniu testu **zepsuj narzedzie celowo** i sprawdz, ze
test oblewa. Do sprawdzania ochrony literalow uzywaj znakow, ktore narzedzie
NAPRAWDE zmienia (cyrylica, greka, CJK) — np. rosyjska nazwe miasta zapisana
przez `"\u041c\u043e\u0441\u043a\u0432\u0430"` w probce. Polskie ogonki sie
do tego nie nadaja.
(Dowody zapisujemy w notacji `\uXXXX`, nie zywcem — patrz wpis nizej
o samym pamietniku.)

### [2026-09-04] Wykrycie skazenia to za malo — sprawdzaj, na CO zamienil
**Objaw:** sabotaz „slepota na cyrylice" przechodzil przez kategorie
wykrywania bez jednego bledu.
**Przyczyna:** test pytal „czy zglosil skazenie" i „czy plik jest czysty".
Obie odpowiedzi byly na TAK, bo znak zostal **usuniety** zamiast
przetransliterowany: `c<U+043E>nter` -> `cnter` zamiast `conter`. Plik czysty,
kompiluje sie, a nazwa zmiennej po cichu inna.
**Wniosek:** zawsze sprawdzaj **doklandy oczekiwany tekst wyjsciowy**, nie
tylko „czy skazenie zniklo".

### [2026-09-04] `compile()` nie wystarcza jako kryterium niepsucia
**Objaw:** turnieje T3 i Z2 pokazywaly „0 popsutych" na 390 plikach, a
Zaglada psula co trzeci realny plik Pythona.
**Przyczyna:** oba turnieje uznawaly plik za caly, jesli przechodzil
`compile()`. Tymczasem obie powazne klasy bledow, jakie te narzedzia
wprowadzaja, `compile()` **przechodza**: rozjazd nazwy w f-stringu daje
`NameError`, niespojnosc identyfikatorow daje `AttributeError`. Skladnia
pozostaje poprawna.
**Wniosek:** kryterium jest **uruchomienie programu i porownanie wyjscia**
przed i po. Wzor: `dev/turnieje/turniej-4-runtime.py`.

### [2026-09-04] Amunicja syntetyczna nie zawiera konstrukcji z prawdziwego kodu
**Objaw:** zadna z 8 probek turniejowych nie zawierala f-stringa ze zmienna
(zmierzone automatem: 0 wystapien).
**Przyczyna:** generatory probek pisze sie „z glowy", a glowa produkuje
proste przypadki. F-string ze zmienna wystepuje w **58/171 = 34%** modulow
biblioteki standardowej.
**Wniosek:** testuj na **prawdziwym kodzie** — biblioteka standardowa
Pythona lezy w `sysconfig.get_paths()['stdlib']` i ma 171 gotowych modulow.
Wzor uzycia w `docs/INZYNIERIA-WSTECZNA.md`.

### [2026-09-04] Skazenie testowe musi byc ODWRACALNE, inaczej oskarzasz niewinnego
**Objaw:** pierwszy przebieg testu na stdlib dal katastrofe: 13 plikow nie
kompilowalo sie po Zagladzie, 9 nie importowalo.
**Przyczyna:** blad **testu**, nie narzedzia. Podmienialem losowe litery na
losowe znaki — np. `s` na cyrylickie `<U+0440>`, ktore transliteruje sie na `r`.
Informacja zostala zniszczona przeze mnie **przed** uruchomieniem narzedzia;
zadne narzedzie by jej nie odtworzylo.
**Wniosek:** buduj zbior **wiernych homoglifow** — takich, dla ktorych
`zamien_znak()` zwraca dokladnie oryginalna litere ASCII (jest ich 52).
Dopiero wtedy zadanie „odtworz oryginal" jest wykonalne, a wynik mierzy
narzedzie, a nie twoj generator.

---

## 3. Pulapki w samym kodzie rodziny

### [2026-09-04] W AnihilatorChwastow.py ta sama funkcja jest zdefiniowana DWA RAZY
**Objaw:** `zaglada_tekst_poza_literalami_multi` w linii **191** i znowu
w linii **429**. Poprawka naniesiona na pierwsza nie robi nic.
**Przyczyna:** Python czyta plik z gory na dol — druga definicja nadpisuje
pierwsza. Sprawdzone empirycznie: `raise RuntimeError` wstawiony na poczatek
tej z linii 191 **nie wybuchl**, selftest dal 9/9 PASS.
**Wniosek:** edytujesz te funkcje? Uzywaj tej z linii **429** (aktywnej).
Przed edycja dowolnej funkcji w tym pliku sprawdz:
`grep -n "^def <nazwa>" AnihilatorChwastow.py` — jesli sa dwa trafienia,
liczy sie ostatnie.

### [2026-09-04] Wersja Pythona zmienia zachowanie tokenizera f-stringow
**Objaw:** kod obslugiwal `FSTRING_START/MIDDLE/END`, a mimo to caly
f-string byl chroniony jako jeden literal.
**Przyczyna:** te tokeny istnieja dopiero od **Pythona 3.12**. Na 3.11
(i starszych) caly f-string wraca jako pojedynczy token `STRING`.
**Wniosek:** sprawdz `hasattr(tokenize, "FSTRING_START")` zanim uznasz, ze
sciezka dziala. Kod musi radzic sobie w obu swiatach.

### [2026-09-04] `SequenceMatcher` na calym pliku jest kwadratowy
**Objaw:** czyszczenie `argparse.py` (99 KB) trwalo **3 min 23 s** przy
rdzeniu liczacym 0.285 s. Wygladalo jak zawieszenie.
**Przyczyna:** `difflib.SequenceMatcher(None, a, b, autojunk=False)` znak
po znaku na calym pliku: 1.67 mld operacji `dict.get`.
**Wniosek:** czyszczenie nie zmienia liczby linii, wiec diff licz **per
linia** (`_zmiany_znakowe` w Zagladzie) — 0.137 s, wynik identyczny.
Zawsze zostaw awaryjny powrot do wariantu globalnego, gdy liczba linii sie
jednak rozni.

### [2026-09-04] Komentarz obiecywal heurystyke, ktorej nie bylo w kodzie
**Objaw:** `--wykonaj` Prokuratora NIGDY nie czyscil plikow `.py`.
**Przyczyna:** w kodzie stalo `elif is_py:` -> POUCZENIE dla kazdego
skazonego Pythona. Komentarz tuz obok mowil „jesli w detail jest cudzyslow,
to prawdopodobnie literal" — heurystyki nigdy nie zaimplementowano.
**Wniosek:** nie ufaj komentarzom przy ocenie, co kod robi. Sprawdzaj
zachowaniem (uruchom) albo AST. Ten sam blad moze siedziec gdzie indziej.

---

## 4. Dokumentacja i bramka spojnosci

### [2026-09-04] Re-embed do RODZINA-DO-CZATU.md rob OD KONCA pliku
**Objaw:** po podmianie osadzonych kopii bramka zglosila
`osadzona kopia PogromcaKwiatkow.py ROZJECHANA (103625 B vs 38694 B)` oraz
`nie osadza ZagladaKultury.py` — plik zostal rozwalony.
**Przyczyna:** podmiana pierwszego bloku przesunela offsety wszystkich
nastepnych markerow, a petla szla od poczatku.
**Wniosek:** iteruj po markerach `### <Nazwa>.py` **od konca** (`range(n-1,
-1, -1)`) — wtedy offsety wczesniejszych blokow sie nie zmieniaja.
Nie tnij po ogrodzeniach ```` ``` ````, bo osadzony kod ich nie ma.

### [2026-09-04] Bramka spojnosci zlapala blad agenta na goracym uczynku
**Objaw:** j.w. — `python3 sprawdz-spojnosc.py` natychmiast pokazal rozjazd
rozmiarow osadzonych kopii.
**Przyczyna:** dziala, bo porownuje sha256 realnego pliku z osadzona kopia.
**Wniosek:** **uruchamiaj `python3 sprawdz-spojnosc.py` po kazdej zmianie
w plikach narzedzi lub dokumentacji, przed commitem.** Zero rozjazdow to
warunek wejscia. To najtansza siatka bezpieczenstwa w tym repo.

### [2026-09-04] Zmiana kodu = podbicie wersji w CZTERECH miejscach
**Objaw:** bramka wyrzucila 12 rozjazdow po podbiciu samej stalej `WERSJA`.
**Przyczyna:** numer wersji zyje w: (1) stalej `WERSJA` w pliku `.py`,
(2) `WERSJE.json`, (3) tekscie README/PROTOKOL/docs, (4) osadzonej kopii
w `docs/RODZINA-DO-CZATU.md`.
**Wniosek:** kolejnosc: popraw kod -> `WERSJA` -> `WERSJE.json` -> teksty
-> re-embed -> `sprawdz-spojnosc.py` -> przelicz `docs/KOMPLECIK.md`.
Pamietaj tez o zasadzie projektu: **poprawka kodu = reset medalu/turnieju**.

---

### [2026-09-04] Pamietnik tez podlega Pogromcy - zero zywych kwiatkow w dokumentach
**Objaw:** Swiezo napisany PAMIETNIK-OPERATORA.md dostal od Pogromcy [BLAD]: 8 znakow CYRYLICA w linii 90.
**Przyczyna:** Wpis o testowaniu ochrony literalow zawieral przyklad z rosyjska nazwa miasta wpisana ZYWCEM. Przyklad byl celowy, ale dokument staje sie wtedy nosnikiem tego, przed czym repo ostrzega - a nastepny agent kopiujacy fragment przenosi skazenie dalej.
**Wniosek:** Znaki obcych alfabetow w dokumentacji zapisuj notacja \uXXXX albo U+XXXX, nigdy zywcem (PROTOKOL par. 5). Po napisaniu KAZDEGO nowego dokumentu uruchom: python3 PogromcaKwiatkow.py <plik>

## 5. Wspolpraca z operatorem-czlowiekiem

### [2026-09-04] Zalaczniki od usera nie docieraja do agenta
**Objaw:** user zapowiedzial analize od zewnetrznego audytora; katalog
`/home/user/uploads/` **nie istnieje**, plikow nigdzie nie bylo.
**Przyczyna:** srodowisko nie przekazuje zalacznikow do sandboxa.
**Wniosek:** popros o **wklejenie tresci wprost do czatu**. Nie zgaduj, co
mogl zawierac zalacznik — zrob wlasna, niezalezna analize i powiedz wprost,
na czym ja opierasz.

### [2026-09-04] „Nie ruszamy dzialajacego kodu, dokladamy kolejny"
**Objaw:** zasada z repo, latwa do zlamania w dobrej wierze przy
„porzadkowaniu".
**Przyczyna:** sprzatanie wyglada niewinnie, wiec wpada do commita razem ze
zmiana logiki. Potem nie da sie cofnac samej naprawy bez cofania kosmetyki.
**Wniosek:** naprawa bledu = tak. Kosmetyka (usuwanie martwego kodu,
przeformatowania) w tym samym commicie co zmiana logiki = nie — utrudnia
cofniecie naprawy. Rozdzielaj commity. Przed zmiana w rodzinie zrob kopie
poza repo (`cp *.py /tmp/backup-rodziny/`).

### [2026-09-04] Agent sam wstawia kwiatki do tekstu - takze do zdan o kwiatkach
**Objaw:** User wylapal w odpowiedzi agenta na czacie slowo 'z realnymi grabiami', gdzie 'gra' to trzy znaki CYRYLICY (U+0433 U+0440 U+0430) doklejone do lacinskiego 'biami'. Kontrolny skan repo znalazl 16 kolejnych zywych homoglifow w trzech dokumentach napisanych przez agenta w tej samej sesji (INZYNIERIA-WSTECZNA, LUKI-W-TESTACH, NAPRAWA-v8.6.0).
**Przyczyna:** Dokladnie mechanizm opisany w SZYBKI-START: model generuje token po tokenie i przy slowach zawierajacych a/e/o/c/p potrafi wskoczyc w zly alfabet. Agent NIE widzi tego u siebie ani przy pisaniu, ani przy wlasnym przegladzie. Tu doszlo sprzezenie: im wiecej agent pisal O cyrylicy, tym czesciej mu sie wstawiala.
**Wniosek:** Nie ufaj wlasnemu tekstowi. Po napisaniu KAZDEGO dokumentu i przed KAZDYM commitem uruchom: python3 PogromcaKwiatkow.py $(git ls-files). Przyklady skazen w dokumentacji zapisuj wylacznie notacja <U+XXXX>, nigdy zywcem - inaczej dokument o kwiatkach sam roznosi kwiatki. Dotyczy to takze tekstu wysylanego na czat, ktorego zaden skaner nie sprawdza.

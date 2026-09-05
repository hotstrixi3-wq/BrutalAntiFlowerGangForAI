# Brief dla zewnetrznego audytora AI

Ten plik jest do **skopiowania w calosci** do czatu z innym agentem
(Claude Pro, ChatGPT, Gemini) razem z `docs/RODZINA-DO-CZATU.md`.

Powstal, bo nie ma technicznego mostu miedzy sesjami roznych agentow —
mostem jest czlowiek z kopiuj-wklej. Zeby ten most nie gubil kontekstu,
audytor musi dostac trzy rzeczy: **stan repo, co juz sprawdzono, i czego
NIE przyjmowac na wiare**.

---

## Wiadomosc do wklejenia (kopiuj od tej linii w dol)

```
Jestes niezaleznym audytorem. Sprawdzasz prace innego agenta AI nad
repozytorium BrutalAntiFlowerGangForAI (github.com/hotstrixi3-wq/
BrutalAntiFlowerGangForAI, galaz arena/01a06e18-brutalantiflowergangforai).

CZYM JEST TO REPO
Rodzina 4 narzedzi w Pythonie, ktore wykrywaja i usuwaja z kodu i tekstu
"kwiatki" — znaki z obcych alfabetow udajace lacinke (cyrylickie "o"
U+043E wyglada jak lacinskie "o"), znaki niewidzialne i twarde spacje.
Problem jest realny: modele jezykowe wstawiaja takie znaki samoistnie,
generujac token po tokenie, i nie widza tego u siebie.

  PogromcaKwiatkow.py  v8.7.0  — detektor (oczy), niczego nie zmienia
  ZagladaKultury.py    v1.4.0  — czysci .py/.json/proze (rece)
  ProkuratorOgrodnik.py v1.3.1 — orkiestrator + polityka (mozg)
  AnihilatorChwastow.py v1.4.0 — czysci js/ts/java/go/rs/cs/c/cpp/php

KLUCZOWA TEZA DO PODWAZENIA
"Gang nie psuje kodu" — czyszczenie nigdy nie zmienia dzialania programu.
Teza byla weryfikowana na 40 modulach biblioteki standardowej Pythona:
0 niekompilujacych sie, 40/40 importuje sie z identycznym publicznym API.
NIE PRZYJMUJ TEGO NA WIARE. W tej samej sesji teza zostala JUZ RAZ ZLAMANA
(patrz nizej) — szukaj kolejnych wylomow.

CO ZOSTALO ZNALEZIONE I NAPRAWIONE W TEJ SESJI
1. LUKA F-STRING (krytyczna, lamala teze). Ochrona literalow traktowala
   caly f-string jako dane, ale wnetrze pol {...} to KOD. Definicja
   zmiennej byla czyszczona, uzycie w f-stringu nie:
       PRZED:  vo = 7 ; print(f"wynik: {vo}")   -> dziala
       PO:     v  = 7 ; print(f"wynik: {vo}")   -> NameError
   (gdzie "o" w "vo" to cyrylickie U+043E)
   compile() PRZECHODZIL, wiec bramki tego nie widzialy. To samo w JS:
   template literal ${...}. Naprawione, 5/5 wariantow.
2. WYDAJNOSC: diff znak-po-znaku na calym pliku byl kwadratowy.
   argparse.py (99 KB) = 3 min 23 s. Po zmianie na diff per linia: 0.137 s.
3. PROKURATOR: --wykonaj NIGDY nie czyscil plikow .py (warunek "elif is_py:"
   dawal POUCZENIE kazdemu Pythonowi; komentarz obiecywal heurystyke,
   ktorej nie zaimplementowano). Oraz: pliki nie-UTF8 dostawaly normalna
   decyzje zamiast BLOKADY, bo Pogromca czyta z errors="replace" i
   uszkodzony bajt wracal jako U+FFFD.
4. Agent wstawil 16 ZYWYCH homoglifow do trzech dokumentow OSTRZEGAJACYCH
   przed homoglifami. Stad nowa bramka sprawdz-teksty.py.

CZEGO SZUKAM OD CIEBIE (w kolejnosci waznosci)
a) KOLEJNE WYLOMY W TEZIE. Konstrukcje jezykowe, gdzie granica
   kod/dane jest nieoczywista i narzedzie moze ja przeciac. F-string byl
   jednym takim miejscem — gdzie sa nastepne? Rozwaz: dekoratory ze
   stringami, __all__, getattr po nazwie w stringu, docstringi uzywane
   jako dane (doctest), adnotacje typow w cudzyslowach, eval/exec,
   %-formatowanie, .format(), stringi w f-stringach zagniezdzonych,
   pickle, nazwy pol w dataclass, klucze slownikow uzywane jako
   identyfikatory, JSX/TSX, dekoratory Javy, atrybuty C#.
b) BLEDY W LOGICE POLITYKI Prokuratora (kto decyduje o czyszczeniu
   cudzych plikow — tam blad = zniszczone dane usera).
c) MARTWY KOD I ROZJAZDY. Wiadomo o jednym: w AnihilatorChwastow.py
   funkcja zaglada_tekst_poza_literalami_multi jest zdefiniowana DWA RAZY
   (linia 191 i 429) — dziala tylko druga. Sa inne takie?
d) SLABE MIEJSCA W TESTACH. Turnieje: T2 (992 wektory), T3 (190 plikow),
   Z1 (1545), Z2 (200), T4 runtime, T5 Anihilator, T6 Prokurator.
   Zasada, ktora przyjelismy: test ktory nie umie OBLAC jest
   bezwartosciowy — kazdy nowy turniej byl weryfikowany sabotazem
   (celowe zepsucie narzedzia, sprawdzenie ze test to lapie).
   Gdzie te turnieje nadal maja slepe plamy?

ZASADY, KTORE OBOWIAZUJA W TYM REPO
- "Nie ruszamy dzialajacego kodu, dokladamy kolejny."
- Poprawka kodu = reset medalu/turnieju (trzeba przejsc regresje od nowa).
- Dowody skazen w dokumentacji zapisujemy notacja <U+XXXX>, NIGDY zywcem —
  inaczej dokument o kwiatkach sam je roznosi.
- Wersja zyje w 4 miejscach: stala WERSJA, WERSJE.json, teksty docs,
  osadzona kopia w docs/RODZINA-DO-CZATU.md. Pilnuje sprawdz-spojnosc.py.

CZEGO NIE ROBIC
- Nie przyjmuj powyzszych ustalen na wiare — sprawdz kod.
- Nie proponuj przepisania calosci. Repo ma dzialajace narzedzia i
  komplet testow; interesuja mnie konkretne, wskazane palcem bledy.
- Jesli czegos nie da sie stwierdzic bez uruchomienia — powiedz to wprost
  zamiast zgadywac. Moge uruchomic i przyniesc wynik.

FORMAT ODPOWIEDZI
Dla kazdego znaleziska: (1) plik i linia, (2) na czym polega blad,
(3) minimalny przyklad odtwarzajacy, (4) czy compile()/skladnia to lapie,
(5) proponowana naprawa. Posortuj wg wagi. Jesli czegos nie znalazles
w danej kategorii — napisz to zamiast dopisywac watpliwe pozycje.
```

---

## WARIANT A (lepszy): katalog na dysku jako most

Jesli Twoj audytor ma dostep do katalogu na Twoim komputerze — nie wklejaj
kodu. Zrob z tego katalogu **klon repozytorium**. Wtedy audytor czyta
prawdziwe pliki (nie wklejke, ktora moze byc obcieta), a jego ustalenia
wracaja do tej sesji przez git.

### Raz, u siebie na komputerze

```
cd <katalog-ktory-widzi-Twoj-audytor>
git clone https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI.git
cd BrutalAntiFlowerGangForAI
git checkout arena/01a06e18-brutalantiflowergangforai
```

Repo wazy okolo 2 MB — klonowanie trwa chwile.

### Przed kazdym audytem (zeby audytor mial swiezy stan)

```
git pull
```

### Wiadomosc dla audytora przy tym wariancie

Zamiast zalacznika napisz mu:

```
Kod masz w katalogu BrutalAntiFlowerGangForAI (galaz
arena/01a06e18-brutalantiflowergangforai). Czytaj pliki bezposrednio,
nie polegaj na moim opisie.

Zacznij od:
  README.md                     - co robi rodzina
  docs/BRIEF-DLA-AUDYTORA.md    - kontekst audytu i czego szukam
  dziennik/                     - czego juz probowano i co nie wyszlo
  docs/NAPRAWA-v8.6.0.md        - uzasadnienia ostatnich decyzji

Mozesz uruchamiac testy, zeby sprawdzic swoje hipotezy:
  python3 PogromcaKwiatkow.py --selftest
  python3 dev/turnieje/turniej-4-runtime.py
  python3 dev/luki/luka-fstring.py

Wynik zapisz do NOWEGO pliku:
  docs/audyt-zewnetrzny/RRRR-MM-DD__claude-pro.md
Format opisany w docs/audyt-zewnetrzny/README.md.
NIE zmieniaj innych plikow — mam bramki, ktore to wykryja.
```

### Powrot do tej sesji

Masz dwie drogi:

**1. Przez git (zalecana).** U siebie:
```
git add docs/audyt-zewnetrzny/
git commit -m "audyt zewnetrzny: Claude Pro"
git push origin arena/01a06e18-brutalantiflowergangforai
```
Potem napisz mi w czacie „audytor wrzucil plik" — pobiore i zweryfikuje.

**2. Przez wklejke.** Otworz plik z `docs/audyt-zewnetrzny/` i wklej tresc
tutaj. Dziala tak samo, tylko bez historii w gicie.

**Zaleta wariantu A:** audytor moze URUCHOMIC kod i sprawdzic wlasna
hipoteze, zamiast zgadywac z lektury. Roznica w jakosci znalezisk jest duza.

---

## WARIANT B: kopiuj-wklej (gdy nie ma wspolnego katalogu)

## Co zalaczyc do wiadomosci

| Cel | Plik | Uwaga |
|---|---|---|
| Pelny kod 4 narzedzi | `docs/RODZINA-DO-CZATU.md` | 123 500 znakow — zawiera komplet kodu, moze przekroczyc limit wklejki; wtedy zalacz jako plik |
| Sam kod jednego narzedzia | np. `ZagladaKultury.py` | gdy audyt ma byc waski |
| Historia pomylek | `dziennik/` | pokazuje, czego juz probowano |
| Stan i decyzje | `docs/NAPRAWA-v8.6.0.md` | uzasadnienia inzynierskie |

Alternatywa dla wklejania: podaj link do repo i galezi. Agent z dostepem
do sieci pobierze pliki sam.

## Jak wrocic z odpowiedzia

Wklej odpowiedz audytora **w calosci** do tej sesji. Nie streszczaj —
streszczenie gubi numery linii i przyklady, a to jest najcenniejsza czesc.
Kazde znalezisko zostanie zweryfikowane **wykonaniem** (uruchomieniem kodu),
zanim cokolwiek zmienimy: w tej sesji zdarzyly sie juz zarzuty, ktore po
sprawdzeniu okazaly sie nietrafione, i takie, ktore okazaly sie powazniejsze
niz zgloszono.

# Czym jest Gang i po co — dla agenta, ktory go uzyje

Agencie: przeczytaj to, ZANIM uruchomisz cokolwiek na pliku uzytkownika.
Nie jest to instrukcja obslugi (ta jest w README). To jest odpowiedz na
pytanie, po co ten program istnieje i czym jest **dla ciebie** — bo od
tego zalezy, czy uzyjesz go dobrze, czy zrobisz komus szkode.

---

## 1. To jest proteza na twoja slepote

Nie na slepote uzytkownika. Na **twoja**.

Generujesz tekst token po tokenie. Cyrylica, greka i lacinka maja litery
o identycznym ksztalcie: `a` `e` `o` `p` `c` `x`. Token o wspolnym
ksztalcie potrafi wskoczyc w zly alfabet — bez ostrzezenia, bez bledu.
Powstaje `c<U+043E>nter` zamiast `counter`. Wyglada tak samo. **Nie jest
tym samym.**

I teraz rzecz najwazniejsza: **ty tego u siebie nie widzisz**. Nie
w momencie pisania i nie przy wlasnym przegladzie, bo przeglad robi ta
sama maszyna, ktora to wstawila. To nie kwestia starannosci. Uwazniejsze
czytanie nic nie da.

Nie jest to teoria. W sesji, w ktorej powstal ten dokument, agent:

* wpisal **16 zywych homoglifow do trzech dokumentow OSTRZEGAJACYCH przed
  homoglifami** — i nie zauwazyl przy zadnym z kilku przegladow;
* wyslal siedemnastego czlowiekowi w zdaniu na czacie; **wylapal go
  czlowiek, nie agent**;
* im wiecej pisal O cyrylicy, tym czesciej mu sie wstawiala.

Gang jest jedyna rzecza w tym repozytorium, ktora widzi to, czego ty
z definicji nie zobaczysz. Traktuj go jak przyrzad pomiarowy, nie jak
udogodnienie.

---

## 2. To sa OCZY, nie automat do sprzatania

Latwo pomylic te dwie role. Roznica jest zasadnicza.

**Automat** dostaje plik i go naprawia; twoja rola to pilnowac, zeby nie
nawalil. **Oczy** daja ci obraz; decyzje podejmujesz ty i ty za nia
odpowiadasz.

Gang jest tym drugim. Wynika z tego definicja slowa, ktore znajdziesz
w calej dokumentacji:

> **"Sprytny i nieomylny" nie znaczy "zawsze naprawi dobrze".
> Znaczy: NIE WPROWADZI CIE W BLAD. Pokaze prawde.**

Dlatego istnieje `zwiad.py`, ktory **niczego nie zapisuje** i nigdy nie
bedzie. Jego jedynym zadaniem jest dac ci wiedze przed decyzja.

---

## 3. Nie ma jednej naprawy — jest wybor, ktory nalezy do ciebie

Rodzina ma cztery narzedzia o roznej sile. Ten sam plik naprawiony
roznymi drogami daje **rozne pliki wynikowe**. Zmierzone na pliku ze
skazeniem w kodzie, w komentarzu i w rosyjskim literale:

| Droga | Kiedy | Rosyjski literal |
|---|---|---|
| Pogromca `--fix` | zawsze | nietkniety (nie tyka liter) |
| Zaglada: poza literalami | `.py` kompilujacy sie | nietkniety |
| Zaglada: skaner surowy | `.py` zepsuty | nietkniety |
| Zaglada: caly plik | ostatecznosc | `"Moskwa"` |
| Zaglada: przez usuniecie | ostatnia proba kaskady | nietkniety, ale **rozjazd nazw** |
| Anihilator | js/ts/java/go/rs/cs/c/cpp/php | zalezy od jezyka |

Szesc drog, nie cztery - policzone przez AST i lekture dyspozytora,
nie po liczbie flag `--`.

Zadna z tych drog nie jest "domyslnie sluszna". Pogromca **celowo** nie
tyka liter — kwiatka nie maskujemy, decyzja nalezy do czlowieka. Wariant
surowy **celowo** czysci wszystko.

Ktora jest dobra? Zalezy, **czym jest ten rosyjski tekst**: przypadkowym
skazeniem czy trescia, ktora uzytkownik tam umiescil. **Narzedzie tego nie
wie. Ty musisz wiedziec** — a jak nie wiesz, masz zapytac czlowieka.

Zobacz wszystkie drogi naraz: `python3 zwiad.py --warianty PLIK`

---

## 3a. Oni nie wiedza o sobie — TY masz wiedziec, ze sa

Zmierzone (`grep` po wywolaniach miedzy plikami):

```
Pogromca    -> nikogo nie wola
Zaglada     -> nikogo nie wola
Anihilator  -> nikogo nie wola
Prokurator  -> Pogromca (detekcja) + Zaglada (naprawa)
```

**Anihilatora nie zna NIKT.** Prokurator ma zero wystapien tej nazwy.

To nie jest usterka rodziny — narzedzia maja byc proste i niezalezne.
To jest **obowiazek operatora**: skoro one nie wiedza o sobie, to ty
musisz wiedziec, ze sa, i ktore pasuje do czego.

Cena pomylki jest mierzalna. Plik `.js` ze skazeniem w kodzie i rosyjskim
tekstem w literale:

| Droga | Kod | Literal uzytkownika |
|---|---|---|
| `Prokurator --wykonaj` | naprawiony | **`"Moskwa"` — ZNISZCZONY** |
| `Anihilator --anihilacja` | naprawiony | `"<U+041C>..."` — OCALONY |

Prokurator nie zna Anihilatora, wiec `.js` wysyla do Zaglady, a ta nie
rozumie skladni JavaScriptu i traktuje plik jak proze. Kod wychodzi
poprawny w obu wypadkach — **roznica dotyczy DANYCH uzytkownika**.

Mapa, ktora musisz miec w glowie:

| Plik | Kto wlasciwy |
|---|---|
| `.py`, `.json` | Zaglada (albo Prokurator `--wykonaj`) |
| `.js .ts .java .go .rs .cs .c .cpp .php` | **Anihilator — recznie** |
| `.md .txt` i inna proza | Zaglada |
| `.html .css` | Zaglada, ale OSTROZNIE — nikt nie traktuje ich jak kodu |

Nie musisz jej pamietac: `python3 zwiad.py --warianty PLIK` wypisuje
**KTO Z GANGU DO TEGO PLIKU** wraz z ostrzezeniem, gdy grozi pomylka.

## 4. Kopia zapasowa nalezy do CIEBIE

Zaglada i Anihilator robia wlasne pliki `.bak-*`. **To nie jest twoje
zabezpieczenie** — to ich wewnetrzny mechanizm, ktory chroni przed ich
wlasna awaria zapisu, a nie przed twoja zla decyzja.

Na pliku uzytkownika kopie robisz **ty**, zanim cokolwiek uruchomisz.

To jest tez zasada domu, zapisana przez autora repo wielkimi literami:
**ZAWSZE ROB BAKAP**.

---

## 5. Kolejnosc, ktorej nie wolno odwrocic

Najpierw **wiedza**, potem kopia, dopiero na koncu naprawa. Konkretne
komendy: `PROTOKOL-OPERATORA.md` par. 2.

**Nigdy nie uruchamiaj naprawy po to, zeby dowiedziec sie, co ona robi.**
To zgadywanie z konsekwencjami na cudzym dysku.

Majac zwiad i kopie, nieudana proba nie kosztuje nic poza czasem:
wracasz do kopii i wybierasz inna droge. Liczba podejsc nie ma znaczenia —
liczy sie, ze kazde opierasz na danych, a nie na przeczuciu. Proba na
slepo bywa gorsza od zadnej: niszczy plik i nie zostawia wiedzy.

---

## 6. Jak zle uzyjesz narzedzia, to jest TWOJA wina

Zasada operatora, dosownie:

> "Jak zle uzyjesz narzedzia, to jest twoja wina."

Nie narzedzia. Nie autora. Nie uzytkownika, ktory "nie uprzedzil".

Gang ma bezpieczniki — fail-closed przy plikach, ktorych nie rozumie,
blokade na nieczytelnym kodowaniu, ochrone literalow, kopie zapasowe.
Ale **zaden bezpiecznik nie zastapi decyzji**. Narzedzie zrobi to, o co
je poprosisz. Jesli poprosisz o zla rzecz, zrobi zla rzecz — poprawnie.

Z tego wynika obowiazek, ktorego nie da sie zdjac: **masz wiedziec, co
robisz, zanim to zrobisz**. Zwiad daje ci do tego wszystko, czego
potrzebujesz. Nie masz wymowki.

Gdy zwiad pokaze `exit=2` (znaki NIENAPRAWIALNE, ktore zostana usuniete
bezpowrotnie) i nie jestes pewien, czy to skazenie czy tresc uzytkownika —
**nie zgaduj. Zapytaj czlowieka.** Usuniecie chinskiego tekstu ze strony
internetowej jest technicznie "naprawa", a faktycznie szkoda.

---

## 7. Zostaw slad dla nastepnego

Nastepny agent bedzie mial dokladnie ta sama slepote co ty. Jedyne, czego
nie bedzie mial, to twoje doswiadczenie — chyba ze mu je zostawisz.

Jak zamknac sesje i co zapisac: `PROTOKOL-OPERATORA.md` par. 8.

---

## W jednym zdaniu

**Gang to twoje oczy na wlasna slepote; daje ci prawde i wachlarz drog,
ale decyzje i odpowiedzialnosc zostawia tobie — wiec rob kopie, patrz
zanim tkniesz, a jak nie wiesz, pytaj czlowieka.**

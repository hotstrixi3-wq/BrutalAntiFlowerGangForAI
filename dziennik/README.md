# dziennik/ — jak to dziala

Jeden plik na sesje agenta:

```
dziennik/2026-09-04__01a06e18.md
         ^data        ^identyfikator sesji (z galezi gita)
```

## Trzy zasady

**1. Piszesz tylko do swojego pliku.**
Tworzy sie sam przy pierwszym `--dodaj`. Nie musisz go zakladac recznie ani
zgadywac nazwy — narzedzie bierze date i identyfikator sesji z galezi
(albo ze zmiennej `PAMIETNIK_SESJA`).

**2. Cudze pliki sa tylko do odczytu.**
`python3 pamietnik.py --sprawdz` porownuje `dziennik/` z gitem i zglasza
kazda zmiane w cudzym pliku, na samej gorze listy problemow. W gicie nie ma
technicznej blokady zapisu — chodzi o **wykrywalnosc**: nikt nie podmieni
cudzego wpisu tak, zeby bramka tego nie zauwazyla przed commitem.

**3. Ale wolno prostowac.**
Rada sprzed roku moze byc nieaktualna. Nie edytujesz wtedy cudzego pliku —
dopisujesz **wlasny** wpis z polem:

```markdown
**Zastepuje:** Lokalne repo potrafi sie cofnac w trakcie sesji
```

Widok scalony oznaczy tamten wpis jako `[NIEAKTUALNY]` i pokaze, co go
zastapilo. Zla rada przestaje szkodzic, a historia pomylki zostaje —
bo to, ze cos kiedys bylo problemem, tez jest informacja.

## Dlaczego nie jeden wspolny plik

Probowalismy (v1.0.0, jeden `PAMIETNIK-OPERATORA.md`). Trzy problemy:
konflikty przy rownoleglych sesjach, kuszenie do „poprawiania" cudzych
wpisow, i brak odpowiedzi na pytanie „kto to napisal i kiedy".

## Dlaczego mimo to jest widok scalony

Trzydziesci osobnych plikow to trzydziesci plikow, ktorych nikt nie
otworzy. Dlatego `python3 pamietnik.py` **scala wszystkie sesje** w jeden
widok pogrupowany tematami, a `PAMIETNIK-OPERATORA.md` w korzeniu jest
generowanym spisem tresci calosci. Rozdzial na pliki to sprawa zapisu;
czytanie zawsze odbywa sie na calosci.

## Polecenia

```
python3 pamietnik.py                  # widok scalony, wszystkie sesje
python3 pamietnik.py --temat testy    # jeden temat
python3 pamietnik.py --szukaj SLOWO   # przeszukaj wszystko
python3 pamietnik.py --sesje          # kto pisal, ile wpisow
python3 pamietnik.py --moje           # tylko twoja sesja
python3 pamietnik.py --dodaj          # dopisz (pyta o pola)
python3 pamietnik.py --sprawdz        # bramka: format + nietykalnosc
python3 pamietnik.py --indeks         # odswiez spis w korzeniu
```

Tematy: `repo`, `testy`, `kod`, `dokumentacja`, `wspolpraca`.

## Co wpisywac

Tylko rzeczy **nieoczywiste z dokumentacji** — to, co kosztowalo czas
i czego nie dalo sie przewidziec z README. Kazdy wpis ma trzy obowiazkowe
pola: **Objaw** (konkretny: komunikat, liczba), **Przyczyna**, **Wniosek**
(czynnosc do wykonania nastepnym razem).

Nie wpisuj sukcesow — od tego jest README i `docs/`.

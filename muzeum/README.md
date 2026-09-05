# Muzeum

**Tu nie ma plików. Są tylko tablice po tych, których już nie ma.**

Agencie: to miejsce cię nie dotyczy. Nic tu nie działa, nic stąd nie
kopiuj, niczego tu nie szukaj. Zajrzysz tylko wtedy, gdy zadasz pytanie
„czy coś takiego kiedyś istniało i dlaczego zniknęło".

Poza tym jednym przypadkiem — **omijaj**.

---

## Jak to działa

Plik, który przestał służyć, **zostaje skasowany**. Naprawdę usunięty
z drzewa. Ale zanim zniknie, dostaje tutaj wpis:

* czym był,
* co wnosił, gdy jeszcze wnosił,
* dlaczego przestał,
* skąd go wyciągnąć, gdyby ktoś jednak potrzebował.

To wszystko. Żadnych kopii, żadnych archiwów „na wszelki wypadek".
Katalog waży tyle, co ten plik — i tyle ma ważyć zawsze.

## Dlaczego tak, a nie magazyn

Magazyn nieużywanych plików rośnie i nikt go nie opróżnia, bo skoro coś
tam trafiło zamiast zniknąć, to znaczy, że ktoś się wahał. Po roku to
wysypisko udające archiwum — a agent, który tam zajrzy, marnuje czas na
ustalanie, co jest żywe, a co nie.

Git już przechowuje wszystko. Kasowanie pliku to nie zniszczenie, tylko
**przeniesienie go do historii**. Sprawdzone: plik usunięty dwadzieścia
commitów temu wraca jedną komendą.

Brakowało tylko **wskazówki, gdzie szukać i po co** — i to jest jedyna
rzecz, którą to muzeum robi.

## Zasada wpisu

Wpis powstaje **razem z kasowaniem**, w tym samym commicie. Nigdy
osobno — inaczej albo plik zniknie bez śladu, albo tablica zostanie po
czymś, co wciąż żyje.

**Sprawdź komendę odzysku, zanim ją wpiszesz.** Ścieżka musi pochodzić
z commita **sprzed** kasacji, nie z tego, w którym plik znika. Pomyliłem
to przy pierwszej tablicy — komenda wyglądała sensownie i nie działała.

---

## Tablice

### `docs/logi/` — surowe logi przebiegów ciągłych

*Skasowane: 2026-09-05, commit `dcc72cc`.*
*Odzysk: `git show dcc72cc:muzeum/logi-petli/petla-rodzinna.log`*
*(sprawdzone — komenda dziala; sciezka jest z commita SPRZED kasacji,
nie z tego, w ktorym plik zniknal)*

**Czym było:** wyjście z `petla-rodzinna.py` i `petla-turniejowa.py` —
skryptów uruchamiających komplet sprawdzianów w kółko przez 20 minut.
Każda linia to jeden cykl: `CYKL 1: 7/7 zielone (1194 s do konca)`.
Dwa pliki, 14 kB.

**Co wnosiło:** dowód stabilności przy długim działaniu — że narzędzia
nie sypią się po setnym uruchomieniu i nie cieknie im pamięć. W czasie,
gdy nie było jeszcze turniejów T4–T9, to była jedyna forma testu
wytrzymałościowego.

**Dlaczego przestało:** wnioski z tych przebiegów są opisane w
`docs/dowody/MEDAL-PEWNIAKA-v8.0.2.md` i `RAPORT-V8-PETLA-BONUS.md` —
tam jest liczba cykli i werdykt. Sam log to półprodukt: 200 powtórzeń
tej samej linii, zero odwołań ze strefy agenta (zmierzone), zero
odpowiedzi na jakiekolwiek pytanie.

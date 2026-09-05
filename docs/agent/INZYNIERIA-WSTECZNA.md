# Inzynieria wsteczna Gangu — analiza calosciowa

Data: 2026-09-04 · Stan repo: commit `448004b` (v8.5.0)

Dokument powstal metoda **empiryczna**: wnioski pochodza z AST kodu i z
URUCHOMIENIA narzedzi na prawdziwych plikach, a nie z dokstringow.
Kazda liczba nizej jest wynikiem wykonanego testu.

---

## 1. Cel istnienia

Gang rozwiazuje jeden problem: **tekst wygladajacy na ASCII, ktory nim nie jest**.

Model jezykowy albo wklejka z sieci potrafi wstawic do kodu cyrylickie `<U+0430>`
(U+0430) zamiast `a`, greckie `<U+03BF>` zamiast `o`, twarda spacje zamiast spacji,
zero-width space w srodku nazwy zmiennej. Efekt: kod wyglada poprawnie na
ekranie, a nie dziala — albo, gorzej, dziala inaczej niz wyglada.
`NameError: name 'diet' is not defined. Did you mean: 'dict'?` przy nazwie,
ktora na ekranie jest napisana `dict`.

Gang wykrywa takie znaki i przywraca ASCII.

## 2. Zalozenie naczelne i dlaczego jest nieoczywiste

> Narzedzie czyszczace kod nie ma prawa tego kodu zepsuc.

To zalozenie jest trudniejsze, niz brzmi, bo naiwne czyszczenie psuje kod
na trzy sposoby naraz:

1. **Podmiana w literale** — `print("cena: 5 zl")` z cyrylickim `<U+0441>` w slowie
   polskim. Zamiana zmienia DANE programu, nie jego kod.
2. **Rozbicie tokena** — twarda spacja miedzy `def` a nazwa: wstawienie
   zwyklej spacji naprawia, ale twarda spacja W SRODKU nazwy zamieniona na
   spacje rozwala skladnie na zawsze. Dlatego `zamien_znak(kod=True)`
   twarde spacje **usuwa**, nie zamienia.
3. **Niespojnosc nazw** — najgrozniejszy. `self._scandir_path` w trzech
   miejscach i `self._VIIIscandir_patKh` w czwartym (U+2167 rzymska osemka
   rozwinieta przez NFKC na `VIII`). Po transliteracji plik **kompiluje sie
   poprawnie** i wybucha `AttributeError` dopiero w runtime.
   `compile()` tego nie widzi — sprawdza skladnie, nie spojnosc nazw.

Odpowiedzia na (3) jest `_napraw_niespojnosc_identyfikatorow` (v1.1.0),
uruchamiana jako OSTATNIA kontrola nawet gdy `compile()` przeszlo za
pierwszym razem.

## 3. Architektura — kto kim jest

Cztery narzedzia, podzial na **oczy**, **rece** i **mozg**:

| Narzedzie | Rola | Zakres | Pisze po plikach? |
|---|---|---|---|
| `PogromcaKwiatkow.py` 8.4.0 | oczy (detektor) | wszystko | tylko z `--fix` |
| `ZagladaKultury.py` 1.3.0 | rece | `.py`, `.json`, proza | tak |
| `AnihilatorChwastow.py` 1.3.0 | rece | js/ts/java/go/rs/cs/c/cpp/php | tak |
| `ProkuratorOgrodnik.py` 1.2.0 | mozg (orkiestrator) | decyduje i wola pozostalych | posrednio |

**Wspolny prefiks wszystkich czterech**: `WERSJA`, `_KOPIE`,
`jest_kopia_zapasowa()` — zabezpieczenie przed przetwarzaniem wlasnych
kopii `.bak-*`. Bez tego drugie uruchomienie zjadaloby backupy.

**Przeplyw miedzy narzedziami** (Prokurator jako dyrygent):

```
ProkuratorOgrodnik.main
  ├─ sciezka_rodzenstwa()        # znajduje rodzenstwo obok siebie na dysku
  ├─ run_pogromca()              # subprocess -> PogromcaKwiatkow.py
  │    └─ parse_pogromca_output() -> rozwiaz_sciezke_z_raportu()
  ├─ classify_findings()         # match_allowlist + notacja_uxxxx
  │                              # (akta bez ZYWYCH znakow — raport o skazeniu
  │                              #  sam nie moze byc skazony)
  └─ run_zaglada_if_allowed()    # subprocess -> ZagladaKultury.py
       polityka: UMORZONE / POUCZENIE / ZAGLADA / BLOKADA
```

Rozdzielenie oczu od rak jest celowe: wykrycie nie oznacza zgody na zapis.
Decyzje podejmuje Prokurator, na podstawie `ALLOWLIST_GLOBS` i
`ALLOWLIST_CLASSES_FOR_I18N` (plik i18n z pelna cyrylica to nie jest skazenie).

## 4. Warstwy ochronne — pieciokrotna bramka

Kolejnosc, w jakiej kod broni sie przed wlasna pomylka:

1. **`jest_kopia_zapasowa()`** — nie dotykaj `.bak-*`.
2. **`wykryj_nieobslugiwane()`** (Anihilator) — *fail-closed*: nieznana
   skladnia => `BlokadaAnihilatora`, zero zapisu. Lepiej nie zrobic nic
   niz zrobic zle.
3. **`_chronione_pozycje()` / `_regiony_literalow()`** — literaly i
   komentarze sa poza zasiegiem podmiany.
4. **Bramka `compile()`** — kandydat nie wchodzi na dysk, jesli sie nie
   kompiluje. Trzy warianty proboawane po kolei (ostrozny surowy => pelny
   => `_sprobuj_naprawy` z usuwaniem zamiast transliteracji).
5. **`_napraw_niespojnosc_identyfikatorow()`** — kontrola PO compile,
   opisana w pkt 2.3.

Dopiero potem `zapisz_bezpiecznie()`: backup + zapis atomowy.

---

## 5. WERYFIKACJA TEZY: czy Gang psuje kod?

Teza do sprawdzenia: *kod musi sie kompilowac i dzialac po uzyciu Gangu*.

### Metodyka

Testy repo (turnieje w `dev/`) operuja na plikach syntetycznych. Zeby nie
ufac wlasnej amunicji, wziolem **prawdziwe moduly biblioteki standardowej
Pythona 3.11** (171 dostepnych), skazil je i przepuscil przez Zaglade.

Kluczowa poprawka metodyczna w trakcie: pierwsze podejscie skazalo pliki
znakami takimi jak cyrylickie `<U+0440>` -> transliterowane na `r`, podczas gdy
oryginalem bylo `s`. Taki test jest **nieuczciwy** — informacja zostala
zniszczona przeze mnie, zadne narzedzie jej nie odtworzy. Dlatego
zbudowalem zbior **52 wiernych homoglifow**: znakow, dla ktorych
`zamien_znak()` zwraca DOKLADNIE oryginalna litere ASCII. Dopiero wtedy
zadanie „odtworz oryginal" jest wykonalne i test mierzy narzedzie,
a nie moj generator.

### Wyniki — 40 modulow stdlib, 6 wiernych homoglifow + 2 znaki niewidzialne na plik

| Miara | Wynik |
|---|---|
| plikow zbadanych | 40 |
| **nie kompiluje sie po Zagladzie** | **0** |
| identyczny bajt-w-bajt z oryginalem | 2 |
| kompiluje sie, ale rozni sie od oryginalu | 38 |

Roznica w 38 plikach wymagala wyjasnienia. Analiza `tokenize` — gdzie
dokladnie leza te roznice:

| Lokalizacja roznicy | Liczba plikow |
|---|---|
| tylko w literalach i komentarzach | **38** |
| **w kodzie wykonywalnym** | **0** |

Czyli: Zaglada **nie ruszyla ani jednego znaku kodu wykonywalnego**.
Roznice to skazenia, ktore moj generator wstrzyknal w stringi i komentarze
— a tam Gang celowo nie wchodzi (warstwa 3). To nie jest defekt,
to zadzialana ochrona danych.

### Test najostrzejszy — czy to sie URUCHAMIA

Kompilacja to za malo (patrz pkt 2.3 — `AttributeError` przechodzi przez
`compile()`). Kazdy modul zostal zaimportowany w osobnym procesie
i porownany zostal jego pelny publiczny interfejs (`dir()`) przed i po:

| Miara | Wynik |
|---|---|
| modulow uruchomionych | 40 |
| **importuje sie + IDENTYCZNE publiczne API** | **40 / 40** |
| awarie runtime | **0** |

**Teza potwierdzona.** Na prawdziwym kodzie produkcyjnym, przy skazeniu
odwracalnym, Zaglada nie zepsula ani jednego pliku: wszystko sie kompiluje,
wszystko sie importuje, publiczne API bez zmian.

---

## 6. Znaleziska

### Z1 (WYDAJNOSC, istotne) — kwadratowy diff zawiesza duze pliki

Podczas testow `ZagladaKultury.py --zaglada` na module `argparse.py`
(99 612 znakow) **nie zakonczyla sie w 120 s**. Pomiar dokladny:

```
real  3m23s   <- caly plik przez CLI
```

Profil wskazuje jednoznacznie:

```
ncalls  tottime  funkcja
     8  405.577  difflib.py:305(find_longest_match)
1673047249  139.068  {method 'get' of 'dict' objects}
     1    0.002  ZagladaKultury.py:350(_napraw_niespojnosc_identyfikatorow)  cumtime 544.7
```

1,67 **miliarda** operacji slownikowych. Zrodlo — linia 371:

```python
sm = difflib.SequenceMatcher(None, oryginal, kandydat, autojunk=False)
```

`SequenceMatcher` na calym pliku **znak po znaku** z `autojunk=False` ma
zlozonosc kwadratowa. Zmierzone skalowanie:

| rozmiar pliku | czas diffa |
|---|---|
| 5 000 | 0.27 s |
| 10 000 | 1.84 s |
| 20 000 | 10.61 s |
| 40 000 | 28.00 s |
| 80 000 | 116.86 s |

Dla porownania sam rdzen czyszczacy to 0.285 s — narzut ~700x.
Poprawnosc jest zachowana (funkcja *dziala*), ale plik ~100 KB wyglada
jak zawieszenie, a plik kilkusetkilobajtowy jest praktycznie nie do
przetworzenia.

**Proponowane rozwiazanie** (zweryfikowane, kod NIE wprowadzony do repo —
zmiana rodziny wymaga zgody i resetuje medal): zmiany po zagladzie sa
zawsze lokalne i nie zmieniaja liczby linii, wiec diff mozna liczyc
**per linia** zamiast globalnie:

```python
lo = oryginal.splitlines(keepends=True)
lk = kandydat.splitlines(keepends=True)
if len(lo) != len(lk):
    return zmiany_globalne(oryginal, kandydat)   # sciezka awaryjna
for a, b in zip(lo, lk):
    if a != b:
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        ...  # offsety przesuniete o poczatek linii
```

Wynik porownania obu wariantow na 25 plikach stdlib:

| Miara | Wynik |
|---|---|
| pliki o **identycznym** zbiorze zmienionych pozycji | **25 / 25** |
| rozbieznosci | 0 |
| czas: diff globalny | 66.71 s |
| czas: diff per linia | 0.014 s |
| **przyspieszenie** | **~4669x** |

Zachowanie bez zmian, czas z minut na milisekundy.

### Z2 — martwy dublet funkcji w `AnihilatorChwastow.py`

`zaglada_tekst_poza_literalami_multi` zdefiniowana **dwa razy**:

- linie **191–301** (111 linii) — MARTWA, nadpisana przy imporcie
- linie **429–495** (67 linii) — AKTYWNA

Obie obsluguja `regex` i backtick; aktywna dodatkowo deleguje do
`zaglada_tekst_poza_literalami_multi_py`. Funkcjonalnie nieszkodliwe
(wersja aktywna jest bogatsza), ale 111 linii martwego kodu to pulapka
przy edycji — poprawka naniesiona na pierwsza definicje nie zadziala.

### Z3 — martwa `baza_bez_ogonkow`

Zdefiniowana w Zagladzie i w Anihilatorze, **0 wywolan** w calym repo.

### Z4 — brak `--help`

`ProkuratorOgrodnik.py` i `AnihilatorChwastow.py` nie obsluguja `--help`
(Pogromca i Zaglada obsluguja).

### Z5 — selftesty drukuja nieaktualne wersje

`AnihilatorChwastow.py` przy `WERSJA = "1.3.0"` drukuje `SELFTEST ... v1.0.0`;
`ProkuratorOgrodnik.py` przy `1.2.0` drukuje `v1.0.1`. Bramka
`sprawdz-spojnosc.py` tego nie lapie, bo pomija stringi wewnatrz kodu
(`WZOR_W_KODZIE`) — swiadomy kompromis przyjety przy v8.5.0, tutaj
pokazuje swoj koszt.

---

## 7. Wniosek koncowy

Teza **„kod kompiluje sie i dziala po uzyciu Gangu" — POTWIERDZONA**
na prawdziwym kodzie produkcyjnym (40 modulow stdlib): 0 plikow
niekompilujacych sie, 0 zmian w kodzie wykonywalnym, 40/40 dziala
z identycznym publicznym API.

Konstrukcja obronna jest przemyslana — piec warstw, fail-closed przy
nieznanej skladni, bramka `compile()` przed kazdym zapisem i kontrola
spojnosci nazw PO kompilacji, ktora lapie klase bledow niewidoczna dla
`compile()`.

Glowna slabosc nie dotyczy poprawnosci, tylko **wydajnosci**: kwadratowy
diff (Z1) czyni narzedzie niepraktycznym dla plikow powyzej ~50 KB.
Poprawka jest prosta i sprawdzona pod katem rownowaznosci.

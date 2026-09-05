# Hierarchia zaufania testów — od czego zacząć, gdy nie ufasz niczemu

Problem postawiony przez operatora:

> „Skoro poprawiłeś testy, to sprawdź pod tym kątem resztę swoich testów.
> Ustal priorytety, żeby nie testować potencjalnie popsutymi testami.
> Trzeba jakoś ustalić pierwszy pewny test."

To jest problem fundamentu. Jeśli test może być zepsuty, to wynik testu
nie jest dowodem — a użycie zepsutego testu do sprawdzenia innego testu
tylko przenosi wątpliwość dalej. Potrzebny jest punkt, od którego można
zacząć, oparty na czymś innym niż zaufanie.

Poniżej wynik pomiaru, nie rozumowania.

---

## 1. Metoda: mutacja zamiast opinii

Nie da się ustalić wiarygodności testu przez czytanie go. Jedyna
mierzalna definicja brzmi:

> **Test jest wiarygodny wtedy, gdy potrafi OBLAĆ na zepsutym narzędziu.**
> Test, który przechodzi na narzędziu z wyciętą funkcją, tej funkcji
> nie testuje — niezależnie od tego, jak wygląda.

Wykonanie: kopia repo → wycięcie jednej zdolności narzędzia → uruchomienie
**wszystkich** testów → zapis, które oblały.

## 2. Wynik pomiaru

| Mutacja (wycięta zdolność) | Kto złapał |
|---|---|
| Pogromca: `klasyfikuj` zwraca zawsze OK | **selftest**, tor, fuzz, T2, T6, T8 |
| Pogromca: `BLOKOWANE` puste | **selftest**, tor, T2, T8 |
| Pogromca: `--fix` nic nie robi | **selftest**, T2, T3, T8 |
| Zagłada: brak ochrony literałów | Z1, Z2, T7, T8 |
| Zagłada: brak transliteracji | Z1, T4, T7, T8 |
| Anihilator: brak blokad | T5, T8 |
| Prokurator: wszystko UMORZONE | T6, T8 |

**Zero mutacji przeszło niezauważenie.** Każda została złapana przez co
najmniej dwa niezależne testy.

## 3. Pierwszy pewny test: `PogromcaKwiatkow.py --selftest`

Wybrany nie dlatego, że „wygląda solidnie", tylko dlatego, że **ma
najmniej rzeczy, które mogą go zawieść**:

| Cecha | selftest Pogromcy | typowy turniej (T8) |
|---|---|---|
| `subprocess` | **nie** | tak (4×) |
| zależność od gita | **nie** | tak (4×) |
| katalogi tymczasowe | **nie** | tak |
| zależność od innych narzędzi rodziny | **nie** | tak |
| próbki | **wbudowane w kod** | generowane / z dysku |
| rozmiar | 76 linii | 300+ linii |

Do tego: złapał **wszystkie trzy** mutacje fundamentu, w tym najcięższą
(`klasyfikuj` zwraca zawsze OK — czyli całkowita ślepota detektora).

Próbki są zapisane sekwencjami `\uXXXX` wprost w kodzie, więc nie zależą
od kodowania pliku, systemu plików ani niczego zewnętrznego. Test albo
się wykona i da wynik, albo interpreter Pythona jest zepsuty — a wtedy
i tak nic nie działa.

## 4. Kolejność uruchamiania (od najpewniejszego)

Gdy nie ufasz niczemu, idź od dołu piramidy w górę. Jeśli poziom oblewa,
**nie ma sensu uruchamiać wyższych** — będą mierzyć zepsutym przyrządem.

```
POZIOM 0  PogromcaKwiatkow.py --selftest
          fundament: zero zaleznosci zewnetrznych, probki w kodzie

POZIOM 1  pozostale selftesty (Zaglada, Prokurator, Anihilator,
          zwiad, pamietnik, sprawdz-teksty)
          kazdy sprawdza swoje narzedzie w izolacji

POZIOM 2  tor-pogromcy, fuzz-pogromcy
          bez subprocess, bez gita; uzywaja Pogromcy jako biblioteki

POZIOM 3  T2, T3, Z1, Z2
          korpusy i wektory; zalezne od tresci probek

POZIOM 4  T4 (runtime), T5 (Anihilator), T6 (Prokurator)
          uruchamiaja narzedzia przez subprocess

POZIOM 5  T7 (zwiad), T8 (bramki)
          najwyzej: zalezne od subprocess, gita, katalogow tymczasowych
          i od poprawnosci wszystkich warstw nizej
```

## 5. Dlaczego to nie jest błędne koło

Zarzut: „testy sprawdzają narzędzia, a narzędzia obsługują testy".

Odpowiedź: poziom 0 **nie używa niczego z repo poza własnym plikiem**.
Nie woła innych narzędzi, nie czyta korpusu, nie potrzebuje gita. Jego
poprawność zależy wyłącznie od interpretera Pythona — czyli od czegoś
spoza tego repozytorium. To jest wyjście z pętli.

Każdy kolejny poziom dokłada dokładnie jedną klasę zależności, więc gdy
coś oblewa, wiadomo, **gdzie szukać**: w warstwie, która właśnie doszła.

## 6. Znane słabości, które ta hierarchia ujawnia

**Poziom 5 jest najbardziej kruchy i to nie jest wada do naprawienia** —
T7 i T8 muszą używać `subprocess` i gita, bo dokładnie to sprawdzają.
Trzeba tylko pamiętać, że ich czerwony wynik może oznaczać problem
w otoczeniu, nie w narzędziu. Przykład zmierzony w tej sesji: T8 dawał
fałszywy alarm, bo kopiował repo bez `.git`, a bramka od v1.1.0 słusznie
odmawia pracy poza repozytorium.

**Sam pomiar mutacyjny też jest testem** i podlega tej samej zasadzie.
Jego wiarygodność opiera się na tym, że sprawdza obserwowalny fakt
(kod wyjścia zmienił się z 0 na 1), a nie na interpretacji.

## 7. Dwie zasady, które z tego wynikają

**Nie sprawdzaj kodu wyjścia w oderwaniu od treści.** Pierwsza wersja T8
przespała 2 z 3 sabotaży, bo `exit=1` padał z innego powodu niż badany
(dopisanie wpisu do dziennika samo wywołuje „RUSZONY CUDZY DZIENNIK").
Poprawne sprawdzenie brzmi:

```python
if kod != 1 or "brakuje pola" not in out:
```

**Po napisaniu testu zepsuj narzędzie i sprawdź, czy test oblewa.**
Jeśli nie oblewa — test jest dekoracją. W tej sesji zdarzyło się to
dwukrotnie: T5 przespał 2 z 4 sabotaży, T8 przespał 2 z 3.

---

## 8. Dwa pomiary, nie jeden

Pomiar globalny (`pomiar-mutacyjny.py`) pyta: **czy ktokolwiek złapał?**
To za mało. Rozkład okazał się bardzo nierówny:

| Turniej | Ile z 9 mutacji złapał |
|---|---|
| T8 bramki | 6 |
| T2, T7 | 3 |
| T1 tor, Z1 | 2 |
| fuzz, T3, Z2, T4, T5, T6 | 1 |
| luka-fstring | **0** |

Zero przy `luka-fstring` nie znaczyło, że jest zepsuta — po prostu żadna
z dziewięciu mutacji nie celowała w jej obszar. Ale gdyby była
dekoracją, pomiar globalny **też pokazałby zero** i nie dałoby się
tego odróżnić.

Dlatego drugi pomiar (`pomiar-per-turniej.py`) pyta inaczej: **czy TEN
turniej łapie to, co deklaruje w swoich kategoriach?** Dla każdej pary
(turniej, kategoria) wycina wadę, którą ta kategoria ma wykrywać,
i uruchamia **wyłącznie ten turniej**.

Wynik 2026-09-05: **16 prób, 0 przespanych.**

```
luka-fstring        dowod luki               tak
T4-runtime          kryterium WYKONANIA      tak
T5-anihilator       B2 poprawnosc naprawy    tak
T5-anihilator       B niepsucie danych       tak
T6-prokurator       C czyste akta            tak
T6-prokurator       D plan-act               tak
T6-prokurator       A polityka .py           tak
T7-zwiad            C rozdzial kod/dane      tak
T7-zwiad            B kompletnosc            tak
T8-bramki           A wykrywalnosc           tak
T8-bramki           C zasieg                 tak
T3-niepsucie        niepsucie --fix          tak
Z2-niepsucie        Z2 niepsucie             tak
tor-pogromcy        wektory detekcji         tak
T2-sprawdzajacy     T2 wektory               tak
Z1-wykrywania       Z1 wykrywanie            tak
```

To ta sama pułapka co przy kodzie wyjścia: obserwujesz skutek, który
ma wiele możliwych przyczyn. Turniej może przechodzić pomiar globalny
**cudzym sukcesem**.

## Jak to uruchomić

Pomiar mutacyjny nie jest częścią zwykłej regresji (trwa ~90 s i psuje
kopię repo). Uruchamiaj go, gdy:

* dodajesz nowy turniej — żeby sprawdzić, czy w ogóle coś łapie,
* podejrzewasz, że test jest dekoracją,
* przed wydaniem, jako kontrola całości.

Kod: `dev/turnieje/pomiar-mutacyjny.py`

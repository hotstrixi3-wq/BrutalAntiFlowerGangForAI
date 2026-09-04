# Czego testy nie sprawdzaja — burza mozgow + weryfikacja

> **STATUS (v8.6.0 / 1.4.0): luka krytyczna f-string ZALATANA, Z1 ZALATANE,
> kryterium wykonania DODANE** — patrz `docs/NAPRAWA-v8.6.0.md`.
> Dowod `dev/luki/luka-fstring.py` daje teraz 0/5 zepsutych (exit 0),
> a nowy `dev/turnieje/turniej-4-runtime.py` pilnuje, zeby nie wrocila.

Data: 2026-09-04 · Stan repo: commit `f159d80`

Metoda: najpierw ustalenie z kodu, co testy **naprawde** pokrywaja, potem
lista hipotez „czego brakuje", potem **wykonanie kazdej hipotezy** na zywym
narzedziu. Nizej tylko wyniki zmierzone — bez domyslow.

---

## 1. Co testy pokrywaja dzisiaj (stan faktyczny)

| Narzedzie | Pliki testowe, ktore je dotykaja |
|---|---|
| `PogromcaKwiatkow.py` | 8 |
| `ZagladaKultury.py` | 3 |
| **`ProkuratorOgrodnik.py`** | **0** |
| **`AnihilatorChwastow.py`** | **0** |
| **`sprawdz-spojnosc.py`** | **0** |

Rozszerzenia wystepujace w probkach generowanych przez turnieje:
`.py` (84), `.md` (20), `.txt` (15), `.json` (6). Zero js/ts/java/go/rs/cs.

Kryterium „niepsucia" w obu turniejach niepsucia to `compile()`
(+ `json.loads` dla JSON). **Zaden test nie URUCHAMIA wyczyszczonego kodu.**
To istotne, bo — jak opisuje `docs/INZYNIERIA-WSTECZNA.md` pkt 2.3 — cala
klasa bledow (niespojnosc nazw) przechodzi przez `compile()` i wybucha
dopiero w runtime.

---

## 2. ZNALEZISKO KRYTYCZNE — wnetrze f-stringa nie jest czyszczone

**To jest realne zlamanie tezy „Gang nie psuje kodu".**
Nie hipoteza — plik, ktory **dzialal** przed Gangiem, po Gangu **wybucha**.

```
PRZED:   v<U+043E> = 7
         print(f"wynik: {v<U+043E>}")        -> dziala, wypisuje "wynik: 7"

PO ZAGLADZIE:
         v  = 7                        <- definicja WYCZYSZCZONA
         print(f"wynik: {v<U+043E>}")         <- uzycie NIE (bo to "literal")
         -> NameError: name 'v<U+043E>' is not defined
```

### Przyczyna

Warstwa ochronna „nie ruszamy literalow" (`_chronione_pozycje`,
`_regiony_literalow`) traktuje f-string jako jeden literal. Ale wnetrze
klamer `{...}` w f-stringu to **kod wykonywalny**, nie dane. Ochrona,
ktora normalnie ratuje dane, tutaj rozjezdza definicje z uzyciem.

### Zasieg — potwierdzony pomiarem

Dotyczy **dwoch narzedzi**, wszystkich wariantow skladni:

| Wariant | Przed | Po |
|---|---|---|
| prosty `f"{v}"` | `wynik: 7` | `NameError` |
| format-spec `f"{a:>3}"` | `1` | `NameError` |
| zagniezdzony `f"{ {i for i in ...} }"` | `{0, 1, 2}` | `NameError` |
| wielolinijkowy `f"""..{x}.."""` | `linia 2` | `NameError` |
| indeks `f"{d[k]}"` | `1` | `NameError` |

**5 / 5 zepsutych.**

To samo w JS — template literal `` `${...}` `` w `AnihilatorChwastow.py`:

```
PRZED:  let v<U+043E> = 7; console.log(`wynik: ${v<U+043E>}`);   -> "wynik: 7"
PO:     let vo = 7; console.log(`wynik: ${v<U+043E>}`);   -> ReferenceError
```

`PogromcaKwiatkow.py --fix` na tej probce **nie zmienil nic** (zostawil
skazenie) — czyli nie psuje, ale i nie naprawia.

### Dlaczego testy tego nie zlapaly

Sprawdzone automatem po wszystkich 8 plikach turniejowych:

```
petla-rodzinna.py               f-string w probkach: 0
petla-turniejowa.py             f-string w probkach: 0
turniej-2-sprawdzajacy.py       f-string w probkach: 0
turniej-3-niepsucie.py          f-string w probkach: 0
turniej-niezalezny.py           f-string w probkach: 0
zaglada-turniej-niepsucie.py    f-string w probkach: 0
zaglada-turniej-wykrywania.py   f-string w probkach: 0
SUMA-KONTROLNA-TESTOW.py        f-string w probkach: 0
```

**Zadna probka testowa nie zawiera f-stringa ze zmienna.**
Dla porownania: **58 / 171 modulow stdlib (34%)** takiego f-stringa uzywa.
Turnieje na 390 plikach pokazuja „0 popsutych", bo omijaja konstrukcje
wystepujaca w co trzecim realnym pliku.

Dodatkowo turnieje sprawdzaja `compile()`, a tu **`compile()` przechodzi** —
skladnia jest poprawna. Nawet gdyby probka zawierala f-string, obecne
kryterium by tego nie wykrylo. Potrzebne jest **uruchomienie**.

Dowod odtwarzalny: `dev/luki/luka-fstring.py` (exit 1 = luka obecna).

---

## 3. Hipotezy sprawdzone — wynik NEGATYWNY (te rzeczy dzialaja)

Zeby nie robic falszywego alarmu, ponizsze tez zostaly wykonane
i **nie wykazaly problemu**:

| Hipoteza | Wynik |
|---|---|
| Idempotencja (2x zaglada = 1x) | OK, identyczny plik |
| CRLF (Windows) — czy zamienia na LF | OK, 3 CR przed i po |
| Brak newline na koncu pliku | OK, nie dodaje |
| Symlink — czy zastapi dowiazanie plikiem | OK, symlink przetrwal |
| Prawa dostepu (755) | OK, zachowane |
| BOM na poczatku `.py` | usuwany, plik nadal kompiluje sie |
| Backup przy 2. przebiegu | **nie nadpisuje** pierwotnego oryginalu |
| Plik nie-UTF8 / binarny z `.py` | czysty `[BLAD WEJSCIA]`, bez tracebacka |
| Exit codes | Pogromca 1, Prokurator 1, Anihilator 2, czysty 0 |
| Dekorator `@dek<U+043E>` | OK |
| Nazwa importu `import js<U+043E>n` | naprawiony poprawnie |

Warstwa obronna jest solidna. Luka jest **jedna, ale trafia w samo serce tezy**.

---

## 4. Pozostale dziury w pokryciu (bez dowodu na blad — brak testu)

### D1. Anihilator: 6 jezykow, zero testow
`js/ts/java/go/rs/cs/c/cpp/php` nie maja ani jednej probki w `dev/`.
Recznie sprawdzone: JS i C przechodza (`node` i `gcc` uruchomily wynik
poprawnie, identyczny output). Reszta jezykow — **nieznana**, bo w tym
sandboxie brak `javac/go/rustc/dotnet/php`. To znaczy tylko tyle, ze nikt
tego nigdy nie zweryfikowal.

### D2. Prokurator: zero testow
Orkiestrator wolajacy dwa subprocesy, z polityka UMORZONE/POUCZENIE/
ZAGLADA/BLOKADA i allowlista — i ani jednego testu. Nietestowane sciezki:
allowlista i18n, `sciezka_rodzenstwa` gdy rodzenstwa brak, zachowanie gdy
subprocess padnie.

### D3. Brak testu wykonania (runtime)
Kryterium `compile()` z zalozenia nie widzi bledow runtime — a wlasnie
takie bledy narzedzie potrafi wprowadzic (patrz pkt 2 i znalezisko
`_scandir_path` z v1.1.0). Test powinien **uruchamiac** wynik.

### D4. Brak testu na prawdziwym kodzie
Cala amunicja jest syntetyczna. Weryfikacja z
`docs/INZYNIERIA-WSTECZNA.md` (40 modulow stdlib) pokazala, ze prawdziwy
kod ma konstrukcje, ktorych generator nie wytwarza — f-string jest tego
dowodem.

### D5. Brak testu wydajnosciowego
Znalezisko Z1 (kwadratowy diff, 3m23s na 99 KB) przeszlo niezauwazone,
bo probki turniejowe sa male. Wystarczylby prog czasowy na plik ~100 KB.

### D6. `sprawdz-spojnosc.py` bez testu
Bramka pilnujaca wersji sama nie ma testu regresji (byla testowana
recznie 4 testami negatywnymi przy v8.5.0, ale nie ma tego w `dev/`).

---

## 5. Co podciagnac — priorytety

1. **Naprawic luke f-string/template-literal** (krytyczne — lamie teze).
   Kierunek: wnetrze `{...}` w f-stringu traktowac jako KOD, nie literal.
   Dla Pythona naturalnym narzedziem jest `ast` / `tokenize`
   (`FormattedValue`), dla JS — parsowanie `${...}` wewnatrz backtickow.
2. **Dodac probki z f-stringiem** do turniejow niepsucia (wszystkie 5
   wariantow z tabeli).
3. **Zmienic kryterium niepsucia z `compile()` na URUCHOM-I-POROWNAJ-WYNIK**
   — inaczej pkt 1 moze wrocic niezauwazony.
4. **Turniej dla Anihilatora** — chociaz js/ts (`node` jest dostepny).
5. **Turniej dla Prokuratora** — polityka + allowlista.
6. **Prog wydajnosciowy** w regresji (plik ~100 KB, limit np. 10 s).

Zadna zmiana w kodzie rodziny nie zostala wprowadzona — zgodnie z zasada
„poprawka = reset medalu" czeka to na decyzje operatora.

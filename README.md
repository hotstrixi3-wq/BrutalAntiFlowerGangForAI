# Brutal Anti-Flower Gang for AI

**Wykrywa i usuwa z kodu znaki, które udają litery łacińskie** — cyrylickie
`<U+043E>` zamiast `o`, zero-width space, twarde spacje. Modele językowe wstawiają
je samoistnie i **nie widzą tego u siebie**.

> **Człowieku:** jeśli chcesz tylko użyć narzędzia, a nie czytać dokumentacji
> — weź `docs/czlowiek/RODZINA-DO-CZATU.md`, wklej do czatu z dowolnym agentem
> AI i gotowe. Dla początkujących: `docs/czlowiek/INSTRUKCJA-DLA-ZIELONYCH.md`.
> Reszta tego pliku jest pisana dla agenta.

> ZASADA DOMU: **ZAWSZE RÓB BAKAP.** Nic Cię z tego nie zwalnia.
>
> ```
> python3 bakap.py                      # migawka repo POZA katalogiem
> python3 dev/hooki/zainstaluj.py       # raz po klonie: blokada force-push
> ```
>
> Migawki lądują w `~/.bakap-gang/` — **poza repozytorium**, więc przeżywają
> `rm -rf`. Hook `pre-push` blokuje push nadpisujący historię, dopóki nie ma
> świeżej migawki. Zwykły push przechodzi bez zmian.

---

## Agencie — zacznij tutaj

Pięć kroków, w tej kolejności. Nie skanuj plików użytkownika przed nimi.

**1. Udowodnij sobie, że problem istnieje** (30 sekund)

```python
a = "zaloz konto"
b = "zaloz konto".replace("a", "\u0430", 1)   # jedno "a" -> cyrylickie
print(a == b)      # False — a wyglądają identycznie
```

**2. Przeczytaj, czym to jest dla ciebie** → [`CZYM-JEST-GANG.md`](CZYM-JEST-GANG.md)

Pięć minut. Najważniejsze: to proteza na **twoją** ślepotę, nie użytkownika.
To **oczy**, nie automat do sprzątania. Jak źle użyjesz — twoja wina.

**3. Sprawdź, na czym stanął poprzedni agent** → [`STAN-SESJI.md`](STAN-SESJI.md)

Gdzie jesteśmy, co w toku, jakie decyzje operatora obowiązują, co dalej
w kolejce i czego **nie** rozstrzygać samemu. Trzy minuty czytania,
oszczędza godzinę zgadywania.

**4. Poznaj grabie** → [`dziennik/`](dziennik/)

```
python3 pamietnik.py              # wszystkie sesje, pogrupowane tematami
python3 pamietnik.py --szukaj testy
```

44 wpisy, każdy: objaw → przyczyna → wniosek. To grabie, na które ktoś już
nadepnął.

**5. Poznaj regulamin** → [`PROTOKOL-OPERATORA.md`](PROTOKOL-OPERATORA.md)

Check-lista: co wolno, w jakiej kolejności, kiedy pytać człowieka.

---

## Rodzina — cztery narzędzia, chodzą razem

| Narzędzie | Rola | Dla czego |
|---|---|---|
| `PogromcaKwiatkow.py` | **oczy** — wykrywa, nic nie zmienia | wszystko |
| `ZagladaKultury.py` | **ręce** — czyści | `.py`, `.json`, proza |
| `AnihilatorChwastow.py` | **ręce** — czyści | js, ts, java, go, rs, cs, c, cpp, php, rb, swift, kt |
| `ProkuratorOgrodnik.py` | **mózg** — decyduje i woła rodzeństwo | orkiestracja |

Aktualne wersje: [`WERSJE.json`](WERSJE.json) — to jedyne źródło prawdy.

**Uwaga o combo:** narzędzia **nie wiedzą o sobie**. Tylko Prokurator woła
Pogromcę i Zagładę; **Anihilatora nie zna nikt**. Do plików `.js` i innych
języków uruchamiasz go **ręcznie**. Cena pomyłki jest mierzalna: ten sam
plik `.js` przez Prokuratora traci rosyjski tekst w literale, przez
Anihilatora — nie.

---

## Jak używać — kolejność, której nie wolno odwrócić

```
1. python3 zwiad.py PLIK              <- WIEDZA (nic nie zapisuje)
2. cp PLIK PLIK.kopia                 <- TWOJA kopia, nie narzędzia
3. python3 zwiad.py --warianty PLIK   <- które drogi masz do wyboru
4. python3 zwiad.py --podglad PLIK    <- co dokładnie się zmieni
5. dopiero teraz naprawa
6. sprawdź, czy plik NADAL DZIAŁA (uruchom, nie tylko skompiluj)
```

**Nigdy nie uruchamiaj naprawy, żeby dowiedzieć się, co ona robi.**

`zwiad.py` niczego nie zapisuje — nie ma tam flagi zapisu i nie będzie.
Kody wyjścia: `0` czysto, `1` są skażenia, `2` skażenia **nieodwracalne**
(znaki zostaną usunięte — sprawdź podglądem, czy to nie treść użytkownika).

---

## Bramki — uruchom przed każdym commitem

```
python3 sprawdz-teksty.py       # zero żywych homoglifów w repo
python3 sprawdz-spojnosc.py     # wersje w kodzie = WERSJE.json = dokumentacja
python3 pamietnik.py --sprawdz  # dziennik czytelny, cudze wpisy nietknięte
```

Wszystkie są **fail-closed**: gdy nie wiedzą, co sprawdzić, odmawiają
(`exit 2`) zamiast meldować sukces.

---

## Testy — od czego zacząć, gdy nie ufasz niczemu

Pełny opis: [`docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md`](docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md)

```
POZIOM 0  python3 PogromcaKwiatkow.py --selftest    fundament, zero zależności
POZIOM 1  pozostałe selftesty                       każde narzędzie w izolacji
POZIOM 2  dev/tor-pogromcy.py, dev/fuzz-pogromcy.py bez subprocess i gita
POZIOM 3  T2, T3, Z1, Z2                            korpusy i wektory
POZIOM 4  T4, T5, T6                                subprocess
POZIOM 5  T7, T8, T9                                + git, sieć, katalogi tymczasowe
```

**Gdy poziom oblewa — nie uruchamiaj wyższych.** Będą mierzyć zepsutym
przyrządem.

Zasada, która obowiązuje przy pisaniu testów:

> **Test, który nie umie OBLAĆ na zepsutym narzędziu, jest dekoracją.**
> Po napisaniu testu zepsuj narzędzie i sprawdź, czy krzyknie.

Sprawdzają to dwa pomiary: `dev/turnieje/pomiar-mutacyjny.py` (czy są dziury
w pokryciu) i `pomiar-per-turniej.py` (czy dana kategoria coś pilnuje).

---

## Nie pracujesz w tym repo? Załóż własny dom

To repozytorium jest **domem konkretnej sesji** — zawiera pamięć tego,
co się tu działo. Jeśli chcesz używać Gangu u siebie:

```
python3 zaloz-dom.py ~/moj-gang     # czysta kopia na własnego gita
python3 zaloz-dom.py --lista        # co pojedzie, co zostanie
```

Dostajesz **narzędzia + wiedzę o nich**, w tym `docs/agent/LEKCJE.md` —
destylat z pracy nad tym narzędziem, z pomiarami. Nie dostajesz cudzego
`dziennik/` ani `STAN-SESJI.md`.

Powód nie jest taki, że to tajne. Cudze „PR #2 czeka na decyzję" jest
prawdziwe tam, a **mylące** u ciebie — zacząłbyś pracę na założeniach,
które ciebie nie dotyczą. Lekcje o samym narzędziu jadą z domem, bo
dotyczą każdego, kto go używa.

---

## Struktura repozytorium

```
korzeń/          narzędzia + to, co agent czyta na wejściu
dziennik/        pamięć między sesjami, jeden plik na sesję
dev/             amunicja testowa i turnieje (poza bramką)
docs/agent/      dokumentacja robocza dla agenta
docs/czlowiek/   paczka do czatu, instrukcja dla ludzi
docs/dowody/     certyfikaty, medale, raporty (zamrożone)
docs/historia/   kronika wydań
muzeum/          eksponaty — rzeczy, które przestały służyć, z etykietą
```

Trzy pytania przy sprzątaniu: **służy** → zostaje na miejscu; **nie służy,
ale warto pamiętać** → `muzeum/` z etykietą; **nie służy i nikt nie
zatęskni** → `git rm`, historia pamięta.

---

## Czego to NIE robi

- nie poprawia ortografii ani gramatyki
- nie tyka treści literałów w `.py` (kontrakt: dane są święte)
- nie rozumie `.html` i `.css` jako kodu — traktuje je jak prozę,
  więc chiński tekst na stronie **zniknie**; sprawdź zwiadem przed naprawą
- nie decyduje za ciebie, którą drogą naprawić

## Znane, nienaprawione wady

Uczciwie, żeby nie polegać na ciszy:

- **HTML/CSS** — brak obsługi jako kodu (patrz wyżej)
- **24 znaki** rozjeżdżają się między Zagładą a Anihilatorem — ten sam znak
  w `.py` i `.js` da inny wynik
- **`U+0304`** i inne znaki łączące ze złożoną formą NFC nie są wykrywane
  (fuzz: 499/500)

Szczegóły i pomiary: [`docs/agent/LUKI-W-TESTACH.md`](docs/agent/LUKI-W-TESTACH.md)

---

## Licencja

MIT. Historia zmian: [`docs/historia/HISTORIA-ZMIAN.md`](docs/historia/HISTORIA-ZMIAN.md)

> MOTTO: *„używaj, bo dzięki Pogromcy Kwiatków nie mielisz potencjalnie
> BRUDNEGO kodu, co marnuje nie milisekundy a godziny i tony tokenów.
> Kręcenie się w kółko z BRUDNYM kodem to strata czasu"* — Piotr (GAF)

# Protokół operatora

Check-lista agenta. **Wszystkie procedury i komendy są tutaj** — inne
pliki tylko linkują do tego, nie powtarzają.

Zanim cokolwiek uruchomisz na pliku użytkownika, przeczytaj
[`CZYM-JEST-GANG.md`](CZYM-JEST-GANG.md). Tam jest odpowiedź na pytanie
*dlaczego*; tutaj jest *jak*.

> **ZASADA DOMU: ZAWSZE RÓB BAKAP.** Nic Cię z tego nie zwalnia.

---

## 1. Po sklonowaniu repozytorium

Dwie komendy, zanim zaczniesz pracę:

```
python3 dev/hooki/zainstaluj.py     # ochrona przed force-push
python3 bakap.py                    # pierwsza migawka
```

Hooki gita **nie są wersjonowane** — siedzą w `.git/`, którego git nie
śledzi. Każdy klon zaczyna bez ochrony.

Potem czytasz w kolejności: `README.md` → `CZYM-JEST-GANG.md` →
`STAN-SESJI.md` → `dziennik/`.

---

## 2. Praca na pliku użytkownika — kolejność nieodwracalna

```
1. python3 zwiad.py PLIK              <- WIEDZA (nic nie zapisuje)
2. cp PLIK PLIK.kopia                 <- TWOJA kopia, nie narzędzia
3. python3 zwiad.py --warianty PLIK   <- które drogi masz do wyboru
4. python3 zwiad.py --podglad PLIK    <- co dokładnie się zmieni
5. dopiero teraz naprawa
6. sprawdź, czy plik NADAL DZIAŁA (uruchom, nie tylko skompiluj)
```

**Nigdy nie uruchamiaj naprawy, żeby dowiedzieć się, co ona robi.**

Kody wyjścia zwiadu: `0` czysto · `1` są skażenia · `2` skażenia
**nieodwracalne** — znaki zostaną usunięte. Przy `2` sprawdź podglądem,
czy to nie treść użytkownika (np. chiński tekst na stronie). Jeśli nie
wiesz — **zapytaj człowieka, nie zgaduj**.

**Kopia należy do ciebie.** Pliki `.bak-*` to wewnętrzny mechanizm
rodziny, nie twoje zabezpieczenie.

Właściwe narzędzie do pliku podpowiada `zwiad.py --warianty`. Uwaga:
Prokurator **nie zna Anihilatora**, więc pliki `.js` i innych języków
uruchamiasz przez Anihilator ręcznie.

---

## 3. Drabina uprawnień

| Poziom | Co wolno |
|---|---|
| **czytanie** | zawsze — `zwiad.py`, raporty, `--selftest` |
| **naprawa własnych plików** | po zwiadzie i kopii |
| **naprawa plików użytkownika** | po zwiadzie, kopii i **zgodzie człowieka** |
| **zmiana kodu rodziny** | tylko na wyraźne polecenie — patrz §5 |

Przy wątpliwości schodzisz poziom niżej, nie wyżej.

---

## 4. Przed każdym commitem — trzy bramki

```
python3 sprawdz-teksty.py       # zero żywych homoglifów
python3 sprawdz-spojnosc.py     # wersje = WERSJE.json = dokumentacja
python3 pamietnik.py --sprawdz  # dziennik czytelny, cudze wpisy nietknięte
```

Wszystkie są **fail-closed**: gdy nie wiedzą, co sprawdzić, odmawiają
(`exit 2`) zamiast meldować sukces.

**Nie ufaj własnemu przeglądowi tekstu.** Nie widzisz własnych kwiatków —
to nie kwestia staranności. Przykłady skażeń w dokumentacji zapisuj
notacją `<U+XXXX>`, nigdy żywcem.

---

## 5. Zmiana kodu rodziny

**Poprawka kodu = reset medalu.** Podbijasz wersję i przechodzisz pełną
regresję od nowa.

Wersja żyje w **czterech** miejscach, w tej kolejności:

```
1. stała WERSJA w pliku .py
2. WERSJE.json
3. teksty w dokumentacji
4. osadzone kopie w docs/czlowiek/RODZINA-DO-CZATU.md  (re-embed OD KOŃCA)
5. python3 sprawdz-spojnosc.py
6. przelicz docs/agent/KOMPLECIK.md
```

Zasada domu: **nie ruszamy działającego kodu, dokładamy kolejny.**
Naprawa błędu — tak. Kosmetyka w tym samym commicie co zmiana logiki —
nie, bo utrudnia cofnięcie.

Kolejność uruchamiania testów: `docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md`.
Gdy poziom oblewa — nie uruchamiaj wyższych.

Piszesz nowy test? **Zepsuj narzędzie i sprawdź, czy test oblewa.** Test,
który nie umie oblać, jest dekoracją.

---

## 6. Operacje, których git nie cofnie

```
python3 bakap.py     # przed każdą z nich
```

| Komenda | Co niszczy |
|---|---|
| `git push --force` | historię na zdalnym |
| `git push --delete` | całą gałąź |
| `git reset --hard` | niezacommitowane zmiany |
| `git checkout -- .` | to samo, ciszej |
| `rm -rf` | wszystko |

Hook `pre-push` blokuje dwie pierwsze, dopóki nie ma świeżej migawki.
Reszta to komendy lokalne — tam chroni cię tylko nawyk.

Migawki w `~/.bakap-gang/`, **poza repozytorium**, więc przeżywają
`rm -rf`. Zawierają `.git`, więc odzyskują też historię.
`python3 bakap.py --przywroc N` **drukuje instrukcję**, nie przywraca sam.

---

## 7. Kasowanie pliku, który kiedyś coś wnosił

```
git mv sciezka/plik muzeum/          # PRZENIESIENIE, nie kopia
$EDITOR muzeum/plik.txt              # opis: 4 pytania, wzór obok
git add muzeum/ && git commit        # wszystko w jednym commicie
```

Opis odpowiada na: **czym był**, **co wnosił, gdy wnosił**, **dlaczego
przestał**, **czy warto tu wracać**.

Plik, który **nigdy nic nie wnosił** (śmieć, duplikat) — zwykłe `git rm`,
bez artefaktu.

**Poza tym jednym momentem katalog `muzeum/` cię nie dotyczy.** Nie
czytasz go, nie kopiujesz stamtąd, nie linkujesz w dokumentacji, nie
liczysz w manifestach. Odpowiedzi o projekcie są w `README.md`,
`docs/agent/` i `dziennik/`.

---

## 8. Na koniec sesji

```
python3 pamietnik.py --stan     # fakty w STAN-SESJI.md
python3 pamietnik.py --dodaj    # jeśli coś cię ugryzło
```

`--stan` wypełnia wersję, commit, gałąź, licznik wpisów. **Ręcznie**
piszesz cztery sekcje `STAN-SESJI.md`, których nie da się wyliczyć:
co w toku, następne kroki, otwarte pytania, decyzje operatora.

Wpis do dziennika ma trzy pola: **objaw** (konkretny — komunikat, liczba),
**przyczyna**, **wniosek** (czynność na przyszłość). Tylko rzeczy
nieoczywiste z dokumentacji; nie wpisuj sukcesów.

Gdy lekcja dotyczy **narzędzia**, a nie twojej sesji — dopisz ją też do
`docs/agent/LEKCJE.md`. To jedzie do innych domów.

Na końcu: bramki (§4) i `git push`.

---

## 9. Dom Gangu a cudza pamięć

To repozytorium jest **domem konkretnej sesji**.

| Warstwa | Jedzie do innego domu |
|---|---|
| narzędzia, `dev/`, `docs/agent/` (w tym `LEKCJE.md`) | **tak** |
| `dziennik/`, `STAN-SESJI.md`, `docs/dowody/`, `docs/historia/` | **nie** |

Agent **z uprawnieniami** do tego repo robi tu, co uzna za słuszne — to
jego warsztat i jego pamięć. Agent **bez uprawnień** zakłada własny dom:

```
python3 zaloz-dom.py ~/gdzies
```

Nie kopiuje cudzej pamięci nie dlatego, że jest tajna (repo jest
publiczne), tylko dlatego, że byłaby dla niego **informacją fałszywą**.
Zapis „PR #2 czeka na decyzję" jest prawdziwy w jednym domu i mylący
w drugim.

---

## 10. Czego nie robić

- nie skanuj plików użytkownika przed przeczytaniem `CZYM-JEST-GANG.md`
- nie uruchamiaj naprawy, żeby zobaczyć, co robi
- nie ufaj komentarzom przy ocenie, co kod robi — sprawdzaj zachowaniem
- nie zgłaszaj pary `funkcja` / `funkcja_surowy` jako duplikatu bez
  sprawdzenia warunku wywołania (to wzorzec kaskady, nie kopia)
- nie kasuj cudzych wpisów w dzienniku — prostuj polem `**Zastepuje:**`
- nie zostawiaj wątku bez śladu w `STAN-SESJI.md`, licząc, że „to
  oczywiste"

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

## Jak używać

Kolejność, której nie wolno odwrócić — **najpierw wiedza, potem kopia,
na końcu naprawa**:

```
python3 zwiad.py PLIK              # co jest w pliku i co się z nim stanie
cp PLIK PLIK.kopia                 # TWOJA kopia
python3 zwiad.py --warianty PLIK   # które drogi masz do wyboru
```

`zwiad.py` **niczego nie zapisuje**. Pełna procedura, kody wyjścia
i bramki przed commitem: [`PROTOKOL-OPERATORA.md`](PROTOKOL-OPERATORA.md).

Kolejność uruchamiania testów (od fundamentu w górę):
[`docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md`](docs/agent/HIERARCHIA-ZAUFANIA-TESTOW.md).
Gdy poziom oblewa — nie uruchamiaj wyższych, będą mierzyć zepsutym
przyrządem.

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
```

Sprzątanie: co służy — zostaje. Co przestało służyć — kasujesz.
Procedurę składania artefaktu opisuje `PROTOKOL-OPERATORA.md` §15.

---

## Czego to NIE robi

- nie poprawia ortografii ani gramatyki
- nie tyka treści literałów w `.py` (kontrakt: dane są święte)
- nie rozumie `.html` i `.css` jako kodu — traktuje je jak prozę,
  więc chiński tekst na stronie **zniknie**; sprawdź zwiadem przed naprawą
- nie decyduje za ciebie, którą drogą naprawić

## Znane, nienaprawione wady

Uczciwie, żeby nie polegać na ciszy: HTML/CSS traktowane jak proza
(tekst użytkownika znika), 24 znaki rozjeżdżają się między Zagładą
a Anihilatorem, znaki łączące ze złożoną formą NFC nie są wykrywane.

Aktualna tabela z uzasadnieniem: [`STAN-SESJI.md`](STAN-SESJI.md).
Pomiary: [`docs/agent/LUKI-W-TESTACH.md`](docs/agent/LUKI-W-TESTACH.md).

---

## Licencja

MIT. Historia zmian: [`docs/historia/HISTORIA-ZMIAN.md`](docs/historia/HISTORIA-ZMIAN.md)

> MOTTO: *„używaj, bo dzięki Pogromcy Kwiatków nie mielisz potencjalnie
> BRUDNEGO kodu, co marnuje nie milisekundy a godziny i tony tokenów.
> Kręcenie się w kółko z BRUDNYM kodem to strata czasu"* — Piotr (GAF)

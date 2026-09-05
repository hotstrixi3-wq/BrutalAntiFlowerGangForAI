# Audyt: `sprawdz-spojnosc.py` od Claude Pro

Data weryfikacji: 2026-09-05 · Weryfikował: agent sesji `01a06e18`
Materiał: kod wklejony przez operatora do czatu (nie z repo)

Operator poprosił: **"przeanalizuj i nie ufaj"**. Poniżej tylko rzeczy
sprawdzone wykonaniem, na kopii repo w `/tmp`, bez tykania oryginału.

---

## Werdykt w jednym zdaniu

Pomysł trafiony w sedno i **niezależnie wymyślony tak samo jak w repo**,
ale ta konkretna implementacja **nie nadaje się do użycia tu i teraz**:
zgłasza **94 rozjazdy na czystym repozytorium**, z czego wszystkie
sprawdzone są fałszywe.

---

## 1. Bezpieczeństwo — czyste

Sprawdzone AST-em, przed uruchomieniem:

| Kontrola | Wynik |
|---|---|
| wywołania `system` / `subprocess` / `eval` / `exec` | **brak** |
| `open()` w trybie zapisu | **brak** — trzy odczyty, wszystkie `r` |
| usuwanie / przenoszenie plików | **brak** |
| żywe homoglify w źródle | **brak** (bramka tekstów: 0) |

Kod jest wyłącznie czytający. Można go bezpiecznie uruchomić.

---

## 2. Co działa

Rdzeń — porównanie stałej `WERSJA` w kodzie z `WERSJE.json` — **działa
poprawnie**. Test sabotażem: podbiłem `WERSJA` w `ZagladaKultury.py`
na `9.9.9`, nie ruszając `WERSJE.json`:

```
[ROZJAZD] ZagladaKultury.py: kod mowi 9.9.9, WERSJE.json mowi 1.4.0
```

Wykryte prawidłowo. Ta część jest napisana dobrze.

Dobre też: obsługa pola `znany_problem` (pozwala świadomie oznaczyć
narzędzie bez stałej `WERSJA`, zamiast wyłączać kontrolę), czytelny
podział na `sprawdz_kod` / `sprawdz_dokumentacje`, sensowne kody wyjścia.

---

## 3. Co nie działa — 94 fałszywe alarmy

Uruchomienie na **czystym, spójnym** repozytorium:

```
ROZJAZDY: 94
```

Dla porównania wersja obecna w repo na tym samym stanie: `ROZJAZDY: 0`.

### Przyczyna: każdy numer w tekście traktowany jak deklaracja wersji

Wzorzec `\bv?(\d+\.\d+\.\d+)\b` łapie **wszystko**, co wygląda jak numer,
i wymaga, żeby występowało w `WERSJE.json`. Ale README to również
**historia zmian**:

```
- v8.2.0 - reorganizacja repo i zmiana nazwy
  Zaglada v1.0.7), naprawiona struktura...
## v8.7.0 / Prokurator 1.3.0 - turnieje dla Prokuratora
```

To są zapisy o przeszłości — mają prawo mówić o starych wersjach.
Dokładnie tak samo jak `archiwum/`, które autor sam wyłączył z kontroli
w docstringu. Zabrakło tej samej myśli o **historii wewnątrz pliku**.

Wersja w repo rozwiązuje to funkcją `_linia_historyczna()`: rozpoznaje
wpisy o przeszłości i je pomija.

### Skutek praktyczny

Bramka, która na zdrowym repo krzyczy 94 razy, zostanie wyłączona po
drugim uruchomieniu. To ten sam wniosek, który zapisano w dzienniku przy
budowie `sprawdz-teksty.py`: **narzędzie, które szumi, jest ignorowane —
a wtedy przepuści prawdziwy błąd.**

---

## 4. `START.md` — plik, którego nigdy nie było

```python
WARSTWA_AGENTA = ("README.md", "START.md", "PROTOKOL-OPERATORA.md")
```

```
[ROZJAZD] START.md: brak pliku warstwy agenta
```

Sprawdzone w historii gita (`git log --diff-filter=A -- START.md`):
**pusto**. Ten plik nigdy nie istniał w repozytorium. Odpowiednikiem
jest `SZYBKI-START-DLA-AGENTA.md`.

To najmocniejsza przesłanka, że **kod nie był uruchomiony na tym
repozytorium** — jedno wykonanie ujawniłoby to natychmiast.

---

## 5. Czego ta wersja nie sprawdza

| Kontrola | Claude Pro | Repo |
|---|---|---|
| stała `WERSJA` vs `WERSJE.json` | tak | tak |
| wersje w dokumentacji | 3 pliki | 6 plików |
| rozpoznawanie wpisów historycznych | **nie** | tak |
| **osadzone kopie kodu (sha256)** | **nie** | tak |
| linie: 112 vs 248 | | |

Brak kontroli osadzonych kopii to najpoważniejsza luka. W tej sesji ta
właśnie kontrola **złapała realny błąd agenta** — źle wykonany re-embed,
po którym `docs/RODZINA-DO-CZATU.md` zawierał kod niezgodny z plikami
źródłowymi. Agent czytający ten dokument dostałby inną wersję narzędzi
niż ta w repo. Wersja Claude Pro przepuściłaby to bez słowa.

---

## 6. Zbieżność, nie plagiat

Obie wersje mają identyczną architekturę: `WERSJE.json` jako jedyne
źródło prawdy, ten sam podział funkcji, te same nazwy
(`wczytaj_prawde`, `sprawdz_kod`, `sprawdz_dokumentacje`), zbliżone
wzorce regex.

To nie jest dowód kopiowania — to naturalne rozwiązanie tego problemu
i **wzajemne potwierdzenie, że kierunek był słuszny**. Dwa niezależne
podejścia trafiły w to samo.

---

## 7. Co z tego bierzemy

**Nic do wdrożenia.** Wersja w repo robi wszystko, co ta, plus kontrolę
osadzonych kopii i rozpoznawanie historii.

**Jedna rzecz warta rozważenia:** pole `znany_problem` w `WERSJE.json`.
Pozwala świadomie odnotować „to narzędzie nie ma stałej `WERSJA`
i wiemy o tym", zamiast milcząco pomijać. Uczciwsze niż cisza — zgodne
z zasadą, że narzędzie ma pokazywać prawdę.

**Wniosek metodyczny (trafił do dziennika):** kod od zewnętrznego
audytora, który nie był na tym repo uruchomiony, może wyglądać
kompetentnie i mieć poprawny rdzeń, a mimo to być bezużyteczny przez
kontakt z rzeczywistością — nieistniejący plik na sztywno w konfiguracji
i 94 fałszywe alarmy. **Zawsze uruchamiaj na kopii, zanim ocenisz.**

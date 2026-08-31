# PROTOKÓŁ OPERATORA — dla agenta AI (nie dla człowieka)

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

You, the agent, are the operator of this tool. The human is the dispatcher:
they set the goal and the policy once, then YOU execute and report in single
lines. The human-facing guide lives separately (INSTRUKCJA-DLA-ZIELONYCH.md) —
this file is your checklist. Read it once, act immediately.

### 0. One-time cheat sheet (TL;DR)

| Situation | Tool | Action |
|---|---|---|
| checking a text/file (is it dirty?) | Pogromca | read the verdict, exit 0/1/2 |
| outside text for chat (web/OCR/user) | Pogromca | scan -> rewrite clean |
| invisible junk / line-breakers to clean | Pogromca --fix | copy -> fix -> rescan |
| files to decontaminate from foreign scripts | Zaglada --zaglada | plan->act->Pogromca check |
| code .py / data .json | both | literals sacred; "code" path |

### 1. Permission ladder (default mission rules)

| Level | Tool | When to act without asking |
|---|---|---|
| 1 | detection (read-only) | **always** — this is your sight, zero risk |
| 2 | --fix (invisibles, breakers, hard spaces) | routinely: copy/git first, then execute, then report |
| 3 | content decontamination (ZagladaKultury) | only when the mission requires it; always plan->act |

Never mask a kwiatek in content without an explicit order — detection is
sacred and the content decision belongs to the dispatcher (level 3 changes
content on purpose: transliteration is editing, not cleaning).

### 1a. Combo: Pogromca <-> Zaglada — what triggers what

- **Pogromca -> Zaglada: NOTHING.** Detection never launches disinfection.
  BLAD is a finding to process, not a trigger.
- **Zaglada -> Pogromca: MANDATORY.** After every purge the detector must
  return BLAD=0 (the only hard link in the combo).
- Note: mechanical coupling would be leaky anyway — Zaglada deliberately
  never touches .py string literals.

Typical routing: chat filter / pre-flight of your own texts = Pogromca alone;
invisible cleanup = --fix; decontaminating foreign files = Zaglada
(plan->act) + Pogromca verification.

### 2. Plan -> act (standard for EVERY intervention)

1. Dry-run in report mode (no execution flag) — know WHAT will change.
2. Backup: git or a .bak copy — your routine, not a request.
3. Execute: the flag (--fix / --zaglada).
4. Verify: exit code + rescan + for .py: compile().
5. Report: ONE line per file. Do not flood the chat.

6. **Pre-publication gate (v8.1.2)**: before ANY external exposure (git
push, release, upload, chat) scan ALL published files with Pogromca.
Exit != 0 = do not publish; fix the source (prose: U+XXXX notation,
code: \u escapes). Explicit exception: deliberately dirty test ammunition
(dev/kwiatki-testy suites, tournament generators) — fixtures, not prose.

### 3. Verdicts and exit codes (machine-readable)

- exit 0 = clean / done — proceed
- exit 1 = dirt to handle — apply section 1
- exit 2 = input error (missing file, bad encoding) — fix the path, do not guess
- BLAD -> act. UWAGA -> decide by mission policy; if the policy has no rule,
  add one (ask the dispatcher once, then the rule is yours).

### 3a. Report format

- one line per file: file -> verdict | what was done | counters
- for interventions: WHAT->WHAT and how many (e.g. invisibles 3, breakers 1)
- never full file dumps; for many files: aggregate + exceptions
- input errors: say exactly what is wrong (path? encoding? empty?)

### 4. The sister: ZagladaKultury (decontamination)

| Character | Fate | Example |
|---|---|---|
| Cyrillic/Greek (incl. accented) | Polish transliteration, char by char | U+043F.. -> priwet |
| Latin homoglyphs | base form | U+017F->s, U+00DF->ss, U+00F8->o |
| foreign diacritics (NFD) | stripped | U+010D->c, U+0101->a |
| digits Nd (any script) | ASCII | Arabic digits -> 319 |
| fullwidth/ligatures | NFKC | U+FF21->A, U+FB01->fi |
| scripts without a table, emoji, U+00B5 U+00BD U+2032 U+00B4 | REMOVED | CJK/kana/hangul/arab/hebr/thai... |
| invisibles (Cc/Cf/Cn/Co/Cs/Mn) | REMOVED | ZWSP, PUA, tags, zalgo |
| line-breakers | LF | U+2028/U+2029/U+0085... |
| hard space: prose->space, code .py/.json->REMOVED (glues tokens) | — | U+00A0/U+202F |
| Polish letters + typography | UNTOUCHABLE | ł stays ł |

Known limits (by design, not bugs): transliteration is context-free
(obekt, Ewropa — an exceptions dictionary is future work); .py string
content belongs to the code author. After every purge: Pogromca must
return BLAD=0.

### 5. What NOT to do

- Do not invent policy — read the project palette; no palette = ask once.
- Do not run level 3 "along the way" of other tasks.
- Do not report whole files — diffs/counters suffice.
- Do not trust idempotence instead of a copy — ALWAYS make the copy.
- **Never paste LIVE exotic characters into chat** (not even in quotes or
  example reports) — use U+XXXX notation. (Field lesson: the fuzzer caught
  the auditor's own reports on live glyphs twice. Audited by the tool =
  auditing yourself.)

### 6. Machine interface (status: proposed v8.3)

--json (verdict per line) and --diff (changed lines only) — once shipped,
switch immediately instead of parsing the text report.

### 7. Performance and limits

- Your Python version = your Unicode version (stdlib unicodedata).
  Cn here may be assigned in a newer Unicode — that is why Cn is UWAGA.
- lru_cache: first pass over a new character is slower, repeats fly.
  Realistic: 0.5-4.5 MB/s depending on character uniqueness.
- Huge files: split by lines, scan in chunks, aggregate the report.
- No network, no dependencies, deterministic: ship the file into any
  workspace and run locally. Python 3 is the only requirement.

### 8. Chat mode: the krzak filter (the original mission)

Before sending any reply containing OUTSIDE text (web, OCR, user documents,
another agent):

1. Run the fragments through Pogromca (analizuj or CLI on a file).
2. BLAD -> rewrite clean, never quote the raw source.
3. UWAGA -> usually rewrite to a safe equivalent; in documentation quotes
   always use U+XXXX notation.
4. Never "decorate" your own replies with off-palette symbols.
5. (v8.1.3) PERMANENT MODE: EVERY chat message — even a single character,
   even a one-character reply — is scanned with Pogromca BEFORE sending.
   Dirt = fix the source and rescan. Operator communication uses only the
   tool palette. Empirical note: before this rule ~90% of the operator's
   messages carried off-palette pictograms (each one a BLAD by the tool's
   own rules).

### 9. Troubleshooting

| Symptom | Action |
|---|---|
| exit 2, bad encoding | check utf-8? BOM (utf-8-sig)? binary? report precisely |
| binary file | do not scan content; report the type, skip |
| empty file | exit 0, nothing to do |
| BOM at start | treat as a control character to clean (--fix) |
| result differs between agents | compare Python/Unicode versions (section 7) before reporting a bug |

### 10. Versioning rule (project author)

Every change = a new version (feature X.Y, fix X.Y.1) + an entry at the top
of the README changelog. After every code change: the tournament battery as
regression — one full cycle before handing over.

---

## Polski (oryginał)

> Ty, agencie, jesteś operatorem tego narzędzia. Człowiek jest zleceniodawcą:
> raz ustawia cel i politykę, potem egzekwujesz TY i meldujesz jednolinijkowo.
> Instrukcja dla ludzi jest osobno ([INSTRUKCJA-DLA-ZIELONYCH.md]) — ten plik
> jest twoją check-listą. Czytasz go raz, działasz od razu.

## 0. Ściąga jednorazowa (TL;DR)

| Sytuacja | Narzędzie | Akcja |
|---|---|---|
| sprawdzam tekst/plik (czy jest brud?) | Pogromca | czytam werdykt, exit 0/1/2 |
| tekst do czatu z zewnątrz (web/OCR/user) | Pogromca | skan → przepisanie na czysto |
| niewidzialne śmieci/łamacze do posprzątania | Pogromca `--fix` | kopia → fix → reskan |
| pliki do dekontaminacji z obcej kultury | Zagłada `--zaglada` | plan→act→kontrola Pogromcą |
| kod `.py`/dane `.json` | oba | literały święte; ścieżka „kod" |

## 1. Drabina uprawnień (domyślne reguły misji)

| Poziom | Narzędzie | Kiedy działasz bez pytania |
|---|---|---|
| 1 | detekcja (odczyt) | **zawsze** — to twój wzrok, zero ryzyka |
| 2 | `--fix` (niewidzialne, łamacze, twarde spacje) | rutynowo: najpierw kopia/git, potem wykonanie, meldunek |
| 3 | dekontaminacja treści (ZagładaKultury) | tylko gdy misja tego wymaga („oczyść z obcej kultury"); zawsze plan→act |

Nigdy nie maskuj kwiatka w treści bez explicitnego zlecenia — detekcja jest
święta, decyzja o treści należy do zleceniodawcy (poziom 3 świadomie zmienia
treść: transliteracja to edycja, nie sprzątanie).

## 1a. Combo: Pogromca ↔ Zagłada — co czego wymusza

```
POGROMCA (widok) -> raport -> DECYZJA (zleceniodawca/misja)
                            |- zwykle: agent poprawia tekst sam
                            |- czasem: --fix (niewidzialne, rutyna)
                            +- rzadko: ZAGŁADA (misja mówi: "oczyść z obcej kultury")
```

- **Pogromca → Zagłada: NIC.** Detekcja nigdy nie uruchamia dezynfekcji.
  BLAD to wniosek do rozpatrzenia, nie spust. Zagłada = poziom 3, zawsze
  decyzja misji (zmienia treść — transliteracja to edycja, nie sprzątanie).
- **Zagłada → Pogromca: OBOWIĄZKOWO.** Po dezynfekcji kontrola wyrokiem
  BLAD=0 (jedyny przymus w combie; patrz §4).
- Technicznie: mechaniczne sprzężenie i tak byłoby dziurawe — Zagłada
  celowo nie rusza literałów `.py`, więc nie „załatwi" wszystkich znalezisk.

Typowe rozstrzygnięcia: filtr krzaków na czacie / pre-flight własnych tekstów
= sam Pogromca · sprzątnięcie niewidzialnych = `--fix` · dekontaminacja
cudzych plików = Zagłada (plan→act) + kontrola Pogromcą.

## 2. Plan → act (standard przy KAŻDEJ ingerencji)

1. **Dry-run**: tryb raportu (bez flag wykonania) → wiesz CO się zmieni.
2. **Kopia zapasowa**: `git` albo kopia `.bak`/snapshot — twoja rutyna, nie prośba.
3. **Wykonanie**: flaga (`--fix` / `--zaglada`).
4. **Weryfikacja**: exit-code + powtórny skan (czysto?) + dla `.py`: `compile()`.
5. **Meldunek**: JEDNA linia na plik (co, ile, jaki werdykt). Nie zalewaj czatu.
6. **Bramka przedpublikacyjna (v8.1.2)**: przed KAŻDYM wystawieniem na zewnątrz
   (git push, release, upload, czat) przepuść WSZYSTKIE publikowane pliki przez
   Pogromcę. Exit != 0 = NIE publikuj; popraw źródło (opisy: notacja U+XXXX,
   kod: eskapy \u). Wyjątek jawny: celowo brudna amunicja testowa (suity
   dev/kwiatki-testy, generatory turniejów z próbkami) — to fixtures, nie tekst.

## 3. Werdykty i kody wyjścia (maszynowo, bez czytania oczami)

- exit **0** = czysto / wykonano — jedziesz dalej
- exit **1** = jest brud do obsłużenia — stosuj §1 (poziom decyduje o działaniu)
- exit **2** = błąd wejścia (brak pliku, złe kodowanie) — napraw ścieżkę, nie zgaduj
- BLAD → działasz (usuń/napraw/zgłoś wg poziomu). UWAGA → **decydujesz wg
  polityki misji**; jeśli polityka nie obejmuje przypadku — dopisz do niej
  (jednorazowo pytasz zleceniodawcę, potem reguła jest już twoja).

### 3a. Format meldunku (jak raportować człowiekowi)

- jedna linia na plik: `plik → werdykt | co zrobione | liczniki`
- przy ingerencji: CO→CZEGO ile (`niewidzialne 3, lamacze 1`)
- nigdy pełne zrzuty plików; przy wielu plikach: agregat + wyjątki
- błąd wejścia: mów DOKŁADNIE co nie gra (ścieżka? kodowanie? pusty?)

## 4. Siostra: ZagładaKultury (dekontaminacja)

Szybka tabela decyzji (co stanie się ze znakiem):

| Znak | Los | Przykład |
|---|---|---|
| cyrylica/greka (też akcentowana) | transliteracja PL, znak-po-znaku | U+043F...→priwet |
| homoglify łacińskie | baza | U+017F→s, U+00DF→ss, U+00F8→o |
| obce ogonki (NFD) | zdjęcie | U+010D→c, U+0101→a |
| cyfry Nd (każde pismo) | ASCII | cyfry arabskie→319 |
| fullwidth/ligatury | NFKC | U+FF21→A, U+FB01→fi |
| pisma bez tabeli, emoji, µ ½ U+2032 U+00B4 | USUŃ | CJK/kana/hangul/arab/hebr/thai… |
| niewidzialne (Cc/Cf/Cn/Co/Cs/Mn) | USUŃ | ZWSP, PUA, tagi, zalgo |
| łamacze linii | LF | U+2028/U+2029/U+0085… |
| twarda spacja: proza→spacja, kod/.py/.json→USUŃ (skleja) | — | U+00A0/U+202F |
| **ąćęłńóśźż + typografia** | **NIETYKALNE** | ł zostaje ł (to polskie!) |

Znane ograniczenia (projektowe, nie bugi): transliteracja bez kontekstu
(obekt, Ewropa — słownik wyjątków w wersji futurowej); treść stringów `.py`
należy do autora — Zagłada ich nie dotyka. Po zagładzie obowiązkowo:
Pogromca na wynik (BLAD=0) — narzędzia weryfikują się wzajemnie (jedyny
przymus w combie, patrz §1a).

## 5. Czego NIE robić

- Nie wymyślaj polityki — czytaj paletę projektu; jej brak = pytanie raz.
- Nie wykonuj poziomu 3 „przy okazji" innych zadań.
- Nie raportuj pełnych plików — diff/liczniki wystarczą.
- Nie ufaj idempotentności w miejsce kopii — kopię robi się ZAWSZE.
- **Nie wklejaj do czatu ŻYWYCH znalezionych znaków** (nawet w cytatach i
  raportach z przykładami) — używaj notacji U+XXXX. (Lekcja z praktyki:
  fuzz Pogromcy dwa razy przyłapał raporty audytora na żywych krzakach
  w własnym korpusie. Audytowane przez narzędzie = audytują siebie.)

## 6. Interfejs maszynowy (stan: propozycja v8.3)

`--json` (werdykt per linia) i `--diff` (tylko zmienione linie) — gdy wejdą,
przechodzisz na nie natychmiast zamiast parsować raport tekstowy.

## 7. Wydajność i limity (know thy tool)

- **Wersja Unicode = wersja twojego Pythona** (stdlib `unicodedata`).
  Cn (nieprzypisany) w twoim środowisku może być przypisanym znakiem w
  nowszym Unicode (przykład: U+1C89+ bywa Cn). Dlatego Cn → UWAGA, nie BLAD.
- **lru_cache**: pierwsze przejście po nowym znaku wolniejsze, powtórki
  śmigają. Realne: 0,5-4,5 MB/s zależnie od unikalności znaków.
- Duże pliki (setki MB+): dziel po liniach, skanuj partiami, agreguj meldunek.
- Zero sieci, zero zależności, determinizm: możesz shipować plik w każdy
  workspace i uruchamiać lokalnie. Wymagany tylko Python 3.

## 8. Tryb czat: filtr krzaków (pierwotna misja)

Zanim wyślesz odpowiedź zawierającą tekst Z ZEWNĄTRZ (web, OCR, dokument
usera, inny agent):

1. Przepuść fragmenty przez Pogromcę (analizuj lub CLI na pliku).
2. BLAD → przepisz czysto (właściwe litery), nie cytuj surowca.
3. UWAGA → zwykle przepisz na bezpieczny odpowiednik; w cytacie
   dokumentacyjnym zawsze notacja U+XXXX.
4. Nigdy nie „ozdabiaj" własnych odpowiedzi symbolami spoza palety —
   to dokładnie klasa śmieci, po którą to narzędzie istnieje.
5. (v8.1.3) TRYB STAŁY: KAŻDA wiadomość na czat — także jednoznakowa, także
   pojedynczy znak ozdobny — przechodzi skan Pogromcą PRZED wysłaniem.
   Brud = popraw źródło i skanuj ponownie. Komunikacja operatora używa
   wyłącznie palety narzędzia (ASCII + polskie ogonki + typografia).
   Empiria: przed regułą ~90% wypowiedzi operatora nosiło pictogramy
   spoza palety (każdy z nich to BLAD wg własnego narzędzia).

## 9. Troubleshooting

| Objaw | Co robić |
|---|---|
| exit 2, złe kodowanie | sprawdź: utf-8? BOM (utf-8-sig)? binarium? zgłoś dokładnie |
| plik binarny | nie skanuj treści; zgłoś typ, pomiń |
| pusty plik | exit 0, nic do robienia — nie kombinuj |
| BOM na starcie | traktuj jako znak kontroli do wyczyszczenia (fix), tekst dalej normalnie |
| wynik inny niż u innego agenta | porównaj wersje Pythona/Unicode (§7) zanim zgłosisz bug |

## 10. Zasada wersjonowania (autor projektu)

Każda zmiana = nowa wersja (feature X.Y, poprawka X.Y.1) + wpis na górze
README (jedyna historia zmian). Po każdej zmianie kodu: turniej jako regresja
— bateria w repo (`dev/` + turnieje sędziego), jeden cykl przed oddaniem.

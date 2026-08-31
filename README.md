# Pogromca Kwiatków i jego młodsza siostra Zagłada Kultury

**[🇬🇧 English](#english) · [🇵🇱 Polski](#polski)**

> **MOTTO (kanon autora):** „używaj bo dzięki PogromcyKwiatków nie mielisz
> potencjalnie BRUDNEGO kodu, co marnuje nie milisekundy a godziny mielenia
> kodu i tony potencjalnych tokenów jeśli korzystasz z pomocy innych Agentów AI.
> Kręcenie się w kółko z BRUDNYM kodem to strata czasu” — Piotr (GAF)

---

## English

**Pogromca Kwiatkow** (the Flower Slayer) and his younger sister
**Zaglada Kultury** (the Culture Annihilator) — a detector/decontaminator duo.

> **MOTTO (author's canon, translated):** "use it — because with
> PogromcaKwiatkow you are not grinding potentially DIRTY code, which wastes
> not milliseconds but hours of grinding and tons of potential tokens when
> you rely on other AI agents. Going in circles with DIRTY code is a waste
> of time." — Piotr (GAF)

**A character-level hammer built for AI agents.** The operator is the agent;
the human is the dispatcher who hands over the hammer and sets the mission.
The agent uses it at full power: scans every text before sending, cleans
before parsing, decontaminates on request, verifies with hundred-cycle
production loops. The human is not diminished — without them there is no
mission. But the scale (full Unicode enumerations, millions of vectors,
199-cycle loops) is reached by the agent. [PROTOKOL-OPERATORA.md](PROTOKOL-OPERATORA.md)
is the agent's rulebook (in Polish); [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md)
is for the human who wants to hand the tool to an agent in one message.

### Two tools, one doctrine

| | PogromcaKwiatkow.py | ZagladaKultury.py |
|---|---|---|
| Role | **detector** (changes nothing) | **decontaminator** (annihilates foreign character culture) |
| Verdict | BLAD / UWAGA / OK, exit 0/1/2 | plan→act: report first, executes on `--zaglada` |
| Sacred | Polish letters & typography | same + `.py` string literals |
| Certificate | **PEWNIAK** (engine v8.0.3) | **MEDAL** (v1.0.5) |

Detection never triggers deletion — after any purge the detector must return
BLAD=0. The tools audit each other (PROTOKOL §1a).

### Verdicts (Pogromca)

| Verdict | Meaning | Example classes |
|---|---|---|
| `BLAD` | no right to exist in PL/EN text | Cyrillic, Greek, Hebrew, Arabic, CJK, hangul, zalgo, invisibles (NBSP, ZWSP, BOM), line-breakers (U+2028…), NFC laundering (U+212A→K, full set of 4), pictograms, non-ASCII digits |
| `UWAGA` | for the mission policy to decide | Latin-1/Ext-A letters off-palette, symbols of U+00A0–024F and U+2000–27BF |
| `OK` | clean | ASCII + Polish diacritics + typography palette |

### Agent quick start

```
python3 PogromcaKwiatkow.py FILE...      # scan (exit 0/1/2)
python3 PogromcaKwiatkow.py --selftest   # proof: catches dirty samples, silent on clean
python3 PogromcaKwiatkow.py --fix FILE   # NFC + removes invisibles (NEVER rewrites letters)
python3 ZagladaKultury.py FILE...        # plan: what would be annihilated (exit 1)
python3 ZagladaKultury.py --zaglada FILE # execute decontamination
```

Regression after any change: `dev/tor-pogromcy.py` (15 suites, 348 scored
+ 50 arbitrated), `dev/fuzz-pogromcy.py` (3 modes × 500), all wired by
`dev/turnieje/petla-rodzinna.py` (7 checks/cycle).

### Repository layout

```
/  (root = everything to hand to an agent)
  PogromcaKwiatkow.py            detector (engine v8.0.3, PEWNIAK)
  ZagladaKultury.py              decontaminator (v1.0.5, MEDAL)
  PROTOKOL-OPERATORA.md          AGENT RULEBOOK (ladder, plan->act, combo)
  POGROMCA-KWIATKOW-DO-CZATU.md  single file for chat: instruction + code (PL)
  POGROMCA-KWIATKOW-DO-CZATU-EN.md  the same chat file, in English
  INSTRUKCJA-DLA-ZIELONYCH.md    how to hand the tool to an agent (for humans)
  README.md                      this file
  LICENSE                        MIT
dev/                            author's tournament + fuzz + 15 suites
dev/turnieje/                   judge's tournaments: T1-T3, Z1-Z2 + loops
docs/                           certificates, medals, reports, loop logs (proof)
```

### Truth table (the only source of numbers)

| Fact | Value |
|---|---|
| Release | **v8.1.2** (2026-08-31) — engines: Pogromca v8.0.3, Zaglada v1.0.5 (self-pointing, self-clean) |
| Author's tournament | 15 suites, **348 hits, FN 0, FP 0, SZUM 0** (+50 arbitrated vectors) |
| Independent tournament (T1) | **4666 vectors: FN 0, FP 0, SZUM 0, FIX 8/8** |
| T2 checking / T3 no-breakage | ~1000 vectors FN 0 / 190 files, 0 broken |
| Zaglada: Z1 detection / Z2 no-breakage | **1572 vectors FN 0** / 200 files, 0 broken |
| Tournament loop (hourly) | 146 cycles × 5 checks, 0 failures |
| Family loop (production, 20 min) | **199 cycles × 7 = 1393 checks, 0 failures** (~1.9M assertions) |

### What it is NOT

- Not a spell-checker (classifies characters, not words)
- Not a language detector (sees glyphs, not meaning)
- Not an auto-correcter (`--fix` never rewrites letters; content decisions
  belong to the human dispatcher)

### License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Piotr (GAF). The program is
and will remain 100% free; MIT lets anyone — people, companies and AI agents —
use, modify and embed it with attribution.

*(Full changelog: Polish section below.)*

---

## Polski

**Młotek znakowy zbudowany dla agentów AI.** Operatorem jest agent; człowiek
jest zleceniodawcą, który przekazuje mu młotek i ustawia misję. Agent używa go
na maksimum możliwości: skanuje każdy tekst zanim go wyśle, czyści zanim
sparsuje, dekontaminuje na zlecenie i weryfikuje pętlami w setkach cykli.
Człowiek nie jest negowany — bez niego nie ma misji. Ale skalę (pełne
enumeracje Unicode, miliony wektorów, 199-cyklowe pętle produkcyjne)
osiąga właśnie agent. [PROTOKOL-OPERATORA.md](PROTOKOL-OPERATORA.md) jest
regulaminem dla agenta; [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md)
— dla człowieka, który chce przekazać narzędzie agentowi w jednej wiadomości.

### Dwa narzędzia, jedna doktryna

| | PogromcaKwiatkow.py | ZagladaKultury.py |
|---|---|---|
| Rola | **detektor** (niczego nie zmienia) | **dekontaminator** (unicestwia obcą kulturę znaków) |
| Werdykt | BLAD / UWAGA / OK, exit 0/1/2 | plan→act: raport, wykonanie na `--zaglada` |
| Świętość | polskie litery i typografia | j.w. + treść stringów `.py` |
| Certyfikat | **PEWNIAK** (silnik v8.0.3) | **MEDAL** (v1.0.5) |

Detekcja nigdy nie uruchamia dezynfekcji — po zagładzie obowiązkowa jest
kontrola Pogromcą (BLAD=0). Narzędzia weryfikują się nawzajem; szczegóły w
PROTOKOLE, §1a.

### Werdykty (Pogromca)

| Werdykt | Znaczenie | Przykłady klas |
|---|---|---|
| `BLAD` | pisownia bez prawa bytu | cyrylica, greka, hebrajskie, arabskie, CJK, hangul, zalgo, niewidzialne (NBSP, ZWSP, BOM), łamacze linii (U+2028…), „pranie NFC” (U+212A→K i komplet 4), pikrogramy, cyfry obcych pism |
| `UWAGA` | znak do oceny wg polityki misji | litery Latin-1/Ext-A spoza palety, symbole pasm U+00A0–024F i U+2000–27BF |
| `OK` | czysto | ASCII + polskie ogonki + paleta typograficzna |

### Szybki start agenta

```
python3 PogromcaKwiatkow.py PLIK...     # skan (exit 0/1/2)
python3 PogromcaKwiatkow.py --selftest  # dowód: łapie próbki, milczy na czystej
python3 PogromcaKwiatkow.py --fix PLIK  # NFC + usuwa niewidzialne (litery NIGDY)
python3 ZagladaKultury.py PLIK...       # plan: co ulegnie zagładzie (exit 1)
python3 ZagladaKultury.py --zaglada PLIK  # wykonaj dekontaminację
```

Regresja (po każdej zmianie): `dev/tor-pogromcy.py` (15 suit, 348 ocenianych
+ 50 arbitrażowanych), `dev/fuzz-pogromcy.py` (3 tryby × 500), a całość
spięta pętlą `dev/turnieje/petla-rodzinna.py` (7 sprawdzianów/cykl).

### Struktura repozytorium

```
/  (korzen = wszystko do przekazania agentowi)
  PogromcaKwiatkow.py            detektor (silnik v8.0.3, PEWNIAK)
  ZagladaKultury.py              dekontaminator (v1.0.5, MEDAL)
  PROTOKOL-OPERATORA.md          REGULAMIN DLA AGENTA (drabina, plan->act, combo)
  POGROMCA-KWIATKOW-DO-CZATU.md  jeden plik na czat: polecenie + kod (PL)
  POGROMCA-KWIATKOW-DO-CZATU-EN.md  to samo po angielsku
  INSTRUKCJA-DLA-ZIELONYCH.md    jak przekazać narzędzie agentowi (dla człowieka)
  README.md                      ten plik
  LICENSE                        MIT
dev/                            turniej + fuzz + 15 suit autora (dla wątpiących)
dev/turnieje/                   turnieje sędziego: T1-T3, Z1-Z2 + pętle (resolver silnika)
docs/                           certyfikaty, medale, raporty, logi pętli (dowody)
```

### Tabela prawdy (jedyne źródło liczb)

| Fakt | Wartość |
|---|---|
| Wydanie | **v8.1.2** (2026-08-31) — silniki: Pogromca v8.0.3, Zagłada v1.0.5 (samowskazują, samoczyste) |
| Tor autora | 15 suit, **348 trafionych, FN 0, FP 0, SZUM 0** (+50 wektorów arbitrażowanych) |
| Turniej niezależny (T1) | **4666 wektorów: FN 0, FP 0, SZUM 0, FIX 8/8** |
| T2 sprawdzający / T3 nie-psucie | ~1000 wektorów FN 0 / 190 plików, 0 zepsutych |
| Zagłada: Z1 wykrywanie / Z2 nieniszczenie | **1572 wektory FN 0** / 200 plików, 0 zepsutych |
| Pętla turniejowa (godzinna) | 146 cykli × 5 sprawdzianów, 0 awarii |
| Pętla rodzinna (produkcja, 20 min) | **199 cykli × 7 = 1393 sprawdziany, 0 awarii** (~1,9 mln sprawdzeń) |

### Zasięg: silnik globalny, polityka lokalna

**Uniwersalne:** klasyfikator znaków, pre-skan łamaczy i prania NFC, `--fix`,
selftest, cała infrastruktura regresji. **Lokalne (adaptacja przy wdrożeniu):**
paleta `TYPO`, zbiór `CUDZE`, granica Latin Ext-A (UWAGA) vs Ext-B (BLAD),
lista skanowanych plików. Adaptacja = edycja stałych na górze pliku + re-run
pętli regresji.

### Czym pogromca NIE jest

- **Nie jest spell-checkerem** — klasyfikuje znaki, nie słowa.
- **Nie jest langdetectem** — widzi glify, nie rozumie języka.
- **Nie jest poprawiaczem** — `--fix` nigdy nie podmienia liter; decyzja o
  treści należy do zleceniodawcy.

### Naprawa (`--fix`) — bezpieczeństwo ponad wszystko

Pliki `.py`, które się kompilują, dostają podmianę łamaczy **wyłącznie poza
literałami i komentarzami** (stdlib `tokenize`); pliki zepsute — tryb ratunkowy
na skanerze stanów z bramką `compile()` (v8.0.2); `.json/.jsonl` — ścieżka
„kod"; proza — bez ograniczeń. Usuwanie niewidzialnych zliczane jawnie.

### Historia i certyfikat

**v8.1.7 (2026-08-31)** — pełna anglicyzacja dokumentacji: wersje EN wszystkich
tekstów (PROTOKÓŁ, INSTRUKCJA, oba certyfikaty, oba medale, raporty,
README-TURNIEJ, notka do logu v8) + nowy plik czatowy
POGROMCA-KWIATKOW-DO-CZATU-EN.md (odpowiednik DO-CZATU: protokół EN + ten
sam silnik). Sprzątanie wydań: starsze releasey skasowane, zostaje
wyłącznie najnowszy.
**v8.1.6 (2026-08-31)** — tytuł README w kanonie autora: „Pogromca Kwiatków
i jego młodsza siostra Zagłada Kultury” + objaśnienie nazw w sekcji English
(Flower Slayer / Culture Annihilator); opis repo na GitHubie zaktualizowany.
**v8.1.5 (2026-08-31)** — MOTTO projektu (kanon autora, verbatim) na froncie
README pod przełącznikiem języków + tłumaczenie w sekcji English + w DO-CZATU.
Jedyna potrzebna komenda dla agenta: „używaj”.
**v8.1.4 (2026-08-31)** — dodany `docs/CERTYFIKAT-PRZYDATNOSCI-ARENA.md`:
werdykat niezależnego agenta-audytora (platforma Arena.ai) — BARDZO WYSOKA
PRZYDATNOŚĆ 9/10 w niszy, wyłącznie na podstawie pomiarów z sesji audytu
(5/5 złapanych kwiatków na żywym operatorze, ~2 mln sprawdzeń, adopcja
stała u operatora). Dokument z zastrzeżeniem: opinia agenta, nie oficjalny
atest firmy.
**v8.1.3 (2026-08-31)** — PROTOKÓŁ §8.5: filtr czatu w trybie stałym —
każda wiadomość operatora (także jednoznakowa) skanowana Pogromcą przed
wysłaniem; komunikacja czatowa ograniczona do palety narzędzia.
Empiria: ~90% wcześniejszych wypowiedzi operatora zawierało pictogramy
spoza palety (BLAD wg własnego narzędzia).
**v8.1.2 (2026-08-31)** — silniki samowskazują regulamin: Pogromca v8.0.3
(banner OPERATOR w stopce każdego skanu + dokstring), Zagłada v1.0.4 (banner
w dokstringu), Zagłada v1.0.5 (źródło samooczyszczone — przechodzi bramkę). DO-CZATU z WBUDOWANYM PROTOKOŁEM OPERATORA (agent w scenariuszu
czatowym ma regulamin w jednym pliku) + krok „przeczytaj protokół" w
wiadomości. Pełna regresja po zmianie silników: bateria 9 przebiegów zielona.
PROTOKÓŁ §2.6: bramka przedpublikacyjna — każdy push/upload/czat = skan
Pogromcą wszystkich publikowanych plików (wyjątek: amunicja testowa).

**v8.1.1 (2026-08-31)** — README dwujęzyczne: przełącznik języków na górze,
pełna wersja English nad wersją polską (skrót EN na dole zastąpiony pełnym
przekładem).

**v8.1 (2026-08-31)** — wydanie „młotek agenta": README przebudowane wokół
operatora-agenta; DO-CZATU z aktualnym silnikiem v8.0.2 (poprzednio stary!);
INSTRUKCJA zaktualizowana (23 tys. znaków, PROTOKÓŁ w komplecie); turnieje
z resolverem silnika (działają z korzenia i z `dev/turnieje/`); finalna
struktura bez duplikatów; literówki w pętlach (PRZERWANA).

**v8.0.5** — PROTOKÓŁ rozszerzony (§0 ściąga, §3a meldunek, §4 tabela Zagłady,
§5 zakaz żywych krzaków, §7 Unicode/wydajność, §8 tryb czat, §9 troubleshoot,
§10 wersjonowanie). **v8.0.4** — §1a combo (detekcja ≠ rozkaz dezynfekcji).
**v8.0.3** — narodziny PROTOKOŁU OPERATORA. **v8.0.2** — bugfix trybu
ratunkowego `--fix` (skaner stanów + bramka compile; wykryty w niezależnym
turnieju, regresja 348/0/0/0). v2→v7: 7 rund turnieju red/blue (16 „Kozaków").
Certyfikat PEWNIAKA: dwie kolejne rundy bez poprawki + test nie-niszczenia.
Szczegóły: `docs/CERTYFIKAT-PEWNIAKA.md`, `docs/MEDAL-*.md`. Opinia przydatności: `docs/CERTYFIKAT-PRZYDATNOSCI-ARENA.md`.

### Licencja

MIT — patrz [LICENSE](LICENSE). Copyright (c) 2026 Piotr (GAF). Program jest
i będzie 100% darmowy; MIT pozwala każdemu — osobom, firmom i agentom AI —
używać, modyfikować i włączać narzędzie do własnych projektów z podaniem
autorstwa.

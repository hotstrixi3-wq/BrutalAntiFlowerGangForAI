# PogromcaKwiatków + ZagładaKultury — młotek znakowy dla agenta AI

> **To narzędzie zbudowano dla agentów AI.** Operator jest agent; człowiek jest
> zleceniodawcą, który przekazuje mu młotek i ustawia misję. Agent używa go na
> maksimum możliwości: skanuje każdy tekst zanim go wyśle, czyści zanim
> sparsuje, dekontaminuje na zlecenie i weryfikuje pętlami w setkach cykli.
> Człowiek nie jest negowany — bez niego nie ma misji. Ale skalę (pełne
> enumeracje Unicode, miliony wektorów, 199-cyklowe pętle produkcyjne)
> osiąga właśnie agent. [PROTOKOL-OPERATORA.md](PROTOKOL-OPERATORA.md) jest
> instrukcją dla agenta; [INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md)
> — dla człowieka, który chce przekazać narzędzie agentowi w jednej wiadomości.

## Dwa narzędzia, jedna doktryna

| | PogromcaKwiatkow.py | ZagladaKultury.py |
|---|---|---|
| Rola | **detektor** (niczego nie zmienia) | **dekontaminator** (unicestwia obcą kulturę znaków) |
| Werdykt | BLAD / UWAGA / OK, exit 0/1/2 | plan→act: raport, wykonanie na `--zaglada` |
| Świętość | polskie litery i typografia | j.w. + treść stringów `.py` |
| Certyfikat | **PEWNIAK** (silnik v8.0.2) | **MEDAL** (v1.0.3) |

Detekcja nigdy nie uruchamia dezynfekcji — po zagładzie obowiązkowa jest
kontrola Pogromcą (BLAD=0). Narzędzia weryfikują się nawzajem; szczegóły w
PROTOKOLE, §1a.

## Werdykty (Pogromca)

| Werdykt | Znaczenie | Przykłady klas |
|---|---|---|
| `BLAD` | pisownia bez prawa bytu | cyrylica, greka, hebrajskie, arabskie, CJK, hangul, zalgo, niewidzialne (NBSP, ZWSP, BOM), łamacze linii (U+2028…), „pranie NFC” (U+212A→K i komplet 4), pikrogramy, cyfry obcych pism |
| `UWAGA` | znak do oceny wg polityki misji | litery Latin-1/Ext-A spoza palety, symbole pasm U+00A0–024F i U+2000–27BF |
| `OK` | czysto | ASCII + polskie ogonki + paleta typograficzna |

## Szybki start agenta

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

## Struktura repozytorium

```
/  (korzen = wszystko do przekazania agentowi)
  PogromcaKwiatkow.py            detektor (silnik v8.0.2, PEWNIAK)
  ZagladaKultury.py              dekontaminator (v1.0.3, MEDAL)
  PROTOKOL-OPERATORA.md          REGULAMIN DLA AGENTA (drabina, plan->act, combo)
  POGROMCA-KWIATKOW-DO-CZATU.md  jeden plik na czat: polecenie + kod
  INSTRUKCJA-DLA-ZIELONYCH.md    jak przekazać narzędzie agentowi (dla człowieka)
  README.md                      ten plik
  LICENSE                        MIT
dev/                            turniej + fuzz + 15 suit autora (dla wątpiących)
dev/turnieje/                   turnieje sędziego: T1-T3, Z1-Z2 + petle (resolver silnika)
docs/                           certyfikaty, medale, raporty, logi pętli (dowody)
```

## Wydanie v8.1 — tabela prawdy (jedyne źródło liczb)

| Fakt | Wartość |
|---|---|
| Wydanie | **v8.1** (2026-08-31) — silnik bez zmian: Pogromca v8.0.2, Zagłada v1.0.3 |
| Tor autora | 15 suit, **348 trafionych, FN 0, FP 0, SZUM 0** (+50 wektorów arbitrażowanych) |
| Turniej niezależny (T1) | **4666 wektorów: FN 0, FP 0, SZUM 0, FIX 8/8** |
| T2 sprawdzający / T3 nie-psucie | ~1000 wektorów FN 0 / 190 plików, 0 zepsutych |
| Zagłada: Z1 wykrywanie / Z2 nieniszczenie | **1572 wektory FN 0** / 200 plików, 0 zepsutych |
| Pętla turniejowa (godzinna) | 146 cykli × 5 sprawdzianów, 0 awarii |
| Pętla rodzinna (produkcja, 20 min) | **199 cykli × 7 = 1393 sprawdziany, 0 awarii** (~1,9 mln sprawdzeń) |

## Zasięg: silnik globalny, polityka lokalna

**Uniwersalne:** klasyfikator znaków, pre-skan łamaczy i prania NFC, `--fix`,
selftest, cała infrastruktura regresji. **Lokalne (adaptacja przy wdrożeniu):**
paleta `TYPO`, zbiór `CUDZE`, granica Latin Ext-A (UWAGA) vs Ext-B (BLAD),
lista skanowanych plików. Adaptacja = edycja stałych na górze pliku + re-run
pętli regresji.

## Czym pogromca NIE jest

- **Nie jest spell-checkerem** — klasyfikuje znaki, nie słowa.
- **Nie jest langdetectem** — widzi glify, nie rozumie języka.
- **Nie jest poprawiaczem** — `--fix` nigdy nie podmienia liter; decyzja o
  treści należy do zleceniodawcy.

## Naprawa (`--fix`) — bezpieczeństwo ponad wszystko

Pliki `.py`, które się kompilują, dostają podmianę łamaczy **wyłącznie poza
literałami i komentarzami** (stdlib `tokenize`); pliki zepsute — tryb ratunkowy
na skanerze stanów z bramką `compile()` (v8.0.2); `.json/.jsonl` — ścieżka
„kod"; proza — bez ograniczeń. Usuwanie niewidzialnych zliczane jawnie.

## Historia i certyfikat

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
Szczegóły: `docs/CERTYFIKAT-PEWNIAKA.md`, `docs/MEDAL-*.md`.

## Licencja

MIT — patrz [LICENSE](LICENSE). Copyright (c) 2026 Piotr (GAF). Program jest
i będzie 100% darmowy; MIT pozwala każdemu — osobom, firmom i agentom AI —
używać, modyfikować i włączać narzędzie do własnych projektów z podaniem
autorstwa.

## English summary (in brief)

**A character-level hammer built for AI agents.** PogromcaKwiatkow detects
foreign-script "kwiatki" (homoglyphs, invisible characters, line-breakers,
NFC laundering, non-ASCII digits) in Polish/English texts; ZagladaKultury
decontaminates on request (Polish transliteration, diacritics stripped,
scriptless glyphs removed — Polish letters untouchable). Detection never
triggers deletion; after any purge the detector must return BLAD=0.
Single-file stdlib Python 3, deterministic, exit-code machine interface.
The human dispatcher hands the tool to an agent (see PROTOKOL-OPERATORA.md);
the agent runs it at machine scale — full Unicode enumerations, tournament
batteries, 199-cycle production loops. Certified: PEWNIAK (engine v8.0.2),
MEDAL (Zaglada v1.0.3). MIT, 100% free.

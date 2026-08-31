# PogromcaKwiatków

> **Oficjalne repozytorium:** https://github.com/hotstrixi3-wq/pogromca-kwiatkow

Wykrywacz obcojęzycznych „kwiatków” w tekstach pisanych po polsku (i ogólnie
łaciną). **Kwiatek** — w slangu pisarzy i redaktorów: literówka, potknięcie
pisarskie. Narzędzie terminuje kwiatki **programowo, przed wrzutą** — tam,
gdzie oko człowieka i tokenizator modelu językowego nie sięgają.

## Nie znasz się? Zacznij tutaj

**[POGROMCA-KWIATKOW-DO-CZATU.md](POGROMCA-KWIATKOW-DO-CZATU.md)** — jeden plik .md do wrzucenia na czat: agent wytnie z niego kod i uruchomi (chat nie przyjmuje .py, a .md tak).
**[INSTRUKCJA-DLA-ZIELONYCH.md](INSTRUKCJA-DLA-ZIELONYCH.md)** — jak dać
narzędzie agentowi AI w jednej wiadomości do skopiowania (bez żadnej
wiedzy technicznej). Raport z testu „nie niszczy kodu”: 
**[RAPORT-TESTU-KWITNICA.md](docs/RAPORT-TESTU-KWITNICA.md)** (100% plików
przywróconych do wzorca).

## Po co to istnieje

Modele językowe generują tekst token po tokenie i potrafią „wskoczyć” w zły
alfabet: słowa o wspólnym korzeniu słowiańskim, glify identyczne z łacińskimi,
niewidzialne znaki formatujące, homoglify. Takie wycieki przechodzą nawet
wzrokową korektę. Pogromca klasyfikuje **każdy znak osobno** i raportuje
linia/znak/kontekst — bez słowników, bez langdetectu, bez sieci: stdlib,
jeden plik, deterministycznie.

## Werdykty

| Werdykt | Znaczenie | Przykłady klas |
|---|---|---|
| `BLAD` | pisownia bez prawa bytu | cyrylica, greka, hebrajskie, arabskie, CJK, hangul, zalgo, niewidzialne (NBSP, ZWSP, BOM), łamacze linii (U+2028…), „pranie NFC” (U+212A→K i komplet 4), pikrogramy, cyfry obcych pism |
| `UWAGA` | znak do oceny człowieka | litery Latin-1/Ext-A spoza palety, symbole pasm U+00A0–024F i U+2000–27BF |
| `OK` | czysto | ASCII + polskie ogonki + paleta typograficzna |

## Struktura repozytorium

```
/  (korzen = wszystko do wdrozenia u agenta)
  PogromcaKwiatkow.py            narzedzie (v8.0.2, PEWNIAK)
  ZagladaKultury.py              siostra: dekontaminator obcej kultury znakow (v1.0.3, MEDAL)
  PROTOKOL-OPERATORA.md          regulamin użycia dla agenta AI (drabina, plan->act, combo)
  POGROMCA-KWIATKOW-DO-CZATU.md  jeden plik na czat: polecenie + kod
  INSTRUKCJA-DLA-ZIELONYCH.md    4 metody wdrozenia (zalacznik .md/.py, wklej, internet)
  README.md                      dokumentacja (PL + English summary)
  LICENSE                        MIT
dev/                            turniej + fuzz + 15 suit (dla watpiacych)
dev/turnieje/                   turnieje sedziego niezaleznego + petle (T1-T3, Z1-Z2)
docs/                           certyfikat + raporty + KOMPLECIK (dowody)
docs/                           + MEDAL-PEWNIAKA v8.0.2, MEDAL-ZAGLADY v1.0.3, logi petli
```

## Szybki start

```
python3 PogromcaKwiatkow.py PLIK...     # skan wskazanych plików
python3 PogromcaKwiatkow.py --selftest  # dowód: łapie próbkę brudną, milczy na czystej
python3 PogromcaKwiatkow.py --fix PLIK  # NFC + usuwa niewidzialne (NIGDY nie podmienia liter)
python3 tor-pogromcy.py                 # turniej: 13 suit regresji (294 wektory)
python3 fuzz-pogromcy.py                # fuzz deterministyczny (3 tryby × 500)
```

Exit: `0` = czysto, `1` = BLAD. Bez argumentów skanuje `.md`/`.txt` wokół
siebie (sekcja `domyslne_pliki()` — do adaptacji pod swój projekt).

## Zasięg: silnik globalny, polityka lokalna

**Uniwersalne (niezależne od projektu):** klasyfikator znaków i wszystkie
klasy kwiatków z tabeli wyżej, pre-skan łamaczy linii i prania NFC,
`--fix`, selftest, oraz cała infrastruktura regresji (tor + fuzz + suity).

**Lokalne (do adaptacji przy wdrożeniu):** paleta `TYPO` (typografia
udokumentowana w macierzystym projekcie), zbiór `CUDZE` (czeski/słowacki/
węgierski — projekt jest PL/EN), granica Latin Ext-A (UWAGA) vs Ext-B
(BLAD), lista skanowanych plików. Adaptacja = edycja stałych na górze
pliku; przy każdej zmianie re-run pełnej pętli (tor + fuzz + selftest).

## Czym pogromca NIE jest

- **Nie jest spell-checkerem** — „blad” pisane samym ASCII przechodzi
  czysto (klasyfikuje znaki, nie słowa); werdykt pada dopiero, gdy literówka
  przekroczy granicę alfabetu lub rodziny diakrytyków (U+0161, U+0151,
  cyrylickie „o” → BLAD z etykietą HOMOGLIF).
- **Nie jest langdetectem** — nie rozumie języka, widzi glify.
- **Nie jest poprawiaczem** — `--fix` nigdy nie podmienia liter; decyzja
  należy do człowieka.

## Naprawa (`--fix`) — bezpieczeństwo ponad wszystko

Od v8: pliki `.py`, które się kompilują, dostają podmianę łamaczy linii
**wyłącznie poza literałami, f-stringami i komentarzami** (stdlib `tokenize`);
proza — bez ograniczeń. Od v8.0.2 także tryb ratunkowy (pliki zepsute)
podmienia łamacze **tylko poza literałami i komentarzami** (awaryjny skaner
stanów), a każdy zapis przechodzi bramkę `compile()` — gdy nic nie kompiluje,
zostaje wariant minimalnie inwazyjny. Usuwanie niewidzialnych
zliczane jawnie w komunikacie. Selftest testuje i detekcję, i naprawę.

## Historia i certyfikat

**v8.0.5 (2026-08-31)** — dokumentacja, kod silnika bez zmian: PROTOKÓŁ-
OPERATORA rozbudowany dla agentów (§0 ściąga, §3a format meldunku, §4 tabela
decyzji Zagłady, §5 zakaz żywych krzaków w czacie, §7 wydajność/limit Unicode,
§8 tryb czat, §9 troubleshooting, §10 wersjonowanie). Zasada: narzędzie
projektowane przez agenta dla agenta — protokół zapisuje praktykę z turniejów.

**v8.0.4 (2026-08-31)** — dokumentacja, kod silnika bez zmian: PROTOKÓŁ-
OPERATORA rozszerzony o doktrynę comba Pogromca↔Zagłada (§1a: detekcja
NIE wymusza dezynfekcji — Zagłada opcjonalna, zawsze decyzja misji;
obowiązkowa kontrola Pogromcą po zagładzie; typowe rozstrzygnięcia użycia).

**v8.0.3 (2026-08-31)** — dokumentacja, kod silnika bez zmian: dodany
**PROTOKÓŁ-OPERATORA.md** — reguły użycia maszynowego dla agentów AI
(drabina uprawnień, plan→act, kody wyjścia, meldunek jednolinijkowy).
Narzędzie jest projektowane dla agentów; instrukcja dla ludzi pozostaje
w INSTRUKCJI-DLA-ZIELONYCH.md.

**v8.0.2 (turniej niezależny, 2026-08-31)** — bug fix trybu ratunkowego `--fix`:
zepsuty `.py` z łamaczem linii w stringu dostawał slepą podmianę także w
literale (efekt: *unterminated string literal*). Teraz: skaner stanów chroni
literały i komentarze, bramka `compile()` pilnuje wyniku. Wykryto w niezależnym
turnieju zewnętrznego audytora (runda R13, scenariusz 6); regresja: tor 348/0/0/0.

v2 → v7 przez 7 rund turnieju red-team/blue-team (16 przeciwników
„Kozaków”, 13 suit, 341 wektorów). Certyfikat PEWNIAKA: dwie kolejne rundy bez żadnej poprawki w kodzie (v7: 294/0/0/0; v8: 322 i 348/0/0/0)
plus bonusowy test nie-niszczenia kodu na żywym produkcie (8/8 scenariuszy).
Szczegóły: `CERTYFIKAT-PEWNIAKA.md`.

## Licencja

MIT - patrz [LICENSE](LICENSE). Copyright (c) 2026 Piotr (GAF). Program
jest i bedzie 100% darmowy; MIT dodatkowo pozwala kazdemu - osobom, firmom
i agentom AI - uzywac, modyfikowac i wlaczac narzedzie do wlasnych
projektow z podaniem autorstwa.

## English summary (in brief)

PogromcaKwiatkow ("kwiatki slayer") is a zero-dependency, single-file Python
tool that detects foreign-alphabet letters and invisible characters leaking
into text and source code: homoglyph confusables (e.g. Cyrillic letters
inside Polish words), zero-width spaces, non-breaking spaces, BOM,
line separators (U+2028/U+2029), "NFC laundering" singletons (U+212A KELVIN
SIGN and friends), pictograms, zalgo and more.

Why: language models generate text token by token and occasionally slip
into the wrong alphabet; such glitches look identical to the human eye and
pass review. This tool catches them programmatically, before they ship.

Verdicts: BLAD (definitely wrong) / UWAGA (for human review) / OK.
The `--fix` mode removes ONLY invisible characters - it never replaces
letters, and in compilable .py files it is literal-aware (stdlib tokenize),
so string contents stay intact.

Evidence: certified through 11 red-team tournament rounds (19 adversarial
generators, 368 regression vectors, zero misses - see docs/), plus a
code-safety test: 20 real CPython files infected with 40 invisible-character
bugs -> 100% detected, 100% restored byte-for-byte.

Quickest use: attach POGROMCA-KWIATKOW-DO-CZATU.md to any AI-agent chat -
it carries both the instructions and the full source. License: MIT.

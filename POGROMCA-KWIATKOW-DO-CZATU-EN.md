# PogromcaKwiatkow — the chat delivery file (English)

This ONE .md file contains everything: an instruction for you, a message
for the AI agent, and the complete tool code. You do not need to download
anything from GitHub or install anything.

## You (the human): do just this

1. Attach this file to a chat with an AI agent.
2. Paste the message below (all of it, unchanged except the brackets).

## Message for the agent (copy in full)

```
Hi! In the attached .md file (POGROMCA-KWIATKOW-DO-CZATU-EN.md) you have the
PogromcaKwiatkow tool. Do exactly this:

1. Read the OPERATOR PROTOCOL section (further down in this file) — it is
   your rulebook for working with the tool. Follow it.
2. Cut the code from the block marked as python (at the bottom, under the
   "TOOL CODE" heading) and save it as PogromcaKwiatkow.py.
3. Run: python3 PogromcaKwiatkow.py --selftest  (must be PASS).
4. Scan: [ENTER THE FILE OR FOLDER PATH HERE].
5. Show me the report in plain English: what was found, where (file,
   line), and what it means (BLAD = definitely a problem, UWAGA = my call).
6. Do NOT change my files without my explicit consent.
```

## What next?

Nothing. The agent knows what to do — the manual ships with the tool.
The only command it will ever need from you is: "use it".

- Is it an antivirus? No — it is text control: characters and alphabets.
- Will it fix typos? No — it guards alphabets, not spelling.
- Offline? Yes — one file, pure Python 3.
- The agent lost the file? Hand it over again.

## OPERATOR PROTOCOL (agent: read and follow — these are your rules)

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

## TOOL CODE (agent: cut the whole block below into PogromcaKwiatkow.py)

```python
# -*- coding: utf-8 -*-
"""PogromcaKwiatków: wykrywacz obcojęzycznych "kwiatków" w polskich tekstach projektu.

(v8.0.3) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
ze siostra ZagladaKultury). Przeczytaj przed pierwszym uzyciem.

Slownik kulturalny: "kwiatek" = w slangu pisarzy i redaktorow GAFa w tekscie,
literowka, potkniecie pisarskie (nie bukiet!). Stad nazwa: narzedzie
TERMINUJE kwiatki, zanim ujrzą swiatlo dzienne.
(chrztet imienia: kwiatkiorz -> KWIATEK TERMINATOR -> PogromcaKwiatków;
wszystkie trzy ochrzcił user, tura 49)

Powód narzędzia (tura 49): asystent wkleił w czacie rosyjskie słowo w polskie
zdanie ("Spokojnie [cyrylica] spać") — model językowy generuje token po
tokenie, a słowa o wspólnym korzeniu słowiańskim + glifach identycznych
z łacińskimi potrafią wskoczyć w zły alfabet i przejść nawet wzrokową
korektę. Narzędzie łapie takie wycieki PROGRAMOWO, przed wrzutą.

Zasady:
- BLAD: pisownie, które w polskich tekstach projektu nie mają prawa bycia
  (cyrylica, greka, hebrajskie, arabskie, dewanagari, tajskie, kana,
  CJK, hangul).
- UWAGA: każdy inny znak poza ASCII + polskimi ogonkami + typografią
  (do oceny człowieka, np. czeskie lub slowackie ogonki, emoji).
- OK: ASCII + ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ + typografia projektowa.

Użycie:
  python3 pewniaki/PogromcaKwiatkow.py            # dokumentacja + produkt + NOTATKI
  python3 pewniaki/PogromcaKwiatkow.py PLIK...    # wskazane pliki
  python3 pewniaki/PogromcaKwiatkow.py --selftest  # dowód: łapie próbkę z czatu
  python3 pewniaki/PogromcaKwiatkow.py --fix        # NFC + usuwa NIEWIDZIALNE (NIGDY nie podmienia liter)
Exit: 0 = czysto, 1 = BLAD.
"""
import io
import os
import sys
import unicodedata
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(HERE)

OGONKI = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
TYPO = set("—–„”\"'…«»·×±→←↔⇄≤≥≈≠°%§€•●○◀▶✕✓✔↑↓")
# po ludzkiej ocenie (tura 49): legalna typografia projektu
TYPO |= set(chr(c) for c in (0x2212, 0x2705, 0x274C))  # minus matematyczny, ✅, ❌
TYPO |= set(chr(c) for c in range(0x2500, 0x2580))    # linie diagramow (MAPA)
TYPO |= set(chr(c) for c in range(0x1F1E6, 0x1F200))  # flagi (README.md)
TYPO |= set("’£½¼¾⌘⌥⇧⌃❓📌📍™²³¹µ¶")  # (kozak 2B) apostrof, waluty, ulamki, skroty, emoji z MAPA-LOGIKI

BLOKOWANE = [
    (0x0370, 0x03FF, "GREKA"),
    (0x0400, 0x052F, "CYRYLICA"),
    (0x0530, 0x058F, "ORMIAŃSKIE"),
    (0x0590, 0x05FF, "HEBRAJSKIE"),
    (0x0600, 0x06FF, "ARABSKIE"),
    (0x0900, 0x097F, "DEWANAGARI"),
    (0x0E00, 0x0E7F, "TAJSKIE"),
    (0x3040, 0x30FF, "KANA (japońskie)"),
    (0x4E00, 0x9FFF, "CJK (chińskie/japońskie)"),
    (0xAC00, 0xD7AF, "HANGUL (koreańskie)"),
    (0xFF66, 0xFF9F, "KATAKANA półszerokości"),
    # (turniej Kozakow, tura 49) klasy pusczone w 1. biegu + luki architekta:
    (0x1C80, 0x1C88, "CYRYLICA ext-C"),
    (0x2DE0, 0x2DFF, "CYRYLICA ext-A"),
    (0xA640, 0xA69F, "CYRYLICA ext-B"),
    (0x1F00, 0x1FFF, "GREKA ext"),
    (0x2C00, 0x2C5F, "GLAGOLICA"),
    (0x2C80, 0x2CFF, "KOPTYJSKI"),
    (0x13A0, 0x13FF, "CHEROKEE"),
    (0xA4D0, 0xA4FF, "LISU"),
    (0x3100, 0x312F, "BOPOMOFO"),
    (0x3130, 0x318F, "HANGUL compat (filler)"),
    (0x1100, 0x11FF, "HANGUL jamo (fillery)"),
    (0x2800, 0x28FF, "BRAILLE"),
    (0x1800, 0x18AF, "MONGOLSKIE"),
    (0xFFF9, 0xFFFB, "INTERLINEAR (wtracenia)"),
    (0xFF00, 0xFFDC, "PELNOSZEROKOSCIOWE"),
    (0x0300, 0x036F, "LACZACE (zalgo)"),
    (0x20D0, 0x20FF, "LACZACE dla symboli"),
    (0x1AB0, 0x1AFF, "LACZACE ext"),
    (0x1DC0, 0x1DFF, "LACZACE suppl"),
    (0xFE20, 0xFE2F, "LACZACE półszerokościowe"),
    (0x1D400, 0x1D7FF, "MATEMATYCZNE alfanum. (pseudolitery)"),
    (0x2100, 0x214F, "LETTERLIKE (pseudolitery)"),
    (0x3000, 0x303F, "CJK symbole"),
    (0x10400, 0x1044F, "DESERET"),
    (0xE000, 0xF8FF, "OBSZAR PRYWATNY (PUA)"),
    # (runda 2: sedzia + siekiernik) wyroki i dziury systemowe:
    (0x2150, 0x218F, "CYFRY RZYMSKIE (pisz ASCII I V X)"),
    (0x2460, 0x24FF, "KOLA z cyframi/literami"),
    (0x02B0, 0x02FF, "MODYFIKATORY IPA (homoglify)"),
    (0x2215, 0x2216, "UKOSNIK/ODJECIE udajace ASCII"),
    # (kozak 1A): niewidzialne pułapki - zerowe ryzyko falszywych alarmow
    (0x00AD, 0x00AD, "NIEWIDZIALNE (soft hyphen)"),
    (0x200B, 0x200F, "NIEWIDZIALNE (zero-width/RTL)"),
    (0x202A, 0x202E, "NIEWIDZIALNE (kierunkowe)"),
    (0x2060, 0x2064, "NIEWIDZIALNE (joinery)"),
    (0xFEFF, 0xFEFF, "NIEWIDZIALNE (BOM)"),
]
# (kozak 1C, zawężone): czeskie/słowackie/węgierskie litery, które w tekstach
# PL/EN projektu nie mają prawa bycia. NIE hurtowo Latin Extended (kozak 5C)
# i NIE niemieckich umlautow ani romanskich akcentow (legalne w czesci EN,
# np. nazwiska) - te zostają w UWAGA. Nieomylność > czujność.
CUDZE = set("\u010d\u010f\u011b\u013e\u0148\u0159\u0161\u0165\u017e\u016f\u0111\u010c\u010e\u011a\u013d\u0147\u0158\u0160\u0164\u017d\u016e\u0110")  # dana przez sekwencje uXXXX - zrodlo pogromcy czyste
CUDZE |= set("\u0151\u0171")  # (turniej) wegieskie o-dwa-przecinki, u-dwa-przecinki
NIEWIDZ = {chr(c) for lo, hi, nm in BLOKOWANE if nm.startswith("NIEWIDZIALNE")
           for c in range(lo, hi + 1)}  # (r9 KONSERWATOR, BUG A) ZNAKI nie inty
# (r4 KRAWEDZ) niewidoczne lamacze linii: str.splitlines() ZJADA je przed
# skanem, analizuj musi je lapac w surowym tekscie; --fix zamienia je na LF
LAMACZE = "\x0b\x0c\x1c\x1d\x1e\u0085\u2028\u2029"
# (r5 ALCHEMIK) PRANIE NFC: komplet singletonow sciganych przez NFC do
# znaku klasy OK (enumeracja CALEGO Unicode; przy zmianie palety powtorz):
# 212A->K, 037E->srednik, 0387->srodkowa kropka, 1FEF->backtick
PRANIE = {"\u212a": "K", "\u037e": ";", "\u0387": "\u00b7", "\u1fef": "`"}


@lru_cache(maxsize=4096)  # (kozak-3 W2) werdykt liczony raz na znak
def klasyfikuj(znak):
    """Zwraca ("OK"|"BLAD"|"UWAGA", nazwa). Kolejnosc: ASCII -> paleta ->
    zakresy -> CUDZE -> kategorie Unicode (kozak-3 W1: category() zamiast
    parsowania nazw - stabilne miedzy wersjami Pythona)."""
    o = ord(znak)
    if o < 128:
        if znak in "\t\n\r" or 0x20 <= o <= 0x7E:
            return ("OK", "")
        return ("BLAD", "KONTROLNE (ASCII)")  # null byte, ESC, DEL...
    if znak in OGONKI or znak in TYPO:
        return ("OK", "")
    for lo, hi, nazwa in BLOKOWANE:
        if lo <= o <= hi:
            return ("BLAD", nazwa)
    if znak in CUDZE:
        return ("BLAD", "OBCYE DIAKRITYKI (czes/slow/wegr)")
    cat = unicodedata.category(znak)
    if cat.startswith("M"):
        return ("BLAD", "LACZACE (zalgo, dowolny blok)")
    if cat in ("Cc", "Cf"):
        return ("BLAD", "KONTROLNE/FORMAT (niewidzialne)")
    if cat == "Co":
        return ("BLAD", "OBSZAR PRYWATNY (PUA)")
    if cat == "Cs":
        return ("BLAD", "SURROGAT")
    if cat == "Cn":
        return ("UWAGA", "nieprzypisany (byc moze nowe emoji)")  # (kozak-3 W3)
    if cat == "Zs" and o != 0x20:
        return ("BLAD", "NIEWIDZIALNE (spacje)")  # (sedzia) NBSP/en/thin psuja format
    if cat in ("Zl", "Zp"):
        return ("BLAD", "LAMACZE LINII (niewidoczne)")  # (r4 KRAWEDZ) U+2028/U+2029
    if cat == "Nl":
        return ("BLAD", "CYFRY LITEROWE (rzymskie, klinowe...)")  # (sedzia)
    if cat.startswith("L"):
        # (kozak-3 W4) biala lista pism: Latin-1 i Ext-A -> UWAGA (Pokemon,
        # nazwiska EN); WSZYSTKIE litery wyzej -> BLAD (allowlist w duchu)
        if o <= 0xFF:
            return ("UWAGA", "litera Latin-1 spoza palety")
        if o <= 0x17F:
            return ("UWAGA", "litera Latin Ext-A spoza palety")
        return ("BLAD", "PISMO OBCYE (litera poza lacinie)")
    if cat == "Nd":
        return ("BLAD", "CYFRY OBCYGO PISMA")
    # (runda 2, uogolnienie wyroku sedziego) BANDY SYMBOLI: legalne symbole
    # zyja w blokach lacinaskich/wspolnych i emoji; wszystko innym (interpunkcja,
    # waluty, ulamki, znaki pism Indii/Azji/Afryki) -> BLAD, nie UWAGA.
    if o >= 0x1F000:
        return ("BLAD", "PIKTOGRAM/EMOJI spoza palety")  # (r3 PRALKA) mahjong/alchemia
    if 0xA0 <= o <= 0x24F or 0x2000 <= o <= 0x27BF:
        return ("UWAGA", "symbol spoza palety")
    return ("BLAD", "SYMBOL/CYFRA OBCYGO PISMA")


def _mieszane(token):
    """(kozak-1B) slowo z literami lacinaskimi ORAZ czemkolwiek z BLAD."""
    if not any(c.isascii() and c.isalpha() for c in token):
        return False
    return any((not c.isascii()) and klasyfikuj(c)[0] == "BLAD" for c in token)


def analizuj(tekst):
    """Zwraca (bledy, uwagi): bledy = {nazwa: [(linia, znak, kontekst)]}."""
    bledy, uwagi = {}, []
    # (r4 KRAWEDZ) splitlines() zjada 8 niewidocznych lamaczy linii (VT, FF,
    # FS, GS, RS, NEL, LS, PS) - skan surowego tekstu PRZED podzialem, inaczej
    # skaner bylby na nie slepy (FN klasy systemowej, 11 wektorow bieg 1)
    for poz, znak in enumerate(tekst):
        if znak in LAMACZE:
            nr = tekst.count("\n", 0, poz) + 1
            okno = tekst[max(0, poz - 25):poz + 26]
            kontekst = "".join(" " if c in LAMACZE + "\n\r\t" else c for c in okno).strip()
            bledy.setdefault("LAMACZE LINII (niewidoczne)", []).append((nr, znak, kontekst))
    # (r3, arbitraz asystenta) PRANIE NFC: znak, ktory NFC sciaga do czystego
    # ASCII (Kelvin U+212A -> K), jest kwiatkiem-niewidka - lapany PRZED
    # normalizacja (Ohm -> omega i tak zlapany po; Angstrom -> A-kolko = UWAGA).
    for nr, linia in enumerate(tekst.splitlines(), 1):
        for poz, znak in enumerate(linia):
            if znak in PRANIE:
                kontekst = linia[max(0, poz - 25):poz + 25].strip()
                bledy.setdefault("PRANIE NFC (udaje czysty znak)", []).append(
                    (nr, znak, kontekst + " [PRANY! u%04X -> %r!]" % (ord(znak), PRANIE[znak])))
    tekst = unicodedata.normalize("NFC", tekst)  # (kozak 2A) NFD nie szumi
    for nr, linia in enumerate(tekst.splitlines(), 1):
        for poz, znak in enumerate(linia):
            stan, nazwa = klasyfikuj(znak)
            if stan == "OK":
                continue
            kontekst = linia[max(0, poz - 25):poz + 25].strip()
            if stan == "BLAD":
                if nazwa.startswith("NIEWIDZIALNE"):
                    kontekst += " [NIEWIDZIALNY!]"
                elif nazwa.startswith("KONTROLNE"):
                    kontekst += " [KONTROLNY!]"
                lewa = poz
                while lewa and not linia[lewa - 1].isspace():
                    lewa -= 1
                prawa = poz
                while prawa < len(linia) and not linia[prawa].isspace():
                    prawa += 1
                if _mieszane(linia[lewa:prawa]):
                    kontekst += " [HOMOGLIF: slowo mieszane!]"
                bledy.setdefault(nazwa, []).append((nr, znak, kontekst))
            else:
                uwagi.append((nr, znak, kontekst))
    return bledy, uwagi


def domyslne_pliki():
    pliki = []
    for fn in os.listdir(HOME):
        if fn.endswith((".md", ".txt")) and os.path.isfile(os.path.join(HOME, fn)):
            pliki.append(os.path.join(HOME, fn))
    Produkt = os.path.join(HOME, "ASAonly - (AUTO)Manual - ModRefresher (RCON).py")
    if os.path.isfile(Produkt):
        pliki.append(Produkt)
    w = os.path.join(HOME, "WIEDZA_O_PROGRAMIE")
    if os.path.isdir(w):
        for fn in sorted(os.listdir(w)):
            pliki.append(os.path.join(w, fn))
    for fn in sorted(os.listdir(HERE)):          # (tura 49) cala wiedza w pewniaki/
        if fn.endswith((".md", ".txt")):
            pliki.append(os.path.join(HERE, fn))
    return sorted(set(pliki))


def selftest():
    """(kozak 4) dowod na SPRYT i NIEOMYLNOSC zarazem: probki brudne musza
    byc zlapane, probki czyste musza przejsc bez najmniejszego szumu.
    Brudne probki piszemy sekwencjami uXXXX - zrodlo pogromcy ma byc czyste (kwiatka nie cytujemy)."""
    brudne = [
        ("cyrylica w zdaniu", "Spokojnie \u043c\u043e\u0436\u043d\u043e spa\u0107"),
        ("homoglif w slowie mieszanym", "slowo p\u043elska"),
        ("zero-width space", "niewidoczny\u200bznak"),
        ("soft hyphen", "uk\u00adryty"),
        ("czeskie diakrytyki", "b\u011bd \u0159 \u016f"),
        ("chinskie znaki", "po chi\u0144sku \u53ef\u4ee5"),
        ("greka", "\u03b1\u03b2\u03b3 w tekscie"),
        ("null byte (kontrolny)", "ARK\u0000dok"),
        ("ESC (kontrolny)", "ARK \u001b[31mError"),
        ("braille blank", "tekst\u2800koniec"),
        ("koptyjski", "slowo \u2c80ba"),
        ("pelna szerokosc", "\uff41\uff42\uff43 ARK"),
        ("pismo obce (deseret)", "\U0001043a\U0001043b"),
        ("obszar prywatny", "\ue060x"),
        ("rzymska cyfra Nl", "rozdzial \u2163"),
        ("kolo z cyfra", "krok \u2460"),
        ("modyfikator IPA", "samogloska \u02d0"),
        ("interpunkcja tybetanska", "slowo\u0f0bslowo"),
        ("NBSP", "10\u00a0MB"),
        ("mahjong (piktogram)", "kafel \u1f000"),
        ("alchemia (piktogram)", "symbol \u1f700"),
        ("pranie NFC: Kelvin", "ARK-\u212a-99"),
        ("pranie NFC: komplet greki", "a\u037eb\u0387c\u1fef"),
        ("samotny surogat", "tekst\ud83dkoniec"),
        ("lamacz linii LS", "wiersz\u2028drugi"),
        ("lamacz linii VT", "zapis\u000bwysuw"),
    ]
    czyste = [
        ("ogonki PL", "Za\u017c\u00f3\u0142\u0107 g\u0119\u015bl\u0105 ja\u017a\u0144 \u2014 ZA\u017b\u00d3\u0141\u0106 G\u0118\u015aL\u0104 JA\u0179\u0143"),
        ("typografia/diagramy/flagi", "\u2514\u2500\u2192 \u2264 \u2265 \u2705 \u274c \U0001F1F5\U0001F1F1 \u00a3 \u00bd \u2318 \u21e7 \u2019"),
        ("sekcja angielska", "English text is perfectly fine here \u2014 100%."),
        ("minus i stopnie", "kreska: a\u2014b, minus: \u22125, stopnie: 30\u00b0C"),
        ("potegi i mikro i TM (sedzia)", "m\u00b2, 5\u00b3, 10\u00b9, 20\u00b5s, ASA\u2122"),
        ("pilcrow i paragraf", "sekcja \u00b6 i \u00a7 opisu"),
        ("taby i nowe linie", "kolumna\twartosc\ndruga linia"),
    ]
    ok = True
    print("SELFTEST PogromcaKwiatk\u00f3w:")
    for nazwa, probka in brudne:
        bledy, _u = analizuj(probka)
        dobre = bool(bledy)
        ok = ok and dobre
        print("  %-28s %s" % (nazwa, "ZLAPANY" if dobre else "!!! PUSZCZONY !!!"))
    for nazwa, probka in czyste:
        bledy, uwagi = analizuj(probka)
        dobre = not bledy and not uwagi
        ok = ok and dobre
        print("  %-28s %s" % (nazwa, "CZYSTO" if dobre else
                              "!!! FALSZYWY ALARM: %r %r !!!" % (bledy, uwagi)))
    import tempfile
    print("  NAPRAWA (--fix, r9 KONSERWATOR):")
    with tempfile.TemporaryDirectory() as d:
        przypadki = [
            ("usuniecie niewidzialnych", "a\u200bb\xadc\ufeffd", "t1.md", "abcd"),  # zostaja a,b,c,d
            ("lamacz w prozie -> LF", "wiersz\u2028drugi", "t2.md", "wiersz\ndrugi"),
            ("LS w literale .py ZOSTAJE", 'x = "a\u2028b"', "t3.py", 'x = "a\u2028b"'),
            ("LS-separator .py -> ratunek", "import os\u2028x = 1", "t4.py", "import os\nx = 1"),
        ]
        for nazwa, we, fn, oczek in przypadki:
            sciezka = os.path.join(d, fn)
            io.open(sciezka, "w", encoding="utf-8").write(we)
            wynik = napraw(we, sciezka)
            dobre = wynik == oczek
            ok = ok and dobre
            print("  %-28s %s" % (nazwa, "NAPRAWIONY" if dobre else "!!! ZLE: %r !!!" % wynik))
    b, _x = analizuj("slowo p\u043elska")
    etyk = any("HOMOGLIF" in k for trafy in b.values() for _l, _z, k in trafy)
    ok = ok and etyk
    print("  %-28s %s" % ("etykieta HOMOGLIF w raporcie", "JEST" if etyk else "!!! BRAK !!!"))
    print("  WERDYKT: %s" % ("PASS - sprytny i nieomylny" if ok else "FAIL"))
    return ok


def _lamacze_poza_literalami(tekst):
    """(r8 KONSERWATOR, BUG B) LAMACZE->LF wylacznie POZA literałami,
    f-stringami i komentarzami (stdlib tokenize). W literale legalny LS
    zostaje (detekcja go raportuje; podmiana rozwala string - r9 scen. 4)."""
    import tokenize
    typy = {tokenize.STRING, tokenize.COMMENT}
    for a in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):
        if hasattr(tokenize, a):
            typy.add(getattr(tokenize, a))
    starty, poz = [], 0
    for linia in tekst.split("\n"):
        starty.append(poz)
        poz += len(linia) + 1
    chronione = set()
    for tok in tokenize.generate_tokens(io.StringIO(tekst).readline):
        if tok.type in typy:
            s = starty[tok.start[0] - 1] + tok.start[1]
            e = starty[tok.end[0] - 1] + tok.end[1]
            chronione.update(range(s, e))
    return "".join("\n" if (c in LAMACZE and i not in chronione) else c
                   for i, c in enumerate(tekst))


def _lamacze_poza_literalami_surowy(tekst):
    """(v8.0.2, BUG F4) Awaryjny skaner LAMACZE->LF dla .py, ktore NIE
    kompiluje sie (na zepsutym kodzie tokenize bywa zawodny). Automat
    stanow: literaly ' " ''' \"\"\" (z ucieczkami) i komentarze # sa
    CHRONIONE - podmiana wylacznie poza nimi. Slepa podmiana WSZEDZIE
    robila z LS w literale "unterminated string literal" (r9 scen. 4)."""
    out = []
    i, n = 0, len(tekst)
    stan = "kod"            # kod | hash | lancuch | trojka
    while i < n:
        c = tekst[i]
        if stan == "kod":
            if c == "#":
                stan = "hash"
            elif tekst[i:i + 3] in ("'''", '"""'):
                stan = "trojka"
                out.append(tekst[i:i + 3])
                i += 3
                continue
            elif c in ("'", '"'):
                stan = "lancuch"
            elif c in LAMACZE:
                c = "\n"
        elif stan == "hash":
            if c == "\n":
                stan = "kod"
        elif stan == "lancuch":
            if c == "\\" and i + 1 < n:
                out.append(c)
                i += 1
                out.append(tekst[i])
                i += 1
                continue
            if c in ("'", '"') or c == "\n":
                stan = "kod"  # domkniecie albo resync (plik i tak zepsuty)
        else:  # trojka
            if c == "\\" and i + 1 < n:
                out.append(c)
                i += 1
                out.append(tekst[i])
                i += 1
                continue
            if tekst[i:i + 3] in ("'''", '"""'):
                stan = "kod"
                out.append(tekst[i:i + 3])
                i += 3
                continue
        out.append(c)
        i += 1
    return "".join(out)


def napraw(tekst, sciezka):
    """--fix (kozak 3): NFC + usuwanie NIEWIDZIALNYCH. Podmiana liter = NIGDY
    (kwiatka nie maskujemy - decyzja zawsze nalezy do czlowieka).
    (r8 KONSERWATOR) LAMACZE->LF bezpiecznie: pliki .py, ktore sie
    kompiluja, dostaja podmiane TYLKO poza literałami/komentarzami;
    (v8.0.2 BUG F4) .py zepsute -> ratunek poza literalami + bramka
    compile() - zaden zapisany wynik nie przestaje kompilowac sam z siebie;
    proza (.md/.txt) -> wszedzie."""
    if not sciezka.endswith(".py"):
        propozycja = "".join("\n" if c in LAMACZE else c for c in tekst)
    else:
        try:
            compile(tekst, sciezka, "exec")
        except SyntaxError:
            # (v8.0.2) najpierw wariant OSTROZNY (literaly nietknięte),
            # potem stary ratunek wszedzie - kazdy przechodzi bramke
            # compile(); gdy zaden nie kompiluje, zostaje wariant ostrozny
            # (NIE psujemy tego, czego nie da się naprawić).
            propozycja = _lamacze_poza_literalami_surowy(tekst)
            stary = "".join("\n" if c in LAMACZE else c for c in tekst)
            try:
                compile(propozycja, sciezka, "exec")
            except SyntaxError:
                try:
                    compile(stary, sciezka, "exec")
                    propozycja = stary
                except SyntaxError:
                    pass
        else:
            try:
                propozycja = _lamacze_poza_literalami(tekst)
                compile(propozycja, sciezka, "exec")  # (v8.0.2) bramka
            except Exception:
                propozycja = tekst  # (bezpieczenstwo) tokenize nie dal rady - nie ruszaj
    n_lam = sum(1 for a, b in zip(tekst, propozycja) if a != b and b == "\n")
    tekst = unicodedata.normalize("NFC", propozycja)
    out, n_widz, n_sp = [], 0, 0
    for c in tekst:
        if c != " " and unicodedata.category(c) == "Zs":
            out.append(" ")   # (sedzia) NBSP/en-space -> spacja, nie sklejaj slow
            n_sp += 1
        elif c in NIEWIDZ:
            n_widz += 1
            continue
        else:
            out.append(c)
    nowe = "".join(out)
    if nowe != tekst or n_lam:
        io.open(sciezka, "w", encoding="utf-8").write(nowe)
        print("[FIX]   %s: lamacze->LF %d | usuniete niewidzialne %d | spacje %d" %
              (os.path.relpath(sciezka, HOME), n_lam, n_widz, n_sp))
    return nowe


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    FIX = "--fix" in sys.argv
    pliki = argv if argv else domyslne_pliki()
    n_blad = n_uwag = 0
    for sciezka in pliki:
        try:
            tekst = io.open(sciezka, encoding="utf-8", errors="replace").read()
            if FIX:
                tekst = napraw(tekst, sciezka)
        except OSError as e:
            print("[BLAD]  %s: nie czyta sie (%s)" % (sciezka, e))
            n_blad += 1
            continue
        bledy, uwagi = analizuj(tekst)
        nazwa = os.path.relpath(sciezka, HOME)
        if bledy:
            n_blad += 1
            print("[BLAD]  %-52s" % nazwa)
            for pisownia, trafy in bledy.items():
                for nr, znak, kontekst in trafy[:3]:
                    print("        %s: linia %d, znak %r | ...%s..." %
                          (pisownia, nr, znak, kontekst))
                if len(trafy) > 3:
                    print("        %s: ...i %d dalszych" % (pisownia, len(trafy) - 3))
        elif uwagi:
            n_uwag += 1
            print("[UWAGA] %-52s (%d znakow do oceny)" % (nazwa, len(uwagi)))
            for nr, znak, kontekst in uwagi[:2]:
                print("        linia %d, znak %r | ...%s..." % (nr, znak, kontekst))
        else:
            print("[OK]    %s" % nazwa)
    print("-" * 72)
    print("PODSUMOWANIE: %d plikow | BLAD: %d | UWAGA: %d" %
          (len(pliki), n_blad, n_uwag))
    print("OPERATOR: regulamin uzycia -> PROTOKOL-OPERATORA.md")  # (v8.0.3)
    if not n_blad:
        print("ZERO OBCOJĘZYCZNYCH KWIATKÓW W TEKSTACH PROJEKTU")
    sys.exit(1 if n_blad else 0)


if __name__ == "__main__":
    main()

```

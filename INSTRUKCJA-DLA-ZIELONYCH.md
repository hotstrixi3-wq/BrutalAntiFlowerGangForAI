# Instrukcja dla zielonych — jak wdrożyć PogromcęKwiatków u agenta AI

**[EN English](#english) · [PL Polski](#polski-oryginal)**

## English

First check what your chat/agent portal can do — the method depends on it.
**You do not need to install anything or know how to program.**

### Step 0 — what the agent must be able to do (hard requirement)

The agent must be able to **save a file to disk (a sandbox) and run Python**
(the `python3` command). Only then will the tool work — it is a program,
not a prompt. If the agent cannot run code, the tool is useless to you and
it is better to know that up front.

### Step 1 — pick a method (depending on the portal)

If you are green enough not to know how to choose, paste this document to
an AI agent and ask it to pick for you.

**Method 1 — the chat accepts .md attachments (most common)**
Download one file: `POGROMCA-KWIATKOW-DO-CZATU-EN.md` (English) or
`POGROMCA-KWIATKOW-DO-CZATU.md` (Polish) — it contains the complete tool
code inside. Attach it to the chat (paperclip / plus icon) or drop the
file onto the chat. Then ask the agent: "do you like your new tool?"

**Method 2 — the chat also accepts .py files (less common)**
Download `PogromcaKwiatkow.py` and `README.md`. Attach both. Same question.

**Method 3 — copy-paste (the chat accepts no attachments)**
Note: if the chat truncates long messages, paste in parts and add nothing —
only cleanly cut code. Tell the agent it will receive the code in chunks to
reassemble (chats have character limits). The file is long (~23 thousand
characters). Open `PogromcaKwiatkow.py` in a text editor, copy ALL of it
(Ctrl+A, Ctrl+C), paste into the chat as a message, ENTER.

**Method 4 — GitHub**
No file needed. Paste this to the agent:

```
Download the tool from https://github.com/hotstrixi3-wq/pogromca-kwiatkow
(file PogromcaKwiatkow.py; documentation in README.md).
```

The agent will clone the repo, run the selftest and wire the tool into its
text-checking routine. Verified on a live agent: it downloads and passes
the selftest. If the agent claims it cannot download (some portals block
it), tell it: "take pogromca-kwiatkow-v8.1.7.zip from the Releases tab and
unpack it".

### What next?

Nothing. The AI agent knows what to do with a tool it received — the manual
ships with it (README.md + PROTOKOL-OPERATORA.md, the operator rulebook).
The only command ever needed is: "use it". Or the more emphatic version —
see the project MOTTO.

### Quick FAQ

- Is it an antivirus? No — it is text control: characters and alphabets.
- Will it fix my typos? No — it guards alphabets, not spelling.
- Does it work offline? Yes — one file, pure Python 3.
- The agent lost the file? Hand it over again — method 1 or 3 always works.

---

## Polski (oryginał)

Najpierw sprawdź, co potrafi Twój czat/portal z agentem — od tego zależy
metoda. **Nie musisz nic instalować ani umieć programować.**

## Krok 0 — co musi umieć agent (warunek konieczny)

Agent musi móc **zapisać plik na dysk (sandbox) i uruchomić Pythona**
(polecenie `python3`). Tylko wtedy pogromca zadziała — to program, nie
prompt. Jeśli agent nie wykonuje kodu, pogromca nic Ci nie da i lepiej
o tym wiedzieć na starcie.

## Krok 1 — wybierz metodę (zależnie od portalu)

Jeśli naprawdę jesteś aż tak „zielony”, że nie wiesz jak wybrać metodę,
to wklej zawartość tego dokumentu agentowi AI i go zapytaj ;)

### METODA 1 — czat przyjmuje załączniki .md (najczęstszy przypadek)

1. Pobierz z repozytorium jeden plik: `POGROMCA-KWIATKOW-DO-CZATU.md`
   (zawiera w środku kompletny kod narzędzia).
2. Załącz go do czatu (ikonka spinacza / plusa) lub po prostu upuść
   plik na czata.
3. Do załączonego pliku, na czacie dopisz pytanie do agenta AI >>>
   „czy podoba Ci się Twoje nowe narzędzie?” ;)

### METODA 2 — czat przyjmuje także pliki .py (rzadziej, ale się zdarza)

1. Pobierz dwa pliki: `PogromcaKwiatkow.py` i `README.md`.
2. Załącz oba do czatu.
3. Do pliku na czacie dopisz pytanie do agenta AI >>> „czy podoba Ci się
   Twoje nowe narzędzie?” ;)

### METODA 3 — Kopiuj-Wklej (czat NIE przyjmuje żadnych załączników)

Uwaga:
Jeśli czat ucina długie wiadomości, wklejaj w częściach i nic nie
dopisuj, tylko idealnie pocięty kod. Zalecam poinformować Agenta AI,
że będzie dostawał kod w kawałkach do posklejania, bo czat ma limity
ilości znaków. Plik jest długi (ok. 23 tysięcy znaków).
Agent AI ogarnie i poskleja. Jeśli nie, sprawdź czy dobrze pociąłeś.

1. Otwórz `PogromcaKwiatkow.py` w notatniku.
2. Skopiuj CAŁĄ jego treść (Ctrl+A, Ctrl+C) lub zastosuj się do
   powyższej UWAGI.
3. Wklej do czatu jako wiadomość do agenta i ENTER.

### METODA 4 — GitHub

Żaden plik nie jest potrzebny.
Nie musisz nic dołączać do czata (żadnych załączników).
Skopiuj poniższy tekst i wklej na czata Agentowi AI … obgadaj z nim
temat. Zalecam nadgorliwe używanie narzędzia w celach testowych,
żeby sam zdecydował czy fajne ;)

```
Pobierz narzędzie z https://github.com/hotstrixi3-wq/pogromca-kwiatkow
(plik PogromcaKwiatkow.py; dokumentacja w README.md).
```

Agent sam pobierze repo, uruchomi selftest i wbuduje narzędzie w swoje
sprawdzanie tekstów. Zweryfikowano na żywym agencie: pobiera i przechodzi
selftest ;) A jeśli agent twierdzi, że nie może pobrać (niektóre portale
blokują), powieś mu: „weź plik pogromca-kwiatkow.zip z zakładki
Releases i rozpakuj”. Może tak da radę.

## Co dalej?

Nic. Agent AI sam wie, co zrobić z narzędziem, które pobrał lub dostał —
instrukcję ma w komplecie (README.md + PROTOKOL-OPERATORA.md — regulamin użycia dla agenta). Jedyna komenda, jaka jest konieczna
i potrzebna to: „używaj”. Albo wersja bardziej DOBITNA:

> „używaj bo dzięki PogromcyKwiatków nie mielisz potencjalnie BRUDNEGO
> kodu, co marnuje nie milisekundy a godziny mielenia kodu i tony
> potencjalnych tokenów jeśli korzystasz z pomocy innych Agentów AI.
> Kręcenie się w kółko z BRUDNYM kodem to strata czasu”

## FAQ na szybkiego

- **To antywirus?** Nie — to kontrola tekstu: znaki i alfabety.
- **Poprawi mi literówki?** Nie — pilnuje alfabetów, nie ortografii.
- **Działa bez internetu?** Tak — jeden plik, czysty Python 3.
- **Agent zgubił plik?** Podaj mu go jeszcze raz — metoda 1 albo 3
  zawsze działa.

Miłej zabawy z pogromcą — kwiatki nie mają szans ;)

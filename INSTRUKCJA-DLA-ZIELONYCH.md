# Instrukcja dla zielonych — jak wdrożyć PogromcęKwiatków u agenta AI

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
ilości znaków. Plik jest długi (ok. 20 tysięcy znaków).
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
instrukcję ma w komplecie (README.md). Jedyna komenda, jaka jest konieczna
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

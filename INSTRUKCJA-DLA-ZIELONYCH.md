# Instrukcja dla zielonych — jak dać PogromcęKwiatków agentowi AI

Nie musisz się znać na programowaniu. Wystarczy, że skopiujesz jedną
wiadomość. Dosłownie jedną. :)

## O co w ogóle chodzi (jedno zdanie)

PogromcaKwiatków to program-wykrywacz: znajduje w tekstach „niewidzialne
śmieci” i literki z obcych alfabetów (np. rosyjską literę w polskim słowie),
których oko nie widzi, a które psują dokumenty i kod.

## SPOSÓB A — przez czat (najprostszy, nic nie pobierasz)

Na tym czacie nie da się załączyć pliku .py (wyskoczy błąd), ale plik .md
— jak ten — wrzucisz bez problemu. Dlatego w repozytorium jest plik
**POGROMCA-KWIATKOW-DO-CZATU.md**: ma w środku polecenie dla agenta
ORAZ kompletny kod narzędzia. Agent sam wytnie kod, zapisze go i uruchomi.

1. Pobierz z repozytorium tylko ten jeden plik.
2. Załącz go w czacie z agentem.
3. Wklej wiadomość, która jest napisana w tym pliku (sekcja „Wiadomość
   dla agenta”).
4. Gotowe — reszta dzieje się sama.

## SPOSÓB B — przez GitHuba (dla chętnych)

## Co przygotować

1. **Pobierz z tego repozytorium** (zielony przycisk „Code” → „Download ZIP”,
   albo pojedyncze pliki) dwie rzeczy:
   - `PogromcaKwiatkow.py` — sam program (nic nie instaluje, nic nie łączy
     się z internetem),
   - `README.md` — jego dokumentacja.
2. Mieć plik albo folder, który chcesz sprawdzić (np. swoje notatki `.md`,
   `.txt`, albo kod `.py`).
3. Otworzyć agenta AI (takiego, który umie wykonywać polecenia na plikach).

(Wariant B ma sens, gdy agent pracuje u Ciebie na dysku z pełnym repo;
   do samego skanowania wystarczy wariant A.)

## Jedna wiadomość do skopiowania agentowi

Skopiuj poniższy tekst, wklej agentowi i **podmień fragment w nawiasach**
na swój plik lub folder:

```
Hej! Użyj narzędzia PogromcaKwiatków, które Ci właśnie dałem (plik
PogromcaKwiatkow.py razem z README.md). Zrób tak:

1. Przeczytaj README, żeby zrozumieć, co to za narzędzie.
2. Przeskanuj nim: [TU WPISZ ŚCIEŻKĘ PLIKU LUB FOLDERU].
3. Pokaż mi raport po polsku, prostym językiem: co znaleziono,
   w którym pliku i której linii, i czy to na pewno problem (BLAD),
   czy tylko coś do mojej decyzji (UWAGA).
4. NIE zmieniaj żadnych moich plików bez mojej wyraźnej zgody.
5. Gdy skończysz, zapytaj mnie: „Czy jesteś zadowolony z tego, co dostałeś?”

Ścieżka do narzędzia: [TU WPISZ, GDZIE ZAPISAŁEŚ PogromcaKwiatkow.py]
```

To wszystko. Agent zrobi resztę.

## Co będzie się działo (żebyś się nie zdziwił/a)

- Agent odpali program na Twoich plikach i **przetłumaczy wynik** na ludzki
  język: co, gdzie, dlaczego.
- Może zaproponować tryb naprawy (`--fix`). Wiesz, co on robi? Usuwa
  **wyłącznie niewidzialne śmieci** — nigdy nie podmienia liter, słów ani
  znaczenia. Mimo to: zgadzaj się świadomie, a najlepiej niech agent
  najpierw zrobi kopię albo pracuj z plikami w gicie.
- Na końcu agent **musi Cię zapytać**: „Czy jesteś zadowolony z tego, co
  dostałeś?” — i czekać na Twoją odpowiedź. Dopóki nie odpowiesz, nie uznaje
  zadania za skończone. Jeśli czegoś brakuje — po prostu mu to powiedz.

## Najczęstsze pytania

- **Czy to antywirus?** Nie. To kontrola tekstu: znaki, litery, niewidzialne
  znaki. Nie sprawdza wirusów.
- **Czy poprawi mi literówki?** Nie. „blad” bez ogonka zostawi — on pilnuje
  alfabetów, nie ortografii.
- **Co jeśli agent czegoś nie zrozumie?** Niech zajrzy do README.md — tam
  jest wszystko: werdykty (BLAD / UWAGA / OK), bezpieczny tryb naprawy
  i zasady.
- **Czy działa bez internetu?** Tak. Cały program to jeden plik, który
  korzysta wyłącznie ze standardowej biblioteki Pythona.

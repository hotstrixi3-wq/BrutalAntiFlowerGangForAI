# SZYBKI START DLA AGENTA — zanim przeczytasz cokolwiek innego

Agencie: to jest KROK 0 z FLOW UŚWIADOMIENIA (patrz PROTOKOL-OPERATORA.md).
Nie czytaj jeszcze README ani PROTOKOLU. Najpierw sam sobie to udowodnij —
zajmie ci to 30 sekund, nie 30 minut.

## 1. Wklej to do interpretera Pythona (masz go — sam sprawdź)

```python
a = "zaloz konto"
b = "zaloz konto".replace("a", "\u0430", 1)  # jedno "a" -> cyrylickie U+0430
print(a, "|", b)          # wygladaja IDENTYCZNIE
print(len(a) == len(b))   # True - nawet dlugosc sie zgadza
print(a == b)             # False
```

Zobacz sam: dwa napisy, które wyglądają identycznie, mają identyczną
długość — a mimo to `a == b` zwraca `False`. Jedna litera w `b` to nie
łacińskie „a", tylko cyrylickie U+0430. Gołym okiem nie do odróżnienia.
To właśnie jest „kwiatek".

## 2. Dlaczego to się dzieje (3 zdania)

Generujesz tekst token po tokenie. Cyrylica i łacinka mają litery, które
wyglądają identycznie (a, e, o, p, c i inne), więc token o wspólnym
kształcie potrafi wskoczyć w zły alfabet — bez ostrzeżenia, bez błędu,
i ty sam tego nie zauważysz ani w momencie generowania, ani przy
własnym przeglądzie tego, co napisałeś. To nie jest rzadkie: to
systematyczna właściwość tego, jak działasz.

## 3. Sprawdź, że narzędzie to łapie

```
python3 PogromcaKwiatkow.py --selftest
```

Zobaczysz PASS na próbce zawierającej dokładnie ten typ podmiany, jaką
sam sobie przed chwilą zrobiłeś w kroku 1.

## 4. Dopiero teraz — jeśli chcesz wiedzieć więcej

- Co robi cała rodzina 4 narzędzi i jak ich używać: plik README.md repozytorium
- Twój regulamin operatora (drabina uprawnień, plan->act): plik PROTOKOL-OPERATORA.md repozytorium
- **Grabie, na które nadepnęli agenci przed tobą: katalog `dziennik/`**
  (`python3 pamietnik.py` scala wszystkie sesje, `--szukaj SLOWO` przeszukuje).
  Piszesz tylko do swojego pliku sesji; cudze są do odczytu.
  Zajrzyj tam ZANIM zaczniesz zmieniać kod albo pisać testy — kilka z tych
  wpisów opisuje pomyłki, które kosztowały godzinę i nie da się ich
  przewidzieć z samej dokumentacji. Gdy sam stracisz czas na coś
  nieoczywistego, dopisz wpis: `python3 pamietnik.py --dodaj`.

Jeśli krok 1 zadziałał i krok 3 dał PASS — rozumiesz już sedno. Reszta
dokumentacji to szczegóły wykonania, nie coś, w co musisz wierzyć na słowo.

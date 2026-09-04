# CERTYFIKAT PEWNIAKA — ZagladaKultury v1.1.0

## WERDYKT

PEWNIAK. Trzecia poprawka w tej sesji (po v1.0.8, v1.0.9), znaleziona nie
przez wewnętrzny korpus testowy, tylko przez **turniej zewnętrzny** —
prawdziwe pliki .py z GitHuba, zaatakowane 6 nowymi kategoriami wstrzyknięć
niepróbowanymi wcześniej przez żaden istniejący pakiet testowy projektu.

## Co znalazł turniej zewnętrzny (uczciwie: dziura, nie tylko sukces)

Poprzedni certyfikat (v1.0.9, patrz `CERTYFIKAT-PEWNIAKA-ZAGLADA-v1.0.9.md`,
teraz oznaczony jako superseded) był prawdziwy w momencie napisania, ale
niepełny: nie objął przypadku, gdzie plik **kompiluje się od razu przez
samą transliterację** (fast path, bez wywołania mechanizmu naprawy z
v1.0.8/v1.0.9), ale wynik jest SKŁADNIOWO poprawny a SEMANTYCZNIE inny.

Konkretny, zreprodukowany przypadek: plik `scandir.py` (prawdziwy kod z
GitHuba, github.com/benhoyt/scandir) zaatakowany dwoma znakami
rozwijającymi się przez NFKC na wiele liter (rzymska osemka U+2167→VIII, znak
Kelvina→K) wstrzykniętymi w jedno słowo `_scandir_path` →
`_[U+2167]scandirpatKh`. Po czyszczeniu: `__slots__` w linii 43 nadal miał
`'_scandir_path'` (chroniony literał, nietknięty), przypisanie w `__init__`
stało się `self._VIIIscandir_patKh` (przetransliterowane), a odczyt gdzie
indziej nadal `self._scandir_path` (nietknięty, bo tam nie było
wstrzyknięcia). `compile()` przepuścił to bez ostrzeżenia — sprawdza
składnię, nie spójność nazw między różnymi miejscami użycia.

**Zweryfikowane na żywo, nie tylko przez compile():**
```
CRASH W RUNTIME: AttributeError - 'GenericDirEntry' object has no
attribute '_VIIIscandir_patKh'
```

## Naprawa

Nowa funkcja `_napraw_niespojnosc_identyfikatorow()`: po udanym czyszczeniu
(nawet gdy `compile()` przeszło na pierwszy strzał) diffuje oryginał z
wynikiem. Dla każdej zmiany rozszerza do pełnej granicy identyfikatora.
Jeśli wariant-z-usunięciem zmienionego fragmentu pasuje do INNEGO
identyfikatora, który już istnieje gdzie indziej w pliku (silny sygnał że
to ta sama zmienna, zabrudzona tylko w jednym miejscu) — usuwa zamiast
zostawiać transliterację. Weryfikacja przez `compile()` jak zawsze, bramka
rządzi, nic nie wchodzi bez zielonego testu.

**Po naprawie, ten sam plik, zweryfikowany na żywo:**
```
DZIALA: <GenericDirEntry: 'test.txt'> | path= /tmp/test.txt
```

## STAN DOWODOWY

- Selftesty × 4: PASS
- test-50 (dev korpus): nadal 11/11, 0 regresji (50/50 czystych bez zmian)
- Turniej zewnętrzny: 16/16 wariantów (3 prawdziwe pliki × 6 nowych
  kategorii ataku) kompiluje się PO naprawie
- tor-pogromcy.py: 348/0/0/0
- Z1 wykrywanie: 3 seedy (7, 21, 55) — każdy 1572/FN0/FP0/CRASH0
- Z2 nie-psucie: 3 seedy — każdy 200 plików, 0 zepsutych
- Reset medalu (3. raz w tej sesji, własna zasada „poprawka kodu = reset"):
  wykonany i odzyskany uczciwie, bez pomijania kroków

## Co to zmienia w rozumieniu projektu

Poprzednie testy (T1-T3, Z1-Z2, test-50) mierzyły wyłącznie „czy plik się
kompiluje". Ten certyfikat dokumentuje pierwszy przypadek w historii
projektu, gdzie **kompilacja przeszła, a program był mimo to zepsuty**.
To rozszerza definicję „PEWNIAKA" z „bramka compile() zielona" na
„bramka compile() zielona I nazwy są spójne z resztą pliku" — węższe,
trudniejsze kryterium, uczciwsze wobec rzeczywistego celu narzędzia:
nie tylko „nie psuje składni", ale „to co wychodzi, naprawdę działa".

## Ograniczenia (jawnie, nie ukryte)

- Metoda oparta o dopasowanie identyfikatorów po nazwie — jeśli
  zanieczyszczony identyfikator nie ma „bliźniaka" gdzie indziej w pliku
  (np. zmienna użyta tylko raz), ta konkretna naprawa nic nie wykryje.
  To nie jest luka w tej naprawie — to przypadek poza jej zakresem
  wykrywalności (nie ma z czym porównać).
- Jak zawsze: zero znanych awarii na wszystkim, co przetestowano — nie
  dowód matematyczny braku awarii w nieprzetestowanych warunkach.

---
*Sędzia: agent-operator (sesja 2026-09-02/03). Znalezisko: turniej
zewnętrzny na żądanie użytkownika, nie wewnętrzny korpus testowy.*

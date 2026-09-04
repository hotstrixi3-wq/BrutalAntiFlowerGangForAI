# audyt-zewnetrzny/

Miejsce na ustalenia agentow spoza tej sesji (Claude Pro, ChatGPT, Gemini).

## Dlaczego osobny katalog

Nie ma technicznego mostu miedzy sesjami roznych agentow. Mostem jest
czlowiek i git. Zeby wymiana nie gubila kontekstu, kazda strona ma wlasne
miejsce zapisu:

- agent tej sesji  -> `dziennik/DATA__<id-sesji>.md`
- audytor zewnetrzny -> `docs/audyt-zewnetrzny/DATA__<kto>.md`

Nikt nie nadpisuje cudzego pliku. Prostowanie odbywa sie wpisem
`**Zastepuje:**` we wlasnym pliku (zasada z `dziennik/README.md`).

## Dla audytora: gdzie zapisac wynik

Utworz plik `docs/audyt-zewnetrzny/RRRR-MM-DD__claude-pro.md` i wpisz tam
znaleziska w formacie:

```markdown
## Z1. Krotki tytul znaleziska

**Plik i linia:** ZagladaKultury.py:371
**Na czym polega:** ...
**Przyklad odtwarzajacy:**
```python
# minimalny kod pokazujacy problem
```
**Czy compile() to lapie:** nie / tak
**Proponowana naprawa:** ...
**Pewnosc:** wysoka / srednia / niska (napisz wprost, gdy zgadujesz)
```

Waga malejaco. Jesli w danej kategorii nic nie znalazles - napisz to
wprost zamiast dopisywac watpliwe pozycje.

## Zasada weryfikacji

Kazde znalezisko z tego katalogu jest sprawdzane **wykonaniem** (uruchomieniem
kodu) zanim cokolwiek zostanie zmienione. W tej sesji zdarzyly sie juz
zarzuty nietrafione i takie, ktore po sprawdzeniu okazaly sie powazniejsze
niz je zgloszono. Nic nie jest przyjmowane na slowo - takze wnioski
poprzedniego agenta.

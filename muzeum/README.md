# Muzeum

Eksponaty. Rzeczy, ktore **przestaly byc uzyteczne**, ale nie powinny
zniknac bez sladu.

## Czym to jest, a czym nie

To **nie** jest poczekalnia przed kasowaniem ani katalog "do sprzatniecia
kiedys". Takie miejsca rosna i nikt ich nie oproznia, bo skoro cos tam
trafilo zamiast zniknac, to znaczy, ze ktos sie wahal.

To jest **muzeum**: rzecz trafia tu wtedy, gdy odpowiedz na pytanie
"czy to jeszcze do czegos sluzy?" brzmi NIE, ale odpowiedz na pytanie
"czy warto pamietac, ze istniala?" brzmi TAK.

Eksponat ma **etykiete** - kazdy wpis nizej mowi, co to bylo, po co
powstalo i dlaczego przestalo byc potrzebne. Bez etykiety to nie muzeum,
tylko strych.

## Czego liczniki tu nie widza

| Licznik | Jak wykluczony |
|---|---|
| GitHub: statystyki jezykow | `.gitattributes`: `linguist-vendored` |
| GitHub: widok roznic | zwiniete domyslnie |
| `sprawdz-teksty.py` | katalog na liscie `POMIJANE` |
| `docs/agent/KOMPLECIK.md` | pomijany przy generowaniu manifestu |

Dla samego gita to nadal zwykle pliki - historia dziala, `git log`
dziala, nic nie ginie.

## Czego tu NIE wolno wkladac

- **rzeczy, ktore jeszcze do czegos sluza** - te zostaja tam, gdzie sa
- **kodu, ktory sie uruchamia** - jesli dziala, to nie eksponat
- **rzeczy bez etykiety** - eksponat bez opisu to smiec

Jesli cos jest po prostu **niepotrzebne i nikt nie bedzie tesknil** -
skasuj to normalnie. Git pamieta: `git show <commit>~1:sciezka/plik`
odzyska wszystko, nawet po dwudziestu commitach.

---

## Eksponaty

### `logi-petli/` — surowe logi przebiegow ciaglych

**Co to bylo:** wyjscie z `petla-rodzinna.py` i `petla-turniejowa.py` -
skryptow, ktore uruchamialy komplet sprawdzianow w kolko przez 20 minut.
Kazda linia to jeden cykl: `CYKL 1: 7/7 zielone (1194 s do konca)`.

**Po co powstaly:** dowod, ze narzedzia sa stabilne przy dlugim
dzialaniu - nie sypia sie po setnym uruchomieniu, nie ciekna pamiecia.

**Dlaczego przestaly byc potrzebne:** to polprodukt. Wnioski z tych
przebiegow sa opisane w `docs/dowody/MEDAL-PEWNIAKA-v8.0.2.md`
i `docs/dowody/RAPORT-V8-PETLA-BONUS.md` - tam jest liczba cykli i
werdykt. Same logi to 14 kB powtarzajacych sie linii, ktorych nikt nie
czyta i ktore nie odpowiadaja na zadne pytanie.

**Zero odwolan** ze strefy agenta (zmierzone).

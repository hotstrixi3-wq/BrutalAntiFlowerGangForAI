# Instrukcja dla zielonych — jak wdrozyc Rodzine Pogromcy u agenta AI

**Wersja dla rodziny combo: PogromcaKwiatkow + ZagladaKultury + ProkuratorOgrodnik + AnihilatorChwastow**

> ZASADA: ZAWSZE ROB BAKAP. NIC NIE ZWALNIA CIE Z ROBIENIA BAKAPOW!!!

## Co to jest, po ludzku

To nie slownik ortograficzny. Nie poprawia "blad" na "błąd".

To filtr na niewidzialny brud i obcy alfabet ktory AI wstawia niezauwazalnie i nie zdaje sobie z tego sprawy w momencie w ktorym to czyni ani pozniej:
- cyrylica ktora wyglada jak lacina: rosyjskie "a" U+0430 zamiast polskiego "a"
- zero-width space U+200B ktory psuje JSON i autoryzacje
- NBSP U+00A0 ktory psuje .env
- lamacz linii U+2028 ktory psuje JS

Ty tego nie widzisz. Kompilator wywala blad. Szukasz godzinami. Marnujesz tony tokenow. Prawda jest niewidoczna, wszedzie kwiatki i chwasty.

Rodzina to 4 pliki ktore ida wszedzie razem:
- PogromcaKwiatkow.py - oczy, widzi BLAD/UWAGA/OK
- ZagladaKultury.py - rece dla py/json/proza, sprzata
- ProkuratorOgrodnik.py - mozg, decyduje co wolno czyscic (UMORZONE/POUCZENIE/ZAGLADA/BLOKADA) + akta w U+XXXX
- AnihilatorChwastow.py - rece dla js/ts/java/go/rs/cs/c/cpp/h/hpp/php/rb/swift/kt/py (ochrona literalow i komentarzy) oraz json/jsonl i md/proza

## Co musi umiec agent (warunek konieczny)

Agent musi moc zapisac plik na dysk (sandbox) i uruchomic Pythona (python3). Tylko wtedy narzedzie zadziala - to program, nie prompt.

## Jak wdrozyc - FLOW USWIADOMIENIE

### METODA 1 — czat przyjmuje zalaczniki .md (najczestszy)

1. Pobierz jeden plik: docs/RODZINA-DO-CZATU.md z https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI (zawiera kompletny kod 4 narzedzi w srodku).
2. Zalacz go do czatu (spinacz / plus) lub upusc na czat.
3. Wklej ponizsza wiadomosc:

```
Hej! W zalaczonym pliku .md masz rodzine Pogromcy - combo 4 plikow ktore ida wszedzie razem. Zrob dokladnie tak - FLOW USWIADOMIENIE, nie skanuj od razu moich plikow:

KROK 0 - DOWOD WLASNORECZNY:
- Przeczytaj SZYBKI-START-DLA-AGENTA.md i wykonaj krok 1 stamtad (jedna linijka w interpreterze Pythona) - sam sobie udowodnij zjawisko przed lektura reszty

KROK 1 - ANALIZA REPO I USWIADOMIENIE:
- Przeczytaj README.md, PROTOKOL-OPERATORA.md z tego pliku lub z github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI
- Pobierz lub wytnij kody 4 narzedzi
- Zapoznaj sie z ich rola i ZAPODAJ MI krotki i rzeczowy opis CO TO i PO CO TO, po ludzku, bez zargonu U+XXXX, wyjasnij ze to nie slownik ortograficzny tylko filtr na niewidzialny brud ktory marnuje godziny i tokeny

KROK 2 - PYTANIE O BEZPIECZNE TESTY:
- Zapytaj: CZY MAM WYKONAC BEZPIECZNE TESTY tego narzedzia? (selftesty, NIE na moich plikach)
- Czekaj na odpowiedz

KROK 3 - BEZPIECZNE TESTY (po zgodzie):
- Uruchom selftesty 4 czlonkow
- Pokaz wyniki

KROK 4 - NATURALNA REAKCJA:
- Daj swoja naturalna reakcje jako agent AI - czy to fajne i potrzebne? Szczerze, bez sciemy.
```

### METODA 2 — GitHub

Wklej do agenta:

```
Pobierz narzedzia rodziny z https://github.com/hotstrixi3-wq/BrutalAntiFlowerGangForAI
Pliki: PogromcaKwiatkow.py, ZagladaKultury.py, ProkuratorOgrodnik.py, AnihilatorChwastow.py, PROTOKOL-OPERATORA.md, RODZINA-DO-CZATU.md
Postepuj zgodnie z FLOW USWIADOMIENIE z RODZINA-DO-CZATU.md
```

## Co dalej?

Agent najpierw przeanalizuje repo i da Ci krotki opis co to i po co. Potem zapyta czy ma wykonac bezpieczne testy. Po testach da naturalna reakcje czy to fajne i potrzebne.

Nie skanuje od razu Twoich plikow. Nie zmienia nic bez zgody. Plan->act, kopia .bak, akta w U+XXXX.

## FAQ

- To antywirus?
Nie, kontrola tekstu: znaki i alfabety.

- Poprawi literowki?
Nie, pilnuje alfabetow, nie ortografii.

- Dziala offline?
Tak, 4 pliki, czysty Python 3 stdlib.

- Agent zgubil pliki rodzinki (nie zdarzyło mi sie)?
Podaj jeszcze raz

- Jakie komendy musze znać żeby tego używać?
to narzedzie jest stworzone przez agentów dla agentow. Ty jako uzytkownik korzystasz pośrednio. w praktyce jedyna komenda jaką musisz znać to "uzyj pogromcy".
bardzo mozliwe ze jakiś bardzo profesjonalny ludzki dłubacz kodów da rade tego używać osobiście ale nie taki jest cel tego narzędzia. narzedzie najlepiej działa w "rekach" agenta AI
AgentAI to ogarnie od ręki, aż bedzie furczało ;) natomiast profesjonalny programista spoci sie jak bedzie chciał użyć tego osobiście ;)

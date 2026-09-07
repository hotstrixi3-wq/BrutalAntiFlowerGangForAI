# ARK: SURVIVAL ASCENDED — ANALIZA MODA „PLAYER STAT LIMITER"
**CEL MODA:** ZAŁOŻYĆ CAP NA STATYSTYKĘ **SPEED (PRĘDKOŚĆ RUCHU)** GRACZA NA SERWERZE.

---

## 0. TL;DR — CO MA ZNACZENIE

1. **„PLAYER STAT LIMITER"** (Cocolosowasted, CurseForge) TO **MOD-BLUEPRINT** DO ARK ASA,
   CZYTAJĄCY CONFIG Z **`GameUserSettings.ini`** W SEKCJI **`[PlayerStatLimiter]`**.
2. **PRĘDKOŚĆ** W ARK TO **STATYSTYKA O INDEKSIE `9`** (`SpeedMultiplier`).
3. W TYM MODZIE CAP NA PRĘDKOŚĆ USTAWISZ JEDNĄ LINIĄ:
   `MaxPlayerSpeed=130.0`
   (WARTOŚĆ **BEZWZGLĘDNA**, GDZIE **100.0 = BAZA**, CZYLI ~130% ≈ OKOŁO 15 PUNKTÓW.)
4. MOD JEST WYSTARCZAJĄCY, JEŚLI CHCESZ TYLKO CAPNĄĆ PRĘDKOŚĆ GRACZA.
   JEŚLI CHCESZ CAPNĄĆ **LICZBĘ PUNKTÓW** (NIE WARTOŚĆ) LUB DZIAŁAĆ **BEZ MODA NA KLIENCIE** —
   PATRZ §5 (ALTERNATYWY).

> **UWAGA O HONESTNOŚCI:** BOT W TYM ŚRODOWISKU **NIE MÓGŁ POBIE RAĆ BINARKI MODA**
> (CURSEFORGE I ark-server-api.com MAJĄ ZBLOKOWANE TLS). ANALIZA NIE JEST WIĘC
> REVERSE-ENGINEERINGIEM SKOMPILOWANYCH BLUEPRINTÓW, TYLKO REKONSTRUKCJĄ NA BAZIE:
> (A) OPUBLIKOWANEGO INTERFEJSU CONFIGA, (B) REALNYCH OTWARTYCH ŹRÓDEŁ STRUKTUR
> MODÓW/PLUGINÓW ASA, KTÓRE ZOSTAŁY PHYSICZNIE POBIERANE.

---

## 1. CO TO JEST ZA MOD (RODZAJ/ARCHITEKTURA)

ASA OD ODMIANY 1.0 UŻYWA **MODÓW JAKO PLUGINÓW** (UE5). POWSTAJĄ W **ARSK: SURVIVAL
ASCENDED DEVKIT** (EDYTOR UNREAL ENGINE 5, `ASA DevKit`). MOD AUTOR TWORZY W UGC MENU:

```
UGC → Create New Mod → template → Create Mod
```

POWSTAJE **PLUGIN** — KATALOG Z PLIKIEM **`.uplugin`** + FOLDER **`Content/`**
(z BLUEPRINTY I ASSETY). STRUKTURA POTWIERDZONA NA POBRANYM, OTWARTYM PRZYKŁADZIE
**`gameserverapp/gsa-mod-asa`**:

```
gsa-mod.uplugin                     <- DESKRYPTOR PLUGINU (JSON, Nazwa/Kategoria "UGC")
Content/
  PrimalGameData_BP_GSA.uasset      <- PODKLASA PrimalGameData (globalne klasy)
  ModDataAsset_GSA.uasset           <- DataAsset rejestrujący zawartość moda
  Buff/Buff_GSA.uasset              <- BUFFY (stany) używane przez mod
  Other/... (widgety, struktury, przedmioty)
```

**PLIK `.uplugin` (POBRANY, AUTENTYCZNY):**
```json
{
	"FileVersion": 3,
	"Version": 1,
	"FriendlyName": "GameServerApp.com Integration",
	"Category": "UGC",
	"CanContainContent": true,
	"ExplicitlyLoaded": true
}
```

**WNIOSEK:** „PLAYER STAT LIMITER" TO DOKŁADNIE TAKI PLUGIN — BLUEPRINTY, KTÓRE
NADpisują/zawieszają się na systemie statystyk postaci i **CLAMPUJĄ WARTOŚĆ**.

---

## 2. INDEKSY STATYSTYK — KLUCZ DO ZROZUMIENIA CAPA

W ARK STATYSTYKI MĄJĄ STAŁĄ KOLEJNOŚĆ (indeksy w tablicach `*StatsMultiplier*`).

| INDEKS | STATYSTYKA | KLUCZ CONFIGA W „PLAYER STAT LIMITER" |
|:---:|---|---|
| 0 | HEALTH | `MaxPlayerHealth` |
| 1 | STAMINA | `MaxPlayerStamina` |
| 2 | TORPIDITY | — |
| 3 | OXYGEN | `MaxPlayerOxygen` |
| 4 | FOOD | `MaxPlayerFood` |
| 5 | WATER | `MaxPlayerWater` |
| 6 | TEMPERATURE | (brak w limiterze) |
| **7** | **WEIGHT** | `MaxPlayerWeight` |
| **8** | **MELEE DAMAGE** | `MaxPlayerDamage` |
| **9** | ** SPEED (prędkość ruchu)** | **`MaxPlayerSpeed`** |
| 10 | FORTITUDE | `MaxPlayerFortitude` |
| — | CRAFTING SPEED | `MaxPlayerCraftingSkill` |

**INDEKS `9` = PRĘDKOŚĆ — POTWIERDZONE** wieloma źródłami konfiguracji ASA, np.
`PerLevelStatsMultiplier_Player[9]=1.8` opisywane jako „SpeedMultiplier".

DWIE RZECZY WARTO ROZRÓŻNIĆ:
- **LICZBA PUNKTÓW (LEVELS)** — ile razy gracz podniósł stat (to limituje np. „SR's Stat Limiter").
- **WARTOŚĆ (VALUE/%)** — wynikowa liczba, np. 130.0 (=130%).

**„PLAYER STAT LIMITER" LIMITUJE WARTOŚĆ BEZWZGLĘDNĄ** (stąd `float`, np. `810.5`).

---

## 3. JAK MOD ENFORCES CAP (MECHANIZM) — REKONSTRUKCJA

TYPOWY MOD-BLUEPRINT TEGO TYPU ROBI COŚ W TYM STYLU (TO STANDARDOWA BUDOWA
MODU CAPPINGU STATYSTYK, NIE TYLKO TEN KONKRETNY):

1. **PODKŁASA `PrimalCharacterStatusComponent`** (lub hook na `PrimalCharacter_BP`).
   W BP nadpisuje się funkcje odpowiedzialne za **locowanie punktów** / **naliczanie
   wartości statystyki** przy levelowaniu.
2. ODCZYT LIMITU Z CONFIGA (`GameUserSettings.ini` → `[PlayerStatLimiter]` → `MaxPlayerSpeed`)
   przez **`GetGameUserSettings` / sekcję INI** (mod ma własną klasę configu, często
   implementowaną przez `UDeveloperSettings` lub własne czytanie `GameUserSettings.ini`).
3. **NA ZWIĘKSZENIE STATYSTYKI:** sprawdź wynikową wartość; jeśli `> limitów` →
   **odrzuć/cofnij naliczenie** (albo ustaw wartość na limit).
4. **NA SPŁAWNIENIE ISTNIEJĄCEJ POSTACI** (gracz, który JUŻ ma za dużo): mod może
   przy „spawn'/ respawn / wejściu na serwer" **przeliczyć i zclampować** bazowe wartości.

> **NIE DZIAŁA TO NA SKOMPILOWANYM BLUEPRINCIE** (`.uasset` to binarka UE; graf nie jest
> tekstem czytelnym dla człowieka). PODAŁEM WIĘC WYŻEJ **STANDARDOWY SCHEMAT**,
> A NIE DOSŁOWNY GRAF AUTORA — BO TEGO NIE DA SIĘ ODCZYTAĆ Z ZEWNĄTRZ.

---

## 4. JAK USTAWIC CAP NA SPEED (KONKRETNIE)

### 4.1. KROK 1 — DODAJ MOD NA SERWER

W **`ShooterGame/Saved/Config/WindowsServer/GameUserSettings.ini`**, sekcja `[ServerSettings]`:

```
[ServerSettings]
ActiveMods=1160661
```
albo (jeśli masz więcej modów):
```
ActiveMods=1160661,923456789
```

W **linii startowej serwera** dodaj:
```
-mods="1160661"
```
(np. `...?MaxPlayers=70 -NoBattleye -mods="1160661"`)

> ID `1160661` = Project ID moda „Player Stat Limiter" z CurseForge.

### 4.2. KROK 2 — USTAW LIMIT PRĘDKOŚCI

W TYM SAMYM **`GameUserSettings.ini`** (nowa sekcja):

```
[PlayerStatLimiter]
MaxPlayerHealth=1000.0
MaxPlayerStamina=1000.0
MaxPlayerOxygen=1000.0
MaxPlayerFood=1000.0
MaxPlayerWater=1000.0
MaxPlayerWeight=5000.0
MaxPlayerDamage=300.0
MaxPlayerSpeed=130.0
MaxPlayerCraftingSkill=200.0
MaxPlayerFortitude=100.0
```

**KLUCZOWE — `MaxPlayerSpeed=130.0`:**
- `100.0` = BAZOWA PRĘDKOŚĆ (100%).
- KAŻDY PUNKT SPED DODAJE JAKĄŚ STAŁĄ (w ARK historycznie ~2.0, więc 130 ≈ ok. 15 punktów).
- **WARTOŚĆ = BEZWZGLĘDNA, nie liczba punktów.** Chcesz cap 130% → `MaxPlayerSpeed=130.0`.
- Chcesz wyłączyć zupełnie → ustaw **bardzo nisko/blisko bazy**, np. `100.0` (chyba że chcesz
  zostawić 0 punktów — wtedy lepsza droga §5.1).

### 4.3. UWAGI

- **RESTART SERWERA PO ZMIANIE CONFIGA.**
- Mod jest **cross-platform**, ale zwykle musi być **w liście modów także po stronie gracza**
  (ASA pobierze go automatycznie, gdy jest w `ActiveMods`).
- **Cap na istniejące postacie** zależy od implementacji — może wymusić kolejne „spawn"
  lub wejście na serwer. Sprawdź po restarcie na graczu z przekroczonym speed.

---

## 5. ALTERNATYWY (JEŚLI MOD NIE WYSTARCZA / CHCESZ INACZEJ)

### 5.1. BEZ MODA — NATYWNIE W `Game.ini` (tylko „przydział punktów")

Nie ma natywnego *twardego capa wartości* prędkości gracza w ASA, ale **możesz
kontrolować przyrost** per poziom. W `Game.ini`:

```
[/Script/ShooterGame.ShooterGameMode]
PerLevelStatsMultiplier_Player[9]=0.0
```

- `0.0` = **punkt w Speed nic nie daje / nie poziomuje się** (najprostszy „cap").
- `0.5` = zmniejszony przyrost.
- **Zastrzeżenie:** nie cofa tego, co gracz już ma; nie ustawia też „maksymalnej wartości"
  (tylko mnożnik przyrostu). To narzędzie **bluntowe** — do miękkiego ograniczania.

### 5.2. PLUGIN **AsaApi** (C#, serwer bez moda na kliencie)

Alternatywny, często mocniejszy kierunek: **AsaApi plugin** (np. „SR's Stat Limiter" na
ark-server-api.com). To **natywny plugin serwerowy (C++)**, instalowany na dedykowanym
serwerze, **bez wymuszania moda dla graczy**, z przeładowaniem przez console/RCON:

```
StatLimiter.Reload      <- przeładuj konfigurację (console/RCON)
```

**Config (JSON, autentyczny opis):**
```json
{
  "PlayerLimits": {
    "Health": 5,
    "Stamina": 5,
    "Oxygen": 5,
    "Food": 5,
    "Water": 5,
    "Weight": 5,
    "MeleeDamageMultiplier": 5,
    "TemperatureFortitude": 5,
    "CraftingSpeedMultiplier": 5
  },
  "DinoLimits": { "Global": { "...": "...", "SpeedMultiplier": 5 }, "...": {} }
}
```

**Ważne:** w „PlayerLimits" **nie ma pola Speed** — Speed jest tylko w `DinoLimits`
(`SpeedMultiplier`). Jeśli chcesz **capnąć prędkość GRACZA liczbą punktów**, ten plugin
tego nie obejmuje (w wersji 1.1). **Do taska „cap Speed gracza" celuje dokładnie
`[PlayerStatLimiter] MaxPlayerSpeed=` z moda z §4.**

### 5.3. ŹRÓDŁA OTWARTE DO PODGLĄDU MECHANIKI

- **`gameserverapp/gsa-mod-asa`** (GitHub) — prawdziwy plugin ASA: `Content/*.uasset` + `gsa-mod.uplugin`.
- **`ArkServerApi/ASA-Plugins`** (GitHub) — pluginy AsaApi po stronie serwera (framework do
  hooków na graczach/dinozaurach — tam zobaczyć, jak C++ plugi się wpięły w zdarzenia).

---

## 6. RYZYKA / CO MOŻE NIE ZADZIAŁAĆ

| RYZYKO | CO ROBIĆ |
|---|---|
| Mod nie działa w multiplayer (producenci ASA niekiedy tak mają) | Użyj najnowszej wersji moda (5.5+); sprawdź, czy działa w singleplayer jako test |
| Cap nie cofa istniejących postaci | Wymusić ponowny „spawn" lub przejście postaci; niektórzy robią reset punktów |
| Wartość `MaxPlayerSpeed` to wartość, nie punkty | Zainwestuj chwilę w test; zacznij np. od `130.0` i skoryguj |
| Mod wymagany u klienta | Upewnij się, że `ActiveMods` jest w `GameUserSettings.ini` (serwer) — klient auto-pobierze |
| Serwer z `Applied Official Server Rates` ignoruje zmiany | Wyłącz „Applied Official Server Rates" w ustawieniach (Event → General Settings) |

---

## 7. PODSUMOWANIE W JEDNYM ZDANIU

**Aby capnąć SPEED gracza w ARK ASA najprostszym, celowanym sposobem:**
dodaj mod **„Player Stat Limiter"** (`ActiveMods=1160661` + `-mods="1160661"`),
a następnie w `GameUserSettings.ini` ustaw
**`[PlayerStatLimiter] MaxPlayerSpeed=130.0`**.

---

## ŹRÓDŁA

- [Player Stat Limiter — opis i klucze configa (CurseForge)](https://www.curseforge.com/ark-survival-ascended/mods/player-stat-limiter)
- [SR's Stat Limiter — config i komendy (ark-server-api.com)](https://ark-server-api.com/resources/srs-stat-limiter.80/)
- [Indeksy `PerLevelStatsMultiplier_Player[n]` — Speed to indeks 9 (Nitrado/Steam guide)](https://steamcommunity.com/app/2399830/discussions/0/4036976577928490911/)
- [Instalacja modów na dedykowanym serwerze ASA (GameUserSettings.ini + -mods)](https://skynethosting.net/blog/how-to-add-mods-to-asa-dedicated-server-complete-guide/)
- [ASA DevKit — mody jako pluginy](https://devkit.studiowildcard.com/getting-started/creating-new-mods)
- POBRANE OTWARTE ŹRÓDŁA: `github.com/gameserverapp/gsa-mod-asa` oraz `github.com/ArkServerApi/ASA-Plugins`

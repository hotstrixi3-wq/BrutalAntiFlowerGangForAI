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
4. **CO USTALONO Z POBRANYCH PLIKÓW (NIE Z OPISU):**
   - MOD TO PLUGIN `PlayerStatLimiter`, ID **`1160661`** (`cf_ugcID`).
   - LOGIKA SIEDZI W ASSETACH **`PlayerLimiter`** + **`PrimalGameData_BP_Limiter`**
     (PODKLASA `PrimalGameData_BP`) + **`ModDataAsset_Limiter`**.
   - MA **DWA BUILDY**: `Windows` (klient) i `WindowsServer` (serwer).
   - GRAF BLUEPRINTU JEST ZKOMPRESOWANY (OODLE) — **nie da się odczytać węzłów**,
     ale architektura i hooki potwierdzone przez import table + manifest.

---

## 1. CO TO JEST ZA MOD — Z FAKTYCZNYCH PLIKÓW

### 1.1. ZAWARTOŚĆ ZIPÓW (ROZPAKOWANO)

Każdy ZIP rozpakowuje się do katalogu **`PlayerStatLimiter/`**:

```
PlayerStatLimiter/
  PlayerStatLimiter.uplugin                 <- DESKRYPTOR PLUGINU (czytelny JSON)
  Manifest_NonUFSFiles_Win64.txt            <- manifest plików poza UFS
  Manifest_UFSFiles_Win64.txt               <- manifest plików w UFS (COOKED)
  Content/Paks/Windows/       ...           <- build KLIENCKI
  Content/Paks/WindowsServer/ ...           <- build SERWEROWY
```

**Z `Manifest_UFSFiles_Win64.txt` (rzeczywiste assety moda):**
```
ShooterGame/Mods/PlayerStatLimiter/AssetRegistry.bin
ShooterGame/Mods/PlayerStatLimiter/Content/ModDataAsset_Limiter.uasset        + .uexp
ShooterGame/Mods/PlayerStatLimiter/Content/PlayerLimiter.uasset               + .uexp
ShooterGame/Mods/PlayerStatLimiter/Content/PrimalGameData_BP_Limiter.uasset   + .uexp
ShooterGame/Mods/PlayerStatLimiter/Content/TestMapArea_Limiter.umap           + .uexp
ShooterGame/Mods/PlayerStatLimiter/Content/Paks/.../PlayerStatLimiterShooterGame-WindowsServer.pak
```

| ASSET | ROLA |
|---|---|
| `PlayerLimiter` | **GŁÓWNA LOGIKA** — Blueprint klasy, która pilnuje limitów statystyk |
| `PrimalGameData_BP_Limiter` | **PODKLASA **`PrimalGameData_BP`** — globalna gra game-data; mod nadpisuje ją, aby podpiąć własne klasy/hooki |
| `ModDataAsset_Limiter` | **DataAsset moda** — rejestruje zawartość moda |
| `TestMapArea_Limiter` | Mapa testowa (tylko do builda) |

### 1.2. `.uplugin` (ODCZYTANY Z PLIKU)

```json
{
  "FileVersion": 3,
  "Version": 1,
  "VersionName": "8A3CF4124B0088438DC0D2BC7EF9CB79",
  "FriendlyName": "Player Stat Limiter",
  "Description": "Mod is made for the ASA pvp community&cf_ugcID=1160661",
  "Category": "UGC",
  "MarketplaceURL": "https://legacy.curseforge.com/ark-survival-ascended/mods/player-stat-limiter",
  "CanContainContent": true,
  "SDKVersion": 598216,
  "ExplicitlyLoaded": true
}
```

**Potwierdzone:**
- `FriendlyName` = **"Player Stat Limiter"**
- `cf_ugcID` = **`1160661`** → ID do `ActiveMods`
- `SDKVersion` = **598216** (build ASA)
- `Category` = **UGC**
- `MarketplaceURL` → strona CurseForge moda

### 1.3. DWIE WERSJE — WHICH ONE

| BUILD | FOLDER | ROZMIAR `.ucas` | DO CZEGO |
|---|---|---|---|
| `Windows` | `Content/Paks/Windows/` | 31 120 B | **KLIENT / singleplayer** |
| `WindowsServer` | `Content/Paks/WindowsServer/` | 28 592 B | **SERWER dedykowany** |

Oba buildy mają te same assety (`PlayerLimiter`, `PrimalGameData_BP_Limiter`), ale
różnią się rozmiarem `.ucas` (client ma trochę więcej danych, np. UI/sieć). **Przy
stawianiu serwera używasz builda `WindowsServer`, a gracze pobierają `Windows`
(auto z serwera).**

---

## 2. INDEKSY STATYSTYK — KLUCZ DO ZROZUMIENIA CAPA

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
| **9** | **SPEED (prędkość ruchu)** | **`MaxPlayerSpeed`** |
| 10 | FORTITUDE | `MaxPlayerFortitude` |
| — | CRAFTING SPEED | `MaxPlayerCraftingSkill` |

**INDEKS `9` = PRĘDKOŚĆ — POTWIERDZONE** wieloma źródłami konfiguracji ASA, np.
`PerLevelStatsMultiplier_Player[9]=1.8` opisywane jako „SpeedMultiplier".

**DWIE RZECZY WARTO ROZRÓŻNIĆ:**
- **LICZBA PUNKTÓW (LEVELS)** — ile razy gracz podniósł stat.
- **WARTOŚĆ (VALUE/%)** — wynikowa liczba, np. 130.0 (=130%).

**„PLAYER STAT LIMITER" LIMITUJE WARTOŚĆ BEZWZGLĘDNĄ** (stąd `float`, np. `810.5`).

---

## 3. JAK MOD DEADLINE CAP (MECHANIZM)

### 3.1. CO POTWIERDZA STRUKTURA PLIKU
- `PrimalGameData_BP_Limiter` **rozszerza `PrimalGameData_BP`** — w tym assetcie ARK
  pozwala modom rejestrować własne klasy. W import table widoczne jest pole
  **`ServerExtraWorldSingletonActorClasses`** oraz referencje do `/Game/PlayerLimiter`.
- `PlayerLimiter` jest **typem rejestrowanym przez PrimalGameData** (jako
  server-wrold-singleton actor / klasa), co znaczy, że **instancja limitera działa
  na serwerze** i może nasłuchiwać zdarzeń statystyk gracza.

### 3.2. JAK TO DZIAŁA W PRAKTYCE (STANDARDOWY SCHEMAT MODU CAPA)
1. `PrimalGameData_BP_Limiter` rejestruje klasy `PlayerLimiter` w globalnej grze.
2. `PlayerLimiter` czyta limit z configa (`GameUserSettings.ini` → `[PlayerStatLimiter]`
   → `MaxPlayerSpeed`).
3. Gdy gracz próbuje podnieść statystykę, `PlayerLimiter` sprawdza **wynikową wartość**:
   jeśli `> limit` → **odrzuca/cofa naliczenie** albo przycina do limitu.
4. Przy wejściu gracza na serwer (lub respawn) może **przeliczyć i zclampować**
   wartość dla postaci, które już mają za dużo.

> **NIE ODKODOWANO GRAFU** — `.uasset`/`.ucas` to zkompresowana binarka (Oodle).
> Schemat w §3.2 to standardowa budowa moda cappingu statystyk ARK, potwierdzona
> przez strukturę assetów (PrimalGameData_BP + singleton actor), **nie** przez
> odczytany graf węzłów.

---

## 4. JAK USTAWIC CAP NA SPEED (KONKRETNIE)

### 4.1. KROK 1 — ZAINSTALUJ MOD NA SERWERZE

Skoro stawiasz serwer na **Windowsie na własnym PC** (home server), użyj builda
**`WindowsServer`**.

1. **Rozpakuj** ZIP `PlayerStatLimiter` (wariant z `Content/Paks/WindowsServer`)
   i wgraj jego zawartość do:
   ```
   ...\ShooterGame\Content\Mods\PlayerStatLimiter\
   ```
2. W **`ShooterGame/Saved/Config/WindowsServer/GameUserSettings.ini`**, sekcja `[ServerSettings]`:
   ```
   [ServerSettings]
   ActiveMods=1160661
   ```
   (albo `ActiveMods=1160661,<inneID>` jeśli masz więcej modów)
3. W **linii startowej serwera** dodaj:
   ```
   -mods="1160661"
   ```
   np. `...?MaxPlayers=70 -NoBattleye -mods="1160661"`.

### 4.2. KROK 2 — USTAW LIMIT PRĘDKOŚCI

W TYM SAMYM **`GameUserSettings.ini`** (nowa sekcja):

```ini
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
- **WARTOŚĆ = BEZWZGLĘDNA, nie liczba punktów.** Chcesz cap 130% → `MaxPlayerSpeed=130.0`.
- Chcesz „zamrozić" Speed przy bazie → ustaw `MaxPlayerSpeed=100.0`.
- Chcesz zupełnie zablokować punktowanie → patrz alternatywa w §5.1.

### 4.3. UWAGI
- **RESTART SERWERA PO ZMIANIE CONFIGA.**
- Mod jest **cross-platform** (ASA klient sam pobierze wariant `Windows`, gdy w
  `ActiveMods` jest ID moda — nie musisz rozsyłać pliku graczom).
- **Cap na istniejące postacie** zależy od implementacji — zwykle wymaga ponownego
  wejścia na serwer / respawn, żeby mod przeliczył wartości.

---

## 5. ALTERNATYWY (JEŚLI MOD NIE WYSTARCZA / CHCESZ INACZEJ)

### 5.1. BEZ MODA — NATYWNIE W `Game.ini` (tylko „przydział punktów")
```ini
[/Script/ShooterGame.ShooterGameMode]
PerLevelStatsMultiplier_Player[9]=0.0
```
- `0.0` = punkt w Speed nic nie daje / nie poziomuje się.
- `0.5` = zmniejszony przyrost.
- **Zastrzeżenie:** nie ustawia wartości bezwzględnej i nie cofa istniejących punktów.

### 5.2. PLUGIN **AsaApi** (C++, serwer bez moda na kliencie)
Natywny plugin serwerowy, np. **SR's Stat Limiter** (ark-server-api.com), instalowany
na dedykowanym serwerze, **bez wymuszania moda u graczy**. Komenda:
```
StatLimiter.Reload
```
**Uwaga (z opisu pluginu v1.1):** w `PlayerLimits` **nie ma pola Speed** — Speed jest
tylko w `DinoLimits` (`SpeedMultiplier`). Wi**c do capnięcia prędkości GRACZA wartocią
bezwzględną celuje dokładnie **`[PlayerStatLimiter] MaxPlayerSpeed=`** z moda (§4).

---

## 6. RYZYKA / CO MOŻE NIE ZADZIAŁAĆ

| RYZYKO | CO ROBIĆ |
|---|---|
| Mod nie działa w multiplayer | Użyj najnowszej wersji (build 5.5+); przetestuj w singleplayer |
| Cap nie cofa istniejących postaci | Wymuś ponowne wejście na serwer / respawn; ewentualny reset punktów |
| `MaxPlayerSpeed` to wartość, nie punkty | Zacznij np. od `130.0` i skoryguj po teście |
| Wgrany zły build (Windows zamiast WindowsServer) | Na serwer wgraj build z `Content/Paks/WindowsServer` |
| `ActiveMods` / `-mods` ID nie zgadza się | Użyj **`1160661`** (potwierdzone z `.uplugin`: `cf_ugcID`) |
| Serwer z `Applied Official Server Rates` ignoruje zmiany | Wyłącz „Applied Official Server Rates" (Event → General Settings) |

---

## 7. PODSUMOWANIE W JEDNYM ZDANIU

**Aby capnąć SPEED gracza w ARK ASA na swoim serwerze Windows:**
wgraj build **`WindowsServer`** moda do `ShooterGame/Content/Mods/PlayerStatLimiter`,
ustaw `ActiveMods=1160661` + `-mods="1160661"`, a w `GameUserSettings.ini` wpisz
**`[PlayerStatLimiter] MaxPlayerSpeed=130.0`**, potem restart serwera.

---

## ŹRÓDŁA / DOWODY

- **POBRANE PLIKI (w `arka_mod/`):** `player stat limiter-windows 2.zip`,
  `player stat limiter-windowsserver 2.zip` — rozpakowane i przeanalizowane.
- [Player Stat Limiter — opis i klucze configa (CurseForge)](https://www.curseforge.com/ark-survival-ascended/mods/player-stat-limiter)
- [SR's Stat Limiter — config i komendy (ark-server-api.com)](https://ark-server-api.com/resources/srs-stat-limiter.80/)
- [Indeksy `PerLevelStatsMultiplier_Player[n]` — Speed to indeks 9](https://steamcommunity.com/app/2399830/discussions/0/4036976577928490911/)
- [Instalacja modów na dedykowanym serwerze ASA (GameUserSettings.ini + -mods)](https://skynethosting.net/blog/how-to-add-mods-to-asa-dedicated-server-complete-guide/)
- [ASA DevKit — mody jako pluginy](https://devkit.studiowildcard.com/getting-started/creating-new-mods)

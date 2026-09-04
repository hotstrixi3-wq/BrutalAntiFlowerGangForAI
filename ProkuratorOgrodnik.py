# -*- coding: utf-8 -*-
"""Prokurator Ogrodnik: uzupelnienie Zaglady Kultury, czlonek rodziny Pogromcy Kwiatkow.

(v1.0.1) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
jest w pliku PROTOKOL-OPERATORA.md (drabina uprawnien, plan->act, combo
z rodzenstwem). Przeczytaj przed pierwszym uzyciem.

Rola w rodzinie:
- PogromcaKwiatkow.py = detektor (widzi, niczego nie zmienia)
- ZagladaKultury.py = dekontaminator (niszczy obca kulture, polska zostawia swieta)
- ProkuratorOgrodnik.py = ogrodnik-prokurator (pielegnuje ogrodek, prowadzi akta chwastow,
  decyduje co wyrwac, co zostawic, co zablokowac. Uzupelnia Zaglade o polityke.)

Problem ktory rozwiazuje:
Pogromca mowi BLAD. Zaglada mowi DO ZAGLADY / ZAGLADA. Ale kto decyduje CZY zaglada ma nastapic?
Czy plik i18n z CJK to brud czy celowa tresc? Czy test fixture z cyrylica to amunicja testowa czy wyciek?
Zaglada nie ma polityki. Prokurator ma.

Kontrakt v1.0.0:
- zbiera dowody: uruchamia Pogromce, parsuje werdykty, grupuje po pliku/linii/klasie
- sprawdza polityke: allowlist, fixtures, i18n, celowo brudna amunicja (dev/kwiatki-testy)
- klasyfikuje: UMORZONE (allowlist), POUCZENIE (UWAGA), ZAGLADA (BLAD do posprzatania), BLOKADA (podejrzenie sabotażu / celowy kwiatek w prozie)
- prowadzi akta: zapisuje dowody w notacji U+XXXX (nigdy zywe kwiatki w raporcie, §5), z kontekstem i ryzykiem
- egzekwuje bramke: exit 0 = czysto lub umorzone, 1 = jest do zaglady, 2 = blokada publikacji
- plan->act: domyslnie raport, --oskarz tworzy akta, --wykonaj uruchamia Zaglade tam gdzie polityka pozwala + kontrola Pogromca

Uzycie:
  python3 ProkuratorOgrodnik.py PLIK...                 # raport prokuratora
  python3 ProkuratorOgrodnik.py --oskarz PLIK...        # akta sprawy do pliku
  python3 ProkuratorOgrodnik.py --wykonaj PLIK...       # wykonaj zaglade gdzie wolno + kontrola
  python3 ProkuratorOgrodnik.py --selftest              # dowod dzialania

Polityka (domyslna, mozna rozszerzyc w pliku):
- dev/kwiatki-testy/*, **/fixtures/*, **/*test*brud* -> UMORZONE (celowo brudna amunicja)
- **/i18n/*, **/locales/*, **/*.po -> UMORZONE dla CJK/arab/hebr (tłumaczenia)
- .py literały -> POUCZENIE (Zaglada ich nie rusza, trzeba recznie)
- reszta BLAD -> ZAGLADA, wiele BLAD w jednym pliku + emoji + CJK -> BLOKADA do recznej oceny

Exit: 0 = czysto / umorzone, 1 = do zaglady, 2 = blokada / blad wejscia
"""

import io
import os
import sys
import subprocess
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

WERSJA = "1.2.0"

# (R3) Kopie zapasowe NIE MOGA byc wejsciem dla narzedzi. "mod.py.bak-zaglada"
# nie konczy sie na ".py", wiec trafialo do trybu prozy i tracilo ochrone
# literalow - chroniona tresc ginela wlasnie w kopii ratunkowej, a obok
# powstawal "mod.py.bak-zaglada.bak-zaglada".
_KOPIE = ("bak-pogromca", "bak-zaglada", "bak-anihilator")


def jest_kopia_zapasowa(sciezka):
    """True dla plikow .bak-pogromca / .bak-zaglada / .bak-anihilator (takze
    z sufiksem liczbowym, np. .bak-zaglada.3)."""
    n = os.path.basename(sciezka)
    for z in _KOPIE:
        if ("." + z) in n:
            return True
    return False


# (v1.1.0) FAIL-CLOSED: rodzenstwo wolane po sciezkach ABSOLUTNYCH liczonych
# z __file__. Do v1.0.1 bylo "PogromcaKwiatkow.py" - sciezka wzgledna, wiec
# Prokurator uruchomiony z innego katalogu roboczego dostawal returncode 2 i
# puste stdout, nie sprawdzal tego, i meldowal "czysto" z kodem wyjscia 0 na
# plikach brudnych. To byl fail-open w narzedziu, ktore ma byc fail-closed.
TU = os.path.dirname(os.path.abspath(__file__))


class BladRodziny(Exception):
    """Awaria uruchomienia rodzenstwa. Zawsze konczy sie BLOKADA, nigdy 'czysto'."""


def sciezka_rodzenstwa(nazwa):
    """Absolutna sciezka do czlonka rodziny lezacego obok tego pliku."""
    p = os.path.join(TU, nazwa)
    if not os.path.isfile(p):
        raise BladRodziny("brak czlonka rodziny: %s (szukano w %s)" % (nazwa, TU))
    return p

# --- polityka domyslna -------------------------------------------------
ALLOWLIST_GLOBS = [
    "dev/kwiatki-testy/*",
    "**/kwiatki-testy/*",
    "**/fixtures/*",
    "**/test_brudne*",
    "**/brudne*",
    "**/i18n/*",
    "**/locales/*",
    "**/*.po",
    "**/node_modules/*",
    "**/.git/*",
]

ALLOWLIST_CLASSES_FOR_I18N = {"CJK", "ARABSKIE", "HEBRAJSKIE", "TAJSKIE", "KANA", "HANGUL", "CYRYLICA", "GREKA"}

def match_allowlist(path: str) -> bool:
    import fnmatch
    for pat in ALLOWLIST_GLOBS:
        if fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(os.path.basename(path), pat):
            return True
    return False

def run_pogromca(files):
    """Uruchamia PogromcaKwiatkow.py i zwraca (stdout, returncode).

    (v1.1.0) Kody wyjscia Pogromcy: 0 = czysto, 1 = jest BLAD. KAZDY inny kod
    oznacza, ze podproces nie wystartowal albo sie wysypal - wtedy rzucamy
    BladRodziny zamiast parsowac puste stdout jako 'brak znalezisk'."""
    cmd = [sys.executable, sciezka_rodzenstwa("PogromcaKwiatkow.py")] + files
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise BladRodziny(
            "Pogromca zakonczyl sie kodem %d (spodziewane 0 lub 1). stderr: %s"
            % (result.returncode, (result.stderr or "").strip()[:300]))
    if result.returncode == 1 and not result.stdout.strip():
        raise BladRodziny("Pogromca zglosil BLAD, ale nie wypisal nic na stdout")
    return result.stdout, result.returncode


def rozwin_argumenty(pliki):
    """(v1.1.0) Zamienia katalogi na liste plikow i odrzuca sciezki nieistniejace.

    Do v1.0.1 katalog szedl wprost do Pogromcy, wracal jako
    '[BLAD] <sciezka>: nie czyta sie (Is a directory)', a parser bral CALY
    ten komunikat bledu za nazwe pliku i dopisywal do akt zmyslone
    znalezisko z decyzja ZAGLADA."""
    wynik, brakujace = [], []
    for a in pliki:
        if os.path.isdir(a):
            for korzen, _katalogi, nazwy in os.walk(a):
                for n in sorted(nazwy):
                    pelna = os.path.join(korzen, n)
                    if jest_kopia_zapasowa(pelna):
                        continue          # (R3) nie tykamy kopii ratunkowych
                    wynik.append(pelna)
        elif os.path.isfile(a):
            wynik.append(a)
        else:
            brakujace.append(a)
    return wynik, brakujace

def rozwiaz_sciezke_z_raportu(kandydat):
    """(v1.1.0) Zamienia sciezke z raportu Pogromcy na istniejacy plik albo None.

    Pogromca wypisuje nazwy przez os.path.relpath(sciezka, HOME), gdzie HOME to
    katalog NADRZEDNY wobec katalogu rodziny - a nie katalog roboczy Prokuratora.
    Dlatego samo os.path.isfile() na tym, co wydrukowal, odrzuca poprawne pliki.
    Sprawdzamy wiec obie bazy, zanim uznamy linie za komunikat bledu."""
    if not kandydat:
        return None
    bazy = (os.path.dirname(TU), TU, os.getcwd())
    if os.path.isabs(kandydat):
        return kandydat if os.path.isfile(kandydat) else None
    for baza in bazy:
        p = os.path.normpath(os.path.join(baza, kandydat))
        if os.path.isfile(p):
            return p
    return None


def parse_pogromca_output(output: str):
    """Parsuje output Pogromcy na liste znalezisk."""
    findings = []
    current_file = None
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("[BLAD]") or line.startswith("[UWAGA]") or line.startswith("[OK]"):
            # Format: [BLAD]  sciezka
            #         KLASA: linia X, znak 'Y' | ...
            m = re.match(r"\[(BLAD|UWAGA|OK)\]\s+(.+)", line)
            if m:
                kandydat = m.group(2).strip()
                # (v1.1.0) Pogromca wypisuje bledy wejscia w tym samym formacie
                # co werdykty ("[BLAD] <sciezka>: nie czyta sie (...)"). Bez tego
                # sprawdzenia komunikat bledu ladowal w aktach jako nazwa pliku
                # z decyzja ZAGLADA - sfabrykowana sprawa.
                if rozwiaz_sciezke_z_raportu(kandydat) is None:
                    findings.append({"file": kandydat, "verdict": "BLAD_WEJSCIA",
                                     "details": [], "surowa_linia": line})
                    current_file = None
                    continue
                current_file = kandydat
                findings.append({"file": current_file, "verdict": m.group(1), "details": []})
        elif "linia" in line and "znak" in line:
            # linia z klasa
            # np: CYRYLICA: linia 1, znak 'a' | ...
            if findings:
                findings[-1]["details"].append(line)
        elif "PODSUMOWANIE" in line:
            continue
    return findings


# (v1.0.1) notacja U+XXXX dla akt: raport Pogromcy niesie ZYWE znaki obce,
# akta jako artefakt archiwalny musza byc czyste (PROTOKOL: "akta w U+XXXX")
_PL = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
_TYPO = "—–„”…€%§°²³±·«»"
_DOZWOLONE = set(chr(c) for c in range(0x20, 0x7F)) | set(_PL) | set(_TYPO)

def notacja_uxxxx(tekst):
    """Zamienia kazdy znak spoza kultury dozwolonej na opis U+XXXX."""
    return "".join(c if c in _DOZWOLONE else "U+%04X" % ord(c) for c in tekst)

def classify_findings(findings):
    """Klasyfikuje na UMORZONE / POUCZENIE / ZAGLADA / BLOKADA."""
    akta = []
    summary = Counter()
    for f in findings:
        path = f["file"]
        verdict = f["verdict"]
        details = f["details"]
        if verdict == "OK":
            summary["OK"] += 1
            continue
        if verdict == "BLAD_WEJSCIA":
            # (v1.1.0) fail-closed: nie umiemy powiedziec nic o pliku, ktorego
            # Pogromca nie przeczytal. To NIE jest "czysto".
            akta.append({
                "plik": path,
                "werdykt_pogromcy": "BLAD_WEJSCIA",
                "klasy": {},
                "decyzja": "BLOKADA",
                "powod": "Pogromca nie przeczytal wejscia - brak podstaw do jakiejkolwiek decyzji",
                "dowody": [notacja_uxxxx(f.get("surowa_linia", ""))],
            })
            summary["BLOKADA"] += 1
            continue
        # policz klasy
        classes = []
        for d in details:
            cls = d.split(":")[0].strip() if ":" in d else "NIEZNANE"
            classes.append(cls)
        class_counter = Counter(classes)

        # polityka
        if match_allowlist(path):
            # sprawdz czy to i18n i czy klasy sa na allowliscie i18n
            if any(g in path for g in ["i18n", "locales", ".po"]) and all(c.split()[0] in ALLOWLIST_CLASSES_FOR_I18N or "CJK" in c or "CYRYLICA" in c for c in classes):
                decyzja = "UMORZONE"
                powod = "allowlist i18n / tlumaczenia"
            else:
                decyzja = "UMORZONE"
                powod = "allowlist: celowo brudna amunicja testowa"
            summary["UMORZONE"] += 1
        elif verdict == "UWAGA":
            decyzja = "POUCZENIE"
            powod = "UWAGA do decyzji misji"
            summary["POUCZENIE"] += 1
        else:  # BLAD
            # jesli .py i detale wskazuja na literał (heurystyka: w raporcie jest 'print' lub cudzyslow)
            is_py = path.endswith(".py")
            # BLOKADA gdy wiele roznych klas + emoji + CJK w jednym pliku prozy
            if len(class_counter) >= 4 and any("EMOJI" in c or "PIKTOGRAM" in c or "CJK" in c for c in classes):
                decyzja = "BLOKADA"
                powod = "wiele obcych kultur + emoji - podejrzenie sabotażu lub celowego kwiatka, wymaga recznej oceny"
                summary["BLOKADA"] += 1
            elif is_py:
                # dla .py - jesli w detail jest cudzyslow, to prawdopodobnie literal
                decyzja = "POUCZENIE"
                powod = ".py literal - Zaglada nie rusza (sacred), wymaga recznej poprawy"
                summary["POUCZENIE"] += 1
            else:
                decyzja = "ZAGLADA"
                powod = "BLAD do dekontaminacji przez Zaglade"
                summary["ZAGLADA"] += 1

        akta.append({
            "plik": path,
            "werdykt_pogromcy": verdict,
            "klasy": dict(class_counter),
            "decyzja": decyzja,
            "powod": powod,
            "dowody": [notacja_uxxxx(d) for d in details[:10]],  # (v1.0.1) escape: raport Pogromcy niesie zywe znaki
        })
    return akta, summary

def run_zaglada_if_allowed(akta):
    """Uruchamia Zaglade tam gdzie decyzja=ZAGLADA."""
    do_zaglady = [a["plik"] for a in akta if a["decyzja"] == "ZAGLADA"]
    if not do_zaglady:
        return
    for plik in do_zaglady:
        cmd = [sys.executable, sciezka_rodzenstwa("ZagladaKultury.py"), "--zaglada", plik]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout.strip())
        # (v1.1.0) awaria Zaglady to nie jest cichy brak zmian
        if result.returncode != 0:
            print("[BLOKADA] %s -> Zaglada zakonczyla sie kodem %d: %s"
                  % (plik, result.returncode, (result.stderr or "").strip()[:200]))
            continue
        # kontrola Pogromca po zagladzie (combo §1a)
        out, code = run_pogromca([plik])
        if code == 0:
            print(f"[KONTROLA] {plik} -> BLAD 0 po zagladzie - OK")
        else:
            print(f"[KONTROLA] {plik} -> nadal BLAD {code} - wymaga recznej interwencji")

def selftest():
    print("SELFTEST Prokuratora Ogrodnika v1.0.1")
    # stworz fixtures
    os.makedirs("tmp_prokurator_test", exist_ok=True)
    # czysty
    with open("tmp_prokurator_test/czysty.py", "w", encoding="utf-8") as f:
        f.write("print('czyste ąćęłńóśźż')\n")
    # brudny poza allowlist
    with open("tmp_prokurator_test/brudny.txt", "w", encoding="utf-8") as f:
        f.write("Spokojnie \u0430 spac\n")  # U+0430
    # brudny w allowlist (fixtures)
    os.makedirs("tmp_prokurator_test/fixtures", exist_ok=True)
    with open("tmp_prokurator_test/fixtures/brudny_fixture.txt", "w", encoding="utf-8") as f:
        f.write("Test \u0430\u0431\u0432\n")
    # i18n
    os.makedirs("tmp_prokurator_test/i18n", exist_ok=True)
    with open("tmp_prokurator_test/i18n/pl.po", "w", encoding="utf-8") as f:
        f.write("msgid \"hello\"\nmsgstr \"\u4e2d\u6587\"\n")

    files = [
        "tmp_prokurator_test/czysty.py",
        "tmp_prokurator_test/brudny.txt",
        "tmp_prokurator_test/fixtures/brudny_fixture.txt",
        "tmp_prokurator_test/i18n/pl.po",
    ]
    out, code = run_pogromca(files)
    print(out)
    findings = parse_pogromca_output(out)
    akta, summary = classify_findings(findings)
    print("\nAKTA PROKURATORA:")
    print(json.dumps(akta, indent=2, ensure_ascii=False))
    print("\nPODSUMOWANIE:", dict(summary))
    # oczekiwane: czysty OK, brudny ZAGLADA, fixture UMORZONE, i18n UMORZONE
    ok = summary.get("OK", 0) == 1 and summary.get("ZAGLADA", 0) == 1 and summary.get("UMORZONE", 0) == 2
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    # sprzatanie
    import shutil
    shutil.rmtree("tmp_prokurator_test")
    return 0 if ok else 1

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if "--selftest" in args:
        return selftest()

    wykonaj = "--wykonaj" in args
    oskarz = "--oskarz" in args
    pliki = [a for a in args if not a.startswith("--")]

    if not pliki:
        print("Podaj pliki do oskarzenia")
        return 2

    # (v1.1.0) katalogi -> pliki, sciezki nieistniejace -> BLOKADA
    pliki, brakujace = rozwin_argumenty(pliki)
    if brakujace:
        for b in brakujace:
            print("[BLOKADA] nie istnieje: %s" % b)
        return 2
    if not pliki:
        print("[BLOKADA] po rozwinieciu argumentow nie zostal zaden plik")
        return 2

    # 1. Dry-run: Pogromca
    try:
        out, code = run_pogromca(pliki)
    except BladRodziny as e:
        # (v1.1.0) fail-closed: awaria rodzenstwa NIGDY nie moze wygladac
        # jak "czysto". Do v1.0.1 konczylo sie to kodem 0 i pustym podsumowaniem.
        print("[BLOKADA] awaria rodzenstwa: %s" % e)
        return 2
    print(out)

    findings = parse_pogromca_output(out)
    akta, summary = classify_findings(findings)

    print("\n=== AKTA PROKURATORA OGRODNIKA ===")
    for a in akta:
        print(f"{a['plik']} -> {a['werdykt_pogromcy']} | {a['decyzja']} | {a['powod']} | klasy: {a['klasy']}")

    print(f"\nPODSUMOWANIE PROKURATORA: {dict(summary)}")
    print("OPERATOR: PROTOKOL §1a + §2.6 - decyzja przed publikacja")

    if oskarz:
        with open("akta_prokuratora.json", "w", encoding="utf-8") as f:
            json.dump(akta, f, indent=2, ensure_ascii=False)
        print("[AKTA] Zapisano akta_prokuratora.json (dowody w notacji U+XXXX, bez zywych kwiatkow)")

    if wykonaj:
        run_zaglada_if_allowed(akta)

    # exit code
    if summary.get("BLOKADA", 0) > 0:
        return 2
    if summary.get("ZAGLADA", 0) > 0 or summary.get("POUCZENIE", 0) > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Prokurator Ogrodnik: uzupelnienie Zaglady Kultury, czlonek rodziny Pogromcy Kwiatkow.

(v1.0.0) OPERATOR — agencie AI: Twoj regulamin uzycia tego narzedzia
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

WERSJA = "1.0.0"

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
    """Uruchamia PogromcaKwiatkow.py i zwraca stdout."""
    cmd = [sys.executable, "PogromcaKwiatkow.py"] + files
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.returncode

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
                current_file = m.group(2).strip()
                findings.append({"file": current_file, "verdict": m.group(1), "details": []})
        elif "linia" in line and "znak" in line:
            # linia z klasa
            # np: CYRYLICA: linia 1, znak 'a' | ...
            if findings:
                findings[-1]["details"].append(line)
        elif "PODSUMOWANIE" in line:
            continue
    return findings

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
            "dowody": details[:10],  # max 10 dowodow, w notacji U+XXXX (Pogromca juz tak raportuje)
        })
    return akta, summary

def run_zaglada_if_allowed(akta):
    """Uruchamia Zaglade tam gdzie decyzja=ZAGLADA."""
    do_zaglady = [a["plik"] for a in akta if a["decyzja"] == "ZAGLADA"]
    if not do_zaglady:
        return
    for plik in do_zaglady:
        cmd = [sys.executable, "ZagladaKultury.py", "--zaglada", plik]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout.strip())
        # kontrola Pogromca po zagladzie (combo §1a)
        out, code = run_pogromca([plik])
        if code == 0:
            print(f"[KONTROLA] {plik} -> BLAD 0 po zagladzie - OK")
        else:
            print(f"[KONTROLA] {plik} -> nadal BLAD {code} - wymaga recznej interwencji")

def selftest():
    print("SELFTEST Prokuratora Ogrodnika v1.0.0")
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

    # 1. Dry-run: Pogromca
    out, code = run_pogromca(pliki)
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

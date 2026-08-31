"""PĘTLA RODZINNA (produkcja) — Pogromca v8.0.x + Zagłada v1.0.x.
Cykl = 7 sprawdzianów: tor autora, fuzz autora, T1, T2, T3 (Pogromca)
+ Z1, Z2 (Zagłada). Świeże seedy co cykl. Budżet sekund z argv (default 1200).
Wpadka = stop natychmiast (exit 2) z ogonem loga. Exit 0 = budżet odmachany."""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "pogromca-kwiatkow-main")
BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
PY = sys.executable

start = time.time()
cykl = 0
awarie = []


def uruchom(cmd, cwd, timeout=300):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"
    except Exception as e:
        return 99, ascii(str(e))


print("PĘTLA RODZINNA start %s | budżet %d s | 7 sprawdzianów/cykl" % (
    time.strftime("%H:%M:%S"), BUDGET), flush=True)
while time.time() - start < BUDGET:
    cykl += 1
    plan = [
        ("T0a-tor", [PY, "dev/tor-pogromcy.py"], REPO),
        ("T0b-fuzz", [PY, "dev/fuzz-pogromcy.py"], REPO),
        ("T1-niezalezny", [PY, "turniej-niezalezny.py"], HERE),
        ("T2-sprawdzajacy", [PY, "turniej-2-sprawdzajacy.py", str(20300000 + cykl)], HERE),
        ("T3-niepsucie", [PY, "turniej-3-niepsucie.py", str(20400000 + cykl)], HERE),
        ("Z1-wykrywanie", [PY, "zaglada-turniej-wykrywania.py", str(20500000 + cykl)], HERE),
        ("Z2-niepsucie", [PY, "zaglada-turniej-niepsucie.py", str(20600000 + cykl)], HERE),
    ]
    for nazwa, cmd, cwd in plan:
        kod, out = uruchom(cmd, cwd)
        if kod != 0:
            print("  CYKL %d %s: EXIT %d — STOP" % (cykl, nazwa, kod), flush=True)
            for ln in out.splitlines()[-15:]:
                print("    | " + ln, flush=True)
            awarie.append((cykl, nazwa, kod))
            print("PĘTLA RZERWANA: cykl %d, %s, exit %d" % (cykl, nazwa, kod), flush=True)
            sys.exit(2)
    print("  CYKL %d: 7/7 zielone (%.0f s do konca)" % (
        cykl, BUDGET - (time.time() - start)), flush=True)

print("=" * 66, flush=True)
print("BUDŻET ODMACHANY: cykli %d | sprawdzianów %d | awarie %d | %.0f s" % (
    cykl, cykl * 7, len(awarie), time.time() - start), flush=True)
sys.exit(0)

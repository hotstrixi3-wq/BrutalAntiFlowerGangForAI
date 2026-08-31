"""PĘTLA TURNIEJOWA — PogromcaKwiatkow v8.0.2.
Jedzie godzinę (budżet z argv, domyślnie 3300 s). Każdy cykl:
  T0a tor autora (348 wektorów)   T0b fuzz autora (3x500)
  T1  turniej niezależny (4666)    T2 turniej sprawdzający (losowy seed)
  T3  turniej nie-psucie kodu (losowy seed)
Medal PEWNIAK: pierwszy cykl w całości zielony BEZ poprawek kodu
(poprawka v8.0.2 wpisana PRZED startem pętli). Dalsze cykle = ciągła
weryfikacja. Wpadka = stop (exit 2) do naprawy. Exit 0 = godzina green."""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "pogromca-kwiatkow-main")
BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 3300
SEED0 = 20260901
PY = sys.executable

start = time.time()
cykl = 0
medal = None
awarie = []


def uruchom(nazwa, cmd, cwd, timeout=300):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"
    except Exception as e:
        return 99, ascii(str(e))


print("PĘTLA TURNIEJOWA start %s | budżet %d s | %s" % (
    time.strftime("%H:%M:%S"), BUDGET, "PogromcaKwiatkow v8.0.2"), flush=True)
while time.time() - start < BUDGET:
    cykl += 1
    pozostalo = BUDGET - (time.time() - start)
    plan = [
        ("T0a-tor", [PY, "dev/tor-pogromcy.py"], REPO),
        ("T0b-fuzz", [PY, "dev/fuzz-pogromcy.py"], REPO),
        ("T1-niezalezny", [PY, "turniej-niezalezny.py"], HERE),
        ("T2-sprawdzajacy", [PY, "turniej-2-sprawdzajacy.py", str(SEED0 + cykl)], HERE),
        ("T3-niepsucie", [PY, "turniej-3-niepsucie.py", str(SEED0 + 100000 + cykl)], HERE),
    ]
    zielone = 0
    for nazwa, cmd, cwd in plan:
        kod, out = uruchom(nazwa, cmd, cwd)
        if kod != 0:
            print("  CYKL %d %s: EXIT %d — STOP" % (cykl, nazwa, kod), flush=True)
            for ln in out.splitlines()[-15:]:
                print("    | " + ln, flush=True)
            awarie.append((cykl, nazwa, kod))
            print("PĘTLA PRZERWANA: cykl %d, %s, exit %d" % (cykl, nazwa, kod),
                  flush=True)
            sys.exit(2)
        zielone += 1
    if medal is None:
        medal = time.strftime("%H:%M:%S")
        print("  CYKL %d: 5/5 ZIELONE *** MEDAL PEWNIAKA v8.0.2 PRZYZNANY (%s) ***"
              % (cykl, medal), flush=True)
    else:
        print("  CYKL %d: 5/5 zielone (%.0f s do konca)" % (
            cykl, pozostalo), flush=True)

print("=" * 66, flush=True)
print("GODZINA ODMACHANA: cykli %d | awarie %d | medal: %s" % (
    cykl, len(awarie), "PEWNIAK v8.0.2 od " + str(medal) if medal else "BRAK"),
    flush=True)
sys.exit(0)

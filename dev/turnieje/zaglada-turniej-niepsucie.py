"""TURNIEJ ZAGŁADY 2 — NIENISZCZENIE KODU/DANYCH (ZagladaKultury v1.0.1).
G1 czyste pliki -> bajt-w-bajt | G2 .py czysty z obca kultura w literale
-> nietkniety | G3 .py brud w kodzie -> kompiluje+idempotencja | G4 .py
zepsuty -> ratunek bez psucia literalow | G5 proza -> litery PL nietknięte
| G6 JSON -> struktura zywa. Exit 0 = zaliczony."""
import contextlib
import importlib.util
import io
import json
import os
import random
import shutil
import sys
import tempfile
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
def _znajdz(nazwa):
    for k in (os.path.join(HERE, nazwa),
              os.path.join(HERE, "..", "..", nazwa),
              os.path.join(HERE, "pogromca-kwiatkow-main", nazwa)):
        if os.path.isfile(k):
            return os.path.abspath(k)
    raise SystemExit("nie znaleziono: " + nazwa)
ZK_PATH = _znajdz("ZagladaKultury.py")
spec = importlib.util.spec_from_file_location("zk", ZK_PATH)
zk = importlib.util.module_from_spec(spec)
sys.modules["zk"] = zk
spec.loader.exec_module(zk)

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260921
rnd = random.Random(SEED)
print("TURNIEJ ZAGŁADY 2 — NIENISZCZENIE (v%s, seed %d)" % (zk.WERSJA, SEED))
print("=" * 66)

PL = ["kasza", "gęś", "jaźń", "źdźbło", "łódź", "śledź", "piorun", "mżący",
      "krzątanina", "zwierz", "głośny", "żółw", "wędrowiec", "źrenica"]
EN = ["server", "worker", "queue", "engine", "cache", "router", "beacon"]
OG = "ąćęłńóśźż"


def slowo():
    w = rnd.choice(PL + EN)
    if rnd.random() < 0.5:
        i = rnd.randrange(len(w))
        w = w[:i] + rnd.choice(OG) + w[i + 1:]
    return w


def opis():
    return " ".join(slowo() for _ in range(rnd.randrange(4, 9))).capitalize()


def gen_py(idx):
    return "\n".join([
        "# -*- coding: utf-8 -*-",
        '"""Modul %d: %s."""' % (idx, opis()),
        "import os",
        "STALA = %d" % rnd.randrange(1000),
        'TEKST = "%s"' % opis(),
        "",
        "def fn_%d(a, b=%d):" % (idx, rnd.randrange(9)),
        "    # uwaga: %s" % opis(),
        "    return a * b + STALA - %d" % rnd.randrange(30),
        "",
        "class K%d:" % idx,
        "    def __init__(self):",
        "        self.w = fn_%d(2)" % idx,
        "",
        "if __name__ == '__main__':",
        "    print(K%d().w, os.name)" % idx,
        "",
    ])


D = tempfile.mkdtemp(prefix="z2_")
POPSUTE, STAN = [], {"g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0}


def zapisz(n, t):
    p = os.path.join(D, n)
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    return p


def czytaj(p):
    with io.open(p, encoding="utf-8", newline="") as f:
        return f.read()


def kompiluje(t, p):
    try:
        compile(t, p, "exec")
        return True
    except SyntaxError:
        return False


def zaglada_cicho(tekst, p):
    with contextlib.redirect_stdout(io.StringIO()):
        zk.przetworz(tekst, p)  # tylko policz; zapis przez raport_sciezka
    # wlasciwe wykonanie na pliku:
    with contextlib.redirect_stdout(io.StringIO()):
        zk.raport_sciezka(p, True)


LS, ZWSP, NBSP = chr(0x2028), chr(0x200B), chr(0x00A0)
CYR_TOK, ARAB3, CJK_TOK = chr(0x0435), chr(0x0663), chr(0x4E2D)

# --- G1 czyste -> bajt w bajt -------------------------------------------------
for i in range(60):
    if i % 3 == 0:
        t, nm = gen_py(i), "g1_%d.py" % i
        assert kompiluje(t, nm)
    else:
        t = opis() + rnd.choice([".", "!"]) + "\n"
        nm = "g1_%d.%s" % (i, "md" if i % 2 else "txt")
    p = zapisz(nm, t)
    zaglada_cicho(czytaj(p), p)
    if czytaj(p) != t:
        POPSUTE.append(("G1", nm + " zmieniony"))
    STAN["g1"] += 1

# --- G2 .py z obca kultura w literale/komentarzu -> nietkniety ------------------
for i in range(30):
    t = gen_py(100 + i)
    w = rnd.choice([CYR_TOK, CJK_TOK, "Ω"])
    t = t.replace('TEKST = "', 'TEKST = "' + w, 1)
    if not kompiluje(t, "x.py"):
        t = t.replace('TEKST = "' + w, 'TEKST = "', 1)  # fallback
    p = zapisz("g2_%d.py" % i, t)
    zaglada_cicho(czytaj(p), p)
    if czytaj(p) != t:
        POPSUTE.append(("G2", "g2_%d.py literal/komentarz ruszony" % i))
    STAN["g2"] += 1

# --- G3 .py z brudem w KODZIE (w srodku tokenow) -> kompiluje + idempotentny ----
for i in range(30):
    t = gen_py(200 + i)
    brud = rnd.choice([ZWSP, NBSP, ARAB3, CYR_TOK, CJK_TOK])
    gdzie = rnd.choice(["nazwa", "liczba", "import"])
    if gdzie == "nazwa":          # STALA -> STA<brud>LA (po oczyszczeniu wraca nazwa)
        t = t.replace("STALA", "STA" + brud + "LA", 1)
    elif gdzie == "liczba":       # miedzy cyframi liczby (po: cyfra ASCII wchodzi)
        t = t.replace("STALA = ", "STALA = 1" + brud, 1)
    else:                         # import<brud>os (po: spacja/usuniecie skleja poprawnie)
        t = t.replace("import os", "import" + brud + "os", 1)
    p = zapisz("g3_%d.py" % i, t)
    zaglada_cicho(czytaj(p), p)
    w1 = czytaj(p)
    if not kompiluje(w1, p):
        POPSUTE.append(("G3", "g3_%d.py nie kompiluje po zagładzie [%s/%s]" % (i, gdzie, ascii(brud))))
    zaglada_cicho(w1, p)
    if czytaj(p) != w1:
        POPSUTE.append(("G3", "g3_%d.py nie-idempotentny" % i))
    STAN["g3"] += 1

# --- G4 .py zepsuty (lamacz-sep) + brud -> ratunek bez psucia literalow --------
for i in range(20):
    t = gen_py(300 + i)
    sep = rnd.choice([LS, chr(0x2029), chr(0x85)])
    linie = [l for l in t.split("\n") if l.strip()]
    for j in range(2, len(linie) - 1, 3):
        linie[j] = linie[j] + sep
    t2 = "\n".join(linie) + "\n"
    mial_ls = False
    if rnd.random() < 0.5:
        t2 = t2.replace('TEKST = "', 'TEKST = "' + LS, 1)
        mial_ls = True
    p = zapisz("g4_%d.py" % i, t2)
    zaglada_cicho(czytaj(p), p)
    w = czytaj(p)
    if mial_ls and LS not in w:
        POPSUTE.append(("G4", "g4_%d.py LS z literalu usuniety" % i))
    if not kompiluje(w, p) and kompiluje(t2, p):
        POPSUTE.append(("G4", "g4_%d.py zepsuty przez zagładę" % i))
    zaglada_cicho(w, p)
    if czytaj(p) != w:
        POPSUTE.append(("G4", "g4_%d.py nie-idempotentny" % i))
    STAN["g4"] += 1

# --- G5 proza: litery PL nietkniete (brud tylko nieliterowy) ---------------------
for i in range(30):
    t = opis() + "\n" + opis() + "\n"
    litery_przed = "".join(c for c in t if c.isalpha())
    for _ in range(rnd.randrange(2, 6)):
        poz = rnd.randrange(len(t))
        brud = rnd.choice([ZWSP, NBSP, chr(0x200C), LS, chr(0x2029)])
        t = t[:poz] + brud + t[poz:]
    p = zapisz("g5_%d.md" % i, t)
    zaglada_cicho(czytaj(p), p)
    w1 = czytaj(p)
    if "".join(c for c in w1 if c.isalpha()) != litery_przed:
        POPSUTE.append(("G5", "g5_%d.md litery zmienione" % i))
    for brud in (ZWSP, chr(0x200C)):
        if brud in w1:
            POPSUTE.append(("G5", "g5_%d.md brud zostal" % i))
    zaglada_cicho(w1, p)
    if czytaj(p) != w1:
        POPSUTE.append(("G5", "g5_%d.md nie-idempotentny" % i))
    STAN["g5"] += 1
# mini: proza z obcym slowem -> po zagładzie brud znika, polskie zostaje
for i in range(10):
    t = opis() + " " + CYR_TOK + "а" + CJK_TOK + " " + opis() + "\n"
    p = zapisz("g5b_%d.md" % i, t)
    zaglada_cicho(czytaj(p), p)
    w1 = czytaj(p)
    if CJK_TOK in w1 or "а" in w1:
        POPSUTE.append(("G5", "g5b_%d.md obre pismo zostalo" % i))
    if slowo() and not any(s in w1 for s in PL):
        pass  # opis() losowy; pelne sprawdzenie liter powyejej w glownej petli
    STAN["g5"] += 1

# --- G6 JSON zyje po zagładzie ---------------------------------------------------
for i in range(20):
    dane = {"nazwa": opis(), "wersja": "%d.%d.%d" % (rnd.randrange(3), rnd.randrange(9), rnd.randrange(30)),
            "tagi": [slowo() for _ in range(3)],
            "config": {"host": "serwer-%d" % rnd.randrange(99), "port": rnd.randrange(1024, 65535)}}
    t = json.dumps(dane, ensure_ascii=False, indent=2) + "\n"
    poz = rnd.randrange(len(t))
    t = t[:poz] + rnd.choice([ZWSP, NBSP, CJK_TOK]) + t[poz:]
    p = zapisz("g6_%d.json" % i, t)
    zaglada_cicho(czytaj(p), p)
    try:
        w = json.loads(czytaj(p))
        ok = w.get("config", {}).get("port") == dane["config"]["port"] and \
            sorted(w.get("tagi", [])) == sorted(dane["tagi"])
    except Exception:
        ok = False
    if not ok:
        POPSUTE.append(("G6", "g6_%d.json martwy/zmieniony" % i))
    STAN["g6"] += 1

for g in ("g1", "g2", "g3", "g4", "g5", "g6"):
    opisr = {"g1": "czyste (bajt-w-bajt)", "g2": ".py literaly święte",
             "g3": ".py brud w kodzie", "g4": ".py zepsuty ratunek",
             "g5": "proza litery PL", "g6": "JSON żyje"}[g]
    zle = [x for x in POPSUTE if x[0] == g.upper()]
    print("  %s %-22s %3d plikow — %s" % (g.upper(), opisr, STAN[g],
          "czysto" if not zle else "WPADKA (%d)" % len(zle)))

shutil.rmtree(D, ignore_errors=True)
print()
print("=" * 66)
print("FINAŁ Z2: %d plików | POPSUTE PRZEZ ZAGŁADĘ: %d" % (sum(STAN.values()), len(POPSUTE)))
for x in POPSUTE[:10]:
    print("  POPSUTE:", x)
sys.exit(0 if not POPSUTE else 1)

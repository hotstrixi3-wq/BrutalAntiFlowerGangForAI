"""TURNIEJ 3 NIE-PSUCIE KODU — PogromcaKwiatkow v8.0.2.
Generator plikow (seed z argv, inny co cykl pętli). Kontrakt --fix:
  G1 czyste .py   -> bajt-w-bajt identyczne
  G2 brudne ale kompilowalne .py -> NADAL kompilowalne + idempotentne
  G3 zepsute .py  -> po fixie kompilowalne (lub nieodwracalnie zepsute:
                     literaly zachowane), nigdy gorzej
  G4 czyste .md/.txt -> bajt-w-bajt identyczne
  G5 brudne .md/.txt -> niewidzialne znikaja, litery nietkniete, idempotentne
Exit 0 = zaliczony."""
import contextlib
import importlib.util
import io
import os
import random
import shutil
import sys
import tempfile
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PK_PATH = os.path.join(HERE, "pogromca-kwiatkow-main", "PogromcaKwiatkow.py")
spec = importlib.util.spec_from_file_location("pk", PK_PATH)
pk = importlib.util.module_from_spec(spec)
sys.modules["pk"] = pk
spec.loader.exec_module(pk)

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260902
rnd = random.Random(SEED)
print("TURNIEJ 3 NIE-PSUCIE — PogromcaKwiatkow v8.0.2 (seed %d)" % SEED)
print("=" * 66)

PL = ["kasza", "serwer", "restart", "harmonogram", "klaster", "wiadomosc",
      "poranek", "rzodkiewka", "zdjecie", "cisza", "obrona", "piorun",
      "zespol", "zadanie", "wdrozenie", "wydajnosc", "bezpieczenstwo"]
EN = ["server", "restart", "message", "cluster", "deploy", "update", "engine"]
OGONKI = "ąćęłńóśźż"


def slowo():
    w = rnd.choice(PL + EN)
    if rnd.random() < 0.5:
        i = rnd.randrange(len(w))
        w = w[:i] + rnd.choice(OGONKI) + w[i + 1:]
    return w


def opis():
    return " ".join(slowo() for _ in range(rnd.randrange(4, 10))).capitalize()


def gen_py(idx):
    linie = [
        "# -*- coding: utf-8 -*-",
        "import os",
        "import sys",
        '"""Modul %d: %s."""' % (idx, opis()),
        "",
        "STALA = %d" % rnd.randrange(1000),
        'TEKST = "%s"' % opis(),
        "DANE = {%r: [%d, %d], %r: \"%s\"}" % (slowo(), rnd.randrange(50),
                                               rnd.randrange(50), slowo(), opis()),
        "",
        "def funkcja_%d(a, b=%d):" % (idx, rnd.randrange(10)),
        "    # komentarz: %s" % opis(),
        "    wynik = a + b * STALA",
        "    if wynik > %d:" % rnd.randrange(100, 200),
        "        return TEKST.upper()",
        "    return wynik - %d" % rnd.randrange(10),
        "",
        "class Klasa%d:" % idx,
        "    '''Docstring: %s.'''" % opis(),
        "",
        "    def __init__(self, w=0):",
        "        self._w = w",
        "",
        "    @property",
        "    def wartosc(self):",
        "        return self._w",
        "",
        "def main():",
        "    k = Klasa%d(%d)" % (idx, rnd.randrange(9)),
        '    print(f"wynik={funkcja_%d(k.wartosc)} ver={sys.version_info[0]}")' % idx,
        "    return os.name",
        "",
        'if __name__ == "__main__":',
        "    main()",
        "",
    ]
    return "\n".join(linie)


def gen_md():
    par = []
    for _ in range(rnd.randrange(2, 6)):
        par.append(opis() + rnd.choice([".", "!"]) )
        if rnd.random() < 0.4:
            par.append("— " + opis() + ": " + slowo() + ", " + slowo() + ".")
    return "\n\n".join(par) + "\n"


D = tempfile.mkdtemp(prefix="t3_")
POPSUTE, STAN = [], {"g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0}


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


def napraw_cicho(t, p):
    with contextlib.redirect_stdout(io.StringIO()):
        return pk.napraw(t, p)


LS, PS, NEL, VT = chr(0x2028), chr(0x2029), chr(0x85), chr(0x0B)
ZWSP, ZWNJ, NBSP, NNBSP = chr(0x200B), chr(0x200C), chr(0x00A0), chr(0x202F)

# --- G1: czyste .py -> bajt w bajt -------------------------------------------
for i in range(60):
    t = gen_py(i)
    assert kompiluje(t, "g%d.py" % i), "generator zepsul plik %d" % i
    p = zapisz("g1_%d.py" % i, t)
    napraw_cicho(czytaj(p), p)
    if czytaj(p) != t:
        POPSUTE.append(("G1", "g1_%d.py zmieniony" % i))
    STAN["g1"] += 1
print("  G1 czyste .py (bajt-w-bajt)      %d plikow — %s" % (
    STAN["g1"], "czysto" if not POPSUTE else "WPADKA"))

# --- G2: brudne ale kompilowalne .py -> nadal kompilowalne --------------------
for i in range(30):
    t = gen_py(100 + i)
    linie = t.split("\n")
    for _ in range(rnd.randrange(1, 4)):
        j = rnd.randrange(len(linie))
        brud = rnd.choice([ZWSP, ZWNJ, NBSP, NNBSP])
        poz = rnd.randrange(len(linie[j]) + 1)
        linie[j] = linie[j][:poz] + brud + linie[j][poz:]
    t2 = "\n".join(linie)
    if not kompiluje(t2, "x.py"):      # wstrzykniecie trafilo w kod? sprobuj innym razem
        t2 = t
    p = zapisz("g2_%d.py" % i, t2)
    napraw_cicho(czytaj(p), p)
    w1 = czytaj(p)
    if not kompiluje(w1, p):
        POPSUTE.append(("G2", "g2_%d.py przestal kompilowac" % i))
    if sorted(c for c in w1 if c.isalpha()) != sorted(c for c in t2 if c.isalpha()):
        POPSUTE.append(("G2", "g2_%d.py litery zmienione" % i))
    napraw_cicho(w1, p)
    if czytaj(p) != w1:
        POPSUTE.append(("G2", "g2_%d.py nie-idempotentny" % i))
    STAN["g2"] += 1
print("  G2 brudne .py (kompiluja dalej)  %d plikow — %s" % (
    STAN["g2"], "czysto" if not [x for x in POPSUTE if x[0] == "G2"] else "WPADKA"))

# --- G3: zepsute .py -> fix albo niewzgledna ostroznosc -----------------------
for i in range(20):
    t = gen_py(200 + i)
    sep = rnd.choice([LS, PS, NEL, VT])
    linie = [l for l in t.split("\n") if l.strip()]
    assert len(linie) >= 10
    # zepsuj: czesc nowych linii zamien na separator-lamacz
    for j in range(2, len(linie) - 1, 3):
        linie[j] = linie[j] + sep
    zepsute = "\n".join(linie) + "\n"
    if rnd.random() < 0.5 and 'TEKST = "' in zepsute:
        zepsute = zepsute.replace('TEKST = "', 'TEKST = "' + LS, 1)  # LS w literale
        mial_ls = True
    else:
        mial_ls = False
    assert not kompiluje(zepsute, "x.py"), "generator nie zepsul (%d)" % i
    p = zapisz("g3_%d.py" % i, zepsute)
    napraw_cicho(czytaj(p), p)
    w = czytaj(p)
    if mial_ls and LS not in w:
        POPSUTE.append(("G3", "g3_%d.py LS z literalu usuniety" % i))
    if not kompiluje(w, p) and kompiluje(zepsute, p):
        POPSUTE.append(("G3", "g3_%d.py zepsuty przez fix" % i))
    napraw_cicho(w, p)
    if czytaj(p) != w:
        POPSUTE.append(("G3", "g3_%d.py nie-idempotentny" % i))
    STAN["g3"] += 1
naprawione = 0
for i in range(20):
    p = os.path.join(D, "g3_%d.py" % i)
    if os.path.exists(p) and kompiluje(czytaj(p), p):
        naprawione += 1
print("  G3 zepsute .py (fix/ostroznosc)  %d plikow (naprawiono %d) — %s" % (
    STAN["g3"], naprawione,
    "czysto" if not [x for x in POPSUTE if x[0] == "G3"] else "WPADKA"))

# --- G4: czyste .md/.txt -> bajt w bajt ----------------------------------------
for i in range(60):
    t = gen_md()
    p = zapisz("g4_%d.%s" % (i, "md" if i % 2 else "txt"), t)
    napraw_cicho(czytaj(p), p)
    if czytaj(p) != t:
        POPSUTE.append(("G4", "g4_%d zmieniony" % i))
    STAN["g4"] += 1
print("  G4 czyste .md/.txt (bajt-w-bajt) %d plikow — %s" % (
    STAN["g4"], "czysto" if not [x for x in POPSUTE if x[0] == "G4"] else "WPADKA"))

# --- G5: brudne .md/.txt -> czyste, litery nietkniete ---------------------------
for i in range(20):
    t = gen_md()
    linie = t.split("\n")
    for _ in range(rnd.randrange(2, 6)):
        j = rnd.randrange(len(linie))
        brud = rnd.choice([ZWSP, ZWNJ, NBSP, NNBSP, LS, PS, NEL])
        poz = rnd.randrange(len(linie[j]) + 1)
        linie[j] = linie[j][:poz] + brud + linie[j][poz:]
    t2 = "\n".join(linie)
    p = zapisz("g5_%d.md" % i, t2)
    napraw_cicho(czytaj(p), p)
    w1 = czytaj(p)
    for brud in (ZWSP, ZWNJ, NBSP, NNBSP, LS, PS, NEL):
        if brud in w1:
            POPSUTE.append(("G5", "g5_%d.md zostawil brud U+%04X" % (i, ord(brud))))
    if sorted(c for c in w1 if c.isalpha()) != sorted(c for c in t2 if c.isalpha()):
        POPSUTE.append(("G5", "g5_%d.md litery zmienione" % i))
    napraw_cicho(w1, p)
    if czytaj(p) != w1:
        POPSUTE.append(("G5", "g5_%d.md nie-idempotentny" % i))
    STAN["g5"] += 1
print("  G5 brudne .md/.txt (sprzatnienie) %d plikow — %s" % (
    STAN["g5"], "czysto" if not [x for x in POPSUTE if x[0] == "G5"] else "WPADKA"))

shutil.rmtree(D, ignore_errors=True)
print()
print("=" * 66)
print("FINAŁ T3: %d plików | POPSUTE PRZEZ --fix: %d" % (
    sum(STAN.values()), len(POPSUTE)))
for x in POPSUTE[:10]:
    print("  POPSUTE:", x)
sys.exit(0 if not POPSUTE else 1)

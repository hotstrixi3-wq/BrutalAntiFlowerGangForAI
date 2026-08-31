"""TURNIEJ 2 SPRAWDZAJĄCY (polowanie na błędy) — PogromcaKwiatkow v8.0.2.
Seed z argv (pętla podaje inny co cykl) — wektory losowe, świeże co cykl.
Klasy oczekiwań zgodne z udokumentowaną polityką (dekompozycja != kwiatek,
Cn = polityka, Co/Cs/Cf/Cc = brud, Nd spoza ASCII = brud w tekście).
Exit 0 = zaliczony, 1 = wpadka."""
import importlib.util
import os
import random
import subprocess
import sys
import tempfile
import time
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PK_PATH = os.path.join(HERE, "pogromca-kwiatkow-main", "PogromcaKwiatkow.py")
spec = importlib.util.spec_from_file_location("pk", PK_PATH)
pk = importlib.util.module_from_spec(spec)
sys.modules["pk"] = pk
spec.loader.exec_module(pk)
BLOK_RANGES = [(lo, hi) for lo, hi, _nm in pk.BLOKOWANE]

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260901
rnd = random.Random(SEED)
print("TURNIEJ 2 SPRAWDZAJĄCY — PogromcaKwiatkow v8.0.2 (seed %d)" % SEED)
print("=" * 66)


def zablokowany(cp):
    return any(lo <= cp <= hi for lo, hi in BLOK_RANGES)


def losuj_kat(kat, n, lo=0x20, hi=0x110000):
    out, guard = [], 0
    while len(out) < n and guard < 400000:
        guard += 1
        cp = rnd.randrange(lo, hi)
        if kat == "Cs":
            cp = rnd.randrange(0xD800, 0xE000)
        if unicodedata.category(chr(cp)) == kat:
            if cp not in out:
                out.append(cp)
    return out


FN, FP, SZUM, POL, CRASH = [], [], [], [], []
N = 0


def sprawdz(vid, tekst, exp):
    global N
    N += 1
    try:
        b, u = pk.analizuj(tekst)
    except Exception as e:
        CRASH.append((vid, ascii(str(e))[:90]))
        return
    w = "BLAD" if b else ("UWAGA" if u else "OK")
    if exp == "BLAD" and not b:
        FN.append((vid, w))
    elif exp == "OK" and b:
        FP.append((vid, "BLAD"))
    elif exp == "OK-SCISLE":
        if b:
            FP.append((vid, "BLAD"))
        elif u:
            SZUM.append((vid, "UWAGA"))
    elif exp == "POLITYKA" and w == "OK":
        POL.append((vid, "OK"))
    elif exp == "NIE-BLAD" and b:
        FP.append((vid, "BLAD-na-czystym"))


def runda(nazwa, ile, fn):
    n0 = N
    fn()
    print("  %-24s %4d wektorow — %s" % (nazwa, N - n0,
          "czysto" if not (FN or FP or SZUM or POL or CRASH) else "WPADKA"))


# --- S1 LOSOWIEC: losowe probki Unicode w klasach o znanej polityce ----------
def s1():
    for cp in losuj_kat("Cf", 60):
        sprawdz("s1-cf:%05X" % cp, "slowo" + chr(cp) + "drugie", "BLAD")
    cc = [c for c in losuj_kat("Cc", 40) if c not in (0x09, 0x0A, 0x0D)]
    for cp in cc:
        sprawdz("s1-cc:%04X" % cp, "slowo" + chr(cp) + "drugie", "BLAD")
    for cp in losuj_kat("Cs", 30):
        sprawdz("s1-cs:%05X" % cp, "slowo" + chr(cp) + "drugie", "BLAD")
    for cp in losuj_kat("Co", 40):
        sprawdz("s1-co:%05X" % cp, "slowo" + chr(cp) + "drugie", "BLAD")
    for cp in losuj_kat("Cn", 60):
        sprawdz("s1-cn:%05X" % cp, "slowo" + chr(cp) + "drugie", "POLITYKA")
    nd = [c for c in losuj_kat("Nd", 60) if c > 0x9F]
    for cp in nd:
        sprawdz("s1-nd:%05X" % cp, "wersja 1." + chr(cp) + ".2", "BLAD")
    mn = [c for c in range(0x300, 0x370)
          if unicodedata.category(chr(c)) == "Mn"]
    for _ in range(40):
        stack = "".join(chr(rnd.choice(mn)) for _ in range(3))
        sprawdz("s1-mn3", "slowo" + stack + "drugie", "BLAD")
    blk, guard = [], 0
    while len(blk) < 60 and guard < 400000:
        guard += 1
        cp = rnd.randrange(0x80, 0x110000)
        c = chr(cp)
        if zablokowany(cp) and unicodedata.category(c).startswith("L") and c not in pk.TYPO:
            blk.append(cp)
    for cp in blk:
        sprawdz("s1-blk:%05X" % cp, "s" + chr(cp) + "erwer", "BLAD")
    so, guard = [], 0
    while len(so) < 30 and guard < 400000:
        guard += 1
        cp = rnd.randrange(0x1F000, 0x110000)
        c = chr(cp)
        if unicodedata.category(c) in ("So", "Sk") and c not in pk.TYPO:
            so.append(cp)
    for cp in so:
        sprawdz("s1-so:%05X" % cp, "status " + chr(cp), "BLAD")


runda("S1 LOSOWIEC", 0, s1)

# --- S2 FALSZ: czyste zdania PL/EN bez prawa do BLAD -------------------------
PL = ["kasza", "serwer", "restart", "harmonogram", "klaster", "ping", "mod",
      "wiadomosc", "poranek", "kawa", "rzodkiewka", "zdjecie", "cisza",
      "obrona", "sprawa", "glos", "piorun", "wrobl", "zimno", "lato",
      "zespol", "zadanie", "wdrozenie", "test", "wydajnosc", "bezpieczenstwo"]
EN = ["server", "restart", "message", "cluster", "deploy", "update",
      "backup", "monitor", "alert", "report", "engine", "worker", "queue",
      "release", "patch", "ticket", "status", "health", "latency", "shard"]
PL_DIak = "ąćęłńóśźż"
BAS_PUNCT = list(",.!?-:;()0123456789")
TYPO = ["—", "„", "”", "…", "%", "§", "€"]


def zdanie(diakrytyczne=True, typografia=False):
    slowa = []
    for _ in range(rnd.randrange(6, 13)):
        if diakrytyczne and rnd.random() < 0.4:
            w = rnd.choice(PL)
            i = rnd.randrange(len(w))
            w = w[:i] + rnd.choice(PL_DIak) + w[i + 1:]
        else:
            w = rnd.choice(PL + EN)
        slowa.append(w)
    s = " ".join(slowa)
    s = s[0].upper() + s[1:]
    if typografia:
        s += " " + rnd.choice(TYPO)
    else:
        s += rnd.choice([".", "!", "?", "."])
    return s


def s2():
    for i in range(150):
        sprawdz("s2-czyste:%d" % i, zdanie(rnd.random() < 0.7, False),
               "OK-SCISLE")
    for i in range(100):
        sprawdz("s2-typo:%d" % i, zdanie(True, True), "NIE-BLAD")


runda("S2 FALSZ", 0, s2)

# --- S3 MUTANT: czyste zdanie + wstrzykniety brud ----------------------------
def s3():
    baza = [zdanie(True, False) for _ in range(10)]
    cf = losuj_kat("Cf", 20) or [0x200B]
    for i in range(50):
        t = rnd.choice(baza)
        p = rnd.randrange(len(t))
        cp = rnd.choice(cf)
        sprawdz("s3-cf:%d" % i, t[:p] + chr(cp) + t[p:], "BLAD")
    for i in range(50):
        t = rnd.choice(baza)
        p = rnd.randrange(len(t))
        cp = rnd.randrange(0xE000, 0xF900)
        sprawdz("s3-pua:%d" % i, t[:p] + chr(cp) + t[p:], "BLAD")
    for i in range(50):
        t = rnd.choice(baza)
        p = rnd.randrange(len(t))
        cp = rnd.choice([0x2028, 0x2029, 0x85, 0x0B, 0x1C])
        sprawdz("s3-lamacz:%d" % i, t[:p] + chr(cp) + t[p:], "BLAD")
    cn = losuj_kat("Cn", 20) or [0x378]
    for i in range(50):
        t = rnd.choice(baza)
        p = rnd.randrange(len(t))
        cp = rnd.choice(cn)
        sprawdz("s3-cn:%d" % i, t[:p] + chr(cp) + t[p:], "POLITYKA")


runda("S3 MUTANT", 0, s3)

# --- S4 NIEMOC-NORM: dekompozycja to nie kwiatek ------------------------------
def s4():
    for i in range(50):
        t = zdanie(True, rnd.random() < 0.5)
        sprawdz("s4-nfd:%d" % i, unicodedata.normalize("NFD", t), "NIE-BLAD")
        sprawdz("s4-nfc-powrot:%d" % i,
                unicodedata.normalize("NFC", unicodedata.normalize("NFD", t)),
                "NIE-BLAD")
        sprawdz("s4-nfkc:%d" % i, unicodedata.normalize("NFKC", t), "NIE-BLAD")


runda("S4 NIEMOC-NORM", 0, s4)

# --- S5 KONSOLA: proces CLI, kody wyjscia, brak traceback --------------------
def s5():
    global N
    D = tempfile.mkdtemp(prefix="t2cli_")
    def z(n, t):
        p = os.path.join(D, n)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        return p
    czysty = z("czysty.txt", zdanie(True, False) + "\n")
    brudny = z("brudny.txt", "tekst " + chr(0xE123) + " koniec\n")
    pusty = z("pusty.txt", "")
    bom = z("bom.txt", "﻿")
    bms = z("bomstart.txt", "﻿tekst pl\n")
    LS = chr(0x2028)
    brudpy = z("brudny.py", "import os" + LS + "x = 1" + LS)
    def run(args):
        return subprocess.run([sys.executable, PK_PATH] + args,
                              capture_output=True, text=True, timeout=60,
                              cwd=D)
    przypadki = [
        ("czysty -> 0", [czysty], {0}),
        ("brudny -> 1", [brudny], {1}),
        ("pusty -> 0", [pusty], {0}),
        ("bom-only -> brak crash", [bom], {0, 1}),
        ("bom+tekst -> brak crash", [bms], {0, 1}),
        ("brudny .py -> 1", [brudpy], {1}),
        ("nieistniejacy -> brak crash", [os.path.join(D, "x.txt")], {1, 2}),
        ("--selftest -> 0", ["--selftest"], {0}),
        ("bez argumentow -> brak crash", [], {0, 1, 2}),
    ]
    for nazwa, args, kody in przypadki:
        r = run(args)
        N += 1
        ok = r.returncode in kody and "Traceback" not in (r.stdout + r.stderr)
        if not ok:
            FN.append(("s5-cli:" + nazwa, "exit=%d" % r.returncode))
        print("    cli: %-28s exit=%d %s" % (nazwa, r.returncode,
              "OK" if ok else "WPADKA"))
    # --fix na txt: ZWSP (niewidzialny) znika; PUA ZOSTAJE (polityka:
    # NIEWIDZ nie zawiera PUA - kasowanie to decyzja czlowieka)
    zwsp = z("zwsp.txt", "tekst " + chr(0x200B) + " koniec\n")
    r = run(["--fix", zwsp])
    N += 1
    t = open(zwsp, encoding="utf-8").read()
    ok = chr(0x200B) not in t and "tekst" in t and r.returncode in (0, 1)
    if not ok:
        FN.append(("s5-fix:zwsp", "exit=%d" % r.returncode))
    r = run(["--fix", brudny])
    N += 1
    t = open(brudny, encoding="utf-8").read()
    ok = chr(0xE123) in t and "tekst" in t
    if not ok:
        FN.append(("s5-fix:pua-zostaje", "skasowal PUA"))
    # --fix na czystym: bajt-w-bajt
    N += 1
    przed = open(czysty, "rb").read()
    r = run(["--fix", czysty])
    ok = open(czysty, "rb").read() == przed
    if not ok:
        FN.append(("s5-fix:czysty", "zmienil czysty"))
    # --fix na zepsutym .py: kompiluje po
    N += 1
    r = run(["--fix", brudpy])
    try:
        compile(open(brudpy, encoding="utf-8").read(), brudpy, "exec")
        ok = True
    except SyntaxError:
        ok = False
    if not ok:
        FN.append(("s5-fix:py", "nie kompiluje po fix"))
    import shutil
    shutil.rmtree(D, ignore_errors=True)


runda("S5 KONSOLA", 0, s5)

# --- S6 SZYBKOSC: 1 MB czystego tekstu ----------------------------------------
def s6():
    tekst = ""
    i = 0
    while len(tekst.encode("utf-8")) < (1 << 20):
        tekst += "%d %s\n" % (i, " ".join(zdanie(True, False) for _ in range(8)))
        i += 1
    global N
    N += 1
    t0 = time.perf_counter()
    pk.analizuj(tekst)
    dt = time.perf_counter() - t0
    print("    1 MB w %.2f s (%.2f MB/s)" % (dt, 1 / dt if dt else 0))
    if dt > 20:
        FN.append(("s6-szybkosc", "%.1f s" % dt))


runda("S6 SZYBKOSC", 0, s6)

print()
print("=" * 66)
print("FINAŁ T2: %d wektorów | FN %d | FP %d | SZUM %d | POLITYKA-ESC %d | CRASH %d"
      % (N, len(FN), len(FP), len(SZUM), len(POL), len(CRASH)))
for nazwa, dane in (("FN", FN), ("FP", FP), ("SZUM", SZUM),
                    ("POL", POL), ("CRASH", CRASH)):
    if dane:
        print("  %s: %s" % (nazwa, dane[:8]))
sys.exit(0 if not (FN or FP or SZUM or POL or CRASH) else 1)

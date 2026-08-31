# -*- coding: utf-8 -*-
"""TURNIEJ NIEZALEZNY — PogromcaKwiatkow v8.0.2 (po bugfixu F4).
Red-team/blue-team na zasadach autora (FN/FP/SZUM), ale w calosci
niezalezne wektory, generowane PROGRAMOWO, deterministycznie.

Rundy:
 R1  AZBUKA       cyrylica (wszystkie odmiany) wstrzykiwana w polskie slowa
 R2  NIEWIDKA     PELNA enumeracja Cc+Cf Unicode x 3 konteksty
 R3  MIESZANIEC   homoglify cyr/greka w tokenach ASCII (+tag HOMOGLIF)
 R3b MIESZANIEC-L homoglify lacińskie (polityka: >=UWAGA)
 R4  PRACZ        singletony NFC (4 twarde) + 2 miekkie + NFD legalne
 R5  ZALGO        znaki skladajace (pelny blok Mn 0300-036F + probki blokow)
 R6  TROJAN       bidi/Trojan Source (RLO/PDF, izolaty, RLM w URL)
 R7  LINIOMISTRZ  8 lamaczy linii x 3 konteksty
 R8  CYFRATA      PELNA enumeracja Nd poza ASCII
 R9  GRAFOMAN     piktogramy >=1F000 (BLAD) + symbole pasma 2000-27BF (polityka)
 R10 STEGO        PUA (3 plany) + TAG + surogaty (BLAD), nieprzypisane (polityka)
 R11 BIALE CHALATY czysty korpus projektowy PL/EN (zero BLAD, zero UWAGA)
 R12 KACZOR       dziwactwa brzegowe
 R13 OBIETNICA    --fix: litery nietknięte / idempotencja / kompilowalnosc
"""
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

BLOK_RANGES = [(lo, hi) for lo, hi, _nm in pk.BLOKOWANE]


def C(*cps):
    return "".join(chr(c) for c in cps)


def zablokowany(cp):
    return any(lo <= cp <= hi for lo, hi in BLOK_RANGES)


WYNIKI = []


def run_runda(nazwa, wektory):
    """wektory: (id, tekst, oczekiwane) — BLAD / OK / OK-SCISLE / POLITYKA."""
    n = fn = 0
    fns, fps, szumy, poles, crashy = [], [], [], [], []
    homoglif_tagi = 0
    homoglif_szanse = 0
    for vid, t, exp in wektory:
        n += 1
        try:
            b, u = pk.analizuj(t)
            w = "BLAD" if b else ("UWAGA" if u else "OK")
        except Exception as e:
            crashy.append((vid, repr(e)[:90]))
            continue
        if exp == "BLAD":
            homoglif_szanse += 1
            txt = "".join(k for trafy in (b or {}).values() for _l, _z, k in trafy)
            if "[HOMOGLIF" in txt:
                homoglif_tagi += 1
            if not b:
                fns.append((vid, w))
        elif exp == "OK":
            if b:
                fps.append((vid, "BLAD"))
        elif exp == "OK-SCISLE":
            if b:
                fps.append((vid, "BLAD"))
            elif u:
                szumy.append((vid, "UWAGA"))
        elif exp == "POLITYKA":  # wymagane >= UWAGA; ucieczka do OK = luka pol.
            if w == "OK":
                poles.append((vid, "OK"))
        elif exp == "MIEKKI":    # kompozycja NFC do litery: BLAD niedopuszczalny
            if b:
                fns.append((vid, "BLAD-niekonsystentnie"))
    WYNIKI.append(dict(runda=nazwa, n=n, fn=fns, fp=fps, szum=szumy,
                       pol=poles, crash=crashy,
                       hom=(homoglif_tagi, homoglif_szanse)))
    tag = ""
    if fns:
        tag += " FN=%d" % len(fns)
    if fps:
        tag += " FP=%d" % len(fps)
    if szumy:
        tag += " SZUM=%d" % len(szumy)
    if poles:
        tag += " POL-ESC=%d" % len(poles)
    if crashy:
        tag += " CRASH=%d" % len(crashy)
    print("  %-14s %5d wektorow —%s" % (nazwa, n, tag or " czysto"), flush=True)
    return fns, fps, szumy, poles, crashy


# ---------------------------------------------------------------------------
R = random.Random(20260831)

print("TURNIEJ NIEZALEZNY — PogromcaKwiatkow v8.0.2 (seed 20260831)")
print("=" * 66)

# --- R1 AZBUKA --------------------------------------------------------------
SLOWA = ["serwer", "mapa", "restart", "gracze", "logowania", "zapis", "swiat",
         "klaster", "Ragnarok", "Genesis", "wyspa", "jaskinia", "dinozaury"]
litery_cyr = list(range(0x410, 0x450)) + list(range(0x400, 0x410)) + \
    [0x456, 0x457, 0x454, 0x490, 0x491, 0x402, 0x452, 0x408, 0x458,
     0x409, 0x459, 0x40A, 0x45A, 0x40B, 0x45B] + \
    list(range(0x1C80, 0x1C89)) + [0xA640, 0xA641, 0xA642, 0xA643] + \
    list(range(0x2DE0, 0x2DF0))
wek = []
i = 0
for cp in litery_cyr:
    slowo = R.choice(SLOWA)
    poz = R.randrange(len(slowo) + 1)
    wek.append(("azbuka:%04X" % cp, slowo[:poz] + chr(cp) + slowo[poz:], "BLAD"))
for cp in litery_cyr[::7]:
    wek.append(("azbuka-solo:%04X" % cp, "slowo " + chr(cp), "BLAD"))
    wek.append(("azbuka-url:%04X" % cp, "https://ex.com/" + chr(cp) + "dmin", "BLAD"))
run_runda("R1 AZBUKA", wek)

# --- R2 NIEWIDKA: pelna enumeracja Cc+Cf ------------------------------------
cc_cf = []
for cp in range(0x110000):
    if cp in (0x09, 0x0A, 0x0D):          # \t \n \r legalne
        continue
    cat = unicodedata.category(chr(cp))
    if cat in ("Cc", "Cf"):
        cc_cf.append(cp)
wek = []
for cp in cc_cf:
    wek.append(("cccf-start:%05X" % cp, chr(cp) + "tekst", "BLAD"))
    wek.append(("cccf-mid:%05X" % cp, "slowo" + chr(cp) + "drugie", "BLAD"))
    wek.append(("cccf-end:%05X" % cp, "tekst" + chr(cp), "BLAD"))
run_runda("R2 NIEWIDKA", wek)

# --- R3 MIESZANIEC (cyr/greka w tokenach) + R3b lacińskie (polityka) --------
MAPA_BLAD = {
    "a": [0x0430, 0x03B1], "c": [0x0441, 0x03F2], "e": [0x0435, 0x03B5],
    "o": [0x043E, 0x03BF], "p": [0x0440, 0x03C1], "x": [0x0445, 0x03C7],
    "y": [0x0443], "i": [0x0456, 0x03B9], "j": [0x0458], "s": [0x0455],
    "A": [0x0410], "B": [0x0412], "C": [0x0421], "E": [0x0415], "H": [0x041D],
    "K": [0x041A, 0x039A], "M": [0x041C], "O": [0x041E, 0x039F],
    "P": [0x0420, 0x03A1], "T": [0x0422, 0x03A4], "X": [0x0425, 0x03A7],
}
MAPA_POL = {"s": [0x017F], "i": [0x0131], "o": [0x00F8], "g": [0x0121],
            "o2": [0x014D]}
IDY = ["admin", "system", "login", "password", "root", "config", "server",
       "user_token", "ARK_Server", "exitCode", "backup"]
wek, wekpol = [], []
for idy in IDY:
    for pos, lit in enumerate(idy):
        for cp in MAPA_BLAD.get(lit, []):
            wek.append(("hom:%s:%d:%04X" % (idy, pos, cp),
                        idy[:pos] + chr(cp) + idy[pos + 1:], "BLAD"))
for idy in ("sql", "login", "system", "roots"):
    mapa = MAPA_POL.get(idy[0]) or MAPA_POL.get(idy[1] + "2") or []
    for cp in ({idy[0]: MAPA_POL.get(idy[0], []), "o": [0x00F8, 0x014D],
                "s": [0x017F], "i": [0x0131], "g": [0x0121]}).get(
                    idy[0] if idy[0] in "sigo" else idy[1] if idy[1] in "sigo" else "o", []):
        poz = 0 if idy[0] in "sigo" else 1
        wekpol.append(("homl:%s:%04X" % (idy, cp),
                       idy[:poz] + chr(cp) + idy[poz + 1:], "POLITYKA"))
run_runda("R3 MIESZANIEC", wek)
run_runda("R3b MIESZANIEC-L", wekpol)

# --- R4 PRACZ ----------------------------------------------------------------
wek = [
    ("pranie:212A", "ARK-" + C(0x212A) + "-99", "BLAD"),
    ("pranie:037E", "a" + C(0x037E) + "b", "BLAD"),
    ("pranie:0387", "a" + C(0x0387) + "b", "BLAD"),
    ("pranie:1FEF", "a" + C(0x1FEF) + "b", "BLAD"),
    ("pranie:1FFD", "a" + C(0x1FFD) + "b", "POLITYKA"),
    ("pranie:212B", "30 " + C(0x212B), "POLITYKA"),
    ("nfd:ogonki", unicodedata.normalize("NFD", "Zażółć gęślą"), "OK-SCISLE"),
    ("nfd:source", unicodedata.normalize("NFD", "źródło świata"), "OK-SCISLE"),
]
run_runda("R4 PRACZ", wek)

# --- R5 ZALGO ----------------------------------------------------------------
wek = []
for cp in range(0x300, 0x370):
    if unicodedata.category(chr(cp)) == "Mn":
        # polityka narzedzia (fuzz C): dekompozycja != kwiatek — jesli
        # NFC(a+mark) komponuje do litery Latin-1/Ext-A (<=0x17F), czysto;
        # kompozycja do litery WYZEJ (Ext-B+, np. ȧ ạ ǎ) = obce pismo -> BLAD
        n = unicodedata.normalize("NFC", "a" + chr(cp))
        exp = "MIEKKI" if (len(n) == 1 and ord(n) <= 0x17F) else "BLAD"
        wek.append(("mn:%04X" % cp, "a" + chr(cp) + "b", exp))
probki = list(range(0x591, 0x5C8)) + list(range(0x64B, 0x660)) + \
    list(range(0x93C, 0x93D)) + list(range(0x941, 0x949)) + \
    [0xE31, 0xE34, 0xE38, 0xE47, 0x3099, 0x309A, 0x488, 0x489] + \
    list(range(0x1DC0, 0x1DE0)) + list(range(0xFE20, 0xFE30)) + \
    list(range(0x20D0, 0x20F1))
for cp in probki:
    if unicodedata.category(chr(cp)) in ("Mn", "Me", "Mc"):
        wek.append(("mark:%04X" % cp, "slowo" + chr(cp) + "koniec", "BLAD"))
for _ in range(40):
    baza = R.choice("aeiou xy kwiat")
    stack = "".join(chr(R.choice(probki)) for _ in range(R.randint(3, 15)))
    wek.append(("zalgo-stack", baza + stack + baza, "BLAD"))
run_runda("R5 ZALGO", wek)

# --- R6 TROJAN ----------------------------------------------------------------
wek = [
    ("trojan:rlo-pdf", "if (access) " + C(0x202E) + " deny; " + C(0x202C), "BLAD"),
    ("trojan:rlo-comment", "# " + C(0x202E) + "} if (isAdmin) { " + C(0x202C), "BLAD"),
    ("trojan:lro", "text " + C(0x202D) + "reversed" + C(0x202C), "BLAD"),
    ("trojan:lri-pdi", "code " + C(0x2066) + "x" + C(0x2069) + " end", "BLAD"),
    ("trojan:rlI", "a" + C(0x2067) + "b" + C(0x2069), "BLAD"),
    ("trojan:fsi", "a" + C(0x2068) + "b", "BLAD"),
    ("trojan:rlm-url", "https://ex.com/" + C(0x200F) + "admin", "BLAD"),
    ("trojan:lrm-path", "C:" + C(0x200E) + "\\Users\\magus", "BLAD"),
    ("trojan:alm", "ala" + C(0x061C) + "ma", "BLAD"),
    ("trojan:klasyk", "/* " + C(0x202E) + " } (isAdmin) if { " + C(0x202C) +
     " */ access = true;", "BLAD"),
    ("trojan:anze", C(0x061A) + "tekst", "BLAD"),
    ("trojan:06DD", "a" + C(0x06DD) + "b", "BLAD"),
    ("trojan:070F", "a" + C(0x070F) + "b", "BLAD"),
    ("trojan:110BD", "a" + C(0x110BD) + "b", "BLAD"),
    ("trojan:1BCA0", "a" + C(0x1BCA0) + "b", "BLAD"),
    ("trojan:1D173", "a" + C(0x1D173) + "b", "BLAD"),
    ("trojan:E0001", "a" + C(0xE0001) + "b", "BLAD"),
]
run_runda("R6 TROJAN", wek)

# --- R7 LINIOMISTRZ -------------------------------------------------------------
LAM = [0x000B, 0x000C, 0x001C, 0x001D, 0x001E, 0x0085, 0x2028, 0x2029]
wek = []
for cp in LAM:
    wek.append(("lam:import:%04X" % cp, "import os" + chr(cp) + "import sys", "BLAD"))
    wek.append(("lam:proza:%04X" % cp, "pierwszy wiersz" + chr(cp) + "drugi", "BLAD"))
    wek.append(("lam:csv:%04X" % cp, "a,b" + chr(cp) + "c,d", "BLAD"))
run_runda("R7 LINIOMISTRZ", wek)

# --- R8 CYFRATA: pelna enumeracja Nd poza ASCII ---------------------------------
nd = [cp for cp in range(0x80, 0x110000)
      if unicodedata.category(chr(cp)) == "Nd"]
wek = [("nd:%05X" % cp, "wersja 1." + chr(cp) + ".2", "BLAD") for cp in nd]
run_runda("R8 CYFRATA", wek)

# --- R9 GRAFOMAN -----------------------------------------------------------------
wek, wekpol = [], []
cp = 0x1F000
while cp < 0x1FFFF:
    if not (0xD800 <= cp <= 0xDFFF):
        cat = unicodedata.category(chr(cp))
        if cat in ("So", "Sk"):
            if chr(cp) not in pk.TYPO:   # flagi 1F1E6-1F1FF legalne wg palety
                wek.append(("pik:%05X" % cp, "status " + chr(cp), "BLAD"))
        elif cat == "Cn":               # nieprzypisane -> polityka Cn
            wekpol.append(("pikCn:%05X" % cp, "status " + chr(cp), "POLITYKA"))
    cp += 61
sym_kat = {"Pd", "Po", "So", "Sk", "Sc", "Sm", "Pi", "Pf", "Ps", "Pe"}
for s_cp in range(0x2000, 0x27C0):
    chtxt = chr(s_cp)
    if chtxt in pk.TYPO or zablokowany(s_cp):
        continue
    if unicodedata.category(chtxt) in sym_kat:
        wekpol.append(("sym:%04X" % s_cp, "znak " + chtxt + " koniec", "POLITYKA"))
run_runda("R9 GRAFOMAN", wek)
run_runda("R9b GRAFOMAN-S", wekpol)

# --- R10 STEGO --------------------------------------------------------------------
wek, wekpol = [], []
for cp in range(0xE000, 0xF900, 17):
    wek.append(("pua:%05X" % cp, "a" + chr(cp) + "b", "BLAD"))
for cp in list(range(0xF0000, 0xF0020)) + list(range(0x100000, 0x100020)):
    wek.append(("pua15/16:%05X" % cp, "a" + chr(cp) + "b", "BLAD"))
for cp in range(0xE0020, 0xE0080, 3):
    wek.append(("tag:%05X" % cp, "a" + chr(cp) + "b", "BLAD"))
for cp in range(0xD800, 0xE000, 97):
    wek.append(("surogat:%05X" % cp, "a" + chr(cp) + "b", "BLAD"))
for cp in [0x2065] + list(range(0x2FE0, 0x2FF0)) + \
        [0xE01F7, 0xE0200, 0xE0FFF, 0x10FFFF, 0x10FFFE, 0x1FFFF, 0x3FFFF]:
    if unicodedata.category(chr(cp)) == "Cn" and not zablokowany(cp):
        wekpol.append(("cn:%05X" % cp, "a" + chr(cp) + "b", "POLITYKA"))
run_runda("R10 STEGO", wek)
run_runda("R10b STEGO-Cn", wekpol)

# --- R11 BIALE CHALATY (czysty korpus — zero BLAD, zero UWAGA) ---------------------
PL_SZ = ["Zażółć gęślą jaźń", "Łódź wyspa Źródło", "świat serwera zapisany",
         "Wlazł kotek na płotek", "ćma ćma ćma", "Święto Lipowa Wyspa"]
EN_SZ = ["The quick brown fox", "server is READY", "backup completed 100%",
         "players online: 42", "load average ~0.8"]
KOD = ["x = 12 * (3 + 4) / 5", "print('Zażółć — test')",
       "if x >= 1 and x <= 9: pass", "def f(): return 'ok'  # komentarz"]
URL = ["https://example.com/path?q=1&r=2", "user@mail.com", "C:\\ASAonly\\backup"]
TYPO_LINIA = ["┌─→ └─┐ │ ≤ ≥ ≈ ≠ ± × ° § € — … „ ” • ✅ ❌ ✓ ✔ ✕ ● ○ ◀ ▶",
              "strefa: 🇵🇱 🇬🇧 | status: ✅ | m² ³ ¹ µs ™ £ ½ ¼ ¾ ⌘⇧"]
wek = []
for i in range(800):
    rodz = R.random()
    if rodz < 0.30:
        t = R.choice(PL_SZ) + " " + R.choice(["—", "…", "•"]) + " " + R.choice(PL_SZ).lower()
    elif rodz < 0.55:
        t = R.choice(EN_SZ) + " " + R.choice(["—", "…"]) + " nr " + str(R.randint(1, 999))
    elif rodz < 0.70:
        t = R.choice(KOD)
    elif rodz < 0.80:
        t = R.choice(URL)
    elif rodz < 0.90:
        t = R.choice(TYPO_LINIA)
    else:
        t = "kolumna\twartość\t" + str(R.randint(0, 99)) + "\t" + R.choice(PL_SZ)
    wek.append(("bialy:%04d" % i, t, "OK-SCISLE"))
run_runda("R11 BIALE", wek)

# --- R12 KACZOR ---------------------------------------------------------------------
wek = [
    ("kaczor:pusty", "", "OK-SCISLE"),
    ("kaczor:sam newline", "\n", "OK-SCISLE"),
    ("kaczor:50x newline", "\n" * 50, "OK-SCISLE"),
    ("kaczor:jeden znak", "a", "OK-SCISLE"),
    ("kaczor:paleta solo", "—", "OK-SCISLE"),
    ("kaczor:ogonek solo", "ą", "OK-SCISLE"),
    ("kaczor:crlf", "wiersz\r\ndrugi\r\n", "OK-SCISLE"),
    ("kaczor:same niewidzialne", C(0x200B, 0x200C, 0x200D), "BLAD"),
    ("kaczor: sam NUL", C(0x0000), "BLAD"),
    ("kaczor: sam BOM", C(0xFEFF), "BLAD"),
    ("kaczor:max cp", C(0x10FFFF), "POLITYKA"),
    ("kaczor:dlugi ascii", "a" * 10000, "OK-SCISLE"),
    ("kaczor:tysiac ogonkow", "ą" * 1000, "OK-SCISLE"),
    ("kaczor:mieszanka palety", "─│┌┐└┘→←↑↓ 🇵🇱 ✅ § € — „” …", "OK-SCISLE"),
]
run_runda("R12 KACZOR", wek)

# --- R13 OBIETNICA (--fix) ------------------------------------------------------------
print("  R13 OBIETNICA (--fix):")
D = tempfile.mkdtemp(prefix="turniej_fix_")
def zapisz(n, t):
    p = os.path.join(D, n)
    io.open(p, "w", encoding="utf-8", newline="").write(t)
    return p
def czytaj(p):
    return io.open(p, encoding="utf-8", newline="").read()
fix_wyniki = []
def fix_check(nazwa, ok):
    fix_wyniki.append((nazwa, ok))
    print("    %-42s %s" % (nazwa, "OK" if ok else "WPADKA"))

t = "Zażółć gęślą jaźń — „cytat” 100% §7 € m² ✅\nlinia2\n"
p = zapisz("o1.md", t); pk.napraw(czytaj(p), p)
fix_check("czysty NFC plik bajt-w-bajt", czytaj(p) == t)
p = zapisz("o2.md", "s" + C(0x0435) + "rwer ma" + C(0x200B) + "buga")
pk.napraw(czytaj(p), p); w = czytaj(p)
fix_check("litery NIGDY nie podmienione (cyrylica zostaje)", C(0x0435) in w and C(0x200B) not in w)
t3 = "a" + C(0x200B) + "b" + C(0x2028) + "c" + C(0x00A0) + "d"
p = zapisz("o3.md", t3); pk.napraw(czytaj(p), p); w1 = czytaj(p)
pk.napraw(w1, p)
fix_check("idempotencja (2. przebieg = zero zmian)", w1 == czytaj(p))
t4 = 'x = "a' + C(0x2028) + 'b"\ny = 1\n'
p = zapisz("o4.py", t4); pk.napraw(czytaj(p), p); w4 = czytaj(p)
try:
    compile(w4, p, "exec"); k4 = True
except SyntaxError:
    k4 = False
fix_check(".py kompilowalny: LS w literale zostaje + kompiluje",
          k4 and C(0x2028) in w4)
t5 = "import os" + C(0x2028) + "x = 1" + C(0x2028)
p = zapisz("o5.py", t5); pk.napraw(czytaj(p), p); w5 = czytaj(p)
try:
    compile(w5, p, "exec"); k5 = True
except SyntaxError:
    k5 = False
fix_check(".py zepsuty (LS-sep) po fix kompiluje", k5)
t6 = 'x = "a' + C(0x2028) + 'b"\nimport os' + C(0x2028) + 'y = 1\n'
p = zapisz("o6.py", t6); pk.napraw(czytaj(p), p); w6 = czytaj(p)
try:
    compile(w6, p, "exec"); k6 = True
except SyntaxError:
    k6 = False
fix_check("zepsuty+LS w literale: kompiluje i LS zostaje",
          k6 and C(0x2028) in w6)
t7 = "x = 1  # kom" + C(0x2028) + "ent\nimport os" + C(0x2028) + "y = 1\n"
p = zapisz("o7.py", t7); pk.napraw(czytaj(p), p); w7 = czytaj(p)
try:
    compile(w7, p, "exec"); k7 = True
except SyntaxError:
    k7 = False
fix_check("zepsuty+LS w komentarzu: kompiluje, LS zostaje",
          k7 and C(0x2028) in w7)
t8 = 's = """a' + C(0x2028) + 'b"""\nimport os' + C(0x2028) + 'x = 2\n'
p = zapisz("o8.py", t8); pk.napraw(czytaj(p), p); w8 = czytaj(p)
try:
    compile(w8, p, "exec"); k8 = True
except SyntaxError:
    k8 = False
fix_check("zepsuty+LS w triple-literale: kompiluje i LS zostaje",
          k8 and C(0x2028) in w8)
shutil.rmtree(D, ignore_errors=True)

# --- FINAŁ -----------------------------------------------------------------------------
print()
print("=" * 66)
tot_n = sum(w["n"] for w in WYNIKI)
tot_fn = sum(len(w["fn"]) for w in WYNIKI)
tot_fp = sum(len(w["fp"]) for w in WYNIKI)
tot_szum = sum(len(w["szum"]) for w in WYNIKI)
tot_pol = sum(len(w["pol"]) for w in WYNIKI)
tot_crash = sum(len(w["crash"]) for w in WYNIKI)
fix_ok = sum(1 for _n, ok in fix_wyniki if ok)
print("FINAŁ: %d wektorów | FN %d | FP %d | SZUM %d | POLITYKA-ESC %d | CRASH %d | FIX %d/%d"
      % (tot_n, tot_fn, tot_fp, tot_szum, tot_pol, tot_crash, fix_ok, len(fix_wyniki)))
for w in WYNIKI:
    if w["fn"]:
        print("  FN [%s]: %s" % (w["runda"], w["fn"][:6]))
    if w["fp"]:
        print("  FP [%s]: %s" % (w["runda"], w["fp"][:6]))
    if w["szum"]:
        print("  SZUM [%s]: %s" % (w["runda"], w["szum"][:6]))
hom = [(w["runda"], w["hom"]) for w in WYNIKI if w["hom"][1]]
for runda, (tagi, szanse) in hom:
    print("  HOMOGLIF-tag [%s]: %d/%d" % (runda, tagi, szanse))

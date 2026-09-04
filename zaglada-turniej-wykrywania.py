"""TURNIEJ ZAGŁADY 1 — WYKRYWANIE/TRANSFORMACJA (kontrakt ZagladaKultury).
Rundy ZR1-ZR11. Exit 0 = zaliczony, 1 = wpadka. Seed z argv (ZR10)."""
import importlib.util
import os
import random
import subprocess
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
spec2 = importlib.util.spec_from_file_location("pk", _znajdz("PogromcaKwiatkow.py"))
pk = importlib.util.module_from_spec(spec2)
sys.modules["pk"] = pk
spec2.loader.exec_module(pk)

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260911
rnd = random.Random(SEED)
print("TURNIEJ ZAGŁADY 1 — WYKRYWANIE (ZagladaKultury v%s, seed %d)" % (zk.WERSJA, SEED))
print("=" * 66)
FN, FP, CRASH = [], [], []
N = 0


def ocen(vid, wejscie, oczekiwany):
    """oczekiwany: string dokladny."""
    global N
    N += 1
    try:
        dostal, licznik = zk.zaglada_tekst(wejscie)
    except Exception as e:
        CRASH.append((vid, ascii(str(e))[:80]))
        return
    if dostal != oczekiwany:
        (FP if oczekiwany == wejscie else FN).append(
            (vid, "=%r" % dostal))


def ocen_usun(vid, wejscie):
    global N
    N += 1
    try:
        dostal, _l = zk.zaglada_tekst(wejscie)
    except Exception as e:
        CRASH.append((vid, ascii(str(e))[:80]))
        return
    if dostal != "":
        FN.append((vid, "=%r" % dostal))


# --- ZR1 CYRYLICA -------------------------------------------------------------
def zr1():
    # transliteracja znak-po-znaku (bez reguł kontekstowych je-/obiekT)
    for we, ocz in [("привет", "priwet"), ("Москва", "Moskwa"),
                    ("спасибо", "spasibo"), ("объект", "obekt"),
                    ("щука", "szczuka"), ("хлеб", "chleb"),
                    ("Европа", "Ewropa"), ("Югра", "Jugra")]:
        ocen("zr1-slowo:%s" % we, we, ocz)
    for cp, ocz in sorted(zk.CYR.items()):
        c = chr(cp)
        if unicodedata.category(c).startswith("L"):
            ocen("zr1-tab:%04X" % cp, c, ocz)


# --- ZR2 GREKA ------------------------------------------------------------------
def zr2():
    # eta->e: transkrypcja tradycyjna (spójna z th/ch)
    for we, ocz in [("Ελλάδα", "Ellada"), ("Θεσσαλονίκη", "Thessalonike"),
                    ("χώρα", "chora"), ("ψυχή", "psyche")]:
        ocen("zr2-slowo:%s" % we, we, ocz)
    for we in "άέήίόύώΆΈΉΊΌΎΏ":
        baza = unicodedata.normalize("NFD", we)[0]
        ocz = zk.GREK.get(ord(baza))
        if ocz is not None:
            ocen("zr2-akcent:%04X" % ord(we), we, ocz)
    for cp, ocz in sorted(zk.GREK.items()):
        c = chr(cp)
        if unicodedata.category(c).startswith("L"):
            ocen("zr2-tab:%04X" % cp, c, ocz)


# --- ZR3 HOMOGLIFY + ŚWIĘTOŚĆ PL ------------------------------------------------
def zr3():
    for cp, ocz in sorted(zk.HOMOGLIFY.items()):
        ocen("zr3-map:%04X" % cp, chr(cp), ocz)
    for c in "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ":
        ocen("zr3-PL-swiety:%04X" % ord(c), c, c)
    ocen("zr3-zdanie", "Zażółć gęślą jaźń", "Zażółć gęślą jaźń")


# --- ZR4 OBCY OGONKI --------------------------------------------------------------
def zr4():
    obce = ["č", "ď", "ľ", "ň", "ř", "š", "ť", "ž", "ā", "ē", "ī", "ō", "ū",
            "ė", "į", "ų", "ů", "ű", "ő", "ğ", "ş", "ç", "à", "é", "ü", "ö",
            "ä", "ÿ", "è", "ì", "ò", "ù", "â", "ê", "î", "ô", "û"]
    for c in obce:
        b = unicodedata.normalize("NFD", c)
        if len(b) > 1 and b[0].isascii():
            ocen("zr4-ogonek:%04X" % ord(c), c, b[0])


# --- ZR5 CYFRY (pełna enumeracja Nd) ----------------------------------------------
def zr5():
    for cp in range(0x80, 0x110000):
        if unicodedata.category(chr(cp)) == "Nd":
            d = unicodedata.digit(chr(cp))
            ocen("zr5-nd:%05X" % cp, chr(cp), str(d))


# --- ZR6 FOLD -----------------------------------------------------------------------
def zr6():
    for we, ocz in [("ＡＢＣｄｅｆ", "ABCdef"), ("ﬁle ﬂag", "file flag"),
                    ("№7", "No7"), ("⑴②Ⅲ", "(1)2III")]:
        ocen("zr6-fold:%s" % we[:6], we, ocz)
    for we, ocz in [("²", "²"), ("— „”…€%§°±·«»", "— „”…€%§°±·«»")]:
        ocen("zr6-typografia-stay", we, ocz)
    ocen_usun("zr6-half", "½")
    ocen_usun("zr6-micro", "µ")
    ocen_usun("zr6-prime", "′")
    ocen_usun("zr6-acute", "´")


# --- ZR7 PISMA BEZ TABELI -> ZAGŁADA ------------------------------------------------
def zr7():
    bloki = [(0x4E00, 0x4E50, "CJK"), (0x3040, 0x3090, "kana"),
             (0xAC00, 0xAC40, "hangul"), (0x0600, 0x0640, "arab"),
             (0x05D0, 0x05F0, "hebr"), (0x0E00, 0x0E50, "thai"),
             (0x0900, 0x0950, "deva"), (0x0530, 0x0560, "armen"),
             (0x10A0, 0x10D0, "gruz"), (0x0E80, 0x0EC0, "lao")]
    for lo, hi, nm in bloki:
        for cp in range(lo, hi, 7):
            if unicodedata.category(chr(cp)).startswith("L"):
                ocen_usun("zr7-%s:%05X" % (nm, cp), chr(cp))
    ocen_usun("zr7-cyr-poza-tabela:046A", chr(0x046A))   # Ѫ (big yus)
    for we, ocz in [("hello 😀 world", "hello  world"),
                    ("⚠️uwaga", "uwaga"), ("ok ✅", "ok ")]:
        ocen("zr7-emoji:%s" % we[:6], we, ocz)


# --- ZR8 NIEWIDZIALNE / SPACJE / ŁAMACZE ----------------------------------------------
def zr8():
    lam = {ord(c) for c in zk.LAMACZE}
    for cp in range(0x110000):
        kat = unicodedata.category(chr(cp))
        if kat in ("Cc", "Cf") and cp not in ((0x09, 0x0A, 0x0D) + tuple(lam)):
            ocen_usun("zr8-cccf:%05X" % cp, chr(cp))
    for cp in range(0x300, 0x370):
        if unicodedata.category(chr(cp)) in ("Mn", "Mc", "Me"):
            ocen_usun("zr8-mn:%04X" % cp, chr(cp))
    for cp in list(range(0xE000, 0xE020)) + list(range(0xD800, 0xD810)) + \
            [0x0378, 0x0380, 0xE01F7, 0x10FFFF and 0x10FFFE, 0x2FE0]:
        ocen_usun("zr8-co-cs-cn:%05X" % cp, chr(cp))
    for cp in range(0xA0, 0x2000, 3):
        if unicodedata.category(chr(cp)) == "Zs":
            ocen("zr8-zs:%04X" % cp, "a" + chr(cp) + "b", "a b")
    for cp in [0x202F, 0x205F, 0x3000]:
        ocen("zr8-zs:%04X" % cp, "a" + chr(cp) + "b", "a b")
    for c in "\x0b\x0c\x1c\x1d\x1e  ":
        ocen("zr8-lamacz:%04X" % ord(c), "wiersz" + c + "drugi", "wiersz\ndrugi")


# --- ZR9 ŚWIĘTOŚĆ POLSKI (40 zdań, bajt-w-bajt) -----------------------------------------
PL_S = ["Zażółć gęślą jaźń — a potem 100% spokoju.",
        "Wieś组委会? nie — wieś Gąski ma ±3 km do morza.",
        ]


def zdanie_pl():
    sl = ["kasza", "gęś", "jaźń", "źdźbło", "łódź", "śledź", "piorun",
          "mżący", "krzątanina", "zwierz", "głośny", "wiać", "żółw"]
    s = " ".join(rnd.choice(sl) for _ in range(rnd.randrange(4, 9)))
    return s.capitalize() + rnd.choice([".", "!", " —", " …"]) + rnd.choice(["", " €", " §7", " 2²"])


def zr9():
    for i in range(40):
        t = zdanie_pl() if i else PL_S[0]
        ocen("zr9-pl:%d" % i, t, t)


# --- ZR10 KONTRASIOSTRA (Zagłada -> Pogromca bez BLAD) -----------------------------------
def zr10():
    bazy = ["serwer działa poprawnie", "restart o 4:00 rano",
            "kasza z serem", "Zażółć gęślą jaźń", "ping <= 45 ms"]
    brudy = []
    for cp in range(0x400, 0x460):
        if unicodedata.category(chr(cp)).startswith("L"):
            brudy.append(chr(cp))
    for cp in range(0x3B1, 0x3C9):
        brudy.append(chr(cp))
    brudy += [chr(0x4E00), chr(0x3040 + 5), chr(0x0600 + 5), chr(0x200B),
              chr(0xE123), chr(0x2028), chr(0x0661), chr(0x017F), chr(0x00DF),
              chr(0xFF21), chr(0x010D)]
    for i in range(120):
        t = rnd.choice(bazy)
        p = rnd.randrange(len(t) + 1)
        if rnd.random() < 0.25:  # czasem wklej caly token
            w = rnd.choice(brudy) * rnd.randrange(1, 4)
        else:
            w = rnd.choice(brudy)
        tekst = t[:p] + w + t[p:]
        global N
        N += 1
        try:
            out, _l = zk.zaglada_tekst(tekst)
            b, u = pk.analizuj(out)
        except Exception as e:
            CRASH.append(("zr10:%d" % i, ascii(str(e))[:80]))
            continue
        if b:
            FN.append(("zr10:%d" % i, "pogromca BLAD po zagładzie: %r" % out[:60]))


# --- ZR11 KONTRAKT-CLI ---------------------------------------------------------------------
def zr11():
    global N
    D = tempfile.mkdtemp(prefix="zcli_")

    def z(nm, t, ext="txt"):
        p = os.path.join(D, nm + "." + ext)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        return p

    def run(args):
        return subprocess.run([sys.executable, ZK_PATH] + args,
                              capture_output=True, text=True, timeout=60)

    czysty = z("czysty", "Zażółć gęślą jaźń — 100% §7\n")
    brudny = z("brudny", "сerwer ma bugа i 汉字\n")
    brak = os.path.join(D, "nie-ma.txt")
    przypadki = [("czysty raport -> 0", [czysty], 0),
                 ("brudny raport -> 1", [brudny], 1),
                 ("brak pliku -> 2", [brak], 2)]
    for nm, args, kod in przypadki:
        N += 1
        r = run(args)
        if r.returncode != kod or "Traceback" in r.stdout + r.stderr:
            FN.append(("z11-cli:" + nm, "exit=%d" % r.returncode))
    N += 1
    r = run(["--zaglada", brudny])
    t = open(brudny, encoding="utf-8").read()
    b, u = pk.analizuj(t)
    if r.returncode != 0 or b:
        FN.append(("z11-zaglada:wykonaj", "exit=%d BLADpo=%s" % (r.returncode, bool(b))))
    N += 1
    r = run(["--zaglada", czysty])
    if r.returncode != 0:
        FN.append(("z11-zaglada:czysty", "exit=%d" % r.returncode))
    # idempotencja API
    for src in ["сerwer ﬁle ٣", "wiersz drugi", "čąü Ａ½"]:
        N += 1
        w1, _l = zk.zaglada_tekst(src)
        w2, _l2 = zk.zaglada_tekst(w1)
        if w1 != w2:
            FN.append(("z11-idem:%r" % src[:10], "nie-idempotentny"))
    # .py z obca kultura w literale -> chroniony (raport: nic do zrobienia)
    N += 1
    pydir = z("pyliteral", 's = "текст"\nx = 1\n', "py")
    r = run([pydir])
    t = open(pydir, encoding="utf-8").read()
    if r.returncode != 0 or t != 's = "текст"\nx = 1\n':
        FN.append(("z11-py-literal", "exit=%d zmienil=%s" % (r.returncode, t != 's = "текст"\nx = 1\n')))
    import shutil
    shutil.rmtree(D, ignore_errors=True)


for fn in (zr1, zr2, zr3, zr4, zr5, zr6, zr7, zr8, zr9, zr10, zr11):
    n0 = N
    fn()
    zle = len(FN) + len(FP) + len(CRASH)
    print("  %-10s %5d wektorow — %s" % (fn.__name__.upper(), N - n0,
          "czysto" if zle == 0 else "WPADKA"))

print()
print("=" * 66)
print("FINAŁ Z1: %d wektorów | FN %d | FP %d | CRASH %d" % (N, len(FN), len(FP), len(CRASH)))
for nm, dane in (("FN", FN), ("FP", FP), ("CRASH", CRASH)):
    for x in dane[:10]:
        print("  %s: %s" % (nm, ascii(str(x))[:140]))
sys.exit(0 if not (FN or FP or CRASH) else 1)

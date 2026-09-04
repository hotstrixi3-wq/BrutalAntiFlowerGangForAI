#!/usr/bin/env python3
"""TURNIEJ 5 — ANIHILATOR CHWASTOW (js/ts/java/go/rs/cs/c/cpp/php/rb...).

Do v1.4.0 Anihilator nie mial ANI JEDNEGO testu poza wlasnym selftestem,
mimo ze obsluguje kilkanascie jezykow i pisze po plikach. Ten turniej to
nadrabia. Cztery niezalezne kategorie:

  A. WYKRYWANIE   — czy widzi skazenie w kodzie kazdego jezyka (i nie
                    zglasza falszywych alarmow na czystych plikach).
  B. NIEPSUCIE    — czy DANE (literaly, komentarze, polskie napisy) i
                    struktura pliku przezywaja czyszczenie bez zmian.
  C. FAIL-CLOSED  — czy BLOKUJE pliki z konstrukcjami, ktorych jego skaner
                    stanow nie rozumie (heredoc, surowe literaly). Lepiej
                    nie zrobic nic niz zrobic zle. Test sprawdza rowniez,
                    ze zablokowany plik NIE ZOSTAL TKNIETY na dysku.
  D. WYKONANIE    — czy program po czyszczeniu naprawde DZIALA i daje ten
                    sam wynik. Uruchamiane realnie tam, gdzie w systemie
                    jest runtime (node dla js, gcc dla c) — reszta jezykow
                    jest wtedy uczciwie raportowana jako POMINIETA, zeby
                    nikt nie wzial braku narzedzia za zdany test.

Uzycie:  python3 dev/turnieje/turniej-5-anihilator.py
Wyjscie: 0 = wszystko zdane, 1 = jest regresja.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANIHILATOR = os.path.join(KORZEN, "AnihilatorChwastow.py")

C = "\u043e"   # cyrylickie o  -> o
A = "\u0430"   # cyrylickie a  -> a
E = "\u0435"   # cyrylickie e  -> e
P = "\u0440"   # cyrylickie er -> r
ZW = "\u200b"  # zero-width space
NB = "\u00a0"  # twarda spacja

POLSKI = "zolw, \u0142\u0105ka, \u017cmija, \u015bnieg, \u0107ma"
# Tekst, ktory Anihilator ZMIENILBY, gdyby trafil na niego poza literalem.
# Polskie znaki sa w DOZWOLONE, wiec same w sobie nie sprawdzaja ochrony
# literalow — do tego potrzebne sa znaki realnie podmieniane (cyrylica,
# greka, homoglify). W literale MUSZA przetrwac nietkniete: to sa DANE.
OBCE_DANE = "\u041c\u043e\u0441\u043a\u0432\u0430 \u0391\u03b8\u03ae\u03bd\u03b1 \u4e2d\u6587"


def uruchom(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=120, cwd=cwd)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"


def anihiluj(sciezka, wykonaj=True):
    cmd = [sys.executable, ANIHILATOR]
    if wykonaj:
        cmd.append("--anihilacja")
    cmd.append(sciezka)
    return uruchom(cmd)


def ma(narzedzie):
    return shutil.which(narzedzie) is not None


# =====================================================================
# A. WYKRYWANIE
# =====================================================================
# (nazwa_pliku, tresc, czy_ma_wykryc)
WYKRYWANIE = [
    ("a.js",   'let c%snter = 0;\nc%snter += 1;\n' % (C, C), True),
    ("a.ts",   'let x%s: number = 1;\nexport default x%s;\n' % (A, A), True),
    ("a.java", 'class T { int v%sl = 1; }\n' % (A,), True),
    ("a.go",   'package main\nfunc main() { s%sm := 1; _ = s%sm }\n' % (C, C), True),
    ("a.rs",   'fn main() { let m%s = 1; println!("{}", m%s); }\n' % (E, E), True),
    ("a.cs",   'class P { static int V%sl = 2; }\n' % (A,), True),
    ("a.c",    '#include <stdio.h>\nint main(){int c%s=1;return c%s-1;}\n' % (E, E), True),
    ("a.cpp",  'int main(){ int v%s = 0; return v%s; }\n' % (A, A), True),
    ("zw.js",  'let li%scznik = 1;\n' % (ZW,), True),
    ("nb.js",  'let a%s= 1;\n' % (NB,), True),
    # czyste — nie wolno podniesc alarmu
    ("czysty.js",   'let counter = 0;\ncounter += 1;\nconsole.log("ok");\n', False),
    ("czysty.java", 'class T { int val = 1; }\n', False),
    ("czysty.c",    '#include <stdio.h>\nint main(){return 0;}\n', False),
    # polskie znaki w literalach i komentarzach to NIE skazenie
    ("polski.js",   '// %s\nconst s = "%s";\nconsole.log(s);\n' % (POLSKI, POLSKI), False),
    ("polski.cs",   'class P { // %s\n  string s = "%s";\n}\n' % (POLSKI, POLSKI), False),
]


def kat_a():
    tmp = tempfile.mkdtemp(prefix="t5a-")
    fn = fp = 0
    szczegoly = []
    for nazwa, tresc, ma_wykryc in WYKRYWANIE:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        kod, out, err = anihiluj(p, wykonaj=False)
        wykryl = "DO ANIHILACJI" in out or "ANIHILACJA" in out
        if ma_wykryc and not wykryl:
            fn += 1
            szczegoly.append(("FN", nazwa, "nie zobaczyl skazenia"))
        elif not ma_wykryc and wykryl:
            fp += 1
            szczegoly.append(("FP", nazwa, out.strip().splitlines()[0][:60] if out.strip() else ""))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== A. WYKRYWANIE ==")
    print("   przypadkow: %d | FN: %d | FP: %d" % (len(WYKRYWANIE), fn, fp))
    for t, n, o in szczegoly:
        print("     [%s] %s: %s" % (t, n, o))
    return fn + fp


# =====================================================================
# B. NIEPSUCIE DANYCH
# =====================================================================
# (nazwa, tresc, fragmenty_ktore_MUSZA_przetrwac_bez_zmian)
NIEPSUCIE = [
    ("dane.js",
     'let c%snter = 0;\nconst opis = "%s";\n// komentarz: %s\nconsole.log(opis);\n'
     % (C, POLSKI, POLSKI),
     [POLSKI]),
    ("tpl.js",
     'let k%s = 3;\nconsole.log(`cena: ${k%s} zl - %s`);\n' % (C, C, POLSKI),
     [POLSKI]),
    ("regex.js",
     'let v%sl = /a[%s]+b/g;\nconsole.log("x".match(v%sl));\n' % (A, POLSKI, A),
     [POLSKI]),
    ("cudzy.java",
     'class T {\n  // %s\n  String s = "%s";\n  int v%sl = 1;\n}\n' % (POLSKI, POLSKI, A),
     [POLSKI]),
    ("blok.cs",
     'class P {\n  /* blok: %s */\n  string s = "%s";\n  int v%sl = 2;\n}\n'
     % (POLSKI, POLSKI, A),
     [POLSKI]),
    ("json-ish.ts",
     'const o%sbj = { klucz: "%s" };\nexport default o%sbj;\n' % (A, POLSKI, A),
     [POLSKI]),
    # --- ostrzejsze: DANE, ktore narzedzie umie zmienic. Polskie znaki sa
    # w DOZWOLONE, wiec przetrwaja nawet przy CALKOWICIE wylaczonej ochronie
    # literalow. Dopiero cyrylica/greka/CJK w stringu sprawdza, czy ochrona
    # naprawde dziala — bez tego test przesypia regresje.
    ("obce-string.js",
     'let c%snter = 1;\nconst ru = "%s";\nconsole.log(ru, c%snter);\n'
     % (C, OBCE_DANE, C),
     [OBCE_DANE]),
    ("obce-komentarz.js",
     '// %s\nlet v%sl = 2;\nconsole.log(v%sl);\n' % (OBCE_DANE, A, A),
     [OBCE_DANE]),
    ("obce-template.js",
     'let k%s = 3;\nconsole.log(`${k%s} %s`);\n' % (C, C, OBCE_DANE),
     [OBCE_DANE]),
    ("obce-java.java",
     'class T {\n  String s = "%s";\n  int v%sl = 1;\n}\n' % (OBCE_DANE, A),
     [OBCE_DANE]),
    ("obce-blok.cs",
     'class P {\n  /* %s */\n  int v%sl = 2;\n}\n' % (OBCE_DANE, A),
     [OBCE_DANE]),
]


def kat_b():
    tmp = tempfile.mkdtemp(prefix="t5b-")
    zle = 0
    szczegoly = []
    for nazwa, tresc, musza in NIEPSUCIE:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        linii_przed = tresc.count("\n")
        anihiluj(p)
        po = io.open(p, encoding="utf-8").read()
        for frag in musza:
            if frag not in po:
                zle += 1
                szczegoly.append((nazwa, "ZNISZCZONE DANE", frag[:30]))
        if po.count("\n") != linii_przed:
            zle += 1
            szczegoly.append((nazwa, "ZMIENIONA LICZBA LINII",
                              "%d -> %d" % (linii_przed, po.count("\n"))))
        # skazenie w KODZIE musi zniknac
        if any(z in po for z in (C, A, E, P, ZW, NB)):
            # dopuszczalne tylko jesli siedzi w chronionym literalu
            if not any(frag in po for frag in musza):
                zle += 1
                szczegoly.append((nazwa, "SKAZENIE ZOSTALO", ""))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== B. NIEPSUCIE DANYCH ==")
    print("   przypadkow: %d | naruszen: %d" % (len(NIEPSUCIE), zle))
    for n, t, o in szczegoly:
        print("     [%s] %s: %s" % (t, n, o))
    return zle


# =====================================================================
# B2. POPRAWNOSC NAPRAWY (nie wystarczy "cos zrobil")
# =====================================================================
# Wykrycie skazenia i usuniecie go to za malo: znak musi zostac zamieniony
# na WLASCIWA litere ASCII. Gdyby transliteracja zamienila sie w usuniecie,
# 'cоnter' stalby sie 'cnter' zamiast 'conter' — plik dalej jest czysty
# i dalej sie kompiluje, ale nazwa zmiennej po cichu sie zmienila.
# (nazwa, tresc, dokladny_tekst_ktory_musi_wyjsc)
NAPRAWA = [
    ("tr-cyr-o.js",  'let c%snter = 0;\n' % C,   'let conter = 0;\n'),
    ("tr-cyr-a.js",  'let w%srtosc = 1;\n' % A,  'let wartosc = 1;\n'),
    ("tr-cyr-e.js",  'let t%skst = 2;\n' % E,    'let tekst = 2;\n'),
    ("tr-cyr-r.js",  'let ba%swa = 3;\n' % P,    'let barwa = 3;\n'),
    ("tr-grk-o.java", 'class T { int p%sle = 1; }\n' % "\u03bf",
     'class T { int pole = 1; }\n'),
    ("tr-grk-a.cs",  'class P { int v%sl = 2; }\n' % "\u03b1",
     'class P { int val = 2; }\n'),
    ("tr-zw.js",     'let li%scznik = 4;\n' % ZW, 'let licznik = 4;\n'),
    # twarda spacja w JS -> zwykla spacja jest POPRAWNA (to nie Python,
    # wciecia nie maja znaczenia skladniowego; usuniecie sklejaloby tokeny)
    ("tr-nbsp.js",   'let a%s= 5;\n' % NB,        'let a = 5;\n'),
]


def kat_b2():
    tmp = tempfile.mkdtemp(prefix="t5b2-")
    zle = 0
    szczegoly = []
    for nazwa, tresc, oczekiwane in NAPRAWA:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        anihiluj(p)
        po = io.open(p, encoding="utf-8").read()
        if po != oczekiwane:
            zle += 1
            szczegoly.append((nazwa, "%r zamiast %r"
                              % (po.strip()[:34], oczekiwane.strip()[:34])))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== B2. POPRAWNOSC NAPRAWY ==")
    print("   przypadkow: %d | zle naprawione: %d" % (len(NAPRAWA), zle))
    for n, o in szczegoly:
        print("     [ZLA NAPRAWA] %s: %s" % (n, o))
    return zle


# =====================================================================
# C. FAIL-CLOSED (blokada nieobslugiwanych konstrukcji)
# =====================================================================
BLOKADY = [
    ("go-backtick.go",
     'package main\nvar s = `surowy %s`\nfunc main(){ _ = s }\n' % POLSKI),
    ("php-heredoc.php",
     '<?php\n$x = <<<EOT\n%s\nEOT;\n' % POLSKI),
    ("cpp-raw.cpp",
     'const char* s = R"(surowy %s)";\nint main(){return 0;}\n' % POLSKI),
    ("rust-raw.rs",
     'fn main() { let s = r#"surowy %s"#; println!("{}", s); }\n' % POLSKI),
    ("java-block.java",
     'class T { String s = """\n  %s\n  """; }\n' % POLSKI),
    ("ruby-heredoc.rb",
     'x = <<~EOT\n  %s\nEOT\n' % POLSKI),
    ("kotlin-multi.kt",
     'val s = """\n  %s\n"""\n' % POLSKI),
    ("swift-multi.swift",
     'let s = """\n  %s\n"""\n' % POLSKI),
]


def kat_c():
    tmp = tempfile.mkdtemp(prefix="t5c-")
    zle = 0
    szczegoly = []
    for nazwa, tresc in BLOKADY:
        p = os.path.join(tmp, nazwa)
        io.open(p, "w", encoding="utf-8").write(tresc)
        przed = io.open(p, encoding="utf-8").read()
        kod, out, err = anihiluj(p)
        calosc = out + err
        zablokowal = "BLOKADA" in calosc
        po = io.open(p, encoding="utf-8").read()
        if not zablokowal:
            zle += 1
            szczegoly.append((nazwa, "BRAK BLOKADY",
                              (out.strip().splitlines() or [""])[0][:50]))
        if po != przed:
            zle += 1
            szczegoly.append((nazwa, "PLIK TKNIETY MIMO BLOKADY", ""))
    shutil.rmtree(tmp, ignore_errors=True)
    print("== C. FAIL-CLOSED (blokady) ==")
    print("   przypadkow: %d | naruszen: %d" % (len(BLOKADY), zle))
    for n, t, o in szczegoly:
        print("     [%s] %s: %s" % (t, n, o))
    return zle


# =====================================================================
# D. WYKONANIE (realny runtime)
# =====================================================================
def kat_d():
    tmp = tempfile.mkdtemp(prefix="t5d-")
    zdane = zle = 0
    pominiete = []
    szczegoly = []

    # --- JavaScript (node) ---
    if ma("node"):
        probki = [
            ("js-zmienna",
             'let c%snter = 0;\nfunction add(){ c%snter += 1; return c%snter; }\n'
             'console.log(add(), add());\n' % (C, C, C), "1 2"),
            ("js-template",
             'let v%s = 7;\nconsole.log(`wynik: ${v%s}`);\n' % (C, C), "wynik: 7"),
            ("js-template-wyrazenie",
             'let n%s = 2;\nconsole.log(`${[1,2].map(x => x * n%s).join(",")}`);\n'
             % (C, C), "2,4"),
            ("js-dane-polskie",
             'let k%s = 3;\nconsole.log(`cena: ${k%s} zl - %s`);\n' % (C, C, POLSKI),
             "cena: 3 zl - " + POLSKI),
            ("js-obiekt",
             'const o%s = { p%sle: 5 };\nconsole.log(o%s.p%sle);\n' % (A, C, A, C), "5"),
            ("js-klasa",
             'class K { constructor(){ this.w%srtosc = 8; } }\n'
             'console.log(new K().w%srtosc);\n' % (A, A), "8"),
        ]
        for nazwa, kod, oczek in probki:
            p = os.path.join(tmp, nazwa + ".js")
            io.open(p, "w", encoding="utf-8").write(kod)
            rc0, out0, _ = uruchom(["node", p])
            anihiluj(p)
            rc1, out1, err1 = uruchom(["node", p])
            if rc1 == 0 and out1.strip() == oczek:
                zdane += 1
            else:
                zle += 1
                szczegoly.append((nazwa, "przed=%r po=%r" % (
                    out0.strip()[:24], (out1.strip() or err1.strip())[:44])))
    else:
        pominiete.append("js (brak node)")

    # --- C (gcc) ---
    if ma("gcc"):
        probki_c = [
            ("c-zmienna",
             '#include <stdio.h>\nint main(){ int c%snter = 0; c%snter += 2;\n'
             '  printf("%%d\\n", c%snter); return 0; }\n' % (C, C, C), "2"),
            ("c-funkcja",
             '#include <stdio.h>\nint p%sdwoj(int x){ return x*2; }\n'
             'int main(){ printf("%%d\\n", p%sdwoj(21)); return 0; }\n' % (C, C), "42"),
            ("c-napis",
             '#include <stdio.h>\nint main(){ int v%sl = 1;\n'
             '  printf("%%s %%d\\n", "%s", v%sl); return 0; }\n'
             % (A, POLSKI, A), POLSKI + " 1"),
        ]
        for nazwa, kod, oczek in probki_c:
            p = os.path.join(tmp, nazwa + ".c")
            io.open(p, "w", encoding="utf-8").write(kod)
            anihiluj(p)
            binp = os.path.join(tmp, nazwa + ".bin")
            rc, _, cerr = uruchom(["gcc", "-o", binp, p])
            if rc != 0:
                zle += 1
                szczegoly.append((nazwa, "NIE KOMPILUJE: " + cerr.strip()[:44]))
                continue
            rc, out, _ = uruchom([binp])
            if rc == 0 and out.strip() == oczek:
                zdane += 1
            else:
                zle += 1
                szczegoly.append((nazwa, "wynik=%r oczekiwano=%r"
                                  % (out.strip()[:24], oczek[:24])))
    else:
        pominiete.append("c (brak gcc)")

    shutil.rmtree(tmp, ignore_errors=True)
    print("== D. WYKONANIE (realny runtime) ==")
    print("   ZDANE: %d | OBLANE: %d" % (zdane, zle))
    if pominiete:
        print("   POMINIETE (brak narzedzia, NIE liczy sie jako zdane): %s"
              % ", ".join(pominiete))
    for n, o in szczegoly:
        print("     [OBLANY] %s: %s" % (n, o))
    return zle


def main():
    print("=" * 66)
    print("TURNIEJ 5 — ANIHILATOR CHWASTOW")
    print("=" * 66)
    zle = kat_a() + kat_b() + kat_b2() + kat_c() + kat_d()
    print()
    print("=" * 66)
    print("FINAL T5: %s" % ("WSZYSTKO ZDANE" if not zle
                            else "REGRESJA — %d naruszen" % zle))
    print("=" * 66)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""POMIAR CELOWANY — czy KAZDY turniej z osobna umie oblac.

Roznica wobec pomiar-mutacyjny.py: tamten pyta "czy KTOKOLWIEK zlapal",
ten pyta "czy TEN KONKRETNY turniej lapie to, co deklaruje w swoich
kategoriach". Turniej moze przechodzic pomiar ogolny dzieki temu, ze
mutacje lapie ktos inny - a sam byc dekoracja.

Dla kazdej pary (turniej, kategoria) wycinamy wade, ktora ta kategoria
MA wykrywac, i uruchamiamy WYLACZNIE ten turniej. Kazde ">>> PRZESPAL <<<"
to kategoria, ktora niczego nie pilnuje.

Wynik z 2026-09-05: 16 prob, 0 przespanych.

Uzycie: python3 dev/turnieje/pomiar-per-turniej.py
Czas: ~20 s. Uruchamiaj po dodaniu nowej kategorii do turnieju.
"""
import os, shutil, subprocess, sys, tempfile
K = "/home/user/BrutalAntiFlowerGangForAI"

# (turniej, kategoria, plik, stare, nowe)
PROBY = [
 ("dev/luki/luka-fstring.py","dowod luki","ZagladaKultury.py",
  "    return chronione - kod_fstring","    return chronione"),
 ("dev/turnieje/turniej-4-runtime.py","kryterium WYKONANIA","ZagladaKultury.py",
  "    return chronione - kod_fstring","    return chronione"),
 ("dev/turnieje/turniej-5-anihilator.py","B2 poprawnosc naprawy","AnihilatorChwastow.py",
  "    if cp in CYR:","    if False and cp in CYR:"),
 ("dev/turnieje/turniej-5-anihilator.py","B niepsucie danych","AnihilatorChwastow.py",
  "        return zaglada_tekst_poza_literalami_multi(tekst, ext)",
  "        return zaglada_tekst(tekst, kod=True)"),
 ("dev/turnieje/turniej-6-prokurator.py","C czyste akta","ProkuratorOgrodnik.py",
  "def notacja_uxxxx(tekst):","def notacja_uxxxx(tekst):\n    return tekst"),
 ("dev/turnieje/turniej-6-prokurator.py","D plan-act","ProkuratorOgrodnik.py",
  '    wykonaj = "--wykonaj" in args','    wykonaj = True'),
 ("dev/turnieje/turniej-6-prokurator.py","A polityka .py","ProkuratorOgrodnik.py",
  "            elif is_py and _py_skazenie_tylko_w_literalach(path):","            elif is_py:"),
 ("dev/turnieje/turniej-7-zwiad.py","C rozdzial kod/dane","zwiad.py",
  "        w_kodzie = (chronione is None) or (i not in chronione)","        w_kodzie = True"),
 ("dev/turnieje/turniej-7-zwiad.py","B kompletnosc","zwiad.py",
  "        if c in Z.DOZWOLONE:","        if c in Z.DOZWOLONE or i % 2:"),
 ("dev/turnieje/turniej-8-bramki.py","A wykrywalnosc","sprawdz-spojnosc.py",
  "def sprawdz_embedy(prawda):","def sprawdz_embedy(prawda):\n    return []"),
 ("dev/turnieje/turniej-8-bramki.py","C zasieg","sprawdz-teksty.py",
  '    "dev/kwiatki-testy/", "fixtures/", "docs/logi/",',
  '    "dev/", "docs/", "fixtures/",'),
 ("dev/turnieje/turniej-3-niepsucie.py","niepsucie --fix","PogromcaKwiatkow.py",
  "def napraw(tekst, sciezka):","def napraw(tekst, sciezka):\n    return tekst"),
 ("dev/turnieje/zaglada-turniej-niepsucie.py","Z2 niepsucie","ZagladaKultury.py",
  "    return chronione - kod_fstring","    return set()"),
 ("dev/tor-pogromcy.py","wektory detekcji","PogromcaKwiatkow.py",
  "    for lo, hi, nazwa in BLOKOWANE:","    for lo, hi, nazwa in ():"),
 ("dev/turnieje/turniej-2-sprawdzajacy.py","T2 wektory","PogromcaKwiatkow.py",
  "def klasyfikuj(znak):",'def klasyfikuj(znak):\n    return ("OK", "")'),
 ("dev/turnieje/zaglada-turniej-wykrywania.py","Z1 wykrywanie","ZagladaKultury.py",
  "    if cp in CYR:","    if False and cp in CYR:"),
]
print("%-32s %-24s %s"%("TURNIEJ","KATEGORIA","CZY ZLAPAL"))
print("-"*82)
przespane=0
for t,kat,plik,stare,nowe in PROBY:
    b=tempfile.mkdtemp(prefix="pt-"); r=os.path.join(b,"repo")
    shutil.copytree(K,r,ignore=shutil.ignore_patterns(".git","__pycache__"))
    for c in (["init","-q"],["add","-A"],["-c","user.email=a@b","-c","user.name=m","commit","-qm","x"]):
        subprocess.run(["git"]+c,cwd=r,capture_output=True)
    p=os.path.join(r,plik); s=open(p,encoding="utf-8").read()
    if stare not in s:
        print("%-32s %-24s WZORZEC NIEAKTUALNY"%(os.path.basename(t)[:32],kat[:24]))
        shutil.rmtree(b,ignore_errors=True); continue
    open(p,"w",encoding="utf-8").write(s.replace(stare,nowe,1))
    try:
        rr=subprocess.run([sys.executable,os.path.join(r,t)],cwd=r,capture_output=True,text=True,timeout=400)
        ok = rr.returncode!=0
    except subprocess.TimeoutExpired: ok=True
    shutil.rmtree(b,ignore_errors=True)
    if not ok: przespane+=1
    print("%-32s %-24s %s"%(os.path.basename(t)[:32],kat[:24],"tak" if ok else ">>> PRZESPAL <<<"))
print("-"*82)
print("PRZESPANYCH: %d z %d"%(przespane,len(PROBY)))

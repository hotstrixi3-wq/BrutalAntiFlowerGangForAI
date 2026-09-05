#!/usr/bin/env python3
"""POMIAR MUTACYJNY — kto pilnuje testów.

Odpowiada na pytanie, którego nie da się rozstrzygnąć lekturą:
**czy ten test w ogóle coś testuje?**

Definicja robocza, jedyna mierzalna:

    Test jest wiarygodny wtedy, gdy potrafi OBLAC na zepsutym narzedziu.
    Test przechodzacy na narzedziu z wycieta funkcja tej funkcji NIE
    TESTUJE - niezaleznie od tego, jak solidnie wyglada.

Metoda: kopia repo -> wyciecie jednej zdolnosci narzedzia -> uruchomienie
wszystkich testow -> zapis, ktore obleja. Mutacja, ktorej nie zlapal
nikt, to dziura w pokryciu.

W tej sesji dwa razy okazalo sie, ze nowy turniej jest dekoracja:
T5 przespal 2 z 4 sabotazy (probki uzywaly polskich znakow, ktore sa
w DOZWOLONE), T8 przespal 2 z 3 (sprawdzal sam kod wyjscia, a exit=1
padal z innego powodu niz badany).

Uzycie:
    python3 dev/turnieje/pomiar-mutacyjny.py           # pelny pomiar
    python3 dev/turnieje/pomiar-mutacyjny.py --szybki  # tylko fundament

Wyjscie: 0 = kazda mutacja zlapana, 1 = ktoras przeszla niezauwazona.
Czas: ~90 s (pelny). Nie jest czescia zwyklej regresji.
"""
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (opis, plik, szukany_fragment, zamiennik)
# Kazda mutacja wycina JEDNA zdolnosc - inaczej nie wiadomo, co zlapal test.
MUTACJE_FUNDAMENT = [
    ("Pogromca: klasyfikuj zawsze OK", "PogromcaKwiatkow.py",
     "def klasyfikuj(znak):", 'def klasyfikuj(znak):\n    return ("OK", "")'),
    ("Pogromca: BLOKOWANE puste", "PogromcaKwiatkow.py",
     "    for lo, hi, nazwa in BLOKOWANE:", "    for lo, hi, nazwa in ():"),
    ("Pogromca: --fix nic nie robi", "PogromcaKwiatkow.py",
     "def napraw(tekst, sciezka):", "def napraw(tekst, sciezka):\n    return tekst"),
]

MUTACJE_RESZTA = [
    ("Zaglada: brak ochrony literalow", "ZagladaKultury.py",
     "    return chronione - kod_fstring", "    return set()"),
    ("Zaglada: brak transliteracji", "ZagladaKultury.py",
     "    if cp in CYR:", "    if False and cp in CYR:"),
    ("Anihilator: brak blokad fail-closed", "AnihilatorChwastow.py",
     "    for marker, opis in NIEOBSLUGIWANE.get(ext, ()):",
     "    for marker, opis in ():"),
    ("Prokurator: wszystko UMORZONE", "ProkuratorOgrodnik.py",
     "def match_allowlist(path: str) -> bool:",
     "def match_allowlist(path: str) -> bool:\n    return True"),
    ("zwiad: symuluj zwraca oryginal", "zwiad.py",
     "def symuluj(tekst, ext):", "def symuluj(tekst, ext):\n    return tekst"),
    ("sprawdz-teksty: nie widzi cyrylicy", "sprawdz-teksty.py",
     'PISMA_HOMOGLIFOWE = ("CYRILLIC", "GREEK", "ARMENIAN", "COPTIC", "CHEROKEE")',
     'PISMA_HOMOGLIFOWE = ()'),
]

SELFTESTY = ["PogromcaKwiatkow.py", "ZagladaKultury.py", "ProkuratorOgrodnik.py",
             "AnihilatorChwastow.py", "zwiad.py", "pamietnik.py", "sprawdz-teksty.py"]

TURNIEJE = [
    "dev/tor-pogromcy.py", "dev/fuzz-pogromcy.py",
    "dev/turnieje/turniej-2-sprawdzajacy.py", "dev/turnieje/turniej-3-niepsucie.py",
    "dev/turnieje/zaglada-turniej-wykrywania.py",
    "dev/turnieje/zaglada-turniej-niepsucie.py",
    "dev/turnieje/turniej-4-runtime.py", "dev/turnieje/turniej-5-anihilator.py",
    "dev/turnieje/turniej-6-prokurator.py", "dev/turnieje/turniej-7-zwiad.py",
    "dev/turnieje/turniej-8-bramki.py", "dev/luki/luka-fstring.py",
]


def przygotuj_kopie(prefix):
    """Kopia repo z wlasnym gitem, w katalogu o pustym rodzicu."""
    baza = tempfile.mkdtemp(prefix=prefix)
    repo = os.path.join(baza, "repo")
    shutil.copytree(KORZEN, repo,
                    ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
    for cmd in (["init", "-q"], ["add", "-A"],
                ["-c", "user.email=mut@local", "-c", "user.name=mutacja",
                 "commit", "-q", "-m", "stan bazowy"]):
        subprocess.run(["git"] + cmd, cwd=repo, capture_output=True, text=True)
    return baza, repo


def kto_zlapal(repo):
    """Lista nazw testow, ktore obleja na tej kopii."""
    zlapali = []
    for nazwa in SELFTESTY:
        p = os.path.join(repo, nazwa)
        if not os.path.exists(p):
            continue
        try:
            r = subprocess.run([sys.executable, p, "--selftest"], cwd=repo,
                               capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                zlapali.append("selftest:" + nazwa.replace(".py", "")[:12])
        except subprocess.TimeoutExpired:
            zlapali.append("selftest:" + nazwa[:12] + "(TO)")
    for t in TURNIEJE:
        p = os.path.join(repo, t)
        if not os.path.exists(p):
            continue
        try:
            r = subprocess.run([sys.executable, p], cwd=repo,
                               capture_output=True, text=True, timeout=300)
            if r.returncode != 0:
                zlapali.append(os.path.basename(t).replace(".py", ""))
        except subprocess.TimeoutExpired:
            zlapali.append(os.path.basename(t)[:16] + "(TO)")
    return zlapali


def main():
    szybki = "--szybki" in sys.argv
    mutacje = MUTACJE_FUNDAMENT + ([] if szybki else MUTACJE_RESZTA)

    print("=" * 74)
    print("POMIAR MUTACYJNY — czy testy w ogole cos testuja")
    print("=" * 74)
    print("Zasada: test przechodzacy na ZEPSUTYM narzedziu tego nie testuje.")
    print()

    nieodkryte = 0
    niepasujace = 0
    for opis, plik, stare, nowe in mutacje:
        baza, repo = przygotuj_kopie("mut-")
        p = os.path.join(repo, plik)
        if not os.path.exists(p):
            print("  %-38s BRAK PLIKU %s" % (opis[:38], plik))
            shutil.rmtree(baza, ignore_errors=True)
            continue
        s = open(p, encoding="utf-8").read()
        if stare not in s:
            # wzorzec sie rozjechal - to tez informacja, mutacja nie zadziala
            print("  %-38s wzorzec nieaktualny (pomijam)" % opis[:38])
            niepasujace += 1
            shutil.rmtree(baza, ignore_errors=True)
            continue
        open(p, "w", encoding="utf-8").write(s.replace(stare, nowe, 1))

        zlapali = kto_zlapal(repo)
        shutil.rmtree(baza, ignore_errors=True)

        if zlapali:
            print("  %-38s zlapali: %s" % (opis[:38], ", ".join(zlapali[:5])))
            if len(zlapali) > 5:
                print("  %-38s          ...i %d wiecej" % ("", len(zlapali) - 5))
        else:
            nieodkryte += 1
            print("  %-38s >>> NIKT NIE ZLAPAL <<<" % opis[:38])

    print()
    print("=" * 74)
    if niepasujace:
        print("UWAGA: %d wzorcow mutacji jest nieaktualnych - zaktualizuj je,"
              % niepasujace)
        print("       inaczej pomiar bedzie z czasem coraz mniej wart.")
    if nieodkryte:
        print("WYNIK: %d mutacji PRZESZLO NIEZAUWAZONE - to dziury w pokryciu"
              % nieodkryte)
    else:
        print("WYNIK: kazda mutacja zlapana przez co najmniej jeden test")
    print("=" * 74)
    return 1 if nieodkryte else 0


if __name__ == "__main__":
    sys.exit(main())

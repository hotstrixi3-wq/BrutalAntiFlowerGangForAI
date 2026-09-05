#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instaluje hooki gita z dev/hooki/ do .git/hooks/.

Hooki nie sa wersjonowane przez gita (siedza w .git/, ktory nie jest
sledzony), wiec po kazdym `git clone` trzeba je zainstalowac na nowo.
Ten skrypt to robi - jedna komenda, bez pamietania sciezek.

Uzycie:  python3 dev/hooki/zainstaluj.py
"""
import os
import shutil
import stat
import sys

TU = os.path.dirname(os.path.abspath(__file__))
KORZEN = os.path.dirname(os.path.dirname(TU))
CEL = os.path.join(KORZEN, ".git", "hooks")


def main():
    if not os.path.isdir(CEL):
        print("[BLAD] %s nie istnieje - czy to na pewno repozytorium git?" % CEL)
        return 1
    ile = 0
    for nazwa in sorted(os.listdir(TU)):
        if nazwa.endswith(".py") or nazwa.startswith("."):
            continue
        zrodlo = os.path.join(TU, nazwa)
        docelowy = os.path.join(CEL, nazwa)
        shutil.copy2(zrodlo, docelowy)
        st = os.stat(docelowy)
        os.chmod(docelowy, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print("  zainstalowany: %s" % nazwa)
        ile += 1
    if not ile:
        print("[UWAGA] nie znalazlem zadnego hooka w %s" % TU)
        return 1
    print()
    print("Gotowe. Od teraz push nadpisujacy historie wymaga swiezej migawki")
    print("(python3 bakap.py). Zwykly push przechodzi bez zmian.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -------------------------------Zadanie 5-----------------------------------
# Napisz program, który sprawdzi, czy wprowadzone haslo spelnia ponizsze wymagania.
#  Zawiera co najmniej 1 litere alfabety [a − z] oraz [A − Z].
#  Zawiera co najmniej 1 liczbe z przedzialu [0 − 9].
#  Zawiera co najmniej 1 znak specjalny ze zbioru [$#@].
#  Dlugosc hasla jest nie mniejsza niz 6 znaków i nie dluzsza niz 16 znaków.
# Podpowiedz: Sprawdz dokumentacje modulu re a nastepnie zastosuj import re i wykorzystaj zawarte w nim funkcje.

import re


haslo = input('Podaj haslo: ')

if re.fullmatch(r'[A-Za-z0-9$#@]{6,16}', haslo):
    print("Haslo prawidlowe")
else:
    print("Haslo nie spelnia wymagan")
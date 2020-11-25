# -------------------------------Zadanie 3-----------------------------------
# Napisz program, który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax2 + bx + c =
# 0, gdzie a, b i c podaje uzytkownik. Program powinien na pocz¡tku sprawdzic, czy wprowadzone równanie jest
# rzeczywi±cie kwadratowe.


import numpy as np

a=float(input('Wprowadz a: '))
b=float(input('Wprowadz b: '))
c=float(input('Wprowadz c: '))

wspolczynniki=[a,b,c]
wyniki=np.roots(wspolczynniki)
if a==0:
    print('Równanie nie jest kwadratowe')
else:
    print('Pierwiastki rownania: ')
    print(wyniki)
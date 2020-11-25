# -------------------------------Zadanie 9-----------------------------------
# Dla zadanej liczby zespolonej z (wykorzystaj input()) wyznacz jej moduł (|z|) oraz argument (arg(z)). Posiłkując
# się dokumentacją do funkcji conjugate() wyznacz z¯.
import cmath
import math

z=complex(input('Wprowadz liczbe zespolona: '))
print('Z =',z)
print('Moduł |z| = ',math.sqrt(pow(z.real,2)+pow(z.imag,2)))
print('arg(z) = ',cmath.polar(z)[1]) #polar daje nam modul z 'z' oraz jego arg
print('z¯ = ',z.conjugate())
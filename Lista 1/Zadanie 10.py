# -------------------------------Zadanie 10-----------------------------------
# Korzystając z cmath wyznacz część rzeczywistą i urojoną dla sin(z) oraz cos(z), gdzie z = i. Czy wszystko działa
# prawidłowo. Czy spełniona jest zależność sin2(z) + cos2(z) = 1.
import math
import cmath

z=complex(0,1)
print('z = ',z)
print('real z : ',z.real)
print('imag z : ', z.imag)
rt=cmath.polar(z)[1]
print('Kąt: ',rt)
result = pow(math.sin(cmath.polar(z)[1]),2) + pow(math.cos(cmath.polar(z)[1]),2)
print('sin^2({}) + cos^2({}) = '.format(rt,rt),result)

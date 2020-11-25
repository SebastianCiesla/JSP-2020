# -------------------------------Zadanie 3-----------------------------------
#Zmodyfikuj program z Zadania 2 w taki sposób, aby długości boków oraz kąt miedzy nimi były pobierane poprzez
import math

def field(a,b,angle):

    field=0.5*a*b*math.sin(math.radians(angle))
    print('Pole trójkąta wynosi : {}'.format(field))

a = float(input('Podaj bok '))
b = float(input('Podaj bok '))
kat = float(input('Podaj kąt '))

field(a,b,kat)
# -------------------------------Zadanie 2-----------------------------------
#Niech a = 3 i b = 4 będą długościami boków trójkąta, a α = 47◦ kątem między nimi. Wyznacz pole trójkąta
import math


def field(a,b,angle):

    field=0.5*a*b*math.sin(math.radians(angle))
    print('Pole trójkąta wynosi : {}'.format(field))

field(3,4,47)

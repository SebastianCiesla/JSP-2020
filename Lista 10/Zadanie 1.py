# -------------------------------Zadanie 1-----------------------------------
# Napisz klasę w Python o nazwie Koło, konstruowaną za pomocą promienia r i zawierającą dwie metody. Metody
# te obliczają pole i obwód koła.
import math
class Kolo():

    def __init__(self,promien): #inicjowanie klasy
        self.r=promien

    #Metoda wyliczajaca pole
    def pole(self):
        pole = math.pi*math.pow(self.r,2)
        print('Pole wynosi {}'.format(pole))
    #Metoda wyliczająca obwod
    def obwod(self):
        obwod = 2*math.pi*self.r
        print('Obwód wynosi {}'.format(obwod))

k1=Kolo(promien=5)
k1.obwod()
k1.pole()
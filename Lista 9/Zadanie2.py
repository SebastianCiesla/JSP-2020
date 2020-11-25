# -------------------------------Zadanie 2-----------------------------------
# Napisz program statystyka.py, który
# • jako argument wejsciowy przyjmuje dane pomiarowe
# • dane pomiarowe moga byc zapisane w pliku lub wprowadzane recznie, czyli poprawne sa obie formy wywolania
#  python statystyka.py <dane.txt oraz python statystyka.py 1,2,3,4
# • dla danych pomiarowych program oblicza wartosc srednia, wariancja i odchylenie standardowe
# • wyniki wypisywane sa na ekran.
# Do obliczenia wartosci sredniej, wariancji i odchylenia standardowego wykorzystaj modul NumPy.
# argumenty wiersza polecen
import numpy as np
import  sys

def statystyka(dane):

    a = np.array(dane)

    srednia = np.mean(a)    #wylicza srednia
    wariacja = np.var(a)    #wylicza wariacje
    odch_stand = np.std(a)  #wylicza odchylenie standardowe

    #Tekst sklada wszystko razem do wyprintowania
    tekst='''
Dane: {}
Średnia: {}
Wariacja: {}
Odchylenie standardowe: {}
'''.format(dane,srednia,wariacja,odch_stand)

    print(tekst)


#statystyka([1,2,3,4])
dane=sys.argv[1:]

statystyka([float(x) for x in dane])
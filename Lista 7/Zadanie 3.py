# -------------------------------Zadanie 3-----------------------------------
# Napisz program sortujący listę w oparciu o algorytm Sortowania bąbelkowego. Zmierz czas działania programu dla
# list wykorzystanych w zadaniu 2.
from time import time as t
import random

#Algorytm na sortowanie babelkowe
def sortowanie_babelkowe(lista):

    posort=lista.copy()
    n=len(lista)-1                           # algorytm wykonuje sie n-1 razy
    while n!=0:                              # za każdym wywołaniem zmniejsza sie range
        for i in range(n):                   # jeśli spełni sie warunek, to dojdzie do zamiany
            if posort[i] > posort[i+1]:      # wstawiam i+1 na miejsce i, potem usuwam i+2 inaczej by sie skopiowalo
                posort.insert(i,posort[i+1]) # i lista wejsciowa by sie powiekszala
                posort.pop(i+2)
        n-=1

#Algorytm na sortowanie przez wstawienie z poprzedniego zadania
def sortowanie_wstawianie(lista):


    posortowane=[]
    #Tworzenie postawy
    if lista[0]<=lista[1]:
        posortowane.append(lista[0])
        posortowane.append(lista[1])
    else:
        posortowane.append(lista[1])
        posortowane.append(lista[0])

    #algorytm

    for i in range(2,len(lista)):

        poz=i-1
        while True:
            if lista[i] > posortowane[poz] and poz>=0:
                posortowane.insert(poz+1,lista[i])
                break
            elif poz<0:
                posortowane.insert(0,lista[i])
                break
            else:
                poz-=1


#Funckja mierzaca czas wykonywania danej funkcji mc(funkcja badana, lista)
def mierzenie_czasow(funkcja,l):

    a=t()
    funkcja(l)
    b=t()
    c=b-a
    print('Funkcja: ',funkcja.__name__,' z lista o dlugosci: {} '.format(len(l)) ,' wykonała się w : {}'.format(c))

#Funkcja zwracajaca liste zawierajaca 3 inne listy
def stworz_listy():
    l1 = [random.randint(0, 20) for _ in range(100)]
    l2 = [random.randint(0, 20) for _ in range(200)]
    l3 = [random.randint(0, 20) for _ in range(300)]

    lc=[l1,l2,l3]

    return lc

#Lista funkcji do sprawdzenia
funk=[sortowanie_babelkowe,sortowanie_wstawianie]

#Dla kazdej funkcji i kazdej listy wykonuje mierzenie czasu ich dzialania
for funkcja in funk:
    for l in stworz_listy():
        mierzenie_czasow(funkcja,l)

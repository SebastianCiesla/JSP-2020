# -------------------------------Zadanie 2-----------------------------------
# Napisz program sortujący listę w oparciu o algorytm Sortowanie przez wstawianie. Zmierz czas działania programu
# dla list zawierających 100, 200 i 300 elementów z przedziału < 0, 20 >. Listy wygeneruj stosując random.randint
import time
from time import time as t
import random

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





#Generowanie 3 list o roznych dlugosciach
l1=[random.randint(0,20) for _ in range(100)]
l2=[random.randint(0,20) for _ in range(200)]
l3=[random.randint(0,20) for _ in range(300)]

#Mierzenie czasu dla 100 elemnt listy
a1=t()
sortowanie_wstawianie(l1)
a2=t()
a=a2-a1
#Mierzenie czasu dla 200 element listy
b1=t()
sortowanie_wstawianie(l2)
b2=t()
b=b2-b1
#Mierzenie czasu dla 300 element listy
c1=t()
sortowanie_wstawianie(l3)
c2=t()
c=c2-c1
#Wyswietlanie wynikow
print('Czas dla 100 elementow : {}'.format(a))
print('Czas dla 200 elementow : {}'.format(b))
print('Czas dla 300 elementow : {}'.format(c))
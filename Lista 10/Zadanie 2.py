# # -------------------------------Zadanie 2-----------------------------------
# Napisz klasę w Python, inicjalizowana za pomocą listy, która zawiera metodę zwracającą wszystkie "podlisty"
# podanej listy. Np. [1, 2, 3] → [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

import itertools
class Klasa():

    def __init__(self,lista):
        self.lista=lista

    #Metoda klasy
    def podlisty(self):
        koniec=[]
        for n in range(len(self.lista)+1):
            x=itertools.combinations(self.lista,n)  #Wszystkie kombinacje listy  (n-zmienna)
            for element in x:   # ta pętla tylko dla estetyki, by wszystko było w listach a nie krotkach
                gotowe=[]
                for i in element:
                    gotowe.append(i)
                koniec.append(gotowe)
        print(koniec)


a=Klasa([1,2,3])
a.podlisty()
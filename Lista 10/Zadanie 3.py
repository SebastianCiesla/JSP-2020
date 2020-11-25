# -------------------------------Zadanie 3-----------------------------------
# Napisz klasę w Python, inicjalizowana za pomocą listy n liczb rzeczywistych. Klasa powinna zawierać metodę
# zwracającą trójelementowe "podlisty", takie że, suma elementów "podlisty" wynosi 0.


import itertools
class Klasa():

    def __init__(self,lista):   #Inicjowanie
        self.lista=lista

    #Metoda klasy
    def podlisty3_sum0(self):
        koniec=[]

        x=itertools.combinations(self.lista,3)  #Wszystkie 3 elementow combinacje zbioru n elementowego

        #Wybieramy tylko te, których suma jest 0
        for element in x:
            gotowe=[]
            for i in element:
                gotowe.append(i)
            if sum(gotowe)==0:
                koniec.append(gotowe)
        print(koniec)

#jakis przyklad
a=Klasa([1,2,3,-4,2,-2,-5])
a.podlisty3_sum0()

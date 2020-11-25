# -------------------------------Zadanie 6-----------------------------------
#Napisz program, który wydrukuje tablice mnozenia i ∗ j, gdzie i wprowadza uzytkownik a j = 1, 2, . . . , 10.

i=int(input('Wprowadz i: '))

lista=[element*i for element in range(1,11) ]

print(lista)


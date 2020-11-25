# -------------------------------Zadanie 2-----------------------------------
#Napisz funkcję, która jako argument dostaje listę i usuwa w niej wszystkie powtarzające się elementy. Np. dla
#[1, 1, 1, 2] otrzymamy [1, 2]


def remove_duplicate1(lista):

    print(list(set(lista)))

def remove_duplicate2(lista):

    lista_end=[]

    for element in lista:
        if element not in lista_end:
            lista_end.append(element)

    print(lista_end)


l=[1, 3,1,2,1, 1, 2,3,2,1,3,1,2]

remove_duplicate1(l)
remove_duplicate2(l)
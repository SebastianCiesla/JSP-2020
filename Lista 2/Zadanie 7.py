# -------------------------------Zadanie 7-----------------------------------
# Sprawdź dokumentację funkcji sorted. Na tej podstawie napisz program, który uporządkuje rosnąco listę ze
# względu na jej drugi element. Np. [(2, 5),(1, 2),(4, 4)] zamieni na [(1, 2),(4, 4),(2, 5)]. Lista do uporządkowania
# to [(2, 8),(5, 5),(9, 3),(1, 0),(3, 2),(6, 4),(1, 9),(10, 3),(2, 3),(1, 7)].


def keyFun(e):
    return e[1]

lista=[(2, 8),(5, 5),(9, 3),(1, 0),(3, 2),(6, 4),(1, 9),(10, 3),(2, 3),(1, 7)]
lista.sort(key=keyFun)
print(lista)
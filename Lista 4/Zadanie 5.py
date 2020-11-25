# -------------------------------Zadanie 5-----------------------------------
#Napisz program, który wypisze wszystkie permutacje podanej listy

import itertools

def perm(lista):
    x=list(itertools.permutations(lista,len(lista)))
    print(x)
    
l=[1,2,3]
perm(l)
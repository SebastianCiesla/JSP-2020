# -------------------------------Zadanie 5-----------------------------------
# Napisz program, który wczyta od użytkownika pewien napis, a następnie w środek wstawi inny napis.
# Np. '[[]]' zamieniamy na '[[Python]]'.

napis1=input('Wprowadz napis 1: ')
napis2=input('Wprowadz napis 2: ')

n=len(napis1)//2
napis1=napis1[0:n]+napis2+napis1[n:]
print(napis1)
# -------------------------------Zadanie 4-----------------------------------
# Napisz program, który wczyta od użytkownika pewien napis, a następnie wszystkie znaki identyczne z pierwszym
# znakiem naszego napisu zostaną zamienione na 0$0, z wyjątkiem pierwszego znaku. Np. 0restart0zamieniamy na0resta$t0.

napis=input('Napis : ')
print(napis)
napis2=napis[0]+napis[1:].replace(napis[0],'$')
print(napis2)
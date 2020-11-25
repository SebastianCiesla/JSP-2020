# -------------------------------Zadanie 8-----------------------------------
# Niech a i b będą liczbami wprowadzanymi poprzez input() takimi, że b < a. Używając instrukcji Pythona oblicz
# resztę z dzielenia b przez a i zapamiętaj wynik w zmiennej o nazwie Z. Następnie, pojedynczym poleceniem Pythona
# i bez użycia nawiasów, przemnóż zmienną Z przez Z + 3. Wyświetl wynik poleceniem print. Wskazówka: Pamiętaj,
# że x = x + 1 można zapisać jako x+ = 1.

a=float(input('Wprowadz a: '))
b=float(input('Wprowadz b: '))
while b>a:
    b = float(input('Wprowadz b<a: '))

z=b%a
print('Reszta z: ',z)
z*=z+3
print('Wynik z=z(z+3) = ',z)
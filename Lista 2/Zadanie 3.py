# -------------------------------Zadanie 3-----------------------------------
# Napisz program, który wczyta od użytkownika pewien napis, a następnie utworzy nowy napis składający się z dwóch
# pierwszych i dwóch ostatnich znaków początkowego napisu


napis=input('Wprowadz napis : ')
print(napis)
res=napis[0:2]+napis[-2:]
print(res)
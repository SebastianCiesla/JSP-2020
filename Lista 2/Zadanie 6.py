# -------------------------------Zadanie 6-----------------------------------
# Stwórz listę studentów: Kasia, Basia, Marek, Darek.
# • Korzystając z funkcji append dodaj do listy Józka.
# • Korzystając z funkcji extend dodaj do listy Anię i Basię.
# • Posortuj alfabetycznie studentów.
# • Wypisz na ekranie:
# – czwartego studenta na liście
# – dwóch pierwszych studentów na liście
# – dwóch ostatnich studentów na liście
# • Korzystając z funkcji remove usuń wszystkie Basie.
# • Korzystając z funkcji len sprawdź ilość studentów.
# • Z ostatecznej listy studentów utwórz krotkę.


lista_studendtow=['Kasia', 'Basia', 'Marek', 'Darek']
print(lista_studendtow)
lista_studendtow.append('Józek')
print(lista_studendtow)
lista_studendtow.extend(['Ania','Basia'])
print(lista_studendtow)
lista_studendtow.sort()
print(lista_studendtow)
print(lista_studendtow[3])
print(lista_studendtow[0:2])
print(lista_studendtow[-2:])
for x in range(2): lista_studendtow.remove('Basia')
print(lista_studendtow)
print(len(lista_studendtow))
print(tuple(lista_studendtow))
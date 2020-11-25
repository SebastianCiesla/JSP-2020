# -------------------------------Zadanie 10-----------------------------------
#• Korzystając z range utwórz listę zawierającą wszystkie wielokrotności liczby 3 mniejsze od 100.
# • Korzystając z del usuń co trzeci element (zaczynając od piątego).
# • Sprawdź definicję funkcji wbudowanej sum. Wykorzystaj ją, aby wyliczyć średnią arytmetyczną otrzymanej
#   listy.

x= list(range(0,100,3))
print(x)
print(x.index(12))
y=list(element for element in x if x.index(element)%5==0 )
print(y)
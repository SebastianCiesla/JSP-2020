# -------------------------------Zadanie 2-----------------------------------
# Napisz program, który wczyta od uzytkownika liczbe calkowita i wyswietli informacje, czy jest to liczba parzysta,
# czy nieparzysta. Nastepnie napisz analogiczny program ale bez uzycia instrukcji if.


liczba=int(input('Wpisz liczbe: '))

if liczba%2==0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


print('Sposób bez if')

liczby=["Liczba parzysta","Liczba nieparzysta"]

liczba=int(input('Wpisz liczbe: '))
print(liczby[liczba%2])
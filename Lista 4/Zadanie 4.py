# -------------------------------Zadanie 4-----------------------------------
# Zdefiniuj funkcję, która dla podanych trzech parametrów: n =numer elementu ciągu, a1 =wartość pierwszego
# elementu ciągu (domyślnie 1), q =wartość iloczynu ciągu geometrycznego (domyślnie 2) zwróci n−ty element ciągu
# geometrycznego.


def geom(n,a1=1,g=2):

    a_n=a1*g**(n-1)
    print('N-ty wyraz ciągu: ',a_n)

geom(3,2,3)
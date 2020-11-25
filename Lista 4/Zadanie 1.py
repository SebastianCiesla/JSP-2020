# -------------------------------Zadanie 1-----------------------------------
#Napisz program, który policzy sumę i/lub iloczyn wszystkich elementów z podanej listy


def program(lista):

    decyzja=input('Aby policzyć sumę wpisz (s), aby iloczyn (i), jeśli sume i iloczyn (a)')
    #Iloczyn#######
    x = 1
    for e in lista:
        x = e * x
    ##############
    if decyzja=='s':
        print('SUMA: ')
        print(sum(lista))
    elif decyzja=='i':
        print('ILOCZYN:')
        print(x)
    elif decyzja == 'a':
        print('SUMA: ',sum(lista))
        print('ILOCZYN: ',x)
    else:
        print('Bład')


l=[1,2,3,4]
program(l)
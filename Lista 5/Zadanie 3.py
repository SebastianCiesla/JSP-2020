# -------------------------------Zadanie 3-----------------------------------
#   Napisz funkcje, która przeliczy wprowadzona liczbe rzymska na jej postac dziesietna

def conventer():

    dictio={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    napis=input('Wprowadz liczbe: ')
    napis2=[x for x in napis]
    napis3=[dictio[e] for e in napis2]
    napis4=[]
    #liczenie
    #Obsluga wszystkich elementow oprocz ostatniego
    for i in range(len(napis3)-1):
        #zgodnie z algorytmem jesli z przodu jest wieksza to odejmuje i dodaje liczbe do listy 4
        if napis3[i]<napis3[i+1]:
            result=napis3[i+1]-napis3[i]
            napis4.append(result)
        # jesli mamy doczynienia z syfuacja [1,10,5] pomijamy '10' bo 10 i 1 zostalo juz odjete
        elif napis3[i]>napis3[i+1] and napis3[i]>napis3[i-1] and i!=0:
            pass
        else:
            napis4.append(napis3[i])
    #Obsluga ostatniego elementu
    if napis3[-1]<=napis3[-2]:
        napis4.append(napis3[-1])
    #Wynik
    print('{} to {}'.format(napis,sum(napis4)))

conventer()
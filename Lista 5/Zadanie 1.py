# -------------------------------Zadanie 1-----------------------------------
# Napisz funkcje, która zamieni podana przez uzytkownika zapisana slownie wartosc (z zakresu od 1 do 59) na
# odpowiadajaca jej liczbe dziesietna

def zamiana():
    #słownik
    dict={
        'jeden':'1',
        'dwa':'2',
        'trzy':'3',
        'cztery':'4',
        'pięć':'5',
        'sześć':'6',
        'siedem':'7',
        'osiem':'8',
        'dziewięć':'9',
        'dziesięć':'10',
        'dwadzieścia':'20',
        'trzydzieści':'30',
        'czterdzieści':'40',
        'pięćdziesiąt':'50'

    }

    napis=input('Podaj liczbę z zakresu 1-59: ')
    splited=napis.split()
    res=''
    #dla liczb jednowyrazowych
    if len(splited)==1:
        if 'naście' in napis:
            res+='1'
            for key in dict.keys():
                if napis[0:3] == key[0:3] and len(dict[key])==1:
                    res+=dict[key]
        else:
            res+=dict[napis]
    #dla liczb dwu wyrazowych np. dwadziescia piec
    if len(splited)>1:
        for e in splited:
            res+=dict[e]
        res=res[0]+res[-1]

    print(res)

zamiana()






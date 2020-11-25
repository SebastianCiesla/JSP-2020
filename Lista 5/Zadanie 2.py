# -------------------------------Zadanie 2-----------------------------------
#Napisz funkcje, która dla wprowadzonej liczby dziesietnej (z zakresu 1-1999) wyswietli jej wartosc zapisan¡ slownie.

def zamiana():
    #słownik
    dict={
        '1':'jeden',
        '2':'dwa',
        '3':'trzy',
        '4':'cztery',
        '5':'pięć',
        '6':'sześć',
        '7':'siedem',
        '8':'osiem',
        '9':'dziewięć',
        '10':'dziesięć',
        '20':'dwadzieścia',
        '30': 'trzydzieści',
        '40':'czterdzieści',
        '50':'pięćdziesiąt',
        '60':'sześćdziesiąt',
        '70':'siedemdziesiąt',
        '80':'osiemdziesiąt',
        '90':'dziewięćdziesiąt',
        '100':'sto',
        '1000':'tysiąc'
    }
    res=''
    l=[]
    l1='10000'
    liczba=int(input('Liczba: '))
    #dziele liczbe na tys,setki, dziesiatki i jednosci do listy l
    for i in range(4):
        r=liczba%int(l1)
        l.append(r)
        l1=l1[:-1]
    print(l)
    #jesli liczba jest 4 cyfrowa dodaje tysiac
    if len(str(liczba))==4:
        res+='Tysiąc '

    #jesli jest 3 cyfrowa
    if len(str(l[1]))==3:
        if str(l[1])[0]=='1':
            res+='sto '
        elif str(l[1])[0]=='2':
            res+='dwieście '
        elif str(l[1])[0]=='3' or str(l[1])[0]=='4':
            res += dict[str(l[1])[0]] + 'sta '
        else:
            res+=dict[str(l[1])[0]]+'set '

    #dzielenie liczby np 25 na 20
    lic2=str(l[-2])
    lic2=lic2[0]+'0'
    l[-2]=lic2

    if len(str(l[-2]))==2:
        if l[-1] == 0:
            if lic2[0]=='0':
                pass
            else:
                res += dict[str(l[-2])]
        elif lic2[0]=='1': #obsługa od 11-19
            dozwolone=[2,3,7,8]
            niedozwolone=[5,9]
            if l[-1] in dozwolone:
                res += dict[str(l[-1])]+'naście'
            elif l[-1] in niedozwolone:
                res += dict[str(l[-1])][:-1] +'tnaście'
            elif l[-1]==1:
                res += 'jedenaście'
            elif l[-1]==4:
                res += 'czternaście'
            elif l[-1]==6:
                res += 'szesnaście'
        #dodawanie do liczby dwucyfrowej drugiej cyfry np 25 -> 5
        else:
            res += dict[str(l[-2])]+' ' # liczy sa dzielona na 20 i 5 i laczane
            res += dict[str(l[-1])]

    print(res)
zamiana()
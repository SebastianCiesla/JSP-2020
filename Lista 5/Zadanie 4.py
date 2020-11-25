# -------------------------------Zadanie 4-----------------------------------
# Dany jest szyfr, który zamienia samogloski wg klucza: klucz = {”a” : ”y”, ”e” : ”i”, ”i” : ”o”, ”o” : ”a”, ”y” : ”e”}.
# Czyli wszystkie a zamienia na y itd.
# Np. tekst: to jest moj tekst po przepuszczeniu przez szyfr wygladac bedzie
# nastapujaco: ta jist maj tikst.
# Napisz funkcje do szyfrowania i deszyfrowania tekstu. Przetestuj szyfrowanie i deszyfrowanie na kilku przykladach.


def szyfrowanie(tekts):

    klucz= {'a' : 'y',
            'e' : 'i',
            'i' : 'o',
            'o': 'a',
            'y' : 'e'
            }
    tekst2=''
    for letter in tekts:
        if letter in klucz.keys():
            tekst2+=klucz[letter]
        else:
            tekst2+=letter

    print('Oryginał: ')
    print(tekts)
    print('Zmieniony: ')
    print(tekst2)
    return tekst2

def deszyfrowanie(tekst):

    klucz = {'a': 'y',
             'e': 'i',
             'i': 'o',
             'o': 'a',
             'y': 'e'
             }

    #odwracanie klucza
    klucz2={}
    for i in klucz.items():
        klucz2[i[1]]=i[0]

    #petla z pierwszej czesci
    tekst2 = ''
    for letter in tekst:
        if letter in klucz2.keys():
            tekst2 += klucz2[letter]
        else:
            tekst2 += letter

    print('Odszyfrowane:')
    print(tekst2)

t='to jest moj tekst'
x=szyfrowanie(t)
deszyfrowanie(x)
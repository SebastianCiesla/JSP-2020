# -------------------------------Zadanie 1-----------------------------------
# W oparciu o Zadanie 2 z listy 6 napisz program, który:
# • pobiera od użytkownika ścieżkę do pliku txt np. plik_do_szyfrowania.txt. Przykład pliku podany na dole.
# • wczytuje ten plik i szyfruje zawartą w nim treść stosując szyfr Cezara. Odpowiednie przesunięcie (w zakresie
#   1 − 10) wprowadza użytkownik.
# • zaszyfrowaną treść zapisujemy do pliku o nazwie plik_zaszyfrowany%n_%Y%m%d.txt, gdzie %n oznacza
#   przesunięcie szyfrujące, %Y%m%d oznacza rok-miesiąc-dzień
# • plik plik_zaszyfrowany%n_%Y%m%d.txt na być zapisany w katalogu podanym przez użytkownika. Jeśli takiego
#   katalogu (takich katalogów) nie ma, należy je stworzyć.

# Program powinien uwzględniać odpowiednie wyjątki np. błąd odczytu plik_do_szyfrowania.txt, błąd zapisu katalogów
# lub pliku plik_zaszyfrowany%n_%Y%m%d.txt itd.

import os
import datetime
import SzyfrCezara


def zadanie1():

    #Wczytywanie pliku
    while True:
        try:
            path=input('Podaj ścieżkę do pliku: ')
            file=open(path,'r')
            lista=[element for element in file]
            break
        except FileNotFoundError:                   # Obsluga bledu zlej sciezki do pliku
            print('Zła nazwa pliku')

    # Wczytywanie przesuniecia
    while True:                                     # program przepusci nas dalej jesli zostanie spelniny warunek 1-10
        przesuniecie = int(input('Podaj przesunięcie z przediału 1-10: '))
        if przesuniecie >=1 and przesuniecie<=10:
            break
        else:
            print('Liczba nie jest z przedziału')

    #Szyfrowanie

    koniec=[SzyfrCezara.szyfrowanie(elemnt,przesuniecie) for elemnt in lista]


    #Zapis pliku
    y=datetime.datetime.now().year
    m=datetime.datetime.now().month
    d=datetime.datetime.now().day
    path2='\plik_zaszyfrowany{}_{}{}{}.txt'.format(przesuniecie,y,d,m)
    while True:
        try:
            katalog=input('Podaj katalog zapisu: ')
            kat= os.path.join(katalog)
            if not os.path.exists(kat):
                os.makedirs(kat)
            name_end=r'{}\{}'.format(kat,path2)
            file2=open(name_end,'a')
            for elm in koniec:
                file2.write(elm)
            file2.close()
            break
        except FileNotFoundError:
            print('''Zła ścieżka do katalogu c\ users \ ...''')
            
    print('Zakończono szyfrowanie')

zadanie1()



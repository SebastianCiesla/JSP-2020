# -------------------------------Zadanie 2-----------------------------------
# W oparciu o powyższe zadanie oraz Zadanie 2 z listy 6 napisz program deszyfrujący, który:
# • pobiera od użytkownika ścieżkę do katalogu, w którym są zaszyfrowane pliki
#  plik_zaszyfrowany%n_%Y%m%d.txt
# • w podanym katalogu program odnajduje odpowiednie pliki i przeprowadza ich deszyfrowanie
# • wartość przesunięcia szyfrującego odczytywana jest z nazwy pliku
# • końcowy wynik zapisać do plik o nazwie plik_deszyfrowany%n_%Y%m%d.txt, gdzie wszystkie oznaczenia jak
#   w zadaniu 1
# Jak wyżej, weź pod uwagę ewentualno błędy IO itd.

import glob
import os
import SzyfrCezara
import datetime

def zadanie2():

    #Wczytywanie katalogu
    while True:
        try:
            path_dir=input('Podaj ścieżkę do pliku: ')
            os.chdir(path_dir)
            for files in glob.glob("*.txt"):
                pa=files                                #szukanie plikow .txt w podanym katalogu
                file=open(files,'r')
                lista=[element for element in file]
                print(lista)
            break
        except FileNotFoundError:                   # Obsluga bledu zlej sciezki do pliku
            print('Zła nazwa pliku')
        except NotADirectoryError:
            print('Niepoprawna nazwa katalogu')

    #Wczytanie przesuniecia z pliku

    key=pa.split('plik_zaszyfrowany')[1][0] #Numer do deszyfracji

    #Odszyfrowywanie

    end=[SzyfrCezara.odszyfrowanie(e,int(key)) for e in lista]

    #Zapis do pliku

    # Zapis pliku
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    path2 = '\plik_deszyfrowany{}_{}{}{}.txt'.format(key, y, d, m)
    while True:
        try:
            katalog = input('Podaj katalog zapisu: ')
            kat = os.path.join(katalog)
            if not os.path.exists(kat):
                os.makedirs(kat)
            name_end = r'{}\{}'.format(kat, path2)
            file2 = open(name_end, 'a')
            for elm in end:
                file2.write(elm)
            file2.close()
            break
        except FileNotFoundError:
            print('''Zła ścieżka do katalogu c\ users \ ...''')

    print('Zakończono odszyfrowanie')



zadanie2()
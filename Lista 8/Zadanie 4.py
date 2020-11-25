# -------------------------------Zadanie 4-----------------------------------
# Napisz program, który wczyta plik PESEL.txt (jeśli istnieje) a następnie z na podstawie nr PESEL:
# • sprawdzi czy PESEL jest poprawnie zdefiniowany (tzn. czy ostatnia cyfra jest prawidłowa)
# • jeśli PESEL jest prawidłowy, odczyta datę urodzenia oraz płeć
# • wyniki w formie "nr PESEL:\n data urodzenia %d-%m-%Y;\t płeć: %płeć" zapisze do pliku.

import math

def zadanie4():

    #Wczytywanie pliku
    path=input('Podaj scieżke do pliku PESEL: ')

    file = open(path,'r')

    peselend=[]
    for pesel in file:

        #Sprawdzanie poprawnosci numeru
        pesel=pesel[:-1]
        pl=[int(n) for n in pesel]

        wynik=1*pl[0] + 3*pl[1] + 7*pl[2] + 9*pl[3] + 1*pl[4] + 3*pl[5] + 7*pl[6] + 9 * pl[7] + 1*pl[8] + 3*pl[9] + 1*pl[10]

        #Jesli pesel zgodny przeprowadzany jest proces odkodowania danych
        if wynik%10 == 0:

            #Odczytywanie roku
            rok2=pesel[0:2]

            #Odczytywanie miesiaca

            miesiac=pesel[2]+pesel[3]
            if pesel[2] == 0 :
                a = int(pesel[3])
                rok1='20'
            elif pesel[2] == 1:
                a = miesiac
                rok1='20'
            else:
                l=int(miesiac)

                if  81<= l <=92:
                    a=l-80
                    rok1='18'
                elif 21<= l <=32:
                    a=l-20
                    rok1 = '20'
                elif 41 <= l <= 52:
                    a=l-40
                    rok1 = '21'
                elif 61 <= l <= 72:
                    a=l-60
                    rok1 = '22'

            rokc=rok1+str(rok2)
            miesiacc=str(a)

            #Odczytywanie dnia
            dzien = pesel[4] + pesel[5]
            if pesel[4] == 0:
                dzien = dzien[-1]

            #Płeć
            if int(pesel[9])%2==0:
                pl='Kobieta'
            else:
                pl='Mężczyzna'
            mess='Numer PESEL: ' + pesel +'\n' + 'Data urodzenia: {}-{}-{}'.format(dzien,miesiacc,rokc) +'\t'+'Płeć: '+ pl

            peselend.append(mess)
        #Jesli nie zgadza sie pesel to zapisuje odpowiedni komunikat
        else:
            mess='Numer PESEL: '+pesel+' jest niepoprawny'
            peselend.append(mess)

    path2='PESEL_odczytany.txt'
    file2 = open(path2,'a')
    for e in peselend:
        file2.write(e+'\n'+'\n')

    file2.close()
    print('Gotowe')

zadanie4()
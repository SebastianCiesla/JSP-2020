# -------------------------------Zadanie 3-----------------------------------
# Napisz program, który losowo generuje nr PESEL (10 razy) i zapisuje do pliku PESEL.txt

import random
import math
def zadanie3():

    numery_pesel=[]
    for _ in range(10):

        pesel = ''

        dzien=random.randint(1,31)
        miesiac=random.randint(1,12)
        rok=random.randint(1800,2299)

        #Okreslenie miesiaca w danym stuleciu
        wynik=math.floor(rok/100)
        if wynik == 18:
            miesiac+=80
        elif wynik == 19:
            miesiac += 0
        elif wynik == 20:
            miesiac+=20
        elif wynik == 21:
            miesiac+=40
        else:
            miesiac+=60



        #Aby zgadzały się 0 przed datami jednocyfrowymi dla miesiecy z 19 wieku i dni 1-9
        if dzien<10:
            nd='0'+str(dzien)
        else:
            nd=str(dzien)

        if wynik == 19 and miesiac<10:
            nm='0'+str(miesiac)
        else:
            nm=str(miesiac)
        #Tworzenie numeru opierac sie o same daty
        pesel += str(rok)[2:] + nm + nd


        for _ in range(4):
            x=random.randint(0,9)
            pesel+=str(x)
        #numer skonczony

        #Liczenie cyfry kontrolnej
        pl=[int(n) for n in pesel]

        s1= 1*pl[0] + 3*pl[1] + 7*pl[2] + 9*pl[3] + 1*pl[4] + 3*pl[5] + 7*pl[6] + 9 * pl[7] + 1*pl[8] + 3*pl[9]
        s2=s1%10
        s3=10-s2
        if s3!=10:
            pesel+=str(s3)
        else:
            pesel+='0'
        numery_pesel.append(pesel)
    #Zapisywanie do pliku

    file=open('PESEL.txt','a')
    for element in numery_pesel:
        file.write(element+'\n')
    file.close()

zadanie3()
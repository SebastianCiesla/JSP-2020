# -------------------------------Zadanie 4-----------------------------------
# Napisz program do przeliczania walut. Kursy walut wczytywane z pliku xml (można pobrać np. z
# https://www.nbp.pl/home.aspx?f=/kursy/kursya.html). Główna klasa powinna być inicjalizowana ścieżką do pliku
# xml, np. kursy = Kursy("/moja/ścieżka/do/pliku.xml"). Program powinien posiadać poniższe opcje:
# • lista dostępnych kursów
# • konwersja PLN ⇔ wybrana waluta
# • konwersja wybrana waluta ⇔ wybrana waluta


from xml.etree import ElementTree
from tkinter import *
import pandas as pd

class KursyWalut():

    def __init__(self,plik):
        self.plik=plik


    def start(self):                    #Start kalkulatora

        MainRoot = Tk()
        MainRoot.title('Kursy walut')       #Inicjowanie tkinkera z oknem

        def obsluga_danych(dane):           #Funckja zamieniajaca dane z xlm do pandasa

            tree = ElementTree.parse(dane)
            root = tree.getroot()

            nazwa_waluty=[]
            przelicznik=[]
            kod_waluty=[]
            kurs_sredni=[]
            for nw in root.iter('nazwa_waluty'):
                nazwa_waluty.append(nw.text)
            for nw in root.iter('przelicznik'):
                nw2=float(nw.text)
                przelicznik.append(nw2)
            for nw in root.iter('kod_waluty'):
                kod_waluty.append(nw.text)
            for nw in root.iter('kurs_sredni'):
                nw2=nw.text.replace(',','.')
                nw3=float(nw2)
                kurs_sredni.append(nw3)

            data={'Nazwa waluty':nazwa_waluty,'Przelicznik':przelicznik,'Kod waluty':kod_waluty,'Kurs średni':kurs_sredni}
            df=pd.DataFrame(data=data)

            return df                           #zwraca dataframe z danymi

        global baza
        baza=obsluga_danych(self.plik)           # nasza 'baza' danych

        # Funckja wyswietlajaca kursy walut
        def lista():

            listaroot=Tk()
            listaroot.title('Lista kursów')

            i=0
            for tyt in baza.columns.tolist():
                nazwy=Label(listaroot,text=tyt)
                nazwy.grid(row=0,column=i)
                i+=1
            n=0
            for nazwa in baza.columns.tolist():
                n1=1
                for nazwa2 in baza[nazwa].values:
                    tabela=Label(listaroot,text=nazwa2)
                    tabela.grid(row=n1,column=n)
                    n1+=1
                n+=1

        # Funckja zamieniajaca PLN -> dowonla walute i odwrotnie
        def wym_pl():

            wympl=Tk()
            wympl.title('Wymiana PLN -> Wybraną waluta')

            # Zamiana PLN -> dowolna waluta
            def przelicz1():
                wynik1=Label(wympl,text=cl.get())
                wynik1.grid(row=0,column=4)
                zl=float(entry1.get())
                indx=baza.index[baza['Nazwa waluty'] == cl.get()].tolist()
                waluta_obca1 = baza.iloc[indx[0],3]
                waluta_obca2 = baza.iloc[indx[0],1]
                calc= (zl * waluta_obca2 ) / ( waluta_obca1)
                wynik2=Label(wympl,text=round(calc,2))
                wynik2.grid(row=1,column=4)

            # Zamiana dowolnej waluty -> PLN
            def przelicz2():

                wynik1=Label(wympl,text=cl2.get())
                wynik1.grid(row=4,column=2)
                waluta_obca=float(entry2.get())
                indx = baza.index[baza['Nazwa waluty'] == cl2.get()].tolist()
                waluta_obca1 = baza.iloc[indx[0], 3]
                waluta_obca2 = baza.iloc[indx[0], 1]
                wynik = waluta_obca * waluta_obca1 / waluta_obca2
                wynik2 = Label(wympl, text=round(wynik,2))
                wynik2.grid(row=5, column=4)

            #Opcja 1
            opcje=baza['Nazwa waluty'].values
            cl = StringVar()

            #Guziory 1

            opcje1 = OptionMenu(wympl,cl,*opcje)
            pln1 = Label(wympl,text='PLN')
            entry1 = Entry(wympl,width=7, borderwidth=5)
            przelicz1 = Button(wympl,text='Przelicz', padx=30, pady=10, command=przelicz1)
            rowno1= Label(wympl,text=' ⇔ ')
            #kreski
            i=0
            for i in range(7):
                kreski = Label(wympl, text=('-' * 15))
                kreski.grid(row=3, column=i)
            # napisy
            napis1=Label(wympl,text='<---Wybierz walutę')
            napsi2=Label(wympl,text='Wybierz walutę--->')
            napis1.grid(row=0,column=6)
            napsi2.grid(row=4,column=0)
            # Gridy
            pln1.grid(row=0,column=2)
            opcje1.grid(row=0,column=5)
            entry1.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
            przelicz1.grid(row=2,column=3)
            rowno1.grid(row=1,column=3)


            #Opcja 2
            cl2 =  StringVar()
            #Guziory 2
            opcje2=OptionMenu(wympl,cl2,*opcje)
            pln2= Label(wympl,text='PLN ')
            entry2 = Entry(wympl, width=7, borderwidth=5)
            przelicz2 = Button(wympl, text='Przelicz', padx=30, pady=10, command=przelicz2)
            rowno2 = Label(wympl, text=' ⇔ ')
            #Gridy 2
            pln2.grid(row=4, column=4)
            opcje2.grid(row=4, column=1)
            entry2.grid(row=5, column=2, columnspan=1, padx=10, pady=10)
            przelicz2.grid(row=6, column=3)
            rowno2.grid(row=5, column=3)

        #Funkcja do zamiany dowolnej waluty
        def w_w():

            ww=Tk()
            ww.title('Wymiana dowolnej waluty')
            #Funkcja przeliczająca walute
            def przelicz1():
                napis1 = Label(ww,text=cl.get())
                napis2 = Label(ww, text=cl2.get())

                #przeliczanie
                indx1 = baza.index[baza['Nazwa waluty'] == cl.get()].tolist()
                waluta_licznik1 = baza.iloc[indx1[0], 3]
                waluta_mianownik1 = baza.iloc[indx1[0], 1]
                wsp1 = waluta_licznik1/waluta_mianownik1 #współczynnik 1

                indx2 = baza.index[baza['Nazwa waluty'] == cl2.get()].tolist()
                waluta_licznik2 = baza.iloc[indx2[0], 3]
                waluta_mianownik2 = baza.iloc[indx2[0], 1]
                wsp2 = waluta_licznik2 / waluta_mianownik2  # współczynnik 2

                wartosc=float(entry1.get())

                wynik = round(wartosc*wsp1 / wsp2,2)

                wynik1=Label(ww,text=wynik)
                napis1.grid(row=0,column=2)
                napis2.grid(row=0,column=4)
                wynik1.grid(row=1,column=4)

            #Guziory
            opcje = baza['Nazwa waluty'].values
            cl = StringVar()
            cl2= StringVar()

            opcje1 = OptionMenu(ww, cl, *opcje)
            opcje2 = OptionMenu(ww, cl2, *opcje)

            entry1 = Entry(ww, width=7, borderwidth=5)
            przelicz1 = Button(ww, text='Przelicz', padx=30, pady=10, command=przelicz1)
            rowno1 = Label(ww, text=' ⇔ ')
            lab1=Label(ww,text='Wybierz walutę--->')
            lab2=Label(ww, text='<---Wybierz walutę')
            #Gridy
            opcje1.grid(row=0, column=1)
            opcje2.grid(row=0, column=5)
            entry1.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
            przelicz1.grid(row=2, column=3)
            rowno1.grid(row=1, column=3)
            lab1.grid(row=0,column=0)
            lab2.grid(row=0,column=6)

        #Napis

        napis1=Label(MainRoot,text='Witaj w przeliczniku walut')

        #Guziory

        guzior_lista=Button(MainRoot, text='Lista dostępnych \n kursów', padx=40, pady=20, command=lista)
        guzior_PLN = Button(MainRoot, text='PLN <=> Waluta', padx=40, pady=20, command=wym_pl)
        guzior_WW = Button(MainRoot, text='Waluta <=> Waluta', padx=40, pady=20, command=w_w)
        wyjscie=Button(MainRoot, text='Wyjście', padx=40, pady=20, command=MainRoot.destroy)


        #Ustawianko
        napis1.grid(row=0,column=1)
        guzior_lista.grid(row=1,column=0)
        guzior_PLN.grid(row=1,column=1)
        guzior_WW.grid(row=1,column=2)
        wyjscie.grid(row=2,column=1)

        MainRoot.mainloop()



KursyWalut('kursy.xml').start()
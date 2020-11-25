# -------------------------------Zadanie 3-----------------------------------
# Rzut ukosny. Napisz program, który pobiera od uzytkownika dwie wartosci: predkosc poczatkowa v0 oraz kat rzutu
# α, i zwraca
# • maksymalna wysokosc na jaka wzniesie sie cialo
# • zasieg rzutu
# • czas lotu
# Program powinien równiez tworzyc 3 wykresy:
# • predkosc chwilowa w kierunku pionowym i poziomym po czasie t v(t)
# • polozenia w funkcji czasu x(t)
# • wykres toru rzutu ukosnego  y(x)
#  Wykorzystaj subplot.
import numpy as np
import math
from matplotlib import pyplot as plt

def zadanie3(kat,predkosc_poczatkowa):

    angle=math.radians(kat)

    #wykonywanie obliczeń - max wysokosc / zasieg / czas lotu

    def obliczenia(k,v0):

        g=9.81
        #Obliczenie max wysokosci
        h_max = (v0**2 * math.pow(math.sin(k),2)) / (2 * g)
        #Obliczenie czasu lotu

        t_calkowity = 2 * v0 * math.sin(k) / g

        # Obliczenie zasiegu

        zasieg= t_calkowity * v0 * math.cos(k)

        return h_max,zasieg,t_calkowity

    #Tworzenie wykresow
    def wykresy(v0,k,t_c,zz):
        g=9.81
        vx=v0*math.cos(k)
        vy=v0*math.sin(k)
        #Wykres predkosc chwilowa w kierunku pionowym i poziomym po czasie t
        x1=np.linspace(0,t_c,400)
        w1y1=np.array(vx + 0*x1)
        w1y2=np.array(np.abs(vy-g*x1))

        #Wykres polozenia w funkcji czasu
        w2y=np.array(vx*x1)
        w2y1=np.array(vy*x1 - g/2 * x1**2)

        #Wykres wykres toru rzutu ukosnego
        x2=np.linspace(0,zz,100)
        #w3y= x2*math.tan(k) - g*x2**2/(2*vx**2)
        w3y = vy*x2/vx - g/2 * (x2/vx)**2

        # Tworzenie wykresow
        plt.figure(figsize=(15,5))
        w1=plt.subplot(1,3,1,title='Prędkość chwilowa v(t)',xlabel='t [s]',ylabel='v [m/s]')
        w1.plot(x1,w1y1,label='Prędkość pozioma - Vx(t)')
        w1.plot(x1,w1y2,label='Prędkość pionowa - Vy(t)')
        plt.legend()

        w2 = plt.subplot(1, 3, 2,title='Położenie od czasu x,y(t)',xlabel='t [s]',ylabel='x,y [m]')
        w2.plot(x1,w2y,label='Położenie poziome X(t)')
        w2.plot(x1,w2y1,label='Położenie pionowa Y(t)')
        plt.legend()

        w3 = plt.subplot(1, 3, 3,title='Tor ruchu y(x)',xlabel='x [m]',ylabel='y [m]')
        w3.plot(x2,w3y,label='Położenie y(x)')
        plt.legend()

        plt.show()


    def koniec():
        #wykonuje funkcje obliczenia i przekazuje to do tekstu
        x=obliczenia(angle,predkosc_poczatkowa)
        tekst='''
Maksymalna wysokość : {} [m]
Zasięg rzutu : {} [m]
Całkowity czas lotu : {} [s]
        '''.format(x[0],x[1],x[2])
        print(tekst)
        #Wykonuje wykresy
        wykresy(predkosc_poczatkowa,angle,x[2],x[1])

    koniec()

zadanie3(45,25)
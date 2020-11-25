#-------------------------------Zadanie 1-----------------------------------
import math

def boki(a,b,c):

    #sprawdzanie czy trojkat o takich bokach istnieje
    l=[a,b,c]
    maxn=max(l)
    l.remove(maxn)
    ls=sum(l)
    #Sprawdzanie warunku na istnienie trojkata
    if maxn<=ls:

        #obwód
        obwod=a+b+c
        print('Obwód trójkąta: ',obwod)
        #pole - wzor herona
        s=obwod/2
        pole=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('Pole trójkąta: ',pole)
        # czy trojkat jest rownoramienny/ rownoboczny/ roznoboczny
        l2={a,b,c}
        if len(l2)==3:
            print('Trójkąt różnoboczny')
        elif len(l2)==2:
            print('Trójkąt równoramienny')
        else:
            print('Trójkąt równoboczny')

        # czy rozwartokatny / prostokatny / ostrokatny

        c=maxn**2
        ab2=sum([i**2 for i in l])
        if c>ab2:
            print('Trójąt jest rozwartokatny')
        elif c<ab2:
            print('Trójąt jest ostrokatny')
        else:
            print('Trójąt jest prostokatny')

    else:
        print('Nie są spełnione warunki trojkata')

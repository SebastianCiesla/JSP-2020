# -------------------------------Zadanie 7-----------------------------------
#Napisz program, który wypiszę n pierwszych wierszy trójkąta Pascala.

import math

def pascal(n):

    pascaltriangle=[]
    kr = 0
    for element_n in range(n+1):
        pasal=[]
        for element_k in range(kr+1):

            n2=math.factorial(element_n)
            k2=math.factorial(element_k)
            n_k=math.factorial(element_n-element_k)
            result=int(n2/(k2*n_k))
            pasal.append(result)

        kr=kr+1
        pascaltriangle.append(pasal)

    # malowanie
    end=[]
    for ele in pascaltriangle:
        p=' '.join(str(e) for e in ele)
        end.append(p)

    l=n
    end2=[]
    for ele in end:
        p=' '*l+ele
        end2.append(p)
        l-=1

    for e in end2:
        print(e)

pascal(5)
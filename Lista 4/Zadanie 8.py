# -------------------------------Zadanie 8-----------------------------------
#Napisz program, który obliczy sumę n pierwszych elementów szeregu harmonicznego.

def harmo(n):

    l=[1/x for x in range(1,n+1)]
    print(sum(l))

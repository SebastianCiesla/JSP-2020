# -------------------------------Zadanie 10-----------------------------------
#Napisz program, który znajdzie największy wspólny dzielnik dwóch liczb całkowitych

def euklidesalgorytm(n1,n2):

    r1=n1%n2
    if r1==0:
        print('najwiekszy wspolny dzielnik {} i {} to: {}'.format(n1,n2,n2))
    else:
        l = [n1, n2, r1]
        while l[-1]!=0:
            last=l[-2]%l[-1]
            l.append(last)
        print('najwiekszy wspolny dzielnik {} i {} to: {}'.format(n1,n2,l[-2]))


euklidesalgorytm(282,78)
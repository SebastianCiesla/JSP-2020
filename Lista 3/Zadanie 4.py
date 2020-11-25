# -------------------------------Zadanie 4-----------------------------------
# Napisz program, który wydrukuje litery alfabetu 'L','A','R' w nastepujacy sposób

def L():
    
    for element in range(7):
        if element == 6:
            print('*****')
        else:
            print('*')

def A():
    p='*'
    s=' '
    s1=1
    sc=8
    for element in range(6):

        if element == 0:
            print(s*sc,p)
            sc-=2
        elif element == 3:
            print(s*sc,p*9)
            sc-=1
            s1+=2
        else:
            print(s*sc,p,s*s1,p)
            sc-=1
            s1+=2

def R():

    p=' '+ '*'*4 + ' '
    p1='*' + ' '*4 + '*'
    p2=' '
    p3='*'
    print(p)
    print(p1)
    print(p1)
    print(p)
    for element in range(3):
        print(p3,p2*element,p3)


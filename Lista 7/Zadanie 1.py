# -------------------------------Zadanie 1-----------------------------------
# Napisz program, który wypisze kolejne elementy szeregu Fibonacci zaczynając od 0 i kończąc na N (gdzie N
# wprowadza użytkownik) w dwóch wersjach: poprzez iterację (np. pętlą for) oraz rekurencyjnie. Korzystając z
# modułu time zmierz czas działania obu programów.


import time

#iteracja for
def fib1(n):
    f=[0,1,1]
    print(f[0])
    print(f[1])
    print(f[2])
    for _ in range(n-3):
        sol=f[-1] + f[-2]
        f.append(sol)
        print(sol)

#rekurencja
def fibre(i):

    def fib2(n):

        if n>1:
            return fib2(n-1)+fib2(n-2)
        elif n == 1:
            return 1
        elif n == 0 :
            return 0

    for x in range(i):
        print(fib2(x))

#Liczenie czasu dla iteracji
x=int(input('Podaj ilosc wyrazo ciagu fibbonaciego: '))
print('Sprawdzanie czasu dla iteracji')
t1=time.time()
fib1(x)
t2=time.time()
#Liczenie czasu dla rekurencji
print('Dla rekurencji')
t3=time.time()
fibre(x)
t4=time.time()
#Prezentacja wynikow
print('Wyniki: ')
print(f'Czas dla "for" {t2-t1} , Czas dla rekurencji: {t4-t3}')




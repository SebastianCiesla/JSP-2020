# -------------------------------Zadanie 7-----------------------------------
#Napisz program, który wypisze kolejne elementy szeregu Fibonacci zaczynajac od 0 i konczac na N, gdzie N
#wprowadza u»ytkownik.

n=int(input('Podaj liczbe elementow ciagu: '))


fibb_list=[0,1]
if n>2:
    for element in range(n-2):
        suma=fibb_list[-1]+fibb_list[-2]
        fibb_list.append(suma)

print(fibb_list)




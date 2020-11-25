# -------------------------------Zadanie 9-----------------------------------
# Napisz program, który pobierze dwie liczny calkowite: m (wiersze) i n (kolumny) a nastepnie wygeneruje
# dwuwymiarowa tablice, której element na pozycji (i, j) jest równy i ∗ j.

m=int(input('podaj m (wiersze) : '))
n=int(input('podaj n (kolumny) : '))

main_list=[]
for row_number in range(1,m+1):
    list=[]
    for column_number in range(1,n+1):
        result=row_number*column_number
        list.append(result)
    main_list.append(list)
#display
for e in main_list: print(e)
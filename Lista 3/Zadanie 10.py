# -------------------------------Zadanie 10-----------------------------------
#Napisz program, który znajdzie wszystkie liczby z przedzialu 100 − 400 takie, ze kazda cyfra z badanej liczby jest
#cyfra parzysta. Wynik nalezy wydrukowac jako liste, w której elementy sa oddzielone przecinkami.


results=[]
ban_numbers=['1','3','5','7','9']
for number in range(100,401):
    strnumb=str(number)
    for number2 in ban_numbers:
        if number2 in strnumb:
            break
    else:
        results.append(strnumb) #pętla for / break -> jeśli pętla for zostaje przerwana przez break
                                #else się nie wykonuje
print(results)

# -------------------------------Zadanie 4-----------------------------------
# Wyświetl na ekranie listę funkcji wbudowanych:
# >>> import builtins
# >>> dir(builtins)
# Następnie sprawdź dokumentację funkcji print:
# >>> help(print)
# i wykorzystaj ją, aby na ekranie wydrukować:
# • tekst ”Ala ma kota”.
# • wynik działania 2 + 2
# • wyniki działań: 2 ∗ ∗5, 35//2, 35/2, 35%2 oddzielone tabulacją (\t)
# • wyniki działań: 2 ∗ ∗5, 35//2, 35/2, 35%2, każdy wynik w nowej linii (\n)

import builtins
print(dir(builtins))

help(print)

print('Ala ma kota')
print(2 + 2)
print(2 ** 5, 35 // 2, 35 % 2,sep='\t')
print(2 ** 5, 35 // 2, 35 % 2, sep='\n')
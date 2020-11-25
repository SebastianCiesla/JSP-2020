# -------------------------------Zadanie 9-----------------------------------
# Sprawdź dokumentację funkcji chain, a następnie napisz program, który obniży stopień zagnieżdżenia listy. Np.
# [[2, 5], [1, 2], [4, 4]] zamieni na [2, 5, 1, 2, 4, 4]. Lista początkowa to [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

import itertools as it

lista_poczatkowa=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
lista_koncowa=list(it.chain.from_iterable(lista_poczatkowa))
print(lista_koncowa)
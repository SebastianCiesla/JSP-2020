# -------------------------------Zadanie 1-----------------------------------
# Dany jest uklad równan
# x + 2y + 3z − 2t − u = 6
# 3x + 5y + 5z − 3t − 9u = 2
# 2x + 3y + 2z − 8u = −5
# 2x + 6y + 7z − 5t + u = 17
# x + 2y + 6z − 4t − 10u = 12
# Stosujac modul NumPy wyznacz x, y, z, t, u.

import numpy as np

r1=[1,2,3,-2,-1]
r2=[3,5,5,-3,-9]
r3=[2,3,2,0,-8]
r4=[2,6,7,-5,1]
r5=[1,2,6,-4,-10]
s=[6,2,-5,17,12]
# uklad zapisany do postaci macierzowej
a=[r1,r2,r3,r4,r5]
#do metody solve przekazywane sa a-> równania i s-> wyniki
res=np.linalg.solve(a,s)
print(res)


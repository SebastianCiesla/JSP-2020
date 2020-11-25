# -------------------------------Zadanie 4-----------------------------------
# Napisz program, który narysuje wykres slupkowy pokazujacy popularnosc róznych jezyków programowania.
# Dla uproszczenia mozemy ograniczyc sie do 10 najpopularniejszych jezyków
# (patrz np https://www.tiobe.com/tiobe-index/).
# Wykres powinien zawierac odpowiednie oznaczenia (opis osi, slupków, tytul wykresu itd.)

import numpy as np
import math
from matplotlib import pyplot as plt

#Dane do wykresu
jezyki=['C','Python','Java','C++','C#','Visual Basic', 'JavaScript', 'PHP', 'R', 'SQL']
dane=[16.21,12.12,11.68,7.60,4.67,4.01,2.03,1.79,1.64,1.54]
x=np.linspace(1,len(jezyki),10)

#Tworzenie wykresu
plt.figure(figsize=(15,5))
wykres=plt.bar(x,dane)
plt.title('Popularność języków programowania')
plt.xticks(x,labels=jezyki)
plt.ylabel('Ocena [%]')
#Dodawanie wartosci nad poszczegolnymi slupkami dla klarownosci
for rect in wykres:
    height=rect.get_height()
    plt.annotate(f'{height} %',xy=(rect.get_x()+0.15,height+0.1))

plt.show()



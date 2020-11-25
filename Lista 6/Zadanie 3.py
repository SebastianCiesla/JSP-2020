# -------------------------------Zadanie 3-----------------------------------
# Napisz skrypt, który dla zadanego n generuje n pierwszych wyrazów ciagu "look-and-say"

def look_and_say(n):

    seq=[1]     #ciąg look and say z pierwszym elementem
    i=n-1       #ilosc wykonywania iteracji

    while i != 0:

        new =[]
        element_cout=[]
        #Dla elementow w ciagu
        for el in range(len(seq)):

            element_cout.append(seq[el])   #dodawanie elementu ciagu do nowej listy
            if el != len(seq)-1:           #Obsluga wszystkich elementow oprócz ostatniego

                if seq[el] != seq[el+1]:    #Jeśli nastepny sie rozni to podsumowuje wszystko
                    lenght=len(element_cout)    #look and say
                    numb=list(set(element_cout))[0]

                    new.append(lenght)
                    new.append(numb)
                    element_cout.clear()

                if seq[el] == seq[el+1]:    #Nic nie robi
                    pass


            elif el == len(seq)-1:      #Obsluga ostatniego elementu

                if  seq[el] == seq[el-1]:   #jesli taki sam jak poprzedni
                    lenght = len(element_cout)
                    numb=list(set(element_cout))[0]
                    new.append(lenght)
                    new.append(numb)
                    element_cout.clear()

                elif seq[el] != seq [el-1]: #jesli rozny
                    new.append(1)
                    new.append(seq[el])

        seq=new
        i-=1

    print(seq)

look_and_say(6)
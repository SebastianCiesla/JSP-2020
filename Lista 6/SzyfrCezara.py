# -------------------------------Zadanie 2-----------------------------------
#A-Z => 65-90 a-z => 97-122


#Funkcja pobiera tekst i przesuniecie o n
def szyfrowanie(tekst,n):

    finish=''
    #przesuniecie n%25 w przypadku, gdy ktos by sobie wymyslil przesuniecie o np 125 :)
    przesuniecie=n%25

    #głowna pętla dla kazdej litery znajduje jej przesuniety odpowiednik
    for letter in tekst:

        num_lett =  ord(letter)
        #Jeśli dana litera jest 'mala'
        if num_lett  in range(65,91):

            num2=num_lett+przesuniecie
            if num2>90:
                num2=num2-91 + 65

            finish += chr(num2)
        # Jeśli dana litera jest 'duza'
        elif num_lett in range(97,123):

            num2 = num_lett + przesuniecie
            if num2 > 122:
                num2 = num2 - 123 + 97

            finish += chr(num2)
        # Gdy dana litera nie bedzie ani duza ani mala -> obsluga znakow specjalnych i cyfr
        else:
            finish += letter

    return finish


def odszyfrowanie(tekst,n):

    finish = ''

    przesuniecie = n % 25

    # głowna pętla
    for letter in tekst:

        num_lett = ord(letter)
        # Jeśli dana litera jest 'mala'
        if num_lett in range(65, 91):

            num2 = num_lett - przesuniecie
            if num2 < 65:
                num2 = 91 - (65 - num2)

            finish += chr(num2)
        # Jeśli dana litera jest 'duza'
        elif num_lett in range(97, 123):

            num2 = num_lett - przesuniecie
            if num2 < 97:
                num2 = 123 - (97 - num2)

            finish += chr(num2)
        #Gdy dana litera nie bedzie ani duza ani mala -> obsluga znakow specjalnych i cyfr
        else:
            finish += letter

    return finish


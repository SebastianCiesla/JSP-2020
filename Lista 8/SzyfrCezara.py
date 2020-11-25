# -------------------------------Zadanie 2-----------------------------------
#A-Z => 65-90 a-z => 97-122



def szyfrowanie(tekst,n):

    finish=''

    przesuniecie=n%25

    #głowna pętla
    for letter in tekst:

        num_lett =  ord(letter)

        if num_lett  in range(65,91):

            num2=num_lett+przesuniecie
            if num2>90:
                num2=num2-91 + 65

            finish += chr(num2)

        elif num_lett in range(97,123):

            num2 = num_lett + przesuniecie
            if num2 > 122:
                num2 = num2 - 123 + 97

            finish += chr(num2)

        else:
            finish += letter

    return finish


def odszyfrowanie(tekst,n):

    finish = ''

    przesuniecie = n % 25

    # głowna pętla
    for letter in tekst:

        num_lett = ord(letter)

        if num_lett in range(65, 91):

            num2 = num_lett - przesuniecie
            if num2 < 65:
                num2 = 91 - (65 - num2)

            finish += chr(num2)

        elif num_lett in range(97, 123):

            num2 = num_lett - przesuniecie
            if num2 < 97:
                num2 = 123 - (97 - num2)

            finish += chr(num2)

        else:
            finish += letter

    return finish


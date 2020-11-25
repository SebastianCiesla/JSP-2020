# -------------------------------Zadanie 2-----------------------------------
# #Stwórz modul SzyfrCezara.py zawierajacy dwie funkcje, które dokonuja szyfrowania lub deszyfrowania podanego
# slowa. Napisz program, który pobiera od uzytkownika dowolne zdania, a nastepnie przeprowadza procedure szyfrowania.
# Pamietaj, ze znaki interpunkcyjne i spacje nie sa szyfrowane. Co wiecej, szyfrowane nie sa cyfry czy znaki
# specjalne, jedynie litery. Po skonczeniu czesci pierwszej, napisz program deszyfruj¡cy.
# Podpowiedz: "Szyfr Cezara zastepuje kazda litere tekstu jawnego inna, przesunieta wzgledem litery kodowanej o stala
# liczbe pozycji w alfabecie." W zwiazku z tym, wykorzystaj funkcje ord i chr.

import SzyfrCezara

tekst='Tajna wiadomosc'

print('Szyfrowanie o np. 10')
print(tekst,'\n')
zasz=SzyfrCezara.szyfrowanie(tekst,10)
print(zasz,'\n')
print('Odszyfrowywanie: ')
odsz=SzyfrCezara.odszyfrowanie(zasz,10)
print(odsz)
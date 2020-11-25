# -------------------------------Zadanie 5-----------------------------------
#Posiłkując się dokumentacją i stosownymi przykładami, wyjaśnić różnicę między operacją dzielenia bez reszty (np.
# 5//2) a zaokrąglaniem liczby zmiennoprzecinkowej wykorzystując round(float), floor(float).
import math

x=5.1
y=5.6

print('Dzielenie bez reszty : ',x,"//2 = ",x//2)
print('Dzielenie bez reszty : ',y,"//2 = ",y//2)

print('Zaokreaglanie round: ',x,'round(x)=',round(x))
print('Zaokreaglanie round: ',y,'round(x)=',round(y))

print('Zaokraglenie floor: ',x,'floor(x)=',math.floor(x))
print('Zaokraglenie floor: ',y,'floor(x)=',math.floor(y))

print('Zaokrąglenie celi: ',x,'celi(x)=',math.ceil(x))
print('Zaokrąglenie celi: ',x,'celi(x)=',math.ceil(x))

print('Dzielenie bez reszty (5//2) działa tak jak floor -> zaokrąglenie w dół')
print('Dzielenie round jest bardziej poprawne matematycznie, można wybrac równiez miejsce po przecinku do zaokrąglenia')
print('np. round(5.76543,2) => 5.77')
print('Metoda celi() -> zaokrągle w górę ')
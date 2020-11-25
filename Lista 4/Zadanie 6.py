# -------------------------------Zadanie 6-----------------------------------
#Napisz program, który przeprowadzi konwencję kodowania RGB na HSV.


import colorsys

def conv_to_HSV(r,g,b):

    x=colorsys.rgb_to_hsv(r,g,b)
    print(x)

conv_to_HSV(0,1,0)


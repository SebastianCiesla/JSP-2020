# -------------------------------Zadanie 3-----------------------------------
#Napisz program, który konwertuje stopnie na radiany i odwrotnie, w zależności od sposobu wywołania funkcji

class Converter:

    def ToRadian(kat):

        result = kat * 3.14 / 180
        print(result)

    def ToAngle(radian):

        result = radian * 180 / 3.14
        print(result)


Converter.ToAngle(1) #57.32
Converter.ToRadian(1) #0.017

class Converter2:

    def __init__(self,cos):
        self.cos=cos

    def ToRadian(self):

        result = self.cos * 3.14 / 180
        print(result)

    def ToAngle(self):

        result = self.cos * 180 / 3.14
        print(result)
        
Converter2(1).ToAngle()
Converter2(1).ToRadian()
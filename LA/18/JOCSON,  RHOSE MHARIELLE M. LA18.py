class Sinigang:
    def __init__(self, main, texture, taste):
        self.__main=main
        self.__texture= texture
        self.__taste= taste
    def __str__(self):
        return f" Yummerz ang sinigang na {self.__main} na {self.__texture}  at soafer {self.__taste}."

sinigang_yobab= Sinigang("baboy","malapot", "asim")
sinigang_hipon= Sinigang("hipon", "maraming kangkong", "linamnam")
sinigang_bangus= Sinigang ("bangus", "maraming tyan", "crispy ang balat")

print(sinigang_yobab)
print(sinigang_hipon)
print(sinigang_bangus)

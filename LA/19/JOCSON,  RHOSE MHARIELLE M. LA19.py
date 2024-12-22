class Sinigang:
    def __init__(self, main, texture, taste):
        self.main=main
        self._texture= texture
        self.__taste= taste
    def __str__(self):
        return f" Yummerz ang sinigang na {self.main} na {self._texture}  at soafer {self.__taste}."

sinigang_yobab= Sinigang("baboy","malapot", "asim")
sinigang_hipon= Sinigang("hipon", "maraming kangkong", "linamnam")
sinigang_bangus= Sinigang ("bangus", "maraming tyan", "crispy ang balat")

print(sinigang_yobab._texture)
print(sinigang_hipon._texture)
print(sinigang_bangus.__taste)

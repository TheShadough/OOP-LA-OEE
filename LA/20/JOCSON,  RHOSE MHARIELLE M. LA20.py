class Sinigang:
    def __init__(self, main, texture, taste):
        self._main=main
        self._texture= texture
        self.__taste= taste
    def __str__(self):
        return f" Yummerz ang sinigang na {self._main} na {self._texture}  at soafer {self.__taste}."
    def di_masarap(self):
        return self.__taste


sinigang_bangus= Sinigang ("bangus", "maraming tyan", "crispy ang balat")

print(sinigang_bangus.di_masarap())

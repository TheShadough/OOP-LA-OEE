class Sinigang:
    def __init__(self, main, texture, taste):
        self._main = main
        self._texture = texture
        self.__taste = taste

    def __str__(self):
        return f" Yummerz ang sinigang na {self._main} na {self._texture}  at soafer {self.__taste}."

    def di_masarap(self):
        return self.__taste

    def set_taste(self, new_taste):
        self.__taste = new_taste
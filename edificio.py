class Edificio:
    def __init__(self, nombre, direccion, cantidad_pisos, cantidad_aulas):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_aulas = cantidad_aulas

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, valor):
            self.__nombre = valor

        @nombre.deleter
        def nombre(self):
            del self.__nombre


        @property
        def direccion(self):
            return self.__direccion


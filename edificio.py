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

    # Property direccion
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    # Property cantidad_pisos
    @property
    def cantidad_pisos(self):
        return self.__cantidad_pisos

    @cantidad_pisos.setter
    def cantidad_pisos(self, value):
        self.__cantidad_pisos = value

    @cantidad_pisos.deleter
    def cantidad_pisos(self):
        del self.__cantidad_pisos

    # Property cantidad_aulas
    @property
    def cantidad_aulas(self):
        return self.__cantidad_aulas

    @cantidad_aulas.setter
    def cantidad_aulas(self, value):
        self.__cantidad_aulas = value

    @cantidad_aulas.deleter
    def cantidad_aulas(self):
        del self.__cantidad_aulas

    def administrar_edificio(self, nombre, direccion, cantidad_pisos, cantidad_aulas):
        self.nombre = nombre
        self.direccion = direccion
        self.cantidad_pisos = cantidad_pisos
        self.cantidad_aulas = cantidad_aulas
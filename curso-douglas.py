class Curso():
    def __init__(self, nombre_curso, creditos, cantidad_hrs_semanales, programa):
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__cantidad_hrs_semanales = cantidad_hrs_semanales
        self.__programa = programa

    @property
    def nombre_curso(self):
        return self.__nombre_curso
    @nombre_curso.setter
    def nombre_curso(self, value):
        self.__nombre_curso = value
    @nombre_curso.deleter
    def nombre_curso(self):
        del self.__nombre_curso

    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def creditos(self, value):
        self.__creditos = value
    @creditos.deleter
    def creditos(self):
        del self.__creditos

    @property
    def cantidad_hrs_semanales(self):
        return self.__cantidad_hrs_semanales
    @cantidad_hrs_semanales.setter
    def cantidad_hrs_semanales(self, value):
        self.__cantidad_hrs_semanales = value
    @cantidad_hrs_semanales.deleter
    def cantidad_hrs_semanales(self):
        del self.__cantidad_hrs_semanales

    @property
    def programa(self):
        return self.__programa
    @programa.setter
    def programa(self, value):
        self.__programa = value
    @programa.deleter
    def programa(self):
        del self.__programa


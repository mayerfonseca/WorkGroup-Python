class Programa:
    def __init__(self, nombre_programa, fecha_creacion, status_programa, director):
        self.__nombre_programa = nombre_programa
        self.__fecha_creacion = fecha_creacion
        self.__status_programa = status_programa
        self.__director = director

        # Property nombre_programa
        @property
        def nombre_programa(self):
            return self.__nombre_programa

        @nombre_programa.setter
        def nombre_programa(self, value):
            self.__nombre_programa = value

        @nombre_programa.deleter
        def nombre_programa(self):
            del self.__nombre_programa

        # Property fecha_creacion
        @property
        def fecha_creacion(self):
            return self.__fecha_creacion

        @fecha_creacion.setter
        def fecha_creacion(self, value):
            self.__fecha_creacion = value

        @fecha_creacion.deleter
        def fecha_creacion(self):
            del self.__fecha_creacion

        # Property status_programa
        @property
        def status_programa(self):
            return self.__status_programa

        @status_programa.setter
        def status_programa(self, value):
            self.__status_programa = value

        @status_programa.deleter
        def status_programa(self):
            del self.__status_programa

        # Property director
        @property
        def director(self):
            return self.__director

        @director.setter
        def director(self, value):
            self.__director = value

        @director.deleter
        def director(self):
            del self.__director
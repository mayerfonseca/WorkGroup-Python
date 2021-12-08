class Curso:
    """Definición de la clase Curso"""
    def __init__(self, nombre_curso, creditos, cant_hrs_semanales, programa):
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__cant_hrs_semanales = cant_hrs_semanales
        self.__programa = programa

        # Property __nombre_cursoasdfasdf
        @property
        def nombre_curso(self):
            return self.__nombre_curso

        @nombre_curso.setter
        def nombre_curso(self, value):
            self.__nombre_curso = value

        @nombre_curso.deleter
        def nombre_curso(self):
            del self.__nombre_curso

        # Property creditos
        @property
        def creditos(self):
            return self.__creditos

        @creditos.setter
        def creditos(self, value):
            self.__creditos = value

        @creditos.deleter
        def creditos(self):
            del self.__creditos

        # Property cant_hrs_semanales
        @property
        def cant_hrs_semanales(self):
            return self.__cant_hrs_semanales

        @cant_hrs_semanales.setter
        def cant_hrs_semanales(self, value):
            self.__cant_hrs_semanales = value

        @cant_hrs_semanales.deleter
        def cant_hrs_semanales(self):
            del self.__cant_hrs_semanales
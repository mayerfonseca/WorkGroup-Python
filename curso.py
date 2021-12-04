class Curso:
    """Definición de la clase Curso"""
    def __init__(self, nombre_curso, creditos, cant_hrs_semanales, programa):
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__cant_hrs_semanales = cant_hrs_semanales
        self.__programa = programa

        # Property __nombre_curso
        @property
        def __nombre_curso(self):
            return self.___nombre_curso

        @__nombre_curso.setter
        def __nombre_curso(self, value):
            self.___nombre_curso = value

        @__nombre_curso.deleter
        def __nombre_curso(self):
            del self.___nombre_curso

        # Property __creditos
        @property
        def __creditos(self):
            return self.___creditos

        @__creditos.setter
        def __creditos(self, value):
            self.___creditos = value

        @__creditos.deleter
        def __creditos(self):
            del self.__creditos

            # Property __cant_hrs_semanales
            @property
            def __cant_hrs_semanales(self):
                return self.__cant_hrs_semanales

            @__cant_hrs_semanales.setter
            def __cant_hrs_semanales(self, value):
                self.__cant_hrs_semanales = value

            @__cant_hrs_semanales.deleter
            def __cant_hrs_semanales(self):
                del self.__cant_hrs_semanales
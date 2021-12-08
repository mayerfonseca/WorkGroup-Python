class Matricula():
    def __init__(self, fecha, hora):
        self.__fecha_matricula = fecha
        self.__hora_matricula = hora

        @property
        def fecha(self):
            return self.__fecha_matricula

        @fecha.setter
        def fecha(self, fecha):
            self.__fecha_matricula = fecha

        @fecha.deleter
        def fecha(self):
            del self.__fecha_matricula

        @property
        def hora(self):
            return self.__hora_matricula

        @hora.setter
        def hora(self, hora):
            self.__hora_matricula = hora

        @hora.deleter
        def hora(self):
            del self.__hora_matricula
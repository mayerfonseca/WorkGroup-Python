class Matricula():
    def __init__(self, fecha, hora):
        self.__fecha_matricula = fecha
        self.__hora_matricula = hora

        @property
        def id(self):
            return self.__id

        @id.setter
        def id(self, id):
            self.__id = id

        @id.deleter
        def id(self):
            del self.__id

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


    def agregar(self, curso):
        nombre_curso = input("Nombre del curso: ")
        return  nombre_curso

    def agregar(self, nota):
        nota_curso = nota
        return nota_curso

    def total_vendido(self, precio):
        precio_mat = precio
        return precio_mat


class TipoProfesor:
    def __init__(self, id_profesor, tipo):
        self._id_profesor = id_profesor
        self.__tipo = tipo

    #Property id_profesor
    @property
    def id_profesor(self):
        return self.__id_profesor

    @id_profesor.setter
    def id_profesor(self, value):
        self.__id_profesor = value

    @id_profesor.deleter
    def id_profesor(self):
        del self.__id_profesor

    #Property tipo
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @tipo.deleter
    def tipo(self):
        del self.__tipo

    def definir_tipo(self, id_profesor, tipo):
        """Metodo para realizar una instanciación para Definir Tipo de Profesor"""
        self.id_profesor = id_profesor
        self.tipo = tipo

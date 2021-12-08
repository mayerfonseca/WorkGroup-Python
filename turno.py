class Turno():
    def __init__(self, turno):
        self.__turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @turno.deleter
    def turno(self, turno):
        del self.__turno
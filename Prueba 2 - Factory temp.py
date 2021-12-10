
class Prueba():
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.getter
    def nombre(self, value):
        self.__nombre = value

    def saludo(self):
        print(f"Clase Padre:" )# {self.__nombre}

    def factory(type):
        if type == "Test1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            return  Test1(nombre, apellido)
        if type == "Test2":
            nombre = input("Ingrese su nombre: ")
            return  Test2(nombre)
        assert 0, "La entidad definida no existe " + type

class Test1(Prueba):
    def __init__(self, nombre,apellido): #, nombre, apellido
        super(Test1, self).__init__(nombre)
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def apellido(self):
        return self.__apellido

    @apellido.getter
    def apellido(self, value):
        self.__apellido = value

    def saludo(self):
        print(f"Clase Hija 1 - nombre: {self.__nombre}, apellido: {self.__apellido}")

class Test2(Prueba):
    def __init__(self,nombre):
        super(Test2, self).__init__(nombre)
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    def saludo(self):
        print("Clase Hija 2")


def saludar(type):
    type.saludo()


hijo = Prueba.factory("Test2")
saludar(hijo)

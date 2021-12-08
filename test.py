class Prueba:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    @nombre.getter
    def nombre(self, value):
        self.__nombre = value

    def saludo(self):
        print(f"Clase Padre: {self.__nombre}" )

    def factory(type):
        class Test1(Prueba):
            def __init__(self, nombre, apellido):
                super(Test1, self).__init__(nombre)
                self.__nombre = nombre
                self.__apellido = apellido

            @property
            def apellido(self):
                return self.__apellido

            @apellido.getter
            def apellido(self, value):
                self.__apellido = value
            @classmethod
            def saludo(self):
                print(f"Clase Hija 1 - nombre: {self.__nombre}, apellido: {self.__apellido}")

        class Test2(Prueba):
            def saludo(self):
                print("Clase Hija 2")

        if (type == "Test1"):
            return Test1()
        if (type == "Test2"):
            return Test2()


#entidad = Prueba.factory("Test1")

entidad = Prueba.factory("Test1")
entidad.nombre = "Jose"
entidad.apellido = "Martinez"
entidad.saludo()


# Una vez creada super clase con constructor no se puede invocar metodos sin inicializar hija
class Aula:
    def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
        self.nombre_aula = nombre_aula
        self.numero_piso = numero_piso
        self.numero_edificio = numero_edificio
        self.capacidad_asientos = capacidad_asientos


        #Property __nombre_aula
        @property
        def nombre_aula(self):
            return self.__nombre_aula

        @nombre_aula.setter
        def nombre_aula(self, value):
            self.__nombre_aula = value

        @nombre_aula.deleter
        def nombre_aula(self):
            del self.__nombre_aula

        # Property __numero_piso
        @property
        def numero_piso(self):
            return self.__numero_piso

        @numero_piso.setter
        def numero_piso(self, value):
            self.__numero_piso = value

        @numero_piso.deleter
        def numero_piso(self):
            del self.__numero_piso

        # Property __numero_edificio
        @property
        def numero_edificio(self):
            return self.__numero_edificio

        @numero_edificio.setter
        def numero_edificio(self, value):
            self.__numero_edificio = value

        @numero_edificio.deleter
        def numero_edificio(self):
            del self.__numero_edificio

        # Property __capacidad_asientos
        @property
        def capacidad_asientos(self):
            return self.__capacidad_asientos

        @capacidad_asientos.setter
        def capacidad_asientos(self, value):
            self.__capacidad_asientos = value

        @capacidad_asientos.deleter
        def capacidad_asientos(self):
            del self.__capacidad_asientos
#
# B1 = Aula("autrophitecus",12,12,10)
# print(B1.__dict__)
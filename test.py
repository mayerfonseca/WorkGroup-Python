class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fec_nac, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fec_nac = fec_nac
        self.__email = email

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def apellido(self):
            return self.__apellido

        @apellido.setter
        def apellido(self, apellido):
            self.__apellido = apellido

        @property
        def cedula(self):
            return self.__cedula

        @cedula.setter
        def cedula(self, cedula):
            self.__cedula = cedula

        @property
        def direccion(self):
            return self.__direccion

        @direccion.setter
        def direccion(self, direccion):
            self.__direccion = direccion

        @property
        def telefono(self):
            return self.__telefono

        @telefono.setter
        def telefono(self, telefono):
            self.__telefono = telefono

        @property
        def fec_nac(self):
            return self.__fec_nac

        @fec_nac.setter
        def fec_nac(self, fec_nac):
            self.__fec_nac = fec_nac

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, email):
            self.__email = email


class Profesor(Persona):
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fec_nac, email, id_profesor):
        super().__init__(nombre, apellido, cedula, direccion, telefono, fec_nac, email)
        self.__id_profesor = id_profesor

        @property
        def id_profesor(self):
            return self.__id_profesor

        @id_profesor.setter
        def id_profesor(self, id_profesor):
            self.__id_profesor = id_profesor


    def display(self):
        print("Profesor " + self.__id_profesor)

class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fec_nac, email, id_estudiante):
        super().__init__(nombre, apellido, cedula, direccion, telefono, fec_nac, email)
        self.__id_estudiante = id_estudiante

        @property
        def id_estudiante(self):
            return self.__id_estudiante

        @id_estudiante.setter
        def id_estudiante(self, id_estudiante):
            self.__id_estudiante = id_estudiante


    def display(self):
        print("Estudiante " + self.__id_estudiante)

def mostrar(clase):
    clase.display()


test1 = Profesor("Juan", "Galgo", "441-090182-0006G", "Matagalpa", "8633-1913", "1982-01-09", "montenegro.jose.m@gmail.com", "123")
test2 = Estudiante("Mario", "Cruz", "441-090182-0006G", "Matagalpa", "8633-1913", "1982-01-09", "montenegro.jose.m@gmail.com", "456")

mostrar(test1)
mostrar(test2)




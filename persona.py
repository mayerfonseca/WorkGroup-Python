class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    # Property apellido
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    #Property cedula
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, value):
        self.__cedula = value

    @cedula.deleter
    def cedula(self):
        del self.__cedula

    #Property direccion
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    #Property telefono
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @telefono.deleter
    def telefono(self):
        del self.__telefono

    #Property fecha_nacimiento
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

    @fecha_nacimiento.deleter
    def fecha_nacimiento(self):
        del self.__fecha_nacimiento

    # Property email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email
    @classmethod
    def crear_persona(self,nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email):
        """Metodo para realizar una instanciación de Persona"""
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email

#def factory(type):
class Profesor(Persona):
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email, id_profesor):
        super(Profesor, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        self.id_profesor = id_profesor

        # Property id_profesor
        @property
        def id_profesor(self):
            return self._id_profesor

        @email.setter
        def id_profesor(self, value):
            self._id_profesor = value

        @id_profesor.deleter
        def id_profesor(self):
            del self._id_profesor

class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email, id_estudiante):
        super(Estudiante, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        self.id_estudiante = id_estudiante

        # Property id_estudiante
        @property
        def id_estudiante(self):
            return self._id_estudiante

        @id_estudiante.setter
        def id_estudiante(self, value):
            self._id_estudiante = value

        @id_estudiante.deleter
        def id_estudiante(self):
            del self._id_estudiante




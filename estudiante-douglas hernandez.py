class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, f_nacimiento, email):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.f_nacimiento = f_nacimiento
        self.email = email
    @property
    def Nombre(self):
        return self.nombre
    @Nombre.setter
    def Nombre(self, value):
        self.nombre = value

    @property
    def Apellido(self):
        return self.apellido
    @Apellido.setter
    def Apellido(self, value):
        self.apellido = value

    @property
    def Cedula(self):
        return self.cedula
    @Cedula.setter
    def Cedula(self, value):
        self.cedula = value

    @property
    def Direccion(self):
        return self.direccion
    @Direccion.setter
    def Direccion(self, value):
        self.direccion = value

    @property
    def Telefono(self):
        return self.telefono
    @Telefono.setter
    def Telefono(self, value):
        self.telefono = value

    @property
    def F_nacimiento(self):
        return self.f_nacimiento
    @F_nacimiento.setter
    def F_nacimiento(self, value):
        self.f_nacimiento = value

    @property
    def Email(self):
        return self.email
    @Email.setter
    def Email(self, value):
        self.email = value

class Estudiante(Persona):
    def __init__(self, Nombre, Apellido, Cedula, Direccion, Telefono, Fecha_nacimiento, email,id_estudiante):
        super(Estudiante, self).__init__(Nombre, Apellido, Cedula, Direccion, Telefono, Fecha_nacimiento, email)
        self.id_estudiante = id_estudiante

    @property
    def id_estudiante(self):
        return self.id_estudiante
    @id_estudiante.setter
    def id_estudiante(self, value):
        self.id_estudiante = value

class Profesor(Persona):
    def __init__(self, Nombre, Apellido, Cedula, Direccion, Telefono, Fecha_nacimiento, email, id_profesor):
        super(Profesor, self).__init__(Nombre, Apellido, Cedula, Direccion, Telefono, Fecha_nacimiento, email)
        self.id_profesor = id_profesor

class personfactory:
    global carnet
    def crear_persona(id_type):
        if id_type >= 1001:
            carnet = Estudiante.id_estudiante
            return carnet
        if id_type <= 1000:
            carnet = Profesor.id_profesor
            return carnet

name = input("ingrese su nombre.\n-")
lastname = input("ingrese su apellido.\n-")
id = input("ingrese su cedula.\n-")
cel = input("ingrese su telefono.\n-")
direc = input("ingrese su direccion.\n-")
f_n = input("ingrese su fecha de nacimiento.\n-")
mail = input("ingrese su email.\n-")
carnet = int(input("ingrese su id.\n-"))
person = personfactory.crear_persona(carnet)
Persona(name, lastname, id, cel, direc, f_n, mail)
print(personfactory.crear_persona(carnet))


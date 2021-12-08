import aula
import curso
import edificio
import matricula
import persona
import programa
import tipoprofesor
from persona import Persona
from persona import *

# nombre_persona = input("Ingrese sus Nombres: ")
# apellido_persona = input("Ingrese sus Apellidos: ")
# cedula_persona = input("Ingrese su No Cedula: ")
# direccion_persona = input("Ingrese su dirección: ")
# telefono_persona = input("Ingrese su telefono: ")
# fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
# email_persona = input("Ingrese su email: ")

nombre_persona = "Jose Alexander"
apellido_persona = "Martinez Briones"
cedula_persona = "Cedula"
direccion_persona = "Dirección"
telefono_persona = "Telefono"
fecha_nacimiento = "fecha de nacimiento"
email_persona = "email"
id_profesor = "256898"

entidad = Persona.factory("Profesor")
entidad.crear(nombre_persona, apellido_persona, cedula_persona, direccion_persona, telefono_persona, fecha_nacimiento, email_persona, id_profesor)



print(entidad.nombre + " " + entidad.apellido)


# Definición de la primera clase base (superclase) Persona
class Persona:
    # Constructor de la clase Persona, se llama al crear una nueva instancia de Persona
    def __init__(self, nombre, edad):
        # Inicialización de atributos de instancia nombre y edad con los valores proporcionados
        self.nombre = nombre
        self.edad = edad

# Definición de la segunda clase base (superclase) Empleado
class Empleado:
    # Constructor de la clase Empleado, se llama al crear una nueva instancia de Empleado
    def __init__(self, salario):
        # Inicialización del atributo de instancia salario con el valor proporcionado
        self.salario = salario

# Definición de una subclase EmpleadoConNombre que hereda de las clases base Persona y Empleado
class EmpleadoConNombre(Persona, Empleado):
    # Constructor de la subclase EmpleadoConNombre, se llama al crear una nueva instancia de EmpleadoConNombre
    def __init__(self, nombre, edad, salario):
        # Llama al constructor de la superclase Persona para inicializar los atributos nombre y edad
        Persona.__init__(self, nombre, edad)
        # Llama al constructor de la superclase Empleado para inicializar el atributo salario
        Empleado.__init__(self, salario)

# Crear una instancia de la subclase EmpleadoConNombre llamada empleado1
empleado1 = EmpleadoConNombre("Juan", 30, 50000)

# Acceder a atributos heredados de ambas clases base e imprimir la información
print(f"{empleado1.nombre} tiene {empleado1.edad} años y gana ${empleado1.salario}.")



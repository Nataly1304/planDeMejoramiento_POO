
# Definición de la clase Estudiante
class Estudiante:
    # Constructor de la clase, se llama al crear una nueva instancia de Estudiante
    def __init__(self, nombre, edad, nota):
        # Inicialización de atributos de instancia con los valores proporcionados
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    # Método que imprime la información del estudiante
    def mostrarInformacion(self):
        # Utiliza f-strings para formatear la cadena con el nombre, edad y nota del estudiante
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}")

# Creación de una instancia de la clase Estudiante (objeto estudiante1)
estudiante1 = Estudiante("Maria", 20, 95)

# Llamada al método mostrar_informacion de la instancia estudiante1
estudiante1.mostrarInformacion()



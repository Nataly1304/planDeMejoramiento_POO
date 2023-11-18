
# Definición de la clase llamada Vehiculo
class Vehiculo:
    # Constructor (__init__) que inicializa el atributo marca
    def __init__(self, marca):
        self.marca = marca

    # Método para obtener la información del vehículo
    def obtenerInfo(self):
        return f"Vehículo de marca {self.marca}"

# Definición de una subclase llamada Coche que hereda de la clase Vehiculo
class Coche(Vehiculo):
    # Constructor de la subclase Coche, que inicializa también el modelo
    def __init__(self, marca, modelo):
        # Llamada al constructor de la clase base (Vehiculo) utilizando super()
        super().__init__(marca) # super() Permite acceder y ejecutar métodos de la clase base desde la subclase, 
        #facilitando así la implementación y extensión de funcionalidades
        # Inicialización del nuevo atributo modelo
        self.modelo = modelo

    # Método para obtener la información específica del coche
    def obtenerInfo(self):
        # Llamada al método obtenerInfo de la clase base utilizando super()
        return f"Coche de marca {self.marca}, modelo {self.modelo}"

# Crear una instancia de la clase Coche
miCoche = Coche("Honda", "Jazz")

# Llamar al método obtener_info de la clase Coche
print(miCoche.obtenerInfo())
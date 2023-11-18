
# Definición de la clase base Vehiculo
class Vehiculo:
    # Método que debe ser implementado por las subclases
    def conducir(self):
        # Lanza una excepción si el método no es implementado en la subclase
        raise NotImplementedError("Subclases deben implementar este método")

# Definición de la subclase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    # Implementación del método conducir para la subclase Coche
    def conducir(self):
        # Retorna la cadena indicando que se está manejando un coche
        return "Manejar un coche"

# Definición de la subclase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    # Implementación del método conducir para la subclase Moto
    def conducir(self):
        # Retorna la cadena indicando que se está conduciendo una moto
        return "Conducir una moto"

# Creación de una instancia de la subclase Coche
coche = Coche()

# Creación de una instancia de la subclase Moto
moto = Moto()

# Imprime el resultado de llamar al método conducir de la instancia de Coche
print(coche.conducir())  # Salida: Manejar un coche

# Imprime el resultado de llamar al método conducir de la instancia de Moto
print(moto.conducir())  # Salida: Conducir una moto 
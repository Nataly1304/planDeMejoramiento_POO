
# Definición de la clase base Vehiculo
class Vehiculo:
    def acelerar(self):
        # Este método no tiene implementación real, solo sirve como un esquema base para las subclases.
        pass

# Definición de la subclase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def acelerar(self):
        # Este método sobrescribe el método acelerar de la clase base para devolver una cadena específica para automóviles.
        return "El automóvil acelera"

# Definición de la subclase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def acelerar(self):
        # Este método sobrescribe el método acelerar de la clase base para devolver una cadena específica para bicicletas.
        return "La bicicleta pedalea más rápido"

# Definición de la subclase Barco que hereda de Vehiculo
class Barco(Vehiculo):
    def acelerar(self):
        # Este método sobrescribe el método acelerar de la clase base para devolver una cadena específica para barcos.
        return "El barco aumenta su velocidad"

# Definición de la función aplicarAceleracion
def aplicarAceleracion(vehiculo):
    # Esta función toma un objeto de tipo Vehiculo como argumento y llama al método acelerar del vehículo.
    return vehiculo.acelerar()

# Creación de instancias de las clases
auto = Automovil()
bicicleta = Bicicleta()
barco = Barco()

# Llamadas a la función aplicarAceleracion para cada vehículo y se imprime el resultado
print(aplicarAceleracion(auto))
print(aplicarAceleracion(bicicleta))
print(aplicarAceleracion(barco))

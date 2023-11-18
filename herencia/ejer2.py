
# Definición de la clase base (superclase) Fruta
class Fruta:
    # Constructor de la clase Fruta, se llama al crear una nueva instancia de Fruta
    def __init__(self, nombre):
        # Inicialización del atributo de instancia nombre con el valor proporcionado
        self.nombre = nombre

# Definición de una subclase Manzana que hereda de la clase base Fruta
class Manzana(Fruta):
    # Constructor de la subclase Manzana, se llama al crear una nueva instancia de Manzana
    def __init__(self, nombre, color):
        # Llama al constructor de la superclase Fruta para inicializar el atributo nombre
        super().__init__(nombre)
        # Inicialización del atributo de instancia color con el valor proporcionado
        self.color = color

# Crear una instancia de la subclase Manzana llamada mi_manzana
manzana1= Manzana("Manzana Gala", "Rojo")

# Acceder a atributos heredados y específicos de la subclase Manzana e imprimir la información
print(f"{manzana1.nombre} de color {manzana1.color}.")


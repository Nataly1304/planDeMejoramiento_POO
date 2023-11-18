
# Definición de la clase base (superclase) llamada Animal
class Animal:
    # Método para obtener el sonido del animal
    def hacerSonido(self):
        return "Sonido genérico"

# Definición de una subclase llamada Perro que hereda de la clase Animal
class Perro(Animal):
    # Método para obtener el sonido específico del perro
    def hacerSonido(self):
        return "Woof!"

# Función que toma un animal como parámetro y llama a su método hacerSonido
def hacerSonidoAnimal(animal):
    return animal.hacerSonido()

# Crear instancias de las clases Animal y Perro
animal = Animal()
perro = Perro()

# Llamar a la función hacer_sonido_animal con diferentes tipos de animales
sonidoAnimalGenerico = hacerSonidoAnimal(animal)
sonidoPerro = hacerSonidoAnimal(perro)

# Imprimir los resultados
print(sonidoAnimalGenerico)
print(sonidoPerro)
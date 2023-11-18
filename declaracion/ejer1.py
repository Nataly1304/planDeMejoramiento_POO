
# definicion de la clase coche 
class Coche: # aca declaramos una clase llamada coche 
    def __init__(self, marca, modelo, año):  # se define el método constructor __init__ que se llama cuando se crea una nueva 
    #instancia de la clase. Este método inicializa los atributos marca, modelo y año del objeto.
        self.marca = marca # aca ya se le asigna el valor de marca al atributo marca del objeto.
        self.modelo = modelo # aca ya se le asigna el valor de modelo al atributo modelo del objeto.
        self.año = año # aca ya se le asigna el valor de año al atributo año del objeto.
        # self se refiere a la instancia actual de la clase. Permitiendo acceder a los atributos y métodos de esa instancia dentro de los métodos de la clase.
    def obtenerInfo(self): # en esta liena se define un método llamado obtenerInfo que toma self como parámetro (la instancia del objeto).
        return f"{self.año} {self.marca} {self.modelo}"  # aca ya se devuelve una cadena que contiene el año, la marca y el modelo del coche.

# aca Crea una instancia de la clase Coche
miCoche = Coche("Toyota", "Camry", 2000) 

# Llamar al método obtenerInfo y mostrar la información del coche
print(miCoche.obtenerInfo())  # aca ya se imprime todo         
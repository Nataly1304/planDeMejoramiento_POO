
# Definición de la clase Libro
class Libro:
    # Constructor de la clase, se llama al crear una nueva instancia de Libro
    def __init__(self, titulo, autor):
        # Inicialización de atributos de instancia con los valores proporcionados
        self.titulo = titulo
        self.autor = autor
    
    # Método que imprime la información del libro
    def obtenerInfo(self):
        # Utiliza f-strings para formatear la cadena con el título y autor del libro
        print(f"Libro: {self.titulo} - Autor: {self.autor}")

# Creación de una instancia de la clase Libro (objeto libro1)
libro1 = Libro("Harry Potter", "J.K. Rowling")

# Llamada al método obtenerInfo de la instancia libro1
libro1.obtenerInfo()


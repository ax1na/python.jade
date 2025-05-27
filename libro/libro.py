#jade rojas
#26-5-25

class Libro:
    # <----- esto es la "inicializar sin inicializarse" ----->
    # titulo = "sin titulo"
    # autor = "desconocido"
    # paginas = 0
    # genero = "indefinido"
    # copias_disponibles = 0

    def __init__(self,titulo,autor,paginas,genero,copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.copias_disponibles = copias_disponibles
    def atributos(self):
        print(self.titulo, ":", sep="")
        print("*Autor:", self.autor)
        print("*Paginas:", self.paginas)
        print("*Genero:", self.genero)
        print("*Copias disponibles:", self.copias_disponibles)
    def incrementar_copias(self, nuevas_copias):
        self.copias_disponibles = self.copias_disponibles + nuevas_copias
    def esta_disponible(self):
        return self.copias_disponibles > 0
    def agotado(self):
        self.copias_disponibles == 0
        print(self.titulo, " Esta agotado")
    def prestar(self, copias=1):
        if self.copias_disponibles >= copias:
            self.copias_disponibles -= copias
            print(f"Has prestado {copias} copia(s) de '{self.titulo}'.")
        else:
            print(f"No hay suficientes copias de '{self.titulo}' para prestar.")

mi_libro = Libro("El Principito", "Antoine de Saint-Exupéry", 96, "Ficción", 10)
mi_libro.atributos()
mi_libro.agotado()
print("¿Está disponible?", mi_libro.esta_disponible())
print("\n <----- Prestar copias de libro ----->")
mi_libro.prestar(3)
mi_libro.atributos()

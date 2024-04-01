class Llibre:
    def __init__(self):
        self.titol = input("Introduce el título del libro: ")
        self.autor = input("Introduce el autor del libro: ")
        self.exemplars = int(input("Introduce el número de ejemplares disponibles: "))

    def informacio(self):
        return f"Título: {self.titol}, Autor: {self.autor}, Ejemplares disponibles: {self.exemplars}"
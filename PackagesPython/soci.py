class Soci:
    def __init__(self):
        self.nom = input("Introduce el nombre del socio: ")
        self.cognom = input("Introduce el apellido del socio: ")
        self.num_soci = input("Introduce el número de socio: ")

    def informacio(self):
        return f"Nombre: {self.nom}, Apellido: {self.cognom}, Número de socio: {self.num_soci}"
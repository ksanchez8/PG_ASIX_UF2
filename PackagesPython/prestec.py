class Prestec:
    def __init__(self, llibre, soci, data_prestec):
        self.llibre = llibre
        self.soci = soci
        self.data_prestec = data_prestec

    def informacio(self):
        return f"Llibre: {self.llibre.informacio()}, Socio: {self.soci.informacio()}, Fecha de préstamo: {self.data_prestec}"
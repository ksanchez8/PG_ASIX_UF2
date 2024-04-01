from llibre import Llibre
from soci import Soci
from prestec import Prestec

if __name__ == "__main__":
    llibre1 = Llibre()
    soci1 = Soci()
    data_prestec = input("Introduce la fecha de préstamo (en formato YYYY-MM-DD): ")
    prestec1 = Prestec(llibre1, soci1, data_prestec)

    
    print(llibre1.informacio())
    print(soci1.informacio())
    print(prestec1.informacio())
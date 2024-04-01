"""
Enunciado del ejercicio:
Gestió de Biblioteca

Imagina que estàs desenvolupant un sistema de gestió per una biblioteca. Necessites crear un conjunt de classes que permetin gestionar llibres, socis i préstecs.

Requisits:

1. Llibre
   - Té títol, autor i número d'exemplars disponibles.
   - Un exemplar es pot tenir en préstec, retornar i s'ha de poder obtenir informació del llibre.

2. Soci:
   - Té nom, cognom i número de soci.
   - Ha de poder sol·licitar un préstec, retornar un préstec i mostrar la informació del soci.

3. Préstec:
   - Té quin llibre està en préstec, el soci que el té i la data de préstec.
   - S'ha de poder registrar el préstec, retornar el préstec i mostrar la informació del préstec.

Que has de fer?

Fent servir python, crea un package per fer aquest exercici. Cada Classe ha d'estar en el seu propi mòdul. Els imports han d'estar en el seu lloc.
"""

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
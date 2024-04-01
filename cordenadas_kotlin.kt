/*
Hay que realizar el siguiente codigo en kotlin:
class Coordenada:
    def __init__(self, x=0, y=0) -> None:
        self.x: int = x
        self.y: int = y
def moure_dreta(coordenada: Coordenada) -> Coordenada:
    return Coordenada(coordenada.x + 1, coordenada.y)
def moure_esquerra(coordenada: Coordenada) -> Coordenada:
    return Coordenada(coordenada.x - 1, coordenada.y)
def moure_amunt(coordenada: Coordenada) -> Coordenada:
    return Coordenada(coordenada.x, coordenada.y + 1)
def moure_avall(coordenada: Coordenada) -> Coordenada:
    return Coordenada(coordenada.x, coordenada.y - 1)
class Main:
    def __init__(self) -> None:
        coordenada: Coordenada = Coordenada()
        nova_coordenada = moure_dreta(coordenada)
        print(f"Nova coordenada despres de moure a la dreta: ({nova_coordenada.x}, {nova_coordenada.y})")

        nova_coordenada = moure_amunt(nova_coordenada)
        print(f"Nova coordenada despres de moure amunt: ({nova_coordenada.x}, {nova_coordenada.y})") 
        print(f"Nova coordenada despres de moure amunt: ({nova_coordenada.x}, {nova_coordenada.y})")


Main()
 */

class Coordenada(var x: Int = 0, var y: Int = 0)

fun moureDreta(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x + 1, coordenada.y)
}

fun moureEsquerra(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x - 1, coordenada.y)
}

fun moureAmunt(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y + 1)
}

fun moureAvall(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y - 1)
}

class Main {
     init {
        val coordenada = Coordenada()
        var novaCoordenada = moureDreta(coordenada) //Movimiento de la coordenada hacia la derecha y asignación de la nueva coordenada a novaCoordenada
        println("Nova coordenada despres de moure a la dreta: (${novaCoordenada.x}, ${novaCoordenada.y})")



     }
}
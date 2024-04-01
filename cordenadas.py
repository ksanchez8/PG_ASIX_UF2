"""
Descompon aquest codi en funcions més petites per millorar la seva modularitat i reutilització. 

Pista: Volem poder moure'ns per una graella bidimensional.

Codi Python:

# Coordenada inicial
coordenada = (0, 0)

# Programa principal
def moure_dreta(coordenada):
    x, y = coordenada
    nova_coordenada = (x + 1, y)
    return nova_coordenada

def moure_esquerra(coordenada):
    x, y = coordenada
    nova_coordenada = (x - 1, y)
    return nova_coordenada

def moure_amunt(coordenada):
    x, y = coordenada
    nova_coordenada = (x, y + 1)
    return nova_coordenada

def moure_avall(coordenada):
    x, y = coordenada
    nova_coordenada = (x, y - 1)
    return nova_coordenada

# Executar moviments
coordenada = moure_dreta(coordenada)
print(f"Nova coordenada després de moure a la dreta: {coordenada}")

coordenada = moure_amunt(coordenada)
print(f"Nova coordenada després de moure amunt: {coordenada}")
"""

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
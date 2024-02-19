#/PRE: Feu un programa anomenat GenerarHistograma que mostri l’histograma de totes les tirades possibles amb dos daus de sis cares. 
#Per fer això, l’estratègia que s’ha considerat és desar dins d’un  array el nombre de repeticions de cada tirada possible (sempre entre 2 i 12) 
#i després treballar a partir d’aquests valors. 

resultados = [] # Lista para almacenar los resultados de las tiradas
maxim_tirades = 36 # Número máximo de tiradas

def contar_repeticiones(maxim_tirades):
    # Generar todas las combinaciones posibles de dos dados
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            suma = dado1 + dado2
            print(f"{dado1} + {dado2} ES {suma}")
            resultados.append(suma)

    # Inicializar variables fuera del segundo bucle
    max_repeticiones = 0
    num_max_repeticiones = None

    # Contar las repeticiones de cada suma posible
    for quantitat in range(2, 13):
        repeticiones = resultados.count(quantitat)
        # Actualizar variables si se encuentra una mayor repetición
        if repeticiones > max_repeticiones:
            max_repeticiones = repeticiones
            num_max_repeticiones = quantitat

    # Imprimir el resultado con el número que más se repite y cuántas veces
    print(f"El numero que mas se repite es: {num_max_repeticiones}, que se repite {max_repeticiones} veces.")

    return resultados

contar_repeticiones(maxim_tirades)

#POST:A continuació, ha de dir quin valor de tirada és el que té més repeticions. 
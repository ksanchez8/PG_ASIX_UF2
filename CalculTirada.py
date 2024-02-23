
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

def calcular_probabilitat(valor):
    if 2 <= valor <= 12:
        tirades_valor = 0
        for tirada in resultados:
            if tirada <= valor:
                tirades_valor += 1
        probabilitat = (tirades_valor * 100) // len(resultados)
        print(f"La probabilitat és {probabilitat:.0f}%.")
    else:
        print("El valor no esta entre 2 i 12.")



contar_repeticiones(maxim_tirades)

valor_a_calcular = int(input("Escriu el valor a calcular [2 - 12]: "))

calcular_probabilitat(valor_a_calcular)
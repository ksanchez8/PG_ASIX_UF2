resultados = []
maxim_tirades = 36

def contar_repeticiones(maxim_tirades):
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            suma = dado1 + dado2
            print(f"{dado1} + {dado2} ES {suma}")
            resultados.append(suma)

    for quantitat in range(2, 13):
        max_repeticiones = 0
        num_max_repeticiones = None
        repeticiones = resultados.count(quantitat)
        if repeticiones > max_repeticiones:
            max_repeticiones = repeticiones
            num_max_repeticiones = quantitat

    print(f"El numero que mas se repite es: {num_max_repeticiones}, que se repite {max_repeticiones} veces.")

    return resultados
            


contar_repeticiones(maxim_tirades)
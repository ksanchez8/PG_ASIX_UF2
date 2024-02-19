resultados = []
maxim_tirades = 36

def contar_repeticiones(maxim_tirades):
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            suma = dado1 + dado2
            print(f"{dado1} + {dado2} ES {suma}")
            resultados.append(suma)

    for i in range(2, 13):
        repeticiones = resultados.count(i)
        print(f"La suma {i} se repite {repeticiones} veces.")

    return resultados
            


contar_repeticiones(maxim_tirades)
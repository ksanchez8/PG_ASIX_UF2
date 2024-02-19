def contar_repeticiones(num_lanzamientos):
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            suma = dado1 + dado2
            print(f"{dado1} + {dado2} ES {suma}")

num_lanzamientos = 100
contar_repeticiones(num_lanzamientos)
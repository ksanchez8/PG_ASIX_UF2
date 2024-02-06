# Programa principal / Mostrar menú
def mostrar_menu(temperatures):
    temperatures = [20,5 21,1 21 21,7 20,9 20,6 19,9 ]
    for setmana in range(1, 53):
        print(f"\n----- Setmana {setmana} de l'any -----")
        print("\nBenvingut al registre de temperatures")
        print("-------------------------------------")
        print("[RT] Registrar temperatures setmanals.")
        print("[MJ] Consultar temperatura mitjana.")
        print("[DF] Consultar diferència màxima.")
        print("[FI] Sortir.")

        opcio = input("Opció: ")

        if opcio == 'RT':
            registrar_temperatures(temperatures)
        elif opcio == 'MJ':
            consultar_temperatura_mitjana(temperatures)
        elif opcio == 'DF':
            consultar_diferencia_maxima(temperatures)
        elif opcio == 'FI':
            break
        else:
            print("Opció no vàlida. Torna a intentar.")


mostrar_menu(temperatures)
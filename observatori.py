# Programa principal / Mostrar menú
temperatures = []
def registrar_temperatures(temperatures):
    temperatures_input = input("Introdueix les temperatures de la setmana anterior: ")

def mostrar_menu(temperatures):
    
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


#Execució del programa
mostrar_menu(temperatures)
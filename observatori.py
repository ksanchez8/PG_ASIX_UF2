# Declaració de la llista on introduirem les temperatures
temperatures = []

# Programa per introduir les temperatures
def registrar_temperatures(temperatures):
    temperatures_input = input("Introdueix les temperatures de la setmana anterior: ")
    temperatura_setmanal = [float(temp.replace(',', '.')) for temp in temperatures_input.split()]
    temperatures.append(temperatura_setmanal)

def consultar_temperatura_mitjana(temperatures):
    if not temperatures:
        print("No hi ha temperatures registrades. ")
    else:
        suma_temperaturas = 0
        for semana in temperatures:
            for temperatura in semana:
                suma_temperaturas += temperatura 
        temperatura_mitjana = suma_temperaturas / (len(temperatures) * len(semana))
        print("La temperatura mitjana és:", temperatura_mitjana)

# Programa principal / Mostrar menú
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

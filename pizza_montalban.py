"""
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
L'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria. Això inclou la presa de comandes, 
la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.
"""

def realitzar_comanda():
    print("Comanda realitzada.")

def modificar_comanda():
    print("Comanda modificada.")

def eliminar_comanda():
    print("Comanda eliminada.")

def seleccionar_pizza():
    print("Seleccionant pizza.")

def afegir_ingredients():
    print("Afegint ingredients.")

def hornear_pizza():
    print("Hornant pizza.")

def empaquetar_pizza():
    print("Empaquetant pizza.")

def afegir_ingredients_estoc():
    print("Afegint ingredients a l'estoc.")

def actualitzar_estoc():
    print("Actualitzant estoc.")

def consultar_estoc():
    print("Consultant estoc.")

def calcular_import_total():
    print("Calculant import total.")

def seleccionar_metode_pagament():
    print("Seleccionant mètode de pagament.")

def realitzar_pagament():
    print("Realitzant pagament.")

def emetre_ticket():
    print("Emetent ticket.")

def inicialitzar_sistema():
    print("Inicialitzant sistema.")

def tancar_sistema():
    print("Tancant sistema.")

def generar_informes():
    print("Generant informes.")

def gestionar_pizzeria():
    print("Benvingut a la pizzeria!")
    while True:
        print("1. Gestionar Comandes")
        print("2. Preparar Pizzes")
        print("3. Gestionar Estoc d'Ingredients")
        print("4. Processar Pagaments")
        print("5. Gestionar Sistema")
        print("6. Sortir")

        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            realitzar_comanda()
            modificar_comanda()
            eliminar_comanda()

        elif opcio == "2":
            seleccionar_pizza()
            afegir_ingredients()
            hornear_pizza()
            empaquetar_pizza()

        elif opcio == "3":
            afegir_ingredients_estoc()
            actualitzar_estoc()
            consultar_estoc()

        elif opcio == "4":
            calcular_import_total()
            seleccionar_metode_pagament()
            realitzar_pagament()
            emetre_ticket()

        elif opcio == "5":
            inicialitzar_sistema()
            tancar_sistema()
            generar_informes()

        elif opcio == "6":
            print("Gràcies per visitar la pizzeria. Fins aviat!")
            break

        else:
            print("Opció no vàlida. Per favor, selecciona una opció correcta.")

gestionar_pizzeria()

"""
EJERCICIO CORREGIDO

1. Gestionar Pizzaria
1.1 Tomar Pedido
1.2 Preparar pedido
1.3 Gestión inventario
1.4 Proceso pago

1.1.1 -Listado de pizza o interficie de usuario
1.1.2 -Verificar stock
1.2.1 -Cocina
1.2.2 -Verificar (QA)
1.3.1 -Atualizar
1.3.2 -Reabastecer
1.4.1 -Calcular costes
1.4.2 -Factura



"""
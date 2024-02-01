"""
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
L'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria. Això inclou la presa de comandes, 
la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.
"""
def mostrar_menu(): #Se crea el menu, mostrando las pizzas a elejir
    menu = {
        "1. Barbacoa": 10€,
        "2. Margarita": 10€,
        "3. Hawuaiana": 11€
    }
    print(menu)
    
    opcion = input("Selecciona la pizza: ")

def estoc_ingredients(): #Se añade para poder introducir lo que hay que reponer
    falta_stock = True
    while falta_stock:
        ingredientes = input("Introduce el ingrediente que falta: ")



def inteficie_usuari():
    print("Bienvenido a Pizzeria MVM")
    pizza = input("Inbtoduce el nombre de la pizz: ")
    ingrediente = input("Intoduce los ingredientes (separados por comas): ").split(',')
    return{"pizza": pizza, "ingredientes": ingrediente}

def verificar_stock(pedido):
    for ingrediente in pedido['ingredientes']:
        if ingrediente in stock:

    return False

def cocina():
    ...

def control_calidad():
    ...

def actualizat_stock():
    ...

def calculo_costes():
    ...

def calculo_costes():
    ...

def facturacion()
def contar_as():
    global fi #Global para no tener problemas con el scope
    fi = False

    while not fi:
        introducir_frase = input("Escriu la frase: ")
        
    
        if introducir_frase == "fi":
            salida()

        else:
            frase_minusculas = introducir_frase.casefold().count('a') #casefold para contar las letras
            print(f'La frase amb mes \'a\' es "{introducir_frase}"')
            print(f'Té {frase_minusculas} \'a\'')

def salida(): #Creación del def de salida
    global fi
    fi = True


contar_as()

def contar_as():
    global fi
    fi = False

    while not fi:
        introducir_frase = input("Escriu la frase: ")
        
    
        if introducir_frase == "fi":
            salida()

        else:
            frase_minusculas = introducir_frase.casefold().count('a')
            print(f'La frase amb mes \'a\' {introducir_frase}')
            print(f'Té {frase_minusculas}')

def salida():
    global fi
    fi = True


contar_as()

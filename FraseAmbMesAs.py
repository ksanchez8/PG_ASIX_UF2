def frase():
    introducir_frase = input("Escriu la frase: ")
    return introducir_frase

def contar_as():
    frase_minusculas = introducir_frase.casefold().count('a')
    

frase()
contar_as()

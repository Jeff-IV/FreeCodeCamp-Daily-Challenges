##Dada una cadena de palabras, devuelve solo las palabras con un número impar de letras.

#Las palabras de la cadena proporcionada estarán separadas por un solo espacio.
#Devuelve las palabras separadas por un solo espacio.


def get_odd_words(s : str) -> str:
    
    def es_impar(palabra: str) -> bool:
        tamaño = len(palabra)
        if tamaño%2 == 1: # Si el residuo de la divison del tamaño y 2 es 1 entonces es impar
            return True
        else:
            return False
     
    palabras = s.split(" ")
    #lista_palabras_impares = [] 
    resultado = ""
    
    for palabra in palabras:
        if es_impar(palabra=palabra):
            #lista_palabras_impares.append(palabra)
            resultado = resultado + " " + palabra
        else: 
            continue
        
    #resultado = " ".join(lista_palabras_impares)

    return resultado

resultado = get_odd_words("Habia una vez un arcoiris grande en el cielo")
print(resultado)
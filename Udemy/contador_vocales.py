# Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".

# Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de vocales encontradas es el que se debe imprimir).


cadena = "Hola Mundo"
contador_vocales = 0
vocales = "a,e,i,o,u"


for letra in cadena:
    if letra in vocales:
        contador_vocales += 1  # Simplemente suma cuando encuentra un elemento en "vocales"

print(contador_vocales)


for letra in cadena:
    if letra in vocales:
        print(letra)

# Escribe una función en Python que acepte dos números enteros. Si el producto de ambos números es menor o igual a 1000, devuelve su producto; de lo contrario, devuelve su suma.

# Objetivo del ejercicio: Aprender el flujo de control básico y el uso de las sentencias if-else. Comprender cómo las decisiones del código modifican el resultado en función de un umbral matemático.


def operacion(n1,n2):
    producto = n1 * n2
    suma = n1 + n2
    
    
    if producto <= 1000:
        return producto
    else:
        return suma
        

n1 = int(input("Dame un numero: "))
n2 = int(input("Dame un numero: "))


resultado = operacion(n1, n2)

print(resultado)
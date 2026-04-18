import time

# Escribe un bucle for que cuente hasta cinco.
for i in range(1,6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(f"{i} Mississippi")
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)

# Escribe una función print con el mensaje final.
print("Lista o no, aquí vengo!")




largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")


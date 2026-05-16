from random import randint


num_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != num_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input("Adivina el numero secreto entre 1-50:  "))
    # AGREGAMOS UNA AYUDA AL JUGADOR
    if adivinanza < num_secreto:
        print("El numero es mayor...")
    if adivinanza > num_secreto:
        print("El numero es menor...")
    # INCREMENTAMOS LA VARIABLE DE INTENTOS
    intentos += 1
if adivinanza == num_secreto:
    print(f"Felicidades adivinaste el numero secreto en {intentos} intentos!!")
else:
    print(f"Se acabaron tus intentos maximos: {INTENTOS_MAXIMOS}")
    print(f"El numero secreto era {num_secreto}")

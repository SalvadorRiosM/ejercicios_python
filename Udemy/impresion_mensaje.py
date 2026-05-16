mensaje = input("Mensaje a repetir: ")
numero_de_repeticiones = int(input("Proporciona el numero de repeticiones: "))


for i in range(numero_de_repeticiones):
    print(i + 1, mensaje)


# SE LE PONE GUION BAJO PARA QUE NO MUESTRE NINGUN INDICE
for _ in range(numero_de_repeticiones):
    print(i + 1, mensaje)

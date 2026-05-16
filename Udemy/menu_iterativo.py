salir = False

while not salir:
    print("\nMenu:")
    print("1. Crear cuenta")
    print("2. Eliminar cuenta")
    print("3. Salir")
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print("Creando tu cuenta...")
    elif opcion == 2:
        print("Eliminando tu cuenta...")
    elif opcion == 3:
        print("Saliendo...\n")
        salir = True
    else:
        print("Opcion Invalida...")

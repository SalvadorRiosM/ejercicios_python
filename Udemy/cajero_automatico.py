salir = False
saldo = 1000
while not salir:
    print("\nOperaciones que puedes realizar:")
    print("1. Consultar saldo: ")
    print("2. Retirar: ")
    print("3. deposito: ")
    print("4. Salir: ")

    opcion = int(input("Escoja una opción: "))
    if opcion == 1:
        print(f"Tu saldo actual es ${saldo:.2f}")
    elif opcion == 2:
        retirar = float(input("Ingresa el monto a retirar: "))
        if retirar <= saldo:
            saldo -= retirar
            print(f"Tu saldo actual es: ${saldo:.2f}")
        else:
            print(f"No cuentas con suficiente saldo, cuentas con ${saldo:.2f}")
    elif opcion == 3:
        deposito = float(input("Ingresa el monto a depositar: "))
        saldo += deposito
        print(f"Tu nuevo saldo es de: ${saldo:.2f}")
    elif opcion == 4:
        print("Saliendo del cajero...")
        salir = True
    else:
        print("Opcion invalida!!")

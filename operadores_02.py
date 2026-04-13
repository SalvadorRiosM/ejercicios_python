# Estás programando el acceso a un área restringida. Para entrar, el usuario01 necesita:
# Tener 18 años o más.
# Y tener una identificación válida.
# O, si no tiene identificación, ser empleado del lugar.
# Tu reto:
# Crea estas variables:
# edad = 20
# tiene_id = False
# es_empleado = True
# Crea una variable llamada puede_entrar. Su valor debe ser una combinación de operadores.
# Pista: Usa paréntesis para agrupar la lógica: (condicion1 and condicion2) or condicion3.
# Imprime el resultado de puede_entrar.
# Prueba de fuego: Cambia es_empleado a False y mira si el resultado cambia a False.


usuario = input("Escribe tu nombre: ").strip().title()
edad = int(input("Dime tu edad: "))
identificacion = ["Narutoño", "Chaa", "Chopo", "Midori"]



if usuario in identificacion and edad >= 18:
    print(f"Acceso valido puede entrar {usuario.title()}")
    
elif edad < 18:
    print(f"Lo sentimos {usuario.title()} tiene {edad} y es menor de edad")
else:
    print(f"Acceso denegado no esta en la lista {usuario.title()}.")
    
    






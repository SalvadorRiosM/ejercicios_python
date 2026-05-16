def imprimir_persona(apellido, edad, nombre="Chaa"):
    print(f"Persona: Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")


# Diferentes formas de llamar la funcion
imprimir_persona("Perez", 28, "Ricardo")

imprimir_persona(nombre="Juan", apellido="Lopez", edad=35)

imprimir_persona("Ramirez", 50)

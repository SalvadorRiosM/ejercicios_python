def todo_mayusculas(nombre, apellido, edad):
    print("Este valor regresa varios valores en (tupla)")
    return nombre.upper(), apellido.upper(), edad


# UNPACKING
nombre, apellido, edad = todo_mayusculas("Juan", "Lopez", 54)
print(f"Su nombre es: {nombre}, apellido: {apellido} y su edad es: {edad}")

print(todo_mayusculas("chocho", "casa", 13))


# SEGUNDA FUNCION
def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z


resultado = obtener_coordenadas()
print(resultado)

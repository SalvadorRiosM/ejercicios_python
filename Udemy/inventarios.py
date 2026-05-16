inventario = []

num_productos = int(input("Cuantos productos deseas agregar al inventario? "))

for elemento in range(num_productos):
    print(f"Proporciona los valores del producto {elemento + 1}")
    # Ponemos las variables para el diccionario
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    # Creamos el diccionario de "producto"
    producto = {"id": elemento + 1, "nombre": nombre,
                "precio": precio, "cantidad": cantidad}
    # Agregamos el diccionario de "producto" a la variable vacia de "inventario"
    inventario.append(producto)
    # Fin de identacion........................................

# Mostrar el inventario inicial
print(f"\nInventario inicial {inventario}")

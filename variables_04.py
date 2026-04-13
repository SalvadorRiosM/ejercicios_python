# El concepto: En Python, una variable puede cambiar de tipo (de número a texto, por ejemplo).

# Reto: Crea una variable llamada dato y asígnale el número 10. Imprime su tipo usando type(). Luego, en la siguiente línea, cambia el valor de esa misma variable dato por el texto "Diez" e imprime su tipo otra vez.

# Objetivo: Ver en la consola cómo la misma variable cambia de int (entero) a str (string).


dato = 10
print(type(dato))
dato = "Diez"
print(type(dato))


# El concepto: Interactuar con el usuario y realizar cálculos básicos.

# Reto: Pide al usuario el nombre de un producto y su precio usando input().

# Importante: Recuerda que input() siempre devuelve texto, así que tendrás que convertir el precio a número (int o float) para poder operarlo.

# Objetivo: Imprime un mensaje que diga: "El producto [nombre] con el 16% de IVA cuesta: [precio_final]".

producto = input("Escribe el nombre de un producto: ")
precio = int(input("Escribe el precio del producto: "))
iva = precio * 16 / 100

total = iva + precio

print(f"El producto {producto} cuesta {precio} con el 16% de IVA cuesta: {total}.")
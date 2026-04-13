# El Intercambio: Crea dos variables, a = 5 y b = 10. Tu reto es intercambiar sus valores para que a valga 10 y b valga 5, pero sin escribir los números de nuevo. (Pista: necesitarás una tercera variable auxiliar).

a = 5
b = 10

# 1. Guardamos el valor de 'a' en una variable auxiliar
auxiliar = a  # auxiliar ahora vale 5

# 2. Ahora que el valor de 'a' está a salvo, podemos sobreescribir 'a'
a = b         # 'a' ahora vale 10

# 3. Finalmente, le damos a 'b' el valor que guardamos en la auxiliar
b = auxiliar  # 'b' ahora vale 5

print(f"a ahora vale: {a}")
print(f"b ahora vale: {b}")



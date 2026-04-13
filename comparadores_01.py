# Crea un nuevo archivo y simplemente imprime (usando print) el resultado directo de estas 3 preguntas: sin usar if
# ¿Es 10 mayor o igual que 10? (Usa >=)
# ¿Es "Python" exactamente igual a "python"? (Usa ==)
# ¿Es 7 diferente de 8? (Usa !=)
# Tu código debería verse algo así:
# print(10 >= 10)... y así con los demás.

print(10>=10)
print("Python" == "Python")
print(7!=7)

# El concepto: Evaluar varias condiciones a la vez.
# Reto: Imagina que para una beca necesitas: ser mayor de 17 años Y tener un promedio mayor a 8.
# Objetivo: Crea las variables edad = 18 y promedio = 8.5. Imprime el resultado de verificar si cumple ambos requisitos usando el operador and.
# Extra: Cambia el and por un or e imprime de nuevo para ver cómo cambia el resultado si solo tuviera que cumplir una de las dos.

edad = 18
promedio = 8.5

edad = 18
promedio = 8.5

# 1. Usando AND (Deben cumplirse AMBAS)
print("--- Resultado con AND ---")
# Aquí comparamos edad > 17 Y promedio > 8
print(edad > 17 and promedio > 8) 

# 2. Usando OR (Basta con que se cumpla UNA)
print("--- Resultado con OR ---")
print(edad > 17 or promedio > 8)

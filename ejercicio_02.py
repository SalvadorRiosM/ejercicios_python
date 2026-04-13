# Reto: Crea un programa que guarde la fecha de hoy en una variable. Luego, crea otra variable con una "fecha de vencimiento" (por ejemplo, el 30 de mayo de 2026).

# Objetivo: Usa un if para comparar ambas fechas. Si la fecha de hoy es menor a la de vencimiento, imprime "Acceso concedido", de lo contrario, imprime "Tu suscripción ha expirado".

from datetime import date

fecha = date.today() # Fecha de hoy

print(fecha)


fecha_vencimiento = date(2026, 5, 30) # Fecha de vencimiento



if fecha < fecha_vencimiento: # Logica
    print("Acceso concedido")
else:
    print("Tu suscripción ha expirado")
    


fecha_formateada = fecha.strftime("%d/%B/%Y")   # Formateo de la fecha ("%d/%A/%Y") ("%d/%B/%Y") 

print(f"La fecha de hoy formateada es: {fecha_formateada}")




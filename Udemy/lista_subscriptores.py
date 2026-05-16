suscriptores = {"luisa@gmail.com", "marco@gmail.com", "elena@gmail.com"}
print(f"Lista de suscriptores{suscriptores}")


nuevo_suscriptor = "karla@gmail.com"

if nuevo_suscriptor in suscriptores:
    print(f"El suscriptor ya esta en la lista: {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}")
print(f"Nueva lista: {suscriptores}")

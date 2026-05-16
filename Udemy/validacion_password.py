password = input("Ingresa un password de 6 letras: ")

while len(password) < 6:
    print("El password no tiene 6 caracteres, vuelve a intentarlo!")
    password = input("Vuelve a poner un password: ")
else:
    print("Password valido!!")

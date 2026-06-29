nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(f"Bienvenido {nombre}, tu registro fue exitoso.")
else:
    print(f"Lo siento {nombre}, debes ser mayor de 18 años para registrarte.")
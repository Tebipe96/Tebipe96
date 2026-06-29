nombre = (input("ingresa tu nombre:"))
edad = int(input("ingresa tu edad:"))
correo = (input("ingresa tu correo:"))

if edad >= 18:
    print(f"bievenido {nombre}. eres mayor de edad y estas habilitado para ingresar")
else:
    print(f"lo sien {nombre}, debes ser mayor de edad para ingresar")
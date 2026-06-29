usuario = (input("ingresa tu usuario:"))
edad  = int(input("ingresa tu edad:"))
correo = (input("ingresa tu correo:"))
if edad < 18:
    print ("lo siento, eres menor de edad, no puedes registrarte")
else: edad >= 18
contreseña = input("ingresa tu contreseña maximo 6 caracteres:")
if len(contreseña) > 6:
        print("lo siento, la contreseña debe tener al menos 6 caracteres")
        contraseña = input("ingresa tu contraseña:")
else:
 print("registro exitoso")
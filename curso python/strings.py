# STRINGS

#Algunos usos comunes
# Guardar nombres
nombre = "Esteban"
apellido = "Peralta"
# Mostrar mensajes
print("Bienvenido al sistema")
#Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
print("Hola", nombre)

# ⚠️ Todo lo que devuelve input() es un string.

# Guardar correos, direcciones o teléfonos
email = "esteban@gmail.com"
telefono = "3804266096"
# Comparar textos
usuario = "admin"

if usuario == "admin":
    print("Acceso permitido")
# Buscar palabras dentro de un texto
mensaje = "Hola Esteban"

print("Esteban" in mensaje)

Resultado:

True
# Convertir texto a mayúsculas o minúsculas
nombre = "esteban"

print(nombre.upper())  # ESTEBAN
print(nombre.capitalize())  # Esteban
# Crear contraseñas, menús y formularios
password = input("Ingrese su contraseña: ")

if password == "1234":
    print("Acceso correcto")
else:
    print("Contraseña incorrecta")
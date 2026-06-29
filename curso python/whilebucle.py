i = 1
while i <= 5:
    print(f"el valor de i es: {i}")
    i = i + 1 #ué ocurre paso a paso: i = 1/Python pregunta: i <= 5 → 1 <= 5 → True/Ejecuta el bloque: print(...) i = i + 1

clave = "" #también puede usarse para pedir datos hasta que el usuario escriba algo válido:

while clave != "1234":
    clave = input("Ingresa la clave: ")

print("Acceso permitido") 



clave_correcta = "1234"
clave = ""

while clave != clave_correcta:
    clave = input("Ingresa la clave: ")

    if clave != clave_correcta:
        print("Clave incorrecta. Intenta nuevamente.")

print("Acceso permitido")

#while → repetir mientras ocurra una condición.

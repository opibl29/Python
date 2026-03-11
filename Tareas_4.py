"""
num = int(input("Numero: "))

for i in range(1, 13):
    print(num, "x", i, "=", num*i)

"---------------------------------------------------------------------------------------------------------------------------"

usuario = "admin"
clave = "1234"

for i in range(3):
    u = input("Usuario: ")
    c = input("Clave: ")

    if u == usuario and c == clave:
        print("Bienvenido")
        break
    elif u != usuario or c != clave:
        print("Incorrecto")
    else:
        print("Ha agotado todos los intentos")

"---------------------------------------------------------------------------------------------------------------------------"



"---------------------------------------------------------------------------------------------------------------------------"

secreta = "python"
palabra = input("Adivina la palabra: ")

if palabra == secreta:
    print("Correcto!")
else:
    print("Incorrecto")

"---------------------------------------------------------------------------------------------------------------------------"
"""

oracion = input("Escribe una oracion: ")

letras = 0
vocales = 0

for c in oracion:
    if c.isalpha():
        letras += 1
        if c.lower() in "aeiou":
            vocales += 1

palabras = len(oracion.split())
espacios = oracion.count(" ")

print("Letras:", letras)
print("Vocales:", vocales)
print("Espacios:", espacios)
print("Palabras:", palabras)
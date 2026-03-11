"""
nombres = []

for i in range(5):
    nombre = input("Nombre: ")
    if len(nombre) > 3:
        nombres.append(nombre)

print(nombres)


lista = [1,2,3,4,5]
print("Tamaño:", len(lista))


"---------------------------------------------------------------------------------------------------------------------------"




numeros = []

for i in range(5):
    n = int(input("Numero: "))
    numeros.append(n)

print("Suma:", sum(numeros))

"---------------------------------------------------------------------------------------------------------------------------"

"""

personas = []

for i in range(3):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    personas.append([nombre, apellido, edad])

for i in range(len(personas)):
    print(i+1, personas[i])


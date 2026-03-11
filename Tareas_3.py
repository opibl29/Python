"""
num = int(input("Numero: "))

if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")



"---------------------------------------------------------------------------------------------------------------------------"

num = int(input("Numero: "))

contador = 0

for i in range(1, num+1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print("Es primo")
else:
    print("No es primo")
"---------------------------------------------------------------------------------------------------------------------------"

texto = input("Escribe algo: ")

if texto.isalpha():
    print("Solo letras")
elif texto.isdigit():
    print("Solo numeros")
else:
    print("Tiene letras, numeros o signos")

"---------------------------------------------------------------------------------------------------------------------------"


edad = int(input("Edad: "))
vive = input("Vive en RD (si/no): ")
trabaja = input("Trabaja (si/no): ")

if edad >= 18 and vive == "si" and trabaja == "si":
    print("Puede optar por nacionalidad dominicana")
else:
    print("No cumple los requisitos")
"---------------------------------------------------------------------------------------------------------------------------"
"""
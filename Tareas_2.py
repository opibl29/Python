"""
tasa = 60.25  # puedes cambiarla

op = input("Escribe 1 para pesos a dólares o 2 para dólares a pesos: ")

monto = float(input("Escribe el monto: "))

if op == "1":
    print("Dólares:", monto / tasa)
else:
    print("Pesos:", monto * tasa)

"---------------------------------------------------------------------------------------------------------------------------"

prestamo = float(input("Valor del prestamo: "))
tiempo = int(input("Tiempo en meses: "))
interes = float(input("Interes (%): "))

total = prestamo + (prestamo * interes / 100)
cuota = total / tiempo

print("Total a pagar:", total)
print("Cuota mensual:", cuota)

"---------------------------------------------------------------------------------------------------------------------------"

f = float(input("Fahrenheit: "))
c = (f - 32) * 5 / 9
print("Celsius:", c)

"---------------------------------------------------------------------------------------------------------------------------"

segundos = int(input("Segundos: "))

minutos = segundos / 60
horas = minutos / 60

print("Minutos:", minutos)
print("Horas:", horas)
"""

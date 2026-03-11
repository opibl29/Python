"""
def sumar(valor1, valor2):
    return valor1 + valor2

# *args es una lista de datos: []
# **kwargs es un diccionario de datos: {}

def sumar(*args, **kwargs)-> int:
    re






def sumar(z,x, y)-> int:
    return z,x + y
def resta(z,x, y)-> int:
    return z,x - y
def multi(z,x, y)-> int:
    return z,x * y
def divi(z,x, y)-> int:
    return z,x / y

x = int(input("Ingresa un valor: "))   
y = int(input("Ingresa otro valor: "))
z = "El valor es: "

print(sumar(z ,x,y))
print(resta(z,x,y))
print(multi(z,x,y))
print(divi(z,x,y))
"""



nombre_fun = str(input("registra el nombre de la funcion"))

def nombre_fun(x, y)-> int:
    return x + y

x = int(input("Ingresa un valor: "))   
y = int(input("Ingresa otro valor: "))

print(nombre_fun(x,y))

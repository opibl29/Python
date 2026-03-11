class Tienda:
    """Esta clase representa una tienda con productos y ventas"""


    def __init__(self, nombre):
        """Esta funcion inicializa la tienda con un nombre, un diccionario para almacenar los productos y una variable para llevar el total de ventas"""
        self.nombre = nombre
        self.productos = {}
        self.ventas = 0


    def agregar_producto(self, nombre, precio, cantidad):
        """Esta función agrega un producto al diccionario de productos con su precio y cantidad"""
        self.productos[nombre] = {
            "precio": precio,
            "cantidad": cantidad
        }
        

    def mostrar_productos(self):
        """Esta función muestra los productos disponibles en la tienda con su precio y cantidad"""
        for producto, datos in self.productos.items():
            print(producto, "- Precio:", datos["precio"], "- Cantidad:", datos["cantidad"])



    def comprar_producto(self, nombre, cantidad):
        """Esta función permite comprar un producto, verificando si existe y si hay suficiente cantidad. Si la compra es exitosa, se actualiza el total de ventas"""
        if nombre in self.productos:
            if self.productos[nombre]["cantidad"] >= cantidad:
                total = self.productos[nombre]["precio"] * cantidad
                self.productos[nombre]["cantidad"] -= cantidad
                self.ventas += total
                print("Compra realizada. Total:", total)
            else:
                print("No hay suficiente cantidad")
        else:
            print("Producto no existe")

    

    def total_ventas(self):
        """Esta función muestra el total de ventas realizadas"""
        print("Ventas totales:", self.ventas)

  


tienda = Tienda("Mi Tienda")

tienda.agregar_producto("Laptop", 50000, 5)
tienda.agregar_producto("Mouse", 500, 20)
tienda.agregar_producto("Teclado", 1500, 10)

tienda.mostrar_productos()

tienda.comprar_producto("Mouse", 2)
tienda.comprar_producto("Laptop", 1)

tienda.total_ventas()

tienda.mostrar_productos()
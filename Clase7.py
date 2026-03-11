class Animal:
    def __init__(self, nombre, especie,cantidad_patas,color):
        self.nombre = nombre
        self.especie = especie
        self.cantidad_patas = cantidad_patas
        self.color = color

    def hacer_sonido(self):
       print(f"{self.nombre} haciendo un sonido.")
    
    def correr(self):
        print(f"{self.nombre} esta corriendo.")
    
perro = Animal("Rex", "Perro", 4,"Negro")
perro.hacer_sonido()
perro.correr()
    

class perro(Animal):
    super().__init__(nombre, especie,cantidad_patas,color)
    def hacer_sonido(self):
        print(f"{self.nombre} ¡Guau!")


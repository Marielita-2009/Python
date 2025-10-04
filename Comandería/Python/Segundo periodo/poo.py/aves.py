class aves:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiene_pico = True
        self.tiene_alas = True

    def describir(self):
        print(f"{self.nombre} tiene pico: {self.tiene_pico}, tiene alas: {self.tiene_alas}")

ave1 = aves("pajarito")
ave1.describir()

print("--Ganso--")

class ganso(aves):
    def __init__(self, nombre, puede_volar, tamaño_alas):
        super().__init__(nombre)
        self.puede_volar = puede_volar
        self.tamaño_alas = tamaño_alas

    def detalles(self):
        self.describir()
        print(f"Puede volar: {self.puede_volar}, largo alas en cm: {self.tamaño_alas}")

ganso1 = ganso("Ganso de canada", True, 170)
ganso1.detalles()

print("--Pato--")

class pato(aves):
    def __init__(self, nombre, puede_volar, tamaño_alas):
        super().__init__(nombre)
        self.puede_volar = puede_volar
        self.tamaño_alas = tamaño_alas

    def detalles(self):
        self.describir()
        print(f"Puede volar: {self.puede_volar}, largo alas en cm: {self.tamaño_alas}")

pato1 = pato("Patito", True, 30)
pato1.detalles()

print("--Gallina--")

class gallina(aves):
    def __init__(self, nombre, puede_volar, tamaño_alas):
        super().__init__(nombre)
        self.puede_volar = puede_volar
        self.tamaño_alas = tamaño_alas

    def detalles(self):
        self.describir()
        print(f"Puede volar: {self.puede_volar}, largo alas en cm: {self.tamaño_alas}")

gallina1 = gallina("Gallinita", True, 45)
gallina1.detalles()

class Humano:
    def __init__(self, edad, nombre, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    def presentar(self):
        presentacion = "hola, soy {}, mi edad es {}, mi trabajo es {}"
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))
    def contratar(self, puesto):
        self.puesto = puesto
        print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto

persona1 = Humano(35, "Josué", "constructor")
persona1.presentar()
persona1.contratar("Constructor")
persona1.presentar()
persona2 = Humano (34, "Karla", "veterianaria")
persona2.presentar()

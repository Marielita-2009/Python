#herencia simple

class Estudiante(object):
    def __init__ (self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

class ciberseguridad(Estudiante):
    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estudio ciberseguridad")

manuel = ciberseguridad(17, "Eydan Manuel Fernández")
manuel.presentarse()
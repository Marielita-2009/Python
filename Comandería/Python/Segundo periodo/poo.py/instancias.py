# Instancias y clases 

class Perros(object):
    "Clase para los perros" # Descripcion
    Collar = True # Variable de clase estatica
    def __init__(self, salud, hambre): 
        self.salud = salud #Variable de instancia
        self.hambre = hambre # Variable de instancia

# print (perros.hambre) no se puede acceder de esta manera porque hambre es una variable 
# Debes instanciar
Dogo = Perros(100, 50) 
print(Dogo.hambre)
print(Perros.Collar)

class animal(object):
    @classmethod
    def correr(self, km):
        print(f"El animal corrio {km} kilometros")

animal.correr(12)

class ave(object):
    def __init__ (self):
        pass

    def hablar (self, color):
        print("Soy una jodida ave de color %s" %color)

loro = ave()
loro.hablar("verde")
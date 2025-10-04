#herencia colectiva

class Estudiante(object):
    def __init__ (self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

class colegio(object):
    def presentarcole(self):
        print("Estudio en el CTP de Puriscal")

class ciberseguridad(Estudiante, colegio):
    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estudio ciberseguridad")

manuel = ciberseguridad(17, "Eydan Manuel Fernández")
manuel.presentarse()
manuel.presentarcole()

# -------------------------------------------------------------------------------------------

class abuelo(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas
class Hijo(abuelo): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        super().__init__( ojos, cejas) #Sobreescribimos cada atributo
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga') #Instanciamos
print (Tomas.ojos, Tomas.cejas, Tomas.cara) #Imprimimos los atributos del objeto

# -------------------------------------------------------------------------------------------

class agregar(list):
    def append(self, alumno):
        print(("alumno agregado"),(alumno))
        super().append(alumno)

lista1 = agregar()
lista1.append("Matias")
print(lista1)

# -------------------------------------------------------------------------------------------


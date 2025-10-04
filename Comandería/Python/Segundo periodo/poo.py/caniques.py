class Perros(object): #Declaramos la clase principal Perros
    def ladrar (self):
        print ("""GUAAAUU GUAAAUU!""")
        
    def grunir (self):
        print ("""GRRRRRR GRRRRR""")
class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrarp(self):
        print ("""guau guau guau""")
        
    def grunir(self):
        print ("""gññññiii gñññiiii""")
class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""GuaUUU GUAAAUUU GuaUUU""")
        
    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")

class shepadoodle(Caniche, Pastor_Aleman):
    def ladrarx(self, veces):
        for cantidad in range(veces):
            super(shepadoodle, self).ladrar()

tomy = Pastor_Aleman()
pinki = Caniche()
cuco = shepadoodle()
cuco.ladrarx(5)

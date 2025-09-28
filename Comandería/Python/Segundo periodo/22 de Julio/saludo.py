def saludar():
    print(f"Hola desde mi primer funcion")
saludar()

def saludar(nombre):
    print(f"Hola", nombre)
    
saludar("Diana")

def bienvenida(nombre, idioma): 
    if idioma == "Español":
        print(f"Bienvenida", nombre)
    else: 
        print("Welcome,", nombre)

bienvenida("Diana", idioma = "Español")

def bienvenida(nombre, idioma):
    idioma = input("¿El idioma establecido es español?")
    if idioma == "si":
        print(f"Bienvenido", nombre)
    else: 
        print(f"Welcome", nombre)
bienvenida("Diana", idioma = "Español")

def bienvenida(nombre, idioma = "Español"):
    if idioma == "Español":
        print(f"Hola", nombre)
    elif idioma == "Inglés":
        print(f"Hi", nombre)
    else: 
        print("Idioma no correspondido")

bienvenida("Diana")

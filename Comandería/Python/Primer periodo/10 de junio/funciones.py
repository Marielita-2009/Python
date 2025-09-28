def saludar():
    print("Hola")
saludar()

def despedir():
    print("Adiós")
despedir()

def nombres():
    nombre = input("Ingrese su nombre:")
    print("Hola",nombre)
nombres()

def saludar_nombre(nombre):
    print(f"Hola, {nombre}")

nombre = input("Introduce tu nombre:")
b = "Roberto"
saludar_nombre(nombre)
saludar_nombre(b)

def suma(num1, num2):
    print("La suma de los numeros e: {sumo}")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el segundo numero: "))
sumo = num1 + num2 
suma()
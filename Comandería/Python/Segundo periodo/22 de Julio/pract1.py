def suma(a , b):
    resultado = a + b
    return resultado

def restar(a , b):
    resultado = a - b
    return resultado

def dividir(a , b):
    resultado = a / b
    return resultado

def multiplicar(a , b):
    resultado = a * b
    return resultado

print("""
      Escoja que desea hacer
      1- sumar
      2- restar 
      3- multiplicar
      4- dividir
      5- salir
      """)

resp = int(input("Ingrese su opcion: "))

if resp == 1: 
    num1 = int(input("Ingrese el primer valor a sumar: "))
    num2 = int(input("Ingrese el segundo valor a sumar: "))
    resultado = suma(num1, num2)
    print(resultado)

if resp == 2: 
    num1 = int(input("Ingrese el primer valor a restar: "))
    num2 = int(input("Ingrese el segundo valor a restar: "))
    resultado = restar(num1, num2)
    print(resultado)

if resp == 3: 
    num1 = int(input("Ingrese el primer valor a multiplicar: "))
    num2 = int(input("Ingrese el segundo valor a multiplicar: "))
    resultado = multiplicar(num1, num2)
    print(resultado)

if resp == 1: 
    num1 = int(input("Ingrese el primer valor a dividir: "))
    num2 = int(input("Ingrese el segundo valor a dividir: "))
    resultado = dividir(num1, num2)
    print(resultado)
else:
    print("Gracias")
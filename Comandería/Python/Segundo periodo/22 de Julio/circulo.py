#para importar una biblioteca import math

import math

def area_circulo(radio):
    return math.pi * (radio ** 2)
print(area_circulo (5))

def area_circulo(radio):
    radio = int(input("Ingrese el area del circulo: "))
    radio = math.pi * (radio ** 2)

def area_circulo(radio):
    return math.pi * (radio ** 2)
area1 = area_circulo(5)
radio1 = float(input("Ingrese el radio"))
area2 = area_circulo(radio1)

print(f"El area con radio 5 es de {area1}")

print(f"El area con radio ingresado es de {area2}")
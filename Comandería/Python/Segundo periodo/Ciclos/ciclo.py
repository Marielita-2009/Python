# for variable in elemento_iterable: (para elementos como listas, tuplas, bibliotecas)
#   cuerpo de la repeticion

numeros = [1,2,3,4,5,6,7,8]
for numero in numeros: 
    print(numero)
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

oracion = "Hola, estoy programando, no me hables"
contador = 0
letra_buscar = "p"

for letra in oracion:
    if letra == letra_buscar: 
        contador += 1

print(f"La letra {letra_buscar} aparece {contador}")

# Ejercicio 1

frutas = ["fresa", "guayaba", "sandia", "manzana"]
for fruta in frutas:
    print(fruta)

# Ejercicio 2

suma = 0

numbers = [1,2,3,4,5]
for number in numbers:
    suma += number

print(f"La suma de los numeros es", suma)

# Ejercicio 3

parrafo = "Van las hormigas diligentes, cual largas hebras andadoras, en el trabajo resistentes, en la obediencia profesoras"
contador1 = 0
contador2 = 0 
contador3 = 0
contador4 = 0
contador5 = 0

letra_buscar1 = "a"

for letra in parrafo: 
    if letra == letra_buscar1: 
        contador1 += 1

print(f"La letra {letra_buscar1} aparece {contador1}, veces en el parrafo")

letra_buscar2 = "e"

for letra in parrafo: 
    if letra == letra_buscar2:
        contador2 += 1

print(f"La letra {letra_buscar2} aparece {contador2}, veces en el parrafo")

letra_buscar3 = "i"

for letra in parrafo:
    if letra == letra_buscar3:
        contador3 += 1

print(f"La letra {letra_buscar3} aparece {contador3}, veces en el parrafo")

letra_buscar4 = "o"

for letra in parrafo:
    if letra == letra_buscar4:
        contador4 += 1

print(f"La letra {letra_buscar4} aparece {contador4}, veces en el parrafo")

letra_buscar5 = "u"

for letra in parrafo: 
    if letra == letra_buscar5:
        contador5 +=1

print(f"La letra {letra_buscar5} aparece {contador5}, veces en el parrafo")

# Ejercicio resuelto

parrafo = """Un párrafo es una unidad de 
sentido y estructura en un texto escrito, 
delimitada por mayúscula al inicio y punto y 
aparte al final, que desarrolla una idea central a 
través de oraciones temáticas y de apoyo. 
Cada párrafo aborda un tema o aspecto específico 
del escrito, manteniendo cohesión y coherencia 
con las demás partes del texto, lo que facilita la 
comprensión del mensaje completo."""

contador = 0
vocales = ["a","e","i","o","u"]

for vocal in vocales:
    for letra in parrafo:
        if letra.lower() == vocal:
            contador +=1
    print(f"La letra {vocal} aparece {contador} veces")

# lower y upper se usan para reconocer si es mayuscula o minuscul